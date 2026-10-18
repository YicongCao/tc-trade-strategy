# 可移植研究报告

报告为独立 HTML，不依赖特定编辑器的渲染 SDK。所有脚本和样式内嵌，打开生成文件即可使用；链接到的外部来源仍需要网络。

```bash
npm ci --prefix reports
npm run build --prefix reports
```

构建器读取 `reports/src/snapshots/*.report.tsx`，生成 `results/reports/*.html` 和 `index.html`。快照内嵌真实数据、观测日及来源，属于本地研究产物，未提交到 Git；全新克隆需先生成或恢复快照，不能只靠构建器重建历史数据。

从仓库根目录启动预览：

```bash
.venv/bin/python -m http.server 8765 --bind 127.0.0.1 --directory results/reports
```

然后在 Codex 浏览器打开 `http://127.0.0.1:8765/`。服务仅暴露报告输出目录。也可直接用浏览器打开 HTML 文件。

现有报告入口：

- [报告目录](../results/reports/index.html)
- [市场舆情与资金分析 · 2026-10-18](../results/reports/market-intelligence-2026-10-18.html)
- [项目与行情检查 · 2026-10-18](../results/reports/project-data-review-2026-10-18.html)

新报告使用 `src/report-ui.tsx` 的普通 React 组件或原生 HTML；共享组件只处理展示。数据采集代码留在 Python 包中。输出保持数据日期，不能把构建时间当作行情更新日。

验证应覆盖构建、浏览器实际显示、分页/筛选等交互以及图表数值。`npm ci` 使用锁文件安装依赖；浏览器运行时无需 CDN 或外网包。
