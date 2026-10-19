// Read-only identifier drift check. Pass a saved /catalog?practice=studio JSON
// response for offline review; without an argument only that public GET is used.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
(async () => {
  const html = fs.readFileSync(path.join(__dirname, '../booking-thanks.html'), 'utf8');
  const match = /var STUDIO_SKUS = (\[[\s\S]*?\]);/.exec(html);
  assert.ok(match, 'confirmation allowlist not found');
  const allowed = JSON.parse(match[1]);
  assert.equal(new Set(allowed).size, allowed.length, 'duplicate identifiers');
  assert.ok(allowed.every(s => typeof s === 'string' && s.startsWith('studio-')), 'invalid Studio identifiers');
  const source = process.argv[2];
  let catalog;
  if (source) catalog = JSON.parse(fs.readFileSync(source, 'utf8'));
  else {
    const res = await fetch('https://wirewalk-orders.wirewalk-upload.workers.dev/catalog?practice=studio',
      { signal: AbortSignal.timeout(15000), redirect: 'error' });
    assert.equal(res.status, 200, 'catalog GET did not return 200');
    catalog = await res.json();
  }
  assert.ok(Array.isArray(catalog.items) && catalog.items.length > 0, 'empty or invalid catalog');
  const payable = catalog.items.filter(i => i && i.practice === 'studio' && i.priceOnApplication !== true);
  assert.ok(payable.length > 0, 'no payable Studio entries');
  for (const item of payable) {
    assert.ok(Number.isSafeInteger(item.list) && item.list > 0, `invalid list fee: ${item.sku}`);
    assert.ok(allowed.includes(item.sku), `payable SKU missing from confirmation: ${item.sku}`);
  }
  for (const item of catalog.items)
    if (item && (item.practice !== 'studio' || item.priceOnApplication === true))
      assert.ok(!allowed.includes(item.sku), `foreign or quote-only SKU allowed: ${item.sku}`);
  // Historical identifiers absent from today's catalog may remain for old receipts.
  console.log(JSON.stringify({ payableStudio: payable.length, allowlisted: allowed.length,
    currentPayableMissing: 0, foreignOrQuotedAllowed: 0, source: source ? 'saved fixture' : 'public GET', readOnly: true }));
})().catch(error => { console.error(error.message); process.exitCode = 1; });
