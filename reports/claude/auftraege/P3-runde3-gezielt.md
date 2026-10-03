# Auftrag P3 Runde 3: abschließende gezielte Nachprüfung vor der Festschreibung von Plan v2.2

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Dies ist eine **gezielte Korrekturprüfung** einzelner offener Punkte, kein Gesamtaudit.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/PLAN-V22-003-manifest.json`, SHA-256 `6a575293673604ed52c83403f86a0b9993b0ce6fefaf929e1e1077a3bdfcde2c`. Prüfe zuerst die Hashes. Der Koordinator ändert während deiner Prüfung keine Dateien dieses Manifests. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema und folge ihnen.

Offene Punkte aus Runde 2 (Berichte `reports/claude/pruefungen/P1-runde2-v22.*` und `P2-runde2-v22.*`): P1-V22-F01, P1-V22-F02, P1-V22-F04, P1-V22-F08, P1-V22-F10 und P2-V22-F01. Abschnitt 9 „Runde 2“ in `docs/analyseplan-v2.2.md` beschreibt die Korrekturen.

Aufgabe: Prüfe je Punkt anhand der tatsächlichen Dateien und mit synthetischen Tests, ob das in Runde 2 beschriebene Restproblem aufgelöst ist. Status je Punkt: BEHOBEN, TEILWEISE oder NICHT_BEHOBEN mit Beleg. Melde neue Probleme nur, wenn die Korrektur sie verursacht hat oder sie die Festschreibung erheblich gefährden.

Regeln: Schreibe nur `reports/claude/pruefungen/P3-runde3-v22.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags, Nachrichten. Nichts unter `data/raw/` oder `data/local/` lesen, `pipeline/v22/run_v22.py` nicht als Kommandozeile ausführen, keine Antwortverteilungen lesen (`data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`). Synthetische Tests und Gegenproben unter `/tmp` sind erlaubt. Die Angular-Tests laufen mit `pnpm --filter politikprofil test --watch=false`, die Python-Tests mit `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -p 'test_*.py'`.

Ausgabe: Bericht und JSON-Urteil. Gesamturteil BESTANDEN nur, wenn kein erhebliches Finding offen bleibt. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
