# Auftrag P1: Prüfung des Plans v2.2 – Methoden und Reproduzierbarkeit

Du bist ein frischer, getrennter Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude (Anthropic) hat den Arbeitsstand von Codex übernommen und einen Plannachtrag v2.2 geschrieben. LIFE-93 verlangt für wesentliche Änderungen an Messmodell und Auswertung zwei getrennte Prüfungen mit unterschiedlichen Schwerpunkten, nach Möglichkeit durch einen frischen Codex-Prüfer. Deine Rolle: **Methoden und Reproduzierbarkeit**. Eine zweite Rolle prüft getrennt Quellen, Konstrukte und politische Fairness. Du erhältst deren Urteil nicht.

Repository und Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/PLAN-V22-001-manifest.json`, SHA-256 `1d269e9ab4fa49d3ba5beec17a600d5b9bd58f3998611f2ffe5e8f842d739639`. Prüfe vor Beginn die Hashes der dort genannten Dateien.

Lies zuerst `.claude/skills/life93-review/SKILL.md` und `.claude/skills/life93-review/references/urteil-schema.json` und folge ihnen (Modus: Prüfung eines Plans vor der Festschreibung).

Regeln:
- Schreibe nur `reports/claude/pruefungen/P1-methoden-v22.md` und `reports/claude/pruefungen/P1-methoden-v22.json`. Keine anderen Dateien ändern, keine Commits, Pushes, Tags, Nachrichten.
- Lies nichts unter `data/raw/` oder `data/local/`. Führe `pipeline/v22/run_v22.py` nicht aus. Synthetische Tests darfst du ausführen (`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest pipeline/v22/test_survey.py pipeline/v22/test_run_v22.py`) und eigene synthetische Gegenproben schreiben, aber nur unter `/tmp`.
- Lies keine Antwortverteilungen (`data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`).
- Belege jede Beanstandung mit Datei und Zeile oder Fundstelle. Kein Finding erfinden, um streng zu wirken.

Prüffragen:
1. Ist das Verfahren für Stichprobenunsicherheit in `docs/analyseplan-v2.2.md` Abschnitt 4 und `pipeline/v22/survey.py` korrekt umgesetzt und angemessen? Taylor-Linearisierung des Quotienten in Domänen, Behandlung von PSUs ohne gültige Antworten, Freiheitsgrade, xlogit-Intervall, Ausschlussbedingungen. Stimmt die Quellenangabe (survey-Handbuch, `outputs/loop/methods/SURVEY-MANUAL.pdf`, svyciprop S. 93–94)? Sind die dokumentierten Annahmen (feste Gewichte, keine Poststratifikation, mit Zurücklegen) ehrlich und vollständig benannt? Fehlt eine wesentliche Einschränkung?
2. Rechnet `pipeline/v22/run_v22.py` nach Plan und v2/v2.1-Verträgen: Deutschland-Filter, Prüfungen von Hash, Runde, Edition und Kennungen, Gewichte, Missing-Gründe, nicht gestellte Fragen, leere Exportzellen, Publikationsregeln 100/5, Gruppenzuordnung nach `data/gruppenvertrag.v2.1.entwurf.json`, Intervalle nur für vorbereitete Referenzen? Gibt es Wege, auf denen Zeilen, Kennungen oder kleine Zellen in Ausgaben gelangen? Ist die Sperre ohne Tag `analyseplan-v2.2` wirksam?
3. Ist der automatische Wortlautabgleich in `pipeline/v22/catalogue_v22.py` ein tatsächlicher Abgleich (kein Selbstvergleich)? Bindet er Codes und Missing-Gründe korrekt aus den Metadaten?
4. Sind Auswahlregeln (Abschnitt 3.1) vor Ergebnissen festgelegt und prüfbar? Ist die Darstellung früherer Kenntnis (Abschnitt 1) ehrlich?
5. Profilregeln (`docs/profilregeln-v1.md`, `web/src/app/policy-draft/profile/`): Sind sie deterministisch, reihenfolgeunabhängig und frei von verdeckten Rechenwerten? Decken die Tests die zugesagten Fälle ab?
6. Was muss vor der Festschreibung korrigiert werden, was darf als offene Grenze bleiben?

Ausgabe: Bericht als Markdown und Urteil als JSON nach dem Skill-Schema. Am Ende des Berichts: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
