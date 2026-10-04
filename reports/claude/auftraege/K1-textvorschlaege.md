# Auftrag K1: inhaltliche Prüfung der Textvorschläge

Du bist ein frischer Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude hat am 4. Oktober 2026 Vorschläge für offene Beschriftungen und sachlich problematische Pflichttexte geschrieben (`docs/vorschlaege-texte-v1.entwurf.md`). Eine frühere technische Prüfung (T2) hat dort nur Fundstellen und Zitate geprüft. Du prüfst den Inhalt der Vorschläge. Steven entscheidet später über die Übernahme. Deine Prüfung ist ein KI-Review, keine Abnahme.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/TEXTE-V1-001-manifest.json`; seinen SHA-256 nennt die Nachricht des Auftraggebers. Prüfe vor Beginn die Hashes. Lies `.claude/skills/life93-review/SKILL.md` und das Urteilsschema und folge ihnen. Modus: Paketprüfung.

## Prüffragen

1. **Sachliche Richtigkeit.** Behauptet ein vorgeschlagener Text etwas, das Profilregeln v1, Plan v2.2 oder die Website nicht tragen? Behebt jeder Vorschlag das genannte Problem tatsächlich? Stimmt die Begründung zu „repräsentativ“ mit der verlinkten ESS-Seite überein?
2. **Untertitel der Bereiche (Abschnitt 5).** Beschreibt jeder Untertitel die Fragen des Bereichs im Katalog (`policy-catalogue.ts`, `area-scope.ts`) vollständig genug und ohne Wertung? Benennt er einen Gegenstand, den keine Frage misst, oder lässt er einen wesentlichen weg? Sind die Untertitel über die Bereiche hinweg gleich sachlich formuliert?
3. **Handbuch.** Folgen alle vorgeschlagenen Texte `docs/handbuch.md`, besonders Abschnitt 7 (Haltung, ehrlicher Status, Begriffe, verbotene Muster, Typografie, Metadaten, Pflichttexte)? Keine direkte Anrede, kein generisches Maskulinum, keine Semikolonketten. Länge der Meta-Beschreibung nach 7.6.
4. **Grenzen des Auftrags.** Führt ein Vorschlag neue Achsen, Gesamtwerte, politische Etiketten, Designrichtungen oder Gestaltungsmuster ein? Ist klar, dass Steven entscheidet und nichts umgesetzt ist?

## Regeln

Schreibe nur `reports/claude/pruefungen/K1-textvorschlaege.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten. Nichts unter `data/raw/`, `data/local/`, `outputs/` oder `data/reference-*` lesen. Keine Antwortverteilungen. Die ESS-Seite zur Stichprobenziehung darfst du öffnen. Keine GESIS-Server.

Ausgabe: Bericht und JSON-Urteil mit Findings nach Schema. Für jedes Finding eine konkrete, überprüfbare Korrektur. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
