// Reverse Aging Routinen – Build für den Routinen-Hub (mehrere kurze Seiten in einer Datei).
// Quelle der Texte: content.md · Kurzfassungen/Karten: hub.json · Aussehen: styles.css · Verhalten: site.js
import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const read = f => fs.readFileSync(path.join(root, f), 'utf8');
const source = read('content.md');
const hub = JSON.parse(read('hub.json'));
const fontPath = path.join(root, 'assets/fonts/barlow-condensed-latin-700-normal.woff2');
const font = fs.existsSync(fontPath) ? fs.readFileSync(fontPath).toString('base64') : '';
const css = read('styles.css').replace('/*FONT*/', font
  ? `@font-face{font-family:"Barlow Condensed";font-style:normal;font-weight:700;font-display:swap;src:url(data:font/woff2;base64,${font}) format("woff2");}`
  : '');
const js = read('site.js');

// ---------- Markdown zerlegen ----------
const body = source.replace(/^---\n[\s\S]*?\n---\n/, '');
const footnotes = new Map();
const lines = [];
for (const line of body.split(/\r?\n/)) {
  const m = line.match(/^\[\^([^\]]+)\]:\s*(.*)$/);
  if (m) footnotes.set(m[1], m[2]); else lines.push(line);
}
const preamble = [];
const sections = new Map();
let current = null;
for (const line of lines) {
  const h2 = line.match(/^##\s+(.+)$/);
  if (h2) { current = h2[1].trim(); sections.set(current, []); continue; }
  if (/^# /.test(line)) continue;
  (current ? sections.get(current) : preamble).push(line);
}

const esc = v => String(v).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const slugify = v => v.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const usedIds = new Set();
function uid(title) {
  const base = slugify(title) || 'abschnitt';
  let id = base, n = 2;
  while (usedIds.has(id)) id = `${base}-${n++}`;
  usedIds.add(id);
  return id;
}

const TAGS = [
  [/\[Buch – verifiziert\]/g, 'book', 'Buch · verifiziert'],
  [/\[Autor – Interview\]/g, 'int', 'Autor-Interview'],
  [/\[Fachliteratur\]/g, 'lit', 'Fachliteratur'],
  [/\[Redaktioneller Vorschlag\]/g, 'red', 'Redaktioneller Vorschlag'],
  [/\[Magazin\]/g, 'mag', 'Magazin'],
];
const tag = (label, kind) => `<span class="tag t-${kind}">${esc(label)}</span>`;

let ctx = null; // { page, order: [], refs: Map }
function inline(value) {
  let t = esc(value);
  t = t.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" loading="lazy">');
  t = t.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    const ext = /^https?:\/\//.test(href);
    return `<a href="${href}"${ext ? ' target="_blank" rel="noopener noreferrer"' : ''}>${label}</a>`;
  });
  t = t.replace(/\[\^([^\]]+)\]/g, (_, id) => {
    if (!ctx) return '';
    if (!ctx.order.includes(id)) ctx.order.push(id);
    const n = ctx.order.indexOf(id) + 1;
    const k = (ctx.refs.get(id) || 0) + 1; ctx.refs.set(id, k);
    return `<sup class="fn"><a href="#fn-${ctx.page}-${id}" id="ref-${ctx.page}-${id}-${k}" aria-label="Quelle ${n}">${n}</a></sup>`;
  });
  t = t.replace(/<\/sup><sup class="fn">/g, '</sup><sup class="fn sep">');
  t = t.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  t = t.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  t = t.replace(/`([^`]+)`/g, '<code>$1</code>');
  for (const [re, kind, label] of TAGS) t = t.replace(re, tag(label, kind));
  return t;
}

function renderBlocks(src) {
  let html = '', para = [], list = null, rows = [], quote = false;
  const fp = () => { if (para.length) { html += `<p>${inline(para.join(' '))}</p>`; para = []; } };
  const cl = () => { if (list) { html += `</${list}>`; list = null; } };
  const cq = () => { if (quote) { html += '</blockquote>'; quote = false; } };
  const ft = () => {
    if (!rows.length) return;
    const r = rows.filter((row, i) => !(i === 1 && row.every(c => /^:?-{3,}:?$/.test(c.trim()))));
    const [head, ...rest] = r;
    html += '<div class="table-wrap"><table><thead><tr>' + head.map(c => `<th>${inline(c.trim())}</th>`).join('') + '</tr></thead><tbody>';
    for (const row of rest) html += '<tr>' + row.map((c, i) => `<td data-label="${esc((head[i] || '').trim())}">${inline(c.trim())}</td>`).join('') + '</tr>';
    html += '</tbody></table></div>';
    rows = [];
  };
  const all = () => { fp(); cl(); ft(); cq(); };
  for (const line of src) {
    const h = line.match(/^(###|####)\s+(.+)$/);
    if (h) { all(); const lvl = h[1].length; html += `<h${lvl} id="${uid(h[2])}">${inline(h[2])}</h${lvl}>`; continue; }
    if (/^---\s*$/.test(line)) { all(); continue; }
    if (/^>\s?/.test(line)) { fp(); cl(); ft(); if (!quote) { html += '<blockquote>'; quote = true; } html += `<p>${inline(line.replace(/^>\s?/, ''))}</p>`; continue; }
    if (quote) cq();
    if (/^\|.*\|\s*$/.test(line)) { fp(); cl(); rows.push(line.trim().slice(1, -1).split('|')); continue; }
    if (rows.length) ft();
    const ul = line.match(/^[-*]\s+(.+)$/), ol = line.match(/^\d+\.\s+(.+)$/);
    if (ul || ol) {
      fp(); const type = ol ? 'ol' : 'ul';
      if (list && list !== type) cl();
      if (!list) { list = type; html += `<${type}>`; }
      html += `<li>${inline((ul || ol)[1])}</li>`; continue;
    }
    if (list && !line.trim()) cl();
    if (!line.trim()) { fp(); continue; }
    para.push(line.trim());
  }
  all();
  return html;
}

// Abschnitt -> Einleitung + aufklappbare Blöcke (### oder #### vor dem ersten ###)
function splitSection(src) {
  const intro = [], blocks = [];
  let cur = null;
  for (const line of src) {
    const h3 = line.match(/^###\s+(.+)$/);
    const h4 = line.match(/^####\s+(.+)$/);
    if (h3 || (h4 && (!cur || cur.level === 4))) {
      cur = { title: (h3 || h4)[1].trim(), level: h3 ? 3 : 4, lines: [] };
      blocks.push(cur); continue;
    }
    (cur ? cur.lines : intro).push(line);
  }
  return { intro, blocks };
}

// Kurzurteil aus der Einleitung lösen (Absatz oder Zitat)
function takeLead(intro) {
  const i = intro.findIndex(l => /^(>\s*)?\*\*Kurzurteil:\*\*/.test(l));
  if (i < 0) return null;
  const out = [];
  let j = i;
  while (j < intro.length && intro[j].trim()) { out.push(intro[j].replace(/^>\s?/, '')); j++; }
  intro.splice(i, j - i);
  return out.join(' ').replace(/^\*\*Kurzurteil:\*\*\s*/, '');
}

// ---------- Module ----------
const pageById = Object.fromEntries(hub.pages.map(p => [p.id, p]));
const arrow = '<span aria-hidden="true">→</span>';

function moduleOverview() {
  const o = hub.overview;
  const cards = o.rhythm.map(r => {
    let h = `<section class="rcard tone-${r.tone}" data-r="${o.rhythm.indexOf(r)}"><div class="rcard-head"><h2>${esc(r.title)}</h2><span>${esc(r.hint)}</span></div>`;
    if (r.lead) h += `<p class="rcard-lead">${esc(r.lead)}</p>`;
    if (r.list) h += '<ol class="anchors-mini">' + r.list.map((x, i) => `<li><span class="num">${i + 1}</span>${esc(x)}</li>`).join('') + '</ol>';
    if (r.week) h += '<div class="week" role="list" aria-label="Beispielwoche">' + r.week.map(([d, w, k]) => `<div role="listitem"><span>${esc(d)}</span><b class="w-${k}">${esc(w)}</b></div>`).join('') + '</div>';
    if (r.weekLegend) h += `<p class="week-legend">${esc(r.weekLegend)}</p>`;
    if (r.rows) h += r.rows.map(([a, b, t, k]) => `<div class="kv"><span>${esc(a)}</span><span class="kv-v">${esc(b)} ${tag(t, k)}</span></div>`).join('');
    if (r.note) h += `<p class="small">${esc(r.note)}</p>`;
    h += '<div class="links">' + r.links.map(([p, l]) => `<a href="#${p}">${esc(l)} ${arrow}</a>`).join('') + '</div></section>';
    return h;
  }).join('');
  const tiles = o.tiles.map(t => `<a class="dtile" href="${t.href}"><span><small>${esc(t.label)}</small><b>${esc(t.title)}</b></span>${t.tag ? tag(t.tag[0], t.tag[1]) : arrow}</a>`).join('');
  const legend = `<p class="legend"><span>Herkunft jeder Empfehlung:</span>${tag('Fachliteratur', 'lit')}${tag('Autor-Interview', 'int')}${tag('Buch · verifiziert', 'book')}${tag('Redaktioneller Vorschlag', 'red')}${tag('Magazin', 'mag')}</p>`;
  const seg = `<div class="tabs rswitch" role="tablist" aria-label="Rhythmus">${o.rhythm.map((r, i) => `<button type="button" role="tab" aria-selected="${i === 0}" tabindex="${i === 0 ? 0 : -1}" data-r="${i}"><b>${esc(['Heute', 'Woche', 'Quartal'][i] || r.title)}</b></button>`).join('')}</div>`;
  return `${seg}<div class="rgrid" data-active="0">${cards}</div><div class="tgrid">${tiles}</div>${legend}`;
}

function moduleMorning() {
  const m = hub.morning;
  const anchors = m.anchors.map(([t, d, v], i) => `<li class="anchor"><span class="num big">${i + 1}</span><span class="anchor-text"><b>${esc(t)}</b><span>${esc(d)}</span></span><span class="pill">${esc(v)}</span></li>`).join('');
  const versions = m.versions.map(([t, d]) => `<div><b>${esc(t)}</b><span>${esc(d)}</span></div>`).join('');
  return `<div class="morning"><div><ol class="anchor-list">${anchors}</ol><div class="versions">${versions}</div><p class="small">${tag(m.tag[0], m.tag[1])} Training und Protein im Detail: <a href="#kraft">Kraft</a> · <a href="#ernaehrung">Ernährung</a></p></div>
  <figure class="a5"><a href="${m.image.src}" target="_blank" rel="noopener"><img src="${m.image.src}" alt="${esc(m.image.alt)}"></a><figcaption>${esc(m.image.caption)}</figcaption></figure></div>`;
}

function pathTabs() {
  return `<div class="tabs" role="tablist" aria-label="Trainingspfad">${hub.paths.tabs.map((t, i) => `<button type="button" role="tab" id="tab-${t.id}" aria-controls="panel-${t.id}" aria-selected="${i === 0}" tabindex="${i === 0 ? 0 : -1}" data-tab="${t.id}"><b>${esc(t.label)}</b><span>${esc(t.sub)}</span></button>`).join('')}</div>`;
}
function modulePaths() {
  const p = hub.paths, s = p.side;
  const panels = p.tabs.map((t, i) => {
    const cards = t.cards.map(c => c[4]
      ? `<div class="ex ex-img"><img src="${c[4]}" alt="${esc(c[1])} als Strichzeichnung" loading="lazy"><small class="lvl">${/^\d+$/.test(c[0]) ? `Übung ${esc(c[0])}` : esc(c[0])}</small><b>${esc(c[1])}</b><span>${esc(c[2])}</span><em>${esc(c[3])}</em></div>`
      : `<div class="ex"><span class="ex-n">${esc(c[0])}</span><b>${esc(c[1])}</b><span>${esc(c[2])}</span><em>${esc(c[3])}</em></div>`).join('');
    return `<div class="panel" role="tabpanel" id="panel-${t.id}" aria-labelledby="tab-${t.id}"${i ? ' hidden' : ''}>
      <div class="exgrid${t.cards[0][4] ? ` exgrid-img n${t.cards.length}` : ''}">${cards}</div>
      <div class="panel-foot"><span>${esc(t.note)}</span><span class="panel-meta">${tag(t.tag[0], t.tag[1])}<a href="#${slugify(t.detail)}">Details ${arrow}</a></span></div></div>`;
  }).join('');
  const prog = `<section class="prog"><div class="prog-head"><h2>Steigerung in drei Phasen</h2><span class="small-inline">${esc(p.progressionNote)}</span>${tag('Redaktioneller Vorschlag', 'red')}</div><div class="prog-steps">${p.progression.map(([a, b, c], i) => `<div class="step s${i + 1}"><b>${esc(a)}</b><span>${esc(b)}</span><small>${esc(c)}</small></div>`).join('')}</div><p class="small"><strong>Regel:</strong> ${esc(p.rule)}</p></section>`;
  const side = `<section class="side"><details open><summary>Vor jeder Einheit</summary><ol>${s.before.map(x => `<li>${esc(x)}</li>`).join('')}</ol><a class="more" href="#${s.beforeHref}">Ausführlich ${arrow}</a></details><details><summary>Sicherheitsgrenzen</summary><p>${esc(s.safety)}</p><a class="more" href="#${s.safetyHref}">Ausführlich ${arrow}</a></details><details class="side-sources"><summary>Quellen</summary><p>Alle Nachweise dieser Seite stehen ganz unten.</p><a class="more" href="#kraft-quellen">Zu den Quellen ${arrow}</a></details></section>`;
  return `<div class="paths">${panels}<div class="kraft-row">${prog}${side}</div></div>`;
}

function moduleCards(id) {
  return '<div class="cgrid">' + hub.cards[id].map(c => `<section class="ccard"><div class="ccard-head"><h2>${esc(c.title)}</h2>${tag(c.tag[0], c.tag[1])}</div><p class="big-num">${esc(c.big)}</p><p class="small">${esc(c.sub)}</p>${c.rows.map(([a, b]) => `<div class="kv"><span>${esc(a)}</span><span class="kv-v">${esc(b)}</span></div>`).join('')}<a class="more" href="#${slugify(c.detail)}">Details ${arrow}</a></section>`).join('') + '</div>';
}

function moduleTests() {
  return '<div class="tests">' + hub.tests.map((t, i) => `<section class="test"><span class="num">${i + 1}</span><h2>${esc(t.name)}</h2><p>${esc(t.how)}</p><p class="test-v">${esc(t.value)}</p>${tag(t.tag[0], t.tag[1])}</section>`).join('') + `</div><p class="note">${esc(hub.testsNote)}</p>`;
}

function moduleTiles() {
  return '<div class="tgrid light">' + hub.tiles.map(t => `<a class="ltile" href="${t.href}"><small>${esc(t.label)}</small><b>${esc(t.title)}</b><span>${esc(t.text)}</span></a>`).join('') + '</div>';
}

const modules = { overview: moduleOverview, morning: moduleMorning, paths: modulePaths, tests: moduleTests, tiles: moduleTiles, cards: id => moduleCards(id) };

// ---------- Seiten ----------
const preQuote = preamble.find(l => /^>\s*\*\*Worum es geht:\*\*/.test(l)) || '';
const missing = [];

function renderPage(page, index) {
  ctx = { page: page.id, order: [], refs: new Map() };
  const single = page.sections.length === 1;
  let lead = page.lead ? esc(page.lead) : '';
  let leadTag = '';
  if (page.leadFromIntroQuote) lead = inline(preQuote.replace(/^>\s*\*\*Worum es geht:\*\*\s*/, ''));
  const parts = page.sections.map(title => {
    const src = sections.get(title);
    if (!src) { missing.push(title); return { title, intro: [], blocks: [] }; }
    return { title, ...splitSection([...src]) };
  });
  const firstLead = takeLead(parts[0].intro);
  if (page.id === 'kraft') { lead = esc(hub.paths.lead); leadTag = ' ' + tag(hub.paths.leadTag[0], hub.paths.leadTag[1]); }
  if (firstLead) {
    if (lead) parts[0].intro.unshift(`**Kurzurteil:** ${firstLead}`, ''); // Seite hat eigene Einleitung: Kurzurteil bleibt im Detail
    else lead = inline(firstLead);
  }

  const headId = single ? uid(parts[0].title) : uid(page.id + '-start');
  const moduleHtml = page.module === 'cards' ? modules.cards(page.id) : modules[page.module]();

  let groups = '';
  const titles = parts.flatMap(p => [...(p.intro.join('').trim() && page.introAs?.[p.title] ? [page.introAs[p.title]] : []), ...p.blocks.map(x => x.title)]);
  const blockCount = titles.length + parts.filter(p => p.intro.join('').trim() && !page.introAs?.[p.title]).length;
  const blockTitles = titles.slice(0, 4).join(' · ') + (titles.length > 4 ? ' …' : '');
  for (const [i, part] of parts.entries()) {
    const gid = single ? uid(page.id + '-details') : uid(part.title);
    const gtitle = page.groupTitles?.[part.title] || (single ? 'Im Detail' : part.title);
    let g = `<section class="group"><h2 class="group-title" id="${gid}">${esc(gtitle)}</h2>`;
    const introHtml = renderBlocks(part.intro);
    if (introHtml.trim()) {
      g += page.introAs?.[part.title]
        ? `<details class="acc" id="${uid(page.introAs[part.title])}"><summary><h3>${esc(page.introAs[part.title])}</h3></summary><div class="acc-body">${introHtml}</div></details>`
        : `<div class="intro">${introHtml}</div>`;
    }
    for (const b of part.blocks) {
      const id = uid(b.title);
      g += `<details class="acc" id="${id}"><summary><h3>${inline(b.title)}</h3></summary><div class="acc-body">${renderBlocks(b.lines)}</div></details>`;
    }
    groups += g + '</section>';
  }

  // Quellen dieser Seite (Fußnoten können in Fußnoten weitere Verweise enthalten – daher Schleife)
  let fnHtml = '';
  for (let k = 0; k < ctx.order.length; k++) {
    const id = ctx.order[k];
    const text = footnotes.has(id) ? inline(footnotes.get(id)) : `<em>Nachweis „${esc(id)}“ fehlt</em>`;
    fnHtml += `<li id="fn-${page.id}-${id}">${text} <a class="back" href="#ref-${page.id}-${id}-1" aria-label="Zurück zur Textstelle">↩</a></li>`;
  }
  let sources = ctx.order.length ? `<details class="acc sources" id="${page.id}-quellen"><summary><h3>Quellen dieser Seite (${ctx.order.length})</h3></summary><div class="acc-body"><ol class="fnlist">${fnHtml}</ol></div></details>` : '';
  if (page.allFootnotes) {
    const saved = ctx; ctx = null;
    const all = [...footnotes].map(([id, t]) => `<li>${inline(t)}</li>`).join('');
    ctx = saved;
    sources += `<details class="acc sources" id="alle-quellennachweise"><summary><h3>Alle Quellennachweise (${footnotes.size})</h3></summary><div class="acc-body"><ol class="fnlist">${all}</ol></div></details>`;
  }

  const prev = hub.pages[index - 1], next = hub.pages[index + 1];
  const pager = `<nav class="pager" aria-label="Seitenwechsel">${prev ? `<a href="#${prev.id}"><small>Zurück</small><b>← ${esc(prev.nav)}</b></a>` : '<span></span>'}${next ? `<a class="next" href="#${next.id}"><small>Weiter</small><b>${esc(next.nav)} →</b></a>` : '<span></span>'}</nav>`;

  return `<section class="page tone-${page.tone}" id="${page.id}" data-page data-title="${esc(page.nav)}"${index ? ' hidden' : ''}>
  <header class="page-head"><div><p class="eyebrow">${esc(page.eyebrow)}</p><h1 id="${headId}" tabindex="-1">${esc(page.title)}</h1>${lead ? `<p class="lead">${lead}${leadTag}</p>` : ''}</div>${page.id === 'ueberblick' ? '<a class="disclaimer" href="#praktische-sicherheitsgrenzen">Keine medizinische Beratung · Sicherheitsgrenzen</a>' : ''}${page.module === 'paths' ? pathTabs() : ''}</header>
  ${moduleHtml}
  <details class="acc all-details" id="${uid(page.id + '-ausfuehrlich')}"><summary><h2>Ausführlich: ${blockCount} ${blockCount === 1 ? 'Abschnitt' : 'Abschnitte'}</h2><span class="small-inline">${esc(blockTitles)}</span></summary><div class="groups">${groups}</div></details>
  ${sources}
  ${pager}
</section>`;
}

const pagesHtml = hub.pages.map(renderPage).join('\n');
const unused = [...sections.keys()].filter(t => !hub.pages.some(p => p.sections.includes(t)));
if (missing.length || unused.length) {
  console.error('Abschnitte fehlen oder sind keiner Seite zugeordnet:', { missing, unused });
  process.exit(1);
}

const ICONS = {
  grid: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
  sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/>',
  dumbbell: '<path d="M6 7v10M18 7v10M3 10v4M21 10v4M6 12h12"/>',
  chart: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
  more: '<circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>',
};
const icon = n => `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">${ICONS[n]}</svg>`;
const topNav = hub.pages.map(p => `<a href="#${p.id}" data-nav="${p.id}">${esc(p.nav)}</a>`).join('');
const mobileMain = hub.pages.filter(p => p.mobile).map(p => `<a href="#${p.id}" data-nav="${p.id}">${icon(p.icon)}<span>${esc(p.nav)}</span></a>`).join('');
const mobileMore = hub.pages.filter(p => !p.mobile).map(p => `<a href="#${p.id}" data-nav="${p.id}">${esc(p.nav)}</a>`).join('');

const html = `<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Reverse Aging als Routine: Morgenroutine, Krafttraining, Ausdauer, Gleichgewicht, Ernährung und Selbsttests – mit Herkunft und Evidenz zu jeder Empfehlung.">
<meta name="theme-color" content="#14201C">
<title>${esc(hub.title)}</title>
<style>${css}</style>
</head>
<body>
<a class="skip" href="#main">Zum Inhalt</a>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="#ueberblick">REVERSE AGING <span>ROUTINEN</span></a>
    <nav class="topnav" aria-label="Hauptnavigation">${topNav}</nav>
    <span class="stand">${esc(hub.standShort)}</span>
  </div>
</header>
<main id="main">
${pagesHtml}
</main>
<footer class="foot"><span>Reverse Aging · Routinen für ein starkes Älterwerden · Stand ${esc(hub.stand)}</span><span>Unabhängige, quellenkritische Darstellung · keine medizinische Beratung</span></footer>
<nav class="tabbar" aria-label="Hauptnavigation mobil">${mobileMain}<button type="button" class="more-btn" aria-expanded="false" aria-controls="more-sheet">${icon('more')}<span>Mehr</span></button></nav>
<div class="more-sheet" id="more-sheet" hidden>${mobileMore}</div>
<script>${js}</script>
</body>
</html>`;

fs.mkdirSync(path.join(root, 'dist'), { recursive: true });
fs.writeFileSync(path.join(root, 'dist', 'index.html'), html);
const copyAssets = process.argv.includes('--assets');
if (copyAssets) {
  for (const f of ['morgenroutine-a5.png', 'morgenroutine-sketchnote.png']) fs.cpSync(path.join(root, 'assets', f), path.join(root, 'dist', 'assets', f));
  fs.cpSync(path.join(root, 'assets', 'workouts'), path.join(root, 'dist', 'assets', 'workouts'), { recursive: true });
}
console.log(`Built dist/index.html (${html.length} bytes, ${hub.pages.length} Seiten, ${footnotes.size} Nachweise)`);
