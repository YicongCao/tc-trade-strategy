# AGENTS.md

## Cursor Cloud specific instructions

### 这是一个文档 / 研究仓库，没有可运行的应用

- 仓库当前**只有 Markdown**：策略原文在 `strategies/`、平台与 MCP 参考在 `dependencies/`、每日预期/复盘在 `notebooks/`。
- `backtest/`、`data/`、`metrics/`、`tests/` 目前都只有 `.gitkeep` 占位（README「计划」里的第一阶段尚未动工），因此**没有依赖清单、没有构建、没有自动化测试、没有 lint 配置**。
- 不要为了"跑起来"去凭空创建回测引擎或测试框架，除非任务明确要求。真正的开发动作发生在下面说的 MCP 工作流里，而不是本地代码。

### 环境与工具

- VM 自带 Python 3.12 与 PyYAML 6.x，`git` 已配置好 `user.name` / `user.email`。当前没有任何需要安装的项目依赖。
- 启动更新脚本是最小化的：仅在将来出现 `requirements.txt` 时才 `pip install`，现状下是空操作，无需手动跑。
- 想快速自检策略文档是否自洽（YAML frontmatter 合法、`strategy_id`/`status` 齐全、README 表格与文件一一对应），可用 PyYAML 解析各 `strategies/*.md` 的 frontmatter 比对；这是本仓库唯一"可执行"的核对动作。

### 核心工作流依赖 Trade Copilot MCP（云端默认不可用）

- 仓库的实际操作（`/review` 复盘、`create_strategy` / `update_strategy` 等写工具）全部通过 **Trade Copilot MCP 服务器**完成，工具 schema 见 `dependencies/trade-copilot-mcp.md`。
- **本云端环境只挂了 `cursor-cloud` 诊断 MCP，没有 Trade Copilot MCP**，也没有对应 OAuth。因此拉实盘数据、跑复盘、改平台策略在这里都无法执行，需要用户在 Cursor 里配置并授权该 MCP 服务器。
- 已知坑：MCP 工具清单**只在 `~/.cursor/mcp.json` 配置指纹变化时才刷新**，换对话、重新 OAuth 都无效；办法是给配置块加个无害字段（如 `"headers": {}`）触发重连再授权，详见 `dependencies/trade-copilot-mcp.md` 的「工具清单刷新」。

### 内容约定（改动前必读）

- 策略是**平台的镜像**：先在平台改提示词，再同步回 `strategies/`，同步后用 `get_strategy_profile` 回读核对，别只信 UI 保存提示。
- 字段口径沿用平台：`stop_loss_pct` / `max_position_pct` / `max_positions` 等，指标参数见 `dependencies/README.md`。
- 提交 / 推送遵循 `.cursor/rules/git-workflow.mdc`（前缀 `chore:`/`docs:`/`feat:`/`fix:`，正文说明"为什么"）。推送前用其中的正则扫一遍凭证类信息；对象级 UUID（如 `strategy_id`）可入库，但 API Key / OAuth token / `user_id` 不可入库。
