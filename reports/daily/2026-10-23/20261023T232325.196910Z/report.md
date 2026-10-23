# 每日交易总结 · 2026-10-23

## 一分钟读懂 · Agent 摘要

### 当前判断

反弹仍脆弱，尚未确认趋势反转。适合等待强势板块回踩后的承接，不宜仅因跌幅大就重仓抄底。

### 与上次相比

相较昨晚盘前日报，防御和金融的日内领先失效；软件/网络安全与能源上升为观察重点。盘中QQQ、SMH的修复未守住全部涨幅，SNDK从反弹转为收跌。

### 最重要的信号

- SPY−0.52%、QQQ−0.01%、RSP−0.77%；SMH+0.74%，仍低于20日线约9.96%，全市场参与面尚未确认。
- IGV+1.72%、CIBR+3.22%、XLE+2.60%；安全事件与油服业绩提供催化，但价格上涨不等于主力净流入。
- WTI触105合约由53%升至84.5%；高收益债利差由327扩大至340bp（截至22日）。VIX19.45未显示极端恐慌，风险也未解除。

### 接下来观察

- 下周QQQ收复709.30、SMH收复533.34后回踩守住，并由SPY和等权跟随，才升级反弹可信度。
- 若QQQ失守701.16、SMH失守521.47且反抽失败，停止加风险；长期反转仍需均线与盈利确认。
- 关注10月28日FOMC及29日SNDK财报；周末能源事件可能导致跳空，首批优先无杠杆篮子。

### 不要忽略

数字区分常规收盘与盘后。CNN、实时成分广度、当期ETF申赎缺失；Brent跨来源报价冲突，不用其自动涨跌幅判断方向。

## 研究结论

10月23日收盘：局部反弹未演变为全面反转。能源、软件/网络安全相对领先，半导体修复收窄；等权与防御回落，油价与信用压力限制风险偏好。当前为纽约盘后，以下建仓条件面向10月26日及随后一周。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-23 → 2026-10-23（纽约交易日） |
| 截止·纽约 | 2026-10-23T19:23:21.520527-04:00 |
| 截止·北京 | 2026-10-24T07:23:21.520527+08:00 |
| 实际生成时间 | 2026-10-23T23:23:21.602145+00:00 |
| 市场阶段 | 盘后 |
| 下一交易日 | 2026-10-26 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-22/20261023T120705.216296Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-24T07:15:00+08:00 |

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
| prices.SPY.volume_vs_previous20_ratio | 0.81 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
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
| prices.QQQ.volume_vs_previous20_ratio | 0.81 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
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
| prices.IWM.volume_vs_previous20_ratio | 0.80 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
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
| prices.GLD.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,010.00 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -1.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -4.09 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -7.20 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -2.20 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.72 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -3.66 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -5.73 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -4.92 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,155.37 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,341.91 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,532.91 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -3.50 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.64 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -11.54 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 71.89 | USD_per_troy_ounce | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.79 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -14.64 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.17 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 103.44 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 3.99 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 2.00 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 11.94 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 23.75 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 4.51 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 2.43 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 13.41 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 21.03 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 94.74 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 92.93 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.29 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 9.19 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 11.31 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 21.28 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.38 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.24 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -2.26 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 111.66 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -1.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 1.64 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 7.04 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 25.42 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -0.81 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 2.07 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 8.51 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 22.70 | pp | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 105.61 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 100.73 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 91.15 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 5.73 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 10.85 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 22.50 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 4.00 | USD_per_barrel | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.58 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -1.33 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.04 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
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
| prices.TLT.volume_vs_previous20_ratio | 0.69 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
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
| prices.^MOVE.distance_sma20_pct | 0.13 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
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
| prices.NVDA.volume_vs_previous20_ratio | 0.75 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
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
| prices.META.volume_vs_previous20_ratio | 0.74 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
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
| prices.CRWV.atr14_pct | 11.88 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
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
| prices.XLI.volume_vs_previous20_ratio | 0.95 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
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
| prices.XLP.volume_vs_previous20_ratio | 1.46 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
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
| prices.SMH.atr14_sma | 18.36 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.48 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -16.83 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
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
| prices.OIH.atr14_sma | 11.55 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.91 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -8.98 | percent | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 2.13 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
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
| prices.KRE.volume_vs_previous20_ratio | 0.99 | ratio | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
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
| prices.SKYY.atr14_sma | 4.73 | USD_per_share | 2026-10-23 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
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
| macro.CBOE_VIX.value | 19.03 | index | 2026-10-22 | lagged | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 248.66 | index | 2026-10-19 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 230.19 | index | 2026-10-19 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 310.16 | index | 2026-10-19 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 177.92 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 176.01 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 760.53 | USD_per_share | 2026-10-23T23:17:31+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 704.27 | USD_per_share | 2026-10-23T23:17:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 527.00 | USD_per_share | 2026-10-23T23:13:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.IWM.value | 275.61 | USD_per_share | 2026-10-23T23:13:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.RSP.value | 216.88 | USD_per_share | 2026-10-23T22:51:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.NVDA.value | 210.96 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.MSFT.value | 524.51 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.AMZN.value | 248 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.GOOGL.value | 320.21 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.META.value | 642.62 | USD_per_share | 缺失 | unverified_trade_timestamp | tc_last_v1 | tc MCP get_symbol_quotes |
| quotes.MU.value | 874.02 | USD_per_share | 2026-10-23T23:17:37+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.SNDK.value | 1,232.00 | USD_per_share | 2026-10-23T23:16:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.BE.value | 190.88 | USD_per_share | 2026-10-23T23:17:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BE |
| quotes.WDC.value | 339.68 | USD_per_share | 2026-10-23T23:16:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/WDC |
| quotes.DRAM.value | 46.79 | USD_per_share | 2026-10-23T23:17:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.IGV.value | 110.58 | USD_per_share | 2026-10-23T23:02:41+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.XLE.value | 69.37 | USD_per_share | 2026-10-23T22:47:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.CIBR.value | 106.52 | USD_per_share | 2026-10-23T22:42:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CIBR |
| quotes.SKYY.value | 167.20 | USD_per_share | 2026-10-23T20:01:34+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SKYY |
| external.close.CIBR_close | 106.12 | USD_per_share | 2026-10-23T20:00:01+00:00 | ok | Yahoo regularMarketPrice及其regularMarketTime；常规收盘样本，不是盘后价 | https://query1.finance.yahoo.com/v8/finance/chart/CIBR |
| external.close.SNDK_close | 1,238.03 | USD_per_share | 2026-10-23T20:00:00+00:00 | ok | Yahoo regularMarketPrice及其regularMarketTime；常规收盘样本，不是盘后价 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| external.close.BE_close | 193.30 | USD_per_share | 2026-10-23T20:00:03+00:00 | ok | Yahoo regularMarketPrice及其regularMarketTime；常规收盘样本，不是盘后价 | https://query1.finance.yahoo.com/v8/finance/chart/BE |
| external.close.WDC_close | 343.67 | USD_per_share | 2026-10-23T20:00:00+00:00 | ok | Yahoo regularMarketPrice及其regularMarketTime；常规收盘样本，不是盘后价 | https://query1.finance.yahoo.com/v8/finance/chart/WDC |

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
        "change": 0.37867248535155795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.124828796386737,
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
        "change": -0.6063284377849643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7633452514994588,
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
        "change": -0.5295923155680442,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7107477113020229,
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
        "change": 0.41249176025394263,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.4384933471679915,
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
        "change": -0.07395523682918181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1787154469332872,
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
        "change": -1.018916425121985,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0873263188894189,
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
        "change": 0.10995689392092345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6260741424560479,
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
        "change": -0.37155107905881835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.6949119187510853,
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
        "change": -0.0632128034319197,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2732107979910712,
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
        "change": -0.018398325510061264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.12729652471828756,
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
        "change": -0.19421390180784737,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.49854412153426253,
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
        "change": 0.12026100158692543,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6063722991943337,
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
        "change": -0.8776284863528883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.8826303142066338,
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
        "change": 0.0028577532087052937,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04571533203125,
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
        "change": 0.008712260227282664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.010349549481431408,
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
        "change": -0.8717774065964611,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5166144855386056,
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
        "change": -1.0150733608011813,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04686156184306656,
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
        "change": -50.39990234375,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -171.10009765625,
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
        "change": 0.9177838539641714,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.50503728070156,
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
        "change": -1.4615897933201616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.2573784792987337,
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
        "change": -1.673552523681443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6919826838627134,
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
        "change": -2.7945875564514777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.429452526511258,
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
        "change": 0.25909356454244525,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.089267728472388,
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
        "change": -2.0463637280939584,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.795344357446451,
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
        "change": -0.6179315491393389,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.011839144314551575,
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
        "change": -0.5240805621838929,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.495589600232841,
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
        "change": -15.560009765625182,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -58.739990234375,
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
        "change": -8.207998046875218,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -32.506005859375364,
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
        "change": -2.262499999999818,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -7.788500976562318,
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
        "change": -0.8483536865488084,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.715046519317621,
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
        "change": -0.9843265694555514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.225093583167471,
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
        "change": -1.0671790616203385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.6164061892322135,
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
        "change": 1.621425083705347,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1071428571428612,
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
        "change": 0.062184117216610435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04687999899859907,
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
        "change": -1.072840573015922,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.642132589079795,
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
        "change": 0.16586963779584107,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.10967333217225517,
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
        "change": 3.970001220703125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.029998779296875,
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
        "change": 1.6030949398622596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4798728785273765,
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
        "change": 0.4706927727953225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -8.406506484743037,
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
        "change": 6.799057554638765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 10.829255340137323,
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
        "change": 5.9751390314240815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 13.74578223868701,
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
        "change": 0.9444046504405339,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.10435756924345085,
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
        "change": -0.11408116197847429,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -9.944472362890753,
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
        "change": 7.854678529180868,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 12.509398879685484,
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
        "change": 8.245646025691666,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 14.679645164965429,
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
        "change": 0.5514999389648523,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7980003356933594,
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
        "change": 0.4438000488281233,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9496003723144497,
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
        "change": 0.23725000381469386,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0966500473022478,
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
        "change": 3.5757653818107693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.07189164241601098,
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
        "change": 3.7583317151340445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1539217562621218,
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
        "change": 4.329493671767381,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.831373839504689,
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
        "change": -0.02974417587975342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2807705214966587,
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
        "change": 3.7513003420719726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9181694643996443,
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
        "change": -0.06362950409617119,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3287544122420484,
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
        "change": -1.5099945068359375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.8000030517578125,
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
        "change": -5.331696588428714,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.054061924741293,
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
        "change": -5.206336934198186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -3.2698746233273734,
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
        "change": 0.8728199495390054,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2692250629833257,
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
        "change": 0.6994259096482232,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 16.311245573093494,
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
        "change": -5.99038687785044,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -5.638292372512121,
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
        "change": -5.791110868971983,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.807840501475091,
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
        "change": 1.9284409240811105,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.9493686025314885,
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
        "change": 2.969932903915808,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 17.24510849937191,
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
        "change": 0.36700019836425213,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9200004577636776,
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
        "change": 0.49180007934569403,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.315199890136711,
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
        "change": 0.2585000228881711,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2398500442504883,
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
        "change": -1.8034322716617313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.22177155964984152,
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
        "change": -2.050269884653245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7787525331300671,
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
        "change": -2.0097518389776923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3127018955033414,
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
        "change": 0.07857131958007812,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.03999982561383941,
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
        "change": 0.11719119356231333,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.022242574645848556,
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
        "change": -1.334271035846224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.334271035846224,
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
        "change": 0.023506046511379663,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2819237855294596,
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
        "change": -0.01745544433593693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.09545028686522983,
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
        "change": -0.45958553750449216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.6583987141347127,
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
        "change": -0.01892852783203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.008510055158627794,
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
        "change": -0.01817427558142848,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.027039299065534372,
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
        "change": -0.6070308837519399,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.15355477625213432,
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
        "change": -0.0073071888514927436,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.019450051443917413,
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
        "change": -0.0261485968823999,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.06783040264229917,
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
        "change": -0.37212277748933387,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.4784842387016408,
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
        "change": -0.0016011047363377884,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.008196907043455326,
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
        "change": -0.06215070842211512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2543123986555873,
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
        "change": 0.16522706093941408,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3000059852799586,
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
        "change": -0.035974121093758527,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.18473922729492642,
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
        "change": -0.014354095458983807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.07642887115477492,
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
        "change": -0.37922367418761205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.609974452635853,
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
        "change": -0.3926580466631968,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4952822059764661,
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
        "change": 0.006071363176618383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.019253822039079993,
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
        "change": 0.008367648437010433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.015934197945507877,
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
        "change": -0.4058358244595772,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4247013114602516,
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
        "change": -0.39782577243958483,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.016688847266840057,
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
        "change": -3.5276947021484375,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.2123031616210938,
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
        "change": -14.663109200896553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9456190841547927,
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
        "change": -2.0560824823280033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.791011644951035,
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
        "change": -13.145131157249178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -33.85452918979115,
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
        "change": -1.1402241173181338,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 6.786532071715108,
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
        "change": -15.321799490318279,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -2.529849531925621,
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
        "change": -2.6408564171018005,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.84078789011518,
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
        "change": -12.706745718638533,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -32.58095390217499,
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
        "change": -2.207400379753821,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 4.718196738755061,
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
        "change": -0.063385009765625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.4331153869628963,
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
        "change": 0.6244461059570199,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.709446105957028,
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
        "change": 0.1874615097045904,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.9413115119934048,
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
        "change": -3.3553164933028734,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.2282039008474799,
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
        "change": -4.8895962543308755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.1468920519180266,
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
        "change": -4.9412529060256105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2465256375446572,
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
        "change": 0.08112880161830383,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.21112877982003386,
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
        "change": 0.2571377563808568,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08874311354519637,
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
        "change": -3.1053650964195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9474499923739614,
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
        "change": 0.111457443237299,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7053700256347497,
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
        "change": -0.6718899626196206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9252845679613495,
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
        "change": -0.4534237963131379,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3618396999297079,
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
        "change": 0.22043991088867188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.3380792236328034,
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
        "change": 0.7272062822006653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.417422566856974,
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
        "change": -0.35967653093073315,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.43999963789646135,
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
        "change": -0.030114310128348087,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.1827392578125,
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
        "change": 0.015128147726425567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.49595016620126176,
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
        "change": -0.669490778877263,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.40478370259748786,
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
        "change": -0.005724029541056552,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.428547515869127,
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
        "change": -1.174411113199092,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -6.102493224558736,
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
        "change": -0.09570094517299133,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5728432791573663,
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
        "change": 0.00288102894423492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.011448083161615497,
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
        "change": -0.43138399187363274,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.3610082909545641,
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
        "change": -1.3304003252396086,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.18722437943368586,
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
        "change": -0.11892863682338195,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5664283207484653,
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
        "change": 0.07787490787497298,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.3078427713456797,
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
        "change": -0.7658699386220728,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.575899361339769,
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
        "change": -0.42305670439619303,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.32648884578610016,
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
        "change": 0.10035732814243836,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3367865426199774,
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
        "change": 0.04478790106336028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6490187359187969,
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
        "change": -0.7318620077302006,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.7427263444445008,
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
        "change": 0.10285622732980038,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2607127598353802,
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
        "change": 0.09210875076487834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.9675380283093258,
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
        "change": -0.2583686382725785,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.06578212234754033,
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
        "change": 0.18613330841066045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.0102478790283271,
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
        "change": 0.40905281933390114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.8018959073394551,
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
        "change": -0.58278584439381,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.107549824788538,
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
        "change": 0.12538499832152894,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5862059402465789,
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
        "change": 2.800666111563821,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6740327647515336,
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
        "change": -0.10082692255283332,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04498384790076848,
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
        "change": 0.004809570312502842,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.024436244964604725,
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
        "change": -1.4151449978705433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6644872697006976,
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
        "change": 0.012499945504324761,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.017500468662806856,
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
        "change": 0.03899059761939139,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.022770927698440246,
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
        "change": -0.1163148359294669,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.31594145483153646,
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
        "change": 0.034542083740234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.2274232482910179,
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
        "change": -1.2432234225214218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.9497887117066344,
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
        "change": 0.07642800467354904,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1121412004743303,
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
        "change": 0.06645838835059492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.09734200830257556,
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
        "change": -0.493124125913597,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.2988186609185066,
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
        "change": -0.2894729715791299,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.09185511581598516,
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
        "change": 0.06544132232664879,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.30410713195800554,
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
        "change": -2.1604589484030656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.38289405180356173,
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
        "change": -0.31940315476259906,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5655634297129712,
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
        "change": -0.035265197753915345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.11361385345459496,
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
        "change": -1.6253656847317721,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.6507677775092868,
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
        "change": -0.25218907082810993,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6263592357904662,
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
        "change": -0.05261116027831747,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.19654624938965526,
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
        "change": -1.6503558799263347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -4.097717495432462,
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
        "change": 0.028928484235491103,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04250063214983246,
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
        "change": 0.05544640107030108,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.10845011837168905,
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
        "change": -0.11332332745609908,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.17251354916724893,
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
        "change": 0.0077304458618101535,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.008411293029780609,
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
        "change": -0.7254616266058389,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.7810199613214719,
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
        "change": -0.31267840180411655,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.39678953167019226,
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
        "change": 0.02757154192243294,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.05150032043457031,
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
        "change": 0.06304328985397678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1072648052341052,
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
        "change": -0.20374790247829067,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1139841175025138,
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
        "change": 0.02610965728759851,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.13607315063476477,
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
        "change": -0.8034336449301405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.4993312176753806,
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
        "change": -0.1073576876981771,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.35393973453022065,
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
        "change": 0.28936767578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 2.722943987165179,
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
        "change": 0.029667861136521534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.5856844729802866,
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
        "change": -1.0550858151203972,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.6918801423855416,
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
        "change": 0.08002853393554688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.13288661411830383,
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
        "change": 0.028294429945139754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.030453977156466028,
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
        "change": -0.37298944505513476,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.3489337309038194,
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
        "change": 0.39658180236816065,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.86485256195067,
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
        "change": 2.5957933624857645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5624080414042609,
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
        "change": 0.0007149832589288252,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.25071607317243316,
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
        "change": -0.059144075537332697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.10923052719925952,
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
        "change": -0.638548161900361,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.11909631325359316,
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
        "change": 0.4177616664341528,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.9441920689174115,
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
        "change": -0.0461046054824128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3933028921220729,
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
        "change": -0.21229483774513414,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.2741815855936398,
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
        "change": -0.007363451707043778,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -1.0501344401930137,
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
        "change": 0.01964977809361057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08286408015659885,
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
        "change": 0.04830998806081688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.28034586416507823,
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
        "change": -0.5522073202965679,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.5047635923181354,
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
        "change": 0.03427455902100007,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.1522527122497621,
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
        "change": 0.020825426343407116,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 3.5596080667573804,
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
        "change": -0.006786346435546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.03250176565987739,
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
        "change": -0.010600291573195753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": -0.1140815650087399,
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
        "change": -0.16441009151549135,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.03223036191002182,
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
        "change": 0.17785753522600434,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.3892876761300226,
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
        "change": 0.05589651028391751,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.08762898342869807,
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
        "change": 2.209906237785045,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 1.7712693093192309,
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
  },
  {
    "id": "external.close.CIBR_close",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "external.close.SNDK_close",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "external.close.BE_close",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "external.close.WDC_close",
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
| 事实指标引用 | ["macro.BAMLH0A0HYM2.value", "macro.DGS10.value", "prices.^VIX.value", "prices.^MOVE.value"] |
| 推断与解释 | 推断：风险偏好下降并伴能源通胀压力，未确认系统性恐慌；信用利差扩张值得警惕。 |
| 反证与缺口 | MOVE回落、VIX低于三个月值；信用滞后一天。 |
| 确认条件 | 信用与波动持续上行、成分广度同步恶化。 |
| 失效条件 | 油价风险消退、信用改善且股市承接恢复。 |
| 观察期限 | 下周至两周 |
| 条件式指导 | 避免仅凭VIX未到极端就认定安全。 |
| 主观置信等级 | medium |
| 判断变化原因 | HY更新至340bp，VIX升19.45但MOVE回落，分歧仍在。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct"] |
| 推断与解释 | 推断：盘中修复未守住，收盘与广度代理均不足以确认反转。 |
| 反证与缺口 | MU/DRAM与软件仍收涨；没有交易所成分广度。 |
| 确认条件 | QQQ709.30/SMH533.34收复回踩，SPY/RSP跟随，之后收复动态均线。 |
| 失效条件 | QQQ701.16/SMH521.47失守且反抽失败。 |
| 观察期限 | 未来1–5交易日 |
| 条件式指导 | 等待确认后分批试探，不把一次拉升当趋势。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对昨晚等待开盘，今日已有收盘证据：反弹收窄。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.IGV.return_5d_pct", "prices.SMH.relative_spy_5d_pp", "prices.XLE.return_1d_pct", "prices.OIH.volume_vs_previous20_ratio"] |
| 推断与解释 | 推断：软件/网络安全及能源优先观察，半导体为高风险修复；不等于主力流入。 |
| 反证与缺口 | 能源依赖事件，软件涨幅未证明利润增长；申赎缺失。 |
| 确认条件 | 相对SPY持续领先，回踩守住，订单/利润或发行人申赎补证。 |
| 失效条件 | 领涨消失、跌破回踩低点或经营逻辑证伪。 |
| 观察期限 | 未来一周 |
| 条件式指导 | 先看强势无杠杆篮子，避免同时集中多个同一风险链。 |
| 主观置信等级 | medium |
| 判断变化原因 | 昨晚防御日内优势消失，IGV五日强势已有延续。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 推断：需求并未全面崩塌，但现金回报与融资估值压力仍压制部分公司。 |
| 反证与缺口 | H100租金2.90、官方公司增长，是全面需求衰退反证。 |
| 确认条件 | 企业自由现金流、融资与价格承接同步改善。 |
| 失效条件 | 订单/指引下修、资本投入长期超过现金生成且融资收紧。 |
| 观察期限 | 下一季度并每日跟踪风险 |
| 条件式指导 | 用公司整体FCFF情景，保留META输入缺口。 |
| 主观置信等级 | medium |
| 判断变化原因 | 五家披露日期未变，更新价格；H100又升，BE股价却大跌。 |

## AI增长与现金回收的冲突 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 五家公司SEC最新10-Q/10-K列表本次均重新检查；META最新仍为10月22日。H100租金更新至23日2.90美元/GPU小时，7日+11.1%。 |
| 事实：市场反应 | NVDA−0.59%、META−0.96%、CRWV−2.46%；MU+2.46%、DRAM+3.02%，SNDK−1.82%、BE−11.24%、WDC−2.97%。 |
| 推断：解释 | 推断：需求增长和估值/融资压力并存，内部严重分化；不能把MU反弹推广到所有存储和电力链。 |
| 受益篮子 | ["现金兑现能力较强的AI供应商观察"] |
| 受损篮子 | ["高预期、依赖融资的算力扩张"] |
| 反证 | 算力租金上涨且企业收入增长，是需求已普遍坍塌的反证。 |
| 下一催化剂 | 下一周云厂商与SNDK披露、现金流与租赁资本投入核对 |
| 证据 | ["https://www.silicondata.com/products/silicon-index/h100", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://www.bloomenergy.com/news/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance/", "https://investor.wdc.com/node/28921/pdf"] |

## 防御与等权相对占优 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 前一日防御轮动未在23日延续；这是一天证据变化，不是把中期结构全部推翻。 |
| 事实：市场反应 | XLP−1.92%、XLV−1.11%、XLF−1.32%、RSP−0.77%；但RSP五日+1.14%、仍在20日线上。 |
| 推断：解释 | 推断：昨日赢家也遭减仓，市场承接不广；周末前风险控制可能参与其中，但无法确认交易者身份。 |
| 受益篮子 | ["等待等权与金融重新承接"] |
| 受损篮子 | ["追逐前一天防御涨幅"] |
| 反证 | RSP、XLV、XLF尚有五日相对优势；单日反转不等于基本面恶化。 |
| 下一催化剂 | 下一常规交易日能否与科技一起上涨 |
| 证据 | ["https://finance.yahoo.com/quote/RSP/history/"] |

## 油价压力与避险分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | WTI Yahoo连续合约103.44；同规则10月触105合约84.5%，较昨晚53%升31.5个百分点。SLB官方Q3收入94.5亿美元、自由现金流8.28亿美元。 |
| 事实：市场反应 | XLE+2.60%、XOP+2.45%、OIH+5.40%；GLD−0.65%、TLT−0.49%，美元UUP+0.21%。 |
| 推断：解释 | 推断：供给风险和油服经营改善共同支持能源；能源上涨同时可能压迫其他行业利润与贴现率。不是所有避险资产都涨。 |
| 受益篮子 | ["XLE", "XOP", "OIH观察"] |
| 受损篮子 | ["能源成本敏感消费/工业", "长久期成长"] |
| 反证 | 若实际通航恢复或需求破坏，油价与能源股可能迅速回吐。 |
| 下一催化剂 | 周末实际通航与供应公告、FOMC |
| 证据 | ["https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-third-quarter-2026-results", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026", "https://finance.yahoo.com/markets/article/brent-crude-tops-116-as-traders-price-in-middle-east-escalation-192101547.html"] |

## 网络安全与软件相对强势 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | CrowdStrike于21日披露PHP2Shell防护；OpenAI23日安全报告说明已于10月1日恢复前沿RL训练和内部推理。发生与披露时间分开。 |
| 事实：市场反应 | IGV+1.72%、SKYY+1.85%、CIBR+3.22%；IGV五日+5.99%，已在20日线上，强于仍远低均线的SMH。 |
| 推断：解释 | 推断：安全防护需求是可核验主题线索；今日涨幅不能完全归因于单条公告，也不能假定已转化为订单收入。 |
| 受益篮子 | ["IGV", "CIBR", "SKYY观察"] |
| 受损篮子 | ["只看硬件跌幅而忽略强势应用篮子"] |
| 反证 | IGV日成交量约前20日均量0.84倍，持续买盘尚需验证；公司自身陈述存在商业立场。 |
| 下一催化剂 | 下周能否守住回踩低点与20日线，随后订单/收入兑现 |
| 证据 | ["https://www.crowdstrike.com/en-us/blog/crowdstrike-protects-customers-from-php-rce-zero-days/", "https://openai.com/index/securing-our-frontier-model-training-environment/"] |

## 财报后的跌幅收窄仍需常规买盘确认 · 失效

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 此前盘前WDC/BE修复剧本未延续到常规收盘；官方增长不等于股票应立即上涨。 |
| 事实：市场反应 | WDC343.67、BE193.30，分别较22日收盘−2.97%、−11.24%；盘后样本339.68/190.88仍弱。 |
| 推断：解释 | 推断：市场对高预期的惩罚仍在；不能因盘前跌幅收窄即视为卖压结束。 |
| 受益篮子 | ["等待重新筑底的观察项"] |
| 受损篮子 | ["BE", "WDC追涨抄底"] |
| 反证 | 收入与指引仍增长，价格弱不证明订单已崩溃；WDC是HDD，不能替代SNDK的NAND财报。 |
| 下一催化剂 | 10月26日是否停止创新低，SNDK29日正式财报 |
| 证据 | ["https://www.bloomenergy.com/news/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance/", "https://investor.wdc.com/node/28921/pdf", "https://investor.sandisk.com/"] |

## 航天重组仍属于事件观察 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Tesla/SpaceX年底正式控制权交易公告合约18.5%，相对昨晚不变。 |
| 事实：市场反应 | ITA−1.10%，ARKX+0.71%，航天篮子也不一致。 |
| 推断：解释 | 本次未核验正式合并公告，仍不把传闻当交易落地。 |
| 受益篮子 | ["航天事件观察"] |
| 受损篮子 | ["传闻驱动追价"] |
| 反证 | 少数股权投资或讨论不满足控制权公告条件。 |
| 下一催化剂 | 正式公司公告，日期未定 |
| 证据 | ["https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 760.53 | 缺失 | 2026-10-23T23:17:31+00:00 | 2026-10-23T23:17:31+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| QQQ | 704.27 | 缺失 | 2026-10-23T23:17:00+00:00 | 2026-10-23T23:17:00+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| SMH | 527.00 | 缺失 | 2026-10-23T23:13:40+00:00 | 2026-10-23T23:13:40+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| IWM | 275.61 | 缺失 | 2026-10-23T23:13:05+00:00 | 2026-10-23T23:13:05+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| RSP | 216.88 | 缺失 | 2026-10-23T22:51:00+00:00 | 2026-10-23T22:51:00+00:00 | 2026-10-23T23:18:35.350046+00:00 | stale |
| NVDA | 210.96 | -0.59 | 缺失 | 缺失 | 2026-10-23T23:18:35.350046+00:00 | unverified_trade_timestamp |
| MSFT | 524.51 | 0.66 | 缺失 | 缺失 | 2026-10-23T23:18:35.350046+00:00 | unverified_trade_timestamp |
| AMZN | 248 | -0.95 | 缺失 | 缺失 | 2026-10-23T23:18:35.350046+00:00 | unverified_trade_timestamp |
| GOOGL | 320.21 | -1.24 | 缺失 | 缺失 | 2026-10-23T23:18:35.350046+00:00 | unverified_trade_timestamp |
| META | 642.62 | -0.96 | 缺失 | 缺失 | 2026-10-23T23:18:35.350046+00:00 | unverified_trade_timestamp |
| MU | 874.02 | 缺失 | 2026-10-23T23:17:37+00:00 | 2026-10-23T23:17:37+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| SNDK | 1,232.00 | 缺失 | 2026-10-23T23:16:40+00:00 | 2026-10-23T23:16:40+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| BE | 190.88 | 缺失 | 2026-10-23T23:17:19+00:00 | 2026-10-23T23:17:19+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| WDC | 339.68 | 缺失 | 2026-10-23T23:16:29+00:00 | 2026-10-23T23:16:29+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| DRAM | 46.79 | 缺失 | 2026-10-23T23:17:00+00:00 | 2026-10-23T23:17:00+00:00 | 2026-10-23T23:18:35.350046+00:00 | ok |
| IGV | 110.58 | 缺失 | 2026-10-23T23:02:41+00:00 | 2026-10-23T23:02:41+00:00 | 2026-10-23T23:18:35.350046+00:00 | stale |
| XLE | 69.37 | 缺失 | 2026-10-23T22:47:00+00:00 | 2026-10-23T22:47:00+00:00 | 2026-10-23T23:18:35.350046+00:00 | stale |
| CIBR | 106.52 | 缺失 | 2026-10-23T22:42:00+00:00 | 2026-10-23T22:42:00+00:00 | 2026-10-23T23:18:35.350046+00:00 | stale |
| SKYY | 167.20 | 缺失 | 2026-10-23T20:01:34+00:00 | 2026-10-23T20:01:34+00:00 | 2026-10-23T23:18:35.350046+00:00 | stale |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 759.97 | USD_per_share | 2026-10-23 | -0.52 | -0.43 | -1.48 | ok |
| QQQ | 704.40 | USD_per_share | 2026-10-23 | -0.01 | -0.76 | -5.39 | ok |
| IWM | 275.75 | USD_per_share | 2026-10-23 | -0.33 | 1.96 | -2.21 | ok |
| RSP | 216.54 | USD_per_share | 2026-10-23 | -0.77 | 1.14 | 2.57 | ok |
| GLD | 366.61 | USD_per_share | 2026-10-23 | -0.65 | -4.03 | -6.81 | ok |
| GC=F | 4,010.00 | USD_per_troy_ounce | 2026-10-23 | -1.24 | -4.09 | -7.20 | ok |
| CL=F | 103.44 | USD_per_barrel | 2026-10-23 | 3.99 | 2.00 | 11.94 | ok |
| BZ=F | 111.66 | USD_per_barrel | 2026-10-23 | -1.33 | 1.64 | 7.04 | ok |
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

结构性避险扩大，仍未确认系统性恐慌。23日Yahoo VIX19.45、VIX3M20.48，近月仍低于三个月（波动率指数关系，不是期货曲线）；MOVE103.31较22日下降3.30%，不支持所有风险指标同步爆发。Cboe官方文件本次仍只到22日19.03。FRED最新HY340bp/IG89bp截至22日，较此前327/88扩大13/1bp；名义2年4.65%、10年4.96%、实际10年2.64%亦截至22日，不冒充23日实时。23日Yahoo TNX4.988%与其22日4.953%相比+3.5bp，口径分开。盈亏平衡通胀率23日2.34%。密歇根10月终值48.0，一年/长期通胀预期4.7%/3.5%，较9月4.6%/3.4%上升。Reuters转载PMI综合57.6低于58.4但仍扩张，产出价格59.8高于58.4；这是增长尚强而通胀黏性的组合，不是已证实衰退。WTI连续103.44、黄金4010为20:59UTC附近最新样本而非结算价。Brent Yahoo111.66与新闻明确12月交割结算116.72存在冲突，历史序列自动显示−1.33%亦与新闻上涨矛盾，暂不用于方向/收益/跨期判断；ICE/CME公开页未解决。STLFSI−0.6328截至16日、GPR248.66截至19日，只作滞后背景；CNN缺失。

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
| CBOE_VIX | 19.03 | index | 2026-10-22 | 3.36 | lagged | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLI | 工业 | -1.27 | -1.87 | -3.41 | -0.74 | -1.44 | -1.93 | 0.95 | 2026-10-23 |
| XLV | 医疗 | -1.11 | 1.45 | 5.03 | -0.59 | 1.88 | 6.50 | 0.90 | 2026-10-23 |
| XLP | 必需消费 | -1.92 | 0.73 | 7.56 | -1.40 | 1.16 | 9.03 | 1.46 | 2026-10-23 |
| XLY | 可选消费 | -1.66 | 0.57 | 2.30 | -1.14 | 1.00 | 3.77 | 0.90 | 2026-10-23 |
| XLC | 通信 | -1.78 | -4.36 | -6.60 | -1.26 | -3.93 | -5.12 | 0.83 | 2026-10-23 |
| XLU | 公用事业 | -0.72 | 0.83 | 7.72 | -0.20 | 1.26 | 9.19 | 0.51 | 2026-10-23 |
| XLRE | 房地产 | 0.12 | 0.97 | 2.43 | 0.64 | 1.40 | 3.91 | 1.22 | 2026-10-23 |
| XLB | 材料 | -0.74 | 0.77 | 3.03 | -0.21 | 1.20 | 4.51 | 0.72 | 2026-10-23 |
| SMH | 半导体 | 0.74 | -2.33 | -13.08 | 1.26 | -1.90 | -11.61 | 0.90 | 2026-10-23 |
| IGV | 软件 | 1.72 | 5.99 | 4.32 | 2.24 | 6.42 | 5.80 | 0.84 | 2026-10-23 |
| XOP | 油气开采 | 2.45 | 0.65 | 11.12 | 2.97 | 1.08 | 12.60 | 0.94 | 2026-10-23 |
| OIH | 油服 | 5.40 | 3.97 | 0.93 | 5.92 | 4.40 | 2.41 | 2.13 | 2026-10-23 |
| ITA | 航空与国防 | -1.10 | -3.27 | -5.42 | -0.58 | -2.84 | -3.94 | 1.00 | 2026-10-23 |
| ARKX | 航天主题 | 0.71 | -0.12 | -8.73 | 1.23 | 0.31 | -7.26 | 0.55 | 2026-10-23 |
| KRE | 区域银行 | 0.07 | 3.80 | 1.27 | 0.59 | 4.23 | 2.75 | 0.99 | 2026-10-23 |
| SKYY | 云计算 | 1.85 | 5.58 | 1.63 | 2.37 | 6.01 | 3.10 | 2.80 | 2026-10-23 |

## 资金证据分层

固定19个板块/主题ETF按22→23日同端点比较。能源XLE+2.60%、油服OIH+5.40%、软件IGV+1.72%、云SKYY+1.85%领先；OIH和SKYY量比分别2.13/2.80，但量能不证明净申购。SMH+0.74%却五日−2.33%、低于20日线9.96%，修复质量弱于IGV（五日+5.99%、高于20日线1.85%）。网络安全额外样本CIBR+3.22%，不混入固定19ETF统计。XLP/XLV/XLF日内优势逆转，RSP−0.77%、IWM−0.33%，并未确认广泛风险偏好。发行人SPY/SMH可见净值仍截至22日，未取得23日连续份额与拆分桥；ICI最近可核验窗口仍截至14日（总净发行532.62亿美元、国内股票296.70亿美元），不能解释23日主力去向。机构持仓披露具有滞后，新闻中的去杠杆说法未取得原始PB数据，不定量归因。

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

2026-10-23T23:23:15.247073+00:00采集25主题及跟踪ID，共1532个活跃候选；新增补查AI training pause、cybersecurity、Sandisk earnings。网络安全未查到；SNDK EPS合约5778699固定阈值47.15美元，盘口17个百分点、流动性仅390.72美元，不纳入定量预警。训练暂停与全面停训规则不同且流动性弱，不把OpenAI旧事件当新结算。九个重点合约规则hash与昨晚一致；两页截断继续标缺口。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.3, {"status": "comparable", "change_pp": 0.40000000000000036}] | {"spread": 0.010000000000000009, "volume24h_usd": 1377.4378, "liquidity_usd": 38049.39289, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["年底AI仅较昨晚+0.4个百分点，小于1个百分点价差，保持观察而非升级警报。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [84.5, {"status": "comparable", "change_pp": 31.499999999999993}] | {"spread": 0.030000000000000027, "volume24h_usd": 25196.822101, "liquidity_usd": 27515.1044, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["WTI触105较昨晚+31.5个百分点，超过当前3个百分点价差；能源ETF走强与供应风险线索配合，仍需同交割与实物证据。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by October 31?", "10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583"] | [0.44999999999999996, {"status": "comparable", "change_pp": 0.09999999999999996}] | {"spread": 0.001, "volume24h_usd": 152807.885715, "liquidity_usd": 146026.57117, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2026-11-01T03:59:00+00:00"} | ["Strait of Hormuz traffic returns to normal by October 31?；专门规则解释，变化须结合价差和经营证据。", "航运恢复速度影响供给风险溢价"] | ["IMF同口径船舶通行7日均值回升", "只有口头提议、无实际通航"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 14071.197193, "liquidity_usd": 613839.8652, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Strait of Hormuz traffic returns to normal by December 31?；专门规则解释，变化须结合价差和经营证据。", "能源中期风险"] | ["实际船舶数据支持改善", "封锁和袭击持续"] | [null, null] |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [75.0, {"status": "comparable", "change_pp": -2.500000000000002}] | {"spread": 0.020000000000000018, "volume24h_usd": 265009.64751800004, "liquidity_usd": 56558.4276, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["US x Iran ceasefire continues through October 31?；专门规则解释，变化须结合价差和经营证据。", "定义差异解释与通航低概率并存"] | ["可信报道符合专门规则", "其他交战行动不能自动当本合约失效"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [73.0, {"status": "comparable", "change_pp": 0.5000000000000004}] | {"spread": 0.020000000000000018, "volume24h_usd": 13475.528782, "liquidity_usd": 227694.0465, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?；专门规则解释，变化须结合价差和经营证据。", "贴现率影响长久期资产"] | ["后续通胀及官方政策支持", "通胀缓解及政策转向"] | [null, null] |
| ["Tesla and SpaceX merger officially announced by December 31?", "2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。", "https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] | [18.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 1018.9836089999999, "liquidity_usd": 30998.3963, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Tesla and SpaceX merger officially announced by December 31?；专门规则解释，变化须结合价差和经营证据。", "航天/汽车事件溢价与融资结构"] | ["正式公告符合控制权转移要求，并核验资产价格反应", "仅委员会讨论、少数股权投资或传闻"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [92.5, {"status": "comparable", "change_pp": -1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 1176041.4923029998, "liquidity_usd": 685110.2812, "quality_flags": [], "retrieved_at": "2026-10-23T23:18:31.676052+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["Will there be no change in Fed interest rates after the October 2026 meeting?；专门规则解释，变化须结合价差和经营证据。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 92.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, 6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [1176041.4923029998, 685110.2812] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:14:38.547954Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 75.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.5, -2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.500000000000002} |
| 24h成交量 / 流动性 USD | [265009.64751800004, 56558.4276] |
| 价差 pp | 2.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:16:39.04771Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.45 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.35, -0.25] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.09999999999999996} |
| 24h成交量 / 流动性 USD | [152807.885715, 146026.57117] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:16:39.04771Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 84.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [45.0, 39.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 31.499999999999993} |
| 24h成交量 / 流动性 USD | [25196.822101, 27515.1044] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:16:39.04771Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [14071.197193, 613839.8652] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:16:39.04771Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 73.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, -3.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5000000000000004} |
| 24h成交量 / 流动性 USD | [13475.528782, 227694.0465] |
| 价差 pp | 2.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:14:38.547954Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.30 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.15, 2.6] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.40000000000000036} |
| 24h成交量 / 流动性 USD | [1377.4378, 38049.39289] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:12:37.451988Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 18.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1018.9836089999999, 30998.3963] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-23T23:12:37.451988Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 21.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, 2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5000000000000004} |
| 24h成交量 / 流动性 USD | [273.49, 11382.8945] |
| 价差 pp | 2.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-23T23:12:37.451988Z |
| 抓取时间 | 2026-10-23T23:18:31.676052+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI 压力：合约、经营与估值分开

三层分开。合约层：年底AI严重下行专门合约9.3%，较昨晚8.9%升0.4个百分点，小于当前1个百分点价差；不视为有效风险跃迁。2027年6月底21%，24h仅273.49美元、价差2个百分点，低信息权重。两者要求90日窗口内至少三项规定严重事件，不是股价普通回调概率。经营层：H10023日2.90美元、7日+11.1%，与全面算力过剩解释矛盾；但META多年度承诺、CRWV弱势、BE财报后重挫仍提示现金回报和融资脆弱性。OpenAI23日披露的是10月1日恢复RL训练，不能写成当日全面停训或当日需求新增。估值层：本次SEC重新核验五家最新财报列表，日期未变（NVDA8/26、MSFT7/29、AMZN7/31、GOOGL7/23、META10/22）；前四家复用核验FCFF底稿并更新23日收盘价格，假设与观测分开。META融资租赁资产新增/净债务缺口仍阻止精确估值。模型是公司整体五年FCFF和终值情景，不能全部归因AI，主观情景不是概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-23T23:19:38.031027+00:00", "latest_filing_date": "2026-08-26"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-23T23:19:40.635192+00:00", "latest_filing_date": "2026-07-29"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-23T23:19:43.659960+00:00", "latest_filing_date": "2026-07-31"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-23T23:19:46.215372+00:00", "latest_filing_date": "2026-07-23"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-23T23:19:48.593464+00:00", "latest_filing_date": "2026-10-22"} |
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
| 确认条件 | 先观察QQQ收复709.30、SMH收复533.34并回踩不破，SPY同步收复763.47、RSP跟涨；下一层为连续收盘改善并收复动态20日线（当前QQQ735.24、SMH585.54）。价格只是观察位，不保证突破有效。 |
| 失效条件 | QQQ701.16、SMH521.47、SPY758.68失守且反抽不能收回；或科技上涨但等权继续走弱、油价信用压力再上行。 |
| 观察期限 | 10月26日至未来5个交易日 |
| 反证 | MU/DRAM收涨与软件强势是积极反证；缺成分广度和可靠逐笔VWAP，不能据一次反抽宣告反转。 |
| 状态 | 观察中 |

## 优先观察软件与网络安全的持续性

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | PHP2Shell防护需求、AI训练安全支出线索 |
| 关联标的 | ["IGV", "CIBR", "SKYY"] |
| 确认条件 | IGV回踩当前20日线108.58附近守住，形成更高低点，再突破23日高点；CIBR需独立确认回踩与成交，不能复制IGV价格位。 |
| 失效条件 | IGV收盘跌回108.58之下并反抽失败；安全新闻没有转化为持续相对强势，或大盘跌破前低。 |
| 观察期限 | 未来1–5个交易日 |
| 反证 | 单日事件涨幅可能过度；没有新增订单/一致预期上修证据，不把主题热度等同盈利。 |
| 状态 | 观察中 |

## 能源强势中的回踩机会

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 供应扰动与SLB经营改善 |
| 关联标的 | ["XLE", "OIH", "XOP"] |
| 确认条件 | 等待回踩后更高低点、相对SPY继续领先；XLE当前20日线65.40仅为结构参考，不能追高后把远处均线当近距离止损。 |
| 失效条件 | 油价同交割合约回落、通航实际改善，同时ETF跌破回踩低点；周末缓和造成跳空则重新估计入场风险。 |
| 观察期限 | 下周1–5个交易日 |
| 反证 | 油价涨会压需求，新闻风险可骤变；不以战争必持续作为交易前提。 |
| 状态 | 观察中 |

## 存储只做有条件观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | SNDK10月29日财报与板块修复 |
| 关联标的 | ["MU", "SNDK", "DRAM", "SMH"] |
| 确认条件 | MU和SMH共同突破23日高点且回踩守住；SNDK至少收回22日收盘1260.93并相对SMH停止走弱，再核验财报前后现金流/指引。 |
| 失效条件 | MU反弹回吐并跌破23日低点858.34，或SMH521.47失守；SNDK继续低于前收并创新低。 |
| 观察期限 | 下一交易日至SNDK财报后两个交易日 |
| 反证 | MU/DRAM上涨不等于NAND/SNDK同步改善；无杠杆标的优先于日复位杠杆ETF，避免把高波动放大为仓位赌注。 |
| 状态 | 观察中 |

## 财报跌后等待重新筑底

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | BE/WDC财报后市场再定价 |
| 关联标的 | ["BE", "WDC"] |
| 确认条件 | 先停止创新低，再出现更高低点与收盘收复前一交易日关键结构，结合电话会和现金回收核验。 |
| 失效条件 | BE失守23日189附近低点且反抽失败，或WDC持续创新低；不得以收入增长抵消价格失效。 |
| 观察期限 | 未来3–10个交易日 |
| 反证 | 经营数据增长仍强，但精确一致预期及完整电话会证据缺失。 |
| 状态 | 观察中 |

## 跨期比较与上期剧本复核

对照10月23日20:07北京时间晚报：常规交易已完成，QQQ由盘前近持平到收盘−0.01%，SMH盘前小涨最终+0.74%；盘中本地取证16:46UTC QQQ707.85/SMH530.44，收盘回至704.40/527.20，反弹未守住全部涨幅。QQQ盘中跌破昨日701.90至701.16后收回，但未突破709.30收盘；SMH守住昨日520.53，未守住上午区间高529.45。原防御优先日内剧本减弱，WDC/BE修复失效；软件和能源获得新增确认。九个重点合约规则hash完全相同：不变93.5→92.5%、12月加25bp72.5→73%（小于2个百分点价差）、WTI触105 53→84.5%、月底正常通航0.35→0.45%、年底通航11.5不变、停火77.5→75%、AI年底8.9→9.3%。远期AI20.5→21%低成交不强化结论。与最近已发布realtime（10月18日）相比，AI回报与能源风险主线仍在，新增证据为周四急跌后的周五修复失败和安全软件领先；不把当时周末数据称为最新。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-22/20261023T120705.216296Z/evidence.json",
    "baseline_cutoff": "2026-10-23T12:07:01.886830+00:00",
    "close_change_pct": {
      "SPY": -0.5222853493339064,
      "QQQ": -0.009928924151680896,
      "IWM": -0.3325309513438346,
      "RSP": -0.7698689053122987,
      "GLD": -0.6477004467310254,
      "GC=F": -1.2412546437767902,
      "CL=F": 3.9911542897184793,
      "BZ=F": -1.334271035846224,
      "TLT": -0.4893583757434872,
      "UUP": 0.20761061153755644,
      "HYG": -0.06484490707229229,
      "LQD": -0.41235165919578654,
      "^VIX": 2.20704183467888,
      "^VIX3M": 1.7892578925789326,
      "^VVIX": 1.6305303567056395,
      "^MOVE": -3.301848392985529,
      "NVDA": -0.5890391406873863,
      "MSFT": 0.6582468264542563,
      "AMZN": -0.950557087785997,
      "GOOGL": -1.236817516046862,
      "META": -0.96015730957284,
      "CRWV": -2.455032196457463,
      "MU": 2.4588725844689296,
      "DRAM": 3.021018079894522,
      "VRT": -0.6493118449053537,
      "XLK": 0.4880988304942102,
      "XLE": 2.604709403846983,
      "XLF": -1.323918763986942,
      "XLI": -1.265519501241763,
      "XLV": -1.114177737704869,
      "XLP": -1.9224311241322622,
      "XLY": -1.6607283076535917,
      "XLC": -1.7780637360567564,
      "XLU": -0.7231107215241561,
      "XLRE": 0.11758992596957452,
      "XLB": -0.7351465728645201,
      "SMH": 0.7356523933689463,
      "IGV": 1.7200102062097988,
      "XOP": 2.448319928768039,
      "OIH": 5.400526618451584,
      "ITA": -1.1003521356671153,
      "ARKX": 0.7087445081650712,
      "KRE": 0.06904491069572583,
      "SKYY": 1.8500445171808044
    },
    "quote_change_pct": {
      "SPY": {
        "change_pct": -0.2085891985514121,
        "from_observed_at": "2026-10-23T12:02:10+00:00",
        "to_observed_at": "2026-10-23T23:17:31+00:00"
      },
      "QQQ": {
        "change_pct": 0.02724122258832562,
        "from_observed_at": "2026-10-23T12:01:53+00:00",
        "to_observed_at": "2026-10-23T23:17:00+00:00"
      },
      "SMH": {
        "change_pct": 0.15026340279429284,
        "from_observed_at": "2026-10-23T12:01:11+00:00",
        "to_observed_at": "2026-10-23T23:13:40+00:00"
      },
      "BE": {
        "change_pct": -9.243058197033093,
        "from_observed_at": "2026-10-23T12:02:19+00:00",
        "to_observed_at": "2026-10-23T23:17:19+00:00"
      },
      "WDC": {
        "change_pct": -1.5420289855072489,
        "from_observed_at": "2026-10-23T12:02:19+00:00",
        "to_observed_at": "2026-10-23T23:16:29+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": -0.15999999999999925,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "BAMLH0A0HYM2": {
        "change": 0.1299999999999999,
        "unit": "percentage_points",
        "observation_date": "2026-10-22"
      },
      "BAMLC0A0CM": {
        "change": 0.010000000000000009,
        "unit": "percentage_points",
        "observation_date": "2026-10-22"
      },
      "DGS10": {
        "change": -0.16999999999999993,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "DFII10": {
        "change": -0.11999999999999966,
        "unit": "percent",
        "observation_date": "2026-10-22"
      },
      "T10YIE": {
        "change": 0.020000000000000018,
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
        "change_pp": -1.0000000000000009
      },
      "4641065": {
        "status": "comparable",
        "change_pp": -2.500000000000002
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.09999999999999996
      },
      "4951227": {
        "status": "comparable",
        "change_pp": 31.499999999999993
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.5000000000000004
      },
      "691340": {
        "status": "comparable",
        "change_pp": 0.40000000000000036
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.5000000000000004
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
    "event": "下一次美股常规开盘；周末消息需重新取证",
    "date": "2026-10-26T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
  },
  {
    "event": "FOMC会议结束与政策决定",
    "date": "2026-10-28T14:00:00-04:00",
    "source": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"
  },
  {
    "event": "Sandisk FY2027 Q1电话会；财报当天盘后公布，具体发布分钟未核验",
    "date": "2026-10-29T16:30:00-04:00",
    "source": "https://investor.sandisk.com/"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| michigan-final-oct26 | 10月终值消费者信心48.0，一年/长期通胀预期4.7%/3.5%；均较9月上升。 | 2026-10-23T10:00:00-04:00 | [{"source": "https://www.sca.isr.umich.edu/", "published_at": null, "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |
| pmi-oct26-flash | Reuters转载核验：综合57.6、前值58.4；产出价格59.8高于58.4。一级公告本次未取得。 | 缺失 | [{"source": "https://theedgemalaysia.com/node/823082", "published_at": null, "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |
| slb-q3-2026 | SLB官方Q3收入94.5亿美元，同比增长6%；自由现金流8.28亿美元。 | 缺失 | [{"source": "https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-third-quarter-2026-results", "published_at": null, "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |
| php2shell-defense | CrowdStrike21日官方安全博客支持网络安全需求主题，但不证明当期新增收入。 | 缺失 | [{"source": "https://www.crowdstrike.com/en-us/blog/crowdstrike-protects-customers-from-php-rce-zero-days/", "published_at": null, "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |
| openai-training-resumed-oct1 | OpenAI23日披露，10月1日已恢复前沿RL训练和内部推理；不能当作23日新停训。 | 缺失 | [{"source": "https://openai.com/index/securing-our-frontier-model-training-environment/", "published_at": null, "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |
| brent-oct23-conflict | Yahoo新闻检索摘要明确12月Brent结算116.72，正文不可访问；与同站行情111.66冲突，暂不用于定量方向。 | 缺失 | [{"source": "https://finance.yahoo.com/markets/article/brent-crude-tops-116-as-traders-price-in-middle-east-escalation-192101547.html", "published_at": null, "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |
| canada-tariff-oct23 | AP报道部分加拿大商品关税调整10月30日生效；原始法律附件未核验，不推算行业盈利影响。 | 缺失 | [{"source": "https://apnews.com/article/ede51283125c071561178e6455048994", "published_at": "2026-10-23T20:28:18+00:00", "retrieved_at": "2026-10-23T23:23:15.247073+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN接口418且官网受限，保留缺失，不以tc温度代替。",
  "Brent Yahoo连续111.66与新闻12月结算116.72矛盾，自动序列1日−1.33%不参与方向和跨期结论；期货最新价不是结算价。",
  "tc报价时间是统一请求时间，已标成交时戳未验证；当前盘后核心报价由Yahoo分钟时间补充。",
  "新闻广域50条has_more；11标的定向39条无has_more仍非全市场覆盖。新闻全文及原响应仅本地。",
  "Polymarket若干两页截断；SNDK新合约宽价差低流动性不做有效概率，AI远期成交低；无完整盘口。",
  "19ETF连续份额和拆分桥缺失，发行人只到22日，ICI14日窗口不等于本日流量；无当期机构净交易数据。",
  "全市场成分涨跌广度、盈利一致预期修正及CME独立政策概率缺失。",
  "常规分钟成交量部分与日线/tc显著不一致，本次不使用未核验VWAP或分钟量作为触发证据。",
  "FRED信用/名义实际利率至22日，Cboe官方VIX至22日，GPR至19日、金融压力至16日；不当实时。",
  "META融资租赁资产新增及净债务缺口，继续暂停精确估值；其余底稿复用并本次核验披露列表。",
  "DRAM长历史不足；无法凭低价高质叙事量化中国厂商对各类存储利润冲击。",
  "PMI采用可访问Reuters转载；SLB搜索官方摘要可得正文受限。加拿大关税法律附件和新增伊朗军事行动原始公告未核验，相关社交线索不当已发生事实。",
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
  "tc 报价质量 stale: RSP, IGV, XLE, CIBR, SKYY；不作为新成交证据",
  "tc 报价质量 unverified_trade_timestamp: NVDA, MSFT, AMZN, GOOGL, META；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.RSP.value, quotes.NVDA.value, quotes.MSFT.value, quotes.AMZN.value, quotes.GOOGL.value, quotes.META.value, quotes.IGV.value, quotes.XLE.value, quotes.CIBR.value, quotes.SKYY.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.sca.isr.umich.edu/",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "本次官方终值，实际请求200"
  },
  {
    "url": "https://theedgemalaysia.com/node/823082",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "Reuters转载正文requests200；一级PMI公告缺失"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "23日2.90与7日+11.1%"
  },
  {
    "url": "https://www.crowdstrike.com/en-us/blog/crowdstrike-protects-customers-from-php-rce-zero-days/",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "21日官方博客"
  },
  {
    "url": "https://openai.com/index/securing-our-frontier-model-training-environment/",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "23日官方披露；10月1日恢复，事件时间分开"
  },
  {
    "url": "https://investorcenter.slb.com/news-releases/news-release-details/slb-announces-third-quarter-2026-results",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "官方搜索摘要核验收入现金流；正文访问受限"
  },
  {
    "url": "https://investor.sandisk.com/",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "官方IR确认29日16:30ET电话会"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "官方会议日期"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "仍截至14日"
  },
  {
    "url": "https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "NAV仍截至22日"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "NAV仍截至22日"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "官网robots限制，接口418"
  },
  {
    "url": "https://www.ice.com/products/219/Brent-Crude-Futures/data",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "动态页无可核验当前数值"
  },
  {
    "url": "https://www.cmegroup.com/markets/energy/crude-oil/light-sweet-crude.quotes.html",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "动态页无可核验当前结算值"
  },
  {
    "url": "https://finance.yahoo.com/markets/article/brent-crude-tops-116-as-traders-price-in-middle-east-escalation-192101547.html",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "搜索摘要与行情冲突保留"
  },
  {
    "url": "https://www.bloomenergy.com/news/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance/",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "此前官方财报已核验，本次复用"
  },
  {
    "url": "https://investor.wdc.com/node/28921/pdf",
    "checked_at": "2026-10-23T23:23:15.247073+00:00",
    "note": "此前官方财报已核验，本次复用"
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
