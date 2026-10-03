// Browserprüfung nach docs/handbuch.md, Kapitel 10. Läuft gegen einen gestarteten Server:
//   pnpm dev                      (in einem zweiten Terminal)
//   pnpm check:browser            (Standard: http://127.0.0.1:4311)
//   pnpm check:browser -- http://127.0.0.1:4312
// Braucht Chromium für Playwright: pnpm exec playwright-core install chromium
// Screenshots landen in outputs/browser/ (von Git ausgeschlossen).
import { mkdirSync, readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { join } from 'node:path';
import { chromium } from 'playwright-core';

const root = new URL('..', import.meta.url).pathname;
const base = (
  process.argv.slice(2).find((arg) => arg.startsWith('http')) ?? 'http://127.0.0.1:4311'
).replace(/\/$/, '');
const axeSource = readFileSync(
  createRequire(import.meta.url).resolve('axe-core/axe.min.js'),
  'utf8',
);
const shots = join(root, 'outputs/browser');
mkdirSync(shots, { recursive: true });

const routes = [
  ...readFileSync(join(root, 'web/src/app/app.routes.ts'), 'utf8').matchAll(/path: '([^'*]*)'/g),
]
  .map((match) => `/${match[1]}`)
  .concat('/gibt-es-nicht');
const viewports = [
  [1440, 1000],
  [1024, 768],
  [768, 1024],
  [390, 844],
  [320, 720],
];
const axeTags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'];
const failures = [];
const fail = (message) => {
  failures.push(message);
  console.log(`FEHLER ${message}`);
};

const browser = await chromium.launch();

async function openPage(path, width, height, options = {}) {
  const page = await browser.newPage({ viewport: { width, height }, ...options });
  const problems = [];
  page.on('request', (request) => {
    if (!request.url().startsWith(base) && !request.url().startsWith('data:')) {
      problems.push(`externe Anfrage ${request.url()}`);
    }
  });
  page.on('requestfailed', (request) => problems.push(`Anfrage fehlgeschlagen ${request.url()}`));
  page.on('pageerror', (error) => problems.push(`Laufzeitfehler ${error.message}`));
  page.on('console', (message) => {
    if (message.type() === 'error') problems.push(`Konsole ${message.text()}`);
  });
  await page.goto(base + path, { waitUntil: 'networkidle' });
  return { page, problems };
}

// 1. Seiten, Breiten, axe, Überlauf, Anfragen, Speicher
for (const path of routes) {
  for (const [width, height] of viewports) {
    const { page, problems } = await openPage(path, width, height);
    for (let y = 0; y < 12000; y += 500) {
      await page.evaluate((top) => window.scrollTo(0, top), y);
      await page.waitForTimeout(40);
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(300);
    await page.addScriptTag({ content: axeSource });
    const violations = await page.evaluate(
      async (tags) =>
        (await window.axe.run(document, { runOnly: tags })).violations.map(
          (v) => `${v.id} (${v.nodes.length})`,
        ),
      axeTags,
    );
    const overflow = await page.evaluate(
      () => document.documentElement.scrollWidth - window.innerWidth,
    );
    const storage = await page.evaluate(
      () => localStorage.length + sessionStorage.length + document.cookie.length,
    );
    const brokenImages = await page.evaluate(
      () =>
        [...document.images].filter((image) => image.complete && image.naturalWidth === 0).length,
    );
    const label = `${path} ${width}×${height}`;
    if (violations.length) fail(`${label}: axe ${violations.join(', ')}`);
    if (overflow > 0) fail(`${label}: waagerechter Bildlauf (${overflow} px)`);
    if (storage > 0) fail(`${label}: Speicher oder Cookies benutzt`);
    if (brokenImages > 0) fail(`${label}: ${brokenImages} Bilder nicht geladen`);
    for (const problem of problems) fail(`${label}: ${problem}`);
    await page.screenshot({
      path: join(shots, `${path.replace(/\W+/g, '_') || 'start'}-${width}.png`),
      fullPage: true,
    });
    await page.close();
    console.log(`geprüft ${label}`);
  }
}

// 2. 200 % Zoom: 1280 × 800 bei Seitenzoom 200 % entspricht 640 × 400 CSS-Pixeln.
for (const path of routes) {
  const { page } = await openPage(path, 640, 400, { deviceScaleFactor: 2 });
  const overflow = await page.evaluate(
    () => document.documentElement.scrollWidth - window.innerWidth,
  );
  if (overflow > 0) fail(`${path} 200 % Zoom: waagerechter Bildlauf (${overflow} px)`);
  await page.close();
}

// 3. Tastatur: Sprunglink auf einer Unterseite und sichtbarer Fokus
{
  const { page } = await openPage('/projekt', 1440, 1000);
  await page.keyboard.press('Tab');
  const skip = await page.evaluate(() => document.activeElement?.textContent?.trim());
  await page.keyboard.press('Enter');
  await page.waitForTimeout(300);
  const focus = await page.evaluate(() => document.activeElement?.id);
  if (
    skip !== 'Zum Inhalt springen' ||
    focus !== 'main-content' ||
    !page.url().endsWith('/projekt')
  ) {
    fail(`Sprunglink: erster Tab „${skip}“, Fokus „${focus}“, Adresse ${page.url()}`);
  }
  for (let i = 0; i < 25; i++) {
    await page.keyboard.press('Tab');
    const outline = await page.evaluate(() => {
      const element = document.activeElement;
      // Am Ende der Tab-Reihenfolge liegt der Fokus wieder auf body.
      if (!element || element === document.body) return 'ende';
      const style = getComputedStyle(element);
      return `${style.outlineStyle} ${style.outlineWidth}`;
    });
    if (outline === 'ende') break;
    if (!outline.startsWith('solid')) {
      fail(`Fokus ohne sichtbaren Rahmen nach ${i + 2} Tabs`);
      break;
    }
  }
  await page.close();
}

// 4. Galerie: drei automatische Wechsel, Stillstand bei reduzierter Bewegung
if (routes.includes('/')) {
  const { page } = await openPage('/', 1440, 1000);
  await page.mouse.move(5, 995);
  const seen = [];
  for (let second = 0; second <= 27; second++) {
    const counter = await page.textContent('.counter');
    if (seen.at(-1) !== counter) seen.push(counter);
    await page.waitForTimeout(1000);
  }
  if (seen.length < 4)
    fail(`Galerie: nur ${seen.length - 1} Wechsel in 27 s (${seen.join(' → ')})`);
  await page.close();

  const { page: reduced } = await openPage('/', 1440, 1000, { reducedMotion: 'reduce' });
  const before = await reduced.textContent('.counter');
  await reduced.waitForTimeout(10000);
  const after = await reduced.textContent('.counter');
  if (before !== after) fail('Galerie wechselt trotz reduzierter Bewegung');
  await reduced.close();
}

await browser.close();
if (failures.length) {
  console.error(`\nBrowserprüfung: ${failures.length} Fehler`);
  process.exit(1);
}
console.log(
  `\nBrowserprüfung bestanden: ${routes.length} Seiten, ${viewports.length} Breiten, 200 % Zoom, Tastatur, Galerie. Screenshots in outputs/browser/.`,
);
