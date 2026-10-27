# 每日交易总结 · 2026-10-26

## 一分钟读懂 · Agent 摘要

### 当前判断

反弹延续，但还不能确认趋势反转。半导体盘前领先，微软与Meta没有同步走强；开盘后的承接比盘前涨幅更重要。

### 与上次相比

相较早报，Meta组合发行已定价，英伟达拟投30亿美元；康宁光通信收入增长提供需求证据。沙特石油枢纽附近遇袭，但尚无已核验的供应损失规模。

### 最重要的信号

- 约11:59UTC：SMH盘前+1.17%、QQQ+0.37%、SPY+0.27%；MSFT−0.71%、META−0.10%。
- 26日收盘突破仍有效，但QQQ量能仅均量0.89倍、等权落后；不能把盘前芯片领涨当全面确认。
- Meta普通股发行价625美元是事件参照，不是保底；融资支持与未来每股现金回报要分开。

### 接下来观察

- 开盘看QQQ715.25、SMH545.34、SPY767.73能否一起突破并回踩守住，等权也应参与。
- 若跌回QQQ709.30、SMH533.34、SPY763.47且反抽失败，反弹降级；不靠一个标的孤立拉升加仓。
- 今晚STX、明日Fed及微软、29日GDP/PCE与Amazon/Sandisk，优先观察承接与指引。

### 不要忽略

盘前薄量且部分报价滞后；没有今天常规VWAP和完整广度。信用、申赎滞后，CNN缺失，不用标题或低流动性盘口替代事实。

## 研究结论

10月27日晚报：半导体盘前延续反弹，但微软、Meta偏弱，仍是分化修复。Meta融资进入定价、英伟达拟参与投资；资金可得性改善不等于稀释和现金回报问题解除。今晚先验证昨日高点的突破承接。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-26 → 2026-10-26（纽约交易日） |
| 截止·纽约 | 2026-10-27T08:08:06.630140-04:00 |
| 截止·北京 | 2026-10-27T20:08:06.630140+08:00 |
| 实际生成时间 | 2026-10-27T12:08:06.827962+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-10-27 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-26/20261026T232315.247706Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-27T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-27T12:00:13.022565+00:00 / 2026-10-27T12:00:13.022565+00:00 | Gamma retrieval snapshot, not last trade timestamp; settlement reviewed |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-10-27T12:00:16.785336+00:00 / 2026-10-27T12:00:16.785336+00:00 | Gamma retrieval snapshot, not last trade timestamp; settlement reviewed |

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
| prices.SPY.volume_vs_previous20_ratio | 0.78 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
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
| prices.QQQ.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
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
| prices.GC=F.value | 4,038.40 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 0.76 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -2.93 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -3.12 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -1.67 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 0.05 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -2.78 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -3.09 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -4.38 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,148.76 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,333.89 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,530.79 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -2.66 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -6.82 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.87 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 69.85 | USD_per_troy_ounce | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.73 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.04 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.18 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 101.76 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -1.46 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -1.83 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 9.89 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 20.18 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -2.17 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -1.69 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 9.92 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 17.47 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 95.19 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 93.32 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.51 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 6.91 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 9.05 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 19.01 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.36 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.29 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -3.85 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.19 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 115.81 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -0.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 5.71 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 10.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 28.51 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -1.49 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 5.86 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 10.03 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 25.80 | pp | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 106.39 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 101.38 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 91.44 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 8.85 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 14.24 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 26.65 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.93 | USD_per_barrel | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.39 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -0.78 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.72 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
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
| prices.TLT.volume_vs_previous20_ratio | 0.50 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
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
| prices.^MOVE.distance_sma50_pct | 15.52 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
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
| prices.MSFT.volume_vs_previous20_ratio | 0.93 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
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
| prices.AMZN.volume_vs_previous20_ratio | 0.91 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
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
| prices.XLE.atr14_pct | 2.13 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.01 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
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
| prices.XLI.volume_vs_previous20_ratio | 0.89 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
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
| prices.XLP.volume_vs_previous20_ratio | 0.97 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
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
| prices.XLRE.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
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
| prices.XOP.atr14_sma | 5.08 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
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
| prices.OIH.atr14_sma | 11.71 | USD_per_share | 2026-10-26 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
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
| macro.CBOE_VIX.value | 18.39 | index | 2026-10-26 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 165.25 | index | 2026-10-26 | ok | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 149.77 | index | 2026-10-26 | ok | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 187.38 | index | 2026-10-26 | ok | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 181.42 | index | 2026-10-26 | ok | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 175.44 | index | 2026-10-26 | ok | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 767.44 | USD_per_share | 2026-10-27T11:59:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 714.82 | USD_per_share | 2026-10-27T11:59:37+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 547.95 | USD_per_share | 2026-10-27T11:59:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.RSP.value | 218.00 | USD_per_share | 2026-10-27T11:07:39+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.META.value | 629.96 | USD_per_share | 2026-10-27T11:59:46+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MSFT.value | 528.80 | USD_per_share | 2026-10-27T11:59:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.AMZN.value | 249.90 | USD_per_share | 2026-10-27T11:58:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.NVDA.value | 217.51 | USD_per_share | 2026-10-27T11:58:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.GOOGL.value | 317.76 | USD_per_share | 2026-10-27T11:59:27+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 111.06 | USD_per_share | 2026-10-27T11:26:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.XLE.value | 69.30 | USD_per_share | 2026-10-27T11:57:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 56.23 | USD_per_share | 2026-10-27T11:52:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.IWM.value | 277.81 | USD_per_share | 2026-10-27T11:59:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.GLD.value | 367.59 | USD_per_share | 2026-10-27T11:54:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.TLT.value | 81.76 | USD_per_share | 2026-10-27T11:57:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| premarket.CL_F.value | 101.10 | USD/barrel | 2026-10-27T11:49:52+00:00 | lagged | Yahoo延迟分钟价；实际时戳不是请求时刻。期货连续/近月合约未对齐，不作官方结算或拼接收益；VIX盘前值不与26日VIX3M拼接期限结构 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| premarket.BZ_F.value | 109.95 | USD/barrel | 2026-10-27T11:49:52+00:00 | lagged | Yahoo延迟分钟价；实际时戳不是请求时刻。期货连续/近月合约未对齐，不作官方结算或拼接收益；VIX盘前值不与26日VIX3M拼接期限结构 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| premarket.ES_F.value | 7,733.25 | index points | 2026-10-27T11:49:51+00:00 | lagged | Yahoo延迟分钟价；实际时戳不是请求时刻。期货连续/近月合约未对齐，不作官方结算或拼接收益；VIX盘前值不与26日VIX3M拼接期限结构 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| premarket.NQ_F.value | 29,546.00 | index points | 2026-10-27T11:49:51+00:00 | lagged | Yahoo延迟分钟价；实际时戳不是请求时刻。期货连续/近月合约未对齐，不作官方结算或拼接收益；VIX盘前值不与26日VIX3M拼接期限结构 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| premarket.VIX.value | 17.87 | index points | 2026-10-27T11:44:46+00:00 | lagged | Yahoo延迟分钟价；实际时戳不是请求时刻。期货连续/近月合约未对齐，不作官方结算或拼接收益；VIX盘前值不与26日VIX3M拼接期限结构 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

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
        "change": 0.4060195922852472,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.0816238403320995,
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
        "change": 0.6866064469665423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4581465264713813,
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
        "change": -0.03925260448631407,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.14001110698940977,
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
        "change": 0.46918060302732556,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3769885253906295,
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
        "change": 1.0806263810646533,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2848221742395527,
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
        "change": 0.07588677671052324,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.13161263640670207,
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
        "change": 0.10230133056643353,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5944820404052962,
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
        "change": 0.4105078159879483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.849141651960362,
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
        "change": -0.06142970493861588,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2335706438337053,
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
        "change": -0.028166964036023368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.11366739859440411,
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
        "change": -0.20677671784824203,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1469642375548451,
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
        "change": 0.115760421752924,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.6016126251220726,
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
        "change": 0.304892322315764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.5844970816382808,
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
        "change": -0.0149993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.050000871930803825,
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
        "change": -0.010224111403006275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.006077129428326833,
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
        "change": 0.15260956901547507,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15609981929964167,
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
        "change": -0.017859322684151913,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.32713753836495485,
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
        "change": -0.009635033990622377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.13127855687299572,
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
        "change": -0.45979591381064866,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.11134203701063627,
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
        "change": 30.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -121.7001953125,
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
        "change": 2.0539731419754514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2632572084438132,
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
        "change": 1.2170400527644731,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.1975956847158695,
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
        "change": 4.131604601680694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.9863364201818663,
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
        "change": 0.5784090054646973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.8639945240789286,
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
        "change": 0.8211301887580236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9758873502203058,
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
        "change": 0.9321109374579861,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.546160456241043,
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
        "change": 2.687614749126311,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1101171479195084,
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
        "change": 0.5880254742539952,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.587514734768037,
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
        "change": -6.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -54.155004882813046,
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
        "change": -7.977998046874745,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -35.73400390625011,
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
        "change": -2.111501464843059,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -9.005502929687282,
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
        "change": 0.886275307303741,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.6413783101199786,
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
        "change": 0.8736808489529624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.0231170060011516,
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
        "change": 0.7143780577737129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.503933229848853,
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
        "change": -2.0428292410714306,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9071393694196388,
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
        "change": -0.06413260931216946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.00475568497404355,
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
        "change": 0.6492400968122762,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.590578576615087,
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
        "change": -0.24265198274217958,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.25756658321713555,
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
        "change": -1.5099945068359375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9000015258789062,
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
        "change": -5.2824238915461175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.6808972525352646,
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
        "change": -3.6670483646889296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -12.415385263281554,
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
        "change": -1.859954076156356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.6648202500337597,
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
        "change": -3.3592376226011744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.11661295880441,
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
        "change": -6.515266844763546,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.968267110758772,
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
        "change": -3.9519774799954166,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -13.763950034806728,
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
        "change": -3.303943928710739,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7886009777714023,
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
        "change": -3.349621153811878,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.393092748115301,
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
        "change": 0.45800018310546875,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8534999847412195,
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
        "change": 0.3872000122070318,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.823800201416006,
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
        "change": 0.2200000190734812,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.084600009918205,
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
        "change": -2.1109137569164558,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.158801182382743,
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
        "change": -2.0792601996656455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -4.250454337702481,
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
        "change": -2.077472626807996,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.779524695429881,
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
        "change": -0.017857687813894962,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4257136753627231,
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
        "change": 0.045407568321658154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4892799850462972,
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
        "change": -1.4268113774073887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.7953335472034149,
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
        "change": 0.11044103940030614,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8132401052197039,
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
        "change": -0.910003662109375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.2599945068359375,
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
        "change": -3.9165231980182624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4974716281353153,
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
        "change": -0.5300309212751486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.995104277898797,
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
        "change": -1.8846059124114412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8230995195836375,
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
        "change": -2.5954497031338555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 15.311549682539873,
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
        "change": -5.14936615123569,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.7848414863588227,
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
        "change": -0.8149600365816356,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.6465395063736237,
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
        "change": -3.328595764965824,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.053119752678719934,
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
        "change": -2.585833234344559,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 16.588029471850763,
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
        "change": 0.5264999389648466,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.238999938964838,
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
        "change": 0.545800018310544,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.442199859619137,
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
        "change": 0.2690999794006359,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.2907499885559162,
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
        "change": -1.4009565517993714,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.670377571721727,
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
        "change": -1.5208633071865023,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 3.5074597091894866,
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
        "change": -1.3718961766589146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 5.130538407955964,
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
        "change": -0.05714307512555772,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07285690307617188,
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
        "change": -0.02252901746500635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.127196448591413,
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
        "change": -0.7796467208637803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4974716281353153,
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
        "change": -0.2486645033432423,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2133713172737064,
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
        "change": -0.013629379272472875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.0852678680419956,
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
        "change": 0.42416391683348653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7627522142945065,
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
        "change": -0.19992784598778662,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.11632489450648092,
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
        "change": -0.07700926988667645,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.06247788167520196,
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
        "change": -0.0011375427246065328,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.007829132080075851,
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
        "change": 0.19401311660163234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.48492875420363957,
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
        "change": -0.23846303199908847,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.18086664605521846,
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
        "change": -0.012008514404300286,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.07097019195556697,
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
        "change": 0.17164702111543972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.1415563196938816,
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
        "change": -0.12477370162573209,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.02843889519079179,
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
        "change": -1.1199951171875,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8899993896484375,
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
        "change": 2.219893893636715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2819395348392493,
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
        "change": -1.3073757771442596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.9953957411522394,
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
        "change": 7.662304608751002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -19.1721252079619,
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
        "change": -6.709985289932916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.060853265846248,
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
        "change": 0.9870509404192873,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.5693093930627566,
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
        "change": -1.5923048924507466,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -3.403430100576788,
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
        "change": 7.49775785390292,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -17.768001693721715,
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
        "change": -5.717701757846402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 6.703484511630414,
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
        "change": 0.3095001220703182,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.7095001220703097,
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
        "change": 0.6591999816894543,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.865000000000009,
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
        "change": 0.1802000045776424,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9348999786377021,
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
        "change": -1.3816311367891632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.7715511079729684,
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
        "change": -2.142999335278173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.8270491800584274,
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
        "change": -1.772762212335735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.46463610155698376,
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
        "change": -0.3521428789411267,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.020000457763671875,
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
        "change": -0.28444444907922595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06546402196638113,
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
        "change": -0.985911207950096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7834501774673814,
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
        "change": 0.15696014404298353,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7072032928466854,
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
        "change": 2.3964171847801197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.9075246536374371,
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
        "change": 0.10327350541865876,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.07888189401383527,
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
        "change": 0.2875201416015898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.3608549499512037,
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
        "change": 1.7774555144802058,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.594925121382019,
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
        "change": 0.2933828156400198,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1257934753840294,
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
        "change": -0.14571380615234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.32142530168805816,
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
        "change": -0.07099980451202947,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2642849441995061,
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
        "change": 0.2066307328576079,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.655352726455081,
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
        "change": -0.04004058837892899,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.22956817626953807,
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
        "change": -0.9891336552360741,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -8.098637659400564,
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
        "change": 0.2761328448985213,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.222128647942896,
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
        "change": -0.06920532226570231,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.288062744140575,
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
        "change": -1.8983188887276126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -11.906759535952604,
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
        "change": 0.641431535993302,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.516427176339285,
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
        "change": 0.17697382685970897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0766417856659798,
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
        "change": 0.857542706366855,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.8572531779117909,
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
        "change": 0.052856990269251725,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5289284842354904,
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
        "change": -0.10989088324844687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.007884360042855,
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
        "change": 0.40544742792172617,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -1.2207548763305596,
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
        "change": 2.8845916748047102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 14.055530548095703,
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
        "change": 3.0881958129129963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.565049281115293,
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
        "change": 0.05675210524763585,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.10563726420081487,
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
        "change": -0.019999912806919706,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.25214358738490494,
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
        "change": -0.19354237168280175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.5217123480903512,
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
        "change": -0.17066213329261137,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.3251185762555937,
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
        "change": 0.19555641174315497,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.745810852050738,
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
        "change": 1.9759717109727788,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -2.5532591320102433,
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
        "change": -0.3765845816665625,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.012351502114800628,
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
        "change": 0.2129919815063488,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.0107028198242176,
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
        "change": 1.6971132875686514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.4529756134384435,
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
        "change": -0.01644978787907969,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.2693521000471152,
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
        "change": 0.00785718645368294,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.16642897469656814,
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
        "change": 0.0018258869784113507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1877672418084404,
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
        "change": -0.1996294165758854,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.11768876181318821,
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
        "change": 0.003977394104005327,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.023654594421387287,
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
        "change": 0.2170647463392461,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.7532418880106926,
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
        "change": -0.151624452209703,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.10755231277615174,
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
        "change": 0.0402893829345885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2037730407714946,
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
        "change": 1.3346303448668935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.04802820913845096,
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
        "change": -0.07009980544388072,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.08697358133712452,
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
        "change": -0.03571428571428559,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.21500069754464324,
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
        "change": -0.01992095379153369,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.08665185300935407,
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
        "change": 0.001828254665927842,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.19249331898747024,
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
        "change": 0.05501281738281705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3041285324096634,
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
        "change": -0.42954819392477805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.516558031808878,
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
        "change": -0.5026950659086604,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1751540314896749,
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
        "change": -0.039502906799313564,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.13205551147460426,
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
        "change": 1.039575933249448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05989496300523589,
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
        "change": 0.04528722775563876,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.026035507602909513,
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
        "change": -0.0628437423706032,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.22655696868896769,
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
        "change": -1.4215874615648998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -5.343936998292664,
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
        "change": 0.07214300973074783,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.10571452549525673,
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
        "change": 0.09510962996991945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1923390018485136,
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
        "change": 0.6030165665496254,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.7800945936464769,
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
        "change": 0.0070926094055181466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.01778961181640426,
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
        "change": -0.03859564691243156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.679613740143949,
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
        "change": -0.06214278084891178,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.057856968470982095,
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
        "change": -0.14566657324658694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.1821962199731313,
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
        "change": -0.12264430525588393,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.29608834862208905,
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
        "change": 0.016556663513178194,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.07497035980224354,
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
        "change": 0.4998189919240392,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.473981473347764,
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
        "change": -0.05985960547411784,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.16521758935856878,
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
        "change": -0.013571602957589302,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.07285772051130024,
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
        "change": -0.028198858497562318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.15381612087790808,
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
        "change": 0.1154179493837052,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.08681079603209274,
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
        "change": 0.3047706635343911,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1526767830834328,
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
        "change": -0.11045246494839456,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05110015067942586,
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
        "change": 0.3902199172973724,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8809444808960052,
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
        "change": 1.6066228163009981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 1.8636480066500667,
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
        "change": 0.18142918178013367,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4528601510184149,
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
        "change": 0.05094701616829056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15996852882037116,
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
        "change": -0.07044288758759187,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2121437084958333,
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
        "change": 0.1528560093470972,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 2.3721422467912934,
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
        "change": 0.0015464714777837507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4853381246516104,
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
        "change": -1.333285108059082,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.1571877256223576,
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
        "change": -0.09849990844725198,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.5194595336914176,
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
        "change": 2.1896429495746776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05674935578791107,
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
        "change": 0.13285718645368316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.9292842320033485,
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
        "change": 0.016052669728357838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.4531682576391216,
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
        "change": 0.15320372362554158,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.05431545791968628,
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
        "change": -0.039135455317951484,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.006039853112136617,
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
        "change": 0.029088745117192616,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.15353252410888274,
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
        "change": 0.3417826860032447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 4.726014574382864,
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
        "change": -0.008571079799107206,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.013570513044084853,
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
        "change": -0.018390323704609024,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.06863022548386888,
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
        "change": -0.1587057133276888,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.2066612011222102,
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
        "change": 0.038572038922991325,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.3428595406668524,
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
        "change": -0.01897016018210973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.05953189781791446,
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
        "change": -2.1579334741253815,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.13530200258660552,
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
    "available_prior_observations": 6,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -1.0599999999999987,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.05000000000000071,
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
| 判断变化原因 | 相较早报：无新完整日线；芯片盘前越昨高、MSFT/META未同步，Meta定价和融资合作新增核验；常规承接仍待验证。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 反弹仍有第一层收盘支持，盘前芯片增强但未全面扩散，维持修复评级。 |
| 反证与缺口 | MSFT盘前逆势、等权报价陈旧；QQQ昨量仅0.89倍，仍低于20日线734.02。 |
| 确认条件 | 27日常规时段QQQ715.25、SMH545.34、SPY767.73同步突破，回踩不快速跌回，RSP/IWM参与且可核验常规VWAP守住；未取得VWAP时不写条件已满足。 |
| 失效条件 | 跌回QQQ709.30、SMH533.34、SPY763.47且反抽失败则降级；再失守26日低点QQQ705.58/SMH530.20/SPY761.63则修复进一步受损。 |
| 观察期限 | 未来1–5交易日 |
| 条件式指导 | 等待确认后分批试探，不把一次拉升当趋势。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较早报：无新完整日线；芯片盘前越昨高、MSFT/META未同步，Meta定价和融资合作新增核验；常规承接仍待验证。 |

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
| 判断变化原因 | 相较早报：无新完整日线；芯片盘前越昨高、MSFT/META未同步，Meta定价和融资合作新增核验；常规承接仍待验证。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 融资可得性和光通信需求有新增证据，但资本支出回报与稀释仍待验证。 |
| 反证与缺口 | 供货商投资客户与远期融资不等于独立需求或当日现金到账。 |
| 确认条件 | 企业自由现金流、融资与价格承接同步改善。 |
| 失效条件 | 订单/指引下修、资本投入长期超过现金生成且融资收紧。 |
| 观察期限 | 下一季度并每日跟踪风险 |
| 条件式指导 | 用公司整体FCFF情景，保留META输入缺口。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较早报：无新完整日线；芯片盘前越昨高、MSFT/META未同步，Meta定价和融资合作新增核验；常规承接仍待验证。 |

## AI融资可得性改善，稀释压力未消失 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Meta公司稿：125亿美元强制可转优先权益、250亿美元普通股远期发行已定价，普通股625美元；NVIDIA官方宣布拟投资30亿美元并扩大Muse合作。 |
| 事实：市场反应 | NVDA盘前约+0.70%、SMH+1.17%，META约−0.10%、MSFT−0.71%，未见全链条同向。 |
| 推断：解释 | 推断：芯片需求预期得到支持，但出资方未来股本和每股回报仍受检验；供应商参与客户融资不是独立终端盈利证明。 |
| 受益篮子 | ["NVDA", "SMH", "光互连观察篮子"] |
| 受损篮子 | ["META等资本投入/稀释敏感公司"] |
| 反证 | 375亿美元定价不等于今日现金全部到账，普通股远期结算预计最迟2027年11月；625不是价格下限。 |
| 下一催化剂 | 发行预计29日交割的条件、后续现金流与融资桥；今晚常规价格承接 |
| 证据 | ["https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html", "https://nvidianews.nvidia.com/news/nvidia-and-meta-to-expand-collaboration-on-muse-and-muse-family-of-models-amid-robust-growth"] |

## 光通信增长与软件云分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 康宁公司稿披露Q3核心销售50.8亿美元、同比+19%，光通信收入+44%；Oracle官方新增28日投资者日。 |
| 事实：市场反应 | 软件/云五日IGV+5.09%、SKYY+5.45%，但MSFT盘前−0.71%；GLW最新成交未专门核验，不写已上涨。 |
| 推断：解释 | 推断：基础设施收入有支撑，不能直接推导所有软件公司或客户资本回报同步改善。 |
| 受益篮子 | ["GLW", "IGV", "SKYY", "ORCL观察篮子"] |
| 受损篮子 | ["订单强而现金回报弱者"] |
| 反证 | 康宁核心指标为非GAAP；其光通信增长不代表整个算力产业盈利；微软盘前逆势。 |
| 下一催化剂 | 28日Oracle投资者日与微软财报 |
| 证据 | ["https://www.stocktitan.net/news/GLW/corning-delivers-outstanding-third-quarter-results-ijv492ou5imj.html", "https://investor.oracle.com/investor-news/news-details/2026/ORACLE-INVESTOR-DAY-MEETING-TO-BE-HELD-OCTOBER-28-2026/default.aspx", "https://www.microsoft.com/en-us/investor/faq"] |

## 地缘设施风险与油价反馈不一致 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Reuters转载报道27日沙特控制Ras Tanura油枢纽附近火情，尚无独立核验的供应损失规模。 |
| 事实：市场反应 | 延迟WTI101.10、Brent109.95；XLE盘前约−0.49%，并未给出全面避险追涨信号。 |
| 推断：解释 | 推断：事件存在与损失规模是两件事；需看持续出口、运输与油价，不凭袭击标题追涨。 |
| 受益篮子 | ["供给受损情景下XLE/XOP/OIH"] |
| 受损篮子 | ["高燃料成本行业"] |
| 反证 | Ras Tanura不是Polymarket东西输油管道合约的同一设施；美国伊朗停火条款也不等于所有地区无袭击。 |
| 下一催化剂 | 设施运营、出口量与航运的独立证据 |
| 证据 | ["https://www.moneycontrol.com/world/saudi-arabia-contains-fire-near-ras-tanura-oil-hub-after-attack-article-14061244.html"] |

## 金融与工业：看现金转换和参与面 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 波音27日官方Q3收入约242亿美元、经营现金流15亿美元、自由现金流5亿美元；核心EPS仍为负。 |
| 事实：市场反应 | 26日XLI+1.42%、XLF+0.21%、KRE+0.37%；今晨RSP报价稀疏，无法证明当前广度扩散。 |
| 推断：解释 | 推断：现金转换改善比只有订单标题更有意义，但不能外推到所有工业或银行。 |
| 受益篮子 | ["XLI", "有交付/现金兑现的工业篮子"] |
| 受损篮子 | ["高融资成本或交付不稳公司"] |
| 反证 | 波音仍亏损；今日BA常规价格尚未形成。ICI净发行仍是14日结束的旧窗口。 |
| 下一催化剂 | 波音今日10:30纽约电话会、明日Fed、29日GDP/PCE |
| 证据 | ["https://boeing.mediaroom.com/2026-10-27-Boeing-Reports-Third-Quarter-Results", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## 半导体与存储：财报前修复 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | STX今晚盘后、SNDK29日财报是需求/价格/毛利率验证点；本次未取得中国存储厂商新增量产份额或利润冲击证据。 |
| 事实：市场反应 | SMH盘前547.95已越26日高点545.34，但仍远低于20日线582.63；MU与DRAM26日分别+2.98%、+2.70%。 |
| 推断：解释 | 推断：盘前突破只提升观察优先级，需要常规回踩、成交与财报支撑；NAND、DRAM、HBM分开核验。 |
| 受益篮子 | ["SMH", "MU", "SNDK", "STX"] |
| 受损篮子 | ["指引下修及高估值者"] |
| 反证 | 尚未开盘；SNDK/STX预测盘口薄且宽，不能当盈利胜率。 |
| 下一催化剂 | 今晚STX电话会；29日SNDK电话会 |
| 证据 | ["https://investors.seagate.com/news/news-details/2026/Seagate-Technology-to-Report-Fiscal-First-Quarter-2027-Financial-Results-on-October-27-2026/default.aspx", "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29"] |

## 航天与军工：项目进度仍是分水岭 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 继续核查SPCE28日转场准备与商业飞行延期、波音交付和现金转换；未发现已核验的新增商业飞行完成事实。 |
| 事实：市场反应 | 26日ITA+2.44%、ARKX+1.11%；今天盘前成分股价格未全覆盖。 |
| 推断：解释 | 推断：行业ETF上涨不能证明每个项目进度改善。 |
| 受益篮子 | ["交付与现金可验证的航天工业篮子"] |
| 受损篮子 | ["持续延期与融资敏感公司"] |
| 反证 | 试飞准备不等于商业收入，延期风险尚未消失。 |
| 下一催化剂 | 28日转场和后续交付；波音电话会 |
| 证据 | ["https://boeing.mediaroom.com/2026-10-27-Boeing-Reports-Third-Quarter-Results", "https://www.stocktitan.net/news/SPCE/virgin-galactic-sets-october-28-for-lead-delta-class-spaceship-s-ysvpiwc45syk.html"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 767.44 | 0.27 | 2026-10-27T11:59:19+00:00 | 2026-10-27T11:59:19+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| QQQ | 714.82 | 0.37 | 2026-10-27T11:59:37+00:00 | 2026-10-27T11:59:37+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| SMH | 547.95 | 1.17 | 2026-10-27T11:59:01+00:00 | 2026-10-27T11:59:01+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| RSP | 218.00 | 0.33 | 2026-10-27T11:07:39+00:00 | 2026-10-27T11:07:39+00:00 | 2026-10-27T11:59:53.441006+00:00 | stale |
| META | 629.96 | -0.10 | 2026-10-27T11:59:46+00:00 | 2026-10-27T11:59:46+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| MSFT | 528.80 | -0.71 | 2026-10-27T11:59:09+00:00 | 2026-10-27T11:59:09+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| AMZN | 249.90 | 0.33 | 2026-10-27T11:58:55+00:00 | 2026-10-27T11:58:55+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| NVDA | 217.51 | 0.70 | 2026-10-27T11:58:57+00:00 | 2026-10-27T11:58:57+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| GOOGL | 317.76 | 0.30 | 2026-10-27T11:59:27+00:00 | 2026-10-27T11:59:27+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| IGV | 111.06 | -0.30 | 2026-10-27T11:26:00+00:00 | 2026-10-27T11:26:00+00:00 | 2026-10-27T11:59:53.441006+00:00 | stale |
| XLE | 69.30 | -0.49 | 2026-10-27T11:57:40+00:00 | 2026-10-27T11:57:40+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| XLF | 56.23 | 0.38 | 2026-10-27T11:52:29+00:00 | 2026-10-27T11:52:29+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| IWM | 277.81 | 0.30 | 2026-10-27T11:59:41+00:00 | 2026-10-27T11:59:41+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| GLD | 367.59 | -0.06 | 2026-10-27T11:54:32+00:00 | 2026-10-27T11:54:32+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |
| TLT | 81.76 | 0.10 | 2026-10-27T11:57:14+00:00 | 2026-10-27T11:57:14+00:00 | 2026-10-27T11:59:53.441006+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 765.37 | USD_per_share | 2026-10-26 | 0.71 | -0.14 | -0.03 | ok |
| QQQ | 712.20 | USD_per_share | 2026-10-26 | 1.11 | -0.86 | -3.30 | ok |
| IWM | 276.99 | USD_per_share | 2026-10-26 | 0.45 | 2.10 | -1.08 | ok |
| RSP | 217.29 | USD_per_share | 2026-10-26 | 0.35 | 1.82 | 3.60 | ok |
| GLD | 367.82 | USD_per_share | 2026-10-26 | 0.33 | -3.13 | -2.67 | ok |
| GC=F | 4,038.40 | USD_per_troy_ounce | 2026-10-26 | 0.76 | -2.93 | -3.12 | ok |
| CL=F | 101.76 | USD_per_barrel | 2026-10-26 | -1.46 | -1.83 | 9.89 | ok |
| BZ=F | 115.81 | USD_per_barrel | 2026-10-26 | -0.78 | 5.71 | 10.00 | ok |
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

判断仍为恐慌缓和后的分化修复，而非全面过热。26日同端点VIX18.39、VIX3M19.94、VVIX101.43、MOVE102.19；27日11:44UTC延迟VIX17.87只作盘前增量，不能与昨日VIX3M合成当前曲线。23日FRED 2年4.69%、10年5.00%、实际10年2.66%、HY338bp、IG91bp仍滞后；26日10年盈亏平衡通胀2.34%独立记录，不混日相减。黄金GLD盘前约−0.06%、TLT+0.10%，不能称全面避险撤退。GPR最新26日165.25、七日181.42，STLFSI至16日−0.6328；不制造战争综合概率。沙特设施附近遇袭但供应损失未核验，油价连续分钟报价仅为水平，不冒充官方结算收益。CNN418，CME概率矩阵未取得，分别缺失。

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
| CBOE_VIX | 18.39 | index | 2026-10-26 | 2.32 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLE | 能源 | 0.45 | 2.71 | 12.14 | -0.26 | 2.86 | 12.17 | 1.01 | 2026-10-26 |
| XLF | 金融 | 0.21 | 1.74 | 3.38 | -0.50 | 1.89 | 3.41 | 0.63 | 2026-10-26 |
| XLI | 工业 | 1.42 | 0.17 | -1.08 | 0.71 | 0.31 | -1.05 | 0.89 | 2026-10-26 |
| XLV | 医疗 | 0.00 | 2.07 | 4.68 | -0.71 | 2.21 | 4.71 | 0.90 | 2026-10-26 |
| XLP | 必需消费 | -0.34 | 0.86 | 6.90 | -1.05 | 1.00 | 6.93 | 0.97 | 2026-10-26 |
| XLY | 可选消费 | 1.03 | -0.17 | 4.83 | 0.32 | -0.03 | 4.86 | 0.94 | 2026-10-26 |
| XLC | 通信 | -1.57 | -5.67 | -6.59 | -2.28 | -5.52 | -6.56 | 1.43 | 2026-10-26 |
| XLU | 公用事业 | -0.02 | 2.88 | 8.41 | -0.73 | 3.02 | 8.44 | 0.39 | 2026-10-26 |
| XLRE | 房地产 | 0.54 | 2.71 | 3.51 | -0.17 | 2.86 | 3.54 | 1.16 | 2026-10-26 |
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

19ETF最新完整26日端点不变：五日IGV+5.09%、SKYY+5.45%、KRE+5.01%、OIH+4.49%、XLE+2.71%，SMH−1.25%；半导体当日+2.74%是强修复，跨期仍弱。SMH量能1.21倍、QQQ0.89倍、SPY0.77倍，未全市场放量。盘前芯片领先但MSFT偏弱；优先看芯片常规承接、软件云延续，其次工业参与；能源须供应证据配合。资金层：VanEck页面更新26日SMH NAV541.56、资产677.2亿美元，但缺连续份额/拆分桥，不以资产增长算净流入；ICI仍为20日发布、截至14日ETF估计净发行532.62亿美元、国内股票296.70亿美元，不是本周或半导体实时资金。13F滞后，不识别当天主力。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-27T12:08:06.326852+00:00：基础25主题/清单及10组主动搜索（Saudi oil attack、Microsoft/Seagate/Sandisk earnings、AI bankruptcy、bank failure、recession、CPI November、Meta offering、Anthropic IPO）。Meta87、Anthropic28、CPI28结果有截断；财报/银行盘口流动性不足，未用价格赌局替代公司事件。未发现直接Meta融资完成的高质量合约；Saudi东西管道与Ras Tanura设施不是同一结算对象。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.35, {"status": "comparable", "change_pp": -0.20000000000000018}] | {"spread": 0.009000000000000008, "volume24h_usd": 273.580777, "liquidity_usd": 41029.23604, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-10-27T12:00:32.551187+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次9.35%，24小时成交约274美元，价差0.9个百分点；同定义比较，非客观概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [40.5, {"status": "comparable", "change_pp": -4.999999999999999}] | {"spread": 0.02999999999999997, "volume24h_usd": 24782.632325000002, "liquidity_usd": 31204.5589, "quality_flags": [], "retrieved_at": "2026-10-27T12:00:32.551187+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["本次40.5%，24小时成交约24783美元，价差3个百分点；同定义比较，非客观概率。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [15.0, {"status": "comparable", "change_pp": -5.000000000000002}] | {"spread": 0.04000000000000001, "volume24h_usd": 71936.912329, "liquidity_usd": 19175.9621, "quality_flags": [], "retrieved_at": "2026-10-27T12:00:13.022565+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["本次15%，24小时成交约71937美元，价差4个百分点；同定义比较，非客观概率。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [93.5, {"status": "comparable", "change_pp": 4.0000000000000036}] | {"spread": 0.009999999999999898, "volume24h_usd": 241725.47106900002, "liquidity_usd": 177171.3603, "quality_flags": [], "retrieved_at": "2026-10-27T12:00:32.551187+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["本次93.5%，24小时成交约241725美元，价差1个百分点；同定义比较，非客观概率。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 32792.277410999995, "liquidity_usd": 500837.9239, "quality_flags": [], "retrieved_at": "2026-10-27T12:00:32.551187+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次11.5%，24小时成交约32792美元，价差1个百分点；同定义比较，非客观概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [93.5, {"status": "comparable", "change_pp": -0.9999999999999898}] | {"spread": 0.009999999999999898, "volume24h_usd": 53250.033851, "liquidity_usd": 38916.5872, "quality_flags": [], "retrieved_at": "2026-10-27T12:00:16.785336+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次93.5%，24小时成交约53250美元，价差1个百分点；同定义比较，非客观概率。公开S-1存在不等于首日挂牌。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [92.7, {"status": "comparable", "change_pp": -0.44999999999999485}] | {"spread": 0.0020000000000000018, "volume24h_usd": 3763231.5918600005, "liquidity_usd": 975102.47927, "quality_flags": [], "retrieved_at": "2026-10-27T12:00:32.551187+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["本次92.7%，24小时成交约3763232美元，价差0.2个百分点；同定义比较，非客观概率。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |
| ["Will Microsoft (MSFT) beat quarterly earnings?", "下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。", "https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82"] | [80.0, {"status": "comparable", "change_pp": -5.999999999999995}] | {"spread": 0.12, "volume24h_usd": 335.832058, "liquidity_usd": 590.2985, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-27T12:00:32.551187+00:00", "contract_end_at": "2026-10-28T21:00:00+00:00"} | ["本次80%，24小时成交约336美元，价差12个百分点；同定义比较，非客观概率。固定GAAP EPS门槛，盘口宽且薄，不是股价胜率。", "财报影响云/AI估值；EPS之外更须检查资本开支、自由现金流与指引。"] | ["官方首次披露GAAP EPS与专门规则核验，同时看指引与股价承接。", "EPS过线但现金回报/指引转差、股价失守；不可由合约直接推导交易方向。"] | [null, null] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 92.70 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.15, 7.2] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.44999999999999485} |
| 24h成交量 / 流动性 USD | [3763231.5918600005, 975102.47927] |
| 价差 pp | 0.20 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:56:19.608813Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 93.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [8.0, 15.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.0000000000000036} |
| 24h成交量 / 流动性 USD | [241725.47106900002, 177171.3603] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.05, -0.8] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [54784.94485000001, 388967.2137] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [32792.277410999995, 500837.9239] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:56:19.608813Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 40.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-5.5, -17.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.999999999999999} |
| 24h成交量 / 流动性 USD | [24782.632325000002, 31204.5589] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:56:19.608813Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 75.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [4651.85095, 161148.5268] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:56:19.608813Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 12.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2864.9300000000003, 30357.4514] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T12:00:20.504224Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [456.064659, 15129.5074] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will Microsoft (MSFT) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1200526 / 5778671 |
| Yes 概率 % | 80.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.0, 3.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -5.999999999999995} |
| 24h成交量 / 流动性 USD | [335.832058, 590.2985] |
| 价差 pp | 12.00 |
| 到期 | 2026-10-28T21:00:00+00:00 |
| 结算规则摘要 | 下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。 |
| 规则指纹 | c38981deb507343e93936539de51b155f638166eb35f7eaca3a8513338e39cb0 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.2, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.20000000000000018} |
| 24h成交量 / 流动性 USD | [273.580777, 41029.23604] |
| 价差 pp | 0.90 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:32.551187+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 15.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-9.0, -5.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -5.000000000000002} |
| 24h成交量 / 流动性 USD | [71936.912329, 19175.9621] |
| 价差 pp | 4.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:13.022565+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 93.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, 16.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.9999999999999898} |
| 24h成交量 / 流动性 USD | [53250.033851, 38916.5872] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-27T11:58:19.88549Z |
| 抓取时间 | 2026-10-27T12:00:16.785336+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## AI 压力：合约、经营与估值分开

三层分别判断。合约：专门2026年严重AI下行9.35%（早报9.55%），2027年6月底22.5%不变；24小时成交分别约274/456美元，极薄，前者−0.20个百分点小于0.9个百分点价差。结算要求90天内至少三项极端事件，不是普通回撤概率。经营/融资：NVIDIA拟投Meta30亿美元、康宁光通信+44%支持需求与融资可得性；供应商投资客户不能单独证明终端现金回报。Meta普通股625美元定价与优先权益票息6.5%已核验，但远期发行不是当日现金入账；Anthropic上期S-1中巨额公允价值损失与现金烧钱必须区分，本次未有新财务数字取代。H100最新仍26日2.89美元/GPU小时、7日+7%，单一型号不代表全行业盈利。估值：本次五家SEC定期财报检查成功，无新增10-Q/K；NVDA/MSFT/AMZN/GOOGL复用已核验底稿，以26日收盘重算五年FCFF与敏感性，盘前价格单独呈现。META定价信息补齐一部分，但净债务/租赁新增、优先权益及远期结算稀释桥尚不完整，继续不可用；不以公司整体估值推算AI客观崩盘概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-27T12:01:49.784099+00:00", "latest_filing_date": "2026-08-26"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-27T12:01:52.937206+00:00", "latest_filing_date": "2026-07-29"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-27T12:01:54.715277+00:00", "latest_filing_date": "2026-07-31"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-27T12:01:56.343084+00:00", "latest_filing_date": "2026-07-23"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-27T12:01:59.766934+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 反弹续航：盘前突破需常规承接

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 26日收盘突破第一层价位；27–29日财报与政策 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP"] |
| 确认条件 | 27日常规时段QQQ715.25、SMH545.34、SPY767.73同步突破，回踩不快速跌回，RSP/IWM参与且可核验常规VWAP守住；未取得VWAP时不写条件已满足。 |
| 失效条件 | 跌回QQQ709.30、SMH533.34、SPY763.47且反抽失败则降级；再失守26日低点QQQ705.58/SMH530.20/SPY761.63则修复进一步受损。 |
| 观察期限 | 未来1–3交易日 |
| 反证 | MSFT盘前逆势、等权报价陈旧；QQQ昨量仅0.89倍，仍低于20日线734.02。 |
| 状态 | 半导体盘前越昨高；常规时段待验证 |

## 软件云延续而非追高

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 微软28日、Amazon29日财报 |
| 关联标的 | ["IGV", "SKYY", "MSFT"] |
| 确认条件 | IGV回踩仍守26日低点109.69及动态20日线108.88附近，突破111.88后不快速跌回；云增长和现金回报指引支持。 |
| 失效条件 | 相对SPY转弱，109.69反抽失败且20日线失守；经营指引转弱。 |
| 观察期限 | 本周 |
| 反证 | MSFT盘前约−0.71%；IGV/SKYY26日量能不足，不能用五日强势跳过财报风险。 |
| 状态 | 相对强势观察 |

## 能源只做有供给证据的强势

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 地缘、航运和油价波动 |
| 关联标的 | ["XLE", "XOP", "OIH"] |
| 确认条件 | XLE守68.62（26日低点），相对SPY继续强；独立供应证据与油价同向。 |
| 失效条件 | 跌破68.62反抽失败或实际供应恢复、风险溢价持续回落。 |
| 观察期限 | 未来一周 |
| 反证 | 设施附近火情不等于可量化供给损失；XLE盘前偏弱，地缘标题与价格反应不一致。 |
| 状态 | 跨期强势但事件敏感 |

## AI融资消息需要每股现金回报确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | Meta正式定价、NVIDIA拟参与融资及Corning需求证据 |
| 关联标的 | ["NVDA", "AVGO", "META"] |
| 确认条件 | META先守627.80，再收复642.62并有常规承接；普通股625发行价仅作观察参照。后续融资交割、租赁/股本桥与每股现金流须改善。 |
| 失效条件 | 627.80失守且反抽失败，尤其跌至625附近仍无承接；或融资/现金流条件恶化。 |
| 观察期限 | 未来两日价格；下一财报周期经营 |
| 反证 | 筹资渠道可缓解融资风险但稀释未消失，不能将发行价当保证底部。 |
| 状态 | 分化，不能一概追AI |

## 跨期比较与上期剧本复核

对照27日早报：没有新增完整常规日线，26日收盘突破和均线距离不变；新增盘前SMH越昨高而MSFT/META偏弱，尚不能升级为全面趋势反转。Meta从发行计划进入定价，NVIDIA参与融资本次核验，原先“条款全未知”已部分解除，但现金到账和稀释桥未完成。康宁/波音新增结果提供行业对照。US-Iran合约上行不代表沙特设施安全，WTI105盘口下降亦非实际供应证明。同规则变化：2589812：93.15%→92.7%（-0.45个百分点）；4641065：89.5%→93.5%（+4.00个百分点）；3501950：0.35%→0.35%（+0.00个百分点）；4951227：45.5%→40.5%（-5.00个百分点）；3215008：74.5%→75.5%（+1.00个百分点）；2176270：11.5%→11.5%（+0.00个百分点）；691340：9.55%→9.35%（-0.20个百分点）；2252540：12.5%→12.5%（+0.00个百分点）；5778671：86%→80%（-6.00个百分点）；4838928：22.5%→22.5%（+0.00个百分点）；5401795：20%→15%（-5.00个百分点）；2413330：94.5%→93.5%（-1.00个百分点）。MSFT EPS盘口从86%至80%但价差12个百分点、成交仅约336美元，6个百分点变化不宜过度解读。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-26/20261026T232315.247706Z/evidence.json",
    "baseline_cutoff": "2026-10-26T23:23:08.626160+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.3453820932724616,
      "CL=F": 0.4342700777058228,
      "BZ=F": 5.147991828914256,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.001366239446831674,
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
        "change_pct": 0.4226586932911225,
        "from_observed_at": "2026-10-26T23:14:16+00:00",
        "to_observed_at": "2026-10-27T11:59:19+00:00"
      },
      "QQQ": {
        "change_pct": 0.4177565498349356,
        "from_observed_at": "2026-10-26T23:17:45+00:00",
        "to_observed_at": "2026-10-27T11:59:37+00:00"
      },
      "SMH": {
        "change_pct": 1.0245026641346744,
        "from_observed_at": "2026-10-26T23:15:37+00:00",
        "to_observed_at": "2026-10-27T11:59:01+00:00"
      },
      "META": {
        "change_pct": -0.44093243777162394,
        "from_observed_at": "2026-10-26T23:14:04+00:00",
        "to_observed_at": "2026-10-27T11:59:46+00:00"
      },
      "MSFT": {
        "change_pct": -0.45180722891567937,
        "from_observed_at": "2026-10-26T23:17:35+00:00",
        "to_observed_at": "2026-10-27T11:59:09+00:00"
      },
      "AMZN": {
        "change_pct": 0.4017677782241824,
        "from_observed_at": "2026-10-26T23:17:37+00:00",
        "to_observed_at": "2026-10-27T11:58:55+00:00"
      },
      "NVDA": {
        "change_pct": 0.6898898250161878,
        "from_observed_at": "2026-10-26T23:18:12+00:00",
        "to_observed_at": "2026-10-27T11:58:57+00:00"
      },
      "GOOGL": {
        "change_pct": 0.10711360342763321,
        "from_observed_at": "2026-10-26T23:18:13+00:00",
        "to_observed_at": "2026-10-27T11:59:27+00:00"
      },
      "IWM": {
        "change_pct": 0.5028579697561542,
        "from_observed_at": "2026-10-26T23:17:05+00:00",
        "to_observed_at": "2026-10-27T11:59:41+00:00"
      },
      "GLD": {
        "change_pct": -0.06147028437821778,
        "from_observed_at": "2026-10-26T23:07:54+00:00",
        "to_observed_at": "2026-10-27T11:54:32+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-23"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-23"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-23"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-23"
      },
      "DFII10": {
        "change": 0.0,
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
        "change": -1.0599999999999987,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_ACT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_THREAT": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_MA7": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      },
      "GPRD_MA30": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-26"
      }
    },
    "event_probability_change": {
      "2589812": {
        "status": "comparable",
        "change_pp": -0.44999999999999485
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 4.0000000000000036
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4951227": {
        "status": "comparable",
        "change_pp": -4.999999999999999
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5778671": {
        "status": "comparable",
        "change_pp": -5.999999999999995
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.20000000000000018
      },
      "5401795": {
        "status": "comparable",
        "change_pp": -5.000000000000002
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -0.9999999999999898
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
    "event": "Anthropic定价/挂牌未定；合约截止不等于发生日期",
    "date": null,
    "source": "https://www.anthropic.com/news/s1-sec"
  },
  {
    "event": "Oracle投资者日",
    "date": "2026-10-28T10:55:00-05:00",
    "source": "https://investor.oracle.com/investor-news/news-details/2026/ORACLE-INVESTOR-DAY-MEETING-TO-BE-HELD-OCTOBER-28-2026/default.aspx"
  },
  {
    "event": "Meta优先权益发行预计交割，附条件；非普通股远期全额结算日",
    "date": "2026-10-29 America/New_York",
    "source": "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"
  },
  {
    "event": "波音Q3电话会",
    "date": "2026-10-27T10:30:00-04:00",
    "source": "https://boeing.mediaroom.com/2026-09-30-Boeing-to-Release-Third-Quarter-Results-on-October-27"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| meta-financing-pricing-20261027 | 组合发行375亿美元已定价，普通股625美元；部分通过远期结算，不代表今天全额到账。 | 缺失 | [{"source": "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html", "published_at": "2026-10-27T01:01:00-04:00", "retrieved_at": "2026-10-27T12:08:06.326852+00:00"}] |
| nvidia-meta-muse-20261026 | 公司宣布拟投Meta30亿美元并扩大合作；官网标26日，27日新闻传播，不能把传播日当首次事件日。 | 缺失 | [{"source": "https://nvidianews.nvidia.com/news/nvidia-and-meta-to-expand-collaboration-on-muse-and-muse-family-of-models-amid-robust-growth", "published_at": null, "retrieved_at": "2026-10-27T12:08:06.326852+00:00"}] |
| corning-q3-20261027 | Q3核心销售50.8亿美元、同比+19%，光通信+44%；核心指标为非GAAP。 | 缺失 | [{"source": "https://www.stocktitan.net/news/GLW/corning-delivers-outstanding-third-quarter-results-ijv492ou5imj.html", "published_at": "2026-10-27T07:01:00-04:00", "retrieved_at": "2026-10-27T12:08:06.326852+00:00"}] |
| boeing-q3-20261027 | Q3收入约242亿美元，经营现金流15亿美元、FCF5亿美元；核心EPS仍亏损。 | 缺失 | [{"source": "https://boeing.mediaroom.com/2026-10-27-Boeing-Reports-Third-Quarter-Results", "published_at": null, "retrieved_at": "2026-10-27T12:08:06.326852+00:00"}] |
| saudi-ras-tanura-20261027 | Reuters转载：Ras Tanura附近遇袭火情获控制，供应损失未量化核验；不同于东西输油管道合约。 | 缺失 | [{"source": "https://www.moneycontrol.com/world/saudi-arabia-contains-fire-near-ras-tanura-oil-hub-after-attack-article-14061244.html", "published_at": "2026-10-27T14:36:00+05:30", "retrieved_at": "2026-10-27T12:08:06.326852+00:00"}] |
| oracle-investor-day-20261028 | Oracle官方23日公告28日10:55美国中部时间投资者日；本次新增核查，非今日新公告。 | 缺失 | [{"source": "https://investor.oracle.com/investor-news/news-details/2026/ORACLE-INVESTOR-DAY-MEETING-TO-BE-HELD-OCTOBER-28-2026/default.aspx", "published_at": null, "retrieved_at": "2026-10-27T12:08:06.326852+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN接口418/官方页面不可读；不以tc温度或加密指标替代。",
  "完整成分广度、历史盈利一致预期修正与27日常规VWAP缺失；盘前尚不能验证开盘承接。",
  "19ETF当期净申赎及连续拆分调整份额缺失；ICI至14日、SMH发行人至26日，不称当期主力净流入。",
  "tc新闻high限50且has_more，主动补查仍非完整新闻库。",
  "tc请求时戳未证明成交时间，使用独立Yahoo分钟包；RSP/IGV部分盘前报价稀疏滞后。",
  "期货连续/近月与Reuters不同合约未对齐，不拼接官方结算收益；VIX盘前不与昨日VIX3M合成当前曲线。",
  "CME页面可读但当期带时点概率矩阵未取得，Polymarket不是FedWatch。",
  "META普通股定价与票息已确认，但净债务/租赁新增及远期/优先权益稀释桥未齐，FCFF反推不可用。",
  "DRAM不足200日历史；Polymarket部分查询截断，EPS和AI崩盘等盘口薄。",
  "沙特火情报道未独立量化供应中断，不能说出口已经停止；公司计划与承诺也不代表全部落实。",
  "NVIDIA8月官方实录预告11月17日、tc日历25日冲突，沿用已核验官方预告并保留临近更新缺口。",
  "Corning公司稿直接页面受403限制，本次通过可读搜索索引核验；NVDA和Meta定价原文已直接读取。",
  "原始采集存在请求失败，见采集质量记录",
  "META 估值: 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。",
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
  "tc 报价质量 stale: RSP, IGV；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.RSP.value, quotes.IGV.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://nvidianews.nvidia.com/news/nvidia-and-meta-to-expand-collaboration-on-muse-and-muse-family-of-models-amid-robust-growth",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://www.moneycontrol.com/world/saudi-arabia-contains-fire-near-ras-tanura-oil-hub-after-attack-article-14061244.html",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://www.stocktitan.net/news/GLW/corning-delivers-outstanding-third-quarter-results-ijv492ou5imj.html",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://boeing.mediaroom.com/2026-10-27-Boeing-Reports-Third-Quarter-Results",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://investor.oracle.com/investor-news/news-details/2026/ORACLE-INVESTOR-DAY-MEETING-TO-BE-HELD-OCTOBER-28-2026/default.aspx",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次核验；官网、公司稿或具名转载。取证时刻不是事件发生时刻。"
  },
  {
    "url": "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-to-Report-Fiscal-First-Quarter-2027-Financial-Results-on-October-27-2026/default.aspx",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.microsoft.com/en-us/investor/faq",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.bea.gov/news/schedule/full",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://www.anthropic.com/news/s1-sec",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://boeing.mediaroom.com/2026-09-30-Boeing-to-Release-Third-Quarter-Results-on-October-27",
    "checked_at": "2026-10-27T12:08:06.326852+00:00",
    "note": "本次查核官方日程/沿用早报已核验公告，旧公告日期不是新事件；NVIDIA日期冲突保留缺口。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-27T11:59:53.441006+00:00",
    "note": "备用分钟价；实际成交分钟见quotes；相对26日常规收盘，仅表示盘前增量。"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
