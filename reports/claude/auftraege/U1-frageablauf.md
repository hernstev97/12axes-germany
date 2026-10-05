# Auftrag U1 (neu): Prüfung des Frageablaufs im Forschungsentwurf

Dieser Auftrag ersetzt `U1-frageansicht.md`. Die Prüfung nach dem alten Auftrag wurde abgebrochen, bevor ein Bericht entstand, weil Steven die Gestaltung am selben Abend erneut geändert hat.

Du bist ein frischer Prüfagent im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude hat am 5. Oktober 2026 nach zwei Vorgaben von Steven den Ablauf des lokalen Forschungsentwurfs neu gestaltet:

- Startbildschirm mit Titel, Einleitung, Speicherhinweis und „Zu den Fragen“.
- Eigener Einleitungsbildschirm vor jedem Block aufeinanderfolgender Fragen mit derselben Originaleinleitung.
- Fragebildschirm mit Fortschritt, Karte, Überspringen mit Grund und Quellen darunter.
- Automatischer Wechsel nach einer Antwort.

Prüfe dieses Oberflächenpaket. Du prüfst keine Fragenauswahl, keine Vergleichswerte und keine Methodik.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/UI-FRAGEANSICHT-002-manifest.json`; seinen SHA-256 nennt die Nachricht des Auftraggebers. Prüfe vor Beginn die Hashes. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema. Modus: Paketprüfung. Den Unterschied zum Ausgangsstand zeigt `git diff 9489579 -- web/src/app/policy-draft/ scripts/check-research-browser.mjs scripts/check-research-engines.mjs docs/handbuch.md`.

Stevens Vorgaben im Wortlaut stehen in `docs/ki-protokoll.md`, Abschnitt „2026-10-05“. Maßgeblich für Gestaltung und Texte ist `docs/handbuch.md` mit dem Abschnitt „Ablauf des Forschungsentwurfs“ in Kapitel 4. Für Inhalt und Daten gilt `AGENTS.md`.

Checks:

- C01 Inhalt unverändert. Fragewortlaut, Antwortlisten, Einleitungen, Definitionen, Situationsbeschreibungen, Entwicklungshinweis und Quellenangaben werden unverändert aus dem Katalog angezeigt. Keine Einleitung geht verloren. Jede Frage mit Einleitung erreicht ihre Einleitung entweder vorher auf dem Einleitungsbildschirm oder über „Einleitung zu dieser Frage anzeigen“. Die Blockbildung ist richtig. Bei der Zahlenreihe der 0–10-Listen bleibt der vollständige Text jeder Antwort ihr zugänglicher Name. Gedruckte Codes stammen aus dem Katalog und sind nicht erfunden.
- C02 Ablauf und automatischer Wechsel.
  - Start, Einleitung und Frage folgen wie im Handbuch beschrieben aufeinander.
  - Der automatische Wechsel ist vor der ersten Auswahl angekündigt (WCAG 2.2, 3.2.2).
  - Pfeiltasten wählen nur aus. Klick, Tippen, Leertaste und Eingabetaste bestätigen.
  - Nach der letzten Frage wechselt die Ansicht nicht von selbst.
  - Zurücksetzen, Navigation und Ausschalten brechen einen laufenden Wechsel ab. Es entsteht kein doppelter Sprung.
  - Der Fokus geht nach jedem Wechsel auf die Überschrift des neuen Bildschirms.
- C03 Barrierefreiheit im Code.
  - Genau eine H1 je Ansicht, auch die nur für Hilfsmittel lesbare H1 auf dem Fragebildschirm.
  - Rollen und Namen von Schalter, Fortschrittsbalken, Radios, `fieldset` und `legend`, dazu gültige `aria-describedby`-Bezüge.
  - Die Reihenfolge der Bedienelemente, vor allem „Auswahl zurücksetzen“ vor den Antworten.
  - Sichtbarer Fokus und Zielgrößen.
  - Kontrast der neu eingesetzten Farbpaare.
  - Die nur für Hilfsmittel lesbare Zählzeile auf schmalen Bildschirmen.
  - Darstellung im Modus für erzwungene Farben und keine Bewegung beim Wechsel.
- C04 Handbuch.
  - Nur Variablen aus `styles.scss`, keine neuen Farben oder Schriften und keine verbotenen Muster aus Kapitel 1 und 7.
  - Schaltflächentexte nennen das Ziel oder die Handlung.
  - Die Musterbeschreibung in Kapitel 4 stimmt mit der Umsetzung überein, einschließlich der begründeten Abweichung bei der ausgefüllten Schaltfläche nach vorn.
- C05 Neutrale Darstellung. Keine Antwort wird durch Farbe, Symbol, Reihenfolge oder Hervorhebung bevorzugt oder abgewertet. Hervorgehoben ist nur die eigene Auswahl.
- C06 Datenschutz. Antworten, Schalterzustand und gesehene Einleitungen bleiben im Arbeitsspeicher. Kein Speichern, keine Anfrage, keine URL-Änderung.
- C07 Tests und Prüfskripte. Die Unit-Tests decken Start, Einleitungen und automatischen Wechsel ab. Die Änderungen an `scripts/check-research-browser.mjs` und `scripts/check-research-engines.mjs` schwächen keine bestehende Prüfung ab.

Regeln:

- Schreibe nur `reports/claude/pruefungen/U1-frageablauf.md` und `.json`.
- Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten.
- Nichts unter `data/raw/`, `data/local/`, `data/reference-*` oder `outputs/` lesen.
- Die Dateien `web/src/app/policy-draft/reviewed-*.ts` enthalten Vergleichswerte und gehören nicht zum Gegenstand.
- Du darfst `pnpm check` ausführen. Browser- und Datenskripte führst du nicht aus.
- Die Browserbeobachtungen des Autors stehen in `docs/validation.md`, Abschnitt „5. Oktober 2026“. Sie sind Angaben des Autors, keine eigene Prüfung.

Ausgabe: Bericht und JSON-Urteil nach dem Schema mit den Checks C01 bis C07 und gegebenenfalls Findings mit den IDs U1-F01 usw. Am Ende stehen die gelesenen Dateien mit Hash, die ausgeführten Befehle und das Modell laut Laufzeit.
