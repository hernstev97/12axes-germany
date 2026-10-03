# Auftrag P5: Prüfung des Planentwurfs v2.3 – Quellen, Konstrukte und Fairness

Du bist ein frischer, getrennter Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude (Anthropic) hat einen Entwurf für einen Analyseplan v2.3 geschrieben: Erweiterung um Erhebungen der Jahre 2024 bis 2026, Wählergruppen nach der Bundestagswahl 2025 und Quellenentscheidungen. Der Entwurf erlaubt noch keine Auswertung. Deine Rolle: **Quellen, Konstrukte, Interpretationen und politische Fairness**. Eine zweite Rolle prüft getrennt Methoden und Reproduzierbarkeit. Du erhältst deren Urteil nicht.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/PLAN-V23-001-manifest.json`; seinen SHA-256 nennt die Nachricht des Auftraggebers. Prüfe vor Beginn die Hashes der dort genannten Dateien. Lies `.claude/skills/life93-review/SKILL.md` und `.claude/skills/life93-review/references/urteil-schema.json` und folge ihnen (Modus: Prüfung eines Planentwurfs vor der Festschreibung).

Regeln:
- Schreibe nur `reports/claude/pruefungen/P5-quellen-fairness-v23.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten.
- Lies nichts unter `data/raw/`, `data/local/` oder `outputs/`. Lies keine Antwortverteilungen und öffne keine Ergebnistabellen externer Quellen. Keine Abrufe von GESIS-Servern. Primärquellen außerhalb von GESIS (Gesetze, Lizenzen, Methodendokumente) darfst du öffnen.
- Belege jede Beanstandung mit Datei und Zeile oder Fundstelle. Kein Finding erfinden.

Prüffragen:
1. Stimmen die Rechtsaussagen (Klassen A, B, C nach R10) für die Quellen, auf die sich der Entwurf stützt, an der Primärquelle? Ist die GESIS-Sperre eingehalten?
2. Sind Konstrukt und Geltungsbereich jedes Kandidaten in Abschnitt 11 richtig beschrieben (EU-Ebene, Entscheidung Deutschlands, Prinzip, Zahlungsbereitschaft)? Sind Prämissen, wertende Begriffe und eingeblendete Informationen erkannt? Sind die Ausschlussgründe für nicht vorgeschlagene Fragen gleich streng auf alle politischen Richtungen angewendet?
3. Ist die Auswahl politisch ausgewogen in dem Sinn, dass keine Richtung durch die Wahl der Items, Formulierungen oder Antwortformate bevorzugt wird? Gibt es einseitige Zustimmungsaussagen ohne Gegenposition, deren Auswahl eine Richtung begünstigt? Nenne konkrete, belegte Fälle, keine allgemeinen Vermutungen.
4. Trennen Plan, Themenabdeckung (Nachträge vom 3. und 4. Oktober 2026) und Entscheidungsvorlage geltende Rechtslage, Vorschläge und Einstellungen korrekt? Stimmen die genannten Gesetze, Daten und Stände an der Primärquelle (Stichproben genügen)?
5. Ist die Entscheidungsvorlage fair und vollständig, sind ihre Empfehlungen begründet? Fehlt eine wesentliche Option?
6. Was muss vor einer Festschreibung korrigiert werden, was darf als offene Grenze bleiben?

Ausgabe: Bericht als Markdown und Urteil als JSON nach dem Skill-Schema. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
