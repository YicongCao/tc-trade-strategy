# 公开市场报告与私人持仓附录

用户已授权三种模式每次运行两个关联阶段，包括定时任务；不需要反复询问。公共阶段使用本技能，私人阶段使用本仓库 `.agents/skills/ibkr-position-review/SKILL.md`，这是串联技能，不是授权创建子代理。

1. 先完成公开市场研究并校验/发布，记录具体报告目录和截止时间。持仓不是公开报告的输入，公共JSON、正文、索引、Git提交和定时提示词不得带私人持仓、数量、账户金额或私人附录路径；公共标的选择仍以市场证据为依据。
2. 按私人技能只读查看授权的 IBKR Trader 当前持仓/风险摘要，逐项研究相关公司或指数将发生的事件，复用刚生成的公共研究，必要时补查公开来源。私人目标URL只保存在忽略的 `sensitive/position-reviews/browser-target.json`，不可写入Git或定时任务提示词。只允许向公共行情/搜索工具提供必要证券代码，不传账户数量、成本和资金。
3. 私人分析JSON保存在 `sensitive/position-reviews/inputs/{run}.json`，通过 `python -m tc_trade_strategy.position_review --public-report reports/{mode}/{period}/{run} --input sensitive/position-reviews/inputs/{run}.json` 输出同源 Markdown/HTML/JSON。路径为 `sensitive/position-reviews/{mode}/{period}/{public_run}/{private_run}/`。私人附录单向记录公共目录与证据摘要hash；公共文件不写回私人信息。
4. 公共报告已发布时，可复用本时段/周期已有版本；检查该 public_run 对应的私人附录，已成功完成同一联动任务则跳过重复。私人先前失败则只重试私人阶段，读取最新实际持仓，不重写公共报告。重试采用新版本、不覆盖旧失败记录。手动 realtime 每次完整刷新并生成新配对。
5. 浏览器不可用、未登录、页面异常、持仓无法核验：私人部分 status=unavailable，只记原因与待处理事项，不生成看似完整的持仓建议，不阻止公共报告发布。公共报告已生成但push失败时可关联本地版本并在私人gaps注明；公共核心市场状态无法核验时只记录失败，不用旧公共报告冒充本次最新结论。
6. 完成通知提供公共链接和私人本地路径；通知正文无需列账户数值。不向邮件/社交平台发送。私人附录不进入公共索引、不调用publish、不提交Git。

Daily 每天北京时间08:00与20:00，含周末/假日。主体仍为最近已完成纽约交易日；晚间更新当时盘前/盘中/休市消息与下一催化剂，不能因没有新收盘日就跳过。早晚独立 delivery_slot；08点前恢复只补上一晚20点，08至20点补当天08点，20点后补当天20点。status/prepare/build 使用实际时点，build 的 cutoff 必须晚于全部取证；通常自动取运行时间即可。若取证跨过下一个08/20时段，重新检查最新时段去重，不能伪造旧时点。Weekly 保持北京时间周日10:00；realtime按需。市场阶段以纽约日历确定，不写死早晚对应阶段。
