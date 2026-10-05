# Prüfung der Repository-Grundlage

Stand: 2026-10-03. Diese Prüfung betrifft die technische und gestalterische Grundlage. Sie ist keine wissenschaftliche Abnahme des geplanten Tests.

## Technische Checks

`pnpm check` prüft Formatierung, strenge TypeScript- und Angular-Templates, zwei Navigationstests und den Produktionsbuild. Die Tests prüfen Titel, Fokusführung und aktive Navigation nach einem Seitenwechsel sowie die Rückkehr aus einer unbekannten Adresse.

Die CodeRabbit-Konfiguration wurde gegen das offizielle [Konfigurationsschema](https://coderabbit.ai/integrations/schema.v2.json) validiert. Die Review-Einstellungen richten sich nach der [CodeRabbit-Dokumentation](https://docs.coderabbit.ai/reference/configuration). Ein tatsächlicher CodeRabbit-Review auf GitHub und ein gehosteter CI-Lauf haben noch nicht stattgefunden.

Alle elf Skills wurden mit der persönlichen Skills CLI eingebunden. Das Manifest enthält alle Verzeichnisse mit `SKILL.md` im zentralen Repository; die kopierten Dateien stimmen bytegenau mit der Quelle überein. Der Git-Ausschluss für Rohdaten, lokale Daten, Umgebungsdateien und lokale Screenshots wurde geprüft.

## Browserbeobachtung

Die erste Desktop-Prüfung lief in der gemeinsamen T3-Vorschau. Deren Größenwechsel brach mehrfach wegen einer verlorenen Browser-Verbindung ab. Nachdem auch `preview_open` keinen erreichbaren Automation-Host mehr meldete, folgte ein lokaler Headless-Lauf mit Playwright und Chromium 153.0.8010.12.

| Ansicht            | Breite × Höhe | Ergebnis  |
| ------------------ | ------------- | --------- |
| Desktop            | 1440 × 1060   | bestanden |
| Tablet             | 768 × 1024    | bestanden |
| Smartphone         | 390 × 844     | bestanden |
| Kleines Smartphone | 320 × 720     | bestanden |

In allen Ansichten wurden Startseite, Projektseite, Fragmentlinks, Lizenzdatei, unbekannte Adresse und Rückkehr zur Startseite geprüft. Der Sprunglink funktioniert per Tastatur. Bei einem Seitenwechsel aktualisieren sich Titel, aktive Navigation und Fokus. Unterseiten lassen sich direkt laden und neu laden.

Die geprüften Seiten haben kein horizontales Überlaufen. Bild und lokale Schriftdateien laden. Es wurden keine Laufzeitfehler, fehlgeschlagenen Anfragen oder Anfragen an externe Dienste beobachtet. Die App legte keine Einträge in LocalStorage oder SessionStorage an.

Desktop und Smartphone wurden zusätzlich anhand der Screenshots visuell geprüft. Die Screenshots und der Browserbericht liegen lokal in `outputs/`, das von Git ausgeschlossen ist. Die Prüfung ersetzt keinen Lauf auf einem physischen Smartphone.

## Offen

Fragen, Modell, Vergleichsdaten und wissenschaftliche Prüfregeln sind noch nicht umgesetzt. Auch die unabhängigen methodischen KI-Erstbewertungen, verbindliche Review-Freigaben und die Verständlichkeitsprüfung stehen aus. Das bleibt der nächste Arbeitsschritt nach dieser Grundlage.

## Überarbeitung der Gestaltung (2026-10-03)

Diese Prüfung betrifft die überarbeitete Gestaltung, die Texte, die Bilder und das neue Handbuch. Sie ist keine wissenschaftliche Abnahme.

### Technische Checks

`pnpm check` ist grün: Formatierung, Handbuch-Prüfung (`scripts/check-handbuch.mjs`: 9 Gemälde, Dateien, Nachweise, Sperrmuster, Farben, Schrift, Seitentitel), strenge Typen, 9 Tests und Produktionsbuild ohne Budget-Warnung. Neu sind sieben Galerie-Tests mit Fake-Timern, darunter mehrere Wechsel hintereinander, reduzierte Bewegung, Anhalten und Fortsetzen, das dauerhafte Anhalten bei Tastaturfokus und die Darstellung eines einzelnen Bildes ohne Steuerung. `scripts/encode-artwork.sh` erzeugt die vorhandenen WebP-Dateien aus den Originalen byte-genau neu (geprüft an „Blick auf Dresden bei Sonnenuntergang“). Die geänderte `.coderabbit.yaml` ist gegen das offizielle Schema gültig. Ein gehosteter CI- oder CodeRabbit-Lauf hat nicht stattgefunden.

### Browserbeobachtung

Lokaler Headless-Lauf mit Playwright 1.62.1 und Chromium gegen den Entwicklungsserver. Geprüft wurden Startseite, Projektseite und eine unbekannte Adresse bei 1440 × 1000, 1024 × 768, 768 × 1024, 390 × 844 und 320 × 720.

- axe-core (WCAG 2.0 bis 2.2 A/AA und Best Practices): keine Verstöße in allen 15 Kombinationen.
- Kein waagerechter Bildlauf, keine Laufzeitfehler, keine fehlgeschlagenen Anfragen, keine Anfragen an externe Dienste, keine Einträge in LocalStorage oder SessionStorage, keine defekten Bilder.
- Der Sprunglink führt auf `/projekt` zum Inhalt, ohne die Seite zu wechseln. Links im Inhaltsverzeichnis setzen den Fokus auf den Zielabschnitt. Die Primärschaltfläche hat einen sichtbaren Fokusrahmen in `--ink`.
- Die Galerie wechselte in 26 Sekunden dreimal. Bei emulierter reduzierter Bewegung wechselte sie in 10 Sekunden nicht; die Schaltfläche hieß „Bildwechsel fortsetzen“.
- Desktop, Tablet und Smartphone wurden zusätzlich anhand von Screenshots visuell geprüft, ebenso alle Galeriebilder im Passepartout.

Vier getrennte Prüfagenten (Gestaltung, Barrierefreiheit, Code, Dokumentation) mit je zwei Gegenprüfungen haben die Zwischenstände geprüft. Ihre bestätigten Befunde sind umgesetzt, darunter ein Fehler, durch den die Galerie nach dem ersten Wechsel stehen blieb. Das sind KI-Reviews und Browserbeobachtungen, keine methodische Prüfung. Ein Lauf auf einem physischen Smartphone fehlt.

Beim abschließenden Codex-Review wurden `pnpm check` und `git diff --check` erneut erfolgreich ausgeführt. Die vorhandenen Desktop- und Smartphone-Screenshots wurden visuell geprüft. In der T3-Vorschau wurden Startseite, Projektseite und der Fragmentlink zum Arbeitsstand geprüft; der Link setzte den Fokus auf `stand`. Beim Größenwechsel verlor die Vorschau wiederholt die Verbindung. Ein vollständiger erneuter Browserlauf in allen Breiten fand in diesem Review deshalb nicht statt; dafür gelten die oben dokumentierten Beobachtungen aus dem vorherigen Lauf.

## Breitenkorrektur der vorhandenen Seiten, 3. Oktober 2026

Start- und Projektseite beschreiben jetzt das breite Ziel, den historischen Neunerbestand und bekannte frühere Dateneinsicht. Bestehende Gestaltung, Navigation und Bilder bleiben erhalten; kein neuer Fragebogen oder Teststart. `pnpm check`036 exit0. In der T3-Vorschau beide Seiten bei1440×1000,1024×768,768×1024,390×844 und320×720: kein horizontaler Überlauf, je eine H1, keine defekten Sprungfragmente und axe4.13.0 ohne Verstöße oder unvollständige Prüfungen. Vier Desktop-/Smartphone-Screenshots visuell gelesen, Schrift/Gemälde und Textfluss passend. Einzelbelege in [breadth-website-technical.json](../reports/loop/breadth-website-technical.json).

Sichtbarer Tastaturfokus bleibt ungeprüft: Die verfügbare Vorschau meldet `document.hasFocus=false`. Echter200%-Zoom bleibt ebenfalls ungeprüft; frühere wirkungslose Vorschau-Tastenkürzel sind keine Abnahme. Unveränderte Galerie-/Bewegungsprüfungen wurden nicht wiederholt. Kein vollständiger WCAG-, Geräte-, Verständlichkeits-, Design- oder Methodenabschluss. Neue Inhaltsprüfung der Texte steht aus.

## Breitentexte, gezielte Korrektur1

3. Oktober2026: WB-001/002/003 unabhängig gezielt geschlossen; aktueller Stand pnpm check038 exit0. Beide Seiten bei fünf festgelegten CSS-Breiten erneut per DOM auf Überlauf, H1 und Originalschrift geprüft, zwei aktuelle Screenshots visuell gelesen. [Technikbeleg](../reports/loop/breadth-website-correction-technical.json). Frühere axe0-Beobachtung nicht als neuer Lauf ausgegeben; keine Änderung an Bedienung/Struktur/Stilen. Echter200%-Zoom und sichtbarer Tastaturfokus weiterhin ungeprüft, keine vollständige Handbuch- oder WCAG-Abnahme.

3.Oktober2026, Methodikseite: normale begrenzte Erstprüfung ohne Blocker, Quellenlinkhinweise umgesetzt. Check042exit0/31Tests/Build vor letzter sachgleicher Wortumbruchkorrektur. Neue Seite bei5CSS-Breiten: anfänglich320px Überlauf, gezielt korrigiert; final keinÜberlauf gegenclientWidth,1H1,lokaleSchrift,axe4.13ohneVerstöße/unvollständigePrüfungen. BeideScreenshots visuell geprüft. EchterBrowser-Ankersprung führt aktivemElement zumAbschnitt; Unitfixture prüftURL/Titel statt nichtinitialisiertemRouterScroller. [Beleg](../reports/loop/methodology-page-technical.json). SichtbarerKeyboardfokus/echter200%-Zoom/Human-WCAG-Gesamtabnahme bleibenoffen.

## 3. Oktober 2026: sichtbarer Fokus und echter 200-%-Tabzoom

Der [technische Nachtrag](../reports/loop/technical-focus-zoom-001.md) ersetzt die früheren offenen Fokus-/Zoomangaben nur für seinen ausgeführten Umfang: Forschungsroute in neun Bedingungen mit allen 43 Fragen, Übersicht und Ergebnissen. 594 native Fokusprüfungen, 441 Überlaufprüfungen, 45 axe-Läufe ohne Verstöße; eine Kontrastregel unvollständig, gezielte Farb-/Sichtprüfung dokumentiert. Startseite, Projektstand und Methodik: 27 weitere Ansichten, 54 Fokusprüfungen und 27 axe-Läufe ohne Verstöße oder unvollständige Regeln. Reset-Fokus und Gruppenquellen-Rahmen korrigiert; native Aufnahmen gesichtet. Kein vollständiger WCAG-, physischer Geräte-, Menschen-, Design- oder Methodenabschluss.

## 4. Oktober 2026: Produktionsbuild, echter 200-%-Zoom der öffentlichen Seiten, weitere Browser-Engines

Geprüft von Claude im Auftrag von Steven. Technische Prüfungen und Browserbeobachtungen, keine wissenschaftliche Abnahme.

- **Produktionsbuild.** `ng build` (Konfiguration production), lokal ausgeliefert mit `node scripts/serve-dist.mjs web/dist/politikprofil/browser 4320`. `node scripts/check-browser.mjs http://127.0.0.1:4320`: vier Seiten in fünf Breiten, Reflow, Tastatur und Galerie bestanden. Die Route `/forschungsentwurf` zeigt im Produktionsbuild „Seite nicht gefunden“ und keinen Fragenentwurf.
- **Echter 200-%-Zoom der öffentlichen Seiten.** `node scripts/check-public-zoom.mjs http://127.0.0.1:4320`, Chromium 151 mit `chrome.tabs.setZoom` über eine lokale Testerweiterung. Startseite, Projektseite, Methodikseite und Fehlerseite bei 1440, 1280, 1024 und 768 Pixeln Fensterbreite, also 720 bis 384 CSS-Pixeln: kein waagerechter Bildlauf über die ganze Seitenhöhe, axe ohne Verstoß, Sprunglink, jeder Tab-Stopp sichtbar mit 2-px-Rahmen im sichtbaren Bereich (13, 43, 34 und 4 Stopps). Keine externe Anfrage, kein Laufzeitfehler.
- **Forschungsentwurf in weiteren Engines.** Forschungsbuild (`ng build --configuration research`) lokal ausgeliefert, `node scripts/check-research-engines.mjs http://127.0.0.1:4321` mit `FIREFOX_EXECUTABLE` auf einen vorhandenen Firefox-155-Build. Chromium 151 und Firefox 155, jeweils 1440 × 1000 und 390 × 844 (Chromium zusätzlich mit Touch- und Mobil-Emulation): alle 62 Fragen, Antwortänderung, Zurücksetzen, Überspringen mit Grund, Zurückgehen ohne Antwortverlust, Ergebnisansicht mit 59 Referenzen und 406 Bereichen, markierte eigene Antwort je beantworteter Referenz, Gruppenvergleich mit Bereichen und Hinweis, Restgruppe „Andere Partei (heterogener Rest)“, Übersicht und Sprung zur letzten Frage. Fokus nach dem Wechsel zwischen Fragen, nach dem Zurücksetzen, nach dem Wechsel zu Ergebnis und Übersicht und nach dem Sprung zur letzten Frage auf der jeweiligen Überschrift. Mit der Tabulatortaste erreicht der Fokus ein Antwortfeld mit sichtbarem 2-px-Rahmen (`:focus-visible`). axe ohne Verstoß, kein Überlauf, keine Anfrage und kein WebSocket-Frame nach dem Laden. Schreibzugriffe auf `localStorage`, `sessionStorage`, `document.cookie`, IndexedDB, Cache Storage und Service Worker werden ab dem ersten Skript mitgeschrieben. An vier Prüfpunkten (Frage 1, Mitte des Ablaufs, Ergebnis mit Gruppenvergleich, Ende) gab es keinen Schreibzugriff, alle Speicher waren leer, alle Schnittstellen waren prüfbar. Zuweisungen der Form `localStorage.x = …` erfasst die Mitschrift nicht, wohl aber den Zustand an den Prüfpunkten. Alle bestanden. Erste Fassung des Skripts: T2-F01 und T2-F02 (Codex) bemängelten zu schwache Fokus- und Speicherprüfung, korrigiert am 4. Oktober 2026.
- **WebKit nicht prüfbar.** Der WebKit-Build für playwright-core 1.62.1 braucht Systembibliotheken, die auf diesem Rechner fehlen (ICU 74, flite, libxml2.so.2, libjxl 0.8). Ihre Installation wäre eine Systemänderung. Safari und WebKit bleiben ungeprüft.
- **Nicht durchführbar.** Physische Smartphones, Touch auf echten Geräten, Screenreader mit Menschen, Hochkontrastmodus. Browser-Emulation ersetzt diese Prüfungen nicht.

## 5. Oktober 2026: neue Frageansicht im Forschungsentwurf

Geprüft von Claude im Auftrag von Steven. Technische Prüfungen und Browserbeobachtungen, keine wissenschaftliche Abnahme und keine Designfreigabe.

- **Technische Prüfungen.** `pnpm check` mit Exit 0: Formatierung, Handbuch-Prüfung, Review-Schema, Typen, 122 Tests (neun neue zum automatischen Wechsel) und Build ohne Budgetwarnung.
- **Chromium mit echtem Zoom.** `node scripts/check-research-browser.mjs http://127.0.0.1:4314`, Chromium 151, neun Bedingungen (1440, 1024, 768, 390 und 320 Pixel bei 100 %, 1280, 1440, 1024 und 768 Pixel bei 200 % Tabzoom). Alle 62 Fragen, Ergebnis, Gruppenvergleich und Übersicht nur mit der Tastatur. Der Schalter für den automatischen Wechsel wird zu Beginn mit der Leertaste ausgeschaltet. Auf einer neu geladenen Seite gilt in jeder Bedingung: Pfeiltasten wählen ohne Wechsel, Leertaste und Mausklick wechseln zur nächsten Frage, und der Fokus steht danach sichtbar auf „Frage n von 62“. Insgesamt 783 Fokusprüfungen, 621 Überlaufprüfungen ohne waagerechten Bildlauf und 54 axe-Läufe ohne Verstoß. Ein axe-Lauf (768 Pixel, Quellen aufgeklappt) meldete die Kontrastregel als unvollständig, nicht als Verstoß. Eine gezielte Wiederholung im selben Zustand ergab keinen unvollständigen Befund. Nach dem Laden gab es keine Anfrage und keinen WebSocket-Frame, und es wurde nichts gespeichert.
- **Chromium und Firefox.** Forschungsbuild, `node scripts/check-research-engines.mjs http://127.0.0.1:4321` mit Firefox 155 aus dem Playwright-Zwischenspeicher. Chromium 151 und Firefox 155 jeweils bei 1440 × 1000 und 390 × 844 bestanden: der vollständige Ablauf wie am 4. Oktober 2026, zusätzlich der automatische Wechsel per Klick und Leertaste und keine Wirkung der Pfeiltasten. WebKit startet weiterhin nicht (fehlende Systembibliotheken).
- **Gefundene und behobene Fehler.**
  - Chromium löst für die Leertaste auf einem schon gewählten Radio kein Klick-Ereignis aus. Deshalb bestätigen Leertaste und Eingabetaste die gewählte Antwort jetzt selbst.
  - Bei 320 Pixel Breite ragte Frage 8 mit „Kinderbetreuungsmöglichkeiten“ 33 bis 35 Pixel über den Rand. Der Fragetext hat jetzt volle Breite und unter 640 Pixel Silbentrennung. Eine Nachprüfung aller 62 Fragen bei 320 und 390 Pixel ergab keinen Überlauf.
- **Sichtprüfung.** Aufnahmen bei 1440, 390 und 320 Pixel angesehen: Frage mittig, Karte mit Oberkante, gewählte Antwort hervorgehoben, 0–10-Liste ab 640 Pixel in einer Zeile mit Endbeschriftungen, darunter untereinander.
- **Nicht durchführbar.** Physische Smartphones, Screenreader mit Menschen, Hochkontrastmodus auf echten Geräten und Safari bzw. WebKit. Ob der automatische Wechsel Menschen hilft oder stört, zeigt erst ein Test mit Menschen.

### Nachtrag am selben Abend: Startbildschirm, Einleitungsbildschirme, kompakter Fragebildschirm

Nach Stevens zweiter Vorgabe neu geprüft. Technische Prüfungen und Browserbeobachtungen, keine wissenschaftliche Abnahme und keine Designfreigabe.

- **Technische Prüfungen.** `pnpm check` mit Exit 0: 129 Tests, darunter Start, Einleitungen und automatischer Wechsel, Build ohne Budgetwarnung.
- **Chromium mit echtem Zoom.** `node scripts/check-research-browser.mjs http://127.0.0.1:4314`, Chromium 151, dieselben neun Bedingungen. Nur mit der Tastatur: Startbildschirm, 24 Einleitungsbildschirme, alle 62 Fragen, Ergebnis, Gruppenvergleich und Übersicht. Auf einer neu geladenen Seite gilt: Pfeiltasten wählen ohne Wechsel; Leertaste und Mausklick wechseln zur nächsten Frage; nach der letzten Frage eines Blocks folgt dessen Einleitung. Alle neun Bedingungen bestanden: 1026 Fokusprüfungen, 846 Überlaufprüfungen ohne waagerechten Bildlauf, 72 axe-Läufe ohne Verstoß. Wie am 3. Oktober 2026 meldet ein axe-Lauf bei 768 Pixel mit aufgeklappten Quellen die Kontrastregel als unvollständig, nicht als Verstoß. Zwei gezielte Nachstellungen dieses Zustands ergaben keinen unvollständigen Befund. Nach dem Laden gab es keine Anfrage, und es wurde nichts gespeichert.
- **Chromium und Firefox.** Forschungsbuild, `node scripts/check-research-engines.mjs http://127.0.0.1:4321`. Chromium 151 und Firefox 155 bei 1440 × 1000 und 390 × 844 bestanden: Start, alle 24 Einleitungen und 62 Fragen, Ergebnis, Gruppenvergleich, Übersicht und automatischer Wechsel. WebKit startet weiterhin nicht.
- **Platz ohne Scrollen.** Gemessen ab der Überschrift „Frage n von 62“ bis unter die Schaltflächen, mit 8 Pixel Abstand, bei abgeschaltetem automatischem Wechsel. Nach jedem Wechsel steht diese Überschrift oben im Fenster.
  - 1440 × 1000: alle 62 Fragen.
  - 1024 × 768: alle bis auf Frage 52 und 56. Sie haben die längsten Texte.
  - 390 × 844: alle bis auf Frage 23, 36, 52 und 56. Frage 23 ist 1 Pixel zu lang.
  - 320 × 720: keine Frage passt ganz, hier bleibt Scrollen nötig.
  - Die Einleitungsbildschirme vor Frage 11 und 38 haben lange Definitionen und brauchen bei 1024 × 768 und auf dem Smartphone Scrollen.
- **Sichtprüfung.** Startbildschirm, Einleitungsbildschirm, Fünferliste und 0–10-Reihe bei 1440, 1024, 390 und 320 Pixel angesehen.
- **Nicht durchführbar.** Physische Smartphones, Screenreader mit Menschen, Hochkontrastmodus auf echten Geräten, Safari und WebKit. Ob Einleitungsbildschirme und automatischer Wechsel Menschen helfen oder stören, zeigt erst ein Test mit Menschen.
