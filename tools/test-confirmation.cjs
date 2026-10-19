// Isolated browser checks against Jekyll output. No Stripe/site request escapes
// the route fixtures, and no checkout or payment is created.
const fs = require('node:fs');
const assert = require('node:assert/strict');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const html = fs.readFileSync(process.argv[2] || '_site/booking/thanks/index.html', 'utf8');
const paid = { service: 'studio-family', livemode: true, paid: true,
  amountFormatted: '$494', balanceDue: 0, email: 'synthetic@example.invalid' };
const scenarios = [
  { name: 'Studio full payment', data: paid, heading: '$494 received. Thank you.', success: true },
  { name: 'Studio retainer preserves balance', data: { ...paid, balanceDue: 35000, balanceDueFormatted: '$350' }, heading: 'received. Thank you.', success: true, text: 'The balance of $350' },
  { name: 'Studio product payment', data: { ...paid, service: 'studio-product-day' }, heading: 'received. Thank you.', success: true },
  { name: 'Forensics payment', data: { ...paid, service: 'f-image-device' } },
  { name: 'Institute payment', data: { ...paid, service: 'ven-120' } },
  { name: 'Unknown Studio identifier', data: { ...paid, service: 'studio-not-a-service' } },
  { name: 'Quote-only wedding', data: { ...paid, service: 'studio-wedding' } },
  { name: 'Missing service', data: { ...paid, service: undefined } },
  { name: 'Null service', data: { ...paid, service: null } },
  { name: 'Array service', data: { ...paid, service: ['studio-family'] } },
  { name: 'Null response', data: null },
  { name: 'Test payment', data: { ...paid, livemode: false }, heading: 'Test payment only.' },
  { name: 'Missing live mode', data: { ...paid, livemode: undefined }, heading: 'Test payment only.' },
  { name: 'Unpaid session', data: { ...paid, paid: false }, heading: 'Payment is not confirmed yet.' },
  { name: 'String true is not paid', data: { ...paid, paid: 'true' }, heading: 'Payment is not confirmed yet.' },
  { name: 'Open unpaid checkout', data: { ...paid, paid: false, paymentStatus: 'unpaid', sessionStatus: 'open' }, heading: 'Payment is not confirmed yet.', text: 'This checkout has not completed.' },
  { name: 'Expired unpaid checkout', data: { ...paid, paid: false, paymentStatus: 'unpaid', sessionStatus: 'expired' }, heading: 'Payment is not confirmed yet.', text: 'This checkout has expired.' },
  { name: 'Completed checkout awaiting payment', data: { ...paid, paid: false, paymentStatus: 'unpaid', sessionStatus: 'complete' }, heading: 'Payment is not confirmed yet.', text: 'Payment processing may still be in progress.' },
  { name: 'String paid flag', data: { ...paid, paid: 'false' }, heading: 'Payment is not confirmed yet.' },
  { name: 'Numeric paid flag', data: { ...paid, paid: 1 }, heading: 'Payment is not confirmed yet.' },
  { name: 'Missing paid flag', data: { ...paid, paid: undefined }, heading: 'Payment is not confirmed yet.' },
  { name: 'Lookup HTTP failure', data: {}, status: 404 },
  { name: 'Lookup network failure', networkFailure: true },
  { name: 'Invalid JSON', raw: 'not json', text: 'The payment status could not be checked' },
  { name: 'Missing URL reference', noReference: true, fetches: 0 },
  { name: 'Provider text remains escaped', data: { ...paid, email: '<img src=x onerror="window.fixtureExecuted=true">', amountFormatted: '<b>$494</b>' }, heading: '<b>$494</b> received. Thank you.', success: true }
];
(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = []; let viewportCases = 0;
  try {
    for (const scenario of scenarios) {
      const context = await browser.newContext({ viewport: { width: 1440, height: 950 } });
      let calls = 0; const errors = [];
      await context.route('**/*', route => {
        const url = new URL(route.request().url());
        if (url.origin === 'https://studio.wirewalk.com' && url.pathname === '/booking/thanks/')
          return route.fulfill({ contentType: 'text/html', body: html });
        if (url.origin === 'https://wirewalk-orders.wirewalk-upload.workers.dev' && url.pathname === '/session') {
          calls++;
          if (scenario.networkFailure) return route.abort('failed');
          return route.fulfill({ status: scenario.status || 200, contentType: 'application/json', body: scenario.raw ?? JSON.stringify(scenario.data) });
        }
        return route.abort('blockedbyclient');
      });
      const page = await context.newPage(); page.on('pageerror', e => errors.push(e.message));
      let failure;
      try {
        await page.goto('https://studio.wirewalk.com/booking/thanks/' + (scenario.noReference ? '' : '?session=cs_test_synthetic_fixture'), { waitUntil: 'domcontentloaded' });
        await page.waitForFunction(() => !document.querySelector('#outcome').textContent.includes('Checking with'));
        const heading = await page.locator('#outcome h1').innerText();
        assert.ok(heading.includes(scenario.heading || 'This page cannot confirm a payment.'), heading);
        assert.equal(await page.locator('#next-steps').isVisible(), !!scenario.success);
        assert.equal(calls, scenario.fetches ?? 1);
        if (scenario.text) assert.ok((await page.locator('#outcome').innerText()).includes(scenario.text), scenario.text);
        if (scenario.data && ['open', 'expired'].includes(scenario.data.sessionStatus))
          assert.ok(!(await page.locator('#outcome').innerText()).includes('processing'), 'unfinished checkout must not suggest processing');
        assert.equal(await page.locator('#outcome img, #outcome b').count(), 0);
        assert.equal(await page.evaluate(() => !!window.fixtureExecuted), false);
        assert.deepEqual(errors, []);
        if (scenario === scenarios[0]) {
          for (const width of [1600,1440,1366,1280,1180,1080,1024,960,860,768,640,480,390]) {
            await page.setViewportSize({ width, height: 950 });
            const overflow = await page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
            assert.ok(overflow <= 1, `overflow ${overflow} at ${width}`); viewportCases++;
          }
        }
      } catch (error) { failure = error.message; }
      results.push({ name: scenario.name, passed: !failure, ...(failure ? { failure } : {}) });
      await context.close();
    }
  } finally { await browser.close(); }
  const summary = { cases: results.length, passed: results.filter(r => r.passed).length, failed: results.filter(r => !r.passed).length, viewportCases, isolated: true };
  console.log(JSON.stringify(summary));
  for (const r of results.filter(r => !r.passed)) console.log(JSON.stringify(r));
  if (process.env.VERIFY_RESULT_FILE) fs.writeFileSync(process.env.VERIFY_RESULT_FILE, JSON.stringify({ summary, results }, null, 2));
  if (summary.failed) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
