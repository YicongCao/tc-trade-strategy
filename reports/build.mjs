import { build } from 'esbuild';
import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.dirname(fileURLToPath(import.meta.url));
const sourceDir = path.join(root, 'src/snapshots');
const outputDir = path.resolve(root, '../results/reports');
const files = (await readdir(sourceDir)).filter(f => f.endsWith('.report.tsx')).sort();
if (!files.length) throw new Error('reports/src/snapshots 中没有报告源文件');
await mkdir(outputDir, { recursive: true });
const css = await readFile(path.join(root, 'style.css'), 'utf8');
const escape = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('"', '&quot;');
const pages = [];
for (const file of files) {
  const name = file.replace('.report.tsx', '');
  const result = await build({
    stdin: {
      contents: `import React from 'react'; import {createRoot} from 'react-dom/client'; import Report from './src/snapshots/${file}'; createRoot(document.getElementById('root')).render(<Report/>);`,
      resolveDir: root, loader: 'tsx',
    },
    bundle: true, write: false, minify: true, jsx: 'automatic',
    define: { 'process.env.NODE_ENV': '"production"' },
    legalComments: 'inline',
  });
  const script = result.outputFiles[0].text.replaceAll('</script', '<\\/script');
  await writeFile(path.join(outputDir, `${name}.html`), `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${escape(name)}</title><style>${css}</style></head><body><nav><a href="index.html">报告目录</a><span>历史研究快照 · 以报告内日期为准</span></nav><main id="root"></main><noscript>此交互报告需要启用 JavaScript，所有资源已内嵌，无需外网连接。</noscript><script>${script}</script></body></html>`);
  pages.push(`<li><a href="${escape(name)}.html">${escape(name)}</a></li>`);
}
await writeFile(path.join(outputDir, 'index.html'), `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>tc 研究报告</title><style>${css}</style></head><body><main class="catalog"><h1>tc 研究报告</h1><p>独立 HTML，可离线打开。保留原始研究日期，旧报告不代表最新行情。</p><ul>${pages.join('')}</ul></main></body></html>`);
console.log(`Built ${files.length} standalone reports in ${outputDir}`);
