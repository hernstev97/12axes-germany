# Auftrag T2 Runde 2: gezielte Nachprüfung der Findings T2-F01 bis T2-F05

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Die Paketprüfung T2 (`reports/claude/pruefungen/T2-technik-v22.md` und `.json`) war NICHT_BESTANDEN mit den Findings T2-F01 bis T2-F05. Claude hat sie in Commit `da10fdf` korrigiert. Prüfe gezielt, ob jedes Finding behoben ist, und ob die Korrekturen neue Fehler einführen. Keine vollständige neue Prüfung.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema. Modus: gezielte Nachprüfung (Runde 2). Dieser Auftrag ist das Umfangsmanifest; seinen SHA-256 nennt die Nachricht des Auftraggebers. Die Findings und das Urteil aus Runde 1 darfst und sollst du lesen.

Prüfgegenstand: `git diff 46e70be..da10fdf -- scripts/check-research-engines.mjs web/src/app/policy-draft/ reports/claude/kontrollrechnung/ docs/validation.md reports/claude/datenzugriff.md` und die neuen JSON-Ausgaben der Gegenproben unter `reports/claude/kontrollrechnung/`. `s1_struktur.py` gehört nicht zum Gegenstand.

Regeln: Schreibe nur `reports/claude/pruefungen/T2-runde2-technik-v22.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten. Nichts unter `data/raw/`, `data/local/` oder `outputs/` lesen und nichts ausführen, was diese Pfade liest. Du darfst `pnpm check` ausführen. Browser- und Datenskripte führst du nicht aus.

Ausgabe: Bericht und JSON-Urteil mit dem Stand jedes Findings (KORRIGIERT, TEILWEISE, OFFEN) und gegebenenfalls neuen Findings. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
