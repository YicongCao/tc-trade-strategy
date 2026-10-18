# 运行研究

工作目录为仓库根目录。技能负责 tc MCP / 搜索 / 判断，Python 不调用模型 API。安装后可用 `us-market-research`，也可用 `.venv/bin/python -m tc_trade_strategy.research`。

```bash
.venv/bin/python -m pip install -e '.[dev]'
us-market-research status --mode daily --tc results/my-run/tc.json --scheduled
us-market-research prepare --mode daily --tc results/my-run/tc.json
us-market-research filings
us-market-research indicators
us-market-research build --mode daily --tc results/my-run/tc.json --snapshot results/research-runs/RUN/snapshot.json --analysis results/my-run/analysis.json --financials results/my-run/financials.json
us-market-research publish --report reports/daily/PERIOD/RUN
```

可选 `--date YYYY-MM-DD` 限制研究交易日；`--cutoff 2026-10-18T12:00:00+08:00` 指明证据截止；`--focus AI,能源` 改变重点。历史日期调用是“现在回顾过去”，不伪称当时可见。采集只能拉当前事件预期，不能伪造历史概率。指定 cutoff 必须覆盖实际取证时刻；默认使用命令实际运行时间。

`prepare` 为原始数据创建唯一目录；MCP 输入也使用唯一运行目录。`build` 与 `publish` 共享非阻塞进程锁；重复手动运行创建新版本，定时运行 `--scheduled` 跳过远端已有的同模式周期。报告不可覆盖。`status` 查看本地 origin/main 跟踪状态，必要时先 `git fetch origin main`；成功发布由远端提交中的同一证据内容确认，不能凭本地目录判断成功。

活跃盘前/盘中/盘后当前 SPY 报价超过20分钟或无时戳时，停止完整报告；周末需核验最近完成日 SPY/QQQ 收盘。宏观与低流动性数据允许滞后但标注。核心失败只写 `results/research-state/failure-*.json`。

发布前暂存区须为空；工作区其他文件可以有改动，不会被报告命令暂存。分歧、认证失败或推送拒绝均保留报告与提交，不强推。先处理已有成果再生成新报告；不要让索引引用未入库文件。恢复发布用同一 `publish --report`，不用重新编造报告。

预览：`.venv/bin/python -m http.server 8766 --bind 127.0.0.1 --directory reports`，在普通浏览器打开 `http://127.0.0.1:8766/`。无需 Node、CDN 或编辑器私有运行时。

## 定时口径

本机 Codex 当前会话 heartbeat：日报北京时间周二至周六08:00，周报周日10:00；实时手动。任务调用统一技能、每次刷新交易日历、只补最新应生成周期。休市没有新完成周期、或该周期已成功推送时跳过。周报星期五休市时可用周四作为周末；半日市13:00纽约收盘；时区库处理夏令时。

电脑休眠或 Codex 关闭不保证运行；恢复后标真实生成时间，不回填虚构时点。成功推送通知路径，失败或需要处理的缺口通知原因。调度通过 Codex 原生 automation_update 管理；配置状态见 `docs/migration.md`。不通过 launchd 再调用旧筛选器。

## 指标与本地历史

每次 build 自动计算趋势/强弱/波动面板，校验 analysis.json 的 indicator_assessments，生成公开的判断依据与历史比较，并写本地敏感目录中的公开指标副本。首次执行 `us-market-research indicators` 从既有公开报告建立基线，更新 `sensitive/market-indicators/index.html`（可直接浏览），同目录还有 Markdown/JSON 和不可覆盖 snapshots。该命令不扫描其他 sensitive 路径，不会读取账户或密钥，不发布本地历史。

已授权此单独目录，AGENTS 的账户隔离仍适用。若未被 Git 忽略、已被跟踪或有符号链接则拒绝写入。build 的本地历史写入失败时报告仍保留，CLI 明确返回失败原因；处理后可用 indicators 重建。指标定义、质量与决策记录见技能 references/indicators.md 和数据契约。

公开历史较短时比较显示无基线，不推断长期趋势；1/5/20/60次观测与交易日收益分别标注。回看历史报告不是当时可交易的数据回测。不要为补齐历史修改已发布报告。
