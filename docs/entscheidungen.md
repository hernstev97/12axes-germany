# Entscheidungen und Abweichungen

Stand 2026-10-03. Frühere Produkt-/Gestaltungsentscheidungen stehen in [project.md](project.md). Diese Einträge betreffen den Beginn der Forschung; sie ersetzen keine wissenschaftliche Abnahme.

| ID            | Entscheidung / Befund                                            | Herkunft                                                                                           | Konsequenz                                                                                                                                                                       |
| ------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E-20261003-01 | Forschung und Prüfregeln nach der Repository-Grundlage beginnen. | Steven: „okay dann fangen wir an.“                                                                 | Öffentliche Recherche und lokale Dokumentation auf `research/life-93-methodology`, Grundlage `1a7b0c3`.                                                                          |
| E-20261003-02 | „Vorerst nur CodeRabbit, methodische Freigabe bleibt offen“.     | Stevens Antwort auf die Review-Frage.                                                              | Keine Claude-Einrichtung und kein zusätzlicher Auftrag an eine andere Modellfamilie. Die strengeren Erstbewertungs-/Freigabeanforderungen bleiben unerfüllt, nicht abgeschwächt. |
| E-20261003-03 | ESS-Account ist inzwischen vorhanden.                            | Zunächst „Noch kein ESS-Konto“, anschließend: „ich habe jetzt einen account beim ess data portal“. | Frühere Zugangsangabe überholt. Keine Anmeldung oder stellvertretende Akzeptanz durchgeführt; spätere Downloadbedingungen dokumentieren.                                         |
| E-20261003-04 | Lizenzbegründung für den Ausschluss der Rohdaten präzisiert.     | Recherche-Agent, B-LIZ-001; keine neue Produktentscheidung.                                        | Rohdatenausschluss bleibt. Ein pauschales ESS-Lizenzverbot wird nicht behauptet; Daten-/Dokumentationslizenzen getrennt behandeln.                                               |
| E-20261003-05 | ESS11 Ausgabe 4.2 als recherchierter Kandidat festhalten.        | Recherche-Agent, B-ESS-001; methodische Entscheidung ausstehend.                                   | Kein Import/Modell aus einem Suchtreffer oder veralteten Zitationsbeispiel ableiten.                                                                                             |

## Abgleich mit LIFE-93

Gelesener Issue-Stand: `updatedAt 2026-10-02T22:07:24.510Z`. Die dortige Claude-Setup-/Action-Vorgabe wird durch Stevens neuere Entscheidung für diesen Arbeitsschritt nicht ausgeführt. Ein verpflichtender GitHub-Check namens `Claude-Review` wird nicht fingiert und nicht durch einen vermeintlich methodischen CodeRabbit-Check ersetzt.

Diese Recherche hat LIFE-93 nicht geändert. Der methodische Anspruch bleibt dokumentiert; die tatsächliche Einrichtung und erforderlichen Bewertungen sind offen. Der lokale Entwurf wurde weder veröffentlicht noch als Phase-0-Abschluss oder Präregistrierung ausgegeben.

## Nachtrag: ausdrücklich beauftragtes KI-Audit

- E-20261003-06: Steven beauftragt fünf echte, getrennte Erstprüfer und anschließend einen sechsten Juror. Ausführung über das verfügbare Subagent-Tool, gleiche zugängliche Modellfamilie; keine Claude-Einrichtung. Tatsächliche Aufträge, Input-/Berichtshashes und Toolgrenzen stehen im [Auditprotokoll](../reports/audit-recherche/agent-protokoll.json).
- E-20261003-07: Die pauschale zusätzliche Plan-Freigabe als Startbedingung war eine zu weitgehende eigene Auslegung. Phase 0 verlangt begründeten Plan und öffentlichen Tag; die getrennten Erstbewertungen gehören vor endgültige Auswahl/Modellarbeit. Keine fachliche Statistik-Abnahme durch Steven eingeführt. A-F01 dokumentiert Ausgangswortlaut, Belege, Änderung und Nachprüfung.
- E-20261003-08: R1-F01 und R4-F01 korrigieren Versionsreichweite und Parteiausschluss. Die übrigen übernommenen Methodik-/Inhaltsanforderungen bleiben bis zur tatsächlich ausgeführten Prüfung offen. Ein geänderter Regeltext erfüllt keine empirische Abnahme.
