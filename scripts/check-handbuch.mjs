// Prüft die mechanisch prüfbaren Regeln aus docs/handbuch.md. Läuft in `pnpm check`.
// Inhaltliche Regeln (Ton, Belege, Bildauswahl) ersetzt das Skript nicht.
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join, relative } from 'node:path';

const root = new URL('..', import.meta.url).pathname;
const src = join(root, 'web/src');
const artDir = join(root, 'web/public/art');
const problems = [];

function filesBelow(dir) {
  return readdirSync(dir).flatMap((name) => {
    const path = join(dir, name);
    return statSync(path).isDirectory() ? filesBelow(path) : [path];
  });
}

function report(file, message) {
  problems.push(`${relative(root, file)}: ${message}`);
}

const indexFile = join(src, 'index.html');
const stylesFile = join(src, 'styles.scss');
const artworksFile = join(src, 'app/art/artworks.ts');
const sources = filesBelow(src).filter(
  (file) => /\.(html|ts|scss)$/.test(file) && !file.endsWith('.spec.ts'),
);

// Gemälde: Daten, Dateien und Nachweise stimmen überein (Handbuch, Kapitel 6).
const artworks = readFileSync(artworksFile, 'utf8');
const widths = (artworks.match(/const WIDTHS = \[([^\]]+)\]/)?.[1] ?? '')
  .split(',')
  .map((value) => Number(value.trim()))
  .filter(Boolean);
if (widths.length === 0) {
  report(artworksFile, 'WIDTHS nicht gefunden');
}
const ids = [...artworks.matchAll(/^\s+id: '([^']*)',$/gm)].map((match) => match[1]);
const constants = [...artworks.matchAll(/^const ([A-Z_]+): Artwork = \{/gm)].map((m) => m[1]);
const assets = readFileSync(join(root, 'docs/assets.md'), 'utf8');
const expectedFiles = new Set();
for (const id of ids) {
  if (!/^[a-z]+(-[a-z0-9]+)+$/.test(id)) {
    report(artworksFile, `id „${id}“ folgt nicht dem Muster <nachname>-<stichwort>`);
  }
  for (const width of widths) {
    const name = `${id}-${width}.webp`;
    expectedFiles.add(name);
    if (!existsSync(join(artDir, name))) {
      report(artworksFile, `Datei web/public/art/${name} fehlt`);
    }
  }
  if (!assets.includes(`- Dateien: \`web/public/art/${id}-{${widths.join(',')}}.webp\`.`)) {
    report(artworksFile, `„${id}“ hat keinen Abschnitt mit Dateizeile in docs/assets.md`);
  }
}
if ((artworks.match(/widths: WIDTHS,/g) ?? []).length !== ids.length) {
  report(artworksFile, 'jedes Werk nutzt `widths: WIDTHS`, keine eigenen Breiten');
}
for (const name of constants) {
  if ((artworks.match(new RegExp(`\\b${name}\\b`, 'g')) ?? []).length < 2) {
    report(artworksFile, `${name} steht in keiner Liste und auf keiner festen Stelle`);
  }
}
for (const name of readdirSync(artDir)) {
  if (!expectedFiles.has(name)) {
    report(join(artDir, name), 'Datei wird in artworks.ts nicht verwendet');
  }
}

// Gestaltung und Texte (Handbuch, Kapitel 3, 6 und 7).
const word = (pattern, flags = 'iu') => new RegExp(`(?<!\\p{L})(?:${pattern})(?!\\p{L})`, flags);
const forbiddenEverywhere = [
  [/—/u, 'englischer Gedankenstrich „—“, im Deutschen „–“ nutzen'],
  [/[\p{Extended_Pictographic}←-⇿✀-❵➔-➿⬀-⯿]/u, 'Emoji, Deko-Zeichen oder Pfeil'],
  [/text-transform:\s*uppercase/, 'gesperrte Großbuchstaben sind nicht erlaubt'],
];
const forbiddenText = [
  [word('du|dich|dir|dein\\p{L}*|euch|euer|eure\\p{L}*'), 'direkte Anrede'],
  [
    word('entdeck\\p{L}*|eintauch\\p{L}*|tauch\\p{L}* ein|Facette\\p{L}*|Reise|Raum für'),
    'Wort aus der Sperrliste',
  ],
  [
    word('Test starten|Jetzt starten|Jetzt testen|Los geht'),
    'Teststart, obwohl es keinen Test gibt',
  ],
  [
    word(
      '(?:Wähler|Nutzer|Teilnehmer|Experten|Bürger|Politiker|Anhänger|Leser|Besucher)(?:n|s)?',
      'u',
    ),
    'generisches Maskulinum',
  ],
  [/\p{L}[*:_]innen|\p{Ll}Innen(?!\p{L})/u, 'Gender-Sonderzeichen'],
];
const colorLiteral = /#[0-9a-fA-F]{3,8}\b|\b(rgb|rgba|hsl|hsla)\(/;
const artComponents = [join(src, 'app/art/art-figure.ts'), join(src, 'app/art/art-gallery.html')];

function visibleText(file, text) {
  // Kommentare enthalten keine sichtbaren Texte.
  return file.endsWith('.ts')
    ? text.replace(/\/\*[\s\S]*?\*\//g, '').replace(/^\s*\/\/.*$/gm, '')
    : text.replace(/<!--[\s\S]*?-->/g, '');
}

// Wortgetreue historische Fragen bleiben erhalten. Nur belegte Wortlaut-Literale
// der hashgebundenen Projektion sind von der Regel zum generischen Maskulinum
// ausgenommen. Eigene Erläuterungen und alle anderen Regeln gelten weiterhin.
const originalCatalogueFile = join(src, 'app/policy-draft/public-catalogue.ts');
let originalWordingLiterals = [];
if (existsSync(originalCatalogueFile)) {
  try {
    execFileSync(process.execPath, [join(src, 'app/policy-draft/verify-public-catalogue.mjs')], {
      stdio: 'pipe',
    });
    const catalogue = JSON.parse(
      readFileSync(join(root, 'data/politikprofil-v2.fragen.entwurf.json'), 'utf8'),
    );
    originalWordingLiterals = catalogue.items.map(
      ({ wordingDe }) => `'${wordingDe.replace(/\\/g, '\\\\').replace(/'/g, "\\'")}'`,
    );
  } catch {
    report(originalCatalogueFile, 'Originalquellen-Parität nicht bestätigt');
  }
}

// Profilregeln zitieren Originalwortlaute in „…“. Wörtlich belegte Zitate aus dem
// v2-Katalog oder der v2.2-Ergänzung sind von der Regel zum generischen Maskulinum
// ausgenommen. Eigene Texte außerhalb der Zitate gelten weiterhin.
const profileRulesFile = join(src, 'app/policy-draft/profile/profile-rules.ts');
const originalWordings = [
  'data/politikprofil-v2.fragen.entwurf.json',
  'data/politikprofil-v2.2.ergaenzung.json',
]
  .filter((path) => existsSync(join(root, path)))
  .flatMap((path) => JSON.parse(readFileSync(join(root, path), 'utf8')).items)
  .map(({ wordingDe }) => wordingDe);
const withoutVerbatimQuotes = (prose) =>
  prose.replace(/„([^“]*)“/g, (quote, inner) =>
    originalWordings.some((wording) => wording.includes(inner)) ? '' : quote,
  );

for (const file of sources) {
  const text = readFileSync(file, 'utf8');
  for (const [pattern, message] of forbiddenEverywhere) {
    if (pattern.test(text)) {
      report(file, message);
    }
  }
  if (file.endsWith('.html')) {
    // Angular-Steuerblöcke wie @for (…; track …) sind kein sichtbarer Text.
    const prose = visibleText(file, text).replace(/@\w+[^{]*\{/g, '');
    if (/\p{L};\s/u.test(prose)) {
      report(file, 'Semikolon im sichtbaren Text, zwei Aussagen werden zwei Sätze');
    }
  }
  if (/\.(html|ts)$/.test(file)) {
    const visible = visibleText(file, text);
    for (const [pattern, message] of forbiddenText) {
      const checked =
        file === originalCatalogueFile && message === 'generisches Maskulinum'
          ? originalWordingLiterals.reduce(
              (prose, literal) => prose.replaceAll(literal, ''),
              visible,
            )
          : file === profileRulesFile && message === 'generisches Maskulinum'
            ? withoutVerbatimQuotes(visible)
            : visible;
      const match = checked.match(pattern);
      if (match) {
        report(file, `${message} („${match[0]}“)`);
      }
    }
  }
  const tokenExceptions = [stylesFile, artworksFile, indexFile];
  if (!tokenExceptions.includes(file) && colorLiteral.test(text)) {
    report(file, 'Farbwert außerhalb von styles.scss, bitte eine Variable nutzen');
  }
  if (file !== stylesFile && /font-family\s*:/.test(text)) {
    report(file, 'Schrift nur über --font-serif in styles.scss festlegen');
  }
  if (!artComponents.includes(file) && /<img\b|url\([^)]*art\/|style\.background/.test(text)) {
    report(file, 'Gemälde nur über app-art-figure oder app-art-gallery einbinden');
  }
  const external =
    /<(?:link|script|img|source|iframe)\b[^>]*\b(?:src|srcset|href)\s*=\s*["']https?:|url\(\s*["']?https?:|@import\s+["']?https?:/;
  if (external.test(text)) {
    report(file, 'externe Datei eingebunden, Assets müssen lokal liegen');
  }
}

// Die Browserfarbe in index.html entspricht dem Papierton.
const paper = readFileSync(stylesFile, 'utf8').match(/--paper: (#[0-9a-f]+);/)?.[1];
const themeColor = readFileSync(indexFile, 'utf8').match(
  /name="theme-color" content="([^"]+)"/,
)?.[1];
if (!paper || themeColor !== paper) {
  report(indexFile, `theme-color „${themeColor}“ entspricht nicht --paper „${paper}“`);
}

// Seitentitel (Handbuch, Kapitel 4).
const routesFile = join(src, 'app/app.routes.ts');
for (const [, title] of readFileSync(routesFile, 'utf8').matchAll(/title: '([^']+)'/g)) {
  if (title !== '12 Axes Deutschland' && !title.endsWith(' · 12 Axes Deutschland')) {
    report(
      routesFile,
      `Seitentitel „${title}“ folgt nicht dem Muster „Seite · 12 Axes Deutschland“`,
    );
  }
}

if (problems.length > 0) {
  console.error(`Handbuch-Prüfung: ${problems.length} Abweichung(en)\n`);
  for (const problem of problems) {
    console.error(`- ${problem}`);
  }
  process.exit(1);
}
console.log(
  `Handbuch-Prüfung bestanden: ${ids.length} Gemälde, ${sources.length} Quelldateien, Seitentitel.`,
);
