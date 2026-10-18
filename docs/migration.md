# 迁移与运行状态

迁移日：2026-10-18；迁移前提交：e26fdc4。仓库名、origin 远程与 tc 现有授权保留。

- 活跃技能统一为 `.agents/skills/us-market-research`；旧 market-research、tc-review 移到 `archive/legacy-strategy/skills/`，不自动发现。
- 旧策略镜像、账户复盘、筛选器与测试、旧 launchd 脚本、回测/指标占位和执行平台文档均可从归档恢复。原路径映射见 [归档说明](../archive/legacy-strategy/README.md)。
- 旧8份报告与原始快照继续保留历史日期，未跟踪大文件仍在本地；新报告才按 modes/period/run 进入 Git。
- 旧 launchd 标识 `com.yicong.tc-trade-strategy.premarket` 已 bootout。原 plist 在 `~/Library/LaunchAgents/` 移除前已逐字节核验备份；备份位于 `~/.codex/backups/us-market-assistant-2026-10-18/`。不自动恢复旧任务。
- 当前渲染器纯 Python + 独立 HTML；旧 React 构建器仅用于历史恢复。新工作流无需 Node 或第二套模型 API。

## 原生调度

日报：北京时间周二至周六08:00。周报：北京时间周日10:00。实时按需。

已通过 Codex automation_update 创建并读取确认两个 ACTIVE heartbeat：`daily-08-00`、`weekly-10-00`，绑定当前研究会话。已核对本机时区 CST +0800（Asia/Shanghai）；日历归属仍使用纽约。若今后修改本机时区，应同步检查调度时间。自动任务调用统一技能，核心数据不可核验时仅记录失败；成功推送后通知报告链接。电脑休眠/应用关闭不保证运行，恢复后只补最新应生成周期。

运行条件依据 [OpenAI 本地调度说明](https://learn.chatgpt.com/docs/automations)（2026-10-18 核验）。
