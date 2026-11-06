# 每日交易总结 · 2026-11-05

## 一分钟读懂 · Agent 摘要

### 当前判断

恐慌后的盘前反抽已出现，但尚不足以确认可靠反弹，更不能称趋势反转。先等今晚就业数据，再看常规开盘后的回踩与收盘承接。

### 与上次相比

相较早报，芯片价格明显修复、VIX从昨日收盘28.18回到盘前约26.57；等权RSP仍弱，AI融资风险未随股价同步消失。

### 最重要的信号

- 20:02北京时间附近：SPY较昨收约+0.33%、QQQ+1.70%、SMH+5.58%，RSP约-0.13%。涨幅集中，不能当全市场资金回流。
- SoftBank信用保护成本升高；Anthropic年内IPO合约较早报回落。融资兑现仍须独立核验。
- Counterpoint称Q3存储价格仍强、CXMT收入份额由10%降至9%；AWS新增园区计划也是需求仍在的反证，但不保证订单如期兑现。

### 接下来观察

- 21:30北京非农、23:00密歇根初值；工资、失业率与通胀预期一起看，不能只看就业总数。
- 开盘后30–60分钟守住昨日收盘、低点抬高，突破开盘区间后回踩不破，并有RSP/更多板块配合，才逐级提高反弹可信度。
- 芯片以SMH447.73为首道修复底线，483.93为昨日日内高点观察；防御板块仍看相对强弱，避免把盘前跳涨当新趋势。

### 不要忽略

真实全成分广度、可靠常规VWAP、当期ETF净申赎及CNN缺失；就业尚未发布。盘前报价异步，部分宏观滞后。

## 研究结论

11月6日晚报：芯片盘前强反抽，等权未跟随；就业与通胀预期发布前仍是脆弱修复。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-05 → 2026-11-05（纽约交易日） |
| 截止·纽约 | 2026-11-06T07:08:34.157113-05:00 |
| 截止·北京 | 2026-11-06T20:08:34.157113+08:00 |
| 实际生成时间 | 2026-11-06T12:08:34.488593+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-11-06 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-11-05/20261105T232152.239453Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-06T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1219847 | 已校验接入 | https://gamma-api.polymarket.com/events/1219847 | 2026-11-06T12:02:44.615322+00:00 / 2026-11-06T12:02:44.615322+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-11-06T12:02:44.666384+00:00 / 2026-11-06T12:02:44.666384+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-11-06T12:02:47.952945+00:00 / 2026-11-06T12:02:47.952945+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1038648 | 未接入 | 缺失 |  /  | 没有可核验的活跃Yes合约 |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-11-06T12:02:48.010405+00:00 / 2026-11-06T12:02:48.010405+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1103684 | 已校验接入 | https://gamma-api.polymarket.com/events/1103684 | 2026-11-06T12:02:49.472044+00:00 / 2026-11-06T12:02:49.472044+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 199777 | 已校验接入 | https://gamma-api.polymarket.com/events/199777 | 2026-11-06T12:02:49.825217+00:00 / 2026-11-06T12:02:49.825217+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1308738 | 已校验接入 | https://gamma-api.polymarket.com/events/1308738 | 2026-11-06T12:03:55.895803+00:00 / 2026-11-06T12:03:55.895803+00:00 | Gamma observation; rule and expiration retained |
| 1120074 | 已校验接入 | https://gamma-api.polymarket.com/events/1120074 | 2026-11-06T12:03:55.896458+00:00 / 2026-11-06T12:03:55.896458+00:00 | Gamma observation; rule and expiration retained |
| 1120075 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |

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
| prices.SPY.value | 733.00 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -4.41 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -4.73 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -5.29 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -4.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 765.53 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 765.83 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 727.39 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -4.25 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -4.29 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 0.77 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 10.97 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.50 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -5.92 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 3.06 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 647.05 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -6.49 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -9.55 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -13.45 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -10.50 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -2.08 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -4.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -8.16 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -5.62 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 712.40 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 722.03 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 679.61 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -9.17 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -10.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | -4.79 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 16.42 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.54 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -14.82 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 2.99 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 270.98 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -4.59 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | -4.59 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -2.37 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -10.25 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | -0.18 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 0.14 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 2.91 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -5.37 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.11 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 282.45 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.99 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | -2.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -4.06 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | -2.52 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 4.58 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.69 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -10.95 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 2.09 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 216.87 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -2.89 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | -1.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 2.36 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -1.54 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 1.52 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 3.29 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 7.65 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 3.34 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 216.57 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 207.00 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 0.14 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.04 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 4.77 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.67 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.23 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -2.89 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 2.75 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 375.49 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 0.81 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | 1.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -0.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -7.27 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | 5.21 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 6.60 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | 4.46 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -2.39 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 373.39 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 385.96 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 411.64 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | 0.56 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -2.71 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -8.78 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 6.44 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.72 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -12.28 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.40 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,113.50 | USD_per_troy_ounce | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 0.99 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | 2.04 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -1.05 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -7.92 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 5.40 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | 6.76 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | 4.24 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -3.05 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,087.78 | USD_per_troy_ounce | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,242.20 | USD_per_troy_ounce | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,505.69 | USD_per_troy_ounce | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | 0.63 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -3.03 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -8.70 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 83.16 | USD_per_troy_ounce | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 2.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -12.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 1.46 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 90.52 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 2.72 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -11.25 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | -1.06 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 8.71 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 7.13 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -6.53 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 4.23 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 13.58 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 98.06 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 95.32 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 87.00 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -7.69 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | -5.04 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 4.05 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 5.23 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 5.78 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -14.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 1.61 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 98.29 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | 3.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -14.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | -5.74 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 10.46 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | 8.29 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -9.72 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | -0.46 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 15.34 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 108.74 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 104.03 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 93.17 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -9.61 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | -5.52 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 5.49 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 5.53 | USD_per_barrel | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 5.63 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -16.45 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 1.71 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.93 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | 0.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.54 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 5.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | 0.16 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 4.62 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 5.27 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 10.50 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 5.04 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 80.52 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.38 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.46 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 1.75 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.92 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.77 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.94 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 1.33 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.92 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.07 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.41 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | -0.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 2.55 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 4.48 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 4.31 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 5.08 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 7.43 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.66 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.96 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | -0.26 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 0.89 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.10 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.35 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.72 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.28 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.31 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.18 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -2.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | 4.10 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 4.34 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 5.47 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 2.48 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.16 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.83 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 78.19 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.15 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.71 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.16 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.33 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.77 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 1.38 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.66 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.15 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.42 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.14 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | 4.56 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 5.15 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 7.43 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 3.91 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.60 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.88 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 106.19 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.76 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.61 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.58 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.65 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.66 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 28.18 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 69.66 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 63.84 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 82.87 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 92.62 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 74.07 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 68.56 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 88.16 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 98.15 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 18.29 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.70 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.35 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 54.09 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 68.76 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 53.58 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 3.21 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 11.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-05 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 25.55 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 35.90 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 31.90 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 41.32 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 37.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 40.31 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 36.63 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 46.60 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 42.76 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 19.77 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.85 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.55 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 29.22 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 35.51 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 24.32 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.79 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 7.01 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-05 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 134.99 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 49.31 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 37.73 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 53.99 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 52.53 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 53.72 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 42.46 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 59.28 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 57.41 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 100.73 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 93.55 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.91 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 34.01 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 44.29 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 36.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 13.35 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 9.89 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-05 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 97.92 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 4.30 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | 4.68 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -4.52 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 25.67 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 8.71 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | 9.41 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | 1.17 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 30.31 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 99.62 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 92.35 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 78.31 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -1.71 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 6.04 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 25.05 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 4.92 | index | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -13.80 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-05 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 181.60 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -9.26 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -15.01 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -21.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -18.87 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -4.85 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -10.28 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -15.92 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -13.99 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 213.68 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 220.59 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.38 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -15.01 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -17.68 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -11.15 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 7.46 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 4.11 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -24.09 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 2.93 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 535.93 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -3.58 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | 1.09 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 2.55 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 9.04 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | 0.83 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | 5.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 7.84 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 13.92 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 531.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 516.13 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 438.43 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 0.81 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 3.84 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 22.24 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 15.42 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -3.58 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.76 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 260.21 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | -2.19 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | 6.74 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 2.42 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -2.65 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 2.22 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 11.46 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 7.71 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | 2.23 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.43 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 253.89 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.82 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | 2.27 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | 2.49 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 6.72 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 10.34 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.97 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -6.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 1.87 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 282.57 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -2.20 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -0.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -18.87 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -17.69 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 2.21 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | 4.29 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -13.58 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -12.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 320.79 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 334.02 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 339.44 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -11.91 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -15.40 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -16.75 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 11.16 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.95 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -20.91 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.45 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 605.08 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -3.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -3.11 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -16.06 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 4.61 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | 0.45 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | 1.61 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -10.78 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 9.49 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 668.10 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 673.98 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.33 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -9.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -10.22 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -4.16 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 23.47 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -22.19 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.17 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 43.66 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -9.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -28.12 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -46.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -59.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -5.42 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -23.39 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -41.19 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -54.60 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 61.11 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 76.37 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 90.40 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -28.55 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -42.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -51.70 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 5.82 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 13.33 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -59.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.31 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 656.39 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -17.46 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -29.74 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -36.62 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -27.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -13.05 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -25.02 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -31.33 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -23.08 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 895.93 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 966.44 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 755.06 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -26.74 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -32.08 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | -13.07 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 57.39 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 8.74 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -40.18 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 2.85 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 37.01 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -17.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -28.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -34.99 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -32.46 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -13.55 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -23.76 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -29.70 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -27.59 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 48.87 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 55.00 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-05 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -24.27 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -32.70 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-05 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 3.20 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 8.64 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -41.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 2.93 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 176.73 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -14.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | -28.14 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -27.49 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -38.70 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -9.61 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | -23.41 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -22.20 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -33.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 217.37 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 238.71 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 271.12 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -18.69 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -25.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -34.81 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 18.37 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 10.40 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -39.84 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 2.51 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 162.38 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -8.00 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -13.97 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -17.90 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -13.92 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -3.59 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -9.24 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -12.61 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -9.04 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 185.23 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 188.85 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.81 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -12.34 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -14.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | -4.38 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 5.45 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 3.35 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -19.61 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 3.29 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 61.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -2.98 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -10.30 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | -5.53 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 1.58 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 1.43 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -5.58 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | -0.24 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 6.46 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 67.28 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.96 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.51 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -8.40 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | -5.13 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 5.34 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.81 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.94 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -11.98 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.96 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 57.50 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -2.87 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.98 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 6.03 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -0.37 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 1.54 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 5.71 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 11.32 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 4.50 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 56.11 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.87 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.50 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 2.93 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 7.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.96 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.67 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -2.87 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 2.08 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 162.47 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | -4.12 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | -4.50 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -3.52 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -12.36 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.28 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 0.22 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 1.77 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -7.48 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 167.84 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 169.64 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.65 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -3.20 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -4.23 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -5.90 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 3.20 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.97 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -12.66 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 2.35 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 184.91 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -2.50 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 0.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 9.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 10.20 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 1.90 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 5.20 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 15.25 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 15.07 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 179.28 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 172.91 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 158.29 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.14 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 6.94 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 16.82 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.60 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.95 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -2.50 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 2.39 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 91.25 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -0.75 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 3.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 9.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 7.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 3.66 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 8.21 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 14.67 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 12.83 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 87.76 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.77 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.78 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 3.97 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 7.65 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.92 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.67 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -0.75 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 2.17 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 117.64 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -3.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 1.24 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 5.31 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | 0.01 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.58 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 5.97 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 10.60 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 4.88 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 115.03 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.24 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.12 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.27 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 3.89 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 2.18 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 2.45 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 2.08 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.83 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 2.54 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 104.34 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -0.59 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | 3.09 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -6.90 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -5.07 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 3.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | 7.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -1.61 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -0.19 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 106.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 109.82 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.13 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -2.15 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -4.99 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -6.94 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 2.06 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.98 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -9.07 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.80 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.30 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.71 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 0.37 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 5.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -0.51 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 3.70 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 5.10 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 10.72 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 4.37 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.48 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.68 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.83 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 1.93 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 3.90 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -1.20 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -1.56 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.81 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 44.30 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -1.82 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 2.88 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 8.45 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | 0.41 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 2.59 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 7.61 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 13.73 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 5.29 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 42.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.45 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.84 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 3.93 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 4.35 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 3.41 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.73 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.66 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -1.82 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.48 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 52.33 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | -2.91 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | -0.38 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 6.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | -0.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 1.50 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 4.35 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 11.50 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 4.86 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 51.45 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.88 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.82 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 1.71 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 2.85 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 2.96 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.92 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.76 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -2.91 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 2.06 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 447.73 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -11.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -20.29 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -26.27 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -23.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -6.80 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -15.56 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -20.98 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -18.57 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 543.91 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 567.82 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 521.45 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -17.68 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -21.15 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -14.14 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 23.94 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 5.35 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -29.37 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 2.85 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 99.01 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -4.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -8.30 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -9.65 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -3.95 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | 0.02 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -3.57 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -4.37 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 0.93 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 107.60 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.93 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 94.04 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -7.98 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -7.41 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 5.28 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.03 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.06 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -12.12 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.82 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 174.10 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -2.89 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -12.74 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | -10.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | -2.12 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | 1.51 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -8.01 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | -4.73 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 2.76 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 196.14 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.35 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 170.67 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -11.24 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | -9.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 2.01 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 6.20 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 3.56 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -15.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.42 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 347.65 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -5.03 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -14.77 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -10.05 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | -15.87 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -0.62 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -10.04 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | -4.76 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | -11.00 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 388.73 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 398.22 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 398.49 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -10.57 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -12.70 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -12.76 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 14.44 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 4.15 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -20.37 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 1.63 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 68.11 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -4.00 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | -4.65 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -0.27 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -18.70 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 0.41 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 0.07 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 5.02 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -13.82 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 69.28 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 70.93 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 76.01 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | -1.68 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -3.97 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -10.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 1.91 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.80 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -19.21 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.06 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 27.05 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -6.48 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -12.73 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -15.67 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -22.04 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -2.07 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -8.00 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -10.38 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -17.16 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 30.22 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.46 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.37 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -10.52 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -14.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -16.46 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.93 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 3.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -22.42 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 2.80 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.31 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -2.46 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | -0.75 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 3.91 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -6.02 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 1.95 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 3.97 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 9.20 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -1.14 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 71.32 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.73 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.47 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 1.39 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.81 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 2.61 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.63 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 2.26 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.68 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.58 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 147.17 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -6.08 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -12.10 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -13.50 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -9.47 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -1.67 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -7.37 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -8.21 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | -4.59 | pp | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 164.30 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.31 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 137.13 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -10.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -10.43 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 7.32 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.06 | USD_per_share | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.44 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -15.85 | percent | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 0.63 | ratio | 2026-11-05 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.58 | percent | 2026-11-04 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.32 | percentage_points | 2026-11-04 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.91 | percentage_points | 2026-11-04 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.90 | percent | 2026-11-04 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.64 | percent | 2026-11-04 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.24 | percent | 2026-11-05 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.52 | index | 2026-10-30 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 28.18 | index | 2026-11-05 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 97.67 | index | 2026-11-02 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 113.60 | index | 2026-11-02 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 94.75 | index | 2026-11-02 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 137.64 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 164.04 | index | 2026-11-02 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AAPL.value | 340.60 | USD_per_share | 2026-11-06T12:02:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| quotes.AMD.value | 436.04 | USD_per_share | 2026-11-06T12:02:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.AMZN.value | 262.78 | USD_per_share | 2026-11-06T12:02:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.ARM.value | 178.02 | USD_per_share | 2026-11-06T12:02:33+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ARM |
| quotes.AVGO.value | 305.91 | USD_per_share | 2026-11-06T12:02:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.BABA.value | 107.04 | USD_per_share | 2026-11-06T12:02:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BABA |
| quotes.CAT.value | 570.94 | USD_per_share | 2026-11-06T12:02:45+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.CEG.value | 242.00 | USD_per_share | 2026-11-06T11:57:31+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.CI.value | 298.00 | USD_per_share | 2026-11-06T11:47:15+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CI |
| quotes.COHR.value | 186.23 | USD_per_share | 2026-11-06T12:02:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COHR |
| quotes.COIN.value | 137.80 | USD_per_share | 2026-11-06T12:02:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COIN |
| quotes.COP.value | 134.50 | USD_per_share | 2026-11-06T10:02:38+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COP |
| quotes.CRWV.value | 47.29 | USD_per_share | 2026-11-06T12:02:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CRWV |
| quotes.CVX.value | 211.93 | USD_per_share | 2026-11-06T11:27:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.DRAM.value | 40.42 | USD_per_share | 2026-11-06T12:02:39+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GDX.value | 85.27 | USD_per_share | 2026-11-06T12:01:36+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GDX |
| quotes.GEV.value | 793.24 | USD_per_share | 2026-11-06T12:02:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 372.18 | USD_per_share | 2026-11-06T12:01:22+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 110.20 | USD_per_share | 2026-11-06T12:00:45+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 283.79 | USD_per_share | 2026-11-06T12:02:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 99.53 | USD_per_share | 2026-11-06T11:33:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.INTC.value | 55.71 | USD_per_share | 2026-11-06T12:02:50+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.IWM.value | 271.16 | USD_per_share | 2026-11-06T12:02:28+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.LITE.value | 562.00 | USD_per_share | 2026-11-06T12:02:43+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LITE |
| quotes.LLY.value | 1,344.00 | USD_per_share | 2026-11-06T12:02:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| quotes.META.value | 604.68 | USD_per_share | 2026-11-06T12:02:31+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MRVL.value | 146.77 | USD_per_share | 2026-11-06T12:02:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MRVL |
| quotes.MSFT.value | 530.61 | USD_per_share | 2026-11-06T12:02:42+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 714.00 | USD_per_share | 2026-11-06T12:02:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 101.53 | USD_per_share | 2026-11-06T12:02:41+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 188.82 | USD_per_share | 2026-11-06T12:02:43+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.ORCL.value | 119.38 | USD_per_share | 2026-11-06T12:02:44+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.PLTR.value | 159.00 | USD_per_share | 2026-11-06T12:02:51+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.QCOM.value | 162.50 | USD_per_share | 2026-11-06T12:02:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QCOM |
| quotes.QQQ.value | 658.02 | USD_per_share | 2026-11-06T12:02:44+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 216.60 | USD_per_share | 2026-11-06T12:00:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 472.70 | USD_per_share | 2026-11-06T12:02:33+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 900.07 | USD_per_share | 2026-11-06T12:02:47+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 735.40 | USD_per_share | 2026-11-06T12:02:36+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 501.24 | USD_per_share | 2026-11-06T12:02:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TAN.value | 45.05 | USD_per_share | 2026-11-06T11:27:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TAN |
| quotes.TLT.value | 81.69 | USD_per_share | 2026-11-06T12:01:12+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 190.93 | USD_per_share | 2026-11-06T12:02:12+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 61.53 | USD_per_share | 2026-11-06T12:00:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 57.00 | USD_per_share | 2026-11-06T12:00:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.XLI.value | 162.51 | USD_per_share | 2026-11-06T09:04:50+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLI |
| quotes.XLV.value | 182.16 | USD_per_share | 2026-11-06T11:42:25+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.XOM.value | 165.00 | USD_per_share | 2026-11-06T11:38:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| latest.BZ_F.value | 98.48 | USD/barrel | 2026-11-06T11:52:48+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| latest.CL_F.value | 90.73 | USD/barrel | 2026-11-06T11:52:48+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| latest.DX-Y.NYB.value | 101.96 | index points | 2026-11-06T11:52:54+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |
| latest.ES_F.value | 7,411.25 | index points | 2026-11-06T11:52:47+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| latest.GC_F.value | 4,078.10 | USD/troy_oz | 2026-11-06T11:52:50+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| latest.NQ_F.value | 27,218.00 | index points | 2026-11-06T11:52:50+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| latest.TNX.value | 4.84 | percent | 2026-11-05T19:59:00+00:00 | lagged | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| latest.VIX.value | 26.57 | index points | 2026-11-06T11:47:46+00:00 | lagged | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -33.80999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -36.3599853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.060931502733092,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.027202819504561,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.013854948254337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.432842693298834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.9492053952847495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.991479246337605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.636860553530043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.068732910243135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.0464996337890398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.636505126953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.6236474609374909,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.0465649414062455,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2645596313476517,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7568945312500546,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.1494962989853885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.0150962942206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.333356098469299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.610699025078047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.686497018416147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.254799280217082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.5349993024553577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.8657182965959827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.26618006141307893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.573201716729966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.339677879725434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.66698123428908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.486742374108423,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.01034865959201,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -44.9000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -68.2900390625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.462233808824815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.07355639443351,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.907662478351205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.089526449945907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.766205312973415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.850504056712506,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.910109539019493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.328919581401708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.401302306091723,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.0463535749289488,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8938075300968684,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.656683756647074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8169999176886655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.8590248103748994,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.2732489854894506,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.260186671158573,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.026501464843818,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.744497680664153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.2715905761718886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.064434814453193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.16430694580071759,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.5970410156249955,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.622142366428461,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.0116277622846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.050074307534926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.039310883896214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.631383224816201,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.296390770136554,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.7235717773437482,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.863568987165177,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.41375624745980044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.78236151786988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.910542348072346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.989553415565743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.484047647035795,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.9577333709445601,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -13.03997802734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.029998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.103059556280366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.558192401862061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.558387699840151,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.240844669033087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.6500032840052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.16258427449907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.856560978813139,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.238261012214817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.042128053547274114,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.5309895823575,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.5445327515858143,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.8080019757342525,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.7007978887204502,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.828894971838535,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2197004252830963,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.16952810197168233,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.329499816894554,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.41250000000002274,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5434259033203261,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.932176513671891,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.024971923828104536,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.38678276062012173,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.584042929604526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.54982924391607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.423666349309096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.9300409449882108,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.699912429687581,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.829486365966707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5821446010044649,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9664284842354913,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.28255303004025123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.41781003770108405,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.285304388752875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.282024926520489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6449890229218593,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.2213255661023235,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.4600067138671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.1699981689453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.748830584651609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.092970121194361,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.154167662930918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.274663439208202,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.684694422043444,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.92235568630852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.112191816116394,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.0530560273050114,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.3121009180814829,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.06576730168980038,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.14031271467658213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.158179254090632,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2645109732413058,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.0691235600290856,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.5246687374136485,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.0156768829381235,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.104999542236328,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.08816436767580171,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.11723114013673808,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.09913337707519077,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5835671234131041,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1020493250966785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.4609673640172636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.9671005980068665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.4209892219581466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1725166118951487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.8319543316318576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3564278738839284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6328571864536827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.19516142643203716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3053229010566987,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.8925834688140473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.0383939144989927,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.934693420372144,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7631703691311036,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.91998291015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.877173420176371,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.1279798068997158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.1506122629065594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.9940511634012115,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.07519977755267027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.880596793269352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.1676484736616528,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.8605504591910789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.1837580825567207,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.155182626404277,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.164467211160896,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.426893856700046,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.024405172837419,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 8.872076039606958,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.46921207986839,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.208182451052056,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.15650024414060226,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.5895004272460938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.9166003417968795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.800600585937502,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.3405500793456895,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.6336001586913653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8452371533882008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.7931381783003917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.0059346184166817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.2068544234821306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8035977532808047,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.0350161911874434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.17785862513950956,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.319281441824777,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.033924652874192995,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3257197390178521,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.7008199473615093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.6165540196127477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.05614560356903198,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.24402144170286122,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 40.5,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 82.10009765625,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.3707900998813924,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.492926332102762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.508331869314028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.7507312071870738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5885661805070663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.0203907034977555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3645943074485958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.5641372804783504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.6901414028516992,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.520129151607323,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.522186817568365,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 8.183573900485907,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.537771575791816,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.011869949835361,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.001454860978639,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.5045956297647844,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.174999999999727,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -40.42500000000018,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.795996093750546,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -66.04399414062482,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.619999999999891,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.313500976562864,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.0437432742068875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.974155856834293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.1984118791200205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.392107129388277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9714329749860973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.1646373969542942,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.564278738839292,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 14.971435546875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.04285648504844786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3302011327820158,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8621057023245005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7476287000210213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.41330221097125075,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.42752281707265993,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.399993896484375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.480003356933594,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 11.017852838984954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.482453103763339,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.008566441847748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.798384439840316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8789895073919807,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.891169756362807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.793148655414446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -26.895613867999305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 17.07878434171805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.5096559232679,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 7.0224213901020835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.365541746541481,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.0702158878927692,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.8996905100252,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 7.4300092089444885,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -21.826880957756167,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.04850006103515625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.2779998779296875,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.16579986572266137,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.0163998413085977,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.14949998855591673,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8685000038147024,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.4917825839938956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.080007491721123,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.356732550175245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.196882479909489,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.584264200953146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.377609050402683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.027143205915177937,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8457145690917969,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.1881619880238814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.479409853943312,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.2677821553057207,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.847588735054625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.23770163436751446,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5226088774373789,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.6699981689453125,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -16.589996337890625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 12.546620208945425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.260219655056208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.508896283947882,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.952153510529332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.17529172480059696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.03033741132012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.0407988330794185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -34.13106416632357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 18.607551711678518,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 8.287422474560769,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 7.522751232202218,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.519310817230497,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.773913670484153,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.038858164982514,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 8.677659386609461,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -29.062331256080427,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.29949989318848225,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.56450004577637,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.20900009155273835,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.2432000732421926,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1652500152587919,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9717500495910656,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.6140968765689934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.80817568487556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.3446732198667686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.28263731897085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.758522677988241,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -19.105344958116977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.05214255196707551,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7035707746233255,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.16314293935060942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.2955075921482875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.1196856409268605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.872060107998797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.05419804430897357,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.3803833359489284,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5934593250225051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.4094367931788634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.41079339750280663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8457943795914358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.7615587411232028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.34957725933566497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.30512488012134353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.209254767043777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.467472177710587,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.6177660263256977,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.60306155075153,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.27863707289027,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.1876466541615454,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.3410565056732695,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.941985433651386,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.277987677286912,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.20299987792968466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.0739997863769446,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.021040496826159938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.11362640380859546,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.013884429931650288,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.21690513610839446,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.04551900277358634,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8217231078665899,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.23810055982669276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4038752704509596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.21998082877019431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.2727836167018327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0021427699497768016,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.052142551967075845,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0006648667415624088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.06906572815839329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2044442071098218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.13445451570984757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2190265368781399,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7158878576094517,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.020000457763671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.12000083923339844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.4483874313070957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.1380238747062279,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.13735846420808162,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8976595774079388,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2750606170608405,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.4832869232540449,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.14759369183412474,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8288001843633097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.509318934040188,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.165226694210789,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.151213412462418,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.535183115890896,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.2242660123455895,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.50819232308356,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.489266861695918,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.239932725879825,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.002999973297121983,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.0005000114440925074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0179999923706049,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.10119998931884666,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.008249998092651367,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.040599994659423544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.07928899635933906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.4121331553596841,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.00642340236414185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7775773037534961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.04102587493757248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.580285954769244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0021429061889648438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.017857006617954807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.007654200626302177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.060062211040936675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.06865931458936991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.41194933982360293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6188030582607952,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.47903462634807115,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.23999786376953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3000030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.0110669328791344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.29671360123908475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.29648410452599583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.0092739867452738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.25903647424814213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7027782454085196,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.426261015581908,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.9262531037799282,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.049864569853957,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.7304892182654763,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.7173708437283413,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.423568706553561,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.6901689210366073,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.288701000929086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.210599537948134,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.142479806463207,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.006999969482421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.030999755859369316,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.04369033813476619,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.0061410522460931816,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0033235549926757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.2944723129272404,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.32013945943412114,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.4291960065015532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2524782178887519,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3775897939755746,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.30273985461414243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.758815935758006,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.004999978201729871,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.026428767613002224,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.007771946586787426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.03571775529450655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.3019433626548329,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8116940961994223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.08671748838082816,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.45209212375514995,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.160003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.598909943805559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.008978329505038296,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.009002450799155959,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4797212382589122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.21342491228941718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.00921669173983286,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.030115160660937335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5661317719289682,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.462021558927533,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.036181149009599,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.022857399053493,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.912563931557747,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.7357804829953323,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.982262554597773,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.66697571419098,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.634864682172103,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.10950012207031534,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5244998931884766,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.033472290039057384,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.08678970336913494,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.012655563354499577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.33389484405518033,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.04771787145816386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.08717976517043091,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.18644123665456647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3396879766519145,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1623968087550165,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.10479019625071473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0021427699497768016,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.023571559361049155,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0029429049460104606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.025077787674586793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1503606087898235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.009113466702170836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3527444971544398,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.05145239159025761,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 11.569999694824219,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.979999542236328,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 89.91606709249285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 67.94186184527933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 65.61129748029441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 73.4535982269183,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 72.72237795112402,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 77.92622475915479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 78.45983068687615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 79.08654795673439,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 95.97699859522595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 71.9690646647839,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 69.62515242854874,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 78.88644092021714,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 76.67158334640877,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 83.9177040054924,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 83.50658177705873,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 84.97475221111635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6385000228881843,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.4929999828338616,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2734000015258822,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6007999992370614,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.060450000762937606,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.10805000305175483,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 59.979796606543985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 51.678678633051604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 67.63471916662917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 61.91253577029218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 62.75786890117301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 59.28627476668932,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.36857148579188737,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1599999155317033,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.717441058690245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.5291648535809603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 21.465716737890883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 13.95697368746217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.75,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.179998397827148,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 47.516862171344606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 35.12381176456831,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 34.09022229049508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 35.63263212953589,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 35.22156012591422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 37.06447936703352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 38.46620841116333,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 35.66814322362937,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 53.577793674077704,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 39.151014584072875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 38.10407723874941,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 41.06547482283473,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 39.17076552119897,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 43.055958613371125,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 43.10306896469337,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 40.7368761338725,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.37349996566772603,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9275000572204597,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.15119998931884737,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3136000442504887,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.030949993133543074,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.05049999237060376,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 32.30766430791595,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 26.43398257516507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 34.9938514723738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 31.03920627849315,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 32.705872034371545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 29.838189679628236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.23500006539481033,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.658571379525321,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.268416808286422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1620564643010924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 12.962968032219358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.512191028129765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 44.58000183105469,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 36.980003356933594,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 65.12806945638687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 47.85957789768565,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 44.14839831329064,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 46.9304017773143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 45.30070162629873,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 47.471668726377686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 53.07013119954605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 44.14890359946733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 71.18900095911997,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 51.88678071719021,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 48.162253261544976,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 52.36324447061313,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 49.24990702158348,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 53.4631479727153,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 57.70699175307609,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 49.21763650971046,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.366500091552737,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.18950080871582,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9950001525878918,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.2804003906250045,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.16210002899170206,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.11140003204346272,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 42.09773840431982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 30.341977799755828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 46.61324873859718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 36.9109192232482,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 44.92109448237449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 37.275685953146876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9092859540666858,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.6542859758649566,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.8709684622935168,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.003154290774501689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 18.15877372764464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.827041333255217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.040000915527344,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.379997253417969,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 10.395198542613382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.371587199286698,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.391111680348725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 17.131003088007613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.23627581600571,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.785911416914452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.2570702689305833,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.063942939401311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 16.456130045346473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.39879001879126,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 9.404966628603063,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 22.563845781306448,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 10.34957944508127,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 17.357886553734293,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.336928849494093,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.694388232762641,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2319999694824304,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.2224998474121094,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5200000000000102,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.571799774169932,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.15625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9628499794006444,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.274187538992081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.445467237397507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.799184753019258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.8412360298387886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.919499100839463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.106314728481799,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.4864283970424106,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.11785725184849305,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3020095593789538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.10917285334562443,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.5563388818598334,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.8556314368399995,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -18.529998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -32.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.085146832590015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.460391736216533,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.924638259190441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.688430931831142,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.483819968794789,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.757508310072163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.98720200861356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -16.443241206484302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.024215329856923873,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.433188916711971,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.9107833109361048,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.255588238532308,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.534614573510039,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.766029063734557,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.350341455083517,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.374508296241169,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.443999481201189,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.245999145507824,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5565130615234466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.3290429687500023,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0064601898193359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.39726310729980696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.612752722221494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.856598738147005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.171713223957756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.953378599066857,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.063358309938273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.890077541722714,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9507152012416293,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.5192860194614957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8555105155155771,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.3276544700276358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.745359619558425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.400767773979107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.447060604328708,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.169008171064639,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -19.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.78997802734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.256536046486708,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.411188388235342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.5762976046960215,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.646535868677911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.3666819740179923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8326933834164052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.4884204591989914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.07829497257454321,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.195604543753617,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6160144312692188,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.4375573435583151,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.786306824620923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.5825234212667567,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.1587858629212,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.148440094331052,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.147027882817678,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6660003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8684967041016307,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.7911999511718477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.039399414062473,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.4730987548828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.9077946472168037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.8686920870302677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.925924881714324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.015095893930543,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.31159360376253886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.668971335635572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7921493027036632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.39642769949776735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.264288766043528,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.17420206543871508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.77294182732683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.5750261881237977,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.1258593356768043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5095749214871521,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.18686298260503365,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.82000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 16.419998168945312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.306835684845293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.0581548639666876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.245912264766492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.36730835127715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.06996810503299145,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.2093504009066525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.3533297083673781,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.93983067359828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.245904182112201,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.085357683471249,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.259767213020829,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 14.800151044575983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.019173500317741,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.200829647244259,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.283530845162664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 13.008563583841415,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3074996948242301,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.5140007019042798,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0014001464843715894,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7847998046874807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1444999694824105,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4332501220702909,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.4139404169641665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.646688267348855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.2917617799027568,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.763282508448032,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.4517597261728197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.556610133045693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.0014299665178577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.338569641113282,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.46336289169256917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.10182182233578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.0928503005721915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.73491950141184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.3038843400452744,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.48392075034321524,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.3599853515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.379448934259534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.43998312572062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 10.62794789024143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 12.02025294784055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.3029970161277475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.780170047614238,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.7888628221938916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.944663906535073,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6814825684735575,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 14.46718594522518,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 14.641802838495764,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 17.453095641139384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.6462083791570024,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.2113091987233666,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.847997731336152,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.01339681677821,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.2860000610351676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -16.304000854492188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.1842059326172034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.2208709716796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.22586288452146164,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.1771931457519145,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.069347263014885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.889675938093628,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.5984872607118117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1793634041818422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.8170587021444913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.07927925313483541,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.4964272635323663,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3814261300223212,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.258746612713471,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.15178326724249303,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.7800607976466765,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.8843889900443855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.017678302945433266,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.97533106252463,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -24.91998291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -19.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.399922725169393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.919671357254986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.9716147416216225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6369134787165276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.4059516386592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.0952006616447143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.6233138747872458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.5417885151086441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.661008777563699,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.8924685377504242,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.957759793367286,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.069756172015362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5432537566255498,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.896278584692892,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.013546678742797,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.5269443951344908,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.790499877929733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -28.661502075195358,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5878869628907069,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.581973876953157,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.031531066894558535,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.06036193847648974,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.9197169557767406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.935465770724198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.779048341545222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.658207655621581,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.942233444547916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.0886707844095755,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.1007167271205347,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.8214198521205383,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3281272866477609,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3310490706233651,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.2047714154631493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.500032378246999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2139220859318205,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.27423383232898213,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.759998321533203,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.080001831054688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.06887701278208702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.840814940138527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.858943761287481,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -37.36446769117493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.2247746226829435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.060509857368473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -13.082144361998239,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.04423594328017,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.12980851551518,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8136121206339659,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.15491118696685646,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -31.931624997876092,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.7244307726018064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.069030611030868,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.445283808468197,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -21.975503033037036,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.8960000991821317,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.396000099182132,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8870000457763751,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.781400070190429,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2519500160217376,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.122350063323978,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.404923634602753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.703803264224257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.504966262494349,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.612796083090146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.116528860654391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.06952971757908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.13928604125976562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.6976432800292969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.0223559057306275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.598640024765581,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.418451845547864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.854452147805866,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.34631706063957524,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5039537450798677,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -138.8399658203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -277.8800048828125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.457576094865217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.4795935667258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.622354074151417,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -38.82426155379919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.724620780534575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -21.771174039923388,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -19.53591175058137,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -32.57571105706789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.396644592132127,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.452390747221237,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.608499125897083,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -33.39141886050036,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.775415385249826,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.779694793585783,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -14.899051197051325,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.506978146824757,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -18.964349365234398,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -64.11823425292971,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.637247314453134,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.942338867187459,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.337825469970653,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 11.19757995605471,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -13.656837436592852,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -24.051305103851718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -13.888961740559804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.37819445133917,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -18.574769749706967,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -38.664754696176374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 6.356427873883931,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.99194968515922,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.325911428959108,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.456096986055366,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -12.653825973999385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -25.325886553385885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.5243709744019347,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.037602048617422,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.10000228881836,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.740001678466797,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -12.645451310357736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.576956583432075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -11.834908594499282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -41.7711853423077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.161150295059329,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.417717802758624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -21.10567741970703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -28.760488250288976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.584519807624644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.549753763927514,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.821053646244948,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -36.33834264900887,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.211944899774579,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.42623855642102,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -16.468816866176986,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -23.69175534004584,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.9960000991821261,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.7909999847412053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.387600021362303,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.161600112915039,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -14.730514447631482,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -22.538063148056718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -14.154156906374673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -24.855323073538926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3650000435965399,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.38500022888183594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.360288572826664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.2045001505823283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -12.731849143051214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -23.168817865351258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.6820248614858873,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.9827908437035053,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -28.82000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -69.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.1294544274666585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.247561391112242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -12.744536084136827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -53.86756793475409,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.880241821405654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.408175577365835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -11.654094462675754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.198214944122586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.931477075266432,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.22035857160768,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.730681135882488,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -48.434725241455254,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.9310364261209045,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -21.416696331028227,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.0172339091457125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -22.129482033879455,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.3499999999999943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.708499145507801,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.7403067016601597,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.516022338867174,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.023073120117146573,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.993080978393607,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -11.823465942774725,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.47303863486086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -11.449940060110618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.07202029019292,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.6235417946308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -25.853557775777773,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.84857177734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.2867137363978784,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.357081007728972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.668339100708342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.810466011003935,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -23.552602177247916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.7537723241083807,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.062288062360125,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -14.1199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -26.360000610351562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.99433494406202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.816754036237693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.37467973073429,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.476234369780677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.539568360222614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.31346824695261,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.87789999546028,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.561350009364826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.9334034413289287,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.789551216733132,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.3608247824799538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.043391676481841,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.5903629649378637,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.3219890006150035,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.241039441930238,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.492617099121691,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.7699996948242358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.639499664306641,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.40493743896485057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8171618652343682,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.09543407440187934,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7514142608642658,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.720897361515266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.704781184826162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.27671908550751,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.52731981296641,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.373604940576694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -16.017220098483044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5707146780831476,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.211429050990514,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5917161825479167,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1103593770793356,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.990096592667085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.049505252649297,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.999131193021719,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.438317218265291,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.8899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.079998016357422,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.7636121153151052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.355282260277237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.101841559431773,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.99131259333367,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.785935361596728,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.118734512463284,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.2870754319273887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -19.021073421833545,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 7.824543618048197,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6719205592273241,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9120133888225634,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.558469900034836,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.8367299663119785,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.12725526612568,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.349785121602654,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.952340511590409,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.180499839782712,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5239999771118136,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.008622131347664208,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3194248199462919,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.06913675308227596,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4702419853210458,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.556441389154596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.324274571718075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.896337501321733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.421000436866024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.3588019565760963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.052560661634473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.08428546360560829,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.3964282444545202,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.22031773871726523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8804158868463383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.6992280494997587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.64684517626694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.15925303880923058,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.183770319642064,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.7000007629394531,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5600013732910156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.386227147704737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.314697063956063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.48595145132713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.47158369227064956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.1096626439762085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.4796654389118693,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.158421326916927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1063551090348178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.32529564497164554,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.2874942444515023,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.4720965030727937,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.904426385569484,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.1604572486914595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.511813807425736,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.4784392266131157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.175088019277952,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.16350002288818644,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9299999237060561,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.011090698242185226,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.0048003387451132085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.023429889678958205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.10798948287963839,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.338069296732371,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7122601669184325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.022015513389764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.011175524579655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.226088843862973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8314755687474307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.12714304242815289,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.2392864227294922,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.26271227535981123,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.40382303904356087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.871622873362689,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.449352749271803,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5315792730795146,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.0706148414712986,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.9900054931640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.660003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.039182391452555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.098221443683859,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.078143862221974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.541671972225627,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.486584610765876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.404915610499827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.859214261999478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.9005547922940096,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.0217491112805366,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.071018624179298,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.064288913967637,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.1088292789267928,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5373792154811263,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.5865636358377788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.7776462915305657,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1681781179491253,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2964996337890682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3754989624023324,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.34773223876953807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.099872436523441,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.012865371704123163,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.1003258514404024,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.9866826236636954,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.337650913836367,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.916078788274458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.8693458986614697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.041232298822939,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.493893376052283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.33928680419921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6157161167689731,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.28140526395932874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4505296423226075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.7578640033154134,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.118058570233718,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8091217991838127,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.3161046681512043,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.75,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.8700103759765625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.569365504619972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.9082163742429685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.058098073640216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.038572837553997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.3904163766473427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7733019004966941,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1200804526372092,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.341096361178229,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.49156599811311974,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8810135547384075,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.0442431253858793,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.394269855744837,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.5587890186374072,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.218177345840912,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.5167801008928343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.727636549064906,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8375000000000057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.522501373291021,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.24063293457032842,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.216780090332037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.14294212341306434,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7672232055663812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.14600974979673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.1713155667456574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.8999626568464665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.2511568533744457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1090785817379007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.016649549876124325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.39642878941127213,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4471435546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2577609992402943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.23376011668148733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.504481655743507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.504481655743507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6862519337094701,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.616079087921614,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.69000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.0699996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.111937386717301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.2935644294511337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.391362196796032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.492846652157057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1474262093093675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.38594688198914007,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.317243332354212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.9377527298396275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.9489941160157902,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7336383900534273,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.6224927514583056,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.925689345455893,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.8017791859753807,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.6055323643484645,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.319617221175829,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.006485640082762,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3915000915527287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.195000076293937,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.11087341308592613,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.47319351196289006,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.05184139251709041,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.2432915115356451,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.2556536251750572,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9206276520131951,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.9560750221856642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.0377819067662015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8915633220824226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.3579131544293936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0714285714285714,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.27928488595145096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.09139019756214295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.25316839669418334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.7504920851464925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.2608398423570422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.7138336723442482,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.0948480385615644,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.69000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.095378504793349,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.588246686619668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.830294667094703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.20455671330765757,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.542546843727569,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.4832666637013325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.8096532221810744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.8486447888524493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.0344470020602574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.561043867115107,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8164397188403667,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.637399406606492,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5933414484428212,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.508212582636272,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.8272073313489683,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 6.917377699095584,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2965000152587862,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7795001983642607,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.014749450683595455,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.08044891357421591,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.015049514770510086,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.06587505340576172,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.352165249999951,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.33548748197753664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.155813140262209,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.198710952253923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.059947577006784,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.3085386256258325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.24500002179826996,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.77642822265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2800537566622361,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.6423964013132522,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.8338938700282488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.9938474671892128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.12756275466327738,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.6408486623238772,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.6200027465820312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.1299972534179688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.060731994400468,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.280539436223893,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.327985567330292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 8.873622705172046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.2350628050989299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.0432199948779868,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2941422920628387,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.346194524933633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.0001995083326234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.307742255728455,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.341840515584629,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 14.30646539847088,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.71414259018582,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.034699241215592,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.931002845592881,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 8.414927435176768,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.38650016784667685,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.3005001068115263,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.15800170898437216,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.9489961242675804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.04627246856689737,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3000782394409214,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.22594637412950425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.94009274617736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.4272438971343995,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.6395289656216967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5143367753194239,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.0324253509833587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.08821432931082573,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.19785690307617165,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.09573632359300888,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.13428606185507852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5403074044287859,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.7276664517803653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.21309539430802493,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.1738500040326323,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.3100013732910156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.15999984741210938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.148441282238799,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.2406155391248572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.265026574206308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.2589269995211696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5483733464003437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.2900026860211993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.194631224446241,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.041025766337898784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 4.912490220494293,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.7865872803797038,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.7488283740480286,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.173915693777665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.4008320488844053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.701476560316406,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.4422293290838013,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.027707143905236,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.11149997711181925,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7124996185302734,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0021517944335940342,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.04861724853515881,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.005797882080081251,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.028497409820559483,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.9998961045259325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.3556536206598802,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.7492502513918753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.26302144653038706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.7205084209074841,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.30103087435658926,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.027857099260602758,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.012142726353236655,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.07430247211879415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.0227081792442827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.704763652459639,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.474287385440908,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.25338955070811475,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.030564726364981,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8199996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.2399978637695312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.1377343640984225,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.0248290428753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.217377527261146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.6097049553076337,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.7696472181693927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.594991230814191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.809862994526835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.3437059276396734,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9231971386346687,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.002373776629261304,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.20352257900680915,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 7.042547648606468,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.1795581771153572,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 8.586470477151797,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.8269975590032077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 9.412438837882808,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.17250003814697124,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7949998855590792,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.008272628784176561,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.08308158874511662,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.018637142181397337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.08274484634399215,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.3537758930746167,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9891746671784052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.9109042016127953,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.1190971349535745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.959988329110618,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.700033314623518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.05121421813964844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.08371434892926888,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.14361266470103828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.14670923460840735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.8173752531823628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.45412346382794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3652268299259731,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.653052803354831,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.5699996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.1999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.403771304282912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.204737127636915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.314398303105826,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.0058019037486607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.834241838905239,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.009341568628086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.723031244572315,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.26772427959420586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.65716019845018,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.17753430813235394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.30054335485148975,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.4270407895501735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.11496355637950906,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.9821376777095185,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.9138293089577276,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.801008630648929,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.15300006866454652,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9445001602172809,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.021882781982419885,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.006757125854491619,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.018571853637695312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.12250789642334325,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.3639004573924547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.2979877631546852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.0402861228615574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3793830860879588,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1278296690574248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.6432371811066817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1278574807303292,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.2478572300502232,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.28842154733086534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.47853289139667066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.9128008355814528,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.2391339589394312,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.08420238593504559,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7454436670303464,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -56.53997802734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -113.93997192382812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.46403107840563,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.155291159826207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.11746882940574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -27.607990187781795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.950997287831253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.1847369149562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -11.458697405066186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -22.0331913144155,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.40309957567254,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.128088340321646,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.103613881151402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -22.17514749448296,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.0017918925465032,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.193257668618594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.821836851536144,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -16.964458404172365,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.977000427246139,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -31.399002075195312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.160800170898483,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.602800292968709,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.22900009155273438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.6192498779297466,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.055076816587636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.312396342573741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.62077054701679,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -19.099843582625752,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -10.8853361264317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -22.394401137104392,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.7792837960379444,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.502142769949774,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.1507372376142664,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.0644169934917658,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -8.91938410628801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.974438797213654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.4849034306464028,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.1675629998506696,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.549995422363281,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.959999084472656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.270258268591721,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.8728956091982325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8372424389687101,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.608755054731741,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.936754340791903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.413929449741286,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.6019683173584505,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.522275151207005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.7906732341413703,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 3.1543072103063285,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.1766125092856266,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.1759123614329074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.012451054492847113,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.422450203403681,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.0348922361715922,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.453542240963871,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.5289997100830135,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.86599960327149,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.0675999450683662,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.01099990844727472,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.018139419555666336,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.10510978698731321,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.75769783055635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.6165447389162075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.193781236119266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.368629679198259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.85953598744735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.656187365784685,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.12285723005022309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.012142726353236544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.01598133128333279,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.24301477268784266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.038338063643787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.9524267596395966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.3493555339275116,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.32688008052901396,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.1899871826171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -25.419998168945312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.4910171714244265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.470533836286093,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.2200380184235655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.086646810807459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.266614143762326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.279464203583217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.036514499981169,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -23.383676645435216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 9.551948674157519,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.5566689832184681,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.793816929830772,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.653804117508624,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.3174087484775767,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.287984957245612,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.6003460535488738,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.314943735192077,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.9694999694824276,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.016500854492193184,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.19254852294923808,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.31010223388670966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.20596427917479332,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.468681716918951,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.196445266946956,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.951473548500005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.6180589584895095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.453528718804696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.1679172808299683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.909183171744523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.253570556640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.282857622419085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2445885331019788,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.096999582732161,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.533431205288661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.408473149082301,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.005329009514548,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9933300185399985,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -18.410003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -60.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.08259557366440085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.735901420341005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.250120343977548,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -22.967062225460488,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.9921739442734046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.076076477639113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.015644623998249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -21.803674128584404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 5.978335929068691,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7086986008364433,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.23626539572321015,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.534219532161654,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.042968548988655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.084597231301508,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.6212159295317949,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -16.73494121834127,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.9419998168945085,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.873501586914017,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.1446002197265557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.025000000000034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.041949920654303696,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.280299835205085,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.267833272235089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.995893661544923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.359606103570057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -14.357570944999885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.629571962670308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.449372613590452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.797143118722099,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5203288292787906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.2992921947229235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.216868438393718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.800449368520706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.6944044028752401,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.1410446066697513,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -144.72999572753906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -146.19000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.457857826815546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.156105095877097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.107344357632551,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -9.454786360257572,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.806756787472322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.2774928223478494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.291868944763287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.743846263828198,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 3.6030736759175457,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.1289022763725356,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.093489409378214,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.021943666958738,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.8575513921875721,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.7139864239897555,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.3449916087667564,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 1.324886646414937,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -138.57749938964844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -137.23749923706055,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -142.49181854248047,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -144.2533901977539,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -152.1948207092285,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -152.72581634521484,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.081239147960103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -5.452662510708373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.7014893855816355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.5635696139976747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.6597353257217806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -4.081516432508459,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.33452388218471,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -2.4873809814453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.34069320887116605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7527892051688587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.3646027463619106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.941847503797913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.2631291511372307,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.25546124473549137,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.9449996948242188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.173473431503892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.100287338639799,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.626018454073801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.31985680001674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.326116969764447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.603475929658014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.0833842580165545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -17.157747297645166,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 2.887458071229199,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.0730845191352376,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.6121635058194643,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.887014106717906,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.37691157447969736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -6.611996683320408,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.4465237044865127,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.089014387402031,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.25124998092651296,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.9137498855590813,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.10810001373290845,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.3665000152587865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.03352499961853539,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.13312498092651737,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.414694839047174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.04344948208441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.645958696532295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.406916310686523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.699264779468972,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.793667850873447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.0857142039707729,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.16542843409946983,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.5185246139972945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9699772164810794,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.378657392918186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.316694279267349,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.412798917982636,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 2.0332362770262447,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.8199996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.5500030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -4.1702942972248636,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.495223694112126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.5561476897352895,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.3763334183172438,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.697716378259308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.2515102658460444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.0803967898609397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7638137292830915,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.8906372055082281,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.5319791253924349,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.45770725851904714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.0565092749815905,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2514890170254418,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 5.739968980491562,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 1.556463763669103,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 4.304919180960043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.13600006103516193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7670001983642578,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.03695281982422216,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.12132537841797841,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.017160644531244884,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.15391923904418547,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.7503774643582446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.881692597090412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.484173363511122,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.5952686764832071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.6083332812924853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.006822632704063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.1700003487723214,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.345001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2847436044480638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.4905511910142559,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.3487302928521085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.7097851897988621,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.4155919094716156,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.9745352753091495,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -9.520004272460938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -20.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.530884365744883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.2377853797224248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -3.0302747855815007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.981886393279865,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.250268771034051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.776157256702449,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -6.735884726213493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -18.549891859877768,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.46995286301179107,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.7894174397821363,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.9835801626728351,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -8.54904369998103,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.301063375749301,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -7.784678010364843,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -2.0990241726834507,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -13.481158949634631,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.1485000610351506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -3.7874992370605582,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.25399993896485284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.4783999633789051,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.13404998779296307,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.789300041198743,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.132246504586181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -10.028912074590968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.646618971629524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -12.028201438635266,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -7.054067232643258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -15.473665405354353,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.04428645542689669,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.03285871233258941,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 0.2372467754064549,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 0.43566439214477537,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -5.443424041217316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -11.578706655995664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -1.4025454047743064,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -1.101378437877563,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.03000000000000025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.08000000000000007,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.17999999999999972,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": 0.050000000000000044,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.04999999999999982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.14999999999999947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-03",
        "to": "2026-11-04",
        "change": -0.009999999999999787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-28",
        "to": "2026-11-04",
        "change": -0.029999999999999805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": -0.019999999999999574,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": -0.10999999999999988,
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
    "available_prior_observations": 14,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-04",
        "to": "2026-11-05",
        "change": 11.57,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-29",
        "to": "2026-11-05",
        "change": 10.98,
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
    "id": "latest.TNX.value",
    "available_prior_observations": 2,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-11-02",
        "to": "2026-11-05",
        "change": -0.057000160217285156,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  }
]
```

## 判断依据 · 反弹是否从局部扩散

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否从局部扩散 |
| 事实指标引用 | ["prices.SPY.distance_sma200_pct", "prices.QQQ.distance_sma200_pct", "prices.RSP.return_1d_pct"] |
| 推断与解释 | 完整日线仍破位，盘前QQQ/SMH强而RSP弱；没有真正广度和回踩证据，评级脆弱修复。 |
| 反证与缺口 | 高波动容易挤空，盘前价格不是常规量价确认；全成分广度缺失。 |
| 确认条件 | SPY守733、QQQ守647.05只是第一层；开盘后30–60分钟低点抬高、突破首30分钟高点后回踩不破，站稳独立核验的常规VWAP，并有RSP/更多板块跟随；收盘延续、次日不吞没才提高可靠性。 |
| 失效条件 | SPY跌破732.71、QQQ跌破647.05后反抽失败，或只芯片涨而RSP持续创新低、VIX重新上行。就业发布前的盘前涨幅不满足条件。 |
| 观察期限 | 今夜两次数据至下周一收盘 |
| 条件式指导 | 等待独立事件与量价确认；先观察，确认后分阶段参与，不以合约报价生成最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较早报增加当前盘前价格、亚洲融资证据及原始存储研究；日线未变。 |

## 判断依据 · 芯片能否重新成为主线

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 芯片能否重新成为主线 |
| 事实指标引用 | ["prices.SMH.distance_sma200_pct", "prices.SMH.volume_vs_previous20_ratio"] |
| 推断与解释 | 涨幅大不能抹去昨日下跌及长期均线破位；先看回踩承接和相对强弱。 |
| 反证与缺口 | 强烈反弹可以是流动性或回补；未获当期净申赎、持仓变化验证。 |
| 确认条件 | SMH不再失守447.73，开盘回踩低点抬高；再收复5日高点483.93并保持，相关个股相对SMH同步改善；两个收盘承接更可靠。旧497.33/504.27仍为更远的修复区域。 |
| 失效条件 | 反抽后重新失守447.73，尤其445.59下方反抽失败；单一存储上涨、其它硬件续跌也降低可信度。 |
| 观察期限 | 未来1–3个交易日，财报/融资新增消息随时重评 |
| 条件式指导 | 等待独立事件与量价确认；先观察，确认后分阶段参与，不以合约报价生成最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较早报增加当前盘前价格、亚洲融资证据及原始存储研究；日线未变。 |

## 判断依据 · 防御篮子是否更合适

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 防御篮子是否更合适 |
| 事实指标引用 | ["prices.XLV.return_20d_pct", "prices.XLP.return_20d_pct", "prices.XLU.return_20d_pct"] |
| 推断与解释 | 20日相对强可列观察，但昨日自身仍跌，不直接推导净流入。 |
| 反证与缺口 | 短期获利回吐风险仍在，20日强不意味着每个交易日上涨。 |
| 确认条件 | 自身守5日低点，收复前收并有一次回踩承接；相对SPY的强势保持，不仅是跌得少。 |
| 失效条件 | 同步新低或利率/能源成本上升压估值及利润，防御标签不能替代止损。 |
| 观察期限 | 未来1–3收盘 |
| 条件式指导 | 等待独立事件与量价确认；先观察，确认后分阶段参与，不以合约报价生成最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较早报增加当前盘前价格、亚洲融资证据及原始存储研究；日线未变。 |

## 判断依据 · 宏观信用是否支持冒险

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 宏观信用是否支持冒险 |
| 事实指标引用 | ["macro.CBOE_VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value"] |
| 推断与解释 | Cboe确认5日恐慌升温；当前VIX回落而信用旧数据未覆盖抛售，新单体CDS压力须区别。 |
| 反证与缺口 | 已宣布投资和ARR不能等同FCFF，单一发行人CDS不是行业违约率。 |
| 确认条件 | 新云资金落实、延期不扩大、信用价差回落，叠加价格停止下跌；分别核验公司事实。 |
| 失效条件 | 新增延误/非预期稀释与信用走弱共振；单一低量预测合约不触发。 |
| 观察期限 | 未来一周及新披露 |
| 条件式指导 | 等待独立事件与量价确认；先观察，确认后分阶段参与，不以合约报价生成最佳仓位。 |
| 主观置信等级 | medium |
| 判断变化原因 | 相较早报增加当前盘前价格、亚洲融资证据及原始存储研究；日线未变。 |

## 芯片超跌反抽尚缺广度 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 6日盘前芯片普遍回升，昨日日线仍是大跌。 |
| 事实：市场反应 | SPY 735.40（较5日收盘+0.33%）；QQQ 658.02（较5日收盘+1.70%）；SMH 472.70（较5日收盘+5.58%）；RSP 216.60（较5日收盘-0.13%）；NVDA 188.82（较5日收盘+3.98%）；MU 714.00（较5日收盘+8.78%）；SNDK 900.07（较5日收盘+11.61%）；AMD 436.04（较5日收盘+7.82%） |
| 推断：解释 | 推断：跌后回补可能推动高贝塔先弹；没有期权/经纪流量，不能断言由空头回补主导。 |
| 受益篮子 | ["SMH、NVDA、MU观察"] |
| 受损篮子 | ["追涨且无失效条件者"] |
| 反证 | RSP盘前仍负、MSFT仍弱；须就业后复核。 |
| 下一催化剂 | 21:30北京就业、常规开盘回踩 |
| 证据 | ["https://za.investing.com/news/stock-market-news/nasdaq-futures-rise-after-steep-ai-selloff-as-chip-stocks-stabilize-4557213", "https://www.bls.gov/schedule/2026/11_sched.htm"] |

## AI融资与项目兑现压力 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | SoftBank CDS上行；Anthropic年内IPO合约下行。 |
| 事实：市场反应 | 美国芯片盘前涨并未消除亚洲融资链压力。 |
| 推断：解释 | 推断：需求在、融资也贵可以同时成立；不因一个合同或CDS把全行业判死。 |
| 受益篮子 | ["融资依赖低、现金回收可验证者"] |
| 受损篮子 | ["高杠杆新云、股权融资依赖者"] |
| 反证 | AWS园区与GPU租金提供需求反证。 |
| 下一催化剂 | 融资条款、投运兑现、NVDA财报 |
| 证据 | ["https://www.zawya.com/en/business/softbank-credit-risk-jumps-to-4-year-high-shares-tumble-as-ai-fears-roil-market-2045075", "https://press.aboutamazon.com/2026/11/our-responsible-approach-to-investing-in-somervell-county-texas", "https://www.silicondata.com/products/silicon-index/h100"] |

## 存储竞争叙事需要区分产品 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Counterpoint原始报告：Q3 CXMT DRAM收入份额9%，环比下降。 |
| 事实：市场反应 | MU盘前明显反弹，尚未恢复昨日大跌。 |
| 推断：解释 | 低价竞争风险长期存在，但本次证据不支持HBM价格已经坍塌；份额不等于盈利。 |
| 受益篮子 | ["产品组合升级且现金兑现的存储观察"] |
| 受损篮子 | ["仅凭标题将DRAM/HBM/NAND混同的交易"] |
| 反证 | 未来新增供给、技术追赶与客户议价仍会改变周期。 |
| 下一催化剂 | 下一季度ASP、HBM交付与库存 |
| 证据 | ["https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b"] |

## 就业与通胀预期的双重检验 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | BLS21:30北京就业，密歇根23:00初值。 |
| 事实：市场反应 | 盘前股指反弹而黄金/国债ETF偏弱。 |
| 推断：解释 | 数据偏强可能提高利率，过弱也可能压增长；市场反应比好坏标签更重要。 |
| 受益篮子 | ["现金、择机防御篮子观察"] |
| 受损篮子 | ["未经确认的高久期风险"] |
| 反证 | 通胀压力缓和且增长不失速可以支持反弹延续。 |
| 下一催化剂 | 就业、消费者通胀预期、下周CPI |
| 证据 | ["https://www.bls.gov/schedule/2026/11_sched.htm", "https://www.sca.isr.umich.edu/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | 340.60 | -1.04 | 2026-11-06T12:02:48+00:00 | 2026-11-06T12:02:48+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| AMD | 436.04 | 7.82 | 2026-11-06T12:02:51+00:00 | 2026-11-06T12:02:51+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| AMZN | 262.78 | 0.99 | 2026-11-06T12:02:42+00:00 | 2026-11-06T12:02:42+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| ARM | 178.02 | 6.78 | 2026-11-06T12:02:33+00:00 | 2026-11-06T12:02:33+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| AVGO | 305.91 | 4.93 | 2026-11-06T12:02:13+00:00 | 2026-11-06T12:02:13+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| BABA | 107.04 | -0.96 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| CAT | 570.94 | 3.13 | 2026-11-06T12:02:45+00:00 | 2026-11-06T12:02:45+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| CEG | 242.00 | 0.98 | 2026-11-06T11:57:31+00:00 | 2026-11-06T11:57:31+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| CI | 298.00 | -1.15 | 2026-11-06T11:47:15+00:00 | 2026-11-06T11:47:15+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| COHR | 186.23 | 9.70 | 2026-11-06T12:02:32+00:00 | 2026-11-06T12:02:32+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| COIN | 137.80 | 0.72 | 2026-11-06T12:02:32+00:00 | 2026-11-06T12:02:32+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| COP | 134.50 | -0.71 | 2026-11-06T10:02:38+00:00 | 2026-11-06T10:02:38+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| CRWV | 47.29 | 8.31 | 2026-11-06T12:02:40+00:00 | 2026-11-06T12:02:40+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| CVX | 211.93 | -0.47 | 2026-11-06T11:27:00+00:00 | 2026-11-06T11:27:00+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| DRAM | 40.42 | 9.22 | 2026-11-06T12:02:39+00:00 | 2026-11-06T12:02:39+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| GDX | 85.27 | -0.56 | 2026-11-06T12:01:36+00:00 | 2026-11-06T12:01:36+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| GEV | 793.24 | 2.95 | 2026-11-06T12:02:04+00:00 | 2026-11-06T12:02:04+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| GLD | 372.18 | -0.88 | 2026-11-06T12:01:22+00:00 | 2026-11-06T12:01:22+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| GLW | 110.20 | 6.55 | 2026-11-06T12:00:45+00:00 | 2026-11-06T12:00:45+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| GOOGL | 283.79 | 0.43 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| IGV | 99.53 | 0.53 | 2026-11-06T11:33:00+00:00 | 2026-11-06T11:33:00+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| INTC | 55.71 | 6.62 | 2026-11-06T12:02:50+00:00 | 2026-11-06T12:02:50+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| IWM | 271.16 | 0.07 | 2026-11-06T12:02:28+00:00 | 2026-11-06T12:02:28+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| LITE | 562.00 | 10.26 | 2026-11-06T12:02:43+00:00 | 2026-11-06T12:02:43+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| LLY | 1,344.00 | -1.52 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| META | 604.68 | -0.07 | 2026-11-06T12:02:31+00:00 | 2026-11-06T12:02:31+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| MRVL | 146.77 | 9.90 | 2026-11-06T12:02:40+00:00 | 2026-11-06T12:02:40+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| MSFT | 530.61 | -0.99 | 2026-11-06T12:02:42+00:00 | 2026-11-06T12:02:42+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| MU | 714.00 | 8.78 | 2026-11-06T12:02:51+00:00 | 2026-11-06T12:02:51+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| NOW | 101.53 | -0.81 | 2026-11-06T12:02:41+00:00 | 2026-11-06T12:02:41+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| NVDA | 188.82 | 3.98 | 2026-11-06T12:02:43+00:00 | 2026-11-06T12:02:43+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| ORCL | 119.38 | 3.66 | 2026-11-06T12:02:44+00:00 | 2026-11-06T12:02:44+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| PLTR | 159.00 | 2.59 | 2026-11-06T12:02:51+00:00 | 2026-11-06T12:02:51+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| QCOM | 162.50 | 3.67 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:35+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| QQQ | 658.02 | 1.70 | 2026-11-06T12:02:44+00:00 | 2026-11-06T12:02:44+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| RSP | 216.60 | -0.13 | 2026-11-06T12:00:55+00:00 | 2026-11-06T12:00:55+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| SMH | 472.70 | 5.58 | 2026-11-06T12:02:33+00:00 | 2026-11-06T12:02:33+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| SNDK | 900.07 | 11.61 | 2026-11-06T12:02:47+00:00 | 2026-11-06T12:02:47+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| SPY | 735.40 | 0.33 | 2026-11-06T12:02:36+00:00 | 2026-11-06T12:02:36+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| STX | 501.24 | 7.44 | 2026-11-06T12:02:32+00:00 | 2026-11-06T12:02:32+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| TAN | 45.05 | 2.18 | 2026-11-06T11:27:00+00:00 | 2026-11-06T11:27:00+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| TLT | 81.69 | -0.30 | 2026-11-06T12:01:12+00:00 | 2026-11-06T12:01:12+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| VRT | 190.93 | 8.03 | 2026-11-06T12:02:12+00:00 | 2026-11-06T12:02:12+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| XLE | 61.53 | -0.16 | 2026-11-06T12:00:04+00:00 | 2026-11-06T12:00:04+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| XLF | 57.00 | -0.87 | 2026-11-06T12:00:40+00:00 | 2026-11-06T12:00:40+00:00 | 2026-11-06T12:02:55.998276+00:00 | ok |
| XLI | 162.51 | 0.02 | 2026-11-06T09:04:50+00:00 | 2026-11-06T09:04:50+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| XLV | 182.16 | -1.49 | 2026-11-06T11:42:25+00:00 | 2026-11-06T11:42:25+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |
| XOM | 165.00 | -0.18 | 2026-11-06T11:38:00+00:00 | 2026-11-06T11:38:00+00:00 | 2026-11-06T12:02:55.998276+00:00 | stale |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 733.00 | USD_per_share | 2026-11-05 | -4.41 | -4.73 | -5.29 | ok |
| QQQ | 647.05 | USD_per_share | 2026-11-05 | -6.49 | -9.55 | -13.45 | ok |
| IWM | 270.98 | USD_per_share | 2026-11-05 | -4.59 | -4.59 | -2.37 | ok |
| RSP | 216.87 | USD_per_share | 2026-11-05 | -2.89 | -1.44 | 2.36 | ok |
| GLD | 375.49 | USD_per_share | 2026-11-05 | 0.81 | 1.88 | -0.83 | ok |
| GC=F | 4,113.50 | USD_per_troy_ounce | 2026-11-05 | 0.99 | 2.04 | -1.05 | ok |
| CL=F | 90.52 | USD_per_barrel | 2026-11-05 | 2.72 | -11.25 | -1.06 | ok |
| BZ=F | 98.29 | USD_per_barrel | 2026-11-05 | 3.88 | -14.44 | -5.74 | ok |
| TLT | 81.93 | USD_per_share | 2026-11-05 | 0.21 | 0.54 | 5.21 | ok |
| UUP | 28.92 | USD_per_share | 2026-11-05 | 0.07 | -0.41 | -0.21 | ok |
| HYG | 77.28 | USD_per_share | 2026-11-05 | -0.31 | -0.39 | 0.18 | ok |
| LQD | 104.66 | USD_per_share | 2026-11-05 | 0.15 | 0.42 | 2.14 | ok |
| ^VIX | 28.18 | index | 2026-11-05 | 69.66 | 63.84 | 82.87 | ok |
| ^VIX3M | 25.55 | index | 2026-11-05 | 35.90 | 31.90 | 41.32 | ok |
| ^VVIX | 134.99 | index | 2026-11-05 | 49.31 | 37.73 | 53.99 | ok |
| ^MOVE | 97.92 | index | 2026-11-05 | 4.30 | 4.68 | -4.52 | ok |
| NVDA | 181.60 | USD_per_share | 2026-11-05 | -9.26 | -15.01 | -21.21 | ok |
| MSFT | 535.93 | USD_per_share | 2026-11-05 | -3.58 | 1.09 | 2.55 | ok |
| AMZN | 260.21 | USD_per_share | 2026-11-05 | -2.19 | 6.74 | 2.42 | ok |
| GOOGL | 282.57 | USD_per_share | 2026-11-05 | -2.20 | -0.44 | -18.87 | ok |
| META | 605.08 | USD_per_share | 2026-11-05 | -3.96 | -3.11 | -16.06 | ok |
| CRWV | 43.66 | USD_per_share | 2026-11-05 | -9.83 | -28.12 | -46.48 | ok |
| MU | 656.39 | USD_per_share | 2026-11-05 | -17.46 | -29.74 | -36.62 | ok |
| DRAM | 37.01 | USD_per_share | 2026-11-05 | -17.96 | -28.48 | -34.99 | ok |
| VRT | 176.73 | USD_per_share | 2026-11-05 | -14.02 | -28.14 | -27.49 | ok |

## 跨资产风险解释

状态：恐慌后的脆弱盘前修复。5日SPY收跌4.41%、QQQ跌6.49%、SMH跌11.21%的完整日线未改变；现在只是不同阶段的报价。SPY 735.40（较5日收盘+0.33%）；QQQ 658.02（较5日收盘+1.70%）；SMH 472.70（较5日收盘+5.58%）；RSP 216.60（较5日收盘-0.13%）；NVDA 188.82（较5日收盘+3.98%）；MU 714.00（较5日收盘+8.78%）；SNDK 900.07（较5日收盘+11.61%）；AMD 436.04（较5日收盘+7.82%）。VIX最新有效分钟11:47UTC为26.57，低于昨收28.18仍显著高于此前16.61；不能拿盘前VIX与昨日VIX3M相除制造当前期限结构。昨日VIX/VIX3M为28.18/25.55≈1.103，VVIX134.99、MOVE97.92；Cboe官方日CSV已更新到5日并确认28.18，修复早报来源缺口。油价连续期货11:52UTC WTI90.73/Brent98.48，黄金期货4078.10、美元指数101.963；连续合约和时点不可混用。GLD盘前372.18低于昨收375.49，TLT81.69低于81.93，说明避险资产也非单向受益。FRED2年4.58%、10年4.90%、实际利率2.64%、HY332bp/IG91bp仍为4日，金融压力10月30日、GPR2日，不能作为今晨信用实时正常的证据。SoftBank Reuters引Markit：6日06:53UTC五年CDS457.5bp、盘中曾466bp，是单发行人融资压力证据，不能套成美国全市场违约概率。就业尚未发布，今日21:30北京数据后需观察股债汇同向/背离；23:00消费者通胀预期可能再次改变走势。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.58 | percent | 2026-11-04 | -0.21 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.32 | percentage_points | 2026-11-04 | 0.23 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.91 | percentage_points | 2026-11-04 | 0.09 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.90 | percent | 2026-11-04 | -0.37 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.64 | percent | 2026-11-04 | -0.27 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.24 | percent | 2026-11-05 | -0.12 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.52 | index | 2026-10-30 | 0.24 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 28.18 | index | 2026-11-05 | 12.77 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLK | 科技 | -8.00 | -13.97 | -17.90 | -3.59 | -9.24 | -12.61 | 3.29 | 2026-11-05 |
| XLE | 能源 | -2.98 | -10.30 | -5.53 | 1.43 | -5.58 | -0.24 | 1.96 | 2026-11-05 |
| XLF | 金融 | -2.87 | 0.98 | 6.03 | 1.54 | 5.71 | 11.32 | 2.08 | 2026-11-05 |
| XLI | 工业 | -4.12 | -4.50 | -3.52 | 0.28 | 0.22 | 1.77 | 2.35 | 2026-11-05 |
| XLV | 医疗 | -2.50 | 0.47 | 9.96 | 1.90 | 5.20 | 15.25 | 2.39 | 2026-11-05 |
| XLP | 必需消费 | -0.75 | 3.48 | 9.39 | 3.66 | 8.21 | 14.67 | 2.17 | 2026-11-05 |
| XLY | 可选消费 | -3.83 | 1.24 | 5.31 | 0.58 | 5.97 | 10.60 | 2.54 | 2026-11-05 |
| XLC | 通信 | -0.59 | 3.09 | -6.90 | 3.82 | 7.82 | -1.61 | 1.80 | 2026-11-05 |
| XLU | 公用事业 | -0.71 | 0.37 | 5.43 | 3.70 | 5.10 | 10.72 | 1.81 | 2026-11-05 |
| XLRE | 房地产 | -1.82 | 2.88 | 8.45 | 2.59 | 7.61 | 13.73 | 1.48 | 2026-11-05 |
| XLB | 材料 | -2.91 | -0.38 | 6.21 | 1.50 | 4.35 | 11.50 | 2.06 | 2026-11-05 |
| SMH | 半导体 | -11.21 | -20.29 | -26.27 | -6.80 | -15.56 | -20.98 | 2.85 | 2026-11-05 |
| IGV | 软件 | -4.39 | -8.30 | -9.65 | 0.02 | -3.57 | -4.37 | 1.82 | 2026-11-05 |
| XOP | 油气开采 | -2.89 | -12.74 | -10.02 | 1.51 | -8.01 | -4.73 | 1.42 | 2026-11-05 |
| OIH | 油服 | -5.03 | -14.77 | -10.05 | -0.62 | -10.04 | -4.76 | 1.63 | 2026-11-05 |
| ITA | 航空与国防 | -4.00 | -4.65 | -0.27 | 0.41 | 0.07 | 5.02 | 1.06 | 2026-11-05 |
| ARKX | 航天主题 | -6.48 | -12.73 | -15.67 | -2.07 | -8.00 | -10.38 | 2.80 | 2026-11-05 |
| KRE | 区域银行 | -2.46 | -0.75 | 3.91 | 1.95 | 3.97 | 9.20 | 1.58 | 2026-11-05 |
| SKYY | 云计算 | -6.08 | -12.10 | -13.50 | -1.67 | -7.37 | -8.21 | 0.63 | 2026-11-05 |

## 资金证据分层

本次19ETF全部重查。ITA历史已由供应商调整，11月4日70.9467、5日68.11，单日约-4.00%，与发行人5日NAV68.08及NAV日变动-4.00%交叉一致；恢复价格比较，不把拆股当崩盘。ITA量比跨拆股可比性仍不足，不依据其成交量讲资金。19样本5日全部下跌：XLC-0.59%；XLU-0.71%；XLP-0.75%；XLRE-1.82%；KRE-2.46%；XLV-2.50%；XLF-2.87%；XOP-2.89%；XLB-2.91%；XLE-2.98%；XLY-3.83%；ITA-4.00%；XLI-4.12%；IGV-4.39%；OIH-5.03%；SKYY-6.08%；ARKX-6.48%；XLK-8.00%；SMH-11.21%。这是ETF样本不是全市场成分广度。20日XLV/XLP/XLU相对更强；盘前SMH强于SPY但RSP未跟，尚非广泛risk-on。资金只分价格量能代理与滞后净发行窗口：ICI11月3日公布截至10月28日一周ETF净发行459.06亿美元，国内股票265.90亿、债券142.34亿、商品-18.89亿；它是估算而非今日主力净流入。发行人单个NAV/份额快照、13F均不能证明当前交易身份。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-11-06T12:08:33.873810+00:00：基础跟踪与主动搜索覆盖科技/半导体/软件/能源/金融/工业/航天、Fed/就业/CPI/关税/出口管制/战争；额外15组风险、参考与催化剂搜索以及3个事件ID直查。Meta/Anthropic/Iran等第一页10项截断，主题无合格结果不代表无事件；不使用价格博彩填补经营判断。相同hash复核15合约。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will Texas enact a data center moratorium by June 30, 2027?", "2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。", "https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928"] | [17.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999981, "volume24h_usd": 158.35, "liquidity_usd": 40027.8589, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-06T12:02:49.472044+00:00", "contract_end_at": "2027-07-01T03:59:00+00:00"} | ["Texas建设限制事件定义狭窄，低报价不能排除行政/地方审核风险。", "数据中心投运、资本占用、供应链订单"] | ["州法律正文与项目延期相互验证", "仅竞选承诺或行政措施不触发此合约"] | [null, null] |
| ["Oracle downgraded to junk by Moody's or S&P by December 31, 2026?", "2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。", "https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by"] | [21.5, {"status": "comparable", "change_pp": 2.4999999999999996}] | {"spread": 0.03, "volume24h_usd": null, "liquidity_usd": 275.8006, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-06T12:02:44.615322+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Oracle评级合约报价上移但成交字段缺失，只作低置信度跟踪；独立SoftBank信用证据不等于Oracle被降级。", "信用成本与资本开支"] | ["正式评级和同券信用价格同时恶化", "仅负面展望不满足规则"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by November 30?", "11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [27.500000000000004, {"status": "comparable", "change_pp": -0.5000000000000004}] | {"spread": 0.010000000000000009, "volume24h_usd": 926.790234, "liquidity_usd": 29178.9674, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-06T12:02:44.666384+00:00", "contract_end_at": "2026-11-30T20:59:00+00:00"} | ["沙特管线军事打击风险", "石油供给与通胀"] | ["独立核验打击与供应变化", "单方威胁/拦截不符合规则"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the Fed increase interest rates by 25 bps after the December 2026 meeting?", "以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。", "https://polymarket.com/event/fed-decision-in-december-20260729232808632"] | [69.5, {"status": "comparable", "change_pp": 5.999999999999995}] | {"spread": 0.010000000000000009, "volume24h_usd": 1290160.233779, "liquidity_usd": 351198.5958, "quality_flags": [], "retrieved_at": "2026-11-06T12:03:08.700663+00:00", "contract_end_at": "2026-12-09T23:59:00+00:00"} | ["12月25bp加息合约较早报回升，尚非Fed实际决策；CME无法直接核验。", "估值折现与资金成本"] | ["官方政策及通胀数据支持", "物价降温且联储指引反向"] | [null, null] |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.8, {"status": "comparable", "change_pp": -4.6}] | {"spread": 0.0020000000000000018, "volume24h_usd": 90589.264449, "liquidity_usd": 124193.42066, "quality_flags": [], "retrieved_at": "2026-11-06T12:03:08.700663+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["AI专门规则，不能当普遍股价下跌概率", "估值与融资信心"] | ["逐条满足至少三项触发", "单一公司下跌不足"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [9.5, {"status": "comparable", "change_pp": -0.9999999999999996}] | {"spread": 0.010000000000000009, "volume24h_usd": 163108.22467499998, "liquidity_usd": 319027.4513, "quality_flags": [], "retrieved_at": "2026-11-06T12:03:08.700663+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["霍尔木兹真实通行比新闻标题重要", "油价/运费"] | ["Portwatch七日均达规则阈值", "宣布开放而运量未恢复"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [21.0, {"status": "comparable", "change_pp": 5.499999999999999}] | {"spread": 0.01999999999999999, "volume24h_usd": 263.25, "liquidity_usd": 1334.9475, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-06T12:02:48.010405+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["Apple/CXMT采购观察", "存储竞争"] | ["正式采购声明符合规则", "传闻或HBM推论不足"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [70.85000000000001, {"status": "comparable", "change_pp": -7.550000000000001}] | {"spread": 0.0010000000000000009, "volume24h_usd": 59075.83693500001, "liquidity_usd": 26407.56214, "quality_flags": [], "retrieved_at": "2026-11-06T12:02:47.952945+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["年内IPO合约降温，跟踪AI融资渠道；不凭市场报价断言延期已决定", "融资可得性与二级估值"] | ["正式公司/交易所发行日程与实际挂牌相互验证", "仅提交S-1或融资传闻不等于完成IPO"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will the US add at least 100k jobs in October?", "按BLS 2026年10月非农就业增量，至少100k为Yes；边界值落较高档。若到下月发布日仍未发布该月数据，则按最后可用月处理。计划11月6日08:30美东；不是经济衰退概率。", "https://polymarket.com/event/how-many-jobs-added-in-october-2026"] | [28.499999999999996, {"status": "comparable", "change_pp": -2.0000000000000018}] | {"spread": 0.04999999999999999, "volume24h_usd": 2298.629427, "liquidity_usd": 875.2952, "quality_flags": ["liquidity_under_10000_or_unknown"], "retrieved_at": "2026-11-06T12:03:55.896458+00:00", "contract_end_at": "2026-11-07T04:59:00+00:00"} | ["至少10万非农就业档，量能有限；不归一化为预测分布", "就业—Fed利率—估值折现及消费预期"] | ["官方首次数据与工资/参与率结合，并看债券和股市同步反应", "单一分档不解释增长质量；低量合约不能替代BLS数据"] | ["2026-11-06T08:30:00-05:00", "https://www.bls.gov/schedule/2026/11_sched.htm"] |
| ["Will the October 2026 unemployment rate be 4.2%?", "BLS 2026年10月季调U-3失业率首次公布为4.2%则Yes，一位小数；后续修订不计。到下月发布日仍无该月值则用最后可用月。", "https://polymarket.com/event/october-unemployment-rate-2026"] | [44.0, {"status": "comparable", "change_pp": 2.500000000000002}] | {"spread": 0.07999999999999996, "volume24h_usd": 874.490119, "liquidity_usd": 1963.4769, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-06T12:03:08.700663+00:00", "contract_end_at": "2026-11-06T13:30:00+00:00"} | ["4.2% U-3失业率精确档；不等于失业率上升概率", "就业—Fed利率—估值折现及消费预期"] | ["官方首次数据与工资/参与率结合，并看债券和股市同步反应", "单一分档不解释增长质量；低量合约不能替代BLS数据"] | ["2026-11-06T08:30:00-05:00", "https://www.bls.gov/schedule/2026/11_sched.htm"] |
| ["Will Nvidia (NVDA) beat quarterly earnings?", "NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。", "https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53"] | [96.8, {"status": "comparable", "change_pp": -1.100000000000001}] | {"spread": 0.05600000000000005, "volume24h_usd": 163.52, "liquidity_usd": 495.84159, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-06T12:03:55.895803+00:00", "contract_end_at": "2026-11-17T22:00:00+00:00"} | ["NVDA固定2.53 EPS门槛，低成交与宽价差；达标不等于股价上涨", "AI需求、利润率、建设兑现"] | ["官方首次EPS超固定门槛且指引/价格承接一致", "即使EPS达标也可能股跌；盈利质量与现金回收需独立核验"] | ["2026-11-17T17:00:00-05:00", "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"] |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 69.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-8.0, -2.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 5.999999999999995} |
| 24h成交量 / 流动性 USD | [1290160.233779, 351198.5958] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:03:08.700663+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.9999999999999996} |
| 24h成交量 / 流动性 USD | [163108.22467499998, 319027.4513] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:03:08.700663+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.80 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.45, -1.4] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -4.6} |
| 24h成交量 / 流动性 USD | [90589.264449, 124193.42066] |
| 价差 pp | 0.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:03:08.700663+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 26.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.5, 4.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -3.9999999999999982} |
| 24h成交量 / 流动性 USD | [37025.870767, 58673.035] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:03:08.700663+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Will the October 2026 unemployment rate be 4.2%?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1120075 / 5211635 |
| Yes 概率 % | 44.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-5.0, 3.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.500000000000002} |
| 24h成交量 / 流动性 USD | [874.490119, 1963.4769] |
| 价差 pp | 8.00 |
| 到期 | 2026-11-06T13:30:00+00:00 |
| 结算规则摘要 | BLS 2026年10月季调U-3失业率首次公布为4.2%则Yes，一位小数；后续修订不计。到下月发布日仍无该月值则用最后可用月。 |
| 规则指纹 | 0303df35e02524a94541a3178780a0a87d85cb14383a8a2d9ea28182cb56c111 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:03:08.700663+00:00 |
| 来源 | https://polymarket.com/event/october-unemployment-rate-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, -11.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [598.24, 21824.8147] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T11:57:13.010526Z |
| 抓取时间 | 2026-11-06T12:03:08.700663+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Oracle downgraded to junk by Moody's or S&P by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1219847 / 5939428 |
| Yes 概率 % | 21.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.5, 5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.4999999999999996} |
| 24h成交量 / 流动性 USD | [null, 275.8006] |
| 价差 pp | 3.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日美东23:59前，Moody’s或S&P正式将Oracle长期主体或高级无担保债评级降至Ba1/BB+或更低才算Yes；负面展望或观察名单不算。低成交量与宽价差，仅作低置信度观察。 |
| 规则指纹 | cb29bc6ea2fb2a6cd1d97dc489f0163f0b47e0cb2d31a9cbb3fe5dda90eb10c4 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:02:44.615322+00:00 |
| 来源 | https://polymarket.com/event/oracle-downgraded-to-junk-by-moodys-or-sp-by |

## Military action against Saudi Oil Pipeline (East-West) by November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401796 |
| Yes 概率 % | 27.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-2.0, -13.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.5000000000000004} |
| 24h成交量 / 流动性 USD | [926.790234, 29178.9674] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-30T20:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。 |
| 规则指纹 | de6f019a1972387984a02c6a8e7cef39e331ff99c1895cf1bba902450d550441 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T11:57:13.010526Z |
| 抓取时间 | 2026-11-06T12:02:44.666384+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 70.85 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-20.25, -22.75] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -7.550000000000001} |
| 24h成交量 / 流动性 USD | [59075.83693500001, 26407.56214] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:02:47.952945+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 21.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [5.0, 5.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 5.499999999999999} |
| 24h成交量 / 流动性 USD | [263.25, 1334.9475] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:02:48.010405+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## Will Texas enact a data center moratorium by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123855 |
| Yes 概率 % | 1.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.05, -0.15] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [null, 52126.5162] |
| 价差 pp | 0.30 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年末23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | b3e9528c7bb241316ba9beb5332075225a4976826229cd820fec02a115957e3a |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T11:57:13.010526Z |
| 抓取时间 | 2026-11-06T12:02:49.472044+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Will Texas enact a data center moratorium by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1103684 / 5123856 |
| Yes 概率 % | 17.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 3.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [158.35, 40027.8589] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 2027年6月30日23:59美东前，Texas以州法律或宪法条款强制暂停全州新数据中心（或覆盖所有单设施超100MW者）才算Yes；仅行政/机构命令、地方暂停、税惠撤销不算。以立法日期而非生效日判断，竞选承诺不算。 |
| 规则指纹 | bad230b7f527696e74d48176c1f04e0fa6e22d9b444c004e912067120edc074f |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:02:49.472044+00:00 |
| 来源 | https://polymarket.com/event/texas-enacts-data-center-moratorium-by-20260928 |

## Major CEX insolvent in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 199777 / 1343533 |
| Yes 概率 % | 3.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.05, -1.45] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.050000000000000044} |
| 24h成交量 / 流动性 USD | [null, 21149.51156] |
| 价差 pp | 1.40 |
| 到期 | 2027-01-01T05:00:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Binance/Coinbase/Bybit/OKX/Kraken任一被正式宣布资不抵债或申请/拟申请任一种破产程序则Yes；按官方代表或可信报道共识。被盗、暂停提款或偿付证明延期本身不是触发。 |
| 规则指纹 | 60d4965584f04350506eafe348b3b70153b2fd33101cc7cd02976facea6531d8 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T09:04:21.476708Z |
| 抓取时间 | 2026-11-06T12:02:49.825217+00:00 |
| 来源 | https://polymarket.com/event/major-cex-insolvent-in-2026 |

## Will Nvidia (NVDA) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1308738 / 6639362 |
| Yes 概率 % | 96.80 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.15, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.100000000000001} |
| 24h成交量 / 流动性 USD | [163.52, 495.84159] |
| 价差 pp | 5.60 |
| 到期 | 2026-11-17T22:00:00+00:00 |
| 结算规则摘要 | NVDA下一次财报首次公布的non-GAAP EPS按美分取整须严格超过固定2.53美元，不是动态一致预期。若缺失依规则转SeekingAlpha，再经96小时转GAAP；预计日后45天未发布为No，后续修订通常不计。低成交、极端报价不等于股票上涨胜率。 |
| 规则指纹 | f9c0b1886ab273be18bc170b3841777783b7f9b2cd80b7ff77a9c0d7a9aa7918 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-06T11:23:13.604762Z |
| 抓取时间 | 2026-11-06T12:03:55.895803+00:00 |
| 来源 | https://polymarket.com/event/nvda-quarterly-earnings-nongaap-eps-11-17-2026-2pt53 |

## Will the US add at least 100k jobs in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1120074 / 5211630 |
| Yes 概率 % | 28.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.0000000000000018} |
| 24h成交量 / 流动性 USD | [2298.629427, 875.2952] |
| 价差 pp | 5.00 |
| 到期 | 2026-11-07T04:59:00+00:00 |
| 结算规则摘要 | 按BLS 2026年10月非农就业增量，至少100k为Yes；边界值落较高档。若到下月发布日仍未发布该月数据，则按最后可用月处理。计划11月6日08:30美东；不是经济衰退概率。 |
| 规则指纹 | 34f44a7c6725e5d40df430e375d2f1b431cbbcb9a48cdc268fed3844d5bd5e51 |
| 质量 | ["liquidity_under_10000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-06T12:01:13.089126Z |
| 抓取时间 | 2026-11-06T12:03:55.896458+00:00 |
| 来源 | https://polymarket.com/event/how-many-jobs-added-in-october-2026 |

## AI 压力：合约、经营与估值分开

三层分开：①事件报价。与早报相同ID且rule_hash一致：2026AI专门合约12.4%→7.8%（-4.6个百分点），2027年6月30.5%→26.5%（-4.0）；年内AnthropicIPO78.4%→70.85%（-7.55）；Oracle年底垃圾评级19%→21.5%但24小时成交缺失、价差3个百分点，不能升级为独立评级事实。AI规则需同一90天内至少三项阈值，不是普通科技回调；SOXX拆股应复权，不可把拆股当40%跌幅。②经营融资：SoftBank单体CDS压力是本次新增风险证据，仍不能推导所有AI公司违约。Counterpoint11月5日原始报告显示CXMT在全球DRAM收入份额Q2 10%→Q3 9%，存储收入增长主要由价格驱动；这与中国厂商已压垮HBM利润的叙事不符。DRAM份额不是HBM份额，更不是NAND；SNDK不能直接套长鑫竞争结论。该报告属于历史季度与研究机构预测，不证明未来毛利。AWS官方11月5日计划在Comanche Peak旁Vistra土地建设园区，并说明水电成本安排，是继续投资的反证；计划不是已建成，也不是新的已确认当期收入。Reuters5日关于60万H200滞留香港属消息源报道，6日被转发不是新订单损失公告；公司未独立确认数量。5日IREN延期与融资待落实、Google长期投入及NET增长见早报历史证据，不装作本轮新公告。H100本次核验仍5日2.97美元/GPU小时，远高于合约1美元连续五日阈值；页首7日涨幅与表格不一致，不引用该涨幅。③整体估值：本次SEC五家定期披露列表均核验，最新日期与早报相同。NVDA沿用已核验FCFF假设并更新可用报价；MSFT/AMZN/GOOGL/META缺最新租赁、净债务、稀释与现金流桥，保持unavailable，不能伪造估值。META5日融资8-K已在早报记录，本次列表无更新。合约定价、经营压力、公司估值隐含要求互不替代。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-11-06T12:04:13.391166+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 181.60 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2448840514337952, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -45.61 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -15.13 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 33.58 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-11-06T12:04:16.053453+00:00", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-06T12:04:18.481535+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-11-06T12:04:21.583718+00:00", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-11-06T12:04:24.095792+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 宽基反弹分级确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 就业与消费者预期发布后 |
| 关联标的 | ["SPY", "QQQ", "RSP"] |
| 确认条件 | SPY守733、QQQ守647.05只是第一层；开盘后30–60分钟低点抬高、突破首30分钟高点后回踩不破，站稳独立核验的常规VWAP，并有RSP/更多板块跟随；收盘延续、次日不吞没才提高可靠性。 |
| 失效条件 | SPY跌破732.71、QQQ跌破647.05后反抽失败，或只芯片涨而RSP持续创新低、VIX重新上行。就业发布前的盘前涨幅不满足条件。 |
| 观察期限 | 今夜两次数据至下周一收盘 |
| 反证 | 高波动容易挤空，盘前价格不是常规量价确认；全成分广度缺失。 |
| 状态 | 早报止跌条件仅盘前初步改善，未正式确认 |

## 芯片强反抽避免追第一根

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 存储研究/项目披露与就业后价格反应 |
| 关联标的 | ["SMH", "NVDA", "MU", "SNDK"] |
| 确认条件 | SMH不再失守447.73，开盘回踩低点抬高；再收复5日高点483.93并保持，相关个股相对SMH同步改善；两个收盘承接更可靠。旧497.33/504.27仍为更远的修复区域。 |
| 失效条件 | 反抽后重新失守447.73，尤其445.59下方反抽失败；单一存储上涨、其它硬件续跌也降低可信度。 |
| 观察期限 | 未来1–3个交易日，财报/融资新增消息随时重评 |
| 反证 | 强烈反弹可以是流动性或回补；未获当期净申赎、持仓变化验证。 |
| 状态 | 观察，盘前不追涨 |

## 防御相对强弱等待自身止跌

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 就业/利率和市场流动性 |
| 关联标的 | ["XLV", "XLP", "XLU", "RSP"] |
| 确认条件 | 自身守5日低点，收复前收并有一次回踩承接；相对SPY的强势保持，不仅是跌得少。 |
| 失效条件 | 同步新低或利率/能源成本上升压估值及利润，防御标签不能替代止损。 |
| 观察期限 | 未来1–3收盘 |
| 反证 | 短期获利回吐风险仍在，20日强不意味着每个交易日上涨。 |
| 状态 | 观察 |

## 融资压力的反证监测

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | AI公司信用和融资、建设交付 |
| 关联标的 | ["NVDA", "MSFT", "AMZN", "GOOGL", "META", "ORCL", "IREN"] |
| 确认条件 | 新云资金落实、延期不扩大、信用价差回落，叠加价格停止下跌；分别核验公司事实。 |
| 失效条件 | 新增延误/非预期稀释与信用走弱共振；单一低量预测合约不触发。 |
| 观察期限 | 未来一周及新披露 |
| 反证 | 已宣布投资和ARR不能等同FCFF，单一发行人CDS不是行业违约率。 |
| 状态 | 维持审慎 |

## 跨期比较与上期剧本复核

对照本日07:15早报：5日收盘和均线状态没有变；此前SPY762.64/QQQ687.87失效仍成立。盘前SPY735.40、QQQ658.02、SMH472.70已高于前收，但尚未经历6日就业和常规开盘，早报要求的回踩/收盘条件未满足；RSP216.60略低前收，降低广泛修复可信度。早报盘后继续跌的即时状态已被当前反弹更新，不能机械延续到盘前。ITA供应商拆股复权已恢复，现可列19样本收益，早报原文件不改。Cboe日线补到5日，信用仍滞后。相同rule_hash合约变化：3215008 +6.00个百分点；2176270 -1.00个百分点；691340 -4.60个百分点；4838928 -4.00个百分点；5211635 +2.50个百分点；2252540 +0.00个百分点；5939428 +2.50个百分点；5401796 -0.50个百分点；2413330 -7.55个百分点；2745561 +5.50个百分点；5123855 +0.00个百分点；5123856 +0.00个百分点；1343533 -0.05个百分点；6639362 -1.10个百分点；5211630 -2.00个百分点。合约元数据更新时间不等于成交时间；非同期限互比。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-11-05/20261105T232152.239453Z/evidence.json",
    "baseline_cutoff": "2026-11-05T23:21:37.252127+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": 0.40518680104322247,
      "CL=F": -0.7020699795221574,
      "BZ=F": -0.9173347386186248,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.00225168036517287,
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
      "ARKX": 0.0,
      "KRE": 0.0,
      "SKYY": 0.0
    },
    "quote_change_pct": {
      "AAPL": {
        "change_pct": -0.5284957205748286,
        "from_observed_at": "2026-11-05T23:16:10+00:00",
        "to_observed_at": "2026-11-06T12:02:48+00:00"
      },
      "AMD": {
        "change_pct": 8.33256935836786,
        "from_observed_at": "2026-11-05T23:16:23+00:00",
        "to_observed_at": "2026-11-06T12:02:51+00:00"
      },
      "AMZN": {
        "change_pct": 2.9177926604785798,
        "from_observed_at": "2026-11-05T23:16:10+00:00",
        "to_observed_at": "2026-11-06T12:02:42+00:00"
      },
      "ARM": {
        "change_pct": 8.65478515625,
        "from_observed_at": "2026-11-05T23:15:53+00:00",
        "to_observed_at": "2026-11-06T12:02:33+00:00"
      },
      "AVGO": {
        "change_pct": 5.355420856867332,
        "from_observed_at": "2026-11-05T23:15:56+00:00",
        "to_observed_at": "2026-11-06T12:02:13+00:00"
      },
      "BABA": {
        "change_pct": 0.4101313320825639,
        "from_observed_at": "2026-11-05T23:16:17+00:00",
        "to_observed_at": "2026-11-06T12:02:35+00:00"
      },
      "CAT": {
        "change_pct": 4.186824817518242,
        "from_observed_at": "2026-11-05T23:15:39+00:00",
        "to_observed_at": "2026-11-06T12:02:45+00:00"
      },
      "CEG": {
        "change_pct": 2.3255813953488413,
        "from_observed_at": "2026-11-05T23:10:13+00:00",
        "to_observed_at": "2026-11-06T11:57:31+00:00"
      },
      "COHR": {
        "change_pct": 13.389978598197128,
        "from_observed_at": "2026-11-05T23:15:46+00:00",
        "to_observed_at": "2026-11-06T12:02:32+00:00"
      },
      "COIN": {
        "change_pct": 2.974144373038423,
        "from_observed_at": "2026-11-05T23:16:11+00:00",
        "to_observed_at": "2026-11-06T12:02:32+00:00"
      },
      "CRWV": {
        "change_pct": 11.63833805476866,
        "from_observed_at": "2026-11-05T23:16:16+00:00",
        "to_observed_at": "2026-11-06T12:02:40+00:00"
      },
      "DRAM": {
        "change_pct": 9.7201411509229,
        "from_observed_at": "2026-11-05T23:15:25+00:00",
        "to_observed_at": "2026-11-06T12:02:39+00:00"
      },
      "GDX": {
        "change_pct": 0.5880514087871491,
        "from_observed_at": "2026-11-05T23:14:14+00:00",
        "to_observed_at": "2026-11-06T12:01:36+00:00"
      },
      "GEV": {
        "change_pct": 4.787318361955095,
        "from_observed_at": "2026-11-05T23:16:10+00:00",
        "to_observed_at": "2026-11-06T12:02:04+00:00"
      },
      "GLD": {
        "change_pct": -0.5816860775723964,
        "from_observed_at": "2026-11-05T23:15:07+00:00",
        "to_observed_at": "2026-11-06T12:01:22+00:00"
      },
      "GLW": {
        "change_pct": 8.785784797630814,
        "from_observed_at": "2026-11-05T23:14:53+00:00",
        "to_observed_at": "2026-11-06T12:00:45+00:00"
      },
      "GOOGL": {
        "change_pct": 1.7350779709625508,
        "from_observed_at": "2026-11-05T23:16:10+00:00",
        "to_observed_at": "2026-11-06T12:02:35+00:00"
      },
      "INTC": {
        "change_pct": 8.978873239436624,
        "from_observed_at": "2026-11-05T23:16:23+00:00",
        "to_observed_at": "2026-11-06T12:02:50+00:00"
      },
      "IWM": {
        "change_pct": 0.48545488234204015,
        "from_observed_at": "2026-11-05T23:13:13+00:00",
        "to_observed_at": "2026-11-06T12:02:28+00:00"
      },
      "LITE": {
        "change_pct": 11.729622266401595,
        "from_observed_at": "2026-11-05T23:16:06+00:00",
        "to_observed_at": "2026-11-06T12:02:43+00:00"
      },
      "LLY": {
        "change_pct": -1.2592603422292292,
        "from_observed_at": "2026-11-05T23:15:16+00:00",
        "to_observed_at": "2026-11-06T12:02:35+00:00"
      },
      "META": {
        "change_pct": 0.8522774655169263,
        "from_observed_at": "2026-11-05T23:15:21+00:00",
        "to_observed_at": "2026-11-06T12:02:31+00:00"
      },
      "MRVL": {
        "change_pct": 11.869850781762704,
        "from_observed_at": "2026-11-05T23:16:14+00:00",
        "to_observed_at": "2026-11-06T12:02:40+00:00"
      },
      "MSFT": {
        "change_pct": 0.3043478260869481,
        "from_observed_at": "2026-11-05T23:15:48+00:00",
        "to_observed_at": "2026-11-06T12:02:42+00:00"
      },
      "MU": {
        "change_pct": 9.539443404620895,
        "from_observed_at": "2026-11-05T23:16:18+00:00",
        "to_observed_at": "2026-11-06T12:02:51+00:00"
      },
      "NOW": {
        "change_pct": 1.4995501349595042,
        "from_observed_at": "2026-11-05T23:15:57+00:00",
        "to_observed_at": "2026-11-06T12:02:41+00:00"
      },
      "NVDA": {
        "change_pct": 4.8143742357067865,
        "from_observed_at": "2026-11-05T23:16:17+00:00",
        "to_observed_at": "2026-11-06T12:02:43+00:00"
      },
      "ORCL": {
        "change_pct": 5.3667255075022124,
        "from_observed_at": "2026-11-05T23:16:07+00:00",
        "to_observed_at": "2026-11-06T12:02:44+00:00"
      },
      "PLTR": {
        "change_pct": 4.16461940606514,
        "from_observed_at": "2026-11-05T23:16:07+00:00",
        "to_observed_at": "2026-11-06T12:02:51+00:00"
      },
      "QCOM": {
        "change_pct": 3.9334825711544674,
        "from_observed_at": "2026-11-05T23:14:49+00:00",
        "to_observed_at": "2026-11-06T12:02:35+00:00"
      },
      "QQQ": {
        "change_pct": 2.345340232280302,
        "from_observed_at": "2026-11-05T23:16:16+00:00",
        "to_observed_at": "2026-11-06T12:02:44+00:00"
      },
      "RSP": {
        "change_pct": 0.17931640534665227,
        "from_observed_at": "2026-11-05T23:15:59+00:00",
        "to_observed_at": "2026-11-06T12:00:55+00:00"
      },
      "SMH": {
        "change_pct": 6.476793938008285,
        "from_observed_at": "2026-11-05T23:16:13+00:00",
        "to_observed_at": "2026-11-06T12:02:33+00:00"
      },
      "SNDK": {
        "change_pct": 11.907472336192981,
        "from_observed_at": "2026-11-05T23:16:12+00:00",
        "to_observed_at": "2026-11-06T12:02:47+00:00"
      },
      "SPY": {
        "change_pct": 0.8295057242750259,
        "from_observed_at": "2026-11-05T23:16:04+00:00",
        "to_observed_at": "2026-11-06T12:02:36+00:00"
      },
      "STX": {
        "change_pct": 8.811744274394883,
        "from_observed_at": "2026-11-05T23:14:20+00:00",
        "to_observed_at": "2026-11-06T12:02:32+00:00"
      },
      "TLT": {
        "change_pct": -0.17658560430159342,
        "from_observed_at": "2026-11-05T23:15:59+00:00",
        "to_observed_at": "2026-11-06T12:01:12+00:00"
      },
      "VRT": {
        "change_pct": 9.85615650172611,
        "from_observed_at": "2026-11-05T23:15:29+00:00",
        "to_observed_at": "2026-11-06T12:02:12+00:00"
      },
      "XLE": {
        "change_pct": -0.5826466311197209,
        "from_observed_at": "2026-11-05T23:03:18+00:00",
        "to_observed_at": "2026-11-06T12:00:04+00:00"
      },
      "XLF": {
        "change_pct": -0.7489104145735448,
        "from_observed_at": "2026-11-05T23:16:05+00:00",
        "to_observed_at": "2026-11-06T12:00:40+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-04"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-04"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-11-04"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-04"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-04"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-11-05"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-30"
      },
      "CBOE_VIX": {
        "change": 11.57,
        "unit": "index",
        "observation_date": "2026-11-05"
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
      "3215008": {
        "status": "comparable",
        "change_pp": 5.999999999999995
      },
      "2176270": {
        "status": "comparable",
        "change_pp": -0.9999999999999996
      },
      "691340": {
        "status": "comparable",
        "change_pp": -4.6
      },
      "4838928": {
        "status": "comparable",
        "change_pp": -3.9999999999999982
      },
      "5211635": {
        "status": "comparable",
        "change_pp": 2.500000000000002
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5939428": {
        "status": "comparable",
        "change_pp": 2.4999999999999996
      },
      "5401796": {
        "status": "comparable",
        "change_pp": -0.5000000000000004
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -7.550000000000001
      },
      "2745561": {
        "status": "comparable",
        "change_pp": 5.499999999999999
      },
      "5123855": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5123856": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "1343533": {
        "status": "comparable",
        "change_pp": -0.050000000000000044
      },
      "6639362": {
        "status": "comparable",
        "change_pp": -1.100000000000001
      },
      "5211630": {
        "status": "comparable",
        "change_pp": -2.0000000000000018
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
    "event": "美国10月就业；同时检查工资、U-3与修订",
    "date": "2026-11-06T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "密歇根11月消费者信心初值及通胀预期",
    "date": "2026-11-06T10:00:00-05:00",
    "source": "https://www.sca.isr.umich.edu/"
  },
  {
    "event": "美国10月CPI（官方11月10日，tc旧缓存12日不采用）",
    "date": "2026-11-10T08:30:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "NVDA Q3 FY27电话会（官方11月17日，tc缓存25日不采用）",
    "date": "2026-11-17T17:00:00-05:00",
    "source": "https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/default.aspx"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| us-premarket-rebound | Reuters报道6日芯片盘前反抽；本报告价格由实际分钟另行核验，不照搬新闻时点涨幅。 | 缺失 | [{"source": "https://za.investing.com/news/stock-market-news/nasdaq-futures-rise-after-steep-ai-selloff-as-chip-stocks-stabilize-4557213", "published_at": null, "retrieved_at": "2026-11-06T12:08:33.873810+00:00"}] |
| softbank-credit | Reuters引Markit：SoftBank五年CDS在6日06:53UTC为457.5bp；是单体融资压力，非客观全行业违约概率。 | 2026-11-06T06:53:00+00:00 | [{"source": "https://www.zawya.com/en/business/softbank-credit-risk-jumps-to-4-year-high-shares-tumble-as-ai-fears-roil-market-2045075", "published_at": null, "retrieved_at": "2026-11-06T12:08:33.873810+00:00"}] |
| counterpoint-q3-memory | 研究机构原始报告：CXMT DRAM收入份额Q2 10%→Q3 9%，HBM产品组合和价格驱动收入；不同于HBM份额或NAND竞争。 | 缺失 | [{"source": "https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b", "published_at": null, "retrieved_at": "2026-11-06T12:08:33.873810+00:00"}] |
| amazon-somervell | AWS官方5日园区计划位于Comanche Peak附近Vistra土地；用水/基础设施承诺不等于项目已建成。 | 缺失 | [{"source": "https://press.aboutamazon.com/2026/11/our-responsible-approach-to-investing-in-somervell-county-texas", "published_at": null, "retrieved_at": "2026-11-06T12:08:33.873810+00:00"}] |
| h200-hongkong | Reuters5日消息源称60万H200待大陆进口许可；6日转发不是新的已确认库存减值或订单取消。 | 缺失 | [{"source": "https://www.investing.com/news/stock-market-news/exclusivenvidia-chips-pile-up-in-hong-kong-as-china-withholds-import-approval-5003223", "published_at": null, "retrieved_at": "2026-11-06T12:08:33.873810+00:00"}] |
| google-wyoming | Google官方170亿美元长期Wyoming投资，承诺承担其用电与相关基础设施成本；不是当季已付资本开支。 | 缺失 | [{"source": "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/wyoming-data-center/", "published_at": null, "retrieved_at": "2026-11-05T23:21:22.602048+00:00"}] |
| iren-results | 盘后更新：AI云收入2亿美元，目标投运后移至1月或2月；后续部分扩张融资依赖市场。 | 缺失 | [{"source": "https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results", "published_at": null, "retrieved_at": "2026-11-05T23:21:22.602048+00:00"}] |
| net-results | 盘后业绩：收入增长39%、全年non-GAAP EPS1.35；FCF率10%低于去年13%。 | 缺失 | [{"source": "https://www.cloudflare.com/zh-tw/press/press-releases/2026/cloudflare-announces-third-quarter-2026-financial-results/", "published_at": null, "retrieved_at": "2026-11-05T23:21:22.602048+00:00"}] |
| meta-funding | 5日8-K：既有150亿美元债完成；600万股额外远期销售协议行使，不重复计债额。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526450074/d166273d8k.htm", "published_at": null, "retrieved_at": "2026-11-05T23:21:22.602048+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN接口418；CME官方页面超时，不能以tc温度或加密恐贪替代。",
  "真实全成分广度、新高新低及可靠常规VWAP缺失；第三方样本范围不一致，未纳入官方广度。盘前成交量不与全天量比。",
  "19ETF当期净申赎、份额拆分桥和逐日机构持仓缺失；仅有10月28日ICI估算窗口。ITA价格复权已恢复，但跨拆股量比未独立验证。",
  "FRED利率及HY/IG仍4日、GPR2日、压力指标10月30日，不能当今日即时数据；当前期货存在换月和延迟。",
  "tc一般50条与高影响主题50条限制，来源当前包含财联社等但均只作线索，不能从一次查询声称完整新闻覆盖。",
  "Polymarket主动搜索与基础查询截断；小成交/宽价差或缺成交降低有效性，不采用供应商未经规则核验的1d/1w变化。",
  "四家公司完整FCFF/租赁/稀释桥仍缺失；不因复核到最新财报列表就编造财务输入。",
  "H100最新仍5日；页首7D变动与明细不一致，仅使用日期明确的2.97。",
  "Reuters消息源H200库存与SoftBank信用属报道证据；Brightspeed 1GW方案未获得公司正式公告，本次不将其写成确定订单。",
  "就业和密歇根初值尚未发布，不填实际结果。盘前报价时点异步，未覆盖收盘确认。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 本次新增30日FWP，29日已定价250亿美元债券、11月4日预定结算；新财报完整TTM/租赁/净债务桥仍缺，不沿用旧精确DCF。",
  "AMZN 估值: 30日新增Q3 10-Q已核验；最新TTM、融资租赁/净债务与稀释桥尚未完整，不沿用旧估值。",
  "GOOGL 估值: 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
  "META 估值: 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。",
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
  "tc 报价质量 stale: CI, COP, CVX, IGV, TAN, XLI, XLV, XOM；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.CI.value, quotes.COP.value, quotes.CVX.value, quotes.IGV.value, quotes.TAN.value, quotes.XLI.value, quotes.XLV.value, quotes.XOM.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.cloudflare.com/zh-tw/press/press-releases/2026/cloudflare-announces-third-quarter-2026-financial-results/",
    "checked_at": "2026-11-05T23:21:22.602048+00:00",
    "note": "早报已核验的历史公告，保留原时点"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000119312526450074/d166273d8k.htm",
    "checked_at": "2026-11-05T23:21:22.602048+00:00",
    "note": "早报已核验的历史公告，保留原时点"
  },
  {
    "url": "https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/wyoming-data-center/",
    "checked_at": "2026-11-05T23:21:22.602048+00:00",
    "note": "早报已核验的历史公告，保留原时点"
  },
  {
    "url": "https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-q1-fy27-results",
    "checked_at": "2026-11-05T23:21:22.602048+00:00",
    "note": "早报已核验的历史公告，保留原时点"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-06T12:03:34.470138+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://www.sca.isr.umich.edu/",
    "checked_at": "2026-11-06T12:08:33.873810+00:00",
    "note": "本次官方原文或Reuters原始报道核验；未确定公告小时留空"
  },
  {
    "url": "https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b",
    "checked_at": "2026-11-06T12:08:33.873810+00:00",
    "note": "本次官方原文或Reuters原始报道核验；未确定公告小时留空"
  },
  {
    "url": "https://www.zawya.com/en/business/softbank-credit-risk-jumps-to-4-year-high-shares-tumble-as-ai-fears-roil-market-2045075",
    "checked_at": "2026-11-06T12:03:54.202513+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://press.aboutamazon.com/2026/11/our-responsible-approach-to-investing-in-somervell-county-texas",
    "checked_at": "2026-11-06T12:03:53.822116+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://za.investing.com/news/stock-market-news/nasdaq-futures-rise-after-steep-ai-selloff-as-chip-stocks-stabilize-4557213",
    "checked_at": "2026-11-06T12:08:33.873810+00:00",
    "note": "本次官方原文或Reuters原始报道核验；未确定公告小时留空"
  },
  {
    "url": "https://www.investing.com/news/stock-market-news/exclusivenvidia-chips-pile-up-in-hong-kong-as-china-withholds-import-approval-5003223",
    "checked_at": "2026-11-06T12:08:33.873810+00:00",
    "note": "本次官方原文或Reuters原始报道核验；未确定公告小时留空"
  },
  {
    "url": "https://www.ishares.com/us/products/239502/ishares-global-infrastructure-etf",
    "checked_at": "2026-11-06T12:03:55.056962+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-06T12:03:34.762231+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-06T12:03:34.909213+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://ecommerce.ismworld.org/SSO/Login.aspx?DPLF=Y&vi=10&vt=8cb238c1c9af0d9a01fe13d766c5eea4b61703e8ea7dadcbf4df21bf26eef079a9dac479deb3fc8f6ec90920b0e8aa1a273ff42ab8fc86cbf1a7d56163e2db0693d8267ddd2f6d94f9724c05c80c6cac747fbb5db4c1a7c193befdad73d2b062dada34b9f8c662bb1df4c3bb472a33963427918e79b9c3f6e4e67e2a2c72b6c0",
    "checked_at": "2026-11-06T12:03:38.098840+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://newsroom.arm.com/news/arm-q2-fye27-results",
    "checked_at": "2026-11-06T12:03:38.235431+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://investors.terawulf.com/news-events/press-releases",
    "checked_at": "2026-11-06T12:03:40.154863+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-06T12:03:35.960430+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://investor.nvidia.com/events-and-presentations/events-and-presentations/default.aspx",
    "checked_at": "2026-11-06T12:03:35.644875+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://home.treasury.gov/news/press-releases/sb0678/",
    "checked_at": "2026-11-06T12:03:45.539360+00:00",
    "note": "本次公开原文检查"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ARM",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CI",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COHR",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COIN",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COP",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CRWV",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GDX",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LITE",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MRVL",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QCOM",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TAN",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-11-06T12:02:55.998276+00:00",
    "note": "实际分钟时间；只用于当前报价，未计算常规VWAP"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
