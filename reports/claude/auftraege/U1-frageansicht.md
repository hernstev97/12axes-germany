# Auftrag U1: Prüfung der neuen Frageansicht im Forschungsentwurf

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude hat am 5. Oktober 2026 nach Stevens Vorgabe die Frageansicht des lokalen Forschungsentwurfs neu gestaltet. Die Frage steht mittig in einer Karte, darüber Position, Fortschrittsbalken und ein Schalter für den automatischen Wechsel nach einer Antwort. Herkunft und Quellen stehen unter der Karte. Das Überspringen mit Grund bleibt. Prüfe dieses Oberflächenpaket. Du prüfst keine Fragenauswahl, keine Vergleichswerte und keine Methodik.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/UI-FRAGEANSICHT-001-manifest.json`; seinen SHA-256 nennt die Nachricht des Auftraggebers. Prüfe vor Beginn die Hashes. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema. Modus: Paketprüfung. Den Unterschied zum Ausgangsstand zeigt `git diff 9489579 -- web/src/app/policy-draft/ scripts/check-research-browser.mjs scripts/check-research-engines.mjs docs/handbuch.md`.

Stevens Vorgabe im Wortlaut steht in `docs/ki-protokoll.md`, Abschnitt „2026-10-05“. Maßgeblich für Gestaltung und Texte ist `docs/handbuch.md`, für Inhalt und Daten `AGENTS.md`.

Checks:

- C01 Inhalt unverändert. Fragewortlaut, Antwortlisten, Einleitungen, Definitionen, Situationsbeschreibungen, Entwicklungshinweis und Quellenangaben werden unverändert aus dem Katalog angezeigt. Bei der Zeilendarstellung der 0–10-Listen bleibt der vollständige Text jeder Antwort ihr zugänglicher Name.
- C02 Automatischer Wechsel. Er ist vor der ersten Auswahl angekündigt (WCAG 2.2, 3.2.2). Pfeiltasten wählen nur aus. Klick, Tippen, Leertaste und Eingabetaste bestätigen. Nach der letzten Frage wechselt die Ansicht nicht. Zurücksetzen, Navigation und Ausschalten brechen einen laufenden Wechsel ab. Der Fokus geht auf die Fragenüberschrift. Es entsteht kein doppelter Sprung.
- C03 Barrierefreiheit im Code. Rollen und Namen von Schalter, Fortschrittsbalken, Radios, `fieldset` und `legend`; gültige `aria-describedby`-Bezüge; sichtbarer Fokus; Zielgrößen; Kontrast der neu eingesetzten Farbpaare; Darstellung im Modus für erzwungene Farben; keine Bewegung beim Wechsel.
- C04 Handbuch. Nur Variablen aus `styles.scss`, keine neuen Farben oder Schriften, keine verbotenen Muster aus Kapitel 1 und 7. Schaltflächentexte nennen das Ziel. Die neue Musterbeschreibung in Kapitel 4 stimmt mit der Umsetzung überein.
- C05 Neutrale Darstellung. Keine Antwort wird durch Farbe, Symbol, Reihenfolge oder Hervorhebung bevorzugt oder abgewertet. Hervorgehoben ist nur die eigene Auswahl.
- C06 Datenschutz. Antworten und Schalterzustand bleiben im Arbeitsspeicher. Kein Speichern, keine Anfrage, keine URL-Änderung.
- C07 Tests und Prüfskripte. Die neuen Unit-Tests decken das Verhalten aus C02 ab. Die Änderungen an `scripts/check-research-browser.mjs` und `scripts/check-research-engines.mjs` schwächen keine bestehende Prüfung ab.

Regeln: Schreibe nur `reports/claude/pruefungen/U1-frageansicht.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten. Nichts unter `data/raw/`, `data/local/`, `data/reference-*` oder `outputs/` lesen. Die Dateien `web/src/app/policy-draft/reviewed-*.ts` enthalten Vergleichswerte und gehören nicht zum Gegenstand. Du darfst `pnpm check` ausführen. Browser- und Datenskripte führst du nicht aus. Die Browserbeobachtungen des Autors stehen in `docs/validation.md`, Abschnitt „5. Oktober 2026“; sie sind Angaben des Autors, keine eigene Prüfung.

Ausgabe: Bericht und JSON-Urteil nach dem Schema mit Checks C01 bis C07 und gegebenenfalls Findings mit IDs U1-F01 usw. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
