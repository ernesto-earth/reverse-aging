import assert from 'node:assert/strict';
import test from 'node:test';
import { checkPublic } from './deploy-pruefen.mjs';

const source = 'http://heger.earth/reverse-aging/';
const destination = 'https://www.heger.earth/reverse-aging/';
const commit = 'a'.repeat(40);
const version = { commit, deployed_at: '2026-11-07T08:05:46.488Z' };
function fixture(responses) {
  const calls = [];
  const fetchImpl = async (url, options) => {
    calls.push({ url, options });
    assert.equal(options.redirect, 'manual');
    assert.equal(options.headers?.authorization, undefined);
    const next = responses.shift();
    assert.ok(next, 'Unexpected extra request.');
    return new Response(next.body || '', { status: next.status, headers: next.location ? { location: next.location } : {} });
  };
  return { calls, fetchImpl };
}
const allowed = () => [{ status: 301, location: destination }, { status: 200 }, { status: 200, body: JSON.stringify(version) }];
const check = f => checkPublic({ expectedCommit: commit, fetchImpl: f.fetchImpl });

test('existing redirect, anonymous requests and exact live commit at checked target', async () => {
  const f = fixture(allowed());
  assert.deepEqual(await check(f), { public: 200, redirects: 1, target: destination, version_url: destination + 'version.json?commit=' + commit, ...version });
  assert.deepEqual(f.calls.map(c => c.url), [source, destination, destination + 'version.json?commit=' + commit]);
  assert.equal(f.calls[2].options.headers['Cache-Control'], 'no-cache');
});
test('direct allowed page succeeds', async () => {
  const f = fixture(allowed().slice(1));
  assert.equal((await check(f)).redirects, 0);
});
for (const target of ['https://evil.invalid/reverse-aging/', 'https://heger.earth.evil.invalid/reverse-aging/', 'https://www.heger.earth/cos/', 'https://user@www.heger.earth/reverse-aging/', 'https://www.heger.earth:8443/reverse-aging/', 'https://www.heger.earth/reverse-aging/?extra=1', 'https://www.heger.earth/reverse-aging/#fragment', 'ftp://heger.earth/reverse-aging/']) {
  test('reject unexpected redirect target: ' + target, async () => {
    const f = fixture([{ status: 301, location: target }]);
    await assert.rejects(check(f)); assert.equal(f.calls.length, 1);
  });
}
test('reject secure downgrade', async () => {
  const f = fixture([{ status: 301, location: destination }, { status: 302, location: source }]);
  await assert.rejects(check(f)); assert.equal(f.calls.length, 2);
});
test('loop stops before extra request', async () => {
  const f = fixture([{ status: 301, location: source }]);
  await assert.rejects(check(f)); assert.equal(f.calls.length, 1);
});
test('redirect needs location', async () => {
  await assert.rejects(check(fixture([{ status: 301 }])));
});
for (const status of [401, 404, 503]) {
  test('page HTTP failure ' + status, async () => { await assert.rejects(check(fixture([{ status }]))); });
}
for (const response of [{ status: 302, location: 'https://evil.invalid/' }, { status: 404 }, { status: 200, body: 'not JSON' }, { status: 200, body: 'null' }, { status: 200, body: JSON.stringify({ ...version, commit: 'b'.repeat(40) }) }, { status: 200, body: JSON.stringify({ ...version, commit: 'a'.repeat(7) }) }, { status: 200, body: JSON.stringify({ commit }) }, { status: 200, body: JSON.stringify({ ...version, deployed_at: 'tomorrow' }) }, { status: 200, body: JSON.stringify({ ...version, deployed_at: '2026-99-99T99:99:99Z' }) }]) {
  test('reject invalid live version: ' + JSON.stringify(response), async () => {
    const f = fixture([...allowed().slice(0, 2), response]);
    await assert.rejects(check(f)); assert.equal(f.calls.length, 3);
  });
}
test('invalid expected commit fails without network', async () => {
  const f = fixture([]);
  await assert.rejects(checkPublic({ expectedCommit: 'a'.repeat(7), fetchImpl: f.fetchImpl }));
  assert.equal(f.calls.length, 0);
});
test('network failure propagates', async () => {
  await assert.rejects(checkPublic({ expectedCommit: commit, fetchImpl: async () => { throw new Error('offline'); } }), /offline/);
});
