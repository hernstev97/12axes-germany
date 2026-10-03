// Real 200 % tab zoom on the public pages (Handbuch Kapitel 8 and 10).
// Uses chrome.tabs.setZoom through a local test extension, not CSS zoom or deviceScaleFactor.
// Runs against a served build, by default the production build:
//   node scripts/serve-dist.mjs web/dist/politikprofil/browser 4320
//   node scripts/check-public-zoom.mjs http://127.0.0.1:4320
// Checks per page and viewport: no horizontal overflow, axe without violations, every Tab
// stop visible with a solid 2 px outline inside the viewport, working skip link. Also checks
// that the production build does not contain the research route.
import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { chromium } from 'playwright-core';

const base = (process.argv[2] ?? 'http://127.0.0.1:4320').replace(/\/$/, '');
assert.match(base, /^http:\/\/(127\.0\.0\.1|localhost):\d+$/);
const output = resolve('outputs/public-zoom');
mkdirSync(output, { recursive: true });
const run = mkdtempSync(`${output}/run-`);
const extension = `${run}/extension`;
mkdirSync(extension);
writeFileSync(
  `${extension}/manifest.json`,
  JSON.stringify({
    manifest_version: 3,
    name: 'Local public tab zoom check',
    version: '1.0',
    permissions: ['tabs'],
    background: { service_worker: 'worker.js' },
  }),
);
writeFileSync(`${extension}/worker.js`, 'chrome.runtime.onInstalled.addListener(() => {});');
const axe = readFileSync(createRequire(import.meta.url).resolve('axe-core/axe.min.js'), 'utf8');
const routes = ['/', '/projekt', '/methodik', '/gibt-es-nicht'];
const conditions = [
  [1440, 1000],
  [1280, 900],
  [1024, 768],
  [768, 1024],
];
const report = { startedUtc: new Date().toISOString(), base, runs: [], failures: [] };
const context = await chromium.launchPersistentContext(`${run}/profile`, {
  channel: 'chromium',
  headless: true,
  viewport: { width: 1280, height: 900 },
  args: [`--disable-extensions-except=${extension}`, `--load-extension=${extension}`],
});
const page = context.pages()[0];
const screenshotSession = await context.newCDPSession(page);
const worker = context.serviceWorkers()[0] ?? (await context.waitForEvent('serviceworker'));
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
const external = [];
page.on('request', (request) => {
  if (!request.url().startsWith(base) && !request.url().startsWith('data:')) {
    external.push(request.url());
  }
});

async function zoom(factor) {
  const observed = await worker.evaluate(async (value) => {
    const [tab] = await chrome.tabs.query({ active: true });
    await chrome.tabs.setZoomSettings(tab.id, { mode: 'automatic', scope: 'per-tab' });
    await chrome.tabs.setZoom(tab.id, value);
    return chrome.tabs.getZoom(tab.id);
  }, factor);
  assert.equal(observed, factor);
  await page.waitForFunction((value) => devicePixelRatio === value, factor);
}

async function focusState() {
  return page.evaluate(() => {
    const element = document.activeElement;
    if (!element || element === document.body) return null;
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    return {
      label: (element.textContent || element.getAttribute('aria-label') || element.tagName)
        .trim()
        .slice(0, 60),
      visible: element.matches(':focus-visible'),
      outline: `${style.outlineStyle} ${style.outlineWidth}`,
      inViewport:
        rect.right > 0 && rect.left < innerWidth && rect.bottom > 0 && rect.top < innerHeight,
    };
  });
}

try {
  for (const [width, height] of conditions) {
    for (const path of routes) {
      const record = { path, width, height, tabStops: 0, maxOverflow: 0 };
      report.runs.push(record);
      await zoom(1);
      await page.setViewportSize({ width, height });
      await page.goto(base + path, { waitUntil: 'networkidle' });
      await zoom(2);
      const layout = await page.evaluate(() => ({
        innerWidth,
        clientWidth: document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
        cssZoom: getComputedStyle(document.documentElement).zoom,
        visualScale: visualViewport.scale,
      }));
      assert.equal(layout.innerWidth, width / 2, `${path} ${width}: CSS width`);
      assert.equal(layout.cssZoom, '1');
      assert.equal(layout.visualScale, 1);
      // Scroll through the whole page to check lazy content and overflow everywhere.
      const total = await page.evaluate(() => document.documentElement.scrollHeight);
      for (let y = 0; y <= total; y += 400) {
        await page.evaluate((top) => window.scrollTo(0, top), y);
        const overflow = await page.evaluate(
          () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
        );
        record.maxOverflow = Math.max(record.maxOverflow, overflow);
      }
      assert.ok(record.maxOverflow <= 1, `${path} ${width}: overflow ${record.maxOverflow}`);
      await page.evaluate(() => window.scrollTo(0, 0));
      if (path === '/methodik' || path === '/') {
        // Native viewport capture; Playwright's clip calculation ignores the tab zoom.
        const shot = await screenshotSession.send('Page.captureScreenshot', {
          format: 'png',
          fromSurface: false,
          captureBeyondViewport: false,
        });
        writeFileSync(
          `${run}/${path.replace(/\W+/g, '_') || 'start'}-${width}.png`,
          Buffer.from(shot.data, 'base64'),
        );
      }
      await page.addScriptTag({ content: axe });
      const violations = await page.evaluate(async () =>
        (
          await window.axe.run(document, {
            runOnly: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'],
          })
        ).violations.map((v) => `${v.id} (${v.nodes.length})`),
      );
      assert.deepEqual(violations, [], `${path} ${width}: axe`);
      await page.keyboard.press('Tab');
      assert.equal((await focusState())?.label, 'Zum Inhalt springen', `${path}: skip link`);
      await page.keyboard.press('Enter');
      await page.waitForFunction(() => document.activeElement?.id === 'main-content');
      for (let i = 0; i < 200; i++) {
        await page.keyboard.press('Tab');
        const state = await focusState();
        if (!state) break;
        assert.ok(
          state.visible && state.inViewport && state.outline === 'solid 2px',
          `${path} ${width}: Tab ${i + 1} ${JSON.stringify(state)}`,
        );
        record.tabStops++;
      }
      console.log(`${path} ${width}×${height} bei 200 %: ${record.tabStops} Tab-Stopps PASS`);
    }
  }
  // The research route must not exist in the production build.
  await zoom(1);
  await page.goto(`${base}/forschungsentwurf`, { waitUntil: 'networkidle' });
  const heading = await page.textContent('h1');
  report.researchRouteHeading = heading?.trim();
  assert.ok(heading?.includes('nicht gefunden'), 'research route present in this build');
  assert.equal(await page.locator('[data-question-id]').count(), 0);
  assert.deepEqual(errors, [], 'page errors');
  assert.deepEqual(external, [], 'external requests');
} catch (error) {
  report.failures.push(error.stack);
  process.exitCode = 1;
} finally {
  report.finishedUtc = new Date().toISOString();
  report.status = report.failures.length ? 'FAIL' : 'PASS';
  writeFileSync(`${run}/report.json`, JSON.stringify(report, null, 2) + '\n');
  console.log(
    JSON.stringify({
      status: report.status,
      report: `${run}/report.json`,
      failures: report.failures,
    }),
  );
  await context.close();
}
