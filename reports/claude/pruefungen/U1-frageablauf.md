# U1: Prüfung des Frageablaufs im Forschungsentwurf

KI-Review vom 6. Oktober 2026 (Ortszeit; die Prüfung begann am Abend des 5. Oktober 2026). Kein Peer Review, keine methodische Validierung, keine Design- oder Releasefreigabe.

- Auftrag: `reports/claude/auftraege/U1-frageablauf.md`, SHA-256 `07e2d3b24caae8969f6dfc166114659c2cac2da7ffbc982c78f8599a5e0a8746`, vor Beginn bestätigt.
- Prüffassung: Manifest `reports/claude/pruefungen/UI-FRAGEANSICHT-002-manifest.json`, SHA-256 `36a0aad0363521742fdbffda9879f9747aaebe36e74a44335a00c6b7796a7acf`, vor Beginn bestätigt. Alle 19 Artefakthashes stimmen. Das Manifest nennt Commit `ea84b93`; HEAD war während der ganzen Prüfung `001dfa3`, der zwischen beiden nur das Manifest und die Auftragsprüfsummen ergänzt. Die Arbeitskopie war vorher und nachher sauber.
- Modus: Der Auftrag nennt „Paketprüfung“. Das Urteilsschema kennt diesen Wert nicht. Im JSON steht deshalb `PR_REVIEW`, weil eine fertige Änderung gegen ihren Ausgangsstand `9489579` geprüft wird.
- Prüferrolle: Codex ist bis zum 10. Oktober 2026 nicht verfügbar. Ich bin ein frischer Claude-Subagent (Anthropic), also aus derselben Modellfamilie wie der Autor. Gemeinsame blinde Flecken sind möglich. Ich habe deshalb Kommentare und Dokumentation nicht als Beleg genommen, sondern Templates, TypeScript, SCSS, Tests und Skripte selbst gelesen und die Block- und Zahlenreihenlogik mit eigenem Code über den öffentlichen Katalog nachgerechnet. Übereinstimmung mit dem Autor ist kein Neutralitäts- oder Qualitätsnachweis.

## Gesamturteil

**BESTANDEN** für den benannten Umfang: Codeprüfung von `app-policy-draft`, `app-policy-progress`, `app-policy-question`, den beiden Prüfskripten und dem Abschnitt „Ablauf des Forschungsentwurfs“ im Handbuch. Alle sieben Checks sind bestanden. Sechs Findings mit Schweregrad niedrig bleiben offen und blockieren den Umfang nicht. Drei davon (U1-F02, U1-F03, U1-F04) sind Vermutungen oder offene Fragen, die erst eine Browser- oder Screenreaderprüfung klärt. Eigene Browserbeobachtungen habe ich nicht gemacht.

Technische Prüfung, Browserbeobachtung und wissenschaftliche Abnahme sind getrennt: `pnpm check` lief bei mir grün (129 Tests). Die Browserbeobachtungen in `docs/validation.md` sind Angaben des Autors und nicht von mir wiederholt. Eine wissenschaftliche Abnahme ist nicht Gegenstand.

## Checks

### C01 Inhalt unverändert: BESTANDEN

- Die neuen Templates zeigen nur Katalogfelder: Fragewortlaut als `legend` aus `displayWording`, Antworten aus `offeredCategories` über `categoryLabel`, Einleitungen und Definitionen auf dem Einleitungsbildschirm (`policy-question.html:10–25`), Situationsbeschreibung in der Karte (`:47–49`), Herkunft und Entwicklungshinweis (`:131–132`). `policy-catalogue.ts` und `policy-source-details.*` sind seit `9489579` unverändert.
- Blockbildung: Ich habe Reihenfolge und Blöcke mit eigenem Node-Code aus den Katalogliteralen nachgebaut (Demokratieblock, `V22_AFTER`, `introductionsBefore` aus `display-additions.ts`). Ergebnis: 62 Fragen, 24 Blöcke, Block 1 = Frage 1 bis 4. Das deckt sich mit `contextBlocks` (`policy-draft.ts:46–63`), dem Protokoll und den Tests. Jede Frage mit Einleitung oder Definition hat einen Block und damit die Schaltfläche „Einleitung zu dieser Frage anzeigen“ (`policy-question.html:124–130`). Ohne Einleitung bleiben A51, E15 und E19 bis E22; sie zeigen den Katalogsatz „Der Katalog enthält für diese Einzelangabe keine zusätzliche Einleitung.“
- Zahlenreihe: Nur die 22 Listen mit elf angebotenen Kategorien erreichen die Schwelle von sieben (alle anderen haben höchstens sechs). Alle 22 erscheinen als Reihe. Keine mittlere Antwort hat einen Text, der versteckt würde. Der zugängliche Name jeder Antwort ist Zahl plus versteckter Text, also der volle `categoryLabel`, bei Endbeschriftungen ohne Zahl (A1, A2, A51) „0: …“ bzw. „10: …“ mit `printedCodeDe` aus dem Katalog. Erfundene Codes gibt es nicht. Bei B37 steht „00“ am Anfang und „1“ bis „10“ danach, weil der Katalog Code 0 als „00“ druckt und die mittleren Labels als „1“ bis „9“ führt.

### C02 Ablauf und automatischer Wechsel: BESTANDEN

- Start, Einleitung, Frage: `view` beginnt mit `'start'` (`policy-draft.ts:111`). `show('questions')` setzt die Einleitung des aktuellen Blocks, `next()` ruft `introduceBlock()` auf, `previous()` und `edit()` setzen `introShown` auf falsch (`:265–317`). Das entspricht dem Handbuch: vorwärts je Block einmal, rückwärts und bei Sprüngen direkt zur Frage.
- Ankündigung: Der Schalter steht im DOM vor den Antworten (`policy-question.html:2–8` vor `:50`) und ist zu Beginn an (`policy-draft.ts:119`).
- Tasten: `handleKey` setzt während eines Pfeil-`keydown` eine Sperre. Das Klickereignis der Pfeilauswahl läuft dadurch ins Leere (`policy-question.ts:114–148`). Leertaste auf einem ungewählten Radio löst den nativen Klick aus. Leertaste oder Eingabetaste auf einem gewählten Radio bestätigen über `keyup`. Jede Bestätigung räumt zuerst den alten Timer weg, es läuft also höchstens ein Timer. Eingabetaste auf einem ungewählten Radio tut nichts.
- Letzte Frage: `confirm` startet dort keinen Timer (`:134`).
- Abbruch: `request()` bricht bei Zurücksetzen, Überspringen, Vorher, Weiter, Einleitung und Rückkehr zur Frage ab (`:162–172`), `setAutoAdvance` beim Ausschalten (`:150–153`), `DestroyRef` beim Wechsel in Übersicht oder Ergebnis (`:95–97`). Der Timer prüft beim Ablauf noch einmal Frage, Antwort und Schalter (`:139–146`). Einen Weg zum doppelten Sprung habe ich nicht gefunden.
- Fokus: Nach Weiter, Vorher, Zurücksetzen, Einleitung, Sprung und Wechsel zu den Fragen geht der Fokus auf `#draft-question-title`, nach der letzten Frage auf die H1 des Ergebnisentwurfs (`policy-draft.ts:485–499`), mit `preventScroll` und `behavior: 'instant'`. Dass Hilfsmittel den Wechsel in jedem Browser ansagen, ist offen (U1-F04).

### C03 Barrierefreiheit im Code: BESTANDEN, Teilpunkt erzwungene Farben eingeschränkt

- H1: Auf Einleitungs- und Fragebildschirm genau die nur für Hilfsmittel lesbare H1 (`policy-draft.html:3`), sonst die sichtbare H1 (`:32`). `app.html` enthält keine H1. In der Frageansicht folgt H2 ohne übersprungene Ebene, `app-policy-source-details` zeigt dort seine H4 nicht (`showOriginal` ist falsch).
- Rollen und Namen: `input type="checkbox" role="switch"` mit umschließendem Label, `progress` mit `aria-label="Bearbeitete Fragen"`, `value` und `max`, native Radios in `fieldset` mit `legend`. `aria-describedby` verweist auf `draft-situation` nur dann, wenn es sie gibt, und auf `draft-development-note`. Beide IDs stehen im selben Bildschirm (`policy-question.html:48–54, 132`).
- Reihenfolge: Die DOM-Reihenfolge folgt der sichtbaren Reihenfolge. „Auswahl zurücksetzen“ steht im Kartenkopf vor den Antworten, WCAG 2.4.3 ist damit erfüllt. Zur Verschiebung auf dem Smartphone siehe U1-F03.
- Fokus und Zielgrößen: sichtbare Fokusrahmen mit 2 px und 4 px Abstand für Schaltflächen (global), Radios, Auswahlliste, Schalter und Zusammenfassungen. Die H2 mit `tabindex="-1"` hat nach Kapitel 8 keinen Rahmen. Zielgrößen: Schaltflächen und Auswahlliste 48 px, „Auswahl zurücksetzen“ 40 px, Antwortzeilen 48 bzw. 44 px, der Schalter liegt in einem 48 px hohen Label. Überall mindestens 24 px.
- Kontrast, selbst nach WCAG-Formel gerechnet: `--ink` auf `--paper` 13,28, `--paper` auf `--ink-hover` 9,11, `--ink` auf `--mat` 11,82, `--ink` auf `--line` 9,54, `--muted` auf `--paper` 6,80, `--forest` auf `--paper` 11,08. Die Werte im Handbuch stimmen.
- Zählzeile: bis 640 px mit dem Clip-Muster nur für Hilfsmittel lesbar, weiter im Baum und `aria-live="polite"` (`policy-progress.scss:73–82`).
- Erzwungene Farben: Der Schalter fällt auf die native Darstellung zurück (`policy-progress.scss:44–48`). Der Fortschrittsbalken hat keine solche Regel und ist dort vermutlich unsichtbar (U1-F02). Die gewählte Antwort verliert Fläche und inneren Rahmen, das native Radio zeigt den Zustand weiter.
- Bewegung: Beim Bildschirmwechsel gibt es keinen Übergang. Gescrollt wird mit `instant`, und `prefers-reduced-motion` schaltet die Übergänge der Antwortzeilen global ab.

### C04 Handbuch: BESTANDEN mit Hinweisen

- In den drei Komponentenstilen stehen nur `var(--…)`, `transparent` und `none`, keine Farbwerte und keine `font-family`. `check:handbuch` lief grün.
- Schaltflächentexte nennen Ziel oder Handlung: „Zu den Fragen“, „Zu Frage n“, „Vorherige Frage“, „Nächste Frage“, „Zum Ergebnisentwurf“, „Zur Fragenübersicht“, „Frage überspringen“, „Auswahl zurücksetzen“, „Einleitung zu dieser Frage anzeigen“.
- Verbotene Muster aus Kapitel 1 und 7 habe ich nicht gefunden. Der Startbildschirm hat genau eine Primärschaltfläche, keine Pfeile, keine Anrede.
- Kapitel 4 stimmt im Kern mit der Umsetzung überein: Startbildschirm in einer 46-rem-Spalte, Einleitung in Lead-Größe, Karte mit Rahmen in `--line` und 3 px `--forest` ohne Schatten und Rundung, gewählte Antwort mit `--ink` und `--mat`, Zahlenreihe ab 640 px einzeilig, darunter 6 + 5, ausgefüllte Schaltfläche nach vorn, 350 ms, Schalter vor den Antworten. Die Abweichung bei der Schaltfläche nach vorn ist umgesetzt wie beschrieben. Kleinere Ungenauigkeiten und eine nicht eingetragene Schriftgröße beschreibt U1-F05, den Konflikt mit Kapitel 5 U1-F06.

### C05 Neutrale Darstellung: BESTANDEN

Antworten stehen in Katalogreihenfolge, alle mit gleichem Rahmen, gleicher Schrift und gleichem Hover. Nichts ist vorausgewählt. Hervorgehoben wird nur `:has(input:checked)`. Die beiden Endbeschriftungen der Zahlenreihe sind gleich gestaltet. Es gibt keine Symbole und keine Farben, die Zustimmung oder Ablehnung werten. Die ausgefüllte Schaltfläche ist Navigation, keine Antwort.

### C06 Datenschutz: BESTANDEN

In den geänderten Dateien und in `PolicyProfileSession` gibt es keine Speicher-, Netzwerk-, Router-, `history`- oder `location`-Aufrufe (grep ohne Treffer). Schalterzustand (`autoAdvance`) und gesehene Einleitungen (`introducedBlocks`) sind Felder der Komponenteninstanz. Die neuen Templates haben keine Formulare und keine Links, alle Schaltflächen sind `type="button"`. Die Tests prüfen `Storage.setItem`, `fetch` und `location` (`policy-draft.spec.ts:525–538, 706–753`). Die Route gibt es nur im lokalen Forschungsbuild (`research-preview.routes.ts` ist leer, `angular.json` ersetzt die Datei nur in `research`).

### C07 Tests und Prüfskripte: BESTANDEN mit Hinweis

- Unit-Tests decken Start (`:883–898`), Einleitungen (`:900–961`) und den automatischen Wechsel (`:770–877`) ab: Voreinstellung und Lage des Schalters, Wechsel mit Fokus, erneutes Bestätigen, Pfeiltasten, Leertaste und Eingabetaste, Ausschalten, Zurücksetzen, kein doppelter Sprung, letzte Frage, Blockende. Sie nutzen echte Timer und lassen drei Abbruchwege aus (U1-F01).
- `check-research-browser.mjs` und `check-research-engines.mjs`: Die Änderungen passen Namen und Abläufe an. Weggefallene Prüfungen sind gleichwertig ersetzt: `reset.isDisabled()` durch `reset.count() === 0`, `input:checked` durch `input[name=draft-original-answer]:checked`, weil der Schalter selbst eine Checkbox ist, `.last()` durch `.first()`, weil die Kartenschaltfläche jetzt vor der gleichnamigen Ansichtsschaltfläche steht. Fokus-, Überlauf-, axe- und Datenschutzprüfungen bleiben. axe-Läufe je Bedingung steigen von fünf auf acht. Eine bestehende Prüfung wird nicht schwächer.
- Grenzen der Skripte, ohne Abschwächung: Im Browserskript läuft der neue Abschnitt zum automatischen Wechsel nach der Datenschutzprüfung mit `loaded = false`, Anfragen in diesem Abschnitt zählt es nicht (das Engines-Skript prüft sie). Die Eingabetaste prüft kein Browserskript, erzwungene Farben emuliert keines.

## Findings

### U1-F01 Echte Timer in den Tests zum automatischen Wechsel (niedrig, belegt, offen)

- Fundstelle: `web/src/app/policy-draft/policy-draft.spec.ts:760–763` (`afterDelay` wartet real 400 ms) und `:755–878`; `docs/handbuch.md:373` „Zeitabhängige Tests nutzen Fake-Timer.“; Vergleich `web/src/app/art/art-gallery.spec.ts` mit `vi.useFakeTimers`.
- Problem: Die Tests weichen von Kapitel 9 ab. Negativtests prüfen nur einen Zeitpunkt 50 ms nach Ablauf, kein Test zeigt, dass vor 350 ms nichts passiert. Den Abbruch durch „Vorherige Frage“, „Einleitung zu dieser Frage anzeigen“ und die Ansichtsnavigation leistet der Code (`policy-question.ts:95–97, 162–172`), getestet ist er nicht. Die Eingabetaste ist nur mit einem synthetischen `keyup` geprüft.
- Auswirkung: Die Funktion stimmt, aber eine Änderung der Pause oder eines Abbruchwegs fiele nicht sicher auf.
- Korrektur: `vi.useFakeTimers()` im Block, `advanceTimersByTimeAsync(AUTO_ADVANCE_DELAY_MS - 1)` ohne und `+ 1` mit Wechsel; drei Tests für die fehlenden Abbruchwege.
- Nachprüfung: Spec-Diff lesen, `pnpm check`.

### U1-F02 Fortschrittsbalken bei erzwungenen Farben (niedrig, Vermutung, offen)

- Fundstelle: `web/src/app/policy-draft/policy-progress.scss:49–66` (`appearance: none`, `border: 0`, nur Hintergrundfarben), `:44–48` (Regel nur für den Schalter), `:73–82` (Zählzeile bis 640 px verborgen); keine `forcedColors`-Emulation in beiden Skripten.
- Problem: Im Modus für erzwungene Farben ersetzen Browser Autorenhintergründe durch Systemfarben. Spur und Wert bekommen dann vermutlich dieselbe Farbe, ohne Rahmen ist der Balken nicht zu sehen. Bis 640 px, also auch bei 1280 px Fensterbreite mit 200 % Zoom, ist zugleich die Zählzeile nur für Hilfsmittel lesbar.
- Auswirkung: Sichtbar bliebe nur „Frage n von N“, nicht die Zahl bearbeiteter Fragen. Einen Verstoß gegen WCAG 2.2 AA belegt das nicht.
- Korrektur: In `@media (forced-colors: active)` den Balken sichtbar machen, etwa mit `appearance: auto` oder mit Rahmen und Wert in Systemfarben (`CanvasText`, `Highlight`). Im Browserskript `page.emulateMedia({ forcedColors: 'active' })` mit Aufnahme ergänzen.
- Nachprüfung: Chromium mit emulierten erzwungenen Farben bei 1440 und 390 px, Balken bei 0, einigen und allen bearbeiteten Fragen ansehen.

### U1-F03 „Auswahl zurücksetzen“ verschiebt auf dem Smartphone die Antworten (niedrig, Vermutung, offen)

- Fundstelle: `web/src/app/policy-draft/policy-question.html:36–46`, `policy-question.scss:48–55, 62–70`.
- Problem: Die Schaltfläche entsteht erst mit der ersten Auswahl im umbrechenden Kartenkopf. Mit den Laufweiten der lokal eingebundenen Libre Baskerville (fontTools, ohne Kerning) misst ihr Text 152,6 px. Bei 390 px Breite bleiben 316 px Karteninhalt. Sie passt dort nur neben „Sozialstaat“, „Klima und Energie“ und „Migration“. In den anderen fünf Bereichen mit 40 der 62 Fragen bricht sie in eine eigene Zeile um, bei 360 und 320 px in sechs Bereichen mit 50 Fragen. Rechnerisch rücken Frage und Antworten im Moment der Auswahl um etwa 29 px nach unten (40 px Mindesthöhe, minus zweimal 0,6 rem Rand, plus 0,5 rem Zeilenabstand). Wer per Tab kommt, hört außerdem „Auswahl zurücksetzen“ vor der Frage.
- Auswirkung: Die gerade angetippte Antwort wandert unter dem Finger weg. Bei ausgeschaltetem Wechsel oder einer schnellen Korrektur kann der zweite Tipp eine andere Antwort treffen. In `docs/validation.md` steht nicht, ob die Platzmessung mit gewählter Antwort lief.
- Korrektur: Den Platz von Anfang an freihalten, zum Beispiel die Schaltfläche immer rendern und ohne Auswahl mit `visibility: hidden` ausblenden, oder sie in eine eigene Zeile oder neben „Frage überspringen“ setzen. Die Lage im Handbuch festhalten.
- Nachprüfung: Bei 390 und 320 px mit ausgeschaltetem Wechsel für eine Frage aus „Demokratie und politische Autorität“ die Oberkante der ersten Antwort vor und nach der ersten Auswahl messen. Erwartet: keine Verschiebung.

### U1-F04 Fokus auf dieselbe H2 wird nicht immer neu angesagt (niedrig, offene Frage, offen)

- Fundstelle: `web/src/app/policy-draft/policy-progress.html:2`, `policy-draft.ts:485–499`.
- Problem: `app-policy-progress` bleibt beim Wechsel bestehen, nur der Text der H2 ändert sich. Liegt der Fokus schon auf der H2, löst `focus()` kein Fokusereignis aus. Das passiert, wenn ein Klick oder Tippen den Fokus nicht auf das Radio legt. Safari und Firefox unter macOS verhalten sich bei Radios so, Chromium nicht. WebKit startet in der Umgebung des Autors nicht, jsdom kann es nicht zeigen.
- Auswirkung: Möglicherweise sagt VoiceOver unter iOS oder macOS den neuen Bildschirm nach einem automatischen Wechsel durch Tippen nicht an. Belegt ist das nicht.
- Korrektur: Mit WebKit und VoiceOver prüfen. Falls bestätigt, vor `focus()` die H2 entfokussieren oder die Überschrift je Bildschirm neu erzeugen.
- Nachprüfung: Safari oder iOS mit VoiceOver, nach Tippen auf eine Antwort wird „Frage 2 von 62, Überschrift“ angesagt.

### U1-F05 Handbuch und Protokoll beschreiben Einzelheiten ungenau (niedrig, belegt, offen)

- Fundstelle: `docs/handbuch.md:89–99, 149–161, 180`; `policy-question.scss:94`; `policy-progress.scss:11–15`; `policy-question.ts:59–65`; `policy-question.html:125–127, 133–136`; `docs/ki-protokoll.md`, Abschnitt 2026-10-05.
- Problem:
  - Die Frage (`legend`) hat `clamp(1.15rem, 2vw, 1.4rem)`. Diese Stufe fehlt in der Größenskala und im Muster. Die H2 „Frage n von N“ ist 1 rem fett ohne `.section-title`, Kapitel 5 nennt für H2 `.section-title`.
  - Blöcke aus einer Frage heißen „Einleitung zu Frage n“, Kapitel 4 nennt nur „n bis m“.
  - „der Link zur Einleitung“ ist eine Schaltfläche.
  - „bleiben Teil des Namens jeder Antwort“ trifft nur die beiden Endantworten. Die mittleren Antworten heißen nach ihrer Zahl, wie im Katalog.
  - Der Satz „Überspringen ist keine politische Antwort …“ unter der Karte und Fortschritt mit Schalter auf dem Einleitungsbildschirm fehlen im Muster.
  - Das Protokoll sagt, „Auswahl zurücksetzen“ erscheine „nur bei einer Antwort“. Umsetzung, Handbuch und Test (`policy-draft.spec.ts:949–961`) zeigen sie auch nach dem Überspringen.
- Auswirkung: Wer nach dem Handbuch nachbaut, bekommt eine andere Frageschrift und andere Überschriften. Die Funktion ist nicht betroffen.
- Korrektur: Größe der Frage und Stil der Fortschritts-H2 in Kapitel 3 oder 4 eintragen oder eine vorhandene Stufe nehmen. Kapitel 4 an den genannten Stellen genauer fassen. Den Protokollsatz in einem neuen Eintrag berichtigen.
- Nachprüfung: Handbuch-Diff gegen Templates und SCSS lesen.

### U1-F06 Ausgefüllte Vorwärtsschaltfläche gegen Kapitel 5, Zuschreibung an Steven (niedrig, offene Frage, offen)

- Fundstelle: `docs/handbuch.md:8, 10, 149, 158, 186`; Stevens Wortlaut in `docs/ki-protokoll.md`, Abschnitt 2026-10-05.
- Problem: Kapitel 5 erlaubt die Primärschaltfläche „nur für Wege zu einer anderen Seite“, und „nur“ ist nach Kapitel 0 Pflicht. Kapitel 4 begründet die ausgefüllte Schaltfläche nach vorn, Kapitel 5 verweist nicht darauf. Kapitel 4 schreibt außerdem den ganzen Ablauf Steven zu. Sein Wortlaut verlangt Startbildschirm, Einleitungsbildschirm, mittige Frage, automatischen Wechsel, Fortschrittsbalken, unauffällige Quellen und das Überspringen mit Grund. Die ausgefüllte Vorwärtsschaltfläche, 350 ms, „je Block einmal in der Sitzung“, die direkte Frage bei Rückwärts und Sprung und die verborgene Zählzeile sind Entscheidungen der Umsetzung. Dass Steven ihnen zugestimmt hat, wie es Kapitel 0 für neue Muster verlangt, steht nirgends.
- Auswirkung: Bei der Vorwärtsschaltfläche widersprechen sich zwei Handbuchregeln, und Autorentscheidungen lesen sich wie Stevens Vorgaben.
- Korrektur: Steven bestätigt die Einzelheiten, oder Kapitel 4 trennt seine Vorgaben von den Umsetzungsentscheidungen. Kapitel 5 nennt die Ausnahme.
- Nachprüfung: Kapitel 4 und 5 und das Protokoll lesen.

## Hinweise ohne Finding

- Weil der Katalog A54 einen zweiten Satz gibt, bilden A54 (Frage 49) und A55/A56 (50–51) zwei Blöcke. Der Einleitungsbildschirm vor Frage 50 wiederholt den ersten Satz, der eben vor Frage 49 stand. Ebenso beginnen die Einleitungen vor Frage 9 und 10 mit demselben E33-Satz. Das folgt der Regel im Handbuch und der gewollten Wiederholung in `display-additions.ts`. Der Verständnistest mit Menschen kann zeigen, ob es stört.
- In der zweizeiligen Zahlenreihe steht die rechte Endbeschriftung unter der leeren sechsten Spalte, nicht unter der 10.
- Die Zählzeile ist `aria-live`. Nach der ersten Antwort auf eine Frage meldet sie sich, 350 ms später folgt die Ansage der H2. Ob das zu viel ist, zeigt nur ein Test mit Screenreader.
- `pnpm check` baut nur die öffentliche Fassung ohne die Forschungskomponenten, und die Konfiguration `research` hat keine Budgets. „Build ohne Budgetwarnung“ in `docs/validation.md` gilt also nicht für diese Komponenten. Die SCSS-Dateien liegen mit 3711, 1695 und 2261 Byte unter den 4 kB aus Kapitel 4.
- Die Übergänge der Antwortzeilen (160 ms) laufen auch beim Auswählen, nicht nur beim Hover. Kapitel 3 nennt nur Hover.

## Offene Punkte

- U1-F02, U1-F03 und U1-F04 brauchen eine Browser- oder Screenreaderprüfung: erzwungene Farben, Verschiebung bei 390 und 320 px, WebKit mit VoiceOver.
- U1-F06 braucht Stevens Entscheidung.
- Eine zweite, unabhängige Prüfung durch eine andere Modellfamilie (Codex ab dem 10. Oktober 2026) steht aus.
- Verständnistest mit Menschen, Designfreigabe, Test- und Ergebnisgestaltung bleiben Stevens Entscheidungen.

## Grenzen

- Nur Codeprüfung und `pnpm check`. Keine Browser- oder Datenskripte, kein Server, kein Screenreader, kein echtes Gerät.
- Block- und Zahlenreihenlogik habe ich mit eigenem Node-Code nachgerechnet, der die Objektliterale aus `public-catalogue.ts` und `public-catalogue-v22.ts` auswertet (nur Metadaten, keine Antwortdaten) und die Logik aus `policy-draft.ts` und `policy-question.ts` nachbaut. Das ist eine Gegenrechnung, kein Lauf der Angular-Komponente. Die Breitenrechnung für U1-F03 nutzt die Laufweiten der Variablenschrift bei 400 und 700 ohne Kerning.
- `web/src/app/policy-draft/reviewed-*.ts` habe ich nicht geöffnet. Die Tests in `pnpm check` importieren sie, das ist Ausführung, kein Lesen.
- Nicht gelesen: `data/raw/`, `data/local/`, `data/reference-*`, `outputs/`, Analyseplan, Abdeckung, Profil- und Prüfregeln (Methodik gehört nicht zum Auftrag). Andere Prüfberichte habe ich nicht gelesen. `K1-runde2-textvorschlaege.json` diente nur als Formatvorlage, ihren Inhalt habe ich nicht bewertet.
- `pnpm check` schreibt den Build nach `web/dist/` (von Git ausgenommen). Meine Logdatei lag unter `/tmp/`. `git status` war nach der Prüfung bis auf diese beiden Berichtsdateien leer.

## Gelesene Dateien mit SHA-256

| Datei | SHA-256 |
| --- | --- |
| `AGENTS.md` | `6d405f6baff0b692edf657dae09c933b3ef978e2f3a98d3caaf14dc7666f627f` |
| `reports/claude/auftraege/U1-frageablauf.md` | `07e2d3b24caae8969f6dfc166114659c2cac2da7ffbc982c78f8599a5e0a8746` |
| `reports/claude/pruefungen/UI-FRAGEANSICHT-002-manifest.json` | `36a0aad0363521742fdbffda9879f9747aaebe36e74a44335a00c6b7796a7acf` |
| `.claude/skills/life93-review/SKILL.md` | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `reports/claude/pruefungen/K1-runde2-textvorschlaege.json` (nur Format) | `f97cbb8cba5492afa96255d09d4e47d8bdb51552a79b4cd0bade98efea2017c7` |
| `docs/handbuch.md` | `37e7b59ee3ea87e059003643795320d96f65d8a93565a9f191c4261484f6602c` |
| `docs/project.md` | `4d23f28649d83b4333af382723b831c16b5e52cf5412a0ff2ef4e0dfa493287d` |
| `docs/ki-protokoll.md` (Abschnitt 2026-10-05) | `2731797ea7690d69cdf25112bb763e10c419169541ab4b8c5e2f3ee3c229ba8f` |
| `docs/validation.md` (Abschnitt 5. Oktober 2026) | `2cd3c640d6837dcf06c960b46e7cf1c95c106a0ef3bdcf7cbba075accac8a28e` |
| `web/src/app/policy-draft/policy-question.ts` | `96503c5bc65a367756047f645cc204c11f1872dd07c7092842a23905e2343486` |
| `web/src/app/policy-draft/policy-question.html` | `05aace4e07dce9e04a94e1c1ba488e4664f94ace36aaaa771093816806b516ae` |
| `web/src/app/policy-draft/policy-question.scss` | `8343eb8407246e62aa31af9a7b5a0d3655e108f29c08c99bf771c81d445b33dc` |
| `web/src/app/policy-draft/policy-progress.ts` | `2cc9baf04f1c0486b19d90798955885f0b2d644ff115d5f8cdd241994a0fdcc0` |
| `web/src/app/policy-draft/policy-progress.html` | `8aecfacfd14c6c1689d419f8fc44c07f8579c48eb91551d0c2dbd41b9c095c77` |
| `web/src/app/policy-draft/policy-progress.scss` | `fdfbc9fe472e083fb12ec92aeaae75bc93cf2eaf0da954c766d28a9592ad06c2` |
| `web/src/app/policy-draft/policy-draft.ts` | `181831dba2ffba8455d48dfc8f06b23792ab8d8734565d4d9a71b2d6bcfbeb61` |
| `web/src/app/policy-draft/policy-draft.html` | `248befd05b80225e144af525098134946cb8cdd48e6d24e5912bc740c59a92a4` |
| `web/src/app/policy-draft/policy-draft.scss` | `1c2d3c22f5483b3ca2bf8af5444a215b4d182b8fae6c587c1526517e90e22862` |
| `web/src/app/policy-draft/policy-draft.spec.ts` | `93407223492e0dcfe8adc0b699225b0b9de26f315896d710fe9f39e32e558f68` |
| `web/src/app/policy-draft/policy-catalogue.ts` | `acde504fa6f0b815d93c66a842d1a25270092713ea898df97b9e8617388a6193` |
| `web/src/app/policy-draft/policy-source-details.html` | `3ebaf5bf8145005ad9706ce42bacd8660cffb15daf152ae4001da4ccf539fdb2` |
| `web/src/app/policy-draft/policy-source-details.ts` | `add8b2721004e120d71e7574d119bdd2ec84b5373c7b2b497d53e74e46a2f659` |
| `web/src/app/policy-draft/policy-source-details.scss` | `98ba630fb6527743e449750fbffde418f28b5993a208e37455205aec2c997f8b` |
| `web/src/styles.scss` | `695afc2c43f15dcaf4ad0406a3bf9910d7b6b7f610e4e52516b72f624ba8cf11` |
| `scripts/check-research-browser.mjs` | `3709963e5723cc39f1753131478070ec1c3083daf079219aaaa3115560fa02c6` |
| `scripts/check-research-engines.mjs` | `875c1f2ccce3efd3f30136ea4486c14a2ec453983359d8566635361f351ea9d5` |
| `scripts/check-review-schema.mjs` (Ausschnitt) | `2575997f720f0c440fc54a9ccc15a2bd8c8fb69638dab8c03cf8b9fdaf810166` |
| `scripts/check-handbuch.mjs` (grep) | `ebb9815ee0341fab5ad8aa58f01dec459dcdc08b75ca87f5a81707bab50e2813` |
| `web/src/app/research-preview/policy-preview.ts` | `c59ee36a05b1addfe8bac56f69df024865c89b3ee5137e75d927d43d183e6e1b` |
| `web/src/app/research-preview.routes.ts` | `d9bda2c42f9c8edec6f02ab7a3d5dd71df6c8e5afe91fe3f33f8b4e1d3bb341a` |
| `web/src/app/research-preview.routes.dev.ts` | `e8557fe29e2ae2d5dcff9dc93e9ac9709d1e82c501d84ff5c0401ed3a3ed121b` |
| `web/angular.json` (Ausschnitt) | `91c9042107b35de10321454587d64abbd7cd18cd25ea345319dd0378b8337ed8` |
| `web/src/app/research/policy-profile.ts` (Ausschnitt) | `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` |
| `web/src/app/policy-draft/display-additions.ts` | `3c8e4ab19577749d1cbb877dd1b13907911feab9f2c866ded64579db48de1565` |
| `web/src/app/policy-draft/catalogue-types.ts` (grep) | `2599cfdf5c77ed912a85926b4e37a025b7d3661d1085749d27dbb5dc8be42822` |
| `web/src/app/policy-draft/public-catalogue.ts` (ausgewertet) | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `web/src/app/policy-draft/public-catalogue-v22.ts` (ausgewertet) | `bc99055a10fb559cf2802d9a579ef3f07a3c8a77bdcc8556a2b08655d9d499cf` |
| `web/src/app/app.html` (grep) | `dac5494b1ad8339c9fca675ff09b243b4fb3dda9a286ab984f77bed40f6a56ac` |
| `web/src/app/art/art-gallery.spec.ts` (grep) | `352ebce33205985b7fa75f88f458750ad62acbe2778c68548a319312c0cd3291` |
| `package.json` (grep) | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` |
| `web/node_modules/@fontsource-variable/libre-baskerville/files/libre-baskerville-latin-wght-normal.woff2` (Laufweiten) | `22219fb90e3b9bd28debd1825fe8d9a0154a0e31f8b3fa601ac1a0a5aa5e6d1b` |

## Ausgeführte Befehle

- `sha256sum` für Auftrag, Manifest und alle gelesenen Dateien; Python-Abgleich aller 19 Manifesthashes.
- `git status --short`, `git log --oneline`, `git rev-parse`, `git diff --stat`, `git diff 9489579 -- …` für die vier Pfade aus dem Auftrag, `git show 9489579:…` für den Ausgangsstand von Template, Spec und Browserskript.
- `grep` nach Speicher-, Netzwerk- und URL-Aufrufen, H1, `forced-colors`, Fake-Timern, Budgets und Zeilennummern.
- `node --input-type=module -` mit Code über die Standardeingabe: Auswertung der Katalogliterale, Nachbau von Reihenfolge, Blöcken und Zahlenreihe, Zählung je Bereich. Keine Datei geschrieben.
- `python3` für WCAG-Kontraste und, mit fontTools 4.66.1, für Laufweiten der lokalen Schrift.
- `pnpm check` (Exit 0: Formatierung, Handbuch-Prüfung, Schema-Fixtures, Typen, 129 Tests in 10 Dateien, Build), Ausgabe nach `/tmp/u1-pnpm-check.log`.
- `pnpm check:review-schema` und eine Ajv-2020-Validierung dieses JSON-Urteils gegen das Schema (siehe JSON, Abschnitt `limits`).

## Modell laut Laufzeit

Anbieter Anthropic. Die Laufzeit nennt den Modellnamen Opus 5.5 (1M context) und die Kennung `claude-opus-5-5[1m]`. Das ist eine Laufzeitangabe, keine nachgewiesene interne Revision. Interne Vorgaben sind unbekannt. Werkzeuge: Bash, Read, Write, Skill `anthropic-skills:unslop` für den Berichtstext.
