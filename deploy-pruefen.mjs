// Deployment verification only; existing URLs and server settings stay unchanged.
import { pathToFileURL } from 'node:url';

const hosts = new Set(['heger.earth', 'www.heger.earth']);
const redirects = new Set([301, 302, 303, 307, 308]);
const path = '/reverse-aging/';

function checkedUrl(value) {
  const url = new URL(value);
  if (!hosts.has(url.hostname) || !['http:', 'https:'].includes(url.protocol) || url.port || url.username || url.password || url.pathname !== path || url.search || url.hash) {
    throw new Error('Unerwartetes Prüfziel; keine Zugangsdaten gesendet.');
  }
  return url;
}

async function resolveAnonymous(entry, fetchImpl) {
  let url = checkedUrl(entry);
  const seen = new Set();
  for (let count = 0; count <= 5; count++) {
    if (seen.has(url.href)) throw new Error('Weiterleitungsschleife im Prüfaufruf.');
    seen.add(url.href);
    const response = await fetchImpl(url.href, { redirect: 'manual', signal: AbortSignal.timeout(20000) });
    await response.body?.cancel();
    if (!redirects.has(response.status)) return { url, status: response.status, redirects: count };
    if (count === 5) throw new Error('Zu viele Weiterleitungen im Prüfaufruf.');
    const location = response.headers.get('location');
    if (!location) throw new Error('Weiterleitung ohne Ziel.');
    const next = checkedUrl(new URL(location, url).href);
    if (url.protocol === 'https:' && next.protocol !== 'https:') throw new Error('Unsichere Rückleitung abgewiesen.');
    url = next;
  }
  throw new Error('Prüfziel nicht ermittelt.');
}

export async function checkPublic({ expectedCommit, fetchImpl = fetch, entry = 'http://heger.earth/reverse-aging/' } = {}) {
  if (!/^[0-9a-f]{40}$/.test(expectedCommit || '')) throw new Error('Ungültiger erwarteter Commit.');
  const target = await resolveAnonymous(entry, fetchImpl);
  if (target.status !== 200) throw new Error(`Reverse-Aging-Seite: HTTP ${target.status} statt 200.`);
  const versionUrl = new URL('version.json', target.url);
  versionUrl.searchParams.set('commit', expectedCommit);
  const response = await fetchImpl(versionUrl.href, {
    redirect: 'manual', signal: AbortSignal.timeout(20000), headers: { 'Cache-Control': 'no-cache' }
  });
  if (response.status !== 200) {
    await response.body?.cancel();
    throw new Error(`Live-Version: HTTP ${response.status} statt 200; keine weitere Weiterleitung.`);
  }
  const version = await response.json();
  if (!/^[0-9a-f]{40}$/.test(version?.commit || '') || version.commit !== expectedCommit) {
    throw new Error('Live-Commit stimmt nicht mit dem gepushten Commit überein.');
  }
  if (typeof version.deployed_at !== 'string' || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|[+-]\d{2}:\d{2})$/.test(version.deployed_at) || !Number.isFinite(Date.parse(version.deployed_at))) {
    throw new Error('deployed_at ist keine gültige ISO-Zeit.');
  }
  return { public: target.status, redirects: target.redirects, target: target.url.href, version_url: versionUrl.href, commit: version.commit, deployed_at: version.deployed_at };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const result = await checkPublic({ expectedCommit: process.argv[2], ...(process.argv[3] ? { entry: process.argv[3] } : {}) });
    console.log(JSON.stringify(result));
  } catch (error) {
    console.error('PRÜFUNG: FEHLER – ' + error.message);
    process.exitCode = 1;
  }
}
