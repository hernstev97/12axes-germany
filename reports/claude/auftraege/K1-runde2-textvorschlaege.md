# Auftrag K1 Runde 2: gezielte Nachprüfung der Textvorschläge

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Die inhaltliche Prüfung K1 der Textvorschläge (`reports/claude/pruefungen/K1-textvorschlaege.md` und `.json`) war NICHT_BESTANDEN mit den Findings K1-F01 bis K1-F05. Claude hat Entwurf 2 von `docs/vorschlaege-texte-v1.entwurf.md` geschrieben und Abschnitt 4 der Entscheidungsvorlage angeglichen. Abschnitt 7 der Vorschläge nennt die Korrekturen. Prüfe gezielt, ob jedes Finding behoben ist und ob die Korrekturen neue Fehler einführen. Keine vollständige neue Prüfung.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/TEXTE-V1-002-manifest.json`; seinen SHA-256 nennt die Nachricht des Auftraggebers. Prüfe vor Beginn die Hashes. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema. Modus: gezielte Nachprüfung (Runde 2). Den Unterschied zu Entwurf 1 zeigt `git diff bb760f3 -- docs/vorschlaege-texte-v1.entwurf.md docs/entscheidungsvorlage-erweiterung-v1.entwurf.md`.

Regeln: Schreibe nur `reports/claude/pruefungen/K1-runde2-textvorschlaege.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten. Nichts unter `data/raw/`, `data/local/`, `outputs/` oder `data/reference-*` lesen. Keine Antwortverteilungen, keine GESIS-Server.

Ausgabe: Bericht und JSON-Urteil mit dem Stand jedes Findings (KORRIGIERT, TEILWEISE, OFFEN) und gegebenenfalls neuen Findings. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
