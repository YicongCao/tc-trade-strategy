# 每日交易总结 · 2026-10-26

## 一分钟读懂 · Agent 摘要

### 当前判断

反弹比昨晚盘前更可信：SPY、QQQ、SMH均收在此前确认位之上，但仍未回到20日均线，先按修复行情管理。

### 与上次相比

昨晚的“等待开盘”已变为首个收盘确认；Meta却由盘前上涨转为收跌。Anthropic公开S-1已核验，Broadcom盘后公布630亿美元算力融资安排。

### 最重要的信号

- QQQ收712.20（+1.11%）、SMH541.62（+2.74%）；SPY765.37（+0.71%），等权RSP只涨0.35%。
- SMH量能为前20日均量1.21倍，QQQ仅0.89倍；VIX降至18.39，短期压力缓和。
- NVDA/MSFT上涨，META/GOOGL下跌；融资和订单能支持投入，却不能替代自由现金流。

### 接下来观察

- 下一交易日先看QQQ709.30、SMH533.34、SPY763.47是否回踩守住；跌回且反抽失败则降级。
- 软件/云优先看延续，芯片看承接；能源仍强但事件风险高，不追单日涨幅。
- 27日STX、28日Fed/微软、29日GDP/PCE与Amazon/Sandisk是下一轮检验。

### 不要忽略

未核验完整成分广度及逐笔VWAP；信用数据滞后、CNN与当期申赎缺失。盘后薄量报价不替代收盘，融资安排不等于回报已兑现。

## 研究结论

10月27日早报：反弹取得第一层收盘确认，仍是分化修复，尚未确认趋势反转。半导体带头、软件/云保持跨周强势，Meta与Google走弱；AI融资窗口打开与资本回报压力同时存在。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-26 → 2026-10-26（纽约交易日） |
| 截止·纽约 | 2026-10-26T19:23:08.626160-04:00 |
| 截止·北京 | 2026-10-27T07:23:08.626160+08:00 |
| 实际生成时间 | 2026-10-26T23:23:08.814647+00:00 |
| 市场阶段 | 盘后 |
| 下一交易日 | 2026-10-27 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-23/20261026T120957.233325Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-27T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-26T23:17:59.559528+00:00 / 2026-10-26T23:17:59.559528+00:00 | Gamma retrieval snapshot; not last trade timestamp; reviewed settlement |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-10-26T23:18:02.448097+00:00 / 2026-10-26T23:18:02.448097+00:00 | Gamma retrieval snapshot; not last trade timestamp; reviewed settlement |

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
| prices.SPY.value | 765.37 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 0.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -0.03 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 2.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.14 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.72 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 724.41 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.62 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -0.18 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 5.65 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.25 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.95 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -1.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 712.20 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 1.11 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -0.86 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -3.30 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 3.63 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.40 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -0.71 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -3.27 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | 0.92 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 734.02 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 725.08 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 676.57 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -2.97 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -1.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 5.27 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 12.36 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.73 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -6.25 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.89 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 276.99 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 2.10 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -1.08 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -4.63 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.26 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 2.25 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -1.05 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -7.34 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.04 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 285.54 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.27 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -0.02 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -3.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -0.10 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.63 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.31 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -8.97 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.60 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 217.29 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 0.35 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 1.82 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 3.60 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 1.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.36 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 1.97 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 3.63 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -1.27 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 213.04 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.85 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.07 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.99 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.07 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.95 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -2.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.88 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 367.82 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 0.33 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -3.13 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -2.67 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -1.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.38 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -2.98 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -2.64 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -3.71 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 378.59 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 393.83 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 413.99 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -2.84 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -6.60 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -11.15 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.31 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -14.07 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,024.50 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 0.41 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -3.26 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -3.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -2.01 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.30 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -3.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -3.42 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -4.72 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,148.07 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,333.61 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,530.72 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -2.98 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.13 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -11.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 67.84 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.33 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.01 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 101.32 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -1.89 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -2.26 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 9.42 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 19.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -2.60 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -2.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 9.45 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 16.96 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 95.16 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 93.31 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.50 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 6.47 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 8.59 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 18.50 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.30 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.24 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -4.26 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 110.14 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -5.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 0.54 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 4.62 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 22.21 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -6.35 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 0.68 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 4.65 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 19.51 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 106.11 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 101.26 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 91.41 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 3.80 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 8.77 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 20.48 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 4.15 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.77 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -5.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.68 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.42 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 2.79 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 4.31 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | 0.49 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -0.29 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 2.94 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 4.34 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -2.22 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 78.89 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.27 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.30 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 3.53 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.94 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.83 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.02 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.37 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.49 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.01 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.03 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.08 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 2.98 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -0.54 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.18 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 1.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 0.27 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.96 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.50 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.89 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.18 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.01 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.12 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.41 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.41 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.57 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.20 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.19 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.48 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.43 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.52 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.63 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 0.04 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -4.14 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.03 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.91 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.22 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.89 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.28 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.36 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.65 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.02 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.16 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 1.11 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.95 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.84 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.55 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 1.25 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 1.98 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -3.55 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.73 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.85 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.90 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.25 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.77 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.64 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.61 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.83 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.69 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 18.39 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -5.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -0.27 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 14.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 15.95 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -6.16 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -0.13 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 14.47 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 14.68 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.65 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.00 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.23 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 10.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 14.94 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 0.90 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.00 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 10.85 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -8.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-26 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 19.94 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -2.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 1.73 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 9.38 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 4.84 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -3.35 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 1.88 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 9.41 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 2.13 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.69 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.52 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.49 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 6.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 7.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -2.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.13 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 5.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -7.26 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-26 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 101.43 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -7.54 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -5.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 11.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 10.68 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -8.25 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -5.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 11.47 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 7.97 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 93.40 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 90.86 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.74 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 8.60 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 11.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 2.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 9.91 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 9.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -7.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-26 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 102.19 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -1.08 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 0.88 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | 6.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 32.56 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -1.79 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 1.02 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 7.22 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 29.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 103.49 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 88.46 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 76.87 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -1.26 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 15.53 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 32.94 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.32 | index | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.20 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -10.04 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-26 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 216.00 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | 2.39 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -0.50 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -5.62 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 7.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | 1.68 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -0.36 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -5.59 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | 5.01 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 224.90 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.22 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.52 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -3.96 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -2.80 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 6.13 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.14 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.84 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -9.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.86 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 532.60 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 1.54 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -0.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 4.59 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 14.82 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.83 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -0.03 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 4.62 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 12.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 527.87 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 509.12 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 435.66 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 0.90 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 4.61 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 22.25 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.12 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -2.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 249.09 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 0.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -5.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 1.19 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -8.28 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -0.27 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -4.95 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 1.23 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -10.99 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.58 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 255.38 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.31 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -2.16 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -2.46 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 2.38 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 6.94 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.79 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -12.30 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 316.80 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -1.06 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -7.96 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -7.57 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -10.99 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -1.78 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -7.81 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -7.54 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -13.70 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 341.79 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 342.30 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.95 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -7.31 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -7.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -7.08 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.42 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -16.06 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.01 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 630.56 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -1.88 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -10.61 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -11.89 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 13.35 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -2.59 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -10.47 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -11.85 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 10.65 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 713.40 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 664.40 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.59 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -11.61 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -5.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -0.16 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 25.92 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 4.11 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -18.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.60 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 55.19 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 1.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -9.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -35.12 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -23.10 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 1.05 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -9.56 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -35.09 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -25.81 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 74.37 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 82.27 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 91.89 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -25.79 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -32.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -39.94 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.50 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 11.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -48.77 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.32 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 903.70 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 2.98 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -0.13 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -14.24 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 9.82 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 2.27 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 0.01 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -14.21 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 7.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 979.09 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 981.24 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 734.78 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -7.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -7.90 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 22.99 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 50.97 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -17.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 48.33 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 2.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 0.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -19.05 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -4.05 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 1.99 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 0.14 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -19.01 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -6.76 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 54.03 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 56.44 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-26 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -10.54 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -14.37 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-26 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.70 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 5.60 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -24.03 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.65 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 199.78 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 2.81 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -3.06 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -18.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -17.28 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 2.10 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -2.91 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -18.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -19.99 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 227.99 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 245.79 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 269.17 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -12.37 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -18.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -25.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 11.83 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.92 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -31.99 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.99 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 186.32 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 1.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | 0.19 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -4.22 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 6.38 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 0.98 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | 0.34 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -4.19 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 3.67 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 192.82 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.46 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 168.40 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -3.37 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -1.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 10.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.24 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.28 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -7.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.83 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 69.64 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 0.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 2.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 12.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 17.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -0.26 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 2.86 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 12.17 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 14.93 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 65.78 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.31 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 57.70 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 5.87 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 8.29 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 20.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.48 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.12 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 56.02 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 0.21 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 1.74 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 3.38 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -1.27 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.50 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 1.89 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 3.41 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -3.98 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 54.78 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.94 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.36 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.27 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 0.15 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 4.98 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.72 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.28 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -4.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.63 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 166.96 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 1.42 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 0.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -1.08 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -6.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.71 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 0.31 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -1.05 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -9.62 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.12 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 171.62 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.45 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -0.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -2.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -3.18 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.71 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.62 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -10.24 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.87 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 179.28 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 0.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.07 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 4.68 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 10.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.71 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 2.21 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 4.71 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 8.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 172.88 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 171.04 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.14 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 4.82 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 14.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.10 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.73 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -1.11 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 87.96 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -0.34 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 0.86 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 6.90 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 4.10 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -1.05 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 1.00 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 6.93 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 1.39 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 84.60 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.15 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.40 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 3.98 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 4.53 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 5.46 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.38 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.57 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -2.26 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 114.26 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 1.03 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | -0.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 4.83 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -1.36 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.32 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | -0.03 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 4.86 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -4.07 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 112.24 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.24 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.31 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 1.80 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 0.90 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | -0.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.63 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.42 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -4.46 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.94 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 103.85 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.57 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -5.67 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -6.59 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -3.74 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -2.28 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -5.52 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -6.56 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -6.45 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 110.15 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 111.24 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.63 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -5.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -6.65 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -7.80 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.76 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -9.50 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.43 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.55 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.02 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 2.88 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 8.41 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -3.35 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -0.73 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 3.02 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 8.44 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -6.06 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 41.29 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.68 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.78 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 3.06 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 2.08 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -2.81 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.63 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.47 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -4.56 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.39 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.80 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 0.54 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 2.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 3.51 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -4.24 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -0.17 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 2.86 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 3.54 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -6.95 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.60 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.65 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.71 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.89 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 0.35 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 0.20 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.64 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.50 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -6.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.15 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.38 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 0.84 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 3.86 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 2.35 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -0.57 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 0.99 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 3.89 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -0.36 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 50.01 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.88 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.64 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 2.73 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 0.99 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 1.46 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.66 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.28 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -3.83 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 541.62 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 2.74 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -1.25 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -9.73 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | 0.20 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 2.02 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -1.10 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -9.70 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -2.51 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 582.63 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 574.17 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 516.25 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -7.04 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -5.67 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 4.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 19.10 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.53 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -14.56 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 111.39 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 0.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | 5.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | 5.65 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 17.77 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 0.01 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | 5.24 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | 5.68 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 15.06 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.88 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.45 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.85 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | 2.30 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 4.64 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 18.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.88 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.59 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -1.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 0.73 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 204.86 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 1.57 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 2.70 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 13.72 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 15.94 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 0.86 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 2.85 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 13.75 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 13.23 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 193.28 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.10 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 168.10 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 5.99 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 7.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 21.87 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 5.07 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.48 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.87 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 402.40 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 1.27 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 4.49 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | 3.24 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 4.57 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 0.56 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 4.63 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 3.27 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 1.86 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 386.30 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 402.04 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 395.84 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 4.17 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | 0.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | 1.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.70 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -7.83 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.80 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 207.16 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 2.44 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | -0.29 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -1.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -13.46 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 1.73 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | -0.14 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -0.97 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -16.17 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.33 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 217.59 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 229.12 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 0.40 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -4.79 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -9.58 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.22 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.04 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -18.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.15 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.17 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 1.11 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 0.47 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -5.92 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -1.41 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 0.40 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 0.61 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -5.89 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -4.11 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.30 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 32.02 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.55 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -3.60 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -5.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -7.32 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.77 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.54 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -13.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.51 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.73 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 0.37 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 5.01 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 3.09 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -3.83 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.34 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 5.15 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 3.12 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -6.54 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.14 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 72.06 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.21 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 3.69 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.93 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.59 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.28 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.14 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 169.86 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 1.49 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 5.45 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | 4.55 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 18.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 0.78 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 5.60 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | 4.59 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 16.07 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 167.21 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.26 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 135.73 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | 1.58 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 3.41 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 25.15 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.78 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.81 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -2.88 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.64 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.69 | percent | 2026-10-23 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.38 | percentage_points | 2026-10-23 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.91 | percentage_points | 2026-10-23 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.00 | percent | 2026-10-23 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.66 | percent | 2026-10-23 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.34 | percent | 2026-10-26 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.63 | index | 2026-10-16 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.45 | index | 2026-10-23 | lagged | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 165.25 | index | 2026-10-26 | ok | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 149.77 | index | 2026-10-26 | ok | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 187.38 | index | 2026-10-26 | ok | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 181.42 | index | 2026-10-26 | ok | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 175.44 | index | 2026-10-26 | ok | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 764.21 | USD_per_share | 2026-10-26T23:14:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 711.85 | USD_per_share | 2026-10-26T23:17:45+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 542.39 | USD_per_share | 2026-10-26T23:15:37+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.RSP.value | 217.25 | USD_per_share | 2026-10-26T21:48:21+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.META.value | 632.75 | USD_per_share | 2026-10-26T23:14:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MSFT.value | 531.20 | USD_per_share | 2026-10-26T23:17:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 248.90 | USD_per_share | 2026-10-26T23:17:37+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.NVDA.value | 216.02 | USD_per_share | 2026-10-26T23:18:12+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.GOOGL.value | 317.42 | USD_per_share | 2026-10-26T23:18:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 111.90 | USD_per_share | 2026-10-26T22:54:46+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.XLE.value | 69.70 | USD_per_share | 2026-10-26T22:44:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 56.00 | USD_per_share | 2026-10-26T23:03:04+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.IWM.value | 276.42 | USD_per_share | 2026-10-26T23:17:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.GLD.value | 367.82 | USD_per_share | 2026-10-26T23:07:54+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.TLT.value | 81.61 | USD_per_share | 2026-10-26T22:38:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| afterhours.CL_F.value | 101.32 | USD/barrel | 2026-10-26T23:07:37+00:00 | lagged | Yahoo延迟分钟价；期货可能已进入下一交易日夜盘，不作为26日官方结算；连续/近月合约未对齐，不拼接跨来源收益 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| afterhours.BZ_F.value | 110.14 | USD/barrel | 2026-10-26T23:07:50+00:00 | lagged | Yahoo延迟分钟价；期货可能已进入下一交易日夜盘，不作为26日官方结算；连续/近月合约未对齐，不拼接跨来源收益 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| afterhours.ES_F.value | 7,706.00 | index points | 2026-10-26T23:08:16+00:00 | lagged | Yahoo延迟分钟价；期货可能已进入下一交易日夜盘，不作为26日官方结算；连续/近月合约未对齐，不拼接跨来源收益 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| afterhours.NQ_F.value | 29,425.00 | index points | 2026-10-26T23:08:19+00:00 | lagged | Yahoo延迟分钟价；期货可能已进入下一交易日夜盘，不作为26日官方结算；连续/近月合约未对齐，不拼接跨来源收益 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 5.4000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.1099853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2328429532174279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.28736985822350736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.284929115306487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3485647715251736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4439898525543837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8762192722623574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.00961646878929745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2764797893108915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.011999511718727263,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.6944976806640852,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.18093994140622272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5854626464844159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.40601867675786707,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0816229248047193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7027132548577564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05445898492782986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.727690634515088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06849336731247213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6866065804956412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.45814639294228243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.06928798130580383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1800013950892856,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.002385748826393974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.024856071985240757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6931194377956418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.14247202676211934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.04405769803307502,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.14481620053617072,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 7.79998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.15997314453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1172525361088148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.09864957849190503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09673251143592632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.8527509011999186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.0828319766828636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.18655027947145353,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4691736984303585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.470671887891073,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.11559041710861306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3860194367154124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.38166162674241333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.504186129674745,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6388421241284798,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.062769551733811,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.47879016721965595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1941920985801815,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.2165008544922102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.345001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3621801757811909,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.1697094726562227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4691857910155477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3769937133788517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2214228732127408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.13039487443897713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1242464557223775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.689990301380683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0806255738692983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2848229814349077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.299285888671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5978655133928577,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.023276376576319757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.23730983747308754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.026773565636418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.8108855754282667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.07079329527163702,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.13670611784558828,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.239990234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.709991455078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7822100934562592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1390755589488757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.14136716880241984,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.486983339548067,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.123843680079717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.9252842438310513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8779713412301771,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9563511664968063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.4506328597611686,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.14829429927463167,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.14356194650406717,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.1384185680228938,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3201461724746668,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.0490649715686935,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8875878100194745,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.2328309558076986,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.15149993896483238,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.5554992675781136,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.546105346679667,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.5332116699218545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1023011016845885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5944818115234511,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.501985102205027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.607793040851747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6185937858676493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.8351129641953627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.41050789845340496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8491417344258188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.06214250837053559,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.234283447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.028424303094130243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.11392473765251099,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4074957474802119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8764641620467533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.20746510179379596,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.14765262150039904,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.75,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.8899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1162252474448797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6686518501941685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6784904934066915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7243679470107853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0275736221444287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.261151591472866,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5237978940859644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1443030963935952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.11661770577254815,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.38128199197066115,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.39356137810020453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3758031754856117,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.41641623040995457,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3849323192105087,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5334143628752619,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.4207828857044866,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.37749938964844887,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.4664993286132812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09291503906248977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.375851135253896,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11575973510741733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6016119384765659,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17161930625293476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1316341696453014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.39264566283292446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.984003389128497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.30489267367075357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5844974329932704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.015713282993861544,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.04928697858537978,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.010552655453575532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.005748585377757576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3379356485326168,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7527592887098042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1512054686880704,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.154695718972237,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.21002197265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -11.8699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9777574612708562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9373728609602283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9050811151621314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.4825091939122967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 4.142289228829765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0215542563989723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7959877704758043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.0958898268732438,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.2550854919465717,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.650003002736721,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6201519998556444,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.8310739654374704,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.6982993762753815,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.145334984136615,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.8056042392651022,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.8194100375623523,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5044998168945654,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.796501159667969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6732000732421852,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.976600341796882,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.21834991455079944,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9045500183106014,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.448483357103302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.8805955816193487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.46609258304912693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.2907764029525435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.33896406330207185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.6672571912540572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.018216814313616325,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.32678004673549044,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.009732225992782562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.13118136487083554,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2826691783944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.772909784402911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.4606745333469606,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.11046341747432431,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 16.60009765625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -135.60009765625,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7071605298236148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9164445962919765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8829158245618585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.531719912918484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.798145656536434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.6528774750376058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.23996482860202395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.202438700941602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4743175766061869,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6290747380684691,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5979867092553715,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.880284684443658,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3541558039820507,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.776658202775248,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2495812973913214,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.925958911630711,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.194995117187318,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -54.850000000000364,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.255996093749673,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -36.012001953125036,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.1810009765622453,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -9.075002441406468,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5674910186538318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9601625987698879,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5589119035306904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.3378859514234236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.40895279668041695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.8093584909421487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.049979073660722,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.9142892020089306,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.1080319992677845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.03914370498157149,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3533589839159621,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.886459689511401,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.408514620391218,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9082960544319029,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.9499969482421875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.3400039672851562,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.708493859309394,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.106967220298541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.091515300692993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -12.839852199285618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.3351187075350666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.189655618655049,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.8789050974111987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.5969454839943857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -6.941336812526822,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.394337078522048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.376444415999481,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -14.188416970810792,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.7791085600894494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3134363463926917,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.869288628621902,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.873425273305276,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4360000610351591,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8314998626709098,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3783999633789108,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.815000152587885,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2178000068664545,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0823999977111782,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.548561276533224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.5964487019995115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.540538737669575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.71173287570641,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.5890050361277765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.291057104749662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.08357184273855989,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.35999952043805816,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0008285234147455967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.44304389330989347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.8425748034618055,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.2110969732578316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.075102566685501,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3723035008661031,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -6.5800018310546875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.589996337890625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.774300879346452,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.355249309463506,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.7057479555014945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.180612756327549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.270242533505611,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.562537101510532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.887058664675251,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 9.019940720998477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -10.00714383256388,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.6426191676870125,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.9906770708079815,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.529177527852722,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.714232386059994,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.43875637377289,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.877442195885955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 10.296420510309368,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.24300003051757812,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9555000305175696,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.432400054931648,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.328799896240241,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2407499885559048,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.262399997711185,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -6.453756296141422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.3824221726203234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -6.992170713867706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9638476974917172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.53512461494541,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.0326900303305315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.16928591047014496,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.29928588867187456,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.35755993503899086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2528925039125842,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.637424402191971,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.355249309463506,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9621913528624955,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9268981667929596,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.34000396728515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.220001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9073617966838698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1550476992568726,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1823757451565386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9873309943570607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.3509131795581553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.779972647694887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0830603191224752,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.9056072499015326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.325481156533558,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8676778410333652,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8974466298500516,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3612337771681129,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09307667299622757,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.90375337543253,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0926767879117727,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.182087039212424,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.16876831054688068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3581398010253878,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.005619964599603122,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05297653198242358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.013629417419437573,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.0852679061889603,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.20994022729692308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3546064061290117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.41648149928712463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.830965145983033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4241639617419857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7627522592030056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0035716465541294484,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.00019559950559511208,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.00013244488393526765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.028217319970801125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9162637084451641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.174614492372374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.2054884737557504,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.12188552227444471,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.05000114440917969,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.010000228881835938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03495472068848482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.10396901750158172,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.1038256086778988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4807559972740516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.10783678390782203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.7457068500117625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.06789576706769385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5123367641128649,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.2677976739059127,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3913388757250891,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3887547239843858,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.867808774251122,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.5518266364622058,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.62192612227412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0775122358569913,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7888165534237563,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.015499973297121272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0774998664855957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.017999992370608453,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07839996337890653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.008699998855593805,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.04439998626709141,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11910748127881288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.234184942393445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11122249024424491,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.24557141129537552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.14687612109292036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.12993325025782987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.002857072012765069,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.020714351109095974,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.010567017957167246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.0715688909216321,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17164828647342478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.034329657294684957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.07700477468390066,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.06248237687797775,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.149993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.25951575787500625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2337012685214912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2343704675730196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.076736238317233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6045127428875308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9213150012826419,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17912888809357153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1628906843867961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9733271953424216,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.053668589702016156,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.05055864773346741,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.27182853320794065,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.839477109666853,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0450957290202845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.18874535688286898,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.4393704736976876,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.00017280578613565467,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.15861206054687216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03448806762695256,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.180328369140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0011380004882823869,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.007829589843751705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.19448876854137875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6852410907289719,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2362742252544181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7026013677138288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.19401369908276234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.48492933668476956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.003571646554129504,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.04343542570933728,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.005343350363919586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05828555788530598,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.18954820039120968,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4675650827147493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.238953801998271,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.18037587605603594,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5760475392565634,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6666013585783892,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6728863911289684,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8156363262725286,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8963880617158138,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.631188486762571,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.310926288273472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0683138874012066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6567954139608645,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.37923150035488185,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3879572758224814,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.532928445252645,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.54760179083857,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7549692145002136,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.32054275706276947,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.344793676712098,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.09951210021972656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.14973487854004475,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.02404724121093693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.15341232299803664,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.012008361816413071,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.07097003936767976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.06746296194188872,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.963494578999291,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.18685617259974752,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2439313577552236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17164687958467484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1415561781631167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0014283316476004781,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.011581729802805252,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.002381423325411691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.004447424498674191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.16044208916884406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0759237784733755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.12477723339489954,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.028442426959959244,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0600013732910156,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05000114440917969,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.656920146821522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3039948985014487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.430189871789612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -21.507188008391974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -16.363437930123805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -9.571237280124524,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.686451222210518,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 17.18399978184716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.88976310003895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0166250402779413,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.145260756483125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -22.855752779917147,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -17.807427782678186,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -10.447456552386882,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.968765398446283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 19.88030596705438,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11599998474121165,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7430000305175781,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.06399999618530394,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3392000198364258,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.016349997520446635,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07835000514984003,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.184981096653797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.472056196860375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.113591536607533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.808995179816719,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.911989024777697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.7112020294036014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.10499995095389236,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.37928547177995964,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1312755200526503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0862888807444993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.147280412325647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.741394497361483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5399990081787109,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3400001525878906,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.42597185863669,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7535280755533345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.8322578309020399,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.579304529234299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.841821549319093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.973066084818285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.1886247236037253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 9.27387322930917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.658814811854118,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.466158217329827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5473287155955529,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -8.927869300759472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -6.285811401873476,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.09684681255592764,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.17900825481442784,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 10.550353018620063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.08550004959106161,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3969999313354471,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.029600028991698224,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.095200004577638,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.007750005722048314,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.033900003433227965,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.393029501400501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4568886906142211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.0935635645190205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2892034653619877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.6738682810056202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5011321205627643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.03571428571428581,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2142857142857143,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3235254210347831,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9951756940532404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.5116232938544707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5813960585483349,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.269996643066406,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.5,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -9.169269530024204,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.827426956375269,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.952480322368391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -29.582048205482373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -13.449107132692053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -13.233584743813953,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.205326257416987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.5280441145742145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -10.402112483241632,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.114796814598777,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.237409437674879,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -30.93061297700754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -14.893096985246437,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -14.10980401607631,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.19570978862769,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.804523903885106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5205001831054688,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.4785007476806697,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2789999389648443,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2391999816894526,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0579000091552615,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2972000122070284,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -9.512971776659061,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -10.317960895224164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -9.47404980235844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.68078449626983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -8.440671132962652,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.897095244025219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4178564889090399,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.310713631766183,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1178362510945323,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.663752339718836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.524334789843545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.004094092206901,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.1185989379882812,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8913955688476562,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.221245339994482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2805880884814824,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.3059975153899117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9940174793978915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 7.663758962083522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -19.170670854629382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -6.708174186981132,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.062664368798032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9884023867770542,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.5679579467049898,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.5909266306963987,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.40205183882244,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 7.4992122072354395,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -17.766547340389195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.7158906548946185,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.705295614582198,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.30956993103028196,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7095699310302734,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6592279052734398,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.8650279235839946,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.18020698547363168,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9349069595336914,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.380348672827847,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.7702686440116522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.141457450536377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.8255072953166316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.770958024679281,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4628319139005299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.35204260689871614,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.019900185721261288,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.2844174248887903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06543699777594547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9846821769483576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7846792084691199,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 5.0399932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.089996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9781143804169408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.006741429622915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9783139819202646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.576206713609908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6500047052416473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.0936884256769979,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5665577579629035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.6439477116265486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.745271427199513,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7193715713994076,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6933848666137776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.2276419420847344,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7939851473127355,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9699076979393548,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5569412891736061,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.92042750093744,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6430000305175838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.7639991760254077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.17816680908202898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.614995422363279,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.15695999145509631,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7072031402587982,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.5084305363109687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6872631123924995,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3441181340499995,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.22088665653777761,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.396417264352624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9075245740649329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.165713718959263,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4035731724330356,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.010601023114185981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2001821158830679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.106668270527523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4556078886738586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.09908584604042847,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.08306955339206556,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 8.0899658203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9200439453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8841385750993691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6974686939795749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6856899424540153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2375132318141358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9755787168682657,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.7701921952127275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.6700495680709508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -25.215428021622913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.34870437811805877,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.41009883575606754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.40076082714752825,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.11105153971103787,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5315888643138824,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.646411467475085,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.6604330992816543,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -23.938948232312022,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1689987182617188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.05500183105471,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7626165771484352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.0623455810547284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.28751983642581536,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3608546447754293,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.312031181568718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.3470821012762535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4344659279447614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.8148598748787927,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7774556001180386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5949250357441862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.07499912806919617,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.35857064383370485,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.017891723053096165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06360936757831803,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4886310863179375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.16929688557297817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.26318271423259565,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.09559337397660528,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.089996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -13.360015869140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.3900717401612583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.540490230437233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.2904992370896515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.215615193421742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.863276880831044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.353293383885811,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -13.589021892748644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -21.352559794015605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.15722878694383047,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.82786008866074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.5754283523961385,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.564179964946916,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4192870282766603,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2295126561481684,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -13.579405423959345,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -20.076080004704714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.14700012207032387,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1510002136230355,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.2711999511718659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.458999633789034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.014000015258773146,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.42065010070800213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.37187618281238066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.716149144400385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5298388760631711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.647697056695154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.442126983699187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.677828324095603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.14642878941127258,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.32071031842912934,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0712868426385862,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2639979060729494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.38377451589795086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.703899861251492,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.19180827486141816,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.6701751844512708,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.410003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -27.3800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17189020175105707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.1189795109225806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.9714057339909719,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.5339549842850175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6770682887451089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.531423643243437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.017178575197603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -18.699447258122092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0609527514663708,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.406349369146088,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.256334849297459,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.882519755810191,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.1210581412994927,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.407642915505795,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.007562106408306,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -17.4229674688112,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.2975006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.087499999999977,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5775561523437318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9946826171874932,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.040041503906252274,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.22956726074221478,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6433865092726592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.82077737838116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.8386309898119837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.4163100713722905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9891334057262835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -8.098637409890774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.033571515764508675,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.6228550502232135,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.038792959825479034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.03050204045124838,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9035338402893061,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.2547608185278065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.27388105291860365,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.21987685596297835,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -12.05999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -74.8800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9165346157063436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.3282850406534652,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.210000174904824,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.5645800341232565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.6203600868402344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.055167986294352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.95710758189081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.262214707648717,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.1493775689237715,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.6156548988769726,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.4949292902113118,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.913144805648431,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1763702342858515,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.931387258556709,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.947491113101513,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.985734918337826,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.2529998779295966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -20.588497924804642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8235034179688228,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 7.1684497070313,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.06920562744141989,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2880624389648574,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.1566705900373897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.7225256591257665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.935203249327289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -12.4283930536354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.898318840487756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -11.906759487712748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6400015694754444,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.514997209821427,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17674704962623533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0764150084325061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.550945503681902,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -9.629753764412731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8542717901776156,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8539822617225514,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9549980163574219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.930000305175781,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 4.215884055238761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.2006636529628754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9527649975032428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 14.14527319714607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9568109612519464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.667969506834503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.508712066554164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -8.132181120272389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.983041102021333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.913293794739368,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.6678358821967567,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 12.796708425620897,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5128211086975583,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.544188779096864,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.5183285353434606,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.855701330961498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.4940000534057702,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.3737499237060575,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0014000701904422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.176300201416026,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.10949998855591048,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4970750045776384,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.720021253780626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5605654577346755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9537142092643691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.618870679180553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.109525860569562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.0954637245347385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.05284990583147309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5289213997977118,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.10990371970062007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0078715235906817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8864735789465286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.504502107484733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.398888419608727,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2273138846435587,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 26.1500244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.20001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5210174249685506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.014617973315322885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.01417615422512064,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 8.360222191476641,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 4.658955336005242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9380510081877684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 9.4726600907149,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 11.54616866547381,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7118255282488772,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.27275188490818447,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.2707529610813664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 7.011657419951467,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.2149654834508574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.8142702804501258,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 9.482276559504198,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 12.822648454784701,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -7.505703735351631,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -46.82513427734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.3561413574218477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.2820422363281523,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.884595489501976,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 14.055534362792969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.3527116268787687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.095798533811147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.78843243635003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.09168076614898268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.0881951743950466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.5650499196332426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6538953778980741,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.350611561563447,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09355303807064086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2672441797869043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3833040882452536,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1093686932630007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.05394612898597717,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.10844324046247356,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2700004577636719,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3223346529865445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.3486815617600234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.3132413354840278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 11.67763020303224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 4.941205413619219,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.4715014718918233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 6.037860421957586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.1041090895656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.5551776062039724,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.6360514199835308,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.5981704507905148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 10.329065431507066,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.4972155610648343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.595282199629466,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 6.047476890746885,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.38058887887649,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.568499946594244,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.494999885559082,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.17979995727539233,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.6317998504638709,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.257692748401853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.435245236381448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.514810890645416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9478548581194577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.020357131958007812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.25178636823381684,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.194281496734642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5209732230385109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9962283544257886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.17244335904941377,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3268998020123961,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 5.459991455078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.3000030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.4591056125477415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.974504716633075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.8047640391420052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 10.846676098978659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 5.1422123690079395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.28577590798497354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.715389787454523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 11.729569257970851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.2262626593303136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.687134858409568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.519834923835518,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 9.498111327453485,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.698222516453555,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.161995180247331,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.7057733186652264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 13.006049047281742,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.2129997253418026,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -11.97300033569337,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.8797595214843739,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -8.308633422851557,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1955564880371412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7458109283447243,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.214157833616726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.746689761453256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.8213882376517567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.17835254760585428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9759716899354416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.5532591530475806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0028577532087048496,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3171408517020105,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.1677876591902221,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8200941153681667,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.8586067653564733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.20887918910955605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.37825808743377076,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.014025007882008889,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.0900115966796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1983126025303825,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.329238338460347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3244049105798119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.489981593467563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.4234887505020897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3420591463325966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9904690640463851,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5254863591215297,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03453035068704535,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.041868480236839645,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0394757952733249,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.141416821942389,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9794988979477068,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5341601259297604,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.0000855328356826,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8019661484324212,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.41049957275390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.562500762939436,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.06937011718747499,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3016384887695267,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.21299224853515852,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0107030868530273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.8044582234744149,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.4516357365078165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.6663113219462122,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3460212134696494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.697113112130765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.45297578887632994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.10285731724330383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6164278302873889,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.017765202642656686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3270793820742659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5297087112275722,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.178218123936424,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.016884285319073822,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2697865974871093,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.30999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.839996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.1575760555035517,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.091908884371584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.116549285330204,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0021471371768111425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3912238356359232,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.592230558030929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6482849882449848,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.2426737460097943,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.3904190087209796,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8045390261480767,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8316201700237169,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.346417634348363,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0527660169184596,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7160112857685714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6386685194556883,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.519153535320687,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.37700004577637003,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5890005111694308,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1619164276122973,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7872575378417963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11997301101684599,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5863850212097148,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.1362989340482068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.24566494672335626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.20992420163445935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5545425521486855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.28690400933961513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9825284835931711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0035716465541293374,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.16214343479701454,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.004327961294296578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.18161339353573247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6447755360281526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.2038444168243998,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.11347376156467381,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11999893188476562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9599990844726562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5385858992449153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0431957387881496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0591108233850344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7253815968780284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4441120969904686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.8796938874579805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3152039279199159,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.606256842554298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3057429460274874,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7558258805646423,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7741817080785474,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.37681682535285477,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.000122244436084884,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.003474615195623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.32482039670921337,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8827366318651895,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.09150009155273864,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3715003967285142,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03869773864745696,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1719486236572223,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.003977184295656855,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.023654384613038815,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0483161108771224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.066198199657431,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.28361473476681276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.017879536460565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.21706515908859192,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7532423007600384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0021427699497766906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.02928570338657921,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.001087886200114685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.030890797335826115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.20564144087205039,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.6451446014235205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.15417731487505237,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.11010517544150111,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3400115966796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2800140380859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.686982061129406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0652404964747073,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.039716195013286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.62823815340718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.330700824186871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8630845926810071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5586205914667524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5908434621018994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.454139107911978,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7778706382512,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7547870797067988,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2796733818820063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8867109716324872,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.013134679581350284,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5682370602560507,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.86732325141279,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09099960327148438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.7495002746582031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3810012817382926,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.8514254760742404,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.04028953552247572,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.20377319335938182,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4448064697899166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6065636249316331,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5759662387075717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.199725281335351,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.334630259199276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.04802812347083352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.02857208251953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1614270891462053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.005728125275457963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.094120275972152,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2580026374947586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1505370310760359,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.08612214688890718,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07095123989209806,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.6300048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.114177737704869,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5998600968304069,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6122568810954743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.061411301911573624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.34342233368636066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7541794892147013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6567615120161463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.2550562549267017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.11866521551255893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3124902386068995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.32732776578898726,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.4099760734367472,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.7874121862407453,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.12203978304765606,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6663779808054437,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.531536044237593,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4010002136230355,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.40500106811524,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2509622192382892,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2236996459961063,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11548294067381448,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6091578674316338,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.24110601226146056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6663449405553967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.15401456220676124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3822740611009854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.08390821082169353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8750579354643637,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.035464695521763456,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.21525028773716537,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0197817357001564,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.08679107110073137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2450493875141624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.001004416779096351,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.19166948110063875,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3000030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.75,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.582522848020107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.12802558517200913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.12956700538238053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.457143822564789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6521953929669255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4457368507785109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.15824802127462068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.24106524513358707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.34967989480267914,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.15934427305149823,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.15536210992410648,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.805708594089962,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.09618524552131,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4304824214838465,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.16786449006391813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0354145441773044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2840000152587834,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.4935001373291072,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.04864990234374034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3409736633300753,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0550133132934576,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.304129028320304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7060512225478099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9661103358459489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.41717642423149126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4696246776813462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.4295488210024345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5165574047312216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.012142726353236766,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.22571291242327018,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.019107270679570743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.24528111093454297,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3333737736186726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.7878710364667705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5147238821372203,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1871828477182348,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.160003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.6863725850713283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.7527658384295144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7438215608836174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.1253877712239966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.5282940748307503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.8387028989279806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.212954610356499,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.205658231295496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4535296318539004,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.0401356966530217,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0287506761901044,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.47395254274917,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0843042222763661,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9624836266656227,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.203338141567201,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.929178441984605,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.26300010681151775,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0270000457763615,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.07360473632812159,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.37491607666015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03950275421142635,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.13205535888671704,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7968435184294131,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.1199420221724932,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.089293590169882,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15694762133011686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.039575802126258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.059895094128425974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0671430315290178,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.14071491786411827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.04476658405809775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1254252730713883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.969930335138347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.16722628847779575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.038891717086571354,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.019639996933842108,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.660003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.239997863769531,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.20474971037220957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.364826573210065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.3080466840329485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.44780926016376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0023382861869656324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.5319086531169317,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.0619172947169537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -7.646295670573522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0280932428452183,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.6521964314335724,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.5929757993394356,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.796374031688934,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.4416515663674172,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.4081279253792887,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -3.052300825927656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.36981588126263,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3665000915527372,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.4139995574951172,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.17457931518553949,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.42188278198241846,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0628438186645468,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2265570449829113,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.189379930241552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.398242920025908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.3435993330585205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.235368571479237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.4215873991094146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.3439369358371795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.07178551810128364,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.10535703386579254,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.09476539151569052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.19199476339428467,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.446626285062635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.437906635093269,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6017649097878999,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7788429368847514,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.01000213623046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1899986267089844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6996094623424653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9902359892367105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.0479798158873352,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.525744477892212,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6880686491770769,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.686045781572237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6483015312184093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.640094648524487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.5332334908749625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7028661310132032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7630507005808482,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.1771797063670384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7559212033773068,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.809826509309881,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6579180000077072,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 7.916574437835379,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.16499996185302734,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6730001449584933,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.028731460571286505,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.10983673095702784,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.007092704772951208,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.017789707183837322,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.4378630940359507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2222542613286258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.04633649099252679,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.1157102408204573,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03859585860719328,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.6796135284491873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.06250708443777897,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05822127205984928,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.14652275090909983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.18305239763564418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2568540822282426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.434960927613597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.12290959536779039,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2963536387339955,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.22999954223632812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1300010681152344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4226955893819717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7025285899251674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7393003296927612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.3081598116386446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0764352708771963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.6667886546701185,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9982126673050651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.313879374358498,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.8101473638354562,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.41515873170166,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4543712143862741,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.959595040113471,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.36755458167718746,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.790569382407761,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0078291360943625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.59035916366939,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.07250003814697692,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.17150001525879333,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.04184265136718324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.18331214904785043,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.016556739807128906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07497043609619425,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.37424593495885006,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3018445230690077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6371231829767732,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.067721653171096,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4998188129479164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.473981294371641,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.011286054338727647,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.03342846461704807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03461063058494718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.03957225787527552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6061439309764545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.5787089485772015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.06775471308083625,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15732248175185037,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.06999969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.43000030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8715716224663717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07750400664621182,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.07805163155845118,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.2102462678525336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8287925597802337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3664540735487618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.5344467436788753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.500006193168547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3612713307510562,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.20986585157729554,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.20687748374803583,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.558811039377707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.6151972927741505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4902348012864044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.544063212468173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.7764859824794383,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.09549999237060547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3585000991821303,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.018386383056636646,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.11422660827636832,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.022411460876462286,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1276093673706029,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.05630398453357888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.12428600637361953,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.17401738418978407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0694974007201652,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.093368756202028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5949592184314012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.013214383806501195,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.07250050136021213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.027503609093782577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.15312087147412834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.13102633679351605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8048801491029716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.11353061862061065,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.08492346526899819,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 14.41998291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -6.84002685546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9995491575167446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1290131631358724,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.085249114869502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.94926084131081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.3521099776195324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.7503640325381546,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3727390206659815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.470038056334445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7667062042993167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.841643304912365,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.800319999563015,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.600696069785636,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9081201250651496,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.626583304800512,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3823554894552794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.7465178456453367,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.9195007324218523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -16.036502075195358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9240002441406432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.177600097656182,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.813199920654256,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.9636000061035475,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9261640736462864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3476414352690087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.658985922460788,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5012993407678472,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.6320982008056992,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.146921870552898,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7257167271205347,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.0650068010602673,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.04120635766150249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6028150449223744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.274803968257478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.0790387430243857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2984889036293784,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.14639502317842013,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8000030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.400001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9966147109124357,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.8579746252608267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.8952109876212422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 9.848596946384692,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.3326974665839764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.717166199845992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7456039479078598,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.6972437949770445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.2294576641298636,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.145344483484334,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.1801401029277292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 8.500032174859518,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.11129238597040647,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.840946927583635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7359874791185632,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.420764005666154,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.29799995422362713,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6504997253417883,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1461999511718659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4815998840332014,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.03484786987304744,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.12348907470702386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4559970303361416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.3744537691611685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6086643316840057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.620419729185143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8086876617634289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.605288602629299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.03071430751255555,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07285799298967621,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.046495158163346595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06311741348812028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.7100408846712036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.79275904290134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.11096903149827131,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05161671722930261,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.3899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.8766018809851506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0258570037338886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.0484037776534514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.036038568221075096,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.5986925900745472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.755136535968797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.14260674388464345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8776365515752662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.1094448342025784,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7384871455103812,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.7634746623469644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.312526203304099,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1547027375201644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.878917263706439,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.15222321267394,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.1541163408861568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2360000610351562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.6270004272461165,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5017361450195494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.2698941040039244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3902193450927882,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.880943908691421,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9685057368685079,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.25745148268017104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.3867634814021423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5672974565395403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.6066232311406488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8636484214897173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1710717337472092,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.44250270298549044,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.04589114972190522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15491266237398582,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.45413895595100007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.07178949768504239,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2107970983983828,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 5.040008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 17.279998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -4.132153171018826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.49910176975485054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5149643602856413,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.407936058135054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.3003039552397464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.137022814075522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.1575676852489503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.240903929839803,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -5.364996124236254,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2117319115313432,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.23003524497915429,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.059371286609881,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.8563141026853627,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.260803541813164,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.1479512164596528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 7.517383719150694,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.6304992675781023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.6580017089843864,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.37859985351559544,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.3309997558593523,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.4311999511718909,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0811500549316406,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1365316280449456,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.642763499595404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.3465803441292667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.850216393416384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1637717118318625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.85117379762947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.14071219308035765,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.359998430524554,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0014713755527671069,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.48232027762105956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.1544295890639997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.9580373152163677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.333766166387404,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15670666729403537,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 4.9300079345703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 3.538174436376862,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.0644128069946985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9828465789912384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.1284718366642355,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 4.4124925686269805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.873587031736302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5166803465350043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.07716153337726794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.305331483159434,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.777042948771191,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.6979174636847514,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.477036608189409,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9685027160725967,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9973677594739447,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.5262968153243008,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1993182559336226,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.10499954223632812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.8970001220703239,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9153359985351699,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.605878295898435,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09850044250487144,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5194600677490371,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.4392869337282685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.626580656264708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.6550807811359656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7035145273467727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.1896431603248505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.0567491450377382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.13142939976283508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9278564453125004,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.01536345044586751,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4524790383566313,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.9491836628687338,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.23721916230826778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.15314491061056723,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.05425664490471194,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3299999237060547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3971533538275285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5870671117147452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.583352724028996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.913300217050654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.807681798218775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.798867466108545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2751663822117778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2857034185890672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.8356895993898994,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2996972534912379,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.29842360872250895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.56473544552548,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.3636919456643923,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9226481938461877,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2847828510010748,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9907763707218233,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09499998092651296,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.6487500190734856,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09380001068115718,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.45899997711181584,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.013350000381471716,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.04245002746581861,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.342976395811546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3959681628820007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.303022340155346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.763037711168458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.0513623956940776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5502388332811696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.007499967302594834,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.0882141930716378,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.0029572921251950213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.281911509308296,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9466434822954728,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.401604667806188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.039393953901520895,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.005781354528567206,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2700042724609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.470001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.30358036652262665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1604714906516822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2140883707277617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.441384232207236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.8181751094834109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.882194923995899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.155047739223646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.189120555434789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.9292625866948012,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8731016324281748,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.9291592554212746,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.092819460682062,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.37418525692902715,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.005975651733541,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.1646642080129439,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.465600344745679,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.10900001525878622,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2115001678466797,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.09517318725585255,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4974909973144577,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.029088973999023438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15353275299071356,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.2241582248061258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.648685721702661,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.5073586469286573,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.474749349514374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3417823483233384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.726014236702958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.008928026471819228,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.013213566371372831,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.018881106952562954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06912100873182281,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3484435825632062,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.478076016428334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.1587295756323508,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2066373388175482,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.5,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 8.779998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.3562586717681393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.12756764224259864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.13254110032834276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 12.076405726193261,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 2.9275599496493943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 8.793715347603982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7340305720837215,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.284071086128737,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.5891016249855672,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.414937500466106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.4174702156348298,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 10.727840954668089,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.48357009709501,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 7.917496075341623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.7244141032944249,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.0075912968178464,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.3699996948242017,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1265007019042912,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.09040008544923239,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.25660034179688296,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.20559997558592613,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9247999954223474,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.2731357746152971,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.177839069909041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4658404657356794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.191635791793048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.654867475373667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.654686596208133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.03910718645368316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.34339468819754426,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.01865510806344206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.05984694993658213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 1.4294699575303271,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.020297792863138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -2.1578180160677416,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.13518654452896528,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.04999999999999982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.06999999999999984,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.06000000000000005,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-22",
        "to": "2026-10-23",
        "change": 0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 6,
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
        "change": -0.08000000000000007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
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
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -83.41177368164062,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_ACT.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -80.4246826171875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_THREAT.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -122.77737426757812,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA7.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.4905548095703125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.GPRD_MA30.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.572418212890625,
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
| 推断与解释 | VIX/MOVE降低与股价修复显示短期恐慌缓和；滞后信用/实际利率仍有压力，不能定性全面过热。 |
| 反证与缺口 | 同日VIX低于VIX3M，但非信用风险消失；美债收益率仍只核验至23日。 |
| 确认条件 | 信用与波动持续上行、成分广度同步恶化。 |
| 失效条件 | 油价风险消退、信用改善且股市承接恢复。 |
| 观察期限 | 未来1–2周 |
| 条件式指导 | 避免仅凭VIX未到极端就认定安全。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较昨晚：突破有收盘确认、波动降低；Meta反向下跌，AnthropicS-1与盘后融资新增；仍未证明中期趋势和现金回报改善。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 第一层收盘突破已确认，反弹可靠性上调一档，仍不足确认趋势反转。 |
| 反证与缺口 | QQQ量能0.89倍、RSP落后SPY；META/GOOGL走弱，尚无完整广度及逐笔VWAP。 |
| 确认条件 | 下一交易日回踩QQQ709.30、SMH533.34、SPY763.47后收复/守住，RSP参与；再突破26日高点QQQ715.25、SMH545.34、SPY767.73并守住，才提高可信度。 |
| 失效条件 | 跌回第一层下方且反抽失败则降级；QQQ705.58/SMH530.20（26日低点）再失守，修复进一步受损；更大结构底部仍看23日低点。 |
| 观察期限 | 未来1–5交易日 |
| 条件式指导 | 等待确认后分批试探，不把一次拉升当趋势。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较昨晚：突破有收盘确认、波动降低；Meta反向下跌，AnthropicS-1与盘后融资新增；仍未证明中期趋势和现金回报改善。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.IGV.return_5d_pct", "prices.SMH.relative_spy_5d_pp", "prices.XLE.return_1d_pct", "prices.OIH.volume_vs_previous20_ratio"] |
| 推断与解释 | 软件/云跨期领先；半导体当天强但五日仍弱。能源保持相对强势，金融工业作扩散验证。 |
| 反证与缺口 | 领涨ETF不代表净申购；部分板块量能较低，财报与油价可能反转。 |
| 确认条件 | 相对SPY持续领先，回踩守住，订单/利润或发行人申赎补证。 |
| 失效条件 | 领涨消失、跌破回踩低点或经营逻辑证伪。 |
| 观察期限 | 未来一周 |
| 条件式指导 | 先看强势无杠杆篮子，避免同时集中多个同一风险链。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较昨晚：突破有收盘确认、波动降低；Meta反向下跌，AnthropicS-1与盘后融资新增；仍未证明中期趋势和现金回报改善。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 融资可得与需求增长存在证据，经营/每股现金回报仍须单独验证。 |
| 反证与缺口 | Anthropic巨额净亏损有大额公允价值项目，不能等同烧钱；Meta收跌反映稀释与回报担忧仍在。 |
| 确认条件 | 企业自由现金流、融资与价格承接同步改善。 |
| 失效条件 | 订单/指引下修、资本投入长期超过现金生成且融资收紧。 |
| 观察期限 | 下一季度并每日跟踪风险 |
| 条件式指导 | 用公司整体FCFF情景，保留META输入缺口。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较昨晚：突破有收盘确认、波动降低；Meta反向下跌，AnthropicS-1与盘后融资新增；仍未证明中期趋势和现金回报改善。 |

## AI融资与资本回报 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Anthropic26日正式提交公开S-1；融资股数和价格区间尚未确定。Broadcom与金融伙伴于收盘后公布630亿美元算力融资交易，通过SPV采购并出租设备，预计2027年开始交付。 |
| 事实：市场反应 | NVDA+2.39%、SMH+2.74%；META−1.88%、GOOGL−1.06%。Broadcom融资公告属盘后增量，不倒灌为26日收盘上涨原因。 |
| 推断：解释 | 推断：投资者愿意交易算力需求，但对出资方的稀释与回报更挑剔；申报、融资承诺、实际交付、盈利四个阶段不能混同。 |
| 受益篮子 | ["NVDA", "AVGO", "SMH"] |
| 受损篮子 | ["META融资稀释敏感篮子", "资本回报较弱公司"] |
| 反证 | 上市尚未完成，Meta正式发行条款仍待核验；合作双方共同融资不构成独立的终端需求证明。 |
| 下一催化剂 | 27–29日财报、融资条款与下一交易日承接 |
| 证据 | ["https://www.anthropic.com/news/s1-sec", "https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx"] |

## 软件与云的相对强势 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 微软官方推出限时自愿离职计划；Cadence盘后披露Q3收入16.33亿美元并提高全年展望，经营利润率同比下降。 |
| 事实：市场反应 | IGV五日+5.09%、SKYY+5.45%，分别明显强于SPY五日−0.14%；当日IGV+0.72%、MSFT+1.54%。 |
| 推断：解释 | 推断：软件/云趋势比单日芯片反弹更完整，但成本控制和收入增长仍需转化为每股现金回报。 |
| 受益篮子 | ["IGV", "SKYY", "MSFT", "CDNS"] |
| 受损篮子 | ["同业中指引下修者"] |
| 反证 | Cadence GAAP经营利润率26.2%低于31.8%；微软计划是自愿选择，不代表已裁员6万人或已实现节省。 |
| 下一催化剂 | 微软28日财报与云业务/资本支出指引 |
| 证据 | ["https://blogs.microsoft.com/blog/2026/10/26/introducing-a-voluntary-exit-offer/", "https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Third-Quarter-2026-Financial-Results/default.aspx", "https://www.microsoft.com/en-us/investor/faq"] |

## 原油风险溢价缓和但能源股坚挺 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Reuters26日盘中报道外交缓和预期与沙特设施风险并存，尚未确认海峡全面恢复。 |
| 事实：市场反应 | XLE收涨0.45%、XOP+1.57%、OIH+1.27%；延迟WTI分钟价约101.32，报价时点见面板。 |
| 推断：解释 | 推断：昨晚担心能源随油价回吐，收盘并未确认这一弱势；能源仍有相对强度，不能直接等同净流入。 |
| 受益篮子 | ["XLE", "XOP", "OIH"] |
| 受损篮子 | ["高燃料成本运输行业"] |
| 反证 | 油价反复、合约换月与地缘消息均可使追涨失效；通航合约与军事停火定义不同。 |
| 下一催化剂 | 实际航运、设施损伤与本周政策声明 |
| 证据 | ["https://finance.yahoo.com/news/oil-prices-down-almost-1-232445179.html"] |

## 金融与工业参与但市场广度仍不完整 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 本周FOMC与GDP/PCE在即；算力融资给金融机构带来业务机会，也带来期限和信用风险。 |
| 事实：市场反应 | XLF+0.21%、KRE+0.37%、XLI+1.42%；RSP+0.35%、IWM+0.45%均落后SPY。 |
| 推断：解释 | 推断：不是只有芯片上涨，但尚不能确认全面风险偏好转向；ETF样本不代表全部成分股广度。 |
| 受益篮子 | ["XLI", "KRE观察篮子"] |
| 受损篮子 | ["融资成本敏感企业"] |
| 反证 | XLF当日量能仅前20日0.63倍；缺少当期申赎和全市场涨跌家数。 |
| 下一催化剂 | 28日Fed、29日GDP/PCE |
| 证据 | ["https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## 存储与半导体财报验证 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | STX27日与SNDK29日财报窗口已官方核验；当前未取得新的中国存储厂商量产份额/利润冲击证据，不将传闻写作本日因果。 |
| 事实：市场反应 | MU+2.98%、DRAM+2.70%、SMH+2.74%，但SMH距20日线仍−7.04%，五日仍−1.25%。 |
| 推断：解释 | 推断：有交易性修复，不等于存储周期、HBM供需或估值风险已解除；NAND、DRAM、HBM须分别验证。 |
| 受益篮子 | ["SMH", "MU", "SNDK", "STX"] |
| 受损篮子 | ["高估值且利润指引下修者"] |
| 反证 | DRAM历史不足200日；SNDK/STX预测盘口太薄或太宽，不能作为胜率。 |
| 下一催化剂 | 27–29日出货量、价格、毛利率及指引 |
| 证据 | ["https://investors.seagate.com/news/news-details/2026/Seagate-Technology-to-Report-Fiscal-First-Quarter-2027-Financial-Results-on-October-27-2026/default.aspx", "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29"] |

## 航天：价格修复与项目延期并存 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Virgin Galactic盘后公司新闻稿称28日转场准备试飞，但商业航班预期推迟至2027年二季度，第二艘延至二季度末/三季度初。 |
| 事实：市场反应 | ITA+2.44%、ARKX+1.11%；未取得SPCE公告后可核验价格，不能把ETF收涨当作认可延期。 |
| 推断：解释 | 推断：航天不能只按同一主题买入，工程进度和资金消耗更重要。 |
| 受益篮子 | ["按订单和交付确认的工业/航天篮子"] |
| 受损篮子 | ["项目延期且融资紧张者"] |
| 反证 | 转场不等于商业收入；消息属于盘后，不解释当天ETF涨幅。 |
| 下一催化剂 | 28日转场受天气和技术条件约束，后续财务指引 |
| 证据 | ["https://www.stocktitan.net/news/SPCE/virgin-galactic-sets-october-28-for-lead-delta-class-spaceship-s-ysvpiwc45syk.html"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 764.21 | -0.15 | 2026-10-26T23:14:16+00:00 | 2026-10-26T23:14:16+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| QQQ | 711.85 | -0.05 | 2026-10-26T23:17:45+00:00 | 2026-10-26T23:17:45+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| SMH | 542.39 | 0.14 | 2026-10-26T23:15:37+00:00 | 2026-10-26T23:15:37+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| RSP | 217.25 | -0.02 | 2026-10-26T21:48:21+00:00 | 2026-10-26T21:48:21+00:00 | 2026-10-26T23:18:18.700885+00:00 | stale |
| META | 632.75 | 0.35 | 2026-10-26T23:14:04+00:00 | 2026-10-26T23:14:04+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| MSFT | 531.20 | -0.26 | 2026-10-26T23:17:35+00:00 | 2026-10-26T23:17:35+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| AMZN | 248.90 | -0.08 | 2026-10-26T23:17:37+00:00 | 2026-10-26T23:17:37+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| NVDA | 216.02 | 0.01 | 2026-10-26T23:18:12+00:00 | 2026-10-26T23:18:12+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| GOOGL | 317.42 | 0.20 | 2026-10-26T23:18:13+00:00 | 2026-10-26T23:18:13+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| IGV | 111.90 | 0.46 | 2026-10-26T22:54:46+00:00 | 2026-10-26T22:54:46+00:00 | 2026-10-26T23:18:18.700885+00:00 | stale |
| XLE | 69.70 | 0.09 | 2026-10-26T22:44:00+00:00 | 2026-10-26T22:44:00+00:00 | 2026-10-26T23:18:18.700885+00:00 | stale |
| XLF | 56.00 | -0.04 | 2026-10-26T23:03:04+00:00 | 2026-10-26T23:03:04+00:00 | 2026-10-26T23:18:18.700885+00:00 | stale |
| IWM | 276.42 | -0.21 | 2026-10-26T23:17:05+00:00 | 2026-10-26T23:17:05+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| GLD | 367.82 | -0.00 | 2026-10-26T23:07:54+00:00 | 2026-10-26T23:07:54+00:00 | 2026-10-26T23:18:18.700885+00:00 | ok |
| TLT | 81.61 | -0.08 | 2026-10-26T22:38:00+00:00 | 2026-10-26T22:38:00+00:00 | 2026-10-26T23:18:18.700885+00:00 | stale |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 765.37 | USD_per_share | 2026-10-26 | 0.71 | -0.14 | -0.03 | ok |
| QQQ | 712.20 | USD_per_share | 2026-10-26 | 1.11 | -0.86 | -3.30 | ok |
| IWM | 276.99 | USD_per_share | 2026-10-26 | 0.45 | 2.10 | -1.08 | ok |
| RSP | 217.29 | USD_per_share | 2026-10-26 | 0.35 | 1.82 | 3.60 | ok |
| GLD | 367.82 | USD_per_share | 2026-10-26 | 0.33 | -3.13 | -2.67 | ok |
| GC=F | 4,024.50 | USD_per_troy_ounce | 2026-10-26 | 0.41 | -3.26 | -3.45 | ok |
| CL=F | 101.32 | USD_per_barrel | 2026-10-26 | -1.89 | -2.26 | 9.42 | ok |
| BZ=F | 110.14 | USD_per_barrel | 2026-10-26 | -5.64 | 0.54 | 4.62 | ok |
| TLT | 81.68 | USD_per_share | 2026-10-26 | 0.42 | 2.79 | 4.31 | ok |
| UUP | 29.01 | USD_per_share | 2026-10-26 | 0.17 | 0.03 | 1.08 | ok |
| HYG | 77.20 | USD_per_share | 2026-10-26 | 0.19 | 0.48 | 0.00 | ok |
| LQD | 104.02 | USD_per_share | 2026-10-26 | 0.16 | 1.11 | 1.95 | ok |
| ^VIX | 18.39 | index | 2026-10-26 | -5.45 | -0.27 | 14.44 | ok |
| ^VIX3M | 19.94 | index | 2026-10-26 | -2.64 | 1.73 | 9.38 | ok |
| ^VVIX | 101.43 | index | 2026-10-26 | -7.54 | -5.14 | 11.44 | ok |
| ^MOVE | 102.19 | index | 2026-10-26 | -1.08 | 0.88 | 6.45 | ok |
| NVDA | 216.00 | USD_per_share | 2026-10-26 | 2.39 | -0.50 | -5.62 | ok |
| MSFT | 532.60 | USD_per_share | 2026-10-26 | 1.54 | -0.17 | 4.59 | ok |
| AMZN | 249.09 | USD_per_share | 2026-10-26 | 0.44 | -5.09 | 1.19 | ok |
| GOOGL | 316.80 | USD_per_share | 2026-10-26 | -1.06 | -7.96 | -7.57 | ok |
| META | 630.56 | USD_per_share | 2026-10-26 | -1.88 | -10.61 | -11.89 | ok |
| CRWV | 55.19 | USD_per_share | 2026-10-26 | 1.76 | -9.70 | -35.12 | ok |
| MU | 903.70 | USD_per_share | 2026-10-26 | 2.98 | -0.13 | -14.24 | ok |
| DRAM | 48.33 | USD_per_share | 2026-10-26 | 2.70 | 0.00 | -19.05 | ok |
| VRT | 199.78 | USD_per_share | 2026-10-26 | 2.81 | -3.06 | -18.14 | ok |

## 跨资产风险解释

判断：恐慌缓和后的分化修复，既不足定性为全面过热，也不能说风险结束。26日VIX18.39、同日VIX3M19.94（指数期限关系，非期货曲线），VVIX101.43、MOVE102.19；GLD+0.33%、TLT+0.42%、UUP+0.17%，不是所有避险指标同向撤退。FRED最近23日2年4.69%、10年5.00%、实际10年2.66%、HY338bp、IG91bp，不能假称26日信用已改善。GPR更新至26日165.25、七日均值181.42，反映新闻计数而非战争客观概率；STLFSI仍至16日−0.6328。CNN418/robots缺失，tc温度不替代。WTI/Brent延迟分钟报价仅作当前水平；Yahoo连续期货的夜盘/换月导致日线归属和Reuters近月价差异，本次不采信其日收益为官方结算跌幅。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.69 | percent | 2026-10-23 | -0.18 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.38 | percentage_points | 2026-10-23 | 0.45 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.91 | percentage_points | 2026-10-23 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.00 | percent | 2026-10-23 | -0.18 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.66 | percent | 2026-10-23 | -0.19 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.34 | percent | 2026-10-26 | 0.00 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.63 | index | 2026-10-16 | 0.04 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.45 | index | 2026-10-23 | 4.58 | lagged | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 165.25 | index | 2026-10-26 | -36.19 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 149.77 | index | 2026-10-26 | -147.74 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 187.38 | index | 2026-10-26 | 26.08 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 181.42 | index | 2026-10-26 | 0.55 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 175.44 | index | 2026-10-26 | 12.06 | ok | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | 1.69 | 0.19 | -4.22 | 0.98 | 0.34 | -4.19 | 0.83 | 2026-10-26 |
| XLE | 能源 | 0.45 | 2.71 | 12.14 | -0.26 | 2.86 | 12.17 | 1.00 | 2026-10-26 |
| XLF | 金融 | 0.21 | 1.74 | 3.38 | -0.50 | 1.89 | 3.41 | 0.63 | 2026-10-26 |
| XLI | 工业 | 1.42 | 0.17 | -1.08 | 0.71 | 0.31 | -1.05 | 0.87 | 2026-10-26 |
| XLV | 医疗 | 0.00 | 2.07 | 4.68 | -0.71 | 2.21 | 4.71 | 0.90 | 2026-10-26 |
| XLP | 必需消费 | -0.34 | 0.86 | 6.90 | -1.05 | 1.00 | 6.93 | 0.96 | 2026-10-26 |
| XLY | 可选消费 | 1.03 | -0.17 | 4.83 | 0.32 | -0.03 | 4.86 | 0.94 | 2026-10-26 |
| XLC | 通信 | -1.57 | -5.67 | -6.59 | -2.28 | -5.52 | -6.56 | 1.43 | 2026-10-26 |
| XLU | 公用事业 | -0.02 | 2.88 | 8.41 | -0.73 | 3.02 | 8.44 | 0.39 | 2026-10-26 |
| XLRE | 房地产 | 0.54 | 2.71 | 3.51 | -0.17 | 2.86 | 3.54 | 1.15 | 2026-10-26 |
| XLB | 材料 | 0.14 | 0.84 | 3.86 | -0.57 | 0.99 | 3.89 | 0.84 | 2026-10-26 |
| SMH | 半导体 | 2.74 | -1.25 | -9.73 | 2.02 | -1.10 | -9.70 | 1.21 | 2026-10-26 |
| IGV | 软件 | 0.72 | 5.09 | 5.65 | 0.01 | 5.24 | 5.68 | 0.73 | 2026-10-26 |
| XOP | 油气开采 | 1.57 | 2.70 | 13.72 | 0.86 | 2.85 | 13.75 | 0.87 | 2026-10-26 |
| OIH | 油服 | 1.27 | 4.49 | 3.24 | 0.56 | 4.63 | 3.27 | 0.80 | 2026-10-26 |
| ITA | 航空与国防 | 2.44 | -0.29 | -1.00 | 1.73 | -0.14 | -0.97 | 1.15 | 2026-10-26 |
| ARKX | 航天主题 | 1.11 | 0.47 | -5.92 | 0.40 | 0.61 | -5.89 | 0.51 | 2026-10-26 |
| KRE | 区域银行 | 0.37 | 5.01 | 3.09 | -0.34 | 5.15 | 3.12 | 0.84 | 2026-10-26 |
| SKYY | 云计算 | 1.49 | 5.45 | 4.55 | 0.78 | 5.60 | 4.59 | 0.64 | 2026-10-26 |

## 资金证据分层

19个ETF同端点26日收盘全部检查。五日IGV+5.09%、SKYY+5.45%、KRE+5.01%、OIH+4.49%、XLE+2.71%；SMH五日−1.25%，当日却领涨2.74%，属于强反弹与跨期强势的区别。相对SPY五日，IGV+5.24个百分点、SMH−1.10个百分点。先观察软件/云延续，再看半导体突破后的回踩，能源保留但不追事件溢价；工业和金融用作参与面辅助。SMH当日量能1.21倍，QQQ0.89倍、SPY0.77倍，不能称全市场放量确认。资金层：发行人SMH页面仍为23日NAV527.13/资产666亿美元，缺少连续份额与拆分桥；ICI最近公布20日、窗口截至14日，全部ETF估计净发行532.62亿美元、国内股票296.70亿美元。这是旧窗口总类数据，既非26日流入也非芯片主力资金；13F不提供当日身份。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-26T23:23:01.505055+00:00：基础25主题/跟踪清单重查，另查Saudi oil attack、Microsoft/Seagate/Sandisk earnings、AI bankruptcy、bank failure、recession、CPI November、Meta offering、Anthropic IPO。Meta87、Anthropic28、CPI28结果截断；SNDK81%但价差18个百分点/24小时仅6.64美元，STX价差25–61个百分点且量缺失，排除强定量信号。银行失败74%、仅857美元/价差4个百分点，缺独立官方新失败证据，不作为危机确认。未找到直接Meta融资完成合约；以Anthropic明确上市定义作参考。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.55, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.01100000000000001, "volume24h_usd": 5121.053741, "liquidity_usd": 42226.53268, "quality_flags": [], "retrieved_at": "2026-10-26T23:18:03.629225+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价9.55%，24小时成交约5121美元，价差1.1个百分点；同规则变化见比较，不是客观概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [45.5, {"status": "comparable", "change_pp": -0.5000000000000004}] | {"spread": 0.02999999999999997, "volume24h_usd": 25605.394336000005, "liquidity_usd": 23626.3439, "quality_flags": [], "retrieved_at": "2026-10-26T23:18:03.629225+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["本次报价45.5%，24小时成交约25605美元，价差3个百分点；同规则变化见比较，不是客观概率。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [20.0, {"status": "comparable", "change_pp": -3.9999999999999982}] | {"spread": 0.01999999999999999, "volume24h_usd": 10980.054622000001, "liquidity_usd": 21254.1621, "quality_flags": [], "retrieved_at": "2026-10-26T23:17:59.559528+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["本次报价20%，24小时成交约10980美元，价差2个百分点；同规则变化见比较，不是客观概率。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [89.5, {"status": "comparable", "change_pp": 4.0000000000000036}] | {"spread": 0.010000000000000009, "volume24h_usd": 205954.749665, "liquidity_usd": 194775.63, "quality_flags": [], "retrieved_at": "2026-10-26T23:18:03.629225+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["本次报价89.5%，24小时成交约205955美元，价差1个百分点；同规则变化见比较，不是客观概率。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 23596.435413999996, "liquidity_usd": 505907.249, "quality_flags": [], "retrieved_at": "2026-10-26T23:18:03.629225+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价11.5%，24小时成交约23596美元，价差1个百分点；同规则变化见比较，不是客观概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [94.5, {"status": "comparable", "change_pp": 2.9999999999999916}] | {"spread": 0.010000000000000009, "volume24h_usd": 57748.97986900001, "liquidity_usd": 28632.1532, "quality_flags": [], "retrieved_at": "2026-10-26T23:18:02.448097+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价94.5%，24小时成交约57749美元，价差1个百分点；同规则变化见比较，不是客观概率。公开S-1已经核验，但尚未挂牌交易。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [93.15, {"status": "comparable", "change_pp": -1.9000000000000017}] | {"spread": 0.0010000000000000009, "volume24h_usd": 4002513.5077449987, "liquidity_usd": 737666.069, "quality_flags": [], "retrieved_at": "2026-10-26T23:18:03.629225+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["本次报价93.15%，24小时成交约4002514美元，价差0.1个百分点；同规则变化见比较，不是客观概率。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |
| ["Will Microsoft (MSFT) beat quarterly earnings?", "下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。", "https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82"] | [86.0, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.12, "volume24h_usd": 541.9942580000001, "liquidity_usd": 601.879, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-26T23:18:03.629225+00:00", "contract_end_at": "2026-10-28T21:00:00+00:00"} | ["本次报价86%，24小时成交约542美元，价差12个百分点；同规则变化见比较，不是客观概率。固定GAAP EPS>4.82，价差宽，不作为股价上涨胜率。", "财报影响云/AI估值；EPS之外更须检查资本开支、自由现金流与指引。"] | ["官方首次披露GAAP EPS与专门规则核验，同时看指引与股价承接。", "EPS过线但现金回报/指引转差、股价失守；不可由合约直接推导交易方向。"] | [null, null] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 93.15 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.35, 8.65] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.9000000000000017} |
| 24h成交量 / 流动性 USD | [4002513.5077449987, 737666.069] |
| 价差 pp | 0.10 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:14:39.688562Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 89.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [10.0, 11.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.0000000000000036} |
| 24h成交量 / 流动性 USD | [205954.749665, 194775.63] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.4, -0.85] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.05} |
| 24h成交量 / 流动性 USD | [70093.02480800002, 301666.27692] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 45.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-18.0, 10.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5000000000000004} |
| 24h成交量 / 流动性 USD | [25605.394336000005, 23626.3439] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:12:39.845363Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 74.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [24844.518606999998, 127619.5066] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:14:39.688562Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [23596.435413999996, 505907.249] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:08:39.945898Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.55 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.2, 1.15] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [5121.053741, 42226.53268] |
| 价差 pp | 1.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 12.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2107.73, 26713.6093] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will Microsoft (MSFT) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1200526 / 5778671 |
| Yes 概率 % | 86.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [8.0, 8.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [541.9942580000001, 601.879] |
| 价差 pp | 12.00 |
| 到期 | 2026-10-28T21:00:00+00:00 |
| 结算规则摘要 | 下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。 |
| 规则指纹 | c38981deb507343e93936539de51b155f638166eb35f7eaca3a8513338e39cb0 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [436.064659, 12973.0834] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:03.629225+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 20.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-10.5, -3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.9999999999999982} |
| 24h成交量 / 流动性 USD | [10980.054622000001, 21254.1621] |
| 价差 pp | 2.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:17:59.559528+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 94.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [12.0, 17.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.9999999999999916} |
| 24h成交量 / 流动性 USD | [57748.97986900001, 28632.1532] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-26T23:16:40.259307Z |
| 抓取时间 | 2026-10-26T23:18:02.448097+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## AI 压力：合约、经营与估值分开

合约层：2026年专门AI严重下行9.55%、2027年6月底22.5%，均与昨晚相同；前者24小时成交约5121美元，后者约436美元，后者很薄。规则要求90天内至少三项极端事件，不能用作普通回撤概率。经营层：Anthropic S-1已直接从SEC取得；2026上半年收入162.86亿美元、经营亏损6.93亿美元、净亏损807.48亿美元，其中可转票据/衍生负债/SAFE公允价值变动损失723.88亿美元。净亏损不是同额现金烧钱，剔除会计项也不自动等于自由现金流盈利。Google合同承诺是2026年4月至2033年7月至少约1145亿美元，非社交摘要所称“最多”；需关注最低采购义务。H100指数26日2.89美元/GPU小时、七日+7.0%，与1美元持续五日阈值仍远，但单一型号不能代表全产业回报。估值层：本次SEC五家10-Q/K均检查成功，无新定期财报；NVDA/MSFT/AMZN/GOOGL复用已核验财务底稿，以26日常规收盘重算五年FCFF/反推/敏感性。META继续缺租赁新增/净债务桥及本次优先权益、股本稀释条款，不给精确估值。假设不等于观测，公司整体估值不全部归因AI。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-26T23:19:06.592818+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 216.00 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2936009060807513, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -54.27 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -28.65 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 12.31 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-26T23:19:10.085392+00:00", "latest_filing_date": "2026-07-29"} |
| 观测财务数据 | {"ttm_revenue_million": 331839.0, "revenue_quarters": [{"end": "2025-09-30", "value": 77673000000, "filed": "2025-10-29", "duration_days": 92}, {"end": "2025-12-31", "value": 81273000000, "filed": "2026-01-28", "duration_days": 92}, {"end": "2026-03-31", "value": 82886000000, "filed": "2026-04-29", "duration_days": 90}, {"end": "2026-06-30", "value": 90007000000, "filed": "2026-07-29", "duration_days": 91}], "cash_million": 20935.0, "liquid_investments_million": 55908.0, "debt_million": 40294.0, "finance_lease_million": 66594.0, "diluted_shares_million": 7453.0, "latest_operating_income_million": 155237.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 331839.0, "income_statement_window": "FY2026 全年"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。融资租赁66594计入债务；资本开支假设涵盖新增租赁，现金支出115948加融资租赁资产新增24608为本年经济资本开支140556。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 532.60 |
| 基期输入 USD million / million shares | {"revenue": 331839.0, "net_debt": 30045.0, "diluted_shares": 7453.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.31782809272571366, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## MSFT · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 143.02 | -73.15 | 8.00 | 42.00 | 10.50 | 76.13 |
| 基准 | 266.55 | -49.95 | 14.00 | 47.00 | 9.50 | 81.05 |
| 乐观 | 484.83 | -8.97 | 20.00 | 52.00 | 8.50 | 84.97 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-26T23:19:11.869016+00:00", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 249.09 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.38872287181370735, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.37 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -64.90 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -4.43 | 18.00 | 22.00 | 9.00 | 86.04 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-26T23:19:14.551453+00:00", "latest_filing_date": "2026-07-23"} |
| 观测财务数据 | {"ttm_revenue_million": 445867.0, "revenue_quarters": [{"end": "2025-09-30", "value": 102346000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 113829000000, "filed": "2026-02-05", "duration_days": 92}, {"end": "2026-03-31", "value": 109896000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 119796000000, "filed": "2026-07-23", "duration_days": 91}], "cash_million": 55911.0, "liquid_investments_million": 186563.0, "debt_million": 100164, "finance_lease_million": 2590.0, "diluted_shares_million": 12309.0, "latest_operating_income_million": 40770.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 119796.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。优先股按完全转换处理：季度稀释股数12309减已计入的16，再加合同最大转换股数54.45825；不再扣19000优先股本金。未来3年优先股息按年1203.125、10%折现约2991.99计入权益桥调整，此为保守假设；capped call 未赋值。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | {"preferred_coupon_pv_million": 2991.9938016528904, "discount_rate": 0.1, "years": 3} |
| 价格 USD | 316.80 |
| 基期输入 USD million / million shares | {"revenue": 445867.0, "net_debt": -136728.0061983471, "diluted_shares": 12347.45825, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.37148795242655386, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## GOOGL · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 66.88 | -78.89 | 7.00 | 31.00 | 11.00 | 79.41 |
| 基准 | 131.94 | -58.35 | 13.00 | 36.00 | 10.00 | 82.80 |
| 乐观 | 250.29 | -20.99 | 19.00 | 41.00 | 9.00 | 85.75 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-26T23:19:17.488436+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 10月22日新10-Q已核验；多年承诺与受限资金已记录，但完整融资租赁负债及资产新增口径未齐，不将不同承诺简单当现有债务，暂停精确FCFF反推。 26日新融资公告已核验；强制转换优先权益、远期发行及潜在ATM条款未齐，额外保留稀释缺口。 |

## 反弹续航：先守住，再扩散

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 26日收盘突破第一层价位；27–29日财报与政策 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP"] |
| 确认条件 | 下一交易日回踩QQQ709.30、SMH533.34、SPY763.47后收复/守住，RSP参与；再突破26日高点QQQ715.25、SMH545.34、SPY767.73并守住，才提高可信度。 |
| 失效条件 | 跌回第一层下方且反抽失败则降级；QQQ705.58/SMH530.20（26日低点）再失守，修复进一步受损；更大结构底部仍看23日低点。 |
| 观察期限 | 未来1–3交易日 |
| 反证 | QQQ量能不足均量，META/GOOGL弱，QQQ734.02与SMH582.63的20日线尚远。 |
| 状态 | 首个收盘确认，回踩与趋势反转未确认 |

## 软件云延续而非追高

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 微软28日、Amazon29日财报 |
| 关联标的 | ["IGV", "SKYY", "MSFT"] |
| 确认条件 | IGV回踩仍守26日低点109.69及动态20日线108.88附近，突破111.88后不快速跌回；云增长和现金回报指引支持。 |
| 失效条件 | 相对SPY转弱，109.69反抽失败且20日线失守；经营指引转弱。 |
| 观察期限 | 本周 |
| 反证 | IGV当日量能0.73倍、SKYY0.64倍；财报跳空可越过止损价。 |
| 状态 | 相对强势观察 |

## 能源只做有供给证据的强势

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 地缘、航运和油价波动 |
| 关联标的 | ["XLE", "XOP", "OIH"] |
| 确认条件 | XLE守68.62（26日低点），相对SPY继续强；独立供应证据与油价同向。 |
| 失效条件 | 跌破68.62反抽失败或实际供应恢复、风险溢价持续回落。 |
| 观察期限 | 未来一周 |
| 反证 | 停火合约变贵、油价边际回落；高位追涨容易被消息反转。 |
| 状态 | 跨期强势但事件敏感 |

## AI融资消息需要每股现金回报确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | Anthropic申报、Broadcom盘后融资、Meta定价待定 |
| 关联标的 | ["NVDA", "AVGO", "META"] |
| 确认条件 | 融资条件落地、交付可核验，随后资本回报/每股自由现金流改善；META先收复642.62再观察，不仅看盘后反抽。 |
| 失效条件 | META失守627.80且反抽失败，或融资条款恶化、投入与经营现金流缺口扩大。 |
| 观察期限 | 未来两日价格；下一财报周期经营 |
| 反证 | META26日放量至1.60倍均量下跌，融资增加并不保证股价上升。 |
| 状态 | 分化，不能一概追AI |

## 跨期比较与上期剧本复核

对照26日晚报（截止12:09UTC）：QQQ709.30、SMH533.34、SPY763.47三项第一层价位现已收盘越过，评级由待验证盘前反弹上调为有首个收盘支持的修复。未核验逐笔常规VWAP、回踩序列和完整广度，不宣称全部条件已满足；QQQ/SMH仍低于20/50日线。Meta昨晚盘前+1.78%转为收盘−1.88%，否定了“融资消息必然带来股价持续上涨”的推断。XLE盘前弱转收涨，原先能源回吐观察未被收盘确认。Anthropic公开S-1从待核验变为已核验。同规则合约：2589812：95.05%→93.15%（-1.90个百分点）；4641065：85.5%→89.5%（+4.00个百分点）；2176270：11.5%→11.5%（+0.00个百分点）；3501950：0.4%→0.35%（-0.05个百分点）；3215008：75.5%→74.5%（-1.00个百分点）；4951227：46%→45.5%（-0.50个百分点）；691340：9.55%→9.55%（+0.00个百分点）；2252540：12.5%→12.5%（+0.00个百分点）；5778671：85%→86%（+1.00个百分点）；4838928：22.5%→22.5%（+0.00个百分点）；5401795：24%→20%（-4.00个百分点）；2413330：91.5%→94.5%（+3.00个百分点）。合约价差和取证时点见详情，不能把变化当独立事实。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-23/20261026T120957.233325Z/evidence.json",
    "baseline_cutoff": "2026-10-26T12:09:51.062988+00:00",
    "close_change_pct": {
      "SPY": 0.7105576038835215,
      "QQQ": 1.107323611957134,
      "IWM": 0.44967914211242466,
      "RSP": 0.34635634213258104,
      "GLD": 0.3300570145398307,
      "GC=F": 0.4141844372546055,
      "CL=F": -1.8882511974721905,
      "BZ=F": -5.637424402191971,
      "TLT": 0.4180034209403827,
      "UUP": 0.17265589084907162,
      "HYG": 0.19467085080271396,
      "LQD": 0.16369588006077684,
      "^VIX": -5.449878312142642,
      "^VIX3M": -2.6367139660577577,
      "^VVIX": -7.5387391733185645,
      "^MOVE": -1.0827596209687762,
      "NVDA": 2.3890752397295545,
      "MSFT": 1.5423854015536254,
      "AMZN": 0.4395146523752613,
      "GOOGL": -1.064927314295805,
      "META": -1.8766919252791836,
      "CRWV": 1.7608518587812982,
      "MU": 2.9798900094374803,
      "DRAM": 2.6986834269079774,
      "VRT": 2.809793767642388,
      "XLK": 1.6864114330245927,
      "XLE": 0.44713334834343144,
      "XLF": 0.2146671352579732,
      "XLI": 1.421462559887643,
      "XLV": 0.0,
      "XLP": -0.33990827611215524,
      "XLY": 1.0256442774177366,
      "XLC": -1.5733140256845468,
      "XLU": -0.02350125918169077,
      "XLRE": 0.5402855153515462,
      "XLB": 0.13642504960185153,
      "SMH": 2.735201550885691,
      "IGV": 0.7233954952973631,
      "XOP": 1.5717180477828885,
      "OIH": 1.268373447432758,
      "ITA": 2.4378223007097466,
      "ARKX": 1.1058978619925997,
      "KRE": 0.3726252772183525,
      "SKYY": 1.4937858454126651
    },
    "quote_change_pct": {
      "SPY": {
        "change_pct": 0.1730262554234585,
        "from_observed_at": "2026-10-26T12:05:11+00:00",
        "to_observed_at": "2026-10-26T23:14:16+00:00"
      },
      "QQQ": {
        "change_pct": 0.3934786900967602,
        "from_observed_at": "2026-10-26T12:05:20+00:00",
        "to_observed_at": "2026-10-26T23:17:45+00:00"
      },
      "SMH": {
        "change_pct": 1.3813084112149543,
        "from_observed_at": "2026-10-26T12:05:12+00:00",
        "to_observed_at": "2026-10-26T23:15:37+00:00"
      },
      "META": {
        "change_pct": -3.254324237379569,
        "from_observed_at": "2026-10-26T12:05:19+00:00",
        "to_observed_at": "2026-10-26T23:14:04+00:00"
      },
      "MSFT": {
        "change_pct": 0.9981937446525313,
        "from_observed_at": "2026-10-26T12:05:22+00:00",
        "to_observed_at": "2026-10-26T23:17:35+00:00"
      },
      "AMZN": {
        "change_pct": -0.4274936932078699,
        "from_observed_at": "2026-10-26T12:04:55+00:00",
        "to_observed_at": "2026-10-26T23:17:37+00:00"
      },
      "NVDA": {
        "change_pct": 1.2340981111278904,
        "from_observed_at": "2026-10-26T12:05:20+00:00",
        "to_observed_at": "2026-10-26T23:18:12+00:00"
      },
      "GOOGL": {
        "change_pct": -1.5415194716208336,
        "from_observed_at": "2026-10-26T12:05:09+00:00",
        "to_observed_at": "2026-10-26T23:18:13+00:00"
      },
      "IWM": {
        "change_pct": -0.0759136753063605,
        "from_observed_at": "2026-10-26T12:05:14+00:00",
        "to_observed_at": "2026-10-26T23:17:05+00:00"
      },
      "GLD": {
        "change_pct": -0.15139352897854952,
        "from_observed_at": "2026-10-26T12:04:39+00:00",
        "to_observed_at": "2026-10-26T23:07:54+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.040000000000000036,
        "unit": "percent",
        "observation_date": "2026-10-23"
      },
      "BAMLH0A0HYM2": {
        "change": -0.020000000000000018,
        "unit": "percentage_points",
        "observation_date": "2026-10-23"
      },
      "BAMLC0A0CM": {
        "change": 0.020000000000000018,
        "unit": "percentage_points",
        "observation_date": "2026-10-23"
      },
      "DGS10": {
        "change": 0.040000000000000036,
        "unit": "percent",
        "observation_date": "2026-10-23"
      },
      "DFII10": {
        "change": 0.020000000000000018,
        "unit": "percent",
        "observation_date": "2026-10-23"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-26"
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
        "change": -83.41177368164062,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_ACT": {
        "change": -80.4246826171875,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_THREAT": {
        "change": -122.77737426757812,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_MA7": {
        "change": 3.4905548095703125,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_MA30": {
        "change": -0.572418212890625,
        "unit": "index",
        "observation_date": "2026-10-26"
      }
    },
    "event_probability_change": {
      "2589812": {
        "status": "comparable",
        "change_pp": -1.9000000000000017
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 4.0000000000000036
      },
      "3501950": {
        "status": "comparable",
        "change_pp": -0.05
      },
      "4951227": {
        "status": "comparable",
        "change_pp": -0.5000000000000004
      },
      "3215008": {
        "status": "comparable",
        "change_pp": -1.0000000000000009
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5778671": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5401795": {
        "status": "comparable",
        "change_pp": -3.9999999999999982
      },
      "2413330": {
        "status": "comparable",
        "change_pp": 2.9999999999999916
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
    "event": "下一交易日常规开盘：检验反弹回踩",
    "date": "2026-10-27T09:30:00-04:00",
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
    "event": "Anthropic定价/首日挂牌与Meta正式发行定价：未定，不把合约截止当发生日",
    "date": null,
    "source": "https://www.anthropic.com/news/s1-sec"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| anthropic-public-s1-20261026 | 公开S-1已提交；价格和数量未定，不等于上市完成。净亏损与经营亏损、现金流必须区分。 | 缺失 | [{"source": "https://www.anthropic.com/news/s1-sec", "published_at": null, "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |
| broadcom-anthropic-finance-20261026 | 盘后宣布630亿美元SPV算力融资，2027年预计交付；不是26日收盘上涨的已知原因。 | 缺失 | [{"source": "https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce", "published_at": "2026-10-26T20:15:00+00:00", "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |
| meta-financing-20261026 | 约350亿美元组合发行与未来ATM计划属于融资渠道，不是已经全部收到950亿美元；股价收跌。 | 缺失 | [{"source": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "published_at": null, "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |
| microsoft-voluntary-exit-20261026 | 官方推出自愿离职计划，适用于部分团队/国家，不代表6万人已离职或利润改善已兑现。 | 缺失 | [{"source": "https://blogs.microsoft.com/blog/2026/10/26/introducing-a-voluntary-exit-offer/", "published_at": null, "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |
| cadence-q3-20261026 | 盘后Q3收入16.33亿美元、积压订单82亿美元，全年展望上调；利润率同比下滑。 | 缺失 | [{"source": "https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Third-Quarter-2026-Financial-Results/default.aspx", "published_at": null, "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |
| spce-schedule-20261026 | 盘后公司新闻稿：28日计划转场试飞准备，商业航班预期延至2027年二季度。 | 缺失 | [{"source": "https://www.stocktitan.net/news/SPCE/virgin-galactic-sets-october-28-for-lead-delta-class-spaceship-s-ysvpiwc45syk.html", "published_at": "2026-10-26T21:58:00+00:00", "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |
| oil-20261026 | Reuters26日12:39GMT报道油价边际回落，设施与供应风险仍在；不冒充收盘结算。 | 缺失 | [{"source": "https://finance.yahoo.com/news/oil-prices-down-almost-1-232445179.html", "published_at": "2026-10-26T12:55:00+00:00", "retrieved_at": "2026-10-26T23:23:01.505055+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN接口418、官方页面robots不可读；不以tc温度或加密恐贪代替。",
  "完整成分广度、涨跌家数、新高新低与历史盈利一致预期修正缺失；RSP及19ETF仅为代理。",
  "逐笔常规VWAP与回踩路径未核验，本次仅确认收盘突破；不由日线反推盘中承接。",
  "19ETF当期净申赎及完整拆分调整份额序列缺失；ICI窗口截至14日、SMH页面至23日，不称当日主力流入。",
  "tc新闻high限50且has_more；主题补查官方资料仍非完整新闻库。",
  "tc报价时戳不能确认为成交时点，本次独立Yahoo分钟包替代；RSP、XLE、TLT等盘后稀疏报价明确陈旧。",
  "连续期货日线可能已进入下一交易日夜盘、成交量异常小；不把其收益与量能作26日官方结算分析。Brent与Reuters近月未对齐。",
  "CME官方页面可达但未取得带时点的当期概率矩阵；Polymarket不是FedWatch。",
  "META租赁新增、净债务桥与26日新优先权益/稀释条款未齐，估值保持不可用。",
  "DRAM上市历史不足200日；交易所全面广度及部分Polymarket查询截断。",
  "部分官方新闻网页直接打开失败，但官方索引摘要可读；Anthropic财务数字另外直接核验SEC原文，原文仅保存在results。",
  "NVIDIA8月官方实录预告11月17日，与tc日历25日冲突；保留官方预告，临近仍须重核，不当作新确认公告。",
  "原始采集存在请求失败，见采集质量记录",
  "META 估值: 10月22日新10-Q已核验；多年承诺与受限资金已记录，但完整融资租赁负债及资产新增口径未齐，不将不同承诺简单当现有债务，暂停精确FCFF反推。 26日新融资公告已核验；强制转换优先权益、远期发行及潜在ATM条款未齐，额外保留稀释缺口。",
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
  "tc 报价质量 stale: RSP, IGV, XLE, XLF, TLT；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.RSP.value, quotes.IGV.value, quotes.XLE.value, quotes.XLF.value, quotes.TLT.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.anthropic.com/news/s1-sec",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://investors.broadcom.com/news-releases/news-release-details/bank-america-blackstone-citi-and-morgan-stanley-announce",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Third-Quarter-2026-Financial-Results/default.aspx",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://blogs.microsoft.com/blog/2026/10/26/introducing-a-voluntary-exit-offer/",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://finance.yahoo.com/news/oil-prices-down-almost-1-232445179.html",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.stocktitan.net/news/SPCE/virgin-galactic-sets-october-28-for-lead-delta-class-spaceship-s-ysvpiwc45syk.html",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.microsoft.com/en-us/investor/faq",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.bea.gov/news/schedule/full",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-to-Report-Fiscal-First-Quarter-2027-Financial-Results-on-October-27-2026/default.aspx",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "本次核验；事件时间未确认则留空；网页/搜索索引时点不等于财务观测日。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-26T23:23:01.505055+00:00",
    "note": "公开备用分钟价，实际分钟时戳见quotes；涨跌幅相对26日常规收盘，仅表示盘后变化。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
