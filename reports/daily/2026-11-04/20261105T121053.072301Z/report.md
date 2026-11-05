# 每日交易总结 · 2026-11-04

## 一分钟读懂 · Agent 摘要

### 当前判断

大盘修复与半导体下跌同时发生，暂不升级为全面可靠反弹。金融、医疗、消费继续优先观察回踩承接，AI硬件先等止跌。

### 与上次相比

相对早报，没有新增完整日线；盘前SMH、MU、SNDK已低于4日低点，高通财报后的下跌扩大。英国央行刚加息25基点至4%。

### 最重要的信号

- SPY盘前仍在昨日收盘附近上方，QQQ偏弱、SMH约492.5，低于早报497.33失效线；这是盘前警报，仍须常规时段确认。
- VIX约16.8并不代表个股风险解除；油价反弹，英国加息提醒通胀压力尚未消失。
- Coherent官方收入增50%、毛利率改善，是AI需求并未全面消失的反证；重点在增长能否兑现为现金及被价格接受。

### 接下来观察

- 开盘后30–60分钟看SPY守762.64、QQQ守687.87、RSP维持相对强；回踩守住、收盘延续比跳空更重要。
- SMH须收回497.33及504.27，并出现低点抬升；未达成前不把下跌中的单次拉升当趋势反转。
- 今晚21:30北京时间Cigna电话会，明晚21:30美国就业；11月10日CPI。数据公布后重评。

### 不要忽略

当前是盘前、报价异步；缺全成分广度、当期申赎和CNN指数。四家AI公司估值底稿仍不全。

## 研究结论

11月5日晚报：大盘修复尚在，半导体盘前跌破前低；英国加息与明晚就业数据要求保留验证空间。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-04 → 2026-11-04（纽约交易日） |
| 截止·纽约 | 2026-11-05T07:08:55.737695-05:00 |
| 截止·北京 | 2026-11-05T20:08:55.737695+08:00 |
| 实际生成时间 | 2026-11-05T12:08:57.970427+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-05 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-04/20261104T232659.811257Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-05T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219847 | 已校验接入 | https://gamma-api.polymarket.com/events/1219847 | 2026-11-05T12:01:00.356445+00:00 / 2026-11-05T12:01:00.356445+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-11-05T12:01:01.193742+00:00 / 2026-11-05T12:01:01.193742+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-11-05T12:01:03.553978+00:00 / 2026-11-05T12:01:03.553978+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1038648 | 未接入 | 缺失 |  /  | 没有可核验的活跃Yes合约 |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-11-05T12:01:04.150951+00:00 / 2026-11-05T12:01:04.150951+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1103684 | 已校验接入 | https://gamma-api.polymarket.com/events/1103684 | 2026-11-05T12:01:04.821683+00:00 / 2026-11-05T12:01:04.821683+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 199777 | 已校验接入 | https://gamma-api.polymarket.com/events/199777 | 2026-11-05T12:01:04.954397+00:00 / 2026-11-05T12:01:04.954397+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1308738 | 已校验接入 | https://gamma-api.polymarket.com/events/1308738 | 2026-11-05T12:05:32.129160+00:00 / 2026-11-05T12:05:32.129160+00:00 | Gamma observation; rule and expiration retained |
| 1120074 | 已校验接入 | https://gamma-api.polymarket.com/events/1120074 | 2026-11-05T12:05:33.035036+00:00 / 2026-11-05T12:05:33.035036+00:00 | Gamma observation; rule and expiration retained |
| 1120075 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |

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
| request.38906ddc2d63 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |

## 决策指标：趋势、相对强弱、波动与宏观

| ID | 数值 | 单位 | 观测日/时间 | 质量 | 定义 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| prices.SPY.value | 766.81 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 1.65 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.71 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -1.34 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -0.24 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 767.57 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.45 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 727.12 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.10 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | 0.05 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 5.46 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 9.44 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.23 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -1.58 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.58 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 691.95 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 0.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -4.64 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -8.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -3.59 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -0.68 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -3.93 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -7.34 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -3.35 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 717.42 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 723.30 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 679.44 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -3.55 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -4.33 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 1.84 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 14.70 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.12 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -8.91 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.51 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 284.02 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 1.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 0.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 2.28 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -5.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.14 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.68 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 3.62 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -5.15 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.44 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 282.99 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.97 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 2.37 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | 0.36 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 2.18 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 4.00 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -6.66 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.44 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 223.33 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 1.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 2.71 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 6.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 1.58 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 0.20 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 3.43 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 7.38 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 1.82 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 216.32 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.72 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.90 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 3.24 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 4.01 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 7.94 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.31 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.03 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.81 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 372.49 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 3.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -0.27 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -0.90 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -7.10 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | 2.03 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 0.44 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | 0.44 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -6.86 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 373.55 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 386.88 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 411.98 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -0.28 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -3.72 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -9.58 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 6.27 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -12.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.35 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,073.00 | USD_per_troy_ounce | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 3.37 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | 0.53 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -1.63 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -8.29 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 1.71 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 1.24 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -0.30 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -8.05 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,089.96 | USD_per_troy_ounce | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,253.00 | USD_per_troy_ounce | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,509.31 | USD_per_troy_ounce | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -0.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -4.23 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -9.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 80.59 | USD_per_troy_ounce | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -13.30 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.04 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 88.12 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -8.29 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -14.26 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -0.18 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 5.91 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -9.95 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -13.55 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 1.16 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 6.15 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 98.11 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.15 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 86.85 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -10.19 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -7.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 1.46 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 5.26 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -16.73 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.37 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 94.62 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -8.67 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -17.95 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -5.57 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 6.42 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -10.32 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -17.24 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -4.23 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 6.66 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 109.04 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 103.82 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.01 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -13.22 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -8.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 1.73 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.48 | USD_per_barrel | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 5.79 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -19.57 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.66 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.76 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.80 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.95 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 5.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.14 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -0.85 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.66 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 7.31 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 0.10 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.32 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.40 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.47 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 1.80 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.69 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.05 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.77 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.94 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.67 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.11 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.90 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.38 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.55 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | -0.48 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 2.70 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -2.03 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.16 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 0.86 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 2.94 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.65 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.95 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | -0.34 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 0.88 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.40 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.10 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.35 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.79 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.65 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.52 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.70 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.44 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.95 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.62 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 1.78 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -1.73 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.16 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.87 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 78.19 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.47 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.46 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.32 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.42 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.47 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 1.29 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.50 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.75 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.35 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.99 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.90 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 1.13 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 3.69 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -0.75 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.49 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.91 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 106.21 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.57 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.61 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.61 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.59 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.80 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.31 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 16.61 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -20.26 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | -1.77 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 10.15 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 14.16 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -21.91 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | -1.06 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 11.49 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 14.65 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 17.65 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.42 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.29 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | -5.89 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 1.13 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | -9.18 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.84 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 17.11 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -21.47 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-04 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 18.80 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -11.61 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | -2.19 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 6.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | -0.58 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -13.26 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | -1.47 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 7.43 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | -0.34 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 19.40 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.70 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.52 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | -3.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 0.52 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -8.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.56 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 8.28 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -12.96 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-04 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 90.41 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -15.82 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | -6.42 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 8.69 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | -0.54 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -17.47 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | -5.71 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 10.03 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | -0.30 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 98.36 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 92.56 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.75 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | -8.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | -2.32 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -8.44 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 12.44 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 13.76 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -18.16 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-04 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 93.88 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -6.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -0.71 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -10.76 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 24.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -7.74 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 0.00 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -9.18 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 24.97 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 99.86 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 91.83 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 78.15 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -5.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 2.24 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 20.13 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 4.43 | index | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 4.72 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -17.36 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-04 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 200.13 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -3.17 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -7.08 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -15.72 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -7.88 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -4.83 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -6.37 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -14.38 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -7.64 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 216.12 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 221.15 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.39 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -7.40 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -9.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -2.08 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.51 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 3.25 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -16.35 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.48 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 555.80 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | 6.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | 4.67 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 4.92 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 10.53 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 5.03 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 5.38 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 6.25 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 10.77 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 530.96 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 515.34 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 437.96 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 4.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 7.85 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 26.91 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 15.03 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.70 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 2.27 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 266.03 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 6.12 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 4.49 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 2.35 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -2.29 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 4.47 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 5.20 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 3.69 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -2.05 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.13 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 253.89 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.67 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 4.68 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 4.78 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 9.18 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 9.34 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -4.34 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 2.17 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 288.93 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 3.18 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -11.07 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -17.57 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -15.91 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 1.53 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -10.36 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -16.23 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -15.67 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 324.07 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 335.20 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 339.67 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -10.84 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -13.80 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -14.94 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 10.66 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.69 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -19.13 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.47 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 630.00 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | 1.44 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | 2.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -12.66 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 5.24 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -0.21 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 3.57 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -11.32 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 5.48 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 673.89 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 673.39 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.36 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -6.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -6.44 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -0.22 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 22.37 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.55 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -18.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.38 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 48.42 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -9.90 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -24.26 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -45.26 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -46.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -11.55 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -23.55 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -43.92 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -46.15 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 63.01 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 77.26 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 90.65 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -23.15 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -37.33 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -46.59 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.96 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 12.30 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -55.05 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.97 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 795.23 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -7.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -19.12 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -26.90 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -8.42 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -8.65 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -18.41 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -25.56 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -8.18 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 914.90 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 972.08 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 753.73 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -13.08 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -18.19 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 5.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 51.04 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 6.42 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -27.52 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.33 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 45.11 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -5.31 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -16.65 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -24.83 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -11.36 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -6.96 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -15.94 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -23.49 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -11.12 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 49.87 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 55.38 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-04 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -9.54 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -18.55 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-04 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.83 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 6.28 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -29.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.25 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 205.55 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -12.89 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -15.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -16.61 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -27.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -14.54 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -14.68 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -15.27 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -26.80 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 220.72 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 240.45 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.14 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -6.87 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -14.52 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -24.19 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 16.53 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 8.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -30.03 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.76 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 176.50 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -0.01 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -7.59 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -12.36 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -5.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -1.66 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -6.88 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -11.02 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -4.80 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 187.00 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.26 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.71 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -5.62 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -6.74 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 4.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.88 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.76 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -12.62 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.29 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 63.52 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -4.74 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -7.20 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 0.25 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 4.87 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -6.39 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -6.49 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 1.59 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 5.11 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 67.46 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.97 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.44 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -5.85 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -2.24 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 8.70 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.73 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.72 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -9.28 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 2.12 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 59.20 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 3.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 5.47 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 10.14 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 2.78 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 1.86 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 6.18 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 11.48 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 3.02 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 55.95 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.88 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.48 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 5.81 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 5.95 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 10.70 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.83 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.54 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 169.46 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -1.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 0.58 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | 0.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -8.50 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | -2.74 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 1.29 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 2.30 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -8.26 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.13 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 169.99 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.67 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 0.79 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -0.31 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -1.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.86 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.69 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -8.90 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.54 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 189.66 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 3.06 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 5.53 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 12.35 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 13.32 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 1.41 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 6.24 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 13.69 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 13.56 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 178.44 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 172.67 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 158.15 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 6.29 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 9.84 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 19.92 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.20 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.69 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.70 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 91.94 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 3.36 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 5.87 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 12.53 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 9.27 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 1.71 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 6.59 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 13.87 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 9.51 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 87.37 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.65 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.73 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 5.23 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 8.61 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 9.81 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.59 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.73 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.46 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 122.33 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 4.26 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 6.07 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 9.85 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 2.82 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 2.61 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 6.78 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 11.19 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 3.06 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 114.73 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.22 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.14 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 6.62 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 8.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 6.24 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.20 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.80 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 2.41 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 104.96 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 3.47 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 1.76 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -5.66 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -5.36 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 1.82 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 2.48 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -4.32 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -5.12 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 107.01 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.98 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.17 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -1.92 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -4.57 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -6.43 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.98 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.88 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -8.53 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.59 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.61 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.44 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 2.64 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 0.69 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -1.21 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 3.35 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 7.32 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 0.93 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.37 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.67 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.82 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.93 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.65 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.48 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.61 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -0.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.56 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 45.12 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 3.32 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 7.10 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 11.22 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | 3.22 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 1.67 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 7.81 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 12.55 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 3.46 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 42.45 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.46 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.82 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 6.28 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 6.27 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 5.37 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.68 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.51 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 53.90 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 2.49 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 3.93 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 10.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 1.71 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 0.84 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 4.65 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 11.38 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 1.95 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 51.30 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.90 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.81 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 5.07 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 5.89 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 6.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.79 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.47 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.98 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 504.27 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -2.75 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -11.17 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -19.32 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -11.98 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -4.40 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -10.46 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -17.98 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -11.74 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 551.88 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 569.98 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 521.22 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -8.63 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -11.53 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -3.25 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 21.16 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 4.20 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -20.45 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 1.36 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 103.56 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 0.88 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -7.46 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -5.72 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -0.35 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.78 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -6.75 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -4.38 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | -0.11 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.13 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 107.00 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.02 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -4.23 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -3.22 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 10.14 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.16 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.05 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -8.09 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.47 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 179.29 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -6.39 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -10.52 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -4.75 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 0.92 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -8.04 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -9.81 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -3.42 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 1.16 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 197.11 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.55 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 170.46 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -9.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -6.40 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 5.18 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 5.95 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.32 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -12.48 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 2.43 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 366.06 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -4.95 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -10.52 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -4.06 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -11.86 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -6.60 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -9.81 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -2.72 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -11.62 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 390.67 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 399.37 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.45 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -6.30 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -8.34 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -8.13 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 13.30 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 3.63 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -16.15 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 2.33 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 212.84 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -1.54 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 2.45 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 4.54 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -15.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -3.19 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 3.17 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 5.88 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -15.17 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 207.85 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 213.42 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.20 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 2.40 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -0.27 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -6.73 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 5.24 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.46 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -15.85 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.32 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 28.92 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -3.31 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -6.10 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -11.34 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -15.95 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -4.96 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -5.39 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -10.00 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -15.72 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 30.48 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.56 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.41 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -5.11 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -8.37 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -10.76 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.84 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.91 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -17.04 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 1.39 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 74.13 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 1.72 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 2.80 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 7.61 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -2.94 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 0.06 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 3.51 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 8.95 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -2.70 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 71.19 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.76 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.45 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 4.14 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 3.30 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 5.22 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.46 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.97 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -4.33 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.17 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 156.69 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 0.46 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -9.07 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -8.25 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -2.73 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -1.20 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -8.35 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -6.91 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -2.49 | pp | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 165.45 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.57 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.00 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -5.29 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -4.79 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 14.37 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.02 | USD_per_share | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.20 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -10.41 | percent | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 2.03 | ratio | 2026-11-04 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.61 | percent | 2026-11-03 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.40 | percentage_points | 2026-11-03 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.93 | percentage_points | 2026-11-03 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.95 | percent | 2026-11-03 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.65 | percent | 2026-11-03 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.26 | percent | 2026-11-04 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.52 | index | 2026-10-30 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 16.61 | index | 2026-11-04 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 97.67 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 113.60 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 94.75 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 137.64 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 164.04 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AAPL.value | 352.39 | USD_per_share | 2026-11-05T12:01:02+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| quotes.AMD.value | 471.50 | USD_per_share | 2026-11-05T12:01:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.AMZN.value | 269.83 | USD_per_share | 2026-11-05T12:00:59+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.ARM.value | 183.00 | USD_per_share | 2026-11-05T12:00:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ARM |
| quotes.AVGO.value | 319.56 | USD_per_share | 2026-11-05T12:00:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.BABA.value | 110.17 | USD_per_share | 2026-11-05T12:00:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BABA |
| quotes.CAT.value | 586.71 | USD_per_share | 2026-11-05T12:00:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.CEG.value | 243.65 | USD_per_share | 2026-11-05T12:00:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.CI.value | 315.88 | USD_per_share | 2026-11-05T12:00:26+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CI |
| quotes.COHR.value | 191.01 | USD_per_share | 2026-11-05T12:00:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COHR |
| quotes.COIN.value | 151.20 | USD_per_share | 2026-11-05T11:53:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COIN |
| quotes.COP.value | 138.88 | USD_per_share | 2026-11-05T11:52:31+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COP |
| quotes.CRWV.value | 46.88 | USD_per_share | 2026-11-05T12:00:45+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| quotes.CVX.value | 218.58 | USD_per_share | 2026-11-05T11:41:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.DRAM.value | 42.97 | USD_per_share | 2026-11-05T12:01:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GDX.value | 87.07 | USD_per_share | 2026-11-05T12:00:12+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GDX |
| quotes.GEV.value | 814.00 | USD_per_share | 2026-11-05T12:00:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 378.35 | USD_per_share | 2026-11-05T12:00:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 115.04 | USD_per_share | 2026-11-05T12:00:24+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 291.96 | USD_per_share | 2026-11-05T12:00:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 103.56 | USD_per_share | 2026-11-05T12:00:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.INTC.value | 57.06 | USD_per_share | 2026-11-05T12:01:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.IWM.value | 285.37 | USD_per_share | 2026-11-05T12:00:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.LITE.value | 603.33 | USD_per_share | 2026-11-05T12:00:22+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LITE |
| quotes.LLY.value | 1,430.95 | USD_per_share | 2026-11-05T12:00:54+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| quotes.META.value | 638.36 | USD_per_share | 2026-11-05T12:00:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MRVL.value | 153.82 | USD_per_share | 2026-11-05T12:00:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MRVL |
| quotes.MSFT.value | 558.28 | USD_per_share | 2026-11-05T12:00:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 769.02 | USD_per_share | 2026-11-05T12:01:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 109.20 | USD_per_share | 2026-11-05T12:00:30+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 198.13 | USD_per_share | 2026-11-05T12:01:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.ORCL.value | 123.30 | USD_per_share | 2026-11-05T12:00:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.PLTR.value | 167.87 | USD_per_share | 2026-11-05T12:01:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.QCOM.value | 156.66 | USD_per_share | 2026-11-05T12:00:57+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QCOM |
| quotes.QQQ.value | 688.19 | USD_per_share | 2026-11-05T12:00:54+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 224.20 | USD_per_share | 2026-11-05T11:54:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 492.50 | USD_per_share | 2026-11-05T12:00:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 993.80 | USD_per_share | 2026-11-05T12:01:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 768.12 | USD_per_share | 2026-11-05T12:00:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 538.00 | USD_per_share | 2026-11-05T11:54:23+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TAN.value | 46.52 | USD_per_share | 2026-11-05T11:33:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TAN |
| quotes.TLT.value | 81.83 | USD_per_share | 2026-11-05T12:00:39+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 199.52 | USD_per_share | 2026-11-05T12:01:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 63.90 | USD_per_share | 2026-11-05T12:00:00+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 59.89 | USD_per_share | 2026-11-05T12:00:47+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.XLI.value | 169.70 | USD_per_share | 2026-11-05T09:02:25+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLI |
| quotes.XLV.value | 190.84 | USD_per_share | 2026-11-05T11:41:43+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.XOM.value | 170.75 | USD_per_share | 2026-11-05T11:36:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| latest.BZ_F.value | 96.64 | USD/barrel | 2026-11-05T11:51:00+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| latest.CL_F.value | 89.23 | USD/barrel | 2026-11-05T11:51:02+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| latest.DX-Y.NYB.value | 101.62 | index points | 2026-11-05T11:51:09+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |
| latest.ES_F.value | 7,733.75 | index points | 2026-11-05T11:51:02+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| latest.GC_F.value | 4,141.90 | USD/troy_oz | 2026-11-05T11:51:05+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| latest.NQ_F.value | 28,432.25 | index points | 2026-11-05T11:51:01+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| latest.TNX.value | 4.89 | percent | 2026-11-04T19:59:00+00:00 | stale | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| latest.VIX.value | 16.80 | index points | 2026-11-05T11:46:01+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |
| intraday.SPY.minute_close_vwap | 767.08 | USD/share | 2026-11-04T16:00:00-05:00 | ok | 2026-11-04 09:30–16:00 America/New_York，390根1分钟收盘价乘分钟量加权，剔除延长时段；非逐笔VWAP，不等同交易终端精确值 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| intraday.QQQ.minute_close_vwap | 694.07 | USD/share | 2026-11-04T16:00:00-05:00 | ok | 2026-11-04 09:30–16:00 America/New_York，390根1分钟收盘价乘分钟量加权，剔除延长时段；非逐笔VWAP，不等同交易终端精确值 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| intraday.SMH.minute_close_vwap | 506.04 | USD/share | 2026-11-04T16:00:00-05:00 | ok | 2026-11-04 09:30–16:00 America/New_York，390根1分钟收盘价乘分钟量加权，剔除延长时段；非逐笔VWAP，不等同交易终端精确值 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| intraday.RSP.minute_close_vwap | 222.61 | USD/share | 2026-11-04T16:00:00-05:00 | ok | 2026-11-04 09:30–16:00 America/New_York，390根1分钟收盘价乘分钟量加权，剔除延长时段；非逐笔VWAP，不等同交易终端精确值 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| intraday.XLF.minute_close_vwap | 58.72 | USD/share | 2026-11-04T16:00:00-05:00 | ok | 2026-11-04 09:30–16:00 America/New_York，390根1分钟收盘价乘分钟量加权，剔除延长时段；非逐笔VWAP，不等同交易终端精确值 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| intraday.XLV.minute_close_vwap | 188.74 | USD/share | 2026-11-04T16:00:00-05:00 | ok | 2026-11-04 09:30–16:00 America/New_York，390根1分钟收盘价乘分钟量加权，剔除延长时段；非逐笔VWAP，不等同交易终端精确值 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 12.46002197265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3525937760838547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3074450709506857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2770405154269526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.6112516669345314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.8361203926653302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.608676524279796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9345990674291325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.6152397080243954,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.5204986572265398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.321505737304733,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.05594482421872726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.37881713867182043,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.47240600585939774,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.8971679687500682,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.6898965887535256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.2830215355965948,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.6184915139509704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.6678145140354808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.6461599945608807,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.0342594645269765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9178597586495538,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.3450055803571423,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.10134737965689022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.3123997145771815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.599304514646005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.7059517912453406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7530485811684865,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8194967664355027,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.66998291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -33.65997314453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3581315460634338,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.36881820201766224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.34831900523174486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.695384399969504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1100267989578647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.767075535484956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2498924493659187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.9357377245495817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.9944622300204209,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.9386268689330235,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.9287215101952078,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.0841327330349735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7260935937074651,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.15839901120516,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.6847066180632138,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.3204980165251863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.288998413085892,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.052496337890602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.36060302734381366,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.7927355957031068,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.42977416992187045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.8888616943360148,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3656194474656824,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.613319955270954,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9693640380721185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.405606455142241,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9178464414630882,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.251773998298415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.15571376255580383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.761426653180804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0020501183756906904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4790914755107645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8780221606973235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.430926247857891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6185910375681885,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6878761469264354,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.22998046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.72998046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2789852796974088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1156615825084426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.109712233712079,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.7692053941086963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.8267592626909366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0523253396149235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0952386303541228,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1329676123349888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.07360849638644584,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.19178348844224313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.16732828171487357,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.1579537271741649,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9906388700256064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.6610018638947195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.8393604370750092,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7482073203593842,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3159988403320426,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.16650085449219887,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.28861083984372726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.7272308349609489,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.11604621887209987,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4839162445068723,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4096741187415551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9231208611521824,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5954644673207952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5676805069924526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4797042226689427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8056387460210646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.1457148960658481,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4949972970145087,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.030803254396468915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.16231540676166656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3900908290691127,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8971485426902293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.723679681795892,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6913939482398898,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.07000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.9000091552734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.18355015915378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.8976279520419137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9135993577535482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.3488641282405576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.780848151083659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5210343421120598,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.638311480945076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.4769238692065376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8309563830699251,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.590182881091228,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6365588423265955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.960115795175089,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9447277584183285,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.129710866391855,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.2962875864840564,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.092163577230933,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6364997863769588,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.406999206542963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.04781005859376819,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.053034362792971024,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.14783729553224134,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6074214172363384,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5823562507682576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5964478290280137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.872763556882595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.772789440158685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.8913801534615526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.5422146799169987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0935712541852678,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.36142948695591515,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.023475952048851,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.1381608320014962,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2056420787635136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.0302058862213146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.62292158075412,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.841041104660199,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 13.22998046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.02001953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.343419760669498,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.3521647620892825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.2242743532358675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.162455904567694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.11741300544567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0228018118036863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.651266650603368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.9267385156959955,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.9908259845856433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.0447196911385968,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.947233837808915,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7737075715022255,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.2812926127803395,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.6314783360834824,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.7166675831742362,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.3114988076716,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.16950073242185226,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.1425003051757585,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.1116003417968727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.789400024414078,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.32370010375979064,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.55835006713869,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5853142153800643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8236158779369118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.6857338667016677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1597825647089106,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.2797966455629712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.09405785633893515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.484283447265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1407078334263394,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.07284118521982408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.30999695176935127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.0906114052344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.23828334473277124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6412430140563288,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.19715506692001195,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 132.60009765625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 21.39990234375,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.100738546412586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.9296157293337353,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.8217635163629193,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.8992659566407286,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.256916726929605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.591893425463864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.556144509670034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.856278015568783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.748144770328731,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6221706583830495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.5447230009359667,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.51051762357526,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.420796334264274,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.20056994974366,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.621545442240901,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.241038307544389,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.385009765625,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -46.79499511718723,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.429999999999382,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -65.5259960937492,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.4639990234372817,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.532001953125473,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.3217593640739396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.6438210935674102,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.387794962321089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.948642618345942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.007662030625813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8027750463235463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.514264787946416,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 11.535714285714278,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.04797722317658293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.2742687378124862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.8226000078577353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.45553031703047253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.07560574173582912,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.09975858121832704,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.969993591308594,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.659996032714844,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.910719530280086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.177181156283723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.449652745000659,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -20.05863089599855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.6163820429766655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.850780101360504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.08397380721928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -29.73388950813807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.26331330636394,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.484626227234408,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.72669326042761,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -19.44737922906402,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.452502435641996,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.242103577080709,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -13.018572874648413,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -29.118649800113673,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.007999801635733661,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7829998016357393,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.11520004272460938,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1739999389648403,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.13890001296996957,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9232500076293917,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.11529498502107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.880923732054665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.49822267033359,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.755764987539624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.353914209781845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.151111418471945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.37714331490652864,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9478579929896762,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8873186345730106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7731634512861412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.5309396706160445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.85240081174507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.08321898100765868,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.36328766462941786,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.979995727539062,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -20.699996948242188,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.5512194946323,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.932440781683216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.923004271156486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -23.92321614434899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.571438273013698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.956861154129577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.680828365179519,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -38.890275070486545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.903813270716157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.239885852633904,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.200044786583438,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -23.311964477414456,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.40755866567903,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.348184629849781,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -13.615427432608652,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -38.27503536246215,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.2789997100829993,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4924999237060632,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.12080001831054688,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4993998718261707,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.14850002288818587,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0535500144958547,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.993200333244776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -20.452044211604825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.765586167530715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -21.56543954767558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.833371365394106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -23.677135177059384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6042856488909045,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.6878569466727122,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0851683424874219,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.5029508136561613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.633454415275386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.3687183644196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.14280482496381253,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.103402525971367,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6500015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7700042724609375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5599814204619422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.585407475552414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5877565712004604,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.01604402182375786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0193667351740432,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4289755655228165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6369384045838089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2975434919689444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.20738764437808754,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.27796240460172816,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3107160557735078,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6272956887582892,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.8167536574912866,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.037652089802613,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.2976606628453236,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.9127831999933398,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.23050003051757528,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.059999847412115,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.027827453613284092,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.11704010009765398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.011532974243166905,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.21394008636474382,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5186423675812124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.3899431236361828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8433156513125706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8108255911683626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7921054088316559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6731376961254032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.05499976021902897,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.03214263916015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.07534214097657299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.048624472719735023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7817086937050077,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5337450699075763,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3178211185633446,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.3149423474379166,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.1100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.15999984741210938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.5518375850361967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.17313302810956221,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.1728351437504938,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.0346764223977067,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.8627230692938581,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.4900890901544783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.3909048071693677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.4952387127324931,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.9044313611200514,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.480578099060248,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.4498756591774464,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.4234247554631754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.6988434619591883,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1185874341253177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.3255038745985006,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.12000099529190233,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.007000064849851384,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.006500053405762429,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.019199981689453693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.1064000320434566,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.008450002670286949,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.040799999237059126,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.35518892206420905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.5742198618040373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.45191120990055733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.9367175579847009,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.4249613484193171,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.7244646857058612,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0014284678867884926,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.012857028416224894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.006264214547463454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.04229708541150512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.377619682528918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.5492614212897151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.08114167259000005,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.2954660722495506,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5399932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.06999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5844166597066991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7143615030337558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7087453730778015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.8826218838754007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8158225789783202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.49873881789894714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6461356321943224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.47550742037760774,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7681771163771556,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.59308356791693,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.5682951423491511,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.2713702169408694,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.02029781368701,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.109937706380849,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.28846343523481,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.1397322876467877,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.016999816894525566,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.05799980163574503,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.03928802490234773,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.010661315917971592,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.00097148895264354,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.29808002471922634,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6778801781634147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.16637514715274193,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7432575975591327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.10352961997893706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6918383874932266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.46927064533448526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0121427263532366,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.027857099260602702,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.012832975267834223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.03628118530673219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6793701663217688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.5223808526957807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5422664193982893,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.132503648787345,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.43000030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7423791644475264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9725444454438015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9692736750688935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.42006946188368754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8037399417610613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.061489791631474944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7111821831890297,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6961713120304802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.6102146116363283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.33490062550688426,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.3077668403580591,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.19118220505084382,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.0323804509042689,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.670166315911271,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.2234168842401028,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3114110200548756,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.12000007629394815,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5244998931884766,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.03826568603516023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.09129104614257244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.01025588989257642,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.33308158874513083,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6373438817775412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.09674337852978443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7874030520620967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.32575420655789333,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7438448516820628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0965975754573245,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.010714394705636177,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.007856641496930772,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.014735341168178095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.005129021069495865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7329900438793224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.01790456130347229,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.31384573816578776,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.27539503281279853,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.219999313354492,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.2999992370605469,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -18.74623730797036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.77749970382607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -20.666784193032317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.152987783888239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -28.628254743039424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.657523006060596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -22.163913112072176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.200460345281212,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -20.09883108405421,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.084944774776755,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -21.943824708459267,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.541736116953708,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -30.464375135704753,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 9.266199530340392,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -23.5357004205066,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 8.265743980607475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.07650003433227681,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8950000286102302,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.028000011444088813,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.35120000839233256,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.004850001335142906,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.05440000534057532,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -24.423796248740235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.817789838877963,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -25.910051687795853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.076151017634699,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -23.105451165740632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.9162854102795155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.18500001089913498,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8278571537562778,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.354706975315043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.199231982661891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -19.952715789447105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.058013091210091,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.470001220703125,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.4200000762939453,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.084827997549672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.824151706182516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.871993691615378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.856164469215041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.483430127577535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4677070322540064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.647043078091812,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.03877399739645737,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.437421773633528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.131596777133202,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.14903420704233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.24491280228051,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -16.319550520242863,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.076383556533802,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.581642145520945,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6540137054208528,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0539999961853006,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5935001373291016,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.011800003051757102,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.17840007781982692,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.012400007247922673,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.02215000152587976,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -13.038685961244967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.291931431569996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -13.277811853481891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.2351587955632866,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.973949819475727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.147905022857543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.1007142748151506,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.44571413312639496,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4353382104531596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.5000072364650894,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.435190634635806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.719062243704688,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -16.98999786376953,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.1999969482421875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -13.040329913917681,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.963661848705467,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.41152358488612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.596290673339368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -21.347966753334013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7237395759738465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -16.634607751863808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.9033174302827165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.392923690001535,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.271106919656152,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -15.688564100313073,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.985039006404836,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -23.184087145999342,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.332416100253643,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -18.569206819292937,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.288077722258321,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.36150016784667116,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.12300071716308,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0948001098632858,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.515000305175775,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.13319999694823537,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.06599998474121094,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -17.675514565165173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.600210616441487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -18.475023532833966,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.435397139443568,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -17.058865596096993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.213246608991218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.841429029192243,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.9921422685895642,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.9603748383162767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.980261999535804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -15.379739002469972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.057961600801921,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.090003967285156,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.6700057983398438,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.703231016610754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.6995768171854224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.8543277524980426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7401956198926918,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2377808841901423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5434795342390437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.379115891549056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.9276781982551014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.055824792694609,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.007021888136109,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.131368267924996,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3514472868272231,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.17081672871926834,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.180919691349759,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -16.02405799980394,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 9.671340988574016,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.5659999847412109,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.8359996795654183,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.39799987792967784,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.4229997253417963,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.17914999008179677,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9597999763488758,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.534521286534188,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.9439392506470536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.106101949383835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.5203000337914236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.086569820205458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.3616635222522646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.06214305332728731,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.5828568594796311,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.22539174048639588,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.5830042079121807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.360919057294268,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.589793844488895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.55999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.465235032151206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.99919990614712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.9185375806228375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.111640706603826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.1185045275685876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.03182268908046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.997601282822071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.620061149470704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.81782880823506,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.3066449770978052,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.19557809604979,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.5003890396692943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.9546249202339165,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.423146164800665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.932200350251204,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.00482144144631,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.8669998168945199,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.661999511718733,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.25363739013670283,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.8456665039062443,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.11237838745117301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.545142517089829,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.2162277088510702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.644115858526742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.8592251030006732,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.5247327516806735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.2652416584283417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.743182903021029,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.09571402413504426,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4607140677315851,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.05695583824572781,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4442789346231417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.742015301776611,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.374351968670121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5788336353820385,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5731792939627017,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 34.80999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 24.78997802734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.9464579474276285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.741737459651365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.614522643022802,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.032469846895237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.485426851200415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.384529479525498,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 7.382998842574473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.5727349107989017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.593864171343774,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.434292388700679,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.33748212759585,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.643721513829769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.649306458535086,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.9932060038052946,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.44839977514534,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.1879746188232962,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3019989013672557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0694976806640852,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2817999267577989,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.182999877929717,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5207270812987872,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7468818664550554,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.314794495480358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.467008589379451,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.502636745668555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.96716747642214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 7.806579538113478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.174764038994084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.017857142857144,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.376432146344866,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.20668145802424442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6979623490963021,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.132858858801525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.2890794299342376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3800774392306194,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8905112192939244,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 15.339996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 11.42999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.059101810863686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.526458620792174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.441586378342156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.450854644101779,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.535744627545402,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.16327530245550115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 7.561084084980174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.933957903784015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.706508034779831,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.219013549841488,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.164545862915203,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 8.06210631103631,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.6996242348800714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.771951826735297,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.626485017551042,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.54919761180841,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.30549926757811363,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.0435005187988224,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.09940002441408069,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.2243997192382778,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.17514999389649688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.2947000885009743,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.917606997902425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.907441403407187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.003293934902887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.983213163214007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 6.221372549742732,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.564231546581676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9892839704241077,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6671404157366077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.1798391301466391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8899996621080564,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.516198547196893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.021695146843319,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.289879825139434,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2083560989646638,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 8.899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -35.96002197265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.80545244456043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.833781718097538,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5805776389773651,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.119988478363126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.8912099257122534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.989152489775048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.718129028731731,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.9905320219411173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4528586684765754,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5263366471468522,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.30353712355041296,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.508736811428594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.055089533046924544,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.38047596549525,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.783529961302598,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.3752923139167237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.0785003662109034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.73899993896481,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.1561425781250136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.250236206054694,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.16222396850588439,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.2088185119628747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5594281962188266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.452925983051872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.942249363535721,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.953662368110072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.659560032986972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.247626411370447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3514273507254462,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6078578404017847,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.008204890657260044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2111637269198994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.541359460800841,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.217691440100648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.453398445703459,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.010226022771218,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 8.969970703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 17.510009765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.9125350488117245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6859268530092906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.7233771307435317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 15.04915914368401,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.290900566790045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.8806787030820633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7660056841737095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9794113018698258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.265128824895579,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3784817820586048,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.446336615316579,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 15.66041081061854,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4547801741247142,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.489355227361859,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.1685933832554234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5946510098942213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.56549987792971,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -27.941500854492233,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2079907226561772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.572498779296893,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.13715667724613922,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.06714569091798239,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9512145865806296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.216834036750141,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.166322044453727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7037649791341707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3993603640952479,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.763052719993586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.4521397181919653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.1849931989397327,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.12408321447206383,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.621502117788733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1535604101558619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.2518305483462235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7988504722501488,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.30001521652909213,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.320003509521484,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.510002136230469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -17.058046923598358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -17.2186438351128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.474111437239722,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -27.67404950837137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.848573717412819,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.638748379790915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.327227351366716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.955356470790228,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -18.41064069968221,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.52608890606349,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -15.751151952666675,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -27.062797841436836,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.684694110078148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.030071855511117,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.261826418795849,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.340116762765835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.001499938964841,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.891499900817863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7924000549316332,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.4970000457763604,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.23400001525878622,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.004100055694579,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.817605216105761,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.068444061217043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.179992697178648,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.492647123323536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.715872322696477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.336533797279916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.32357161385672484,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.4126428876604358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6158825267178472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.339482219024175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.938274708759749,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.39710540511389,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3710412223298416,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.13382791420059637,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -59.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -188.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.581918920509757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.866325695464631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.189645359295666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -26.73390566123448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.694300821481626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -19.224568961729425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.754467681446176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.586266183799495,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.934512696593611,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.173770766415316,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.466685874722618,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -26.122653994299952,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.530421214146955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.61589243744963,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.689066748875309,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -17.9710264757751,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.62994384765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -53.301248168945335,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.7518640136718204,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.358941650390648,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.1524800109863236,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 12.84169357299811,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.072860618366393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.632377401606899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.910661855951881,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -18.477697704206562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.26811457114638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -27.203799421230816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.0392892020089306,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.980221330178537,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.4447564775646793,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.53025134744213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.456530436326624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -17.134254312556486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5416646891266131,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.20196758379105018,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.009998321533203,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.160401106409553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.436548465262021,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.947471784692842,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -26.737688266842653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.869512954154928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.491217171327873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.4062171735928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.955021891776962,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.512994882493409,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.743993536212706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.224512300119795,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -26.12643659990812,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.705633346820257,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.882540647048078,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.340816241021932,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.339782183752565,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.744999885559082,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.308999824523923,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.22260002136230383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.8418000793457026,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.667224440293115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.314558811518694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.223751020035781,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.805176709500877,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.06071417672293533,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.13714299883161285,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.20597569992330378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2986290502303905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.9767350232206553,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.162210740021894,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6037970768589673,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0905439181773604,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -30.419998168945312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -37.38999938964844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -18.122468875782026,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -29.37593584826436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -28.533133894431828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -29.903951521010605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -9.826386465649696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -17.28467539478018,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.42825785177082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -17.06608500033746,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -19.475062651865883,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -30.683380919215043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -29.81017440985878,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -29.292699854076076,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.662506858315027,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.675998870500386,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -16.362856919199952,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.450845292313065,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.047000122070301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.3684989929199105,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.0027462768554756,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.0760363769531125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.15245513916016762,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3827493286132722,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.79999507416627,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.326672002210184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.243636965874561,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.2737156757353,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -11.268141035522671,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.249050848146883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0667855398995538,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.1259983607700885,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4885453406477085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.524126850177815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.355110418048096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.72773160801226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0549917948573655,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.566382423526199,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.0099945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.3200884575856109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.8025351920327384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7416517399855609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.896389559120577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.25971064055718607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.932539464489066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.11185822863308914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.355675253047755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.6726822336694656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.109980262983424,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.018692255412514,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.285137892186045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.5764097521081446,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.323862940209269,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.8227408387960433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.7404355450233595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.2444999694824048,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.322999572753901,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.10056335449218068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.3059432983398551,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.17584903717039424,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8699124526977471,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.618648098513142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.927015821133551,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.04424894893950704,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.498594159674732,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.11376372161635562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.123571549862852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.08142852783203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7321428571428568,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.04597609045659956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5930659187302005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.004947775661356957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.178217821782173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.16322504298404406,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.40090768666193277,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.1599998474121094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.929996490478516,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.8914687497070055,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.090903378694844,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.95926156288472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.62779227713497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.343553900813846,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.048283036656459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.589083292989929,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.793367448494465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.24406252579086,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.39834844964553,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.236302078311673,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.016540610200439,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.1796742934791755,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.439606512376663,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.52368236041906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.17812774047007,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.007999992370599784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0049997329711857,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.03653411865235512,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4381606292724598,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.08422534942626925,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5142220306396439,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.695736042514042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.841984334975372,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.921344603943945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.303132261239988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.572105421866391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.476088230648093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.16357122148786285,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.33071381705147895,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.37443158374843444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6793868115134414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.512996285219073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.574265405760249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1798321312523088,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2353382707902067,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.0100021362304688,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.0699996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.157416535902769,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.067217024482738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.1251404610720623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.308845439924137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.251736999309541,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.02717775589987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5070012287529595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.464917609833475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.8048227598189146,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7597719535320522,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.8480999456451093,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.920097106858668,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.4156166066442104,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.635854280179666,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.572402161323827,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.0801573178578705,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.27250003814697266,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9404998779296818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.021912841796876137,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.00045539855956633346,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.033214130401610475,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.10138610839843665,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.0923632172508375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.771945264512455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5570914540154597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.49511366913038,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.692235389381593,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.541515118408991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0828574044363839,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.14714322771344868,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.09543561018114755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.18520013432674465,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9938466422270373,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.810358021506677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6277639364098954,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.809088793985093,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.8600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.970001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.0343653892574753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.425139633313366,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.4490766482121442,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4687522947818934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1167407697735388,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.060905372550346115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.5555223021088587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8653995965227868,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.38695916534133,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.7325847042640516,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.7261171636390973,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0800039617164248,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7193796228917915,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.669581896830142,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.4901213695379916,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4806393045471822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.08100051879884518,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.004499053955072441,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.1692361450195392,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.9787860107421977,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0361220550537098,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.15028228759766193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.15536999783179,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5796012541153583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.9939420875068494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.138056025277423,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.0979756412953678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4767699099431755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.05857195172991059,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.3721444266183034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.052502770884687466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.21115897194449884,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.9999461869694368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5214777976951694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.2841751120166838,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.42671812590863745,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.6399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 9.94000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.379077679796194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.763506146568484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.829626137571628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.09492743615072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.218898804743551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.641749006014796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.6504803017569216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.024033794289217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.0264839037123394,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4560610756177983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5525856221446759,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.706179103085251,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3827784120782223,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 8.250425530294592,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.7158812343277887,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6392735023136105,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0425003051757926,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.577001190185541,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.30076629638671193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1567428588867017,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.18081542968749886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7703791809082077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.5546638179059222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.919081908109211,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.0804051355002304,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.0547045653390965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.4330674557446557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.728937243480981,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0921434674944197,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.16571589878627258,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.0016737348129958196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.0011724306467295609,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.45977760976720905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8714847239156609,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5343948318939833,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6815393425980709,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.9900054931640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.431251362248135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.7171597967635917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.8074777351640776,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.182834757024236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.7928434142397105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.7917339424465855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.877310534961831,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.883694336284618,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.07865758616428,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.409714725812906,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.5304372197371245,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.794086423958767,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9567230215743798,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.400410466726382,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9427114675326997,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.4989340443090144,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.512000274658206,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.195999908447263,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.11970626831055142,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.40642883300782273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.05568420410155284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.23446586608886832,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.8221054809999035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.2746396038493497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.383228505035606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.5296363345910695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5004865015882745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.800053239806392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0799996512276786,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.2671421595982144,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.03164865323815613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.20578712238546015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.069806060677326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.500390710807111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.04991812651541272,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5055733131677338,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 5.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.963923535688086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.365421508181644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.441124645940642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.242652054176578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.8294521816545375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.8880484089493415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.556803261418341,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.104960759736976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.6113297596042315,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.057976437230958,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.164084130513689,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.853903721111109,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.9933317889892077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.496724933229138,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.6222041939892082,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.720200467761371,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5485000610351562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.8525001525878935,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0927842712402338,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.02311172485352131,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.01972984313964332,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.08703823089599894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.866796223136215,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.451538719462378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.331083326615114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.161707076201227,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.32507460391045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.155215580195428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.2521427699497769,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5571425301688058,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.13816182626850937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.3737882840559916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.8951993730449535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.5674877749187983,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0220649656113567,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5120902636808649,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5199966430664062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.8199996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.293087917524983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.8948229334331064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.8306268199954197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.114689508696936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.482232508405313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3935476413728276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.6319301094831715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.280197988452514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9404941414411283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.5873778624824206,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.553586304568467,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.725941175631468,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.6461121157399825,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.002224165652622,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.6973310420540395,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.89543769647691,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.31500015258788494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.3505001068115234,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.15696426391602358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.9858808898925844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.03742500305175156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.3269261169433548,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5674894535310697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.7721425772221036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.331973358950446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.487990512395788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.168187984431503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.8897066419112036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.14142826625279015,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.200714111328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.07406712854710706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.16136976893674526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.0675352009293277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5860563789317776,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.3261654207277076,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.34021218213188376,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.19000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1199989318847656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.0100674145145705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2777245821537164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3056906760643194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4692410518387433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.48736267244242626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.7551473765187176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7234986856027747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.6534644290066476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.3425263615692842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.029720488796969313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.028650160637366806,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.0804927187732747,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.3487577202229044,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8535291477610789,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.658097753031907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.268704137031043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.12299995422362997,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7739995956420884,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.01232261657715128,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.03529167175292969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.007641849517817434,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.02853000640868686,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.15007462360265844,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7773390291785143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.4251155321367994,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6011522628071715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.41631092608787057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.4927138423743167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.014999934605189669,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.003571374075753253,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.02845394251951494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.028292220090011977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.431955552842056,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6551039967676604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6357486868619252,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9918720508727377,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.4500007629394531,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.9899978637695312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.251617635855464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.050796360267562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.1988669629903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.930647034654314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.962140984877928,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 8.233022889951027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.037192079109997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 9.165973964546092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.8990238597716091,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.7433512893168754,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.9218264475633466,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.5418987015888455,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.1260205922125976,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 10.841699414230822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.1025930116808644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 9.781213672570487,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.22749996185302734,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7414999008178711,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0027723693847647723,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.10589828491210795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.023469600677486824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.07957195281982621,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.8612705440404618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.278834230050244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.4082775784616715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 7.288798361164206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.3303199359432822,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.799495264201072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.057143347603934136,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.04535729544503342,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.0806172480022549,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.0002850734665320598,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.9153891681696464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.339021535586475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.21820987432348726,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.018120016092942226,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3100013732910156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.0400009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.5032642141898505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.336467121963892,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.3693560519563617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.881446139199828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 4.293863455093216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.556214485618381,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.3599192650611944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5158421226860064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.150670438105996,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0290220510132064,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.092315536529409,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.4926978061343594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.4577430624278858,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.164891009898177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.42532019763206197,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.131081830710402,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.24600009918213317,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9909999847412152,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.01130889892578324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.020137405395509234,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.03160512924194592,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.12602546691894645,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.0597103955707796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.9852787598302113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.5507377554012,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.9675694834371056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.5140117339723878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.761455255608559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.02357128688267296,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.14357076372419086,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.008212274586123725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.21903174559301042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.0122937454883916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.9277781403514114,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6980853077001823,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.1179567495055978,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -14.250030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -63.399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.756833336997179,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.484834098304791,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.0965285011651975,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.138995190685709,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.3001278753655185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.534140037113893,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.0466994390362814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.587469618395662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.109427113081034,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.792279169255476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.3735690165921515,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.527743523751179,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.1362482680308474,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.925463512834096,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.981298506465414,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.972229910371267,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.038002014160156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -26.22900238037107,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.0310003662109466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.4270001220702397,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5693998718261355,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.240949707031291,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.565265306106511,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.821142057671093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.335849643293596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.528018414669681,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.8427699534009476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.845206962838784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.05143301827567015,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.5800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.12525822579606594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9232160303567873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.247993369419717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.001576187836147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.43917378961744413,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.61620545753588,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.350006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.13084299768630903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7603700830155491,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.6975211594364641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.3009132893494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.9292290115453854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.816955553881513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.891459691103159,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.06211078157092,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.2217507783975456,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.5470749879351366,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.579519355990489,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.689661622414869,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.09310861888005473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.208279029601718,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.04313937632597353,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.446871073546527,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.3139999389648409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.3499999999999943,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.03419998168945426,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.15980010986328352,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.03823989868163835,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.11016723632812386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1072158017381817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.445935299372718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.810429610188002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.9600705123444975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.9127789798659691,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.020413504532243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.008571624755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.31857190813337066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.035069883467536034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5120843773341734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.798787530940448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.411028880106174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.48939355468990164,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.3334912106554144,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -12.230010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -21.080001831054688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.331828342276546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.565752961294757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.27575518212522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.19885734856415,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.378260352539744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.487131202963347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.378982608426355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.076124147329374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.6844221183604,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.873198032245443,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.552795697552174,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.58760568162962,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -8.214380745205075,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.87845467868355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -10.313581675855488,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.46088443930498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.4475006103515682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7139991760253963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.05428588867187045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7812509155273517,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.2559528350830078,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.6198695373535372,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.984540945035377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.586174040013397,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -6.356549428257342,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.4335618248676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.343583685315557,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.494126333746028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7350006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.9707151140485495,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5957186464957962,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8336428826972102,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.969936029430112,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.289954978155702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1932251150615938,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.6998108636621607,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -19.04998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -43.040008544921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.9389978137088226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.002890927429771,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.709516555935811,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.463951926608143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.4351103691940046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.178927338874026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.479764565927571,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -16.178816102712545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.291591589792677,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.310335998380457,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.986557071362764,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.852700259673613,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.271230761859335,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.570250814594228,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -7.414363633356704,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.563576394688152,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7740005493163835,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.4074981689453239,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.7926000976562477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.0961999511719114,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.20839996337889488,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.675199890136696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.68129671101648,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.395551268107173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.579063070996348,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.242230604605208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.831582463800156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.235303082759819,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8628561837332587,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7457166399274566,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.4037894861754845,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8089871870018825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.363458788511242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.858447448048013,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.3204150813003601,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.747211828015284,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.3300018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 5.0999908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.234513984437314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.277534107783652,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.369955381201261,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.5074134729571087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7401666772312243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.268002923247516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.586907977902495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.6152034362069152,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.5871077605211688,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.5849791787343377,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.646995896628213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.11866513989164,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.0959537154341064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.876679447527311,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.521507045331628,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.230443144231309,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.4619995117187443,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.653000640869152,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.4237744140625068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.3928710937499886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.12231910705565952,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.6442194366455283,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.8337808109454956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.6524413822309736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.3595810880550618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.4689129285291775,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.408475191879666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.4911013129750748,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.19857134137834898,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.2078563145228802,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.1298201970201429,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5209288573001831,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.3165871642720752,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.0163900276131344,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.05674010335378221,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.5480574717728893,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.9899997711181641,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.8799991607666016,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.459743569584374,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.180224386902597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.088328353350655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.92222415631164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.3517601493048712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.894454282669028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.8770699666033863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.725743654799679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -5.812337345668228,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -4.487669457853283,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.365368868777608,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -6.310972489377109,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -3.187880541970201,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.285777758389232,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.811669034032519,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.110503946775285,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.18499994277954102,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.711499881744384,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.07140003204345646,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.3113999938964831,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.0244999980926508,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.11434997558593096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.6562906992008806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -3.8631696170317364,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.9226655867435882,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.002944566159339,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.9851200286447828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.4669429295150165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.007928575788225367,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.11078562055315289,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.12275339435711796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.537181062568119,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -2.83993044688642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -5.392998071859889,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8442856780127902,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8364590533259709,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.0199966430664062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.868011490678124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.36271123063313,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 2.387940459598914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.6913903710280334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 3.5960539245655454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.7612825857635146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.657698799983486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 3.894168542326848,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.5154177145942693,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.0552661596824442,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.1108999441719614,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.3026420379625647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.7599335319002156,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 6.369959110043311,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.2769002674456464,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 4.509408250351243,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.2619998931884737,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.7765003204345646,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.004418792724607101,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.11867767333984602,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.04159229278565135,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.17553955078125227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.377763135869925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 1.7204824087156956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.735562544728464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.9806643530305044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.7131634144781582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.6115511640046885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.09500013078962044,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.22000067574637283,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.09652179596935695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.24983800027185454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.613139207888004,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 2.606828627786051,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.36870209603285187,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.3855056440304223,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.7100067138671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.6199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.4700712674224894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.04054620904834216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.03670360166988473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.47379988871341,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.5385807571993908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -13.323853603113145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.2540592091954008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -15.036678230488087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.822665043506344,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -1.347991279999028,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.313744117096837,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -11.862548221778878,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.297539635465939,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -10.71517707883335,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -1.6805398582337316,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -14.421438522463692,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.704499816894554,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -2.61599960327149,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.03820007324219432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.09940002441405227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.18255001068115462,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.8481500625610465,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.8288779726589155,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -7.819884297832879,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.45343372325846687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -9.4283330645493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.3663467904946778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -12.185231012743579,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.1771425519670755,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.20714351109096008,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.12814456163240662,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.4105158667817399,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 0.405973306847196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -8.931325502715982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": 1.2395575356163664,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.971866786050724,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.020000000000000462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.03000000000000025,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.21999999999999975,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": -0.009999999999999898,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.050000000000000044,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": -0.040000000000000036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-03",
        "change": 0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-27",
        "to": "2026-11-03",
        "change": 0.009999999999999787,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.1200000000000001,
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
    "available_prior_observations": 13,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -4.219999999999999,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.3000000000000007,
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
        "change": -67.5849609375,
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
        "change": -36.172332763671875,
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
        "change": -92.63170623779297,
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
        "change": -43.773468017578125,
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
        "change": -11.395751953125,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "intraday.SPY.minute_close_vwap",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "intraday.QQQ.minute_close_vwap",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "intraday.SMH.minute_close_vwap",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "intraday.RSP.minute_close_vwap",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "intraday.XLF.minute_close_vwap",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  },
  {
    "id": "intraday.XLV.minute_close_vwap",
    "available_prior_observations": 0,
    "changes": [],
    "status": "no_baseline"
  }
]
```

## 判断依据 · 反弹可靠吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹可靠吗？ |
| 事实指标引用 | ["prices.SPY.distance_sma20_pct", "prices.QQQ.distance_sma20_pct", "intraday.QQQ.minute_close_vwap"] |
| 推断与解释 | 大盘放量、等权参与是真的；尾盘回吐和QQQ均线缺口使趋势反转尚未确认。 |
| 反证与缺口 | 低VIX不阻止半导体下跌。 |
| 确认条件 | SPY守762.64并站稳767.57附近；QQQ守687.87并回收昨收691.95及4日分钟均价近似694.07；RSP相对强。开盘30–60分钟回踩不破并维持当日常规VWAP上方，再看收盘及次日延续；当前尚无今日常规VWAP。 |
| 失效条件 | SPY失762.64或QQQ失687.87后反抽不回，且等权转弱、油价/VIX升高，降低宽基反弹评级。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 条件式指导 | 依据回踩和次日收盘逐步提升置信度；不把单次跳涨当趋势反转或最优仓位依据。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报无新完整日线，新增盘前弱势、BoE加息与Coherent官方财报；不能重复计算昨天放量。 |

## 判断依据 · 优先板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先板块？ |
| 事实指标引用 | ["prices.XLF.return_5d_pct", "prices.XLV.return_5d_pct", "prices.RSP.relative_spy_1d_pp"] |
| 推断与解释 | 金融医疗消费更强，工业军工退出共同领先假设。 |
| 反证与缺口 | 离均线偏远，追涨可能承受回吐；申赎不明。 |
| 确认条件 | XLF回踩57.94附近有承接后重回58.72并守59.20；XLV守185.33、回到188.74以上；XLY维持相对SPY强势，依据次日开盘区间而非盘前跳空追入。 |
| 失效条件 | XLF失57.94或XLV失185.33且反抽失败；等权跌破221.07、油价急反弹亦削弱剧本。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 条件式指导 | 依据回踩和次日收盘逐步提升置信度；不把单次跳涨当趋势反转或最优仓位依据。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报无新完整日线，新增盘前弱势、BoE加息与Coherent官方财报；不能重复计算昨天放量。 |

## 判断依据 · 半导体见底了吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 半导体见底了吗？ |
| 事实指标引用 | ["prices.SMH.distance_sma200_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | SMH盘前跌破497.33，MU/SNDK跌前低，AI止跌条件未满足；需常规时段复核。 |
| 反证与缺口 | 财报需求仍在，价格下跌不代表技术失去价值。 |
| 确认条件 | SMH先收回497.33与昨收504.27并形成更高低点；MU回收782、SNDK回收1014且相对SMH不再新低。随后看SMH511.63及521–522区，常规VWAP须开盘后真实计算。 |
| 失效条件 | 盘前已低于上述昨日低点；若常规开盘后30–60分钟仍不能收回、反抽缩量/再创新低，确认失败延续，不用低VIX抄底。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 条件式指导 | 依据回踩和次日收盘逐步提升置信度；不把单次跳涨当趋势反转或最优仓位依据。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报无新完整日线，新增盘前弱势、BoE加息与Coherent官方财报；不能重复计算昨天放量。 |

## 判断依据 · 宏观/融资风险消失了吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 宏观/融资风险消失了吗？ |
| 事实指标引用 | ["prices.^VIX.value", "macro.BAMLH0A0HYM2.value", "macro.DGS2.value"] |
| 推断与解释 | 波动下降与总量信用温和，但通胀分项、公司融资和审批仍限制风险预算。 |
| 反证与缺口 | FRED/GPR滞后且不是今日公司信用报价。 |
| 确认条件 | 弱势篮子不再相对大盘下行，投运审批和现金流能被官方验证，信用成本改善须同债券同窗口。 |
| 失效条件 | 项目延误、融资稀释加速或信用继续恶化与股价新低共振时下调；不把单一低量合约当信号。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 条件式指导 | 依据回踩和次日收盘逐步提升置信度；不把单次跳涨当趋势反转或最优仓位依据。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相对早报无新完整日线，新增盘前弱势、BoE加息与Coherent官方财报；不能重复计算昨天放量。 |

## 非AI轮动仍强，半导体盘前破位 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 完整日线仍为4日；5日盘前芯片财报继续被消化。 |
| 事实：市场反应 | 金融、医疗/宽基稳；SMH、MU、SNDK低于4日低点。 |
| 推断：解释 | 推断：市场选择增长兑现与风险暴露，而不是普涨。 |
| 受益篮子 | ["XLF", "XLV", "XLY", "RSP观察篮子"] |
| 受损篮子 | ["存储、高杠杆芯片与AI建设链"] |
| 反证 | 盘前薄量可能放大跌幅；常规回收关键位可以削弱破位判断。 |
| 下一催化剂 | 今晚开盘前30–60分钟与就业数据 |
| 证据 | ["https://www.bls.gov/schedule/2026/11_sched.htm"] |

## 光通信增长与手机盈利压力分化 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Coherent官方收入毛利增长；QCOM成本上升且手机收入下降。 |
| 事实：市场反应 | Coherent盘前相对强，高通与存储弱。 |
| 推断：解释 | 同属芯片/AI并不意味着订单、利润率和估值驱动一致。 |
| 受益篮子 | ["COHR等兑现毛利的光通信观察"] |
| 受损篮子 | ["成本转嫁落后、现金回收差者"] |
| 反证 | Coherent强增长不能独自抬升整个SMH；高估值下好财报仍可能被卖出。 |
| 下一催化剂 | 常规时段是否守开盘区间/VWAP；NVDA11月17日财报 |
| 证据 | ["https://ir.coherent.com/news-releases/news-release-details/coherent-corp-reports-first-quarter-fiscal-2027-results", "https://investor.qualcomm.com/files/content_files/FY2026-4th-Quarter-Earnings-Release.pdf"] |

## 油价回升与英国加息 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 英国央行加息25bp至4%，中期价格风险仍高。 |
| 事实：市场反应 | 原油盘前回升、黄金走高，股市内部仍分化。 |
| 推断：解释 | 推断：能源下降的通胀缓和需要持续验证，不能由一天油跌推出宽松。 |
| 受益篮子 | ["现金流稳健、成本转嫁强者"] |
| 受损篮子 | ["高久期估值及能源成本敏感者"] |
| 反证 | 英国政策不决定Fed路径；油价持续下行可改变预期。 |
| 下一催化剂 | 明晚就业、10日CPI及真实通行量 |
| 证据 | ["https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026", "https://www.bls.gov/schedule/2026/11_sched.htm"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | 352.39 | 0.82 | 2026-11-05T12:01:02+00:00 | 2026-11-05T12:01:02+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| AMD | 471.50 | -3.54 | 2026-11-05T12:01:07+00:00 | 2026-11-05T12:01:07+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| AMZN | 269.83 | 1.43 | 2026-11-05T12:00:59+00:00 | 2026-11-05T12:00:59+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| ARM | 183.00 | -4.59 | 2026-11-05T12:00:48+00:00 | 2026-11-05T12:00:48+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| AVGO | 319.56 | -1.82 | 2026-11-05T12:00:50+00:00 | 2026-11-05T12:00:50+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| BABA | 110.17 | 4.63 | 2026-11-05T12:00:35+00:00 | 2026-11-05T12:00:35+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| CAT | 586.71 | -0.78 | 2026-11-05T12:00:00+00:00 | 2026-11-05T12:00:00+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| CEG | 243.65 | -0.84 | 2026-11-05T12:00:09+00:00 | 2026-11-05T12:00:09+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| CI | 315.88 | 3.43 | 2026-11-05T12:00:26+00:00 | 2026-11-05T12:00:26+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| COHR | 191.01 | -2.09 | 2026-11-05T12:00:53+00:00 | 2026-11-05T12:00:53+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| COIN | 151.20 | -0.20 | 2026-11-05T11:53:29+00:00 | 2026-11-05T11:53:29+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| COP | 138.88 | 1.41 | 2026-11-05T11:52:31+00:00 | 2026-11-05T11:52:31+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| CRWV | 46.88 | -3.18 | 2026-11-05T12:00:45+00:00 | 2026-11-05T12:00:45+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| CVX | 218.58 | 0.75 | 2026-11-05T11:41:00+00:00 | 2026-11-05T11:41:00+00:00 | 2026-11-05T12:01:11.278539+00:00 | stale |
| DRAM | 42.97 | -4.74 | 2026-11-05T12:01:03+00:00 | 2026-11-05T12:01:03+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| GDX | 87.07 | 2.93 | 2026-11-05T12:00:12+00:00 | 2026-11-05T12:00:12+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| GEV | 814.00 | -2.26 | 2026-11-05T12:00:25+00:00 | 2026-11-05T12:00:25+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| GLD | 378.35 | 1.57 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| GLW | 115.04 | -3.14 | 2026-11-05T12:00:24+00:00 | 2026-11-05T12:00:24+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| GOOGL | 291.96 | 1.05 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| IGV | 103.56 | 0.00 | 2026-11-05T12:00:04+00:00 | 2026-11-05T12:00:04+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| INTC | 57.06 | -2.08 | 2026-11-05T12:01:00+00:00 | 2026-11-05T12:01:00+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| IWM | 285.37 | 0.48 | 2026-11-05T12:00:16+00:00 | 2026-11-05T12:00:16+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| LITE | 603.33 | -3.74 | 2026-11-05T12:00:22+00:00 | 2026-11-05T12:00:22+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| LLY | 1,430.95 | 0.91 | 2026-11-05T12:00:54+00:00 | 2026-11-05T12:00:54+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| META | 638.36 | 1.33 | 2026-11-05T12:00:55+00:00 | 2026-11-05T12:00:55+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| MRVL | 153.82 | -3.74 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| MSFT | 558.28 | 0.45 | 2026-11-05T12:00:58+00:00 | 2026-11-05T12:00:58+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| MU | 769.02 | -3.30 | 2026-11-05T12:01:06+00:00 | 2026-11-05T12:01:06+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| NOW | 109.20 | 0.36 | 2026-11-05T12:00:30+00:00 | 2026-11-05T12:00:30+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| NVDA | 198.13 | -1.00 | 2026-11-05T12:01:01+00:00 | 2026-11-05T12:01:01+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| ORCL | 123.30 | -0.35 | 2026-11-05T12:00:50+00:00 | 2026-11-05T12:00:50+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| PLTR | 167.87 | -2.23 | 2026-11-05T12:01:05+00:00 | 2026-11-05T12:01:05+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| QCOM | 156.66 | -9.54 | 2026-11-05T12:00:57+00:00 | 2026-11-05T12:00:57+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| QQQ | 688.19 | -0.54 | 2026-11-05T12:00:54+00:00 | 2026-11-05T12:00:54+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| RSP | 224.20 | 0.39 | 2026-11-05T11:54:48+00:00 | 2026-11-05T11:54:48+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| SMH | 492.50 | -2.33 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:00:56+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| SNDK | 993.80 | -4.20 | 2026-11-05T12:01:01+00:00 | 2026-11-05T12:01:01+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| SPY | 768.12 | 0.17 | 2026-11-05T12:00:58+00:00 | 2026-11-05T12:00:58+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| STX | 538.00 | -3.42 | 2026-11-05T11:54:23+00:00 | 2026-11-05T11:54:23+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| TAN | 46.52 | 1.59 | 2026-11-05T11:33:00+00:00 | 2026-11-05T11:33:00+00:00 | 2026-11-05T12:01:11.278539+00:00 | stale |
| TLT | 81.83 | 0.09 | 2026-11-05T12:00:39+00:00 | 2026-11-05T12:00:39+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| VRT | 199.52 | -2.93 | 2026-11-05T12:01:01+00:00 | 2026-11-05T12:01:01+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| XLE | 63.90 | 0.60 | 2026-11-05T12:00:00+00:00 | 2026-11-05T12:00:00+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| XLF | 59.89 | 1.17 | 2026-11-05T12:00:47+00:00 | 2026-11-05T12:00:47+00:00 | 2026-11-05T12:01:11.278539+00:00 | ok |
| XLI | 169.70 | 0.14 | 2026-11-05T09:02:25+00:00 | 2026-11-05T09:02:25+00:00 | 2026-11-05T12:01:11.278539+00:00 | stale |
| XLV | 190.84 | 0.62 | 2026-11-05T11:41:43+00:00 | 2026-11-05T11:41:43+00:00 | 2026-11-05T12:01:11.278539+00:00 | stale |
| XOM | 170.75 | 0.87 | 2026-11-05T11:36:00+00:00 | 2026-11-05T11:36:00+00:00 | 2026-11-05T12:01:11.278539+00:00 | stale |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 766.81 | USD_per_share | 2026-11-04 | 1.65 | -0.71 | -1.34 | ok |
| QQQ | 691.95 | USD_per_share | 2026-11-04 | 0.97 | -4.64 | -8.68 | ok |
| IWM | 284.02 | USD_per_share | 2026-11-04 | 1.51 | 0.97 | 2.28 | ok |
| RSP | 223.33 | USD_per_share | 2026-11-04 | 1.86 | 2.71 | 6.04 | ok |
| GLD | 372.49 | USD_per_share | 2026-11-04 | 3.68 | -0.27 | -0.90 | ok |
| GC=F | 4,073.00 | USD_per_troy_ounce | 2026-11-04 | 3.37 | 0.53 | -1.63 | ok |
| CL=F | 88.12 | USD_per_barrel | 2026-11-04 | -8.29 | -14.26 | -0.18 | ok |
| BZ=F | 94.62 | USD_per_barrel | 2026-11-04 | -8.67 | -17.95 | -5.57 | ok |
| TLT | 81.76 | USD_per_share | 2026-11-04 | 0.80 | 0.95 | 5.98 | ok |
| UUP | 28.90 | USD_per_share | 2026-11-04 | -0.38 | -0.55 | -0.48 | ok |
| HYG | 77.52 | USD_per_share | 2026-11-04 | 0.70 | -0.09 | 0.44 | ok |
| LQD | 104.50 | USD_per_share | 2026-11-04 | 0.75 | 0.41 | 2.35 | ok |
| ^VIX | 16.61 | index | 2026-11-04 | -20.26 | -1.77 | 10.15 | ok |
| ^VIX3M | 18.80 | index | 2026-11-04 | -11.61 | -2.19 | 6.09 | ok |
| ^VVIX | 90.41 | index | 2026-11-04 | -15.82 | -6.42 | 8.69 | ok |
| ^MOVE | 93.88 | index | 2026-11-04 | -6.09 | -0.71 | -10.76 | ok |
| NVDA | 200.13 | USD_per_share | 2026-11-04 | -3.17 | -7.08 | -15.72 | ok |
| MSFT | 555.80 | USD_per_share | 2026-11-04 | 6.68 | 4.67 | 4.92 | ok |
| AMZN | 266.03 | USD_per_share | 2026-11-04 | 6.12 | 4.49 | 2.35 | ok |
| GOOGL | 288.93 | USD_per_share | 2026-11-04 | 3.18 | -11.07 | -17.57 | ok |
| META | 630.00 | USD_per_share | 2026-11-04 | 1.44 | 2.86 | -12.66 | ok |
| CRWV | 48.42 | USD_per_share | 2026-11-04 | -9.90 | -24.26 | -45.26 | ok |
| MU | 795.23 | USD_per_share | 2026-11-04 | -7.00 | -19.12 | -26.90 | ok |
| DRAM | 45.11 | USD_per_share | 2026-11-04 | -5.31 | -16.65 | -24.83 | ok |
| VRT | 205.55 | USD_per_share | 2026-11-04 | -12.89 | -15.39 | -16.61 | ok |

## 跨资产风险解释

当前更接近宽基恐慌消退、局部AI链去风险的混合阶段，不是单一恐慌或过热周期。11月4日VIX16.61、VIX3M18.80，期限比约0.884；今晚Cboe CSV已更新4日16.61，补上早报官方序列缺口。MOVE93.88、VVIX90.41仍是4日。盘前VIX约16.8、黄金连续期货4141.9、WTI89.23、Brent96.64、美元101.622，保留各分钟时点，不能视为同时成交。相较4日连续日线，油价反弹，昨日大跌并不意味着能源冲击结束。英国央行5日官方8比1决定加息25bp至4%，另一票主张50bp；预测2027年中通胀约5%。这是英国政策，不冒充Fed已加息，但说明能源传导仍具粘性。FRED2年4.61%、10年4.95%、实际10年2.65%、HY340bp/IG93bp仍3日；T10YIE2.26为4日。STLFSI−0.5224截至10月30日，GPR97.67/7日均137.64截至2日。避险、战争影响采用这些分项并列，无合成指数。Fed12月25bp加息合约77.5%，并非客观概率；CME超时、CNN418仍缺失。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.61 | percent | 2026-11-03 | -0.23 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.40 | percentage_points | 2026-11-03 | 0.37 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.93 | percentage_points | 2026-11-03 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.95 | percent | 2026-11-03 | -0.36 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.65 | percent | 2026-11-03 | -0.30 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.26 | percent | 2026-11-04 | -0.10 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.52 | index | 2026-10-30 | 0.24 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 16.61 | index | 2026-11-04 | 1.53 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 97.67 | index | 2026-11-02 | -213.94 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 113.60 | index | 2026-11-02 | -291.60 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 94.75 | index | 2026-11-02 | -209.43 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 137.64 | index | 2026-11-02 | -46.66 | lagged | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 164.04 | index | 2026-11-02 | -2.33 | lagged | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -0.01 | -7.59 | -12.36 | -1.66 | -6.88 | -11.02 | 1.29 | 2026-11-04 |
| XLE | 能源 | -4.74 | -7.20 | 0.25 | -6.39 | -6.49 | 1.59 | 2.12 | 2026-11-04 |
| XLF | 金融 | 3.51 | 5.47 | 10.14 | 1.86 | 6.18 | 11.48 | 1.54 | 2026-11-04 |
| XLI | 工业 | -1.09 | 0.58 | 0.97 | -2.74 | 1.29 | 2.30 | 1.54 | 2026-11-04 |
| XLV | 医疗 | 3.06 | 5.53 | 12.35 | 1.41 | 6.24 | 13.69 | 1.70 | 2026-11-04 |
| XLP | 必需消费 | 3.36 | 5.87 | 12.53 | 1.71 | 6.59 | 13.87 | 1.46 | 2026-11-04 |
| XLY | 可选消费 | 4.26 | 6.07 | 9.85 | 2.61 | 6.78 | 11.19 | 2.41 | 2026-11-04 |
| XLC | 通信 | 3.47 | 1.76 | -5.66 | 1.82 | 2.48 | -4.32 | 1.59 | 2026-11-04 |
| XLU | 公用事业 | 0.44 | 2.64 | 5.98 | -1.21 | 3.35 | 7.32 | 1.56 | 2026-11-04 |
| XLRE | 房地产 | 3.32 | 7.10 | 11.22 | 1.67 | 7.81 | 12.55 | 1.12 | 2026-11-04 |
| XLB | 材料 | 2.49 | 3.93 | 10.04 | 0.84 | 4.65 | 11.38 | 1.98 | 2026-11-04 |
| SMH | 半导体 | -2.75 | -11.17 | -19.32 | -4.40 | -10.46 | -17.98 | 1.36 | 2026-11-04 |
| IGV | 软件 | 0.88 | -7.46 | -5.72 | -0.78 | -6.75 | -4.38 | 1.47 | 2026-11-04 |
| XOP | 油气开采 | -6.39 | -10.52 | -4.75 | -8.04 | -9.81 | -3.42 | 2.43 | 2026-11-04 |
| OIH | 油服 | -4.95 | -10.52 | -4.06 | -6.60 | -9.81 | -2.72 | 2.33 | 2026-11-04 |
| ITA | 航空与国防 | -1.54 | 2.45 | 4.54 | -3.19 | 3.17 | 5.88 | 1.32 | 2026-11-04 |
| ARKX | 航天主题 | -3.31 | -6.10 | -11.34 | -4.96 | -5.39 | -10.00 | 1.39 | 2026-11-04 |
| KRE | 区域银行 | 1.72 | 2.80 | 7.61 | 0.06 | 3.51 | 8.95 | 1.17 | 2026-11-04 |
| SKYY | 云计算 | 0.46 | -9.07 | -8.25 | -1.20 | -8.35 | -6.91 | 2.03 | 2026-11-04 |

## 资金证据分层

19只板块/主题ETF同端点11月3日至4日重算。XLY日涨跌+4.26%、5日+6.07%；XLF日涨跌+3.51%、5日+5.47%；XLV日涨跌+3.06%、5日+5.53%；XLP日涨跌+3.36%、5日+5.87%；XLRE日涨跌+3.32%、5日+7.10%；XLC日涨跌+3.47%、5日+1.76%；SMH日涨跌-2.75%、5日-11.17%；IGV日涨跌+0.88%、5日-7.46%；SKYY日涨跌+0.46%、5日-9.07%；XLI日涨跌-1.09%、5日+0.58%；ITA日涨跌-1.54%、5日+2.45%；XLE日涨跌-4.74%、5日-7.20%；XOP日涨跌-6.39%、5日-10.52%；OIH日涨跌-4.95%、5日-10.52%；ARKX日涨跌-3.31%、5日-6.10%。金融、医疗、消费强于SPY；工业/军工虽然5日仍正，4日逆势下跌，退出原“共同领先”假设。RSP+1.86%强于SPY+1.65%、量比1.80，参与面代理改善，但不是全成分上涨家数。SPY量比1.57、QQQ1.50，量能扩张仍需看收盘位置：SPY几乎贴20日均767.57，QQQ低于20日均约3.55%，SMH低于20日均约8.63%且跌破200日均521.22。不是所有上涨都已回到上升趋势。ICI最新仍截至10月28日：全部ETF净发行459.06亿美元、国内股265.90亿、债券142.34亿、商品−18.89亿。发行人页面仅单期份额/NAV，缺19ETF当期净申赎与拆分桥；不能把今日涨幅写成主力净买入，滞后机构持仓也不能解释今日资金。 今晚没有新的完整常规日线，以上仍为11月4日。盘前SPY、RSP、XLF/XLV相对稳定，SMH、MU、SNDK弱于宽基；成交稀疏时不能用盘前量比对比整日。发行人SMH页面本次再次检查，单期份额/NAV不足以得出当期净申赎；ICI最新仍10月28日，没有把旧窗口包装成今日主力流入。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-11-05T12:08:53.573272+00:00：基础全领域加15组主动搜索，覆盖AI/银行破产、Fed/衰退、油气战争、软件信用、芯片/H200、Apple/CXMT、IPO、Texas政策及就业。Meta offering首10/77、Anthropic首10/29、Iran首10/11被截断，保留覆盖缺口。直接事件ID核验NVDA及两组10月就业，新增明日就业参考。没有把单日股票涨跌博彩当宏观风险。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will Texas enact a data center moratorium by June 30, 2027?", "2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。", "https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928"] | [17.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999981, "volume24h_usd": 9240.737954, "liquidity_usd": 43907.0223, "quality_flags": [], "retrieved_at": "2026-11-05T12:01:04.821683+00:00", "contract_end_at": "2027-07-01T03:59:00+00:00"} | ["Texas建设限制事件定义狭窄，低报价不能排除行政/地方审核风险。", "数据中心投运、资本占用、供应链订单"] | ["州法律正文与项目延期相互验证", "仅竞选承诺或行政措施不触发此合约"] | [null, null] |
| ["Oracle downgraded to junk by Moody's or S&P by December 31, 2026?", "2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。", "https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by"] | [16.5, {"status": "comparable", "change_pp": -0.5000000000000004}] | {"spread": 0.04999999999999999, "volume24h_usd": 12.680873000000002, "liquidity_usd": 330.4926, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-05T12:01:00.356445+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Oracle正式垃圾级评级观察，低量宽价差仅弱信号", "信用成本与资本开支"] | ["正式评级和同券信用价格同时恶化", "仅负面展望不满足规则"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by November 30?", "11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [29.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 976.72292, "liquidity_usd": 30987.71, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-05T12:01:01.193742+00:00", "contract_end_at": "2026-11-30T20:59:00+00:00"} | ["沙特管线军事打击风险", "石油供给与通胀"] | ["独立核验打击与供应变化", "单方威胁/拦截不符合规则"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [77.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 247764.16682699998, "liquidity_usd": 575164.4731, "quality_flags": [], "retrieved_at": "2026-11-05T12:01:25.861942+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月加息档定价仍高", "估值折现与资金成本"] | ["官方政策及通胀数据支持", "物价降温且联储指引反向"] | [null, null] |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [8.25, {"status": "comparable", "change_pp": 1.45}] | {"spread": 0.0050000000000000044, "volume24h_usd": 2830.5615030000004, "liquidity_usd": 29799.87116, "quality_flags": [], "retrieved_at": "2026-11-05T12:01:25.861942+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["AI专门规则，不能当普遍股价下跌概率", "估值与融资信心"] | ["逐条满足至少三项触发", "单一公司下跌不足"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [10.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 274618.559857, "liquidity_usd": 360778.354, "quality_flags": [], "retrieved_at": "2026-11-05T12:01:25.861942+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["霍尔木兹真实通行比新闻标题重要", "油价/运费"] | ["Portwatch七日均达规则阈值", "宣布开放而运量未恢复"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [16.0, {"status": "comparable", "change_pp": 5.500000000000001}] | {"spread": 0.020000000000000018, "volume24h_usd": 282.038092, "liquidity_usd": 1660.9165, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-05T12:01:04.150951+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Apple/CXMT采购观察", "存储竞争"] | ["正式采购声明符合规则", "传闻或HBM推论不足"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the US add at least 100k jobs in October?", "按BLS 2026年10月非农就业增量，至少100k为Yes；边界值落较高档。若到下月发布日仍未发布该月数据，则按最后可用月处理。计划11月6日08:30美东；不是经济衰退概率。", "https://polymarket.com/event/how-many-jobs-added-in-october-2026"] | [27.500000000000004, {"status": "no_baseline"}] | {"spread": 0.02999999999999997, "volume24h_usd": 557.293925, "liquidity_usd": 1327.4133, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-05T12:05:33.035036+00:00", "contract_end_at": "2026-11-07T04:59:00+00:00"} | ["至少10万非农就业档，量能有限；不归一化为预测分布", "就业—Fed利率—估值折现及消费预期"] | ["官方首次数据与工资/参与率结合，并看债券和股市同步反应", "单一分档不解释增长质量；低量合约不能替代BLS数据"] | ["2026-11-06T08:30:00-05:00", "https://www.bls.gov/schedule/2026/11_sched.htm"] |
| ["Will the October 2026 unemployment rate be 4.2%?", "BLS 2026年10月季调U-3失业率首次公布为4.2%则Yes，一位小数；后续修订不计。到下月发布日仍无该月值则用最后可用月。", "https://polymarket.com/event/october-unemployment-rate-2026"] | [43.5, {"status": "no_baseline"}] | {"spread": 0.010000000000000009, "volume24h_usd": 188.89459800000006, "liquidity_usd": 1799.7289, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-05T12:01:25.861942+00:00", "contract_end_at": "2026-11-06T13:30:00+00:00"} | ["4.2% U-3失业率精确档；不等于失业率上升概率", "就业—Fed利率—估值折现及消费预期"] | ["官方首次数据与工资/参与率结合，并看债券和股市同步反应", "单一分档不解释增长质量；低量合约不能替代BLS数据"] | ["2026-11-06T08:30:00-05:00", "https://www.bls.gov/schedule/2026/11_sched.htm"] |
| ["Will Nvidia (NVDA) beat quarterly earnings?", "NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。", "https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53"] | [97.95, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.03700000000000003, "volume24h_usd": 30.02, "liquidity_usd": 518.45306, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-05T12:05:32.129160+00:00", "contract_end_at": "2026-11-17T22:00:00+00:00"} | ["NVDA固定2.53美元EPS合约；极低近期成交且价差3.7个百分点，不是股票上涨胜率", "AI需求、利润率、建设兑现"] | ["官方首次EPS超固定门槛且指引/价格承接一致", "即使EPS达标也可能股跌；盈利质量与现金回收需独立核验"] | ["2026-11-17T17:00:00-05:00", "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"] |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 10.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [274618.559857, 360778.354] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:25.861942+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 77.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [247764.16682699998, 575164.4731] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-05T11:57:27.437392Z |
| 抓取时间 | 2026-11-05T12:01:25.861942+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 8.25 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.25, -0.05] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.45} |
| 24h成交量 / 流动性 USD | [2830.5615030000004, 29799.87116] |
| 价差 pp | 0.50 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:25.861942+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 23.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, 0.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.5000000000000004} |
| 24h成交量 / 流动性 USD | [922.999581, 8783.044] |
| 价差 pp | 2.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:25.861942+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will the October 2026 unemployment rate be 4.2%?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1120075 / 5211635 |
| Yes 概率 % | 43.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -1.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [188.89459800000006, 1799.7289] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-06T13:30:00+00:00 |
| 结算规则摘要 | BLS 2026年10月季调U-3失业率首次公布为4.2%则Yes，一位小数；后续修订不计。到下月发布日仍无该月值则用最后可用月。 |
| 规则指纹 | 0303df35e02524a94541a3178780a0a87d85cb14383a8a2d9ea28182cb56c111 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:25.861942+00:00 |
| 来源 | https://polymarket.com/event/october-unemployment-rate-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, -9.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [48.219231, 19331.8645] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:25.861942+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Oracle downgraded to junk by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219847 / 5939428 |
| Yes 概率 % | 16.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5000000000000004} |
| 24h成交量 / 流动性 USD | [12.680873000000002, 330.4926] |
| 价差 pp | 5.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。 |
| 规则指纹 | cb29bc6ea2fb2a6cd1d97dc489f0163f0b47e0cb2d31a9cbb3fe5dda90eb10c4 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T11:53:27.624054Z |
| 抓取时间 | 2026-11-05T12:01:00.356445+00:00 |
| 来源 | https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by |

## Military action against Saudi Oil Pipeline (East-West) by November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401796 |
| Yes 概率 % | 29.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-4.5, -19.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [976.72292, 30987.71] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-30T20:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。 |
| 规则指纹 | de6f019a1972387984a02c6a8e7cef39e331ff99c1895cf1bba902450d550441 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T11:51:26.893215Z |
| 抓取时间 | 2026-11-05T12:01:01.193742+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 91.10 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, -3.7] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.6000000000000014} |
| 24h成交量 / 流动性 USD | [34410.17966, 37622.4774] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:03.553978+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 16.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.0, 0.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 5.500000000000001} |
| 24h成交量 / 流动性 USD | [282.038092, 1660.9165] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T11:51:26.893215Z |
| 抓取时间 | 2026-11-05T12:01:04.150951+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## Will Texas enact a data center moratorium by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123855 |
| Yes 概率 % | 2.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.2, 0.25] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.2499999999999999} |
| 24h成交量 / 流动性 USD | [1118.926, 72022.97436] |
| 价差 pp | 0.40 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | b3e9528c7bb241316ba9beb5332075225a4976826229cd820fec02a115957e3a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:04.821683+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Will Texas enact a data center moratorium by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123856 |
| Yes 概率 % | 17.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [9240.737954, 43907.0223] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | bad230b7f527696e74d48176c1f04e0fa6e22d9b444c004e912067120edc074f |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-05T11:59:26.47873Z |
| 抓取时间 | 2026-11-05T12:01:04.821683+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Major CEX insolvent in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 199777 / 1343533 |
| Yes 概率 % | 3.05 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -0.05] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [null, 21118.70598] |
| 价差 pp | 1.50 |
| 到期 | 2027-01-01T05:00:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Binance/Coinbase/Bybit/OKX/Kraken任一被正式宣布资不抵债或申请/拟申请任一种破产程序则Yes；按官方代表或可信报道共识。被盗、暂停提款或偿付证明延期本身不是触发。 |
| 规则指纹 | 60d4965584f04350506eafe348b3b70153b2fd33101cc7cd02976facea6531d8 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T06:27:25.40885Z |
| 抓取时间 | 2026-11-05T12:01:04.954397+00:00 |
| 来源 | https://polymarket.com/event/major-cex-insolvent-in-2026 |

## Will Nvidia (NVDA) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1308738 / 6639362 |
| Yes 概率 % | 97.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.05, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [30.02, 518.45306] |
| 价差 pp | 3.70 |
| 到期 | 2026-11-17T22:00:00+00:00 |
| 结算规则摘要 | NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。 |
| 规则指纹 | f9c0b1886ab273be18bc170b3841777783b7f9b2cd80b7ff77a9c0d7a9aa7918 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T12:01:27.354097Z |
| 抓取时间 | 2026-11-05T12:05:32.129160+00:00 |
| 来源 | https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53 |

## Will the US add at least 100k jobs in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1120074 / 5211630 |
| Yes 概率 % | 27.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.5, -3.0] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [557.293925, 1327.4133] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-07T04:59:00+00:00 |
| 结算规则摘要 | 按BLS 2026年10月非农就业增量，至少100k为Yes；边界值落较高档。若到下月发布日仍未发布该月数据，则按最后可用月处理。计划11月6日08:30美东；不是经济衰退概率。 |
| 规则指纹 | 34f44a7c6725e5d40df430e375d2f1b431cbbcb9a48cdc268fed3844d5bd5e51 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-05T12:01:56.812079Z |
| 抓取时间 | 2026-11-05T12:05:33.035036+00:00 |
| 来源 | https://polymarket.com/event/how-many-jobs-added-in-october-2026 |

## AI 压力：合约、经营与估值分开

三层分别看。合约层：2026专门AI泡沫8.25%，较早报6.8%升1.45个百分点；2027年6月23%，升0.5个百分点，规则不同不拼接。Apple采购CXMT合约16%，较10.5%升5.5个百分点，只是采购定义的市场报价，不证明HBM已被替代；Oracle年底垃圾评级16.5%，低量宽价差，只是弱参考。市场经营层：半导体及存储盘前跌破昨日低点，高通约156.66、较173.19收盘跌约9.55%；官方财报手机收入下降与成本上升说明利润兑现仍有压力。反证是Coherent官方Q1收入23.7亿美元、同比50%，non-GAAP毛利率40.6%、EPS2.09；Q2指引收入25.5–27.5亿、EPS2.28–2.48，表明光通信需求仍在，不能把全AI链归于同一衰退。Meta新424B5为既有150亿美元债的补充文件，不再次计新增融资；90亿欧元债分币种处理。H100本次仍4日2.96美元/GPU小时，页首7D与历史表口径冲突，不能外推全部算力。H200新闻的“少量获批、香港等待”与8月18日Reuters报道重合，未核验5日新增大规模放行，拒绝当作新利好。估值层：五家最新定期披露列表全部再次核验，日期仍NVDA8月26、MSFT10月28、AMZN10月30、GOOGL10月29、META10月22；复用NVDA底稿、更新报价，四家公司FCFF/净债务/租赁/稀释桥缺口不变，保留不可用而不造数。模型是企业整体现金流情景，不等于AI崩溃概率。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-11-05T12:04:50.518918+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 200.13 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2720043073706636, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -50.65 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -22.99 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 21.21 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-11-05T12:04:53.778626+00:00", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-05T12:04:57.093050+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-11-05T12:05:00.095674+00:00", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-11-05T12:05:02.708897+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 大盘反弹：收盘质量需第二天补证

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举后第一日放量修复 |
| 关联标的 | ["SPY", "QQQ", "RSP"] |
| 确认条件 | SPY守762.64并站稳767.57附近；QQQ守687.87并回收昨收691.95及4日分钟均价近似694.07；RSP相对强。开盘30–60分钟回踩不破并维持当日常规VWAP上方，再看收盘及次日延续；当前尚无今日常规VWAP。 |
| 失效条件 | SPY失762.64或QQQ失687.87后反抽不回，且等权转弱、油价/VIX升高，降低宽基反弹评级。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 反证 | SPY/QQQ日涨但尾盘低于各自分钟均价近似；QQQ20日均717.42尚远。 |
| 状态 | 等待常规时段验证 |

## 金融医疗消费：回踩强于追高

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 油价/利率下降与参与面扩大 |
| 关联标的 | ["XLF", "XLV", "XLY", "RSP"] |
| 确认条件 | XLF回踩57.94附近有承接后重回58.72并守59.20；XLV守185.33、回到188.74以上；XLY维持相对SPY强势，依据次日开盘区间而非盘前跳空追入。 |
| 失效条件 | XLF失57.94或XLV失185.33且反抽失败；等权跌破221.07、油价急反弹亦削弱剧本。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 反证 | 这几类距20日均约6%，单日追涨的回撤容忍度低；无当期申赎佐证。 |
| 状态 | 观察中 |

## 半导体与存储：先停止创新低

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | QCOM/Arm结果与光通信披露复核 |
| 关联标的 | ["SMH", "NVDA", "MU", "DRAM", "SNDK"] |
| 确认条件 | SMH先收回497.33与昨收504.27并形成更高低点；MU回收782、SNDK回收1014且相对SMH不再新低。随后看SMH511.63及521–522区，常规VWAP须开盘后真实计算。 |
| 失效条件 | 盘前已低于上述昨日低点；若常规开盘后30–60分钟仍不能收回、反抽缩量/再创新低，确认失败延续，不用低VIX抄底。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 反证 | 盘前突破不等于收盘破位；Coherent/Arm经营增长是需求仍在的反证，若带动成分广度改善应重评。 |
| 状态 | 盘前失效警报，等待常规确认 |

## AI融资与算力：价格和信用同时修复

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | Meta欧元最终定价、建设政策变化 |
| 关联标的 | ["CRWV", "ORCL", "VRT", "MSFT", "META"] |
| 确认条件 | 弱势篮子不再相对大盘下行，投运审批和现金流能被官方验证，信用成本改善须同债券同窗口。 |
| 失效条件 | 项目延误、融资稀释加速或信用继续恶化与股价新低共振时下调；不把单一低量合约当信号。 |
| 观察期限 | 下一1–3个常规交易日；就业/CPI前后重评 |
| 反证 | 融资窗口未关闭，微软/Meta强于建设链；行业内部不能一刀切。 |
| 状态 | 观察中 |

## 跨期比较与上期剧本复核

对比今天07:15早报：完整交易日未改变，量比与均线不当新证据。SPY约768仍在早报767.57附近，但QQQ约688仅靠近687.87防线；SMH约492.5已低于497.33，MU约769低于782、SNDK约994低于1014。AI反弹的止跌条件尚未满足；盘前触发只记警报，不能称常规日线已确认。新增英国加息，Coherent盈利增长提供行业内部反证。Cboe官方补齐4日VIX。相同规则合约变化：3215008 +0.00个百分点；2176270 +0.00个百分点；2252540 +0.00个百分点；691340 +1.45个百分点；4838928 +0.50个百分点；5939428 -0.50个百分点；6639362 +0.00个百分点；5401796 +0.00个百分点；2413330 +1.60个百分点；2745561 +5.50个百分点；5123855 -0.25个百分点；5123856 +0.00个百分点；1343533 +0.00个百分点。就业合约是新跟踪基线；不同分档价格不相加当客观分布。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-04/20261104T232659.811257Z/evidence.json",
    "baseline_cutoff": "2026-11-04T23:26:45.506909+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.019646599816258714,
      "CL=F": 0.09086986622302007,
      "BZ=F": -0.010561668737207874,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.004900191310619473,
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
      "AAPL": {
        "change_pct": 0.6372873804818324,
        "from_observed_at": "2026-11-04T23:23:22+00:00",
        "to_observed_at": "2026-11-05T12:01:02+00:00"
      },
      "AMD": {
        "change_pct": -3.4128352563021824,
        "from_observed_at": "2026-11-04T23:25:24+00:00",
        "to_observed_at": "2026-11-05T12:01:07+00:00"
      },
      "AMZN": {
        "change_pct": 1.5942061726024193,
        "from_observed_at": "2026-11-04T23:24:55+00:00",
        "to_observed_at": "2026-11-05T12:00:59+00:00"
      },
      "ARM": {
        "change_pct": -3.072033898305093,
        "from_observed_at": "2026-11-04T23:25:13+00:00",
        "to_observed_at": "2026-11-05T12:00:48+00:00"
      },
      "AVGO": {
        "change_pct": -2.037521841758372,
        "from_observed_at": "2026-11-04T23:24:56+00:00",
        "to_observed_at": "2026-11-05T12:00:50+00:00"
      },
      "BABA": {
        "change_pct": 4.436439472935838,
        "from_observed_at": "2026-11-04T23:21:37+00:00",
        "to_observed_at": "2026-11-05T12:00:35+00:00"
      },
      "CAT": {
        "change_pct": -1.2272727272727213,
        "from_observed_at": "2026-11-04T23:24:33+00:00",
        "to_observed_at": "2026-11-05T12:00:00+00:00"
      },
      "COIN": {
        "change_pct": -0.2835850425377595,
        "from_observed_at": "2026-11-04T23:14:24+00:00",
        "to_observed_at": "2026-11-05T11:53:29+00:00"
      },
      "CRWV": {
        "change_pct": -3.8950389503894955,
        "from_observed_at": "2026-11-04T23:24:19+00:00",
        "to_observed_at": "2026-11-05T12:00:45+00:00"
      },
      "DRAM": {
        "change_pct": -4.553107743703877,
        "from_observed_at": "2026-11-04T23:24:39+00:00",
        "to_observed_at": "2026-11-05T12:01:03+00:00"
      },
      "GDX": {
        "change_pct": 3.017037387600574,
        "from_observed_at": "2026-11-04T23:25:05+00:00",
        "to_observed_at": "2026-11-05T12:00:12+00:00"
      },
      "GEV": {
        "change_pct": -2.173420566439932,
        "from_observed_at": "2026-11-04T23:19:56+00:00",
        "to_observed_at": "2026-11-05T12:00:25+00:00"
      },
      "GLD": {
        "change_pct": 1.764706989890108,
        "from_observed_at": "2026-11-04T23:10:24+00:00",
        "to_observed_at": "2026-11-05T12:00:56+00:00"
      },
      "GLW": {
        "change_pct": -3.066172672648626,
        "from_observed_at": "2026-11-04T23:19:20+00:00",
        "to_observed_at": "2026-11-05T12:00:24+00:00"
      },
      "GOOGL": {
        "change_pct": 0.09084676037023343,
        "from_observed_at": "2026-11-04T23:25:21+00:00",
        "to_observed_at": "2026-11-05T12:00:56+00:00"
      },
      "INTC": {
        "change_pct": -1.9756055660539396,
        "from_observed_at": "2026-11-04T23:25:29+00:00",
        "to_observed_at": "2026-11-05T12:01:00+00:00"
      },
      "IWM": {
        "change_pct": 0.28577774279159307,
        "from_observed_at": "2026-11-04T23:24:20+00:00",
        "to_observed_at": "2026-11-05T12:00:16+00:00"
      },
      "LITE": {
        "change_pct": -2.0981403952876954,
        "from_observed_at": "2026-11-04T23:24:46+00:00",
        "to_observed_at": "2026-11-05T12:00:22+00:00"
      },
      "LLY": {
        "change_pct": 1.0378040600176552,
        "from_observed_at": "2026-11-04T23:23:43+00:00",
        "to_observed_at": "2026-11-05T12:00:54+00:00"
      },
      "META": {
        "change_pct": 1.072151237353336,
        "from_observed_at": "2026-11-04T23:24:52+00:00",
        "to_observed_at": "2026-11-05T12:00:55+00:00"
      },
      "MRVL": {
        "change_pct": -2.899138073612839,
        "from_observed_at": "2026-11-04T23:24:33+00:00",
        "to_observed_at": "2026-11-05T12:00:56+00:00"
      },
      "MSFT": {
        "change_pct": 0.6036797433910612,
        "from_observed_at": "2026-11-04T23:24:43+00:00",
        "to_observed_at": "2026-11-05T12:00:58+00:00"
      },
      "MU": {
        "change_pct": -3.1241339346451458,
        "from_observed_at": "2026-11-04T23:25:32+00:00",
        "to_observed_at": "2026-11-05T12:01:06+00:00"
      },
      "NOW": {
        "change_pct": 0.4599816007359703,
        "from_observed_at": "2026-11-04T23:24:23+00:00",
        "to_observed_at": "2026-11-05T12:00:30+00:00"
      },
      "NVDA": {
        "change_pct": -1.5513867674490034,
        "from_observed_at": "2026-11-04T23:25:29+00:00",
        "to_observed_at": "2026-11-05T12:01:01+00:00"
      },
      "ORCL": {
        "change_pct": -0.8045052292839916,
        "from_observed_at": "2026-11-04T23:24:40+00:00",
        "to_observed_at": "2026-11-05T12:00:50+00:00"
      },
      "PLTR": {
        "change_pct": -2.486203891954686,
        "from_observed_at": "2026-11-04T23:24:48+00:00",
        "to_observed_at": "2026-11-05T12:01:05+00:00"
      },
      "QCOM": {
        "change_pct": -2.6533275337103146,
        "from_observed_at": "2026-11-04T23:24:37+00:00",
        "to_observed_at": "2026-11-05T12:00:57+00:00"
      },
      "QQQ": {
        "change_pct": -0.5553371963643139,
        "from_observed_at": "2026-11-04T23:25:22+00:00",
        "to_observed_at": "2026-11-05T12:00:54+00:00"
      },
      "RSP": {
        "change_pct": 0.20111731843575065,
        "from_observed_at": "2026-11-04T23:20:48+00:00",
        "to_observed_at": "2026-11-05T11:54:48+00:00"
      },
      "SMH": {
        "change_pct": -2.1322258211950884,
        "from_observed_at": "2026-11-04T23:24:45+00:00",
        "to_observed_at": "2026-11-05T12:00:56+00:00"
      },
      "SNDK": {
        "change_pct": -3.8152571572366067,
        "from_observed_at": "2026-11-04T23:24:41+00:00",
        "to_observed_at": "2026-11-05T12:01:01+00:00"
      },
      "SPY": {
        "change_pct": 0.04819277108434328,
        "from_observed_at": "2026-11-04T23:23:54+00:00",
        "to_observed_at": "2026-11-05T12:00:58+00:00"
      },
      "TLT": {
        "change_pct": 0.1835210577864732,
        "from_observed_at": "2026-11-04T23:07:41+00:00",
        "to_observed_at": "2026-11-05T12:00:39+00:00"
      },
      "VRT": {
        "change_pct": -3.356744974570103,
        "from_observed_at": "2026-11-04T23:22:09+00:00",
        "to_observed_at": "2026-11-05T12:01:01+00:00"
      },
      "XLE": {
        "change_pct": 0.6933501418216137,
        "from_observed_at": "2026-11-04T23:20:59+00:00",
        "to_observed_at": "2026-11-05T12:00:00+00:00"
      },
      "XLF": {
        "change_pct": 1.1997296383913447,
        "from_observed_at": "2026-11-04T23:20:28+00:00",
        "to_observed_at": "2026-11-05T12:00:47+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-03"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-03"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-03"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-03"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-03"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-04"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-30"
      },
      "CBOE_VIX": {
        "change": -4.219999999999999,
        "unit": "index",
        "observation_date": "2026-11-04"
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
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "691340": {
        "status": "comparable",
        "change_pp": 1.45
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.5000000000000004
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5939428": {
        "status": "comparable",
        "change_pp": -0.5000000000000004
      },
      "5401796": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2413330": {
        "status": "comparable",
        "change_pp": 1.6000000000000014
      },
      "2745561": {
        "status": "comparable",
        "change_pp": 5.500000000000001
      },
      "5123855": {
        "status": "comparable",
        "change_pp": -0.2499999999999999
      },
      "5123856": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "1343533": {
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
    "event": "Cigna已到业绩发布时间；管理层电话会，具体本季数字原文仍未获取",
    "date": "2026-11-05T08:30:00-05:00",
    "source": "https://newsroom.thecignagroup.com/2026-10-09-The-Cigna-Groups-Third-Quarter-2026-Earnings-Release-Details"
  },
  {
    "event": "10月就业报告",
    "date": "2026-11-06T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "10月CPI",
    "date": "2026-11-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA财报电话会",
    "date": "2026-11-17T17:00:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  },
  {
    "event": "财政部3年/10年/30年再融资拍卖：11月9/10/12日各13:00美东；11月16日计划结算",
    "date": "2026-11-09T13:00:00-05:00",
    "source": "https://home.treasury.gov/news/press-releases/sb0678/"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| boe-hike | 英国央行8比1加息25bp至4%；另一票希望50bp，不能视为Fed动作。 | 2026-11-05T12:00:00+00:00 | [{"source": "https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026", "published_at": "2026-11-05T12:00:00+00:00", "retrieved_at": "2026-11-05T12:08:53.573272+00:00"}] |
| cohr-earnings | Coherent Q1收入23.7亿美元同比约50%，non-GAAP毛利40.6%、EPS2.09；Q2收入指引25.5–27.5亿。 | 2026-11-04T16:05:00-05:00 | [{"source": "https://ir.coherent.com/news-releases/news-release-details/coherent-corp-reports-first-quarter-fiscal-2027-results", "published_at": "2026-11-04T16:05:00-05:00", "retrieved_at": "2026-11-05T12:08:53.573272+00:00"}] |
| h200-old-news | H200少量入华与香港等待线索和8月18日Reuters已报事实重合，本次未核验新的大规模许可，不按新利好计。 | 缺失 | [{"source": "https://www.investing.com/news/stock-market-news/nvidia-h200-chips-reach-china-in-small-shipments-ft-reports-4866385", "published_at": null, "retrieved_at": "2026-11-05T12:08:53.573272+00:00"}] |
| meta-supplement | 5日新424B5属于既有150亿美元融资的补充文件，不重复计算为又一笔新增债务。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526448015/d135326d424b5.htm", "published_at": null, "retrieved_at": "2026-11-05T12:08:53.573272+00:00"}] |
| ci-call | 官方确定5日8:30美东电话会；tc给出的EPS7.98/全年30.60尚未取得结果原文，仅作线索，未用作核心判断。 | 缺失 | [{"source": "https://newsroom.thecignagroup.com/2026-10-09-The-Cigna-Groups-Third-Quarter-2026-Earnings-Release-Details", "published_at": null, "retrieved_at": "2026-11-05T12:08:53.573272+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN418、CME超时，缺失不替代；全成分涨跌家数和高于均线比例缺失。",
  "tc高影响新闻43条、查询limit50无has_more，但仅覆盖指定两天与高影响筛选，不代表全市场新闻覆盖。",
  "盘前报价异步、部分ETF稀疏，报价时间逐项保留；没有今日常规VWAP或开盘区间。文中694.07等仅为11月4日分钟量价近似。",
  "19ETF当期净申赎及发行人份额拆分桥缺失；ICI只到10月28日。上涨/放量不等于主力净买入。",
  "FRED利率信用截至3日、金融压力至10月30日、GPR2日；10年收益率备用指数仍4日，不能写实时利率下降。",
  "四家公司企业FCFF底稿未完备，NVDA保留既有租赁近似与假设局限；无新财报不编新基本面。",
  "Cigna官网动态结果未提取成功，tc EPS/指引数字仅线索；H200新闻新颖性未确认；伊朗油轮触雷为单方宣称，未核验独立损害，不写既成封锁。",
  "Polymarket搜索有截断与同名噪声；Oracle/NVDA/就业合约低量；不同到期、分档不可直接加总或替换。",
  "COHR官方网页由web工具成功读取，直接requests403；英国央行已读正式决定，搜索缓存仍显示旧3.75%不采用。",
  "期货为连续代码，换月与延迟未消除；H100页首7D与历史/FAQ口径冲突，只使用明确日期值。",
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
  "tc 报价质量 stale: CVX, TAN, XLI, XLV, XOM；不作为新成交证据",
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
  "request.38906ddc2d63: request_failed",
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.CVX.value, quotes.TAN.value, quotes.XLI.value, quotes.XLV.value, quotes.XOM.value, latest.TNX.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://ecommerce.ismworld.org/SSO/Login.aspx?DPLF=Y&vi=10&vt=94b6a992da90ad8a8ea93a8073f390759d48e3339f2146ab07fa2f46b1f1f3df0fdc9a0094757e6b3c9471f5c81e6ad80958c235e67be91a978a547a29dcc4df21370a624cf2f3f406f8b12f9d559d8482d68f5611e6a3f72696ffc31e98c86eba035508cd154cbebe25411ff118e73dce359bdf5561d04978add8883dea9933",
    "checked_at": "2026-11-04T23:20:55.839037+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://newsroom.arm.com/news/arm-q2-fye27-results",
    "checked_at": "2026-11-05T12:01:05.759069+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526447522/d154804dfwp.htm",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://news.microsoft.com/source/2026/10/29/microsoft-announces-debt-offerings-7/",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://investors.terawulf.com/news-events/press-releases",
    "checked_at": "2026-11-05T12:01:08.132875+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-05T12:01:02.891933+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://investor.nvidia.com/events-and-presentations/events-and-presentations/default.aspx",
    "checked_at": "2026-11-05T12:01:02.632871+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-05T12:01:01.289728+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-05T12:01:01.671951+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://home.treasury.gov/news/press-releases/sb0678/",
    "checked_at": "2026-11-05T12:01:13.840147+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-05T12:01:02.379421+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/services/october/",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://investor.qualcomm.com/files/content_files/FY2026-4th-Quarter-Earnings-Release.pdf",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://www.texastribune.org/2026/11/04/data-center-texas-pause-gina-hinojosa-governor-policies/",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://apnews.com/article/4d12764c0b3ce38ffde3077712811182",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ARM",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COIN",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CRWV",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GDX",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LITE",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MRVL",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-11-04T23:25:37.996035+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QCOM",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TAN",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1633978/000162828026068655/lite-20261102.htm",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx",
    "checked_at": "2026-11-04T23:26:45.076502+00:00",
    "note": "早报已核验的历史证据，本次未重复抓取；不是新增事件"
  },
  {
    "url": "https://ecommerce.ismworld.org/SSO/Login.aspx?DPLF=Y&vi=10&vt=7cba24803cd4e908a67d0a0a6bcdf4c6c0ea255ba4d63e37a58999fbb63156ab6a97ec1f4e1ae73dc44e2e29262e7e29ccb3ed692a7e69fb37543efd719feaa722b184b9131ed18a1226664cef48a9b2c02da88f0f4d8d60bc92ff7822398a5f15345ead7aa3ff249f7b37c429896cdda93a97aaee5261245a79899bf8292d02",
    "checked_at": "2026-11-05T12:01:05.663766+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/november-2026",
    "checked_at": "2026-11-05T12:08:53.573272+00:00",
    "note": "本次web原文或搜索摘要核验，未知时间留空"
  },
  {
    "url": "https://investors.thecignagroup.com/overview/default.aspx",
    "checked_at": "2026-11-05T12:05:32.241793+00:00",
    "note": "本次公开页面检查；动态缺项见缺口"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526448015/d135326d424b5.htm",
    "checked_at": "2026-11-05T12:08:53.573272+00:00",
    "note": "本次web原文或搜索摘要核验，未知时间留空"
  },
  {
    "url": "https://ir.coherent.com/news-releases/news-release-details/coherent-corp-reports-first-quarter-fiscal-2027-results",
    "checked_at": "2026-11-05T12:08:53.573272+00:00",
    "note": "本次web原文或搜索摘要核验，未知时间留空"
  },
  {
    "url": "https://newsroom.thecignagroup.com/2026-10-09-The-Cigna-Groups-Third-Quarter-2026-Earnings-Release-Details",
    "checked_at": "2026-11-05T12:08:53.573272+00:00",
    "note": "本次web原文或搜索摘要核验，未知时间留空"
  },
  {
    "url": "https://www.investing.com/news/stock-market-news/nvidia-h200-chips-reach-china-in-small-shipments-ft-reports-4866385",
    "checked_at": "2026-11-05T12:08:53.573272+00:00",
    "note": "本次web原文或搜索摘要核验，未知时间留空"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CI",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COHR",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COP",
    "checked_at": "2026-11-05T12:01:11.278539+00:00",
    "note": "真实分钟时间；盘前不能当常规成交"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
