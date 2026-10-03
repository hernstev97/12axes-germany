# Angular: gezielte Scrollkorrektur, Runde 1

Stand: 2026-10-03. Autor: Codex-Subagent `angular_policy_draft`.

## Auftrag und Befund

Diese Runde bearbeitet ausschließlich AUI-ROOT-01 auf der gesicherten Ausgangsfassung des Checkpoints 44 (`acc294a6a21b411faaff4eccdd514834ace5a1b3`). Root beobachtete im lokalen Research-Browser nach dem nativen Bearbeiten der letzten Ergebnisfrage E35: Die H2 „Frage 43 von 43“ war fokussiert, lag bei 1280 × 800 aber oberhalb des sichtbaren Ausschnitts (`scrollY: 1188`, `top: -391.34375`, `bottom: -355.109375`). Quelle ist `reports/loop/angular-preview-initial-technical.json`; dies ist Roots Browserbeobachtung vor dieser Korrektur.

Geändert wurden nur `policy-draft.ts`, `policy-draft.spec.ts` und dieser neue Bericht. Originalautorbericht, Bindingbericht, öffentliche Katalogdaten und generierte Referenzeingabe bleiben unverändert. Es gab keine Git-, Server-, Installations-, Routing- oder Speicheränderung und keinen neuen Datenzugriff oder Zahlenlauf.

## Korrektur

Das vorhandene `focus()` wartet weiterhin mit `afterNextRender` auf den gerenderten Zielzustand. Es bestimmt dann die aktuelle H1 oder Fragen-H2, setzt den nativen Fokus mit `preventScroll: true` und ruft unmittelbar danach auf derselben Überschrift `scrollIntoView({ block: 'start', inline: 'nearest', behavior: 'instant' })` auf. Ein fehlendes Ziel wird weiterhin übersprungen. Die explizite Reihenfolge verhindert einen zusätzlichen impliziten Fokus-Scroll und fordert den sichtbaren Ausschnitt für das aktuelle Ziel an. `instant` verlangt keine Animation; damit entsteht auch keine Bewegung, die erst durch eine Reduced-Motion-Abfrage abgeschaltet werden müsste.

Antwortzustände, Fragenreihenfolge, Originaltexte und Codes, Quellenkontext, optionales Referenzinput und die 42 akzeptierten historischen Verteilungen wurden nicht geändert. Die gezielte Sichtbarkeitskorrektur ist ausdrücklich von Root beauftragt; sie erweitert keinen Produktablauf.

## Gezielte Prüfungen

Die Komponententests prüfen die tatsächliche native Fokuswirkung (`document.activeElement`) und die anschließende Scroll-Anforderung auf dem nach dem Rendern gefundenen Ziel. Abgedeckt sind Vorwärts-, Rückwärts- und Überspringen-Wechsel, alle sechs Wechsel zwischen Fragen, Übersicht und Ergebnis, Bearbeiten der letzten Frage aus Übersicht und Ergebnis sowie beide Übergänge von Frage 43 ins Ergebnis. Eine bloße Radioauswahl darf keinen neuen Fokus-/Scroll-Aufruf anfordern. Die sieben bestehenden Komponententests bleiben erhalten.

jsdom besitzt keine Layoutberechnung und in dieser Umgebung kein `scrollIntoView`. Eine ausschließlich in der Spec eingerichtete und nach jedem Test zurückgesetzte Testdouble protokolliert Ziel, Optionen und `document.activeElement` beim Aufruf. Der Fokus-Spy führt den ursprünglichen nativen Fokus weiter aus. Das belegt Aufrufreihenfolge und Zielbindung, keine tatsächlichen Browserkoordinaten oder Viewport-Sichtbarkeit.

- Regressionstest vor der Implementierung: 10 fehlgeschlagen, 1 bestanden, 7 übersprungen. Neun Fehler zeigten den fehlenden Scroll-Aufruf der alten Fassung. Ein weiterer Fehler war ein falsch gewählter Testbuttontext an der letzten Frage; der korrekte Text ist „Zum Ergebnisentwurf“. Der Test wurde anschließend auf den tatsächlichen Button in `.question-controls` begrenzt, damit er den Frage-43-Übergang prüft. Dieser zehnte Fehler ist kein Produktregressionsbeleg.
- Nach Korrektur: zunächst 18/18 Komponententests bestanden. Danach wurde die Ansichtswechselprüfung auf alle sechs tatsächlichen Wechsel erweitert.
- Abschließender Lauf: `pnpm --filter politikprofil test --watch=false --include 'src/app/policy-draft/policy-draft.spec.ts'` — **21/21 bestanden**, eine Testdatei, Exit 0. Bundleabschluss `2026-10-03T15:14:14.680Z`, Testdauer 7,47 s.
- `pnpm --filter politikprofil typecheck` — **bestanden**, Exit 0 (`ngc --noEmit -p tsconfig.app.json` und `tsc --noEmit -p tsconfig.spec.json`).
- Prettier wurde nur für die beiden erlaubten Code-/Specdateien und diesen neuen Bericht ausgeführt. Der abschließende `prettier --check` derselben drei Dateien hat **bestanden**, Exit 0.

Der tatsächliche Browsercheck „Ergebnis-E35 bearbeiten → fokussierte Frage sichtbar“ bleibt bei Root offen. AR-L01 und die vor dieser Runde nicht verifizierten Browserbeobachtungen werden durch jsdom nicht als erledigt ausgegeben. Es gab keinen vollständigen Neuaudit und keine neue wissenschaftliche, menschliche oder Release-Freigabe.

## Gelesene Dateien und SHA256

In dieser Runde gelesen: die erlaubte technische Browserbelegdatei, `policy-draft.ts`, `policy-draft.spec.ts` und die passenden Navigation-/Fragenkontrollstellen in `policy-draft.html`. Handbuch und Projektgrundlagen wurden bereits für die gesicherte Ausgangsfassung vollständig gelesen. Die unveränderten Artefakte unten wurden in dieser Runde nur gehasht.

| Datei | SHA256 |
| --- | --- |
| `policy-draft.ts`, vorher | `cc5f6122faa183d9e9e46bb1bef65ae6d6d0831e91bfb1de257eba57d68ec725` |
| `policy-draft.ts`, jetzt | `fa926ffbdbff04c6efc9fd059b839c03c0e1e02fdda14b4cbfa5338154b798be` |
| `policy-draft.spec.ts`, vorher | `e9cd038e558357e7a07157dbf1c18e3682b074c373fe2a7ad6d5331a9f426f09` |
| `policy-draft.spec.ts`, jetzt | `4cd1041e00e19175da2bb382ada5ebd6f6c447ea5def6822b72af1ae4eb60661` |
| `public-catalogue.ts`, unverändert | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `reviewed-historical-references.ts`, unverändert | `4a305618c23d8f9059782b364387e741616b399961989a1bd6448b1014520bcb` |
| `ANGULAR-POLICY-DRAFT-WIP.md`, unverändert | `a0f1474a8360045f7b5800c0a1b3f5dbf102dd15c7aa62cdf74bac8766a6425d` |
| `ANGULAR-REFERENCE-BINDING-WIP.md`, unverändert | `051a4b933bf2da29b9291a1380f47980831f206e27568abdb41b101e9f98ab43` |
| `angular-preview-initial-technical.json`, Ausgangsbeleg | `646a28797206886297ebbe2aafb38fe5ce2573bb3c584dae398a206fdb340537` |
