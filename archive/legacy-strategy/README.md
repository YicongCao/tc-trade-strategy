# 历史策略系统归档

2026-10-18 仓库改为纯市场研究。本目录冻结旧策略镜像、账户复盘、us-mushroom 筛选流程、调度脚本、未实现占位与旧平台执行说明。归档内容不是当前 Codex 指令；新技能不得默认读取。

| 原路径 | 归档位置 |
| --- | --- |
| strategies/, reviews/, backtest/, metrics/, scripts/, data/symbols.txt | 本目录下同名相对路径 |
| src/tc_trade_strategy/{premarket,market_data,screening}.py | 本目录下同名相对路径 |
| tests/{test_market_data,test_screening}.py | 本目录下同名相对路径 |
| .agents/skills/{tc-review,market-research} | skills/ 下对应目录，退出技能发现 |
| dependencies/ 旧平台与流程文件 | dependencies/ 下原名；当前市场接入说明已重写 |
| reports/src/, build.mjs, style.css, package*.json | reports/ 下同名路径；普通 React 历史渲染器 |
| 原 README.md / AGENTS.md | README.original.md / AGENTS.original.md |

所有旧文件日期及原有数据保留，不改写历史结论。历史快照 sources 与 results 原本被忽略，继续仅本地保存；原始账户数据不会因目录移动而新增入库。迁移前 Git 版本为 `e26fdc4`，可逐文件对照。

恢复时先备份活跃文件，再按表复制需要的文件到原路径；不要整体重置仓库。恢复旧技能需用户明确决定，勿复制整个 skills 目录回自动发现路径。旧 Python 入口需要恢复相应 pyproject 命令；恢复旧 launchd 不属于新研究流程。

旧8份报告可在本地 `results/reports/` 查看；构建源位于本目录 reports/src/snapshots（忽略）。恢复旧 reports 目录到原位置后按 README.original.md / 历史文档构建，避免与新 reports 索引互相覆盖。
