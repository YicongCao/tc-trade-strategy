# 每日交易总结 · 2026-11-09

## 一分钟读懂 · Agent 摘要

### 当前判断

从脆弱的盘前修复，上调为初步可靠的收盘反弹，尚不是趋势反转。今晚21:30北京CPI、22:30开盘后的回踩比继续追高更关键。

### 与上次相比

相对昨晚，半导体从盘前偏弱转为领涨，19个ETF全部收涨、等权跟随；NVDA仍单独下跌。CNN恐贪从盘前25升至32，离过热仍远。

### 最重要的信号

- SPY+2.37%、QQQ+3.54%、SMH+5.05%，突破上期观察高点；RSP+2.27%、IWM+3.23%，参与面扩大。
- VIX19.92、三个月VIX20.85，期限比约0.955；但QQQ679.35略低于200日线680.09，SPY仍低于20日线762.09。
- NVDA-4.27%，AMZN/GOOGL虽上涨却靠近日内低位收盘；单个大阳线不能代表所有AI公司的盈利风险解除。

### 接下来观察

- CPI后先看SPY742.21–741.09、QQQ664.52–662.02、SMH476.25回踩；守住并突破周一高点、收盘保留进展才进一步升级。
- 先观察现金流较强的云端、金融医疗与等权；半导体看反弹持续性，NVDA需单独收复185.22验证。
- CoreWeave明晨06:00电话会、Nebius周四、NVDA17日：看交付、融资、现金回收，不只看EPS。

### 不要忽略

缺完整成分广度、当期净申赎、可靠VWAP和四家公司完整估值；期货已进入新交易时段，不把最新报价当周一结算。预测价格不是客观概率。

## 研究结论

11月10日早报：普涨与波动回落确认反弹升级，但QQQ尚未站稳200日线；今晚CPI检验承接，NVDA治理风险单列。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-09 → 2026-11-09（纽约交易日） |
| 截止·纽约 | 2026-11-09T18:23:53.019915-05:00 |
| 截止·北京 | 2026-11-10T07:23:53.019915+08:00 |
| 实际生成时间 | 2026-11-09T23:23:53.426533+00:00 |
| 市场阶段 | 盘后 |
| 下一交易日 | 2026-11-10 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-06/20261109T120751.728794Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-10T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219847 | 已校验接入 | https://gamma-api.polymarket.com/events/1219847 | 2026-11-09T23:19:00.941593+00:00 / 2026-11-09T23:19:00.941593+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-11-09T23:19:00.953139+00:00 / 2026-11-09T23:19:00.953139+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-11-09T23:19:03.794892+00:00 / 2026-11-09T23:19:03.794892+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-11-09T23:19:03.311716+00:00 / 2026-11-09T23:19:03.311716+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1103684 | 已校验接入 | https://gamma-api.polymarket.com/events/1103684 | 2026-11-09T23:19:04.395652+00:00 / 2026-11-09T23:19:04.395652+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1189688 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 1308738 | 已校验接入 | https://gamma-api.polymarket.com/events/1308738 | 2026-11-09T23:20:36.234807+00:00 / 2026-11-09T23:20:36.234807+00:00 | Gamma observation, not last trade; each contract and rule retained |
| 1343940 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |

## 仍需核验的数据与影响

| 数据 | 状态 | 需要核验 | 影响 |
| --- | --- | --- | --- |
| history.DRAM | insufficient_history | 连续完整交易日 OHLC；SMA200 至少200条，ATR14至少15条 | 降低相关判断可信度；保留缺口 |
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
| prices.SPY.value | 752.69 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 2.37 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | 0.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -3.27 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -2.81 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 762.09 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 764.86 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 727.99 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -1.23 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -1.59 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 3.39 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 11.98 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.59 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -3.39 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 679.35 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 3.54 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -0.26 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -8.94 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -6.98 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 1.18 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -0.33 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -5.67 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -4.17 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 704.30 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 720.02 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 680.09 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -3.54 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -5.65 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | -0.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 17.56 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.58 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -10.57 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.09 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 282.51 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 3.23 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 1.21 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 1.66 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -7.16 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.86 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.13 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 4.92 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.35 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.07 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 281.69 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 278.12 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 1.96 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | 0.29 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 1.58 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 5.05 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.79 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -7.16 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 220.95 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 2.27 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.44 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 3.64 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -0.44 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.10 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 0.36 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 6.91 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 2.36 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 217.11 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.56 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.21 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.77 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 2.98 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.96 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.34 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.07 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 379.53 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 1.88 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | 4.94 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -0.69 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -5.47 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.48 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 4.87 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | 2.58 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -2.66 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 372.66 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 384.37 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 410.85 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | 1.84 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -1.26 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -7.62 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 6.97 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.84 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -11.34 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.83 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,147.70 | USD_per_troy_ounce | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 1.79 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | 4.49 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -1.02 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -6.53 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.58 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 4.41 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | 2.24 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -3.72 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,078.57 | USD_per_troy_ounce | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,222.78 | USD_per_troy_ounce | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,497.34 | USD_per_troy_ounce | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | 1.69 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -1.78 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -7.77 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 87.07 | USD_per_troy_ounce | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.10 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -11.71 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 86.25 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -5.04 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -10.58 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -7.99 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 4.67 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -7.41 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -10.66 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | -4.72 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 7.48 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 97.64 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.52 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.28 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -11.66 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -9.71 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | -1.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.78 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.54 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -18.50 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 92.15 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -6.28 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -12.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -13.60 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 4.10 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -8.64 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -12.12 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -10.33 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 6.91 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 107.69 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.26 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.47 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -14.43 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -11.62 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | -1.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.58 | USD_per_barrel | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 6.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -21.67 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.96 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.28 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 5.01 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | 0.69 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -2.32 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 0.20 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 8.28 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 3.49 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.91 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.21 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.14 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 1.30 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 2.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.74 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.90 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.04 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.75 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.97 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.03 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | -0.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.06 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -2.92 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | -0.04 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 2.72 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 5.86 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.99 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.70 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.98 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | -0.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 0.93 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.11 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.39 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.51 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.36 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.81 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.28 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.79 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -2.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.73 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 3.55 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 1.01 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.17 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.60 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.88 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.43 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.48 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.33 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.73 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.67 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.13 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.93 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.04 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.52 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -2.23 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.85 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 5.30 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 2.28 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.81 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.62 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.77 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.83 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 1.02 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.04 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.57 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.54 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.21 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.60 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 19.92 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -22.31 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -5.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 30.97 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 31.14 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -24.68 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -5.89 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 34.23 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 33.48 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 19.06 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 17.02 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.41 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 4.49 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 17.03 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 8.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 3.66 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 18.35 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -29.31 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-09 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.85 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -15.24 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -3.47 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 16.29 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 12.95 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -17.61 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | -3.55 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 19.55 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 15.75 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 20.26 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 19.06 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.59 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 2.91 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 9.37 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 1.26 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 2.06 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 9.90 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -18.40 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-09 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 98.43 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -19.28 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -10.90 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 14.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 12.52 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -21.65 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -10.98 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 17.81 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 15.32 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 103.21 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 94.57 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 99.02 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | -4.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 4.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -0.60 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 14.74 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 14.97 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -27.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-09 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 85.98 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -7.32 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -14.32 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -12.68 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 24.20 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -9.68 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -14.40 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -9.36 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 27.20 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 98.60 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 93.13 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 78.62 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -12.80 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | -7.68 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 9.37 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.47 | index | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 6.36 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -24.31 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-09 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 178.67 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -4.27 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -11.58 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -21.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -20.56 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -6.64 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -11.65 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -17.79 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -17.75 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 209.16 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 219.00 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.35 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -14.58 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -18.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -12.57 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 8.79 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 4.92 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -25.32 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 3.88 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 545.18 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 2.75 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | 7.51 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 0.74 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 10.26 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.38 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 7.43 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 4.01 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 13.06 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 531.61 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 517.28 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 439.26 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 2.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 5.39 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 24.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 16.54 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 3.03 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -1.91 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.99 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 266.93 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 2.94 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 8.67 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 2.85 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 1.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 0.58 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 8.59 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 6.12 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 4.44 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.65 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 253.96 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 244.08 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 4.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 5.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 9.36 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 10.55 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.95 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -0.13 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 288.15 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 1.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | 3.28 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -18.31 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -16.64 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -1.18 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 3.20 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -15.04 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -13.84 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 314.21 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 331.74 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 339.02 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -8.29 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -13.14 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -15.01 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 11.66 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 4.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -18.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 0.93 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 641.37 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 5.12 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | 5.71 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -13.67 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 8.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 2.75 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 5.63 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -10.41 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 11.63 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 657.59 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 676.05 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.07 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -2.47 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -5.13 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | 1.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 24.74 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.86 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -17.52 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.76 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 48.98 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 5.56 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -2.33 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -38.97 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -53.47 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 3.19 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -2.41 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -35.71 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -50.66 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 57.76 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 74.86 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 89.95 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -15.20 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -34.57 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -45.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.51 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.25 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -54.53 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.71 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 733.15 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 6.25 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -12.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -25.86 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -24.53 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 3.89 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -12.13 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -22.60 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -21.73 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 866.20 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 957.54 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 758.20 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -15.36 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -23.43 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | -3.30 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 60.10 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 8.20 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -33.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 41.78 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 6.34 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -9.80 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -23.65 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -27.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 3.97 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -9.88 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -20.38 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -24.31 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 47.33 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 54.36 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-09 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -11.73 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -23.15 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-09 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.32 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 7.95 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -34.33 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.06 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 200.47 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 9.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -10.60 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -16.25 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -31.76 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 7.26 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -10.68 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -12.98 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -28.95 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 212.43 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 235.85 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.22 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -5.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -15.00 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -26.09 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 19.48 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 9.72 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -31.76 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.87 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 170.88 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 3.73 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -1.92 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -12.98 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -9.96 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.36 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -2.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -9.71 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -7.16 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 182.26 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 188.09 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 170.04 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -6.24 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -9.15 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 0.49 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 5.72 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.35 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -15.41 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.25 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 61.94 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 0.52 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -7.90 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -6.17 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 0.64 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -1.85 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -7.97 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | -2.90 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 3.45 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.91 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.95 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.64 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -7.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -4.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 5.62 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.82 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.94 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -11.54 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.10 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 57.99 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 1.45 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.75 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 5.34 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 0.06 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.91 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 0.67 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 8.61 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 2.87 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 56.38 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.86 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.55 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.86 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 3.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 8.30 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 1.01 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.75 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -2.04 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 168.89 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 3.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -0.48 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -0.15 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -9.20 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 1.46 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | -0.56 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 3.11 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -6.40 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.50 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 169.17 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.68 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 0.83 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -0.17 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -2.19 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.48 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 2.06 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -9.20 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 188.33 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 1.91 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.02 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 9.50 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 12.95 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.46 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 1.94 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 12.77 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 15.76 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 180.80 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 173.54 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 158.60 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 4.17 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 8.52 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 18.75 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.77 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 2.00 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.70 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.88 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 90.89 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 0.90 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 0.07 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 7.68 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 6.27 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -1.47 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | -0.01 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 10.94 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 9.08 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 88.42 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 85.00 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.87 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.80 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 6.93 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.37 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.79 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.97 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -1.14 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.94 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 121.01 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 2.92 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 2.41 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 7.78 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 2.60 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.55 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 2.33 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 11.05 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 5.41 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 115.70 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.36 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.10 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 4.59 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 6.75 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 5.14 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.63 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -1.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 107.36 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 2.45 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 7.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -3.67 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -4.64 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.09 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 7.00 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -0.40 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -1.83 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 106.14 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.59 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.03 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | 1.15 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -2.04 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -4.17 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.29 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 2.13 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -6.44 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 0.97 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.79 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 1.53 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.27 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.19 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -0.45 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -0.84 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 0.20 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 8.45 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 2.36 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.67 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.71 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.84 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.61 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.99 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.12 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.64 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.46 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -0.45 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.64 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 1.45 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 2.29 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 6.49 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -0.56 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -0.91 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 2.21 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 9.75 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 2.24 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 42.88 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.46 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.88 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 4.10 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 5.14 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 4.10 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.76 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.70 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -1.06 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.22 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.94 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 1.91 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | -1.36 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 7.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 1.23 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -0.46 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | -1.44 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 10.34 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 4.03 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 51.75 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.86 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.86 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 2.30 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 4.10 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 4.09 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 1.01 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.91 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -1.78 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.97 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 487.41 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 5.05 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -4.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -17.53 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -17.08 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 2.69 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -4.19 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -14.26 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -14.28 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 531.76 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 564.32 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 522.19 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -8.34 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -13.63 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -6.66 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 25.35 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 5.20 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -23.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 101.46 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 2.61 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -0.43 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -8.82 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -2.52 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 0.24 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -0.51 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -5.56 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 0.29 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 106.42 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.54 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.07 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -4.66 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -4.77 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 7.86 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.06 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.02 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -9.95 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.91 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 174.15 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 0.22 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -10.03 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -10.37 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -3.13 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -2.15 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -10.11 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -7.10 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | -0.32 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 194.25 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.91 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 171.08 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -10.35 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -8.78 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 1.80 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 6.19 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -14.99 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.15 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 360.58 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 1.24 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -7.31 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -7.23 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -14.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -1.12 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -7.39 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -3.97 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -11.61 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 385.70 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 395.89 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.67 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -6.51 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -8.92 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -9.55 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 15.06 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 4.18 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -17.41 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.72 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 71.67 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 3.90 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 0.15 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 4.36 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -14.99 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 1.53 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 0.08 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 7.62 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -12.19 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 69.43 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.63 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 75.93 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 3.23 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | 1.47 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -5.61 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 2.11 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.94 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -14.99 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 0.70 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.03 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 5.67 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 1.56 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -5.45 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -13.86 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 3.30 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 1.48 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -2.18 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -11.05 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 29.95 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.32 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.33 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | 0.27 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -4.12 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -7.11 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 1.07 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.56 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -13.86 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 3.23 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 73.45 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 1.73 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | -0.38 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 5.59 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -5.21 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.64 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | -0.46 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 8.86 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -2.41 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 71.68 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.68 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.52 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 2.48 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 2.46 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 4.15 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.64 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.24 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -5.21 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.88 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 150.71 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 2.91 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -2.48 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -12.64 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -8.85 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 0.54 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -2.56 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -9.37 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -6.04 | pp | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 161.79 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 163.62 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.38 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -6.85 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -7.89 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 9.70 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.15 | USD_per_share | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.42 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -13.83 | percent | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 2.16 | ratio | 2026-11-09 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.51 | percent | 2026-11-06 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.42 | percentage_points | 2026-11-06 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.93 | percentage_points | 2026-11-06 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.86 | percent | 2026-11-06 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.63 | percent | 2026-11-06 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.22 | percent | 2026-11-09 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.52 | index | 2026-10-30 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 25.64 | index | 2026-11-06 | lagged | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 113.95 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 129.82 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 108.29 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 158.85 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 184.74 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 753.60 | USD_per_share | 2026-11-09T23:15:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 680.17 | USD_per_share | 2026-11-09T23:18:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 488.80 | USD_per_share | 2026-11-09T23:12:21+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.NVDA.value | 179.30 | USD_per_share | 2026-11-09T23:18:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.MSFT.value | 545.21 | USD_per_share | 2026-11-09T23:16:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 268.33 | USD_per_share | 2026-11-09T23:18:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.GOOGL.value | 290.30 | USD_per_share | 2026-11-09T23:18:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.META.value | 644.43 | USD_per_share | 2026-11-09T23:18:49+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.SPY.price | 753.60 | USD | 2026-11-09T23:15:29+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| observed.QQQ.price | 680.17 | USD | 2026-11-09T23:18:48+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| observed.SMH.price | 488.80 | USD | 2026-11-09T23:12:21+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| observed.NVDA.price | 179.30 | USD | 2026-11-09T23:18:58+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| observed.MSFT.price | 545.21 | USD | 2026-11-09T23:16:51+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| observed.AMZN.price | 268.33 | USD | 2026-11-09T23:18:53+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| observed.GOOGL.price | 290.30 | USD | 2026-11-09T23:18:50+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| observed.META.price | 644.43 | USD | 2026-11-09T23:18:49+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| observed.CL_F.price | 86.24 | USD | 2026-11-09T23:09:00+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| observed.BZ_F.price | 92.20 | USD | 2026-11-09T23:09:00+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| observed.GC_F.price | 4,146.90 | USD | 2026-11-09T23:09:04+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| observed.TNX.price | 4.86 | percent | 2026-11-09T19:59:00+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| observed.DX-Y.NYB.price | 101.68 | index points | 2026-11-09T23:04:59+00:00 | ok | 最后非空分钟close，非VWAP；股票为盘后，期货已属新时段，TNX直接为百分数且仅至19:59UTC。 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 17.4000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.59002685546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.0540049066247734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.845429406619815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.7818319289823923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.812255103230831,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.293269252904928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.33209173482430243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.4348271587836368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.31064742379908195,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2704986572265398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.238500976562477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2950854492188455,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.68536376953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3440109252929915,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.6794747924803914,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.4437699024440263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0059664261416246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.312019113408459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.29334200764481455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.342395284462384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.15784317094211797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8635733468191962,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.00750732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.07978662575977347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.39863283083278334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2333778914218394,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.07573282100018508,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.26202833435844375,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.23816185131887369,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 23.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.74005126953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.145013679746932,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.905014054695234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.725042908633192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.112672518484628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7286883448673027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9933558659216288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3063029501207657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.2753053514322437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.09100877312215871,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.0595846480754187,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9432109796508001,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.300417415253797,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.435419091962375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.3254476007459317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8714757913371285,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.9646579276331622,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.3345001220703807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -20.127499389648506,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7266857910155977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.050162353515589,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.2937179565429915,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.405675659179792,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7400926053703265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.4397461359209056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.320943106325191,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.28744824250294077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3769917212274736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4632801763390315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9453604561941944,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.3346470424107135,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.05249216577138904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.34938455968451976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.060579841235956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.22905659519330968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.4028712638888732,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.2778287260255208,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 8.839996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.3699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.23747217521284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.2981760803956206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.2335453351096777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.43106754040509454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.548167077763753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.15509652338104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.4339043120063852,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.03366170696218518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.18346726858806672,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4527466737758057,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4517134061272854,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3811875628257364,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2548978248588245,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.487188258205342,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.000922846777251074,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.34430913076126757,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.230500793457054,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.12399902343747726,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.24939147949220342,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.9366833496093818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0974218750000091,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.34603279113770213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.108255548713079,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.2613510803837436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.2241152511249815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.8729787755066507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.1439989458899364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0866739428184058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3214285714285712,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9499991280691962,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.059702214130741504,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.31874696783007117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.9050720042538725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1074753987680666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1033804248977721,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.1210089301845565,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.970001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.6460937126382755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.5030242447125142,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4761723745971844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.79702831837829,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2270581313512894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.556722819618205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.1903582707735625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7698910149777194,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5920888060135021,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3424051619073007,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3056595543852079,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.609283421609121,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.06621112155363917,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.22463108479390304,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.24446888801007427,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.45924359117863744,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3879997253417855,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7714996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.021729125976548858,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.14681671142579944,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.12264541625975767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5761775207519406,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.078773803451439,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.38676269523145734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2735320546727555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5221934041646392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.3029607229890336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.1721024318843023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.2128557477678572,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7149974278041298,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.06814528681925247,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.3191225441396315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.194059847002172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.1844664190577494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.17539218535258727,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4923690651205652,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.010009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 17.8800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.672747652708596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.23188620017853268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.23885592755643614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.621462614146523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.450294581398127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.0305163328728355,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.1599575661251693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.773072138950729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6187427460838224,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.6135432064412822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.5429760014259566,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.809207510915692,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.15702532849319883,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.362608067697138,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2748695926584674,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.0837195627498115,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.13099975585936363,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.2104995727539176,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.5872003173828375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.965601196289072,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.392350006103527,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.763100280761705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.916206141775112,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.3702051434797005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9715889429715694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.851747557468922,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.7927325481868817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.728102262196497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.2885720389229913,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8042798723493307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.04289568316596393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.13156812307913923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.6375848916496576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.176888026932058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.007333547559961073,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.19589035919189968,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 72.80029296875,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 192.000244140625,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.724930163323558,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.32973169800523117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.027493336169337468,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.534440065063407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.3299317453251644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.81413534693914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2895521017826432,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.565119436514429,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6709252566987844,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.5156977086145837,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.80932526515173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.722184961832577,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.03666249242023634,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.146227081763442,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.1452750570009935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.875766860313511,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.144995117187591,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -26.415002441406614,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.643994140625182,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -57.52198730468717,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.1599999999998545,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.641998291015625,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8374634129444956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.331638748796186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8983539471764233,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.805656975298767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.7024760574766757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.632285305793071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.0928780691964306,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 11.65712193080357,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.01385564385732918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.19279821985743006,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.549667844426006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.087024822748841,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3197517075821679,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.004658852985423827,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.5800018310546875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.099998474121094,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.3848602882887615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.4201583350621174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.1794213957219046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.268263167109055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.879680899142382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -15.728077009893981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.118443325604341,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.568907576735462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.438865194913535,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.42527107155769706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.602410533260489,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.080518270339887,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -9.17295015204731,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -15.395985275069679,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -9.553270484387978,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.25826015293638,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.3744998931884709,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.1439998626708956,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.056999969482433244,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7077998352050798,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.12590000152587777,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7554500007629343,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.335305934127386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.198905032560688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.851401548802159,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -11.32625971317961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.3976104237478895,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.535291807692795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.34214292253766754,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.20571463448660676,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.0971090107404704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.794717587646744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.32769701579153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.543606065739805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.1866152929260287,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.001687215754685156,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.1699981689453125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.169998168945312,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.30594601639406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.047253826389531,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.377556626558221,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.124007193336851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.484337251684382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -17.583115002322458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -8.81986475240768,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -20.758586863872843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -8.359950923018832,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.201824419769716,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.5957246975758288,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.9362622965676817,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -9.77760650458931,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -17.251023267498155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -11.254691911191317,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -20.44793944007376,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7250000000000085,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.4500000000000028,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.05680007934570597,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7966001892089878,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13135002136230867,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8160000610351688,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.118739691174534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.013717991098481,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.969241514914502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.442990115156537,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.748747928740794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.002439814602774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.017142704554967025,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.08928462437221,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.397190989246619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7501420574788398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.244813159603126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.345119204426135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.4066720870871632,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0010304577611627125,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.04000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2299957275390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.06103739233371819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.18322927529984545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.18365522183461103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2201909426227333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.0429667675411638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.9818403673602205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7193412284921319,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1560816125410156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.9929675142910552,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.6622001313199695,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.5981767071477813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.5920641606080976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.3362360204460924,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6497486325359194,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.7154859302915049,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.4667290363400975,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.19549980163574787,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0174995422363367,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.005448608398424426,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.06829635620115937,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.015031661987308098,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.06978897094727188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.19578805990074777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0021893817783845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.05680688229925401,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.3734241047148368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.06592577471844496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.3590940343955018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.03215735299246647,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.12108666556222092,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.03969459265830211,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.15069032171513497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.048299886375968715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2777128313351085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2575683351696091,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.18271275913517127,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.15999984741210938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.010000228881835938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2753993324883806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.41132722981611636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.4137417899908957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2068894822535139,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.928305877760438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.44577509192659237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.31177635779033874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.11123789422025077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.329404239113154,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.2567566364359313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.195573718973288,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.605365620977317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.221575130665366,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.11368335710228994,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.746603516573975,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.19940952957883074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.00799999237060689,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.007000064849854937,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.015799980163571092,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0961999511718723,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.010299997329710209,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.04479999542236257,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.5241412432205661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.05860255332956754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6133379252306614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.30446313143779324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6102265906558824,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.13027080836096605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0014286041259765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.007030424528486956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.00013366999016350967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.5492614212897151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.034329657294684957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.029195615181286882,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.09711604946925889,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.279998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6200027465820312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4272456860598073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.059957102100384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.064644182640473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.2079015651622393,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.28464383244550806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4015624650257621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.45288458605390325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.663200526229335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.6267592205649661,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.785472304519431,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.7171877463419194,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6043535380685916,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.00862542045942,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7336541998500645,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.9819425727297335,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.973847950028417,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.011000061035161934,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.02050018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.028881988525398583,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.17352539062500227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.0005435562133868643,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.006481742858895245,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.34854678450555454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7769052088990036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3978616779912292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0200779899515178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3602074655832621,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8042925701240544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0014283316476004226,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.005713326590401802,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.000309227894935149,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0040049129123727045,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3538361624800257,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7835012464288527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1212290163080747,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.1965712841149836,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9599990844726562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.2581486541991196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6709971650812774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6763025114842502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.2236744846160885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.03267490752765223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.19121904304859605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5339603825075367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.3101171560801705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.7958562524256538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.1744322415385375,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.105529417498142,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5885806186147424,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.32594416043258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5233107778728989,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.9008667762761,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.6207645798792525,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.10449981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5189998626708956,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.015608215332036934,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.1262466430664091,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.011653671264653553,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.05708972930908374,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.03339701451381405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4227865533316555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1503043807818516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0482758975924766,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.14324695435239398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9605066469509871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.023929050990513345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.08821487426757812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.023621851926227455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.09010317730335915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13212962643606163,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9060418579570184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.21021066592877358,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5604012289716405,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.719999313354492,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.2299995422363281,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -13.295402316530915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -31.217229732102194,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -37.84443336709792,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -20.82375912696618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -41.80980483290297,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.309297117342581,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -48.790908977545286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.6657430741064765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -15.349407223155687,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -34.06265913872201,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -40.626265296080305,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -22.63601423019701,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -44.103074085807904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.977205382518278,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -51.49941924514776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.7877404027057295,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.2355000019073472,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7815000057220445,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.09999999999999787,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7331999969482403,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.01784999847411939,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.15025000095367602,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -31.68727431531302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -17.88878697001326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -34.49370238402152,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.818789743932825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -31.198850993816585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.6247161406037804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.29428577423095703,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9378571510314941,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.241883236811352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.501590666827543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -20.298081090878874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -29.3115689830732,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.75,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.75,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -11.525706962097049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.19000262481628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -21.85528072008138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -11.79719609747003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -22.1500090562877,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.7144470350912258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -19.24007404228112,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.4377017438854907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -13.579711868721821,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -22.035432031436095,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -24.637112649063777,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -13.60945120070086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -24.44327830919263,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.382355300266923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -21.674901201064753,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.1270543200864083,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1460000038146987,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0965000152587905,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.06740001678466712,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.42540004730224723,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.008500003814695845,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.06769999504089341,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -19.39073146702073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.802132547173258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -20.129494233157242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.520570354479506,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -18.262467234026023,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.9887065352237183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.19428566523960655,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5592857088361469,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.299546851259934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.9331771825715123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -14.677104156467392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.39529939700907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -23.51000213623047,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.040000915527344,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -9.612590487017503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -23.075898175161935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -25.47184800147845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.811438687125502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -29.114923461190063,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.71843207521253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -23.85056568984227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.657158738320335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -11.666595393642275,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -25.92132758178175,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -28.25367993046084,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -21.623693790356334,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -31.40819271409499,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.386340340388227,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -26.285392848625904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.346511314521253,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.446500778198242,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.23600006103515625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.4818003845214776,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.01700000762939169,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.16775001525878963,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -23.49920360264582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.796923946311484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -25.18252770655929,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -15.879490007374832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -23.72096741999892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.348177207268863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8142858232770642,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.660714830671038,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.5548329738963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.0405816456157915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -17.416105770453527,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -27.083490406880305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.78619384765625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.377700805664062,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.0556768575327062,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.476258228181398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.90945887179778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.535316217549619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.80532900270566,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.222476589272151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.486165907543981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.646226428247527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.10968176415748,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.321687634801213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -9.691290800780171,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.34757132078045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.473987148553972,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.177425807639491,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.067385977175885,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.546882914849217,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6243099212646541,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.500384902954096,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.32247604370117244,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.2384457397460977,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.14741901397704282,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.868011474609375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -6.290377265686298,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.064181760570536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.632554859108609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.09135561507549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -8.853278660444452,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.712623591607013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4086788722446988,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4424716404506137,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9054732409196404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.3514289030275544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.973762270078019,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.65642693555089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.970001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -23.389999389648438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -7.045580167411147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.009502076352011,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.7798350612698854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.122064577210317,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.456914766226923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.633585850489297,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.4920988559871446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.881167311222738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -9.099585074035922,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.854931482971826,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.561666990252277,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.934319680441147,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -4.7501840191318525,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.301494115664996,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.926926014770782,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.570519887423655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.382500457763655,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -10.45299987792967,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7727368164062511,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.435730285644553,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.04280944824219546,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.17874031066895668,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.805452272575881,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.584613150276041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.3396103737331035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.66545870546156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.8810774428802315,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -11.532716987353464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7649993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.0495071411132804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6198431630554628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.5834736315998632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.3313831456716194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.776792698793336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2899489404415903,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.718423886483905,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 14.57000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 38.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7385660217597594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.579715547873132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.838170085245165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 12.289201242021587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.5782443346717523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.183524999279231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.2662282146074473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.638645472925122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.684561115134986,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.734286141253317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.056338156262772,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 10.476946138790755,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7150249182331754,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.515616734103534,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.831401055823811,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.949292896724204,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.20149841308591476,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.5309967041015398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6329992675780431,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.8905987548828307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.41083633422846333,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.1363775634765148,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.7028909070525464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.883876928090049,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.690985790598188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.614788971135788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.203879156587419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.100384161889274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6642892020089306,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.756432669503349,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.041886741022472584,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5130432136659246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.6214479388664507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.774312188681174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.08228759712332656,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5547457464090866,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.6300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 21.29998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.292258577521856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.745743847833169,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7872465366439263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 10.060626816836871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.044006694939972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.146448657066549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.82847228423282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 12.140330425936519,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2382536708970826,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.099685558786646,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.9945853923384664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.248371713606039,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.7507374420350441,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.478540391890851,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3936451254491828,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 12.450977849735601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3699996948242301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5464981079101676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.010000000000019327,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.058800659179667036,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13884994506835824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6411499023437557,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.8481214141352185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.157012704143185,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.000389128839376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.409525032325272,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.0655698235310345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.461631008322202,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.792144775390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.1942868913923004,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.18913910959582658,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5504371385510116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.632703264757664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 11.54152611144208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1600634118220493,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.3436375903835316,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 9.160003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4012638648992928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.4871150913239095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.5179778799093269,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 15.218247666124597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7120639091572585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1701295505923248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.084310592076477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.563350875187844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.6527410417254806,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3583143152959054,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2638540490730659,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 13.405992562893765,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.5812053437476692,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.5022212854166295,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3505165667071601,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.873998298986926,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.2285003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -16.31950073242183,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.164347534179683,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.973848266601578,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.1957160949707486,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0560408020019736,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9942891172556667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 7.299086128396482,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3160898568768573,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.248802590138592,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.0425036485986716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.957445173059181,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3671417236328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7399945940290191,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.08101854466995606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.13233393486365452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9493746247847596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.148769046906452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.024469646365001596,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5290615659593795,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 31.219970703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 34.6400146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.278862639045489,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.459882436669817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.496295804273478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 9.488479818756979,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4264232210243861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.545755051470968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.187910690913645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.268504360817739,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2248577324207153,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.614453030050002,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7144638752910852,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 7.676224715526148,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.8668460318805415,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.877846786295271,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7530835321300087,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.579151784616822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.079501342773483,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -26.753997802734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2761157226561863,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.1110180664062455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.07849334716797784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.14008850097661707,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.458819719222185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.874716410082595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.447346025123277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.440249794716555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.959150350692987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.51040480794488,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.907854352678573,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1957135881696423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.04854640304586111,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.023115299004888623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.014965421994532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.454791529222646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13066664250489524,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.06036479366917413,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.579998016357422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.1700019836425781,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7154307894128742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 14.162486347199987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 13.103476931724812,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.799079239303651,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.496446126592147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.6402303494514996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.878239802698282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.778074734212758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.7694356960376476,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 11.317056940580173,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 10.321645002742418,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.98682413607282,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2031768736872195,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.9723220842758025,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4434126439146482,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.467427310413676,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.564000129699707,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.144500160217284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7050000762939419,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.8426001739501885,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2200000190734812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.1703500556945698,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.5844280700648845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 9.841142616129229,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.024972764694667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7081812550872257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.9939519743639735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5846369700300116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.15892846243722136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.4571426936558316,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.9681335254969348,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.643073233071373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.394874163151478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.086050261936883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.18631971080937004,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.08856200727573293,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 43.1500244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -100.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.133197621799109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 12.034982146741713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 9.961896632301691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.290984945051234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.07316438597265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.221102813222412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.809216014926431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.538155295403968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.9208072848256643,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 9.189552740121899,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.1800647033192995,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.103240048282064,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.779895133067722,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.8890110783981093,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3743888561427937,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.227507871604885,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -12.786715698242233,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -72.83769226074219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.9912634277343386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.388966064453143,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.6689607238769213,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 9.085898742675795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.140291123319464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.130872888774384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.805444428795649,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.849017862420126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.490372410713174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.580717887364214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2457144601004515,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.909999302455361,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.33209679336232334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.0565832973018647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.9326781484232356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.154066728642814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.4862706876961391,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.08133504299965355,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.4899978637695312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.540000915527344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.17698041960847455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 9.857582112636809,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 8.361494231047317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.642471960287943,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.651510174641519,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.2428799689017573,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.8744616760207933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.652461911519055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.8770244870162989,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 7.012152706016995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.579662302064925,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.454727063518773,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.358240921736591,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.5749717037260602,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.439634517237156,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -18.341814487719972,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6470001220703097,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.87700004577637,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.28100006103515796,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3748001098632798,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.380489603363737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.1825134436389106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.951798237706306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.249507679546873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.07464272635323654,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.3814285823277066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.3138929168014899,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.6027387944167524,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.913860272829403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.1361222756198615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.35807269776967043,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.14736235621531235,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 17.610000610351562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -23.770004272460938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.1617478592999495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 13.183004387305365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 10.750285993827333,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -22.843722628101304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 8.433287304757407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.6632369707997015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.526563842110985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.09937405898798,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.107742952675176,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 10.337574980685549,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.968454064844941,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -24.655977731332136,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.140018051852477,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.331145235975399,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.0917366833273476,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -13.788726635188898,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.9444999694824219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -11.195999908447249,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.130939331054691,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.979822387695322,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.09053138732906518,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5250505828857399,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 9.070794606231647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.904676136809428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.836500374585288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.727348360417974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.470382226924173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.92448502449188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6714281354631702,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.9113649640764514,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.5688318739975973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.774561633222965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.994527013753835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.091421225990882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2842277667365596,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.02049482286528126,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.339996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2737033186074784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.673991994695749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.3108338317291786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.577092367048884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.1482919196154775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.31701890466508864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.580990614694368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.7561003290852426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.219698411982705,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.8285625880759344,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.5290019027467863,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.764837263818053,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8550226667105498,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6491106394893915,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.1461634559107328,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.44545290528616,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2739997863769474,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.2649993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2918710327148517,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3369775390625023,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13155738830567998,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.661811447143549,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.9962745938162403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.8316700824154033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.400117393467527,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.1219922146033845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.5358229160074917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.364515314898563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1892852783203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5278560093470981,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.00987576663162093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.367163499284739,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.0396036582417967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.653463533609223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.50273696121546,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.39437724916605865,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.31999969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.310001373291016,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5355407554287428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.475319388713261,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.100656891484823,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.463977999941326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.8491997794626842,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.154703998548522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.8738323332495801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -17.008569084708313,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.5184641511960306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.6298899820934465,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.31882496250243,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.2762331031721565,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.1424690323676123,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -11.82261226372422,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.308659492033217,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -16.69792166090923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2035001754760799,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4025001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.007392654418950428,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.09333877563476278,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.06852966308593977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.38977798461914404,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7575532102170106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.335392031940346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.50348082057321,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.324489524245738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.42273273048549775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.821880830257657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.01500047956194206,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.28571319580078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.039620552935213826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.657133157018035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.45701186827450435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.58354988269887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.05731785493607644,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5012586607995644,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.43000030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.04337220114309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4060160838726068,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.40319455765291945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.001972747131009,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9006252950243043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.4893890431513013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.6014420404447671,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.2236414193957259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.010632705481683491,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.2514454904924217,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.1850264866353117,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.8142278503618394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3926439578806242,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.1572973083269993,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.8333851183388696,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.08700600440335604,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.14700012207030966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8635002136230412,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0018980407714863645,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.014090957641599289,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.02780633926391829,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.12149042129517085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2071440659714439,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.8253082199300099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4824730827405208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7958184175906213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.49457620778779,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5585883398042224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.01642853873116623,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.24964332580566395,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.003361530246979161,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4206525555275382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4020301019561643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6841421638114631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0455566842337356,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.23817172725673452,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.220001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.82000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7005951610239896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.443756908447936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.342383572542095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.130282517046511,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7340346282742187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.0755700457656161,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.00499409417354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0961208998077634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.6465902543992161,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4016724981718789,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.43944835644029734,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.942537620277342,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4407653753692906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.40766178058991853,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5701669353899037,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.785473476008681,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.012999725341813928,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5704986572265796,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.1555038452148665,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.1294909667968795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.029849243164079553,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.07421203613282046,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.721059257099202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.145633214380525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.7649787731528495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.18060828210447744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.5858147394608912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.517136412551189,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.272857666015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6607153756277904,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.08891690014904818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.3992803266985008,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3439056250695316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.44084028390967234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.09527386320063602,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.19066818518649398,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.7299957275390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9696611967394584,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.0562151038749144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.058442821816986,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.946846694634651,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3101596123002537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7940139090145237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.7820162450368677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1077647098456396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.08434370988531503,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7892143027449006,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.7233891071654064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.7591017978654815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.983109640604674,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.46192217419022086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3471890862532305,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.418412133644722,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8169998168945369,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.243000793457043,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.35645111083982783,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.3750546264648449,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.16389358520507358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7808321380615268,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.488481162809907,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.3907134560646952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8149032213736769,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.2997630698243343,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.105214293964419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.775967108082078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.020001002720424044,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5057133265904019,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.04906097543198973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.23350275333653214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8612246710623226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5552131932491045,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.48593149526708834,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6192148323485094,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.80999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.1813877561237427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6776345957659302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6720392425062061,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.1967951242365844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2939455766560961,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.403644941421914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8368431313207081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.140066805758111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.12738284949896928,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.523064002385745,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.4538711714885983,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.009050227467416,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.5872148295610256,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.071553206597612,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.5979840274629282,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.8294193819590294,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3239997863769446,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.9174999237060462,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.11996627807616278,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5030914306640568,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0477357864379826,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.24404602050780966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5413982248529292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.20936528568183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.803184260786538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5657019055341772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9045906853717636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.24449765291159054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.009285518101283419,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2778565543038505,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.0073867045122553154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.30460849096857623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.881006675097673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.1420524514636377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.4012717085736106,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7073131265492754,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.4300003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.8499984741210938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.9681639820334227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5077276746060955,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5052354355080668,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0012868722004464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.593402064130413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7752048135374556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.1186677395296347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.8040105718133987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9141590754086493,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.3377017320137194,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.276596493474325,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.813541975431277,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3001328112254846,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1072965483617594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6838405807459971,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.114657995612481,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4370002746582031,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7990005493164034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.08115173339844262,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.21357833862305142,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.006796188354499577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.04460002899169524,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.579270093708863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8502414989980611,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.951510741151475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.317399861585634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.9861334650706395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.5159421579559638,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1764281136648993,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6746417454310825,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.08654524840689559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5184492783700811,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.803891321699492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.12214994542689706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.29061126821135064,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7167667413340855,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.5699996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 7.099998474121094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.0212370346133657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.0921628173387496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.186691989557965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 10.538491726543242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.394516152259639,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.499534339148328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9520366558526403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.945807262869029,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.03276787201140774,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7532665892810653,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.5951399394244268,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.726236623312412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.8987531006452891,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.831626073972631,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.48279050293099646,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.2564546866681106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.20449981689453978,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.6959999084472628,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.10517669677733466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7554438781738213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.04271720886229957,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.24191177368163608,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.6110911965418815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.174589154330725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.436704112935995,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 7.10477506135887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.329653650306618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.5303425719809285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1250005449567526,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.40321459089006706,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.06699043469509602,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2511650722316623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.2396511501736054,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.187362504680694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.12851000330183215,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.3673419276238009,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6599998474121094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.12000274658203125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.92286244770552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9776484915805961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9655594745615725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.357400466710957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.0349763848993998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.068369350830968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.8993194697579421,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3207728180213762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.13114245891925336,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.8677809150392188,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.8162724544208197,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.169655569941788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2582928680055279,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.7362776160066655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.5355076890256947,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0101253942222943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1079999923706012,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5414999008178683,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.027437973022458095,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.05752540588378707,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.010500888824459764,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.03499300003051786,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.2901497878798462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0339642253629044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.5143507682390256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.1431094407640332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.48179846628127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.19414684338373567,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.018571308680943033,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.03392791748046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.02069389769507768,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.07367541693610868,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.500457556516388,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.272816772030704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.019563990820942623,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.027650615964984526,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.131743259769192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.3658221757028901,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3688399623292815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.32885852847750474,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7447427810587381,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.8141306247324565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.0997928855721373,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.6008070732110857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.07773835314441868,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.479607230916925,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.4129919666531103,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.4833965747533262,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.5485264718461895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4820388899081536,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3350342732114995,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.9114544970101677,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13600006103515483,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7840000152587905,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.010625534057616903,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.02625175476074304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.021802005767817434,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.09531251907348093,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.1660128264529224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4367403598646069,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4814823766164942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.4188714395084743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4403417028667986,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.105374888367595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.008750098092215386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.1196071079799107,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.004810833773671863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.23516869095754944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4184383971608927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.9182519190872216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.1871185412590759,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.09992341328298515,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.9899978637695312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7299995422363281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.6318373146525964,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.14231364445473904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13775282635053454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.817144577729605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9811687764344166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3449505026112307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4561956794927555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7745708509347526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.577832408027823,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.703115762165076,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.6440791026318577,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.629399680960436,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.312100476470512,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0128587677869287,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.9786314792908817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.46392342713567114,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.17500000000000426,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8430002212524457,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.225036620894798e-05,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.046115875244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0180179595947223,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.10612070083617908,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.5723687531323138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.1278385960476607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.946484352840483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.33978935282959,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9103992250012913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.6560350026994186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.053928375244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2903573172433036,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0673356983282698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.567036934502712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8367306785588955,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.7810813951628535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.32849705134939156,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.8203068494996234,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 23.45001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -20.899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.429369664168556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 7.768243939513885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 7.090465285177428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.0384049572997336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.573609910600052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.2857553937484134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.16348781347574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.315325759770683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6246352424562174,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.922814532894071,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.308633356195036,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2261498540689031,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.2803406576951257,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.617847128572718,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.7286606546921028,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.004678335971601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -5.1789993286132585,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -31.86150207519529,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3139996337890807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.252199707031309,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4366000366210301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.1313499450683366,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.251453539474449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.4733684336358799,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.346428082070709,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.5606850662466147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.416341785133849,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.401292256095656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.7135685511997778,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.626427786690847,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.10910311665244077,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.927298454710936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.6993234427947783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.297048918053445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.2687502844005736,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.34995001720757934,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.5800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.740530022744725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.90091126289407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.755663247866959,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 8.087815625589323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.414697422048274,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.6973538517048183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.445444464382808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.7479904330236828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6865251161199515,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.055481856274255,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9738313188845669,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.275560522358492,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.1214281691433463,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.3652621168805155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.010617305599171,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.437343009224601,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.4909999847412081,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.4484996795654297,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.16080001831053892,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4187998962402304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.018841590881351067,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.10685394287109773,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.8510331289174573,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7400065983448902,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.5613875692758743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.038506146119200224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.721582351720331,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5909237858373606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.05500030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.174285888671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.02307008918311171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.1580133042126639,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.289874743040343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.39052316371432916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.016179263416443268,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4722969383760748,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.3799896240234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.410003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.4082211705891847,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.224561806453643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.690391294070761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.51193675084226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.0979864901930156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -13.630990020848033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.5007573960989942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.91386419750822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.6457837360355887,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.3791323998338285,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9085593650883688,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.32419185407309,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.3912557430979433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -13.29889828602373,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -2.935584554882631,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -19.60321677370914,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.0069999694824219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.1585006713867188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.22103118896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5667410278320233,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.2033019256591615,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1845133209228322,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.6569925733343265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -8.398086600474164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.304294644851522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.866820518087739,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.10126524340734466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -12.134686172550555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.0739288330078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9139284406389505,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.050310803917590796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8283332388882627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.18548746602133903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -9.474765012340136,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.0788450834952954,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0628894653636969,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.42999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -28.45001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2011319281367117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.720447513098448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.1524492925531975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.9905004008669476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.1279024694208495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.797839913900916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.1638807495952932,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.61178676533299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.255136834761485,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.8750181064786338,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3706173635708048,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.802755504097778,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.1653667834840786,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.465748179076613,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.5987079083789304,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -14.301139341533908,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.4060012817383267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.0645019531250455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.1546002197265466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -4.739801025390591,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.10339996337893353,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.7193997192383108,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4839454008985342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.814851756392525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3806028615078834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.023753381077935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.0880170000033385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.3126368679852005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.08428519112723265,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.304284232003349,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.02828037065420741,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.897724099263653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.01470356224128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -6.5165635352187685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.18653215825358327,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.5433028086452568,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.6899948120117188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -143.00999450683594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.62232386450989,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.544382494537544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.488694796480372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.476321024049378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.2182447782273425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.638421705178227,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.0339374746146675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.7056136970124527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5683189578851167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.301046912082271,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.2931371325020202,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.2885761272802085,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.9249755253224148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.9705134400025299,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.40088968416896975,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.3949662732133703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.14966659545898153,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -137.56549949645998,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.11693603515624318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -143.55204895019529,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.03245128631591854,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -152.53168529510498,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.6597929388898276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4856351572625428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.9699473320540912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.2391169187371265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.5815655325898135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.4224023447534808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.10119083949497787,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.8271424429757253,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0320819373130905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6409611843821539,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.1906404573894065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.13047838255315725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.011385704651406203,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.4792345560003537,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.6100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.46000099182128906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.5809077164645737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.403533691251262,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.154495430237228,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.5443658633846464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 6.292030495095059,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.7017896313405245,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.595077137281677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.1407999817657153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.4730971901601997,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.558104284631447,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3726635012548356,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7321107601538155,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.9987612421901306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 5.033881366164827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.1602499784980402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.1698474420333671,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.08649997711181712,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.8777499198913574,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.04639995574951428,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.36470001220703097,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.018599996566777577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.13057498931885192,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.6490475935141005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.347220121381879,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.274563579596403,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 2.5553241681287924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.030787213942933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.7908935884115458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.07000010354178288,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2047857557024274,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.04461670721543243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.6371612296124893,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.618475565584124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.3195667922182857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.943881096182129,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.5466037683447427,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.28000640869140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.8834256660408277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6572567569311349,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.6436177089930606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.7547210545860503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.969782926155327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8472958772301364,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3974319888404807,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.5087981145780813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.1705792405839457,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.50268616355095,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -3.425449637975453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.5669761578168813,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.3234863267496024,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1793876120544384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.037395169943156,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.1981506907789994,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.19449996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.8924995422363224,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.008584594726556816,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.10482986450195142,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.034998455047599464,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.1420673751831032,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.4698713793096507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.687675092538088,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.755823097699194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.24041889682508977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.7216873542609257,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.6081005569421594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.0021433149065290813,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.2646446228027344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.03578916992277836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.36743926095719126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.6131392078879925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.361351453056014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.24129506337904372,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.45628987789583575,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.260009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.839996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.3980803147961036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.176046609019559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 5.852358390055867,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 6.528673218750026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.624709723877684,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.634354994318322,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 4.4485983179443735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.811099452258542,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3440754081713302,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 3.330617202399744,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.070526461073475,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 4.716418115519195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.3314404709727565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.302263259494019,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.0137711591607363,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -7.50045202845946,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -1.0899993896484546,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -5.116499328613287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.28859985351562045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.0436001586913903,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.13680004119871114,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.726600036621079,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 3.2388383092944553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 0.5548964107984444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.7611607668609146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -1.7482402948237885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.9945899454958633,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -3.393262884531943,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 0.08500126429966492,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.40142713274274566,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.04131751676549689,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.17487086297402055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 2.4358223914986983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -2.1956637608164584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": 1.372974072558075,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": 1.1138411815931195,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.04999999999999982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.04999999999999982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -0.06000000000000005,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.0,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.009999999999999898,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.020000000000000462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": -0.08000000000000007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": 0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 0.029999999999999805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 16,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-06",
        "to": "2026-11-09",
        "change": -0.009999999999999787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-11-02",
        "to": "2026-11-09",
        "change": -0.06999999999999984,
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
    "available_prior_observations": 15,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-05",
        "to": "2026-11-06",
        "change": -2.539999999999999,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-30",
        "to": "2026-11-06",
        "change": 6.219999999999999,
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

## 判断依据 · 反弹是否足以升级风险判断

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否足以升级风险判断 |
| 事实指标引用 | ["prices.SPY.distance_sma20_pct", "prices.QQQ.distance_sma20_pct", "prices.RSP.return_1d_pct"] |
| 推断与解释 | 从脆弱的盘前修复，上调为初步可靠的收盘反弹，尚不是趋势反转。今晚21:30北京CPI、22:30开盘后的回踩比继续追高更关键。 |
| 反证与缺口 | QQQ仍低于200日线；AMZN/GOOGL收盘承接弱，缺全市场广度。 |
| 确认条件 | SPY742.21–741.09、QQQ664.52–662.02回踩承接，RSP守217.67；随后突破SPY755.42、QQQ约682（日内高点供应商681.695–682.48有差异）且收盘保持；QQQ站稳动态200日线约680.09，再看SPY20日线762.09。 |
| 失效条件 | CPI后跌破上述支撑且反抽失败先下调；进一步失守SPY734.58、QQQ654会否定大部分修复。VIX重返25.64加强风险。 |
| 观察期限 | 11月10日至13日，AI财报延伸至17日 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 从盘前分化更新为周一收盘普涨、期限关系改善；保留趋势及现金流限制。 |

## 判断依据 · 哪些板块值得优先观察

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 哪些板块值得优先观察 |
| 事实指标引用 | ["prices.XLF.return_5d_pct", "prices.XLV.return_20d_pct", "prices.OIH.return_5d_pct"] |
| 推断与解释 | 金融医疗和云端部分公司跨期占优，芯片首日反弹强但5日仍弱，分层观察。 |
| 反证与缺口 | 当日相对强不等于持续强，更不等于净流入。 |
| 确认条件 | MSFT守538.70并突破548.28后承接；XLF守57.255再试58.26/59.20；XLV守近期低点并保持5/20日相对强度；XLI站稳约169.18动态50日线。 |
| 失效条件 | 强势板块回踩失败且相对SPY转弱，或只剩少数权重拉升；日内高点不是自动买点。 |
| 观察期限 | 11月10日至13日，AI财报延伸至17日 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 从盘前分化更新为周一收盘普涨、期限关系改善；保留趋势及现金流限制。 |

## 判断依据 · AI基本面压力是否解除

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI基本面压力是否解除 |
| 事实指标引用 | ["prices.SMH.return_5d_pct", "prices.SMH.volume_vs_previous20_ratio"] |
| 推断与解释 | 股价修复不等于交付/融资解除；H1009日3.01支持需求尚有韧性。 |
| 反证与缺口 | 缺完整现金回收和四家公司估值桥；不能由价格替代基本面。 |
| 确认条件 | 投产按时、资金条款可落实、客户现金回收与利润匹配，相关股财报后守住低点且次日不回吐。 |
| 失效条件 | 新增延期、融资缺口/信用走阔与价格转弱共振；EPS达标不能掩盖指引恶化。 |
| 观察期限 | 11月10日至13日，AI财报延伸至17日 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 从盘前分化更新为周一收盘普涨、期限关系改善；保留趋势及现金流限制。 |

## 判断依据 · 恐慌是否明显缓解

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌是否明显缓解 |
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | VIX19.92与VIX3M20.85同日比0.955，CNN32；恐慌缓解但不构成过热。 |
| 反证与缺口 | 信用仅截至6日，战争与CPI可再次放大波动。 |
| 确认条件 | SPY742.21–741.09、QQQ664.52–662.02回踩承接，RSP守217.67；随后突破SPY755.42、QQQ约682（日内高点供应商681.695–682.48有差异）且收盘保持；QQQ站稳动态200日线约680.09，再看SPY20日线762.09。 |
| 失效条件 | CPI后跌破上述支撑且反抽失败先下调；进一步失守SPY734.58、QQQ654会否定大部分修复。VIX重返25.64加强风险。 |
| 观察期限 | 11月10日至13日，AI财报延伸至17日 |
| 条件式指导 | 条件未满足先观察；不以单次越线或涨跌幅指定最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 从盘前分化更新为周一收盘普涨、期限关系改善；保留趋势及现金流限制。 |

## 宽基反弹扩大但趋势仍待修复 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 油价走低与风险偏好恢复，CPI前市场重新买入成长与周期。 |
| 事实：市场反应 | 19/19ETF上涨，RSP/IWM跟随，QQQ仍略低于200日线。 |
| 推断：解释 | 推断：不只是单一权重拉升，反弹可靠性上升；日线趋势仍未完成修复。 |
| 受益篮子 | ["MSFT", "XLC", "XLF", "XLV", "IWM"] |
| 受损篮子 | ["无基本面支撑且相对弱的反弹篮子"] |
| 反证 | QQQ与SPY仍低于20/50日线，反弹可能包含空头回补；缺完整成分广度。 |
| 下一催化剂 | 11月10日08:30EST CPI与随后收盘承接 |
| 证据 | ["https://www.bls.gov/schedule/2026/11_sched.htm", "https://apnews.com/article/d938f8e6ff42b3706e1d36e6245ec56b"] |

## 半导体普涨与NVIDIA治理折价分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | NVIDIA独立调查仍在，行业交付/融资问题留待财报。 |
| 事实：市场反应 | SMH+5.05%，NVDA-4.27%，MU+6.25%；涨跌不能代表同一经营风险。 |
| 推断：解释 | 推断：单股治理折价暂未蔓延为全行业抛售，但并未证明需求/现金流压力消失。 |
| 受益篮子 | ["相对强的芯片、设备与云端观察篮子"] |
| 受损篮子 | ["NVDA治理风险", "交付延期且高负债的算力企业"] |
| 反证 | H1003.01仍强；MSFT和AMZN财务能力不代表所有供应商安全。 |
| 下一催化剂 | CoreWeave10日、Nebius12日、NVDA17日财报 |
| 证据 | ["https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors", "https://www.silicondata.com/products/silicon-index/h100"] |

## 外交缓和预期压低能源溢价 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 公开报道特朗普认为近期新增对伊军事行动可能性降低，仍无全面和平或通航恢复的充分证据。 |
| 事实：市场反应 | 原油继续回落，XLE小涨但5日仍-7.90%，油服与上游未恢复持续强势。 |
| 推断：解释 | 推断：市场优先交易能源成本缓解；消息逆转和真实供应中断仍会令油价反弹。 |
| 受益篮子 | ["航空运输及能源成本较高的下游观察篮子"] |
| 受损篮子 | ["XLE", "XOP", "OIH的旧趋势"] |
| 反证 | 谈判声明可逆，沙特管道/油轮事件有专门地域和真实性要求。 |
| 下一催化剂 | 外交正式文件、运输与库存数据、CPI |
| 证据 | ["https://apnews.com/article/d938f8e6ff42b3706e1d36e6245ec56b"] |

## CPI成为反弹能否延续的检验 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 官方CPI为10日08:30EST，tc概览12日日期不采用。 |
| 事实：市场反应 | VIX期限比回到1以下，CNN32仍Fear；10年收益率并未明显下降。 |
| 推断：解释 | 推断：波动压缩可支持修复，但通胀/实际利率与盈利须继续配合。 |
| 受益篮子 | ["通胀缓解下现金回报可见的成长资产"] |
| 受损篮子 | ["再通胀时长久期和高杠杆资产"] |
| 反证 | 预测市场恰0.2%与恰0.3%合约不是市场一致预期；CME未核验。 |
| 下一催化剂 | 10日CPI、13日PPI |
| 证据 | ["https://www.bls.gov/schedule/2026/11_sched.htm"] |

## 航天订单增长要转为现金与利润 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 盘后新增：Rocket Lab官方披露Q3纪录营收2.68亿美元，积压订单35.7亿美元、环比+52%，经营现金流为正，Q4指引收入与毛利扩张。 |
| 事实：市场反应 | ARKX当天+5.67%发生于财报前，不能由盘后披露解释；tc盘后下跌线索未作正式价格核验。 |
| 推断：解释 | 推断：订单增长是支持，兑现节奏与费用才决定估值，利好不保证股价上涨。 |
| 受益篮子 | ["ARKX", "RKLB等订单兑现观察篮子"] |
| 受损篮子 | ["延期与现金消耗大的高估值承包商"] |
| 反证 | 积压订单不等于当期收入；未核验的EPS miss不作为确定事实。 |
| 下一催化剂 | 财报后首个常规收盘和后续交付 |
| 证据 | ["https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-third-quarter-2026-financial-results-posts"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 753.60 | 缺失 | 2026-11-09T23:15:29+00:00 | 2026-11-09T23:15:29+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| QQQ | 680.17 | 缺失 | 2026-11-09T23:18:48+00:00 | 2026-11-09T23:18:48+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| SMH | 488.80 | 缺失 | 2026-11-09T23:12:21+00:00 | 2026-11-09T23:12:21+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| NVDA | 179.30 | 缺失 | 2026-11-09T23:18:58+00:00 | 2026-11-09T23:18:58+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| MSFT | 545.21 | 缺失 | 2026-11-09T23:16:51+00:00 | 2026-11-09T23:16:51+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| AMZN | 268.33 | 缺失 | 2026-11-09T23:18:53+00:00 | 2026-11-09T23:18:53+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| GOOGL | 290.30 | 缺失 | 2026-11-09T23:18:50+00:00 | 2026-11-09T23:18:50+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |
| META | 644.43 | 缺失 | 2026-11-09T23:18:49+00:00 | 2026-11-09T23:18:49+00:00 | 2026-11-09T23:20:17.110961+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 752.69 | USD_per_share | 2026-11-09 | 2.37 | 0.08 | -3.27 | ok |
| QQQ | 679.35 | USD_per_share | 2026-11-09 | 3.54 | -0.26 | -8.94 | ok |
| IWM | 282.51 | USD_per_share | 2026-11-09 | 3.23 | 1.21 | 1.66 | ok |
| RSP | 220.95 | USD_per_share | 2026-11-09 | 2.27 | 0.44 | 3.64 | ok |
| GLD | 379.53 | USD_per_share | 2026-11-09 | 1.88 | 4.94 | -0.69 | ok |
| GC=F | 4,147.70 | USD_per_troy_ounce | 2026-11-09 | 1.79 | 4.49 | -1.02 | ok |
| CL=F | 86.25 | USD_per_barrel | 2026-11-09 | -5.04 | -10.58 | -7.99 | ok |
| BZ=F | 92.15 | USD_per_barrel | 2026-11-09 | -6.28 | -12.05 | -13.60 | ok |
| TLT | 81.96 | USD_per_share | 2026-11-09 | 0.05 | 0.28 | 5.01 | ok |
| UUP | 28.97 | USD_per_share | 2026-11-09 | -0.55 | 0.03 | -0.55 | ok |
| HYG | 77.51 | USD_per_share | 2026-11-09 | 0.36 | 0.81 | 0.28 | ok |
| LQD | 104.67 | USD_per_share | 2026-11-09 | 0.13 | 0.93 | 2.04 | ok |
| ^VIX | 19.92 | index | 2026-11-09 | -22.31 | -5.82 | 30.97 | ok |
| ^VIX3M | 20.85 | index | 2026-11-09 | -15.24 | -3.47 | 16.29 | ok |
| ^VVIX | 98.43 | index | 2026-11-09 | -19.28 | -10.90 | 14.55 | ok |
| ^MOVE | 85.98 | index | 2026-11-09 | -7.32 | -14.32 | -12.68 | ok |
| NVDA | 178.67 | USD_per_share | 2026-11-09 | -4.27 | -11.58 | -21.05 | ok |
| MSFT | 545.18 | USD_per_share | 2026-11-09 | 2.75 | 7.51 | 0.74 | ok |
| AMZN | 266.93 | USD_per_share | 2026-11-09 | 2.94 | 8.67 | 2.85 | ok |
| GOOGL | 288.15 | USD_per_share | 2026-11-09 | 1.18 | 3.28 | -18.31 | ok |
| META | 641.37 | USD_per_share | 2026-11-09 | 5.12 | 5.71 | -13.67 | ok |
| CRWV | 48.98 | USD_per_share | 2026-11-09 | 5.56 | -2.33 | -38.97 | ok |
| MU | 733.15 | USD_per_share | 2026-11-09 | 6.25 | -12.05 | -25.86 | ok |
| DRAM | 41.78 | USD_per_share | 2026-11-09 | 6.34 | -9.80 | -23.65 | ok |
| VRT | 200.47 | USD_per_share | 2026-11-09 | 9.63 | -10.60 | -16.25 | ok |

## 跨资产风险解释

恐慌明显降温，仍不是过热。11月9日VIX19.92、VIX3M20.85，同日比值0.955（周五约1.042），是波动率指数期限关系而非期货曲线；VVIX98.43、MOVE85.984也下降。CNN浏览器核验32、前收22，更新9日18:03:38EST，Fear而非Extreme Fear；tc温度不替代CNN。美元UUP-0.55%、GLD+1.88%，黄金与股票共涨并不等于战争已经结束。盘后23:09UTC WTI86.24、Brent92.20是期货新时段报价，供应商日线和结算口径不同，不将日线-5.04%/-6.28%称为周一正式结算收益。Yahoo10年收益率9日4.864%，较6日4.859%略升，不是利率全面下行。FRED2年4.51%、10年4.86%、实际10年2.63%、HY342bp、IG93bp截至6日，HY较5日348bp回落但不证明周一信用同步改善；盈亏平衡通胀9日2.22%。金融压力截至10月30日、GPR截至11月2日，不能反映最新战争。谈判报道与油价回落一致，但不代表运输恢复；以多指标并列，不制造战争总指数。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.51 | percent | 2026-11-06 | -0.24 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.42 | percentage_points | 2026-11-06 | 0.31 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.93 | percentage_points | 2026-11-06 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.86 | percent | 2026-11-06 | -0.36 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.63 | percent | 2026-11-06 | -0.24 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.22 | percent | 2026-11-09 | -0.11 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.52 | index | 2026-10-30 | 0.24 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 25.64 | index | 2026-11-06 | 10.80 | lagged | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 113.95 | index | 2026-11-02 | -245.09 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 129.82 | index | 2026-11-02 | -342.91 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 108.29 | index | 2026-11-02 | -240.96 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 158.85 | index | 2026-11-02 | -44.27 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 184.74 | index | 2026-11-02 | 13.98 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

```json
{
  "value": 32,
  "rating": "Extreme Fear",
  "observed_at": "2026-11-09T18:03:38-05:00",
  "retrieved_at": "2026-11-09T23:23:52.619808+00:00",
  "source": "https://www.cnn.com/markets/fear-and-greed",
  "quality": "verified_browser",
  "previous_close": 22,
  "one_week_ago": 19,
  "note": "CNN浏览器加载后核验32/Fear，API418；晚报盘前25不是前收。"
}
```

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | 3.73 | -1.92 | -12.98 | 1.36 | -2.00 | -9.71 | 1.25 | 2026-11-09 |
| XLE | 能源 | 0.52 | -7.90 | -6.17 | -1.85 | -7.97 | -2.90 | 1.10 | 2026-11-09 |
| XLF | 金融 | 1.45 | 0.75 | 5.34 | -0.91 | 0.67 | 8.61 | 1.02 | 2026-11-09 |
| XLI | 工业 | 3.82 | -0.48 | -0.15 | 1.46 | -0.56 | 3.11 | 1.02 | 2026-11-09 |
| XLV | 医疗 | 1.91 | 2.02 | 9.50 | -0.46 | 1.94 | 12.77 | 0.88 | 2026-11-09 |
| XLP | 必需消费 | 0.90 | 0.07 | 7.68 | -1.47 | -0.01 | 10.94 | 0.94 | 2026-11-09 |
| XLY | 可选消费 | 2.92 | 2.41 | 7.78 | 0.55 | 2.33 | 11.05 | 0.92 | 2026-11-09 |
| XLC | 通信 | 2.45 | 7.08 | -3.67 | 0.09 | 7.00 | -0.40 | 0.97 | 2026-11-09 |
| XLU | 公用事业 | 1.53 | 0.27 | 5.19 | -0.84 | 0.20 | 8.45 | 1.02 | 2026-11-09 |
| XLRE | 房地产 | 1.45 | 2.29 | 6.49 | -0.91 | 2.21 | 9.75 | 1.22 | 2026-11-09 |
| XLB | 材料 | 1.91 | -1.36 | 7.08 | -0.46 | -1.44 | 10.34 | 0.97 | 2026-11-09 |
| SMH | 半导体 | 5.05 | -4.11 | -17.53 | 2.69 | -4.19 | -14.26 | 1.26 | 2026-11-09 |
| IGV | 软件 | 2.61 | -0.43 | -8.82 | 0.24 | -0.51 | -5.56 | 0.91 | 2026-11-09 |
| XOP | 油气开采 | 0.22 | -10.03 | -10.37 | -2.15 | -10.11 | -7.10 | 1.15 | 2026-11-09 |
| OIH | 油服 | 1.24 | -7.31 | -7.23 | -1.12 | -7.39 | -3.97 | 0.72 | 2026-11-09 |
| ITA | 航空与国防 | 3.90 | 0.15 | 4.36 | 1.53 | 0.08 | 7.62 | 0.70 | 2026-11-09 |
| ARKX | 航天主题 | 5.67 | 1.56 | -5.45 | 3.30 | 1.48 | -2.18 | 3.23 | 2026-11-09 |
| KRE | 区域银行 | 1.73 | -0.38 | 5.59 | -0.64 | -0.46 | 8.86 | 0.88 | 2026-11-09 |
| SKYY | 云计算 | 2.91 | -2.48 | -12.64 | 0.54 | -2.56 | -9.37 | 2.16 | 2026-11-09 |

## 资金证据分层

19个板块与主题ETF全部收涨，较周五7/19扩散；RSP+2.27%略落后SPY+2.37%，IWM+3.23%，这是ETF样本参与面而非全市场涨跌家数。当天SMH+5.05%、ARKX+5.67%、ITA+3.90%、XLI+3.82%、XLK+3.73%；但5日SMH仍-4.11%、XLE-7.90%、XOP-10.03%，不能因反弹就恢复旧趋势。5日XLC+7.08%、XLY+2.41%、XLV+2.02%、XLF+0.75%，更适合优先观察承接，金融医疗当日强度落后SPY也须承认。MSFT/AMZN5日分别+7.51%/+8.67%，NVDA-11.58%、MU-12.05%，AI内部区别大。成交量相对前20日均量SPY1.04倍、QQQ1.09倍、SMH1.26倍，参与改善但非巨量确认；NVDA3.88倍说明个股风险成交集中。SMH、QQQ仍低于多条关键均线，工业接近50日线169.18。价格与成交量仅为交易偏好，不称主力净流入。发行人SMH页仍截至6日NAV464.02，缺连续份额和拆分桥；ICI本次仍11月3日发布、10月28日一周净发行459.06亿美元，其中国内股票265.90亿、债券142.34亿、商品-18.89亿。当前轮动与滞后申赎分列。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

本轮配置清单及20组Gamma主动搜索覆盖Fed/CPI/衰退/银行、AI泡沫/破产/Oracle评级、Apple/CXMT、Texas数据中心、Anthropic、伊朗/沙特/Khor Mor、NVIDIA治理和航天。每组最多10项，有截断；Iran November strike一次超时，已由配置与停火/海峡事件补覆盖。15个合约规则hash一致；Huang离任规则文字补充实际发生情形，hash变更，重新核验并重设基线；RKLB活跃EPS合约已不在结果，财报已发布，移出未来事件，不伪造平台结算。新增工业/软件高质量合约未找到不等于无风险。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.1499999999999995, {"status": "comparable", "change_pp": -0.10000000000000009}] | {"spread": 0.0010000000000000009, "volume24h_usd": 42340.498488, "liquidity_usd": 168308.72412, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:21.229954+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["AI专门阈值，不能解释为普通回调概率", "融资/资本开支/估值"] | ["三项规则证据逐项核验", "单只股大跌或主观泡沫报道不算"] | [null, null] |
| ["Oracle downgraded to junk by Moody's or S&P by December 31, 2026?", "2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。", "https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by"] | [8.85, {"status": "comparable", "change_pp": -0.3500000000000003}] | {"spread": 0.133, "volume24h_usd": null, "liquidity_usd": 615.02009, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-09T23:19:00.941593+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["正式信用降级的专门事件；极宽价差与低成交，不把中间价波动当信用改善。", "信用融资成本"] | ["Moody’s/S&P正式降至非投资级", "负面观察/展望不是降级"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by November 30?", "11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [81.0, {"status": "comparable", "change_pp": 50.0}] | {"spread": 0.019999999999999907, "volume24h_usd": 17479.617412, "liquidity_usd": 45746.193, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:00.953139+00:00", "contract_end_at": "2026-11-30T20:59:00+00:00"} | ["仅指定东西管道/泵站命中；沙特阿美办公楼、其他油气田或油轮事件不自动触发。", "油价/通胀/利润率"] | ["专门地域和武器条件独立确认", "威胁、残骸或其它航道事故不算"] | [null, null] |
| ["Jensen Huang announced resignation or removal by December 31, 2026?", "年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 本轮规则补充无合格公告但实际发生合格辞任/撤职也算；规则hash已变，不计算前期概率差。", "https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31"] | [13.5, {"status": "definition_changed_or_unknown", "change_pp": null}] | {"spread": 0.010000000000000009, "volume24h_usd": 378251.5668849999, "liquidity_usd": 55917.7739, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:21.229954+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["管理层离任专门事件规则文字变更，本次重新建立基线13.5%，不与旧规则相减；不能解释成订单损失或定罪概率。", "管理连续性、政策限制与NVDA/SMH风险溢价"] | ["公司正式更新及现货/行业相对走弱共同核验", "调查澄清且经营/价格保持，不凭盘口即认定离任"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [79.5, {"status": "comparable", "change_pp": 3.0000000000000027}] | {"spread": 0.010000000000000009, "volume24h_usd": 148004.068634, "liquidity_usd": 583903.4795, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:21.229954+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月单次加息25bp合约；CME动态概率未独立核验，不混为Fed承诺。", "贴现率"] | ["官方政策与经济数据核验", "报价变化不等于实际决策"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [9.5, {"status": "comparable", "change_pp": 0.9999999999999996}] | {"spread": 0.010000000000000009, "volume24h_usd": 501929.076654, "liquidity_usd": 208360.6678, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:21.229954+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["海峡恢复按IMF船流阈值，不按谈判标题", "能源供应与运输"] | ["7日通行均值达60", "口头开放不算"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [96.8, {"status": "comparable", "change_pp": 9.599999999999998}] | {"spread": 0.01200000000000001, "volume24h_usd": 144651.280194, "liquidity_usd": 60318.48327, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:03.794892+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["正式上市交易与融资退出窗口；提交申请不等于IPO完成。", "融资退出渠道"] | ["交易所实际开始交易", "只提交文件不算"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [18.0, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.01999999999999999, "volume24h_usd": 1.41, "liquidity_usd": 1798.8632, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-09T23:19:03.311716+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["中国存储竞争的专门采购事件", "DRAM采购与议价"] | ["正式采购公告/可信报道证实", "不等于HBM或NAND利润已崩溃"] | [null, null] |
| ["Will Texas enact a data center moratorium by June 30, 2027?", "2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。", "https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928"] | [17.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999981, "volume24h_usd": 77.99, "liquidity_usd": 33234.5102, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-09T23:19:04.395652+00:00", "contract_end_at": "2027-07-01T03:59:00+00:00"} | ["Texas全州法定暂停，期限不同不能拼接；要求州级成文法制定，非仅行政令。", "建设许可、投产进度与贴现率"] | ["符合范围的州法律或宪法条款正式制定；不要求已经实施", "地方限制、提案或选举言论不算"] | [null, null] |
| ["US x Iran Effective Ceasefire by November 15?", "须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。", "https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108"] | [43.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 67176.16575300001, "liquidity_usd": 80396.1674, "quality_flags": [], "retrieved_at": "2026-11-09T23:19:21.229954+00:00", "contract_end_at": "2026-11-15T20:29:00+00:00"} | ["只衡量特定美国攻击的连续14日间隔及报道窗口，不等于全面和平或海峡恢复。", "能源风险溢价、通胀与风险偏好"] | ["逐日核验合资格行动与14日及额外3日报道窗口", "发生符合规则的命中行动重新计时；口头缓和不算完成"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will Core CPI MoM be 0.2% in October?", "按BLS首次发布2026年10月季调核心CPI月环比一位小数恰为0.2%结算；不是超过此值，也非同比或总体CPI。计划11月10日08:30ET；若延期，按规则等至下一次计划发布，仍缺则用最近可用月。", "https://polymarket.com/event/core-cpi-mom-october-2026"] | [54.50000000000001, {"status": "comparable", "change_pp": 6.000000000000005}] | {"spread": 0.10999999999999999, "volume24h_usd": 1022.773234, "liquidity_usd": 1972.5107, "quality_flags": ["liquidity_under_10000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-09T23:19:21.229954+00:00", "contract_end_at": "2026-11-11T04:59:00+00:00"} | ["核心CPI环比恰0.2%；不是低于门槛累计概率", "利率与风险偏好"] | ["BLS首次值及股债汇反应", "低量/宽价差不能替代官方数据"] | ["2026-11-10T08:30:00-05:00", "https://www.bls.gov/schedule/2026/11_sched.htm"] |
| ["Will Nvidia (NVDA) beat quarterly earnings?", "NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。", "https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53"] | [93.7, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.10399999999999998, "volume24h_usd": null, "liquidity_usd": 403.85762, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-09T23:20:36.234807+00:00", "contract_end_at": "2026-11-17T22:00:00+00:00"} | ["固定EPS门槛，宽价差降低解释力；超预期不能排除治理/指引风险。", "需求与利润兑现"] | ["首次EPS/指引/现金流同时看", "业绩达标仍可能股价下跌"] | ["2026-11-17T16:20:00-05:00", "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873"] |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.0, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.9999999999999996} |
| 24h成交量 / 流动性 USD | [501929.076654, 208360.6678] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:16:15.190971Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Jensen Huang announced resignation or removal by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1343940 / 6882826 |
| Yes 概率 % | 13.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, null] |
| 与上一快照可比变化 | {"status": "definition_changed_or_unknown", "change_pp": null} |
| 24h成交量 / 流动性 USD | [378251.5668849999, 55917.7739] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 年末23:59美东前，黄仁勋/NVIDIA或授权代表正式明确宣布辞任或被撤去CEO，且预定在宣布后18个月内实施则Yes；不要求年内实际离任。临时休假、停职、条件式考虑、未被接受辞呈和媒体单独传闻不算。以官方信息优先；不得把调查直接视为离任。 本轮规则补充无合格公告但实际发生合格辞任/撤职也算；规则hash已变，不计算前期概率差。 |
| 规则指纹 | 967939ae08f1461b2a8b5a40c6c07828619958ef439b679055b7698fa1e18988 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/jensen-huang-announced-resignation-or-removal-by-december-31 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 79.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.0, 7.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 3.0000000000000027} |
| 24h成交量 / 流动性 USD | [148004.068634, 583903.4795] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:16:15.190971Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## US x Iran Effective Ceasefire by November 15?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1337182 / 6831494 |
| Yes 概率 % | 43.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [67176.16575300001, 80396.1674] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-15T20:29:00+00:00 |
| 结算规则摘要 | 须完成连续14个伊朗标准时间日，美国未对伊朗陆地及内水实施命中目标的合资格空袭/地对地导弹攻击，且该14天首日在创建后至11月15日范围内；最后一次合资格行动次日为首日，无行动则创建日为首日。拦截碎片、威胁、海域/领空、地面入侵、网络、小型武器/部分小型袭击等不算。第14日后再留3个日历日报道窗口，按官方信息及可信报道综合裁定。不是双方全面停火，也不要求14天在15日前完成。 |
| 规则指纹 | c70e370d0e95bf9245a1a527f4f02bb307f13aa2766e1cc24004c7559bfb4b53 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/us-x-iran-effective-ceasefire-begins-by-2-week-pause-20261108 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.15 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.05, -1.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.10000000000000009} |
| 24h成交量 / 流动性 USD | [42340.498488, 168308.72412] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:16:15.190971Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.0} |
| 24h成交量 / 流动性 USD | [13746.895657, 69408.0992] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:16:15.190971Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will Core CPI MoM be 0.2% in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1189688 / 5699271 |
| Yes 概率 % | 54.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [7.5, 12.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 6.000000000000005} |
| 24h成交量 / 流动性 USD | [1022.773234, 1972.5107] |
| 价差 pp | 11.00 |
| 到期 | 2026-11-11T04:59:00+00:00 |
| 结算规则摘要 | 按BLS首次发布2026年10月季调核心CPI月环比一位小数恰为0.2%结算；不是超过此值，也非同比或总体CPI。计划11月10日08:30ET；若延期，按规则等至下一次计划发布，仍缺则用最近可用月。 |
| 规则指纹 | 45dda9ee16dc73ce90be8c4ebccc0c3d9bb30b030af1c018876e6a0f462eb329 |
| 质量 | ["liquidity_under_10000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/core-cpi-mom-october-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.49999999999999906} |
| 24h成交量 / 流动性 USD | [802.37, 21915.9234] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:14:13.937325Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will Core CPI MoM be 0.3% in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1189688 / 5699272 |
| Yes 概率 % | 27.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-6.0, -9.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.999999999999999} |
| 24h成交量 / 流动性 USD | [374.217472, 1489.4671] |
| 价差 pp | 4.00 |
| 到期 | 2026-11-11T04:59:00+00:00 |
| 结算规则摘要 | 按BLS首次发布2026年10月季调核心CPI月环比一位小数恰为0.3%结算；不是超过此值，也非同比或总体CPI。计划11月10日08:30ET；若延期，按规则等至下一次计划发布，仍缺则用最近可用月。 |
| 规则指纹 | d590364746a9b5934e2a977dbef3e79e36f630c91f1b4964443a078174d83e57 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:21.229954+00:00 |
| 来源 | https://polymarket.com/event/core-cpi-mom-october-2026 |

## Oracle downgraded to junk by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219847 / 5939428 |
| Yes 概率 % | 8.85 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.35, -8.65] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.3500000000000003} |
| 24h成交量 / 流动性 USD | [null, 615.02009] |
| 价差 pp | 13.30 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。 |
| 规则指纹 | cb29bc6ea2fb2a6cd1d97dc489f0163f0b47e0cb2d31a9cbb3fe5dda90eb10c4 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:00.941593+00:00 |
| 来源 | https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by |

## Military action against Saudi Oil Pipeline (East-West) by November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401796 |
| Yes 概率 % | 81.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [48.0, 42.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 50.0} |
| 24h成交量 / 流动性 USD | [17479.617412, 45746.193] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-30T20:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。 |
| 规则指纹 | de6f019a1972387984a02c6a8e7cef39e331ff99c1895cf1bba902450d550441 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:00.953139+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 96.80 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [9.7, 4.75] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 9.599999999999998} |
| 24h成交量 / 流动性 USD | [144651.280194, 60318.48327] |
| 价差 pp | 1.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:03.794892+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 18.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 6.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1.41, 1798.8632] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:03.311716+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## Will Texas enact a data center moratorium by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123855 |
| Yes 概率 % | 1.80 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.1, -0.4] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.10000000000000009} |
| 24h成交量 / 流动性 USD | [604.67, 50035.49208] |
| 价差 pp | 0.40 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | b3e9528c7bb241316ba9beb5332075225a4976826229cd820fec02a115957e3a |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:04.395652+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Will Texas enact a data center moratorium by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123856 |
| Yes 概率 % | 17.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [77.99, 33234.5102] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | bad230b7f527696e74d48176c1f04e0fa6e22d9b444c004e912067120edc074f |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:18:14.359804Z |
| 抓取时间 | 2026-11-09T23:19:04.395652+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Will Nvidia (NVDA) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1308738 / 6639362 |
| Yes 概率 % | 93.70 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.05, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [null, 403.85762] |
| 价差 pp | 10.40 |
| 到期 | 2026-11-17T22:00:00+00:00 |
| 结算规则摘要 | NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。 |
| 规则指纹 | f9c0b1886ab273be18bc170b3841777783b7f9b2cd80b7ff77a9c0d7a9aa7918 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-09T23:02:14.713378Z |
| 抓取时间 | 2026-11-09T23:20:36.234807+00:00 |
| 来源 | https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53 |

## AI 压力：合约、经营与估值分开

第一层：同规则AI泡沫2026报价7.15%、2027年6月22.5%，比晚报7.25%/25.5%下降；严格结算条件不是普通调整概率。H100标准化neocloud指数11月9日3.01美元/GPU小时，8日3.00，未满足≤1连续5日条件，不能以NVDA单日下跌宣布泡沫破裂。第二层：NVDA-4.27%而SMH+5.05%，治理风险与行业需求分化。董事会8日官方公告确认独立调查，表示暂无理由认为国家安全或机密受损并支持管理层；不能等同已经泄密、定罪、离任或订单取消。盘后FBI/拟议诉讼快讯未取得正式调查范围/法院全文，仅列待核验，不倒灌为全天涨跌原因。近期韩国合作是建设计划，不是已兑现收入。MSFT/AMZN上涨，META+5.12%；AMZN、GOOGL靠近日内低点收盘是承接反证。CRWV/NBIS财报须检验资本开支、债务条款、现金回收、交付与电力许可。第三层：本次SEC逐家检查定期披露，复用已核验财务底稿而非编造新基本面；NVDA公司整体五年FCFF、悲观/基准/乐观与反推只是情景，不是客观概率或全归AI。MSFT/AMZN/GOOGL/META完整TTM、租赁、净债务与稀释桥缺失，明确无法出完整估值。价格反弹不自动改善经营假设。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"checked_at": "2026-11-09T23:20:16.357290+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 178.67 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.24038408973004166, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -44.72 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -13.74 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 35.77 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"checked_at": "2026-11-09T23:20:18.802571+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-09T23:20:21.240552+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"checked_at": "2026-11-09T23:20:23.701960+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"checked_at": "2026-11-09T23:20:26.012432+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 沿用底稿的历史核验说明（其中“本次”指原核验日）；本轮最新定期财报列表检查见disclosure_check。22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基反弹的次日承接

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | CPI与波动回落后的再定价 |
| 关联标的 | ["SPY", "QQQ", "RSP", "IWM"] |
| 确认条件 | SPY742.21–741.09、QQQ664.52–662.02回踩承接，RSP守217.67；随后突破SPY755.42、QQQ约682（日内高点供应商681.695–682.48有差异）且收盘保持；QQQ站稳动态200日线约680.09，再看SPY20日线762.09。 |
| 失效条件 | CPI后跌破上述支撑且反抽失败先下调；进一步失守SPY734.58、QQQ654会否定大部分修复。VIX重返25.64加强风险。 |
| 观察期限 | 11月10日CPI至11日收盘 |
| 反证 | 首日普涨支持修复，但缺可靠VWAP及完整成分广度；不能假定盘中每次回踩都有效。 |
| 状态 | 首次收盘确认，等次日保持 |

## 半导体可观察，NVDA需单独验证

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 行业修复、治理进展、算力财报 |
| 关联标的 | ["SMH", "NVDA", "MU", "SNDK"] |
| 确认条件 | SMH守476.25旧突破区，再突破490.47并收盘保持；MU守724.80后观察200日线758.20。NVDA至少收复185.22，进一步194.90且相对SMH不再恶化才升级。 |
| 失效条件 | SMH跌回476.25且反抽失败下调，462.88再破升级警惕；NVDA170.24再破且治理风险扩散单独处理。 |
| 观察期限 | 未来1–3交易日及17日财报 |
| 反证 | SMH5日仍跌4.11%，NVDA是明显弱项；芯片反弹不是全产业基本面反转。 |
| 状态 | 行业改善、单股风险保留 |

## 优先观察持续强度而非单日涨幅

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | CPI、利率、政策与盈利 |
| 关联标的 | ["MSFT", "XLF", "XLV", "XLC", "XLI"] |
| 确认条件 | MSFT守538.70并突破548.28后承接；XLF守57.255再试58.26/59.20；XLV守近期低点并保持5/20日相对强度；XLI站稳约169.18动态50日线。 |
| 失效条件 | 强势板块回踩失败且相对SPY转弱，或只剩少数权重拉升；日内高点不是自动买点。 |
| 观察期限 | 11月10–13日 |
| 反证 | 金融/医疗当日落后SPY，AMZN与GOOGL收盘承接弱；不能把所有云端等同强势。 |
| 状态 | 观察确认后逐步参与 |

## AI融资改善必须核验现金

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | CRWV/NBIS/NVDA财报及许可披露 |
| 关联标的 | ["CRWV", "NBIS", "NVDA", "MSFT", "AMZN", "META", "GOOGL"] |
| 确认条件 | 投产按时、资金条款可落实、客户现金回收与利润匹配，相关股财报后守住低点且次日不回吐。 |
| 失效条件 | 新增延期、融资缺口/信用走阔与价格转弱共振；EPS达标不能掩盖指引恶化。 |
| 观察期限 | 11月10–17日及财报后1–3日 |
| 反证 | H100报价仍有韧性，不能先假定需求塌陷。 |
| 状态 | 等待财报证据 |

## 航天财报后验证订单质量

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | RKLB盘后已公布的新业绩 |
| 关联标的 | ["RKLB", "ARKX"] |
| 确认条件 | 核验收入、毛利和经营现金流指引，再看财报后开盘区间及收盘能否保持；不以积压订单总额代替利润。 |
| 失效条件 | 利好后跌破开盘低点且反抽失败，或交付/毛利/现金指引恶化。 |
| 观察期限 | 财报后两个交易日 |
| 反证 | 盘后消息不是盘前价格原因，薄盘和高波动使跳空不可靠。 |
| 状态 | 已发布业绩，等待价格消化 |

## 跨期比较与上期剧本复核

对照11月9日晚报：SPY742.21、QQQ664.52、SMH476.25的突破与收盘条件均已达成，RSP收复原观察区，不能继续写成盘前等待；但逐笔回踩/VWAP没有可靠证据，次日保持尚未发生。NVDA185.22预警从盘前转为常规收盘失守，仍未收复194.90；MU收复旧724.80条件，尚未站上200日线约758.20。风险由脆弱修复升级初步确认，不把两个不同资产的证据混成全行业反转。CNN由盘前25升32；VIX期限关系恢复正向。RKLB财报已发布，从将要发生转入盘后增量，活跃EPS合约未再搜到，不伪造结算结果。同规则事件较晚报：2176270 +1.00个百分点；3215008 +3.00个百分点；691340 -0.10个百分点；4838928 -3.00个百分点；2252540 +0.50个百分点；2413330 +9.60个百分点；2745561 +0.00个百分点；5401796 +50.00个百分点；5939428 -0.35个百分点；5123855 -0.10个百分点；5123856 +0.00个百分点；6639362 +0.00个百分点；5699271 +6.00个百分点；5699272 -5.00个百分点；6831494 +1.00个百分点。宽价差变化只作观察。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-06/20261109T120751.728794Z/evidence.json",
    "baseline_cutoff": "2026-11-09T12:07:32.565388+00:00",
    "close_change_pct": {
      "SPY": 2.366416642960889,
      "QQQ": 3.543667255777039,
      "IWM": 3.230166223609632,
      "RSP": 2.2679906629348823,
      "GLD": 1.881780836562763,
      "GC=F": 1.7865541415355457,
      "CL=F": -5.042388790846408,
      "BZ=F": -6.275425333702589,
      "TLT": 0.048829243678505385,
      "UUP": -0.5492614212897151,
      "HYG": 0.36255181552020677,
      "LQD": 0.1339322599094528,
      "^VIX": -22.30889020872524,
      "^VIX3M": -15.243902202638726,
      "^VVIX": -19.27997512344428,
      "^MOVE": -7.315073939008753,
      "NVDA": -4.270253561276616,
      "MSFT": 2.745897688782706,
      "AMZN": 2.9425396228342615,
      "GOOGL": 1.1833679091343807,
      "META": 5.116769557307821,
      "CRWV": 5.560340369640859,
      "MU": 6.253626726675732,
      "DRAM": 6.337484870827503,
      "VRT": 9.630318577913567,
      "XLK": 3.727084609028508,
      "XLE": 0.5193114254642417,
      "XLF": 1.4520675879467593,
      "XLI": 3.823692930913536,
      "XLV": 1.910172468075233,
      "XLP": 0.8991979819370943,
      "XLY": 2.9171629969050317,
      "XLC": 2.4525237831574564,
      "XLU": 1.5302569697825286,
      "XLRE": 1.4545440673828125,
      "XLB": 1.9056743969786183,
      "SMH": 5.054317751297255,
      "IGV": 2.609225225241918,
      "XOP": 0.21867388771403817,
      "OIH": 1.243855889849832,
      "ITA": 3.8996733561935004,
      "ARKX": 5.665026762946823,
      "KRE": 1.7313020122370348,
      "SKYY": 2.9088493372455115
    },
    "quote_change_pct": {
      "SPY": {
        "change_pct": 1.8584848280056798,
        "from_observed_at": "2026-11-09T12:00:59+00:00",
        "to_observed_at": "2026-11-09T23:15:29+00:00"
      },
      "QQQ": {
        "change_pct": 3.1592198258864723,
        "from_observed_at": "2026-11-09T12:01:00+00:00",
        "to_observed_at": "2026-11-09T23:18:48+00:00"
      },
      "SMH": {
        "change_pct": 5.668208742271608,
        "from_observed_at": "2026-11-09T12:00:55+00:00",
        "to_observed_at": "2026-11-09T23:12:21+00:00"
      },
      "NVDA": {
        "change_pct": 1.2792936094064844,
        "from_observed_at": "2026-11-09T12:01:01+00:00",
        "to_observed_at": "2026-11-09T23:18:58+00:00"
      },
      "MSFT": {
        "change_pct": 0.833861505418998,
        "from_observed_at": "2026-11-09T12:01:02+00:00",
        "to_observed_at": "2026-11-09T23:16:51+00:00"
      },
      "AMZN": {
        "change_pct": 0.5961615027078704,
        "from_observed_at": "2026-11-09T12:00:42+00:00",
        "to_observed_at": "2026-11-09T23:18:53+00:00"
      },
      "GOOGL": {
        "change_pct": 0.09892762318541859,
        "from_observed_at": "2026-11-09T12:01:01+00:00",
        "to_observed_at": "2026-11-09T23:18:50+00:00"
      },
      "META": {
        "change_pct": 3.353541185527331,
        "from_observed_at": "2026-11-09T12:00:51+00:00",
        "to_observed_at": "2026-11-09T23:18:49+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.04999999999999982,
        "unit": "percent",
        "observation_date": "2026-11-06"
      },
      "BAMLH0A0HYM2": {
        "change": -0.06000000000000005,
        "unit": "percentage_points",
        "observation_date": "2026-11-06"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-06"
      },
      "DGS10": {
        "change": 0.020000000000000462,
        "unit": "percent",
        "observation_date": "2026-11-06"
      },
      "DFII10": {
        "change": 0.029999999999999805,
        "unit": "percent",
        "observation_date": "2026-11-06"
      },
      "T10YIE": {
        "change": -0.009999999999999787,
        "unit": "percent",
        "observation_date": "2026-11-09"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-30"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-11-06"
      },
      "GPRD": {
        "change": 16.277969360351562,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_ACT": {
        "change": 16.227874755859375,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_THREAT": {
        "change": 13.53564453125,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_MA7": {
        "change": 21.203353881835938,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_MA30": {
        "change": 20.7001953125,
        "unit": "index",
        "observation_date": "2026-11-02"
      }
    },
    "event_probability_change": {
      "2176270": {
        "status": "comparable",
        "change_pp": 0.9999999999999996
      },
      "6882826": {
        "status": "definition_changed_or_unknown",
        "change_pp": null
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 3.0000000000000027
      },
      "6831494": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.10000000000000009
      },
      "4838928": {
        "status": "comparable",
        "change_pp": -3.0
      },
      "5699271": {
        "status": "comparable",
        "change_pp": 6.000000000000005
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.49999999999999906
      },
      "5699272": {
        "status": "comparable",
        "change_pp": -4.999999999999999
      },
      "5939428": {
        "status": "comparable",
        "change_pp": -0.3500000000000003
      },
      "5401796": {
        "status": "comparable",
        "change_pp": 50.0
      },
      "2413330": {
        "status": "comparable",
        "change_pp": 9.599999999999998
      },
      "2745561": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5123855": {
        "status": "comparable",
        "change_pp": -0.10000000000000009
      },
      "5123856": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "6639362": {
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
    "event": "10月CPI/实际工资；北京10日21:30，tc缓存12日错误",
    "date": "2026-11-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "CoreWeave Q3电话会；北京11日06:00，tc缓存12日错误",
    "date": "2026-11-10T17:00:00-05:00",
    "source": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx"
  },
  {
    "event": "Nebius Q3：官方11月12日美股开盘前，发布时间分钟未核验",
    "date": null,
    "source": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call"
  },
  {
    "event": "10月PPI；北京13日21:30",
    "date": "2026-11-13T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA Q3预计业绩16:20ET、电话会17:00ET；北京时间次日",
    "date": "2026-11-17T16:20:00-05:00",
    "source": "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873"
  },
  {
    "event": "11月26日感恩节休市、27日股票13:00EST半日市；11日股票正常交易",
    "date": null,
    "source": "https://www.nyse.com/markets/hours-calendars"
  },
  {
    "event": "Nebius Q3电话会；北京12日21:00，业绩为此前盘前披露",
    "date": "2026-11-12T08:00:00-05:00",
    "source": "https://assets.nebius.com/assets/7a58f9de-6a9b-4124-b71e-db5185af68df/30102026%20Nebius%20Group%20announces%20date%20of%20third%20quarter%202026%20results%20and%20conference%20call.pdf"
  },
  {
    "event": "盘后已发生：RKLB Q3官方业绩发布，已移出未来事件；北京时间10日05:05",
    "date": "2026-11-09T16:05:00-05:00",
    "source": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-third-quarter-2026-financial-results-posts"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| nvda-governance | 董事会独立调查仍在，无正式结论；不将盘后FBI/诉讼快讯当已定罪。 | 缺失 | [{"source": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors", "published_at": null, "retrieved_at": "2026-11-09T23:23:52.619808+00:00"}] |
| broad-rally | 公开收盘报道确认普涨与油价回落，NVDA独立走弱；原因解释是推断。 | 缺失 | [{"source": "https://apnews.com/article/d938f8e6ff42b3706e1d36e6245ec56b", "published_at": null, "retrieved_at": "2026-11-09T23:23:52.619808+00:00"}] |
| rklb-results | 盘后新增：纪录营收2.68亿美元、积压35.7亿美元，经营现金流为正，Q4指引增长；不把订单直接等同利润。 | 2026-11-09T16:05:00-05:00 | [{"source": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-third-quarter-2026-financial-results-posts", "published_at": "2026-11-09T16:05:00-05:00", "retrieved_at": "2026-11-09T23:23:52.619808+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "tc报价时间为请求时间，不当成交时间；独立Yahoo分钟timestamp核验盘后，原包保留。",
  "总新闻50条与AI补查50条均截断，按事件去重，覆盖非全市场。",
  "缺可靠常规VWAP/开盘回踩序列与全市场成分广度；tc/Yahoo部分日内高低/成交量有差异，QQQ高点用约682区间而非精确触发。",
  "期货已经进入新交易时段，Yahoo连续日线可能含新时段，不把最新值当周一正式结算，不将换月回报作纯现货回报。",
  "当期ETF净申赎和机构持仓缺失；ICI滞后窗口仅背景，价格量能不是主力净流入。",
  "CME动态概率未核验；CNN API418由浏览器补核。",
  "FRED信用/实际利率截至6日，CBOE CSV仅截至6日，最新VIX等采用Yahoo同日序列；GPR截至2日。",
  "四家完整DCF仍缺，NVDA仅复用已核验公司整体假设；未把调查机械改成经营下修。",
  "RKLB活跃合约不见不能冒充已正式结算；未核验其盘后报价与一致预期差异。",
  "Gamma搜索截断/一次超时、Oracle/NVDA/CPI部分宽价差，低量合约不当独立强信号。",
  "DRAM不足200日历史，缺盈利一致预期修正；地区袭击细节和NVDA盘后法律线索仍待官方核验。",
  "历史来源保留旧核验时间，本次重查才追加记录。",
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
    "url": "https://www.bls.gov/news.release/empsit.nr0.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.sca.isr.umich.edu/",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526450754/d44678d424b5.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1878848/000187884826000065/irenreportsq1-fy27result.htm",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.investing.com/news/stock-market-news/microsoft-is-winding-down-oracle-deal-to-rent-ai-cloud-capacity-bloomberg-news-reports-5008946",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://apnews.com/article/bc902d3400cb5d022f8bafd247ef975b",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.bea.gov/news/schedule",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.nyse.com/markets/hours-calendars",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://apnews.com/article/4ac9a6a3c35aeec37374fc8083bf9395",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-08T02:04:12.815853+00:00",
    "note": "历史底稿来源（保留原核验时间）；本次核验；新闻保留归属及限制，Nebius另核官方10月30日PDF"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ARM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QCOM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CI",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COIN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SO",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COHR",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TAN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ILMN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COP",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CRWV",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GDX",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LITE",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MRVL",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-11-08T02:00:00.831098+00:00",
    "note": "历史底稿来源（保留原核验时间）；11月6日常规时间戳，非周末新成交"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-11-08T02:00:50.879922+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-11-08T02:00:53.682582+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-11-08T02:00:56.065684+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-11-08T02:00:58.942985+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-11-08T02:01:01.304983+00:00",
    "note": "历史底稿来源（保留原核验时间）；最新定期财报列表；非全面8K检查"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-08T02:05:37.724337+00:00",
    "note": "历史底稿来源（保留原核验时间）；浏览器只读官方页面22，更新11月6日18:59:54EST"
  },
  {
    "url": "https://assets.nebius.com/assets/7a58f9de-6a9b-4124-b71e-db5185af68df/30102026%20Nebius%20Group%20announces%20date%20of%20third%20quarter%202026%20results%20and%20conference%20call.pdf",
    "checked_at": "2026-11-08T02:05:37.724337+00:00",
    "note": "历史底稿来源（保留原核验时间）；公司10月30日PDF确认11月12日盘前业绩、08:00EST电话会；网页正文缺失，以PDF为准"
  },
  {
    "url": "https://au.investing.com/news/stock-market-news/coreweave-seeks-truce-with-texas-governorelect-hinojosa-4753439",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；媒体报道CoreWeave寻求与得州候任政府合作，尚无完整信件和监管回复，不能认定项目放行。"
  },
  {
    "url": "https://stopdirtydatacentres.eu/",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；行动组织官网列6–7日活动并要求暂停大规模数据中心；这是组织诉求，不是政府禁令。"
  },
  {
    "url": "https://www.ukmto.org/-/media/ukmto/products/20261107-ukmto_advisory-198-26.pdf",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；UKMTO198-26收到阿曼湾散货船与军队事件报告；船员、损害和环境影响未知，不能据此确认两艘油轮触雷。"
  },
  {
    "url": "https://berkshirehathaway.com/news/nov0726.pdf",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；7日官方Q3经营利润127.05亿美元低于上年134.85亿，同时本季回购约96亿美元；不把回购当全市场底部信号。"
  },
  {
    "url": "https://www.wam.ae/en/article/c2o8dle-uae-national-guard-rescues-people-after-oil-tanker",
    "checked_at": "2026-11-08T02:17:05.773028+00:00",
    "note": "历史底稿来源（保留原核验时间）；官方22人救援资料明确10月10日，不能核验11月8日新快讯；不认定为同一事件"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "董事会宣布独立调查，未确认机密受损；不把调查当定罪、离任或订单取消。"
  },
  {
    "url": "https://www.rba.gov.au/speeches/2026/sp-ag-2026-11-09.html",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "Hunter官方讲话讨论AI投资回报不足的资产重估风险，短期需求推动通胀；这是条件风险框架，不是Fed政策或崩溃预测。"
  },
  {
    "url": "https://www.al-monitor.com/originals/2026/11/production-suspended-iraqs-khor-mor-gas-field-after-drone-attack-sources-say",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "Reuters据安全消息源报道Khor Mor气田遭无人机袭击后停产，运营方恢复时点/持续损失未确认。"
  },
  {
    "url": "https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "NASA公告八家可竞争未来月球配送任务，十年总框架上限100亿美元，不等于已获全部订单。"
  },
  {
    "url": "https://www.forth.news/lists/centcom/Cgoet5KhSp6nWZnwnUeuR",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "CENTCOM新闻稿转载称设立Tampa协调小组，处理陆路/里海武器等运输；不是已证实所有能源陆路被物理封闭。"
  },
  {
    "url": "https://www.bls.gov/news.release/empsit.nr0.htm",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "BLS10月就业新增16.5万，失业率4.1%；民间预期分歧不采用单一未经核验值。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本次重查仍截至10月28日的净发行；不是本周资金"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "8日3.00、7日3.04、6日2.99美元/GPU小时"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本次查发行人，尚未取得完整份额/NAV/拆分桥"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本次官方页只有动态工具入口，无法核验78%快讯数值"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "浏览器重新核验22，11月6日18:59:54EST"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://www.nyse.com/markets/hours-calendars",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://assets.nebius.com/assets/7a58f9de-6a9b-4124-b71e-db5185af68df/30102026%20Nebius%20Group%20announces%20date%20of%20third%20quarter%202026%20results%20and%20conference%20call.pdf",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-date-third-quarter-2026-financial-results",
    "checked_at": "2026-11-08T23:21:08.298739+00:00",
    "note": "本轮核验官方日历；交易休市以本轮tc日历为准"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873",
    "checked_at": "2026-11-08T23:22:07.360445+00:00",
    "note": "再次核对约13:20太平洋时间业绩公布、14:00电话会；换算16:20/17:00EST"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "董事会独立调查、目前未认定安全或机密受损；不等于离任/订单取消。"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/nvidia-rebellions-and-sk-telecom-announce-collaboration-to-advance-sovereign-ai-infrastructure-with-nvidia-nvlink-fusion",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "NVIDIA/Rebellions/SK Telecom宣布NVLink Fusion合作；计划部署不是已兑现收入。"
  },
  {
    "url": "https://chinaselectcommittee.house.gov/sites/evo-subsites/selectcommitteeontheccp.house.gov/files/evo-media-document/nvidia-letter-pdf.pdf",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "11月4日信函请求18日闭门简报，11日前回复或提出替代日期；非确认日程或传票。"
  },
  {
    "url": "https://apnews.com/article/f7b507b55634985d6013d36265b3fbc0",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "AP报道外交接触尚无突破、特朗普有条件不新增打击；未宣布全面停火。"
  },
  {
    "url": "https://apnews.com/article/3345b9f05c54d58909e88f6dcb9c1cd8",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "AP报道中方否认相关指控；否认与调查分别呈现，不直接认定任何一方指控已证实。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "本次核验仍截至10月28日"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "截至6日NAV464.02，NVDA权重20.75%；缺份额桥"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "截至8日3.00"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "9日06:45:01EST值25"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "动态概率未获取，不引用快讯81%为官方核验"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "CPI10日、PPI13日08:30EST"
  },
  {
    "url": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-date-third-quarter-2026-financial-results",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "9日盘后，电话会17EST"
  },
  {
    "url": "https://investors.coreweave.com/events-and-presentations/event-details/2026/CoreWeave-Third-Quarter-2026-Earnings-Call/default.aspx",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "10日17EST"
  },
  {
    "url": "https://nebius.com/newsroom/nebius-group-announces-date-of-third-quarter-2026-results-and-conference-call",
    "checked_at": "2026-11-09T12:07:25.694612+00:00",
    "note": "12日盘前，电话会08EST"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "董事会独立调查仍在，无正式结论；不将盘后FBI/诉讼快讯当已定罪。"
  },
  {
    "url": "https://apnews.com/article/d938f8e6ff42b3706e1d36e6245ec56b",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "公开收盘报道确认普涨与油价回落，NVDA独立走弱；原因解释是推断。"
  },
  {
    "url": "https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-announces-third-quarter-2026-financial-results-posts",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "盘后新增：纪录营收2.68亿美元、积压35.7亿美元，经营现金流为正，Q4指引增长；不把订单直接等同利润。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "官方CPI10日、PPI13日08:30EST"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "仍为10月28日窗口"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "9日3.01，采用有日期表格不采用陈旧FAQ"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "浏览器32/Fear，9日18:03:38EST"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "发行人仍截至6日，缺份额序列"
  },
  {
    "url": "https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Date-of-Third-Quarter-2026-Financial-Results-and-Conference-Call/default.aspx",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "10日17EST电话会"
  },
  {
    "url": "https://nebius.com/investor-events",
    "checked_at": "2026-11-09T23:23:52.619808+00:00",
    "note": "12日08EST电话会"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
