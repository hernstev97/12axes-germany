# Auftrag P4: Prüfung des Planentwurfs v2.3 – Methoden und Reproduzierbarkeit

Du bist ein frischer, getrennter Prüfagent (Codex, OpenAI) im Projekt „12 Axes Deutschland“ (Linear LIFE-93). Claude (Anthropic) hat einen Entwurf für einen Analyseplan v2.3 geschrieben: Erweiterung um Erhebungen der Jahre 2024 bis 2026, Wählergruppen nach der Bundestagswahl 2025 und eine Entscheidung zur Sichtbarkeit von Gruppenvergleichen. Der Entwurf erlaubt noch keine Auswertung. Deine Rolle: **Methoden und Reproduzierbarkeit**. Eine zweite Rolle prüft getrennt Quellen, Konstrukte und politische Fairness. Du erhältst deren Urteil nicht.

Arbeitsverzeichnis: `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`, Branch `research/life-93-claude-20261003`. Prüffassung: Manifest `reports/claude/pruefungen/PLAN-V23-001-manifest.json`; seinen SHA-256 nennt die Nachricht des Auftraggebers. Prüfe vor Beginn die Hashes der dort genannten Dateien. Lies `.claude/skills/life93-review/SKILL.md` und `.claude/skills/life93-review/references/urteil-schema.json` und folge ihnen (Modus: Prüfung eines Planentwurfs vor der Festschreibung).

Regeln:
- Schreibe nur `reports/claude/pruefungen/P4-methoden-v23.md` und `.json`. Keine anderen Dateien ändern, keine Commits, Tags oder Nachrichten.
- Lies nichts unter `data/raw/`, `data/local/` oder `outputs/`. Lies keine Antwortverteilungen (`data/reference-*`, `reports/phasen/02-*` bis `04-*`, `web/src/app/policy-draft/reviewed-*`). Öffne keine Ergebnistabellen externer Quellen.
- Belege jede Beanstandung mit Datei und Zeile oder Fundstelle. Kein Finding erfinden.

Prüffragen:
1. Sind die Quellenklassen Z, T und Q (Abschnitt 3) und ihre Anzeigeregeln (Abschnitt 6) methodisch begründet und vollständig? Ist der Verzicht auf Unsicherheitsbereiche bei Klasse T ohne veröffentlichtes Design richtig, oder gibt es ein vertretbares, vorab festlegbares Verfahren? Ist die zweifache unabhängige Übertragung der Tabellenwerte ausreichend beschrieben?
2. Sind die Auswahlregeln (Abschnitt 4) vor Ergebnissen festgelegt, prüfbar und auf die Kandidaten in Abschnitt 11 tatsächlich angewendet? Ist die Trennung von Auswahlrolle und technischer Rolle (Abschnitte 4 und 10, Strukturprüfung S1) wirksam, oder gibt es Wege, auf denen Verteilungen die Auswahl beeinflussen?
3. Regeln für historische und aktuelle Vergleiche und getrennte Populationen (Abschnitte 3 und 5): Verhindern sie Zusammenlegung, Trendaussagen und Verwechslung der Populationen?
4. Wählergruppen 2025 (Abschnitt 7): Reichen die Bedingungen für ESS12 (Rückerinnerung, Modi, Codekonkordanz, Gruppenvertrag vor Einsicht)?
5. Sichtbarkeit der Gruppenvergleiche (Abschnitt 8): Stimmen die Zählungen aus den öffentlichen Status? Ist die Bewertung der Optionen A bis C methodisch richtig, insbesondere das Rückrechnungsrisiko bei Option B?
6. Was muss vor einer Festschreibung korrigiert werden, was darf als offene Grenze bleiben?

Ausgabe: Bericht als Markdown und Urteil als JSON nach dem Skill-Schema. Am Ende: gelesene Dateien mit Hash, ausgeführte Befehle, Modell laut Laufzeit.
