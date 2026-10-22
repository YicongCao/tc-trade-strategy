# 每日交易总结 · 2026-10-21

## 一分钟读懂 · Agent 摘要

### 当前判断

今晚更接近反弹受挫、风险重新升温，尚无充分证据认定系统性恐慌；不宜把昨日上涨当成趋势反转。

### 与上次相比

较今早，META由盘后高于昨收转为盘前下跌，QQQ、SMH继续走弱；最新10-Q补充大额长期采购及租赁承诺。FRED已恢复，但利率信用仍滞后。

### 最重要的信号

- 北京时间约20:02，SPY较昨收−0.94%、QQQ−1.58%、SMH−3.18%、META−2.27%，半导体明显偏弱。
- VIX约18.14（19:48观测），高于昨收16.68；黄金ETF盘前也下跌，不能认定资金统一涌向避险资产。
- META约8250亿美元的广义承诺横跨多年且混合不同性质，不是当年现金支出；真正要看兑现收入、现金回收与融资安排。

### 接下来观察

- 开盘30分钟后，QQQ/SMH能否收回常规VWAP并守住开盘低点；若反抽失败、再创新低且油价/波动上行，优先降低反弹假说的权重。
- 即便盘中修复，仍需随后连续两次收盘站稳20日线；关注纽约08:30的LMT电话会与能源供应核验。

### 不要忽略

尚未开盘，无今晚VWAP或回踩结论；油轮损坏为伊方说法，AP未独立确认。CNN、当期板块净申赎与真实广度仍缺。

## 研究结论

北京时间10月22日晚间：反弹置信度下降，盘前科技再度弱于大盘；META现金回收与长期支出承诺、地缘供应风险成为主要压力。最近完整收盘日仍为10月21日，不把今晚盘前下跌写成已完成交易日。等待常规开盘承接，避免用昨日反弹或单条高需求消息替代确认。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-21 → 2026-10-21（纽约交易日） |
| 截止·纽约 | 2026-10-22T08:06:20.692158-04:00 |
| 截止·北京 | 2026-10-22T20:06:20.692158+08:00 |
| 实际生成时间 | 2026-10-22T12:06:20.766262+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-10-22 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-21/20261021T232422.143072Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-22T20:00:00+08:00 |

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
| prices.SPY.value | 773.09 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 0.53 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | 0.45 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | 0.69 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 4.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.88 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 767.35 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 723.24 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | 0.29 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | 0.75 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 6.89 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.07 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.91 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -0.77 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 725.20 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 1.05 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -0.51 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -2.16 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 7.47 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.53 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -0.97 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -2.85 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | 2.86 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 739.07 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 726.35 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 675.27 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -1.88 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -0.16 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 7.39 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 11.26 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.55 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -4.54 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.91 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 276.48 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.25 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 1.88 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -1.93 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -5.51 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.27 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.43 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -2.62 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -10.12 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.75 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 287.13 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 276.95 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -0.46 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -3.71 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -0.17 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.88 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.40 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -9.14 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.60 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 216.64 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 0.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 2.15 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 2.52 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -0.11 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.16 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 1.69 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 1.83 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -4.72 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 211.99 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 215.09 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 205.72 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 2.19 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 0.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.31 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.02 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.93 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -2.39 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.95 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 378.95 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 0.34 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | 0.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -3.55 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | 2.59 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.18 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 0.33 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -4.23 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -2.02 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 381.57 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 395.87 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 414.64 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -0.69 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -4.27 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -8.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 4.93 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.30 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -11.47 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.89 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,150.00 | USD_per_troy_ounce | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 0.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | 1.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -3.90 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | 2.76 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.35 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 0.57 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -4.59 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -1.85 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,182.81 | USD_per_troy_ounce | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,358.26 | USD_per_troy_ounce | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,537.35 | USD_per_troy_ounce | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -0.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -4.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -8.54 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 68.67 | USD_per_troy_ounce | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.65 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -11.66 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.09 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 97.15 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -4.56 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 2.17 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 5.41 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 22.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -5.08 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 1.71 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 4.73 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 17.96 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 93.94 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 92.16 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 84.84 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 3.41 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 5.41 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 14.51 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.42 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.55 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -8.20 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.33 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 108.82 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 0.03 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 2.60 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 5.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 29.41 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -0.50 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 2.15 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 4.88 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 24.80 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 104.92 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 99.75 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 90.63 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 3.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 9.09 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 20.07 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.92 | USD_per_barrel | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.60 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -0.95 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.23 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 80.24 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.14 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 1.71 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 0.13 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -3.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -0.39 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.26 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | -0.56 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -8.22 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 78.48 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.27 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.34 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 2.25 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | -0.04 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -3.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.80 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.00 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -3.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.71 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.92 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.07 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.69 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.94 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 1.19 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -0.46 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | -1.14 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 0.25 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | -3.42 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.92 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.45 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.86 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.64 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.13 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.45 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.56 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 76.98 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.20 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.22 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | -1.00 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.63 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.33 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | -0.23 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | -1.68 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -6.24 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.08 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 78.02 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.90 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | -0.13 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -1.33 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.29 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.37 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.55 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.21 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.54 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | -0.23 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -2.14 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.54 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.08 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | -0.91 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -6.75 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.50 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.92 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.94 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.69 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.69 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -2.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.61 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.59 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -2.59 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.92 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 16.68 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -3.64 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -1.13 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 9.88 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | -19.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -4.16 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -1.58 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 9.19 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | -25.51 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.14 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 15.74 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.17 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 3.35 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 5.95 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | -8.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 1.66 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 9.94 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -19.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-21 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 18.72 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -1.42 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -0.37 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 3.37 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | -5.74 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -1.95 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | -0.83 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 2.68 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | -10.35 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.39 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.42 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.46 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 1.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 1.65 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -8.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 0.91 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 4.86 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -12.93 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-21 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 94.55 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -2.68 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 0.11 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 6.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | -4.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -3.20 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -0.35 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 6.03 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | -8.63 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 90.91 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 89.78 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.50 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 4.00 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 5.31 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -4.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 8.25 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 8.73 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -13.98 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-21 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 95.94 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -5.66 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -3.15 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | 22.12 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 24.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -6.19 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -3.60 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 22.16 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 19.40 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 102.68 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 86.60 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 76.29 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -6.56 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 10.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 25.75 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.03 | index | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.24 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -15.55 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-21 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 221.97 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | 2.54 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | 0.30 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -1.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 12.80 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | 2.02 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -0.15 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -2.26 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | 8.19 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 226.87 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.91 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.12 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -2.16 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -0.42 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 9.28 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 5.89 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.65 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -7.22 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 532.95 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 0.20 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -0.14 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 6.46 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 35.75 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -0.32 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -0.59 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 5.78 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 31.14 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 525.13 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 507.19 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 434.92 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 1.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 5.08 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 22.54 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.12 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.09 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -1.93 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.65 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 262.37 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -0.10 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 3.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 5.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | 13.65 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | -0.62 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 2.81 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 4.57 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 9.04 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.46 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 256.33 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.21 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 3.11 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 2.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 7.88 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 6.47 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.47 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -7.62 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.86 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 334.76 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -1.62 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -3.70 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -0.91 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | 0.38 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | -2.15 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -4.16 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -1.60 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -4.23 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 345.18 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 343.78 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.94 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -3.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -2.62 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -1.81 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.11 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.42 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -11.30 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 697.52 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 0.47 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -5.43 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -6.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 17.64 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -0.05 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -5.88 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -6.95 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 13.03 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 729.54 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 661.21 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.73 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -4.39 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | 5.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | 10.41 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 22.56 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.23 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -10.30 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.46 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 61.82 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -0.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -6.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -28.86 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -8.14 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -1.02 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -6.47 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -29.55 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -12.75 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 79.26 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 85.35 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 92.23 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -22.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -27.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -32.97 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.27 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 10.15 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -42.62 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.63 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 913.67 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 1.96 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -0.05 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -14.75 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 11.37 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 1.44 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -0.50 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -15.43 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 6.76 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 1,008.02 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 985.13 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 726.63 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -9.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -7.25 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 25.74 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 47.14 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.16 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -16.73 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.79 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 49.16 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 3.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -1.95 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -20.58 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | 2.91 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 2.49 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -2.41 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -21.27 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -1.70 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 56.09 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 57.00 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-21 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -12.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -13.76 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-21 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.45 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 4.98 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -22.73 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.74 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 212.15 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 4.22 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -4.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -14.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -21.28 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 3.69 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -5.25 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -15.41 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -25.89 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 235.64 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 251.38 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 268.76 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -9.97 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -15.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -21.06 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 10.99 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -27.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.27 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 188.54 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 1.67 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -0.99 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -3.48 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 10.33 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.15 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -1.45 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -4.17 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 5.72 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 194.50 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.81 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 167.82 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -3.06 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -0.67 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 12.35 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 3.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -6.66 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 68.16 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 0.28 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 0.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 9.28 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 19.10 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -0.25 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 0.33 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 8.60 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 14.49 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 64.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 63.84 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 57.34 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 5.21 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 6.77 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 18.88 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.34 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 1.97 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -0.12 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 56.04 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 0.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 2.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 2.75 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -2.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 0.05 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 2.33 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 2.06 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -6.97 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 54.53 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 56.04 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.35 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 0.00 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 5.04 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.68 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.21 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -3.96 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 168.31 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 0.91 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 0.76 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -1.05 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -7.52 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.38 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 0.31 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -1.74 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -12.13 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.61 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 172.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.34 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -0.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -2.59 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -2.34 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.52 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -9.52 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.99 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 178.94 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.86 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 6.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 7.39 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -1.01 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 2.41 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 5.32 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 2.78 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 171.48 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 170.29 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 156.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 4.35 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 5.08 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 14.13 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 2.99 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.67 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 87.11 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -0.73 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 1.22 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 5.68 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 0.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -1.25 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 0.77 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 4.99 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | -3.89 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 83.59 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 83.94 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.21 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 4.21 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 3.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 4.68 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.14 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.31 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -0.73 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.05 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 115.53 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 0.03 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 3.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 4.41 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 2.94 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -0.50 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 3.16 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 3.72 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -1.67 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 111.61 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.46 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.41 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 3.51 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 1.82 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 0.10 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.52 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.32 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.40 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.92 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 108.97 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.11 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -1.67 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -3.19 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -0.31 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -1.63 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -2.12 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -3.88 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -4.92 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 111.22 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 111.60 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -2.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -2.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -3.39 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.59 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.46 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -5.04 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.48 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.00 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.29 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.67 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.66 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -7.05 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -0.24 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 0.22 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 4.97 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -11.66 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 40.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.75 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.76 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.96 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 0.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -4.03 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.67 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.60 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -8.60 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.14 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.06 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.76 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.37 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 0.53 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -7.82 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -1.28 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 0.92 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | -0.16 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -12.43 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.43 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.77 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.67 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 1.52 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | -1.65 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | -1.42 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.63 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -7.82 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.86 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.32 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 3.32 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 2.07 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | -1.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -0.35 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 2.87 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 1.38 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -6.11 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 49.74 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.92 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.57 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 3.17 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 0.78 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 1.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.69 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.35 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -3.94 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.68 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 556.70 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 1.89 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -1.42 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -7.43 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | 5.12 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 1.37 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -1.88 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -8.12 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | 0.51 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 593.37 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 577.56 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 514.05 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -6.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -3.61 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 8.30 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 16.81 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.02 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -12.18 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.01 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 108.82 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 1.77 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | 1.09 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | 0.67 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 18.57 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 1.24 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | 0.63 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -0.02 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 13.96 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.28 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.10 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.77 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | 0.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 2.56 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 16.05 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.85 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.62 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -3.42 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.26 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 199.02 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -0.51 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 0.60 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 8.96 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 20.10 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -1.04 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 0.14 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 8.27 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 15.49 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 190.39 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 188.76 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 166.95 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 4.53 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 5.44 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 19.21 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.61 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.32 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -0.68 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.72 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 393.58 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 2.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 2.93 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -0.53 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 5.99 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 1.73 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 2.48 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -1.21 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 1.38 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 386.34 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 403.41 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 394.61 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 1.87 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -2.44 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -0.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 9.83 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -9.85 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.92 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 205.79 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -0.17 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 0.76 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -3.80 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -15.90 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -0.70 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 0.31 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -4.49 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -20.51 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 207.42 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 220.38 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 229.46 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | -0.79 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -6.62 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -10.32 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 3.64 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 1.77 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -18.64 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.27 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.55 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 1.56 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 0.08 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -6.49 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -0.07 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 1.04 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -0.37 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -7.18 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -4.67 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.69 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 32.31 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.59 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -3.60 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -5.45 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -6.26 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.72 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -12.36 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.66 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 70.62 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 0.00 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 3.03 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 0.34 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -7.51 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.53 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 2.58 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | -0.35 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -12.12 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 69.91 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 72.34 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.12 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 1.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | -2.38 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 0.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.24 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.75 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -8.86 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 166.63 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 2.01 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 1.59 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -0.54 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 20.83 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 1.49 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 1.14 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -1.23 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 16.22 | pp | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 166.84 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.17 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 135.17 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -0.13 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 1.50 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 23.27 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.52 | USD_per_share | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.71 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -4.72 | percent | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.54 | ratio | 2026-10-21 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.79 | percent | 2026-10-20 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.33 | percentage_points | 2026-10-20 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.87 | percentage_points | 2026-10-20 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.12 | percent | 2026-10-20 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.77 | percent | 2026-10-20 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.37 | percent | 2026-10-21 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.72 | index | 2026-10-09 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 16.68 | index | 2026-10-21 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 248.66 | index | 2026-10-19 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 230.19 | index | 2026-10-19 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 310.16 | index | 2026-10-19 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 177.92 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 176.01 | index | 2026-10-19 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.SPY.value | 765.81 | USD_per_share | 2026-10-22T12:02:11+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.QQQ.value | 713.71 | USD_per_share | 2026-10-22T12:02:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.SMH.value | 539.00 | USD_per_share | 2026-10-22T12:01:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.META.value | 681.72 | USD_per_share | 2026-10-22T12:02:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.NVDA.value | 217.11 | USD_per_share | 2026-10-22T12:02:02+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| live.^VIX.value | 18.14 | index | 2026-10-22T11:48:31+00:00 | lagged | Yahoo最后非空分钟观测；连续期货有换月风险，不与结算或ICE/Pyth规则直接等同 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |
| live.CL=F.value | 99.45 | USD_per_barrel | 2026-10-22T11:53:33+00:00 | lagged | Yahoo最后非空分钟观测；连续期货有换月风险，不与结算或ICE/Pyth规则直接等同 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| live.BZ=F.value | 112.05 | USD_per_barrel | 2026-10-22T11:53:13+00:00 | lagged | Yahoo最后非空分钟观测；连续期货有换月风险，不与结算或ICE/Pyth规则直接等同 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| live.GLD.value | 372.26 | USD_per_share | 2026-10-22T12:03:14+00:00 | ok | Yahoo最后非空分钟观测；连续期货有换月风险，不与结算或ICE/Pyth规则直接等同 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.0400390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19002854522964796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.6051479628451992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.2475561580182037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2974654761385809,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.26400146484377274,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.08877441406252728,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4534997558594114,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4899039835099206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5148962908734234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.49188772929558144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.058576311383928825,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.012420898418212811,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5185586932496489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.07495030598764763,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 7.57000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.1564797942630767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.9741371128658156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8308682725976744,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.155519649133053,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9664512490334287,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.3689891500206164,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5833121145794706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8580541729944722,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8005004882812727,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.14995727539064774,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5465374755858647,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.129314710841478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0217995669569602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0349511402944378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.13571602957589235,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.002525861294636833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9964994328822581,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.061853933433064445,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.70001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.4049727799488876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.215538699961306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.050037814690686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.09121979897262023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5950013251785355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6103907371161066,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8024816566724824,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.20624567716595976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.27200012207032387,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.47451843261717386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.12726638793947131,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.34916569920510065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4022557413265404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.20698054379869602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1971391950334822,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.07504505551785101,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2300437452180777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4036324033522052,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.779998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7914231902447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9451307762751382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0843926517454694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8013580555609967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9814517354743479,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.660017186570061,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.16316350627273435,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.0988235316995771,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2665000915527287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06447082519531477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.12145240783689815,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.23976932290361574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3927063749476378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3171768859140389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06214250837053603,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03214925946323777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.351452524448459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.08795314221361494,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.300018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8815215933001164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8405318351793265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.0584125670066737,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7874842184549156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6914930480704684,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.23538387233412728,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8108564089884709,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.4900187423163347,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6964996337890739,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4401995849609648,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.14904998779297784,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5210369170774332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.43435698634505204,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.34625478472192306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0007106236049105874,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.004286360033085801,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.30369292132215087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11282800770143919,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 7.39990234375,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5992923705254283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.855530080056056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.4426958549707996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.1468098766100887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4092638252957803,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2503821172108567,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19513969695259625,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8493444004715078,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -8.419995117187682,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.822001953125437,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.507499999999709,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3758765542373532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.29659634639150934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19341229047082997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.0785435267857224,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.028991263872113038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.15751846931336644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2566971416066164,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.6399993896484375,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.7544267997869905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.95982245959108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.1973094268253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6462453400589254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.9444553450166384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -7.564970422436279,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.4448655848435044,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9437108161975054,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.24949989318847088,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.27900009155273153,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19415000915526548,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.227760359575374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.369832264254804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.74439502190709,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04571424211774566,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2521349277367859,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.3843894069430895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0163202009513699,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.029998779296875,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.7213240197718407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.33080208400591005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.043603281041319,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 6.287649805488726,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5312954745421927,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.9359500468511088,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.2911594390595225,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.990184329350143,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2869998931884794,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3981999206542923,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2353000068664528,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2558378536203998,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4070078660611358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.27937554983112634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.23928615025111633,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.22094439731725846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.02730637095412769,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3900152222553881,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7059115568529339,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5345086344503702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7151076566415013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.431043597642522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8959401020825819,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.1396565972955695,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4675514986232976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7285090737811029,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.005137634277332381,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.026156616210940342,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.021360397338867188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.13348486599382703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1695546161849637,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.15662714419015789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04714257376534592,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06020373416436653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.13212965037358027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.14847916135482375,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.020000457763671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.41403463873971313,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2733049760439865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.532309405422704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.14069527680147242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.22400609351006517,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.8784529388891857,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.7798655634409077,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.15677019933710845,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.013500022888184304,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.015600013732910867,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.009250001907346928,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.022484447307424826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.014574924783339327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.03733611498182299,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.01214286259242467,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.0423262072219015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.06865931458936991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.06431014497300247,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.15000152587890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19523821723803625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5585939227683911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9088516960722437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.005901631272497987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.005209672008388289,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.046554040076808,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.33870446194596004,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2915638448660829,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03870277404784872,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03492691040040086,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.0019498825073185344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.24463354644777002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.23632504695366707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19503684475258298,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.027143205915178548,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.036058980867468504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.18955784170353596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.08973515532925647,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.01000213623046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3401760945619725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.11759343278343604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.1297358627352705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.30352327966373105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5302046397916205,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.7227413956286353,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.11782029528293325,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6009887558023124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.011682510375976562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03766906738280795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.017168006896980614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0017179868661898468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.02636370619284456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.006345983030875413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03428595406668533,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03315951693929098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.009439887072737463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.24331461777994468,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6299991607666016,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.488478265924887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -14.48578433368991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -11.93419598925909,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -14.321939198576883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.2984497206952392,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -16.090932296535108,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -13.181752147277294,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -16.503439235150573,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.07499999999999929,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04260000228881822,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.006500000953675311,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.4043404785053974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.300052717878811,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.502110109650191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.022142955235072703,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.23381776527118703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.049366725167303,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2700004577636719,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.690444575869754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -6.107517800899065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.468153992820212,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.24991607049454867,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.500416030640106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -7.712665763744264,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.715710150838415,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.047549405644032205,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.030499935150146484,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.003800010681150212,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.001999998092649946,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.6395902496699755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.4447840275535473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.328838490009698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.016428538731166342,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.01739607323836978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.255816082621731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.5999984741210938,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 6.469897033431359,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -13.679552700049857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -10.093369036482258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.29380090119667246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 6.279868488201712,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -15.284700662895055,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -11.340925194500464,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.591266377335252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.29750022888184446,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.07300003051757642,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.020200004577631603,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.210650548264704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.9838787122915553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.6598570678848628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1157139369419653,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11453203861389305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.365570364381142,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.7599945068359375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -6.05857227816563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.7530247659706917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.1230815420345337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -8.12887529638024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -6.248600823395278,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.358172728815891,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.66089527023664,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -8.65426035863485,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8690002441406364,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.40960006713866903,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.16790000915527514,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -6.455301091560905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -7.209712738159803,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -7.843862875791906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.022857121058873275,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3191624823591104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.070417767785541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.826361350932749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.575818283321265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.848148049763878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.514978019831849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.636332805703101,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.9706703204760663,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.6005918917456747,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.2175125436932674,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.17699966430663494,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.09426208496094546,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1714458465576172,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.498730495671575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.426299130260423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.6176826355654557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11357225690569184,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.014970331840906237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.29894661165151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.07982373890803962,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.08001708984375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5123316743968376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9921784575500867,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.33682858042294317,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.2046009717527468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3223031291671896,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3870304947048875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5843847384411474,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5020664478913268,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.6180007934569858,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6017333984375455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3154045104980696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.10736884244006983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.08837996339046139,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1595753186181419,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.17285592215401735,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03673759960634504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19873347420816811,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.016705383482813807,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.260009765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.16758400611408542,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.696495637936568,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.2551028928381234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1479443140516512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3576125513437334,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.09134767509136887,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0075467348199196,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.14952116208693056,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6549995422363395,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.19799987792970342,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.14654998779298012,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3685301926949158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.02235363200944196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.17201135396880396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04571642194475434,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.014966048653482389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.09154629099449263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.09115793547851114,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -5.519989013671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4890639997469082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11094740371905276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.189569872619923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.8892253617912154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6790925449765561,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.494200559126146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9420137146017193,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.186690837929796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.15349884033207672,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1763824462890966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.09417282104493552,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5553571373165487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5549275403123675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.6466334980706265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5578569684709827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.124640891934241,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.4626074825950468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.46996720753224186,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.27001953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.057259083477103,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.524678759318146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5105196406806511,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6421864973421556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8672305382474552,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.919530796472947,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.7580757986988544,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.34472102120357384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.3289978027344205,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9774499511719341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.20210876464841476,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.7510657313925417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.17959858072680301,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4824578223194145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.654998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0791145512884941,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.42053259665300047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6197336487542093,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3100013732910156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.1514464433224023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 14.13158197104981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4721021939543384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.090716428429243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.3414749885520503,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 12.52643400820461,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.7196583519725444,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.7932509522906592,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.2540000915527258,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5700000000000074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.07520000457763842,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8296976936364011,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11970324273785593,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.28124552051532703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.06357165745326476,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.15295795301423354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2877576938932336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5751940390710926,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 17.5999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.939929818855369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.927393033809414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.494226940968602,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 11.811835200641507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.749901273625721,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.322245070964215,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.246670782950396,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 11.514369724502926,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -7.902066040039017,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9057324218750864,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.008740539550786,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.4374350036321477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7028567717184853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9093824203897825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.642002684211036,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3961720318586712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.6040556254480727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.041594966524513444,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.4399986267089844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.279756953135571,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 7.735100585176447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.410552255233036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 11.893179352688621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.089728407905923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 6.129952622331247,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.1629960972148297,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 11.59571387655004,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6370000839233398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03459999084473253,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.522654863578323,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.5769817517927187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.044285637991768656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.24310430340143974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.263437049489305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.16677786319544574,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 8.589996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.442712429565311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 9.421777665887566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.963673314680751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 7.925412730393379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.252683884335663,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 7.816629703042367,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.716117156662545,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 7.627947254254796,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.831500244140642,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.3918188476562534,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19159927368167473,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.3116740057793965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.8629851494180514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.1421756251775435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3721433367047986,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03572113595041415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.248726594605557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.12095874926602224,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.0999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9513270974765407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.530230413064007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.0367983284417246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.8124758966029404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7612985522468927,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.9250824502188073,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.7892421704235213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.5150104204643595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3400001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.05333831787109489,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.22219898223877976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7602340460680206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.6057741559300398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7006970997506041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04785701206752213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.007803196640892018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.5346489330329565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04147025346966671,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.028803924707121453,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3621543517802417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7361108850574496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.939704678118904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1612246205225265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.967302314625441,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.9836670430756538,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.6422392019803222,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.28950023651123047,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1518006896972679,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11090608596801843,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.17762982916420533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04384944322914919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.10163545629884396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04142870221819184,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06645000934326384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.27843266024943913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3992752753016583,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.31999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6243925170955622,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.146229149426703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0714392213884594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6713200343817616,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8144210623252102,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4589188134184963,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.17611693662974437,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9687855105203429,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.07500000000000284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.031123123168946165,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.002941207885740482,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4461207337595585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6262127163834341,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5940592962421443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.021428244454520073,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.045432984758542405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5483815338078402,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2428815664731252,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.5099945068359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8332720008373595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8689703819422587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9856132594035727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.1848427423088,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6432434556077116,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2638224190970595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.26194289861463105,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8873772661702191,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.08950042724609375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3378448486328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04862663269042855,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9480352337694509,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0622893213551698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8488407581322743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.05285753522600434,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.0452509191264443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8117810505287935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3235053267854897,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.863427972367183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.125725015234071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1621453405777462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.0775610367120168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.053456517596831,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.730872978079271,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.085410817440458,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.3750265128505976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5069999694824219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2314111328124966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.12899475097657387,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8241690239102262,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6604504856172921,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6557013589287379,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04214259556361588,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.015252814005565885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.48938096261215147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.034656635620164966,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.6399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.3485401365236127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.0084450865256906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3903825900197777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.760505800084534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5385686817532607,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -4.613593049370889,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.637938748037982,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.057971276223115,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.23400001525878622,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.05946685791015227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.05611034393311343,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.0603597837233636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8365985007087406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8402640179890009,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.023571014404296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.036400435241850104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7293440337873935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.200246836084212,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.029998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8826422011424251,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.819760417730242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.5882596923662007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.4959561392469123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.072670746372073,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7853875451149572,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.34070353434799694,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.7934216153854932,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2439998626708899,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06895904541015341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.020134086608877055,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.19984196680944422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.08826843526299477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.04344872734189931,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.010714394705636066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.009618894676993728,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.025083305344264506,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1386235067740963,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.220001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.1980199118190038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1920422555645951,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.24745643350873037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.99810969323292,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.3880484570486518,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.4131057072806041,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.495012591526934,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -3.295575169371501,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1794998168945341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03868957519530625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03858154296875682,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9373007054305549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.0589501700142945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.048232619894085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04357092721121636,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.023404729339783437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.0631818916802867,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.7966718154660367,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11999893188476562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.970724079575036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6472494425834086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.3295055857829094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5901729743244104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.160752624804684,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9578985202617907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0819494277647057,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2927074981858304,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11249999999999716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.026230697631838495,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0008651733398465922,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.010251192562771294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.3504343894662698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2723104435542911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.017142977033342666,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04552876723598098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2611390667430875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.637303224642346,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.31999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.4589431318140953,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.05898030397242238,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8081659630998828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.208816300698845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.6489716770437433,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5461676588727769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.439390194918321,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.506281776837426,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.011000061035154829,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.033041229248048865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.012905616760249927,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7995534097597679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.671754768077093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7800539379969385,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.009285790579659614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.033142495770156044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7013545927455516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.005496225908592223,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.09000015258789062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3738773735586953,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.28492410738854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6831015392204653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.6449870672373135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5639059187883433,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.3202238554566588,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5644546187977384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.942452543375894,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.05200004577636719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.033522262573242756,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.026653099060062857,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.07315555252167538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.24291385182366731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.12455434311176017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03571428571428581,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.07208051531144077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.168463453077361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2889826565564221,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 10.34002685546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.2754269774495017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.676933314580468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.6240909645795067,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.516311436197629,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.0853984322198538,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.07178535173527,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.3765348065613043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.218845960059048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.2354980468750227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.32459960937501364,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8955500793456395,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.088183444778979,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8434321172617674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8260014671970026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.0592825753348194,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.06798722538589708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.631176282888834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.024954780912091024,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8806324385583819,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.736162654792064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4974325395253443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.9443182783052997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.690603893328734,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.131014691946865,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7501236184928595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6468528021667179,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.03600006103515341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0980000305175821,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.026047134399419747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.712692585697484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.68813939325263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9838765349605705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0378570556640625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.010968796482083487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.6774646492977214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.7044505235858982,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.029998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8056421222427224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4813441397245599,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.1911246533984787,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.3133846268216693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9956706674723703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.1238038231206393,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.438680811416683,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.0159191506830876,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.8185005187988281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4271679687499841,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.36575908660890377,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9946682461210443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.7860691108571016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8800655880461221,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.1771425519670755,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.07661184198252702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5140227339046399,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.0021132073493427272,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 8.689971923828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.317497133373958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.365978217638345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.048580000917122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 6.191088296615832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.12746858814431,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.760830254793145,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.801023842898918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 5.893622820477251,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.10400085449219887,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4344000244140602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4094999694824537,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.2761001863532138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.256747646868939,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.1008270997889267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1799992152622778,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.009607220389014515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9904650215544653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.31819428868868616,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.3600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6003025038834431,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.2950134889285305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.13226132694784676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.5167009994611291,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4102739586537951,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.9001614517737297,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.3798174849660505,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8141664755997091,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.4065002441406307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.9163665771484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.10061241149901434,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.020833545535181575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.22398421613720743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.11751365408826331,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.21214185442243316,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.10599843666064679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.14233391053988242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03623728121497538,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.4699993133544922,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.3960000991297683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.40760044661751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.4697096698807375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.0179062770709466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.2059715539001203,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.8024524837723104,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.2221535118625342,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7204408009323657,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.10599994659423828,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.07720001220702954,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.0044500064849799514,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.7994702078122038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.676522956428272,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.454773857530677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.016428811209542427,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.017777622528944992,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.3482481501016608,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.13845354392915,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.9636161830843157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.7758139877024117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.1416875817850225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.5553732788190278,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -2.1536447283139637,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8293339751427875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.10586857623318124,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -1.8528387549576095,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.012000274658205967,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.11510009765623863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.02600799560546818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.01734237806192418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.1550835293919861,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.03737252309818917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.08000019618443077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.11328262967010794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.12235647630604118,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 3.290008544921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.611182654051512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 6.360397329629963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8763542309572778,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.5895407966318267,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.421154108821864,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 4.7552493667847635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.6287980729390741,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.2920753204932449,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04549942016603836,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.11080017089844318,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.19029998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9986583426904847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.9368392887342822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 2.263611738866512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.019287109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.04281210853319406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 1.8811873499935627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.8320588326642853,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-20",
        "change": 0.020000000000000462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-20",
        "change": 0.040000000000000036,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-20",
        "change": 0.0,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-20",
        "change": -0.03000000000000025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-19",
        "to": "2026-10-20",
        "change": -0.029999999999999805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": 0.020000000000000018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 3,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-20",
        "to": "2026-10-21",
        "change": -0.629999999999999,
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
| 事实指标引用 | ["macro.BAMLH0A0HYM2.value", "macro.DGS10.value", "prices.^VIX.value"] |
| 推断与解释 | 推断：估值与地缘压力升温，尚不满足系统性恐慌的多指标确认。 |
| 反证与缺口 | 信用仍截至10月20日；盘前VIX不同于收盘值，当前全市场广度未取得。 |
| 确认条件 | 波动、信用和市场广度同步恶化才提高恐慌判断。 |
| 失效条件 | 地缘缓和且成长价格、现金回收持续改善。 |
| 观察期限 | 下一交易日至两周 |
| 条件式指导 | 观察多指标，不依赖单一情绪读数。 |
| 主观置信等级 | medium |
| 判断变化原因 | 完整收盘日未变；盘前弱化、META新10-Q及FRED恢复成为本次增量。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct"] |
| 推断与解释 | 盘前跌幅削弱反弹；完整收盘仍未收复QQQ/SMH20日线，今晚盘中条件尚无法判断。 |
| 反证与缺口 | 反弹低成交且盘后回吐；未核验完整VWAP。 |
| 确认条件 | 常规回踩守住并连续两次收盘收复20日线。 |
| 失效条件 | 失守前收盘反抽失败并再次相对走弱。 |
| 观察期限 | 1–5个交易日 |
| 条件式指导 | 从价格承接到收盘趋势逐级确认，不跳步。 |
| 主观置信等级 | medium |
| 判断变化原因 | 完整收盘日未变；盘前弱化、META新10-Q及FRED恢复成为本次增量。 |

## 判断依据 · 轮动是否等于资金流入？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 轮动是否等于资金流入？ |
| 事实指标引用 | ["prices.SMH.relative_spy_5d_pp", "prices.RSP.relative_spy_5d_pp", "prices.IGV.return_1d_pct"] |
| 推断与解释 | 科技一日领先与五日仍弱可并存；价量只是偏好证据。 |
| 反证与缺口 | 当期份额/申赎缺失。 |
| 确认条件 | 相对强弱延续、发行人净申赎和盈利互相支持。 |
| 失效条件 | 领涨迅速消失、财报不支持。 |
| 观察期限 | 1–2周 |
| 条件式指导 | 保留资金数据的真实窗口，不把上涨称主力净流入。 |
| 主观置信等级 | medium |
| 判断变化原因 | 完整收盘日未变；盘前弱化、META新10-Q及FRED恢复成为本次增量。 |

## 判断依据 · AI支出增长是利好吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI支出增长是利好吗？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.SMH.distance_sma20_pct", "prices.CRWV.distance_sma20_pct"] |
| 推断与解释 | META多年采购及租赁承诺增加现金回收约束；需求增长与融资压力可同时存在。 |
| 反证与缺口 | META收入+26%、H100租金未崩，不能直接宣告泡沫破裂。 |
| 确认条件 | 收入、利润和企业自由现金流可持续改善，价格承接配合。 |
| 失效条件 | 融资收紧或资本开支增速长期高于现金创造，订单开始下修。 |
| 观察期限 | 下一季度并每日观察价格风险 |
| 条件式指导 | 区分观测、管理层指引和估值假设；META暂停精确估值。 |
| 主观置信等级 | medium |
| 判断变化原因 | 完整收盘日未变；盘前弱化、META新10-Q及FRED恢复成为本次增量。 |

## AI现金回收压力重新压过需求叙事 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 10月22日META新10-Q列出4545.2亿美元不可取消采购等承诺、3557.3亿美元尚未开始的租赁、最高147.2亿美元附条件云采购。三项算术合计8249.7亿美元；覆盖不同性质及多年期限，不是今年资本开支或现有债务。108亿美元资金被转为受限现金等价物。 |
| 事实：市场反应 | SPY.US 765.81，相对10月21日常规收盘-0.94%（UTC 12:02:11）；QQQ.US 713.71，相对10月21日常规收盘-1.58%（UTC 12:02:03）；SMH.US 539.00，相对10月21日常规收盘-3.18%（UTC 12:01:58）；META.US 681.72，相对10月21日常规收盘-2.27%（UTC 12:02:09）；NVDA.US 217.11，相对10月21日常规收盘-2.19%（UTC 12:02:02） |
| 推断：解释 | 推断：收入增长并未消除投资锁定和现金回收风险，盘前转弱降低利好兑现的置信度；不能把股价变化全部归于单一披露。 |
| 受益篮子 | ["NVDA", "SMH", "云基础设施观察"] |
| 受损篮子 | ["现金回收慢且依赖融资的AI供应商"] |
| 反证 | Q3营收同比+26%、H100租金未崩，需求尚有支持；融资租赁和经营租赁不能不加区分直接从股权价值扣除。 |
| 下一催化剂 | 今晚常规交易消化META披露，随后核验云厂商财报与支出兑现。 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://www.silicondata.com/products/silicon-index/h100"] |

## 科技重新领涨，防御相对回落 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 10月21日科技领涨仍是最新完整交易日事实；22日盘前SMH明显弱于SPY，昨晚轮动尚未延续。 |
| 事实：市场反应 | 最新盘前SMH约−3.18%、QQQ−1.58%、SPY−0.94%，盘前成交量不能与全天量直接比较。 |
| 推断：解释 | 一日轮动不足以证明持续资金偏好；当前应先检查领涨者能否保住反弹结构。 |
| 受益篮子 | ["SMH", "IGV", "SKYY"] |
| 受损篮子 | ["短期防御相对表现"] |
| 反证 | 尚未常规开盘，盘前流动性较薄；完整19ETF的相对收益仍截至10月21日。 |
| 下一催化剂 | 未来1–3个常规交易日的相对强弱与盈利验证 |
| 证据 | ["https://finance.yahoo.com/quote/SMH/history/", "https://finance.yahoo.com/quote/QQQ/history/"] |

## 地缘风险在盘后重新定价 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | AP报道伊朗方面声称七艘油轮受袭或触雷，但明确未能独立确认；UKMTO未报告这批最新袭击。不能把单方说法写成七艘损毁已核实。 |
| 事实：市场反应 | 当前可得延迟分钟报价Brent112.05、WTI99.45（UTC11:53），相对本批10月21日连续收盘均上行；美伊月底停火合约却从今早68%回升至73.5%。 |
| 推断：解释 | 海运风险、美国直接打击伊朗和油价触价合约定义不同，可出现不同方向；不能相加成战争概率。 |
| 受益篮子 | ["能源与黄金观察篮子"] |
| 受损篮子 | ["航空运输", "高估值久期资产"] |
| 反证 | 未核验该批油轮损失与实际新增出口损失；连续油价存在换月和历史回写。 |
| 下一催化剂 | 官方事件核验和下一交易时段油价反应 |
| 证据 | ["https://apnews.com/article/2abebce2fca2c085e0e0ee717e42cf28", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] |

## 航天合并仍是事件预期 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Tesla/SpaceX年底正式宣布控制权交易合约16.5%，低于今早20.5%；传闻、谈判与正式公告仍需区分。 |
| 事实：市场反应 | 本次未独立采集TSLA当前分钟价，不借用昨夜数字。 |
| 推断：解释 | 委员会讨论、正式宣布与交割是不同阶段。 |
| 受益篮子 | ["TSLA事件观察"] |
| 受损篮子 | ["仅凭讨论追价"] |
| 反证 | 合约变化不是正式交易失败证据，具体公告仍未确认。 |
| 下一催化剂 | 公司正式公告，日期未定 |
| 证据 | ["https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] |

## 国防订单与工业AI兑现分开看 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | LMT官方Q3营收207亿美元、同比+11%，积压订单2920亿美元，并上调全年展望；西门子工业AI合作官方更新实际为10月19日，今天传播不构成全新事件。 |
| 事实：市场反应 | LMT本次没有可核验即时价格，先列经营证据；工业AI不能用NVDA全股涨跌单独证明兑现。 |
| 推断：解释 | 订单支持中期收入可见度，但交付、利润率与现金流仍是约束；产品合作不等于已确认收入。 |
| 受益篮子 | ["LMT", "工业自动化观察"] |
| 受损篮子 | ["仅凭消息重复传播追价"] |
| 反证 | LMT当季自由现金流30亿美元，低于去年33亿美元；不要只看积压订单增长。 |
| 下一催化剂 | LMT纽约10月22日08:30电话会 |
| 证据 | ["https://investors.lockheedmartin.com/node/53326/pdf", "https://press.siemens.com/global/en/pressrelease/siemens-partners-nvidia-advance-ai-driven-autonomous-factories"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| SPY | 765.81 | -0.94 | 2026-10-22T12:02:11+00:00 | 2026-10-22T12:02:11+00:00 | 2026-10-22T12:02:13.295497+00:00 | ok |
| QQQ | 713.71 | -1.58 | 2026-10-22T12:02:03+00:00 | 2026-10-22T12:02:03+00:00 | 2026-10-22T12:02:13.295497+00:00 | ok |
| SMH | 539.00 | -3.18 | 2026-10-22T12:01:58+00:00 | 2026-10-22T12:01:58+00:00 | 2026-10-22T12:02:13.295497+00:00 | ok |
| META | 681.72 | -2.27 | 2026-10-22T12:02:09+00:00 | 2026-10-22T12:02:09+00:00 | 2026-10-22T12:02:13.295497+00:00 | ok |
| NVDA | 217.11 | -2.19 | 2026-10-22T12:02:02+00:00 | 2026-10-22T12:02:02+00:00 | 2026-10-22T12:02:13.295497+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 773.09 | USD_per_share | 2026-10-21 | 0.53 | 0.45 | 0.69 | ok |
| QQQ | 725.20 | USD_per_share | 2026-10-21 | 1.05 | -0.51 | -2.16 | ok |
| IWM | 276.48 | USD_per_share | 2026-10-21 | 0.25 | 1.88 | -1.93 | ok |
| RSP | 216.64 | USD_per_share | 2026-10-21 | 0.36 | 2.15 | 2.52 | ok |
| GLD | 378.95 | USD_per_share | 2026-10-21 | 0.34 | 0.79 | -3.55 | ok |
| GC=F | 4,150.00 | USD_per_troy_ounce | 2026-10-21 | 0.18 | 1.02 | -3.90 | ok |
| CL=F | 97.15 | USD_per_barrel | 2026-10-21 | -4.56 | 2.17 | 5.41 | ok |
| BZ=F | 108.82 | USD_per_barrel | 2026-10-21 | 0.03 | 2.60 | 5.57 | ok |
| TLT | 80.24 | USD_per_share | 2026-10-21 | 0.14 | 1.71 | 0.13 | ok |
| UUP | 28.92 | USD_per_share | 2026-10-21 | 0.07 | -0.69 | 0.94 | ok |
| HYG | 76.98 | USD_per_share | 2026-10-21 | 0.20 | 0.22 | -1.00 | ok |
| LQD | 103.21 | USD_per_share | 2026-10-21 | -0.01 | 0.54 | -0.23 | ok |
| ^VIX | 16.68 | index | 2026-10-21 | -3.64 | -1.13 | 9.88 | ok |
| ^VIX3M | 18.72 | index | 2026-10-21 | -1.42 | -0.37 | 3.37 | ok |
| ^VVIX | 94.55 | index | 2026-10-21 | -2.68 | 0.11 | 6.72 | ok |
| ^MOVE | 95.94 | index | 2026-10-21 | -5.66 | -3.15 | 22.12 | ok |
| NVDA | 221.97 | USD_per_share | 2026-10-21 | 2.54 | 0.30 | -1.57 | ok |
| MSFT | 532.95 | USD_per_share | 2026-10-21 | 0.20 | -0.14 | 6.46 | ok |
| AMZN | 262.37 | USD_per_share | 2026-10-21 | -0.10 | 3.26 | 5.26 | ok |
| GOOGL | 334.76 | USD_per_share | 2026-10-21 | -1.62 | -3.70 | -0.91 | ok |
| META | 697.52 | USD_per_share | 2026-10-21 | 0.47 | -5.43 | -6.26 | ok |
| CRWV | 61.82 | USD_per_share | 2026-10-21 | -0.50 | -6.02 | -28.86 | ok |
| MU | 913.67 | USD_per_share | 2026-10-21 | 1.96 | -0.05 | -14.75 | ok |
| DRAM | 49.16 | USD_per_share | 2026-10-21 | 3.02 | -1.95 | -20.58 | ok |
| VRT | 212.15 | USD_per_share | 2026-10-21 | 4.22 | -4.79 | -14.72 | ok |

## 跨资产风险解释

推断：相对今早风险重新升温，但不是已证实系统性恐慌。盘前VIX分钟观测18.14（UTC11:48:31），高于10月21日官方收盘16.68；当前VIX3M未另查，不拿不同日读数拼期限曲线。上日同日VIX16.68/VIX3M18.72仍作为历史关系。盘前GLD372.26（UTC12:03），低于昨收378.95；黄金并未与风险同向上涨，不能认定统一避险周期。FRED恢复：2年4.79%、10年5.12%、实际10年2.77%、HY333bp、IG87bp，均截至10月20日，不能冒充今晚；10年盈亏平衡2.37%截至21日，金融压力−0.7206截至9日，GPR248.66截至19日。最新完整MOVE95.94。油价原始历史修订：本次10月21日CL=F97.15/Brent108.82，不同于今早97.87/110.05；当日未完成期货、结算和换月会改变数值，不将快照差当收益。UTC11:53可得连续报价99.45/112.05仅作风险代理，不裁决ICE/Pyth触价合约。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.79 | percent | 2026-10-20 | 0.03 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.33 | percentage_points | 2026-10-20 | 0.65 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.87 | percentage_points | 2026-10-20 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.12 | percent | 2026-10-20 | 0.16 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.77 | percent | 2026-10-20 | 0.15 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.37 | percent | 2026-10-21 | 0.04 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.72 | index | 2026-10-09 | 0.04 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 16.68 | index | 2026-10-21 | 1.50 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLK | 科技 | 1.67 | -0.99 | -3.48 | 1.15 | -1.45 | -4.17 | 1.16 | 2026-10-21 |
| XLE | 能源 | 0.28 | 0.78 | 9.28 | -0.25 | 0.33 | 8.60 | 0.82 | 2026-10-21 |
| XLF | 金融 | 0.57 | 2.79 | 2.75 | 0.05 | 2.33 | 2.06 | 0.77 | 2026-10-21 |
| XLI | 工业 | 0.91 | 0.76 | -1.05 | 0.38 | 0.31 | -1.74 | 0.99 | 2026-10-21 |
| XLV | 医疗 | -0.49 | 2.86 | 6.01 | -1.01 | 2.41 | 5.32 | 1.00 | 2026-10-21 |
| XLP | 必需消费 | -0.73 | 1.22 | 5.68 | -1.25 | 0.77 | 4.99 | 1.05 | 2026-10-21 |
| XLY | 可选消费 | 0.03 | 3.61 | 4.41 | -0.50 | 3.16 | 3.72 | 0.92 | 2026-10-21 |
| XLC | 通信 | -1.11 | -1.67 | -3.19 | -1.63 | -2.12 | -3.88 | 1.48 | 2026-10-21 |
| XLU | 公用事业 | 0.29 | 0.67 | 5.66 | -0.24 | 0.22 | 4.97 | 1.14 | 2026-10-21 |
| XLRE | 房地产 | -0.76 | 1.37 | 0.53 | -1.28 | 0.92 | -0.16 | 0.86 | 2026-10-21 |
| XLB | 材料 | 0.18 | 3.32 | 2.07 | -0.35 | 2.87 | 1.38 | 0.68 | 2026-10-21 |
| SMH | 半导体 | 1.89 | -1.42 | -7.43 | 1.37 | -1.88 | -8.12 | 1.01 | 2026-10-21 |
| IGV | 软件 | 1.77 | 1.09 | 0.67 | 1.24 | 0.63 | -0.02 | 1.26 | 2026-10-21 |
| XOP | 油气开采 | -0.51 | 0.60 | 8.96 | -1.04 | 0.14 | 8.27 | 0.72 | 2026-10-21 |
| OIH | 油服 | 2.26 | 2.93 | -0.53 | 1.73 | 2.48 | -1.21 | 0.92 | 2026-10-21 |
| ITA | 航空与国防 | -0.17 | 0.76 | -3.80 | -0.70 | 0.31 | -4.49 | 1.27 | 2026-10-21 |
| ARKX | 航天主题 | 1.56 | 0.08 | -6.49 | 1.04 | -0.37 | -7.18 | 0.66 | 2026-10-21 |
| KRE | 区域银行 | 0.00 | 3.03 | 0.34 | -0.53 | 2.58 | -0.35 | 0.96 | 2026-10-21 |
| SKYY | 云计算 | 2.01 | 1.59 | -0.54 | 1.49 | 1.14 | -1.23 | 0.54 | 2026-10-21 |

## 资金证据分层

19ETF完整收盘窗口未变，继续按相同端点展示1/5/20/60日相对SPY强弱。盘前科技更弱是新观察，与昨日科技轮动分开。发行人SPY/SMH补查仍未取得当期连续份额及拆分信息；ETF Action10月21日报告可读，但其1 Day数据在页面没有足够明确的实际结算日，不冒充10月21日净申赎。保留之前公开报告明确日期的个体ETF窗口，属于历史证据；ICI本次核验仍为截至10月14日全行业ETF净发行532.62亿美元，国内股票296.70亿美元。公开资金报告不识别主力身份，涨跌/成交额不等于净流入；当前机构交易与最新13F穿透仍缺。

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

2026-10-22T12:06:20.342325+00:00本次采集1495个候选，覆盖25主题与跟踪ID；额外搜索META价格/财报、芯片出口、政府停摆、美国伊朗及近期Fed催化剂。剔除过期2025合约和混合选举/历史截止合约，平台AI摘要不作新闻证据。九个已核验重点合约规则hash不变。部分查询两页截断，未核验到可直接表示META现金回收的近期合约。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.35, {"status": "comparable", "change_pp": -0.050000000000000044}] | {"spread": 0.009000000000000008, "volume24h_usd": 3115.781909, "liquidity_usd": 43710.75164, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["AI bubble burst in 2026?；按本次专门规则报价解释，不与不同期限相加。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [41.0, {"status": "comparable", "change_pp": 4.999999999999999}] | {"spread": 0.019999999999999962, "volume24h_usd": 9308.605402, "liquidity_usd": 17676.1277, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?；按本次专门规则报价解释，不与不同期限相加。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by October 31?", "10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583"] | [0.8999999999999999, {"status": "comparable", "change_pp": 0.09999999999999992}] | {"spread": 0.002, "volume24h_usd": 36939.084322, "liquidity_usd": 130493.39435, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2026-11-01T03:59:00+00:00"} | ["Strait of Hormuz traffic returns to normal by October 31?；按本次专门规则报价解释，不与不同期限相加。", "航运恢复速度影响供给风险溢价"] | ["IMF同口径船舶通行7日均值回升", "只有口头提议、无实际通航"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 18127.457383, "liquidity_usd": 588479.0395, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Strait of Hormuz traffic returns to normal by December 31?；按本次专门规则报价解释，不与不同期限相加。", "能源中期风险"] | ["实际船舶数据支持改善", "封锁和袭击持续"] | [null, null] |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [73.5, {"status": "comparable", "change_pp": 5.499999999999994}] | {"spread": 0.010000000000000009, "volume24h_usd": 459240.856453, "liquidity_usd": 163289.4721, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["US x Iran ceasefire continues through October 31?；按本次专门规则报价解释，不与不同期限相加。", "定义差异解释与通航低概率并存"] | ["可信报道符合专门规则", "其他交战行动不能自动当本合约失效"] | [null, null] |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [78.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 24313.934538, "liquidity_usd": 146562.2061, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?；按本次专门规则报价解释，不与不同期限相加。", "贴现率影响长久期资产"] | ["后续通胀及官方政策支持", "通胀缓解及政策转向"] | [null, null] |
| ["Tesla and SpaceX merger officially announced by December 31?", "2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。", "https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30"] | [16.5, {"status": "comparable", "change_pp": -3.9999999999999982}] | {"spread": 0.010000000000000009, "volume24h_usd": 12979.993488999999, "liquidity_usd": 35760.1808, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Tesla and SpaceX merger officially announced by December 31?；按本次专门规则报价解释，不与不同期限相加。", "航天/汽车事件溢价与融资结构"] | ["正式公告符合控制权转移要求，并核验资产价格反应", "仅委员会讨论、少数股权投资或传闻"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [89.5, {"status": "comparable", "change_pp": 2.0000000000000018}] | {"spread": 0.010000000000000009, "volume24h_usd": 516426.805288, "liquidity_usd": 885392.1027, "quality_flags": [], "retrieved_at": "2026-10-22T12:02:27.298488+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["Will there be no change in Fed interest rates after the October 2026 meeting?；按本次专门规则报价解释，不与不同期限相加。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 89.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, 17.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000018} |
| 24h成交量 / 流动性 USD | [516426.805288, 885392.1027] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:56:57.685031Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 73.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-8.0, -6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 5.499999999999994} |
| 24h成交量 / 流动性 USD | [459240.856453, 163289.4721] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T12:00:57.925529Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.15, -0.05] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.09999999999999992} |
| 24h成交量 / 流动性 USD | [36939.084322, 130493.39435] |
| 价差 pp | 0.20 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T12:00:57.925529Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 78.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [24313.934538, 146562.2061] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:58:58.314965Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [18127.457383, 588479.0395] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:56:57.685031Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 16.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.0, -6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.9999999999999982} |
| 24h成交量 / 流动性 USD | [12979.993488999999, 35760.1808] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:56:57.685031Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 41.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, 19.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 4.999999999999999} |
| 24h成交量 / 流动性 USD | [9308.605402, 17676.1277] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:56:57.685031Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.85, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.050000000000000044} |
| 24h成交量 / 流动性 USD | [3115.781909, 43710.75164] |
| 价差 pp | 0.90 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:58:58.314965Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 20.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.5, 1.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1133.435486, 17802.5203] |
| 价差 pp | 2.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-22T11:58:58.314965Z |
| 抓取时间 | 2026-10-22T12:02:27.298488+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI 压力：合约、经营与估值分开

第一层：AI年底专门合约9.35%、2027年6月底20.0%；年底较今早9.4%微降0.05个百分点，远小于0.9个百分点价差，不构成风险显著下降信号；24h成交约3116/1133美元。规则要求90日窗口内多项触发，不是产业泡沫客观概率。第二层：H100官方带日期读数仍10月21日2.86美元/GPU小时、7日+10%，没有新增日序列；FAQ未标日期的2.53不采用。META新10-Q明确多年承诺与受限现金，强化流动性与回收检验；约8250亿美元不能全部当成当前负债，也不能忽略。其当季负FCF与强收入并存，公司FCF含租赁本金不等于FCFF。个体AI融资实时CDS仍缺。第三层：五家公司SEC检查完成，NVDA/MSFT/AMZN/GOOGL没有更新10-Q/10-K，复用核验底稿，以同一10月21日完整收盘估值，盘前价格单列未混用。META新增10月22日Q3 10-Q，原Q2底稿已停用；本次加入承诺及受限现金事实，但未核验完整融资租赁净债务/新增资产口径，因此仍暂停精确FCFF估值和反推。其余四家公司情景是公司整体假设，不是纯AI估值或客观概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-22T12:03:48.774980+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 221.97 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3013813936572717, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -55.50 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -30.57 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 9.28 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-22T12:03:51.397203+00:00", "latest_filing_date": "2026-07-29"} |
| 观测财务数据 | {"ttm_revenue_million": 331839.0, "revenue_quarters": [{"end": "2025-09-30", "value": 77673000000, "filed": "2025-10-29", "duration_days": 92}, {"end": "2025-12-31", "value": 81273000000, "filed": "2026-01-28", "duration_days": 92}, {"end": "2026-03-31", "value": 82886000000, "filed": "2026-04-29", "duration_days": 90}, {"end": "2026-06-30", "value": 90007000000, "filed": "2026-07-29", "duration_days": 91}], "cash_million": 20935.0, "liquid_investments_million": 55908.0, "debt_million": 40294.0, "finance_lease_million": 66594.0, "diluted_shares_million": 7453.0, "latest_operating_income_million": 155237.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 331839.0, "income_statement_window": "FY2026 全年"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。融资租赁66594计入债务；资本开支假设涵盖新增租赁，现金支出115948加融资租赁资产新增24608为本年经济资本开支140556。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 532.95 |
| 基期输入 USD million / million shares | {"revenue": 331839.0, "net_debt": 30045.0, "diluted_shares": 7453.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.31800818623408544, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## MSFT · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 143.02 | -73.16 | 8.00 | 42.00 | 10.50 | 76.13 |
| 基准 | 266.55 | -49.99 | 14.00 | 47.00 | 9.50 | 81.05 |
| 乐观 | 484.83 | -9.03 | 20.00 | 52.00 | 8.50 | 84.97 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-22T12:03:54.043565+00:00", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 262.37 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.40355285716263445, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.60 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -66.68 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -9.27 | 18.00 | 22.00 | 9.00 | 86.04 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-22T12:03:56.571484+00:00", "latest_filing_date": "2026-07-23"} |
| 观测财务数据 | {"ttm_revenue_million": 445867.0, "revenue_quarters": [{"end": "2025-09-30", "value": 102346000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 113829000000, "filed": "2026-02-05", "duration_days": 92}, {"end": "2026-03-31", "value": 109896000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 119796000000, "filed": "2026-07-23", "duration_days": 91}], "cash_million": 55911.0, "liquid_investments_million": 186563.0, "debt_million": 100164, "finance_lease_million": 2590.0, "diluted_shares_million": 12309.0, "latest_operating_income_million": 40770.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 119796.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。优先股按完全转换处理：季度稀释股数12309减已计入的16，再加合同最大转换股数54.45825；不再扣19000优先股本金。未来3年优先股息按年1203.125、10%折现约2991.99计入权益桥调整，此为保守假设；capped call 未赋值。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | {"preferred_coupon_pv_million": 2991.9938016528904, "discount_rate": 0.1, "years": 3} |
| 价格 USD | 334.76 |
| 基期输入 USD million / million shares | {"revenue": 445867.0, "net_debt": -136728.0061983471, "diluted_shares": 12347.45825, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.38776222326163146, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## GOOGL · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 66.88 | -80.02 | 7.00 | 31.00 | 11.00 | 79.41 |
| 基准 | 131.94 | -60.59 | 13.00 | 36.00 | 10.00 | 82.80 |
| 乐观 | 250.29 | -25.23 | 19.00 | 41.00 | 9.00 | 85.75 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-22T12:03:58.920455+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 10月22日新10-Q已核验；多年承诺与受限资金已记录，但完整融资租赁负债及资产新增口径未齐，不将不同承诺简单当现有债务，暂停精确FCFF反推。 |

## 科技反弹延续

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | META现金回收/承诺披露、能源风险及常规开盘承接 |
| 关联标的 | ["QQQ", "SMH", "NVDA", "META"] |
| 确认条件 | 下一常规开盘30分钟后守住开盘区间低点和常规VWAP、回踩量能收敛；随后QQQ/SMH连续两次收盘站上各自当时20日线。当前参考20日线QQQ739.07、SMH593.37，随时间更新。 |
| 失效条件 | 跌破10月21日收盘后反抽失败且相对SPY转弱；或指引/现金回收恶化。单次跌破不等于必跌。 |
| 观察期限 | 下一交易日至5个交易日 |
| 反证 | 盘前半导体弱于大盘，尚无连续收盘趋势确认；高需求表态不等于现金回报。 |
| 状态 | 盘前明显受挫；今晚常规确认尚未开始 |

## 地缘与通胀再次压制估值

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 官方确认新增袭击、供应损失或利率压力 |
| 关联标的 | ["XLE", "GLD", "QQQ", "TLT"] |
| 确认条件 | 已核验供应受损，同时同交割原油持续走高、VIX回升与成长相对弱势相互印证。VIX25与HY400bp仅作研究压力阈值，非自然分界，HY当前缺失。 |
| 失效条件 | 供应和通航改善获得官方核验且油价风险溢价回落，科技稳住结构。 |
| 观察期限 | 未来1–10个交易日 |
| 反证 | 常规VIX下降；机场遇袭不等于油田停产或美国打击伊朗。 |
| 状态 | 风险升温但供应损失仍需独立核验 |

## 跨期比较与上期剧本复核

相对10月22日07:15时段：完整美股收盘日未变；盘前SPY/QQQ/SMH跌幅扩大、META转为低于昨收，反弹置信度下调，尚未常规开盘不能声称今晚VWAP条件失败。旧要求连续两次收盘站稳20日线仍未通过。九合约rule_hash一致：Fed10月不变87.5%→89.5%（+2个百分点），12月加25bp78.5%不变；美伊月底停火68%→73.5%（+5.5），WTI触105 36%→41%（+5），年底AI9.4%→9.35%（−0.05，小于价差），合并公告20.5%→16.5%（−4）。不同合约方向不一源于各自事件定义与交易信息，不能简单合成市场情绪。FRED从失败恢复是证据覆盖改善，并非市场风险本身改善。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-21/20261021T232422.143072Z/evidence.json",
    "baseline_cutoff": "2026-10-21T23:24:20.052987+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.14720668452439245,
      "CL=F": -0.735670992640558,
      "BZ=F": -1.1176768040207175,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": 0.0013598542554227322,
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
        "change_pct": -0.5595621461590428,
        "from_observed_at": "2026-10-21T23:18:36+00:00",
        "to_observed_at": "2026-10-22T12:02:11+00:00"
      },
      "QQQ": {
        "change_pct": -0.9561476547321646,
        "from_observed_at": "2026-10-21T23:20:18+00:00",
        "to_observed_at": "2026-10-22T12:02:03+00:00"
      },
      "SMH": {
        "change_pct": -2.0000000000000018,
        "from_observed_at": "2026-10-21T23:11:26+00:00",
        "to_observed_at": "2026-10-22T12:01:58+00:00"
      },
      "META": {
        "change_pct": -4.333440920572551,
        "from_observed_at": "2026-10-21T23:20:32+00:00",
        "to_observed_at": "2026-10-22T12:02:09+00:00"
      }
    },
    "macro_change": {
      "CBOE_VIX": {
        "change": -0.629999999999999,
        "unit": "index",
        "observation_date": "2026-10-21"
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
        "change_pp": 2.0000000000000018
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 5.499999999999994
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.09999999999999992
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": -3.9999999999999982
      },
      "4951227": {
        "status": "comparable",
        "change_pp": 4.999999999999999
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.050000000000000044
      },
      "4838928": {
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
    "event": "LMT Q3电话会",
    "date": "2026-10-22T08:30:00-04:00",
    "source": "https://investors.lockheedmartin.com/news-releases/news-release-details/lockheed-martin-announces-third-quarter-2026-earnings-results"
  },
  {
    "event": "常规开盘，验证盘前跌幅承接",
    "date": "2026-10-22T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
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
| meta-q3-10q | Q3正式10-Q新增多年采购/未开始租赁及附条件云采购、受限现金信息；不全等于当期债务。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "published_at": null, "retrieved_at": "2026-10-22T12:06:20.342325+00:00"}] |
| iran-tankers-claim | 伊方声称七艘油轮受损；AP明确未独立确认。 | 缺失 | [{"source": "https://apnews.com/article/2abebce2fca2c085e0e0ee717e42cf28", "published_at": "2026-10-22T08:52:03+00:00", "retrieved_at": "2026-10-22T12:06:20.342325+00:00"}] |
| lmt-q3-results | 官方营收与订单增长，上调全年展望；FCF同比下降。 | 缺失 | [{"source": "https://investors.lockheedmartin.com/node/53326/pdf", "published_at": null, "retrieved_at": "2026-10-22T12:06:20.342325+00:00"}] |
| siemens-industrial-ai | 官方实际发表于10月19日，今天重复传播不当成新事件。 | 缺失 | [{"source": "https://press.siemens.com/global/en/pressrelease/siemens-partners-nvidia-advance-ai-driven-autonomous-factories", "published_at": null, "retrieved_at": "2026-10-22T12:06:20.342325+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN接口418、网页robots限制；真实成分广度和当前VIX期货曲线缺失。",
  "FRED恢复但收益率/信用截至10月20日，金融压力截至9日；不可当实时。",
  "tc行情ts仍为请求时间，已排除其成交资格；当前价用Yahoo实际分钟时间。",
  "当前VIX和原油分钟观测约滞后10–15分钟，外部指标标lagged；不是实时可执行报价。",
  "tc全市场及主题筛选均50条且has_more；全市场最早仅10:51UTC，主题最早03:31UTC；更早新闻可能遗漏。来源实际包含cls/financialjuice，旧工具描述未同步，逐条按真实URL核验。",
  "Polymarket部分主题查询两页截断；单方油轮消息未独立确认，不能当作既成事实。",
  "ETF当前发行人净申赎及拆分信息不足，ETF Action未明确实际日界；保留较早明确窗口。",
  "连续期货上日历史相较今早回写，完整换月桥未取得；不用跨快照差值当涨跌。",
  "META新10-Q已取得，融资租赁净债务和新增资产未齐，仍暂停精确估值；不是没有新财报。",
  "尚未今晚常规开盘，没有当日VWAP、开盘区间或回踩结论；DRAM长历史不足。",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "本次Requests取得最新Q3 10-Q原文，正文保留results，仅精简事实入库"
  },
  {
    "url": "https://apnews.com/article/2abebce2fca2c085e0e0ee717e42cf28",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "伊方宣称与AP未独立核验并列"
  },
  {
    "url": "https://press.siemens.com/global/en/pressrelease/siemens-partners-nvidia-advance-ai-driven-autonomous-factories",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "10月19日官方发布，避免新闻重复"
  },
  {
    "url": "https://investors.lockheedmartin.com/node/53326/pdf",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "官方Q3结果及现金流"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "仍10月21日带日期主读数2.86"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "数据窗口仍截至10月14日"
  },
  {
    "url": "https://www.etfaction.com/tech-sector-and-value-lead-as-growth-lags/",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "报告可读，但1 Day实际日界不明确，不新增精确流量"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "未取得连续份额与拆分"
  },
  {
    "url": "https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "单点份额不足计算流量"
  },
  {
    "url": "https://www.cnn.com/markets/fear-and-greed",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "接口418，网页robots限制"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "当前分钟成交时点及前收盘分母核验"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "当前分钟成交时点及前收盘分母核验"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "当前分钟成交时点及前收盘分母核验"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "当前分钟成交时点及前收盘分母核验"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-22T12:06:20.342325+00:00",
    "note": "当前分钟成交时点及前收盘分母核验"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001045810.json",
    "checked_at": "2026-10-22T12:03:48.774980+00:00",
    "note": "最新披露列表；META本次新增10月22日10-Q"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0000789019.json",
    "checked_at": "2026-10-22T12:03:51.397203+00:00",
    "note": "最新披露列表；META本次新增10月22日10-Q"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001018724.json",
    "checked_at": "2026-10-22T12:03:54.043565+00:00",
    "note": "最新披露列表；META本次新增10月22日10-Q"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001652044.json",
    "checked_at": "2026-10-22T12:03:56.571484+00:00",
    "note": "最新披露列表；META本次新增10月22日10-Q"
  },
  {
    "url": "https://data.sec.gov/submissions/CIK0001326801.json",
    "checked_at": "2026-10-22T12:03:58.920455+00:00",
    "note": "最新披露列表；META本次新增10月22日10-Q"
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
