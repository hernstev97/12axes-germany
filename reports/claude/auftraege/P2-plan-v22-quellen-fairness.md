# Auftrag P2: Prüfung des Plans v2.2 – Quellen, Konstrukte, Interpretationen und politische Fairness

Du bist ein frischer, getrennter Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude (Anthropic) hat den Arbeitsstand von Codex übernommen und einen Plannachtrag v2.2 geschrieben. LIFE-93 verlangt für wesentliche Änderungen an Messmodell und Auswertung zwei getrennte Prüfungen mit unterschiedlichen Schwerpunkten, nach Möglichkeit durch einen frischen Codex-Prüfer. Deine Rolle: **Quellen, Konstrukte, Interpretationen und politische Fairness**. Eine zweite Rolle prüft getrennt Methoden und Reproduzierbarkeit. Du erhältst deren Urteil nicht.

Repository und Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/PLAN-V22-001-manifest.json`, SHA-256 `1d269e9ab4fa49d3ba5beec17a600d5b9bd58f3998611f2ffe5e8f842d739639`. Prüfe vor Beginn die Hashes der dort genannten Dateien.

Lies zuerst `.claude/skills/life93-review/SKILL.md` und `.claude/skills/life93-review/references/urteil-schema.json` und folge ihnen (Modus: Prüfung eines Plans vor der Festschreibung).

Regeln:
- Schreibe nur `reports/claude/pruefungen/P2-quellen-fairness-v22.md` und `reports/claude/pruefungen/P2-quellen-fairness-v22.json`. Keine anderen Dateien ändern, keine Commits, Pushes, Tags, Nachrichten.
- Lies nichts unter `data/raw/` oder `data/local/`. Lies keine Antwortverteilungen (`data/reference-v2/`, `data/reference-groups-v21/`, `reports/phasen/02-*`, `reports/phasen/03-*`, `web/src/app/policy-draft/reviewed-historical-*.ts`).
- Originalfragebögen liegen unter `outputs/loop/breadth-data-001/sources/` (z. B. mit `pdftotext -raw -f N -l N`). Die ESS10-Webfassung liegt als Bildschirmfotos in `ess10-de-questionnaire.pdf` ab etwa PDF-Seite 100; prüfe für die neuen ESS10-Fragen stichprobenartig, ob die Webfassung inhaltlich abweicht.
- Belege jede Beanstandung mit Datei und Zeile oder PDF-Seite. Kein Finding erfinden, um streng zu wirken. Gleiche Belegstandards für alle politischen Positionen.

Prüffragen:
1. Auswahl der 18 neuen Fragen (`docs/analyseplan-v2.2.md` Abschnitt 3): Sind Ein- und Ausschlüsse inhaltlich begründet? Begünstigt die Auswahl oder eine Auslassung systematisch eine politische Richtung (zum Beispiel durch die Wahl der Fragen zu Asyl, Autorität, Parteiverbot, Energiequellen, Lebensformen)? Fehlen naheliegende lokale ESS-Fragen, deren Auslassung begründet werden müsste?
2. Stimmen Wortlaute, Einleitungen, Definitionen und Antwortlisten in `data/politikprofil-v2.2.ergaenzung.json` mit den deutschen Originalen überein? Sind die Kontexthinweise (z. B. nicht vorgelesener Code 55, gedruckte Codes 0–5 bei Liste 31, Pandemiehinweis) korrekt?
3. Profilregeln und Texte (`docs/profilregeln-v1.md`, `web/src/app/policy-draft/profile/profile-rules.ts`, `profile-structure.ts`): Beschreiben Titel, Kontextmerkmale, Blockhinweise und Querbezüge nur, was die Fragen erfassen? Sind sie sprachlich symmetrisch für alle Antwortrichtungen? Legen Querbezüge oder Hinweise eine Deutung, ein Motiv oder einen „Widerspruch“ nahe? Sind Rechtsangaben (Kernkraft April 2023, Eheöffnung 2017) korrekt belegt oder sollten sie entfallen?
4. Themenabdeckung (`docs/abdeckung-v2.2.md`): Sind „Erfasst“, „Nicht erfasst“, Bewertung und Art der Lücke je Bereich zutreffend und für alle Bereiche nach gleichen Maßstäben formuliert? Stichprobenartig gegen R1–R3 prüfen.
5. Interpretationsgrenzen: Werden historische Vergleiche, Zeitbezüge und die Pandemiefragen so begrenzt, dass keine Gegenwartsnorm, Parteiposition oder Personeneigenschaft behauptet wird?
6. Was muss vor der Festschreibung korrigiert werden, was darf als offene Grenze bleiben?

Ausgabe: Bericht als Markdown und Urteil als JSON nach dem Skill-Schema. Am Ende des Berichts: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
