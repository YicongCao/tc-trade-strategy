# Codex 工作约定 · 美股主观交易辅助器

本仓库是数日至数周波段交易的纯市场研究助手。中文沟通，先结论，再证据、时点与限制。使用 `$us-market-research`，模式为 `weekly | daily | realtime`。

## 边界

- 三种模式均输出关联的公开市场报告与本地私人持仓附录。公共报告阶段只读取公开行情、新闻、经济日历与披露；私人阶段按用户持续授权调用 `ibkr-position-review`，只读查看已授权 IBKR Trader 的当前持仓与风险摘要，结合公共研究逐项检查事件并提出条件式建议。独立账户复盘仍限用户已授权页面或文件；延续同一授权不重复确认。不修改 tc 策略，不执行交易。
- tc 仅调用 `get_market_overview`、`get_symbol_quotes`、`get_symbol_kline`、`get_trading_calendar`、`list_news_for_period`。工具当前 schema 优先于旧文档。
- 新工作流不默认读取 `archive/`。归档保存历史用途，不是当前指令。
- `sensitive/` 是用户本地存放账户交易记录、IBKR 密钥等敏感资料的目录，整个目录不入 Git。公共市场研究、报告和发布流程不得读取、复制或上传其中内容；不得强制暂存。用户已授权建立 `sensitive/market-indicators/`：仅在此子目录保存公开市场指标与评估历史，允许本地历史比较；公共报告不得读取它，只能从公开报告比较，不扫描 sensitive 其他路径。已授权的个人分析只访问指定资料，输出留在该目录，不读取登录密钥、不进入公共报告或自动发布。关联流程额外只允许读取 `sensitive/position-reviews/browser-target.json` 的站点定位信息、当前私人分析输入与同类附录，不扫描其他敏感目录；不得读取密钥。站点不可访问或数据未核验时写私人失败附录，公共报告照常处理。
- 不新增付费订阅、公开站点或需要模型 API Key 的研究服务。

## 研究与交付

- 项目技能在 `.agents/skills/`，常驻约定在本文件。Codex MCP 使用现有授权；接入说明见 `dependencies/trade-copilot-mcp.md`。
- 研究日属于 `America/New_York`，同时展示 `Asia/Shanghai`；使用交易日历处理节假日、半日市和夏令时。记录真实生成时间，不伪造历史时点。
- 五类信息每次均检查。事实、推断、假设分开；预测市场报价不等于客观概率；上涨或放量不等于主力净流入。缺口明确列出。
- 研究对象生成同源 Markdown / 独立 HTML / 精简 JSON，写入 `reports/{mode}/{period}/{run}/`。已发布版本不可修改。根目录入口为 `README.md`，历史入口为 `reports/index.html`。
- 不生成依赖其他编辑器 Canvas 的文件，不写编辑器私有报告目录。交付用可点击绝对路径；HTML 需实际浏览器验证。
- 原始响应、新闻全文、缓存和运行日志放忽略的 `results/`；个人账户资料与密钥放忽略的 `sensitive/`，不能混入证据 JSON。

## 执行与验证

```bash
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m tc_trade_strategy.research --help
.venv/bin/pytest -q
.venv/bin/ruff check src tests
```

流程与输入契约见 `docs/research-workflow.md`、`docs/data-contract.md`。运行锁保护写入和发布；失败保留本地成果。核心市场状态无法核验时只写失败记录。

## Git

- 沿用用户授权：实现变更验证后提交推送 `origin main`，仓库名和远程不变。只暂存本次相关文件，不强推、不覆盖他人工作。
- 日常报告用 `us-market-research publish --report ...`，只暂存该报告和历史索引。已有暂存内容则停止，保留原状。
- 凭证、账户标识、完整接口响应不入库。历史原本未跟踪的大文件不因归档批量提交。
- 报告成功推送后给出链接；失败说明原因与本地路径。Daily 每天北京时间08:00和20:00按日期+时段去重，休市仍更新消息；Weekly 周日10:00按交易周去重。恢复只补最新应生成时段/周期。公共已发布时可复用，但仍检查关联私人附录，不能因公共去重省略私人阶段。
