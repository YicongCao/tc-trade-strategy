# AGENTS.md

## Cursor Cloud specific instructions

这是一个**纯文档 / 研究型仓库**，不是可构建运行的应用工程。理解这一点能省掉大量找不到入口的时间：

- 没有源码、没有依赖清单（`requirements.txt` / `pyproject.toml` / `package.json` 都不存在），也没有构建产物。`backtest/`、`data/`、`metrics/`、`tests/` 目前都只有 `.gitkeep`，README 里的回测引擎属于"计划"，尚未落地。
- `.gitignore` 里的 Python 工具链（pytest / ruff / mypy）是**为将来预留**的，当前没有对应代码，所以「装依赖 / 跑 lint / 跑测试 / 构建」这些步骤此刻都没有实际对象，缺少 `ruff`、`pytest` 属正常现象，不是环境损坏。
- 系统自带 Python 3.12 + PyYAML 6，足以校验/编辑策略文档，无需额外安装。所以 update script 是空操作。

### 真正的「应用」是 Trade Copilot MCP + Markdown 工作流

本仓库的核心能力靠外部 **Trade Copilot MCP 服务器**（HTTP，端点 `https://tc.zkd.me/api/mcp`）提供：读写策略、拉决策/成交/复盘数据。相关工具口径见 `dependencies/trade-copilot-mcp.md`，平台能力见 `dependencies/trade-copilot-platform.md`，开发前先读 `dependencies/README.md`。

- 该 MCP **不会随 VM 自动接入**，也不能靠 update script 装。要在 Cloud Agent 里用它，必须由用户在 [cursor.com/agents](https://cursor.com/agents) 的 MCP 设置里以 **HTTP** 传输添加该 server 并完成一次 **OAuth 授权**（支持动态客户端注册，无需平台侧配合）。授权前 `GetMcpTools` 只能看到 `cursor-cloud`，看不到 `trade-copilot`，此时所有策略读写类任务都无法进行。
- 已知坑：**MCP 工具清单只在 `~/.cursor/mcp.json` 的配置指纹变化时才刷新**——换新对话、重新 OAuth 都无效，须改配置块（如加 `"headers": {}`）触发重连，详见 `dependencies/trade-copilot-mcp.md` 的「工具清单刷新」。
- MCP 的 K 线/行情有限制（一次一个标的、最多 120 根、无分钟级），**不能当回测数据源**；但平台喂给 AI 策略的 K 线是完整的，两条管道不同源，别混用。

### 常见任务从哪入手

- **复盘**：用 `/review`（定义在 `.cursor/commands/review.md`），可带日期参数如 `/review 2026-07-30`，不带则取 `notebooks/` 下最新的 `*-expectations.md`。整套流程依赖上面的 MCP 已接入。
- **改策略**：改动是单向的——**先在平台改，再把提示词原文同步回 `strategies/`**，仓库是镜像；同步后用 `get_strategy_profile` 回读核对。策略文件带 YAML frontmatter（`strategy_id`、`risk_config` 等，字段口径抄平台）。
- **校验策略文档**：可用 PyYAML 快速解析所有 `strategies/*.md` 的 frontmatter 做规范性自检，例如
  `python3 -c "import glob,re,yaml;[yaml.safe_load(re.match(r'---\n(.*?)\n---',open(f).read(),16).group(1)) for f in glob.glob('strategies/*.md')]"`。

### Git 约定

见 `.cursor/rules/git-workflow.mdc`：完成变更即提交并推送，提交摘要用中文，`strategy_id` 等对象 UUID 可入库，但 API Key / OAuth token / `user_id` 一律不入库。
