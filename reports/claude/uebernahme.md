# Übernahme von LIFE-93 durch Claude

Stand: 2026-10-03, 21:00–21:30 Uhr (MESZ). Verfasst von Claude (Anthropic, Modell laut Laufzeit `claude-opus-5-5`) im T3-Code-Thread `60cbaa36-abf8-49ac-9ba7-5a60e3aff64d` („Politiktest wissenschaftlich fundieren“). Auftrag: Stevens Nachricht „Mach hier weiter, alles steht im Issue“ mit Link auf LIFE-93. Der Nachtrag „Claude: Abschlussprüfung, Ergänzungen und Übernahme“ in LIFE-93 regelt diese Übernahme. Steven hat während der Übernahme die Abschnitte 2a bis 2c ergänzt (Issue-Stand `updatedAt` 2026-10-03T18:57:55Z). Beide Issue-Fassungen sind gelesen.

## Tatsächlicher Ausgangsstand

| Punkt                       | Befund                                                                                                                                                                                                                                        |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Codex-Arbeitsbranch         | `research/life-93-night-20261003`, HEAD `e9898fb423a3ba9fbe6387ed9215dbe83666aedc`, lokal und auf `origin` gleich, Worktree ohne ungesicherte Änderungen                                                                                      |
| Codex-Worktree              | `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`                                                                                                                                                                      |
| Codex-Thread                | `6975a99d-529e-40d2-b9ec-e06c85c1dc94`, Status `completed`, letzter Lauf endete 2026-10-03T18:46:22Z. Die letzte Codex-Nachricht übergibt ausdrücklich an die Claude-Schlusskontrolle. Kein Nutzungslimit gemeldet.                           |
| Weitere schreibende Agenten | Keine. In T3 lief beim Start nur dieser Thread. Die drei Codex-Server waren laut Übergabebeleg beendet.                                                                                                                                       |
| Eigener Arbeitsbranch       | `research/life-93-claude-20261003`, abgezweigt von `e9898fb` in `/home/stevenh/.t3/worktrees/12axes-germany/t3code-794dd32c`. Der Codex-Worktree bleibt unberührt.                                                                            |
| Lokale Eingaben             | Die fünf ESS-CSV-Dateien liegen im Codex-Worktree unter `data/raw/`. Im eigenen Worktree verweisen ignorierte Symlinks darauf. Die öffentlichen Quellen-Caches unter `outputs/loop/` sind als Hardlinks übernommen (ignoriert, nicht in Git). |
| Erste technische Gegenprobe | `scripts/build-policy-v2-report.py --check` und `scripts/build-policy-group-report-v21.py --check` laufen im eigenen Worktree mit Exitcode 0. Das ist ein Bytevergleich der Darstellung, keine Kontrolle der Rohrechnung.                     |
| Weitere Worktrees           | `/home/stevenh/projects/12axes-germany` (Branch `research/life-93-methodology`, Stand `1a7b0c3`) und `life93-cli-reproduction-20261003` (losgelöst, `ccb431d`). Beide unverändert.                                                            |

## Was vor dem eigenen Urteil gelesen wurde

LIFE-93 vollständig einschließlich beider Kommentare, `AGENTS.md`, `docs/project.md`, `reports/loop/handoff.md`, `docs/claude-schlusskontrolle-v2.md`, `docs/auftrag-life-93-breite-2026-10-03.md`, `docs/auftrag-life-93-fortsetzung-2026-10-03.md`, `docs/abdeckung-v2.md`, `docs/empirie-plan-v2.entwurf.md`, `docs/reproduktion-life93-v2.md`, `docs/handbuch.md`, die Statusfelder von `reports/loop/state.json` und eine Statusübersicht von `reports/loop/findings.json`, die letzten Nachrichten des Codex-Threads ab Position 1880.

Damit kannte ich Codex' eigene Zusammenfassung und Grenzbeschreibungen, bevor ich selbst prüfte. Die inhaltlichen Prüfungen habe ich deshalb an frische Subagents mit eigenem, begrenztem Kontext gegeben (siehe `reports/claude/auftraege/`). Sie lesen Codex' Entscheidungs- und Reviewdokumente erst nach ihrem eigenen Urteil. Alle Prüfer gehören wie ich zur Claude-Familie. Gegenüber Codex' Arbeit sind sie eine andere Modellfamilie, gegenüber meinen eigenen Ergänzungen nicht.

## Stand der Artefakte

| Artefakt                                                         | Stand bei Übernahme                                                                                                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Historische Neunerfassung v1 (ESS11, Teil A/B, Tags v1)          | Fertig und eingefroren. Teil B wurde einmal geöffnet und gerechnet. Die alte Folge ist angehalten.                                      |
| Fragenkatalog v2, 43 ESS-Originalfragen in acht Bereichen        | Fertig gebunden, Status `DRAFT_NOT_GATE`. Von Claude noch nicht geprüft.                                                                |
| Historische Einzelreferenzen (42 veröffentlicht, `cttresa` null) | Gerechnet, exportiert, von zwei Codex-Rollen begrenzt geprüft. Unabhängige Kontrollrechnung fehlt.                                      |
| Historische Wählergruppen v2.1 (ESS5/8/9, 63 Paare)              | Gerechnet, exportiert, begrenzt geprüft. Unabhängige Kontrollrechnung fehlt.                                                            |
| Themenmatrix `docs/abdeckung-v2.md`                              | Begonnen. Außen-/Verteidigungs-, Bildungs-/Forschungs- und Digitalpolitik fehlen im Fragenbestand. GLES und ISSP sind nur recherchiert. |
| Erklärendes Profil (LIFE-93, Abschnitt 2a)                       | Nicht vorhanden. Die Ergebnisansicht zeigt je Frage die gewählte Kategorie, eine kurze Umschreibung und historische Anteile.            |
| Stichprobenunsicherheit                                          | Nicht berechnet. Plan v2 beschreibt das Verfahren und schließt Konfidenzintervalle für die erste Fassung aus.                           |
| Forschungsoberfläche `/forschungsentwurf`                        | Nur im lokalen Research-Build. Technisch geprüft in Chromium (Fokus, 200-%-Zoom). Gestaltung nicht freigegeben.                         |
| Verständnistest mit fünf Personen                                | Vorbereitet (Pläne 0.1/0.2), keine Durchführung.                                                                                        |
| Setup-Abnahme (Branch-Schutz, Review-Check)                      | Nicht erfüllt.                                                                                                                          |
| Freigaben durch Steven (Gestaltung, Rechte, Teststart, Release)  | Extern offen.                                                                                                                           |

## Widersprüche und wie sie hier gelten

1. `AGENTS.md` auf dem Codex-Branch untersagt weitere Claude-Zugriffe und nennt Claude als später von Steven veranlasste Kontrolle. Der Nachtrag in LIFE-93 beauftragt Claude jetzt mit Prüfung und Fortsetzung. Der Nachtrag gilt. `AGENTS.md` wird im Rahmen von Abschnitt 2c angepasst.
2. Der Hauptteil von LIFE-93 beschreibt Codex als leitenden Agenten, ein Claude-Review per GitHub Action und automatisches Mergen. Der Nachtrag schließt Merge nach `main`, Deployment und Veröffentlichung ohne Stevens Freigabe aus. Es gibt in dieser Übernahme keinen Merge und kein Auto-Merge.
3. Der Hauptteil nennt den ESS als einzige Quelle und sieht Dimensionen mit 0–1-Rohscores und Perzentilen vor. Der Nachtrag öffnet die Quellenbasis. Abschnitt 2a erlaubt Beschreibungen ohne Gesamtpunktzahl und verlangt Skalen nur bei fachlicher Begründung. Die Form des Profils wird deshalb neu begründet, nicht aus dem Hauptteil übernommen.
4. Das Handbuch sagt, Test und Ergebnis seien noch nicht gestaltet und neue Muster brauchten Stevens Absprache. Abschnitt 2a verlangt die Umsetzung in der tatsächlichen Ergebnisansicht. Die Umsetzung erfolgt im lokalen Forschungsentwurf innerhalb der vorhandenen Klassen und Leitplanken. Die Gestaltungsfreigabe bleibt offen.
5. `docs/project.md` enthält ältere Aussagen („Steven richtet Claude vorerst nicht ein“, „Es gibt noch keinen Fragenkatalog“). Sie stehen in als historisch markierten Abschnitten, widersprechen aber dem aktuellen Stand und werden nach Abschnitt 2c abgeglichen.

Der Codex-Thread ist über T3 lesbar. Die Nachrichten von Steven darin extrahiert ein eigener Subagent nach `reports/claude/agenten/T3-thread-nutzernachrichten.md`.

## Arbeitsplan

1. Themenrecherche in drei getrennten Aufträgen (R1–R3) und Recherche zur Profilform (R4).
2. Nachträgliche Prüfungen des Codex-Stands: unabhängige Kontrollrechnung (V1), Quellen, Konstrukte und Fairness (V2), Technik, Browser und Datenschutz (T1).
3. Versionierter Plannachtrag vor jeder neuen Auswertung: neue Fragen, Stichprobenunsicherheit, Regeln des erklärenden Profils. Prüfung durch zwei getrennte Rollen, davon nach Möglichkeit ein frischer Codex-Prüfer.
4. Auswertung, Export, Website, Methodenbericht, Dokumentenabgleich.
5. Abschlussbericht `reports/claude/abschlusspruefung.md` mit Vorschlag zur Abnahme durch Steven.
