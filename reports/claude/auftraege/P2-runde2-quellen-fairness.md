# Auftrag P2 Runde 2: gezielte Nachprüfung der Korrekturen am Plan v2.2

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Dies ist eine **gezielte Korrekturprüfung**, kein neues Gesamtaudit. Ein früherer Codex-Prüfer hat Fassung 1.0 des Plans v2.2 geprüft. Sein Bericht: `reports/claude/pruefungen/P2-quellen-fairness-v22.md` und `.json`. Claude hat danach Fassung 1.1 erstellt. Abschnitt 9 in `docs/analyseplan-v2.2.md` listet die Korrekturen.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/PLAN-V22-002-manifest.json`, SHA-256 `67506f10f9cfb2a56a352d7cec31f25671207fabd0aa421ca9fc88a3e4644eab`. Prüfe zuerst die Hashes. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema und folge ihnen.

Aufgabe: Prüfe für jedes Finding `P2-V22-F..` im früheren Bericht anhand der tatsächlichen Dateien, ob die Korrektur das belegte Problem auflöst. Status je Finding: BEHOBEN, TEILWEISE oder NICHT_BEHOBEN, mit Beleg (Datei und Zeile, ausgeführter synthetischer Test). Melde neue Probleme nur, wenn die Korrektur sie verursacht hat oder sie für die Festschreibung erheblich sind. Keine Wunschprüfungen.

Regeln: Schreibe nur `reports/claude/pruefungen/P2-runde2-v22.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags, Nachrichten. Nichts unter `data/raw/` oder `data/local/` lesen, `pipeline/v22/run_v22.py` nicht als Kommandozeile ausführen, keine Antwortverteilungen lesen (`data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`). Synthetische Tests und eigene Gegenproben unter `/tmp` sind erlaubt.

Ausgabe: Bericht und JSON-Urteil. Gesamturteil BESTANDEN nur, wenn kein erhebliches Finding offen bleibt. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
