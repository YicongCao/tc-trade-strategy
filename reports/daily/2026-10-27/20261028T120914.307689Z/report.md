# 每日交易总结 · 2026-10-27

## 一分钟读懂 · Agent 摘要

### 当前判断

反弹仍在增强，AI需求证据改善，但未确认全面反转。今晚优先观察存储/半导体和电力散热，软件云等待财报承接。

### 与上次相比

相比早报，SK海力士与Vertiv新财报支持需求；盘前MU、SNDK上涨，STX跌幅收窄但仍跌。金融、小盘落后，不能把AI领涨等同于全面回暖。

### 最重要的信号

- 约20:00北京时间，QQQ723.90、SMH564.18已高于昨日高点；SPY770.67仍低于771.14，尚无常规时段确认。
- 约20:05，VRT盘前约+15.3%、MU+3.6%；强业绩后能否守住涨幅比标题更重要。
- 27日VIX17.52、成交量偏低；原油延迟报价回升，油价触及105合约由26%升至39.5%，仍需防通胀扰动。

### 接下来观察

- 开盘后看QQQ722.87、SMH559.81能否回踩守住，SPY能否站上771.14；再看等权与金融是否跟随。
- 北京时间明日02:00 Fed决定、02:30记者会；盘后微软等财报可能改变方向。
- 若高开后跌回昨日收盘且反抽失败，降级为脆弱反弹；不要因盘前突破直接扩大风险。

### 不要忽略

当前为盘前，缺完整广度和常规VWAP。CNN及CME概率矩阵缺失；信用、申赎滞后，预测合约不等于客观概率。

## 研究结论

10月28日晚报：存储与电力设备财报强化AI需求证据，盘前半导体领先；反弹仍需今晚开盘、Fed决定及云厂商财报三道验证。当前是修复增强且分化，不能当成全面趋势反转。

## 时点与口径

| 项目 | 内容 |
| --- | --- |
| 模式 | 每日交易总结 |
| 常规交易窗口 | 2026-10-27 → 2026-10-27（纽约交易日） |
| 截止·纽约 | 2026-10-28T08:09:06.406417-04:00 |
| 截止·北京 | 2026-10-28T20:09:06.406417+08:00 |
| 实际生成时间 | 2026-10-28T12:09:06.622969+00:00 |
| 市场阶段 | 盘前 |
| 下一交易日 | 2026-10-28 |
| 运行重点 | 全市场 |
| 上一版本 | reports/daily/2026-10-27/20261027T232257.797862Z/evidence.json |
| 质量 | partial |
| Daily 北京时间计划时段 | 2026-10-28T20:00:00+08:00 |

## 采集、补查与剩余缺口

| 目标 | 补查结果 | 来源 | 观测 / 抓取时间 | 说明 |
| --- | --- | --- | --- | --- |
| 1147445 | 已校验接入 | https://gamma-api.polymarket.com/events/1147445 | 2026-10-28T12:00:32.169280+00:00 / 2026-10-28T12:00:32.169280+00:00 | Gamma retrieval snapshot, not last trade time; same settlement reviewed |
| 549019 | 已校验接入 | https://gamma-api.polymarket.com/events/549019 | 2026-10-28T12:00:33.890317+00:00 / 2026-10-28T12:00:33.890317+00:00 | Gamma retrieval snapshot, not last trade time; same settlement reviewed |

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
| prices.SPY.value | 769.66 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_1d_pct | 0.56 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_5d_pct | 0.08 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_20d_pct | 0.71 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.return_60d_pct | 1.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_1d_pp | 0.00 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_5d_pp | 0.00 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_20d_pp | 0.00 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.relative_spy_60d_pp | 0.00 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma20 | 770.41 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma50 | 766.70 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.sma200 | 724.81 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma20_pct | -0.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma50_pct | 0.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.distance_sma200_pct | 6.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_sma | 7.28 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.atr14_pct | 0.95 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.drawdown_from_63d_high_pct | -1.21 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SPY/history/ |
| prices.SPY.volume_vs_previous20_ratio | 0.71 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SPY/history/ |
| prices.QQQ.value | 721.25 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_1d_pct | 1.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_5d_pct | 0.50 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_20d_pct | -2.26 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.return_60d_pct | 3.13 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_1d_pp | 0.71 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_5d_pp | 0.43 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_20d_pp | -2.97 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.relative_spy_60d_pp | 1.30 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma20 | 733.18 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma50 | 724.92 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.sma200 | 677.05 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma20_pct | -1.63 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma50_pct | -0.51 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.distance_sma200_pct | 6.53 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_sma | 12.55 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.atr14_pct | 1.74 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.drawdown_from_63d_high_pct | -5.06 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.QQQ.volume_vs_previous20_ratio | 0.85 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/QQQ/history/ |
| prices.IWM.value | 280.18 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_1d_pct | 1.15 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_5d_pct | 1.60 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_20d_pct | 0.42 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.return_60d_pct | -5.17 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_1d_pp | 0.59 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_5d_pp | 1.52 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_20d_pp | -0.30 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.relative_spy_60d_pp | -7.00 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma20 | 277.10 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma50 | 285.08 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.sma200 | 277.38 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma20_pct | 1.11 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma50_pct | -1.72 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.distance_sma200_pct | 1.01 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_sma | 3.57 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.atr14_pct | 1.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.drawdown_from_63d_high_pct | -7.92 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IWM/history/ |
| prices.IWM.volume_vs_previous20_ratio | 0.75 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IWM/history/ |
| prices.RSP.value | 217.52 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_1d_pct | 0.11 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_5d_pct | 0.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_20d_pct | 3.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.return_60d_pct | 0.57 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_1d_pp | -0.45 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_5d_pp | 0.69 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_20d_pp | 3.11 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.relative_spy_60d_pp | -1.27 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma20 | 213.44 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma50 | 214.80 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.sma200 | 206.18 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma20_pct | 1.91 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma50_pct | 1.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.distance_sma200_pct | 5.50 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_sma | 2.00 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.atr14_pct | 0.92 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.drawdown_from_63d_high_pct | -1.99 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/RSP/history/ |
| prices.RSP.volume_vs_previous20_ratio | 1.06 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/RSP/history/ |
| prices.GLD.value | 372.28 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_1d_pct | 1.21 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_5d_pct | -1.42 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_20d_pct | -2.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.return_60d_pct | 0.15 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_1d_pp | 0.65 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_5d_pp | -1.50 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_20d_pp | -3.49 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.relative_spy_60d_pp | -1.68 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma20 | 378.06 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma50 | 393.17 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.sma200 | 413.78 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma20_pct | -1.53 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma50_pct | -5.31 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.distance_sma200_pct | -10.03 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_sma | 5.08 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.atr14_pct | 1.36 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.drawdown_from_63d_high_pct | -13.03 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GLD.volume_vs_previous20_ratio | 0.67 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GLD/history/ |
| prices.GC=F.value | 4,074.60 | USD_per_troy_ounce | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_1d_pct | 0.90 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_5d_pct | -1.64 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_20d_pct | -2.51 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.return_60d_pct | -0.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_1d_pp | 0.34 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_5d_pp | -1.72 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_20d_pp | -3.23 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.relative_spy_60d_pp | -2.22 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma20 | 4,143.51 | USD_per_troy_ounce | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma50 | 4,325.91 | USD_per_troy_ounce | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.sma200 | 4,528.66 | USD_per_troy_ounce | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma20_pct | -1.66 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma50_pct | -5.81 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.distance_sma200_pct | -10.03 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_sma | 67.79 | USD_per_troy_ounce | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.atr14_pct | 1.66 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.drawdown_from_63d_high_pct | -13.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.GC=F.volume_vs_previous20_ratio | 0.85 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GC=F/history/ |
| prices.CL=F.value | 99.90 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_1d_pct | -1.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_5d_pct | -1.86 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_20d_pct | 11.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.return_60d_pct | 24.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_1d_pp | -2.39 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_5d_pp | -1.94 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_20d_pp | 11.06 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.relative_spy_60d_pp | 22.51 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma20 | 95.71 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma50 | 93.62 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.sma200 | 85.71 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma20_pct | 4.38 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma50_pct | 6.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.distance_sma200_pct | 16.55 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_sma | 4.39 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.atr14_pct | 4.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.drawdown_from_63d_high_pct | -5.60 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.CL=F.volume_vs_previous20_ratio | 0.97 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CL=F/history/ |
| prices.BZ=F.value | 113.88 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_1d_pct | -1.67 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_5d_pct | 4.68 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_20d_pct | 11.00 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.return_60d_pct | 35.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_1d_pp | -2.23 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_5d_pp | 4.60 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_20d_pp | 10.29 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.relative_spy_60d_pp | 34.11 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma20 | 106.96 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma50 | 101.84 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.sma200 | 91.70 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma20_pct | 6.47 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma50_pct | 11.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.distance_sma200_pct | 24.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_sma | 3.97 | USD_per_barrel | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.atr14_pct | 3.48 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.drawdown_from_63d_high_pct | -2.43 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.BZ=F.volume_vs_previous20_ratio | 0.51 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/BZ=F/history/ |
| prices.TLT.value | 81.63 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_1d_pct | -0.06 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_5d_pct | 1.87 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_20d_pct | 4.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.return_60d_pct | 0.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_1d_pp | -0.62 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_5d_pp | 1.79 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_20d_pp | 4.05 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.relative_spy_60d_pp | -1.73 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma20 | 79.08 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma50 | 80.29 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.sma200 | 83.28 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma20_pct | 3.22 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma50_pct | 1.67 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.distance_sma200_pct | -1.98 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_sma | 0.79 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.atr14_pct | 0.96 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.drawdown_from_63d_high_pct | -1.43 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/TLT/history/ |
| prices.TLT.volume_vs_previous20_ratio | 0.42 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/TLT/history/ |
| prices.UUP.value | 29.12 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_1d_pct | 0.38 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_5d_pct | 0.76 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_20d_pct | 1.29 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.return_60d_pct | 3.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_1d_pp | -0.18 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_5d_pp | 0.68 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_20d_pp | 0.57 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.relative_spy_60d_pp | 1.54 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma20 | 28.98 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma50 | 28.52 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.sma200 | 27.90 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma20_pct | 0.49 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma50_pct | 2.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.distance_sma200_pct | 4.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_sma | 0.11 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.atr14_pct | 0.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.drawdown_from_63d_high_pct | -0.03 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/UUP/history/ |
| prices.UUP.volume_vs_previous20_ratio | 0.72 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/UUP/history/ |
| prices.HYG.value | 77.60 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_1d_pct | 0.52 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_5d_pct | 1.00 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_20d_pct | 0.76 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.return_60d_pct | -1.18 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_1d_pp | -0.04 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_5d_pp | 0.92 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_20d_pp | 0.04 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.relative_spy_60d_pp | -3.02 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma20 | 77.06 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma50 | 77.89 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.sma200 | 77.89 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma20_pct | 0.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma50_pct | -0.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.distance_sma200_pct | -0.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_sma | 0.29 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.atr14_pct | 0.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.drawdown_from_63d_high_pct | -1.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/HYG/history/ |
| prices.HYG.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/HYG/history/ |
| prices.LQD.value | 104.30 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_1d_pct | 0.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_5d_pct | 1.05 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_20d_pct | 2.28 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.return_60d_pct | -0.87 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_1d_pp | -0.29 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_5d_pp | 0.97 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_20d_pp | 1.57 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.relative_spy_60d_pp | -2.70 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma20 | 102.85 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma50 | 103.83 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.sma200 | 105.89 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma20_pct | 1.41 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma50_pct | 0.45 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.distance_sma200_pct | -1.50 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_sma | 0.60 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.atr14_pct | 0.58 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.drawdown_from_63d_high_pct | -1.56 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/LQD/history/ |
| prices.LQD.volume_vs_previous20_ratio | 0.75 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/LQD/history/ |
| prices.^VIX.value | 17.52 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_1d_pct | -4.73 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_5d_pct | 1.21 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_20d_pct | 9.23 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.return_60d_pct | 6.18 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_1d_pp | -5.29 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_5d_pp | 1.13 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_20d_pp | 8.51 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.relative_spy_60d_pp | 6.15 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma20 | 16.73 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma50 | 16.03 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.sma200 | 18.23 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma20_pct | 4.75 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma50_pct | 9.28 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.distance_sma200_pct | -3.91 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_sma | 2.00 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.atr14_pct | 11.42 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.drawdown_from_63d_high_pct | -12.36 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-27 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX/history/ |
| prices.^VIX3M.value | 19.57 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_1d_pct | -1.86 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_5d_pct | 3.05 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_20d_pct | 8.18 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.return_60d_pct | 3.38 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_1d_pp | -2.42 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_5d_pp | 2.97 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_20d_pp | 7.47 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.relative_spy_60d_pp | 1.55 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma20 | 18.76 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma50 | 18.53 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.sma200 | 20.49 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma20_pct | 4.30 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma50_pct | 5.63 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.distance_sma200_pct | -4.51 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_sma | 1.12 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.atr14_pct | 5.73 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.drawdown_from_63d_high_pct | -4.54 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VIX3M.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-27 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VIX3M/history/ |
| prices.^VVIX.value | 99.45 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_1d_pct | -1.95 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_5d_pct | 2.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_20d_pct | 10.86 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.return_60d_pct | 9.51 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_1d_pp | -2.51 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_5d_pp | 2.29 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_20d_pp | 10.14 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.relative_spy_60d_pp | 7.68 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma20 | 93.88 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma50 | 90.97 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.sma200 | 98.80 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma20_pct | 5.93 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma50_pct | 9.32 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.distance_sma200_pct | 0.66 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_sma | 9.77 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.atr14_pct | 9.82 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.drawdown_from_63d_high_pct | -9.52 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^VVIX.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-27 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^VVIX/history/ |
| prices.^MOVE.value | 97.87 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_1d_pct | -4.23 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_5d_pct | -3.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_20d_pct | -3.88 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.return_60d_pct | 17.89 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_1d_pp | -4.79 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_5d_pp | -3.85 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_20d_pp | -4.41 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.relative_spy_60d_pp | 14.60 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma20 | 103.29 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma50 | 89.02 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.sma200 | 77.03 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma20_pct | -5.25 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma50_pct | 9.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.distance_sma200_pct | 27.06 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_sma | 5.02 | index | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.atr14_pct | 5.13 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.drawdown_from_63d_high_pct | -13.85 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.^MOVE.volume_vs_previous20_ratio | 缺失 | ratio | 2026-10-27 | unavailable | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/^MOVE/history/ |
| prices.NVDA.value | 217.94 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_1d_pct | 0.90 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_5d_pct | 0.68 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_20d_pct | -4.08 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.return_60d_pct | 5.59 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_1d_pp | 0.34 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_5d_pp | 0.60 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_20d_pp | -4.79 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.relative_spy_60d_pp | 3.75 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma20 | 224.44 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma50 | 222.08 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.sma200 | 203.69 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma20_pct | -2.89 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma50_pct | -1.86 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.distance_sma200_pct | 7.00 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_sma | 6.20 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.atr14_pct | 2.85 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.drawdown_from_63d_high_pct | -8.90 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.NVDA.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/NVDA/history/ |
| prices.MSFT.value | 531.33 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_1d_pct | -0.24 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_5d_pct | -0.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_20d_pct | 4.40 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.return_60d_pct | 9.16 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_1d_pp | -0.80 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_5d_pp | -0.18 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_20d_pp | 3.68 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.relative_spy_60d_pp | 7.33 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma20 | 528.99 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma50 | 510.15 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.sma200 | 435.93 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma20_pct | 0.44 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma50_pct | 4.15 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.distance_sma200_pct | 21.88 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_sma | 11.07 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.atr14_pct | 2.08 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.drawdown_from_63d_high_pct | -2.23 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.MSFT.volume_vs_previous20_ratio | 0.97 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MSFT/history/ |
| prices.AMZN.value | 253.10 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_1d_pct | 1.61 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_5d_pct | -3.63 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_20d_pct | 2.61 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.return_60d_pct | -10.89 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_1d_pp | 1.05 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_5d_pp | -3.71 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_20d_pp | 1.89 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.relative_spy_60d_pp | -12.72 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma20 | 254.90 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma50 | 255.21 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.sma200 | 243.34 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma20_pct | -0.71 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma50_pct | -0.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.distance_sma200_pct | 4.01 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_sma | 6.87 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.atr14_pct | 2.71 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.drawdown_from_63d_high_pct | -10.89 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.AMZN.volume_vs_previous20_ratio | 0.96 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/AMZN/history/ |
| prices.GOOGL.value | 320.58 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_1d_pct | 1.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_5d_pct | -5.79 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_20d_pct | -5.97 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.return_60d_pct | -14.12 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_1d_pp | 0.63 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_5d_pp | -5.87 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_20d_pp | -6.68 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.relative_spy_60d_pp | -15.95 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma20 | 340.77 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma50 | 341.84 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.sma200 | 340.91 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma20_pct | -5.92 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma50_pct | -6.22 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.distance_sma200_pct | -5.96 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_sma | 8.38 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.atr14_pct | 2.61 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.drawdown_from_63d_high_pct | -15.06 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.GOOGL.volume_vs_previous20_ratio | 1.19 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/GOOGL/history/ |
| prices.META.value | 620.19 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_1d_pct | -1.64 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_5d_pct | -10.67 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_20d_pct | -16.05 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.return_60d_pct | 5.16 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_1d_pp | -2.21 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_5d_pp | -10.75 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_20d_pp | -16.77 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.relative_spy_60d_pp | 3.32 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma20 | 707.47 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma50 | 665.43 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.sma200 | 631.43 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma20_pct | -12.34 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma50_pct | -6.80 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.distance_sma200_pct | -1.78 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_sma | 25.40 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/META/history/ |
| prices.META.atr14_pct | 4.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.drawdown_from_63d_high_pct | -20.24 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/META/history/ |
| prices.META.volume_vs_previous20_ratio | 2.64 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/META/history/ |
| prices.CRWV.value | 59.57 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_1d_pct | 7.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_5d_pct | -4.12 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_20d_pct | -30.68 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.return_60d_pct | -30.54 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_1d_pp | 7.38 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_5d_pp | -4.20 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_20d_pp | -31.39 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.relative_spy_60d_pp | -32.37 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma20 | 73.06 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma50 | 81.34 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.sma200 | 91.79 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma20_pct | -18.46 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma50_pct | -26.76 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.distance_sma200_pct | -35.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_sma | 6.54 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.atr14_pct | 10.98 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.drawdown_from_63d_high_pct | -44.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.CRWV.volume_vs_previous20_ratio | 0.98 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/CRWV/history/ |
| prices.MU.value | 928.76 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_1d_pct | 2.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_5d_pct | 3.65 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_20d_pct | -12.79 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.return_60d_pct | 11.98 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_1d_pp | 2.21 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_5d_pp | 3.57 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_20d_pp | -13.50 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.relative_spy_60d_pp | 10.15 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma20 | 972.28 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma50 | 979.58 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.sma200 | 737.70 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma20_pct | -4.48 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma50_pct | -5.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.distance_sma200_pct | 25.90 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_sma | 47.71 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.atr14_pct | 5.14 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.drawdown_from_63d_high_pct | -15.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/MU/history/ |
| prices.MU.volume_vs_previous20_ratio | 0.85 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/MU/history/ |
| prices.DRAM.value | 50.52 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_1d_pct | 4.53 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_5d_pct | 5.87 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_20d_pct | -17.57 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.return_60d_pct | -1.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_1d_pp | 3.97 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_5d_pp | 5.79 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_20d_pp | -18.29 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.relative_spy_60d_pp | -3.03 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma20 | 53.49 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma50 | 56.25 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.sma200 | 缺失 | USD_per_share | 2026-10-27 | unavailable | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma20_pct | -5.55 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma50_pct | -10.18 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.distance_sma200_pct | 缺失 | percent | 2026-10-27 | unavailable | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_sma | 2.69 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.atr14_pct | 5.33 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.drawdown_from_63d_high_pct | -20.59 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.DRAM.volume_vs_previous20_ratio | 1.17 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/DRAM/history/ |
| prices.VRT.value | 208.56 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_1d_pct | 4.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_5d_pct | 2.46 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_20d_pct | -16.02 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.return_60d_pct | -20.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_1d_pp | 3.83 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_5d_pp | 2.38 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_20d_pp | -16.73 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.relative_spy_60d_pp | -22.53 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma20 | 226.00 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma50 | 244.12 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.sma200 | 269.39 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma20_pct | -7.72 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma50_pct | -14.57 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.distance_sma200_pct | -22.58 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_sma | 11.66 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.atr14_pct | 5.59 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.drawdown_from_63d_high_pct | -29.01 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/VRT/history/ |
| prices.VRT.volume_vs_previous20_ratio | 1.50 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/VRT/history/ |
| prices.XLK.value | 189.49 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_1d_pct | 1.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_5d_pct | 2.18 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_20d_pct | -2.58 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.return_60d_pct | 6.56 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_1d_pp | 1.14 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_5d_pp | 2.10 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_20d_pp | -3.29 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.relative_spy_60d_pp | 4.72 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma20 | 192.56 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma50 | 189.45 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.sma200 | 168.62 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma20_pct | -1.60 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma50_pct | 0.02 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.distance_sma200_pct | 12.38 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_sma | 4.34 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.atr14_pct | 2.29 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.drawdown_from_63d_high_pct | -6.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLK.volume_vs_previous20_ratio | 0.87 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLK/history/ |
| prices.XLE.value | 68.21 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_1d_pct | -2.05 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_5d_pct | 0.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_20d_pct | 10.84 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.return_60d_pct | 16.71 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_1d_pp | -2.61 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_5d_pp | 0.27 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_20d_pp | 10.12 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.relative_spy_60d_pp | 14.88 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma20 | 66.11 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma50 | 64.43 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.sma200 | 57.81 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma20_pct | 3.17 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma50_pct | 5.86 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.distance_sma200_pct | 17.99 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_sma | 1.49 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.atr14_pct | 2.19 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.drawdown_from_63d_high_pct | -2.05 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLE.volume_vs_previous20_ratio | 0.99 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLE/history/ |
| prices.XLF.value | 55.88 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_1d_pct | -0.25 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_5d_pct | 0.29 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_20d_pct | 3.46 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.return_60d_pct | -2.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_1d_pp | -0.81 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_5d_pp | 0.21 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_20d_pp | 2.75 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.relative_spy_60d_pp | -4.10 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma20 | 54.87 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma50 | 55.91 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.sma200 | 53.37 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma20_pct | 1.84 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma50_pct | -0.05 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.distance_sma200_pct | 4.71 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_sma | 0.71 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.atr14_pct | 1.28 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.drawdown_from_63d_high_pct | -4.24 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLF.volume_vs_previous20_ratio | 0.77 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLF/history/ |
| prices.XLI.value | 167.92 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_1d_pct | 0.57 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_5d_pct | 0.67 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_20d_pct | -0.72 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.return_60d_pct | -8.07 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_1d_pp | 0.01 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_5d_pp | 0.59 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_20d_pp | -1.43 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.relative_spy_60d_pp | -9.91 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma20 | 168.06 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma50 | 171.26 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.sma200 | 172.48 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma20_pct | -0.09 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma50_pct | -1.95 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.distance_sma200_pct | -2.65 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_sma | 2.49 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.atr14_pct | 1.48 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.drawdown_from_63d_high_pct | -9.73 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLI.volume_vs_previous20_ratio | 0.84 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLI/history/ |
| prices.XLV.value | 179.18 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_1d_pct | -0.06 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_5d_pct | -0.36 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_20d_pct | 4.95 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.return_60d_pct | 10.86 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_1d_pp | -0.62 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_5d_pp | -0.44 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_20d_pp | 4.23 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.relative_spy_60d_pp | 9.03 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma20 | 173.30 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma50 | 171.30 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.sma200 | 157.26 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma20_pct | 3.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma50_pct | 4.60 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.distance_sma200_pct | 13.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_sma | 2.99 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.atr14_pct | 1.67 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.drawdown_from_63d_high_pct | -1.17 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLV.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLV/history/ |
| prices.XLP.value | 87.15 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_1d_pct | -0.92 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_5d_pct | -0.68 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_20d_pct | 6.48 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.return_60d_pct | 3.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_1d_pp | -1.48 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_5d_pp | -0.76 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_20d_pp | 5.76 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.relative_spy_60d_pp | 1.54 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma20 | 84.86 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma50 | 84.21 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.sma200 | 83.45 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma20_pct | 2.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma50_pct | 3.49 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.distance_sma200_pct | 4.43 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_sma | 1.41 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.atr14_pct | 1.62 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.drawdown_from_63d_high_pct | -3.16 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLP.volume_vs_previous20_ratio | 0.92 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLP/history/ |
| prices.XLY.value | 115.45 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_1d_pct | 1.04 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_5d_pct | -0.04 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_20d_pct | 5.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.return_60d_pct | -2.12 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_1d_pp | 0.48 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_5d_pp | -0.12 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_20d_pp | 5.06 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.relative_spy_60d_pp | -3.95 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma20 | 112.55 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma50 | 113.22 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.sma200 | 115.27 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma20_pct | 2.57 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma50_pct | 1.97 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.distance_sma200_pct | 0.16 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_sma | 1.65 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.atr14_pct | 1.43 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.drawdown_from_63d_high_pct | -3.47 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLY.volume_vs_previous20_ratio | 0.82 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLY/history/ |
| prices.XLC.value | 103.58 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_1d_pct | -0.26 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_5d_pct | -6.00 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_20d_pct | -7.08 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.return_60d_pct | -6.66 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_1d_pp | -0.82 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_5d_pp | -6.08 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_20d_pp | -7.79 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.relative_spy_60d_pp | -8.50 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma20 | 109.76 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma50 | 111.11 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.sma200 | 112.57 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma20_pct | -5.63 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma50_pct | -6.77 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.distance_sma200_pct | -7.98 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_sma | 1.74 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.atr14_pct | 1.68 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.drawdown_from_63d_high_pct | -9.73 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLC.volume_vs_previous20_ratio | 1.10 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLC/history/ |
| prices.XLU.value | 42.85 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_1d_pct | 0.71 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_5d_pct | 2.32 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_20d_pct | 7.91 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.return_60d_pct | -2.69 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_1d_pp | 0.14 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_5d_pp | 2.24 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_20d_pp | 7.19 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.relative_spy_60d_pp | -4.53 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma20 | 41.44 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma50 | 41.66 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.sma200 | 43.79 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma20_pct | 3.40 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma50_pct | 2.85 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.distance_sma200_pct | -2.14 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_sma | 0.62 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.atr14_pct | 1.44 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.drawdown_from_63d_high_pct | -3.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLU.volume_vs_previous20_ratio | 0.48 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLU/history/ |
| prices.XLRE.value | 42.44 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_1d_pct | -0.84 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_5d_pct | 0.14 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_20d_pct | 2.66 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.return_60d_pct | -5.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_1d_pp | -1.40 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_5d_pp | 0.06 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_20d_pp | 1.95 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.relative_spy_60d_pp | -7.11 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma20 | 41.65 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma50 | 42.61 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.sma200 | 42.73 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma20_pct | 1.89 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma50_pct | -0.39 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.distance_sma200_pct | -0.67 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_sma | 0.64 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.atr14_pct | 1.50 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.drawdown_from_63d_high_pct | -5.65 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLRE.volume_vs_previous20_ratio | 0.90 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLRE/history/ |
| prices.XLB.value | 51.78 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_1d_pct | 0.78 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_5d_pct | 1.07 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_20d_pct | 5.46 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.return_60d_pct | 1.98 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_1d_pp | 0.22 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_5d_pp | 0.99 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_20d_pp | 4.74 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.relative_spy_60d_pp | 0.14 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma20 | 50.15 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma50 | 50.87 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.sma200 | 50.66 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma20_pct | 3.25 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma50_pct | 1.78 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.distance_sma200_pct | 2.21 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_sma | 0.64 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.atr14_pct | 1.25 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.drawdown_from_63d_high_pct | -3.08 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XLB/history/ |
| prices.XLB.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XLB/history/ |
| prices.SMH.value | 557.98 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_1d_pct | 3.02 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_5d_pct | 2.13 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_20d_pct | -8.06 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.return_60d_pct | 2.30 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_1d_pp | 2.46 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_5d_pp | 2.05 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_20d_pp | -8.78 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.relative_spy_60d_pp | 0.46 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma20 | 580.18 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma50 | 573.45 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.sma200 | 517.09 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma20_pct | -3.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma50_pct | -2.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.distance_sma200_pct | 7.91 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_sma | 19.42 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.atr14_pct | 3.48 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.drawdown_from_63d_high_pct | -11.98 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SMH/history/ |
| prices.SMH.volume_vs_previous20_ratio | 0.94 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SMH/history/ |
| prices.IGV.value | 111.78 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_1d_pct | 0.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_5d_pct | 4.54 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_20d_pct | 6.23 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.return_60d_pct | 14.74 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_1d_pp | -0.21 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_5d_pp | 4.46 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_20d_pp | 5.52 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.relative_spy_60d_pp | 12.91 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma20 | 109.21 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma50 | 106.64 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.sma200 | 93.88 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma20_pct | 2.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma50_pct | 4.82 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.distance_sma200_pct | 19.07 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_sma | 2.87 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.atr14_pct | 2.56 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.drawdown_from_63d_high_pct | -0.79 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/IGV/history/ |
| prices.IGV.volume_vs_previous20_ratio | 1.00 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/IGV/history/ |
| prices.XOP.value | 200.01 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_1d_pct | -2.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_5d_pct | -0.02 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_20d_pct | 11.97 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.return_60d_pct | 15.22 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_1d_pp | -2.93 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_5d_pp | -0.10 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_20d_pp | 11.25 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.relative_spy_60d_pp | 13.39 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma20 | 194.35 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma50 | 190.45 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.sma200 | 168.47 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma20_pct | 2.91 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma50_pct | 5.02 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.distance_sma200_pct | 18.72 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_sma | 5.18 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.atr14_pct | 2.59 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.drawdown_from_63d_high_pct | -2.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/XOP/history/ |
| prices.XOP.volume_vs_previous20_ratio | 1.04 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/XOP/history/ |
| prices.OIH.value | 408.87 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_1d_pct | 1.61 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_5d_pct | 6.23 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_20d_pct | 7.52 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.return_60d_pct | 7.00 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_1d_pp | 1.05 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_5d_pp | 6.15 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_20d_pp | 6.81 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.relative_spy_60d_pp | 5.16 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma20 | 387.73 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma50 | 401.69 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.sma200 | 396.30 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma20_pct | 5.45 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma50_pct | 1.79 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.distance_sma200_pct | 3.17 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_sma | 11.28 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.atr14_pct | 2.76 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.drawdown_from_63d_high_pct | -6.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/OIH/history/ |
| prices.OIH.volume_vs_previous20_ratio | 0.72 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/OIH/history/ |
| prices.ITA.value | 206.22 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_1d_pct | -0.45 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_5d_pct | 0.03 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_20d_pct | -1.47 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.return_60d_pct | -16.10 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_1d_pp | -1.01 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_5d_pp | -0.05 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_20d_pp | -2.19 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.relative_spy_60d_pp | -17.94 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma20 | 206.17 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma50 | 216.70 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.sma200 | 228.99 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma20_pct | 0.02 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma50_pct | -4.83 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.distance_sma200_pct | -9.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_sma | 4.06 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.atr14_pct | 1.97 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.drawdown_from_63d_high_pct | -18.47 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ITA.volume_vs_previous20_ratio | 1.02 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ITA/history/ |
| prices.ARKX.value | 30.84 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_1d_pct | 2.22 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_5d_pct | 2.53 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_20d_pct | -3.38 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.return_60d_pct | -2.37 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_1d_pp | 1.66 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_5d_pp | 2.45 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_20d_pp | -4.10 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.relative_spy_60d_pp | -4.21 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma20 | 31.24 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma50 | 31.94 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.sma200 | 32.54 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma20_pct | -1.29 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma50_pct | -3.44 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.distance_sma200_pct | -5.22 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_sma | 0.76 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.atr14_pct | 2.46 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.drawdown_from_63d_high_pct | -11.53 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.ARKX.volume_vs_previous20_ratio | 0.97 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/ARKX/history/ |
| prices.KRE.value | 72.58 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_1d_pct | -0.21 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_5d_pct | 2.78 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_20d_pct | 3.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.return_60d_pct | -5.28 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_1d_pp | -0.77 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_5d_pp | 2.70 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_20d_pp | 3.22 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.relative_spy_60d_pp | -7.11 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma20 | 70.28 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma50 | 71.97 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.sma200 | 70.24 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma20_pct | 3.28 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma50_pct | 0.85 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.distance_sma200_pct | 3.33 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_sma | 1.24 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.atr14_pct | 1.70 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.drawdown_from_63d_high_pct | -6.33 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/KRE/history/ |
| prices.KRE.volume_vs_previous20_ratio | 0.79 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/KRE/history/ |
| prices.SKYY.value | 171.46 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:value | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_1d_pct | 0.94 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_1d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_5d_pct | 4.97 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_5d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_20d_pct | 5.35 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_20d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.return_60d_pct | 15.87 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:return_60d_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_1d_pp | 0.38 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_1d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_5d_pp | 4.89 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_5d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_20d_pp | 4.64 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_20d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.relative_spy_60d_pp | 14.03 | pp | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:relative_spy_60d_pp | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma20 | 167.65 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma20 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma50 | 164.45 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma50 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.sma200 | 135.94 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:sma200 | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma20_pct | 2.27 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma20_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma50_pct | 4.26 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma50_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.distance_sma200_pct | 26.13 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:distance_sma200_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_sma | 4.82 | USD_per_share | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_sma | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.atr14_pct | 2.81 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:atr14_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.drawdown_from_63d_high_pct | -1.96 | percent | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:drawdown_from_63d_high_pct | https://finance.yahoo.com/quote/SKYY/history/ |
| prices.SKYY.volume_vs_previous20_ratio | 1.31 | ratio | 2026-10-27 | ok | yahoo_auto_adjust_ohlc_v1:volume_vs_previous20_ratio | https://finance.yahoo.com/quote/SKYY/history/ |
| macro.DGS2.value | 4.68 | percent | 2026-10-26 | lagged | source_series_v1:DGS2 | https://fred.stlouisfed.org/series/DGS2 |
| macro.BAMLH0A0HYM2.value | 3.30 | percentage_points | 2026-10-26 | lagged | source_series_v1:BAMLH0A0HYM2 | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| macro.BAMLC0A0CM.value | 0.90 | percentage_points | 2026-10-26 | lagged | source_series_v1:BAMLC0A0CM | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| macro.DGS10.value | 5.00 | percent | 2026-10-26 | lagged | source_series_v1:DGS10 | https://fred.stlouisfed.org/series/DGS10 |
| macro.DFII10.value | 2.66 | percent | 2026-10-26 | lagged | source_series_v1:DFII10 | https://fred.stlouisfed.org/series/DFII10 |
| macro.T10YIE.value | 2.35 | percent | 2026-10-27 | ok | source_series_v1:T10YIE | https://fred.stlouisfed.org/series/T10YIE |
| macro.STLFSI4.value | -0.63 | index | 2026-10-16 | lagged | source_series_v1:STLFSI4 | https://fred.stlouisfed.org/series/STLFSI4 |
| macro.CBOE_VIX.value | 17.52 | index | 2026-10-27 | ok | source_series_v1:CBOE_VIX | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
| macro.GPRD.value | 165.25 | index | 2026-10-26 | lagged | source_series_v1:GPRD | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_ACT.value | 149.77 | index | 2026-10-26 | lagged | source_series_v1:GPRD_ACT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_THREAT.value | 187.38 | index | 2026-10-26 | lagged | source_series_v1:GPRD_THREAT | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA7.value | 181.42 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA7 | https://www.matteoiacoviello.com/gpr.htm |
| macro.GPRD_MA30.value | 175.44 | index | 2026-10-26 | lagged | source_series_v1:GPRD_MA30 | https://www.matteoiacoviello.com/gpr.htm |
| quotes.AMZN.value | 253.30 | USD_per_share | 2026-10-28T12:00:12+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AMZN |
| quotes.AVGO.value | 348.05 | USD_per_share | 2026-10-28T12:00:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/AVGO |
| quotes.CEG.value | 262.00 | USD_per_share | 2026-10-28T11:58:32+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/CEG |
| quotes.DRAM.value | 52.62 | USD_per_share | 2026-10-28T12:05:03+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/DRAM |
| quotes.GEV.value | 911.59 | USD_per_share | 2026-10-28T12:04:46+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GEV |
| quotes.GLD.value | 370.73 | USD_per_share | 2026-10-28T11:58:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLD |
| quotes.GLW.value | 128.81 | USD_per_share | 2026-10-28T12:00:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GLW |
| quotes.GOOGL.value | 324.69 | USD_per_share | 2026-10-28T12:00:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/GOOGL |
| quotes.IGV.value | 111.18 | USD_per_share | 2026-10-28T11:36:00+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IGV |
| quotes.IWM.value | 279.50 | USD_per_share | 2026-10-28T11:59:56+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/IWM |
| quotes.META.value | 620.58 | USD_per_share | 2026-10-28T12:00:24+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/META |
| quotes.MSFT.value | 529.00 | USD_per_share | 2026-10-28T12:00:06+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MSFT |
| quotes.MU.value | 962.40 | USD_per_share | 2026-10-28T12:05:07+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/MU |
| quotes.NVDA.value | 219.61 | USD_per_share | 2026-10-28T12:00:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NVDA |
| quotes.NXPI.value | 235.00 | USD_per_share | 2026-10-28T11:44:17+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/NXPI |
| quotes.ORCL.value | 131.56 | USD_per_share | 2026-10-28T12:00:29+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/ORCL |
| quotes.QQQ.value | 723.90 | USD_per_share | 2026-10-28T12:00:27+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/QQQ |
| quotes.RSP.value | 217.22 | USD_per_share | 2026-10-28T11:37:28+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/RSP |
| quotes.SMH.value | 564.18 | USD_per_share | 2026-10-28T12:00:28+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SMH |
| quotes.SNDK.value | 1,365.26 | USD_per_share | 2026-10-28T12:00:25+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SNDK |
| quotes.SPY.value | 770.67 | USD_per_share | 2026-10-28T12:00:10+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/SPY |
| quotes.STX.value | 653.23 | USD_per_share | 2026-10-28T12:00:27+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/STX |
| quotes.TLT.value | 81.41 | USD_per_share | 2026-10-28T12:00:14+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/TLT |
| quotes.VRT.value | 240.46 | USD_per_share | 2026-10-28T12:05:05+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/VRT |
| quotes.XLE.value | 68.43 | USD_per_share | 2026-10-28T11:48:57+00:00 | stale | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLE |
| quotes.XLF.value | 55.52 | USD_per_share | 2026-10-28T11:50:13+00:00 | ok | tc_last_v1 | https://query1.finance.yahoo.com/v8/finance/chart/XLF |
| premarket.BZ_F.value | 111.29 | USD/barrel | 2026-10-28T11:50:03+00:00 | lagged | Yahoo延迟分钟行情真实时间；期货换月/合约未对齐，仅作水平，不作官方结算收益。盘前VIX不与前日VIX3M拼接期限结构。 | https://query1.finance.yahoo.com/v8/finance/chart/BZ=F |
| premarket.CL_F.value | 101.77 | USD/barrel | 2026-10-28T11:50:30+00:00 | lagged | Yahoo延迟分钟行情真实时间；期货换月/合约未对齐，仅作水平，不作官方结算收益。盘前VIX不与前日VIX3M拼接期限结构。 | https://query1.finance.yahoo.com/v8/finance/chart/CL=F |
| premarket.ES_F.value | 7,771.50 | index points | 2026-10-28T11:50:33+00:00 | lagged | Yahoo延迟分钟行情真实时间；期货换月/合约未对齐，仅作水平，不作官方结算收益。盘前VIX不与前日VIX3M拼接期限结构。 | https://query1.finance.yahoo.com/v8/finance/chart/ES=F |
| premarket.NQ_F.value | 29,955.25 | index points | 2026-10-28T11:50:30+00:00 | lagged | Yahoo延迟分钟行情真实时间；期货换月/合约未对齐，仅作水平，不作官方结算收益。盘前VIX不与前日VIX3M拼接期限结构。 | https://query1.finance.yahoo.com/v8/finance/chart/NQ=F |
| premarket.VIX.value | 17.45 | index points | 2026-10-28T11:45:31+00:00 | lagged | Yahoo延迟分钟行情真实时间；期货换月/合约未对齐，仅作水平，不作官方结算收益。盘前VIX不与前日VIX3M拼接期限结构。 | https://query1.finance.yahoo.com/v8/finance/chart/^VIX |

## 指标历史比较（不同日期观测，非连续交易日）

```json
[
  {
    "id": "prices.SPY.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.28997802734375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6099853515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1500472553315202,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2252103551135587,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.22413269765242383,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2309756945303119,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7458138061674613,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2743497416375704,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8747339241601315,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.47728286647384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2729980468749318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2049987792969432,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.021921386718759095,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5660803222656341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4048419189452943,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.030590515136737,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5216264731699116,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.10573147132399985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5623956025363142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.15356624706088784,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.532860679743119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.21392950347669526,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.03142874581473176,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.1535731724330356,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0011969262183151308,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.019218749587764594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5506395768739014,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.07829459119436111,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SPY.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0672563752026426,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.13093367626485142,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 9.04998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.6199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.16338512685962758,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3723263795032414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.361942585432785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.993013216697494,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0429539251844644,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7304751472870583,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4940534475551539,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.1826927683105346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3134323821911478,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1471160243896827,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.137809887780361,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.7620375221671822,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2971401190170031,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.4561254056494879,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3806804766049776,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2945900981633054,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8339996337890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.6875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15720458984378638,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.2771215820312136,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4836398315429733,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.3276742553711074,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.3447088669880425,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.378432816646502,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.26971119324375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.673459634045348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.2614816679843655,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.16901250439047555,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1971435546875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.4242946079799115,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.005563868462664878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.18969211509980255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1913208689286696,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.47652834757146945,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.QQQ.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.048338058562470865,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.005491661032748563,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.19000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.399993896484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7019879050278011,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5071356733880261,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5093607434949243,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.927967347171966,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5013988420242375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.398997683188055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5364846800923635,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.4344435723534499,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8520351603593213,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7323460285015848,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7334934411473482,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6969916526416542,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7555850358567762,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.1246479415504846,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.338249244067768,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.91172643882729,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.05849914550782387,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.9255004882812159,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4617590332031227,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.5265991210937386,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1085171508788676,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5596183013915947,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1301065523500964,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.9191779017451727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.276097723216274,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.393231176140187,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.110973945840299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3852856778221678,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.06285749162946441,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.510711669921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03734683479549017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.20548882170784988,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0483247313473498,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.445962034257441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IWM.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.14810926751711628,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2592024749079971,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.230010986328125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.660003662109375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.24050195700899835,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.0469135550013275,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0538489701388931,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.4311677177617046,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.22847538458199423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.390195573617482,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8748482192941109,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.12765498411435594,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.09045470167747816,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.2721239101148862,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.277981667791317,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.6621434122920165,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5173384215854671,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1158458319799114,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.00011429513397942515,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.349627882359484,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4010002136230355,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7144996643066293,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04886291503908069,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3540081787109557,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11127647399902685,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5864914703369095,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08385678316169543,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.0412080598031217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1300862030985117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9381495342801749,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.05464888563053716,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5064624244673022,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.07071467808314735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.07928575788225456,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03351615976709099,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.04379338588221904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.10363854911257242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7479658854952831,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.RSP.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.18136463525869173,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.19792950917631214,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.459991455078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.3699951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8824902548496771,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7498299294028352,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7042829812027316,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.36867928186917753,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.10108800665329376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.832987667450671,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.154585719443324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.6527784467696085,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0325375101811973,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.5246195742892765,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4801502835503078,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.5996549763994894,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.846901812820755,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.558637925813101,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.0293196436034555,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8245044197042315,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5305007934570085,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.206001281738281,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.6641998291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.1429998779296966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.21095001220697895,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.0123500061034747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.316040275449104,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3213170949526334,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.292151802353791,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.6040645102645792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1231612719864952,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.075039083921025,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.23357064383370485,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.14999607631138456,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08003104895641044,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.05910261156722063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0418836589268796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.254466565119639,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GLD.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.09990130189896285,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.10642859947448713,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 36.2001953125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -68.0,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.13540242038085903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3170624247450302,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.283933916401958,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8108080268284135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6041659378626774,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.827749368490529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.2816181955874861,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.9977317899135039,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2854496757123792,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0918520696314715,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0598012187495343,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.0417837213587253,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.14164786830478393,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.553399626852959,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.1563521197476176,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.47955107656033613,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.2550048828125,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -47.72001953125073,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -7.982001953125291,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -38.17400390625062,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.1314990234377547,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -10.202001953124636,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.997111317588717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5028023412245397,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0087592747036416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7342589428618647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8413104483026022,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.2959401938484199,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.0571463448660694,
        "unit": "USD_per_troy_ounce"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.9571358816964306,
        "unit": "USD_per_troy_ounce"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0658538490903382,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.019933333681701804,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7705776494856025,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.4474861174831002,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GC=F.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.32614354468109374,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.02215659867127473,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.8600006103515625,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.8899993896484375,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3656495203941512,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.023853632103432165,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.02384660214137524,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -9.982960011638632,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.877963295436592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.158172631017476,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.162284989608246,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1290064842980563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.21560226506263103,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.24906398721699086,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.24797929979379907,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -11.213935706168943,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1321494892691302,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.883822889379905,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.037018913768378,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.606289350771899,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5260002136230497,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.0194999694824247,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.30800003051757585,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7386001586913977,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2039000129699673,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0661500167846611,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.5308518437371585,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.2670065968728474,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.3454146411191035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.075886939100882,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.4532005516707756,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.700940089269512,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.025713784354073788,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0185699462890625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.10557805639238715,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.09982360093962939,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.75753621673449,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.785882412310269,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CL=F.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2161157233077351,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6587026854076485,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.9300003051757812,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.089996337890625,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8868763305673433,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.9727739733307761,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0355450917219455,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.74563070642626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0030738774776662,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3928809274676759,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 7.437228177741506,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 12.822335364727078,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7368290752358231,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1979843284443348,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.2596777893743694,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5146550118959485,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.25726007131020445,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11853118583010591,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 8.311962101901639,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 15.299618231200917,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.56450004577637,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.3264999389648438,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.460199890136721,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.480999755859372,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.25269998550415096,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3032499694824224,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.3790049358664236,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.497275593856507,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.4114103739764534,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.3306102494460976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.453809459126365,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.840415916329089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.04285757882254426,
        "unit": "USD_per_barrel"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.18571472167968794,
        "unit": "USD_per_barrel"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09508300222237454,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.33375731686844246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.6535300591081992,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.4592101962476067,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.BZ=F.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.20878963932400774,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3300833165367295,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0500030517578125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.5,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.47922165254051796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.904407479857039,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.9219019813154317,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.37379208481338466,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4558436463440785,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.353287831897358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.39145155355055916,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.2812459015367224,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.32917439720899777,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1296178349705976,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.1460346789678555,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.6047677793436965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.28997015982338326,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.078938090259788,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.48328237060957235,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.758528768010563,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.18568992614746094,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6084335327148409,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.01831222534180199,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.008887481689455967,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.016680870056148933,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.08211582183838573,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.306335457276119,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1111634471676846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08548842372202436,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8793191621654826,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.040401175341242546,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8959505976524738,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04499980381556912,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.061427525111607095,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.054502487773883224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.09471083732703878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.06037716103530766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.3093917539624087,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.TLT.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08286614425060068,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1468151885755316,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.220001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.20652580333804238,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7240105958068566,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7267663608065744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1747607196346377,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.20682195753103372,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.18775995190121186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.39048849859297796,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.3234362984982715,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.35657305866956257,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.49880024069329787,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5026336631541506,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.056214974895674175,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5389918486364276,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.4621096935387823,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.2652224227531095,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.8007191649721115,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.01850004196166921,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.07499990463256978,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.020400009155270737,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.08359996795654112,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.00895000457763473,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.04439999580383258,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3156517563420502,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5004151659723788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.31287144708331827,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.47347536804596135,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.360905699850278,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6234341348743788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.004999978201729913,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.02857140132359097,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.01870491118078782,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1018132694160393,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.377619682528918,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.755239365057836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.UUP.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.15154340466993232,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.22558917142788415,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.40000152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7699966430664062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3234658612325081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.518136712035222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5206319358920242,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3394693026865023,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7520597860388945,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.660906297267873,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2434007110206471,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.4559394756397217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4735131165640283,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.29292635692166336,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.29649923823960034,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.10849360815619047,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0062459798714331605,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3865565556303028,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.118134635180779,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.9332223421135617,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.02913322448729616,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.05490226745605753,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.024507751464838634,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.16750274658203068,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0005755233764688228,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.005558052062980323,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.48117531214222353,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0701643956033458,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5447430293242461,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2002876756738057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5128026999111301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9955846691338754,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.006428854806082629,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.027857099260602647,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.006410279211314096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.03996655626790463,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.505484364105313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9730494468200623,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.HYG.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2543160837072632,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.25760111420943343,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.28000640869140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0800018310546875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1054892936825258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.0613008063910625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.06177591164120422,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3929725871723244,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3343236190604948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.6405800743274375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.031053585728857414,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.971801128496208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.255536549014046,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2865111615046212,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.28590860929362805,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8380031073579874,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4114901871069665,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.366230332689867,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8436803384312741,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.4490839949700476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11649932861328693,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.33715858459473225,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.010117797851563637,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1266560363769429,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.012538452148433521,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.06788711547851278,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.15755778113817343,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7199973208521504,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.27942533826570415,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1612217028693972,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.27607076722785395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0824176339862657,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03857149396623882,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.03928647722516743,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03863121664628477,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.044087138972613404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2642593654165748,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.019291788133514,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.LQD.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.06044313274803992,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.4072154923463136,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8699989318847656,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.21000099182128906,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7190519893615743,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3971619385434781,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.484333217202427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -12.146344247198936,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.209907917450817,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -12.588689427717604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -9.770258411689525,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 11.12415848375864,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8690992446930945,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1719515834299195,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.2602005195500032,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -13.377319941729247,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.955721723618279,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -13.863039169355176,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -8.534412093252497,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 15.155694195056858,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.07399997711181783,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6620000362396254,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.03360000610351399,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.33220003128051623,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.007700004577639419,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.07325001239776796,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.690077802035831,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.009367909754812,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.667256273178545,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.9745733862204666,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.814228221295124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7688221418595043,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.005714212145124131,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3214283670697893,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.571506670970301,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7183046959391923,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.352170794627787,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.858735205449314,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.37000083923339844,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5799999237060547,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7811431068622698,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.256677092229408,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.3195440859511187,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.680731999716346,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.1988352536766094,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3448615230111649,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.4561403183409594,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 9.370977329855801,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.93119036219379,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0314667371158492,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0954113882986949,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.9117076942466573,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.944649059844071,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.9294882186264051,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5814063941808278,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 11.84826019632964,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.07399997711181783,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.40199995040893555,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.010599975585936505,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.10559997558593892,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.008450002670286949,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.037500009536742596,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.3927634789431496,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.8752785223421711,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.0587938623898516,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.5430781496585286,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.8455671086213483,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.6602638090378665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.007142884390694659,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.19428566523960666,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.07044100926894803,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.8481876603583407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VIX3M.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.71922461498344,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.137832814701827,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.9800033569335938,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.2999954223632812,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.586650687686811,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.194080738519547,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 7.511020072491903,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -11.417967059753796,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.579846964132134,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.9517456555459916,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.168738635686518,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 13.240464787163797,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.736697943018332,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.9688703834059895,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 7.28688737483948,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -12.648942754284107,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.3256607702995957,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -7.226095397183563,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2940047115263864,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 15.717747653637637,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.48699989318846804,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.266500473022461,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11059997558594148,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2569999694824219,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.056299972534191056,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.318249969482423,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.672346631900081,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.280312626364477,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.312316839199813,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0319713172707523,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.062654692230481,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.0102259179922255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.14428601946149477,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.4007132393973212,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0495359892995495,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2092068223870758,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^VVIX.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.8014769274511284,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.0926170009365475,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.319999694824219,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.8299942016601562,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.143308045713622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.622279808434215,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.644550630116018,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.369396097620082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -10.327311235020275,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -29.12569839277891,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -14.672091524796453,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -14.500131510119527,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.993260790382102,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.847490163547774,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.868683327768442,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.600371792150394,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -11.631561246169552,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -30.22999538825324,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -14.508293994778516,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -13.450684031238588,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1974998474121037,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.4870002746582145,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.56580001831054,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.837400054931635,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.15465000152588004,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9008499908447334,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.993421305159717,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.1458929259829205,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.5868578431661255,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -8.063155937485146,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.875420262562443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.534822263841875,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.29285703386579254,
        "unit": "index"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.022142682756697063,
        "unit": "index"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.06952994272752555,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.21513119135283976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.^MOVE.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.802816683847354,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.371473814352777,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.94000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.470001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.4909259613007375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1837428698638242,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1811727188466126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.952141168042779,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.539228248053071,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3379924676404151,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.130448731447432,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.6940450402708,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.3408787059692173,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9585325147502655,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9570400211941887,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.7211654735124675,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7934144418856093,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.06364272600284515,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.2557148072873003,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.21676217379696,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4635002136230355,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.607499694824213,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.13636993408204034,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7346286010742062,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.16755783081055142,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7344568634033237,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0627413040889544,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.762683902058948,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9332508672482143,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.983302970338662,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.865136834663538,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3370988070354075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.05714307512555816,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.4228581019810269,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0009014573608032705,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.17602180426014646,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8109021889575629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6144462409925513,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.NVDA.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03638537661868502,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.06602730324157902,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.26995849609375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.53997802734375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.780830492486385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.07082623041563263,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.07092343793881906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.029309461298312,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1960882660664076,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.405961381559174,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.660024279763576,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -27.787324829055592,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.6307832371548647,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.15438412469792606,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15320925971360477,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7983337667680002,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.9419020722338693,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.680311123196745,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.785290355603444,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -25.31004196258175,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.118501281738304,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.480003356933594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0376513671874932,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.5647796630859716,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.27535720825193266,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3266546630859466,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.453407852616583,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1545593001832,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4617168034527941,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8394798129985892,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.36854275052244745,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.4963048100818064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.047855922154019126,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.22785295758928648,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.004018413578591673,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.04072516873458021,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.23368450962697462,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.0993611215778234,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MSFT.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.035576785209655126,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3024812734084771,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.010009765625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -9.529998779296875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1703491818131795,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.5412821358042006,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.461820639018108,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.194932183367862,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4123300829604446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3935141866163283,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.605385422258177,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -24.387569699643052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.3203964371446997,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.316071780690642,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.2376879413656843,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.425907877898174,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6665162767929833,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.6678639282538987,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.7306514980980463,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -21.910286833169213,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.32150039672850994,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0900001525878906,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1641998291015625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.3139996337890523,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.028600006103516762,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.26860008239745525,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4497687506924706,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.181226473253529,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6340001043103292,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.207030749732609,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6359018615873522,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.035669679363441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.07143075125558074,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3528529575892856,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.07236024233100746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2328176102115167,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.411875896323611,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.3553972072149154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.AMZN.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.04999184955996161,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.007103786225771014,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -19.70001220703125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.2581087931306976,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.326307744009226,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.1657877852021556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.9734227375983853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6049028115673432,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.867912597532674,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.1292627027948203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -18.38416252955647,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.4081560484622178,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.1010973888956674,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.9416550875497318,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.204398432128697,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8590890053998823,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.1422623391702444,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.2545287786346897,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -15.90687966308263,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0170013427734261,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.5605010986328125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.46398071289064546,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.1184564208984398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.036760559082040345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0640986633300713,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.3858761808223319,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.462308616513965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.231415933013258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.149900728803137,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1188216031982048,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.797454366566324,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.046425955636161476,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2928532191685278,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04582596623472712,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.06518172820730062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0015698373867181,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.219826559410345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.GOOGL.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.18282151616762676,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.45207194569749753,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -10.3699951171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -74.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.23212278715781798,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.05832475125931991,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05297407995922221,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.7168069117498348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.167077151268375,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -10.30388751487208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -8.197687478191561,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -11.837817165736109,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.38217004248933817,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2835351063728786,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.27710677761164604,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.947782606280146,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.912890957435836,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -11.57823725650965,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -7.322953554031431,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -9.36053429926227,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -5.929998779296966,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -24.400997924804756,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0333740234374318,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.205841064453125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15596527099603463,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.09545196533201761,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7249194099104965,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -7.196554846861913,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.7057655184334326,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -12.111732710945056,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.6176329437466608,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -11.712240286176291,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.527143205915177,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.4964250837053577,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.016251263938223737,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9404839871771578,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.3336070112837213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -9.524298795097497,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.META.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0391286601441847,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8005287287726388,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.380001068115234,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.5600013732910156,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 6.175370603807329,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.283732027573952,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.581830935302989,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 16.031252716150213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.447884561729754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.2874734364455307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -7.437141981987747,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -18.30534885174484,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 6.325417859138849,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.058521672460393,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.357698237650565,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 14.800277021619898,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.7020707555622963,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.5618231780831024,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -6.562408057827618,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -15.828065985271003,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.318000030517581,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -7.460249900817871,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.9286000061035082,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.583700180053711,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.10284999847412735,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5139750099182123,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 7.334120442561364,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.375599510119521,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 6.1508806147101325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9276072574892815,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.839181476310394,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.4121261184211633,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.03892871311732726,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.327500207083566,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.800471210801156,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.979337644325943,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.065720719977435,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.376312348946243,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.CRWV.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3418753804159933,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.22081328444037,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 25.05999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 32.69000244140625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.20684616523172217,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.7488441372338532,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.7807654144088487,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 9.625869238241558,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.459524874274921,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.455548999507519,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.1650048315677424,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 12.426991349707663,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05679890990020198,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.5236337821202945,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.556632716756425,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 8.394893543711246,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7137110681074592,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.181199257869947,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.0397387557278748,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 14.904274216181502,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -6.8076171875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -43.63687438964848,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.6566162109375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.64276855468745,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.9196113586425554,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 14.070743103027326,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.223688153517923,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.320791179365049,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.713983642172213,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.7686393810571595,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.910298507489273,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.069430956754516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.2584119237139646,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.0673222906200053,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5030152084930446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.4181161693245903,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.283959421494629,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.979355400580573,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.MU.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.004591610209837116,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.10124820714110394,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.1899986267089844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.799999237060547,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.8326605493750758,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.793501202107121,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.867559022286395,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 15.557186041778381,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4730258653223203,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.4199394253642765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.856985585203764,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.7903661236498944,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.982707804706596,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.568290846993563,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.643426324633971,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 14.32621034724807,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7272120591548585,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.145589683726705,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.7317195093638955,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 10.267648990123735,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5385000228881793,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.238500022888182,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.19739997863769077,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7915998840332037,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.9949340406522325,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 10.328008295407487,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.194149826523663,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.155661725540098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.013571602957589413,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.1985716138567244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2694862486644789,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.10352687008099437,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.442311637027416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.401130594262327,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.DRAM.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5214951816138783,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2685842786470579,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 8.779998779296875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.0,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5850399659369296,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.617661882875846,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.513344947748832,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 16.670950905886563,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.118007666898002,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.669166081503562,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.4161863869664586,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 8.50853984372866,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7350872212684498,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.3924515277622875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 5.2892122500964085,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 15.43997521135625,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.3721938607305404,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.39481633986599,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.541452462806326,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 10.985822710202498,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.988999938964838,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -11.466999816894543,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.6759661865234534,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -8.655123291015627,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.22546508789065456,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.830918350219747,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.656078720273404,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.5616593069252485,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.154629324419856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.903368397808849,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.197037734043075,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.622228000680881,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.16857147216796875,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0421404157366077,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3300135414573795,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.37467165908719036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.988752869905209,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.0266749602568055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.VRT.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5045437806066213,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.10689249854131044,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.1699981689453125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.0500030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.014961497596410744,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.9810052460043082,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.9904060994685446,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.706717249768791,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6445917082021473,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.942077164385626,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.17529538097564856,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.03991647127232767,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.16500875292793094,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7557948908907495,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7662734018161208,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.4757415552384785,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8987779020346855,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.6677274227480559,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.05002930513578,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.5171993377461677,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2504997253417969,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.2715003967284986,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.012163085937515916,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3005450439453057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.21932666778565135,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0217361831665244,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7718999662748702,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.2259000592121274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6795535163095288,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.292771040809005,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7360413137602606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7313984411768448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.10071454729352602,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5971418108258923,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.015087074777731857,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2719921446231348,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5693060242303556,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.004952005820705,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLK.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.039213823921795066,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.24448171633342408,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.4300003051757812,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.23999786376953125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.5005513806651614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.304152783492075,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.360764977994001,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7927459379027724,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.3032327955414313,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.8190479899089063,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.9260858512251993,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.446266558449679,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.350504125333641,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.5293631386056337,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.584897675646425,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.0237216324330842,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.049046601708893,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.4553017517286637,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05135192706506686,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.031016308024162,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3334999084472656,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.6130002975463924,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11999549865723225,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7443410491943396,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11223474502563846,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5825839614868187,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.697105703826508,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.2081530945336825,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.4210876462829045,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8604531061029874,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.7079997154189073,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7818147811805574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.01285661969866081,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11142785208565864,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.06342455731314622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.15620523272728404,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.05341803232173,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.657760571128053,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLE.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.01754418210315134,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.22745516046499026,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1399993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.15999984741210938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.46457678985355466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.448601683201789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.4564010261709948,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.3545896293032378,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.08531669281877097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.783491225233358,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0019506870245443,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5768062586745448,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.31452953452203447,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.6738120383153476,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.6805337238234186,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.5855653238335496,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.6604971133486903,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5091414835957875,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.12721676286441275,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.9004766077992947,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09350013732910156,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.41900043487549254,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.029938659667969603,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.1641648101806652,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.004116821289059658,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.020502758026118784,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4294188148821654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.489822396935069,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1967851736400017,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5779938693406872,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.27043125201495766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2596824891863969,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0021427699497766906,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.012142998831612739,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0006305416492740079,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.018122402161748985,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.23991610388798223,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2741907669039261,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLF.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.13313588504735463,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2441239659713148,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.959991455078125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.1199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8464796798717478,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5029824113033765,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5034648994707069,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7801307488759188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3628921699804666,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3225104558868384,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.1617886643935922,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6330621201465441,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.6964324245402276,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2777720561898178,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2793322018182831,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.549155054345607,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3829216361869947,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.04816071424926793,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2870547402334598,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.110344986620385,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.060500335693348006,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.6365005493163949,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3580117797851585,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.863333435058621,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.03635879516602358,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.1897788238525493,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.606956855399654,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.040872680006677,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7639101008134253,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7022254731393294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5361588940384299,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5428137781728792,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.21928514753069184,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.08214351109095963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1398733826455305,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.05921200432641349,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5160964946388749,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6021153114806452,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLI.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04978606513953987,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.46904184742921473,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.100006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.6400146484375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05578207507617172,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.429829084831203,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.4225321856260695,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.344369111132742,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2663926765043012,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.895629649958396,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.14966322427891754,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.39384486431919363,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09426518025534847,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.655039439944762,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.6466648832784934,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -7.575344805663054,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.47942112966315964,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.169979391595967,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0243971484390482,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.8711277307930327,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.42249984741212643,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.331000518798845,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.25533752441407387,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2385934448242324,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11898307800294106,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5970688629150516,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3105327091151855,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.784010550148274,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2146174008834878,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1381746789518976,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.14991637448506978,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8427908526867682,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1071428571428572,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.03999982561383897,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05883068474078068,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.016296581222992268,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05516056361404287,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1693383013189118,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLV.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.007237024419321725,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.07393943517108215,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.80999755859375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5999984741210938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5809620820330985,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.540066460881473,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.5437520739505661,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.912286626727669,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.42799417350345426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.4073359479418892,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.727705892503816,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.10200679520158129,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4309148267015783,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.7652768159950316,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.76788477160299,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.14326232125798,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.173807979670915,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8670137936956817,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1470280316563155,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.3752760712722587,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2650001525878878,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.507500457763669,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.06046569824219716,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.33433837890625284,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.04699031829834155,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.29347640991211676,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.2791736040795199,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.5771173857006113,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.036914020320423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.127844957046431,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0300195261116363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.090090795611398,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.024999891008649522,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2935703822544644,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.043313104273529746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.34561007688171763,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.9000973195042783,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.155902217255213,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLP.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05525802109285716,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3341428505961582,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1899948120117188,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.0500030517578125,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.01583549657431238,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.13286460376142895,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.13143818103558136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.837880948758098,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9461792606607622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.949828772870422,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7601397467610793,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.5534929237614055,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.16588275190583257,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.09234575135212975,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.09269451661684247,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.0688566432884095,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.20036545449330134,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.6754790312328516,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.11459417739905176,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.076210057287566,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3149997711181669,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.18349990844726,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.02086868286133381,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3176446533203148,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.040956420898439205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.16241836547851562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7723652200385622,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1349292443958436,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0696913328452906,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.24126250384184367,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0675694264731694,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.09760772096139014,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.019285474504743494,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11214283534458724,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.0020325171961510513,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.09771049186289238,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9950072612086251,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.04180976175645057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLY.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.12230705362975258,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.23494284491836814,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.26999664306640625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.6100006103515625,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.3133268836205136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.3508274607508355,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.33064189542084677,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.137315245769791,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.48522296729484093,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.136186515850781,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.9234380109562363,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -9.350338821751624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4633741389520338,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5760378158643942,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5547745930732706,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.368290940300103,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.2310367734623027,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.410536257488352,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.0487040867961053,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -6.873055955277785,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3944999694824247,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.6414997100830107,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.13751922607421818,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5339491271972605,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.06632431030273267,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2646113586425827,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09287721049915376,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.543071897773843,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.12746128969527426,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.474884963778536,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.18553017392320914,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.642541522145816,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.019999912806919706,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11285781860351562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.014879385656025423,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.20346032513382561,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2352911922147385,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -5.760349115774789,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLC.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.33500013888910285,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.41595539502300405,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2999992370605469,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9699974060058594,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7285523577472919,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5522033745726906,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5610375493676711,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.2922465518770307,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.500314594088592,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.576455001510871,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6594631316503174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.950901131767316,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8785996130788121,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7774137296862493,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.785170247020095,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0612708573467189,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.2461284002560538,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.3021052598733003,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5341970558104485,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.428183998241156,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.15699996948242045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7624999999999957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.020150451660157387,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.11128349304199503,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.006046047210695349,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.02592117309570341,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.33345222586407264,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.44643103097044,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7694494347032066,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.5960370621701534,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6716990020721569,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.1585635377536554,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.009285790579659614,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.07428550720214844,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03196591754362221,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2106963293159947,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.210950932451838,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.514298168897057,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLU.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09475177158054049,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.018417995753788663,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.05999755859375,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.381408451727295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.5449936596028344,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.570215288910793,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.1732734721091154,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8457950680549331,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.9432078785228133,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0366820760477786,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.3328420953222064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.231361196395775,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.770204014716393,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.794347986563217,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.4042491666394272,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.5916088742223944,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.6688581368852429,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.1619481518876471,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.8101249617960464,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.05499992370605611,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.2324998855590863,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04031608581543367,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.19064041137695398,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.014463710784916373,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.07468448638915959,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.0001844619759837,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.42710772682454934,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7499513103065847,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5838580937830407,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.876451371107001,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.03325120906946255,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.006071363176618383,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.019142968314034614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0015903803080095091,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.04304992732215651,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.44183667535624416,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.4644072830234052,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLRE.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.2643114366182472,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.03115514262420782,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3999977111816406,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5499992370605469,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6420835196201624,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.22895258275665853,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2296229563087726,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.963415576257188,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5973238537618117,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.07293206626258,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.37601053035303256,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8292352531638079,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7921307749516826,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.003742227643099838,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.005490258656348779,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.1943912707874995,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8515100475943504,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.7985823246250097,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.49872339380709896,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.306518119637648,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.1340000152587848,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.45750007629393963,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.004413909912109659,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.08451278686523267,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.02065967559814652,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11979507446289261,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5231222752005493,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.15620349497127428,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7950279943219174,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2481332526245836,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7481943160199345,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.8459704182436356,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.013571330479213217,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.08214323861258377,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.03611116717298257,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.17371525874772553,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.7487209044773069,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.0294957064061805,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XLB.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.18493285760235245,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0568434548975848,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 16.3599853515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 11.6199951171875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.28536369763745295,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.4034621848468727,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.3739351734409118,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 9.22739543935084,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6708638221012428,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.9976381709412294,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.093655080838097,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.694537477836201,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.43541095296897314,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.178251829733314,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.149802475788488,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.996419744820527,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9250500159337811,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7232884293036594,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.9683890049982287,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.17182034431004,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.4460021972656705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -15.427502441406318,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7218005371094023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.438400878906236,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8437998962402844,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.942099914550795,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.211736454769476,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.442055226024888,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.97166174219683,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.7581118117977144,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.9926289885930046,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.4354804469445481,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3199986049107153,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.5521458217075903,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.046038655422110164,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3931019494419208,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.5808463040657994,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8330958620688342,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SMH.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.27553441258611944,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.042262253100773806,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3899993896484375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.849998474121094,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.37327484552143186,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.536757791918574,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5591457022684265,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 8.184984926860972,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.5815147284414124,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.065935222553986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.0330100348719746,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.881518742635027,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.22322759018991167,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.7619681470321327,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7832783999208504,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.954009232330661,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.16429907772604935,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.791585480916416,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.158276110711842,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.40423587616118617,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.32799987792969887,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9694995880126953,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.19580001831054972,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6389999389648438,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.033998413085939205,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.13584133148194155,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.049851695110092464,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.564005411837279,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.17357675816844775,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.943465474336394,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.37243777438682457,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.001109447926089,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.01714379446847092,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.04857145036969879,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.024366858997358687,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.07085794340151752,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.346143069127991,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.304605088258429,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.IGV.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.2767027492297245,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.44890811800456376,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -4.850006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.040008544921875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.9391914877251466,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.6582448980588813,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.722159675738234,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.13510072319784516,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.7537928038994224,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8152408616053606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7184136952219209,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -3.567348991977859,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.7891442323936264,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.88345525317244,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.9462923733906576,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.366076417728157,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.499606610066884,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5408911199677906,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.15632022893821151,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.090066125504018,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.0689994812011605,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.773999786376947,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3477630615234375,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.1212829589843807,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.37115173339844887,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8883946609497286,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.0785850114390723,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.61282916232064,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.7433775231528346,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.2041553105108793,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -3.1473450797046887,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.369865598894382,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09500013078962066,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3878598894391745,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.10767927384916431,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.19439935552866006,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.367473439942258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.2027854356437837,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.XOP.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.17697651585040808,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.32260216654448925,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 6.470001220703125,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 23.97998046875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.33947976301422766,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.6675697849343751,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7434333075449615,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.661916638564625,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 4.288723992160448,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 10.098083662716062,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.426529859178994,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.202443295439265,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.48952701834574786,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.4423594298208164,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5193006098925377,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.4309409440343135,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.542910185992987,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 8.823733921078492,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 3.3012637833391256,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 9.679726161913106,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4304992675781705,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.2809967041015966,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.35460021972659206,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.1566003417968886,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4569499206542673,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.0935998535156273,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.2843727520637227,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.8556887742047365,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.6990529060822324,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.481463763341965,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.5153963435203588,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.5351954679123345,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4335719517299097,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.6328539167131702,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15210432341948676,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.25235491471961957,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.4819738466486427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.492688901528631,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.OIH.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0849530290467504,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11338306840817158,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.94000244140625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.07000732421875,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.8915790224654847,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.32117620706593186,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.3227497754153208,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.0199591654582285,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.46804083780451755,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.1966543914307413,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.6401646614624283,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.717695172036592,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.7415317671339645,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.09596585195237317,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.09861707776289697,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.2509348599885404,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.2138546439719788,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.9223046497931708,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.765430737302296,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.7595876944372506,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15400009155271732,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.6584999084472543,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.8937826538085858,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.605876159667957,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.13083091735839503,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5737717437744152,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.38093504062455263,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.8318805858009148,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04109884437415445,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.0122922052903665,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3588427153796374,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.25558433491240606,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15857151576450956,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6285705566406246,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.06761199658892969,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3042407426093654,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.3716499904589874,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0276788870239848,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ITA.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.12908495686578836,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.28378656361865007,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6700000762939453,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7600002288818359,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.1148514737702397,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.054251713660604,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.0603980889316142,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.852298125389599,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.5410805359731286,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.575382126517624,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.9689392914095096,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2908376362899312,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.26489872910176,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.8290413585470455,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.8362653912791904,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.621322430859287,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.7952667298056664,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.301032384880054,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.09420536724937811,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.1864452301839084,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0539999961853006,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.5547499656677246,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.07720001220702954,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.4495999908447246,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.012999992370602342,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.05575001716613315,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.311135072001158,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.1123157138838735,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.325569685486262,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.6869764711514703,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 2.0961373256541567,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.493824625480878,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.008928435189383355,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.053571564810616645,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08413521502833365,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.11604390833937117,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.9219737939275667,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.180149786503904,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.ARKX.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.4628281108113228,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.8230597693718444,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.15000152587890625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 1.9599990844726562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5788696316187614,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.1698605374847246,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.234692127408322,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.5165034324449369,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.8481279825205412,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.73880916446131,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -1.4437101743293934,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.6785347924976648,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4288223762872412,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -2.3950708925982833,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.458824825060746,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.714472262085375,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.10231417635307993,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.46445942282374,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5689762501692623,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.155817658971504,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.13750000000000284,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.37750015258789915,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08743438720703978,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.48533691406250057,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.03128726959228345,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.15232463836669297,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.41633263936673437,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.2462893655262883,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.08580055650042606,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 3.3806924705705788,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.25968542751149126,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.571819219988236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.0450003487723214,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.08071517944335938,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.05836173429104852,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.16154803759264613,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.19357867411062735,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 2.5294010964699414,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.KRE.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.04992327665487428,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.2962017691671076,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 1.600006103515625,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 8.120010375976562,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_1d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.5518300596088377,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.46107033857272217,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_5d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.47947477499246105,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 9.740359769658236,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_20d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.796807206909933,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 7.771271843007687,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.return_60d_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.9162002724497427,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -4.377388790750157,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_1d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.4017828042773175,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.6862806936862809,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_5d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -0.7036074726448849,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 8.509384075127924,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_20d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.05099340074247216,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 6.496922101370117,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.relative_spy_60d_pp",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.0414663482896103,
        "unit": "pp"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -1.9001059242763159,
        "unit": "pp"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma20",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.43550033569337643,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.7645011901855412,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma50",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.18440002441406023,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.38980041503907614,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.sma200",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.21255004882812045,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.959500045776366,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma20_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.690498045384258,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.3971312683269375,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma50_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.857001699922133,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.7017339645705984,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.distance_sma200_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9813227551379136,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 5.119133917747252,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_sma",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.045000348772321175,
        "unit": "USD_per_share"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.3235746111188611,
        "unit": "USD_per_share"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.atr14_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": -2.8825060689463555e-06,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.05826715704334973,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.drawdown_from_63d_high_pct",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.9148642627363035,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 4.642924354917222,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "prices.SKYY.volume_vs_previous20_ratio",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.6667491748414454,
        "unit": "ratio"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": -0.05960216026668408,
        "unit": "ratio"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS2.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.010000000000000675,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": -0.08999999999999986,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLH0A0HYM2.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.08000000000000007,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.009999999999999787,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.BAMLC0A0CM.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-23",
        "to": "2026-10-26",
        "change": -0.010000000000000009,
        "unit": "percentage_points"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-19",
        "to": "2026-10-26",
        "change": 0.030000000000000027,
        "unit": "percentage_points"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DGS10.value",
    "available_prior_observations": 7,
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
        "change": -0.15000000000000036,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.DFII10.value",
    "available_prior_observations": 7,
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
        "change": -0.13999999999999968,
        "unit": "percent"
      }
    ],
    "status": "comparable"
  },
  {
    "id": "macro.T10YIE.value",
    "available_prior_observations": 7,
    "changes": [
      {
        "prior_distinct_observations": 1,
        "from": "2026-10-26",
        "to": "2026-10-27",
        "change": 0.010000000000000231,
        "unit": "percent"
      },
      {
        "prior_distinct_observations": 5,
        "from": "2026-10-20",
        "to": "2026-10-27",
        "change": 0.0,
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
  }
]
```

## 判断依据 · 恐慌还是过热？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 恐慌还是过热？ |
| 事实指标引用 | ["macro.BAMLH0A0HYM2.value", "macro.DGS10.value", "prices.^VIX.value", "prices.^MOVE.value"] |
| 推断与解释 | 恐慌缓和，盘前VIX低位但油价风险回升；Fed未公布，不能认定风险解除。 |
| 反证与缺口 | 信用滞后，原油触及门槛合约上行；高AI订单并不能消除融资风险。 |
| 确认条件 | 信用与波动持续上行、成分广度同步恶化。 |
| 失效条件 | 油价风险消退、信用改善且股市承接恢复。 |
| 观察期限 | 未来1–2周 |
| 条件式指导 | 避免仅凭VIX未到极端就认定安全。 |
| 主观置信等级 | medium |
| 判断变化原因 | 没有新完整交易日；新增SK海力士/VRT财报、半导体盘前走强与原油风险报价上升。日线及较慢宏观指标未重复当成新信号。 |

## 判断依据 · 反弹是否可靠？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 反弹是否可靠？ |
| 事实指标引用 | ["prices.QQQ.distance_sma20_pct", "prices.SMH.distance_sma20_pct", "prices.SPY.distance_sma20_pct", "prices.RSP.return_1d_pct", "prices.RSP.return_5d_pct"] |
| 推断与解释 | 27日收盘修复有效，28日盘前半导体更强；缺金融/小盘同步，常规确认未发生。 |
| 反证与缺口 | 量能未扩大；META放量下跌，STX/NXPI盘后回落；没有完整广度/VWAP。 |
| 确认条件 | QQQ722.87、SMH559.81（27日高点）开盘回踩守住并重新走高，SPY突破771.14，等权/金融加入；观察首30–60分钟的更高低点和可得常规VWAP，再看Fed公布后及收盘。进一步QQQ724.92/SMH573.45为27日50日均线参考，会动态变化。 |
| 失效条件 | 高开后跌回QQQ721.25、SMH557.98、SPY769.66昨收，反抽不能收复，先降级；跌破QQQ713.59、SMH546.67、SPY765.21昨日低点属于更强失效。不是必须等最远止损才降风险。 |
| 观察期限 | 未来1–5交易日 |
| 条件式指导 | 等待确认后分批试探，不把一次拉升当趋势。 |
| 主观置信等级 | medium |
| 判断变化原因 | 没有新完整交易日；新增SK海力士/VRT财报、半导体盘前走强与原油风险报价上升。日线及较慢宏观指标未重复当成新信号。 |

## 判断依据 · 优先观察哪些板块？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | 优先观察哪些板块？ |
| 事实指标引用 | ["prices.IGV.return_5d_pct", "prices.SMH.relative_spy_5d_pp", "prices.XLE.return_1d_pct", "prices.OIH.volume_vs_previous20_ratio"] |
| 推断与解释 | 软件云跨期领先，半导体五日转领先；能源和金融当天偏弱，行业之间分化。 |
| 反证与缺口 | ICI只是至21日的全市场估计净发行，无19ETF实时申赎；股价上涨不是主力净流入。 |
| 确认条件 | 相对SPY持续领先，回踩守住，订单/利润或发行人申赎补证。 |
| 失效条件 | 领涨消失、跌破回踩低点或经营逻辑证伪。 |
| 观察期限 | 未来一周 |
| 条件式指导 | 先看强势无杠杆篮子，避免同时集中多个同一风险链。 |
| 主观置信等级 | medium |
| 判断变化原因 | 没有新完整交易日；新增SK海力士/VRT财报、半导体盘前走强与原油风险报价上升。日线及较慢宏观指标未重复当成新信号。 |

## 判断依据 · AI需求与估值如何区分？

| 要素 | 记录 |
| --- | --- |
| 评估问题 | AI需求与估值如何区分？ |
| 事实指标引用 | ["prices.NVDA.return_1d_pct", "prices.CRWV.distance_sma20_pct", "prices.MU.return_1d_pct"] |
| 推断与解释 | 存储与散热新财报支持实际需求，仍应分别评估估值、融资和资本回报。 |
| 反证与缺口 | 部分业绩股仍跌，META融资桥未完整，单公司利润率不是全行业长期利润率。 |
| 确认条件 | 企业自由现金流、融资与价格承接同步改善。 |
| 失效条件 | 订单/指引下修、资本投入长期超过现金生成且融资收紧。 |
| 观察期限 | 下一季度并每日跟踪风险 |
| 条件式指导 | 用公司整体FCFF情景，保留META输入缺口。 |
| 主观置信等级 | medium |
| 判断变化原因 | 没有新完整交易日；新增SK海力士/VRT财报、半导体盘前走强与原油风险报价上升。日线及较慢宏观指标未重复当成新信号。 |

## 存储需求获新财报支持，价格仍分化 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | SK海力士28日披露初步Q3收入104.6155万亿韩元、营业利润83.3338万亿、营业利润率约80%；2027–28年超过一半产能已有长期协议。数字为公司K-IFRS初步披露，尚未完成独立审计。 |
| 事实：市场反应 | 约12:00–12:05UTC盘前，MU962.40（较27日收盘+3.62%）、SNDK1365.26（+4.63%）、DRAM52.6221（+4.16%）、SMH564.18（+1.11%）；STX653.23仍−2.19%，NXPI235仍−7.30%。 |
| 推断：解释 | 推断：DRAM/HBM需求并未呈现普遍盈利坍塌，但股票仍受预期定价影响。半导体、硬盘和闪存不是同一盈利周期。缺少中国厂商新增份额/成交价证据，不能把所有跌幅归于低价竞争。 |
| 受益篮子 | ["SMH", "MU", "SNDK观察篮子"] |
| 受损篮子 | ["高估值且无法兑现现金流者"] |
| 反证 | SK海力士高利润不能外推每家企业或永久供需；长期协议不等于全部现金已收取。STX/NXPI仍下跌，盘前成交不能证明常规承接。 |
| 下一催化剂 | 28日常规开盘承接；29日SNDK财报 |
| 证据 | ["https://news.skhynix.com/en/q3-2026-business-results/", "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-First-Quarter-2027-Financial-Results/default.aspx", "https://investors.nxp.com/news-releases/news-release-details/nxp-semiconductors-reports-third-quarter-2026-results"] |

## 电力散热：财报兑现成为独立观察线 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Vertiv公司发布Q3收入43.13亿美元，同比增长61%；调整后EPS2.21、调整后自由现金流6.52亿美元，并上调全年指引。GEV上调指引的报道已核对财经来源，官方详细正文受限，具体数据仅作二级线索。 |
| 事实：市场反应 | 12:05UTC附近VRT240.46，较208.56收盘+15.30%；GEV911.59，较895.08收盘+1.84%；CEG262，约+1.17%。 |
| 推断：解释 | 推断：市场更愿意奖励可交付订单和现金流，但高开会提高短期预期门槛；先检验开盘后卖压。 |
| 受益篮子 | ["VRT", "GEV", "CEG观察篮子"] |
| 受损篮子 | ["订单无法变现或投入回报弱者"] |
| 反证 | 盘前报价不代表常规成交深度；不同公司的能源/数据中心业务占比不同。GEV并购和预测数字不作为独立核验后的估值输入。 |
| 下一催化剂 | VRT28日11:00纽约电话会，随后常规收盘；GEV交付与现金流更新 |
| 证据 | ["https://www.prnewswire.com/news-releases/vertiv-reports-strong-third-quarter-2026-with-net-sales-growth-of-61-organic-orders-growth-over-100-and-diluted-eps-growth-of-91-adjusted-diluted-eps-growth-of-78-raises-full-year-2026-guidance-across-all-key-metrics-302921936.html", "https://ca.investing.com/news/earnings/ge-vernova-stock-gains-on-earnings-beat-raised-guidance-4908455", "https://www.gevernova.com/investors"] |

## AI融资由能筹钱转向谁承担信用风险 · 新增

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 博通27日8-K披露26日安排：客户租赁违约时，责任以未偿租赁额72.5%减资产处置回收计算；全部部署后最高未折现潜在责任约430亿美元。 |
| 事实：市场反应 | META收620.19、−1.64%，量能2.61倍；跌破625发行参考价。NVDA+0.90%，AI链条分化。 |
| 推断：解释 | 推断：订单可见度应与客户支付能力、设备残值和出资方责任一起审视；融资打通不等于终端回报验证。 |
| 受益篮子 | ["有现金转换和客户信用保障者"] |
| 受损篮子 | ["融资和设备残值敏感者"] |
| 反证 | 430亿美元是满足部署条件后的最大潜在金额，不是当期损失或已全部借款；公司认为触发概率低属于管理层判断。 |
| 下一催化剂 | 融资交割、客户付款和后续担保披露；Meta是否收复625/627.80 |
| 证据 | ["https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |

## 云与算力：增长和替代竞争并存 · 强化

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | Oracle和Google宣布OCI提供Google TPU，计划2027年推出并多年扩张；康宁已公布光通信收入同比+44%。 |
| 事实：市场反应 | IGV+0.35%、SKYY+0.94%，五日分别+4.54%、+4.97%；MSFT−0.24%，仍有个股分化。 |
| 推断：解释 | 推断：多种芯片支持算力需求，也可能改变供应商份额和单位经济性；不能把未来计划当今天收入。 |
| 受益篮子 | ["IGV", "SKYY", "ORCL", "GOOGL", "光互连篮子"] |
| 受损篮子 | ["定价权被替代方案削弱者"] |
| 反证 | TPU合作未给出可核验的本季收入/利润贡献；H100租金只反映单一型号。 |
| 下一催化剂 | 28日Oracle投资者日、微软财报；Alphabet日程待官方页面恢复核验 |
| 证据 | ["https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/", "https://cloud.google.com/blog/products/infrastructure/bringing-google-tpus-to-oracle-cloud-infrastructure", "https://www.stocktitan.net/news/GLW/corning-delivers-outstanding-third-quarter-results-ijv492ou5imj.html"] |

## 原油风险回升，核电与油气驱动分开 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | DOE27日宣布对Constellation最高50亿美元有条件贷款承诺，拟支持约1.1GW核电增容；地缘谈判与供应风险同时存在。 |
| 事实：市场反应 | 12:00UTC附近XLE68.43，仍低于旧支撑68.62；11:50UTC延迟WTI101.77、Brent111.29，连续合约仅作水平。 |
| 推断：解释 | 推断：航运风险与AI电力需求并行，不能把油气、油服与核电都归入同一个方向。 |
| 受益篮子 | ["政策支持的核电项目观察篮子"] |
| 受损篮子 | ["油价回落下上游高敏感者"] |
| 反证 | Reuters转引的周末航运数据属于此前周末，不是28日实时流量。tc关于最新美军航运警告未找到同日官方公告，保持未核验；DOE贷款有条件。 |
| 下一催化剂 | 正式放款/工程进度；地缘供应与航运证据 |
| 证据 | ["https://www.energy.gov/articles/fact-sheet-energy-department-delivering-president-trumps-commitment-expand-american", "https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp"] |

## 金融、工业和航天：扩散未整齐 · 待核验

| 主题要素 | 内容 |
| --- | --- |
| 事实：发生了什么 | 波音Q3已披露现金流改善但核心EPS仍亏损；Virgin Galactic计划28日转场为试飞准备，商业飞行仍有延期风险。 |
| 事实：市场反应 | XLF−0.25%、KRE−0.21%、XLI+0.58%、ITA−0.45%、ARKX+2.22%；IWM+1.15%但等权RSP仅+0.11%。 |
| 推断：解释 | 推断：小盘参与有利修复，银行/工业/航天仍须逐项验证，指数不是公司项目完成证明。 |
| 受益篮子 | ["现金转换改善的工业", "可核验交付的航天"] |
| 受损篮子 | ["持续延期或融资敏感公司"] |
| 反证 | 金融没有同步确认；转场计划不等于已经完成或商业收入兑现。 |
| 下一催化剂 | 28日Fed、SPCE转场进度；29日GDP/PCE |
| 证据 | ["https://boeing.mediaroom.com/2026-10-27-Boeing-Reports-Third-Quarter-Results", "https://www.virgingalactic.com/news/virgin-galactic-sets-october-28-for-lead-delta-class-spaceships-arrival-at-spaceport-america", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |

## tc 报价（供应商时戳不等于成交时戳）

| 标的 | 价格 USD | 变化% | 观测时间 | 供应商时间 | 抓取时间 | 质量 |
| --- | --- | --- | --- | --- | --- | --- |
| AMZN | 253.30 | 0.08 | 2026-10-28T12:00:12+00:00 | 2026-10-28T12:00:12+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| AVGO | 348.05 | 1.67 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| CEG | 262.00 | 1.17 | 2026-10-28T11:58:32+00:00 | 2026-10-28T11:58:32+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| DRAM | 52.62 | 4.16 | 2026-10-28T12:05:03+00:00 | 2026-10-28T12:05:03+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| GEV | 911.59 | 1.84 | 2026-10-28T12:04:46+00:00 | 2026-10-28T12:04:46+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| GLD | 370.73 | -0.42 | 2026-10-28T11:58:07+00:00 | 2026-10-28T11:58:07+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| GLW | 128.81 | 1.99 | 2026-10-28T12:00:07+00:00 | 2026-10-28T12:00:07+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| GOOGL | 324.69 | 1.28 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| IGV | 111.18 | -0.54 | 2026-10-28T11:36:00+00:00 | 2026-10-28T11:36:00+00:00 | 2026-10-28T12:05:14.584197+00:00 | stale |
| IWM | 279.50 | -0.24 | 2026-10-28T11:59:56+00:00 | 2026-10-28T11:59:56+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| META | 620.58 | 0.06 | 2026-10-28T12:00:24+00:00 | 2026-10-28T12:00:24+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| MSFT | 529.00 | -0.44 | 2026-10-28T12:00:06+00:00 | 2026-10-28T12:00:06+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| MU | 962.40 | 3.62 | 2026-10-28T12:05:07+00:00 | 2026-10-28T12:05:07+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| NVDA | 219.61 | 0.77 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| NXPI | 235.00 | -7.30 | 2026-10-28T11:44:17+00:00 | 2026-10-28T11:44:17+00:00 | 2026-10-28T12:05:14.584197+00:00 | stale |
| ORCL | 131.56 | 0.79 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:00:29+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| QQQ | 723.90 | 0.37 | 2026-10-28T12:00:27+00:00 | 2026-10-28T12:00:27+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| RSP | 217.22 | -0.14 | 2026-10-28T11:37:28+00:00 | 2026-10-28T11:37:28+00:00 | 2026-10-28T12:05:14.584197+00:00 | stale |
| SMH | 564.18 | 1.11 | 2026-10-28T12:00:28+00:00 | 2026-10-28T12:00:28+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| SNDK | 1,365.26 | 4.63 | 2026-10-28T12:00:25+00:00 | 2026-10-28T12:00:25+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| SPY | 770.67 | 0.13 | 2026-10-28T12:00:10+00:00 | 2026-10-28T12:00:10+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| STX | 653.23 | -2.19 | 2026-10-28T12:00:27+00:00 | 2026-10-28T12:00:27+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| TLT | 81.41 | -0.27 | 2026-10-28T12:00:14+00:00 | 2026-10-28T12:00:14+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| VRT | 240.46 | 15.30 | 2026-10-28T12:05:05+00:00 | 2026-10-28T12:05:05+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |
| XLE | 68.43 | 0.33 | 2026-10-28T11:48:57+00:00 | 2026-10-28T11:48:57+00:00 | 2026-10-28T12:05:14.584197+00:00 | stale |
| XLF | 55.52 | -0.64 | 2026-10-28T11:50:13+00:00 | 2026-10-28T11:50:13+00:00 | 2026-10-28T12:05:14.584197+00:00 | ok |

## 核心行情与风险代理

| 标的 | 价格/指数 | 单位 | 观测日 | 1日% | 5日% | 20日% | 质量 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SPY | 769.66 | USD_per_share | 2026-10-27 | 0.56 | 0.08 | 0.71 | ok |
| QQQ | 721.25 | USD_per_share | 2026-10-27 | 1.27 | 0.50 | -2.26 | ok |
| IWM | 280.18 | USD_per_share | 2026-10-27 | 1.15 | 1.60 | 0.42 | ok |
| RSP | 217.52 | USD_per_share | 2026-10-27 | 0.11 | 0.77 | 3.83 | ok |
| GLD | 372.28 | USD_per_share | 2026-10-27 | 1.21 | -1.42 | -2.77 | ok |
| GC=F | 4,074.60 | USD_per_troy_ounce | 2026-10-27 | 0.90 | -1.64 | -2.51 | ok |
| CL=F | 99.90 | USD_per_barrel | 2026-10-27 | -1.83 | -1.86 | 11.77 | ok |
| BZ=F | 113.88 | USD_per_barrel | 2026-10-27 | -1.67 | 4.68 | 11.00 | ok |
| TLT | 81.63 | USD_per_share | 2026-10-27 | -0.06 | 1.87 | 4.77 | ok |
| UUP | 29.12 | USD_per_share | 2026-10-27 | 0.38 | 0.76 | 1.29 | ok |
| HYG | 77.60 | USD_per_share | 2026-10-27 | 0.52 | 1.00 | 0.76 | ok |
| LQD | 104.30 | USD_per_share | 2026-10-27 | 0.27 | 1.05 | 2.28 | ok |
| ^VIX | 17.52 | index | 2026-10-27 | -4.73 | 1.21 | 9.23 | ok |
| ^VIX3M | 19.57 | index | 2026-10-27 | -1.86 | 3.05 | 8.18 | ok |
| ^VVIX | 99.45 | index | 2026-10-27 | -1.95 | 2.37 | 10.86 | ok |
| ^MOVE | 97.87 | index | 2026-10-27 | -4.23 | -3.77 | -3.88 | ok |
| NVDA | 217.94 | USD_per_share | 2026-10-27 | 0.90 | 0.68 | -4.08 | ok |
| MSFT | 531.33 | USD_per_share | 2026-10-27 | -0.24 | -0.10 | 4.40 | ok |
| AMZN | 253.10 | USD_per_share | 2026-10-27 | 1.61 | -3.63 | 2.61 | ok |
| GOOGL | 320.58 | USD_per_share | 2026-10-27 | 1.19 | -5.79 | -5.97 | ok |
| META | 620.19 | USD_per_share | 2026-10-27 | -1.64 | -10.67 | -16.05 | ok |
| CRWV | 59.57 | USD_per_share | 2026-10-27 | 7.94 | -4.12 | -30.68 | ok |
| MU | 928.76 | USD_per_share | 2026-10-27 | 2.77 | 3.65 | -12.79 | ok |
| DRAM | 50.52 | USD_per_share | 2026-10-27 | 4.53 | 5.87 | -17.57 | ok |
| VRT | 208.56 | USD_per_share | 2026-10-27 | 4.39 | 2.46 | -16.02 | ok |

## 跨资产风险解释

判断仍是恐慌缓和后的修复，不是全面过热。27日收盘VIX17.52（本次Cboe已更新至27日）、VIX3M19.57、VVIX99.45、MOVE97.87，期限结构正常；28日11:45UTC VIX17.45是盘前延迟读数，不与旧VIX3M混算。26日FRED2年4.68%、10年5.00%、实际10年2.66%、HY330bp/IG90bp仍有滞后；27日盈亏平衡2.35%。28日盘前GLD370.73、TLT81.41均低于昨收，不能证明全面避险解除。11:50UTC WTI101.77/Brent111.29仅作连续合约水平，较早报同数据接口读数提高，但换月未对齐，不使用机械日线跌幅。GPR26日165.25、7日181.42及STLFSI16日−0.6328反映较慢背景。CNN418和CME当前矩阵缺失。Fed28日14:00纽约决定、14:30记者会尚未发生；持平预期高不等于表态鸽派。

## 宏观与地缘风险指标

| 指标 | 数值 | 单位 | 观测日 | 20次观测变化 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- | --- |
| DGS2 | 4.68 | percent | 2026-10-26 | -0.13 | lagged | https://fred.stlouisfed.org/series/DGS2 |
| BAMLH0A0HYM2 | 3.30 | percentage_points | 2026-10-26 | 0.28 | lagged | https://fred.stlouisfed.org/series/BAMLH0A0HYM2 |
| BAMLC0A0CM | 0.90 | percentage_points | 2026-10-26 | 0.07 | lagged | https://fred.stlouisfed.org/series/BAMLC0A0CM |
| DGS10 | 5.00 | percent | 2026-10-26 | -0.17 | lagged | https://fred.stlouisfed.org/series/DGS10 |
| DFII10 | 2.66 | percent | 2026-10-26 | -0.17 | lagged | https://fred.stlouisfed.org/series/DFII10 |
| T10YIE | 2.35 | percent | 2026-10-27 | 0.01 | ok | https://fred.stlouisfed.org/series/T10YIE |
| STLFSI4 | -0.63 | index | 2026-10-16 | 0.04 | lagged | https://fred.stlouisfed.org/series/STLFSI4 |
| CBOE_VIX | 17.52 | index | 2026-10-27 | 1.48 | ok | https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv |
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
| XLK | 科技 | 1.70 | 2.18 | -2.58 | 1.14 | 2.10 | -3.29 | 0.87 | 2026-10-27 |
| XLE | 能源 | -2.05 | 0.35 | 10.84 | -2.61 | 0.27 | 10.12 | 0.99 | 2026-10-27 |
| XLF | 金融 | -0.25 | 0.29 | 3.46 | -0.81 | 0.21 | 2.75 | 0.77 | 2026-10-27 |
| XLI | 工业 | 0.57 | 0.67 | -0.72 | 0.01 | 0.59 | -1.43 | 0.84 | 2026-10-27 |
| XLV | 医疗 | -0.06 | -0.36 | 4.95 | -0.62 | -0.44 | 4.23 | 0.90 | 2026-10-27 |
| XLP | 必需消费 | -0.92 | -0.68 | 6.48 | -1.48 | -0.76 | 5.76 | 0.92 | 2026-10-27 |
| XLY | 可选消费 | 1.04 | -0.04 | 5.77 | 0.48 | -0.12 | 5.06 | 0.82 | 2026-10-27 |
| XLC | 通信 | -0.26 | -6.00 | -7.08 | -0.82 | -6.08 | -7.79 | 1.10 | 2026-10-27 |
| XLU | 公用事业 | 0.71 | 2.32 | 7.91 | 0.14 | 2.24 | 7.19 | 0.48 | 2026-10-27 |
| XLRE | 房地产 | -0.84 | 0.14 | 2.66 | -1.40 | 0.06 | 1.95 | 0.90 | 2026-10-27 |
| XLB | 材料 | 0.78 | 1.07 | 5.46 | 0.22 | 0.99 | 4.74 | 1.02 | 2026-10-27 |
| SMH | 半导体 | 3.02 | 2.13 | -8.06 | 2.46 | 2.05 | -8.78 | 0.94 | 2026-10-27 |
| IGV | 软件 | 0.35 | 4.54 | 6.23 | -0.21 | 4.46 | 5.52 | 1.00 | 2026-10-27 |
| XOP | 油气开采 | -2.37 | -0.02 | 11.97 | -2.93 | -0.10 | 11.25 | 1.04 | 2026-10-27 |
| OIH | 油服 | 1.61 | 6.23 | 7.52 | 1.05 | 6.15 | 6.81 | 0.72 | 2026-10-27 |
| ITA | 航空与国防 | -0.45 | 0.03 | -1.47 | -1.01 | -0.05 | -2.19 | 1.02 | 2026-10-27 |
| ARKX | 航天主题 | 2.22 | 2.53 | -3.38 | 1.66 | 2.45 | -4.10 | 0.97 | 2026-10-27 |
| KRE | 区域银行 | -0.21 | 2.78 | 3.94 | -0.77 | 2.70 | 3.22 | 0.79 | 2026-10-27 |
| SKYY | 云计算 | 0.94 | 4.97 | 5.35 | 0.38 | 4.89 | 4.64 | 1.31 | 2026-10-27 |

## 资金证据分层

完整19ETF按20日至27日同端点比较：五日OIH+6.23%、SKYY+4.97%、IGV+4.54%、KRE+2.77%、ARKX+2.53%、SMH+2.13%，SPY+0.08%；半导体从五日落后转为领先，但软件云仍较强。当天XLE−2.05%、XOP−2.37%、XLF−0.25%显示扩散不齐。QQQ/SMH/SPY量能0.83/0.93/0.70倍，并未全面放量。优先观察软件云的财报承接、半导体盘后卖压，工业金融作扩散验证；能源不能因地缘标题追涨。资金证据：ICI27日发布截至21日ETF估计净发行458.21亿美元，其中国内股票278.23亿美元；前周总额修订为532.61亿美元，窗口有滞后且无19板块分项。发行人VanEck本次页面超时，最近已核验窗口为26日，仅历史参考；无连续份额/拆分桥，不能由资产变动推净申购。盘前新变化：半导体与电力设备领先，XLF55.52低于55.88昨收、IWM279.50低于280.18昨收；RSP/IGV报价稀疏，不足判断广度。优先级：存储/半导体与电力散热的财报后承接，软件云等待今晚财报；金融工业是扩散验证。19ETF价格轮动不是19ETF主力净流入。

## 最近可核验 ETF 申赎窗口

| 标的 | 金额 USD million | 起始日 | 结束日 | 质量 | 来源 |
| --- | --- | --- | --- | --- | --- |

## Polymarket 搜索覆盖与限制

2026-10-28T12:09:06.088310+00:00：基础25主题与10组主动搜索Saudi oil attack、Microsoft earnings、Oracle AI、Sandisk earnings、AI bankruptcy、bank failure、recession、CPI November、Meta offering、Anthropic IPO。CPI/Meta/Anthropic截断；复核12项同rule_hash。未确认可直接代表VRT/SK海力士本季基本面或博通租赁担保的高质量合约。

## Polymarket · 值得警惕的信号

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["AI bubble burst in 2026?", "期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。", "https://polymarket.com/event/ai-bubble-burst-by"] | [7.9, {"status": "comparable", "change_pp": -0.20000000000000018}] | {"spread": 0.01200000000000001, "volume24h_usd": 13538.507858, "liquidity_usd": 32151.01246, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:59.762297+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["报价7.9%，24小时成交约13539美元，价差1.2个百分点；专门结算规则，不是股价胜率。", "AI估值与融资风险"] | ["同规则价格持续上行并有经营/信用证据", "现金流和信用改善"] | [null, null] |
| ["Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?", "10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。", "https://polymarket.com/event/what-price-will-wti-hit-in-october-2026"] | [39.5, {"status": "comparable", "change_pp": 13.5}] | {"spread": 0.02999999999999997, "volume24h_usd": 16143.888259999998, "liquidity_usd": 32470.2332, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:59.762297+00:00", "contract_end_at": "2026-11-01T03:59:59.999000+00:00"} | ["报价39.5%，24小时成交约16144美元，价差3个百分点；专门结算规则，不是股价胜率。", "能源成本→利率→成长估值"] | ["供应中断与可核验油价共同走强", "通行恢复及供应增加"] | [null, null] |
| ["Military action against Saudi Oil Pipeline (East-West) by October 31?", "截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。", "https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt"] | [13.5, {"status": "comparable", "change_pp": 3.0000000000000013}] | {"spread": 0.03, "volume24h_usd": 10766.281352, "liquidity_usd": 27628.1904, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:32.169280+00:00", "contract_end_at": "2026-10-31T20:59:00+00:00"} | ["报价13.5%，24小时成交约10766美元，价差3个百分点；专门结算规则，不是股价胜率。", "若管线或泵站实际受损，可能影响绕行出口能力，抬高能源成本。"] | ["沙特官方/独立来源证实直接命中与供应影响，且市场恢复交易后油价持续走强。", "只有已拦截导弹或警报解除，未发生合格命中；供应正常且价格回落。"] | [null, null] |

## Polymarket · 有参考价值的事件

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["US x Iran ceasefire continues through October 31?", "截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。", "https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt"] | [95.5, {"status": "comparable", "change_pp": 1.0000000000000009}] | {"spread": 0.010000000000000009, "volume24h_usd": 241150.531245, "liquidity_usd": 175451.8099, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:59.762297+00:00", "contract_end_at": "2026-10-31T23:59:00+00:00"} | ["报价95.5%，24小时成交约241151美元，价差1个百分点；专门结算规则，不是股价胜率。", "仅美国对伊朗领土合格打击的定义，与沙特/胡塞管线风险不同。"] | ["规则所列打击事实及资产反应共同核验。", "其他地区攻击不能自动算作该合约触发。"] | [null, null] |
| ["Strait of Hormuz traffic returns to normal by December 31?", "期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。", "https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31"] | [11.5, {"status": "comparable", "change_pp": 0.0}] | {"spread": 0.009999999999999995, "volume24h_usd": 32848.61534799999, "liquidity_usd": 341032.7698, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:59.762297+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["报价11.5%，24小时成交约32849美元，价差1个百分点；专门结算规则，不是股价胜率。", "IMF七日平均船舶到达不少于60，不能由单日放行新闻替代。"] | ["官方Portwatch连续数据达到定义。", "只出现局部绕行或有限通航。"] | [null, null] |
| ["Will Anthropic IPO by December 31, 2026?", "Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。", "https://polymarket.com/event/anthropic-ipo-by"] | [95.25, {"status": "comparable", "change_pp": 1.749999999999996}] | {"spread": 0.0010000000000000009, "volume24h_usd": 11818.132354, "liquidity_usd": 44780.8229, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:33.890317+00:00", "contract_end_at": "2027-01-01T04:59:00+00:00"} | ["报价95.25%，24小时成交约11818美元，价差0.1个百分点；专门结算规则，不是股价胜率。", "AI一级市场融资窗口与公开估值参照；不等于云供应商利润"] | ["官方招股文件、定价及交易所首日交易依次核验", "仅保密/公开申报、尚未挂牌交易；不以媒体时刻替代官方"] | [null, null] |

## Polymarket · 将要发生的事件及概率

| 合约 / 结算定义 | Yes % / 同规则跨期变化 | 质量与时点 | 入选原因 / 资产传导 | 确认 / 失效 | 事件时间 / 官方来源 |
| --- | --- | --- | --- | --- | --- |
| ["Will there be no change in Fed interest rates after the October 2026 meeting?", "以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。", "https://polymarket.com/event/fed-decision-in-october-20260617190323537"] | [94.95, {"status": "comparable", "change_pp": -0.7000000000000006}] | {"spread": 0.0010000000000000009, "volume24h_usd": 3965283.4029459995, "liquidity_usd": 1012198.74683, "quality_flags": [], "retrieved_at": "2026-10-28T12:00:59.762297+00:00", "contract_end_at": "2026-10-29T03:59:00+00:00"} | ["报价94.95%，24小时成交约3965283美元，价差0.1个百分点；专门结算规则，不是股价胜率。", "政策上限变化影响折现率"] | ["官方声明发布后核验", "会前预期不是实际决定"] | ["2026-10-28T14:00:00-04:00", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"] |
| ["Will Microsoft (MSFT) beat quarterly earnings?", "下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。", "https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82"] | [83.0, {"status": "comparable", "change_pp": 1.9999999999999907}] | {"spread": 0.18000000000000005, "volume24h_usd": 117.381039, "liquidity_usd": 83.4776, "quality_flags": ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"], "retrieved_at": "2026-10-28T12:00:59.762297+00:00", "contract_end_at": "2026-10-28T21:00:00+00:00"} | ["报价83%，24小时成交约117美元，价差18个百分点；专门结算规则，不是股价胜率。微软成交极低，18个百分点价差，大幅折价其信号价值。", "财报影响云/AI估值；EPS之外更须检查资本开支、自由现金流与指引。"] | ["官方首次披露GAAP EPS与专门规则核验，同时看指引与股价承接。", "EPS过线但现金回报/指引转差、股价失守；不可由合约直接推导交易方向。"] | [null, null] |

## Will there be no change in Fed interest rates after the October 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 606422 / 2589812 |
| Yes 概率 % | 94.95 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.25, 6.45] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.7000000000000006} |
| 24h成交量 / 流动性 USD | [3965283.4029459995, 1012198.74683] |
| 价差 pp | 0.10 |
| 到期 | 2026-10-29T03:59:00+00:00 |
| 结算规则摘要 | 以10月27–28日FOMC前后联邦基金目标区间上限不变结算；非25bp标准变动向上取整至25bp档；若下一会议期限仍无声明按不变档结算。 |
| 规则指纹 | fbc973610971c579003bb7db1464373da28fb0d8484ae204350268d22f83fb7e |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-october-20260617190323537 |

## US x Iran ceasefire continues through October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1038648 / 4641065 |
| Yes 概率 % | 95.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [2.0, 14.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.0000000000000009} |
| 24h成交量 / 流动性 USD | [241150.531245, 175451.8099] |
| 价差 pp | 1.00 |
| 到期 | 2026-10-31T23:59:00+00:00 |
| 结算规则摘要 | 截至10月31日伊朗标准时间23:59，美国未对伊朗领土及内水实施规则列明的直接命中空袭或地对地打击才为Yes。海域/空域、拦截碎片、小型打击、网络战等不计；争议信息允许三日核验。不是所有交战方全面停火，也不等于海峡畅通。 |
| 规则指纹 | 4ad99c00bba55951472643794eca27dab0743ff8891a0f80509306b4b3c87506 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/us-iran-ceasefire-continues-throughptptpt |

## Strait of Hormuz traffic returns to normal by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 830253 / 3501950 |
| Yes 概率 % | 0.30 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-0.05, -0.45] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.05} |
| 24h成交量 / 流动性 USD | [126461.95615500002, 304591.78415] |
| 价差 pp | 0.20 |
| 到期 | 2026-11-01T03:59:00+00:00 |
| 结算规则摘要 | 10月31日前IMF Portwatch海峡船舶通行7日均值任一天达到60才为Yes；非宣布开放。末日数据等待14日，有窗口内修订和明显数据错误处理。 |
| 规则指纹 | be893052d9d9b648fb6ffa8b901ed6d9775d1cd3d1be9f830e1dcf5d0f046390 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-october-31-20260810151043583 |

## Will the Fed increase interest rates by 25 bps after the December 2026 meeting?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 770450 / 3215008 |
| Yes 概率 % | 76.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, -1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [112056.40740700002, 386252.0022] |
| 价差 pp | 1.00 |
| 到期 | 2026-12-09T23:59:00+00:00 |
| 结算规则摘要 | 以12月8–9日FOMC前后目标区间上限上调25bp档结算；非标准变动按规则向上取整；不是全年累计加息25bp。 |
| 规则指纹 | 933a10a15eeec0ff1de30468fa20540301ed243f75cc3572d42946192f81a123 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/fed-decision-in-december-20260729232808632 |

## Strait of Hormuz traffic returns to normal by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 455875 / 2176270 |
| Yes 概率 % | 11.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [32848.61534799999, 341032.7698] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限内IMF Portwatch霍尔木兹海峡船舶通行7日均值任一天达到60；不是新闻宣布开放。末日数据允许14日等待；窗口内修订及先前达标有专门处理，见原规则。 |
| 规则指纹 | b0c8ba27f4437b0d8ab819ae170bec118166232e39cdcaefb95bd352d29073d4 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:56:36.719965Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/strait-of-hormuz-traffic-returns-to-normal-by-december-31 |

## Will WTI Crude Oil (WTI) hit (HIGH) $105 in October?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1078055 / 4951227 |
| Yes 概率 % | 39.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.0, null] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 13.5} |
| 24h成交量 / 流动性 USD | [16143.888259999998, 32470.2332] |
| 价差 pp | 3.00 |
| 到期 | 2026-11-01T03:59:59.999000+00:00 |
| 结算规则摘要 | 10月交易时段内，Pyth的ICE WTI活跃月合约1分钟最终高价达到105美元即Yes；按规则提前3个交易时段换月，数据不可用时可依ICE日高低。不是月末价格，也不能以Yahoo CL=F直接结算。 |
| 规则指纹 | 0c455b139d74a669b793323a95aea1e08486656281c457348bd488137e37ae8a |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/what-price-will-wti-hit-in-october-2026 |

## AI bubble burst in 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 691340 |
| Yes 概率 % | 7.90 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.45, -2.3] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": -0.20000000000000018} |
| 24h成交量 / 流动性 USD | [13538.507858, 32151.01246] |
| 价差 pp | 1.20 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | fc153b2136a8dfbadcd169dce1add40690acb1748566b99716fe7ae8fcb07330 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:56:36.719965Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## AI bubble burst by June 30, 2027?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 85299 / 4838928 |
| Yes 概率 % | 22.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [null, 1.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [2443.043479, 20104.1371] |
| 价差 pp | 1.00 |
| 到期 | 2027-07-01T03:59:00+00:00 |
| 结算规则摘要 | 期限前同一90天窗口内至少三项触发：NVDA较收盘历史高点跌50%；SOXX跌40%；OpenAI或Anthropic破产；OpenAI被收购；指定SiliconData H100租金连续5天≤1美元；TSM/ASML/AVGO/ANET/SMCI之一较收盘历史高点跌50%。以公司/交易所及可信报道裁决；2026版未含2027版额外90天举例澄清，两个期限不作同定义比较。 |
| 规则指纹 | bd0420587e08487fffa5050e7fd9b79ffff909a9f843d3f620207ee859462505 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:56:36.719965Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/ai-bubble-burst-by |

## Tesla and SpaceX merger officially announced by December 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 192962 / 2252540 |
| Yes 概率 % | 13.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.0, -6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 0.0} |
| 24h成交量 / 流动性 USD | [1813.341649, 25435.9739] |
| 价差 pp | 1.00 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | 2026年12月31日23:59纽约时间前，Tesla或SpaceX正式宣布双方合并或一方收购另一方的控制权即Yes；无需在期限内完成交易。控制权通常为过半权益或等效治理权；少数股权投资及仅讨论不算。以公司公告或可信报道共识核验；旧URL中的june-30不是本合约期限。 |
| 规则指纹 | 909906ae3b6db7e473468713ea6a1e1e4cf4c931fe247c7d3d576e7986513008 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/tesla-and-spacex-merger-officially-announced-by-june-30 |

## Will Microsoft (MSFT) beat quarterly earnings?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1200526 / 5778671 |
| Yes 概率 % | 83.00 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [3.0, 5.5] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.9999999999999907} |
| 24h成交量 / 流动性 USD | [117.381039, 83.4776] |
| 价差 pp | 18.00 |
| 到期 | 2026-10-28T21:00:00+00:00 |
| 结算规则摘要 | 下一季度首次披露GAAP EPS严格大于固定4.82美元，四舍五入到美分；优先稀释、未披露才用基本EPS。官方财报优先，缺失用SeekingAlpha；公告日收盘后96小时仍无数据或预期日后45天无财报则No。除明显即时错误外不采用后续重述。4.82为建约时阈值，不是当前一致预期；合约价格不能解释成股价上涨概率。 |
| 规则指纹 | c38981deb507343e93936539de51b155f638166eb35f7eaca3a8513338e39cb0 |
| 质量 | ["liquidity_under_10000_or_unknown", "volume24h_under_1000_or_unknown", "spread_over_5pp_or_invalid"] |
| 元数据更新（不是成交时间） | 2026-10-28T11:36:36.965853Z |
| 抓取时间 | 2026-10-28T12:00:59.762297+00:00 |
| 来源 | https://polymarket.com/event/msft-quarterly-earnings-gaap-eps-10-28-2026-4pt82 |

## Military action against Saudi Oil Pipeline (East-West) by October 31?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 1147445 / 5401795 |
| Yes 概率 % | 13.50 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [-1.5, -6.0] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 3.0000000000000013} |
| 24h成交量 / 流动性 USD | [10766.281352, 27628.1904] |
| 价差 pp | 3.00 |
| 到期 | 2026-10-31T20:59:00+00:00 |
| 结算规则摘要 | 截至10月31日利雅得23:59，空袭或地对地武器直接命中东西输油管线或泵站才算Yes；拦截弹碎片、未执行威胁、网络攻击等排除。按沙特官方及可信报道共识裁决，争议可等待三天。价格不证明已命中或发生供应损失。 |
| 规则指纹 | 069363ea2366e79b0328bfc26ff2cd674087f85aac50b63930c45e30f0b86adf |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:32.169280+00:00 |
| 来源 | https://polymarket.com/event/military-action-against-saudi-oil-pipeline-east-west-byptptpt |

## Will Anthropic IPO by December 31, 2026?

| 事件要素 | 内容 |
| --- | --- |
| 事件 / 合约 ID | 549019 / 2413330 |
| Yes 概率 % | 95.25 |
| 供应商 1日 / 1周变化 pp（规则历史未核验） | [1.75, 16.75] |
| 与上一快照可比变化 | {"status": "comparable", "change_pp": 1.749999999999996} |
| 24h成交量 / 流动性 USD | [11818.132354, 44780.8229] |
| 价差 pp | 0.10 |
| 到期 | 2027-01-01T04:59:00+00:00 |
| 结算规则摘要 | Anthropic股份在2026年12月31日23:59美东前于公开证券交易所挂牌并开始交易才为Yes；仅提交S-1不算。被已上市公司收购则No。官方文件/公司与交易所公告优先，可信报道共识可辅助。 |
| 规则指纹 | 91cad6e5770d0b925976d3fbba5e8c61a7f0561a5ee40474d459b9851b8bf4e0 |
| 质量 | 通过启发式筛选 |
| 元数据更新（不是成交时间） | 2026-10-28T11:58:36.395579Z |
| 抓取时间 | 2026-10-28T12:00:33.890317+00:00 |
| 来源 | https://polymarket.com/event/anthropic-ipo-by |

## AI 压力：合约、经营与估值分开

合约层：2026专门AI下行报价7.9%，较早报8.1%下降0.2个百分点；2027年6月底22.5%不变。前者24小时成交约13539美元、价差1.2个百分点，变化小于价差；要求90天内至少三项极端事件，不是普通回撤概率。经营信用层：SK海力士和Vertiv新财报反驳需求已普遍坍塌，但不消除客户融资、设备残值和资本回报风险；博通最大或有责任不是已实现亏损，Meta仍需完整股权/融资桥。H100带日期主读数仍至27日2.89美元/GPU小时、7日+6.2%，FAQ旧读数不采用。估值层：本次五家SEC最新定期财报列表均核验，无新增10-Q/K；NVDA/MSFT/AMZN/GOOGL复用财务底稿，以27日收盘重算五年FCFF情景及敏感性。今晚新财报尚未发布，不编新基本面。META缺融资租赁、优先权益/远期稀释桥，精确估值与反推保持不可用。情景权重非客观概率，公司整体价值非全部AI价值。

## NVDA · 五年 FCFF

| 估值要素 | 内容 |
| --- | --- |
| 状态 | scenario_analysis |
| 财务底稿 | TTM 至 2026-07-26；最新 10-Q / filed 2026-08-26 |
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001045810.json", "checked_at": "2026-10-28T12:04:27.133006+00:00", "latest_filing_date": "2026-08-26"} |
| 观测财务数据 | {"ttm_revenue_million": 302970, "revenue_quarters": [{"end": "2025-10-26", "value": 57006000000, "filed": "2025-11-19", "duration_days": 91}, {"end": "2026-01-25", "value": 68127000000, "filed": "2026-02-25", "duration_days": 91}, {"end": "2026-04-26", "value": 81615000000, "filed": "2026-05-20", "duration_days": 91}, {"end": "2026-07-26", "value": 96221000000, "filed": "2026-08-26", "duration_days": 91}], "cash_million": 22443.0, "liquid_investments_million": 34143.0, "debt_million": 33366.0, "finance_lease_million": 0, "diluted_shares_million": 24285.0, "latest_operating_income_million": 63734.0, "observed_end": "2026-07-26", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 96221.0, "income_statement_window": "最近单季度", "ttm_bridge_note": "采用同版 FY2026全年 + FY2027半年 - FY2026半年；与四季逐项求和差1百万为披露舍入差。"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json", "https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。10-Q Note14 表明融资租赁费用不重大；模型按不重大近似零，不将其称为精确零负债。未确认担保仅作为压力情景，非已到期净债务。市场化股权42783和非市场化股权51157不作为类现金；非经营资产加回为0的保守假设。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 217.94 |
| 基期输入 USD million / million shares | {"revenue": 302970, "net_debt": -23220.0, "diluted_shares": 24285.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.2961487944658686, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## NVDA · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 98.77 | -54.68 | 14.00 | 60.00 | 12.00 | 68.42 |
| 基准 | 154.12 | -29.28 | 20.00 | 65.00 | 11.00 | 74.20 |
| 乐观 | 242.58 | 11.31 | 26.00 | 70.00 | 10.00 | 79.05 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0000789019.json", "checked_at": "2026-10-28T12:04:36.641590+00:00", "latest_filing_date": "2026-07-29"} |
| 观测财务数据 | {"ttm_revenue_million": 331839.0, "revenue_quarters": [{"end": "2025-09-30", "value": 77673000000, "filed": "2025-10-29", "duration_days": 92}, {"end": "2025-12-31", "value": 81273000000, "filed": "2026-01-28", "duration_days": 92}, {"end": "2026-03-31", "value": 82886000000, "filed": "2026-04-29", "duration_days": 90}, {"end": "2026-06-30", "value": 90007000000, "filed": "2026-07-29", "duration_days": 91}], "cash_million": 20935.0, "liquid_investments_million": 55908.0, "debt_million": 40294.0, "finance_lease_million": 66594.0, "diluted_shares_million": 7453.0, "latest_operating_income_million": 155237.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 331839.0, "income_statement_window": "FY2026 全年"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000789019.json", "https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。融资租赁66594计入债务；资本开支假设涵盖新增租赁，现金支出115948加融资租赁资产新增24608为本年经济资本开支140556。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 531.33 |
| 基期输入 USD million / million shares | {"revenue": 331839.0, "net_debt": 30045.0, "diluted_shares": 7453.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.31717389479314473, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## MSFT · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 143.02 | -73.08 | 8.00 | 42.00 | 10.50 | 76.13 |
| 基准 | 266.55 | -49.83 | 14.00 | 47.00 | 9.50 | 81.05 |
| 乐观 | 484.83 | -8.75 | 20.00 | 52.00 | 8.50 | 84.97 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001018724.json", "checked_at": "2026-10-28T12:04:40.194158+00:00", "latest_filing_date": "2026-07-31"} |
| 观测财务数据 | {"ttm_revenue_million": 775680.0, "revenue_quarters": [{"end": "2025-09-30", "value": 180169000000, "filed": "2025-10-31", "duration_days": 92}, {"end": "2025-12-31", "value": 213386000000, "filed": "2026-02-06", "duration_days": 92}, {"end": "2026-03-31", "value": 181519000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 200606000000, "filed": "2026-07-31", "duration_days": 91}], "cash_million": 78213.0, "liquid_investments_million": 44775.0, "debt_million": 133320.0, "finance_lease_million": 13451.0, "diluted_shares_million": 10903.0, "latest_operating_income_million": 27461.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "RevenueFromContractWithCustomerExcludingAssessedTax", "latest_reported_revenue_million": 200606.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001018724.json", "https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。总长期债务132995（含当前部分）加短期借款325，融资租赁13451另加；未将其他长期负债全部误作有息债务。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | 无 |
| 价格 USD | 253.10 |
| 基期输入 USD million / million shares | {"revenue": 775680.0, "net_debt": 23783.0, "diluted_shares": 10903.0, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.39326648066939984, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## AMZN · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 11.53 | -95.44 | 6.00 | 12.00 | 11.00 | 84.01 |
| 基准 | 87.42 | -65.46 | 12.00 | 17.00 | 10.00 | 83.61 |
| 乐观 | 238.05 | -5.95 | 18.00 | 22.00 | 9.00 | 86.04 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001652044.json", "checked_at": "2026-10-28T12:04:42.533312+00:00", "latest_filing_date": "2026-07-23"} |
| 观测财务数据 | {"ttm_revenue_million": 445867.0, "revenue_quarters": [{"end": "2025-09-30", "value": 102346000000, "filed": "2025-10-30", "duration_days": 92}, {"end": "2025-12-31", "value": 113829000000, "filed": "2026-02-05", "duration_days": 92}, {"end": "2026-03-31", "value": 109896000000, "filed": "2026-04-30", "duration_days": 90}, {"end": "2026-06-30", "value": 119796000000, "filed": "2026-07-23", "duration_days": 91}], "cash_million": 55911.0, "liquid_investments_million": 186563.0, "debt_million": 100164, "finance_lease_million": 2590.0, "diluted_shares_million": 12309.0, "latest_operating_income_million": 40770.0, "observed_end": "2026-06-30", "unit": "USD million; shares million; revenue_quarters.value USD", "revenue_tag": "Revenues", "latest_reported_revenue_million": 119796.0, "income_statement_window": "最近单季度"} |
| 来源 | ["https://data.sec.gov/api/xbrl/companyfacts/CIK0001652044.json", "https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/goog-20260630.htm"] |
| 口径 | 经营租赁费用留在EBIT且不重复扣租赁负债；融资租赁计入净债务，新增资产在资本开支中，融资本金不再扣。SBC保留为费用；新增净稀释假设0，不把同一SBC再次扣价。现金和可交易债券按账面近似可用现金；非经营私募投资不加回、税务价值未建模。股数采用最新披露的稀释口径，非当日实时股数。优先股按完全转换处理：季度稀释股数12309减已计入的16，再加合同最大转换股数54.45825；不再扣19000优先股本金。未来3年优先股息按年1203.125、10%折现约2991.99计入权益桥调整，此为保守假设；capped call 未赋值。 |
| 主观假设说明 | 三情景均为研究假设，不是公司指引。资本开支从起始压力水平向第5年终点线性收敛，经营利润率同样收敛；DA终点比例固定，需持续核验算力折旧。终值敏感性远高于短期行情，不将模型差价直接当交易信号。 |
| 权益桥额外假设 | {"preferred_coupon_pv_million": 2991.9938016528904, "discount_rate": 0.1, "years": 3} |
| 价格 USD | 320.58 |
| 基期输入 USD million / million shares | {"revenue": 445867.0, "net_debt": -136728.0061983471, "diluted_shares": 12347.45825, "non_operating_assets": 0} |
| 反推五年收入增长 | {"status": "solved", "growth": 0.3749762723448141, "note": "其余假设固定时的五年收入 CAGR，不是一致预期或事件概率"} |

## GOOGL · 情景结果

| 情景 | 每股 USD | 相对现价% | 收入CAGR% | 第5年利润率% | WACC% | 终值占EV% |
| --- | --- | --- | --- | --- | --- | --- |
| 悲观 | 66.88 | -79.14 | 7.00 | 31.00 | 11.00 | 79.41 |
| 基准 | 131.94 | -58.84 | 13.00 | 36.00 | 10.00 | 82.80 |
| 乐观 | 250.29 | -21.92 | 19.00 | 41.00 | 9.00 | 85.75 |

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
| 披露检查 | {"status": "verified", "source": "https://data.sec.gov/submissions/CIK0001326801.json", "checked_at": "2026-10-28T12:04:46.269143+00:00", "latest_filing_date": "2026-10-22"} |
| 观测财务数据 | {"revenue_million": 64601, "operating_cashflow_million": 32790, "reported_capex_including_finance_lease_principal_million": 34910, "company_defined_fcf_million": -2120, "diluted_shares_million": 2573, "reported_operating_income_million": 12988, "legal_charge_million": 9900, "observed_end": "2026-09-30", "published_at": "2026-10-21T16:01:00-04:00", "unit": "USD million; shares million", "noncancelable_commitments_million": 454520, "leases_not_commenced_million": 355730, "contingent_cloud_capacity_max_million": 14720, "restricted_cash_reclassified_million": 10800, "commitments_due_2026_million": 45850, "commitments_due_2027_million": 121410} |
| 来源 | ["https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html", "https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm", "https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Announces-Launch-of-Offering-of-Depositary-Shares-Representing-Series-A-Mandatory-Convertible-Preferred-Stock-and-Offering-of-Class-A-Common-Stock-in-Connection-with-Forward-Sale-Agreements/default.aspx", "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html"] |
| 口径 | 公司FCF扣除融资租赁本金，不能直接代替模型FCFF；融资租赁负债/新增资产未齐，不假设零。法律费用不全归AI经营。 |
| 主观假设说明 | 缺失 |
| 权益桥额外假设 | 无 |
| 缺失原因 | 22日10-Q已核验，本次无新增定期财报。27日普通股625美元定价、优先票息6.5%已核验；完整融资租赁负债/新增资产、优先权益/远期发行与现金到账桥未齐，不用不同承诺简单充当现有债务，暂停精确FCFF反推。 |

## 盘前突破须经过开盘和Fed两次验证

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 27日收盘越过前日高点；28日Fed与财报 |
| 关联标的 | ["SPY", "QQQ", "SMH", "RSP", "IWM"] |
| 确认条件 | QQQ722.87、SMH559.81（27日高点）开盘回踩守住并重新走高，SPY突破771.14，等权/金融加入；观察首30–60分钟的更高低点和可得常规VWAP，再看Fed公布后及收盘。进一步QQQ724.92/SMH573.45为27日50日均线参考，会动态变化。 |
| 失效条件 | 高开后跌回QQQ721.25、SMH557.98、SPY769.66昨收，反抽不能收复，先降级；跌破QQQ713.59、SMH546.67、SPY765.21昨日低点属于更强失效。不是必须等最远止损才降风险。 |
| 观察期限 | 未来1–3交易日 |
| 反证 | 金融/小盘盘前偏弱，量能未确认；Fed和今晚财报均可改变路径。 |
| 状态 | 盘前增强，常规与政策后确认未发生 |

## 软件云：等待财报后承接

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 28日微软和Oracle投资者日、29日Amazon |
| 关联标的 | ["IGV", "SKYY", "MSFT", "ORCL"] |
| 确认条件 | IGV守26日低点109.69及最新20日线109.21附近，突破前高111.88后稳定；云增长、资本开支回报及FCF口径支持。 |
| 失效条件 | 相对SPY转弱、109.69/动态20日线反抽失败，或财报现金流/指引恶化。 |
| 观察期限 | 本周财报后1–3日 |
| 反证 | MSFT27日−0.24%；跨期强不保证财报跳空向上。 |
| 状态 | 优先观察但避免事前押方向 |

## 能源降级，油服与核电分开

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 油价、设施与DOE条件贷款 |
| 关联标的 | ["XLE", "XOP", "OIH", "CEG"] |
| 确认条件 | XLE重新收复68.62且相对SPY恢复，供应证据与价格一致；核电独立验证条件贷款落实和工程进度。 |
| 失效条件 | 68.62反抽失败、供应风险溢价持续回落；核电放款/项目延期。 |
| 观察期限 | 未来一周 |
| 反证 | XLE27日收68.21已失守原守位前提；OIH上涨不代表所有能源强。 |
| 状态 | 原价格前提失效，等待重建 |

## AI融资：先查信用再看反弹

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | 博通或有担保与Meta发行定价 |
| 关联标的 | ["AVGO", "META", "NVDA"] |
| 确认条件 | META先收回625/627.80并有承接，再看628.46（27日高点）；融资、股本与设备现金回报的披露能解释债务责任。 |
| 失效条件 | 619.21（27日低点）失守且反抽失败，或客户信用、残值/融资条件恶化。 |
| 观察期限 | 未来两日价格；下一财报周期经营 |
| 反证 | 最大或有金额不是已实现损失，价格弱也不能独自证明信用事件发生。 |
| 状态 | Meta旧支撑条件已失效，保持分化判断 |

## 电力散热财报后观察

| 条件剧本 | 内容 |
| --- | --- |
| 催化剂 | VRT财报与11:00纽约电话会 |
| 关联标的 | ["VRT", "GEV", "CEG"] |
| 确认条件 | 不以盘前涨幅追入：首30–60分钟形成开盘区间，回踩守其下沿和常规VWAP、再突破区间上沿；板块与QQQ同向，电话会未削弱现金流指引。 |
| 失效条件 | 高开低走跌破开盘区间下沿且反抽失败，或指引质量、应收/资本支出解释恶化。 |
| 观察期限 | 今日开盘至未来1–3日 |
| 反证 | 开盘区间和VWAP尚未形成，不能预填价格；财报强但估值预期过高仍可下跌。 |
| 状态 | 新增观察，等待常规承接 |

## 跨期比较与上期剧本复核

与28日早报相比，没有新增完整常规交易日，27日收盘第二层突破结论不重复当成新信号。新增SK海力士/VRT需求证据；STX盘后629.89至盘前653.23，卖压减轻但仍低于667.85常规收盘。QQQ/SMH盘前高于昨日高点，尚无回踩/VWAP/收盘验证；SPY尚未越昨日高点，金融小盘偏弱。Meta仍低于625/627.80，旧支撑未恢复。原油风险报价抬头。相同规则合约：2589812: 95.65%→94.95%（-0.70个百分点）；4641065: 94.5%→95.5%（+1.00个百分点）；3501950: 0.25%→0.3%（+0.05个百分点）；3215008: 76.5%→76.5%（+0.00个百分点）；2176270: 11.5%→11.5%（+0.00个百分点）；4951227: 26%→39.5%（+13.50个百分点）；691340: 8.1%→7.9%（-0.20个百分点）；2252540: 13.5%→13.5%（+0.00个百分点）；4838928: 22.5%→22.5%（+0.00个百分点）；5778671: 81%→83%（+2.00个百分点）；5401795: 10.5%→13.5%（+3.00个百分点）；2413330: 93.5%→95.25%（+1.75个百分点）。WTI触及不是收盘门槛；停火延续不等于航运恢复。

## 可计算的跨期变化

```json
[
  {
    "mode": "daily",
    "baseline": "reports/daily/2026-10-27/20261027T232257.797862Z/evidence.json",
    "baseline_cutoff": "2026-10-27T23:22:50.332510+00:00",
    "close_change_pct": {
      "SPY": 0.0,
      "QQQ": 0.0,
      "IWM": 0.0,
      "RSP": 0.0,
      "GLD": 0.0,
      "GC=F": -0.04660621473691062,
      "CL=F": -0.010011145895150175,
      "BZ=F": 3.999997491705898,
      "TLT": 0.0,
      "UUP": 0.0,
      "HYG": 0.0,
      "LQD": 0.0,
      "^VIX": 0.0,
      "^VIX3M": 0.0,
      "^VVIX": 0.0,
      "^MOVE": -0.004084642205215427,
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
      "AMZN": {
        "change_pct": -0.03946329913180335,
        "from_observed_at": "2026-10-27T23:16:29+00:00",
        "to_observed_at": "2026-10-28T12:00:12+00:00"
      },
      "AVGO": {
        "change_pct": 2.046500718327615,
        "from_observed_at": "2026-10-27T23:15:32+00:00",
        "to_observed_at": "2026-10-28T12:00:29+00:00"
      },
      "CEG": {
        "change_pct": 0.9317308559087856,
        "from_observed_at": "2026-10-27T23:10:43+00:00",
        "to_observed_at": "2026-10-28T11:58:32+00:00"
      },
      "GLW": {
        "change_pct": 2.4686182483493857,
        "from_observed_at": "2026-10-27T23:12:42+00:00",
        "to_observed_at": "2026-10-28T12:00:07+00:00"
      },
      "GOOGL": {
        "change_pct": 0.8729961476326542,
        "from_observed_at": "2026-10-27T23:16:18+00:00",
        "to_observed_at": "2026-10-28T12:00:29+00:00"
      },
      "IWM": {
        "change_pct": -0.23557966876072145,
        "from_observed_at": "2026-10-27T23:16:34+00:00",
        "to_observed_at": "2026-10-28T11:59:56+00:00"
      },
      "META": {
        "change_pct": 0.16301628548831548,
        "from_observed_at": "2026-10-27T23:16:01+00:00",
        "to_observed_at": "2026-10-28T12:00:24+00:00"
      },
      "MSFT": {
        "change_pct": -0.6050129645635338,
        "from_observed_at": "2026-10-27T23:15:21+00:00",
        "to_observed_at": "2026-10-28T12:00:06+00:00"
      },
      "NVDA": {
        "change_pct": 0.8866225652333748,
        "from_observed_at": "2026-10-27T23:15:31+00:00",
        "to_observed_at": "2026-10-28T12:00:29+00:00"
      },
      "ORCL": {
        "change_pct": 0.41881883471119874,
        "from_observed_at": "2026-10-27T23:16:14+00:00",
        "to_observed_at": "2026-10-28T12:00:29+00:00"
      },
      "QQQ": {
        "change_pct": 0.36438539668885994,
        "from_observed_at": "2026-10-27T23:16:23+00:00",
        "to_observed_at": "2026-10-28T12:00:27+00:00"
      },
      "SMH": {
        "change_pct": 1.654054054054055,
        "from_observed_at": "2026-10-27T23:15:49+00:00",
        "to_observed_at": "2026-10-28T12:00:28+00:00"
      },
      "SNDK": {
        "change_pct": 5.711188540456824,
        "from_observed_at": "2026-10-27T23:14:18+00:00",
        "to_observed_at": "2026-10-28T12:00:25+00:00"
      },
      "SPY": {
        "change_pct": 0.10131317460935207,
        "from_observed_at": "2026-10-27T23:15:04+00:00",
        "to_observed_at": "2026-10-28T12:00:10+00:00"
      },
      "STX": {
        "change_pct": 3.705408880915728,
        "from_observed_at": "2026-10-27T23:15:49+00:00",
        "to_observed_at": "2026-10-28T12:00:27+00:00"
      },
      "TLT": {
        "change_pct": -0.21963691272866015,
        "from_observed_at": "2026-10-27T23:15:10+00:00",
        "to_observed_at": "2026-10-28T12:00:14+00:00"
      }
    },
    "macro_change": {
      "DGS2": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-26"
      },
      "BAMLH0A0HYM2": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-26"
      },
      "BAMLC0A0CM": {
        "change": 0.0,
        "unit": "percentage_points",
        "observation_date": "2026-10-26"
      },
      "DGS10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-26"
      },
      "DFII10": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-26"
      },
      "T10YIE": {
        "change": 0.0,
        "unit": "percent",
        "observation_date": "2026-10-27"
      },
      "STLFSI4": {
        "change": 0.0,
        "unit": "index",
        "observation_date": "2026-10-16"
      },
      "CBOE_VIX": {
        "change": -0.870000000000001,
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
      "2589812": {
        "status": "comparable",
        "change_pp": -0.7000000000000006
      },
      "4641065": {
        "status": "comparable",
        "change_pp": 1.0000000000000009
      },
      "3501950": {
        "status": "comparable",
        "change_pp": 0.05
      },
      "3215008": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2176270": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "4951227": {
        "status": "comparable",
        "change_pp": 13.5
      },
      "691340": {
        "status": "comparable",
        "change_pp": -0.20000000000000018
      },
      "4838928": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "2252540": {
        "status": "comparable",
        "change_pp": 0.0
      },
      "5778671": {
        "status": "comparable",
        "change_pp": 1.9999999999999907
      },
      "5401795": {
        "status": "comparable",
        "change_pp": 3.0000000000000013
      },
      "2413330": {
        "status": "comparable",
        "change_pp": 1.749999999999996
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
    "event": "下一交易日常规开盘，验证财报后卖压",
    "date": "2026-10-28T09:30:00-04:00",
    "source": "tc:get_trading_calendar"
  },
  {
    "event": "FOMC政策决定；27–28日会议",
    "date": "2026-10-28T14:00:00-04:00",
    "source": "https://www.federalreserve.gov/newsevents/2026-october.htm"
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
    "event": "SPCE计划转场，非已完成；具体分钟未知",
    "date": "2026-10-28 America/New_York",
    "source": "https://www.virgingalactic.com/news/virgin-galactic-sets-october-28-for-lead-delta-class-spaceships-arrival-at-spaceport-america"
  },
  {
    "event": "Alphabet财报电话会：RTTNews指向28日16:30纽约，官方链接仍无法读取，待官方确认",
    "date": null,
    "source": "https://www.rttnews.com/3703989/alphabet-q3-26-earnings-conference-call-at-4-30-pm-et.aspx"
  },
  {
    "event": "FOMC记者会",
    "date": "2026-10-28T14:30:00-04:00",
    "source": "https://www.federalreserve.gov/newsevents/2026-october.htm"
  },
  {
    "event": "Vertiv财报电话会",
    "date": "2026-10-28T11:00:00-04:00",
    "source": "https://www.prnewswire.com/news-releases/vertiv-reports-strong-third-quarter-2026-with-net-sales-growth-of-61-organic-orders-growth-over-100-and-diluted-eps-growth-of-91-adjusted-diluted-eps-growth-of-78-raises-full-year-2026-guidance-across-all-key-metrics-302921936.html"
  }
]
```

## 新闻事件去重与时间

| 事件 | 摘要 | 发生时间（未知留空） | 各来源发布时间 / 抓取时间 |
| --- | --- | --- | --- |
| skhynix-3q26-20261028 | 初步Q3收入104.6155万亿韩元、营业利润83.3338万亿、营业利润率约80%；支持需求但不外推永久利润。 | 缺失 | [{"source": "https://news.skhynix.com/en/q3-2026-business-results/", "published_at": null, "retrieved_at": "2026-10-28T12:09:06.088310+00:00"}] |
| vrt-q3-20261028 | Q3收入43.13亿美元、调整后EPS2.21、调整后FCF6.52亿美元；上调全年指引。 | 缺失 | [{"source": "https://www.prnewswire.com/news-releases/vertiv-reports-strong-third-quarter-2026-with-net-sales-growth-of-61-organic-orders-growth-over-100-and-diluted-eps-growth-of-91-adjusted-diluted-eps-growth-of-78-raises-full-year-2026-guidance-across-all-key-metrics-302921936.html", "published_at": "2026-10-28T05:55:00-04:00", "retrieved_at": "2026-10-28T12:09:06.088310+00:00"}] |
| gev-q3-20261028 | 财经来源确认上调指引；官方正文访问失败，具体指引与收购条款保留二级线索，不据此改写估值。 | 缺失 | [{"source": "https://ca.investing.com/news/earnings/ge-vernova-stock-gains-on-earnings-beat-raised-guidance-4908455", "published_at": null, "retrieved_at": "2026-10-28T12:09:06.088310+00:00"}] |
| hormuz-weekend-flow-20261028 | Reuters转引此前周末航运放缓数据；这是周末窗口，不是今日实时船流。 | 缺失 | [{"source": "https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp", "published_at": null, "retrieved_at": "2026-10-28T12:09:06.088310+00:00"}] |
| stx-fy27q1-20261027 | 盘后财报：收入42.33亿美元、非GAAP EPS7.68；48亿美元中值收入指引是下一季度FY2027Q2，纠正tc摘要全年误标。 | 缺失 | [{"source": "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-First-Quarter-2027-Financial-Results/default.aspx", "published_at": null, "retrieved_at": "2026-10-27T23:22:43.584056+00:00"}] |
| nxpi-q3-20261027 | Q3收入37.86亿美元、非GAAP EPS4.20；下季EPS4.14–4.58。业绩后股价承接偏弱。 | 缺失 | [{"source": "https://investors.nxp.com/news-releases/news-release-details/nxp-semiconductors-reports-third-quarter-2026-results", "published_at": "2026-10-27T16:10:00-04:00", "retrieved_at": "2026-10-27T23:22:43.584056+00:00"}] |
| avgo-residual-backstop-20261026 | 26日达成、27日8-K披露：租赁违约责任以未偿款72.5%减回收计算；全部部署后最大未折现潜在责任约430亿美元，不是当期损失。 | 缺失 | [{"source": "https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3", "published_at": null, "retrieved_at": "2026-10-27T23:22:43.584056+00:00"}] |
| oracle-google-tpu-20261027 | OCI计划2027年提供Google TPU并多年扩张，尚非本期收入贡献。 | 缺失 | [{"source": "https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/", "published_at": null, "retrieved_at": "2026-10-27T23:22:43.584056+00:00"}] |

## 覆盖范围与数据缺口

```json
[
  "CNN接口418，无法核验当期Fear & Greed；不以tc温度替代。",
  "常规VWAP、完整成分广度和历史一致预期修正缺失；OHLC不能重建回踩顺序。",
  "tc高影响新闻限50且has_more，主动补查不能保证完整覆盖。",
  "原油近月/连续合约换月未对齐，数据面板机械日线变化不作为官方结算或归因依据。",
  "CME当期带时点概率矩阵未取到；Polymarket不等于FedWatch。",
  "META融资、租赁新增、优先权益/远期稀释完整桥缺失，精确FCFF暂停。",
  "DRAM不足200日历史；部分Polymarket查询截断、财报盘口宽薄。",
  "H100有日期主读数2.89与静态FAQ2.53不一致，仅使用27日标注读数。",
  "NVDA官网8月实录预告11月17日，与tc25日冲突；需临近复核。Alphabet官方事件页本次无法访问，不伪造确定分钟。",
  "VanEck发行人页面本次超时；最近已核验数据至26日，ICI至21日，均不是28日实时板块申赎。",
  "tc高影响筛选追加美国标的查询，仍有has_more和来源截断；不能保证全球新闻覆盖。",
  "RSP/IGV盘前分钟稀疏；其他报价取实际分钟时间，各标的并非同秒。",
  "GEV官方详细结果正文不可读取，二级报道与官方事件页分别标记；最新美军航运警告未获同日官方核验。",
  "同一交易日多时段更新，日线/财务底稿不变不表示采集失败；本次盘前涨跌与27日收盘分开。",
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
  "tc 报价质量 stale: IGV, NXPI, RSP, XLE；不作为新成交证据",
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
  "指标缺失/历史不足: prices.^VIX.volume_vs_previous20_ratio, prices.^VIX3M.volume_vs_previous20_ratio, prices.^VVIX.volume_vs_previous20_ratio, prices.^MOVE.volume_vs_previous20_ratio, prices.DRAM.sma200, prices.DRAM.distance_sma200_pct, quotes.IGV.value, quotes.NXPI.value, quotes.RSP.value, quotes.XLE.value"
]
```

## 来源、时间与核验记录

```json
[
  {
    "url": "https://investors.seagate.com/news/news-details/2026/Seagate-Technology-Reports-Fiscal-First-Quarter-2027-Financial-Results/default.aspx",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://investors.nxp.com/news-releases/news-release-details/nxp-semiconductors-reports-third-quarter-2026-results",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://investors.broadcom.com/static-files/0ee4f6b7-4a23-4de0-8f3e-48f147ae30d3",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.oracle.com/news/announcement/ai-world-oracle-brings-google-tpus-to-oracle-cloud-infrastructure-2026-10-27/",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.energy.gov/articles/fact-sheet-energy-department-delivering-president-trumps-commitment-expand-american",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.virgingalactic.com/news/virgin-galactic-sets-october-28-for-lead-delta-class-spaceships-arrival-at-spaceport-america",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.prnewswire.com/news-releases/meta-announces-pricing-of-offering-of-depositary-shares-representing-series-a-mandatory-convertible-preferred-stock-and-offering-of-class-a-common-stock-in-connection-with-forward-sale-agreements-302920247.html",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.stocktitan.net/news/GLW/corning-delivers-outstanding-third-quarter-results-ijv492ou5imj.html",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://boeing.mediaroom.com/2026-10-27-Boeing-Reports-Third-Quarter-Results",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次公开来源核验；无具体事件分钟则不猜测。公司前瞻计划与实际完成区分。"
  },
  {
    "url": "https://www.microsoft.com/en-us/investor/faq",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://www.bea.gov/news/schedule/full",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://investor.sandisk.com/news-releases/news-release-details/sandisk-report-first-quarter-fiscal-year-2027-results-october-29",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://www.aboutamazon.com/news/company-news/amazon-earnings-q3-2026-report",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://www.bls.gov/schedule/2026/11_sched.htm",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://www.anthropic.com/news/s1-sec",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://investor.oracle.com/investor-news/news-details/2026/ORACLE-INVESTOR-DAY-MEETING-TO-BE-HELD-OCTOBER-28-2026/default.aspx",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://abc.xyz/investor/",
    "checked_at": "2026-10-27T23:22:43.584056+00:00",
    "note": "本次日程检查或沿用已核验官方公告；受限/冲突项见缺口，旧公告不是新事件。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-10-27T23:16:42.611425+00:00",
    "note": "实际分钟时戳；盘后涨跌相对27日常规收盘，不能解释常规上涨原因。"
  },
  {
    "url": "https://news.skhynix.com/en/q3-2026-business-results/",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "初步公司财报；不把前瞻订单当已收现金"
  },
  {
    "url": "https://www.prnewswire.com/news-releases/vertiv-reports-strong-third-quarter-2026-with-net-sales-growth-of-61-organic-orders-growth-over-100-and-diluted-eps-growth-of-91-adjusted-diluted-eps-growth-of-78-raises-full-year-2026-guidance-across-all-key-metrics-302921936.html",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "公司发布经PRNewswire分发"
  },
  {
    "url": "https://ca.investing.com/news/earnings/ge-vernova-stock-gains-on-earnings-beat-raised-guidance-4908455",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "二级财经核验；官方结果正文访问失败"
  },
  {
    "url": "https://www.federalreserve.gov/newsevents/2026-october.htm",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "官方14:00决定/14:30记者会"
  },
  {
    "url": "https://www.gulf-times.com/article/731298/shopping/shipping-slows-through-strait-of-hormuz-after-tanker-attacks/amp",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "Reuters转载；航运数据是此前周末窗口"
  },
  {
    "url": "https://www.silicondata.com/products/silicon-index/h100",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "最新页面仍标27日"
  },
  {
    "url": "https://www.ici.org/research/stats/etf_flows",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "27日发布、至21日窗口"
  },
  {
    "url": "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "页面可读但当期概率矩阵缺失"
  },
  {
    "url": "https://www.vaneck.com/us/en/investments/semiconductor-etf-smh/",
    "checked_at": "2026-10-28T12:09:06.088310+00:00",
    "note": "本次访问超时，无新份额证据"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AMZN",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/AVGO",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/CEG",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/DRAM",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GEV",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLD",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GLW",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/GOOGL",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IGV",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/IWM",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/META",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MSFT",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/MU",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NVDA",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/NXPI",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/ORCL",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/QQQ",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/RSP",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SMH",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SNDK",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/SPY",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/STX",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/TLT",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/VRT",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLE",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  },
  {
    "url": "https://query1.finance.yahoo.com/v8/finance/chart/XLF",
    "checked_at": "2026-10-28T12:05:14.584197+00:00",
    "note": "本次盘前真实分钟报价，非同秒；相对27日常规收盘"
  }
]
```

## 付费信源建议（未订阅）

```json
[]
```
