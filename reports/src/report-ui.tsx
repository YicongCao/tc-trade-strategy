import React from 'react';
export { useState } from 'react';

// Small, browser-native presentation components for the migrated reports.
const theme = {
  bg: { editor: 'var(--bg)', primary: 'var(--surface)', secondary: 'var(--surface)' },
  text: { primary: 'var(--text)', secondary: 'var(--muted)', tertiary: 'var(--muted)' },
  stroke: { primary: 'var(--border)', secondary: 'var(--border)', tertiary: 'var(--border)' },
  accent: { primary: 'var(--accent)' },
};
export const useReportTheme = () => theme;
type Props = { children?: React.ReactNode; style?: React.CSSProperties; [key: string]: any };
export function Stack({ children, gap = 12, style }: Props) {
  return <div style={{ display: 'flex', flexDirection: 'column', gap, ...style }}>{children}</div>;
}
export function Row({ children, gap = 12, justify, align, wrap, style }: Props) {
  return <div style={{ display: 'flex', gap, justifyContent: justify, alignItems: align, flexWrap: wrap ? 'wrap' : undefined, ...style }}>{children}</div>;
}
export function Grid({ children, columns = 2, gap = 16, style }: Props) {
  return <div className="grid" style={{ '--columns': typeof columns === 'number' ? `repeat(${columns}, minmax(0, 1fr))` : columns, gap, ...style } as React.CSSProperties}>{children}</div>;
}
export const H1 = ({ children, style }: Props) => <h1 style={style}>{children}</h1>;
export const H2 = ({ children, style }: Props) => <h2 style={style}>{children}</h2>;
export function Text({ children, tone, size, weight, style }: Props) {
  return <div style={{ color: tone === 'secondary' || tone === 'tertiary' ? 'var(--muted)' : undefined, fontSize: size === 'small' ? 13 : undefined, fontWeight: weight === 'bold' ? 700 : weight === 'semibold' ? 600 : undefined, ...style }}>{children}</div>;
}
export const Link = ({ href, children }: Props) => <a href={href} target="_blank" rel="noreferrer">{children}</a>;
export const Divider = ({ style }: Props) => <hr style={style} />;
export const Card = ({ children, variant, style }: Props) => <section className={variant === 'borderless' ? '' : 'card'} style={style}>{children}</section>;
export const CardHeader = ({ children, trailing }: Props) => <header className="card-header"><strong>{children}</strong><small>{trailing}</small></header>;
export const CardBody = ({ children }: Props) => <div className="card-body">{children}</div>;
export const Stat = ({ value, label, tone }: Props) => <div><div className={`stat ${tone || ''}`}>{value}</div><small>{label}</small></div>;
export const Callout = ({ children, title, tone }: Props) => <aside className={`callout ${tone || ''}`}>{title && <strong>{title}</strong>}<div>{children}</div></aside>;
export const Pill = ({ children, active, onClick }: Props) => <button type="button" aria-pressed={!!active} className={active ? 'active' : ''} onClick={onClick}>{children}</button>;
export function Table({ headers, rows, columnAlign = [] }: Props) {
  return <div className="table-wrap"><table><thead><tr>{headers.map((h: any, i: number) => <th key={i} style={{ textAlign: columnAlign[i] }}>{h}</th>)}</tr></thead><tbody>{rows.map((row: any[], i: number) => <tr key={i}>{row.map((cell, j) => <td key={j} style={{ textAlign: columnAlign[j] }}>{cell}</td>)}</tr>)}</tbody></table></div>;
}

const palette = ['#3676d9', '#1e9974', '#ba6a20', '#9355b4'];
function Chart({ categories, series, height = 280, yMin, beginAtZero = true, referenceLines = [], valueSuffix = '', showValues, bars = false }: Props) {
  const values = series.flatMap((s: any) => s.data).filter(Number.isFinite);
  const low = yMin ?? Math.min(...values, ...(beginAtZero || bars ? [0] : []));
  const high = Math.max(...values, ...referenceLines.map((r: any) => r.value), ...(bars ? [0] : []));
  const span = high - low || 1;
  const width = 1000, left = 70, right = 20, top = 30, bottom = 55;
  const plotW = width - left - right, plotH = height - top - bottom;
  const y = (v: number) => top + (high - v) / span * plotH;
  const x = (i: number) => left + (bars ? (i + .5) / categories.length : i / Math.max(1, categories.length - 1)) * plotW;
  return <div className="chart">
    <div className="legend">{series.map((s: any, i: number) => <span key={s.name} style={{ color: palette[i % palette.length] }}>● {s.name}</span>)}</div>
    <svg role="img" aria-label={series.map((s: any) => s.name).join('、')} viewBox={`0 0 ${width} ${height}`}>
      {Array.from({ length: 5 }, (_, i) => { const v = low + span * i / 4; return <g key={i}><line x1={left} x2={width - right} y1={y(v)} y2={y(v)} stroke="var(--border)" /><text x={left - 8} y={y(v) + 4} textAnchor="end">{v.toFixed(1)}{valueSuffix}</text></g>; })}
      {categories.map((c: string, i: number) => <text key={i} x={x(i)} y={height - 20} textAnchor="middle">{c}</text>)}
      {referenceLines.map((r: any, i: number) => <g key={i}><line x1={left} x2={width - right} y1={y(r.value)} y2={y(r.value)} stroke="var(--muted)" strokeDasharray="5 4" /><text x={left + 5} y={y(r.value) - 5}>{r.label}</text></g>)}
      {series.map((s: any, si: number) => {
        const color = palette[si % palette.length];
        const barWidth = plotW / categories.length * .7 / series.length;
        return <g key={s.name}>
          {!bars && <polyline fill="none" stroke={color} strokeWidth="2.5" points={s.data.map((v: number, i: number) => `${x(i)},${y(v)}`).join(' ')} />}
          {s.data.map((v: number, i: number) => <g key={i}>
            {bars ? <rect x={x(i) - barWidth * series.length / 2 + si * barWidth} y={Math.min(y(0), y(v))} width={barWidth - 3} height={Math.abs(y(v) - y(0))} fill={color}><title>{s.name} · {categories[i]}: {v}{valueSuffix}</title></rect> : <circle cx={x(i)} cy={y(v)} r="3" fill={color}><title>{s.name} · {categories[i]}: {v}{valueSuffix}</title></circle>}
            {bars && showValues && <text x={x(i) - barWidth * series.length / 2 + (si + .5) * barWidth} y={y(v) + (v < 0 ? 16 : -6)} textAnchor="middle">{v}{valueSuffix}</text>}
          </g>)}
        </g>;
      })}
    </svg>
    <details><summary>查看图表原始数值</summary><Table headers={['日期 / 指标', ...series.map((s: any) => s.name)]} rows={categories.map((c: string, i: number) => [c, ...series.map((s: any) => `${s.data[i]}${valueSuffix}`)])} /></details>
  </div>;
}
export const LineChart = (props: Props) => <Chart {...props} />;
export const BarChart = (props: Props) => <Chart {...props} bars />;
