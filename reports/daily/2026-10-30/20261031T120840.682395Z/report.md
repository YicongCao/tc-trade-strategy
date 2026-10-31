# 每日交易总结 · 2026-10-30

## 一分钟读懂 · Agent 摘要

### 当前判断

仍是风险厌恶阶段，反弹可靠性尚未改善。今天休市，不能用刷新后的页面价格宣称出现新反弹。

### 与上次相比

相对今早，苹果正式确认中国AI功能测试时间；中国制造业PMI降至49.3，伊朗扩大报复范围的威胁增加尾部风险。前者是应用需求线索，后两者分别影响增长与供应。

### 最重要的信号

- 周五QQQ收690.49、跌3.47%，SMH收522.49、跌6.98%；能源和防御板块相对抗跌。
- VIX19.42仍低于3个月20.78；信用只到29日，尚不能确认系统性流动性危机。
- 苹果11月4日测试、12月正式推出部分中国AI功能；不包含全部新一代Siri，收入效果尚未兑现。

### 接下来观察

- 周一先守QQQ683.45、SMH511.63，再看更高低点、当日VWAP及698.63/535.32的夺回。
- 能源和医疗优先看回踩；AAPL/BABA列新增观察，不能只凭公告追涨。
- 11月2日北京时间22:30恢复常规交易，随后PLTR、AMD财报检验AI兑现。

### 不要忽略

周末消息没有新成交验证；广度、当期ETF申赎、CNN及四家新财报估值桥仍缺。油价源更新不能当周末涨幅。

## 研究结论

10月31日晚报：周末没有新价格确认；苹果中国AI落地提供需求线索，PMI收缩与伊朗威胁强化谨慎。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-30 → 2026-10-30（纽约交易日） |
| 截止·纽约 | 2026-10-31T08:08:30.089418-04:00 |
| 截止·北京 | 2026-10-31T20:08:30.089418+08:00 |
| 实际生成时间 | 2026-10-31T12:08:30.341098+00:00 |
| 市场阶段 | 休市 |
| 下一交易日 | 2026-11-02 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-30/20261030T232258.406851Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-31T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-31T12:02:38.503551+00:00 / 2026-10-31T12:02:38.503551+00:00 | Gamma current quote snapshot; not last trade time; same rule hash for comparison |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-10-31T12:02:41.304759+00:00 / 2026-10-31T12:02:41.304759+00:00 | Gamma current quote snapshot; not last trade time; same rule hash for comparison |
| 1262633 | 已校验接入 | https://gamma-api.polymarket.com/events/1262633 | 2026-10-31T12:02:38.487182+00:00 / 2026-10-31T12:02:38.487182+00:00 | Gamma current quote snapshot; not last trade time; same rule hash for comparison |
| 1262630 | 已校验接入 | https://gamma-api.polymarket.com/events/1262630 | 2026-10-31T12:02:38.487507+00:00 / 2026-10-31T12:02:38.487507+00:00 | Gamma current quote snapshot; not last trade time; same rule hash for comparison |
| 1038648 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-10-31T12:02:41.445709+00:00 / 2026-10-31T12:02:41.445709+00:00 | Current Gamma snapshot; new expiry separate baseline |

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
| prices.SPY.value | 755.72 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -1.77 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.56 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -1.81 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -1.43 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.47 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.77 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 725.98 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -1.91 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -1.44 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 4.10 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 8.30 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.10 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -3.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 2.06 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 690.49 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -3.47 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -1.97 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -7.88 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -3.28 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -1.70 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -1.42 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -6.07 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -1.85 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 728.19 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 724.70 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 678.38 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -5.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -4.72 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 1.79 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 14.38 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.08 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -9.11 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 2.32 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 279.33 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -1.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 1.30 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -0.78 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -6.10 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.13 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.86 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 1.03 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.67 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.41 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 284.03 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.70 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 0.69 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -1.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 0.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 4.02 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.44 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -8.20 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.97 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 218.31 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.79 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.82 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 4.09 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 0.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 0.99 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 1.38 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 5.90 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 1.68 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 214.89 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.72 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.52 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.67 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.18 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.63 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.20 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 355.78 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | -3.47 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -2.95 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -6.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -8.70 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -1.70 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -2.39 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -4.60 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -7.27 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 375.76 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 390.57 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 412.92 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -5.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -8.91 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -13.84 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.87 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -16.89 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 2.03 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 3,898.90 | USD_per_troy_ounce | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -3.29 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -2.72 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -6.33 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -9.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -1.51 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -2.16 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -4.52 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -7.89 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,115.04 | USD_per_troy_ounce | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,294.80 | USD_per_troy_ounce | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,519.32 | USD_per_troy_ounce | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -5.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -9.22 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -13.73 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 74.95 | USD_per_troy_ounce | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.92 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -17.01 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 104.12 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 2.08 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 0.82 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 14.28 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 34.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 3.85 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 1.38 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 16.09 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 36.14 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 97.44 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 94.63 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 86.34 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 6.86 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 10.03 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 20.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.26 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.09 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -1.62 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.98 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 117.64 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 2.40 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 0.79 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 15.05 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 42.61 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 4.18 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 1.35 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 16.86 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 44.04 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 108.94 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 103.27 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 92.46 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 7.98 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 13.92 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 27.24 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.70 | USD_per_barrel | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.14 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.19 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.84 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.43 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.61 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 5.63 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 2.20 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.17 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 7.44 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 1.38 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 79.66 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.27 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.23 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 2.73 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.95 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.67 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.85 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.04 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.00 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.14 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.14 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 0.38 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 2.87 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 1.64 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.70 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 2.19 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 4.30 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.59 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.93 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | -0.01 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.45 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.11 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.39 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.45 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.05 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.43 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.19 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.49 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.68 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.58 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 1.58 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 1.05 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 2.48 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -0.16 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.16 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.81 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.35 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.49 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.31 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.40 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.15 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 1.17 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.27 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.05 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.40 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.40 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.13 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 1.82 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.96 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 4.20 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 0.30 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.20 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.77 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.85 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.48 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.49 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.64 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.61 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 19.42 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 12.91 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -0.15 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 26.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 30.34 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 14.68 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 0.40 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 28.65 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 32.36 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 17.00 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.18 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.26 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 14.23 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 20.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 6.36 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.48 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 12.78 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -2.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-30 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 20.78 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 7.28 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 1.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 15.38 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 11.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 9.05 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 2.02 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 17.19 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 12.61 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.98 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.58 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.51 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 9.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 11.87 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 1.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.38 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 6.64 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-30 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 106.43 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 8.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -2.98 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 22.31 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 19.96 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 10.36 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -2.42 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 24.11 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 21.39 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 95.51 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 91.60 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.81 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 11.43 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 16.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 7.72 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 11.36 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 10.68 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -3.17 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-30 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 100.20 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 7.12 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -3.01 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -7.33 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 36.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 8.89 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -2.45 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -6.25 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 37.76 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 101.45 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 90.35 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 77.54 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -1.23 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 10.90 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 29.22 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.09 | index | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.08 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -11.80 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-30 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 204.64 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -4.22 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -3.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -12.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -6.45 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -2.45 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -2.44 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -10.72 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -5.02 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 221.46 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 221.68 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.09 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -7.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -7.69 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 0.27 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.54 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 3.20 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -14.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.69 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 521.91 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -1.55 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -0.50 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 0.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 4.61 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.22 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 0.06 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 2.65 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 6.03 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 530.98 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 512.91 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 436.85 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -1.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 1.75 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 19.47 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.74 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -3.96 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.69 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 240.35 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -1.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -3.08 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -4.44 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -11.72 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 0.36 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -2.53 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | -2.63 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -10.29 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.39 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.28 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.40 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -5.52 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -5.48 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | -1.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 7.71 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.21 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -13.57 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 2.75 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 279.84 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -1.40 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -12.61 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -18.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -21.73 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.37 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -12.05 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -16.72 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -20.30 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 333.91 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 339.03 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.34 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -16.19 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -17.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -17.78 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 10.84 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.87 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -25.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 2.12 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 614.99 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -1.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -4.30 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -15.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 4.34 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 0.25 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -3.74 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -13.72 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 5.76 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 691.11 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 669.79 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.28 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -11.01 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -8.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -2.58 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 25.05 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 4.07 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -20.91 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.12 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 54.87 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -9.66 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | 1.17 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -38.77 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -35.70 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -7.89 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | 1.73 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -36.97 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -34.27 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 68.77 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 79.45 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 91.35 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -20.21 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -30.94 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -39.93 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.82 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 12.42 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -49.07 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 884.74 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -5.30 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | 0.82 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -17.68 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 0.39 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -3.53 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 1.38 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -15.87 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 1.81 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 950.55 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 978.59 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 746.62 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -6.92 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -9.59 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 18.50 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 50.99 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.76 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -19.37 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.19 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 48.01 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -7.23 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 2.02 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -22.29 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -6.67 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -5.45 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 2.58 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -20.48 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -5.24 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 51.97 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 55.97 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-30 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -7.63 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -14.22 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-30 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.95 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 6.15 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -24.54 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.40 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 232.50 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -5.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 19.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -7.80 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -15.49 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -3.68 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 20.21 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -6.00 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -14.06 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 225.09 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 242.59 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 270.44 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | 3.29 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -4.16 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -14.03 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 15.06 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 6.48 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -20.86 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 179.51 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -4.89 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -2.03 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -10.16 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -3.03 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -3.12 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -1.47 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -8.35 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -1.60 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 190.86 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.60 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.24 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -5.95 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -5.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 6.07 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.87 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -11.13 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 2.21 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 70.02 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 1.91 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 1.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 11.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 21.11 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 3.68 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 1.55 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 13.27 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 22.53 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 67.12 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.78 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.15 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 4.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 8.09 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 20.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.43 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.01 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 56.51 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -0.76 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 1.09 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 5.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -1.90 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 1.02 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 1.65 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 7.45 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -0.48 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 55.33 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.87 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.41 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.13 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 1.15 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 5.81 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.75 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.33 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -3.16 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.15 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 167.40 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -1.60 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 1.69 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -1.50 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -9.15 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.17 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 2.25 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 0.31 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -7.73 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.09 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 170.51 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.58 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -0.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -1.82 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -3.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.75 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.64 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -10.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.45 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 184.87 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 0.45 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 3.12 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 11.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 12.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 2.22 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 3.68 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 13.06 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 14.27 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 175.69 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 171.96 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.67 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 5.22 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 7.51 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 17.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.35 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.81 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | 0.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 2.13 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 89.42 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 1.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 1.31 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 11.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 5.76 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 3.18 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 1.87 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 12.85 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 7.18 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 86.01 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.39 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.58 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 3.96 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 5.97 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 6.99 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.47 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.64 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -0.63 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.96 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 115.38 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 2.02 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 4.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -2.09 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 1.07 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 2.58 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 6.66 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -0.66 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 113.51 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.14 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.16 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 1.64 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 1.98 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 0.19 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.74 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.51 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 1.43 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 99.90 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -1.29 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -5.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -9.45 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -9.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.48 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -4.76 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -7.64 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -8.42 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 108.41 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 110.56 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.35 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -7.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -9.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -11.08 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.89 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.90 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -12.94 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.22 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.43 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.67 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 2.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 9.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 0.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 2.45 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 2.60 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 10.85 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 2.28 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 41.95 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.63 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.80 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 3.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.33 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.63 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.45 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -1.27 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.01 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 43.17 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 0.26 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 5.78 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -2.85 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 2.03 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 1.97 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 7.59 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -1.42 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.95 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.50 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.77 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 2.91 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 1.57 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 0.94 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.65 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.50 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -4.03 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.11 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.74 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.40 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 2.79 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 7.94 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 1.56 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 2.17 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 3.35 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 9.75 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 2.98 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 50.70 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.90 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.72 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 4.02 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 3.62 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 3.97 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.67 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.27 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -1.28 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 522.49 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -6.98 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -0.89 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -17.14 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -8.57 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -5.20 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -0.33 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -15.34 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -7.15 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 569.90 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 572.62 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 519.50 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -8.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -8.75 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 0.58 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 21.01 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 4.02 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -17.58 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.99 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 104.29 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -3.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -5.70 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -3.82 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 4.90 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -1.64 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -5.14 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -2.01 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 6.32 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 109.26 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.99 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.95 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -4.55 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -2.53 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 11.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.18 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.05 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -7.44 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.86 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 203.76 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 2.13 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 1.03 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 10.18 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 22.46 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 3.90 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 1.59 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 11.99 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 23.89 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 197.10 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.38 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 169.57 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 3.38 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 6.47 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 20.17 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.93 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.42 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -0.54 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.69 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 411.57 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 0.90 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 3.58 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | 7.54 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 4.97 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 2.67 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 4.14 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 9.35 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 6.40 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 392.05 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 401.16 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 397.64 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 4.98 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | 2.60 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | 3.50 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.68 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.84 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -5.73 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 209.74 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -2.13 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 3.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 0.94 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -16.00 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -0.35 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 4.27 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 2.75 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -14.58 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.61 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 214.63 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.59 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 1.51 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -2.28 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -8.25 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.77 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.27 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -17.07 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.47 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.79 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -3.87 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -0.17 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -8.84 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -9.75 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -2.10 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 0.39 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -7.03 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -8.33 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 30.99 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.76 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.48 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -3.88 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -6.20 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -8.29 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.83 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.80 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -14.54 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.95 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.01 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -1.17 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | -0.62 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 1.74 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -5.32 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 0.61 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | -0.06 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 3.55 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -3.89 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.62 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.80 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.35 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 1.97 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.29 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 2.37 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.33 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.84 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -7.07 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.21 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 159.77 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -4.57 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -4.54 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -4.98 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 6.10 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -2.80 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -3.98 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -3.17 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 7.52 | pp | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 167.67 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.80 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 136.51 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -4.71 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -3.05 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 17.04 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.45 | USD_per_share | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.41 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -8.65 | percent | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-30 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.61 | percent | 2026-10-29 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.26 | percentage_points | 2026-10-29 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.89 | percentage_points | 2026-10-29 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.98 | percent | 2026-10-29 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.63 | percent | 2026-10-29 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.34 | percent | 2026-10-30 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.58 | index | 2026-10-23 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.42 | index | 2026-10-30 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 165.25 | index | 2026-10-26 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 149.77 | index | 2026-10-26 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 187.38 | index | 2026-10-26 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 181.42 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 175.44 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AAPL.value | 345.10 | USD_per_share | 2026-10-30T23:59:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| quotes.AMD.value | 508.22 | USD_per_share | 2026-10-30T23:59:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.AMZN.value | 240.80 | USD_per_share | 2026-10-30T23:59:59+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.AVGO.value | 327.13 | USD_per_share | 2026-10-30T23:59:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.BABA.value | 97.98 | USD_per_share | 2026-10-30T23:54:54+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BABA |
| quotes.CAT.value | 624.89 | USD_per_share | 2026-10-30T23:57:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.CEG.value | 262.87 | USD_per_share | 2026-10-30T23:51:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.CVX.value | 235.89 | USD_per_share | 2026-10-30T23:41:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.DRAM.value | 48.37 | USD_per_share | 2026-10-30T23:59:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GEV.value | 860.35 | USD_per_share | 2026-10-30T23:56:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 356.15 | USD_per_share | 2026-10-30T23:59:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 123.69 | USD_per_share | 2026-10-30T23:59:31+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 281.48 | USD_per_share | 2026-10-30T23:59:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 104.47 | USD_per_share | 2026-10-30T23:27:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.ILMN.value | 238.86 | USD_per_share | 2026-10-30T21:29:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ILMN |
| quotes.INTC.value | 64.89 | USD_per_share | 2026-10-30T23:59:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.IWM.value | 279.82 | USD_per_share | 2026-10-30T23:57:11+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.LLY.value | 1,414.51 | USD_per_share | 2026-10-30T23:59:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| quotes.META.value | 614.00 | USD_per_share | 2026-10-30T23:59:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MSFT.value | 522.99 | USD_per_share | 2026-10-30T23:59:12+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 889.20 | USD_per_share | 2026-10-30T23:59:54+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 105.34 | USD_per_share | 2026-10-30T23:59:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 205.25 | USD_per_share | 2026-10-30T23:59:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.NXPI.value | 259.09 | USD_per_share | 2026-10-30T21:07:33+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.ORCL.value | 130.98 | USD_per_share | 2026-10-30T23:59:47+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.PLTR.value | 184.78 | USD_per_share | 2026-10-30T23:57:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.QQQ.value | 692.74 | USD_per_share | 2026-10-30T23:59:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 218.45 | USD_per_share | 2026-10-30T23:55:47+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 526.71 | USD_per_share | 2026-10-30T23:59:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 1,157.58 | USD_per_share | 2026-10-30T23:59:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 757.12 | USD_per_share | 2026-10-30T23:59:59+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 649.18 | USD_per_share | 2026-10-30T23:59:02+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TLT.value | 81.65 | USD_per_share | 2026-10-30T23:59:30+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 232.97 | USD_per_share | 2026-10-30T23:59:27+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 70.02 | USD_per_share | 2026-10-30T23:55:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 56.58 | USD_per_share | 2026-10-30T22:38:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.XLI.value | 167.77 | USD_per_share | 2026-10-30T23:15:11+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLI |
| quotes.XLV.value | 185.00 | USD_per_share | 2026-10-30T23:58:10+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.XOM.value | 187.02 | USD_per_share | 2026-10-30T23:47:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| latest.BZ_F.value | 113.43 | USD/barrel | 2026-10-30T20:59:00+00:00 | ok | 30日最后可得分钟报价；期货已结束当日交易且具体交割月未对齐，不能由抓取时间认定实时成交 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| latest.CL_F.value | 104.12 | USD/barrel | 2026-10-30T20:59:00+00:00 | ok | 30日最后可得分钟报价；期货已结束当日交易且具体交割月未对齐，不能由抓取时间认定实时成交 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| latest.ES_F.value | 7,614.00 | index points | 2026-10-30T20:59:00+00:00 | ok | 30日最后可得分钟报价；期货已结束当日交易且具体交割月未对齐，不能由抓取时间认定实时成交 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| latest.NQ_F.value | 28,534.00 | index points | 2026-10-30T20:59:00+00:00 | ok | 30日最后可得分钟报价；期货已结束当日交易且具体交割月未对齐，不能由抓取时间认定实时成交 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| latest.VIX.value | 19.42 | index points | 2026-10-30T20:15:00+00:00 | ok | 30日最后可得分钟报价；期货已结束当日交易且具体交割月未对齐，不能由抓取时间认定实时成交 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -13.6400146484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.390931538170359,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.2506187408371727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2660710991523438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.12948754628129278,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.511531631248687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3333073495666805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.6188123799023568,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.14557038378407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6960021972656705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.31749572753903976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.09982055664067957,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.1233618164062591,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3535519409180097,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.981938171386787,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.680230813934569,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5922762308385066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7658209213198495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.538326561775837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9304652005241119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8719746915240689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1892830984933038,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.114288330078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.17404242010479065,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1527615065650264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7507623224867541,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5455082023259394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.008869010000916,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.242232614137471,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -24.85003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -13.9100341796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.058522375580174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.4639486289234522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.5177470462202876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.2139625131786014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.28619479450949,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.4969226628463685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.110675396482021,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.437643035885687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.667590837409815,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.2133298880862795,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.2516759470679437,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.0844749668973086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7746631632608034,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.163615313279688,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4918630165796642,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.2920726521016177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.954501342773483,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.0475036621094205,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.39399902343757276,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7363378906250091,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.36521942138676877,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.277005920410147,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.015623052771632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.9830016822856891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.37535677051799,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8207510417768025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.7199707115526115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.400198692062583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.8192836216517865,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.318572998046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3266489815406761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.37026887529385966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.271205210171823,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8310868903765432,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2867470467034114,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.5001726794167456,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.680023193359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.579986572265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.614811402083461,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.3153064601690523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.35470607650916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6651934666092707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.5663305341105946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4279880921654997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0891583210028593,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5897204784861332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.223879863913102,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.06468771933187956,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.08863497735681625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5357059203279779,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.054798902861907806,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.7612954417321802,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5296540588994976,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.5558499052979364,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.10950012207030113,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.21699981689454262,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3512921142578307,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.0607952880859557,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.08956565856937004,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5302503967285475,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.6466523097475427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2126915898057145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5242047577097018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.9597617350959107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7182941410575525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0991998043212048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4107142857142856,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3342851911272322,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1683486829124774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.10252682133146784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5379875554938582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.1764845107589004,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.09923066178074091,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1591215868248309,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7299957275390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.7700042724609375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9866054218425688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.016349864149955984,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.01661413184324001,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3269741860209674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.191318372380068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.5188597421571304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.2656006388005894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6645954992565928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5956738836722097,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2342688766872167,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2494569673091038,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.19748663973967462,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3202132588686188,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.8521670917238113,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3532117411017675,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.480974884527477,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.42900009155275143,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.229998779296892,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.022901611328137506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.2193853759765716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.10989089965821108,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5698529815673794,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0098688901127195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.23296986433845035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7947514748179341,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9272412131386965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8943984494672597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5669381415689845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1457148960658481,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.09571511404854904,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.07407045889862462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.036042298508168535,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7795029708594359,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7975300556261389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2194565150329567,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4731138524128303,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -12.790008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.829986572265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.147581701424861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.822470291733581,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.837560180198173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.077225008206439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.7008848593882857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4040667647405183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.2895487672406016,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.899879970006195,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.756650163254502,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.5718515508964082,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5714890810458293,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2067125544877317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.18935322813959843,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7373741143071992,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.6707363873382448,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.7543095862221243,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2180007934570654,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.3290008544922216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1896002197265716,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.9331994628906273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3508000183105082,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.288999938964821,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.086823764960744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.025366801501349,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.9881394318445063,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8370244107607139,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.021686486769015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.3464858894531417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7485722133091519,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5478559221540182,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2603977958215702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.19821335211427682,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.9878310384018114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.529956873167027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8680608166527655,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7947163525686609,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -132.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -109.0,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.7881262138632623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.9937233966820567,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.005413434099068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4228263263371121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.261411522070377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9220773565944427,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.959718394384491,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.070745558772151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.3971946756929032,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7431046558448839,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7393423349467243,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.552313872618405,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.25012010917830985,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2553847061611236,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.340906014482134,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.9251751749880803,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -13.169995117187682,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -40.224999999999454,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -13.449999999999818,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -47.06799804687489,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.6840014648441866,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -13.581003417968532,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.9073557706810638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.7059753096989816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.792082370126014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.5263200155879666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.859201858673412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.146163516120925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.764299665178569,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.057181222098208,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2309717593091627,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.12855929360166907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.8204692730369274,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.3202351000832113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06791200776646766,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.45924330517263234,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.1200027465820312,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.850006103515625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.837335396820384,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.741808596560701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7203881342540805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.011040603728941,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.4485014450978735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.5274778480084414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8888122891548988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 11.169931499321883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.228266934990743,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4911898557235288,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.4543170351017367,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8815530574476482,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.9600330763465585,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.8607851975751206,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7300000907474598,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 15.315501883105952,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.6505001068115206,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.709000396728513,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3258000183105594,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.701199951171887,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2105000114440969,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0550500297546392,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.4721951712146408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.158600449984039,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.867922900702501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.0995506856112733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.166642015339228,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4951308151199143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.1257144383021771,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.1228577750069757,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.20825865953648126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.15263246229593364,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.0032152602306175,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8031806565330757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.10308836486643713,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.09712287191855462,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.7600021362304688,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9199981689453125,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.7840579984940605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7343675963942475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7227908376838732,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.456101935584545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.7651551181275167,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.1648395814075645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9828578704092195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 11.509349615491345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.17498953666442,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5162511444429252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5432802614684706,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.326614389303252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 5.276686749376202,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.4981469309742437,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.36404549050686086,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 15.654919999275414,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7694999694824247,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.078499984741214,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.47720001220703523,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.434399871826173,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2556000137329022,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.28169996261596,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.7833133108175137,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.2710736271884358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.1562485947083534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8379798033347097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.6407571376062755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7796418173756194,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.13071441650390625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.2864287240164618,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.1892739552161231,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.27016490189575926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.5764255894805346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.1434600000349751,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7752327212434489,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.34999847412109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.18786149320542123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9188570667438167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9205515586086288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.9967806279767011,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7630120212531954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.667605109358284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.003070013684182,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5477969322660092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2030700449649379,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.1694758075809895,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.1866226577609726,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8672930816954083,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.2745436525018823,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.000912458924965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.6218823935865387,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.693367316050079,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2179996490478402,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9375579833984347,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.002866973876948009,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.008532867431640057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.017564125061028335,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0833488845825201,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.15865243018160502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.588347501657549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4323861840708654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6121046930100738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4411984107250633,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6985523704302832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.030000414167131728,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.024285997663225478,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.03233901070573686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.02345152276211704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.42261249046300353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.109454041687663,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.42964894240353846,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3452678894705006,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.04000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.04000091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06892605754548198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.34535480666929574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3463088473381726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.00018444386702398674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.10450728172184398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8072175601082643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5086317713788091,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0406430018196291,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.322005480624877,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.905263934167877,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9197622518141713,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1293031024142688,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.616038912970531,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4739102105415838,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1101806085235477,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.1049273819644405,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0055000305175774145,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.05800008773803711,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.021800003051758665,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.10180004119873232,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.008350000381469158,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0433500003814693,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.15692047717892343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0621769044029552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.21747151478170856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.22215166355274985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.17434627125600954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.017994838745893915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.00357137407575335,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.006428582327706475,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.01175528660612063,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.02274247677359509,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.13731862917873983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.13731862917873983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2655305699731938,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4068944861634348,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.15000152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.37999725341796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.18046958384745349,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.12850585644735846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.12938980121508514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2459767778020483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.20815511629481698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2761462510342048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.11625259179622871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.01991588119827359,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2104619543229056,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.1221128843898143,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1366812979372587,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.37546432408334107,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.30337651495387,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6094536006008853,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.5025597881061281,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.165486264982343,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.02599983215331747,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.12540550231933878,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.026917419433587497,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.13592483520507415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.0004658889770468022,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.000409011840815765,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.22829915328201889,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3299237609414307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.15829912638746224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6610423356556372,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.1919807546313379,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4883713457099703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.004286084856305827,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.023572104317801323,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.006293479863608398,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.02863239129498174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.18955784170353596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.48020484317826684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.23766707165041534,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.281668988155668,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.04999542236328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4199981689453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.09616417902054142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4603227029279844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4619627671253901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.030772428600323032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.24971536915334713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3418847472230544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.399217631202875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.01840631234925061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2947673591498177,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.710941443765157,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.728033866277734,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.09871511768096974,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.761247000402034,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.675192096789735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.018030011105232,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.16397669613332,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.12199974060058594,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5639614105224666,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.01785736083985512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.09848800659180768,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.014571647644032737,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0656487655639637,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.07108504611372801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.1459764618833459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.06545879522721343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4996287286873624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.06078785266380171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.45761849613515926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.00571441650390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0014288766043526469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0051889186683484745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.003855478658365441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.04718503771311555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.396388879308196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3945149874004019,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.39534405837119124,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.219999313354492,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.030000686645507812,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 11.192005188747768,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 10.699930344868271,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 9.462149248127815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.5471005751753983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 21.90314984713435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.9550788974119335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 16.804213288806615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 8.697043728645795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 12.582936726918126,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 11.950549085705441,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 10.72822034728016,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.676588121456691,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 24.41468147838304,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.621771547845249,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 19.18251518688167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 12.707482253610706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.20549998283386017,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4644999980926521,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.08579999923706083,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.24760000228882006,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.01780000209808108,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.04945000648498521,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 11.82049829582783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.3902274522571876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 13.151742002391465,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.0528796594794905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 12.066986803242418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4536131261977827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.431428568703788,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5914287567138674,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8586172139147283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.0604793477745886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 11.105549468599683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.0052993697595287,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.4099998474121094,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3000011444091797,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.498851768541858,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.490038887605997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 5.192483410023563,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.5624125792806698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 11.128457908538426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.158376751939505,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.966091852750125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.156812327039729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.889783306712217,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.74065762844317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.458554509175906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6919001255619626,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 13.639989539787113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.491684101506186,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 10.58490423265248,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 10.3023827108238,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1385000228881843,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3800000190734849,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.03440002441406165,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.08960002899169695,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0070499992370613995,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.030800008773805843,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.677595632007826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6233242116508109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.3971345410247515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0806454348375887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.8427683103795545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3126236406506342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.24714279174804688,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2885713577270508,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7922365420765249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3117088546321956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 5.512191028129765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.744188175644981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.419998168945312,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.2699966430664062,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.141831131021314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.960427693924553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.218701477927013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.7897823859211024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 15.784192088873208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.580936120554277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 11.579499826246575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.073240739272332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.532762669191673,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 8.211046434761725,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.484772577079356,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.6602948396398096,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 18.295723720121895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.247628770987596,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 13.198312206148932,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 8.218811123056401,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9705001831054716,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.634500122070307,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3313999938964969,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0253999328613332,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.007900009155278553,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.12420001983642237,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.762368207566372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.681697361950345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.803256936746727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.925397794018593,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.51374726608456,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.449219025105843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.6671425955636163,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.8664267403738837,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7837326154675583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.0196586357260653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.660811471565843,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.975158342382722,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.659996032714844,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.1100006103515625,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.188164473124449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 10.423949335059701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 9.438159455883033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.19631146728422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 7.976326515614441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.119379982165885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 15.574892993697762,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.0910391859173814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 9.579096011294808,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 11.674568075896875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 10.704230555035377,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.0668239210029276,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 9.941273917238359,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.976710904919102,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 17.151166534598804,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.934194353108495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.39650001525878054,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.7324993133544808,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5787998962402412,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.553399963378908,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.19704998016358388,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8501000022888263,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.923763388077431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.3557028274753025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 6.70366809601688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.767409659571587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 8.281661615797312,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.487634758933545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2864287240164618,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5835707528250555,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.055218155793457235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4120593794602696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 5.862672642757159,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.737676630391894,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -9.020004272460938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.32000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.423073419683087,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.6326233688413256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.679115934720356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.5154237612008403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.077915636593655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.259156363806229,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.02104482191632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -14.731717203648108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.032141881512728,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.382004628004153,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.4130448355680123,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.3859362149195475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.5663840053449682,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.925849014239548,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.4022324420139625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.586146819864037,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4654998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.0819999694824105,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.23935272216797898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7093139648437727,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.10963752746582145,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7299333190917991,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.438738033977917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.1297383586362004,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.9648960111691944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.5473852691409338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.475842129400576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.4676546108391326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5971429007393976,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5621435982840399,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4144010516387442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3622117675441072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.770274228955694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.641701713386457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9317254605001664,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9343268478517406,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -8.23004150390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.60003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.3885901015149082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.21067472785762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.234403749764602,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.36243009712373375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.535123723788879,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7694351552902878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.352537194107132,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -11.88464640013147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.002341436655450835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.9600559870204473,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.968332650612258,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.49191764340502653,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.023592092540192233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4361278057236073,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.733724814204775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.739076016347401,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.21899719238285797,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.278997802734352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8151995849608511,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.55596740722649,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3271299743652776,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4863848876953512,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.591164657969013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.2921792538587162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7691126110520372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.4234042837104166,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9748761675280022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.0050869472752346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.580004010881698,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6971435546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.14432023940698446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1440618671531846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5144063518340634,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.47843160597874634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.26049405030418926,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0479813055357081,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.4399871826171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.649993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.834835540687741,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.46048818780073386,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.4526710169850179,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.2846749582598247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.652333170716514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.772115727325231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1354156906450026,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -17.02827086085924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.2257670788581,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7901305530364389,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.813400082167326,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.155187411978532,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.14080153946782703,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.4388083777585505,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.48339668925735424,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -12.88270047707517,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5584999084472599,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.039498901367181816,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.39519958496092045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.36859954833983,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.018500061035155113,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1077000427246162,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1423117474107514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.992050882049591,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.204062286853513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.486377354045055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4209160737316262,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.188068419897361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7142835344587057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6299961635044644,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.33828446445739013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3530456837477196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5933518027910516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8889405979964575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.39620161833281387,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.045396956485872,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.980010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -40.3699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 11.238902256557083,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.16548354928346276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.14667731620816582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.623614630749486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.443589290812586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -11.63870091132555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.08813668304521372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -17.758132838402307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 12.62983379472744,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.08513519155371,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1193937829441776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.494127084468194,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.06794234043609748,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -11.305393561758871,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.5306756968571449,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -13.612562454618237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.1830001831054915,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.177999877929722,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2122235107422057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.8491094970703443,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.2767398071288767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6426576232910293,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3893344809705592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.524798396948885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8756813715493195,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.847293477439244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1016604230881377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -11.684258026670603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0642852783203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.454291207449776,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.07698090426010973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.254923425830612,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0545662020333886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.696662037638248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.309029991300508,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.38615203582953,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -9.530029296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -27.6300048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.490095104207258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5658192802613815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5498824665353785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.105065466990666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5629741621927309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.0260806888891523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.8201649012285381,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -14.976401484722881,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.099163566036899,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6847994605757912,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7161886326169653,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.234553013271958,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.948557469055956,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6927733393224713,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.2013525213261813,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.830831100938813,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.654501342773415,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -26.542498779296807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3918078613280613,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.2120715332031295,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.00525238037107556,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3838238525390807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6456013878503928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5588834725546956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.616998226307043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.023358695495595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5104701565535894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.314998433926986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2378583635602673,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.2328578404017847,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.13605115880287322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.138901609966827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2255853300246038,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.5532869415193957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3209176311597448,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.377735854471253,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.870002746582031,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6349983215332031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.67431604294638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.209114303991237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -8.073782797028507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 12.825818333690275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -7.353357707182418,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.694002256267666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.2681881090155898,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.086424676991232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.283384504776021,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.958495563154065,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.807711697876163,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 12.955305879971569,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.8418260759337315,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.36069490670098503,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.6493757291132312,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.940854293207163,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7375001907348633,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.10050029754639,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6978000640869055,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.815200119018556,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.1746500205993584,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6507000160217302,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.359307990344766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 8.304540167777198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.7225117547602515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.926846676759947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.299000566567557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.1150521051822793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3007142203194757,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.37035696847098176,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.6956486142642753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5374240856577295,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.448809582910151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5894349779506811,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.09518578058998606,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.013984010421556503,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -49.530029296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 7.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3219658930978193,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.760340924609565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -8.261926919329678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9661156616137867,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.82626968665428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2265634924530033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.228937854300607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.04056711968953852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.0689656450725398,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.509722183772393,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.995855820177333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0956032078950795,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3147380554055932,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.5598708420196825,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.6101254743982505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.186137503473608,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -9.49904174804692,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -36.045346069336006,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.788734130859325,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.002982177734339,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.7581680297852245,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 14.732374267578166,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.238175553994695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.129314165094311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.887166294279366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.100054039018838,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -7.097833135609747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.402890876793908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.5848483484765552,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6713769624863701,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.47515194360488966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.02928905403732518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.5141495642607925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6552943103135931,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.37224294691046533,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.39958144543822105,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.740001678466797,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9499969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.8479008427509385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.248074463405242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -11.269397322674445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7054516532955191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.71614326563785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6976617392568052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.9649459242593763,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.4199210854824145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4569693045805794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -8.99745572256807,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -10.003326223522102,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8349391995768118,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.204611634389167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.0309690888234826,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.3461335443570195,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 7.565491469266485,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6885000228881779,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.621500015258789,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.1914000701904257,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6559999847412072,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.894161520163454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.175523491030566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.367392372955294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.6715976370694694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1428574153355191,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2300000871930803,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7208759677146306,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3644880497124552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.878657248125798,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4932363473619468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.448406192964088,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5789172248086885,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -13.419998168945312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 38.17999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.683697054042237,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.80774665739907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.084402041070593,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 25.509829494051417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -7.722686947055202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 15.474634821611524,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.987283150504794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.922394023600603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.292765515871878,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.5571279165618974,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.818330941918248,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 25.63931704033271,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.211155315806515,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 15.807942171178201,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.3684707706024373,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.2231763601834658,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.9839996337890682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.114498901367199,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6413031005859295,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.088013610839852,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.30879066467286975,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4615447998046989,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.486513263098814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 18.880063589642138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.264768692273547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 17.384321931221315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.0663176323956005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 13.727528879076335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9742845807756684,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.2339259556361597,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.749706284151233,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3913628126880475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.568230480411309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 12.996649037329309,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.34955297630784044,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.2697389017618059,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -9.230010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.720001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.7070877965016296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.378429824292142,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.5401675394403105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8994213670495697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.5744492472635585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.515740210518871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.668037883044029,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.416907297362563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.3161562583312705,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.127811083454969,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.274096440287966,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.7699338207682769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.0629176160148717,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.18243286095219,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.0492255031416726,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.271336913578493,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0150001525878736,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.366999053955084,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06753173828124659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.06914367675781818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.17665035247802052,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0465892028808526,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.312916583449644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7730587505366806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.832620170582224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.9972456535355176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.570476396331436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.8718471672264165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.6328582763671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7321439470563611,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4679397849449045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4546394153977902,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.569312369469369,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8415847627243132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.360490176869209,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3582564371440062,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.30999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6899948120117188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.526717854593862,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.698149112697477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6919057208618407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6020768515024644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.8759890891820952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.28917161198218544,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.503180763248956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.8204836540533407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.917649392764221,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5524696281396957,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5741653782905032,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4725893052211716,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.387520720430782,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.044135737584495516,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.1219931431513146,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.966054037837409,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3599998474121122,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.7184995651245174,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.13293380737304972,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6278849029540936,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.11446985244751318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5748471832275399,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3997182549556841,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.686196919536731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.8041869466535632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.017603184653225412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.019680031274927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0037771541300699596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.007143293108258897,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.04714311872209831,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.02842420484983199,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.08826261665592572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3354398525655675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.22651301635852827,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.19996224965391418,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.43000030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6099967956542969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.1982556369344652,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.568737317645851,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.579318447258359,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.40678862643808156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8636304267352068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.713010475972278,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.42265535746207616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.32005692178194156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8073240987641062,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.8193560584830237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.8453895464107029,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5362761727193743,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.64790120451348,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.046317825538958,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1961570224402807,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.825513462002128,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.15099983215332458,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6465000152587947,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.004783172607417896,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.11028564453124545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.015071678161618252,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.047532863616943644,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0587367961478966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.09193185525666614,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7609863820255081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2890596808744048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8352424254779223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.048936739583839,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.030714307512555772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.037142617361886066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.06398337483672889,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.05193440331665178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7368889117836952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.045347804480012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1436397676604857,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.36344250224609664,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.730010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.779998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.5780128154093918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3391421739334044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3504936302918926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.560458211883377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.3839852888496327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.908579817937972,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.693779188242095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.681435713476576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1870812772390327,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9114765669037683,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9155774688604512,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.68994575816467,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.12754634239905416,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.2418871675046526,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9250331916602619,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.4641346703074944,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.12750015258788494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.12899932861327557,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.23776306152342386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.4951809692382767,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.022151412963864914,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.16894927978518126,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5474567836818665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.7290203986145003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4621845950553602,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.4697317510266164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.594568277916486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.51740237723138,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.16428593226841492,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.06357356480189713,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.12289162013785826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.010912319116041846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4676683765428962,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4945420790008157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.41690767658569317,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4940495859627012,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.589996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9527447916718454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.5651676645324852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.6067238310662812,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6636699389369847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5127893912332482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.220479538691005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.30818751570109804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.789818501156649,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5618132535014864,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.815786405369658,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.872794930218625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.7931574852182774,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.024321022481935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.553786888257685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.9269998956034549,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.935388884940719,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9345001220703182,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.2150001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2627447509765659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.1623825073242244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.14471679687500227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6466181182861419,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.0877324233568677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2796165205259058,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.318897543784491,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.5412702236034423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.41918423873547894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.0771477800512343,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1950007847377231,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.20928737095424088,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.09779205153748194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.06029669127565995,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.114177737704869,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3639182160592571,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2319611574108824,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2399978637695312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.1599960327148438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.13686021062566667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.328643257811237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.325626063735676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5838680125312967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2671760263615948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.4839105845959617,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.7354020768592937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.811566808700782,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.2540713275446924,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.579261998648409,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.591697162888019,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7133555588125895,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.7787076576102816,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.8172179341626418,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.3542144567616505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.9571371924848515,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4444999694824219,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6979999542236328,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.09314926147462188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2827568054199219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.04372158050537678,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.22961818695068814,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9090945458829935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7179239307184115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3539739586312827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0230018035318755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.4284200511823997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0969954157453943,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0842851911272322,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.09857068743024566,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.07245477743160311,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0900656337110104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3779285400658425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2890277366945702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8859316705718083,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.48800434164989004,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8199996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.279998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.4600324348012728,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.9550486894437382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9812259619453201,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4468233729043822,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9388773315810015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.5553814802160346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.24703575546651813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.9413308710418473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06910089663091368,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.205667430280911,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.247297061097664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.576310919185675,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5726542996676853,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.888688829782715,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3717766244358387,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2042395127422223,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.26699981689452557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.5389999389648352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.02087173461914915,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.17341857910156477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.030573730468745453,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.18934925079345533,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.9637240594164709,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6391605464686201,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.705845643126013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.168269184338689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6852694540494975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.141064231699785,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.06928525652204254,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.18142809186662956,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.07027231221044827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1300001921926277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.6856379895973097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.9064077574523557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5346714145366355,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5367898459314236,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.30999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.6100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5769071740875487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.48372763246644634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4640135745220597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.9569907229860837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.5045507460614385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.8499962383183632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.437517271808142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.171894296510143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.9678387122579077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.734346373303619,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.730084673674404,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8275031767047905,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.0069808851872484,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.5166888887516823,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1812951080942149,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.026323912726072,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5209999084472656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.1100002288818303,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.20832839965819971,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.854855041503896,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.07843177795410838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3474608230590803,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7618628463173742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.3167548471798813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0126705945082914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.34179705673532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.10317403160699,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.703873527068003,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.027500152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.20214298793247787,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.05171897431435779,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.29242617562547357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1416100728485858,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.888889420785681,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.40491991842835984,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.39337714561776616,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.29000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8699989318847656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8575341831007277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.395342802262034,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.4143582165321744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2149775199101098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.31865331967246746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3188362907190276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3158930527189527,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.8528740508900325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5333973550696314,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.6459615430992067,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.6804293156845183,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3444650661914026,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.8301849509211543,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6521436402857077,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.9347054326213096,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 8.998444434674102,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.1799999237060561,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8274999618530288,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.0004102325439419019,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0846396636962865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.005713481903079298,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.028585586547855257,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.24813893916373342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.03228048373513648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.6976969661210308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.2974880113269203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.6492034095191057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.9226965249498074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.005000250680106011,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.05999946594238281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0018724488989150245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.17052828280536647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.769834552267612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.5498365897373105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2308794807871365,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5049197679892119,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.10999679565429688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5999984741210938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.9520037382618538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1378601254615086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.13944696345431495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4369542855178876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06765508558403965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.3526710547346017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.0836557707326944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.3865064684906905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5610722000914947,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.3884788662986813,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.4055180626066588,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5664418317991804,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.443876545664647,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.685978404301282,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.7024681506350507,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.53207685227476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.117999839782712,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.42549991607666016,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.030674362182615766,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.18647186279296335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0137683677673337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.07258089065551587,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.027338695425216386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.3904220824625604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.33185137401277043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.8491076260349404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2247620358514224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2336563425098257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.002499989100865019,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.005214418683733291,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.00963812938036579,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.03339368563500522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.2445385057616054,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.6708733115544447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.28130670052470486,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.11311292148827778,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.21000289916992188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4300003051757812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8921592045816107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.1349236603383717,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1619087292249253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.0210679894580696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.278962000403026,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.9089253153382195,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3075491800982997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.7395973620269012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4987723335887484,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.3855424011755444,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.427979828377269,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.1505555357393624,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.2325696308456617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.2422326649049005,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.9263615600006565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.885167745810971,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.19400005340575888,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7809999465942354,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.011202697753908808,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.00024185180663494066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.023040695190431393,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.10797735214233484,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.016233375701446562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.2371588133627487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.38989179831872,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.810150746945994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.36694233382525976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.603341175299989,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.0007141658238002391,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0007144383021764344,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.006449064526582671,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.03687320372377978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3930861507803973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.6766931208959677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.3002219277612759,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2919083538691196,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -39.17999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.71002197265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.918673031376009,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.711277559018647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -8.215464784717453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.4389790477235431,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -8.057049671759351,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.0603714562163145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -7.162958169595412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.401385638375556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.5277414932056494,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.460658818181475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.949393685565108,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.568466594004836,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.5455180405106645,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.7270641066496335,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.544145789693055,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.255815254591486,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.4054992675780795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -15.64450378417962,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8032006835936727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -2.476002197265643,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.6706999206543287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 4.063449554443309,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.94886573959772,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.6451343766369586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.7048904830159675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.42615193533056406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -7.68161678001178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.7066766156190738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.5664236886160694,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.6342817034040173,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.7373881586520419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5355940812818814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.180784219403801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7430228413399895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.3107433156561075,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0800800294108726,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.6800003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.299995422363281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.11233391555005579,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.128364622779113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.006868188058322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -11.686746450940987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.5778998317941513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -8.13847252016,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.6754722817309942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -13.620500984100993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.5032654537204149,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.877745881941941,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.7407970889059787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -11.557258904659696,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0663682005454644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.80516517059332,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.05665990182863734,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.474930600316924,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.20699996948242472,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6774997711181641,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.047599945068355964,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6918000793456969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.016194725036626778,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.1411366271972696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.1812202029391723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.397538572348949,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.484412499734313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.560943328851232,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.936686975003356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.882602907690206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.13285718645368272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2649993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.22693059762524914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4132488657133728,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.266175880874445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.591546573841799,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.36669353362955603,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.0202179787250305,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.239990234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.0699920654296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.5493059435421683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.32322462825624676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.31974702974870706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.37256696013865387,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.9239574299204865,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.9417357793955361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1980773535328773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.664811511764945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.9402374817125274,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.927394112580926,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9463240694036368,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5020545064199466,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 4.435489061169173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6084284298288551,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.816889733435236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 10.810381895549014,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.9415000915527401,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.059499359130854,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3410888671874943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.784310302734383,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.36754158020019645,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.8583761978149482,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.665328176386871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.6457407927665813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.0292966127108514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.08982421335532731,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.2448883444045045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.097268036784115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.012857709612164925,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0314298357282361,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.045017373562332264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.009270399462635304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.0697013676376774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5369550425843528,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.268364147338105,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7563050036501182,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.670013427734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 14.21002197265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.1930634258994988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.500792987010116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.620176916672891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.39584061305062423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5171084078622323,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.608998935190313,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.9606124585034737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.7577240283558551,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.583994964069858,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.250174246172943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.354105817520548,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.2663530667693319,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 3.02864003911092,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.942306284756995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.6581999213988832,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.3878463554282146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.4434997558594205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.379998779296898,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.08979980468751592,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.2665997314452966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.4277999877929801,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.231549835205101,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5516158511851943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.947875867380433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.93761590354835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.8540337000181335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8124674590437975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.0096152113574526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.033571515764508675,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.11643110002790102,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.017297086106476733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.0721608604642503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.8406279583608178,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.254849605961974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5279665999787865,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.1163548399127112,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.55999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 7.510009765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.285649110110291,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.0275048375744666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0888310066750284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.985235283802094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.070588138901286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.354477866590036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0471578280338623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.0260290768770766,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.894717571939932,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.22311390326270608,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.17724009247731498,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 7.114722830083386,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.44094349234740093,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 6.687785216156717,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5716545518684946,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.119541306906992,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.09750061035154545,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.17950210571288494,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.5508984374999955,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.8738769531250057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.14410263061523665,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.6277436065673783,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.2560257884122414,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.5497605253112074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.8689577777619815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 5.169511291775908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.93576879485322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 3.5276322721252154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.36785779680524566,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.6799992152622769,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.22000471180880066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.25187000625957934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.8028921782469745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.9692423495900044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.15409808814045212,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.47001688570389233,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1999988555908203,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.049999237060546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.48909804602553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.580957688073473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.757502579723905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.050403463130366255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.777954881213631,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.11110656941813879,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.874311742244896,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -8.074216329795913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.0981665078551712,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.3303389472363,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.4914314805715607,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.07908408315092652,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.266423249964944,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.22220078014854217,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.2554993623425394,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -3.9286459460118435,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.14449996948242116,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3974999427795396,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06259994506835653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.3501999664306652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.023699989318849646,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.08124998092651481,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.4077176579670576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 1.057800186355362,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.5864733046513164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8673064971536526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.624627579093354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.07527665220814406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.07214287349155968,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.07450022016252789,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.3411168483645981,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.2543529422768116,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -3.442337448595689,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.1434286752298508,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.18286202431535548,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4028849336382937,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8499984741210938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.4499969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.206696463120983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.235663723488234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2424849680523264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.4170481708941445,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.4223359778587916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.4659515297752659,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.06473762087537693,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.3322311795871622,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.8157649249506238,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.014955017348938782,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.023586131100017393,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.287560624612851,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.08919565338989521,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7992588793419464,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 1.55407475902698,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 2.8133392041969074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.061500167846674,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5870002746581946,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.045538024902356256,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.34854629516601676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.03089479446410337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.16292034149169865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2936180904279837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.4973414270147423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.1194786103997822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.13921513526815588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.2538264339394978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.8788096169082271,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.04142870221819206,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.03928538731166298,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.0783845884012806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.06567450398922703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.0969326921997702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.5807261765115372,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.5982011762751213,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.20747053708766094,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -7.649993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -7.589996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.7314348510594773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.4193874751019235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -6.421688787092661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -10.118379641924701,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.25350160683451,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.605395124184965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.9865907416355864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -13.4212200526467,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.34050331288911817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.16876873426475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.1556176879403175,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.98889209564341,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -2.741969975585823,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.272087774618285,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -1.3677783617332295,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -9.27564966886263,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.41849975585938637,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.8259994506835824,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.007200012207050577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.625800170898458,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.16775001525880384,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.988500061035154,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.31393742414804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -5.020920829256115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.646447751972915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.992708255966338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -5.754892932278796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -6.4542944137667675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.41857147216796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.7085723876953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.40581882055425433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.5780216121806987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -4.374174580125922,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -4.339868697111949,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.7311311799413713,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -1.8040409572700784,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.05999999999999961,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.040000000000000036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.11999999999999966,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.14000000000000012,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": 0.030000000000000027,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.0,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.0699999999999994,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": 0.020000000000000462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-28",
        "to": "2026-10-29",
        "change": -0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-22",
        "to": "2026-10-29",
        "change": -0.010000000000000231,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.010000000000000231,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.0,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.STLFSI4.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-16",
        "to": "2026-10-23",
        "change": 0.04910000000000003,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.CBOE_VIX.value",
    "available_prior_observations": 10,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 2.2200000000000024,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.029999999999997584,
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
  },
  {
    "id": "latest.BZ_F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "latest.CL_F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "latest.ES_F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "latest.NQ_F.value",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "latest.VIX.value",
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
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value", "prices.^MOVE.value"] |
| 推断与解释 | 风险厌恶加深且向金融等权扩散；期限未倒挂不足以证明安全，尚不能确认系统性危机。 |
| 反证与缺口 | 能源医疗等仍抗跌，微软能融资；信用只到29日，滞后。 |
| 确认条件 | 信用不扩张、油价与利率稳定且次日波动率不突升 |
| 失效条件 | 股票再跌同时VIX期限倒挂/信用走阔、油价冲击加剧 |
| 观察期限 | 11月2日及未来1–3交易日 |
| 条件式指导 | 等待多市场共振；不因单个VIX低值扩大方向风险 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对今早无新常规交易；Apple中国AI、PMI与伊朗威胁改变催化剂观察，收盘技术信号不变。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 周五旧反弹确认失败；尾盘离低点不是趋势反转。 |
| 反证与缺口 | AMZN较盘前明显恢复、部分防御板块强，但指数未夺回旧关口。 |
| 确认条件 | 下一交易日先守QQQ683.45、SMH511.63、SPY750.36的周五低点；首30–60分钟低点抬升、收回当日常规VWAP并回踩不破，再看QQQ698.63、SMH535.32、SPY761.46周五高点。收盘保留修复，随后再收QQQ704.40/711.62、SMH546.67/555.50，才能逐步上调评级。RSP/XLF同步改善是扩散证据；没有实测VWAP不得宣称已达成。 |
| 失效条件 | 跌破周五低点且反抽无法收回，或反弹突破后跌回开盘区间并持续弱于SPY，修复失败；VIX期限倒挂、信用继续走阔或油价供给冲击会加强反证。单次越线不是自动下单信号。 |
| 观察期限 | 11月2日及未来1–3交易日 |
| 条件式指导 | 等下一常规时段的回踩和收盘共同确认；单次越线不追。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对今早无新常规交易；Apple中国AI、PMI与伊朗威胁改变催化剂观察，收盘技术信号不变。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.XLE.return_1d_pct", "prices.XLV.return_1d_pct", "prices.XLP.return_1d_pct", "prices.SMH.relative_spy_5d_pp"] |
| 推断与解释 | 能源医疗/必需消费优先回踩观察，金融下调；军工航天也下跌，不由新闻直接推演股价。 |
| 反证与缺口 | 19ETF价格轮动非资金流，现金流披露与市场预期可能分化 |
| 确认条件 | 行业相对QQQ强，回踩后高低点抬升，金融等权扩散 |
| 失效条件 | 好财报仍持续弱于指数、资金现金回报恶化 |
| 观察期限 | 11月2日及未来1–3交易日 |
| 条件式指导 | 分行业看，不把相对收益叫净流入。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对今早无新常规交易；Apple中国AI、PMI与伊朗威胁改变催化剂观察，收盘技术信号不变。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | Meta信用展望增加回报风险，微软可融资构成反证；需求与融资能力、股东回报须分开。 |
| 反证与缺口 | H10030日2.90、AWS增长强；并非普遍需求崩塌。 Apple中国AI落地是新增应用线索，尚非现金回报证明。 |
| 确认条件 | 现金回收改善、融资压力不增且价格重新获得承接 |
| 失效条件 | 投入加速而现金回收放缓、稀释/信用压力同步上升 |
| 观察期限 | 11月2日及未来1–3交易日 |
| 条件式指导 | 新披露先更新财务桥，四家公司暂不输出旧DCF。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对今早无新常规交易；Apple中国AI、PMI与伊朗威胁改变催化剂观察，收盘技术信号不变。 |

## AI云：收入兑现不等于现金回报 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | AI资本投入与现金回收的矛盾延续；30日17:01EDT标普官方记录将META展望由稳定改为负面，AA−评级不变。微软30日提交29日债券定价表。 |
| 事实：市场反应 | 30日MSFT−1.55%、AMZN−1.41%、GOOGL−1.40%、META−1.53%；META展望发生于盘后，不能倒推解释常规跌幅。AMZN从盘前低位修复，但未收回29日收盘。 |
| 推断：解释 | 推断：需求仍增长，投资者更在意现金回报、租赁与稀释。微软能定价发债是融资可得性的反证；Meta展望变化是信用压力信号，尚非降级或违约。 |
| 受益篮子 | ["现金回收与价格承接更好的云公司观察篮子"] |
| 受损篮子 | ["持续投入超现金回收且估值承压者"] |
| 反证 | AWS增速39.3%、微软仍有正公司自由现金流，H100租金维持；不能把股价调整直接等同AI需求消失。 |
| 下一催化剂 | 11月4日微软预定债券结算、后续Meta现金流与融资披露、下周PLTR/AMD |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm", "https://spratings.spglobal.com/ratings/en/regulatory/ratings-actions", "https://www.streetinsider.com/Reuters/S%26P%2BGlobal%2Brevises%2Boutlook%2Bon%2BMeta%2Bto%2Bnegative%2Bon%2Bcashflow%2Bconcerns/27267040.html", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm", "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm", "https://www.silicondata.com/products/silicon-index/h100"] |

## 存储与芯片：强业绩仍需承接 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Sandisk FY27Q1收入110.31亿美元、同比378%，non-GAAP EPS49.51；Q2收入指引122–126亿、EPS55–57（拆分前）。Intel Q4收入指引150–160亿，官方同时提到PC疲弱与数据中心供给约束。 |
| 事实：市场反应 | 30日SMH−6.98%、MU−5.30%、DRAM−7.23%、SNDK−13.47%、VRT−5.46%。 |
| 推断：解释 | 推断：强业绩仍遭遇估值和风险预算调整。QQQ最高698.63低于昨晚确认704.40，SMH最高535.32低于546.67；旧修复条件未成立。 |
| 受益篮子 | ["财报后守住开盘区间、强于SMH的存储/设备观察篮子"] |
| 受损篮子 | ["高预期且反抽反复失守者"] |
| 反证 | AWS与Sandisk经营数据强；周五均从低点回升，但尚未夺回失地，不将尾盘反抽当趋势反转。 |
| 下一催化剂 | 周一开盘承接、AMD11月3日财报；SNDK11月20日拆股须调整比较口径 |
| 证据 | ["https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results", "https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000188/q326earningsrelease.htm", "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"] |

## 防御轮动缩窄，金融不再领先 · 减弱

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 29日金融医疗与等权收涨；30日ABBV官方新财报收入174.04亿美元、调整EPS3.82，全年调整EPS指引升至13.95–13.99。 |
| 事实：市场反应 | 30日RSP−0.79%、XLF−0.76%、XLI−1.60%，XLV+0.45%、XLP+1.41%、XLU+0.67%。 |
| 推断：解释 | 推断：昨晚金融医疗共同走强的判断必须拆开，金融与等权失守原条件，医疗及必需消费更抗跌。相对强不等于绝对低风险；XLV不能代表小型生物科技。 |
| 受益篮子 | ["金融", "医疗", "现金回报稳健的工业观察篮子"] |
| 受损篮子 | ["相对弱势科技权重"] |
| 反证 | RSP跌幅小于SPY，尚有相对防御；若金融重新收回前日价格且信用稳定，可恢复观察优先级。 |
| 下一催化剂 | 下周非农、行业财报与风险偏好扩散 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm", "https://www.ici.org/research/stats/etf_flows", "https://query1.finance.yahoo.com/v8/finance/chart/XLV"] |

## 利率与避险信号并不一致 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Logan30日官方讲话支持本周暂缓、维持3.75–4.00%，个人主张至少再两次25bp加息；不是FOMC承诺。 本次复核Musalem30日讲话，也倾向很快进一步收紧，但仍是个人条件式观点。 |
| 事实：市场反应 | 30日GLD−3.47%、TLT+0.43%、UUP−0.14%；VIX19.42、MOVE100.20同步上升。 |
| 推断：解释 | 推断：国债上升与黄金下跌不能归为统一避险潮；通胀与投入回报压力削弱简单降息救市叙事，仍需观察信用。 |
| 受益篮子 | ["能传导成本且现金稳健者"] |
| 受损篮子 | ["折现率敏感且现金回收慢者"] |
| 反证 | VIX期限仍正斜率；实际收益率和信用仅29日，未完整覆盖周五冲击。 |
| 下一催化剂 | 11月6日非农、11月10日CPI及后续官员表态 |
| 证据 | ["https://www.dallasfed.org/news/speeches/logan/2026/lkl261030", "https://fred.stlouisfed.org/series/DGS10", "https://query1.finance.yahoo.com/v8/finance/chart/GLD", "https://www.stlouisfed.org/from-the-president/remarks/2026/remarks-on-us-economy-and-monetary-policy-somc"] |

## 能源现金回报与地缘溢价 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 31日伊朗领导层被报道要求遇美以攻击时作出不受地域限制的回应；这是条件式威胁，未证实攻击已经发生。中国官方制造业PMI49.3由扩张转收缩，为需求侧反证。 |
| 事实：市场反应 | 最近交易日30日XLE+1.91%、XOP+2.13%；周末消息尚无美国常规交易反馈。最新抓取WTI104.12、Brent113.43对应周五20:59UTC分钟，和今早源值不同且合约月未对齐，不计算周末涨幅。 |
| 推断：解释 | 推断：供应风险支持能源溢价，增长放缓和谈判改善则压制需求/溢价，必须分开检验。 |
| 受益篮子 | ["实际供应受益且价格有承接的油气观察篮子"] |
| 受损篮子 | ["燃料成本敏感企业、融资依赖链条"] |
| 反证 | 油价反转或谈判改善会削弱溢价；军工ITA−2.13%、航天ARKX−3.87%，地缘新闻并未保证相关股票普涨。 |
| 下一催化剂 | 周末独立航运通报、周一油价与能源回踩；所谓11月4日军事行动时间没有官方确认 |
| 证据 | ["https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/cvx-20261030.htm", "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm", "https://www.axios.com/2026/10/31/irans-supreme-leader-maximum-response-us-attack", "https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html"] |

## 苹果中国AI应用落地，等待商业兑现 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Apple31日官方宣布中国部分核心AI功能11月4日开发者测试、12月iOS27.3正式推出；部分体验接入千问。并非全部下一代Siri，也非所有平台已获审批。 |
| 事实：市场反应 | 周末暂无美国常规市场反应；AAPL345.10、BABA97.9845是周五盘后末笔，不能解释为对周六正式公告的反应。 |
| 推断：解释 | 推断：应用落地是AI需求反证，可观察AAPL/BABA及软件；没有获客、付费和成本数据前，不能升级为盈利已改善。 |
| 受益篮子 | ["AAPL", "BABA"] |
| 受损篮子 | ["推断：缺乏差异化、获客成本更高的竞争应用，尚无公司级损失证据"] |
| 反证 | 推出范围有限、商业化回报与计算成本未披露，其他平台仍待审批。 |
| 下一催化剂 | 11月4日中国Beta与后续用户/财务数据 |
| 证据 | ["https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | 345.10 | 0.14 | 2026-10-30T23:59:55+00:00 | 2026-10-30T23:59:55+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| AMD | 508.22 | 0.68 | 2026-10-30T23:59:53+00:00 | 2026-10-30T23:59:53+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| AMZN | 240.80 | 0.19 | 2026-10-30T23:59:59+00:00 | 2026-10-30T23:59:59+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| AVGO | 327.13 | 0.32 | 2026-10-30T23:59:58+00:00 | 2026-10-30T23:59:58+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| BABA | 97.98 | -0.06 | 2026-10-30T23:54:54+00:00 | 2026-10-30T23:54:54+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| CAT | 624.89 | 0.34 | 2026-10-30T23:57:14+00:00 | 2026-10-30T23:57:14+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| CEG | 262.87 | 0.19 | 2026-10-30T23:51:56+00:00 | 2026-10-30T23:51:56+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| CVX | 235.89 | 0.16 | 2026-10-30T23:41:06+00:00 | 2026-10-30T23:41:06+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| DRAM | 48.37 | 0.75 | 2026-10-30T23:59:50+00:00 | 2026-10-30T23:59:50+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| GEV | 860.35 | 0.29 | 2026-10-30T23:56:56+00:00 | 2026-10-30T23:56:56+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| GLD | 356.15 | 0.10 | 2026-10-30T23:59:50+00:00 | 2026-10-30T23:59:50+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| GLW | 123.69 | 0.31 | 2026-10-30T23:59:31+00:00 | 2026-10-30T23:59:31+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| GOOGL | 281.48 | 0.59 | 2026-10-30T23:59:41+00:00 | 2026-10-30T23:59:41+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| IGV | 104.47 | 0.17 | 2026-10-30T23:27:35+00:00 | 2026-10-30T23:27:35+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| ILMN | 238.86 | 1.22 | 2026-10-30T21:29:41+00:00 | 2026-10-30T21:29:41+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| INTC | 64.89 | -1.32 | 2026-10-30T23:59:56+00:00 | 2026-10-30T23:59:56+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| IWM | 279.82 | 0.18 | 2026-10-30T23:57:11+00:00 | 2026-10-30T23:57:11+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| LLY | 1,414.51 | -0.21 | 2026-10-30T23:59:03+00:00 | 2026-10-30T23:59:03+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| META | 614.00 | -0.16 | 2026-10-30T23:59:56+00:00 | 2026-10-30T23:59:56+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| MSFT | 522.99 | 0.21 | 2026-10-30T23:59:12+00:00 | 2026-10-30T23:59:12+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| MU | 889.20 | 0.50 | 2026-10-30T23:59:54+00:00 | 2026-10-30T23:59:54+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| NOW | 105.34 | 0.21 | 2026-10-30T23:59:32+00:00 | 2026-10-30T23:59:32+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| NVDA | 205.25 | 0.30 | 2026-10-30T23:59:57+00:00 | 2026-10-30T23:59:57+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| NXPI | 259.09 | -0.20 | 2026-10-30T21:07:33+00:00 | 2026-10-30T21:07:33+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| ORCL | 130.98 | 0.24 | 2026-10-30T23:59:47+00:00 | 2026-10-30T23:59:47+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| PLTR | 184.78 | 0.37 | 2026-10-30T23:57:25+00:00 | 2026-10-30T23:57:25+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| QQQ | 692.74 | 0.33 | 2026-10-30T23:59:55+00:00 | 2026-10-30T23:59:55+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| RSP | 218.45 | 0.06 | 2026-10-30T23:55:47+00:00 | 2026-10-30T23:55:47+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| SMH | 526.71 | 0.81 | 2026-10-30T23:59:52+00:00 | 2026-10-30T23:59:52+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| SNDK | 1,157.58 | 0.58 | 2026-10-30T23:59:57+00:00 | 2026-10-30T23:59:57+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| SPY | 757.12 | 0.19 | 2026-10-30T23:59:59+00:00 | 2026-10-30T23:59:59+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| STX | 649.18 | 0.71 | 2026-10-30T23:59:02+00:00 | 2026-10-30T23:59:02+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| TLT | 81.65 | -0.23 | 2026-10-30T23:59:30+00:00 | 2026-10-30T23:59:30+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| VRT | 232.97 | 0.20 | 2026-10-30T23:59:27+00:00 | 2026-10-30T23:59:27+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| XLE | 70.02 | 0.00 | 2026-10-30T23:55:14+00:00 | 2026-10-30T23:55:14+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| XLF | 56.58 | 0.12 | 2026-10-30T22:38:25+00:00 | 2026-10-30T22:38:25+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| XLI | 167.77 | 0.22 | 2026-10-30T23:15:11+00:00 | 2026-10-30T23:15:11+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| XLV | 185.00 | 0.07 | 2026-10-30T23:58:10+00:00 | 2026-10-30T23:58:10+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |
| XOM | 187.02 | -0.12 | 2026-10-30T23:47:04+00:00 | 2026-10-30T23:47:04+00:00 | 2026-10-31T12:02:18.014317+00:00 | last_session |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 755.72 | USD_per_share | 2026-10-30 | -1.77 | -0.56 | -1.81 | ok |
| QQQ | 690.49 | USD_per_share | 2026-10-30 | -3.47 | -1.97 | -7.88 | ok |
| IWM | 279.33 | USD_per_share | 2026-10-30 | -1.65 | 1.30 | -0.78 | ok |
| RSP | 218.31 | USD_per_share | 2026-10-30 | -0.79 | 0.82 | 4.09 | ok |
| GLD | 355.78 | USD_per_share | 2026-10-30 | -3.47 | -2.95 | -6.41 | ok |
| GC=F | 3,898.90 | USD_per_troy_ounce | 2026-10-30 | -3.29 | -2.72 | -6.33 | ok |
| CL=F | 104.12 | USD_per_barrel | 2026-10-30 | 2.08 | 0.82 | 14.28 | ok |
| BZ=F | 117.64 | USD_per_barrel | 2026-10-30 | 2.40 | 0.79 | 15.05 | ok |
| TLT | 81.84 | USD_per_share | 2026-10-30 | 0.43 | 0.61 | 5.63 | ok |
| UUP | 29.00 | USD_per_share | 2026-10-30 | -0.14 | 0.14 | 0.38 | ok |
| HYG | 77.43 | USD_per_share | 2026-10-30 | -0.19 | 0.49 | 0.68 | ok |
| LQD | 104.27 | USD_per_share | 2026-10-30 | 0.05 | 0.40 | 2.40 | ok |
| ^VIX | 19.42 | index | 2026-10-30 | 12.91 | -0.15 | 26.85 | ok |
| ^VIX3M | 20.78 | index | 2026-10-30 | 7.28 | 1.46 | 15.38 | ok |
| ^VVIX | 106.43 | index | 2026-10-30 | 8.59 | -2.98 | 22.31 | ok |
| ^MOVE | 100.20 | index | 2026-10-30 | 7.12 | -3.01 | -7.33 | ok |
| NVDA | 204.64 | USD_per_share | 2026-10-30 | -4.22 | -3.00 | -12.53 | ok |
| MSFT | 521.91 | USD_per_share | 2026-10-30 | -1.55 | -0.50 | 0.85 | ok |
| AMZN | 240.35 | USD_per_share | 2026-10-30 | -1.41 | -3.08 | -4.44 | ok |
| GOOGL | 279.84 | USD_per_share | 2026-10-30 | -1.40 | -12.61 | -18.53 | ok |
| META | 614.99 | USD_per_share | 2026-10-30 | -1.53 | -4.30 | -15.53 | ok |
| CRWV | 54.87 | USD_per_share | 2026-10-30 | -9.66 | 1.17 | -38.77 | ok |
| MU | 884.74 | USD_per_share | 2026-10-30 | -5.30 | 0.82 | -17.68 | ok |
| DRAM | 48.01 | USD_per_share | 2026-10-30 | -7.23 | 2.02 | -22.29 | ok |
| VRT | 232.50 | USD_per_share | 2026-10-30 | -5.46 | 19.65 | -7.80 | ok |

## 跨资产风险解释

更接近风险厌恶加深，而非过热；不能仅凭VIX未到某整数阈值断言安全。30日同日VIX19.42、VIX3M20.78，比值约0.935，期限尚未倒挂；VVIX106.43、MOVE100.20，波动压力上升。29日HY OAS326bp/IG89bp，较上期28日314/86走阔12/3bp，尚不覆盖30日完整冲击。美债2年4.61%、10年4.98%、实际10年2.63%均29日；盈亏平衡30日2.34%，金融压力23日−0.5837，GPR26日165.25（MA7 181.42）。黄金跌而国债涨、美元弱，风险通道分化。CNN418；CME官方矩阵referrer失败。Logan的再加息主张为个人观点，现行目标区间3.75–4.00%，不把预测合约当政策事实；不存在已验证统一避险/战争指数。 本次晚间复查宏观日期仍未前移。Musalem30日讲话倾向很快继续收紧，但也承认AI融资利差扩大、融资渠道仍健康；不存在已实施的新一次加息。中国31日官方制造业PMI49.3较前月50.1降0.8个百分点；扩散指数不是GDP增速。伊朗最新条件威胁不等于已开战。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.61 | percent | 2026-10-29 | -0.27 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.26 | percentage_points | 2026-10-29 | 0.02 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.89 | percentage_points | 2026-10-29 | 0.03 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.98 | percent | 2026-10-29 | -0.31 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.63 | percent | 2026-10-29 | -0.30 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.34 | percent | 2026-10-30 | -0.02 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.58 | index | 2026-10-23 | 0.28 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.42 | index | 2026-10-30 | 4.11 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 165.25 | index | 2026-10-26 | -36.19 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 149.77 | index | 2026-10-26 | -147.74 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 187.38 | index | 2026-10-26 | 26.08 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 181.42 | index | 2026-10-26 | 0.55 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 175.44 | index | 2026-10-26 | 12.06 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -4.89 | -2.03 | -10.16 | -3.12 | -1.47 | -8.35 | 2.21 | 2026-10-30 |
| XLE | 能源 | 1.91 | 1.00 | 11.46 | 3.68 | 1.55 | 13.27 | 1.01 | 2026-10-30 |
| XLF | 金融 | -0.76 | 1.09 | 5.65 | 1.02 | 1.65 | 7.45 | 1.15 | 2026-10-30 |
| XLI | 工业 | -1.60 | 1.69 | -1.50 | 0.17 | 2.25 | 0.31 | 1.45 | 2026-10-30 |
| XLV | 医疗 | 0.45 | 3.12 | 11.25 | 2.22 | 3.68 | 13.06 | 2.13 | 2026-10-30 |
| XLP | 必需消费 | 1.41 | 1.31 | 11.04 | 3.18 | 1.87 | 12.85 | 1.96 | 2026-10-30 |
| XLY | 可选消费 | -0.71 | 2.02 | 4.85 | 1.07 | 2.58 | 6.66 | 1.43 | 2026-10-30 |
| XLC | 通信 | -1.29 | -5.32 | -9.45 | 0.48 | -4.76 | -7.64 | 1.22 | 2026-10-30 |
| XLU | 公用事业 | 0.67 | 2.04 | 9.04 | 2.45 | 2.60 | 10.85 | 1.01 | 2026-10-30 |
| XLRE | 房地产 | 0.26 | 1.41 | 5.78 | 2.03 | 1.97 | 7.59 | 1.11 | 2026-10-30 |
| XLB | 材料 | 0.40 | 2.79 | 7.94 | 2.17 | 3.35 | 9.75 | 1.02 | 2026-10-30 |
| SMH | 半导体 | -6.98 | -0.89 | -17.14 | -5.20 | -0.33 | -15.34 | 1.99 | 2026-10-30 |
| IGV | 软件 | -3.41 | -5.70 | -3.82 | -1.64 | -5.14 | -2.01 | 1.86 | 2026-10-30 |
| XOP | 油气开采 | 2.13 | 1.03 | 10.18 | 3.90 | 1.59 | 11.99 | 1.69 | 2026-10-30 |
| OIH | 油服 | 0.90 | 3.58 | 7.54 | 2.67 | 4.14 | 9.35 | 1.02 | 2026-10-30 |
| ITA | 航空与国防 | -2.13 | 3.71 | 0.94 | -0.35 | 4.27 | 2.75 | 1.47 | 2026-10-30 |
| ARKX | 航天主题 | -3.87 | -0.17 | -8.84 | -2.10 | 0.39 | -7.03 | 0.95 | 2026-10-30 |
| KRE | 区域银行 | -1.17 | -0.62 | 1.74 | 0.61 | -0.06 | 3.55 | 1.21 | 2026-10-30 |
| SKYY | 云计算 | -4.57 | -4.54 | -4.98 | -2.80 | -3.98 | -3.17 | 1.00 | 2026-10-30 |

## 资金证据分层

19个行业主题ETF的30日同端点价格量能覆盖完整：能源XLE+1.91%、油气XOP+2.13%、必需消费XLP+1.41%、医疗XLV+0.45%；半导体SMH−6.98%、科技XLK−4.89%、云SKYY−4.57%、软件IGV−3.41%。SMH五日相对SPY已转−0.33个百分点（上期+6.62），不能再用此前反弹解释为领先。金融和工业同跌，防御轮动较29日缩窄；相对今早没有新交易日。流量证据另列：ICI最新仍27日发布截至21日周净发行，全ETF458.21亿美元、国内股票278.23亿、债券95.67亿；不代表30日资金。发行人VanEck本次展示30日NAV522.76、资产664.4亿美元，缺精确份额/拆分桥，不能用资产变动计算净申赎。无当期机构持仓证据；上涨、放量及相对收益不叫主力净流入。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-31T12:08:07.493709+00:00：全主题基础查询及12组主动补查，新增11月伊朗合约与Apple中国AI/CXMT。CPI/Meta/Anthropic各25/86/31项仅首10，基础多组截断。Apple已披露季度收入类合约价差27–74个百分点且成交少，不用于解释未来AI采用；CXMT仅低质量参考，不当HBM竞争证据。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [9.55, {"status": "comparable", "change_pp": -0.15000000000000013}] | {"spread": 0.0030000000000000027, "volume24h_usd": 3659.058615, "liquidity_usd": 44619.45024, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:16.523281+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价9.55%，24h成交约3659美元；结算定义、到期和价差优先，不是客观概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [5.0, {"status": "comparable", "change_pp": -5.0}] | {"spread": 0.04000000000000001, "volume24h_usd": 10573.288459, "liquidity_usd": 15825.9169, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:38.503551+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["本次报价5%，24h成交约10573美元；结算定义、到期和价差优先，不是客观概率。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |
| ["US x Iran ceasefire continues through November 30?", "指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [37.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000009, "volume24h_usd": 9104.128368, "liquidity_usd": 89005.9293, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:16.523281+00:00", "contract_end_at": "2026-11-30T23:59:00+00:00"} | ["新增11月30日期限独立基线，不能延用10月31日高概率", "美国对伊朗直接合格军事行动的尾部风险，不含所有中东冲突"] | ["按规则核验实际行动，并看油价、信用及股票承接", "只有威胁或其他地域事件不能判定触发"] | [null, null] |
| ["US x Iran ceasefire continues through November 2?", "指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [92.45, {"status": "no_baseline"}] | {"spread": 0.0030000000000000027, "volume24h_usd": 94662.112871, "liquidity_usd": 89550.01334, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:16.523281+00:00", "contract_end_at": "2026-11-03T04:59:00+00:00"} | ["新增11月2日期限基线，贴近下次开盘但截止不等同股市收盘", "近端周末与周一风险"] | ["按规则核验实际行动，并看油价、信用及股票承接", "只有威胁或其他地域事件不能判定触发"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [97.45, {"status": "comparable", "change_pp": 1.8000000000000016}] | {"spread": 0.0010000000000000009, "volume24h_usd": 180090.876485, "liquidity_usd": 90580.59181, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:16.523281+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["本次报价97.45%，24h成交约180091美元；结算定义、到期和价差优先，不是客观概率。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.009999999999999995, "volume24h_usd": 104908.435736, "liquidity_usd": 300526.3915, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:16.523281+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价11.5%，24h成交约104908美元；结算定义、到期和价差优先，不是客观概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [87.9, {"status": "comparable", "change_pp": -2.3499999999999965}] | {"spread": 0.008000000000000007, "volume24h_usd": 12801.78608, "liquidity_usd": 19450.83609, "quality_flags": [], "retrieved_at": "2026-10-31T12:02:41.304759+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["本次报价87.9%，24h成交约12802美元；结算定义、到期和价差优先，不是客观概率。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [16.5, {"status": "no_baseline"}] | {"spread": 0.04999999999999999, "volume24h_usd": 51.82, "liquidity_usd": 1077.7132, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-10-31T12:02:41.445709+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["价差5个百分点、24h仅约52美元；仅低质量观察", "Apple采购/协议可能改变存储供应链，不证明HBM良率或AI利润已崩塌"] | ["公司官方采购/协议与量产、价格资料分别验证", "传闻或审批申请尚非已采购；没有交付不一定阻止本合约Yes"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will AMD (AMD) beat quarterly earnings?", "AMD下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定1.97美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。", "https://polymarket.com/event/amd-quarterly-earnings-nongaap-eps-11-03-2026-1pt97"] | [75.0, {"status": "comparable", "change_pp": -4.0000000000000036}] | {"spread": 0.08000000000000007, "volume24h_usd": 34.008667, "liquidity_usd": 290.2931, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-31T12:02:38.487182+00:00", "contract_end_at": "2026-11-03T22:00:00+00:00"} | ["本次报价75%，24h成交约34美元；结算定义、到期和价差优先，不是客观概率。", "AMD11月3日电话会时间已核验；PLTR官方预告11月2日盘后，具体分钟未核验故留空。两者检验AI硬件/软件兑现。"] | ["官方主要non-GAAP EPS按固定阈值核验，再看订单、现金和财报后价格。", "EPS过线但指引/价格承接失败，不能当作买入依据。"] | ["2026-11-03T17:00:00-05:00", "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"] |
| ["Will Palantir (PLTR) beat quarterly earnings?", "Palantir下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定0.42美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。", "https://polymarket.com/event/pltr-quarterly-earnings-nongaap-eps-11-02-2026-0pt42"] | [82.0, {"status": "comparable", "change_pp": -3.0000000000000027}] | {"spread": 0.039999999999999925, "volume24h_usd": 332.303075, "liquidity_usd": 872.0932, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-10-31T12:02:38.487507+00:00", "contract_end_at": "2026-11-02T22:00:00+00:00"} | ["本次报价82%，24h成交约332美元；结算定义、到期和价差优先，不是客观概率。", "AMD11月3日电话会时间已核验；PLTR官方预告11月2日盘后，具体分钟未核验故留空。两者检验AI硬件/软件兑现。"] | ["官方主要non-GAAP EPS按固定阈值核验，再看订单、现金和财报后价格。", "EPS过线但指引/价格承接失败，不能当作买入依据。"] | [null, null] |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 69.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -4.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.0000000000000009} |
| 24h成交量 / 流动性 USD | [236114.865096, 574579.9337] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T11:58:15.716458Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 97.45 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.1, 18.95] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.8000000000000016} |
| 24h成交量 / 流动性 USD | [180090.876485, 90580.59181] |
| 价差 pp | 0.10 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:00:15.63765Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [104908.435736, 300526.3915] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:00:15.63765Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran ceasefire continues through November 2?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 6369333 |
| Yes 概率 % | 92.45 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.5, null] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [94662.112871, 89550.01334] |
| 价差 pp | 0.30 |
| 到期 | 2026-11-03T04:59:00+00:00 |
| 结算规则摘要 | 指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。 |
| 规则指纹 | 9b8785d047097fb1a2f6691d76f44da8472e9f99ec1707edac4350b22b4d6259 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:00:15.63765Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.05 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -0.35] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [34525.6, 653183.54074] |
| 价差 pp | 缺失 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | ["spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-31T12:00:15.63765Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## US x Iran ceasefire continues through November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4713483 |
| Yes 概率 % | 37.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 2.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [9104.128368, 89005.9293] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-30T23:59:00+00:00 |
| 结算规则摘要 | 指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。 |
| 规则指纹 | 2f10f9c94ec72b4835bbb7166be00ea0e23e8f953e2f04a18c6d8cb64275e844 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:00:15.63765Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 1.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [4265.949736999999, 15019.5998] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T11:56:16.040425Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 9.55 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.35, 0.1] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.15000000000000013} |
| 24h成交量 / 流动性 USD | [3659.058615, 44619.45024] |
| 价差 pp | 0.30 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T11:56:16.040425Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 17.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.0, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.5000000000000013} |
| 24h成交量 / 流动性 USD | [1938.27, 17447.0091] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:00:15.63765Z |
| 抓取时间 | 2026-10-31T12:02:16.523281+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 5.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -8.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -5.0} |
| 24h成交量 / 流动性 USD | [10573.288459, 15825.9169] |
| 价差 pp | 4.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:02:16.43618Z |
| 抓取时间 | 2026-10-31T12:02:38.503551+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 87.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-5.7, 9.4] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.3499999999999965} |
| 24h成交量 / 流动性 USD | [12801.78608, 19450.83609] |
| 价差 pp | 0.80 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-31T12:02:16.43618Z |
| 抓取时间 | 2026-10-31T12:02:41.304759+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will AMD (AMD) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262633 / 6280962 |
| Yes 概率 % | 75.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-9.5, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.0000000000000036} |
| 24h成交量 / 流动性 USD | [34.008667, 290.2931] |
| 价差 pp | 8.00 |
| 到期 | 2026-11-03T22:00:00+00:00 |
| 结算规则摘要 | AMD下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定1.97美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。 |
| 规则指纹 | 45fb7613b172228eb6c9f337a9f40f9667816eecd866e1137e8b1f62ff7355e6 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-31T11:36:15.804987Z |
| 抓取时间 | 2026-10-31T12:02:38.487182+00:00 |
| 来源 | https://polymarket.com/event/amd-quarterly-earnings-nongaap-eps-11-03-2026-1pt97 |

## Will Palantir (PLTR) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262630 / 6280959 |
| Yes 概率 % | 82.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-3.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.0000000000000027} |
| 24h成交量 / 流动性 USD | [332.303075, 872.0932] |
| 价差 pp | 4.00 |
| 到期 | 2026-11-02T22:00:00+00:00 |
| 结算规则摘要 | Palantir下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定0.42美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。 |
| 规则指纹 | d3c8b7becbdaf8a9088e9ce0ead238b19bc1a5cf62e8f1a6ee479a1e1d8a7bef |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-31T12:02:16.43618Z |
| 抓取时间 | 2026-10-31T12:02:38.487507+00:00 |
| 来源 | https://polymarket.com/event/pltr-quarterly-earnings-nongaap-eps-11-02-2026-0pt42 |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 16.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, 1.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [51.82, 1077.7132] |
| 价差 pp | 5.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-31T12:02:16.43618Z |
| 抓取时间 | 2026-10-31T12:02:41.445709+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## AI 压力：合约、经营与估值分开

预测层：2026专门AI合约9.55%，2027年6月版本22.5%，均须90天窗口至少三项极端条件；不能当普通回调概率，两个版本定义也不直接互比。经营层：AWS增长39.3%与Amazon TTM公司FCF−423.57亿美元并存，不是单季度或FCFF；H10030日日期表2.90美元/GPU小时，与23日相同，手算7日0%，标题4.7%冲突不采用。融资层：标普30日17:01EDT确认META展望转负、AA−不变，现金回收压力值得关注但不是违约；MSFT30日提交29日定价表，合计250亿美元本金（固定230亿、浮动20亿），固定票息4.85–6.35%、浮动SOFR+35/53bp，预定11月4日结算，不能称已到账。AAA/Aaa稳定评级与融资可得性反驳全面信用冻结；不同期限票息不能当相同期限融资利差变化。估值层：31日晚五家SEC均复查，无比今早更新的定期财报，NVDA无新定期财报按30日收盘更新旧核验底稿；MSFT/AMZN/GOOGL/META最新TTM、净债务、租赁和稀释桥未齐，暂停精确DCF与隐含增长反推。情景不是客观概率，公司整体估值不全归AI。 苹果中国AI应用落地提供需求侧新线索，但不证明资本回报周期缩短；微软和Meta融资旧披露维持原核验时点。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-31T12:05:53.224326+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 204.64 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.27828385715229753, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -51.73 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -24.69 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 18.54 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-31T12:05:54.373708+00:00", "latest_filing_date": "2026-10-28"} |
| 观测财务数据 | {"revenue_million": 92279, "operating_income_million": 45915, "operating_cashflow_million": 58000, "cash_capex_million": 39367, "cfo_less_cash_capex_million": 18633, "diluted_shares_million": 7446, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null} |
| 来源 | ["https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast", "https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。 |

## AMZN · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | FY2026 Q3 ended 2026-09-30 |
| 披露检查 | {"checked_at": "2026-10-31T12:06:01.915793+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
| 观测财务数据 | {"revenue_quarter_million": 201900, "aws_revenue_quarter_million": 45980, "cfo_ttm_million": 168300, "net_cash_capex_ttm_million": 210657, "company_cash_fcf_ttm_million": -42357, "gaap_eps": 1.89} |
| 来源 | ["https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "https://data.sec.gov/submissions/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm"] |
| 口径 | TTM公司现金FCF=CFO减净现金资本支出；不等于FCFF；不能当单季。融资租赁和债务股数桥待补。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。 |

## GOOGL · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-31T12:06:04.777771+00:00", "latest_filing_date": "2026-10-29"} |
| 观测财务数据 | {"revenue_million": 127577, "operating_income_million": 40576, "net_income_million": 26468, "net_income_to_common_million": 26170, "operating_cashflow_million": 42290, "cash_capex_million": 51355, "cfo_less_cash_capex_million": -9065, "diluted_shares_million": 12368, "common_stock_net_proceeds_million": 12371, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null, "finance_lease_liabilities_million": 3705} |
| 来源 | ["https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。 |

## META · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-31T12:06:07.198972+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 周五修复失败后重新验证

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 周一价格承接与周末消息 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP"] |
| 确认条件 | 下一交易日先守QQQ683.45、SMH511.63、SPY750.36的周五低点；首30–60分钟低点抬升、收回当日常规VWAP并回踩不破，再看QQQ698.63、SMH535.32、SPY761.46周五高点。收盘保留修复，随后再收QQQ704.40/711.62、SMH546.67/555.50，才能逐步上调评级。RSP/XLF同步改善是扩散证据；没有实测VWAP不得宣称已达成。 |
| 失效条件 | 跌破周五低点且反抽无法收回，或反弹突破后跌回开盘区间并持续弱于SPY，修复失败；VIX期限倒挂、信用继续走阔或油价供给冲击会加强反证。单次越线不是自动下单信号。 |
| 观察期限 | 11月2日及随后1–3个交易日 |
| 反证 | AMZN从盘前低位回升、能源医疗仍强；但周五科技未收复首道关口。 |
| 状态 | 旧剧本失败；新一轮等待 |

## 能源和医疗回踩承接

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 财报现金回报、供给消息及防御轮动 |
| 关联标的 | ["XLE", "XLV", "XLP"] |
| 确认条件 | 周一XLE守69.28、XLV守184.52的周五低点并重新高低点抬升，站回实测当日VWAP、保持相对SPY强度；能源70.15/医疗187.99上方突破须有持续承接。 |
| 失效条件 | 跌破周五低点反抽失败、好业绩下仍持续跑输SPY；能源另看供应溢价快速消退。 |
| 观察期限 | 未来1–3交易日 |
| 反证 | 医疗ETF不代表小型生物科技；高开或相对抗跌不保证正收益。 |
| 状态 | 优先观察，等待回踩 |

## 金融恢复观察资格

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 信用变化与市场扩散 |
| 关联标的 | ["XLF", "RSP"] |
| 确认条件 | XLF先收56.67/56.94，RSP先收220.04；低点抬升、收盘保持且信用不继续恶化。 |
| 失效条件 | XLF56.33、RSP217.36周五低点失守后反抽失败。 |
| 观察期限 | 未来1–3交易日 |
| 反证 | 两者周五仍相对强于SPY，但绝对价格条件已失守。 |
| 状态 | 原条件失败，优先级下调 |

## 芯片和存储需价格再确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | AMD下周财报、强业绩兑现检验 |
| 关联标的 | ["MU", "DRAM", "SNDK", "VRT"] |
| 确认条件 | 先守MU861.59、DRAM46.96、SNDK1115.16、VRT226.86周五低点，回踩后站回当日VWAP且强于SMH；再看MU906.54、DRAM49.31、SNDK1239、VRT240.78周五高点。不一次要求越过全部远端旧阻力。 |
| 失效条件 | 破周五低点且反抽失败，或EPS好但价格、现金回收指引继续走弱。 |
| 观察期限 | 周一至AMD财报后1–3日 |
| 反证 | 经营仍强，可快速反抽；SNDK8拆1不改变价值，20日起须调整比较价。 |
| 状态 | 高波动等待，不以跌幅当买点 |

## AI云与软件现金回报检验

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | Meta展望、微软债券结算和PLTR财报 |
| 关联标的 | ["MSFT", "AMZN", "GOOGL", "META", "IGV"] |
| 确认条件 | IGV守103.33、先收107.05周五高点；龙头反抽后低点抬升、现金流预期停止下修，融资完成不伴随额外恶化。 |
| 失效条件 | 公司投入继续加速而现金回收/信用下降，反抽持续低于前高。 |
| 观察期限 | 未来1–3交易日及下一披露 |
| 反证 | 微软仍能发债、云需求高增长，不支持所有AI公司融资已冻结。 |
| 状态 | 观察现金回报，不把完成融资等同股价见底 |

## 苹果应用与软件事件观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 11月4日Apple中国AI测试、OKTA纳入S&P500生效 |
| 关联标的 | ["AAPL", "BABA", "OKTA", "IGV"] |
| 确认条件 | 周一价格守开盘区间、形成更高低点，站回实测常规VWAP且持续强于QQQ；后续验证用户采用/经营兑现。OKTA单独核验指数生效前后价格及成交，不当软件全面复苏。 |
| 失效条件 | 高开后跌破开盘低点且反抽失败；商业化延迟/成本超预期；指数被动买盘结束后走势转弱。 |
| 观察期限 | 11月2–4日与随后1–3交易日 |
| 反证 | 无新经营收入证明，指数纳入是机械需求而非盈利上修，当前未取得OKTA新报价。 |
| 状态 | 新增观察，等待开盘确认 |

## 跨期比较与上期剧本复核

相对31日早报：最新完整交易日仍30日，19个ETF收盘轮动与旧反弹失败判断未变。新增Apple中国AI官方时间表、PMI49.3及伊朗条件威胁；Musalem是补核验30日讲话，不是31日新讲话。周五盘后QQQ692.74、SMH526.7142仍低于698.63/535.32，薄量修复不算新常规突破。石油源值修订/时间端点不同，不作为周末上涨。相同规则比较：4641065 95.65%→97.45%（+1.80个百分点）；3215008 70.5%→69.5%（-1.00个百分点）；3501950 0.05%→0.05%（+0.00个百分点）；2176270 10.5%→11.5%（+1.00个百分点）；691340 9.7%→9.55%（-0.15个百分点）；4838928 22.5%→22.5%（+0.00个百分点）；2252540 19%→17.5%（-1.50个百分点）；5401795 10%→5%（-5.00个百分点）；2413330 90.25%→87.9%（-2.35个百分点）；6280962 79%→75%（-4.00个百分点）；6280959 85%→82%（-3.00个百分点）。新增11月2日/30日停火合约分别建基线，不与10月31日拼接；临近到期上升不等于全面风险消失。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-30/20261030T232258.406851Z/evidence.json",
    "baseline_cutoff": "2026-10-30T23:22:47.723020+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.36036964534282845,
      "CL=F": 1.1364796823919,
      "BZ=F": 4.727140988193024,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": 0.0023909054221782355,
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
      "AMD": {
        "change_pct": -0.07487228651862354,
        "from_observed_at": "2026-10-30T23:16:34+00:00",
        "to_observed_at": "2026-10-30T23:59:53+00:00"
      },
      "AMZN": {
        "change_pct": 0.16222286926501628,
        "from_observed_at": "2026-10-30T23:16:13+00:00",
        "to_observed_at": "2026-10-30T23:59:59+00:00"
      },
      "AVGO": {
        "change_pct": 0.07090853472009329,
        "from_observed_at": "2026-10-30T23:16:00+00:00",
        "to_observed_at": "2026-10-30T23:59:58+00:00"
      },
      "CAT": {
        "change_pct": 0.18629855867122735,
        "from_observed_at": "2026-10-30T23:07:09+00:00",
        "to_observed_at": "2026-10-30T23:57:14+00:00"
      },
      "DRAM": {
        "change_pct": 0.2950586488677631,
        "from_observed_at": "2026-10-30T23:15:37+00:00",
        "to_observed_at": "2026-10-30T23:59:50+00:00"
      },
      "GLD": {
        "change_pct": 0.0702444506883948,
        "from_observed_at": "2026-10-30T23:16:23+00:00",
        "to_observed_at": "2026-10-30T23:59:50+00:00"
      },
      "GLW": {
        "change_pct": 0.048531909730642475,
        "from_observed_at": "2026-10-30T23:11:34+00:00",
        "to_observed_at": "2026-10-30T23:59:31+00:00"
      },
      "GOOGL": {
        "change_pct": 0.028784648187629713,
        "from_observed_at": "2026-10-30T23:16:30+00:00",
        "to_observed_at": "2026-10-30T23:59:41+00:00"
      },
      "INTC": {
        "change_pct": -0.07622479384656877,
        "from_observed_at": "2026-10-30T23:16:44+00:00",
        "to_observed_at": "2026-10-30T23:59:56+00:00"
      },
      "LLY": {
        "change_pct": -0.2461212976022531,
        "from_observed_at": "2026-10-30T23:11:49+00:00",
        "to_observed_at": "2026-10-30T23:59:03+00:00"
      },
      "META": {
        "change_pct": 0.07541513775934927,
        "from_observed_at": "2026-10-30T23:14:56+00:00",
        "to_observed_at": "2026-10-30T23:59:56+00:00"
      },
      "MSFT": {
        "change_pct": 0.011856271393884121,
        "from_observed_at": "2026-10-30T23:15:16+00:00",
        "to_observed_at": "2026-10-30T23:59:12+00:00"
      },
      "MU": {
        "change_pct": 0.18330886586230832,
        "from_observed_at": "2026-10-30T23:15:58+00:00",
        "to_observed_at": "2026-10-30T23:59:54+00:00"
      },
      "NOW": {
        "change_pct": 0.04273504273504258,
        "from_observed_at": "2026-10-30T23:15:59+00:00",
        "to_observed_at": "2026-10-30T23:59:32+00:00"
      },
      "NVDA": {
        "change_pct": 0.09211893046459085,
        "from_observed_at": "2026-10-30T23:16:11+00:00",
        "to_observed_at": "2026-10-30T23:59:57+00:00"
      },
      "ORCL": {
        "change_pct": 0.06417112299466066,
        "from_observed_at": "2026-10-30T23:15:01+00:00",
        "to_observed_at": "2026-10-30T23:59:47+00:00"
      },
      "PLTR": {
        "change_pct": 0.18607677293429603,
        "from_observed_at": "2026-10-30T23:16:09+00:00",
        "to_observed_at": "2026-10-30T23:57:25+00:00"
      },
      "QQQ": {
        "change_pct": 0.07947241067804978,
        "from_observed_at": "2026-10-30T23:16:24+00:00",
        "to_observed_at": "2026-10-30T23:59:55+00:00"
      },
      "SMH": {
        "change_pct": 0.33415879305089824,
        "from_observed_at": "2026-10-30T23:14:13+00:00",
        "to_observed_at": "2026-10-30T23:59:52+00:00"
      },
      "SNDK": {
        "change_pct": 0.48415798611112226,
        "from_observed_at": "2026-10-30T23:16:36+00:00",
        "to_observed_at": "2026-10-30T23:59:57+00:00"
      },
      "SPY": {
        "change_pct": 0.10577533319229282,
        "from_observed_at": "2026-10-30T23:13:48+00:00",
        "to_observed_at": "2026-10-30T23:59:59+00:00"
      },
      "TLT": {
        "change_pct": -0.05557228436362527,
        "from_observed_at": "2026-10-30T23:16:09+00:00",
        "to_observed_at": "2026-10-30T23:59:30+00:00"
      },
      "VRT": {
        "change_pct": -0.16370259267195486,
        "from_observed_at": "2026-10-30T23:15:20+00:00",
        "to_observed_at": "2026-10-30T23:59:27+00:00"
      },
      "XLE": {
        "change_pct": -0.1141226818830221,
        "from_observed_at": "2026-10-30T23:15:06+00:00",
        "to_observed_at": "2026-10-30T23:55:14+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-29"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-29"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-29"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-29"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-29"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-30"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-23"
      },
      "CBOE_VIX": {
        "change": 2.2200000000000024,
        "unit": "index",
        "observation_date": "2026-10-30"
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
      "3215008": {
        "status": "comparable",
        "change_pp": -1.0000000000000009
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 1.8000000000000016
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.15000000000000013
      },
      "2252540": {
        "status": "comparable",
        "change_pp": -1.5000000000000013
      },
      "5401795": {
        "status": "comparable",
        "change_pp": -5.0
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -2.3499999999999965
      },
      "6280962": {
        "status": "comparable",
        "change_pp": -4.0000000000000036
      },
      "6280959": {
        "status": "comparable",
        "change_pp": -3.0000000000000027
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
    "event": "下一常规开盘，已转冬令时：北京时间22:30",
    "date": "2026-11-02T09:30:00-05:00",
    "source": "tc:get_trading_calendar"
  },
  {
    "event": "AMD Q3电话会（11月已进入冬令时）",
    "date": "2026-11-03T17:00:00-05:00",
    "source": "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"
  },
  {
    "event": "Sandisk按8拆1调整交易；不产生额外价值",
    "date": "2026-11-20T09:30:00-05:00",
    "source": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results"
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
    "event": "MSFT债券预定结算；不是已到账",
    "date": "2026-11-04 America/New_York",
    "source": "https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm"
  },
  {
    "event": "PLTR官方预告11月2日盘后财报，具体分钟未核验",
    "date": "2026-11-02 America/New_York",
    "source": "https://investors.palantir.com/news-details/2026/Palantir-Announces-Date-of-Third-Quarter-2026-Earnings-Release-and-Webcast/default.aspx"
  },
  {
    "event": "Apple中国部分AI功能开发者Beta，时刻未定；12月正式版",
    "date": "2026-11-04 Asia/Shanghai",
    "source": "https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/"
  },
  {
    "event": "OKTA纳入S&P500于开盘前生效；KVUE被替换",
    "date": "2026-11-04 America/New_York",
    "source": "https://press.spglobal.com/2026-10-30-Okta-Set-to-Join-S-P-500-Others-to-Join-S-P-MidCap-400-and-S-P-SmallCap-600"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| bea-gdp-q3-advance | Q3实际GDP年化环比3.4%；强增长与月度通胀分别解释。 | 2026-10-29T08:30:00-04:00 | [{"source": "https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026", "published_at": "2026-10-29T08:30:00-04:00", "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| bea-pce-september | 9月PCE同比3.6%、核心3.1%，实际消费环比接近零。 | 2026-10-29T08:30:00-04:00 | [{"source": "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026", "published_at": "2026-10-29T08:30:00-04:00", "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| amzn-q326 | 盘后AWS增长强但TTM现金支出压力大；现金FCF负值不是单季数。 | 缺失 | [{"source": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| sndk-fy27q1 | 盘后业绩及Q2指引增长；宣布8拆1，11月20日调整交易。 | 2026-10-29T16:05:00-04:00 | [{"source": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results", "published_at": "2026-10-29T16:05:00-04:00", "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| intc-q326 | Q4收入指引150–160亿美元；PC弱与数据中心供给约束并存。 | 缺失 | [{"source": "https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000188/q326earningsrelease.htm", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| nvda-nscale-credit-talks | Reuters转述The Information谈判消息且未独立确认，不作已成交担保或负债。 | 缺失 | [{"source": "https://www.boursorama.com/bourse/actualites/selon-information-nvidia-serait-en-pourparlers-pour-apporter-un-soutien-financier-a-l-accord-conclu-entre-nscale-et-anthropic-2f2a778a7b8f5d0b9e87ab8c7f3c9978", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| saudi-houthi-claim | AP转述胡塞声称袭击油设施，实际供应损失未独立确认。 | 缺失 | [{"source": "https://apnews.com/article/c11dac838a072af25ba8d0eb81d01035", "published_at": null, "retrieved_at": "2026-10-30T00:28:00.796032+00:00"}] |
| amzn-10q-20261030 | SEC新增Q3 10-Q；现金FCF与融资租赁仍须桥接，旧Q2估值不可复用。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm", "published_at": null, "retrieved_at": "2026-10-30T12:08:37.599365+00:00"}] |
| xom-q326 | Q3调整EPS4.23，经营现金257亿美元、公司FCF191亿；不等于所有油企同质受益。 | 缺失 | [{"source": "https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results", "published_at": null, "retrieved_at": "2026-10-30T12:08:37.599365+00:00"}] |
| abbv-q326 | Q3收入174.04亿美元、调整EPS3.82，全年调整EPS指引上调至13.95–13.99。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm", "published_at": null, "retrieved_at": "2026-10-30T12:08:37.599365+00:00"}] |
| cvx-q326 | Q3调整EPS5.28、经营现金160亿美元、公司FCF120亿；调整FCF含TCO还贷及出售资产影响。 | 2026-10-30T05:15:00-05:00 | [{"source": "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm", "published_at": "2026-10-30T05:15:00-05:00", "retrieved_at": "2026-10-30T12:08:48.737544+00:00"}] |
| meta-sp-outlook-20261030 | 官方评级行动确认AA−不变、展望稳定转负；发生于盘后，非当日常规下跌的事前催化。 | 2026-10-30T17:01:00-04:00 | [{"source": "https://spratings.spglobal.com/ratings/en/regulatory/ratings-actions", "published_at": "2026-10-30T17:01:00-04:00", "retrieved_at": "2026-10-30T23:22:47.326817+00:00"}] |
| msft-final-terms-20261030 | 30日新FWP列29日定价，本金合计250亿美元，11月4日预定结算；票息期限不同不横比。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm", "published_at": null, "retrieved_at": "2026-10-30T23:22:47.326817+00:00"}] |
| logan-20261030 | 支持本周暂缓但个人认为至少再两次25bp加息；非FOMC承诺。 | 缺失 | [{"source": "https://www.dallasfed.org/news/speeches/logan/2026/lkl261030", "published_at": null, "retrieved_at": "2026-10-30T23:22:47.326817+00:00"}] |
| apple-china-ai-20261031 | Apple官方公布11月4日测试、12月正式发布部分核心AI功能，与千问合作；范围有限并非全部新Siri。 | 缺失 | [{"source": "https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/", "published_at": null, "retrieved_at": "2026-10-31T12:08:07.493709+00:00"}] |
| china-pmi-20261031 | 官方10月制造业PMI49.3，较前月50.1下降0.8个百分点。 | 2026-10-31T09:30:00+08:00 | [{"source": "https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html", "published_at": "2026-10-31T09:30:00+08:00", "retrieved_at": "2026-10-31T12:08:07.493709+00:00"}] |
| iran-response-20261031 | Axios报道伊朗领导层要求若遭美以攻击扩大回应范围；条件威胁不等于攻击已发生。 | 缺失 | [{"source": "https://www.axios.com/2026/10/31/irans-supreme-leader-maximum-response-us-attack", "published_at": "2026-10-31T11:48:31+00:00", "retrieved_at": "2026-10-31T12:08:07.493709+00:00"}] |
| musalem-20261030 | 30日官方讲话倾向很快进一步紧缩，同时认为融资渠道仍健康；本次补核验，个人观点。 | 缺失 | [{"source": "https://www.stlouisfed.org/from-the-president/remarks/2026/remarks-on-us-economy-and-monetary-policy-somc", "published_at": null, "retrieved_at": "2026-10-31T12:08:07.493709+00:00"}] |
| okta-sp500-20261030 | 官方公告OKTA11月4日开盘前纳入S&P500，替换KVUE；不等于盈利上修。 | 缺失 | [{"source": "https://press.spglobal.com/2026-10-30-Okta-Set-to-Join-S-P-500-Others-to-Join-S-P-MidCap-400-and-S-P-SmallCap-600", "published_at": null, "retrieved_at": "2026-10-31T12:08:07.493709+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN418；CME官方矩阵referrer拒绝，未替代为tc温度或加密指数。",
  "未取得30日完整市场成分广度、常规VWAP/首30分钟成交验证；尾盘回升不证明承接可靠。",
  "利率/信用仅29日、金融压力23日、GPR26日，不能确认30日及盘后全部冲击。",
  "期货连续日线与分钟具体合约月未对齐；不把WTI/Brent方向差异直接归因供需。",
  "ETF当期精确份额/拆分桥缺失；ICI至21日、VanEck页面至30日，不把资产变化当净流入。",
  "MSFT/AMZN/GOOGL/META新财报后TTM、净债务、租赁和稀释桥未齐，暂停精确DCF。",
  "UKMTO公开页动态记录未加载，不能把0条当无事故；伊朗多船水雷说法及11月4日军事行动传言未独立核验。",
  "tc本次高影响新闻查询上限50条，Polymarket多组截断；临近到期与低流动性合约质量受限。",
  "H100网页标题7D与日期表不一致，采用30日与23日同为2.90自行计算0%。",
  "NVDA旧官方实录预告11月17日，tc日历列25日，日期冲突尚未取得临近IR最终确认；作为待核验事项。",
  "周末无新常规成交；不能验证周一VWAP或把周五末笔报价归因周六消息。",
  "本次Nasdaq官方检索未取得同日完整广度；第三方样本/口径冲突，未将其当全市场广度。",
  "Apple中国AI未取得量化商业回报；OKTA指数事件已核验，但本次未取得其报价，不虚构事件涨幅。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。",
  "AMZN 估值: 30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。",
  "GOOGL 估值: 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
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
    "url": "https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日新业绩；公司TTM FCF口径"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-reports-fiscal-first-quarter-2027-financial-results",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日16:05EDT财报及拆分"
  },
  {
    "url": "https://www.intc.com/filings-reports/all-sec-filings/content/0000050863-26-000188/q326earningsrelease.htm",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "Q3官方SEC附件"
  },
  {
    "url": "https://www.bea.gov/news/2026/personal-income-and-outlays-september-2026",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日08:30EDT月度数据"
  },
  {
    "url": "https://www.bea.gov/news/2026/gdp-advance-estimate-3rd-quarter-2026",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "29日08:30EDT季度年化数据"
  },
  {
    "url": "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "11月3日17:00ET，冬令时"
  },
  {
    "url": "https://investors.palantir.com/news-details/2026/Palantir-Announces-Date-of-Third-Quarter-2026-Earnings-Release-and-Webcast/",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "官方搜索结果确认11月2日盘后，正文动态无精确分钟"
  },
  {
    "url": "https://www.boursorama.com/bourse/actualites/selon-information-nvidia-serait-en-pourparlers-pour-apporter-un-soutien-financier-a-l-accord-conclu-entre-nscale-et-anthropic-2f2a778a7b8f5d0b9e87ab8c7f3c9978",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "Reuters转述且未独立核验"
  },
  {
    "url": "https://apnews.com/article/c11dac838a072af25ba8d0eb81d01035",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "胡塞声称，供应损失未核验"
  },
  {
    "url": "https://www.cmegroup.com/fedwatch",
    "checked_at": "2026-10-30T00:28:00.796032+00:00",
    "note": "页面可读，矩阵失败"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日SEC新10-Q全文核验"
  },
  {
    "url": "https://investor.exxonmobil.com/company-information/press-releases/detail/1213/exxonmobil-announces-third-quarter-2026-results",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日新官方业绩"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/cvx-20261030.htm",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日SEC8-K，业绩附件另核验"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1551152/000155115226000033/abbv-20260930xexhibit991.htm",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "30日SEC官方业绩附件"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-10-30T12:08:37.599365+00:00",
    "note": "矩阵null referrer错误，概率缺失"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/93410/000009341026000196/a09302026ex9918-k.htm",
    "checked_at": "2026-10-30T12:08:48.737544+00:00",
    "note": "官方Q3业绩附件，发布05:15中央夏令时间；现金流非同质"
  },
  {
    "url": "https://www.dallasfed.org/news/speeches/logan/2026/lkl261030",
    "checked_at": "2026-10-30T23:22:47.326817+00:00",
    "note": "官方全文，本人政策观点"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/789019/000119312526439794/d799291dfwp.htm",
    "checked_at": "2026-10-30T23:22:47.326817+00:00",
    "note": "SEC新定价表，计算合计本金250亿美元"
  },
  {
    "url": "https://spratings.spglobal.com/ratings/en/regulatory/ratings-actions",
    "checked_at": "2026-10-30T23:22:47.326817+00:00",
    "note": "官方评级行动：17:01EDT，AA−不变、展望转负"
  },
  {
    "url": "https://www.streetinsider.com/Reuters/S%26P%2BGlobal%2Brevises%2Boutlook%2Bon%2BMeta%2Bto%2Bnegative%2Bon%2Bcashflow%2Bconcerns/27267040.html",
    "checked_at": "2026-10-30T23:22:47.326817+00:00",
    "note": "现金支出与经营现金流不确定性的报道；与官方评级行动交叉"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "本次重查：ICI截至21日，H10030日2.90；VanEck30日NAV522.76资产664.4亿，仍缺份额桥。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "本次重查：ICI截至21日，H10030日2.90；VanEck30日NAV522.76资产664.4亿，仍缺份额桥。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "本次重查：ICI截至21日，H10030日2.90；VanEck30日NAV522.76资产664.4亿，仍缺份额桥。"
  },
  {
    "url": "https://www.ukmto.org/recent-incidents",
    "checked_at": "2026-10-30T23:22:47.326817+00:00",
    "note": "动态事件未加载，不等于无事故"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ILMN",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-10-30T23:16:46.776004+00:00",
    "note": "30日盘后独立实际分钟时间；未有成交的时段不可称实时"
  },
  {
    "url": "https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "官方正文已读取，发布日期31日，精确分钟未知"
  },
  {
    "url": "https://www.stats.gov.cn/sj/zxfbhjd/202610/t20261031_1965718.html",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "官方31日09:30，制造业49.3"
  },
  {
    "url": "https://www.stlouisfed.org/from-the-president/remarks/2026/remarks-on-us-economy-and-monetary-policy-somc",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "官方30日讲话，本次复核"
  },
  {
    "url": "https://www.axios.com/2026/10/31/irans-supreme-leader-maximum-response-us-attack",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "可访问搜索摘录，尚未取得独立官方全文；条件威胁"
  },
  {
    "url": "https://press.spglobal.com/2026-10-30-Okta-Set-to-Join-S-P-500-Others-to-Join-S-P-MidCap-400-and-S-P-SmallCap-600",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "官方30日公告，11月4日开盘前生效"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "入口可读，矩阵referrer错误"
  },
  {
    "url": "https://www.nasdaq.com/market-activity",
    "checked_at": "2026-10-31T12:08:07.493709+00:00",
    "note": "未取得同日广度"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ILMN",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-10-31T12:02:18.014317+00:00",
    "note": "周六抓取周五最后分钟；不是周末新成交"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
