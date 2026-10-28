# 每日交易总结 · 2026-10-28

## 一分钟读懂 · Agent 摘要

### 当前判断

修复仍在，但可靠性下降。收盘上涨不能抵消盘后财报冲击，目前不适合把局部反弹认作全面反转。

### 与上次相比

美联储维持3.75%–4.00%，两票主张加息。微软云增长强，Alphabet云需求也强但现金支出沉重；两家盘后走势分化，软件和半导体受压。

### 最重要的信号

- 28日QQQ收725.61、SMH567.67，但量能仅前20日均量约0.79/0.73倍，等权RSP微跌。
- 本次盘后分钟行情：QQQ716.81（较28日收盘-1.21%）、SMH558.37（较28日收盘-1.64%）；已回吐主要收盘涨幅。
- VIX收16.91、信用利差改善仍有滞后，尚无全面恐慌证据；低VIX也不能保证财报风险消失。

### 接下来观察

- 29日开盘看QQQ先收复721.25，再守725.10–725.61；SMH先守557.98–559.81，再收567.67。
- 优先看存储/电力设备能否抗跌；软件云等待重新承接，金融与等权验证扩散。
- 北京时间今晚20:30 GDP/PCE；次日04:30 Sandisk、05:00 Amazon电话会，勿把EPS过线等同股价上涨。

### 不要忽略

盘后流动性较薄，无29日开盘区间/VWAP；CNN、真实广度和当期板块申赎缺失，新财报融资租赁桥待补。

## 研究结论

10月29日早报：28日收盘修复继续，但盘后云厂商财报分化引发纳指、半导体和软件回吐；反弹可靠性下调，等待下一交易日承接。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-28 → 2026-10-28（纽约交易日） |
| 截止·纽约 | 2026-10-28T19:41:44.078124-04:00 |
| 截止·北京 | 2026-10-29T07:41:44.078124+08:00 |
| 实际生成时间 | 2026-10-28T23:41:44.297016+00:00 |
| 市场阶段 | 盘后 |
| 下一交易日 | 2026-10-29 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-27/20261028T120914.307689Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-29T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-28T23:34:17.113935+00:00 / 2026-10-28T23:34:17.113935+00:00 | Gamma snapshot, not last trade; reviewed settlement definition |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-10-28T23:34:19.715644+00:00 / 2026-10-28T23:34:19.715644+00:00 | Gamma snapshot, not last trade; reviewed settlement definition |
| 1200533 | 已校验接入 | https://gamma-api.polymarket.com/events/1200533 | 2026-10-28T23:34:17.087893+00:00 / 2026-10-28T23:34:17.087893+00:00 | Gamma snapshot, not last trade; reviewed settlement definition |
| 1200552 | 已校验接入 | https://gamma-api.polymarket.com/events/1200552 | 2026-10-28T23:34:17.111141+00:00 / 2026-10-28T23:34:17.111141+00:00 | Gamma snapshot, not last trade; reviewed settlement definition |

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
| prices.SPY.value | 772.31 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 0.34 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -0.10 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | 1.27 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 0.38 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.90 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.83 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 725.23 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | 0.18 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | 0.71 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 6.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.09 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.92 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -0.87 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.76 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 725.61 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 0.60 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | 0.06 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -1.91 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 0.35 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.26 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | 0.16 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -3.18 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -0.03 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 732.48 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 725.10 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 677.55 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -0.94 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | 0.07 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 7.09 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 11.93 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.64 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -4.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.79 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 281.29 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 0.40 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 1.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 1.22 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -6.52 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.05 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.84 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -0.05 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -6.90 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.27 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 284.72 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.49 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 1.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -1.20 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 1.37 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.50 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -7.56 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.75 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 217.43 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | -0.04 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.36 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 4.52 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | -0.90 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.39 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 0.47 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 3.25 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -1.28 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 213.91 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.77 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.29 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.64 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.40 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 1.95 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.90 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -2.03 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 0.97 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 373.51 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 0.33 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -1.44 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -1.92 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -0.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | -0.01 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -1.33 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -3.19 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -0.55 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 377.69 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 392.67 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 413.54 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -1.11 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -4.88 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -9.68 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.13 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.37 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -12.75 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,065.30 | USD_per_troy_ounce | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | -0.23 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -2.04 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -2.90 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -2.10 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | -0.57 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -1.94 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -4.17 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -2.48 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,137.44 | USD_per_troy_ounce | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,318.80 | USD_per_troy_ounce | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,525.91 | USD_per_troy_ounce | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -1.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -5.87 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.18 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 66.04 | USD_per_troy_ounce | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.62 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -13.46 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.02 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 101.94 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | 2.04 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | 4.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 12.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 34.54 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | 1.70 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | 5.03 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 11.47 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 34.16 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 96.29 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 93.96 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.92 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 5.87 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 8.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 18.64 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.20 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.12 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -3.68 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.01 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 110.59 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -2.89 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 1.63 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 6.82 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 39.35 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -3.23 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 1.73 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 5.55 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 38.98 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 107.31 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 102.23 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 91.93 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 3.06 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 8.18 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 20.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.81 | USD_per_barrel | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -5.25 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 80.99 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -0.78 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 4.55 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -1.44 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -1.13 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.04 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 3.28 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -1.82 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 79.26 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.29 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.26 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 2.19 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 0.88 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -2.73 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.80 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.99 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -2.21 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.80 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.06 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.21 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.01 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.20 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -0.55 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.58 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | -0.26 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 2.82 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.99 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.54 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.91 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.23 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.82 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.13 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.11 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.39 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.94 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.59 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.01 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 0.79 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.94 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.36 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.89 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | -0.33 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -1.87 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.10 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.86 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.64 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.35 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.39 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.30 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.38 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -1.95 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 1.16 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.07 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.22 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 0.83 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.69 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.56 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.93 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 1.02 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -2.06 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.97 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.82 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.87 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.07 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.70 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.60 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.58 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.78 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.03 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 16.91 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -3.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 1.38 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 3.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 6.96 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -3.83 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 1.48 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 2.22 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 6.38 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.75 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.07 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.23 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 0.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 5.21 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | -7.26 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.01 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 11.91 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -15.41 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-28 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 19.22 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -1.79 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 2.67 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 4.63 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | -0.62 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -2.13 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 2.77 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 3.36 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | -1.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.81 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.53 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.50 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 2.20 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 3.75 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -6.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.11 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 5.78 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -6.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-28 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 96.61 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -2.86 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 2.18 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 7.97 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 4.36 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -3.20 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 2.28 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 6.70 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 3.99 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 94.24 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 91.04 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.81 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 2.51 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 6.11 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | -2.23 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 9.45 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 9.78 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -12.10 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-28 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 94.55 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -3.39 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -1.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -11.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 17.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -3.74 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -1.35 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -12.37 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 15.30 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 102.69 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 89.40 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 77.19 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -7.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 5.76 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 22.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.01 | index | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -16.77 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-28 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 215.38 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -1.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -2.97 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -5.69 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 1.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -1.52 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -2.87 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -6.96 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | 1.36 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 223.79 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.00 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.84 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -3.76 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -2.98 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 5.66 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.05 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.81 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -9.97 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 531.01 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -0.06 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -0.36 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 3.53 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 7.95 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -0.40 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -0.26 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 2.26 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 7.58 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 529.90 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 511.16 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 436.21 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 0.21 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 3.88 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 21.73 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 10.62 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.00 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -2.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.25 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 254.60 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 0.59 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -2.96 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 2.19 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -8.23 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 0.25 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -2.86 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 0.92 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -8.60 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 255.17 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 255.12 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.38 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -0.22 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -0.20 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 4.61 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 6.67 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.62 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -10.36 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.94 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 324.89 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 1.34 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -2.95 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -5.58 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -13.92 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 1.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -2.85 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -6.85 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -14.29 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 339.81 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 341.45 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.88 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -4.39 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -4.85 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -4.69 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.05 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -13.92 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 2.22 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 612.49 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -1.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -12.19 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -15.54 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 4.26 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -1.59 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -12.09 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -16.81 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 3.88 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 701.83 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 666.82 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.29 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -12.73 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -8.15 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -2.98 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 25.55 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 4.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -21.23 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 1.66 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 63.93 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 7.32 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | 3.41 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -26.62 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -30.44 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 6.97 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | 3.51 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -27.89 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -30.81 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 71.90 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 80.75 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 91.66 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -11.08 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -20.83 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -30.25 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.37 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 9.96 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -40.66 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 1.08 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 983.23 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 5.86 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | 7.61 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -7.67 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 10.16 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 5.52 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 7.71 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -8.94 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 9.79 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 968.20 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 980.43 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 740.88 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | 1.55 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | 0.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 32.71 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 48.06 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 4.89 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -10.39 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.11 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 54.12 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 7.13 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 10.09 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -10.34 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -1.40 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 6.78 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 10.19 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -11.61 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -1.78 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 53.18 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 56.23 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-28 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | 1.77 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -3.75 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-28 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.69 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 4.98 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -14.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.17 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 242.94 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 16.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 14.51 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | 0.68 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -9.98 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 16.14 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 14.61 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -0.59 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -10.35 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 226.08 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 243.53 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 269.76 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | 7.46 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -0.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -9.94 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 13.40 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.52 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -17.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 3.33 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 191.00 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 0.80 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | 1.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -2.43 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 2.31 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 0.45 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | 1.41 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -3.70 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 1.94 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 192.33 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.56 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 168.84 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -0.69 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | 0.76 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 13.12 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.14 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -5.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.89 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 68.45 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | 0.35 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 0.43 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 11.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 17.66 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | 0.01 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 0.53 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 10.03 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 17.29 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.46 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.53 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 57.92 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 3.00 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 6.07 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 18.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.40 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.05 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -1.71 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.89 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 56.13 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 0.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.16 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 5.11 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -2.68 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 0.10 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 0.26 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 3.84 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -3.06 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 55.01 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.88 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.37 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 2.04 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 0.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 5.16 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.69 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.22 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -3.81 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.73 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 168.49 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 0.34 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 0.11 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | 0.90 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -9.37 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | -0.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 0.21 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -0.36 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -9.74 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.14 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 170.97 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.52 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 0.21 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -1.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -2.33 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.49 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -9.42 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.12 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 179.72 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | 0.30 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 0.44 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 6.71 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 11.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.04 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 0.54 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 5.44 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 10.92 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 173.87 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 171.51 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.38 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.37 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 4.79 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 14.20 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.04 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.69 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.87 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 86.84 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -0.36 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | -0.31 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 7.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 2.39 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -0.70 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | -0.21 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 6.47 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 2.02 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 85.17 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.25 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.49 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 1.96 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 3.08 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 4.01 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.33 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.53 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -3.50 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.95 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 115.33 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | -0.10 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | -0.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 5.96 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -2.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | -0.45 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | -0.07 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 4.69 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -2.66 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 112.88 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.20 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.23 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 1.88 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 0.09 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.65 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.43 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.57 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 103.14 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -0.42 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -5.35 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -7.06 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -7.64 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -0.77 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -5.25 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -8.33 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -8.02 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 109.36 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 110.97 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.50 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -5.69 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -7.05 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -8.32 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.78 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.72 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -10.12 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.25 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.49 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | -0.84 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 1.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 7.73 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -2.96 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | -1.18 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 1.27 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 6.46 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -3.34 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 41.60 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.64 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.79 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 2.15 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 2.05 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -2.97 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.60 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.42 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -3.51 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.57 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.13 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.73 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 0.17 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 2.98 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -5.95 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -1.07 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 0.27 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 1.71 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -6.32 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.71 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.57 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.74 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 1.00 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | -1.02 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | -1.43 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.64 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.51 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -6.34 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.86 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.15 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 1.05 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 6.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 0.19 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | -0.19 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 1.15 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 5.22 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | -0.19 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 50.31 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.88 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.68 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 3.09 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 1.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 2.33 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.65 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.25 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -2.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 0.86 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 567.67 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 1.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | 1.97 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -6.79 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -1.40 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 1.39 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | 2.07 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -8.06 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -1.77 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 578.11 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 573.40 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 517.98 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -1.81 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -1.00 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 9.59 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 18.58 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.27 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -10.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.73 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 111.91 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 0.12 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | 2.84 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | 5.10 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 9.72 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.23 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | 2.94 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | 3.83 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 9.34 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 109.48 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.84 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.91 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | 2.22 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 4.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 19.16 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.84 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.54 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -0.67 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.14 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 200.37 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | 0.18 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | 0.68 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 11.73 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 16.99 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -0.16 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | 0.78 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 10.46 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 16.62 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 195.40 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.77 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 168.84 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 2.55 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 5.03 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 18.67 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 4.98 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.49 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -2.19 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 0.73 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 409.10 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 0.06 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 3.94 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | 8.12 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 4.32 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -0.29 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 4.04 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 6.85 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 3.95 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 389.26 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 401.46 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 396.78 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 5.10 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | 1.90 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | 3.11 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.55 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.82 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -6.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 1.58 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 207.74 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 0.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 0.95 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 0.27 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -17.02 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 0.39 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 1.05 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -1.00 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -17.40 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.20 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 215.81 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.85 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 0.75 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -3.74 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -9.22 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.01 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 1.93 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -17.87 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.80 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -0.13 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 0.82 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -3.45 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -7.23 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -0.47 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 0.92 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -4.72 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -7.60 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.19 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.87 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.52 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -1.24 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -3.37 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -5.29 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.73 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.37 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -11.65 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.55 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.11 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.65 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 2.11 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 3.85 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -6.83 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.99 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 2.21 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 2.58 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -7.21 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.41 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.88 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.28 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 2.42 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.32 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 2.61 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.24 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.72 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.94 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.78 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 172.31 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 0.50 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 3.41 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | 5.07 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 12.31 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 0.15 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 3.51 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | 3.80 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 11.93 | pp | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 168.07 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.67 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 136.15 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | 2.53 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 4.64 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 26.56 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.81 | USD_per_share | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.79 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -1.48 | percent | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 1.06 | ratio | 2026-10-28 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.70 | percent | 2026-10-27 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.18 | percentage_points | 2026-10-27 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.88 | percentage_points | 2026-10-27 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.99 | percent | 2026-10-27 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.64 | percent | 2026-10-27 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.38 | percent | 2026-10-28 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.58 | index | 2026-10-23 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 17.52 | index | 2026-10-27 | lagged | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 165.25 | index | 2026-10-26 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 149.77 | index | 2026-10-26 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 187.38 | index | 2026-10-26 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 181.42 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 175.44 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AMZN.value | 252.96 | USD_per_share | 2026-10-28T23:38:08+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.AVGO.value | 342.68 | USD_per_share | 2026-10-28T23:38:08+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.CEG.value | 257.00 | USD_per_share | 2026-10-28T23:27:30+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.DRAM.value | 52.55 | USD_per_share | 2026-10-28T23:37:44+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GEV.value | 867.00 | USD_per_share | 2026-10-28T23:08:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 371.18 | USD_per_share | 2026-10-28T23:35:28+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 128.68 | USD_per_share | 2026-10-28T23:38:17+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 292.73 | USD_per_share | 2026-10-28T23:38:17+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 107.56 | USD_per_share | 2026-10-28T23:25:27+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.IWM.value | 282.00 | USD_per_share | 2026-10-28T23:36:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.META.value | 616.95 | USD_per_share | 2026-10-28T23:38:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MSFT.value | 544.72 | USD_per_share | 2026-10-28T23:38:09+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 957.75 | USD_per_share | 2026-10-28T23:38:08+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 123.94 | USD_per_share | 2026-10-28T23:38:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 213.91 | USD_per_share | 2026-10-28T23:37:36+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.NXPI.value | 248.70 | USD_per_share | 2026-10-28T21:35:35+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.ORCL.value | 140.78 | USD_per_share | 2026-10-28T23:38:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.QQQ.value | 716.81 | USD_per_share | 2026-10-28T23:38:10+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 217.53 | USD_per_share | 2026-10-28T22:51:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 558.37 | USD_per_share | 2026-10-28T23:36:23+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 1,361.96 | USD_per_share | 2026-10-28T23:38:17+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 768.48 | USD_per_share | 2026-10-28T23:38:08+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 678.51 | USD_per_share | 2026-10-28T23:38:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TLT.value | 81.20 | USD_per_share | 2026-10-28T23:31:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 236.66 | USD_per_share | 2026-10-28T23:36:53+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 68.69 | USD_per_share | 2026-10-28T23:23:45+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 56.43 | USD_per_share | 2026-10-28T23:25:38+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| afterhours.BZ_F.value | 110.59 | USD/barrel | 2026-10-28T23:22:00+00:00 | lagged | 真实分钟时间，延迟报价；连续期货合约未对齐不计算结算收益；VIX为常规结束读数非盘后实时 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| afterhours.CL_F.value | 101.95 | USD/barrel | 2026-10-28T23:27:28+00:00 | lagged | 真实分钟时间，延迟报价；连续期货合约未对齐不计算结算收益；VIX为常规结束读数非盘后实时 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| afterhours.ES_F.value | 7,751.25 | index points | 2026-10-28T23:28:13+00:00 | lagged | 真实分钟时间，延迟报价；连续期货合约未对齐不计算结算收益；VIX为常规结束读数非盘后实时 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| afterhours.NQ_F.value | 29,662.75 | index points | 2026-10-28T23:28:19+00:00 | lagged | 真实分钟时间，延迟报价；连续期货合约未对齐不计算结算收益；VIX为常规结束读数非盘后实时 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| afterhours.VIX.value | 16.91 | index points | 2026-10-28T20:15:00+00:00 | lagged | 真实分钟时间，延迟报价；连续期货合约未对齐不计算结算收益；VIX为常规结束读数非盘后实时 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.6500244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.780029296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.21619928827487644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.1810174783909657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.18021433819782606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5543866065127134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5548232961871014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.581616879806468,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.4590402596209806,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.2337886022334015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.48399963378915345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0149993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.13521972656246817,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5196350097656932,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.41268981933592386,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.9897805786132494,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.281036395429779,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.10313611675614176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3278797099193431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.03345033389319241,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3049808538889254,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.40083637888335133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1914280482700894,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.020721435546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.02803294988268501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0036066981232923956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.34014354217296594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.10012055988232182,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.04536050582480777,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.01062286445239602,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.3599853515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.40997314453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6662047039380781,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4503581186979133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.44790511258037125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5709709912513072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.34626302154165955,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.2458698962310435,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.7851602081115034,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -7.123372625555091,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4500054156632016,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2693406403069476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2676907743825452,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.1253575977640207,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2085602746454418,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.33574698357542454,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3261199484905228,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.8895840233216896,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7080017089843977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.595001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.17693725585934317,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2501416015625182,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5028436279296784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.283980407714921,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6903241896999757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9394422955049997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5770179585560142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.2286780256444021,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5644296034180263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.30150903248593597,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6199994768415191,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6685791015625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09590362734012858,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.09126262646503713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5739390655946863,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.05396798028389771,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.054509376949870125,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.12185497141568313,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.110015869140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.80999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7554874846597892,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.14234962190107225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.14425460950815427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.1433167432811855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8041697740633458,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.1531296425607147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3567164643577545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.0134926909769248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5392881963849128,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.32336710029203797,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.32446894770598034,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.41106986323152794,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.24934647787624442,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.5715127627542467,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1023237952632261,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.2202959112564757,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.16999969482418464,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4835006713867074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.36315856933595114,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.415239257812516,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.10776000976562727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5401119232177507,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.338345069534407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.908357272074479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5152198810501218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.5061953158637684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3607998078392294,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.5391049418627012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06357029506138412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.3771427699497769,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.027620641962388337,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.1580644081523872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.36478250696735426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.5807007960067176,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0038547968344722072,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1482847252786803,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0900115966796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7899932861328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.14723522132793487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.40272558608456244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.40436148196336674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.7806599760002095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6954335014336399,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0012364233056523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.4657326156430117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.792029544196371,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.06896406694694157,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.22170810769359672,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.22414714376554068,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.226273369487496,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.14061020524653856,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4196195434991843,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.00669235602203111,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.44175905803703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4704994201660213,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.9184989929199219,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03073822021482897,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.3202755737304699,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.10993759155272187,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5749766540527332,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.26622936526556895,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5472067479723064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0274172420847707,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5180259172477664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09985705554460544,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0894284830086578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.05014256068638412,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.06728581019810265,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.02268124560531859,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.03432537202429986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.04055750306587447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.35595585798094964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09265186437359163,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.01732450258910556,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.230010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.44000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8821478414424488,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.013839505339729996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.013595912033292912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.222807029081797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8463456058653285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.6209207063093256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3270681625181515,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.7673308277426756,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6659485531675724,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.16717797305123572,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.16661842616453315,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.6684204225690835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2915223096782271,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0393038265028571,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.131972097102829,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.466457774490726,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.36649932861331536,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.8760009765625227,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5007995605468523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.203599853515584,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.24360000610352017,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.106900024414017,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.42121847788226807,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4211355341477985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.43400787603741264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6044136205722186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3504358435950099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.0708580250479383,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.051428658621651024,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.200714111328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.009279773614047304,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07266874521435374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.28733874489751443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2708207415442754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4872345013574547,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.2679778941815284,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -9.300048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -84.699951171875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.1246439258131735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4068738715935716,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.39948152215154575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.065819629036015,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.38512505082962667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9999284626901028,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.71359533244968,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.858136998973272,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9084446375382971,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.22585639320260587,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2192671839537197,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.5114330225233017,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.939948347016728,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.4183115828836348,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2545550728286994,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6243483967398711,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -6.07000732421875,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -45.370031738281796,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -7.106000976562427,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -39.45800292968761,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.7470007324218386,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -11.441502685546766,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.08050849322494003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.959187388686833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.060360712732466126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.0912160019858401,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.15087512073482934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.6402276050540792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.7571498325892918,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.6357421875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03941693057879081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.030359000388379576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.19796605250921218,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.8029706393056788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8299092188236454,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.064449761758987,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.0400009155273438,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.790000915527344,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.8698736773985942,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.6004468450821525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 6.787283989074799,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.7641464370272484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.970573058027302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.326055115870078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 10.192210003652068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 11.96746182800905,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.086072965673471,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.781464323473118,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 6.967498327272625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.3185330435399614,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4157497618402015,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.744438236063611,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 11.651250263273045,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 16.20125043024245,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5760002136230469,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.3460002899170007,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3400000000000034,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7996000671386696,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.21220001220703466,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0842000198364303,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.494264152304181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.4550179150067075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.78494881672282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.0788941418767424,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.0863700501607667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.129824982798345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.19142859322684203,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2185728890555252,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.27571087836318675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4280222051603433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.9276205992927897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.526127593925611,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9642900325455507,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.3219075480892721,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.2900009155273438,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7699966430664062,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.222483793384721,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.916581786487338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.0521992902591943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9757664998270243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.1856953718600645,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2507888366489306,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.4086554465958514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 9.943341005834203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.0062845051098446,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.735564308096372,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.8719849520613683,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4213798933143109,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.740518668047166,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6691719568424626,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.8676957062168285,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 14.177129608067602,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.35299987792969034,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.3924999237060547,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.39139999389648494,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.4741998291015648,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2335999870300327,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.3015499496460023,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.4161829464009585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6630694989240515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.646413961372552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9087958458653187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.8944239336202067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.22536753254000885,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.15642929077148438,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.102857862200056,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.037776440448880066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.15058936000006407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.8187122010959853,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.30522876829772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5038229744881983,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.223921513280316,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.75,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7228065279028861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9213024509069911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9372621951559523,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7765456455189668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2200033028610937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.418176872394763,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5402863011279244,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.17200319805132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5066072396280097,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7402849725160254,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7570478569581263,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.22215903900625333,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7748265990481951,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.8365599925882954,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.08124604150694381,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.405791800284722,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.17610015869139772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7793960571289062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0006393432617244343,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.01662979125975994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.018625144958491546,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.07938056945801009,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.0368656833167789,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.05918710214292133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7963256388851203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9134389070953985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7467435562800606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9925798971822553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.013571058000837022,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.0007138933454241547,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.02437643276610746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.01013067039656479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7727797574927475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.404482346096081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3790898259580279,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.08379547602767257,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.060001373291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5852303602646769,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.27525440319753347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2771579678758407,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.1709077278027835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.278968465613727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06558098790776512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.17636327589818368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0063777457986154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.36903107198980045,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.09423692480656776,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09694362967801462,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.725294334315497,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8337917618008284,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5160358918987029,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.282676983722797,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.240166348032017,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.014499950408936257,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07599983215332173,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.018400001525879617,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.08639995574950987,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.00889999389648466,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.04404998779297031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.25721795475988074,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.22071276390507322,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2760572342315415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.18284320903108053,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.24827753243403805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3378204874585178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.001785687037876682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.014642851693289619,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.006945035858395676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.05254202633574212,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20597794376812084,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.4806021067003452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2225456763663534,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.3838247028212352,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01000213623046875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6099929809570312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5310260631011254,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.20812756830393964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20980382279178755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5710715571263236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.18272588514116617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.9347804863367957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3108457939401288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.13919205042709493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.314826774826249,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.027110089912973923,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.02958948459396149,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.125458163639037,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3720974110459352,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.3531636065303276,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.1481944656808518,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.372980652660496,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.036099624633791905,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.019900131225583095,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.02312362670899404,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.15569946289062386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0003346633911007757,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.003273506164561013,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06012256637484281,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7654082827807329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.01674225135654961,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9807048800766882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.013269054412479164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7872787699688133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.00964300973074772,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.008929116385323621,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.012475861499416985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.00856828609898086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01263976046352866,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7708518446529977,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2612601612449297,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6085964307836196,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.23000335693359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8600006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4897061231237676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2108308349528576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2130574258700335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.29750859408572694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.004176126211508091,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.515020337803675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8208387221606883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.45448568599925077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.27350683484889116,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.02981335656189188,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03284308767220745,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8518952005984404,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5506471699755933,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.933403457997207,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6382015374602923,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.688274288232652,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.11645011901855185,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.46529121398926065,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.017494659423832104,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.10648162841796704,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.013061370849612786,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.06378047943114495,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3380664169484904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3802129170374702,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20461904396584796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9302389527107047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20509129741674847,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8709803535386418,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0033427647181919484,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.0016577584402901469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.004484931832540395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.006442690200782031,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.21706712717886045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.811664548027391,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.27750146192072145,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.11360058735435252,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6100006103515625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.22999954223632812,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.249087770193003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15777144281159394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1657167685676697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.5051568550586434,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -5.738559095001494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.393052533460009,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7757969983162694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 26.221894680651793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.4652870584678794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.33878892120255966,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.34593110676549577,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.059543461571357,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -6.2933823911885955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.9746694132664775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.23057101187797802,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 31.88970444208541,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.028499984741209516,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6155000209808357,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.04039999008178796,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.330000019073486,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0007999992370599784,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06755001068115263,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.818994984009816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.4240224152592305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.069806230787166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7443268991288221,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.349691407571554,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9212408439381417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.012857300894601131,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3564286231994631,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4881241652843027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.972611095952308,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.0515288511053438,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.856573079511273,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.35000038146972656,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.06711717024477926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.36665031339556675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.38329843934019614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.043487361842523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.5542121447379236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2588033710934532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.001353668696128,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.119707590665124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2833164585196557,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.18563283500460104,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20308410114237008,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.5978739683552363,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.109035440925025,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6771864912869852,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.5423134090751476,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 9.353496192898525,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.042499923706053266,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.41399993896484233,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0010000228881850148,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.10839996337890412,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.00494999885559011,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.04045001029968276,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.0968771644958695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.41799160751627706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.8836180775956501,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.104244099616426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.7304866119877147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.2586156870598497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.009285654340471572,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.20142854963030143,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.05597191837436455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.921555651971075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.7073189339986587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.6863299633249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.839996337890625,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.05999755859375,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9036143047551293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.17943059966694097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.18872947660859563,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0728561636874643,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.8889465884981878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2526767924380788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -5.15010436366674,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 8.384161324693729,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6874150164802528,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0015868787240247428,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.008515138410769563,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.6272427702001777,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.443769884685289,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6710599126316108,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.6910641040457595,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 12.617949926927128,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3564998626709013,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.3255001068115178,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.07479995727538835,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2587998962402338,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.017400016784662853,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.31544998168945426,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.414297149080081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.483959227179854,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.209220465112473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8066295644498345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.891802386233666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.778280599643422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3214285714285712,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.1949986049107153,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.04389404815236375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.050780735620819,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.5839288902413937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.8742584750762958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.3201065063476562,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.390106201171875,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8350553517511017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.2713478214825162,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.317039940276222,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.700668608626832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -7.42464400327003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -33.427260854014406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4047936107603327,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.776049824499619,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0512546400259781,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.452365299873482,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.497254278474048,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.2550552151395453,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -7.956894211016241,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -34.52599432903284,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6950092477389553,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.101414424864782,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6025051116943416,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.015494918823236503,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3783979797363344,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.8061979675293003,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.16499948501586914,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8979494667053274,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.6771725491386835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.367764383560699,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.1789862125269925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.032429411852335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.572772275955096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.263731664005064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.010371071951730038,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.01108551025390625,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1693234908074075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06529219980113687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.9226290061121887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.223685052679425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.55999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.589996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.0727833657538386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.7154018468227634,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.6479464932842376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.2716236085627237,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.612339332704205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.1224949148276675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.849643940721492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -11.05866700082414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.8565840774789621,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.5343843684317977,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.4677321550864115,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.7172370020500103,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.1671626288913064,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.7041117946341355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.3906036811005116,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.824878398590739,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6500000000000057,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.080500030517584,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0822879028320358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9111785888671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1543588256835733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7173698425292798,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8619023224569755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5979489160696025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.116790882698382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.559787042620143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3369029482861672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.6174867768162153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.14999934605189758,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1592864990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03582674468070923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15516539142034347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.07005412966641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.7545545003253684,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.07664579505762958,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06284935939116898,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.32000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.94000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.17821748964430562,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.26328795433689933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.262487644381626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.22535664063340066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8643427712271778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.9334755723634087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.2080548372151778,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -27.790778694518025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.39441677791918206,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.08227047594593362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.08227330618379991,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.32902996587931277,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.4191660674142792,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.5150924521698768,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2509854224058028,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -23.55699009228462,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.9054992675780795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.7675018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0056994628906182,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.9687457275390443,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2841912841797125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2954414367675895,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2320295454766974,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2792200032198275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2675187758794051,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.1953785522684557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1527668591965856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.8086469878965339,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4487871442522309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5037841796875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0832604335321927,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.08724800266042787,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0588844083228901,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.3569790041088816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2845703091257812,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6037569660170721,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.5,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -7.769989013671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.017212722443106,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.69165341947518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6672160992056142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.224211722098816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4192825269820455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.067899606436497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.660754622974226,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -21.874759390720477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8010134341682296,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8726708978661457,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8474304374034403,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.669825115586102,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9741058231691468,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.649516486242965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.119794882595208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -17.640970788487074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2725006103515568,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.707501220703108,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0970001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2129998779296614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.04065002441407728,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1627001190185524,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4818032127621441,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.33089306779647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6256770775717402,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.559000040151427,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5989571211845623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.2647012042100743,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1971435546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.20142582484653992,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09341946533147905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15436419353352004,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.528131842131641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.735719074088782,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01843401108063647,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07982771062364569,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.310028076171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -9.8699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.15126554116031699,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.9666372849164513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.840974170209743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7566040288923048,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.389033314953358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.668449155199239,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2005038733054132,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -14.29443329445984,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.36746482943519343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.147654763307417,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.021188508407569,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.3109906354050178,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.16578998123374333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.250066035005707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.6595441329263956,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -10.060644692226438,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9594985961914517,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.3665008544921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.38177795410155113,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.3238519287108943,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03162887573239459,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.061703033447258804,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.533995596632387,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.37295588256503,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.3671159839125266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.2278572045782425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2731204368275577,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.87770043166814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3203560965401788,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.055352347237723976,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1332615790731193,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0565610410684223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.1420093950894383,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.61520968172586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0302318156350512,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0123365538003068,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -7.70001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -85.030029296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.40301216739951906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.712571667336904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5227087349557689,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.7641944060237496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5136828116641414,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -9.279685062527289,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8993274656031947,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -13.37933112868146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6192114556743955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5315541889459383,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3424943967579424,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.209807799511036,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.04114048452295904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -9.861301942333755,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.559712794017786,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -9.145542526448057,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -5.6345001220702216,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -27.706500244140557,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.3849743652343705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.613365478515561,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.13915802001952216,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4367187499999545,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3933433950056191,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -8.340963973260074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3483159946383605,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -13.639647286310218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.198066551655641,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -13.392764660151347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.15356881277901735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.9949951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.07655596636582196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9379254022544856,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.990240607659242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -10.93507199940974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9832850170836755,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.19751006293475393,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.3600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.1100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6171010378987596,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.818077432997594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 7.533530776396469,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 9.43320152149687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.057673073038437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.2423018305472446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.10345823696623668,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -22.292607043207845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.40090174962388314,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.9990949113885605,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 7.713745114594294,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 9.987588128009584,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.5028497768513347,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.6606849507407766,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.5624984965872208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -18.05881844097444,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.1595001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -7.365749931335458,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5847999572753935,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.598500137329097,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.12999999999999545,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5687750053405694,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 7.379270893375512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 10.925172709858632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 5.929580910273437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.737484925024862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.848878275225108,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.7179976773192713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1678573063441684,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.09607124328613281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.0110605345461643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.18468084323445488,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.047155364792758,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.9586007097397484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.09987657095981994,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5457426744094576,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 54.469970703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 69.55999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.0917619323554746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.9006762507339587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.9650991938962044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.663575398328348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 5.112368671167733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.07369072970665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.8216930709795243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2065369219133686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.307961220630351,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.0816937291249245,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.145313532094031,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 8.217962004841063,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.5575453749806325,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.4920738499001835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.36265281135854366,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.0272516803200338,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.085620117187432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -39.8204284667969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8523596191406568,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.6961413574218795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.188067932128888,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 14.250070495605428,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 6.028999673040347,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 10.912355848773249,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 5.47326924820316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.539051857541835,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 6.810261729871179,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.970310266235913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3463456409224577,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9210260345134884,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.249360433349751,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.27130457081567005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.9643740980044875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.339673873136988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2631363204800935,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.322789561096684,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.5999984741210938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.959999084472656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.5945436751448447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.108287924116394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.221942808201829,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 12.044028264803764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 7.234223389581695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 10.243610559712936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20976793622454748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.312581165263274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.810742963419721,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.28930540250736,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 4.402157146399656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 12.598414871316479,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 6.6794000933945945,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 9.66199367990647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2492723233964331,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.07879256302987248,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3120000839233441,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.9135000228881864,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.019599990844731963,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7765998840332031,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 7.324068333233391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 14.129421765062556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 6.434039835192307,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 10.012719808939686,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.003571374075753475,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.24642862592424652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.34777677012962105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.0011455966471869417,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 5.65859562175639,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 7.796289166529412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.006451490664340476,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.4289106511781632,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 34.3800048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 30.790008544921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 12.08963370277727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 12.264583156087806,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 12.057042218624513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 19.30621545862351,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 16.693843371580783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 15.399336138403596,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 10.718429820215801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 11.301556933551081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 12.305832991052148,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 12.445600634478772,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 12.23725655682234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 19.860602065136224,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 16.139020075393685,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 14.81771925859713,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 12.17747007983678,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 15.535345535784483,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.08150024414061363,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -9.553999328613287,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5906640624999966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -7.8539685058593705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.36513595581055824,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0044550323486305,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 15.17343960897487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 17.423424910120723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 14.324708507076245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 15.365091755467043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 12.639872417391494,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 11.119924792894832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.7432141985212048,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.413211277553014,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.07341102801402943,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3369817670235751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 11.703115324247214,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 10.481063689898463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.8284738648332983,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0563251126406312,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.5099945068359375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.4600067138671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.90450002806024,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.8748218795324725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.879229917583424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.29725691912136,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.14926815579952013,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0545469917434214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.242408620197358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -8.01496804552797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6883007397853635,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6938044011415068,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6990155793855979,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.8516435256340733,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4055551403875812,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.47293011193695333,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.783368360576377,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.781179443294569,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.23750000000001137,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.1690002441406193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.11192749023439319,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.24195587158200738,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2236876296996968,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0232248306274414,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.9066316409863329,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.3722976541304397,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7375031110067987,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.424499995885764,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7454312241920622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7761325656183029,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1957146780831467,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.35357012067522353,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.12057537116628447,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15921997009774236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7475220330870886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2178251058748373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.013599324402500335,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.27235264540059045,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.23999786376953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.2899932861328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.405269471979876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07231276378067975,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.07236580525624703,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.35822578086628365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.46233214453113014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.017491019497486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.9510431888628759,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.4349280477057071,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.6214687602547526,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.25333024217164546,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2525801434540731,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.19616082564642978,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09249115165597033,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4358741396910197,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.4100834484838565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.798860554527696,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3474998474121094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.6709999084472713,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.10292549133301065,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6954658508300824,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.11505271911620696,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5867305946350072,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.17835938420580622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.2088826495752834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.20304900834380302,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7012535409883336,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1799681630005665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7034820744788348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09357125418526802,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.05928530011858246,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1443775194820196,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07827772258852828,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3446264587492309,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5915667726282612,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.10157920744935578,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07024090738731226,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.25,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.09000015258789062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6972969044548916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.12691226165133518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1265499143606741,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.627368693090615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.6500315620627148,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.3620835659076134,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4107959790969673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.31628220338975055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.913496192729768,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.054105216739630535,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.053664423837151976,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.0729820865779014,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0952082658756135,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7804666861011453,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0482442805240133,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.917506398843651,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.13649997711181783,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.48050041198730753,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.030120315551762644,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.16316200256348168,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.007540550231937004,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.025102100372315306,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.20177151019775685,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7341716204968707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5012938706121406,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.45307502356939366,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.45359477703923456,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.11921796998348722,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.028571265084402997,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0049999782017298156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.05659520127231121,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.006960185647980177,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4284234818638484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1542327149599343,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03175853557728636,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.030516136079096756,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.57000732421875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1800079345703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.23553115869960894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.565820748233592,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5645096570942698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6533492901606097,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.6197357403359702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.956632936819236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.2912285791249598,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.8430092012872157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0193318704247325,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.38480326984262625,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.38429531889644375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.09896268364789629,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0649124441488689,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.3750160570127679,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.16781168049601902,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.390779400946185,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.07550048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.47149963378905113,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2917590332031068,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.8172476196289153,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.03305816650390625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.174210357666027,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2941443128187671,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3869817590559932,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5007168708965448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.1406530226807043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3117506882193255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.0057237082599304046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.006070818219866325,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.03535679408482162,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.00862391360016801,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.0225849988001372,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.30643895879660477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.09677321974845654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2773127578639877,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.13177623722026266,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.540008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.779998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.35715977738415283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7907586649201326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7918192123367973,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.4268248835618733,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.760085274775669,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7023102842395268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4301565463302506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.901562447361461,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5733590656590293,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9717761433110983,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.9720335505346234,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.8724382770491599,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2052619785885677,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.12069340443305876,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.889196805951233,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 8.135351049594863,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5650001525878849,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.3890007019043082,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.21274230957030227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.219924621582038,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.12133682250976108,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5894109344482388,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.025400059798719177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9852415860367669,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.18510588104212466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2926183122924808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.25528019180238637,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06819069804435607,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.041071210588727425,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.04321398053850434,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.017831685156761923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.01678791793933554,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2978535774032509,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.3821037613035094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.12175830216999495,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.013162231378747835,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.31000518798828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2700042724609375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5651558629524711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3736295385946109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.37380110929265964,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5300404309093185,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2666695095783886,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0643880475400556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.983075671020095,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.6754233338628577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7813551512273476,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5546470169855766,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5540154474904857,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9756538243966051,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7118462133912873,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4827711677335875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.47596458860088564,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.909211936096259,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3119998931884851,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.585500335693368,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.03638320922850369,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.31125473022460426,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.040877838134761646,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.278243904113765,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7401519766351727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.2569095786124205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.41266111618669665,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.7039075725243871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.42243382126223583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6722605988846331,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0824999128069197,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.18749945504324783,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.08922948141095088,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.21998016022891664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3444884935518977,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.7710466770197173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.03563548776922931,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.0982605267427169,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.1999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.1454166474085925,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.12990984250473847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.12981988296711933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.7874612494554594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.191017247382419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.5525863278866403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.16786350716120335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.225400291675697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9292173591337161,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.05110763588622724,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.050394455230706736,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.233074642942746,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.36380604880468237,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9709694480801723,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2911767524597773,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9916116894422955,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.32450027465820597,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.264000320434576,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01548568725586108,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.26417129516602245,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.04210346221923089,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.18438774108886946,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.40118508402284814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.3362723616092476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0920530792355656,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06094098934328329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06754108467164066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.013382091052149825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.12285723005022331,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0014831393229550738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.10881252586284118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.10033322137706913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.1672262884777842,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.08033559316957328,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.015983744974698566,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.44000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.8300018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1648076384225705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6823848126455978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6486319110904697,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.680725590243916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.022174347455039545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.8665557348870117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9771674746105292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -7.329396603129235,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.05139164985230593,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8634022910365635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8288462492882953,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.1263389837312032,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5326489487320609,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.448172614693479,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4818727850104505,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.095608000895833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3915000915527287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.8534999847412053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1395416259765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6348011779785168,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06674057006836165,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2927703857421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06449273803534794,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.670263930378636,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.27928348911292566,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.695218282877168,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.33652643775664615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.930835340008377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.03142820085798004,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.18785694667271202,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.037656926322546136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.2645219807961552,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3834443933823479,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -5.080611617476849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1508239773579687,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.22989244308506396,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3599967956542969,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.4900016784667969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5451836737667701,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.1266629687644247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.1494644402953336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.49553266899828863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.17405304714406267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0728963685838986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.27064263559595236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.090085521846953,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3289843854918937,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.945645490373459,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9692501020975075,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.049919275511002,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.728876343331164,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4912794887774306,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.1883976240250282,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 8.323874124080355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.15250015258789062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8025001525878892,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.024173736572265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.10922653198242216,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0039029693603538362,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.028958969116210653,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.2445441325691808,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.8083642941615121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8048754453747531,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4407272273291305,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.830784786839267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0554683073600972,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.013214111328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.07035664149693077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01891102712991355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.18407858920992726,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.16385593607749493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.0893031660764745,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.08719304678246326,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5685281736136714,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.30999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06999969482421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.11068568702424786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.02463515923550874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.024857729196070544,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2073960468854672,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.32130149652893625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.456343411951867,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6710849358788735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.870573460142178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3268849752991243,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.20565263762647445,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2050720673938966,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6530094403727538,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2335217996581651,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.8747265321453987,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7879553237421071,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 6.104362062375579,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.06100006103515199,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.28249988555908345,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.042549438476562784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2001486206054679,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.012327785491940801,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.07410665512085046,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8921843648923122,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5197386819570937,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6287126452458547,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.626900216614279,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7539466706951936,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.00714394176771771,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0016427721296038422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.011499949863978842,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.01491740409640041,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.024824835648400878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6891686191160318,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.476593256652925,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1994550261847693,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.23610639471756933,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5400009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6240052224844472,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.021175266169093376,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.021365067476741828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.26970475112247,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0304566868579723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.420287213900087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.7869231891051385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.6872991312959829,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4078059342095708,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15984221222187234,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.15884927072108423,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.7153181446097565,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.47563339067087096,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.838670334093619,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.32788292948415787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.921087733529384,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.15799999237060547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5635000228881779,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.006343994140621589,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.044646530151368324,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.01977609634399613,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.11291807174682589,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.16525891859811015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.08221097614851125,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.14454712345206566,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.149766524252982,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.11797300159495094,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8393890767268264,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0032144274030413422,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.04321452549525662,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.004276670547986194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.09735807288829856,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.14974846513535756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.010780718464177,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.16493448110521114,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.18089163034879574,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 9.69000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 10.969970703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.283943365912621,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.15590815851524997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.15626662355976428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.394195501210606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.2741048258112073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.64765203217293,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.6918458612378746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -6.513619819599303,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.0677440776377445,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.02510931987571574,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.02394771463806178,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.9485821077233196,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7192815296241051,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.06603515236646018,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.232805601616894,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.279831217365902,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.0665008544921193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -15.258505249023415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.04200073242191138,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.155802001953134,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8850498962401616,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.931599731445317,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.019922119503903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.373793900749812,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.6970362620885027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.6117159566244497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.6863549271600933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2958339069076388,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8350001743861597,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.77642822265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2064980540888408,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.25459112073897705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.5286326026510366,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7305521818310368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.20517498351563257,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.2723920175284974,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1300048828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.0900039672851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.23381640551736194,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.6512066359943178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.696120899406628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7527013726622798,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.1350044384591085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.433498244569534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -5.024610771867799,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -8.850447792808126,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01761711724248549,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.4701891576033521,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5159065612088019,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.307087979174993,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.6898277346462098,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.8518813647630656,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.5655705122468184,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.6166591905747225,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.27150001525878054,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2049995422363224,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.19900009155273324,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7399999999999949,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.03289875030517919,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.142692947387701,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.13507870384315002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7162341222966448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.07354984970386891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.181776231379895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.09672075735780439,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.1139536703233226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.02785709926060287,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.01714270455496658,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.027870650680834608,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.08775979760026864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.11538553734381507,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.7425259763045218,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1327829516944401,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.12275945388689435,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.3499908447265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.54746475049612,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6948619746799611,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6983184441524015,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.08187358122999644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2363118523486918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.7700536626551475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.771503111444673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -3.109230507354855,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 2.7636640387709965,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.8758794530709268,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8785327823502276,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6362601877427099,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.791135148535794,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.1884367828486795,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 3.2305433710656537,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.124558094878548,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.051999664306635,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.007498931884754,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3151220703124977,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0092370605468943,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.37231124877928323,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.894946823120108,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3698439361225381,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.9880048523221339,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.015233706947581638,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.40285249270619605,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.048573943074824655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5383739539230845,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.19928523472377258,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3657172066824774,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1041111489847859,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.16690004852640117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1757300640822912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5130326376568526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3197586246592803,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.004956749234551694,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.230010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 15.52001953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5515979241518485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.2015252725914314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.287051319083133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0088871018431478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.597887385436203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 8.647391047235143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.6752871456560356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.663932146832603,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.335398635876972,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.0205077942004657,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.1068369808853067,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.5632737083558617,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.043064089249101656,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 8.065774167428675,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.216246886035055,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.5698564554007985,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.5365005493163721,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.9214981079101676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.22779968261716022,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.9499999999999886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.47875000000004775,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.1628498840332213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.3571534851160907,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.2224351027354325,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.1150503094336619,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.339766425906689,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06651787119889008,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.367850496924518,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.2721426827566962,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.7249973842075885,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.06497117682963971,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3269333119382738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.05268472980953831,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.5549086097837037,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8622746121130203,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6574633918325057,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.5200042724609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.95001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.1908356973465484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9117094005290372,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.9136144604884322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.1886687839587342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.7418753165458156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.070791034924404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.9225676891876162,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.1235618617630792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.4070349856214248,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0927268789200029,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0938287986862583,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7430553904714476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.1870520203587143,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.4891741551179356,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.5364725704333644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.110226740470324,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.028000640869123572,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.2239990234375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8825604248046943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.572070007324214,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.14108657836914062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6142459106445415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7235696756404897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.534616715906223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 1.0934939758308615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.8818019649840205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.7197185038114071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.0928164928120765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0499997820172986,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.3664289202008928,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.03847366535974883,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15976864058896978,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.6009660703780959,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7709788679419631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.24859409627308482,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4961433786767595,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.04000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.25,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.35045398987902,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.692202375348184,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.7082658859983724,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7364317927737174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.06481869962094988,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.0408537570159373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -4.854751063182217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -7.163494976543094,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.1342547016041435,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5111848969572184,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5280515478005463,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2908183992864308,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6196419958080508,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.4592368772094693,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.3957108035612356,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -2.929706374309693,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.05500001907348917,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.5037500381469755,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0636000061035169,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.43599998474121193,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.01645000457764212,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.06775001525879532,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.045821350504215985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.358666856575886,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.06717472816847314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.0776282428916715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.07505563193619391,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9639951360140069,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.027314186096191406,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.009828567504882812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.08549274937638751,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.012773536434038668,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.1147473173464757,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.7171543190557674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.41970759133795355,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.10431381678064788,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.470001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4899978637695312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.4413186227915089,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.6475629771919178,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6655355457712453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.9248461010287201,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0930920577201455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.5040295249561426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5564166053550377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.6774914659616549,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.22511933451663246,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.4665454988009521,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.48532120757341923,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.3704594945160067,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6479153539072469,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.9224126451496746,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.09737634573405707,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 4.911280068195056,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.13349990844726278,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.49899978637695597,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.0860955810546784,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.45633239746094034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.03286891937256087,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.15918556213378565,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8633464634740129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.4002852801141996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.5330542812991945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.692554659879398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.7171214581621621,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.8920702849242632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.0049999782017298156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.004284994942801212,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.01803079211270675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.030234615809831444,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.6065419174971503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.9228591789727911,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.008430196432393733,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -0.18227548929346016,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.8499908447265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.67999267578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.44621869759466914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.5184716902189033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.5624866984961905,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.817475741532082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2782955564650358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.616622055585374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -3.561727369653834,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -8.528656957035817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.2300194093197927,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -1.3374542118279376,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -1.3822723602983644,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.3718623480447953,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.8331188526521371,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 5.035005175778906,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -2.1026871100328535,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": -4.294868354802414,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.415999603271473,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 1.2260002136230526,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.21880004882811477,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.4978002929687477,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.20970001220703693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.9789000701904342,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.252601502720462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 2.6510744283569143,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.3776479278923217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.1425426037286375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4300411280329328,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.285563306913673,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.011785234723771687,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.2925022670200894,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.020714945683802277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.08036431989274151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.4860145506849767,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 3.2477515556086356,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": -0.25285214408966095,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.5196045283079402,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.020000000000000462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.11999999999999966,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1499999999999999,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.020000000000000018,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.010000000000000009,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.009999999999999787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1299999999999999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.020000000000000018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1299999999999999,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 8,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-27",
        "to": "2026-10-28",
        "change": 0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-21",
        "to": "2026-10-28",
        "change": 0.009999999999999787,
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
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.870000000000001,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.21000000000000085,
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
    "id": "afterhours.VIX.value",
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
| 推断与解释 | 推断：恐慌缓和后的修复，财报风险重新上升；既无全面恐慌也无全面过热证据。 |
| 反证与缺口 | 收盘VIX不能解释盘后，信用滞后，Fed两票主张加息 |
| 确认条件 | 信用不扩张、油价与利率稳定且次日波动率不突升 |
| 失效条件 | 股票再跌同时VIX期限倒挂/信用走阔、油价冲击加剧 |
| 观察期限 | 下一交易日及未来1–3日 |
| 条件式指导 | 等待多市场共振；不因单个VIX低值扩大方向风险 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增28日完整收盘与Fed决定、云公司盘后财报；收盘突破部分达标，但盘后回吐使可靠性下调。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 收盘突破部分有效，盘后失守重要收复位；反弹可靠性下降。 |
| 反证与缺口 | 等权未跟、量能不足；盘后流动性低 |
| 确认条件 | 29日常规开盘首30–60分钟，QQQ先收复721.25/722.87，再站回725.10–725.61；SMH先守557.98–559.81再收复567.67。回踩低点抬高、可得常规VWAP守住、RSP/金融跟随；收盘仍守住才升级确认。 |
| 失效条件 | QQQ不能收复721.25、SMH跌回557.98且反抽失败，维持脆弱；进一步QQQ失守713.59、SMH546.67是旧结构更强失效。SPY失守766.83附近50日线且无法收复亦降级；不要等最远失效点才控制风险。 |
| 观察期限 | 下一交易日及未来1–3日 |
| 条件式指导 | 等待29日回踩与收盘确认，盘后仅作预警 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增28日完整收盘与Fed决定、云公司盘后财报；收盘突破部分达标，但盘后回吐使可靠性下调。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.IGV.return_5d_pct", "prices.SMH.relative_spy_5d_pp", "prices.XLE.return_1d_pct", "prices.OIH.volume_vs_previous20_ratio"] |
| 推断与解释 | 存储/电力散热有业绩支持；软件云盘后冲击，优先比较抗跌而非追涨。 |
| 反证与缺口 | 19ETF价格轮动非资金流，现金流披露与市场预期可能分化 |
| 确认条件 | 行业相对QQQ强，回踩后高低点抬升，金融等权扩散 |
| 失效条件 | 好财报仍持续弱于指数、资金现金回报恶化 |
| 观察期限 | 下一交易日及未来1–3日 |
| 条件式指导 | 将强业绩与强承接同时作为观察条件 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增28日完整收盘与Fed决定、云公司盘后财报；收盘突破部分达标，但盘后回吐使可靠性下调。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 需求仍强与现金投入压力可以共存；微软/Alphabet新财报需要新估值底稿。 |
| 反证与缺口 | H100租金上涨、两家云收入增长强，不能认定AI需求崩塌 |
| 确认条件 | 现金回收改善、融资压力不增且价格重新获得承接 |
| 失效条件 | 投入加速而现金回收放缓、稀释/信用压力同步上升 |
| 观察期限 | 下一交易日及未来1–3日 |
| 条件式指导 | 拒绝把单季EPS或AI合约当完整估值；关键输入不足暂不反推 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增28日完整收盘与Fed决定、云公司盘后财报；收盘突破部分达标，但盘后回吐使可靠性下调。 |

## AI云：需求增长与现金回报分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 微软FY27Q1收入922.79亿美元、Azure同比48%；Alphabet Q3收入1275.77亿美元、Cloud同比103%，营业利润405.76亿美元。Alphabet净利264.68亿、归普通股261.70亿，EPS2.12；不能把投资损益造成的EPS变化全部归于核心经营。 |
| 事实：市场反应 | MSFT544.72（较28日收盘+2.58%）；GOOGL292.73（较28日收盘-9.90%）；IGV107.56（较28日收盘-3.89%）。均为28日盘后不同分钟，见报价时间。 |
| 推断：解释 | 推断：市场在检验资本投入能否转化为现金，经营增长和股票回报不必同向。Alphabet Q3经营现金422.90亿美元低于现金资本支出513.55亿，单季公司口径现金FCF为−90.65亿；这不等于公司破产，也不是模型FCFF。 |
| 受益篮子 | ["现金回收更好且股价守住的云公司观察篮子"] |
| 受损篮子 | ["资本回报不足、融资稀释偏高者"] |
| 反证 | 微软现金CFO减现金capex仍为正；AlphabetCloud强劲且TPU设备销售有贡献，不能把收入全部看作经常性订阅。电话会完整指引未获一手正文。 |
| 下一催化剂 | Amazon29日财报与29日常规承接 |
| 证据 | ["https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm"] |

## 存储/电力设备：好财报后能否抗住云端冲击 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 28日常规MU涨5.87%、DRAM涨7.13%、VRT涨16.48%，VRT成交约前20日3.33倍；此前SK海力士/VRT披露支持需求。 |
| 事实：市场反应 | MU957.75（较28日收盘-2.59%）；DRAM52.55（较28日收盘-2.90%）；VRT236.66（较28日收盘-2.59%）；SNDK1361.96（较28日收盘-3.05%） |
| 推断：解释 | 推断：订单与需求证据仍强，但云客户现金消耗可影响供应链估值；以相对QQQ的抗跌和回踩为准。 |
| 受益篮子 | ["MU", "VRT", "SMH"] |
| 受损篮子 | ["缺现金回报或高预期未兑现者"] |
| 反证 | 半导体SMH仍低于50日线573.40；单家公司强不代表全板块。SNDK尚未公布下一季财报。 |
| 下一催化剂 | Sandisk29日16:30纽约电话会；29日常规开盘 |
| 证据 | ["https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29", "https://news.skhynix.com/en/q3-2026-business-results/", "https://www.prnewswire.com/news-releases/vertiv-reports-strong-third-quarter-2026-with-net-sales-growth-of-61-organic-orders-growth-over-100-and-diluted-eps-growth-of-91-adjusted-diluted-eps-growth-of-78-raises-full-year-2026-guidance-across-all-key-metrics-302921936.html"] |

## 政策：按兵不动仍保留紧缩风险 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 28日Fed维持3.75%–4.00%，10–2；Cook与Hammack主张加25bp。声明称通胀仍高、活动稳健。 |
| 事实：市场反应 | 28日VIX16.91，但TLT跌0.78%、黄金GLD涨0.33%；盘后风险资产回落发生在财报之后。 |
| 推断：解释 | 推断：不加息不等于转鸽；成长股仍需要现金流和折现率共同配合，不能单一归因。 |
| 受益篮子 | ["能传导成本且现金稳健企业"] |
| 受损篮子 | ["久期长且融资依赖高者"] |
| 反证 | 信用利差最新至27日，不能证明28日Fed后信用立即改善；未获取记者会全文。 |
| 下一催化剂 | 29日08:30纽约GDP/PCE |
| 证据 | ["https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm", "https://www.bea.gov/news/schedule/full"] |

## 原油、航运与融资：风险尚未清零 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 本次延迟WTI/Brent约102/111美元；航运恢复与军事停火不同。管线风险、WTI触及门槛和12月加息合约仍需联合观察。 |
| 事实：市场反应 | XLE68.69（较28日收盘+0.35%）；XLE28日收68.45仍未明确收复旧68.62。 |
| 推断：解释 | 推断：油价上行可帮助部分油气现金流，同时提高全市场通胀折现压力；不自造战争综合指数。 |
| 受益篮子 | ["有实际产量与现金流的油气篮子"] |
| 受损篮子 | ["燃料成本敏感行业及高久期资产"] |
| 反证 | 外交信件/并购等tc消息未有一手确认；连续期货换月，不能把日线跳变全当需求崩塌。 |
| 下一催化剂 | 航运实流、官方供应公告及GDP/PCE |
| 证据 | ["https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm", "https://gamma-api.polymarket.com/events/1147445"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AMZN | 252.96 | -0.64 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| AVGO | 342.68 | -2.60 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| CEG | 257.00 | -0.42 | 2026-10-28T23:27:30+00:00 | 2026-10-28T23:27:30+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| DRAM | 52.55 | -2.90 | 2026-10-28T23:37:44+00:00 | 2026-10-28T23:37:44+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| GEV | 867.00 | -1.26 | 2026-10-28T23:08:00+00:00 | 2026-10-28T23:08:00+00:00 | 2026-10-28T23:38:23.897697+00:00 | stale |
| GLD | 371.18 | -0.62 | 2026-10-28T23:35:28+00:00 | 2026-10-28T23:35:28+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| GLW | 128.68 | -1.92 | 2026-10-28T23:38:17+00:00 | 2026-10-28T23:38:17+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| GOOGL | 292.73 | -9.90 | 2026-10-28T23:38:17+00:00 | 2026-10-28T23:38:17+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| IGV | 107.56 | -3.89 | 2026-10-28T23:25:27+00:00 | 2026-10-28T23:25:27+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| IWM | 282.00 | 0.25 | 2026-10-28T23:36:32+00:00 | 2026-10-28T23:36:32+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| META | 616.95 | 0.73 | 2026-10-28T23:38:09+00:00 | 2026-10-28T23:38:09+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| MSFT | 544.72 | 2.58 | 2026-10-28T23:38:09+00:00 | 2026-10-28T23:38:09+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| MU | 957.75 | -2.59 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| NOW | 123.94 | -17.44 | 2026-10-28T23:38:01+00:00 | 2026-10-28T23:38:01+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| NVDA | 213.91 | -0.68 | 2026-10-28T23:37:36+00:00 | 2026-10-28T23:37:36+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| NXPI | 248.70 | -1.19 | 2026-10-28T21:35:35+00:00 | 2026-10-28T21:35:35+00:00 | 2026-10-28T23:38:23.897697+00:00 | stale |
| ORCL | 140.78 | -2.60 | 2026-10-28T23:38:16+00:00 | 2026-10-28T23:38:16+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| QQQ | 716.81 | -1.21 | 2026-10-28T23:38:10+00:00 | 2026-10-28T23:38:10+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| RSP | 217.53 | 0.05 | 2026-10-28T22:51:00+00:00 | 2026-10-28T22:51:00+00:00 | 2026-10-28T23:38:23.897697+00:00 | stale |
| SMH | 558.37 | -1.64 | 2026-10-28T23:36:23+00:00 | 2026-10-28T23:36:23+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| SNDK | 1,361.96 | -3.05 | 2026-10-28T23:38:17+00:00 | 2026-10-28T23:38:17+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| SPY | 768.48 | -0.50 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:08+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| STX | 678.51 | -2.79 | 2026-10-28T23:38:16+00:00 | 2026-10-28T23:38:16+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| TLT | 81.20 | 0.26 | 2026-10-28T23:31:14+00:00 | 2026-10-28T23:31:14+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| VRT | 236.66 | -2.59 | 2026-10-28T23:36:53+00:00 | 2026-10-28T23:36:53+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| XLE | 68.69 | 0.35 | 2026-10-28T23:23:45+00:00 | 2026-10-28T23:23:45+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |
| XLF | 56.43 | 0.54 | 2026-10-28T23:25:38+00:00 | 2026-10-28T23:25:38+00:00 | 2026-10-28T23:38:23.897697+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 772.31 | USD_per_share | 2026-10-28 | 0.34 | -0.10 | 1.27 | ok |
| QQQ | 725.61 | USD_per_share | 2026-10-28 | 0.60 | 0.06 | -1.91 | ok |
| IWM | 281.29 | USD_per_share | 2026-10-28 | 0.40 | 1.74 | 1.22 | ok |
| RSP | 217.43 | USD_per_share | 2026-10-28 | -0.04 | 0.36 | 4.52 | ok |
| GLD | 373.51 | USD_per_share | 2026-10-28 | 0.33 | -1.44 | -1.92 | ok |
| GC=F | 4,065.30 | USD_per_troy_ounce | 2026-10-28 | -0.23 | -2.04 | -2.90 | ok |
| CL=F | 101.94 | USD_per_barrel | 2026-10-28 | 2.04 | 4.93 | 12.74 | ok |
| BZ=F | 110.59 | USD_per_barrel | 2026-10-28 | -2.89 | 1.63 | 6.82 | ok |
| TLT | 80.99 | USD_per_share | 2026-10-28 | -0.78 | 0.93 | 4.55 | ok |
| UUP | 29.06 | USD_per_share | 2026-10-28 | -0.21 | 0.48 | 1.01 | ok |
| HYG | 77.59 | USD_per_share | 2026-10-28 | -0.01 | 0.79 | 0.94 | ok |
| LQD | 104.07 | USD_per_share | 2026-10-28 | -0.22 | 0.83 | 2.29 | ok |
| ^VIX | 16.91 | index | 2026-10-28 | -3.48 | 1.38 | 3.49 | ok |
| ^VIX3M | 19.22 | index | 2026-10-28 | -1.79 | 2.67 | 4.63 | ok |
| ^VVIX | 96.61 | index | 2026-10-28 | -2.86 | 2.18 | 7.97 | ok |
| ^MOVE | 94.55 | index | 2026-10-28 | -3.39 | -1.45 | -11.30 | ok |
| NVDA | 215.38 | USD_per_share | 2026-10-28 | -1.17 | -2.97 | -5.69 | ok |
| MSFT | 531.01 | USD_per_share | 2026-10-28 | -0.06 | -0.36 | 3.53 | ok |
| AMZN | 254.60 | USD_per_share | 2026-10-28 | 0.59 | -2.96 | 2.19 | ok |
| GOOGL | 324.89 | USD_per_share | 2026-10-28 | 1.34 | -2.95 | -5.58 | ok |
| META | 612.49 | USD_per_share | 2026-10-28 | -1.24 | -12.19 | -15.54 | ok |
| CRWV | 63.93 | USD_per_share | 2026-10-28 | 7.32 | 3.41 | -26.62 | ok |
| MU | 983.23 | USD_per_share | 2026-10-28 | 5.86 | 7.61 | -7.67 | ok |
| DRAM | 54.12 | USD_per_share | 2026-10-28 | 7.13 | 10.09 | -10.34 | ok |
| VRT | 242.94 | USD_per_share | 2026-10-28 | 16.48 | 14.51 | 0.68 | ok |

## 跨资产风险解释

判断为恐慌缓和后的脆弱修复，既非全市场极端恐慌，也没有全面过热证据。28日同日Yahoo VIX16.91、VIX3M19.22、VVIX96.61、MOVE94.55，波动率指数期限关系正常；Cboe备用官方CSV仅到27日17.52，明确不是同日冲突。27日FRED2年4.70%、10年4.99%、实际10年2.64%、HY318bp/IG88bp；28日盈亏平衡通胀2.38%。23日STLFSI−0.5837；GPR26日165.25、7日181.42。黄金与国债并不同向，油价仍高：不合成未经验证避险指数。Fed持平但两票支持加息；CME概率矩阵未可得，Polymarket12月合约不是CME替代。CNN418缺失。盘后VIX没有新有效读数，不能用16.91证明盘后财报风险不大。美元代理见同源指标面板，不能用黄金上涨单独推断美元风险。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.70 | percent | 2026-10-27 | -0.22 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.18 | percentage_points | 2026-10-27 | 0.10 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.88 | percentage_points | 2026-10-27 | 0.04 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.99 | percent | 2026-10-27 | -0.25 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.64 | percent | 2026-10-27 | -0.26 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.38 | percent | 2026-10-28 | 0.03 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.58 | index | 2026-10-23 | 0.28 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 17.52 | index | 2026-10-27 | 1.48 | lagged | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLK | 科技 | 0.80 | 1.30 | -2.43 | 0.45 | 1.41 | -3.70 | 0.89 | 2026-10-28 |
| XLE | 能源 | 0.35 | 0.43 | 11.30 | 0.01 | 0.53 | 10.03 | 0.89 | 2026-10-28 |
| XLF | 金融 | 0.45 | 0.16 | 5.11 | 0.10 | 0.26 | 3.84 | 0.73 | 2026-10-28 |
| XLI | 工业 | 0.34 | 0.11 | 0.90 | -0.00 | 0.21 | -0.36 | 1.12 | 2026-10-28 |
| XLV | 医疗 | 0.30 | 0.44 | 6.71 | -0.04 | 0.54 | 5.44 | 1.02 | 2026-10-28 |
| XLP | 必需消费 | -0.36 | -0.31 | 7.74 | -0.70 | -0.21 | 6.47 | 0.95 | 2026-10-28 |
| XLY | 可选消费 | -0.10 | -0.17 | 5.96 | -0.45 | -0.07 | 4.69 | 0.90 | 2026-10-28 |
| XLC | 通信 | -0.42 | -5.35 | -7.06 | -0.77 | -5.25 | -8.33 | 1.25 | 2026-10-28 |
| XLU | 公用事业 | -0.84 | 1.17 | 7.73 | -1.18 | 1.27 | 6.46 | 0.57 | 2026-10-28 |
| XLRE | 房地产 | -0.73 | 0.17 | 2.98 | -1.07 | 0.27 | 1.71 | 1.10 | 2026-10-28 |
| XLB | 材料 | 0.15 | 1.05 | 6.49 | -0.19 | 1.15 | 5.22 | 0.86 | 2026-10-28 |
| SMH | 半导体 | 1.74 | 1.97 | -6.79 | 1.39 | 2.07 | -8.06 | 0.73 | 2026-10-28 |
| IGV | 软件 | 0.12 | 2.84 | 5.10 | -0.23 | 2.94 | 3.83 | 1.14 | 2026-10-28 |
| XOP | 油气开采 | 0.18 | 0.68 | 11.73 | -0.16 | 0.78 | 10.46 | 0.73 | 2026-10-28 |
| OIH | 油服 | 0.06 | 3.94 | 8.12 | -0.29 | 4.04 | 6.85 | 1.58 | 2026-10-28 |
| ITA | 航空与国防 | 0.74 | 0.95 | 0.27 | 0.39 | 1.05 | -1.00 | 0.77 | 2026-10-28 |
| ARKX | 航天主题 | -0.13 | 0.82 | -3.45 | -0.47 | 0.92 | -4.72 | 0.55 | 2026-10-28 |
| KRE | 区域银行 | -0.65 | 2.11 | 3.85 | -0.99 | 2.21 | 2.58 | 0.78 | 2026-10-28 |
| SKYY | 云计算 | 0.50 | 3.41 | 5.07 | 0.15 | 3.51 | 3.80 | 1.06 | 2026-10-28 |

## 资金证据分层

19ETF按28日完整收盘同端点比较：SMH单日+1.74%，5日相对SPY+2.07个百分点；IGV5日相对+2.94个百分点，但盘后下跌破坏短线强势。RSP当日−0.04%而SPY+0.34%，扩散不足；XLF+0.45%但相对成交仅0.74倍。优先观察存储/半导体、电力散热能否抗跌，软件云等财报后重建，金融工业用作扩散确认，能源须看供应和油价。发行人VanEck页面仅至27日：NAV557.91美元、资产710.5亿美元；无完整份额拆分桥，不能估当日净申购。ICI27日发布至21日周窗口：全ETF净发行458.21亿美元，国内股票278.23亿美元、债券95.67亿美元；这是滞后行业汇总，不是28日19ETF主力流向。未取得当期可核验机构持仓变化。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-28T23:41:32.481283+00:00：基础25主题及10组主动搜索覆盖政策、战争油价、AI融资、银行、科技存储、软件与航天参考。CPI/Meta/Anthropic及基础部分查询截断，非全市场覆盖。已发生Fed/微软从未来栏删除，补Amazon/Sandisk正式日期；未发现能直接代表当前算力信用风险的高质量合约。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.8, {"status": "comparable", "change_pp": -0.10000000000000009}] | {"spread": 0.01200000000000001, "volume24h_usd": 720.916742, "liquidity_usd": 30565.81086, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-10-28T23:34:29.412913+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["报价7.8%，24h成交约721美元，价差1.2个百分点。低量/宽价差降低可信度；非股价上涨概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [37.5, {"status": "comparable", "change_pp": -2.0000000000000018}] | {"spread": 0.030000000000000027, "volume24h_usd": 29107.621668999996, "liquidity_usd": 26539.0084, "quality_flags": [], "retrieved_at": "2026-10-28T23:34:29.412913+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["报价37.5%，24h成交约29108美元，价差3个百分点。低量/宽价差降低可信度；非股价上涨概率。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [13.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.010000000000000009, "volume24h_usd": 11586.412368, "liquidity_usd": 22316.3532, "quality_flags": [], "retrieved_at": "2026-10-28T23:34:17.113935+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["报价13.5%，24h成交约11586美元，价差1个百分点。低量/宽价差降低可信度；非股价上涨概率。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [96.55, {"status": "comparable", "change_pp": 1.0500000000000065}] | {"spread": 0.0030000000000000027, "volume24h_usd": 239902.316242, "liquidity_usd": 157648.59451, "quality_flags": [], "retrieved_at": "2026-10-28T23:34:29.412913+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["报价96.55%，24h成交约239902美元，价差0.3个百分点。低量/宽价差降低可信度；非股价上涨概率。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 44597.364864, "liquidity_usd": 330010.7249, "quality_flags": [], "retrieved_at": "2026-10-28T23:34:29.412913+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["报价11.5%，24h成交约44597美元，价差1个百分点。低量/宽价差降低可信度；非股价上涨概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [94.65, {"status": "comparable", "change_pp": -0.6000000000000005}] | {"spread": 0.0030000000000000027, "volume24h_usd": 12761.264357999997, "liquidity_usd": 46448.97491, "quality_flags": [], "retrieved_at": "2026-10-28T23:34:19.715644+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["报价94.65%，24h成交约12761美元，价差0.3个百分点。低量/宽价差降低可信度；非股价上涨概率。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will Amazon (AMZN) beat quarterly earnings?", "下一季度首次披露GAAP EPS严格大于固定2.00美元，四舍五入到美分；优先稀释股数，官方优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报为No。后续重述除明显即时错误不计。阈值是建约时预估，不是当前一致预期，更非股价上涨胜率。", "https://polymarket.com/event/amzn-quarterly-earnings-gaap-eps-10-29-2026-2pt00"] | [64.5, {"status": "no_baseline"}] | {"spread": 0.050000000000000044, "volume24h_usd": 1457.416457, "liquidity_usd": 565.7137, "quality_flags": ["liquidity_under_10000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-28T23:34:17.087893+00:00", "contract_end_at": "2026-10-29T21:00:00+00:00"} | ["报价64.5%，24h成交约1457美元，价差5个百分点。低量/宽价差降低可信度；非股价上涨概率。", "电话会时间，不是必然发布分钟；EPS固定门槛不同于最新一致预期和股价方向"] | ["官方业绩按专门EPS定义核验，同时看现金流、指引与股价承接", "EPS过线但股价失守或现金回报恶化，不能据合约直接买入"] | ["2026-10-29T17:00:00-04:00", "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report"] |
| ["Will SanDisk (SNDK) beat quarterly earnings?", "下一季度首次披露主要non-GAAP EPS严格大于固定47.15美元，四舍五入到美分；官方优先，其次SeekingAlpha；96小时仍无non-GAAP才转GAAP，同样无数据或预期日后45天未发布为No。优先稀释EPS，后续重述除明显即时错误不计；不代表股价涨幅或正确估值。", "https://polymarket.com/event/sndk-quarterly-earnings-nongaap-eps-10-29-2026-47pt15"] | [86.0, {"status": "no_baseline"}] | {"spread": 0.09999999999999998, "volume24h_usd": 2322.525789, "liquidity_usd": 338.4914, "quality_flags": ["liquidity_under_10000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-28T23:34:17.111141+00:00", "contract_end_at": "2026-10-29T21:00:00+00:00"} | ["报价86%，24h成交约2323美元，价差10个百分点。低量/宽价差降低可信度；非股价上涨概率。", "电话会时间，不是必然发布分钟；EPS固定门槛不同于最新一致预期和股价方向"] | ["官方业绩按专门EPS定义核验，同时看现金流、指引与股价承接", "EPS过线但股价失守或现金回报恶化，不能据合约直接买入"] | ["2026-10-29T16:30:00-04:00", "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29"] |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 79.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.5, 0.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.500000000000002} |
| 24h成交量 / 流动性 USD | [362681.145775, 566090.925] |
| 价差 pp | 2.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 96.55 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.05, 28.05] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0500000000000065} |
| 24h成交量 / 流动性 USD | [239902.316242, 157648.59451] |
| 价差 pp | 0.30 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.35 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.1, -0.45] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.05} |
| 24h成交量 / 流动性 USD | [112039.736452, 205068.70662] |
| 价差 pp | 0.10 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [44597.364864, 330010.7249] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:28:43.955727Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 37.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [9.0, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -2.0000000000000018} |
| 24h成交量 / 流动性 USD | [29107.621668999996, 26539.0084] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:30:45.127293Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 15.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, -5.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.9999999999999991} |
| 24h成交量 / 流动性 USD | [2111.791153, 25765.5362] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [913.0434789999999, 11058.3325] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-28T23:28:43.955727Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.80 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.1, -1.7] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.10000000000000009} |
| 24h成交量 / 流动性 USD | [720.916742, 30565.81086] |
| 价差 pp | 1.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-10-28T23:28:43.955727Z |
| 抓取时间 | 2026-10-28T23:34:29.412913+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 13.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.5, -9.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [11586.412368, 22316.3532] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:17.113935+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 94.65 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.15, 8.15] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.6000000000000005} |
| 24h成交量 / 流动性 USD | [12761.264357999997, 46448.97491] |
| 价差 pp | 0.30 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:19.715644+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will Amazon (AMZN) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1200533 / 5778679 |
| Yes 概率 % | 64.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.5, 7.5] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [1457.416457, 565.7137] |
| 价差 pp | 5.00 |
| 到期 | 2026-10-29T21:00:00+00:00 |
| 结算规则摘要 | 下一季度首次披露GAAP EPS严格大于固定2.00美元，四舍五入到美分；优先稀释股数，官方优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报为No。后续重述除明显即时错误不计。阈值是建约时预估，不是当前一致预期，更非股价上涨胜率。 |
| 规则指纹 | ae2e6de5f9809adb3fd78a4abd5ee020076b7d0c45c6bb87b33ec71171223b21 |
| 质量 | ["liquidity_under_10000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:17.087893+00:00 |
| 来源 | https://polymarket.com/event/amzn-quarterly-earnings-gaap-eps-10-29-2026-2pt00 |

## Will SanDisk (SNDK) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1200552 / 5778699 |
| Yes 概率 % | 86.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.5, -5.5] |
| 与上一快照可比变化 | {"status": "no_baseline"} |
| 24h成交量 / 流动性 USD | [2322.525789, 338.4914] |
| 价差 pp | 10.00 |
| 到期 | 2026-10-29T21:00:00+00:00 |
| 结算规则摘要 | 下一季度首次披露主要non-GAAP EPS严格大于固定47.15美元，四舍五入到美分；官方优先，其次SeekingAlpha；96小时仍无non-GAAP才转GAAP，同样无数据或预期日后45天未发布为No。优先稀释EPS，后续重述除明显即时错误不计；不代表股价涨幅或正确估值。 |
| 规则指纹 | c10253c33b53164de814697e204ca3819998a4abec4ee0849664365afffed04c |
| 质量 | ["liquidity_under_10000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-28T23:32:44.383569Z |
| 抓取时间 | 2026-10-28T23:34:17.111141+00:00 |
| 来源 | https://polymarket.com/event/sndk-quarterly-earnings-nongaap-eps-10-29-2026-47pt15 |

## AI 压力：合约、经营与估值分开

三层分开：专门AI合约2026定价7.8%，2027年6月底22.5%；规则要求90天内至少三项极端触发，不是普通10%回撤概率。经营层：微软增长与正现金差额、Alphabet云增长反驳需求普遍消失；但Alphabet单季CFO−现金capex转负，且Q3普通股发行净募123.71亿美元、债务发行净募289.96亿美元，融资/稀释应独立跟踪。H100带日期读数28日2.90美元/GPU小时，7日+6.2%，FAQ旧2.53不采用。估值层：五家重新核验SEC列表，发现MSFT新10-Q、Alphabet新8-K业绩；新融资租赁/优先权益/TTM桥未完成，两家暂停旧估值而记录新经营事实，META亦暂不可用。NVDA/AMZN无新定期财报，复用核验底稿按28日收盘重算情景；AMZN29日财报后须重审。公司现金FCF不替代FCFF；不把公司整体价值全部归AI、也不把情景当概率。假设性恶化门槛：云增长/现金回收连续走弱且融资成本/稀释升高、GPU租金下行，需多项证据共振；未达到不代表没有估值回撤。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-28T23:36:45.852722+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 215.38 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2927825949238555, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -54.14 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -28.44 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 12.63 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-28T23:36:47.749684+00:00", "latest_filing_date": "2026-10-28"} |
| 观测财务数据 | {"revenue_million": 92279, "operating_income_million": 45915, "operating_cashflow_million": 58000, "cash_capex_million": 39367, "cfo_less_cash_capex_million": 18633, "diluted_shares_million": 7446, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null} |
| 来源 | ["https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。 |

## AMZN · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-06-30；最新 10-Q / filed 2026-07-31 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-28T23:36:49.893151+00:00", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 254.60 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3949512351888248, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.47 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -65.66 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -6.50 | 18.00 | 22.00 | 9.00 | 86.04 |

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
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm", "checked_at": "2026-10-28T23:41:32.481283+00:00", "latest_filing_date": "2026-10-28"} |
| 观测财务数据 | {"revenue_million": 127577, "operating_income_million": 40576, "net_income_million": 26468, "net_income_to_common_million": 26170, "operating_cashflow_million": 42290, "cash_capex_million": 51355, "cfo_less_cash_capex_million": -9065, "diluted_shares_million": 12368, "common_stock_net_proceeds_million": 12371, "unit": "USD million; shares million", "observed_end": "2026-09-30", "published_at": null} |
| 来源 | ["https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm"] |
| 口径 | 单季CFO减现金capex不等于FCFF；融资租赁新增/负债、优先权益、TTM及稀释桥须完整后重算；不假设缺失项为零。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。 |

## META · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | unavailable |
| 财务底稿 | 2026Q3 ended 2026-09-30 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-28T23:36:53.781442+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 指数修复重新确认

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 29日GDP/PCE与财报后常规承接 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP"] |
| 确认条件 | 29日常规开盘首30–60分钟，QQQ先收复721.25/722.87，再站回725.10–725.61；SMH先守557.98–559.81再收复567.67。回踩低点抬高、可得常规VWAP守住、RSP/金融跟随；收盘仍守住才升级确认。 |
| 失效条件 | QQQ不能收复721.25、SMH跌回557.98且反抽失败，维持脆弱；进一步QQQ失守713.59、SMH546.67是旧结构更强失效。SPY失守766.83附近50日线且无法收复亦降级；不要等最远失效点才控制风险。 |
| 观察期限 | 29日开盘至未来1–3个交易日 |
| 反证 | 盘后薄量不是完整市场；28日成交偏低、等权不跟，不能用一次越线认定反转。 |
| 状态 | 由修复增强下调为脆弱，等待重新确认 |

## 存储/散热保留观察，避免财报前押注

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | SNDK财报及云客户资本开支解释 |
| 关联标的 | ["MU", "SNDK", "DRAM", "VRT"] |
| 确认条件 | 29日首30–60分钟形成更高低点，守住常规VWAP/开盘区间，强于SMH与QQQ；MU重返并守28日收983.23、VRT242.94可作进一步确认，不追单个瞬时触价。 |
| 失效条件 | 跌破当日开盘区间下沿反抽失败且弱于行业；SNDK财报后指引、现金流或价格承接不达要求。 |
| 观察期限 | 29日开盘至财报后1–3日 |
| 反证 | 需求强不等于估值便宜；DRAM是ETF非单家公司，产品暴露须区分，未形成的VWAP不可预填。 |
| 状态 | 观察 |

## 软件云等待现金回报与价格共同修复

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | MSFT/GOOGL财报后消化及AMZN财报 |
| 关联标的 | ["MSFT", "GOOGL", "AMZN", "IGV"] |
| 确认条件 | MSFT守531.01财报前收盘并形成更高低点，IGV收复109.69再111.88–111.91；GOOGL需在下一常规时段建立承接并逐步收复缺口，不能仅凭低价。 |
| 失效条件 | IGV反抽不回109.69、MSFT跌回531.01后无法收复，或现金流/融资指引继续恶化。 |
| 观察期限 | 未来1–3日 |
| 反证 | 云增长已强，市场可能迅速修复；盘后价格可逆，无可靠全市场广度。 |
| 状态 | 暂不确认 |

## 跨期比较与上期剧本复核

对28日晚报的复核：SPY收772.31高于旧771.14，QQQ725.61高于722.87并略越更新50日线725.10，SMH567.67高于559.81，但仍未越50日线573.40；收盘条件部分实现，等权与量能条件不足。VRT强业绩反应兑现。盘后QQQ跌回721.25以下、SMH回到旧557.98–559.81带，故下调可靠性，不撤销真实收盘数据，也不把盘后薄量成交等同次日确认。Fed持平与微软GAAP4.92高于旧合约阈值4.82已由官方核验，不宣称平台已经正式结算；从未来事件栏移除。相同规则变化：4641065 95.5%→96.55%（+1.05个百分点）；3501950 0.3%→0.35%（+0.05个百分点）；3215008 76.5%→79%（+2.50个百分点）；2176270 11.5%→11.5%（+0.00个百分点）；4951227 39.5%→37.5%（-2.00个百分点）；691340 7.9%→7.8%（-0.10个百分点）；4838928 22.5%→22.5%（+0.00个百分点）；2252540 13.5%→15.5%（+2.00个百分点）；5401795 13.5%→13.5%（+0.00个百分点）；2413330 95.25%→94.65%（-0.60个百分点）。多数小变动须和价差比较。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-27/20261028T120914.307689Z/evidence.json",
    "baseline_cutoff": "2026-10-28T12:09:06.406417+00:00",
    "close_change_pct": {
      "SPY": 0.3443110602771249,
      "QQQ": 0.6045040348786834,
      "IWM": 0.3961795624804365,
      "RSP": -0.04138083620435218,
      "GLD": 0.330399427947059,
      "GC=F": -0.2282444560258723,
      "CL=F": 2.0420429272955287,
      "BZ=F": -2.8890068448158446,
      "TLT": -0.7840247595030214,
      "UUP": -0.2060486660775629,
      "HYG": -0.012889351065903387,
      "LQD": -0.22052094938046496,
      "^VIX": -3.481738552588065,
      "^VIX3M": -1.7884536889507086,
      "^VVIX": -2.8557027903868826,
      "^MOVE": -3.3923637612890634,
      "NVDA": -1.1746340873250216,
      "MSFT": -0.06022760128845395,
      "AMZN": 0.5926511117453348,
      "GOOGL": 1.3444470199952097,
      "META": -1.2415569707218466,
      "CRWV": 7.319121424689867,
      "MU": 5.864805776561233,
      "DRAM": 7.125887651427898,
      "VRT": 16.48446743635659,
      "XLK": 0.7968729025607635,
      "XLE": 0.35185143965814625,
      "XLF": 0.4473872498593101,
      "XLI": 0.3394517213162862,
      "XLV": 0.3013777023079811,
      "XLP": -0.35571449519278264,
      "XLY": -0.10393687341654356,
      "XLC": -0.4247947804866037,
      "XLU": -0.840132575201169,
      "XLRE": -0.730437249351501,
      "XLB": 0.15450334673756672,
      "SMH": 1.7366218826105229,
      "IGV": 0.11630424425856933,
      "XOP": 0.17999131055386197,
      "OIH": 0.0562552862951371,
      "ITA": 0.7370789755908103,
      "ARKX": -0.1297046541161806,
      "KRE": -0.6475629771919178,
      "SKYY": 0.4957370882091583
    },
    "quote_change_pct": {
      "AMZN": {
        "change_pct": -0.13422818791946067,
        "from_observed_at": "2026-10-28T12:00:12+00:00",
        "to_observed_at": "2026-10-28T23:38:08+00:00"
      },
      "AVGO": {
        "change_pct": -1.542881769860649,
        "from_observed_at": "2026-10-28T12:00:29+00:00",
        "to_observed_at": "2026-10-28T23:38:08+00:00"
      },
      "CEG": {
        "change_pct": -1.9083969465648831,
        "from_observed_at": "2026-10-28T11:58:32+00:00",
        "to_observed_at": "2026-10-28T23:27:30+00:00"
      },
      "DRAM": {
        "change_pct": -0.13701467634321673,
        "from_observed_at": "2026-10-28T12:05:03+00:00",
        "to_observed_at": "2026-10-28T23:37:44+00:00"
      },
      "GLD": {
        "change_pct": 0.12032889358108978,
        "from_observed_at": "2026-10-28T11:58:07+00:00",
        "to_observed_at": "2026-10-28T23:35:28+00:00"
      },
      "GLW": {
        "change_pct": -0.10348310306466102,
        "from_observed_at": "2026-10-28T12:00:07+00:00",
        "to_observed_at": "2026-10-28T23:38:17+00:00"
      },
      "GOOGL": {
        "change_pct": -9.843235085774115,
        "from_observed_at": "2026-10-28T12:00:29+00:00",
        "to_observed_at": "2026-10-28T23:38:17+00:00"
      },
      "IWM": {
        "change_pct": 0.8944543828264706,
        "from_observed_at": "2026-10-28T11:59:56+00:00",
        "to_observed_at": "2026-10-28T23:36:32+00:00"
      },
      "META": {
        "change_pct": -0.5849366721454086,
        "from_observed_at": "2026-10-28T12:00:24+00:00",
        "to_observed_at": "2026-10-28T23:38:09+00:00"
      },
      "MSFT": {
        "change_pct": 2.971644612476365,
        "from_observed_at": "2026-10-28T12:00:06+00:00",
        "to_observed_at": "2026-10-28T23:38:09+00:00"
      },
      "MU": {
        "change_pct": -0.48316708229426686,
        "from_observed_at": "2026-10-28T12:05:07+00:00",
        "to_observed_at": "2026-10-28T23:38:08+00:00"
      },
      "NVDA": {
        "change_pct": -2.595510222667463,
        "from_observed_at": "2026-10-28T12:00:29+00:00",
        "to_observed_at": "2026-10-28T23:37:36+00:00"
      },
      "ORCL": {
        "change_pct": 7.011629674673148,
        "from_observed_at": "2026-10-28T12:00:29+00:00",
        "to_observed_at": "2026-10-28T23:38:16+00:00"
      },
      "QQQ": {
        "change_pct": -0.9790750762366351,
        "from_observed_at": "2026-10-28T12:00:27+00:00",
        "to_observed_at": "2026-10-28T23:38:10+00:00"
      },
      "SMH": {
        "change_pct": -1.0298131801907084,
        "from_observed_at": "2026-10-28T12:00:28+00:00",
        "to_observed_at": "2026-10-28T23:36:23+00:00"
      },
      "SNDK": {
        "change_pct": -0.24171220133893945,
        "from_observed_at": "2026-10-28T12:00:25+00:00",
        "to_observed_at": "2026-10-28T23:38:17+00:00"
      },
      "SPY": {
        "change_pct": -0.28416832107126533,
        "from_observed_at": "2026-10-28T12:00:10+00:00",
        "to_observed_at": "2026-10-28T23:38:08+00:00"
      },
      "STX": {
        "change_pct": 3.8699998469145624,
        "from_observed_at": "2026-10-28T12:00:27+00:00",
        "to_observed_at": "2026-10-28T23:38:16+00:00"
      },
      "TLT": {
        "change_pct": -0.2579535683576828,
        "from_observed_at": "2026-10-28T12:00:14+00:00",
        "to_observed_at": "2026-10-28T23:31:14+00:00"
      },
      "VRT": {
        "change_pct": -1.5819678948681748,
        "from_observed_at": "2026-10-28T12:05:05+00:00",
        "to_observed_at": "2026-10-28T23:36:53+00:00"
      },
      "XLF": {
        "change_pct": 1.6431916426512982,
        "from_observed_at": "2026-10-28T11:50:13+00:00",
        "to_observed_at": "2026-10-28T23:25:38+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.020000000000000462,
        "unit": "percent",
        "observation_date": "2026-10-27"
      },
      "BAMLH0A0HYM2": {
        "change": -0.11999999999999966,
        "unit": "percentage_points",
        "observation_date": "2026-10-27"
      },
      "BAMLC0A0CM": {
        "change": -0.020000000000000018,
        "unit": "percentage_points",
        "observation_date": "2026-10-27"
      },
      "DGS10": {
        "change": -0.009999999999999787,
        "unit": "percent",
        "observation_date": "2026-10-27"
      },
      "DFII10": {
        "change": -0.020000000000000018,
        "unit": "percent",
        "observation_date": "2026-10-27"
      },
      "T10YIE": {
        "change": 0.029999999999999805,
        "unit": "percent",
        "observation_date": "2026-10-28"
      },
      "STLFSI4": {
        "change": 0.04910000000000003,
        "unit": "index",
        "observation_date": "2026-10-23"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-27"
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
        "change_pp": 2.500000000000002
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 1.0500000000000065
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.05
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4951227": {
        "status": "comparable",
        "change_pp": -2.0000000000000018
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 1.9999999999999991
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.10000000000000009
      },
      "5401795": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -0.6000000000000005
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
    "event": "下一常规开盘：检验盘后回吐",
    "date": "2026-10-29T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
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
    "event": "Meta优先权益发行预计交割，附条件；非普通股远期全额结算日",
    "date": "2026-10-29 America/New_York",
    "source": "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| fed-20261028 | 维持3.75%–4.00%；两票主张+25bp，不是降息承诺。 | 2026-10-28T14:00:00-04:00 | [{"source": "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm", "published_at": "2026-10-28T14:00:00-04:00", "retrieved_at": "2026-10-28T23:41:32.481283+00:00"}] |
| msft-fy27q1 | 收入922.79亿美元、Azure+48%；CFO580亿美元减现金capex393.67亿仍为正，非FCFF。 | 缺失 | [{"source": "https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast", "published_at": null, "retrieved_at": "2026-10-28T23:41:32.481283+00:00"}] |
| goog-q326 | 收入1275.77亿美元、Cloud+103%；单季CFO422.90亿、现金capex513.55亿，新增融资与普通股稀释须跟踪。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm", "published_at": null, "retrieved_at": "2026-10-28T23:41:32.481283+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN官方API418，无替代伪造数值；CME当期概率矩阵不可得。",
  "缺成分股20/50日均线广度、涨跌家数、新高新低；RSP与19ETF样本不能代替全市场。",
  "缺下一常规时段开盘区间/VWAP与可靠盘后广度；RSP/XLF/XLE分钟成交稀疏，报价非同秒。",
  "当期19ETF净申赎、拆分调整后的连续份额和当期机构流向不可得；ICI仅至21日。",
  "MSFT新10-Q及Alphabet8-K已发现；新季度租赁/优先权益/TTM财务桥未齐，不继续使用两家旧DCF。META完整融资桥仍缺失。",
  "微软完整电话会指引与Fed记者会正文未可读；tc的Azure49–50%、1700亿美元capex等只作线索，不写成已核验官方指引。",
  "tc50条上限与has_more、主动搜索截断导致覆盖不完整；外交信件、光通信并购消息未获官方确认，不据此给方向。",
  "原油连续合约未作换月对齐，不机械使用连续日线收益；GPR仅26日，信用27日，CboeCSV27日但Yahoo波动率系列28日已更新。",
  "缺最新一致盈利预测修正与完整实时融资利差；无法量化客观AI泡沫破裂概率。",
  "原始采集存在请求失败，见采集质量记录",
  "MSFT 估值: 已发现新季度披露；必要TTM、融资租赁及优先权益/稀释桥未完成，暂停旧底稿估值和价格反推。",
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
  "tc 报价质量 stale: GEV, NXPI, RSP；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.GEV.value, quotes.NXPI.value, quotes.RSP.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "Fed声明已核验；记者会全文未取到"
  },
  {
    "url": "https://www.microsoft.com/en-us/Investor/earnings/FY-2027-Q1/press-release-webcast",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "最新Q1经营与现金流；不是完整新FCFF底稿"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000080/googexhibit991q32026.htm",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "SEC8-K附件一手业绩；通过公开HTTP读取"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "带日期H100值2.90；FAQ旧值不采用"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "27日发布至21日周度行业汇总"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "页面至27日，不推净申赎"
  },
  {
    "url": "https://www.bea.gov/news/schedule/full",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "29日GDP/PCE官方日程"
  },
  {
    "url": "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "29日17:00纽约电话会"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "29日16:30纽约电话会"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "6日就业、10日CPI；进入EST"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-10-28T23:41:32.481283+00:00",
    "note": "页面可达但当期概率矩阵缺失"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-28T23:38:23.897697+00:00",
    "note": "真实分钟报价；盘后相对28日常规收盘，非同秒"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
