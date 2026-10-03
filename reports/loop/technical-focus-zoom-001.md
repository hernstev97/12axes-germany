# LIFE-93: Tastaturfokus und echter Browserzoom

Technische Nacharbeit am 3. Oktober 2026, ausgehend von Commit `9de6ec5a31c365c898b45f4394d2cf1ff0052476`. Der [maschinenlesbare Beleg](technical-focus-zoom-001.json) bindet tatsächliche Läufe, Code-/Browserversion, ursprüngliche Prüferberichte und gesichtete Aufnahmen.

## Korrekturen

TFZ-S01: Der Gruppenquellen-Summary erhält den vorhandenen Fokusrahmen mit 2 px und 4 px Abstand. TFZ-S04: Nach dem Zurücksetzen deaktivierte sich der fokussierte Button; nach dem Rendern fiel der Fokus im Chromium auf `body`. Der bestehende Fokuswechsel führt jetzt zur Frageüberschrift. Der nächste Tab erreicht die erste Antwortoption. Der neue Regressionstest prüft deaktivierten Reset, leere Auswahl und Fokus-/Scrollziel; jsdom beweist kein Layout. Beide Änderungen wurden gezielt statisch nachgeprüft. Fragen, Antworten, Vergleichsdaten, Forschungskriterien und Tags unverändert.

Der [neue Browserchecker](../../scripts/check-research-browser.mjs) erreicht die Entwicklungsroute ausdrücklich. Der unveränderte allgemeine Checker bleibt ein eigener Prüfweg für die normale Website. Vier konkrete Prüfcodelücken wurden nach einem getrennten Erstbericht gezielt korrigiert: Fokusübergaben, tatsächlicher Detailszustand, gerenderte Gruppenauswahl und Fokusfarbe. Originalberichte und frühere Fehlversuche bleiben erhalten.

## Tatsächlich ausgeführte Prüfungen

Der endgültige Lauf nutzt den vorhandenen lokalen Chromium mit eigenem Profil und eigener QA-Erweiterung. `chrome.tabs.setZoom/getZoom` bestätigen automatischen Tabzoom mit Faktor 2. Bei unveränderter Fenstergröße 1280 × 900 ergeben sich 640 × 450 CSS-Pixel. CSS-Zoom und Pinch-Skalierung bleiben 1; kein eigener Pixeldichte-Override. Die Bedienung eines Browsermenüs wurde nicht geprüft. [Chrome-API](https://developer.chrome.com/docs/extensions/reference/api/tabs#method-setZoom).

| Fenster     |  Zoom | CSS-Größe   |
| ----------- | ----: | ----------- |
| 1440 × 1000 | 100 % | 1440 × 1000 |
| 1024 × 768  | 100 % | 1024 × 768  |
| 768 × 1024  | 100 % | 768 × 1024  |
| 390 × 844   | 100 % | 390 × 844   |
| 320 × 720   | 100 % | 320 × 720   |
| 1280 × 900  | 200 % | 640 × 450   |
| 1440 × 1000 | 200 % | 720 × 500   |
| 1024 × 768  | 200 % | 512 × 384   |
| 768 × 1024  | 200 % | 384 × 512   |

Je Bedingung: alle 43 Fragen per nativen Tastaturereignissen, Auswahl, Zurücksetzen, Radio-Pfeiltasten, Rückwärtsnavigation, Überspringen, Übersicht, Ergebnisse, Antwortbearbeitung und entfernter Sprung zu Frage 43. Die 42 folgenden Fragenwechsel warten vor dem nächsten Tab auf fokussierte, vertikal sichtbare Überschrift. Insgesamt 594 Fokusprüfungen mit sichtbarem Rahmenzustand, deckender Farbe und berechnetem Kontrast mindestens 13,27:1 gegen den nächsten deckenden Elternhintergrund. Repräsentative native Aufnahmen wurden tatsächlich angesehen; kein sichtbarer horizontaler Ausschnittfehler in diesen Aufnahmen. Die Bildliste steht im JSON-Beleg.

Geöffnet wurden die Quellen der ersten Frage einschließlich drei verschachtelter Abschnitte, der erste Ergebnisquellenblock und die Gruppenquellen nach tatsächlicher Auswahl der ersten ESS5-Gruppe. `details.open`, nichtleere Auswahl und passende gerenderte Gruppenhinweise sind geprüft. 441 Dokument-Überlaufprüfungen ohne horizontalen Überlauf. 45 axe-Läufe ohne Verstöße; eine Kontrastregel blieb unvollständig. Zusätzlich Startseite, Projektstand und Methodik in denselben neun Bedingungen: 27 Ansichten, 54 repräsentative Fokusprüfungen, 27 axe-Läufe ohne Verstöße oder unvollständige Regeln. Galerie-Zeitabläufe wurden nicht wiederholt.

Die unvollständige axe-Regel betrifft `details:nth-child(9) > .original-text` bei 768 × 1024 und geöffneten Zitationsquellen. axe meldet `bgOverlap`, auch nach nativem Scrollen zum vollständig sichtbaren Absatz. Gezielte Lektüre zeigt Textfarbe `rgb(30,43,36)`, Papier `rgb(246,243,235)`, Deckkraft 1 und rechnerischen Kontrast 13,28:1. Die nativen Aufnahmen vor/nach dem Scrollen wurden angesehen; Text ist lesbar. Zwei sichtbare Hit-Test-Punkte trafen den Absatz selbst. Die automatische Unvollständigkeit bleibt dokumentiert; daraus entsteht kein vollständiger WCAG-Pass.

Playwrights Surface-Aufnahme war bei echtem Tabzoom leer und zählt nicht als Sichtbeleg. Der endgültige Lauf nutzt die [native Chromium-Viewport-Aufnahme](https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot) mit `fromSurface=false`. Frühere automatische PASS-Läufe hatten weniger Guards beziehungsweise unbrauchbare Zoombilder; sie werden nicht nachträglich zum endgültigen Prüfumfang umbenannt.

## Wiederholung und Grenzen

Mit bestehenden Projektabhängigkeiten und vorhandenem Playwright-Chromium:

```bash
pnpm dev:research
node scripts/check-research-browser.mjs
```

Das Skript legt nur eigene lokale Profile, Erweiterung und technische Bilder unter dem ignorierten `outputs/research-browser` an. Sein Browser schließt im `finally`-Block. Keine globale Installation, privaten Analysepfade oder Rohdaten. Demonstrative Auswahlen sind technische Zustände; null reale Menschen.

Dieser Chromium-Lauf prüft keine physischen Smartphones, anderen Browser oder mobilen Pinch-Zoom. Nicht jede Quelle jeder Frage oder jede Gruppenvariante wurde erneut geöffnet. Die Farbheuristik und einzelne Aufnahmen ersetzen keine vollständige Pixel-/WCAG-Prüfung. Menschenverständnis, Gestaltung, Datenrechte, Claude-Schlusskontrolle und persönlicher Release bleiben offen. Check059: `pnpm check` Exit 0, 79 Tests in sieben Dateien, Typecheck, Format-/Handbuch-/Schemaschutz und Produktionsbuild. [Serverstopp](technical-focus-zoom-server-shutdown.json): nur verifizierte Listener-PIDs signalisiert; alle drei Ports und pnpm-Wrapper beendet. Erste vorzeitige PARTIAL-Prüfung erhalten, anschließende Nachprüfung PASS.
