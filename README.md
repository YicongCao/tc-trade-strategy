# 美股主观交易辅助器

基于 Trade Copilot MCP 和公开数据，为数日至数周的波段交易提供市场研究：事件预期、跨资产风险、板块轮动、AI 经营压力与估值、当前交易主题。只做研究，不读取账户、不修改策略、不交易。

**报告入口：[历史索引 HTML](reports/index.html) · [历史索引 Markdown](reports/index.md)**

在 Codex 中调用：

```text
$us-market-research weekly
$us-market-research daily
$us-market-research realtime，重点关注 AI 资本开支和能源
```

每次输出有催化剂、确认条件、失效条件、期限和反证的条件剧本。证据不足保留观察项。报告包含来源时点和缺口，不把价格轮动当作机构净流入，也不把预测市场价格当作客观概率。

| 位置 | 用途 |
| --- | --- |
| [.agents/skills/us-market-research](.agents/skills/us-market-research/SKILL.md) | 唯一研究技能 |
| [docs/research-workflow.md](docs/research-workflow.md) | 手动运行、定时口径、失败恢复 |
| [docs/data-contract.md](docs/data-contract.md) | 研究输入与财务底稿契约 |
| [dependencies/trade-copilot-mcp.md](dependencies/trade-copilot-mcp.md) | tc 市场接口与现有授权 |
| config/ | Polymarket 跟踪事件、财务底稿和模型假设 |
| src/tc_trade_strategy/ | 采集、日历、计算、校验、渲染、发布 |
| reports/{weekly,daily,realtime}/ | 不可覆盖的报告版本，Markdown + HTML + evidence.json |
| results/ | 本地原始数据、缓存、失败日志，不入库 |
| sensitive/ | 本地账户记录与 IBKR 密钥等敏感资料，整个目录被 Git 忽略，研究流程不读取 |
| [archive/legacy-strategy](archive/legacy-strategy/README.md) | 旧策略与筛选系统的可恢复归档 |

安装与验证：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/pytest -q
.venv/bin/ruff check src tests
```

自动调度：北京时间周二至周六08:00日报、周日10:00周报；实时按需。由本机 Codex 原生调度运行，电脑休眠/应用关闭不承诺执行；恢复后只补最新周期。成功报告提交推送 origin main，已发布周期跳过。调度与迁移记录见 [migration.md](docs/migration.md)。

免费数据为默认。CNN、当期 ETF 申赎或关键财务输入缺失时会明确标注；模型情景不是概率或收益承诺。
