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

## 2026-10-03: Vollauftrag und LOOP-000

Der gespeicherte Vollauftrag erweitert den Ausführungsumfang auf alle LIFE-93-Phasen, erhält aber deren methodische und menschliche Voraussetzungen. Keine erneute Beauftragung pro Phase erforderlich; keine automatische Veröffentlichung oder Merge. Eigenbranch-Checkpoints werden verifiziert gepusht.

Vier Integrationsfindings und der zusätzliche Lizenzsatzbefund wurden angenommen; Begründungen, Quellen und Nachprüfungen in reports/loop/LOOP-000-entscheidungen.md. Die Handbuchpräzisierung erlaubt, einen tatsächlich ausgeführten begrenzten Methodenreview zu benennen; daraus entstehen weder empirische Evidenz noch Abnahme. Erstberichte und Ausgangsmanifeste unverändert erhalten.

## 2026-10-03: Fortsetzung nach dem Haltepunkt

E-20261003-09: Steven ersetzt Claude als Voraussetzung der Hauptarbeit durch zwei getrennte Codex-Erstbewertungen und vereinfacht die Reviewstruktur. Der [datierte Nachtrag](auftrag-life-93-fortsetzung-2026-10-03.md) enthält den aktuellen Vertrag. Claude-Schlusskontrolle, menschliche Tests und Releasefreigaben bleiben ausstehend. Fachliche Anforderungen werden dadurch nicht als bestanden erklärt.

## 2026-10-03: konkreter Vor-A-Vertrag

E-20261003-10: Die getrennten Codex-Übergangsurteile und die gezielte erste Korrekturrunde tragen den begrenzten Planfreeze vor A. PE-M01 geschlossen; Quellenmetadaten PE-S01/02 korrigiert. Die [Planfestschreibung](planfestschreibung-v1.md) benennt verbindliche Artefakte, gleiche Modellfamilie und weiterhin offene empirische/menschliche/Claude-Prüfungen. Tags und tatsächliche Dateneinsicht werden erst in ihren Ausführungsbelegen als erfolgt erfasst.
