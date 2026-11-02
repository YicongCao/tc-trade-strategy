# 每日交易总结 · 2026-11-02

## 一分钟读懂 · Agent 摘要

### 当前判断

昨晚科技反弹失败，当前仍宜按防守与板块分化处理，不能把盘后小幅修复认作趋势反转。

### 与上次相比

相对晚报，QQQ、半导体及存储跌破原守位；金融、工业和必需消费更强。油价大跌，但AI融资和利润回报压力未消失。

### 最重要的信号

- 11月2日收盘SPY−0.48%、QQQ−1.36%、SMH−2.71%；MU−5.78%、SNDK−6.59%。
- XLF+1.86%、RSP+0.76%，说明并非全市场同步抛售；VIX升至21.15，信用利差最新可得30日仍走阔。
- PLTR上调全年指引、Apple收入增长，却在本次盘后报价中均低于收盘：好消息不保证买盘接力。

### 接下来观察

- 优先观察金融、工业、必需消费能否守住突破；先验证回踩，再考虑参与。
- 科技须先收回QQQ683.45/690.49、SMH511.63/522.49，再确认常规时段更高低点、收盘和次日延续。
- 11月3日中期选举、JOLTS、AMD财报，4日服务业ISM和国债再融资安排；避免把事件前反抽当确定结果。

### 不要忽略

分钟成交量与日量明显不符，本次不采用计算VWAP；CNN、完整广度、当期申赎和四家公司估值桥仍缺。

## 研究结论

11月3日早报：科技反弹失败，金融与等权分化走强；财报超预期仍需价格承接。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-11-02 → 2026-11-02（纽约交易日） |
| 截止·纽约 | 2026-11-02T18:57:50.722549-05:00 |
| 截止·北京 | 2026-11-03T07:57:50.722549+08:00 |
| 实际生成时间 | 2026-11-02T23:57:51.023151+00:00 |
| 市场阶段 | 盘后 |
| 下一交易日 | 2026-11-03 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-30/20261102T121041.786096Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-11-03T07:15:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-11-02T23:52:24.076287+00:00 / 2026-11-02T23:52:24.076287+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-11-02T23:52:26.488206+00:00 / 2026-11-02T23:52:26.488206+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1262633 | 已校验接入 | https://gamma-api.polymarket.com/events/1262633 | 2026-11-02T23:52:24.048044+00:00 / 2026-11-02T23:52:24.048044+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 1038648 | 冲突，保留原值 | 缺失 |  /  | 已有合约不可静默覆盖；重新采集统一时点快照 |
| 652109 | 已校验接入 | https://gamma-api.polymarket.com/events/652109 | 2026-11-02T23:52:26.874069+00:00 / 2026-11-02T23:52:26.874069+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 32224 | 已校验接入 | https://gamma-api.polymarket.com/events/32224 | 2026-11-02T23:52:27.694070+00:00 / 2026-11-02T23:52:27.694070+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |
| 199777 | 已校验接入 | https://gamma-api.polymarket.com/events/199777 | 2026-11-02T23:52:27.611349+00:00 / 2026-11-02T23:52:27.611349+00:00 | Gamma snapshot quote not last trade; distinct expiry and rule hash stays separate |

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
| cnn | missing | 核验 CNN Fear & Greed 原值及更新时间 | 降低相关判断可信度；保留缺口 |
| news | truncated | 按事件/时间分批核验新闻线索 | 降低相关判断可信度；保留缺口 |
| request.fa27edcf5f54 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |
| request.38906ddc2d63 | request_failed | 核验该来源失败影响，见本地原始错误 | 降低相关判断可信度；保留缺口 |

## 决策指标：趋势、相对强弱、波动与宏观

| ID | 数值 | 单位 | 观测日/时间 | 质量 | 定义 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| prices.SPY.value | 752.10 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | -0.48 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | -1.73 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | -2.93 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | -2.49 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 769.33 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.54 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 726.31 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -2.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | -1.88 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 3.55 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 8.97 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 1.19 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -3.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 1.28 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 681.09 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | -1.36 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | -4.37 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -9.93 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | -5.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | -0.88 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | -2.63 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -7.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | -3.21 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 724.43 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 724.07 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 678.68 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -5.98 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -5.94 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 0.35 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 15.22 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 2.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -10.34 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 1.37 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 279.14 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | -0.07 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 0.78 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | -1.50 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -7.19 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.41 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 2.51 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | 1.44 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -4.70 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.20 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 283.63 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.77 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 0.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -1.58 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 0.49 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 4.10 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.47 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -8.27 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 1.00 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 219.98 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 0.76 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 1.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 4.20 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 0.33 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | 1.24 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 2.97 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 7.13 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | 2.82 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 215.34 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.71 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.64 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 2.16 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 2.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 6.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.24 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 1.02 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -0.88 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.61 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 361.65 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 1.65 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -1.68 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -4.72 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | -9.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | 2.13 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | 0.06 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -1.78 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -6.75 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 374.87 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 389.34 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 412.61 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -3.53 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -7.11 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -12.35 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 6.17 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.71 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -15.52 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 1.02 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 3,955.70 | USD_per_troy_ounce | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 1.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -2.05 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -4.84 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -10.09 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 1.94 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -0.31 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -1.90 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -7.60 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,104.98 | USD_per_troy_ounce | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,280.30 | USD_per_troy_ounce | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,515.98 | USD_per_troy_ounce | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -3.64 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -7.58 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -12.41 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 75.41 | USD_per_troy_ounce | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.91 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -15.80 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.01 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 96.35 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -7.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -5.32 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 7.74 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 23.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -6.98 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -3.58 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 10.67 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 25.74 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 97.78 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 94.82 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 86.53 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | -1.47 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 1.62 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 11.35 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.58 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.75 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -8.96 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 104.32 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -11.32 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | -9.92 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 3.99 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 24.86 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -10.84 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | -8.19 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 6.92 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 27.35 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 109.14 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 103.46 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 92.66 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | -4.42 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 0.83 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 12.59 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 4.49 | USD_per_barrel | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 4.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -11.32 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.00 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.73 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -0.13 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 0.06 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 5.99 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | -0.47 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | 0.34 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.80 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 8.92 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | 2.03 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 79.89 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.28 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.21 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 2.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.81 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.78 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.86 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 1.05 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.31 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.94 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 28.96 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | -0.14 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | -0.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | -0.10 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | 0.34 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 1.56 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 2.83 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 5.67 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 29.00 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.61 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.93 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | -0.14 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 1.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 3.68 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.11 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.39 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.58 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 1.35 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 76.89 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | -0.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | -0.40 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | -0.12 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -2.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.22 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 1.33 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 2.82 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | 0.04 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.15 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.77 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | -0.34 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -1.13 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -1.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.32 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.42 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -2.83 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 103.71 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | -0.54 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | -0.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 1.85 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -1.84 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.06 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 1.44 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 4.78 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | 0.66 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 103.29 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.74 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.83 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 0.40 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | -0.03 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -2.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.66 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.64 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -2.12 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 1.16 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 21.15 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | 8.91 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 15.01 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 36.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 36.80 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | 9.39 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 16.74 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 39.21 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 39.27 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 17.28 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.29 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.26 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 22.38 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 29.84 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | 15.80 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.72 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 12.85 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-02 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 21.60 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | 3.95 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 8.32 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 20.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 15.38 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | 4.43 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 10.06 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 22.93 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 17.88 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 19.16 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.64 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.52 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 12.71 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 15.89 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | 5.25 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.51 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 6.97 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-02 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 110.47 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | 3.80 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 8.91 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 29.27 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 22.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | 4.27 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 10.65 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 32.20 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 24.67 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 96.76 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 92.09 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.85 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 14.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 19.96 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 11.75 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 12.08 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 10.93 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-02 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 100.36 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | 0.16 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -1.79 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -6.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 31.85 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | 0.64 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -0.06 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -4.18 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 33.75 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 101.10 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 90.90 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 77.75 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -0.73 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 10.41 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 29.08 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.02 | index | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -11.65 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-11-02 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 202.06 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | -1.26 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | -6.45 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -15.42 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | -9.68 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | -0.78 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | -4.72 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -12.49 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | -7.18 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 219.62 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 221.44 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 204.17 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -7.99 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -8.75 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | -1.03 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.74 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 3.33 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -15.54 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 1.16 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 507.12 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -2.83 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -4.78 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | -3.44 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 1.62 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -2.35 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -3.05 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | -0.51 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 4.11 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 530.08 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 513.39 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 437.12 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | -4.33 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | -1.22 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 16.01 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 12.78 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.52 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -6.69 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 1.54 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 245.63 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 2.20 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -1.39 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | -2.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -10.51 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 2.68 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | 0.34 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 0.64 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -8.02 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.10 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 254.02 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.44 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -3.33 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -3.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 0.90 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 8.36 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 3.40 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -11.67 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 1.39 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 278.99 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | -0.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -11.93 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -19.48 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -21.21 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.18 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -10.20 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -16.54 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -18.71 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 330.53 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 337.72 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.08 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -15.59 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -17.39 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -17.96 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 10.92 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 3.92 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -22.97 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.46 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 606.73 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -1.34 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -3.78 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -18.22 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 2.55 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -0.86 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -2.05 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -15.29 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 5.05 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 684.35 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 670.93 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.21 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -11.34 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -9.57 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -3.88 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 23.54 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 3.88 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -21.97 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 0.82 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 50.15 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | -8.60 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -9.13 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -42.61 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -44.69 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | -8.12 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -7.40 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -39.68 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -42.19 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 66.91 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 78.70 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 91.13 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -25.04 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -36.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -44.97 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.97 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 13.89 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -53.45 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.80 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 833.59 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | -5.78 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | -7.76 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -21.64 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | -5.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | -5.30 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | -6.02 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -18.71 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | -2.50 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 939.04 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 975.93 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 749.11 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -11.23 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -14.59 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 11.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 51.19 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 6.14 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -24.03 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 46.32 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | -3.52 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | -4.16 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -24.89 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -8.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | -3.04 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | -2.43 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -21.96 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -5.96 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 51.21 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 55.74 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-11-02 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -9.54 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -16.90 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-11-02 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.94 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 6.35 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -27.19 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 0.92 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 224.24 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | -3.55 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 12.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -11.58 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -17.66 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | -3.07 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 13.98 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -8.65 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -15.16 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 223.62 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 241.83 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 270.69 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | 0.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -7.27 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -17.16 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 15.57 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 6.94 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -23.67 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 0.85 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 174.22 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | -2.95 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | -6.49 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -13.29 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | -7.21 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | -2.47 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | -4.76 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -10.36 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | -4.71 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 189.52 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.43 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 169.38 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -8.07 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | -8.03 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 2.86 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 5.19 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.98 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -13.75 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 1.65 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 67.25 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -3.96 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | -3.43 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 5.99 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 17.65 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -3.48 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | -1.70 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 8.92 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 20.15 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 67.31 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.86 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 58.25 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | -0.09 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 3.69 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 15.44 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.54 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -3.96 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 1.61 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 57.56 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | 1.86 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 2.75 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 6.83 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | 0.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | 2.34 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 4.48 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 9.76 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | 2.78 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 55.52 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.87 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.43 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 3.68 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | 3.02 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 7.74 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.76 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.33 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -1.36 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 169.71 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 1.38 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 1.65 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -0.23 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -8.11 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 1.86 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 3.38 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | 2.70 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -5.61 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.07 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 170.30 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.60 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | 0.98 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -0.35 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -1.68 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.82 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.66 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -8.76 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 1.21 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 184.60 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.15 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | 2.97 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 10.29 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 11.85 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | 0.33 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | 4.70 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 13.23 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 14.34 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 176.55 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 172.17 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.82 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 4.56 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 7.22 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 16.97 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 3.26 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.77 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -0.15 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 1.50 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 90.83 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | 1.58 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | 3.26 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 12.08 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 7.41 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | 2.06 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | 5.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 15.01 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 9.90 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 86.50 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.49 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.63 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 5.01 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 7.50 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 8.61 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.51 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.66 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 1.65 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 118.16 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 2.41 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | 3.41 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 7.01 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -1.20 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 2.89 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | 5.15 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 9.94 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | 1.29 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 113.90 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.14 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.14 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 3.74 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 4.43 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 2.62 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.96 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.66 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -1.20 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 1.64 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 100.26 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | 0.36 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -3.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -10.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -9.58 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | 0.84 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -1.72 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -7.24 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -7.09 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 107.84 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 110.35 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.27 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -7.03 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -9.14 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -10.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.89 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.88 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -12.63 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.34 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 43.67 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.55 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 2.63 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 9.26 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | 0.87 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 1.03 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 4.37 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 12.19 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | 3.37 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 42.13 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.65 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.81 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 3.65 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 4.85 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -0.32 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.61 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.39 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -0.72 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 1.05 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 43.64 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | 1.09 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 1.96 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 7.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -2.16 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | 1.57 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 3.70 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 10.24 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | 0.33 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 42.10 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.48 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.78 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 3.66 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | 2.72 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | 2.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.64 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -2.98 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 1.12 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 53.67 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 1.76 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 4.46 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 8.42 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 2.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 2.24 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 6.19 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 11.36 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 4.49 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 50.91 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.90 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.75 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 5.42 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 5.44 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 5.75 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.72 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.35 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | 0.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.79 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 508.31 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | -2.71 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | -6.15 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -19.81 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | -12.77 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | -2.23 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | -4.42 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -16.88 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | -10.27 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 563.62 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 571.57 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 520.06 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -9.81 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -11.07 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | -2.26 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 21.73 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 4.27 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -19.81 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.91 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 101.90 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | -2.29 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | -8.52 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | -7.13 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | -0.77 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -1.81 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | -6.79 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | -4.19 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 1.73 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 108.87 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.96 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.96 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | -6.40 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | -4.73 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 8.45 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 3.23 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 3.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -9.56 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.38 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 193.56 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -5.01 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -5.52 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 3.27 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 16.79 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -4.53 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -3.78 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 6.20 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 19.28 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 197.41 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 191.48 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 169.89 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | -1.95 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 1.09 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 13.93 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 5.27 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.72 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -5.52 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 2.22 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 389.03 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | -5.48 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | -3.32 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | -1.44 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 0.19 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | -5.00 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | -1.59 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 1.50 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 2.69 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 391.76 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 400.63 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 397.95 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | -0.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | -2.90 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | -2.24 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 12.75 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 3.28 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -10.89 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 1.26 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 214.68 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | 2.36 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 3.63 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | 3.72 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -14.29 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | 2.83 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | 5.36 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | 6.65 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -11.79 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.99 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 214.18 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.46 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 3.71 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | 0.23 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -6.03 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.93 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 2.30 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -15.12 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.18 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 29.57 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | -0.74 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | -1.99 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -10.15 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -13.71 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | -0.26 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | -0.25 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -7.22 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -11.22 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 30.83 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.69 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.46 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -4.08 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -6.68 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -8.90 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.86 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.92 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -15.17 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 1.69 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 73.73 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | 2.39 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 1.37 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 4.74 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -2.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | 2.87 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 3.11 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 7.68 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -0.21 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.78 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.79 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.38 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 4.16 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 2.70 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 4.76 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.38 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.87 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -4.85 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 1.33 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 154.55 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | -3.27 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | -9.01 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | -9.00 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | -1.04 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | -2.79 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | -7.28 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | -6.07 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 1.46 | pp | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 166.91 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.67 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 136.66 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | -7.40 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | -6.14 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 13.09 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 5.55 | USD_per_share | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 3.59 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -11.63 | percent | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 1.05 | ratio | 2026-11-02 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.56 | percent | 2026-10-30 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.44 | percentage_points | 2026-10-30 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.94 | percentage_points | 2026-10-30 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 4.94 | percent | 2026-10-30 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.60 | percent | 2026-10-30 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.29 | percent | 2026-11-02 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.58 | index | 2026-10-23 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 19.42 | index | 2026-10-30 | lagged | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 97.67 | index | 2026-11-02 | ok | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 113.60 | index | 2026-11-02 | ok | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 94.75 | index | 2026-11-02 | ok | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 137.64 | index | 2026-11-02 | ok | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 164.04 | index | 2026-11-02 | ok | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AAPL.value | 328.92 | USD_per_share | 2026-11-02T23:52:28+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AAPL |
| quotes.AMD.value | 473.79 | USD_per_share | 2026-11-02T23:52:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMD |
| quotes.AMZN.value | 246.82 | USD_per_share | 2026-11-02T23:51:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.AVGO.value | 323.64 | USD_per_share | 2026-11-02T23:52:22+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.BABA.value | 101.90 | USD_per_share | 2026-11-02T23:45:08+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/BABA |
| quotes.CAT.value | 614.41 | USD_per_share | 2026-11-02T23:50:26+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CAT |
| quotes.CEG.value | 258.00 | USD_per_share | 2026-11-02T23:47:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.COIN.value | 137.60 | USD_per_share | 2026-11-02T23:51:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/COIN |
| quotes.CVX.value | 228.65 | USD_per_share | 2026-11-02T23:29:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CVX |
| quotes.DRAM.value | 47.18 | USD_per_share | 2026-11-02T23:48:17+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GEV.value | 867.37 | USD_per_share | 2026-11-02T23:40:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 361.69 | USD_per_share | 2026-11-02T23:51:58+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 124.23 | USD_per_share | 2026-11-02T23:49:55+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 280.15 | USD_per_share | 2026-11-02T23:52:15+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 102.12 | USD_per_share | 2026-11-02T23:14:10+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.ILMN.value | 226.58 | USD_per_share | 2026-11-02T21:33:54+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ILMN |
| quotes.INTC.value | 60.50 | USD_per_share | 2026-11-02T23:52:21+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/INTC |
| quotes.IWM.value | 279.50 | USD_per_share | 2026-11-02T23:45:01+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.LITE.value | 688.20 | USD_per_share | 2026-11-02T23:51:35+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LITE |
| quotes.LLY.value | 1,410.99 | USD_per_share | 2026-11-02T23:36:39+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/LLY |
| quotes.META.value | 609.80 | USD_per_share | 2026-11-02T23:51:04+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MRVL.value | 174.50 | USD_per_share | 2026-11-02T23:51:20+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MRVL |
| quotes.MSFT.value | 509.00 | USD_per_share | 2026-11-02T23:52:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 842.67 | USD_per_share | 2026-11-02T23:52:20+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NOW.value | 106.40 | USD_per_share | 2026-11-02T23:50:34+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NOW |
| quotes.NVDA.value | 203.84 | USD_per_share | 2026-11-02T23:52:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.NXPI.value | 257.54 | USD_per_share | 2026-11-02T21:31:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.ORCL.value | 119.94 | USD_per_share | 2026-11-02T23:51:10+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.PLTR.value | 172.51 | USD_per_share | 2026-11-02T23:52:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/PLTR |
| quotes.QQQ.value | 682.98 | USD_per_share | 2026-11-02T23:52:16+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 220.80 | USD_per_share | 2026-11-02T23:41:48+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 513.57 | USD_per_share | 2026-11-02T23:51:11+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 1,094.30 | USD_per_share | 2026-11-02T23:51:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 753.31 | USD_per_share | 2026-11-02T23:49:40+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 598.15 | USD_per_share | 2026-11-02T23:42:18+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TLT.value | 81.60 | USD_per_share | 2026-11-02T23:41:26+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 226.30 | USD_per_share | 2026-11-02T23:45:52+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 67.55 | USD_per_share | 2026-11-02T23:49:21+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 57.59 | USD_per_share | 2026-11-02T23:29:48+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| quotes.XLI.value | 169.71 | USD_per_share | 2026-11-02T22:51:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLI |
| quotes.XLV.value | 184.59 | USD_per_share | 2026-11-02T23:31:06+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLV |
| quotes.XOM.value | 180.00 | USD_per_share | 2026-11-02T23:41:19+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XOM |
| latest.BZ_F.value | 104.32 | USD/barrel | 2026-11-02T23:41:00+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| latest.CL_F.value | 96.33 | USD/barrel | 2026-11-02T23:42:14+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| latest.DX-Y.NYB.value | 101.80 | index points | 2026-11-02T23:04:59+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB |
| latest.ES_F.value | 7,587.75 | index points | 2026-11-02T23:42:23+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| latest.GC_F.value | 3,955.70 | USD/troy_oz | 2026-11-02T23:42:27+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/GC=F |
| latest.NQ_F.value | 28,243.00 | index points | 2026-11-02T23:42:22+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| latest.TNX.value | 4.89 | percent | 2026-11-02T19:59:00+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/^TNX |
| latest.VIX.value | 21.15 | index points | 2026-11-02T21:15:00+00:00 | ok | 提供者最后有效分钟或实际regularMarketTime；期货连续代码具体合约月未对齐，不直接拼接其他序列收益 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.6199951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.27001953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2938913265121532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1895703675424474,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.1745718920831871,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.588988553670967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.124908525169932,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.9022057272909962,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.068455088104514,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.204409003099286,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.136502075195267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8070068359375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.23446533203127728,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.17688720703131366,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3261245727539972,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9020440673828034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.32563954378729276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.6206290294835557,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.44210458547898623,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.7081217817699113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5451495276929119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.1037307974572483,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6753583635602673,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7203587123325885,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.09507989922222748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.2454556569608599,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4646440067778035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.7032716468993847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7831107296788375,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4983744889449476,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -9.39996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -31.1099853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1125307541569383,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.468670410875329,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.3934178302171705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.5106478319598455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.049470831874122,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.629225471403354,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.422429670620074,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.32924640493612,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.818639427644785,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.2791000433328814,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.2188459381339833,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.9216592782888786,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9245623067041899,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.727019744112358,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.3539745825155598,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.1248374018368335,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.7554992675781023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.586502075195312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6321472167968523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.0063049316406705,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3071014404296193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.114925231933512,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.8059945443945944,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.0104190998930243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.2150261585323836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.160023656031564,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.431088891174248,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.911913735353224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.849286760602677,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.868573869977677,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.15342906162104475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5004215603385846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.2373909000359848,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.095251356048946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9495540391629256,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.47473186354329666,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.189971923828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.1500244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.579827554726898,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5176889988984135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5220624073402291,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.3286230427519197,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7182999182328453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.41415550614706254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0938364892621344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.5615283089784446,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.28593622821474485,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6718813686440339,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.652509484742958,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.26036551091904725,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.40660860693708667,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.4880502211439337,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.02538140115762033,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.6428806941208416,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.21199951171877274,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.15650024414060226,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4007720947265625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.9154620361328512,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07709472656250682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.505044479370099,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.008476148517888582,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.719182636118576,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07198472466678485,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4131526738950462,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.09630839443850459,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5923833451767946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07714189801897309,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4728567940848212,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02861586347572742,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.15930964884321863,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.062430129653090916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7065586336255976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.033466230360473026,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.39936453503354596,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.69000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5511851876846228,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.41861007608978706,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.42057511856437024,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5848895608632887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.10569072376376276,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5969768437764644,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07382600831256081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1145673850299964,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.25729386117246955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6081804436322344,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5951470106475574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0040989928076782,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2305992489336948,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.4991825710674607,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1422810964170749,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.08984161806929,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.44300003051756676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.29549942016601,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.017197265624986358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.14366760253906818,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.113893432617175,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5679860687255882,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5665334472882977,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.16194427669691258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7859439191508777,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.3205394694566497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7499156330251333,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0119614132279464,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.06500026157924088,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.17571476527622742,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02196993058937735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.06823634050055216,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7524692190277738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.2120636261212958,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.40954593742182377,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.730050220819179,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 5.8699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.170013427734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 5.120065374848837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.3198376218443997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2766348163186336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4487787093629412,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.69205961247647,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.0461628516127766,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5432399906718075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.239107731153807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.8261740483366835,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.509407989386847,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.4512067084018208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.037767263033908,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.816968137646402,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8560428756782197,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5252150974327066,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.03469872805452,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.8949996948242074,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.7195007324218636,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.2341998291015557,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.494199218749998,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.3083999633789176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.3790499877929392,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7919290689529017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.6819210896517491,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7964495258015587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5066674680082821,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.487044054364473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1984058983907406,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2935703822544635,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8592856270926337,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.054376008901238615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.2622243950061378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.3712698896798923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.4413561618815347,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0048505338461875,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.24966173253312207,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 56.800048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -82.699951171875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.7435219327813805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6958253941238723,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6717892300916684,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8775755036643074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.490377191407699,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.7191500536785527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7721263457383998,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.421280909975248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.4496306062692272,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.8853957616663197,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.8463611221748555,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.4665640573352743,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.615285716577631,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1830556736124436,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2963287423661143,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.2168719068759613,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -10.05499267578125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -43.779992675780704,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -14.498002929687573,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -53.58800292968772,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.340001220703016,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -14.809503173828489,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6157649513235173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.9764856656792054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.634502583913732,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.765498280627197,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.3215639480487216,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.5389776258459165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4643205915178612,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.5643310546875,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.015864888145340483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.17682701476849805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2090776786922603,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.7603975182032272,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9534864964671793,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.170077818897632,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.7700042724609375,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.410003662109375,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -9.540981191185027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.000365896199611,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.139525358464626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.4835175975046373,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.541551194341654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.1541192701768566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -11.472183223277476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.056985898645582,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -10.834872517697182,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.810795528657164,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.964953466381439,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.8945290438336704,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.41664266917172,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7480864571141392,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -10.403728135172962,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.261394901744868,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.34599990844726847,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.5970001220703125,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1858000183105446,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4997999572753997,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18579999923706225,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0208500099182203,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.324284982353426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.371971675421008,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.410451890330828,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.430742376276456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -9.238725165283789,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.656383353595707,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3178569248744427,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.212856837681362,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6597351413196906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4616951107020988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.341967436478791,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.111975402538327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9770000895139306,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1845640008327913,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -13.319999694824219,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.489997863769531,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -13.725188040852355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.54303243922834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -10.70963091151389,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -15.635701925823287,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -11.064103304880081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.014657811061075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -17.751867832952236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.647068514327035,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -15.019079367364508,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.353462071685893,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -9.535059019430703,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -14.046713372152318,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -9.939194779710146,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.112452083770079,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -16.683412744847722,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.557340488772251,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.20000000000000284,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.75200004577637,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.19860000610351847,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.0871998596191474,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.20280000686645394,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.215399990081778,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -12.402046750922713,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.272163826311777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -13.092661969606368,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.409778465754574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -14.653869838490397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -14.061615479207102,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7907142639160156,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5614286150251115,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1591728112366457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9115369268058928,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -11.32267916009212,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.54303243922834,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.1863036291871927,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7128718470873993,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.10999298095703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0500030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5638987226216696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5524034525617227,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5534855088856538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.7326418820188936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.36419496891906267,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6808868987191916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.42382758777884666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.9590909746353127,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.8577900491338228,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6371669149807246,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6210863831975333,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1436533283479267,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.4891034940889956,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.583092626010188,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6446275003256674,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.2453180284639735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2310001373291044,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9997898101806584,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.006421661376947441,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.009334564208984375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.01801696777343409,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.08773616790770689,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4347082290262039,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.232995957980676,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.14516859707573992,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.05045459664720919,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.11089789376236281,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.16349019925929742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.006785801478794595,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.027500152587890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.009705181190194923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.03302425906837669,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.13281317220720235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.060377161035296556,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.1077969701408148,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4373987653174724,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.04000091552734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.05000114440917969,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.00018999634185945524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.3105900823226704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.31048301676297463,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.2068418519520998,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4842430364434769,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1836238126439191,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2972852782525903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.18874650936526738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.2940813228540127,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.878980285219777,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8640888753202125,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.382146701718867,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6406654887264551,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.718581914647077,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.3657403663571044,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.393155512464554,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.0015000343322739695,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.04100008010864187,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.021199989318848367,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.10500003814697223,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.007649993896485796,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.04229999542236129,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.13276192683039367,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.31404631251216175,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.21501670301868891,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5483908568156837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.17164394713933273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.336514906978147,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.0021427699497767877,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.005714280264718194,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.006854735064988571,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.019030193881416413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.13731862917873983,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.17164828647342478,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.30460236650704653,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7885061225571578,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5400009155273438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5040545230605264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8920761373828912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.8947339160661594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8831276058371307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7930291751709451,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.12139566702427107,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.8705014221130125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.0297144290083105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.7979458495726797,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.2974942301595562,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.27983797601702776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7058609478338362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.33187934999898694,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.780810060266725,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.19795366599150155,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.174694574090976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.00450019836425497,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.12073249816894815,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.03870758056640966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.14014434814453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.003165817260736503,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.002436790466305183,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6940468208582184,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5586118284581665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6448143282013818,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.22004621780016276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6892571855371399,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.39489958931818725,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.015714372907366048,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.042858123779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02322978777782747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0572055294367288,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6824024453453204,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.3917458025582632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.24453882665683957,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.2755931934979169,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.55999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5850359489040224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7007607852326014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7024449825212109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.4061038022505024,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5499337607032917,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.10443707519605105,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7063633254677293,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.9988833013919507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.8789272754161757,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.48880958230984595,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4721269095619762,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.18288475142046456,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5749747644666403,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.797768652094945,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3620917626367848,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.2055257017073355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.09399986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5584491729736385,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.026280517578115337,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.10072128295898608,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.016695289611817543,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.0703358459472696,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6340993186748634,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.847538742500098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5143320467362877,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.20155949064867285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5136125835140115,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.22764082446479206,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.019285474504743272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.019284929547991103,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02190614078038755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.0204320854474338,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5285255536291555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.2925787634898036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.05424911705036206,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4658686429465613,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7299995422363281,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.760000228881836,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.998632656170198,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 14.358217835519595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 15.162403519066471,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 15.279314222452257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 9.430570480536744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 21.838929513248615,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 6.469080056106556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 20.85257500696287,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.292523982682351,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 15.54778820306204,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 16.336975411149655,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 16.868302776123222,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 10.555479005706673,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 24.74113524053961,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 6.909378927427554,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 24.585626579484543,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2814999580383315,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6299999713897719,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.10599998474121008,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.2895999908447262,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0052999973297112035,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.03840000629424978,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 8.149732018567102,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 11.94448566296371,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 9.839861511681637,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 14.90057338880968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 9.44157632593625,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 14.899952224516166,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2357142993382042,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7221431050981792,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.06901465044249733,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9982184781644357,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.851424218862486,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.004004000947662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8199996948242188,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6599998474121094,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.333196358007373,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.582814388235314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 6.860124565892066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.590279314270696,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.61965551982677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 10.619853821085368,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.202170649488979,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 10.547607700132433,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.627087684519527,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.772384755777761,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 8.034696457975254,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.179267867941665,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 5.7445640449967,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 13.522059548376362,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 5.270625737593493,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 15.75201670323172,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18000001907348562,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4744999885559089,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.062000007629393394,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.12200000762939212,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.01350000381469485,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.03655000686645238,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.2507913488172946,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.020496638566985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.027568094684632,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.20177709404124,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.9290847012724672,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.915576622928722,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.125,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.37785707201276497,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.32646123477804245,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.314644668375455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.255811469499451,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.040000915527344,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 9.040000915527344,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.795034998912539,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 11.334662225036219,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 11.893405308489502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 14.056103244936791,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 6.95993384102529,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 17.828104853163065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.212625665804378,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 11.491192662493697,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.088926325424691,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 12.524232592578667,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 13.06797720057269,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 15.645091798607758,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 8.084842366195218,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 20.73031058045406,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.281080753908892,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 16.69560166559298,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2505001068115291,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.364500045776367,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4840000915527298,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.2304000854492188,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.047849998474120525,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1141500091552814,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.735124633077236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.566399047785952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.776459449985861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.325111458325708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.034670258556129,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 9.026122366412938,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7150001525878906,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.1635704040527344,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2567645461082435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1585869307397765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.1662298616893736,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.715406309150197,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.16150665283203125,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.8284988403320312,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.9587600849237985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.2452953564991875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2210449940288859,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.667890696111075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8760365570616324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.905648033855254,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.33187511866042,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7129290146448852,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.252651411435952,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.434865724041635,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.395616886112073,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.078902142440108,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.072551695898584,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.401917062923438,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.017196818092536,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.634699292862361,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.3464248657226676,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.3884243011474666,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5436300659179665,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.43783004760742,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.21125751495360134,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8811575126647853,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4981654655525358,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5240937748663965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4855839148869787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.109994239180393,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.1433841865938561,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.8582567331916664,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.06379318237304688,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.2952210562569757,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.07173239082878968,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.19934732120983334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1421713512336229,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.6095940712081749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.5800018310546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.94000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.960911024604107,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.6498267246541594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.4578728643775425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.9516106074986475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.8923598325273456,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.801520901575222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.2293321841068483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -17.394491629792054,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6670196980919538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.460256357111712,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.283300972294355,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.36262205382768,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.7674513073574136,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.899315174284226,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.1608770960023342,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.190082626692767,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.8419998168945426,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.280999755859369,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.24840026855466135,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7795474243164051,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07723358154296989,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6502067565917855,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.39974000598516124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.03790890093233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0615699176325206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.953073320823454,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.3015871566252057,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.165658952244458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.195492335728237,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5919222150530139,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.13755592286604434,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4891666672959656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.07841572137416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.82678570528814,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.527294360032309,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.3037589824007728,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -14.78997802734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -25.47998046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.2813899576870624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.3762032606440515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.2883669375407445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.611626782871026,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.285137409894646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.0301512820532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.9908231084270653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.205419940487584,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.5752812841992156,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.186632893101604,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.1137950454575574,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.022638229200059,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.160228884724714,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.127945554762204,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.9223680203225513,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.001010937388298,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9029998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.206999206542946,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.47760009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.2709509277343045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.266694641113304,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4655589294433753,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.622709204625362,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.226919640052796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.975517924095583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.833388135750761,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.45639097812451,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.238933314691472,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.04571533203125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6678597586495538,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2717985872039419,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.43375217741022265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.7214974137693804,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.688560106066064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.14397810059967808,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6106203892960103,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 5.279998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.459991455078125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.6078410505878233,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7572811226258311,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.695622203855085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.701446482684912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1458550628241753,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.4895375453321,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2096294035915154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.2296195645190817,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.31394972407567,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.9468514901682785,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.870194095938272,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.290435036355879,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.2707635879941073,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.5873318180411036,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.2780844916960294,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.9747894385802045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.28849945068358807,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.47499847412109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.2600000000000193,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.3573995971679835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.03725006103513806,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1309500885009811,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1851756951661643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1787513696958074,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.175331921112955,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8408843089952711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1538210187016738,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.476374384894874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6457148960658472,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4214248657226554,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1938819447514688,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6179274330112179,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.8986654855723266,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6259503716779182,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.3607452757174812,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4780209479107832,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.850006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -37.80999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.098553883140796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7611801321062761,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.672375800469716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.9798330962887984,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9436846905596532,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.905317313140095,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5221205802977913,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.218833682906912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.19533744337135728,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9507504996487235,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.846947692552904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.390844542617831,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1812238346102788,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.0031115858491,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5905756684023054,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.014424679807625,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.3740005493164062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.254499816894565,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.3121704101562273,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.58372375488284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.26571945190431734,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.868336791992192,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5983292435068552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.28308264416937,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.06901789807904635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.939644589548214,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.18570026736149714,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.880824565068858,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.08214460100446352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.502864292689731,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.04124783094245643,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.2573782969475893,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.879116162725147,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.914012034623795,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6600932679026086,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4499259230284003,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.260009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -23.83001708984375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18286371047222527,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5335790459171874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.520403726066343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.835469367961833,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6868048050894835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.33324558081887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.7837904020729045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.803084304904974,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.111027616039928,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7231494134596348,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6949756181495301,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.4244579216328,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.5618962799195515,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.4310398535278743,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7153353139683905,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.598675301805689,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.7585021972656705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -29.04800109863288,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1452722167969114,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.533840332031218,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.06237976074214657,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.37699798583980737,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.32817657685293256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.26961054062976153,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.387853571957475,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.476009018125781,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.298965618372716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.715645210667695,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.510711669921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.3850010463169617,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.19353788898010027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.23161010587298225,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0622576782559854,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.064599116093479,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.3049277381503587,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7847345900459607,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.719997406005859,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.039997100830078,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.062000522889571,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.362997836340426,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -10.302911657184621,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5701416790024112,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.8387390842523033,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.489552301771916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.992821138949537,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -21.587957882494933,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.23189080362258263,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.17342746879798,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -9.128339765101433,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.1591302326733786,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.713830559082375,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.587346574480918,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.924366050845023,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -16.383548879395647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.8619998931884822,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.468500137329102,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7539999389648528,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.5677999877929665,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.22430000305176634,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7655000305175861,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.8341166011974686,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7504023127991033,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.3359256214640105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.3627931539684326,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.031842645830373,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.026316401217656,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.15164266313825348,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4691426413399835,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.4715887443470717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.118903713253248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.381321135178517,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.6783597361743645,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.10905422317910829,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.528485661522391,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -51.14996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -70.1099853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.47988707992534607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.761245429503461,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.57743066397575,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.625491156587083,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.9625629698327174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.394954813384956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.3833907232318285,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -14.81548369425719,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.7737784064374997,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.571675061961015,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.4028587718925625,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.036502602916116,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.837654444662787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.492749086093962,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.3149356351273145,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.611074691157905,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -11.51012268066404,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -40.049765014648415,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6607580566405886,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.3075988769530795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.486030120849591,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 14.33380950927733,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.306170089982597,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.5295675517670553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.994652942477185,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.683031339808377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.221343588327356,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.712429769465027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2028166687139148,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.22029825330221087,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.377946611116454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.50078870322442,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.661789790490058,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.389799568421719,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.06416218346142988,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.2786671567291553,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.6899986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.0100021362304688,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.7069591417014154,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.218780668717283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.177604762167754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.1589117733882075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6017769492248455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.845320623587259,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.7905324200896864,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.408471756564858,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.413067815189262,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.029210301174835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.003032870084567,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.5699232197172406,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.4768684240549135,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.943114896296265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7220773319851723,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7959372465344279,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7674999237060547,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.8204999923706,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.22720001220703523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7034000396728501,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.9158409638592726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.00198977876944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.682293454104146,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.5255067076800923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.014642987932477869,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.23535701206752213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.19295311629147616,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7509835376867331,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6563952453353394,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.1593872523991813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4828764804086372,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.26670287769266265,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.259994506835938,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 24.460006713867188,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.904372692912626,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.362479577034186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.404527533783067,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 15.300537921126343,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.7803091661536277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.552113286449956,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.173627386948052,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.380631623094132,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6104813664004727,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.172909209491738,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.229955641699879,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 16.88952647479731,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6554006409836957,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 9.454319013740951,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.105172298843538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.823777380005154,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.4689994812011662,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.3704986572265625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7529159545898381,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.961170043945316,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2590961456298828,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.5250843048095817,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.0152014433164176,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 12.650704312708994,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.1171832974578484,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 11.445750396111709,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.133696958292642,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.617860282573343,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5110637119838177,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.7478474208286823,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4665421906879841,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0256926625662537,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.8117409703881755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.32630130158466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.25091187044423924,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.14406619053948266,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.2899932861328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.9434236081306904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.6333188186918335,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.463970604318878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.68779688194826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.1335295932481397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.0727585542691,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.179517928692922,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.58689429010187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6495322816185372,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.4437484511493865,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.2893987122356907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.0988083282772925,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.0086210680782077,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.1705528269781045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.1110628405884078,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.382485287002584,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.3354995727539176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.291999053955095,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.17752655029295283,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.03901275634765966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.14641376495362124,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9800109481811603,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.1284464556183043,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.705963429629399,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.703916807367335,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.367473782849065,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.2148027667312284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.783763197617066,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3242852347237726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9535718645368298,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2684867008150049,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7053609135701384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6188085574914926,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.990102031443378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5626802543077543,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8120259707153316,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.7699966430664062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.3899993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.862568254398526,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.403141311592451,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.427167469253002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.14579360608567,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.472346832658249,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.152742280276358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.4559129173057386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.012855724992586914,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.1564595809106795,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.2135709440500038,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.2525955771698145,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.556805052414703,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.347438307488316,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.250536552985361,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.3874578292012245,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.217264728091873,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18999996185301882,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.5314994812011662,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.079720840454101,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5456893157958973,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.10282611846923828,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5577004623413089,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.409824453756849,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.959722439245374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.403795603457894,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.596116620439128,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.967531118297774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.258212637211045,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.11071395874023438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.055713653564453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.24849865931268278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1584101556783457,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.9560079632490197,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.9560079632490197,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5987269432164768,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.598394110138448,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0500030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.5400009155273438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.613265118160457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6434165365613929,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6577912346267265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0054690376797737,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1840843357528552,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.452982714734665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1870255827899365,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.551764733088079,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.319373791648304,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.8329869041038402,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.832363126709913,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.59445759135074,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.308992860922787,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.355188442025661,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.2554806708944506,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.756173736187366,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18400001525878906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7389999389648452,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.005654296874993747,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.06593360900879475,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.01923492431640028,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.06279024124145138,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5528708941475289,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4126229280137403,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.8691070184360559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.874551964543648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.927255621273205,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.759127916831061,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.012499945504324872,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.04749979291643425,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.002540334492149965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.04830618262438713,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.799383853606984,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.6390902172149455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.11007747023692538,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.625144424692725,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.3100128173828125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.75,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.9845976976407673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.04152653742204304,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.041635971678566364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.479106045191525,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2711665999920796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8490455937431807,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0447415745635027,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.1953147303798257,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.690706371128614,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1480438301204043,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1329359204046208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.068094598862492,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.3960751251620116,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.751251321034177,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1131966626680168,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.0090942727194605,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.019499969482410506,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.0574996948242017,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.20113708496094773,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.3153167724609318,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.026211700439461083,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.15487182617187045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.3860187616631103,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.670232690487694,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.4723582840723837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.3661237963914283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.323609846357876,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.5063817500743482,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07428632463727691,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1092878069196428,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.021440919248991053,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.03808136364049086,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2418751347376578,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.4784145762437149,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.24537044883696946,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.3187789425696125,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.269989013671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.32000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5970325626272976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.14604263579968135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.15059628263620617,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9008167752053042,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.9522789058743726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.611622966502993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0013451943945437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.131711794745959,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.8909238891394509,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.043527731742766,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0239756094469805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.4898053288762707,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.17262961929555942,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.51382869379399,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.06710989370997034,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.336120797845245,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8615005493163892,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.6755004882812443,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.21291503906249432,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1243353271484295,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.14781082153319858,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6789463043213004,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6663699664719136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8543525663154528,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.2897713674256286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.405513418384575,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.28089410424407646,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.8801616596836332,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.08214351109095963,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.16285814557756684,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.04185064756719137,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.038366997500002276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.14604263579968135,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9681351019051876,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6304639815796242,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5996689211653303,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.410003662109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.8700027465820312,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.17062044402404997,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9167408538151798,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.9485557687864086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.4028567759353248,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0410914684741535,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.177197446037041,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6549608815038086,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.30827966892997,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.1232708824881033,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.106311221357627,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.123127660869596,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.991845329606292,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1659999936440855,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.079403173328037,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.7234159696083227,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 8.512688672029256,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4895000457763672,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9034999847412166,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.10803695678710312,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.34214385986328466,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0500847244262701,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.22468997955321868,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0417310343808772,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0298583262102756,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5332853801994561,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.973463607962823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.621965027841953,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.1485087840102945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.03999982561383919,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1264277866908481,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.018506140501566737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.08946450353300639,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6334033874376921,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.255804897750935,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.312942970628207,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6777564369303435,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.7800064086914062,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.9000015258789062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.1151149405087897,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.3837910448811996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.39735518967814,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.5880001234661396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1568273626017653,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.1839147679870496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8867641977544749,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.15838793706912657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.8212236139966365,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.573361412423647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.5719270817613267,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.176988677137106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.2817358877716964,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.086120495278045,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.955219285858989,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.362796940168412,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.38700027465820597,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6630001068115234,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.007987365722655682,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.0918264770507875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.01890956878662564,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.1687559127807674,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.0953674164293945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9376844444686014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.4498487834947236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.528824377663531,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.430883379257587,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.532371677707924,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.21892929077148438,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.33321435110909614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.14978664158674082,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.23502024972127078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.3244862371948005,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.260963659508809,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2059707798749486,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6974733980507335,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.589996337890625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6546970694090168,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.9336749915032536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.8601265039966952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.21118246504356,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7240896944877182,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.576424218993047,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.26793806459273206,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.842038937200456,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3608057428968636,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.123245359045701,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.034698396079882,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.800171018714527,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4008188306822138,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.6742184917020513,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.3363931526972461,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.6376299341011702,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5674999237060661,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.311000061035159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.21548110961914801,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8957568359375045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.07450103759765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.3591181182861334,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8187790541941862,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.3085958627441432,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5026757888479292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.4955219348288704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3796518582569579,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.9026342072461455,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.008571624755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.12142835344587066,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.015359244084707457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.18195730157084666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3137260220928635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.1285371136301823,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1139427237420989,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.09569669718976037,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.23999786376953125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1199989318847656,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.1196236025359454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5761097373836233,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5880245950414364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.24497770093578897,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.21852577934906492,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8492934208910157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.022482056213801727,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.227054575885425,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.4135149290480986,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7656801049260706,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7625964871246231,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.3440108527351775,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.343434304518997,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.7514991481820115,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0909371443183158,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 9.431463578984712,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18499984741210795,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8474998474121094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02424369812011662,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.03166450500488338,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.004758281707758272,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.026251354217528444,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.11502570437944559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5851692821505328,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5154872865801963,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.7666388069145897,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.537069120894007,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.4983610768952946,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.021785736083984375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.019642421177455405,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.057832220775051235,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.08269393033383077,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.545616199235166,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.8385987067442344,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.03362759050265085,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6611916637477466,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.470001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8400001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.8332718402488393,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5484363763283762,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.5531775183158949,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.7491685258589786,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5197951359830153,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.7960309198404207,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.6865328962354145,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.07482669742104,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.46061948626331395,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7380067438708235,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.727749410399082,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8398200278119883,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.6447036611529473,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.6982366471314165,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7549879843399285,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.279235700520326,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.14850006103515767,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5014999389648409,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.021274337768559803,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.16590354919433992,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.014604854583744498,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.07062919616699759,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7534339638844978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7696101113882081,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1571979249504816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.369182368008649,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0640752487524718,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.79791232926223,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.009285790579659614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.003214154924665258,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.03743543626148904,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.036218491311547085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0448794942908064,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.1096088748687967,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.01086282966752039,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.042390486346639555,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.9299964904785156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.289997100830078,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.3635836650500277,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6269357029220277,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.6699998037974506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.613016161697069,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.48318055967568885,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.563313315233675,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.44177559643119313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.35307378522078103,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.06969233853787449,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.816506070464475,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.8445716958806373,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.2020047153680355,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.60808908484562,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.4655190425246705,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.5102306845357072,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.851335217878505,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.20849990844726562,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8939998626708956,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0075051879882792605,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.025649719238280966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.026654052734372158,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1122198295593293,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.4007530509836386,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.694215848879966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.81171394849875,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.44784731125496,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7778410339073902,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.287813687578046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.05142838614327572,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.06428555079868858,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.07376315869528449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.06508881346906703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.2805807258616242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.826247509964076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.7767446023601436,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9532350068455581,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -14.17999267578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -33.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.2616989774330705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.449127739102321,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.256664681615797,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.902934748761756,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.6682885109722747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.080769944808122,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.193957311668829,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.968081970710365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.967807650920917,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.2595573715598745,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.08209278953261,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.3139461950907894,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.5433799858023445,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.178564217517128,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.1255022235643146,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.76367296761108,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.2795013427735284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -19.004504394531295,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0421997070312727,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.5942016601562727,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.559499969482431,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.8097496032714844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.4944241671885798,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.7754538641979076,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.3144927715212607,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.399630629312613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.8348073409420915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.173582157366864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.719286237444198,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.6278512137276806,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.2536650205630311,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.74805274418341,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.236944648943396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.254771458540864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.0788982659183577,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.3035889000418761,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.3899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.489997863769531,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.1166683789171628,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.015081532949515,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.8229002383935224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.614435701713269,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.3091016594079097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.780271646151887,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.667720185895774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -18.542617222088907,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.17722294759499047,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.8255111654070677,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.6483283463103344,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.0254471480423,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.1841931342379777,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.87806591886089,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.59926509779126,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.338208218989623,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.3909999847412138,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.011500167846676845,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.02940002441405909,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5162001037597719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.010693550109863281,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.11698230743408544,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.852474108327396,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.706009711012486,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.2076250195024234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.377232680037661,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.5561822054950945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.24747277494873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.055714743477957906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.35142844063895096,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.12616056837906964,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.5859045922557891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.1212385093542947,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.422825967867297,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4750350061263051,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6556354375471198,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -10.199996948242188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -11.300003051757812,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.130983219251397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.577605966522493,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.542287179603912,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.21812399711871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.917190341067503,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.457618710537586,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.675883211832346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.8463215560479558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.42487454576355,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.388035598980046,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.367715287520725,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.629135443447742,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.792281815897571,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.55541298324659,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.607428123727832,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.050730559147242,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.305999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.129499053955072,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.09545501708984716,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.3780291748046807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3247364044189567,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7928930664062648,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.3272766827180735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.941523212353163,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.3799890117486315,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.676928279795447,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.233517477156525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.937408600573683,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.33714185442243316,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1871425083705356,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3017910955076615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.24157367987673561,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.979008551133813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.5159635937181655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.522340152853868,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.349088044091578,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -22.540008544921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.3699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.376325254690085,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.744965070681374,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.898671385805355,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.8094763591416205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -8.980303882049101,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.671608902098534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.777770188018748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.377926531125653,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.670216581202238,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -5.555394703138927,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.724099493722168,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -6.220487805470654,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.8553953568791695,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.7694031748075378,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.7093150999142344,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.826482471973633,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.28350067138671875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.465998840332077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.5259997558594023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.4139996337891034,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3095500183105173,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.1098999023437273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.677504497415608,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.8661602580801215,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.491439434283429,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.9839860783945626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.7445332955546435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.8986897960290534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0771440778459827,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0407191685267865,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.4412650833505025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.36755775140846847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.1628588662276815,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.0624388493297072,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.24315959089145256,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4600898590378233,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.9399871826171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.519989013671875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.483147834897538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.08253143905379012,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.08355929800394346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.918829406806912,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.781711425979716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.723696723942772,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7177860006663224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8249234227457585,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.189256508385385,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1070389284886573,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.0910125940792437,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.507817960477878,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.906619951149648,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 7.6259024512337685,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.7862410887708364,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.379485580353528,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.3849998474121321,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6695014953613452,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.44770385742188523,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.406244812011721,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.12962753295900598,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.6588719940185683,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.197712431397836,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.3081860229807747,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.5106993648445264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 5.025129875484469,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.214348064181449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.552337692966356,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.16785648890903992,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7149985177176337,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02590369651973745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.26172103305095895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.9531291711760055,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.973187857897276,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.28578316494748224,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.031029997130868514,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.220001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.6000003814697266,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.1337062516039627,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.8444047902970384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.8211740222939032,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.4549302094532655,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -1.3055641221997654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.224352489836679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.960008793567372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.309391505575062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.8398149250918094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.654834422754591,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6466021302107161,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.8659416557822985,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.18065559702983336,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.3221467625456835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.891553705462858,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -7.104982502475776,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.16700000762939382,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.46949996948242045,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.07360000610351847,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.3299999618530265,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.02510000228881637,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.09299998283385946,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.19297540611145125,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.4781516155676351,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.4764458087400003,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.9121616517416937,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.6068771704345934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.582962913920527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.03100000108991352,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.09800025394984657,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.12564897400843655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.3829592084104432,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.63109930249915,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -1.7211714600244736,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.737546307366079,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1795666963223241,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.720001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.555177581960678,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 2.0159334919498173,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.9959764658523893,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.635160075769517,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.0072140573154993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.6549904776073543,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.61763154032314,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1303526215123316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.2612862554485247,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 3.2055038594922647,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.1705483579355764,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -2.04617152209855,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 4.132122582485431,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 4.55719620489835,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 3.686086628427654,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 6.334761624611618,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1670001983642635,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.6450004577636719,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.014120941162104828,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.26749404907226904,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.03330289840697276,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.1671340942382784,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.1893598516955937,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.4678601998747256,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.4156422889685336,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.7690685067717205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.3954771999473934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.1748854799014996,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.0510711669921875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.09892763410295768,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.02622741403754203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.11029224173137808,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 2.2196811253851427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 1.2905113663103993,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1257601127068455,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.49193636312219524,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -5.220001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -15.30999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.302145686147072,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -4.760983117186712,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.478171966565282,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -14.46401050816164,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -4.0245952722123395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -13.5575503460467,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -7.133355728564805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -19.820545209127783,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.008254359634918718,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -3.571412749644265,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.303600074482094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.875021954490673,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.8996867470424075,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -10.655344618755702,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -6.064900640460291,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -14.616136206028497,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.7644996643066406,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.30849990844725994,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.13359985351564774,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.40180023193357783,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.1460500335693382,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.9289501190185661,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.691063657312509,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.985120261183921,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.091403693530559,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -9.549952415232577,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -3.9449062561638186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -12.054068145304253,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.10142953055245574,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7714298793247769,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.18079698436597624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.7777887567287847,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -2.9847339693066957,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -8.754072623948971,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 0.04986091512268631,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": 0.40375343197798963,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.05000000000000071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.13000000000000078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.18000000000000016,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.06000000000000005,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": 0.04999999999999993,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": 0.029999999999999916,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.040000000000000036,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.05999999999999961,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-29",
        "to": "2026-10-30",
        "change": -0.029999999999999805,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-23",
        "to": "2026-10-30",
        "change": -0.06000000000000005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 11,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.04999999999999982,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-26",
        "to": "2026-11-02",
        "change": -0.04999999999999982,
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
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": -0.034999847412109375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "latest.VIX.value",
    "available_prior_observations": 1,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-30",
        "to": "2026-11-02",
        "change": 1.7299995422363281,
        "unit": "index points"
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
| 事实指标引用 | ["prices.^VIX.value", "prices.^VIX3M.value", "macro.BAMLH0A0HYM2.value", "prices.^MOVE.value"] |
| 推断与解释 | 风险厌恶加深但并非全部板块同步恐慌；VIX期限未倒挂，信用最新可得仍走阔。 |
| 反证与缺口 | 金融等权上涨、油价下降；信用只有30日。 |
| 确认条件 | QQQ先收回683.45再690.49，SMH先511.63再522.49；下一常规时段低点抬升、有效VWAP回踩不破且收盘保持。再看QQQ699.43、SMH532.76本日高点，次日延续才升级；SPY同步收回755.72并守住。 |
| 失效条件 | QQQ680.33、SMH506.44或SPY751.60再破且反抽不回；突破后跌回开盘区间。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 条件式指导 | 按条件分步观察；确认失败保留现金，不用涨幅或高预测概率替代风险预算。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增11月2日完整收盘、ISM/SLOOS、融资文件及盘后财报；科技反弹由待确认降为失败，金融相对强度提高。 |

## 判断依据 · 反弹可靠吗？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹可靠吗？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct"] |
| 推断与解释 | 本日科技反弹失败；QQQ/SMH收于旧支持下，盘后反抽不足以改变评级。 |
| 反证与缺口 | RSP和XLF改善是最强反证；完整广度缺失。 |
| 确认条件 | QQQ先收回683.45再690.49，SMH先511.63再522.49；下一常规时段低点抬升、有效VWAP回踩不破且收盘保持。再看QQQ699.43、SMH532.76本日高点，次日延续才升级；SPY同步收回755.72并守住。 |
| 失效条件 | QQQ680.33、SMH506.44或SPY751.60再破且反抽不回；突破后跌回开盘区间。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 条件式指导 | 按条件分步观察；确认失败保留现金，不用涨幅或高预测概率替代风险预算。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增11月2日完整收盘、ISM/SLOOS、融资文件及盘后财报；科技反弹由待确认降为失败，金融相对强度提高。 |

## 判断依据 · 哪些板块优先？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 哪些板块优先？ |
| 事实指标引用 | ["prices.XLF.return_1d_pct", "prices.XLI.return_1d_pct", "prices.XLP.return_1d_pct", "prices.SMH.return_5d_pct"] |
| 推断与解释 | 金融/工业/必需消费和军工优先观察承接，芯片/云/能源等待新确认。 |
| 反证与缺口 | 当期净申赎缺失，不能把相对强势称主力流入。 |
| 确认条件 | XLF57.20附近突破位回踩承接、日低56.87不破，RSP先收回220.23再看220.95；行业继续相对SPY强且收盘守位。XLI/XLP/ITA使用各自下一交易日开盘区间，不伪造尚未形成的价格。 |
| 失效条件 | XLF跌破56.87反抽不回、RSP219.51失守；行业同步转弱或信用压力扩大。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 条件式指导 | 按条件分步观察；确认失败保留现金，不用涨幅或高预测概率替代风险预算。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增11月2日完整收盘、ISM/SLOOS、融资文件及盘后财报；科技反弹由待确认降为失败，金融相对强度提高。 |

## 判断依据 · AI需求与回报如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与回报如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 投入承诺增长与现金、稀释压力同时存在；PLTR强指引不阻止盘后下跌。 |
| 反证与缺口 | H100租价并未崩塌、融资仍可进行。 |
| 确认条件 | PLTR收回178.34常规收盘、AAPL收回338.32，并在常规回踩后守住；IGV先收103.33且相对QQQ改善。下一开盘区间形成后再定失效，不把盘后短暂上涨当信号。 |
| 失效条件 | 财报后开盘低点失守、反抽缩量而下跌持续；指引成本压力扩大。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 条件式指导 | 按条件分步观察；确认失败保留现金，不用涨幅或高预测概率替代风险预算。 |
| 主观置信等级 | medium |
| 判断变化原因 | 新增11月2日完整收盘、ISM/SLOOS、融资文件及盘后财报；科技反弹由待确认降为失败，金融相对强度提高。 |

## AI融资与现金回报 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Oracle股债各100亿美元初步文件、Anthropic多年算力承诺；META新增股权结构说明。 |
| 事实：市场反应 | MSFT−2.83%、GOOGL−0.30%、META−1.34%，AMZN+2.20%，云SKYY−3.27%。 |
| 推断：解释 | 推断：投资者更关注投入能否转成现金回报；同产业公司表现分化。 |
| 受益篮子 | ["现金回收可验证的软件/基础设施"] |
| 受损篮子 | ["融资依赖、股权稀释与高估值篮子"] |
| 反证 | H100价格与云需求并未全面崩塌，融资市场仍可进入。 |
| 下一催化剂 | AMD财报、微软4日计划结算、下一次现金流披露 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm", "https://www.sec.gov/Archives/edgar/data/1341439/000119312526442729/d181425d424b5.htm", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026068935/meta-20261102.htm", "https://www.silicondata.com/products/silicon-index/h100"] |

## 芯片存储反弹失败 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 盘前反抽后收盘继续破位；光通信并购从谈判升级为正式协议。 |
| 事实：市场反应 | SMH−2.71%、MU−5.78%、SNDK−6.59%、DRAM−3.52%，均未守住晚报关键支持。 |
| 推断：解释 | 推断：抛压未消化；不把并购规模等同需求立即增长，也不将全部跌幅归因中国竞争。 |
| 受益篮子 | ["等待确认的高质量芯片"] |
| 受损篮子 | ["高弹性存储、杠杆半导体"] |
| 反证 | 盘后小幅修复、业务需求仍增长，但需要下一常规时段验证。 |
| 下一催化剂 | 3日AMD、5日LITE、17日NVDA |
| 证据 | ["https://investor.lumentum.com/financial-news-releases/news-details/2026/Marvell-and-Lumentum-to-Combine-Creating-a-Category-Leader-in-AI-Connectivity/default.aspx", "https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm"] |

## 金融工业与必需消费相对强 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 制造业扩张与贷款调查分化，指数内部轮动。 |
| 事实：市场反应 | XLF+1.86%、XLI+1.38%、XLP+1.58%、RSP+0.76%。 |
| 推断：解释 | 推断：部分非科技资产承接，不能判定全市场恐慌；也不能用19ETF代替成分广度。 |
| 受益篮子 | ["XLF", "XLI", "XLP", "ITA"] |
| 受损篮子 | ["弱势科技追涨"] |
| 反证 | 信用利差滞后走阔、小企业贷款标准更紧，金融上涨不消除信用风险。 |
| 下一催化剂 | 3日JOLTS、中期选举结果、4日ISM服务业 |
| 证据 | ["https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/october/", "https://www.federalreserve.gov/data/sloos/sloos-202610.htm"] |

## 油价下跌与能源破位 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 外交表态与袭击消息互相冲突，实际霍尔木兹恢复尚未证实。 |
| 事实：市场反应 | XLE−3.96%、XOP−5.01%、OIH−5.48%；原油大跌。 |
| 推断：解释 | 推断：供给溢价消退或需求预期变化压制能源，不因地缘新闻多就追多。 |
| 受益篮子 | ["成本受益的运输与部分消费企业（需另验个股）"] |
| 受损篮子 | ["油气生产与油服"] |
| 反证 | 新增供应中断可以逆转油价；实际通航需Portwatch，口头承诺不足。 |
| 下一催化剂 | 官方外交、航运与油价/能源共同止跌 |
| 证据 | ["https://www.opec.org/pr-detail/620-1-november-2026.html", "https://www.ukmto.org/ukmto-products/warnings"] |

## 强财报不保证股价承接 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | PLTR上调全年指引；AppleQ4收入1145亿美元、EPS2.10含0.05关税退款。 |
| 事实：市场反应 | PLTR收178.34，本次盘后约172.51；Apple收338.32，盘后约328.92。均为实际分钟报价，异步且非最终盘后收盘。 |
| 推断：解释 | 推断：预期、估值、成本和仓位结构影响价格反应，需等开盘回踩而非只看beat。 |
| 受益篮子 | ["未来能守住财报后低点的软件/消费科技"] |
| 受损篮子 | ["单纯追财报headline的高估值标的"] |
| 反证 | PLTR指引强、Apple收入增长，不能据盘后下跌断言经营衰退。 |
| 下一催化剂 | 3日常规时段承接与AMD指引 |
| 证据 | ["https://www.sec.gov/Archives/edgar/data/1321655/000132165526000045/a2026q3ex991pressrelease.htm", "https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/"] |

## 增长、通胀与政策事件窗口 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | ISM扩张但价格高，SLOOS部分信贷收紧；财政部下调季度净借款估计至6180亿美元。 |
| 事实：市场反应 | VIX上升、黄金上涨；等权金融强而科技弱。 |
| 推断：解释 | 推断：政策与折现率风险尚未消退，单一恐慌/过热标签不足。 |
| 受益篮子 | ["有现金回报且能承接的篮子"] |
| 受损篮子 | ["融资敏感与事件前追涨"] |
| 反证 | 油价大跌降低通胀压力；借款下调部分来自期初现金，不等于结构性财政改善。 |
| 下一催化剂 | 3日选举/JOLTS、4日再融资公告、6日非农、10日CPI |
| 证据 | ["https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/october/", "https://www.federalreserve.gov/data/sloos/sloos-202610.htm", "https://home.treasury.gov/news/press-releases/sb0675/"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AAPL | 328.92 | -2.78 | 2026-11-02T23:52:28+00:00 | 2026-11-02T23:52:28+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| AMD | 473.79 | 1.49 | 2026-11-02T23:52:04+00:00 | 2026-11-02T23:52:04+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| AMZN | 246.82 | 0.48 | 2026-11-02T23:51:48+00:00 | 2026-11-02T23:51:48+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| AVGO | 323.64 | 0.44 | 2026-11-02T23:52:22+00:00 | 2026-11-02T23:52:22+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| BABA | 101.90 | 0.39 | 2026-11-02T23:45:08+00:00 | 2026-11-02T23:45:08+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| CAT | 614.41 | 0.13 | 2026-11-02T23:50:26+00:00 | 2026-11-02T23:50:26+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| CEG | 258.00 | 0.29 | 2026-11-02T23:47:19+00:00 | 2026-11-02T23:47:19+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| COIN | 137.60 | -0.17 | 2026-11-02T23:51:13+00:00 | 2026-11-02T23:51:13+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| CVX | 228.65 | 0.39 | 2026-11-02T23:29:00+00:00 | 2026-11-02T23:29:00+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| DRAM | 47.18 | 1.86 | 2026-11-02T23:48:17+00:00 | 2026-11-02T23:48:17+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| GEV | 867.37 | 0.59 | 2026-11-02T23:40:35+00:00 | 2026-11-02T23:40:35+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| GLD | 361.69 | 0.01 | 2026-11-02T23:51:58+00:00 | 2026-11-02T23:51:58+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| GLW | 124.23 | 0.84 | 2026-11-02T23:49:55+00:00 | 2026-11-02T23:49:55+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| GOOGL | 280.15 | 0.42 | 2026-11-02T23:52:15+00:00 | 2026-11-02T23:52:15+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| IGV | 102.12 | 0.22 | 2026-11-02T23:14:10+00:00 | 2026-11-02T23:14:10+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| ILMN | 226.58 | 0.00 | 2026-11-02T21:33:54+00:00 | 2026-11-02T21:33:54+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| INTC | 60.50 | 0.88 | 2026-11-02T23:52:21+00:00 | 2026-11-02T23:52:21+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| IWM | 279.50 | 0.13 | 2026-11-02T23:45:01+00:00 | 2026-11-02T23:45:01+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| LITE | 688.20 | 0.56 | 2026-11-02T23:51:35+00:00 | 2026-11-02T23:51:35+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| LLY | 1,410.99 | 0.00 | 2026-11-02T23:36:39+00:00 | 2026-11-02T23:36:39+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| META | 609.80 | 0.51 | 2026-11-02T23:51:04+00:00 | 2026-11-02T23:51:04+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| MRVL | 174.50 | 1.80 | 2026-11-02T23:51:20+00:00 | 2026-11-02T23:51:20+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| MSFT | 509.00 | 0.37 | 2026-11-02T23:52:07+00:00 | 2026-11-02T23:52:07+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| MU | 842.67 | 1.09 | 2026-11-02T23:52:20+00:00 | 2026-11-02T23:52:20+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| NOW | 106.40 | 0.37 | 2026-11-02T23:50:34+00:00 | 2026-11-02T23:50:34+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| NVDA | 203.84 | 0.88 | 2026-11-02T23:52:07+00:00 | 2026-11-02T23:52:07+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| NXPI | 257.54 | 0.12 | 2026-11-02T21:31:00+00:00 | 2026-11-02T21:31:00+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| ORCL | 119.94 | 0.60 | 2026-11-02T23:51:10+00:00 | 2026-11-02T23:51:10+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| PLTR | 172.51 | -3.27 | 2026-11-02T23:52:05+00:00 | 2026-11-02T23:52:05+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| QQQ | 682.98 | 0.28 | 2026-11-02T23:52:16+00:00 | 2026-11-02T23:52:16+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| RSP | 220.80 | 0.37 | 2026-11-02T23:41:48+00:00 | 2026-11-02T23:41:48+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| SMH | 513.57 | 1.03 | 2026-11-02T23:51:11+00:00 | 2026-11-02T23:51:11+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| SNDK | 1,094.30 | 1.79 | 2026-11-02T23:51:56+00:00 | 2026-11-02T23:51:56+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| SPY | 753.31 | 0.16 | 2026-11-02T23:49:40+00:00 | 2026-11-02T23:49:40+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| STX | 598.15 | 0.74 | 2026-11-02T23:42:18+00:00 | 2026-11-02T23:42:18+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| TLT | 81.60 | -0.16 | 2026-11-02T23:41:26+00:00 | 2026-11-02T23:41:26+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| VRT | 226.30 | 0.92 | 2026-11-02T23:45:52+00:00 | 2026-11-02T23:45:52+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| XLE | 67.55 | 0.45 | 2026-11-02T23:49:21+00:00 | 2026-11-02T23:49:21+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |
| XLF | 57.59 | 0.05 | 2026-11-02T23:29:48+00:00 | 2026-11-02T23:29:48+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| XLI | 169.71 | -0.00 | 2026-11-02T22:51:00+00:00 | 2026-11-02T22:51:00+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| XLV | 184.59 | -0.00 | 2026-11-02T23:31:06+00:00 | 2026-11-02T23:31:06+00:00 | 2026-11-02T23:52:31.294817+00:00 | stale |
| XOM | 180.00 | 0.18 | 2026-11-02T23:41:19+00:00 | 2026-11-02T23:41:19+00:00 | 2026-11-02T23:52:31.294817+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 752.10 | USD_per_share | 2026-11-02 | -0.48 | -1.73 | -2.93 | ok |
| QQQ | 681.09 | USD_per_share | 2026-11-02 | -1.36 | -4.37 | -9.93 | ok |
| IWM | 279.14 | USD_per_share | 2026-11-02 | -0.07 | 0.78 | -1.50 | ok |
| RSP | 219.98 | USD_per_share | 2026-11-02 | 0.76 | 1.24 | 4.20 | ok |
| GLD | 361.65 | USD_per_share | 2026-11-02 | 1.65 | -1.68 | -4.72 | ok |
| GC=F | 3,955.70 | USD_per_troy_ounce | 2026-11-02 | 1.46 | -2.05 | -4.84 | ok |
| CL=F | 96.35 | USD_per_barrel | 2026-11-02 | -7.46 | -5.32 | 7.74 | ok |
| BZ=F | 104.32 | USD_per_barrel | 2026-11-02 | -11.32 | -9.92 | 3.99 | ok |
| TLT | 81.73 | USD_per_share | 2026-11-02 | -0.13 | 0.06 | 5.99 | ok |
| UUP | 28.96 | USD_per_share | 2026-11-02 | -0.14 | -0.17 | -0.10 | ok |
| HYG | 76.89 | USD_per_share | 2026-11-02 | -0.70 | -0.40 | -0.12 | ok |
| LQD | 103.71 | USD_per_share | 2026-11-02 | -0.54 | -0.30 | 1.85 | ok |
| ^VIX | 21.15 | index | 2026-11-02 | 8.91 | 15.01 | 36.28 | ok |
| ^VIX3M | 21.60 | index | 2026-11-02 | 3.95 | 8.32 | 20.00 | ok |
| ^VVIX | 110.47 | index | 2026-11-02 | 3.80 | 8.91 | 29.27 | ok |
| ^MOVE | 100.36 | index | 2026-11-02 | 0.16 | -1.79 | -6.46 | ok |
| NVDA | 202.06 | USD_per_share | 2026-11-02 | -1.26 | -6.45 | -15.42 | ok |
| MSFT | 507.12 | USD_per_share | 2026-11-02 | -2.83 | -4.78 | -3.44 | ok |
| AMZN | 245.63 | USD_per_share | 2026-11-02 | 2.20 | -1.39 | -2.30 | ok |
| GOOGL | 278.99 | USD_per_share | 2026-11-02 | -0.30 | -11.93 | -19.48 | ok |
| META | 606.73 | USD_per_share | 2026-11-02 | -1.34 | -3.78 | -18.22 | ok |
| CRWV | 50.15 | USD_per_share | 2026-11-02 | -8.60 | -9.13 | -42.61 | ok |
| MU | 833.59 | USD_per_share | 2026-11-02 | -5.78 | -7.76 | -21.64 | ok |
| DRAM | 46.32 | USD_per_share | 2026-11-02 | -3.52 | -4.16 | -24.89 | ok |
| VRT | 224.24 | USD_per_share | 2026-11-02 | -3.55 | 12.24 | -11.58 | ok |

## 跨资产风险解释

判断：风险厌恶加深且行业分化，不是全面过热，也没有足够证据确认系统性挤兑。11月2日VIX21.15、VIX3M21.60，同日比值约0.979，仍未倒挂；VVIX110.47、MOVE100.36。FRED最新30日2年4.56%、10年4.94%、实际10年2.60%，HY344bp、IG94bp，分别较上期29日326/89bp再走阔18/5bp；不是2日当日利差。2日盈亏平衡通胀2.29%，GPR97.67、7日均137.64；金融压力仍23日−0.5837。黄金GLD+1.65%与科技下跌相伴，原油下跌未带来科技收盘修复。盘后连续WTI约96.33、Brent104.32，但Brent日线与新闻结算口径/换月不一致，不采用连续日线−11.32%解释同一合约日跌幅。tc转述WTI12月结算96.46（−7.36%）仅作标明合约的新闻线索，当前连续报价另列。官方ISM制造业55.5、订单55.5、生产59、价格75.2（较前月−2.7点），增长仍扩张而成本仍高；SLOOS显示大型C&I标准基本不变、小企业及CRE更紧，C&I与CRE需求偏弱。通胀与融资压力并存，不简单归为衰退。联邦基金最近已核验区间3.75–4.00%；本次没有新政策决定。CME页面超时，tc加息74.9%未独立核验，不替代为官方数值。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.56 | percent | 2026-10-30 | -0.22 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.44 | percentage_points | 2026-10-30 | 0.34 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.94 | percentage_points | 2026-10-30 | 0.09 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 4.94 | percent | 2026-10-30 | -0.30 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.60 | percent | 2026-10-30 | -0.28 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.29 | percent | 2026-11-02 | -0.07 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.58 | index | 2026-10-23 | 0.28 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 19.42 | index | 2026-10-30 | 4.11 | lagged | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| GPRD | 97.67 | index | 2026-11-02 | -213.94 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_ACT | 113.60 | index | 2026-11-02 | -291.60 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_THREAT | 94.75 | index | 2026-11-02 | -209.43 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA7 | 137.64 | index | 2026-11-02 | -46.66 | ok | https://www.matteoiacoviello.com/gpr.htm |
| GPRD_MA30 | 164.04 | index | 2026-11-02 | -2.33 | ok | https://www.matteoiacoviello.com/gpr.htm |

## CNN Fear & Greed

缺失：CNN 无可核验数据，不使用替代指数

## 19 板块与主题 ETF：价格量能证据

| 标的 | 板块 | 1日% | 5日% | 20日% | 相对SPY 1日pp | 相对SPY 5日pp | 相对SPY 20日pp | 成交量/前20日 | 观测日 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| XLK | 科技 | -2.95 | -6.49 | -13.29 | -2.47 | -4.76 | -10.36 | 1.65 | 2026-11-02 |
| XLE | 能源 | -3.96 | -3.43 | 5.99 | -3.48 | -1.70 | 8.92 | 1.61 | 2026-11-02 |
| XLF | 金融 | 1.86 | 2.75 | 6.83 | 2.34 | 4.48 | 9.76 | 1.26 | 2026-11-02 |
| XLI | 工业 | 1.38 | 1.65 | -0.23 | 1.86 | 3.38 | 2.70 | 1.21 | 2026-11-02 |
| XLV | 医疗 | -0.15 | 2.97 | 10.29 | 0.33 | 4.70 | 13.23 | 1.50 | 2026-11-02 |
| XLP | 必需消费 | 1.58 | 3.26 | 12.08 | 2.06 | 5.00 | 15.01 | 1.65 | 2026-11-02 |
| XLY | 可选消费 | 2.41 | 3.41 | 7.01 | 2.89 | 5.15 | 9.94 | 1.64 | 2026-11-02 |
| XLC | 通信 | 0.36 | -3.46 | -10.17 | 0.84 | -1.72 | -7.24 | 1.34 | 2026-11-02 |
| XLU | 公用事业 | 0.55 | 2.63 | 9.26 | 1.03 | 4.37 | 12.19 | 1.05 | 2026-11-02 |
| XLRE | 房地产 | 1.09 | 1.96 | 7.30 | 1.57 | 3.70 | 10.24 | 1.12 | 2026-11-02 |
| XLB | 材料 | 1.76 | 4.46 | 8.42 | 2.24 | 6.19 | 11.36 | 1.79 | 2026-11-02 |
| SMH | 半导体 | -2.71 | -6.15 | -19.81 | -2.23 | -4.42 | -16.88 | 0.91 | 2026-11-02 |
| IGV | 软件 | -2.29 | -8.52 | -7.13 | -1.81 | -6.79 | -4.19 | 1.38 | 2026-11-02 |
| XOP | 油气开采 | -5.01 | -5.52 | 3.27 | -4.53 | -3.78 | 6.20 | 2.22 | 2026-11-02 |
| OIH | 油服 | -5.48 | -3.32 | -1.44 | -5.00 | -1.59 | 1.50 | 1.26 | 2026-11-02 |
| ITA | 航空与国防 | 2.36 | 3.63 | 3.72 | 2.83 | 5.36 | 6.65 | 1.18 | 2026-11-02 |
| ARKX | 航天主题 | -0.74 | -1.99 | -10.15 | -0.26 | -0.25 | -7.22 | 1.69 | 2026-11-02 |
| KRE | 区域银行 | 2.39 | 1.37 | 4.74 | 2.87 | 3.11 | 7.68 | 1.33 | 2026-11-02 |
| SKYY | 云计算 | -3.27 | -9.01 | -9.00 | -2.79 | -7.28 | -6.07 | 1.05 | 2026-11-02 |

## 资金证据分层

19个ETF全部以10月30日至11月2日同端点比较：XLY 118.16（日+2.41%，5交易日+3.41%）；KRE 73.73（日+2.39%，5交易日+1.37%）；ITA 214.68（日+2.36%，5交易日+3.63%）；XLF 57.56（日+1.86%，5交易日+2.75%）；XLB 53.67（日+1.76%，5交易日+4.46%）；XLP 90.83（日+1.58%，5交易日+3.26%）；XLI 169.71（日+1.38%，5交易日+1.65%）；XLV 184.60（日-0.15%，5交易日+2.97%）；XLK 174.22（日-2.95%，5交易日-6.49%）；SMH 508.31（日-2.71%，5交易日-6.15%）；IGV 101.90（日-2.29%，5交易日-8.52%）；SKYY 154.55（日-3.27%，5交易日-9.01%）；XLE 67.25（日-3.96%，5交易日-3.43%）；XOP 193.56（日-5.01%，5交易日-5.52%）；OIH 389.03（日-5.48%，5交易日-3.32%）。RSP+0.76%而SPY−0.48%，金融与等权扩散改善，但芯片/云仍弱，反弹不是普涨。优先观察XLF/XLI/XLP及军工能否连续守位，医疗仅相对抗跌；半导体等待破位收回，能源等待油价和股价同步止跌。XOP量/前20日均量约2.22，但下跌放量不等于可识别的主力净卖出。ICI重查仍为27日发布、截至21日周，全ETF净发行458.21亿美元，国内股票278.23亿、债券95.67亿；与本日价格轮动分开。VanEck页面仍30日NAV522.76、资产664.4亿，没有精确连续份额和拆分桥，不计算当日净申赎；机构持仓滞后，无法识别当日主力身份。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-11-02T23:57:50.367766+00:00：基础全领域采集并主动补查15组，覆盖政策/联储、通胀衰退、信用、AI/IPO/财报、航运油气、半导体、航天。CPI25、Meta76、Anthropic31、Congress88仅首10；基础inflation第二页SSL失败。OPEC命中OPEN为噪声，未采纳。PLTR EPS活跃合约已退出搜索，不列临近事件；11月2日伊朗合约期限已过、裁决仍未核验。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [8.75, {"status": "comparable", "change_pp": 2.1999999999999993}] | {"spread": 0.0049999999999999906, "volume24h_usd": 10392.444905999999, "liquidity_usd": 18581.62496, "quality_flags": [], "retrieved_at": "2026-11-02T23:52:37.747279+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["US x Iran ceasefire continues through November 30?", "指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [36.0, {"status": "comparable", "change_pp": -1.5000000000000013}] | {"spread": 0.020000000000000018, "volume24h_usd": 13843.325197999999, "liquidity_usd": 67036.2439, "quality_flags": [], "retrieved_at": "2026-11-02T23:52:37.747279+00:00", "contract_end_at": "2026-11-30T23:59:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "美国对伊朗直接合格军事行动的尾部风险，不含所有中东冲突"] | ["按规则核验实际行动，并看油价、信用及股票承接", "只有威胁或其他地域事件不能判定触发"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by November 30?", "11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [38.5, {"status": "comparable", "change_pp": 2.500000000000002}] | {"spread": 0.030000000000000027, "volume24h_usd": 453.656204, "liquidity_usd": 30257.5241, "quality_flags": ["volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-02T23:52:24.076287+00:00", "contract_end_at": "2026-11-30T20:59:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "沙特管线供应尾部风险，不能将所有中东威胁视为已命中"] | ["按规则核验官方事实，再验证资产价格和信用传导", "传闻、广义风险或股价变化不满足专门结算条件"] | [null, null] |
| ["Major CEX insolvent in 2026?", "2026年12月31日23:59ET前Binance/Coinbase/Bybit/OKX/Kraken任一被正式宣布资不抵债或申请/拟申请任一种破产程序则Yes；按官方代表或可信报道共识。被盗、暂停提款或偿付证明延期本身不是触发。", "https://polymarket.com/event/major-cex-insolvent-in-2026"] | [3.1, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.013999999999999999, "volume24h_usd": 1111.11, "liquidity_usd": 24184.21898, "quality_flags": [], "retrieved_at": "2026-11-02T23:52:27.611349+00:00", "contract_end_at": "2027-01-01T05:00:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "五家加密平台任一破产的专门合约，安全事故本身不触发"] | ["按规则核验官方事实，再验证资产价格和信用传导", "传闻、广义风险或股价变化不满足专门结算条件"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 96155.99616899999, "liquidity_usd": 299964.7218, "quality_flags": [], "retrieved_at": "2026-11-02T23:52:37.747279+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [92.05, {"status": "comparable", "change_pp": -0.9000000000000008}] | {"spread": 0.0010000000000000009, "volume24h_usd": 10323.683989, "liquidity_usd": 38167.30796, "quality_flags": [], "retrieved_at": "2026-11-02T23:52:26.488206+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["新增S-1/A仍不等于挂牌交易；上市窗口有参考性，未确认定价。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |
| ["Will Apple purchase memory CXMT chips in 2026?", "2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。", "https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147"] | [11.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.03, "volume24h_usd": 81.75, "liquidity_usd": 1343.0273, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"], "retrieved_at": "2026-11-02T23:52:26.874069+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "Apple采购/协议可能改变存储供应链，不证明HBM良率或AI利润已崩塌"] | ["公司官方采购/协议与量产、价格资料分别验证", "传闻或审批申请尚非已采购；没有交付不一定阻止本合约Yes"] | [null, null] |
| ["Will the Democratic Party control the Senate after the 2026 Midterm elections?", "2026选举后民主党控制参议院：过半席位，50比50按副总统党籍；独立议员依正式党团归属。计入规则指定常规/特别选举与后续决选；争议可等待新国会确定，非选举夜即必须结算。不直接代表法案或行业收益。", "https://polymarket.com/event/which-party-will-win-the-senate-in-2026"] | [75.5, {"status": "comparable", "change_pp": 3.0000000000000027}] | {"spread": 0.010000000000000009, "volume24h_usd": 1169310.3967620004, "liquidity_usd": 1994978.0198, "quality_flags": [], "retrieved_at": "2026-11-02T23:52:27.694070+00:00", "contract_end_at": "2026-11-04T04:59:00+00:00"} | ["同规则当前报价与价差见合约卡；结合独立官方事实，预测价格不是客观概率。", "参议院控制权关系政策可能性，不能当具体法案通过概率"] | ["按规则核验官方事实，再验证资产价格和信用传导", "传闻、广义风险或股价变化不满足专门结算条件"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will AMD (AMD) beat quarterly earnings?", "AMD下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定1.97美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。", "https://polymarket.com/event/amd-quarterly-earnings-nongaap-eps-11-03-2026-1pt97"] | [76.0, {"status": "comparable", "change_pp": -7.9999999999999964}] | {"spread": 0.26, "volume24h_usd": 566.940954, "liquidity_usd": 281.8248, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-11-02T23:52:24.048044+00:00", "contract_end_at": "2026-11-03T22:00:00+00:00"} | ["AMD盘口63/89、价差26个百分点，成交稀疏，中间价76%信息质量低；固定EPS门槛不是当前共识。", "AMD下一次财报检验AI芯片需求、利润和指引，EPS过线不等于股价上涨。"] | ["官方主要non-GAAP EPS按固定阈值核验，再看订单、现金和财报后价格。", "EPS过线但指引/价格承接失败，不能当作买入依据。"] | ["2026-11-03T17:00:00-05:00", "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"] |

## US x Iran ceasefire continues through November 2?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 6369333 |
| Yes 概率 % | 95.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.25, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.7000000000000015} |
| 24h成交量 / 流动性 USD | [298009.42591399996, 58802.3995] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-03T04:59:00+00:00 |
| 结算规则摘要 | 指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。 |
| 规则指纹 | 9b8785d047097fb1a2f6691d76f44da8472e9f99ec1707edac4350b22b4d6259 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 72.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.0, -2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.0000000000000018} |
| 24h成交量 / 流动性 USD | [233157.226891, 346183.9839] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:47:59.731326Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [96155.99616899999, 299964.7218] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:49:59.332425Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## US x Iran ceasefire continues through November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4713483 |
| Yes 概率 % | 36.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.5, -2.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -1.5000000000000013} |
| 24h成交量 / 流动性 USD | [13843.325197999999, 67036.2439] |
| 价差 pp | 2.00 |
| 到期 | 2026-11-30T23:59:00+00:00 |
| 结算规则摘要 | 指定日期伊朗标准时间23:59前美国发起、直接命中伊朗陆地/内水的合格空袭或地对地导弹攻击则No，否则Yes。威胁、拦截残骸、网络攻击、伊朗领海外海行动等不算；冲突报道最多等待三完整日综合裁决。与10月31日版本到期不同，不拼接概率。 |
| 规则指纹 | 2f10f9c94ec72b4835bbb7166be00ea0e23e8f953e2f04a18c6d8cb64275e844 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 8.75 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.95, -0.8] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.1999999999999993} |
| 24h成交量 / 流动性 USD | [10392.444905999999, 18581.62496] |
| 价差 pp | 0.50 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 9.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-7.5, -3.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -7.000000000000001} |
| 24h成交量 / 流动性 USD | [6559.7724, 17215.2721] |
| 价差 pp | 2.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [86.956522, 8651.4823] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:37.747279+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Military action against Saudi Oil Pipeline (East-West) by November 30?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401796 |
| Yes 概率 % | 38.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, -11.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 2.500000000000002} |
| 24h成交量 / 流动性 USD | [453.656204, 30257.5241] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-30T20:59:00+00:00 |
| 结算规则摘要 | 11月30日23:59利雅得时间前，合格空袭或地对地导弹（含指定单向攻击无人机）直接命中沙特东西输油管或泵站则Yes；不要求已证明显著损害。拦截残骸、小型短程弹药、地面入侵、炮火、网络攻击或未执行威胁不算。官方沙特信息与可信报道共识，冲突可等待三完整日。不同期限不拼接。 |
| 规则指纹 | de6f019a1972387984a02c6a8e7cef39e331ff99c1895cf1bba902450d550441 |
| 质量 | ["volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:24.076287+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 92.05 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [0.05, -1.95] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.9000000000000008} |
| 24h成交量 / 流动性 USD | [10323.683989, 38167.30796] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:26.488206+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## Will AMD (AMD) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1262633 / 6280962 |
| Yes 概率 % | 76.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [25.0, 21.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -7.9999999999999964} |
| 24h成交量 / 流动性 USD | [566.940954, 281.8248] |
| 价差 pp | 26.00 |
| 到期 | 2026-11-03T22:00:00+00:00 |
| 结算规则摘要 | AMD下一季度首次主要non-GAAP EPS四舍五入至美分后严格大于固定1.97美元才Yes；优先稀释EPS、官方财报，其次SeekingAlpha。公告日16点后96小时仍无non-GAAP则转GAAP（稀释优先），仍无为No；预定日后45天未披露亦No。除明显即时错误外不取后续重述。门槛固定于建约，不是最新一致预期，更非股价上涨概率。 |
| 规则指纹 | 45fb7613b172228eb6c9f337a9f40f9667816eecd866e1137e8b1f62ff7355e6 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-11-02T23:32:01.880215Z |
| 抓取时间 | 2026-11-02T23:52:24.048044+00:00 |
| 来源 | https://polymarket.com/event/amd-quarterly-earnings-nongaap-eps-11-03-2026-1pt97 |

## Will Apple purchase memory CXMT chips in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 652109 / 2745561 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.5, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [81.75, 1343.0273] |
| 价差 pp | 3.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Apple官方宣布使用/购买/采购CXMT存储器即可Yes，不要求同期交付；经确认达成采购或供货协议也可。官方信息优先、可信报道共识辅助。不等同HBM已量产或全球利润率下降。 |
| 规则指纹 | f9ba1bef2cbca87ceaec660e27ab85bc0edd5723bc3e5e58937caf9155b3e790 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown"] |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:26.874069+00:00 |
| 来源 | https://polymarket.com/event/will-apple-purchase-memory-cxmt-chips-in-2026-20260630171913147 |

## Will the Democratic Party control the Senate after the 2026 Midterm elections?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 32224 / 562793 |
| Yes 概率 % | 75.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [4.0, 10.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 3.0000000000000027} |
| 24h成交量 / 流动性 USD | [1169310.3967620004, 1994978.0198] |
| 价差 pp | 1.00 |
| 到期 | 2026-11-04T04:59:00+00:00 |
| 结算规则摘要 | 2026选举后民主党控制参议院：过半席位，50比50按副总统党籍；独立议员依正式党团归属。计入规则指定常规/特别选举与后续决选；争议可等待新国会确定，非选举夜即必须结算。不直接代表法案或行业收益。 |
| 规则指纹 | a217a3e252ccd4578fd29941f90ef8ad364f7d2b7116d35f26945dd2a9d4399c |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:27.694070+00:00 |
| 来源 | https://polymarket.com/event/which-party-will-win-the-senate-in-2026 |

## Major CEX insolvent in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 199777 / 1343533 |
| Yes 概率 % | 3.10 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.75, -0.1] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1111.11, 24184.21898] |
| 价差 pp | 1.40 |
| 到期 | 2027-01-01T05:00:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59ET前Binance/Coinbase/Bybit/OKX/Kraken任一被正式宣布资不抵债或申请/拟申请任一种破产程序则Yes；按官方代表或可信报道共识。被盗、暂停提款或偿付证明延期本身不是触发。 |
| 规则指纹 | 60d4965584f04350506eafe348b3b70153b2fd33101cc7cd02976facea6531d8 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-11-02T23:51:59.978432Z |
| 抓取时间 | 2026-11-02T23:52:27.611349+00:00 |
| 来源 | https://polymarket.com/event/major-cex-insolvent-in-2026 |

## AI 压力：合约、经营与估值分开

三层分开。合约层：2026 AI极端事件合约8.75%，2027年6月版22.5%，均有同一90天至少三项专门触发条件；不是普通回撤或产业泡沫客观概率。经营/融资层：Anthropic新S-1/A披露约8954亿美元采购与租赁承诺，其中未来12个月约698亿美元；属于多年承诺，不是今年资本开支或已经支付。Q3经营亏损5.67亿美元，短约算力和非现金捐赠相关费用影响，不能与调整后利润混用；Google最低1213亿美元云支出承诺横跨2026年4月至2033年7月。Oracle正式初步文件为股票100亿+债券100亿美元，融资能力存在同时有稀释/信用代价，不能把认购需求当经营盈利。MRVL/LITE正式签订全股票并购，4.5股换1股，隐含企业价值1150亿美元；固定换股比例不保证LITE获得固定1132美元，仍待交割与审批。H100日期表2日2.94美元/GPU小时，较26日2.89约+1.73%，与标题7D5.8%不一致，采用日期表；不支持租赁价格已全面坍塌。PLTR上调收入指引，但本次盘后低于收盘，需求增长与股价回报必须分开。五家公司SEC定期财报重查均无更新：NVDA8月26日、MSFT10月28日、GOOGL29日、AMZN30日、META22日；Meta新增DEF14C涉及2027年1月19日拟生效Class C结构，不是本日新增财报或已经发行融资。估值层：NVDA复用核验FCFF底稿更新收盘价情景；其余四家最新TTM/净债务/融资租赁/稀释桥仍不完整，DCF及反推继续不可用，不把旧底稿当最新。情景是假设、没有客观概率，公司整体价值不全归因AI。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-11-02T23:53:35.216231+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 202.06 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.27470596526505553, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -51.12 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -23.73 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 20.05 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-11-02T23:53:37.716308+00:00", "latest_filing_date": "2026-10-28"} |
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
| 披露检查 | {"checked_at": "2026-11-02T23:53:40.645855+00:00", "status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "latest_filing_date": "2026-10-30"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-11-02T23:53:43.023190+00:00", "latest_filing_date": "2026-10-29"} |
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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-11-02T23:53:45.558307+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 科技先修复破位，再谈加风险

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举、JOLTS与AMD财报 |
| 关联标的 | ["SPY", "QQQ", "SMH"] |
| 确认条件 | QQQ先收回683.45再690.49，SMH先511.63再522.49；下一常规时段低点抬升、有效VWAP回踩不破且收盘保持。再看QQQ699.43、SMH532.76本日高点，次日延续才升级；SPY同步收回755.72并守住。 |
| 失效条件 | QQQ680.33、SMH506.44或SPY751.60再破且反抽不回；突破后跌回开盘区间。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 反证 | 盘后小涨与金融强势是反证，但不自动修复芯片破位。 |
| 状态 | 原反弹剧本失败，等待新确认 |

## 相对强势板块等待回踩

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 选举及宏观政策 |
| 关联标的 | ["XLF", "XLI", "XLP", "ITA", "RSP"] |
| 确认条件 | XLF57.20附近突破位回踩承接、日低56.87不破，RSP先收回220.23再看220.95；行业继续相对SPY强且收盘守位。XLI/XLP/ITA使用各自下一交易日开盘区间，不伪造尚未形成的价格。 |
| 失效条件 | XLF跌破56.87反抽不回、RSP219.51失守；行业同步转弱或信用压力扩大。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 反证 | 行业价格强不等于申购资金已确认，SLOOS并非全部宽松。 |
| 状态 | 优先观察，非无条件买入 |

## 存储不抢第一次反抽

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | AMD指引及存储需求 |
| 关联标的 | ["MU", "DRAM", "SNDK", "VRT"] |
| 确认条件 | 先重回MU861.59、DRAM46.96、SNDK1115.16、VRT226.86，再看实际常规VWAP与更高低点；相对SMH止跌、收盘守住，才考虑小步观察参与。 |
| 失效条件 | 再破MU829.24、DRAM46.29、SNDK1067.40、VRT223.64且无承接；财报好但继续跑输。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 反证 | 基本面可能仍增长，跌幅大不自动便宜。SNDK拆分后须重算参考价。 |
| 状态 | 原支持失败 |

## 能源需要双重止跌

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 外交/实际供应与需求 |
| 关联标的 | ["XLE", "XOP", "OIH"] |
| 确认条件 | 油价同合约不再创新低且XLE先收回69.28；形成更高低点并守住常规VWAP，才重建能源观察优先级。 |
| 失效条件 | XLE67.23低点继续失守，或股价反抽时油价继续下跌。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 反证 | 航运尾部风险未消除，既不能盲目追多也不宜把谈判当和平。 |
| 状态 | 暂缓追涨 |

## 财报后的软件与苹果

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 财报、3日开盘、4日中国AI测试 |
| 关联标的 | ["PLTR", "AAPL", "IGV"] |
| 确认条件 | PLTR收回178.34常规收盘、AAPL收回338.32，并在常规回踩后守住；IGV先收103.33且相对QQQ改善。下一开盘区间形成后再定失效，不把盘后短暂上涨当信号。 |
| 失效条件 | 财报后开盘低点失守、反抽缩量而下跌持续；指引成本压力扩大。 |
| 观察期限 | 11月3日起1–3个常规交易日，事件后复核 |
| 反证 | 收入指引增长是经营证据，但估值和已反映预期仍可能压制股价。 |
| 状态 | 观察中 |

## 跨期比较与上期剧本复核

逐条复核11月2日晚报：①QQQ收681.09低于683.45、SMH508.31低于511.63，科技修复失败；SPY日高763.86一度过761.46但收752.10，说明瞬间突破不等于确认。②能源XLE收67.25失守69.28；XLV盘中破184.52后收184.60，只能算收回而非强势确认。③XLF收57.56已超过56.94/57.20，金融条件改善；RSP219.98仍未收回220.04/220.23，不能宣称广泛确认全部完成。④MU833.59、DRAM46.32、SNDK1075.08、VRT224.24均破晚报守位；DRAM日高49.41略过49.31后失败，正是必须等回踩/收盘的例子。⑤IGV101.90低于103.33，软件修复未确认；PLTR好财报后目前仍走弱。⑥Apple中国AI尚待4日测试，Apple新财报盘后下跌，未证实事件买盘。分钟成交量与日线量显著冲突（如QQQ分钟合计6.59亿远高于tc日量5459万），故本次不采用加权VWAP数字，不能声称已准确验证该条件。 同规则报价变化：6369333 -1.70个百分点；3215008 +2.00个百分点；2176270 +0.00个百分点；4713483 -1.50个百分点；691340 +2.20个百分点；2252540 -7.00个百分点；4838928 +0.00个百分点；5401796 +2.50个百分点；2413330 -0.90个百分点；6280962 -8.00个百分点；2745561 +1.00个百分点；562793 +3.00个百分点；1343533 +0.00个百分点。AMD当前买卖63/89、价差26个百分点且成交稀疏，相比上一版2点价差已严重变差，中间价变化不足以表示真实预期改变。Nov2伊朗合约已过规则截止、平台仍有报价且结算未核验，单列历史待裁决；PLTR EPS合约未出现在本次活跃搜索，不保留为将发生事件。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-30/20261102T121041.786096Z/evidence.json",
    "baseline_cutoff": "2026-11-02T12:10:28.031263+00:00",
    "close_change_pct": {
      "SPY": -0.47901276365892587,
      "QQQ": -1.3613467989181949,
      "IWM": -0.06800985678598881,
      "RSP": 0.7649664182223681,
      "GLD": 1.6498946363842304,
      "GC=F": 1.4568224435303145,
      "CL=F": -7.462547125908525,
      "BZ=F": -11.32267916009212,
      "TLT": -0.13440003162134007,
      "UUP": -0.13793419147359876,
      "HYG": -0.6974052865801772,
      "LQD": -0.5370649051718246,
      "^VIX": 8.908339523376952,
      "^VIX3M": 3.9461004221775564,
      "^VVIX": 3.7959230517176534,
      "^MOVE": 0.1611842891726445,
      "NVDA": -1.2607514849246049,
      "MSFT": -2.833817859090426,
      "AMZN": 2.1967957750010925,
      "GOOGL": -0.3037471821895288,
      "META": -1.3431128793619962,
      "CRWV": -8.602145977559129,
      "MU": -5.781355420065982,
      "DRAM": -3.5200972418093057,
      "VRT": -3.552685809391798,
      "XLK": -2.946907385667241,
      "XLE": -3.9560079632490197,
      "XLF": 1.858083671819366,
      "XLI": 1.3799360224655999,
      "XLV": -0.14604263579968135,
      "XLP": 1.5768325777030245,
      "XLY": 2.409435322298936,
      "XLC": 0.3603609658187068,
      "XLU": 0.5526084782019325,
      "XLRE": 1.0887218916799224,
      "XLB": 1.7633607525238792,
      "SMH": -2.713926188216631,
      "IGV": -2.291686037652152,
      "XOP": -5.005887918739605,
      "OIH": -5.476591623248616,
      "ITA": 2.3552908616559565,
      "ARKX": -0.7385069283044388,
      "KRE": 2.38855876916817,
      "SKYY": -3.267197271774047
    },
    "quote_change_pct": {
      "AAPL": {
        "change_pct": -4.467325007261113,
        "from_observed_at": "2026-11-02T12:03:23+00:00",
        "to_observed_at": "2026-11-02T23:52:28+00:00"
      },
      "AMD": {
        "change_pct": -7.321701028911232,
        "from_observed_at": "2026-11-02T12:03:23+00:00",
        "to_observed_at": "2026-11-02T23:52:04+00:00"
      },
      "AMZN": {
        "change_pct": 1.9917355371900758,
        "from_observed_at": "2026-11-02T12:03:20+00:00",
        "to_observed_at": "2026-11-02T23:51:48+00:00"
      },
      "AVGO": {
        "change_pct": -1.6471160274721952,
        "from_observed_at": "2026-11-02T12:03:13+00:00",
        "to_observed_at": "2026-11-02T23:52:22+00:00"
      },
      "BABA": {
        "change_pct": 0.5326553545231372,
        "from_observed_at": "2026-11-02T12:02:13+00:00",
        "to_observed_at": "2026-11-02T23:45:08+00:00"
      },
      "DRAM": {
        "change_pct": -4.86081003417993,
        "from_observed_at": "2026-11-02T12:02:55+00:00",
        "to_observed_at": "2026-11-02T23:48:17+00:00"
      },
      "GLD": {
        "change_pct": 1.1581063529159108,
        "from_observed_at": "2026-11-02T12:02:48+00:00",
        "to_observed_at": "2026-11-02T23:51:58+00:00"
      },
      "GLW": {
        "change_pct": -1.7245471086148156,
        "from_observed_at": "2026-11-02T12:03:26+00:00",
        "to_observed_at": "2026-11-02T23:49:55+00:00"
      },
      "GOOGL": {
        "change_pct": -0.8774723136255935,
        "from_observed_at": "2026-11-02T12:03:21+00:00",
        "to_observed_at": "2026-11-02T23:52:15+00:00"
      },
      "INTC": {
        "change_pct": -6.375735066542876,
        "from_observed_at": "2026-11-02T12:03:29+00:00",
        "to_observed_at": "2026-11-02T23:52:21+00:00"
      },
      "IWM": {
        "change_pct": -0.654012938082027,
        "from_observed_at": "2026-11-02T12:02:23+00:00",
        "to_observed_at": "2026-11-02T23:45:01+00:00"
      },
      "META": {
        "change_pct": -0.35947712418301636,
        "from_observed_at": "2026-11-02T12:03:21+00:00",
        "to_observed_at": "2026-11-02T23:51:04+00:00"
      },
      "MSFT": {
        "change_pct": -3.0753118156717107,
        "from_observed_at": "2026-11-02T12:02:37+00:00",
        "to_observed_at": "2026-11-02T23:52:07+00:00"
      },
      "MU": {
        "change_pct": -6.424066095145031,
        "from_observed_at": "2026-11-02T12:03:23+00:00",
        "to_observed_at": "2026-11-02T23:52:20+00:00"
      },
      "NOW": {
        "change_pct": 0.7132039753904307,
        "from_observed_at": "2026-11-02T12:02:48+00:00",
        "to_observed_at": "2026-11-02T23:50:34+00:00"
      },
      "NVDA": {
        "change_pct": -1.3881800304291758,
        "from_observed_at": "2026-11-02T12:03:18+00:00",
        "to_observed_at": "2026-11-02T23:52:07+00:00"
      },
      "ORCL": {
        "change_pct": -9.005386541233594,
        "from_observed_at": "2026-11-02T12:03:14+00:00",
        "to_observed_at": "2026-11-02T23:51:10+00:00"
      },
      "PLTR": {
        "change_pct": -7.191794271462381,
        "from_observed_at": "2026-11-02T12:03:23+00:00",
        "to_observed_at": "2026-11-02T23:52:05+00:00"
      },
      "QQQ": {
        "change_pct": -1.8579988791654012,
        "from_observed_at": "2026-11-02T12:03:21+00:00",
        "to_observed_at": "2026-11-02T23:52:16+00:00"
      },
      "SMH": {
        "change_pct": -3.0581195613190726,
        "from_observed_at": "2026-11-02T12:02:47+00:00",
        "to_observed_at": "2026-11-02T23:51:11+00:00"
      },
      "SNDK": {
        "change_pct": -6.492271577273623,
        "from_observed_at": "2026-11-02T12:03:23+00:00",
        "to_observed_at": "2026-11-02T23:51:56+00:00"
      },
      "SPY": {
        "change_pct": -0.7914976557973019,
        "from_observed_at": "2026-11-02T12:02:53+00:00",
        "to_observed_at": "2026-11-02T23:49:40+00:00"
      },
      "STX": {
        "change_pct": -8.95318307678421,
        "from_observed_at": "2026-11-02T12:02:36+00:00",
        "to_observed_at": "2026-11-02T23:42:18+00:00"
      },
      "TLT": {
        "change_pct": 0.1718634912840633,
        "from_observed_at": "2026-11-02T12:01:47+00:00",
        "to_observed_at": "2026-11-02T23:41:26+00:00"
      },
      "VRT": {
        "change_pct": -4.883994620040344,
        "from_observed_at": "2026-11-02T12:03:20+00:00",
        "to_observed_at": "2026-11-02T23:45:52+00:00"
      },
      "XLE": {
        "change_pct": -2.568296552718874,
        "from_observed_at": "2026-11-02T12:01:42+00:00",
        "to_observed_at": "2026-11-02T23:49:21+00:00"
      },
      "XOM": {
        "change_pct": -2.7237354085603016,
        "from_observed_at": "2026-11-02T12:01:42+00:00",
        "to_observed_at": "2026-11-02T23:41:19+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": -0.05000000000000071,
        "unit": "percent",
        "observation_date": "2026-10-30"
      },
      "BAMLH0A0HYM2": {
        "change": 0.18000000000000016,
        "unit": "percentage_points",
        "observation_date": "2026-10-30"
      },
      "BAMLC0A0CM": {
        "change": 0.04999999999999993,
        "unit": "percentage_points",
        "observation_date": "2026-10-30"
      },
      "DGS10": {
        "change": -0.040000000000000036,
        "unit": "percent",
        "observation_date": "2026-10-30"
      },
      "DFII10": {
        "change": -0.029999999999999805,
        "unit": "percent",
        "observation_date": "2026-10-30"
      },
      "T10YIE": {
        "change": -0.04999999999999982,
        "unit": "percent",
        "observation_date": "2026-11-02"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-23"
      },
      "CBOE_VIX": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-30"
      },
      "GPRD": {
        "change": -67.5849609375,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_ACT": {
        "change": -36.172332763671875,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_THREAT": {
        "change": -92.63170623779297,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_MA7": {
        "change": -43.773468017578125,
        "unit": "index",
        "observation_date": "2026-11-02"
      },
      "GPRD_MA30": {
        "change": -11.395751953125,
        "unit": "index",
        "observation_date": "2026-11-02"
      }
    },
    "event_probability_change": {
      "6369333": {
        "status": "comparable",
        "change_pp": -1.7000000000000015
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 2.0000000000000018
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4713483": {
        "status": "comparable",
        "change_pp": -1.5000000000000013
      },
      "691340": {
        "status": "comparable",
        "change_pp": 2.1999999999999993
      },
      "2252540": {
        "status": "comparable",
        "change_pp": -7.000000000000001
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5401796": {
        "status": "comparable",
        "change_pp": 2.500000000000002
      },
      "2413330": {
        "status": "comparable",
        "change_pp": -0.9000000000000008
      },
      "6280962": {
        "status": "comparable",
        "change_pp": -7.9999999999999964
      },
      "2745561": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "562793": {
        "status": "comparable",
        "change_pp": 3.0000000000000027
      },
      "1343533": {
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
    "event": "美国中期选举，结果可能跨日/延迟",
    "date": "2026-11-03 America/New_York",
    "source": "https://www.usa.gov/midterm-state-and-local-elections"
  },
  {
    "event": "9月JOLTS",
    "date": "2026-11-03T10:00:00-05:00",
    "source": "https://www.bls.gov/schedule/2026/11_sched.htm"
  },
  {
    "event": "AMD财报电话会；发布在收盘后",
    "date": "2026-11-03T17:00:00-05:00",
    "source": "https://ir.amd.com/news-events/press-releases/detail/1300/amd-to-report-fiscal-third-quarter-2026-financial-results"
  },
  {
    "event": "ISM服务业",
    "date": "2026-11-04T10:00:00-05:00",
    "source": "https://www.ismworld.org/supply-management-news-and-reports/reports/rob-report-calendar/"
  },
  {
    "event": "财政部季度再融资详细安排",
    "date": "2026-11-04 America/New_York",
    "source": "https://home.treasury.gov/news/press-releases/sb0675/"
  },
  {
    "event": "微软原250亿美元债券计划结算，非新增同额发行",
    "date": "2026-11-04 America/New_York",
    "source": "https://www.sec.gov/Archives/edgar/data/789019/000119312526442618/d150456d424b2.htm"
  },
  {
    "event": "Apple中国AI开发者Beta计划",
    "date": "2026-11-04 Asia/Shanghai",
    "source": "https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/"
  },
  {
    "event": "Lumentum财报；分钟未本次核验",
    "date": "2026-11-05 America/New_York",
    "source": "https://www.investor.lumentum.com/overview/default.aspx"
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
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| ism-oct | ISM制造业55.5、订单55.5、价格75.2，价格环比下降但仍处涨价区间。 | 2026-11-02T10:00:00-05:00 | [{"source": "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/october/", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| sloos-oct | 季度贷款调查：大中型C&I标准基本不变，小企业和CRE标准更紧，需求偏弱。 | 2026-11-02T14:00:00-05:00 | [{"source": "https://www.federalreserve.gov/data/sloos/sloos-202610.htm", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| treasury-nov2 | Q4净借款预估6180亿美元较8月低100亿；剔除期初现金影响则高240亿。tc所述870亿/5月与官方口径不符，未采用。 | 2026-11-02T15:00:00-05:00 | [{"source": "https://home.treasury.gov/news/press-releases/sb0675/", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| oracle-financing | 初步文件：普通股100亿美元与优先债券100亿美元，定价/交割不能从初步文件推定完成。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526442729/d181425d424b5.htm", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| anthropic-s1a | 新招股修订披露8954亿美元多年承诺、未来12个月约698亿；Q3经营亏损5.67亿。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| marvell-lite-agreement | 正式全股票并购协议：4.5股MRVL换1股LITE，隐含企业价值1150亿美元；仍需审批和交割。 | 缺失 | [{"source": "https://investor.lumentum.com/financial-news-releases/news-details/2026/Marvell-and-Lumentum-to-Combine-Creating-a-Category-Leader-in-AI-Connectivity/default.aspx", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| pltr-q3 | 盘后新财报上调全年收入指引至85.30–85.34亿美元，调整后FCF48–50亿；不能等同FCFF或股价上涨。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1321655/000132165526000045/a2026q3ex991pressrelease.htm", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| apple-q4 | 盘后Apple收入1145亿美元+12%，EPS2.10含0.05关税退款，毛利率47.9%含约1个百分点退款益处。 | 缺失 | [{"source": "https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| meta-classc | Meta新增DEF14C拟建立Class C结构，计划2027年1月19日生效；不是本日发行完成。 | 缺失 | [{"source": "https://www.sec.gov/Archives/edgar/data/1326801/000162828026068935/meta-20261102.htm", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |
| h100-nov2 | H100日期表2日2.94较26日2.89约+1.73%，与页面5.8%标题不符。 | 缺失 | [{"source": "https://www.silicondata.com/products/silicon-index/h100", "published_at": null, "retrieved_at": "2026-11-02T23:57:50.367766+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN重试仍418；CME页面超时，未核验当前概率矩阵，不使用tc数字冒充官方。",
  "分钟成交量合计与同日tc/日线量大幅不符，弃用VWAP计算；首30分钟价格可作辅助但未经第二分钟源交叉验证。",
  "完整成分涨跌广度、行业当日ETF申赎及精确份额/拆分桥缺失；ICI窗口截至10月21日。",
  "信用与名义/实际利率最新可得30日，金融压力23日；不能当11月2日实时信用。",
  "Brent连续日线−11.32%与新闻结算−7.63%口径冲突，具体合约月未对齐，不把连续收益当同一合约变化。",
  "五家已检查新定期披露；MSFT/AMZN/GOOGL/META现金流与债务/租赁/稀释桥仍不齐，估值不可用。",
  "tc新闻高影响50条has_more=true，有截断；关键事件按官方核验，但不是全部新闻覆盖。",
  "Polymarket多个搜索截断、inflation页失败、AMD价差扩大；成交时戳/订单深度缺失。Nov2伊朗合约规则期限已过仍报价，未核验最终裁决。",
  "H100标题7D5.8%与日期表1.73%不符，采用日期表；单型号/口径不能代表全产业。",
  "Binance PoR入口202空白，未验证最新完整储备或审计；安全事件不等于破产。",
  "地缘爆炸/无人机与外交表态多为tc二手线索，尚无独立官方完整确认；没有推定袭击方或结算结果。",
  "部分盘后ETF成交较稀疏且时点异步；tc返回常规收盘价格配请求时间，规范包仅使用公开分钟实际时戳。",
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
  "tc 新闻达到查询条数上限；仅社交平台线索，非完整财经新闻",
  "tc 报价质量 stale: CVX, IGV, ILMN, LLY, NXPI, XLF, XLI, XLV；不作为新成交证据",
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
  "cnn: missing",
  "news: truncated",
  "request.fa27edcf5f54: request_failed",
  "request.38906ddc2d63: request_failed",
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.CVX.value, quotes.IGV.value, quotes.ILMN.value, quotes.LLY.value, quotes.NXPI.value, quotes.XLF.value, quotes.XLI.value, quotes.XLV.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/october/",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "ISM制造业55.5、订单55.5、价格75.2，价格环比下降但仍处涨价区间。"
  },
  {
    "url": "https://www.federalreserve.gov/data/sloos/sloos-202610.htm",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "季度贷款调查：大中型C&I标准基本不变，小企业和CRE标准更紧，需求偏弱。"
  },
  {
    "url": "https://home.treasury.gov/news/press-releases/sb0675/",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "Q4净借款预估6180亿美元较8月低100亿；剔除期初现金影响则高240亿。tc所述870亿/5月与官方口径不符，未采用。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526442729/d181425d424b5.htm",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "初步文件：普通股100亿美元与优先债券100亿美元，定价/交割不能从初步文件推定完成。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "新招股修订披露8954亿美元多年承诺、未来12个月约698亿；Q3经营亏损5.67亿。"
  },
  {
    "url": "https://investor.lumentum.com/financial-news-releases/news-details/2026/Marvell-and-Lumentum-to-Combine-Creating-a-Category-Leader-in-AI-Connectivity/default.aspx",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "正式全股票并购协议：4.5股MRVL换1股LITE，隐含企业价值1150亿美元；仍需审批和交割。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1321655/000132165526000045/a2026q3ex991pressrelease.htm",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "盘后新财报上调全年收入指引至85.30–85.34亿美元，调整后FCF48–50亿；不能等同FCFF或股价上涨。"
  },
  {
    "url": "https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "盘后Apple收入1145亿美元+12%，EPS2.10含0.05关税退款，毛利率47.9%含约1个百分点退款益处。"
  },
  {
    "url": "https://www.sec.gov/Archives/edgar/data/1326801/000162828026068935/meta-20261102.htm",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "Meta新增DEF14C拟建立Class C结构，计划2027年1月19日生效；不是本日发行完成。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-11-02T23:57:50.367766+00:00",
    "note": "H100日期表2日2.94较26日2.89约+1.73%，与页面5.8%标题不符。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-11-02T23:52:26.385494+00:00",
    "note": "本次检查公开资料；原观测/披露日期独立保留"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-11-02T23:52:25.940750+00:00",
    "note": "本次检查公开资料；原观测/披露日期独立保留"
  },
  {
    "url": "https://www.apple.com.cn/newsroom/2026/10/apple-intelligence-features-are-coming-to-users-in-china/",
    "checked_at": "2026-11-02T23:52:24.356512+00:00",
    "note": "本次检查公开资料；原观测/披露日期独立保留"
  },
  {
    "url": "https://investor.nvidia.com/events-and-presentations/events-and-presentations/default.aspx",
    "checked_at": "2026-11-02T23:52:26.305590+00:00",
    "note": "本次检查公开资料；原观测/披露日期独立保留"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-11-02T23:53:50.518749+00:00",
    "note": "本次检查公开资料；原观测/披露日期独立保留"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AAPL",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMD",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BABA",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CAT",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/COIN",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CVX",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ILMN",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/INTC",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LITE",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/LLY",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MRVL",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NOW",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/PLTR",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLI",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLV",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XOM",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/BZ=F",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CL=F",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DX-Y.NYB",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ES=F",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GC=F",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NQ=F",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/^TNX",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/^VIX",
    "checked_at": "2026-11-02T23:52:31.294817+00:00",
    "note": "真实分钟时点与常规收盘分开；分钟量校验失败故不采用VWAP"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
