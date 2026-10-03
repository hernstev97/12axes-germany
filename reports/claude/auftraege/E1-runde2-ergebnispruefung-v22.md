# Auftrag E1 Runde 2: Nachprüfung der v2.2-Kandidaten und Prüfung der ESS5/ESS8-Bereiche

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Plan v2.2 ist mit dem Tag `analyseplan-v2.2` (Commit `b6af9a472c71ade865543cf75100c44a164ee12d`) festgeschrieben. Die erste Ergebnisprüfung E1 (`reports/claude/pruefungen/E1-ergebnis-v22.md` und `.json`) war NICHT_BESTANDEN mit den Findings E1-V22-F01 bis F03. Claude hat den Export daraufhin umgebaut. Außerdem liegen jetzt die SDDF-Dateien für ESS5 und ESS8 vor. Nach Plan 4.1 erhalten diese Studien Bereiche nach demselben Verfahren ohne neuen Plan, sofern jeder deutsche Fall über `idno` genau einer Designzeile zugeordnet wird. Du prüfst beides vor dem Export. Die Fragenauswahl ist nicht Gegenstand.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema und folge ihnen. Modus: gezielte Nachprüfung der E1-Findings (Runde 2) und Ergebnisprüfung der neuen ESS5/ESS8-Bereiche. Dieser Auftrag ist das Umfangsmanifest. Seinen SHA-256 nennt die Nachricht des Auftraggebers außerhalb dieser Datei. Die Findings und Urteile aus E1 Runde 1 darfst und sollst du lesen.

## Prüfgegenstand

- Neue Kandidatenfassung: `outputs/claude/v22-candidate-2/{ESS5e03_6,ESS8e02_3,ESS9e03_3,ESS10SCe03_2,ESS11e04_2}.json` und der aggregierte Zellnachweis `outputs/claude/v22-candidate-2/zellnachweis.json`. Soll-SHA-256:
  - `ESS10SCe03_2.json`: `2f79c5def38e0dc4a9bb8c199256e939a713f745b5e8b4db97ec4339aa069c42`
  - `ESS11e04_2.json`: `5e8acdee4c151d9e223828d7b6ac49a885a5903f58965b281d22d40397375af3`
  - `ESS5e03_6.json`: `454e500f7642a3abc138b121305e929265a8019f426fe8ddd0728ab6fdc74bb7`
  - `ESS8e02_3.json`: `b61d3f66ee660bcbc062c0b7278dbb9f507f9df58fea4f7ca8c6663d0d8b5d4b`
  - `ESS9e03_3.json`: `de294c01a673878cdca7f9a24c7c3574ab913178247a00c2500be79fc8427c2e`
  - `zellnachweis.json`: `67d03502b85ad0f8b01f7cf9ae28dc4bfa5977c6ad322337c8ef883afbbcd2b9`
- Laufbeleg mit den Abschnitten `designRun` und `candidateExportRound2`: `reports/claude/v22-laufbeleg.json`.
- Code: `pipeline/v22/export_v22.py`, `pipeline/v22/run_v22_sddf.py`, `pipeline/v22/sav.py`, `pipeline/v22/survey.py`, `pipeline/v22/run_v22.py` und die Tests `pipeline/v22/test_*.py`.
- Unabhängige Gegenprobe: `reports/claude/kontrollrechnung/sddf_gegenprobe.py` und `sddf-gegenprobe.json`.
- Plan und Bindung: `docs/analyseplan-v2.2.md`, `data/politikprofil-v2.2.ergaenzung.json`, `data/analysevertrag.v2.entwurf.json`, `data/gruppenvertrag.v2.1.entwurf.json`.
- Zum Abgleich: `data/reference-v2/*.json`, `data/reference-groups-v21/*.json` und die erste Kandidatenfassung `outputs/claude/v22-candidate/*.json`.

## Regeln

Schreibe nur `reports/claude/pruefungen/E1-runde2-ergebnis-v22.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten. Nichts unter `data/raw/` oder `data/local/` lesen oder ausführen, was diese Dateien liest. Keine Werte zurückgehaltener Referenzen erschließen oder berichten. Du darfst die Python-Tests mit `python3 -m unittest discover -s pipeline/v22 -t .` ausführen. Sie lesen keine Befragungsdaten.

## Prüffragen

1. E1-V22-F01: Trägt jede Referenz mit Zahlen den Status `prepared_pending_result_review`? Haben alle anderen `reference = null`? Setzt der Code `reviewed_historical_reference` nur in der Stufe `release` mit einer an beide privaten Läufe und alle Kandidatenhashes gebundenen Entscheidung?
2. E1-V22-F02: Folgen die Kategorien jeder Referenz und jedes Paares exakt `apiValidCodeOrder` (neue Fragen) beziehungsweise `categoryCodes` im Analysevertrag (v2-Fragen)? Sind die Anteile je Code gegenüber der ersten Kandidatenfassung unverändert?
3. E1-V22-F03: Passt der Zellnachweis zu den Kandidaten (gleiche Menge vorbereiteter Referenzen, gleiche `validCount`, Bindung an die Hashes)? Hält jede vorbereitete Referenz 100 gültige Antworten und mindestens fünf Fälle je positiver Kategorie, und summieren sich die Häufigkeiten zu `validCount`? Enthält der Nachweis nur vorbereitete Referenzen?
4. ESS5/ESS8-Design: Ist die Bedingung aus Plan 4.1 im Code geprüft (vollständige Eins-zu-eins-Zuordnung, sonst kein Bereich)? Ist die Behandlung von PSU und Stratum richtig? Ist es planmäßig, dass `PROB` nicht verwendet wird? Prüfe die Anmerkungen im Laufbeleg. Ist der SPSS-Leser für die genutzten Merkmale tragfähig (Tests, Formatregeln)?
5. ESS5/ESS8-Bereiche: Liegen alle Bereiche in [0, 1] und enthalten ihren Anteil? Passen die Freiheitsgrade zu Strata und PSUs? Fehlen Bereiche nur bei Anteil 0 oder 1? Sind die Breiten im Verhältnis zur Fallzahl plausibel (grober Designeffekt wie in E1, ohne neue Schwellen)? Ist die Gegenprobe wirklich unabhängig genug, und was deckt sie nicht ab?
6. Bekannte Werte: Stimmen die Anteile der in v2 und v2.1 veröffentlichten Einzelreferenzen und Gruppenpaare (jetzt auch die v2.1-Paare von ESS5 und ESS8) mit den veröffentlichten Dateien überein? Stimmen Status und Gruppendefinitionen?
7. Ist es planmäßig, dass jetzt auch die bereits veröffentlichten Paare von ESS5 und ESS8 mit Bereich exportiert werden (Plan 4.1: „jeder veröffentlichte Kategorienanteil einer Einzelreferenz und eines Gruppenpaares, dessen Studie ein vollständiges Stichprobendesign enthält“)?
8. Empfiehl ausdrücklich, welche Einzelreferenzen und Paare exportiert werden dürfen und welche nicht, mit Grund, und nenne die Liste so, dass sie direkt in eine Exportentscheidung übernommen werden kann.

Ausgabe: Bericht und JSON-Urteil. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
