# T1: Technik- und Browserprüfung des Codex-Stands

Stand: 2026-10-03, Prüfzeit etwa 19:00–19:37 UTC. Prüfgegenstand ist der Codex-Stand `e9898fb423a3ba9fbe6387ed9215dbe83666aedc` im Worktree `t3code-794dd32c`. Dieser Bericht enthält technische Prüfungen und Browserbeobachtungen. Er enthält keine wissenschaftliche oder methodische Abnahme und ersetzt keine Prüfung mit Menschen.

## Kurzfassung

1. Technische Prüfungen sind grün: `pnpm check` (Exit 0, 79 Angular-Tests), 325 Python-Tests, 14 Node-Generatortests, Katalog- und Berichts-Bytevergleiche, `pnpm audit` ohne bekannte Schwachstellen. R ist nicht installiert; R-Tests liefen nicht.
2. Das vorhandene Skript `scripts/check-research-browser.mjs` war in dieser Umgebung in 0 von 5 Läufen vollständig grün. Ursache sind Wettläufe zwischen sehr schnellen Tastendrücken und dem Rendern. Der in `reports/loop/technical-focus-zoom-001.md` dokumentierte PASS ist hier nicht stabil wiederholbar.
3. Daraus folgt ein echter, aber eng begrenzter Anwendungsbefund: Bei Eingaben schneller als ein Renderzyklus kann ein Radio im DOM markiert bleiben, während der App-Zustand „Unberührt“ lautet. Mit 30 ms oder 80 ms Abstand zwischen Tasten trat das in 240 Versuchen nicht auf. Für menschliche Bedienung halte ich es für unwahrscheinlich, aber nicht ausgeschlossen.
4. Eigener Browserdurchgang in fünf Breiten und bei echtem 200-%-Tabzoom: kein waagerechter Bildlauf, axe-core ohne Verstöße, sichtbarer Fokus an allen geprüften Tabstopps, Sprunglink funktioniert, bei reduzierter Bewegung keine Übergänge oder Animationen.
5. Die Seite zeigt fehlende Vergleichsdaten ehrlich an. `cttresa` zeigt den Zurückhaltungshinweis ohne Zahlen. Gruppenvergleiche: 63 angezeigte und 111 zurückgehaltene Frage-Gruppen-Paare, passend zu `docs/reproduktion-life93-v2.md`. Eine stille Ersetzung habe ich nicht gefunden.
6. Datenschutz: Nach dem Laden der Seite gab es während vollständiger Durchgänge keine Netzwerkanfrage, keine externe Anfrage, keinen POST und keine Speicherung in Storage, Cookies, IndexedDB, Cache oder URL. Der Produktionsbuild enthält die Forschungsroute nicht. Die Git-Historie enthält keine Rohdaten, keine `data/local`-Dateien und keine erkennbaren Secrets.
7. Neu: Die lokalen T3-Checkpoint-Refs (`refs/t3/...`) speichern unversionierte, nicht ignorierte Dateien als Git-Objekte, darunter bereits Berichte paralleler Agenten.
8. Veraltete oder uneinheitliche Statusaussagen: Die Startseite nennt den Themenbericht „in Darstellungsprüfung“, die Projektseite „als Forschungsfassung gesichert“. Weitere Punkte stehen in Abschnitt 4.
9. Die Abnahme in LIFE-93 verlangt einen Playwright-Test, der Antwortdaten in Netzwerkanfragen ausschließt. Ein solcher automatischer Browsertest fehlt; vorhanden sind nur jsdom-Spione auf `fetch` und `Storage.setItem`.

## 1 Technische Prüfungen

Ausgangslage: Während meines `pnpm check` war `.prettierignore` im Worktree bereits verändert. Der Koordinator hat diese Änderung danach als Commit `75dbae4` (Elternteil `e9898fb`) festgehalten. `git diff --name-only e9898fb HEAD` nennt außer `reports/claude/` nur `.prettierignore`. Die Änderung ergänzt ausschließlich Ignoriereinträge für `reports/claude/…`, die es in `e9898fb` nicht gibt. Das Ergebnis lässt sich deshalb auf `e9898fb` übertragen. Einen frischen Checkout von `e9898fb` habe ich nicht angelegt.

| Prüfung | Befehl | Ergebnis | Log |
| --- | --- | --- | --- |
| Gesamtcheck | `pnpm check` | Exit 0 in 23,7 s: Prettier, Handbuch-Prüfung (9 Gemälde, 46 Quelldateien), Review-Schema (20 synthetische Fälle), Typecheck, Vitest 7 Dateien und 79 Tests, Produktionsbuild | `outputs/claude-t1/pnpm-check.log` |
| Python | `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/tests` | 325 Tests, OK, keine übersprungenen, 6,9 s; `git status` vorher und nachher gleich | `outputs/claude-t1/python-unittest.log` |
| R | nicht ausgeführt | `R` und `Rscript` nicht installiert | – |
| Node-Generatortests (zusätzlich) | `node --test` auf `reference-generator.test.mjs` und `group-reference-generator.test.mjs` | 14 von 14 bestanden | `outputs/claude-t1/node-test-mjs.log` |
| Katalogparität (zusätzlich) | `node web/src/app/policy-draft/verify-public-catalogue.mjs` | PASS: 43 Originalfragen, 315 Codebindungen | `outputs/claude-t1/verify-public-catalogue.log` |
| Berichtsbytes (zusätzlich) | `build-policy-v2-report.py --check`, `build-policy-group-report-v21.py --check` | beide Exit 0, SHA256 `470c73eb…` und `ecb731bc…` | `outputs/claude-t1/report-checks.log` |
| Abhängigkeiten | `pnpm audit --prod`, zusätzlich `pnpm audit` | jeweils „No known vulnerabilities found“, ohne Anmeldung | `outputs/claude-t1/pnpm-audit-*.log` |

Versionen: Node 24.21.0, pnpm 11.23.0, Python 3.14.7, Angular 22.2.1, playwright-core 1.62.1, axe-core 4.13.0, Chromium 151.0.7922.34. Die CI (`.github/workflows/ci.yml`) führt nur `pnpm install --frozen-lockfile` und `pnpm check` aus. Python-Tests laufen dort nicht.

## 2 Browserbeobachtungen

Alle Beobachtungen stammen aus Chromium 151 über playwright-core, headless, auf Linux. Breiten und Zoom sind emuliert. Physische Geräte habe ich nicht genutzt. Alle Auswahlen sind synthetische Klicks oder Tastendrücke.

### 2.1 Vorhandenes Skript `check-research-browser.mjs`

Ich habe das Skript unverändert gegen `http://127.0.0.1:4324` ausgeführt, mit Arbeitsverzeichnis `outputs/claude-t1`, damit seine Ausgaben dort landen.

| Lauf (UTC) | bestandene Bedingungen | Abbruch |
| --- | --- | --- |
| 19:08:36 | 5 von 9 | 1280 × 900, Zoom 2: Zeile 250, `input:checked` = 1 statt 0 nach „Auswahl zurücksetzen“ |
| 19:09:58 | 0 | 1440 × 1000, Zoom 1: Zeile 250, wie oben |
| 19:13:07 | 8 von 9 | 768 × 1024, Zoom 2: Zeile 355, „next from question 1“, Fokusrahmen `none` |
| 19:14:23 | 1 | 1024 × 768, Zoom 1: Zeile 250 |
| 19:14:34 | 2 | 768 × 1024, Zoom 1: Zeile 250 |

In den bestandenen Bedingungen meldete das Skript je 43 Fragen, 66 Fokusprüfungen und 5 axe-Läufe ohne Verstöße. Im ersten Lauf blieb bei 768 × 1024 eine axe-Regel `color-contrast` unvollständig, wie bei Codex dokumentiert. Echter 200-%-Zoom bestand im dritten Lauf für 1280 × 900, 1440 × 1000 und 1024 × 768.

### 2.2 Ursache des Abbruchs in Zeile 250

Ein instrumentierter Nachbau (`outputs/claude-t1/diag-reset4.mjs`, Log `diag-reset4.log`) protokolliert `change`-Ereignisse und jede Zuweisung an `input.checked`. In einem von 12 Läufen ergab sich diese Folge:

```text
217 keydown Space      217 change value=1
217 keydown ArrowDown  218 change value=2   218 write value=2 -> true
219 keydown ArrowUp    219 change value=1
228 keydown Enter (Zurücksetzen)            235 write value=2 -> false
```

Nach ArrowUp hält die App den Code 1. Bevor Angular rendert, kommt schon das Zurücksetzen. Angular schreibt `[checked]` nur, wenn sich der gebundene Wert gegenüber dem letzten Rendern ändert. Für Radio 1 war der zuletzt gerenderte Wert `false` und bleibt `false`. Radio 1 bleibt deshalb im DOM markiert, obwohl der Status „Unberührt“ lautet. Dieselbe Folge mit „Zur nächsten Frage“ statt Zurücksetzen lässt ein markiertes Radio in Frage 2 stehen, weil die Eingabeelemente über `track category.code` wiederverwendet werden. Das trat in meinem Grenzfalllauf in 3 von 10 und 6 von 10 Versuchen auf (`research/report.json`, `research/report-edge.json`).

Zeitabhängigkeit (`diag-race-timing*.json`, je 15 Versuche für Zurücksetzen und für Weiter):

| Browsermodus | CPU-Drosselung | Abstand zwischen Tasten | Abweichungen |
| --- | --- | --- | --- |
| headless shell | keine | 0 ms | 1 von 30 |
| headless shell | keine | 30 ms, 80 ms | 0 von 60 |
| headless shell | 6-fach | 0, 30, 80 ms | 0 von 90 |
| Chromium-Kanal | keine und 6-fach | 0, 30, 80 ms | 0 von 180 |

Mit üblichen Wartezeiten nach jedem Schritt trat keine Abweichung auf: In fünf vollständigen Durchgängen stimmten DOM und Status bei jeder Ankunft auf einer neuen Frage überein. Für den Fokusabbruch in Zeile 355 vermute ich eine verwandte Ursache: Nach „Zu den Fragen“ setzt `afterNextRender` den Fokus erst nach dem Rendern auf die H1, und das Skript drückt schon Tab. Diese Vermutung habe ich nicht gesondert instrumentiert.

### 2.3 Eigener Durchgang durch `/forschungsentwurf`

Skript `outputs/claude-t1/t1-research.mjs`, Bericht `research/report.json`, 19:16–19:18 UTC, reduzierte Bewegung emuliert. Je Breite wurden alle 43 Fragen mit einem wechselnden Muster bearbeitet: erste, letzte und mittlere Kategorie, Überspringen mit allen drei Gründen, Auswahl mit anschließendem Zurücksetzen, nur Weiter. Bei Frage 8 ging der Durchgang einmal zurück. Danach folgten der Abgleich der Ergebnisansicht, alle 26 Gruppenauswahlen, alle 173 `details` geöffnet, die Übersicht und Frage 1 mit geöffneten Quellen.

| Breite | Ergebniseinträge geprüft | Abweichungen | waagerechter Überlauf | axe-Verstöße (5 Ansichten) |
| --- | --- | --- | --- | --- |
| 1440 × 1000 | 43 | 0 | 0 px, keine Elemente außerhalb | 0 |
| 1024 × 768 | 43 | 0 | 0 px | 0 |
| 768 × 1024 | 43 | 0 | 0 px | 0 |
| 390 × 844 | 43 | 0 | 0 px | 0 |
| 320 × 720 | 43 | 0 | 0 px | 0 |

Weitere Beobachtungen je Breite: `lang="de"`, eine H1, Landmarken vorhanden. Der Ergebnisstatus enthält beide Statussätze aus LIFE-93, Phase 6, im Wortlaut, verglichen mit der Repository-Kopie `reports/loop/issue-2026-10-03.md`, Zeilen 178–179, nicht mit Linear selbst. Er enthält außerdem die Standardformel zur fehlenden Validierung. Wörter wie „Gesamtwert“, „Score“, „Punkte“ oder „passt zu“ kommen nicht vor. Beim Zurückgehen war die frühere Auswahl erhalten. Nach einem Wechsel der Studie wird die Gruppenauswahl geleert. Nach Bearbeiten einer Frage und Rückkehr bleiben Studie und Gruppe gewählt (`extra-report.json`).

Hinweis zur Darstellung: Die auf eine Nachkommastelle gerundeten Einzelanteile summieren sich je Frage auf 99,8 bis 100,1 %. Ein Rundungshinweis steht nicht auf der Seite.

### 2.4 Tastatur, Fokus und Sprunglink

- Der erste Tab erreicht „Zum Inhalt springen“. Der Link ist sichtbar, Enter setzt den Fokus auf `main#main-content`, der nächste Tab erreicht den ersten Link im Inhalt. Geprüft auf der Forschungsseite bei 1440 und 390 px und auf Start-, Projekt- und Methodikseite bei 1440 und 320 px.
- Vollständige Tab-Zyklen ohne Problem (`:focus-visible`, Rahmen mindestens 2 px, im Sichtbereich): Frage 1 mit 18 Stopps bei 1440 und 390 px, Ergebnisansicht mit gewählter Gruppe mit 97 Stopps bei 1440 und 320 px.
- Bei echtem 200-%-Zoom ergaben 25 Tabs je Fenstergröße nur sichtbare 2-px-Rahmen. Der einzige Treffer ohne Rahmen war `body` beim Übergang vom letzten Element zurück zur Browseroberfläche.
- Zurücksetzen und „Zur vorherigen Frage“ sind auf Frage 1 deaktiviert und deshalb nicht im Tabpfad. Das ist übliches Verhalten.

### 2.5 200-%-Zoom

Skript `t1-zoom.mjs` mit demselben Verfahren wie das vorhandene Skript (`chrome.tabs.setZoom`, Faktor 2, `devicePixelRatio` 2, CSS-Zoom 1). Fenster 1280 × 900, 1440 × 1000, 1024 × 768 und 768 × 1024 ergeben 640, 720, 512 und 384 CSS-px Breite. Gemessen wurden alle 43 Fragen einzeln, Frage 43 mit geöffneten Quellen, die Ergebnisse mit ESS8-Gruppe und allen geöffneten `details`, die Übersicht sowie Start-, Projekt- und Methodikseite. Überall 0 px Überlauf und kein Element außerhalb des Sichtbereichs. Bildschirmaufnahmen liegen in `outputs/claude-t1/zoom/`.

### 2.6 Reduzierte Bewegung

Bei `prefers-reduced-motion: reduce` gilt auf der Startseite `transition: none 0s` für Primärschaltfläche, Bilder und Kopflinks, ohne die Einstellung `background-color 0.16s`. Die Galerie blieb 20 s auf demselben Bild, die Schaltfläche lautete „Bildwechsel fortsetzen“. Ohne die Einstellung wechselte sie in 20 s zweimal (4 → 5 → 6 von 6). Die Forschungsseite hat in beiden Fällen kein Element mit Übergang oder Animation und `document.getAnimations()` ist leer.

### 2.7 Angesehene Bildschirmaufnahmen

Tatsächlich angesehen habe ich: `research/shots/1440-q1.png`, `320-q1.png`, `320-group-reference.png`, `1440-results-top.png`, `390-cttresa.png`, `1024-group-reference.png`, `320-results-top.png`, `768-overview.png`, `zoom/1280-z2-group-reference.png` und das Fehlerbild des ersten Skriptlaufs. Ich habe darin keinen abgeschnittenen Text und keine Überlappung gesehen. Bei 320 px stehen die drei Ansichtsschaltflächen untereinander. Die Statusleiste trennt Wörter, etwa „ver-fügbar“. Die übrigen Aufnahmen habe ich nicht einzeln angesehen.

### 2.8 Grenzfälle

Bericht `research/report-edge.json`, Breite 1024 × 768.

| Fall | Beobachtung |
| --- | --- |
| Keine Antwort, direkt zum Ergebnis | 43 × „Unberührt“ mit „Keine Auswahl und kein bewusstes Überspringen …“. Die 42 historischen Einzelreferenzen und der Hinweis zu `cttresa` erscheinen trotzdem. |
| Alle mit „Weiß nicht“ übersprungen | 43 × „Übersprungen“, Grund „Weiß nicht“, Text „Keine politische Aussage abgeleitet …“ |
| Alle mit „Keine Antwort geben“ | 43 × „Übersprungen“ mit diesem Grund |
| Alle erste bzw. alle letzte Kategorie | 43 × „Beantwortet“ mit der gewählten Originalkategorie. Keine Zusammenfassung, kein Gesamtwert, keine Richtungsbezeichnung. |
| `cttresa` (Frage 16, ESS10-SC B6) | Vor und nach der Antwort nur „Die historische Referenz … bleibt wegen unzureichender Basis oder Zellbesetzung zurückgehalten. Es werden keine Referenzzahlen angezeigt.“ Mit ESS9-Gruppe: „Kein passender Gruppenvergleich: … anderen Studie …“. Für ESS10-SC gibt es keine Gruppenstudie im Auswahlfeld. |
| Gruppen ohne Freigabe | ESS5: 8 Gruppen, 21 Paare mit Zahlen, 27 ohne. ESS8: 9 Gruppen, 30 und 60. ESS9: 9 Gruppen, 12 und 24. In keinem Hinweis ohne Freigabe steht eine Prozentzahl. Ohne gewählte Gruppe erscheint kein Gruppentext. |
| Schnelles Wechseln | 25 synchron ausgelöste Klicks auf Weiter führen genau zu Frage 26, 60 Klicks auf Zurück zu Frage 1. Mit Playwright-Klicks ohne Warten kam ein Klick nicht an (Frage 25); das schreibe ich der Testmechanik zu, nicht der App. 30 schnelle Ansichtswechsel: keine Fehler, Zählung unverändert. 15 schnelle Mausfolgen auf Radios mit Zurücksetzen: keine Abweichung. Schnelle Tastaturfolgen: siehe 2.2. |
| Neuladen | Vorher „3 beantwortet“, danach „0 beantwortet, 0 übersprungen, 43 unberührt“ und Frage 1. Das entspricht dem Hinweis auf der Seite. URL unverändert, Speicher leer. |
| Überspringgrund | Der Grund bleibt der Frage zugeordnet und erscheint beim Zurückgehen wieder. Nach einer Antwort wird er auf „Keine Angabe“ zurückgesetzt. Die nächste Frage beginnt mit „Keine Angabe“. |
| Browser-Zurück | Ansichtswechsel erzeugen keine Verlaufseinträge (`history.length` bleibt 2). Browser-Zurück verlässt deshalb die Seite, und die Antworten gehen verloren. Getestet habe ich nur die Verlaufslänge, nicht die Zurück-Taste. |

Die Seite zeigt fehlende Daten ehrlich an. In allen Fällen erscheint entweder eine Referenz mit Zahlen, ein ausdrücklicher Zurückhaltungshinweis, ein Hinweis auf eine andere Studie oder kein Gruppentext. Ersatzwerte wie 0 %, Mittelwerte oder Werte anderer Studien habe ich nicht gefunden. Die Prüfung erfolgte über DOM-Texte und Klassen, nicht über einen Zahlenabgleich mit `data/reference-*`; der gehört zu V1.

## 3 Datenschutz und Sicherheit

### 3.1 Netzwerk

Ich habe alle Anfragen des Browserkontexts sowie WebSocket-Frames in sechs vollständigen Durchgängen und den Grenzfällen protokolliert. Beim Laden entstehen 23 GET-Anfragen an `127.0.0.1:4324`: Dokument, Skripte, Stylesheet, Schrift und Vite-Module. Danach gab es bis zum Ende jedes Durchgangs keine einzige Anfrage. Externe Anfragen, Anfragen mit Body und andere Methoden als GET: keine. Der Vite-Entwicklungsserver öffnet einen HMR-WebSocket; die Seite sendete darüber keinen Frame. Diesen WebSocket gibt es nur im Entwicklungsserver. Den Produktionsbuild habe ich nicht im Browser geladen.

### 3.2 Speicherung

Nach den Durchgängen waren `localStorage` und `sessionStorage` leer. `document.cookie` und die Context-Cookies waren leer, `indexedDB.databases()` und `caches.keys()` ebenfalls. Service Worker: keine. Die URL blieb `http://127.0.0.1:4324/forschungsentwurf`. Auf Start-, Projekt- und Methodikseite galt in allen 25 Seitenaufrufen dasselbe für Storage und Cookies.

### 3.3 Produktionsbuild

`web/dist/politikprofil/browser` stammt aus meinem `pnpm check` (19:06 UTC). Die Zeichenketten „forschungsentwurf“, „Fragenentwurf“, „Diese Frage überspringen“, `REVIEWED_HISTORICAL`, `categoryShares`, `second_vote` und `ESS10SCe03_2` kommen nicht vor. `cttresa` und `pspwght` stehen nur im Methodik-Chunk als Fließtext. `localStorage`, `sessionStorage`, `indexedDB`, `sendBeacon`, `XMLHttpRequest` und `fetch(` kommen nicht vor. `document.cookie` steht nur in Angulars Bibliotheksfunktion `getCookie`. Im Entwicklungsserver (Port 4321) zeigt `/forschungsentwurf` „Seite nicht gefunden“. Der Build verlinkt GitHub-Seiten auf dem Zweig `research/life-93-night-20261003`. Diese Links lieferten um 19:32 UTC ohne Anmeldung HTTP 200, hängen aber am Fortbestand dieses Zweigs.

### 3.4 Git-Historie

Geprüft wurden alle Commits aus allen Refs einschließlich Reflog, darunter `refs/t3/...`, Tags und `origin`: zuerst 126 Commits gegen 19:10 UTC, Wiederholung der Pfad-, Secret- und `idno`-Suche mit 131 Commits um 19:36 UTC. Die Zahl stieg durch neue T3-Checkpoints.

- Unter `data/raw/` lag jemals nur die leere `.gitkeep` (Blob `e69de29…`). Unter `data/local/` lag nie eine Datei. `run.json` und `private`-Pfade kommen nicht vor.
- CSV-Dateien in der Historie: `data/inventar.csv`, `data/inventar.entwurf.csv`, deren Kopien in `reports/loop/packages/…` sowie `reports/loop/reviews/ITEM-FIRST-001-{methods,sources}.csv`. Ich habe nur Kopfzeile, Zeilen- und Bytezahl gelesen. Es sind Fragen- und Bewertungsinventare (Spalten wie `inventar_id`, `frage_id`, `wortlaut_de`), keine Befragtenzeilen.
- Die größten Blobs (bis 3,4 MB) sind Inventar-JSON und -CSV, Schema und Bilder.
- `idno` kommt nur als Spaltenname in Verträgen, Pipeline-Code, Tests und Dokumentation vor, etwa `"id_column": "idno"`. Das gilt auch für die Auftragsdateien und die T3-Checkpoints von `reports/claude/kontrollrechnung/` (geprüft nur die Zeilen mit `idno`, Ziffernfolgen maskiert). Werte habe ich nicht gefunden. Die öffentlichen Referenz-JSON unter `data/reference-v2` und `data/reference-groups-v21` haben höchstens 17 Einträge je Liste, also keine Personenlisten.
- Secret-Muster (private Schlüssel, GitHub-, OpenAI-, Anthropic-, AWS-, Slack- und Google-Token, JWT, Zuweisungen an `api_key`, `secret`, `password` oder `token`) in allen Commits: keine Treffer. Dateinamen wie `.env`, `*.pem`, `*.key` oder `id_rsa`: keine.
- `.gitignore` schließt `data/raw/**`, `data/local/` und `outputs/` aus, geprüft mit `git check-ignore`. `data/raw/` und `data/local/` habe ich nicht geöffnet und nicht aufgelistet.

### 3.5 T3-Checkpoint-Refs

Die lokalen Refs `refs/t3/orchestration-v2/checkpoints/…` (47) und `refs/t3/checkpoints/…` (17) enthalten Bäume mit unversionierten Dateien des Worktrees. Nur dort, in keinem Zweig, stehen derzeit `reports/claude/agenten/R4-profilform.md`, `T3-thread-nutzernachrichten.md`, `V2-quellen-konstrukte-fairness.md`, `V2-urteil.json` sowie `reports/claude/kontrollrechnung/bericht.md`, `kontrolle.py` und `vergleich.json`. Ignorierte Pfade wie `data/raw/`, `data/local/` und `outputs/` fand ich in keinem Checkpoint. Folge: Jede private Zwischendatei an einem nicht ignorierten Ort wird zum Git-Objekt, auch ohne Commit. Ob `refs/t3` jemals gepusht wird, kann ich lokal nicht feststellen. Unter `refs/remotes/origin` stehen nur Zweige. Inhalte der fremden Dateien habe ich nicht geprüft.

### 3.6 Workflows und CodeRabbit

`.github/workflows/ci.yml` hat `permissions: contents: read`, keine Secrets und keine Pfade unter `data/raw` oder `data/local`; er führt nur `pnpm check` aus. `.coderabbit.yaml` (gelesen bis Zeile 60) fordert für `pipeline/**`, keine Rohdaten in Review-Ausgaben zu kopieren. Rohdaten liegen nicht im Repository und sind CodeRabbit damit nicht zugänglich.

### 3.7 Automatischer Netzwerktest

Die Abnahme in LIFE-93 (Repository-Kopie `reports/loop/issue-2026-10-03.md`, Zeile 183) verlangt einen Playwright-Test, der sicherstellt, dass keine Netzwerkanfrage Antwortdaten enthält. `check-research-browser.mjs` protokolliert keine Anfragen. `policy-draft.spec.ts` (Zeilen 284–296 und 452–496) beobachtet in jsdom nur `fetch` und `Storage.setItem`. Nicht abgedeckt sind `XMLHttpRequest`, `sendBeacon`, WebSocket, Bild-Beacons, Cookies und IndexedDB. Meine Beobachtung in 3.1 und 3.2 ersetzt diesen fehlenden automatischen Test nicht.

## 4 Startseite, Projektseite und Methodikseite (Port 4321)

Skript `t1-pages.mjs`, Bericht `pages/report.json`, 19:20–19:22 UTC. Geprüft wurden `/`, `/projekt`, `/methodik`, `/forschungsentwurf` und `/gibt-es-nicht` in fünf Breiten, jeweils mit allen `details` geöffnet und einmal ganz durchgescrollt: 0 px Überlauf, axe ohne Verstöße und ohne unvollständige Regeln, keine externe Anfrage, keine Laufzeitfehler, alle Bilder mit `alt`, Titel nach Handbuch. Tab-Zyklen ohne Problem: Startseite 18, Projektseite 48, Methodikseite 34 Stopps bei 1440 und 320 px. Bei 200 % Zoom: siehe 2.5.

Statusaussagen, verglichen mit `docs/reproduktion-life93-v2.md` und den Entscheidungsdateien in `reports/loop/`:

| Fundstelle | Aussage | Befund |
| --- | --- | --- |
| Startseite, „Stand der Arbeit“, Analyse und Auswertung (`web/src/app/pages/home/home.html`, Zeile 119) | „Themenbericht in Darstellungsprüfung.“ | Veraltet und widersprüchlich. Laut `reports/loop/RESULTS-V2-PRESENTATION-001-entscheidung.md` urteilen beide Rollen `ACCEPTED_BOUNDED`. Die Projektseite sagt „Breiter Themenbericht: Als Forschungsfassung gesichert“. |
| Start- und Projektseite, Faktenlisten | „Fünf getrennte Einzelstudienläufe ausgeführt.“ und „42 historische Einzelreferenzen“ | Unvollständig. Die drei Gruppenläufe und die 63 veröffentlichten Gruppenpaare fehlen in den Faktenlisten. Fließtext und „Nächster Arbeitsschritt“ nennen die Gruppenreferenzen. |
| Start- und Projektseite, KI-Prüfungen | „Zwei getrennte Codex-Rollen haben die historischen Einzelreferenzen begrenzt geprüft.“ | Unvollständig. Die Methodikseite nennt auch zwei begrenzte Ergebnisprüfungen der Gruppenreferenzen. |
| Start-, Projekt- und Methodikseite | Darstellung der Gruppenreferenzen „wird noch geprüft“ bzw. „bleiben zu prüfen“ | Mehrdeutig. Laut `GROUP-PRESENTATION-V21-001-entscheidung.md` wurde eine begrenzte Darstellungsprüfung durch Codex angenommen. Offen sind die menschliche Prüfung und die Freigaben. |
| `web/src/index.html`, Meta-Beschreibung (159 Zeichen) | „… ein Profil politischer Einstellungen mit mehreren Dimensionen bilden soll“ | Möglicherweise überholt. `docs/project.md` nennt Zahl und Struktur der Dimensionen offen, und die aktuelle Fassung hat bewusst keine gemeinsamen Dimensionen. Das ist eine Produktentscheidung für Steven. |

Die Vorlagen und Komponenten von Start-, Projekt- und Methodikseite sowie `web/src/index.html` wurden zuletzt in `320e632` geändert (2026-10-03 18:05 +0200). Die Gruppen- und Darstellungsentscheidungen kamen danach. Statusleiste, Fußzeile, Standardformel und „In Vorbereitung“ entsprechen Kapitel 7.7 des Handbuchs. Einen sichtbaren Teststart gibt es nicht.

## 5 Nicht geprüft und Grenzen

- Keine physischen Smartphones, kein Firefox, kein WebKit, kein Screenreader, kein Touch, kein Pinch-Zoom, kein Zoom über das Browsermenü, kein Hochkontrastmodus.
- axe-core prüft nur einen Teil von WCAG 2.2 AA. Eine vollständige WCAG-Prüfung fand nicht statt.
- Den Produktionsbuild habe ich nur statisch durchsucht, nicht ausgeliefert und nicht im Browser geöffnet. Die Seiten auf Port 4321 liefen in der Entwicklungskonfiguration.
- `pnpm check:browser` (`scripts/check-browser.mjs`) habe ich nicht ausgeführt, weil es nach `outputs/browser/` schreibt. Abschnitt 4 deckt dieselben Punkte ab.
- Zahlenwerte der Referenzen habe ich nicht mit `data/reference-*` abgeglichen (Auftrag V1). Inhaltliche Richtigkeit von Fragen, Übersetzungen, Rubriken und Fairness habe ich nicht geprüft.
- LIFE-93 habe ich nur in der Repository-Kopie gelesen, nicht live in Linear.
- Die Ursache des Fokusabbruchs in Zeile 355 ist eine Vermutung.
- Die Häufigkeiten der Wettläufe beruhen auf kleinen Stichproben auf einer Maschine.
- Kein frischer Checkout von `e9898fb`; Begründung der Übertragbarkeit in Abschnitt 1.
- Keine Verständlichkeitsprüfung mit Menschen und keine wissenschaftliche Abnahme. Diese technischen Ergebnisse sind keine methodische Validierung.

## 6 Vorschläge (nicht umgesetzt, nicht getestet)

1. Radiozustand robust binden: zum Beispiel nach jeder Zustandsänderung `checked` aller Radios aus dem Zustand setzen, Angulars `RadioControlValueAccessor` nutzen oder die Eingabeelemente je Frage neu erzeugen, etwa mit `track` über Frage-ID und Code. Die letzte Variante behebt nur die Übertragung auf die nächste Frage.
2. `check-research-browser.mjs` nach Tasten- und Ansichtswechseln auf den gerenderten Zustand warten lassen, etwa auf die Statuszeile oder den H1-Fokus, und nur wiederholt grüne Läufe als Beleg verwenden.
3. Einen Playwright-Netzwerktest nach LIFE-93 ergänzen: alle Anfragen, Bodies und WebSocket-Frames nach dem Laden protokollieren, dazu Storage, Cookies und IndexedDB.
4. Statuszeilen auf Start- und Projektseite an die Entscheidungen vom 3. Oktober 2026 angleichen und die Meta-Beschreibung mit Steven abstimmen.
5. Private Zwischendateien nur unter ignorierten Pfaden ablegen, solange T3-Checkpoints nicht ignorierte Dateien erfassen.

## Anhang

### Tatsächlich geöffnete Quellen (UTC, ungefähr)

- 19:03: `reports/claude/auftraege/T1-technik-browser.vollstaendig.md`, `docs/handbuch.md` (vollständig), `docs/reproduktion-life93-v2.md` (vollständig), `docs/project.md` (vollständig), `AGENTS.md` (aus dem Kontext)
- 19:04–19:06: `package.json`, `web/package.json`, `web/angular.json` (bis Zeile 150), `.gitignore`, `.github/workflows/ci.yml`, `web/src/app/app.routes.ts`, `research-preview.routes*.ts`, `app.config.ts`, `research-preview/policy-preview.ts`, `policy-draft/policy-draft.ts`, `policy-draft.html`, `policy-source-details.{html,ts}`, `historical-reference.ts` (bis Zeile 400), `group-reference.ts` (bis Zeile 120), `research/policy-profile.ts`, `scripts/check-research-browser.mjs` (vollständig), `scripts/check-browser.mjs` (bis Zeile 60), Ausschnitte aus `web/src/styles.scss` und den SCSS-Dateien in `policy-draft/`
- 19:10–19:12: `reviewed-historical-references.ts` (Anfang und Treffer zu `cttresa`), Kopfzeilen der vier CSV-Dateien aus 3.4
- 19:23–19:27: `reports/loop/technical-focus-zoom-001.md` (bis Zeile 60), `RESULTS-V2-PRESENTATION-001-entscheidung.md` (erste 2500 Zeichen), `GROUP-PRESENTATION-V21-001-entscheidung.md` (erste 1500 Zeichen), `reports/loop/issue-2026-10-03.md` (Kopf und Zeilen 176–184), `policy-draft.spec.ts` (Zeilen 278–300 und 450–500), `.coderabbit.yaml` (bis Zeile 60), `web/dist/politikprofil/browser/index.html`
- 19:32: `https://github.com/hernstev97/12axes-germany` und zwei Unterseiten, nur HTTP-Status abgefragt (200)
- Indirekt: npm-Registry über `pnpm audit`

### Ausgeführte Befehle (Kurzform)

`git log`, `git status`, `git diff`, `git rev-list --all --reflog`, `git ls-tree -r` über alle Commits, `git grep` über alle Commits (`idno`, Secret-Muster), `git cat-file --batch-check`, `git for-each-ref`, `git check-ignore`; `pnpm check`; Python-Unittests; `node --test`; `verify-public-catalogue.mjs`; beide Bericht-Builder mit `--check`; `pnpm audit --prod` und `pnpm audit`; `pnpm ls -r --depth 0`; Server `pnpm --filter politikprofil start --configuration research --host 127.0.0.1 --port 4324` und `… start --host 127.0.0.1 --port 4321`; fünfmal `node ../../scripts/check-research-browser.mjs http://127.0.0.1:4324`; eigene Skripte `t1-research.mjs`, `t1-pages.mjs`, `t1-zoom.mjs`, `t1-extra.mjs`, `diag-reset*.mjs`, `diag-race-timing*.mjs` sowie ein Inline-Skript für die Bewegungseinstellungen (`reduced-motion.log`); `grep` im Produktionsbuild; `curl` (nur HTTP-Status). Zwei kurzlebige Pfadlisten unter `/tmp` habe ich sofort gelöscht. Nach dem Ende habe ich nur meine vier eigenen Prozesse mit SIGTERM beendet: die beiden `ng serve` mit den PIDs 765673 und 765361 und ihre `pnpm`-Eltern 765609 und 765305. Danach waren die Ports 4321 und 4324 frei (`ss -ltnp`). Meine Chromium-Profile unter `outputs/claude-t1/` habe ich gelöscht. Alle Protokolle, Skripte und Bilder liegen unter `outputs/claude-t1/` (ignoriert). Quellcode und Dokumente habe ich nicht verändert.

### Modell

Laut Laufzeitumgebung (Systemangabe dieser Sitzung): Claude Opus 5.5, Modell-ID `claude-opus-5-5[1m]`.
