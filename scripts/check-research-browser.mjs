// Local research UI only. Requires the existing Playwright Chromium and pnpm dev:research.
// Real tab zoom uses chrome.tabs.setZoom/getZoom, not CSS zoom or deviceScaleFactor.
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
import { mkdirSync, mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { chromium } from 'playwright-core';

const base = process.argv[2] ?? 'http://127.0.0.1:4314';
assert.match(base, /^http:\/\/(127\.0\.0\.1|localhost):\d+$/);
const output = resolve('outputs/research-browser');
mkdirSync(output, { recursive: true });
const run = mkdtempSync(`${output}/focus-zoom-`);
const extension = `${run}/extension`;
mkdirSync(extension);
writeFileSync(
  `${extension}/manifest.json`,
  JSON.stringify({
    manifest_version: 3,
    name: 'Local research tab zoom check',
    version: '1.0',
    permissions: ['tabs'],
    background: { service_worker: 'worker.js' },
  }),
);
writeFileSync(`${extension}/worker.js`, 'chrome.runtime.onInstalled.addListener(() => {});');
const axe = readFileSync(createRequire(import.meta.url).resolve('axe-core/axe.min.js'), 'utf8');
const report = {
  startedUtc: new Date().toISOString(),
  command: `node scripts/check-research-browser.mjs ${base}`,
  scriptSha256: createHash('sha256')
    .update(readFileSync(new URL(import.meta.url)))
    .digest('hex'),
  browser: null,
  zoomApi: 'chrome.tabs.setZoom/getZoom; automatic mode, per-tab scope',
  zoomDocumentation:
    'https://developer.chrome.com/docs/extensions/reference/api/tabs#method-setZoom',
  syntheticDemonstrationOnly: true,
  realPeople: 0,
  runs: [],
  failures: [],
};
const context = await chromium.launchPersistentContext(`${run}/profile`, {
  channel: 'chromium',
  headless: true,
  viewport: { width: 1280, height: 900 },
  reducedMotion: 'reduce',
  args: [`--disable-extensions-except=${extension}`, `--load-extension=${extension}`],
});
const page = context.pages()[0];
const screenshotSession = await context.newCDPSession(page);
const worker = context.serviceWorkers()[0] ?? (await context.waitForEvent('serviceworker'));
report.browser = context.browser().version();
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
// Privacy: after the page has loaded, no request and no WebSocket frame may leave the page.
let loaded = false;
const lateRequests = [];
const sentFrames = [];
page.on('request', (request) => {
  if (loaded) lateRequests.push(`${request.method()} ${request.url()}`);
});
page.on('websocket', (socket) =>
  socket.on('framesent', () => {
    if (loaded) sentFrames.push(socket.url());
  }),
);

async function stored() {
  const inPage = await page.evaluate(async () => ({
    localStorage: localStorage.length,
    sessionStorage: sessionStorage.length,
    cookie: document.cookie.length,
    indexedDB: (await indexedDB.databases()).length,
    caches: (await caches.keys()).length,
    serviceWorkers: (await navigator.serviceWorker.getRegistrations()).length,
    path: location.pathname + location.search + location.hash,
  }));
  return { ...inPage, contextCookies: (await context.cookies()).length };
}

async function zoom(factor) {
  const observed = await worker.evaluate(async (value) => {
    const [tab] = await chrome.tabs.query({ active: true });
    await chrome.tabs.setZoomSettings(tab.id, { mode: 'automatic', scope: 'per-tab' });
    await chrome.tabs.setZoom(tab.id, value);
    return {
      factor: await chrome.tabs.getZoom(tab.id),
      settings: await chrome.tabs.getZoomSettings(tab.id),
    };
  }, factor);
  assert.equal(observed.factor, factor);
  await page.waitForFunction((value) => devicePixelRatio === value, factor);
  return observed;
}

async function layout(label, record) {
  const value = await page.evaluate(() => ({
    width: innerWidth,
    height: innerHeight,
    clientWidth: document.documentElement.clientWidth,
    scrollWidth: document.documentElement.scrollWidth,
    dpr: devicePixelRatio,
    visualScale: visualViewport.scale,
    cssZoom: getComputedStyle(document.documentElement).zoom,
    heading: document.querySelector('#draft-question-title')?.textContent.trim(),
  }));
  assert.equal(value.visualScale, 1, `${label}: no pinch zoom`);
  assert.equal(value.cssZoom, '1', `${label}: no CSS zoom`);
  assert.ok(
    value.scrollWidth <= value.clientWidth + 1,
    `${label}: horizontal overflow ${JSON.stringify(value)}`,
  );
  record.layouts++;
  record.maxOverflow = Math.max(record.maxOverflow, value.scrollWidth - value.clientWidth);
  return value;
}

async function focus(record, label, sample = true) {
  const value = await page.evaluate(() => {
    const element = document.activeElement;
    const style = getComputedStyle(element);
    const rect = element.getBoundingClientRect();
    let background = element.parentElement;
    while (background && getComputedStyle(background).backgroundColor === 'rgba(0, 0, 0, 0)') {
      background = background.parentElement;
    }
    const surroundingColor = background
      ? getComputedStyle(background).backgroundColor
      : 'rgb(255, 255, 255)';
    const components = (color) => color.match(/[\d.]+/g).map(Number);
    const outline = components(style.outlineColor);
    const luminance = (channels) =>
      channels
        .slice(0, 3)
        .map((channel) => {
          const value = channel / 255;
          return value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4;
        })
        .reduce((sum, value, index) => sum + value * [0.2126, 0.7152, 0.0722][index], 0);
    const levels = [luminance(outline), luminance(components(surroundingColor))].sort(
      (a, b) => b - a,
    );
    return {
      documentFocused: document.hasFocus(),
      tag: element.tagName,
      id: element.id,
      type: element.type ?? null,
      label: (element.textContent || element.getAttribute('aria-label') || '').trim().slice(0, 100),
      visible: element.matches(':focus-visible'),
      outlineStyle: style.outlineStyle,
      outlineWidth: style.outlineWidth,
      outlineOffset: style.outlineOffset,
      outlineColor: style.outlineColor,
      outlineOpacity: outline[3] ?? 1,
      surroundingColor,
      outlineContrast: (levels[0] + 0.05) / (levels[1] + 0.05),
      inViewport:
        rect.right > 0 && rect.left < innerWidth && rect.bottom > 0 && rect.top < innerHeight,
    };
  });
  assert.ok(
    value.documentFocused && value.visible && value.inViewport,
    `${label}: ${JSON.stringify(value)}`,
  );
  assert.equal(value.outlineStyle, 'solid', label);
  assert.equal(value.outlineWidth, '2px', label);
  assert.equal(value.outlineOffset, '4px', label);
  assert.equal(value.outlineOpacity, 1, label);
  assert.ok(value.outlineContrast >= 3, `${label}: focus contrast ${value.outlineContrast}`);
  record.keyboardFocusChecks++;
  if (sample) record.focusSamples.push({ check: label, ...value });
}

async function tabTo(locator, record, label) {
  for (let count = 0; count < 180; count++) {
    await page.keyboard.press('Tab');
    if (await locator.evaluate((element) => element === document.activeElement)) {
      await focus(record, label);
      return;
    }
  }
  throw Error(`Tab target not reached: ${label}`);
}

async function shiftTabTo(locator, record, label) {
  for (let count = 0; count < 40; count++) {
    await page.keyboard.press('Shift+Tab');
    if (await locator.evaluate((element) => element === document.activeElement)) {
      await focus(record, label);
      return;
    }
  }
  throw Error(`Shift+Tab target not reached: ${label}`);
}

function headingFocused(text, prefix = false) {
  return page.waitForFunction(
    ([expected, startsWith]) => {
      const element = document.activeElement;
      const value = element?.id === 'draft-question-title' ? element.textContent.trim() : '';
      return startsWith ? value.startsWith(expected) : value === expected;
    },
    [text, prefix],
  );
}

async function audit(label, record) {
  if (!(await page.evaluate(() => !!window.axe))) await page.addScriptTag({ content: axe });
  const result = await page.evaluate(async () => {
    const value = await window.axe.run(document, {
      runOnly: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'],
    });
    return {
      violations: value.violations.map((entry) => entry.id),
      incomplete: value.incomplete.map((entry) => entry.id),
    };
  });
  record.axe.push({ label, ...result });
  assert.deepEqual(result.violations, [], label);
}

async function shot(label, record) {
  const path = `${run}/${record.label}-${label}.png`;
  // Surface capture produced blank images at real tab zoom in this Chromium.
  // Capture the native viewport without applying Playwright's CSS clip calculation.
  const value = await screenshotSession.send('Page.captureScreenshot', {
    format: 'png',
    fromSurface: false,
    captureBeyondViewport: false,
  });
  writeFileSync(path, Buffer.from(value.data, 'base64'));
  record.screenshots.push(path);
}

const conditions = [
  [1440, 1000, 1],
  [1024, 768, 1],
  [768, 1024, 1],
  [390, 844, 1],
  [320, 720, 1],
  [1280, 900, 2],
  [1440, 1000, 2],
  [1024, 768, 2],
  [768, 1024, 2],
];
try {
  for (const [width, height, factor] of conditions) {
    const record = {
      label: `${width}x${height}-zoom${factor}`,
      viewport: { width, height },
      zoom: null,
      layouts: 0,
      maxOverflow: 0,
      keyboardFocusChecks: 0,
      focusSamples: [],
      axe: [],
      screenshots: [],
    };
    report.runs.push(record);
    await zoom(1);
    await page.setViewportSize({ width, height });
    await page.goto(`${base}/forschungsentwurf`);
    await page.getByRole('heading', { name: 'Fragenentwurf', exact: true }).waitFor();
    await page.waitForLoadState('networkidle');
    loaded = true;
    record.zoom = await zoom(factor);
    record.measured = await layout('start', record);
    assert.equal(record.measured.width, width / factor);
    await audit('start', record);
    await tabTo(page.locator('.skip-link'), record, 'skip link');
    await page.keyboard.press('Enter');
    assert.equal(
      await page.locator('#main-content').evaluate((e) => e === document.activeElement),
      true,
    );
    // Start screen, then the introduction of the first question block on its own screen.
    await tabTo(
      page.getByRole('button', { name: 'Zu den Fragen', exact: true }),
      record,
      'start button',
    );
    await page.keyboard.press('Enter');
    await headingFocused('Einleitung zu Frage 1', true);
    assert.equal(await page.locator('input[name=draft-original-answer]').count(), 0);
    await layout('introduction 1', record);
    await audit('introduction 1', record);
    await shot('introduction', record);
    // The single-step checks below run with the automatic change switched off by keyboard.
    const autoAdvance = page.locator('#draft-auto-advance');
    assert.ok(await autoAdvance.isChecked(), 'auto-advance starts on');
    await tabTo(autoAdvance, record, 'auto-advance switch');
    await page.keyboard.press('Space');
    assert.equal(await autoAdvance.isChecked(), false, 'auto-advance switched off');
    await tabTo(
      page.getByRole('button', { name: 'Zu Frage 1', exact: true }),
      record,
      'question 1',
    );
    await page.keyboard.press('Enter');
    const firstHeading = await (
      await page.waitForFunction(() => {
        const element = document.activeElement;
        const text = element?.id === 'draft-question-title' ? element.textContent.trim() : '';
        return /^Frage 1 von \d+$/.test(text) ? text : null;
      })
    ).jsonValue();
    const total = Number(firstHeading.match(/^Frage 1 von (\d+)$/)[1]);
    await layout('question 1', record);
    await tabTo(page.locator('input[name=draft-original-answer]').first(), record, 'first radio');
    await shot('question-radio', record);
    await page.keyboard.press('Space');
    const originalCode = await page
      .locator('input[name=draft-original-answer]:checked')
      .inputValue();
    await page.keyboard.press('ArrowDown');
    assert.notEqual(
      await page.locator('input[name=draft-original-answer]:checked').inputValue(),
      originalCode,
    );
    await page.keyboard.press('ArrowUp');
    assert.equal(
      await page.locator('input[name=draft-original-answer]:checked').inputValue(),
      originalCode,
    );
    await focus(record, 'radio arrow navigation');
    // The reset button appears after the skip controls once there is an answer.
    const reset = page.getByRole('button', { name: 'Auswahl zurücksetzen', exact: true });
    await tabTo(reset, record, 'reset button');
    await page.keyboard.press('Enter');
    await page.waitForFunction(() => document.activeElement.id === 'draft-question-title');
    assert.equal(await reset.count(), 0);
    assert.equal(await page.locator('input[name=draft-original-answer]:checked').count(), 0);
    // From the question heading, the switch for the automatic change comes before the answers.
    await page.keyboard.press('Tab');
    assert.equal(await autoAdvance.evaluate((e) => e === document.activeElement), true);
    await page.keyboard.press('Tab');
    assert.equal(
      await page
        .locator('input[name=draft-original-answer]')
        .first()
        .evaluate((e) => e === document.activeElement),
      true,
    );
    await focus(record, 'first radio after reset');
    await page.keyboard.press('Space');
    await tabTo(
      page.locator('app-policy-source-details summary').first(),
      record,
      'question sources',
    );
    await page.keyboard.press('Enter');
    const questionSources = page.locator('app-policy-source-details summary');
    assert.ok(await questionSources.first().evaluate((e) => e.parentElement.open));
    for (let source = 1; source < (await questionSources.count()); source++) {
      await tabTo(questionSources.nth(source), record, `nested question source ${source}`);
      await page.keyboard.press('Enter');
      assert.ok(await questionSources.nth(source).evaluate((e) => e.parentElement.open));
    }
    record.nestedQuestionSourcesOpened = (await questionSources.count()) - 1;
    await layout('question sources expanded', record);
    await audit('question sources expanded', record);
    await shot('question-sources', record);
    await tabTo(questionSources.first(), record, 'close question sources');
    await page.keyboard.press('Enter');
    assert.equal(await questionSources.first().evaluate((e) => e.parentElement.open), false);
    // Back to the question controls without changing the answer.
    await shiftTabTo(page.locator('#draft-skip-reason'), record, 'back to skip reason');
    record.introductions = 1;
    for (let question = 1; question <= total; question++) {
      await page.waitForFunction(
        (n) => {
          const text = document.querySelector('#draft-question-title')?.textContent.trim() ?? '';
          return (
            text === `Frage ${n[0]} von ${n[1]}` || text.startsWith(`Einleitung zu Frage ${n[0]}`)
          );
        },
        [question, total],
      );
      if (question > 1) {
        const heading = (await page.locator('#draft-question-title').innerText()).trim();
        if (heading.startsWith('Einleitung')) {
          // Moving forward into a new block shows its original introduction first.
          await headingFocused(heading);
          record.introductions++;
          await layout(`introduction ${question}`, record);
          await tabTo(
            page.getByRole('button', { name: `Zu Frage ${question}`, exact: true }),
            record,
            `introduction to question ${question}`,
          );
          await page.keyboard.press('Enter');
        }
        await headingFocused(`Frage ${question} von ${total}`);
        assert.ok(
          await page.locator('#draft-question-title').evaluate((e) => {
            const rect = e.getBoundingClientRect();
            return rect.top >= 0 && rect.bottom <= innerHeight;
          }),
          `question ${question}: heading focus/scroll`,
        );
      }
      await layout(`question ${question}`, record);
      if (question === 2) {
        await tabTo(
          page.locator('input[name=draft-original-answer]').first(),
          record,
          'second radio',
        );
        await page.keyboard.press('Space');
        await tabTo(
          page.getByRole('button', { name: 'Vorherige Frage', exact: true }),
          record,
          'previous question',
        );
        await page.keyboard.press('Enter');
        await page.waitForFunction(
          (n) =>
            document.activeElement.id === 'draft-question-title' &&
            document.activeElement.textContent.trim() === `Frage 1 von ${n}`,
          total,
        );
        await tabTo(
          page.getByRole('button', { name: 'Nächste Frage', exact: true }),
          record,
          'return to second question',
        );
        await page.keyboard.press('Enter');
        await page.waitForFunction(
          (n) =>
            document.activeElement.id === 'draft-question-title' &&
            document.activeElement.textContent.trim() === `Frage 2 von ${n}`,
          total,
        );
      }
      if (question === 3) {
        await tabTo(page.locator('#draft-skip-reason'), record, 'skip reason');
        await page.keyboard.press('ArrowDown');
        await tabTo(
          page.getByRole('button', { name: 'Frage überspringen', exact: true }),
          record,
          'skip button',
        );
      } else {
        const next = page.getByRole('button', {
          name: question === total ? 'Zum Ergebnisentwurf' : 'Nächste Frage',
          exact: true,
        });
        // On the last question the card control comes before the view link of the same name.
        const target = question === total ? next.first() : next;
        await tabTo(target, record, `next from question ${question}`);
      }
      await page.keyboard.press('Enter');
    }
    record.questionsTraversed = total;
    record.questionFocusTransitions = total - 1;
    await page.getByRole('heading', { name: 'Ergebnisentwurf', exact: true }).waitFor();
    await page.waitForFunction(
      () =>
        document.activeElement.tagName === 'H1' &&
        document.activeElement.textContent.trim() === 'Ergebnisentwurf',
    );
    assert.equal(await page.locator('.result-item').count(), total);
    record.resultItems = total;
    await layout('results', record);
    await audit('results', record);
    await tabTo(page.locator('#draft-group-study'), record, 'group study');
    await page.keyboard.press('ArrowDown');
    await page.waitForFunction(() => !document.querySelector('#draft-vote-group').disabled);
    await tabTo(page.locator('#draft-vote-group'), record, 'historical vote group');
    await page.keyboard.press('ArrowDown');
    await page.waitForFunction(() => document.querySelector('#draft-vote-group').value !== '');
    record.selectedStudy = await page.locator('#draft-group-study').inputValue();
    record.selectedGroup = await page.locator('#draft-vote-group').inputValue();
    const selectedGroupLabel = (
      await page.locator('#draft-vote-group option:checked').innerText()
    ).trim();
    await page.waitForFunction(
      (label) =>
        [...document.querySelectorAll('p.meta')].some((e) =>
          e.textContent.trim().startsWith(`Vergleichsgruppe: ${label}.`),
        ),
      selectedGroupLabel,
    );
    await page.locator('.group-reference').first().waitFor();
    assert.ok(
      (await page.locator('.group-reference').first().innerText()).includes(record.selectedStudy),
    );
    assert.ok(
      (await page.locator('.group-reference').first().innerText()).includes(selectedGroupLabel),
    );
    await tabTo(page.locator('.group-sources > summary'), record, 'group sources');
    await shot('group-sources-focus', record);
    await page.keyboard.press('Enter');
    assert.ok(await page.locator('.group-sources').evaluate((e) => e.open));
    await layout('group sources expanded', record);
    await audit('group sources expanded', record);
    await shot('group-sources-expanded', record);
    await page.keyboard.press('Enter');
    assert.equal(await page.locator('.group-sources').evaluate((e) => e.open), false);
    await tabTo(
      page.locator('.result-item app-policy-source-details summary').first(),
      record,
      'result sources',
    );
    await page.keyboard.press('Enter');
    assert.ok(
      await page
        .locator('.result-item app-policy-source-details summary')
        .first()
        .evaluate((e) => e.parentElement.open),
    );
    await layout('result sources expanded', record);
    await audit('result sources expanded', record);
    await shot('result-sources-focus', record);
    await page.keyboard.press('Enter');
    await tabTo(page.locator('.result-item button').first(), record, 'edit result');
    await page.keyboard.press('Enter');
    await page.waitForFunction(() => document.activeElement.id === 'draft-question-title');
    await tabTo(
      page.locator('input[name=draft-original-answer]:checked'),
      record,
      'retained answer after edit',
    );
    await tabTo(
      page.getByRole('button', { name: 'Zur Fragenübersicht', exact: true }),
      record,
      'overview button',
    );
    await page.keyboard.press('Enter');
    await page.getByRole('heading', { name: 'Fragenübersicht', exact: true }).waitFor();
    await layout('overview', record);
    await audit('overview', record);
    // Pointer jump verifies the distant edit's focus/scroll target, independently of Tab checks.
    await page.locator('.overview-list li:last-child button').click();
    await page.waitForFunction(
      (n) =>
        document.activeElement.id === 'draft-question-title' &&
        document.activeElement.textContent.trim() === `Frage ${n} von ${n}`,
      total,
    );
    assert.ok(
      await page.locator('#draft-question-title').evaluate((e) => {
        const r = e.getBoundingClientRect();
        return r.top >= 0 && r.bottom <= innerHeight;
      }),
    );
    await page.keyboard.press('Tab');
    await focus(record, 'first control after distant edit');
    await shot('last-question-focus', record);
    record.privacy = {
      requestsAfterLoad: [...lateRequests],
      webSocketFramesSent: sentFrames.length,
      storage: await stored(),
    };
    assert.deepEqual(lateRequests, [], `${record.label}: requests after load`);
    assert.equal(sentFrames.length, 0, `${record.label}: WebSocket frames sent`);
    assert.deepEqual(
      record.privacy.storage,
      {
        localStorage: 0,
        sessionStorage: 0,
        cookie: 0,
        indexedDB: 0,
        caches: 0,
        serviceWorkers: 0,
        path: '/forschungsentwurf',
        contextCookies: 0,
      },
      `${record.label}: nothing stored`,
    );
    loaded = false;
    // Automatic change on a fresh page: arrow keys only select, Space and a click confirm.
    await page.goto(`${base}/forschungsentwurf`);
    await page.getByRole('heading', { name: 'Fragenentwurf', exact: true }).waitFor();
    await tabTo(
      page.getByRole('button', { name: 'Zu den Fragen', exact: true }),
      record,
      'auto: start button',
    );
    await page.keyboard.press('Enter');
    await headingFocused('Einleitung zu Frage 1', true);
    assert.ok(await page.locator('#draft-auto-advance').isChecked(), 'auto-advance on after load');
    await tabTo(
      page.getByRole('button', { name: 'Zu Frage 1', exact: true }),
      record,
      'auto: question 1',
    );
    await page.keyboard.press('Enter');
    await headingFocused(`Frage 1 von ${total}`);
    await tabTo(page.locator('input[name=draft-original-answer]').first(), record, 'auto radio');
    await page.keyboard.press('ArrowDown');
    await page.waitForTimeout(800);
    assert.equal(
      (await page.locator('#draft-question-title').innerText()).trim(),
      `Frage 1 von ${total}`,
      'arrow keys do not advance',
    );
    await page.keyboard.press('Space');
    await page.waitForFunction(
      (n) =>
        document.activeElement.id === 'draft-question-title' &&
        document.activeElement.textContent.trim() === `Frage 2 von ${n}`,
      total,
    );
    await page.locator('label.answer-option').first().click();
    await page.waitForFunction(
      (n) =>
        document.activeElement.id === 'draft-question-title' &&
        document.activeElement.textContent.trim() === `Frage 3 von ${n}`,
      total,
    );
    await layout('after automatic change', record);
    await audit('after automatic change', record);
    await shot('after-automatic-change', record);
    // After the last question of a block the next introduction follows.
    await page.locator('label.answer-option').first().click();
    await headingFocused(`Frage 4 von ${total}`);
    await page.locator('label.answer-option').first().click();
    await headingFocused('Einleitung zu Frage 5', true);
    record.autoAdvance =
      'arrow keys select without change; Space and click advance; block end leads to introduction';
    console.log(
      `${record.label}: start, ${record.introductions} introductions, ${total} questions, results, overview, ${record.keyboardFocusChecks} focus checks, ${record.axe.length} axe checks, no request or storage after load PASS`,
    );
  }
  assert.deepEqual(errors, [], 'page errors');
} catch (error) {
  report.failures.push(error.stack);
  process.exitCode = 1;
  await screenshotSession
    .send('Page.captureScreenshot', {
      format: 'png',
      fromSurface: false,
      captureBeyondViewport: false,
    })
    .then((value) => writeFileSync(`${run}/failure.png`, Buffer.from(value.data, 'base64')))
    .catch(() => {});
} finally {
  report.finishedUtc = new Date().toISOString();
  report.status = report.failures.length ? 'FAIL' : 'PASS';
  report.pageErrors = errors;
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
