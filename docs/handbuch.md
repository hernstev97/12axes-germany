# Handbuch für Gestaltung und Texte

Stand: 3. Oktober 2026. Dieses Handbuch gilt für jede Arbeit an Oberfläche, Bedienung, Bildern und sichtbaren Texten der Website „12 Axes Deutschland“. Es ersetzt die frühere `design.md`.

## 0 Gebrauch

- Wer `web/`, sichtbare Texte, Bilder oder dieses Handbuch ändert, liest es vorher ganz.
- „Muss“, „nie“ und „nur“ sind Pflicht. „Soll“ ist der Normalfall; eine Abweichung steht mit Begründung im PR.
- Rangfolge: `AGENTS.md` und [LIFE-93](https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent) regeln Inhalt, Wissenschaft und Daten und gehen vor. Danach kommt dieses Handbuch, danach der eigene Geschmack. Widerspricht das Handbuch `AGENTS.md`, ist das Handbuch falsch; der Agent meldet das.
- Fehlt eine Regel, gilt das nächstliegende vorhandene Muster. Ein neues Muster (neue Komponente, Farbe, Seitenart, Bildregel) stimmt der Agent vorher mit Steven ab und trägt es im selben PR hier ein.
- Name, Flagge, Farben, Schrift, Bildauswahl und Ton entscheidet Steven.
- `pnpm check` führt `scripts/check-handbuch.mjs` aus. Regeln mit dem Vermerk _(automatisch geprüft)_ prüft das Skript. Alles andere prüft der Agent nach Kapitel 10.

## 1 Leitbild

Die Website ist die sachliche Informationsseite eines Forschungsprototyps. Sie soll ruhig, sorgfältig und vertrauenswürdig wirken, etwa wie die Projektseite eines Instituts oder einer Bibliothek. Die Gestaltung stammt von [Contra Labs](https://contralabs.com/): warmes Papier, große Serifen, viel Raum und klassische Gemälde, hier aus der deutschen Romantik. Code, Marken und Assets von Contra Labs übernimmt das Projekt nicht.

„Offiziell“ heißt hier: klare Ordnung, nüchterne Sprache, belegte Angaben. Es heißt nicht amtlich. Die Seite darf nie wie ein Angebot einer Behörde, einer Partei oder des European Social Survey aussehen.

Die erste Fassung vom 3. Oktober 2026 wirkte nach Stevens Urteil „extrem vibe coded“ und esoterisch. Diese Muster kommen nicht zurück:

- Slogans und Pointen wie „Politik hat viele Seiten. Du auch.“
- kleine gesperrte Großbuchstabenzeilen über Titeln, etwa „EIN POLITIKTEST IN VORBEREITUNG“
- Zweizeiler-Taglines wie „Noch am Anfang. Von Anfang an offen.“ oder „Ein eigenes Profil. Raum für Unterschiede.“
- kursive Halbsätze als Pointe im Titel („Die eigene Haltung _besser verstehen._“)
- Deko-Zeichen (✳, ↗, ↓) und Pillen-Schaltflächen mit Pfeilen
- maskierte oder abgerundete Gemälde
- mehrere gleichwertige Aktionen im ersten Bildschirm
- direkte Anrede und Werbesprache

## 2 Name und Marke

### Name

- Der Name lautet „12 Axes Deutschland“: Ziffern 12, Leerzeichen, „Axes“ mit großem A, Leerzeichen, „Deutschland“. Nicht „12axes“, „12 AXES“ oder „12 Achsen“.
- Der Name ist vorläufig. Die Zahl zwölf ist keine methodische Vorgabe. Kein Text darf zwölf Dimensionen ankündigen oder nahelegen.
- 12 Axes (12axes.vercel.app) ist an diesem Projekt nicht beteiligt. Von 12 Axes übernimmt das Projekt nichts: kein Modell, keine Fragen, Texte, Gestaltung, Farben, Schriften, kein Code und keine Daten. Die Lizenz von 12 Axes behält all das dem Autor vor.

### Wortmarke

- Aufbau: Flagge, dann „**12 Axes** Deutschland“. „12 Axes“ steht in Strichstärke 700, „Deutschland“ in 400. Die Wortmarke bricht nie um.
- Kopf: 1,25 rem, auf dem Smartphone 1,12 rem. Fußzeile: gleiche Aufteilung ohne Flagge.
- Die Wortmarke im Kopf ist der Link zur Startseite mit `aria-label="12 Axes Deutschland, Startseite"`.

### Flagge

- Die Website zeigt die Bundesflagge: drei waagerechte Streifen Schwarz, Rot, Gold im Verhältnis 3 : 5.
- Farben `--flag-black` `#000`, `--flag-red` `#f00`, `--flag-gold` `#fc0` aus dem Styleguide der Bundesregierung (Herkunft in `assets.md`).
- Größe im Kopf 30 × 18 px, auf dem Smartphone 25 × 15 px, mit Haarlinie `--hairline`, vor der Wortmarke, `aria-hidden="true"`.
- Die Flagge steht nur im Kopf und im Favicon (`web/public/favicon.svg`: Flagge 3 : 5 über der Zahl 12).
- Nie: Bundesadler, Wappen, Bundesdienstflagge, senkrechter Flaggenstab wie im Erscheinungsbild der Bundesregierung, die Schrift BundesSans, das Wort „offiziell“, Flaggen als Schmuck im Inhalt. Die Flaggenfarben sind keine Gestaltungsfarben, auch nicht für Schaltflächen, Antworten oder Diagramme.

## 3 Grundlagen

Die Gestaltungswerte des Seitenlayouts stehen als CSS-Variablen in `web/src/styles.scss`. Komponenten nutzen diese Variablen. Farbwerte und Schriftangaben außerhalb von `styles.scss` sind nicht erlaubt _(automatisch geprüft)_. Ausgenommen sind die mittleren Bildfarben (`Artwork.tone`) in `artworks.ts` als Platzhalter beim Laden und die `theme-color` in `index.html`. Die `theme-color` entspricht `--paper` _(automatisch geprüft)_. Das eigenständige SVG-Favicon folgt Kapitel 2.

### Farben

| Variable            | Wert                 | Einsatz                                                                                                          |
| ------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `--paper`           | `#f6f3eb`            | Seitenhintergrund                                                                                                |
| `--mat`             | `#ebe6da`            | Passepartout der Galerie, gewählte Antwort im Forschungsentwurf                                                  |
| `--ink`             | `#1e2b24`            | Text, Titel, Primärschaltfläche, Rahmen                                                                          |
| `--ink-hover`       | `#33463b`            | Hover der Primärschaltfläche                                                                                     |
| `--muted`           | `#4c574f`            | Nebentext: Bildunterschrift, Datum, Status, Brotkrumen                                                           |
| `--line`            | `#d4d0c3`            | Trennlinien, Rahmen der Galerie-Schaltflächen, Rahmen von Fragekarte und Antworten, Spur des Fortschrittsbalkens |
| `--forest`          | `#1f3a32`            | dunkle Fläche und Fußzeile, Oberkante der Fragekarte                                                             |
| `--forest-line`     | `#3d5a50`            | Unterstreichung in der Fußzeile                                                                                  |
| `--on-forest`       | `#f2efe6`            | Text auf `--forest`                                                                                              |
| `--on-forest-muted` | `#c5cfc6`            | Nebentext auf `--forest`                                                                                         |
| `--selection`       | `#d5dfd2`            | Textauswahl                                                                                                      |
| `--hairline`        | Tinte mit 12 %       | Haarlinie um die Flagge                                                                                          |
| `--shadow-art`      | zwei weiche Schatten | Gemälde in der Galerie                                                                                           |
| `--focus`           | `var(--ink)`         | Fokusrahmen; auf `--forest` auf `--on-forest` setzen                                                             |

Gemessene Kontraste: `--ink` auf `--paper` 13,3 : 1, `--muted` auf `--paper` 6,8 : 1, `--muted` auf `--mat` 6,1 : 1, `--on-forest` auf `--forest` 10,7 : 1, `--on-forest-muted` auf `--forest` 7,7 : 1, `--paper` auf `--ink-hover` 9,1 : 1, `--ink` auf `--mat` 11,8 : 1 (gewählte Antwort), `--ink` auf `--line` 9,5 : 1 (Fortschrittsbalken). `--line` (1,4 : 1) ist nur Linie und trägt keine Information.

Neue Farben gibt es nur nach Absprache. Farben von Parteien oder politischen Lagern sind tabu. Farben für Ergebnisse und Antworten sind noch nicht festgelegt.

### Schrift

- Einzige Schrift ist Libre Baskerville (`--font-serif`), lokal aus `@fontsource-variable/libre-baskerville`, Strichstärken 400 und 700 _(automatisch geprüft: keine andere `font-family`)_.
- Kursiv nur für Werktitel in `<cite>`.
- Keine Großbuchstaben-Transformation _(automatisch geprüft)_ und keine Sperrung. Titel haben `letter-spacing: -0.012em`, die Wortmarke `-0.01em`, alles andere 0.
- Die Grundgröße steht in Prozent, nie in px, damit die eingestellte Schriftgröße des Browsers wirkt: 106,25 % (17 px), bis 640 px Breite 100 %.

### Größenskala

| Variable / Element | Wert                                 | Einsatz                                                                        |
| ------------------ | ------------------------------------ | ------------------------------------------------------------------------------ |
| `--size-display`   | `clamp(2.3rem, 4.4vw, 4rem)`         | nur H1 der Startseite (`.display-title`)                                       |
| `--size-title`     | `clamp(2.1rem, 3.6vw, 3.25rem)`      | H1 aller anderen Seiten (`.page-title`)                                        |
| `--size-section`   | `clamp(1.6rem, 2.4vw, 2.15rem)`      | H2 (`.section-title`)                                                          |
| `h3`               | 1 rem, fett                          | Listenüberschriften                                                            |
| Fließtext          | 1 rem, Zeilenhöhe 1,7                | Absätze, Listen                                                                |
| `--size-lead`      | 1,12 rem, Zeilenhöhe 1,65            | ein Einleitungsabsatz unter der H1 (`.lead`)                                   |
| `--size-ui`        | 0,94 rem                             | Navigation, Inhaltsverzeichnis, Schaltflächen, Umfangslisten und Bildnachweise |
| `--size-small`     | 0,84 rem                             | Bildunterschrift, Statusleiste, Brotkrumen, Datum                              |
| `--size-brand`     | 1,25 rem, bis 640 px Breite 1,12 rem | Wortmarke im Kopf                                                              |

Titel haben Zeilenhöhe 1,12 bis 1,18 und `text-wrap: balance`. Zeilenumbrüche in Titeln mit `<br>` sind nicht erlaubt.

### Raster

- Inhalt steht in `.page-width`: höchstens `--page-width` (1240 px), Seitenrand `--page-padding`.
- Jeder Mehrspalter nutzt `.grid` (12 Spalten, Abstand `--gutter`) und genau diese Bereiche:

| Klasse                | Spalten | Einsatz                                 |
| --------------------- | ------- | --------------------------------------- |
| `.area-title`         | 1–5     | Abschnittstitel                         |
| `.area-body`          | 6–12    | Abschnittsinhalt                        |
| `.area-half`          | 1–6     | Text im Hero und auf der dunklen Fläche |
| `.area-half-end`      | 7–12    | Galerie im Hero                         |
| `.area-text-wide`     | 1–7     | Kopf einer Dokumentseite                |
| `.area-figure`        | 8–12    | Gemälde neben Text (Querformat)         |
| `.area-figure-narrow` | 9–12    | Gemälde neben Text (Hochformat)         |

- Unter 860 px Breite stapeln sich alle Bereiche.
- Eigene `grid-template-columns` für Seitenlayouts sind nicht erlaubt. Komponenten dürfen intern eigene Raster haben (Faktenliste, Umfangslisten).

### Abstände und Umbrüche

- Abschnitte (`.section`) haben oben und unten `--section-space` und oben eine Linie in `--line`. Dokumentseiten nutzen `--section-space-dense`. Nach der dunklen Fläche entfällt die Linie.
- Umbruchpunkte: 1180 px (Umfangslisten einspaltig), 860 px (Raster einspaltig), 640 px (Grundgröße 100 %, Silbentrennung in Absätzen und Listen, Faktenliste einspaltig), 480 px (Galerie-Steuerung unter der Bildunterschrift). Weitere Umbruchpunkte nur mit Begründung.
- Datumsangaben und andere Wortgruppen, die nicht getrennt werden dürfen, stehen in `<span class="nowrap">`.

### Bewegung

- Erlaubt sind die Überblendung der Galerie (1 s) und Farbwechsel bei Hover (160 ms).
- Keine Scroll-Animationen, kein Parallax, kein Einblenden beim Scrollen, kein automatisches Scrollen.
- `prefers-reduced-motion: reduce` schaltet Übergänge global ab und startet die Galerie nicht von selbst.

## 4 Seiten

### Rahmen

Jede Seite hat dieselbe Hülle aus `web/src/app/app.html`: Sprunglink, Kopf mit Wortmarke und Hauptnavigation, Statusleiste, `<main id="main-content">`, Fußzeile. Seiten wiederholen diese Teile nicht.

### Seitenarten

**Startseite.** Hero mit H1 (`.display-title`), Lead und genau einer Primärschaltfläche in `.area-half`, daneben die Galerie in `.area-half-end`. Danach Abschnitte mit Titel links und Inhalt rechts, genau eine dunkle Fläche mit einem Gemälde und am Ende „Stand der Arbeit“.

**Dokumentseite** (heute „Projektstand“, später etwa Methodik, Grenzen, Daten und Lizenzen). Kopf in `.area-text-wide` mit Brotkrumen, H1 (`.page-title`), Datumszeile „Stand: …“, Lead und Inhaltsverzeichnis, daneben höchstens ein Gemälde in `.area-figure-narrow`. Danach Abschnitte mit `--section-space-dense`, jeder mit H2 in `.area-title` und Inhalt in `.area-body`.

**Fehlerseite.** H1, ein Satz, eine Primärschaltfläche „Zur Startseite“, ein Gemälde.

**Test und Ergebnis.** Noch nicht gestaltet. Bis Steven eine Gestaltung freigibt, gelten nur diese Leitplanken: kein sichtbarer Teststart, bevor ein freigegebener Test existiert (`AGENTS.md`); keine Gemälde; Text, Antworten und Fortschritt im Vordergrund; keine Flaggen-, Partei- oder Lagerfarben; der Statushinweis aus LIFE-93, Phase 6, steht auf jeder Ergebnisseite.

**Ablauf des Forschungsentwurfs** (`app-policy-draft`, `app-policy-progress`, `app-policy-question`). Er gilt nur für den lokalen Forschungsentwurf und ist keine Freigabe von Test oder Ergebnis.

Steven hat am 5. Oktober 2026 vorgegeben:

- ein eigener Startbildschirm vor den Fragen,
- die Originaleinleitung als eigener Bildschirm vor ihrem Frageblock,
- die Frage mittig, mit Fortschrittsbalken und automatischem Wechsel nach einer Antwort,
- Herkunft, Originalkontext, Version und Quellen unauffällig unter der Frage,
- das Überspringen mit Grund bleibt,
- das Beantworten so fokussiert wie möglich und möglichst ohne Scrollen.

Die folgenden Einzelheiten hat Claude festgelegt. Sie gelten, bis Steven die Gestaltung von Test und Ergebnis entscheidet (Kapitel 11).

- **Startbildschirm.** H1 „Fragenentwurf“, Datumszeile, Lead und Speicherhinweis stehen mittig in einer Spalte von höchstens 46 rem. Darunter folgt die Primärschaltfläche „Zu den Fragen“, dann die Textschaltflächen „Zur Fragenübersicht“ und „Zum Ergebnisentwurf“.
- **Einleitungsbildschirm.** Fragen, die nacheinander dieselbe Originaleinleitung haben, bilden einen Block. Vor dem ersten Block und beim Vorwärtsgehen in einen neuen Block steht die Einleitung auf einem eigenen Bildschirm, je Block einmal in der Sitzung. Oben stehen Fortschritt und Schalter wie auf dem Fragebildschirm. Die H2 lautet „Einleitung zu Frage n bis m“, bei einem Block aus einer Frage „Einleitung zu Frage n“. Die Einleitung steht in Lead-Größe. Unter der Karte stehen „Vorherige Frage“ und „Zu Frage n“. Rückwärts und bei Sprüngen aus Übersicht oder Ergebnis erscheint die Frage direkt. Die Einleitung öffnet dann die Schaltfläche „Einleitung zu dieser Frage anzeigen“ unter der Karte.
- **Fragebildschirm.** Er hat keinen sichtbaren Seitenkopf, die H1 „Fragenentwurf“ ist nur für Hilfsmittel lesbar. Oben steht der Fortschritt: „Frage n von N“ als H2 in 1 rem fett und als Fokusziel, der Schalter „Nach einer Antwort automatisch zur nächsten Frage“, ein Balken für bearbeitete Fragen und die Zählzeile. Bearbeitet heißt beantwortet oder übersprungen. Bis 640 px ist die Zählzeile nur für Hilfsmittel lesbar. Die H2 entsteht je Bildschirm neu, damit Hilfsmittel den Fokuswechsel ansagen.
- Die Karte hat einen Rahmen in `--line` und eine Oberkante von 3 px in `--forest`. Sie hat keinen Schatten und keine Rundung.
- In der Karte steht oben der Bereich, dahinter „Übersprungen“, wenn die Frage übersprungen wurde. Danach folgen eine fragebezogene Situationsbeschreibung, falls vorhanden, und die Frage als `legend` in `clamp(1.15rem, 2vw, 1.4rem)`. Dann kommen die Antworten als native Radios in gerahmten Zeilen, am Ende das Überspringen mit Grund und „Frage überspringen“. Gibt es eine Antwort oder ein Überspringen, folgt dahinter „Auswahl zurücksetzen“. Es steht unter den Antworten, damit sein Erscheinen keine Antwort verschiebt.
- Die gewählte Antwort hat einen Rahmen in `--ink` und die Fläche `--mat`. Der Wechsel geschieht ohne Übergang. Antworten haben keine Symbole und keine Farben, die Zustimmung oder Ablehnung werten.
- 0–10-Listen stehen als Zahlenreihe: über 640 px in einer Zeile, sonst in zwei Zeilen zu sechs und fünf, die zweite rechtsbündig. Die Endbeschriftungen stehen sichtbar darunter und bleiben Teil des Namens der beiden Endantworten. Die übrigen Antworten heißen wie im Katalog nach ihrer Zahl. Endbeschriftungen ohne Zahl erhalten den Code aus dem deutschen Originalfragebogen.
- Unter der Karte stehen „Vorherige Frage“ und „Nächste Frage“. Bei der letzten Frage heißt die zweite Schaltfläche „Zum Ergebnisentwurf“. Die Schaltfläche nach vorn ist ausgefüllt wie eine Primärschaltfläche, weil sie zum nächsten Bildschirm führt (Ausnahme zu Kapitel 5).
- Danach folgen unauffällig:
  - die Schaltfläche zur Einleitung,
  - Herkunft und Entwicklungshinweis,
  - der Satz „Überspringen ist keine politische Antwort …“,
  - „Originalkontext, Version und Quellen“,
  - die Textschaltflächen „Zur Fragenübersicht“ und „Zum Ergebnisentwurf“.
- Der automatische Wechsel ist zu Beginn eingeschaltet. Nach Klick, Tippen, Leertaste oder Eingabetaste auf einer gewählten Antwort folgt nach 350 ms der nächste Bildschirm, und der Fokus geht auf die H2. Pfeiltasten wählen nur aus. Nach der letzten Frage wechselt die Ansicht nicht von selbst.
- Der Schalter steht vor den Antworten. So ist der Wechsel angekündigt, bevor jemand antwortet (WCAG 3.2.2).
- Beim Wechsel gibt es keinen Übergang und keine Animation.
- Bei erzwungenen Farben zeigt der Schalter die native Darstellung. Der Fortschrittsbalken behält seine Farben, weil sonst Spur und Wert gleich aussähen.

### Neue Seite anlegen

1. Route in `web/src/app/app.routes.ts` mit `loadComponent` und Titel nach dem Muster „Seitenname · 12 Axes Deutschland“; die Startseite heißt nur „12 Axes Deutschland“ _(automatisch geprüft)_.
2. Komponente als Standalone-Komponente mit `ChangeDetectionStrategy.OnPush`, Vorlage in `.html`, Stil in `.scss` unter 4 kB.
3. Seitenart wählen und nur Klassen und Variablen aus Kapitel 3 und 5 nutzen.
4. Die Hauptnavigation hat höchstens vier Einträge. Neue Einträge nur nach Absprache; sonst verlinkt die Projektseite oder die Fußzeile.
5. Links innerhalb der App nutzen `routerLink` und für Sprungziele `fragment`, nie `href="#…"`. Wegen `<base href="/">` würde ein solcher Link auf Unterseiten die Startseite laden. `app.ts` führt den Fokus nach Seitenwechseln zu `main` und nach Sprunglinks zum Ziel.
6. Ändert sich Navigation oder Seitentitel, gehört ein Test in `app.spec.ts` dazu.

## 5 Komponenten

**Kopf** (`app.html`, `.site-header`). Wortmarke links, Hauptnavigation rechts, Linie darunter. Navigationslinks sind ohne Unterstreichung und unterstrichen bei Hover und auf der aktiven Seite (`routerLinkActive`, `aria-current="page"`).

**Statusleiste** (`.status-bar`). Steht auf jeder Seite unter dem Kopf. Etikett „In Vorbereitung“ mit Rahmen, ein Satz, ein Link „Zum Stand der Arbeit“ auf `/projekt#stand`. Text und Etikett ändern sich nur, wenn sich der Projektstatus ändert.

**Fußzeile** (`.site-footer`). Waldgrün. Wortmarke ohne Flagge, Status, Pflichthinweis (Kapitel 7.7) und die Links „Projektstand“, „Bild- und Schriftnachweise“, „Quellcode auf GitHub“.

**Titel.** Genau eine H1 je Seite. Startseite `.display-title`, alle anderen Seiten `.page-title`, Abschnitte H2 mit `.section-title`, Listenüberschriften H3. Keine Kursive, keine Hervorhebung von Halbsätzen, keine Ebene überspringen.

**Lead** (`.lead`). Höchstens einer je Seite, direkt unter der H1, zwei bis drei Sätze.

**Fließtext** (`.prose`). Absätze mit höchstens fünf Sätzen. Links im Fließtext sind unterstrichen.

**Primärschaltfläche** (`.button.primary`). Rechteckig, Radius 2 px, mindestens 48 px hoch, ohne Symbol oder Pfeil. Höchstens eine je Bildschirmhöhe, nur für Wege zu einer anderen Seite. Eine zweite, gleichwertige Schaltfläche daneben gibt es nicht; für weitere Wege gibt es Textlinks. Ausnahme bis zu Stevens Entscheidung: die ausgefüllte Schaltfläche nach vorn im Ablauf des Forschungsentwurfs (Kapitel 4).

**Textlink** (`.text-link`). Unter einem Absatzblock, etwa „Zum ausführlichen Projektstand“ oder „Quellcode auf GitHub“. Externe Links haben kein Symbol; der Linktext nennt das Ziel.

**Faktenliste** (`dl.facts`). Für Stand und Eigenschaften: `dt` ist die Bezeichnung, `dd` der Wert mit großem Anfangsbuchstaben („Noch nicht festgelegt“). Jede Zeile ist eine belegbare Tatsache. Darüber oder darunter steht das Datum des Stands.

**Umfangslisten** (`.scope`). Zwei Listen mit H3 „Vorgesehen“ und „Nicht vorgesehen“ und Linien zwischen den Einträgen.

**Brotkrumen** (`nav.breadcrumb`, `aria-label="Brotkrumennavigation"`). Nur auf Dokumentseiten. Letzter Eintrag ohne Link mit `aria-current="page"`. Der Trenner „/“ kommt aus CSS mit leerem Alternativtext (`content: '/' / ''`).

**Inhaltsverzeichnis** (`nav.toc`, `aria-label="Inhalt dieser Seite"`). Auf Dokumentseiten ab vier Abschnitten, im Kopf unter dem Lead. Einträge sind `routerLink` mit `fragment`.

**Dunkle Fläche** (`.basis` auf der Startseite). Höchstens eine je Seite, über die ganze Breite. Setzt `--focus`, `--caption-color` und `--caption-strong` für helle Darstellung. Enthält Text in `.area-half` und ein Gemälde in `.area-figure`.

**Galerie** (`app-art-gallery`, `web/src/app/art/art-gallery.*`). Nur im Hero der Startseite. Verhalten:

- quadratisches Passepartout in `--mat`, Bild mit 7 % Rand, ganz und unbeschnitten, Schatten `--shadow-art`
- Wechsel alle 8 s mit 1 s Überblendung; die Bildunterschrift blendet mit; alle Unterschriften liegen übereinander, damit die Höhe gleich bleibt
- Start bei einem zufälligen Bild; geladen werden nur das aktuelle und das nächste Bild
- Pause bei Hover und bei verborgenem Tab; dauerhafte Pause, sobald der Tastaturfokus in die Galerie kommt (WAI-ARIA-Karussellmuster)
- bei reduzierter Bewegung kein automatischer Start
- Steuerung in dieser Reihenfolge: Anhalten/Fortsetzen, Vorheriges Bild, Nächstes Bild, Zähler; Schaltflächen 40 × 40 px; bei nur einem Bild keine Steuerung
- `aria-roledescription` „Galerie“ und „Bild“, verborgene Bilder `inert` und `aria-hidden`, Bildunterschriften nur bei angehaltenem Wechsel `aria-live="polite"`
- darunter der Link „Zu den Bildnachweisen“

Jede Änderung am Verhalten braucht einen Test in `art-gallery.spec.ts`.

**Einzelbild** (`app-art-figure`). Gemälde mit Bildunterschrift. Das `sizes`-Attribut nennt die tatsächlich angezeigte Breite in px und vw, nie in rem. `[priority]="true"` nur für das größte Bild im ersten Bildschirm (Projekt- und Fehlerseite); alle anderen Bilder laden verzögert.

**Bildnachweisliste.** Auf `/projekt#bildnachweise`, erzeugt aus `ALL_ARTWORKS`. Nie von Hand pflegen.

## 6 Bilder

### Platz

- Gemälde stehen auf der Startseite (Galerie und ein Bild auf der dunklen Fläche), auf Dokumentseiten (höchstens eines, im Kopf) und auf der Fehlerseite (eines).
- Jedes Werk hat genau einen Platz auf der Website.
- Nie: im Test oder Ergebnis, neben einer bestimmten politischen Position, Dimension oder Antwort, als Hintergrund hinter Text, als Illustration einer Haltung.
- Bilder nur über `app-art-figure` oder `app-art-gallery` einbinden _(automatisch geprüft)_. Daten nur in `web/src/app/art/artworks.ts`.

### Auswahlregeln

Ein Werk kommt nur auf die Seite, wenn alle Punkte erfüllt sind:

1. Deutsche Romantik oder ihr unmittelbares Umfeld (etwa 1800 bis 1860), Künstler seit mehr als 70 Jahren tot.
2. Landschaft, Stadtansicht oder ruhiger Innenraum. Keine Fahnen, Uniformen, Kampfszenen, Hünengräber, Kreuze oder Gottesdienste im Vordergrund, keine Bezüge zu Kriegen.
3. Keine ausgeprägte politische Rezeption. Prüfstellen sind der Sammlungstext und der Wikipedia-Artikel zum Werk. Beispiele für Ausschlüsse: „Das Eismeer“, „Mondaufgang am Meer“.
4. Provenienz ohne Bedenken. Ausgeschlossen sind Werke mit dem Sammlungsstatus „ungeklärt, bedenklich“ oder „NS-verfolgungsbedingt entzogen“ und Werke, deren Besitzwechsel zwischen 1933 und 1945 unklar ist. Beispiel: „Wanderer über dem Nebelmeer“.
5. Reproduktion auf Wikimedia Commons als gemeinfrei gekennzeichnet (PD-Art), vollständig, ohne Rahmen, unverzerrt und farbtreu im Vergleich mit dem Bild der Sammlung. Beispiel für einen Ausschluss: „Der Watzmann“ (nur verzerrte Reproduktion).

### Verfahren für ein neues Werk

1. Commons-Datei finden, etwa über `https://commons.wikimedia.org/w/api.php?action=query&titles=File:…&prop=imageinfo&iiprop=url|size|sha1|extmetadata&format=json`. Die beste vollständige Fassung wählen und mit dem Bild der Sammlung vergleichen.
2. Kennzeichnung der Dateiseite wörtlich festhalten.
3. Titel, Datierung, Technik und Sammlung auf der Sammlungsseite belegen. Die Website übernimmt die Angaben der Sammlung.
4. Provenienz auf der Sammlungsseite lesen und den Status wörtlich festhalten. Lost Art (lostart.de) und Proveana (proveana.de) abfragen; wenn eine Bot-Sperre das verhindert, das in `assets.md` vermerken.
5. Politische, patriotische und religiöse Lesarten recherchieren und mit Quelle festhalten.
6. Original herunterladen, mit einem User-Agent, der das Projekt nennt (Wikimedia sperrt anonyme Abrufe). Das Original bleibt außerhalb des Repositorys.
7. `scripts/encode-artwork.sh <id> <original>` ausführen. Das Skript rechnet Nicht-sRGB-Profile nach sRGB um, entfernt Metadaten, erzeugt `web/public/art/<id>-{480,800,1200}.webp` mit Qualität 83 ohne Zuschnitt und gibt Prüfsumme und mittlere Farbe aus.
8. 800er-Datei ansehen und den Alt-Text schreiben.
9. Eintrag in `artworks.ts` anlegen (`id`, `artist`, `title`, `date`, `collection`, `alt`, Originalmaße, `widths`, `source`, `tone` = mittlere Farbe) und in eine der Listen (`HOME_GALLERY` oder eine feste Stelle) aufnehmen.
10. Abschnitt in `docs/assets.md` nach dem Muster der vorhandenen Einträge: Einsatz, Sammlung mit Link, Commons-Dateiseite und Originaldatei mit Maßen, Kennzeichnung, SHA-256, Farbe, Provenienz, Dateien, Hinweise _(automatisch geprüft: jede `id` hat Dateien und einen Nachweis, keine verwaisten Dateien)_.

### Werk entfernen

Eintrag aus `artworks.ts` löschen, WebP-Dateien löschen, den Abschnitt in `assets.md` unter „Geprüft und verworfen“ mit Grund zusammenfassen.

### Alt-Text

- Beschreibt, was zu sehen ist: Ort, Figuren, Licht, Vordergrund und Hintergrund.
- Keine Deutung, keine Stimmungswörter wie „erhaben“ oder „sehnsuchtsvoll“, nicht „Gemälde von …“ (das steht in der Unterschrift).
- Höchstens zwei kurze Sätze, etwa 160 Zeichen.

### Bildunterschrift

Drei Zeilen: Künstler; `<cite>Titel</cite>`, Datierung; Sammlung als „Museum, Stadt“ oder Museumsname. Datierung so, wie die Sammlung sie angibt („um 1822“, „1821/22“, „1808–1810“).

## 7 Texte

### 7.1 Haltung

- Sachlich, beschreibend, ruhig. Kurze Sätze im Aktiv. Ein Gedanke je Satz.
- Keine direkte Anrede, weder du noch Sie _(automatisch geprüft für du-Formen)_. Die Texte beschreiben das Projekt.
- Keine Wertung politischer Positionen, keine Aussagen darüber, welche Einstellung richtig ist.
- Jeder Satz muss für dieses Projekt gelten. Ein Satz, der in jedem anderen Projekt stehen könnte, fällt weg.

### 7.2 Ehrlicher Status

- Präsens nur für das, was es gibt. Geplantes mit „soll“, „sollen“, „geplant“ oder „vorgesehen“.
- Nichts erfinden: keine Fragen, Dimensionen, Dimensionsnamen, Werte, Bearbeitungszeiten, Termine oder Gütesiegel. Zahlen nur, wenn sie belegt sind; Analysezahlen nie von Hand.
- Nie „validiert“, „wissenschaftlich geprüft“, „neutral“ oder „objektiv“ als Eigenschaft des Projekts. Die Standardformel lautet: „Das Projekt ist weder validiert noch wissenschaftlich geprüft und kann keine Neutralität garantieren.“
- Technische Prüfungen, CI und KI-Übereinstimmung ersetzen keine methodische Evidenz oder Abnahme. Ein KI-Review zu Methoden darf seinen tatsächlich geprüften Umfang und Befund nennen. Er ersetzt weder empirische Nachweise noch die vorgeschriebenen getrennten Erstbewertungen und Reviews; er ist keine Begutachtung durch Fachleute.
- Belegquellen für Projektfakten sind `docs/project.md`, `AGENTS.md` und LIFE-93. Ändert sich der Stand, ändern sich Faktenlisten und Datumszeilen im selben PR.

### 7.3 Begriffe

| Begriff                                              | Verwendung                                                                                     | Nicht                                                                          |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| der geplante Test, Test zu politischen Einstellungen | Name der Sache                                                                                 | Quiz, Politiktest als Hauptbegriff, Wahlhilfe                                  |
| Einstellung                                          | was der Test beschreibt                                                                        | Haltung, Gesinnung, Meinung, Identität                                         |
| Profil                                               | Ergebnis mit mehreren Dimensionen                                                              | Typ, Persönlichkeit                                                            |
| Dimension                                            | Teil des Profils                                                                               | Achse (außer im Namen), Skala                                                  |
| Bevölkerung                                          | Befragte des ESS in Deutschland                                                                | „die Deutschen“                                                                |
| Wählergruppe                                         | Befragte, die nach eigener Angabe bei der letzten Bundestagswahl dieselbe Partei gewählt haben | Wähler, Anhänger, „reale Wählergruppen“, Partei                                |
| Befragte, Wählerschaft                               | neutrale Personenbezeichnungen                                                                 | generisches Maskulinum, Gender-Sonderzeichen _(teilweise automatisch geprüft)_ |
| European Social Survey (ESS)                         | beim ersten Vorkommen ausgeschrieben, verlinkt, „repräsentative wissenschaftliche Befragung“   | Quelle der Interpretation                                                      |
| eigenes Modell                                       | Auswahl, Dimensionen, Auswertung und Deutung durch das Projekt                                 | Modell des ESS                                                                 |
| Vergleichsdaten, Vergleichswerte                     | Werte aus den ESS-Daten                                                                        | Durchschnittsmeinung                                                           |
| methodische Prüfung                                  | geplante Prüfung von Auswahl, Modell und Texten                                                | wissenschaftliche Prüfung als künftiger Zustand                                |
| Begutachtung durch Fachleute                         | findet nicht statt; so benennen                                                                | Peer Review                                                                    |
| KI-Reviews                                           | Reviews durch Sprachmodelle                                                                    | Reviews ohne Zusatz, Gutachten                                                 |
| technische Prüfungen                                 | CI, Tests, Build                                                                               | Qualitätsnachweis                                                              |
| zusammengefasste Ergebnisse aus den ESS-Daten        | was veröffentlicht werden soll                                                                 | aggregierte Ergebnisse, gesammelte Testergebnisse                              |
| Staaten, Personen aus der Politik                    | was nicht zugeordnet wird                                                                      | Länder (verwechselbar mit Bundesländern), Politiker                            |
| Website                                              | die ganze Seite                                                                                | Webseite, Plattform, App                                                       |
| 12 Axes                                              | „der Online-Test 12 Axes“                                                                      | Partner, Original, Vorlage für Fragen                                          |

### 7.4 Verbotene Muster

- Slogans, Wortspiele, Taglines, rhetorische Fragen, Ausrufezeichen, Metaphern, Pathos
- Meta-Sätze über den eigenen Text („Diese Seite beschreibt …“)
- Werbe- und Sperrwörter wie entdecken, eintauchen, Facetten, Reise, „Raum für“, „Test starten“ _(automatisch geprüft)_
- KI-Muster nach `.agents/skills/unslop/SKILL.md`: „nicht nur … sondern auch“, Dreierreihen um ihrer selbst willen, Füllwörter (zudem, ferner, hierbei, hinsichtlich, im Rahmen von), „dient als“, „stellt dar“, Nominalstil, Amtsdeutsch („erfolgen“, „seitens“), Lehnübersetzungen („real“, „erklärendes Ergebnis“)
- Ketten aus Semikolons; zwei Aussagen werden zwei Sätze
- Emojis, Deko-Zeichen und Pfeile _(automatisch geprüft)_

### 7.5 Typografie

- Anführungszeichen „so“, verschachtelt ‚so‘.
- Gedankenstrich – mit Leerzeichen; Bis-Strich – ohne Leerzeichen in Spannen („1808–1810“). Nie der englische Strich „—“ _(automatisch geprüft)_.
- Datum „3. Oktober 2026“, in Fließtext ohne Umbruch (`.nowrap`). Im Repository ISO-Format „2026-10-03“.
- Zahlen bis zwölf im Fließtext als Wort, außer in Namen, Daten, Maßen und Tabellen.
- Keine Großbuchstabenwörter zur Betonung, keine fett gesetzten Satzteile im Fließtext.

### 7.6 Bedienelemente, Titel und Metadaten

- Link- und Schaltflächentexte nennen das Ziel: „Zum Projektstand“, „Zur Startseite“, „Quellcode auf GitHub“. Nie „Hier klicken“, „Mehr“ oder „Weiter“.
- `aria-label` sind deutsch und beschreiben die Handlung („Bildwechsel anhalten“, „Nächstes Bild“).
- Seitentitel siehe Kapitel 4. Die Meta-Beschreibung in `index.html` hat höchstens 160 Zeichen, beginnt mit dem Namen und nennt den Status.

### 7.7 Pflichttexte

- Statusleiste: Etikett „In Vorbereitung“, Satz „Der geplante Test ist noch nicht verfügbar.“, Link „Zum Stand der Arbeit“.
- Fußzeile: „Diese Website ist kein Angebot einer Behörde, einer Partei, des European Social Survey oder von 12 Axes. Das Projekt entsteht mit KI-Agenten. Fachleute haben es nicht begutachtet.“
- Projektstand: die Standardformel aus 7.2.
- Ergebnisseiten (später): der Statushinweis aus LIFE-93, Phase 6, im Wortlaut.

Diese Texte ändern sich nur, wenn sich der Sachstand ändert.

### 7.8 Vorgehen beim Schreiben

1. Belegbare Fakten aus `docs/project.md`, `AGENTS.md` und LIFE-93 sammeln.
2. Entwurf schreiben, dann `.agents/skills/unslop/SKILL.md` anwenden.
3. Gegen 7.2 bis 7.7 prüfen.
4. Längere neue Texte (ein Abschnitt oder mehr) lässt der Agent zusätzlich von einem getrennten Prüfagenten auf Fakten, KI-Ton und Neutralität lesen. Übereinstimmung von Agenten ist kein Beleg.

### 7.9 Beispiele

| Früher                                             | Heute                                                               | Grund                                                  |
| -------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------ |
| „Politik hat viele Seiten. Du auch.“               | „12 Axes Deutschland plant einen Test zu politischen Einstellungen“ | Slogan und Anrede; Titel nennt jetzt Urheber und Sache |
| „EIN POLITIKTEST IN VORBEREITUNG“ über dem Titel   | Statusleiste mit Etikett „In Vorbereitung“                          | gesperrte Großbuchstaben                               |
| „Das Vorhaben entdecken ↓“ und zweite Schaltfläche | eine Schaltfläche „Zum Projektstand“                                | Werbewort, Pfeil, doppelte Aktion                      |
| „Noch am Anfang. Von Anfang an offen.“             | Faktenliste „Stand der Arbeit“                                      | Tagline statt Tatsachen                                |
| „Wissenschaftliche Prüfungen: Noch nicht erfolgt“  | „Methodische Prüfungen: Noch keine“                                 | kündigte ein „wissenschaftlich geprüft“ an             |
| „Reviews“                                          | „KI-Reviews“                                                        | sonst als Peer Review lesbar                           |
| „realen Wählergruppen“                             | „Wählergruppen“ mit Definition                                      | Lehnübersetzung, unklar                                |

## 8 Barrierefreiheit

Ziel ist WCAG 2.2 AA.

- `lang="de"`, genau eine H1, keine übersprungenen Ebenen, Landmarken `header`, `nav` mit `aria-label`, `main`, `footer`.
- Der Sprunglink nutzt `skipToContent()` in `app.ts`.
- Fokus immer sichtbar: `outline: 2px solid var(--focus)` mit 4 px Abstand. Auf dunklen Flächen `--focus` umsetzen. Fokusrahmen nur bei Sprungzielen mit `tabindex="-1"` ausblenden.
- Kontrast für Text mindestens 4,5 : 1, für große Schrift und Bedienelemente 3 : 1. Neue Farbpaare messen und in Kapitel 3 eintragen.
- Zielgröße mindestens 24 × 24 px; die Website nutzt 40 px (Galerie) und 48 px (Schaltflächen).
- Jedes Gemälde hat einen Alt-Text; Schmuck wie die Flagge hat `aria-hidden="true"`.
- Inhalte, die sich länger als 5 s von selbst bewegen, haben eine Pause.
- Bei 320 px Breite und bei 200 % Zoom gibt es keinen waagerechten Bildlauf.
- Trennzeichen aus CSS haben leeren Alternativtext.

## 9 Technik

- Angular mit Standalone-Komponenten, `OnPush`, Signals und `input()`; keine Zone.
- `styles.scss` enthält Variablen, Raster und gemeinsame Klassen. Komponentenstile regeln nur das eigene Layout und bleiben unter 4 kB.
- Schrift und Bilder liegen lokal. Keine externen Dateien, keine Tracking-, Analyse- oder KI-Dienste, keine Cookies, kein Speichern von Eingaben _(automatisch geprüft für eingebundene externe Dateien)_.
- Die Galerie- und Navigationstests liegen in `art-gallery.spec.ts` und `app.spec.ts`. Zeitabhängige Tests nutzen Fake-Timer.

## 10 Prüfablauf

Die automatisierte Browserprüfung läuft separat von `pnpm check`. Einmalig Chromium mit `pnpm exec playwright-core install chromium` installieren, dann den Entwicklungsserver mit `pnpm dev` starten. In einem zweiten Terminal `pnpm check:browser` ausführen. Der Standard ist `http://127.0.0.1:4311`; eine andere Adresse lässt sich mit `pnpm check:browser -- http://127.0.0.1:4312` angeben. Die Screenshots liegen in `outputs/browser/` und werden zusätzlich visuell geprüft.

Eine Änderung an Oberfläche oder Text ist fertig, wenn alle Punkte erledigt sind:

1. `pnpm check` ist grün (Formatierung, Handbuch-Prüfung, Typen, Tests, Build).
2. Browser: alle betroffenen Seiten bei 1440 × 1000, 1024 × 768, 768 × 1024, 390 × 844 und 320 × 720 angesehen, ohne waagerechten Bildlauf. Tastaturdurchgang mit Sprunglink und sichtbarem Fokus. Reduzierte Bewegung emuliert. axe-core ohne Verstöße. Bei Änderungen an der Galerie mindestens drei automatische Wechsel beobachtet.
3. Texte nach Kapitel 7, Bilder nach Kapitel 6 geprüft.
4. Dokumentation nachgezogen: `assets.md` bei Bildern und Schriften, `project.md` bei Entscheidungen, `ki-protokoll.md` mit Auftrag im Wortlaut, Modell und Prüfergebnissen, `validation.md` mit den Browserbeobachtungen, dieses Handbuch bei neuen Mustern.
5. Bericht trennt technische Prüfungen, Browserbeobachtungen und wissenschaftliche Abnahmen. Nichts davon wird als methodische Validierung ausgegeben.

## 11 Offene Entscheidungen

- Ob der Name mit dem Autor von 12 Axes abgestimmt wird, entscheidet Steven.
- Ob und wie die Website eine verantwortliche Person nennt, entscheidet Steven.
- Die Gestaltung von Test- und Ergebnisseiten steht aus. Dazu gehören die Einzelheiten, die Claude im Ablauf des Forschungsentwurfs festgelegt hat (Kapitel 4), etwa die ausgefüllte Schaltfläche nach vorn, die Pause von 350 ms und die Einleitung einmal je Block.
- „Wanderer über dem Nebelmeer“ kommt nur zurück, wenn die Hamburger Kunsthalle die Provenienz als unbedenklich einstuft.
