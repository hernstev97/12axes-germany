# Auftrag E1: Ergebnisprüfung der v2.2-Referenzen vor dem Export

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Plan v2.2 ist mit dem Tag `analyseplan-v2.2` (Commit `b6af9a472c71ade865543cf75100c44a164ee12d`) festgeschrieben. Claude hat danach den privaten Lauf ausgeführt und einen Kandidatenexport erzeugt. Laut Plan, Abschnitt 8.3, prüft ein frischer Prüfagent die Ergebnisse vor dem Export. Du bist diese Prüfung. Es ist keine Prüfung der Fragenauswahl mehr; diese ist festgeschrieben.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema und folge ihnen.

Prüfgegenstand:
- Kandidatenexport (zusammengefasste Werte, nur vorbereitete Referenzen tragen Zahlen): `outputs/claude/v22-candidate/{ESS5e03_6,ESS8e02_3,ESS9e03_3,ESS10SCe03_2,ESS11e04_2}.json`. SHA-256 stehen in `reports/claude/v22-laufbeleg.json` unter `candidateExport`.
- Laufbeleg: `reports/claude/v22-laufbeleg.json`.
- Plan und Bindung: `docs/analyseplan-v2.2.md`, `data/politikprofil-v2.2.ergaenzung.json`, `data/gruppenvertrag.v2.1.entwurf.json`, `pipeline/v22/export_v22.py`, `pipeline/v22/survey.py`.
- Zum Abgleich der bekannten Fragen darfst du jetzt die veröffentlichten v2-Dateien `data/reference-v2/*.json` und `data/reference-groups-v21/*.json` lesen.

Regeln: Schreibe nur `reports/claude/pruefungen/E1-ergebnis-v22.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags, Nachrichten. Nichts unter `data/raw/` oder `data/local/` lesen. Keine Werte zurückgehaltener Referenzen erschließen oder berichten.

Prüffragen:
1. Tragen nur Referenzen mit dem Status `prepared_pending_result_review` Zahlen? Hält jede veröffentlichte Referenz die Regeln 100/5? Fehlen Gewichtssummen bei Missing-Gründen mit eins bis vier Fällen?
2. Summieren sich die Anteile zu 1? Passen Kategorien und Codes zum Katalog (einschließlich Code 55 bei den Energiequellen)?
3. Stimmen die Anteile der 42 bekannten Einzelreferenzen und 12 bekannten ESS9-Gruppenpaare mit den veröffentlichten v2-Dateien überein?
4. Intervalle: nur für ESS9, ESS10 Self-completion und ESS11; jeder Bereich liegt in [0, 1] und enthält seinen Schätzwert; Freiheitsgrade passen zu Strata und PSUs; keine Bereiche bei Anteil 0 oder 1. Sind Breiten im Verhältnis zur Fallzahl plausibel (Designeffekt grob prüfen, ohne neue Schwellen zu erfinden)?
5. Gruppenpaare: nur neue ESS5/ESS8-Fragen und ESS9-Intervalle, gleiche Gruppendefinitionen wie v2.1.
6. Gibt es Auffälligkeiten, die auf Kodier- oder Polungsfehler hindeuten (z. B. vertauschte Kategorien im Vergleich zu Wortlaut und Antwortliste)? Benenne sie mit Beleg. Inhaltliche Ergebnisse bewertest du nicht politisch.
7. Empfiehl ausdrücklich, welche Fragen und Paare exportiert werden dürfen und welche nicht, mit Grund.

Ausgabe: Bericht und JSON-Urteil. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
