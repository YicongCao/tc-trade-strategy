# Codex 工作流与迁移记录

2026-10-18：本项目从 Cursor 工作流迁移到 Codex。业务代码、策略原文、历史数据和 Git 远程保持原用途。

## 当前入口

- `AGENTS.md`：项目目的、中文沟通、数据口径、验证、Git 和报告交付约定。
- `.agents/skills/tc-review/SKILL.md`：原交易复盘命令，改用 `$tc-review`，避免与代码审查混淆。
- `.agents/skills/market-research/SKILL.md`：行情、新闻、预测市场、风险、轮动及 AI 主题研究。
- `dependencies/risk-config-warnings.md`：原常驻风控规则的专题参考；当前接口和历史案例分开标注。
- `reports/`：浏览器原生报告组件与构建脚本；`results/reports/index.html` 为本地报告目录。
- `~/.codex/config.toml`：已有 tc 连接。迁移没有复制凭证或新增重复连接。

项目目录布局遵循 [Codex 技能](https://learn.chatgpt.com/docs/build-skills)、[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) 和 [MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) 官方文档。

## 常用提示词

直接描述目标和范围即可，日期按需要替换：

```text
$tc-review 2026-10-16
对照冻结的预期，核验实际决策和成交，给出命中、落空、无法判定及依据。
```

```text
$market-research
更新美股事件预期、风险指标、板块轮动与 AI 交易主题。
标注各来源观测日，区分价格轮动和资金申赎，输出独立 HTML 报告。
```

```text
检查 us-mushroom 的筛选数据是否新鲜，修复导致陈旧数据进入结果的问题，
保留真实缺口，运行相关检查，并按仓库约定提交推送。
```

```text
分析 DRAM 网格的风控告警，结合当前配置与历史复盘说明是否需要修改。
如需改动，先准备字段 diff；本次只做分析，不执行平台变更。
```

## 用户级技能清理

原 `~/.agents/skills/` 中有 26 个技能，其中多项只改了产品名称，实际仍依赖旧产品路径、SDK 和工具。完整备份位于本机 `~/.codex/backups/cursor-migration-2026-10-18/`，不进入仓库。

- 保留可跨客户端使用的 `autopilot`、`shell`、`split-to-prs`。
- `canvas`、`visualize` → `portable-reports`，不再强制私有 Canvas 格式。
- `create-rule`、`create-hook`、`create-subagent`、`update-cli-config`、`update-cursor-settings`、`statusline` → `codex-configuration`，按实际官方接口实施。
- `create-skill` → 系统 `skill-creator`；`sdk` → 系统 `openai-docs` 核验当前 Codex SDK；不继续引用其他产品 SDK。
- `automate`、`loop`、`rename-chat`、`goal`、`onboard` → `codex-app-workflows` 和当前原生工具。
- `review`、`review-bugbot`、`review-security` → `code-review`，不依赖固定名称的旧子代理。
- `new-repo`、`origin`、`share` → `git-publishing`，使用实际 Git 远程。
- `migrate-to-skills` → `migrate-project-to-codex`。
- `deploy-with-vercel` 的旧固定 MCP 工作流退出自动发现；需要部署时使用当前可用插件或项目 CLI，接入后按实际接口执行。本次没有安装部署能力。

23 个旧技能已退出发现目录；6 个原生替代技能加上保留的 3 个技能构成新的用户级集合。系统和插件托管技能未改写。通用偏好另写入 `~/.codex/AGENTS.md`。

## 报告迁移

项目原私有目录内的 8 份报告均转为 `.report.tsx` 普通 React 源文件，依赖本项目 `report-ui.tsx`，输出独立 HTML。主题切换、事件搜索、质量过滤、周期切换、图表与表格保留；图表另提供原始数值表。迁移不刷新历史行情或改变研究日期。

含数据的报告源文件保存在 `reports/src/snapshots/`，输出保存在 `results/reports/`，均被 Git 忽略。代码和构建器入库，用户数据留本地。备份含原始 8 份文件；清理私有目录前先验证转换结果。

验证结果：8 份报告均在 Codex 浏览器实际渲染；舆情报告的六个标签、搜索、质量过滤及板块周期切换通过；历史图表显示正常，原数据与文字逐文件一致。Python 9 项测试与 Ruff 检查通过，8 个新技能通过格式验证。迁移还修复了项目移动目录后虚拟环境脚本残留的旧绝对路径。

## 验证与恢复

新技能可由 Codex 自动发现；若选择器仍显示旧技能，重启 Codex 后检查。已有会话可能保留旧上下文，但本项目明确要求使用新入口。

项目规则和说明可从迁移前提交 `3295bb8` 恢复；回退时应只恢复相关文件，不整体重置后续工作。用户级原始技能及原报告位于上述备份目录，`manifest.json` 记录替换清单。恢复用户级技能前先备份当前版本，避免覆盖后来改动。
