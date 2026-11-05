import { createRequire } from 'node:module'; import fs from 'node:fs'; const { chromium } = createRequire(import.meta.url)('playwright');
const b = await chromium.launch(); const p = await b.newPage({ viewport:{width:800,height:400}, deviceScaleFactor:2 });
for (const f of fs.readdirSync('.').filter(f=>f.endsWith('.svg'))) {
  await p.setContent(`<html><body style="margin:0;background:transparent">${fs.readFileSync(f,'utf8')}</body></html>`);
  await p.locator('svg').screenshot({ path: f.replace('.svg','.png'), omitBackground: true });
}
await p.setContent(`<html><body style="margin:0;background:#FAFAF7;display:grid;grid-template-columns:1fr 1fr;width:1600px">${fs.readdirSync('.').filter(f=>f.endsWith('.svg')).map(f=>fs.readFileSync(f,'utf8')).join('')}</body></html>`);
await p.setViewportSize({width:1600,height:1200}); await p.screenshot({path:'sheet.png', fullPage:true}); await b.close();
