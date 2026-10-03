// Research draft in Chromium, Firefox and WebKit (local research build only).
//   cd web && npx ng build --configuration research --output-path ../outputs/claude/research-build
//   node scripts/serve-dist.mjs outputs/claude/research-build/browser 4321
//   node scripts/check-research-engines.mjs http://127.0.0.1:4321
// Full flow through every question with answer changes, reset, skipping with a reason,
// going back, the result view, historical references with intervals, group comparisons,
// the overview and a distant edit. Checks focus after view changes, overflow, axe and
// privacy (no request after load, nothing stored). Synthetic technical answers only.
// Engine emulation is not a physical device and not a screen reader test.
import assert from 'node:assert/strict';
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { chromium, firefox, webkit } from 'playwright-core';

const base = (process.argv[2] ?? 'http://127.0.0.1:4321').replace(/\/$/, '');
assert.match(base, /^http:\/\/(127\.0\.0\.1|localhost):\d+$/);
const output = resolve('outputs/research-engines');
mkdirSync(output, { recursive: true });
const run = mkdtempSync(`${output}/run-`);
const axe = readFileSync(createRequire(import.meta.url).resolve('axe-core/axe.min.js'), 'utf8');
const engines = { chromium, firefox, webkit };
const viewports = [
  { label: 'desktop', viewport: { width: 1440, height: 1000 } },
  { label: 'smartphone', viewport: { width: 390, height: 844 }, mobile: true },
];
const report = { startedUtc: new Date().toISOString(), base, runs: [], failures: [] };

async function check(engineName, setting) {
  const browserType = engines[engineName];
  // Optional path to an installed build of another revision, e.g. FIREFOX_EXECUTABLE.
  const executablePath = process.env[`${engineName.toUpperCase()}_EXECUTABLE`];
  let browser;
  try {
    browser = await browserType.launch({ headless: true, executablePath });
  } catch (error) {
    report.runs.push({
      engine: engineName,
      setting: setting.label,
      status: 'NICHT_DURCHFÜHRBAR',
      reason: error.message.split('\n').slice(0, 4).join(' '),
    });
    console.log(`${engineName} ${setting.label}: NICHT_DURCHFÜHRBAR (Browser startet nicht)`);
    return;
  }
  const options = { viewport: setting.viewport, reducedMotion: 'reduce' };
  if (setting.mobile && engineName !== 'firefox') {
    Object.assign(options, { isMobile: true, hasTouch: true, deviceScaleFactor: 3 });
  }
  const context = await browser.newContext(options);
  // Record every write to client-side storage from the first script on, so that a value
  // written and removed before the end does not go unnoticed.
  await context.addInitScript(() => {
    const calls = [];
    const unavailable = [];
    window.__storageCalls = calls;
    window.__storageUnavailable = unavailable;
    const wrap = (prototype, name, label) => {
      const original = prototype?.[name];
      if (typeof original !== 'function') {
        unavailable.push(label);
        return;
      }
      prototype[name] = function (...args) {
        calls.push(label);
        return original.apply(this, args);
      };
    };
    wrap(window.Storage?.prototype, 'setItem', 'Storage.setItem');
    wrap(window.IDBFactory?.prototype, 'open', 'indexedDB.open');
    wrap(window.CacheStorage?.prototype, 'open', 'caches.open');
    wrap(window.ServiceWorkerContainer?.prototype, 'register', 'serviceWorker.register');
    const cookie = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie');
    if (cookie?.set) {
      Object.defineProperty(Document.prototype, 'cookie', {
        configurable: true,
        get: cookie.get,
        set(value) {
          calls.push('document.cookie');
          return cookie.set.call(this, value);
        },
      });
    } else unavailable.push('document.cookie');
  });
  const page = await context.newPage();
  const record = {
    engine: engineName,
    version: browser.version(),
    setting: setting.label,
    steps: [],
  };
  report.runs.push(record);
  const errors = [];
  const late = [];
  let loaded = false;
  page.on('pageerror', (error) => errors.push(error.message));
  page.on('request', (request) => {
    if (loaded) late.push(`${request.method()} ${request.url()}`);
  });
  page.on('websocket', (socket) => socket.on('framesent', () => late.push(`ws ${socket.url()}`)));
  const step = (text) => record.steps.push(text);
  record.storageChecks = [];

  async function storageCheck(label) {
    const state = await page.evaluate(async () => ({
      calls: [...window.__storageCalls],
      unavailable: [...window.__storageUnavailable],
      local: localStorage.length,
      session: sessionStorage.length,
      cookie: document.cookie.length,
      idb: indexedDB.databases ? (await indexedDB.databases()).length : 'NICHT_GEPRÜFT',
      caches: typeof caches === 'undefined' ? 'NICHT_GEPRÜFT' : (await caches.keys()).length,
      sw: navigator.serviceWorker
        ? (await navigator.serviceWorker.getRegistrations()).length
        : 'NICHT_GEPRÜFT',
      path: location.pathname + location.search + location.hash,
    }));
    record.storageChecks.push({ label, ...state });
    assert.deepEqual(state.calls, [], `${label}: storage writes ${state.calls.join(', ')}`);
    for (const key of ['local', 'session', 'cookie', 'idb', 'caches', 'sw']) {
      assert.ok(
        state[key] === 0 || state[key] === 'NICHT_GEPRÜFT',
        `${label}: ${key} ${state[key]}`,
      );
    }
    assert.equal(state.path, '/forschungsentwurf', `${label}: URL`);
    assert.equal((await context.cookies()).length, 0, `${label}: context cookies`);
  }

  async function overflow(label) {
    const value = await page.evaluate(
      () => document.documentElement.scrollWidth - document.documentElement.clientWidth,
    );
    assert.ok(value <= 1, `${engineName} ${setting.label} ${label}: overflow ${value}`);
  }
  async function axeCheck(label) {
    await page.addScriptTag({ content: axe });
    const violations = await page.evaluate(async () =>
      (
        await window.axe.run(document, {
          runOnly: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'],
        })
      ).violations.map((v) => `${v.id} (${v.nodes.length})`),
    );
    assert.deepEqual(violations, [], `${engineName} ${setting.label} ${label}: axe`);
  }
  async function headingFocused(text) {
    await page.waitForFunction(
      (expected) => document.activeElement?.textContent?.trim() === expected,
      text,
    );
  }
  const checked = () => page.locator('input[name=draft-original-answer]:checked');
  const options_ = () => page.locator('label.answer-option');
  const button = (name) => page.getByRole('button', { name, exact: true });

  try {
    await page.goto(`${base}/forschungsentwurf`, { waitUntil: 'networkidle' });
    await page.getByRole('heading', { name: 'Fragenentwurf', exact: true }).waitFor();
    loaded = true;
    const total = Number(
      (await page.locator('#draft-question-title').innerText()).match(/von (\d+)$/)[1],
    );
    record.questions = total;
    await overflow('question 1');
    await storageCheck('question 1');
    await axeCheck('question 1');

    // Keyboard: the first radio gets a visible focus ring.
    await page.locator('#draft-question-title').focus();
    for (let i = 0; i < 40; i++) {
      await page.keyboard.press('Tab');
      if (await page.evaluate(() => document.activeElement?.name === 'draft-original-answer')) {
        break;
      }
    }
    const ring = await page.evaluate(() => {
      const element = document.activeElement;
      const style = getComputedStyle(element.closest('label') ?? element);
      const own = getComputedStyle(element);
      return {
        name: element.name,
        outline: `${own.outlineStyle} ${own.outlineWidth}`,
        labelOutline: `${style.outlineStyle} ${style.outlineWidth}`,
        focusVisible: element.matches(':focus-visible'),
      };
    });
    record.radioFocus = ring;
    assert.equal(ring.name, 'draft-original-answer', 'Tab reaches a radio');
    assert.ok(ring.focusVisible, 'radio focus visible');
    assert.equal(ring.outline, 'solid 2px', 'radio focus outline');
    step(`radio focus ${JSON.stringify(ring)}`);

    let skipped = 0;
    let answered = 0;
    for (let question = 1; question <= total; question++) {
      const count = await options_().count();
      if (question === 1) {
        await options_().nth(0).click();
        await options_().nth(1).click();
        assert.equal(await checked().count(), 1);
        assert.equal(
          await checked().inputValue(),
          await options_().nth(1).locator('input').inputValue(),
          'answer change',
        );
        step('answer changed on question 1');
        answered++;
      } else if (question === 2) {
        await page.selectOption('#draft-skip-reason', 'dont-know');
        await button('Diese Frage überspringen').click();
        skipped++;
        await headingFocused(`Frage 3 von ${total}`);
        step('question 2 skipped with reason');
        continue;
      } else if (question === 3) {
        await options_()
          .nth(count - 1)
          .click();
        await button('Auswahl zurücksetzen').click();
        await page.waitForFunction(() => document.activeElement?.id === 'draft-question-title');
        // The native radio is aligned after the next render; allow that render, nothing more.
        await page
          .waitForFunction(
            () =>
              document.querySelectorAll('input[name=draft-original-answer]:checked').length === 0,
            null,
            { timeout: 3000 },
          )
          .catch(() => {
            throw new Error('reset: a radio stays checked after the next render');
          });
        await options_().nth(0).click();
        answered++;
        step('question 3 reset and answered again');
      } else if (question === 5) {
        await options_()
          .nth(question % count)
          .click();
        answered++;
        await button('Zur vorherigen Frage').click();
        await headingFocused(`Frage 4 von ${total}`);
        assert.equal(await checked().count(), 1, 'answer kept after going back');
        await button('Zur nächsten Frage').click();
        await headingFocused(`Frage 5 von ${total}`);
        assert.equal(await checked().count(), 1, 'answer kept after returning');
        step('back and forward keeps answers');
      } else {
        await options_()
          .nth(question % count)
          .click();
        answered++;
      }
      const next =
        question === total ? button('Zum Ergebnisentwurf').last() : button('Zur nächsten Frage');
      await next.click();
      if (question < total) {
        await headingFocused(`Frage ${question + 1} von ${total}`);
        await page.waitForFunction(
          () => document.querySelectorAll('input[name=draft-original-answer]:checked').length === 0,
          null,
          { timeout: 3000 },
        );
      }
      if (question === Math.floor(total / 2)) {
        await overflow(`question ${question}`);
        await storageCheck(`question ${question}`);
      }
    }
    await page.getByRole('heading', { name: 'Ergebnisentwurf', exact: true }).waitFor();
    await headingFocused('Ergebnisentwurf');
    const counts = (await page.locator('[aria-live=polite]').first().innerText()).replace(
      /\s+/g,
      ' ',
    );
    assert.ok(
      counts.includes(`${answered} beantwortet, ${skipped} übersprungen, 0 unberührt`),
      `counts ${counts}`,
    );
    assert.equal(await page.locator('.result-item').count(), total);
    const withReference = await page.locator('.result-item .historical-reference').count();
    const intervals = await page.locator('.result-item .historical-reference .interval').count();
    const ownMarks = await page
      .locator('.result-item .historical-reference .own-answer-label')
      .count();
    const withheld = await page.locator('.result-item .reference-withheld').count();
    record.results = { answered, skipped, withReference, intervals, ownMarks, withheld };
    assert.ok(withReference > 50 && intervals > withReference, 'references with intervals');
    const answeredWithReference = await page.evaluate(
      () =>
        [...document.querySelectorAll('.result-item')].filter(
          (item) =>
            item.querySelector('.historical-reference') &&
            item.querySelector('.state')?.textContent.trim() === 'Beantwortet',
        ).length,
    );
    record.results.answeredWithReference = answeredWithReference;
    assert.equal(ownMarks, answeredWithReference, 'own answer marked once per answered reference');
    await overflow('results');
    await axeCheck('results');

    await page.selectOption('#draft-group-study', 'ESS9e03_3');
    await page.selectOption('#draft-vote-group', 'ESS9e03_3:second_vote:1');
    await page.locator('.group-reference').first().waitFor();
    const groupRefs = await page.locator('.group-reference').count();
    const groupIntervals = await page.locator('.group-reference .interval').count();
    assert.ok(groupRefs > 0 && groupIntervals > 0, 'group comparison with intervals');
    assert.ok(await page.locator('.group-coverage').isVisible(), 'coverage note');
    await page.selectOption('#draft-group-study', 'ESS8e02_3');
    const lastGroup = await page.locator('#draft-vote-group option').last().getAttribute('value');
    await page.selectOption('#draft-vote-group', lastGroup);
    assert.ok(
      (await page.locator('#draft-vote-group option:checked').innerText()).includes(
        'Andere Partei (heterogener Rest)',
      ),
    );
    assert.ok(await page.locator('.group-other-limit').isVisible());
    record.groups = { groupRefs, groupIntervals };
    await overflow('groups');
    await axeCheck('groups');

    await storageCheck('results and groups');
    await button('Zur Fragenübersicht').first().click();
    await headingFocused('Fragenübersicht');
    await page.getByRole('heading', { name: 'Fragenübersicht', exact: true }).waitFor();
    await page.locator('.overview-list li:last-child button').click();
    await headingFocused(`Frage ${total} von ${total}`);
    assert.equal(await checked().count(), 1, 'distant edit keeps answer');
    step('overview edit to last question');

    assert.deepEqual(errors, [], 'page errors');
    assert.deepEqual(late, [], 'requests after load');
    await storageCheck('end');
    record.privacy = {
      notChecked: record.storageChecks.at(-1).unavailable.concat(
        Object.entries(record.storageChecks.at(-1))
          .filter(([, value]) => value === 'NICHT_GEPRÜFT')
          .map(([key]) => key),
      ),
    };
    await page.screenshot({ path: `${run}/${engineName}-${setting.label}-end.png` });
    record.status = 'PASS';
    console.log(`${engineName} ${record.version} ${setting.label}: ${total} Fragen PASS`);
  } catch (error) {
    record.status = 'FAIL';
    report.failures.push(`${engineName} ${setting.label}: ${error.stack}`);
    await page
      .screenshot({ path: `${run}/${engineName}-${setting.label}-failure.png` })
      .catch(() => {});
    console.log(`${engineName} ${setting.label}: FAIL ${error.message.split('\n')[0]}`);
  } finally {
    await browser.close();
  }
}

for (const engineName of Object.keys(engines)) {
  for (const setting of viewports) await check(engineName, setting);
}
report.finishedUtc = new Date().toISOString();
report.status = report.failures.length ? 'FAIL' : 'PASS';
writeFileSync(`${run}/report.json`, JSON.stringify(report, null, 2) + '\n');
console.log(JSON.stringify({ status: report.status, report: `${run}/report.json` }));
process.exitCode = report.failures.length ? 1 : 0;
