# Arbeitsloop für LIFE-93

Der [dauerhafte Auftrag](auftrag-life-93-2026-10-03.md) umfasst alle Phasen von LIFE-93. Die ergänzende Sicherungsanweisung verlangt Commits und verifizierte Pushes auf den eigenen Arbeitsbranch nach jedem abgeschlossenen Paket und spätestens alle 30 Minuten mit Änderungen. Unfertiges heißt WIP. Kein Push auf main, Force-Push oder automatischer Merge.

## Wiederaufnahme

Zuerst den Auftrag, AGENTS.md, docs/project.md, diesen Plan, reports/loop/state.json und reports/loop/findings.json lesen. Den tatsächlichen Git-Stand, manifestegebundene Prüfungen und laufende Agents abgleichen. Nur ein Koordinator darf den gemeinsamen Zustand schreiben. Frühere Findings behalten ihre IDs und Reparaturrunden. Eine Unterbrechung setzt fehlende Zugänge oder Abnahmen nicht zurück.

Arbeitsfassung: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`. Der ursprüngliche Arbeitsbaum enthält unverändert die vorherige uncommittete Recherche. Eine zusätzliche Sicherung liegt dort unter `outputs/loop/bootstrap-20261003T010447Z/`. Rohdaten sind im Worktree nur verknüpft und bleiben unveröffentlicht. Ein vorhandener Link ist keine Analysefreigabe.

## Verfahren je Paket

1. Aufgaben, freigegebene Eingaben, Artefakte und Abnahmekriterien vor Durchführung im Zustand festhalten.
2. Abgegrenzte Arbeit ausführen. Autoren schreiben getrennte Dateien. Neue tragende Aussagen benötigen Originalfundstellen und Beleg-IDs.
3. Prüfpaket einfrieren: Commit, Datei-Hashes, Plan-/Quellen-/Datenversionen, Rohdateihash, Modellkonfiguration und Outputs. Keine Antwortdaten in öffentliche Pakete.
4. Mindestens zwei passende echte Reviewer mit frischem Kontext prüfen die unveränderte Fassung, ohne andere Urteile oder Autorenverteidigung. An den vier großen Forschungsabnahmen fünf Reviewer in getrennten Wellen, anschließend ein bislang unbeteiligter Juror.
5. Erst nach vollständigen Erstberichten zusammenführen. Jedes Finding mit belegter Annahmeentscheidung bearbeiten; betroffene Rechnungen wiederholen. Erhebliche Korrekturen unabhängig nachprüfen. Nach zwei strittigen Runden begrenzen, Unsicherheit sichtbar machen oder betroffene Funktion ausschließen und diese Änderung prüfen.
6. Zustand, Findings, Belegregister, Entscheidungen und Phasenbericht fortschreiben. Abnahmen gelten nur für ihre geprüften Manifeste. Arbeitspaket committen, eigenen Branch pushen, Remote-Commit vergleichen und im Zustand erfassen.

## Status und Grenzen

Prüfungen: BESTANDEN, NICHT_BESTANDEN, NICHT_GEPRÜFT, BLOCKIERT, IN_DIESER_PHASE_NICHT_ERFORDERLICH. Loop: RUNNING, BLOCKED, READY_FOR_APPROVAL, WAITING_FOR_HUMAN_TEST, DONE. Eine formale Kontrolle bestätigt keine Validität oder Neutralität. Geplante Prüfungen gelten nicht als ausgeführt.

Die aktuelle LIFE-93-Fassung wird unter reports/loop/issue-2026-10-03.\* gesichert. Das bestehende KI-Audit mit fünf Erstprüfern und Juror bleibt erhalten. Es bestätigt seine jeweiligen Forschungsfassungen, nicht automatisch die inzwischen zusammengeführte UI oder neue Forschung. Alle zugänglichen Codex-Subagents gehören laut Laufzeit zu GPT-6.1-Sol; interne Modellrevisionen und Anbieterregeln sind unbekannt.

Claude-Erstbewertungen, Claude-Review und Setup-Abnahme sind nicht ausgeführt. Der neue Auftrag hebt diese Voraussetzungen ausdrücklich nicht auf. Öffentliche Quellenarbeit, vollständige Inventarisierung, Themenrahmen, Planentwürfe und rohempiriefreie Infrastruktur können weitergehen. Keine endgültigen Items, ESS-Modellläufe, B-Zugriffe oder Entblindung ohne ihre Voraussetzungen. Kein persönlicher Statistiktermin wird zusätzlich eingeführt.

Das UI/UX-Handbuch liegt als docs/handbuch.md vor und wurde vollständig gelesen. Die von main übernommene UI bleibt erhalten. Fachliche Grenzen gehen vor Darstellung; fehlende Messbefunde werden nicht durch Texte oder Grafiken ersetzt. Designentscheidungen, persönliche Releasefreigabe und menschlicher Verständnistest bleiben echte Voraussetzungen.

## Erste Pakete

| Paket                                              | Artefakte                                                                                                                             | Vorab festgelegte Abnahme                                                                                                                                                                                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| LOOP-000: main und Zustand                         | Sicherungsmanifest, Merge, Integritätsbeleg, Auftrag und Loopzustand                                                                  | Ausgangsarbeit erhalten; sämtliche main-Webdateien und Handbuch unverändert übernommen; Konflikte nachvollziehbar gelöst; lokale Technik und zwei unabhängige Integrationsprüfungen                                |
| LOOP-001: Quellenbestand und Theorie               | Originalfrageninventar als Entwurf, Quellen-/Fundstellenregister, Deutschland-Themenrahmen und konkurrierende Erwartungen als Entwurf | Keine Rohantwortanalyse; Wortlaute und Kodierungen aus offiziellen Quellen; Fundstellen und Parserprüfungen; mindestens zwei unabhängige Berichte je relevantem Teil; getrennte Claude-Urteile weiterhin offen     |
| LOOP-002: Analyseplan und Sicherheitsinfrastruktur | Begründete konkrete Planparameter als Entwurf; kontrollierte Zugriffe und synthetische technische Tests                               | Quellenbezogene Methodenprüfung, konkrete Entscheidung/Folge für jedes Gate; fünf Fachreviews und neuer Juror für die große Planabnahme; fehlende Claude-/Setup-Prüfung blockiert abhängige empirische Entwicklung |

Weitere Pakete werden konkretisiert, sobald die jeweiligen Voraussetzungen vorliegen. Der Morgenbericht hält erledigte Arbeit, tatsächliche Prüfungen, Korrekturen, Grenzen und die kleinste benötigte menschliche Handlung fest.
