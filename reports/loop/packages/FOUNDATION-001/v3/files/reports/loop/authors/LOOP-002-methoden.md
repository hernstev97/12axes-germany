# LOOP-002 — Methodenautor

Stand: 2026-10-03. Arbeitsort: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Rolle: abgegrenzter Methoden-/Statistikautor, kein Reviewer. Der tatsächlich erhaltene vollständige Startauftrag ist wortgetreu in [LOOP-002-methoden-auftrag.txt](./LOOP-002-methoden-auftrag.txt) erhalten. Es wurden keine weiteren Agenten gestartet, keine Commits/Pushes ausgeführt und keine gemeinsamen Plan-, Website- oder Zustandsdateien geändert.

## Substanzieller Beitrag

[analyseplan-methoden.entwurf.md](../../../docs/analyseplan-methoden.entwurf.md) arbeitet sämtliche P01–P13 als überprüfbare Vorschläge mit Eingaben, Annahmen, Regeln und Konsequenzen aus. Die wichtigsten Entscheidungen betreffen ganze PSUs im A/B-Split, einen dokumentierten ordinalen COMPLEX-Softwareweg, ausschließlich vollständige Itemmasken als anfängliche Begrenzung, den beobachteten Score als Reliabilitätsziel, gemeinsame Designkovarianz sowie Fallzahl **und** tatsächliche Präzision. Latente Faktoren, beobachtete Komposite, Referenzunsicherheit und persönlicher Messfehler bleiben getrennte Zielgrößen.

Der Entwurf verwendet keine unbegründeten universellen Fit-/Ladungs-/Omega-Grenzen. Stattdessen schlägt er explizite Fehlerfolgen im veröffentlichten Wertebereich und eine noch durchzuführende designgerechte Kalibrierung vor. Wo eine passende Methode oder ihre Evidenz fehlt, steht ein offener Blocker. Die Vollmaskenbegrenzung, eine eigene PVQ-Entscheidung und die Aussetzung der optionalen Rangfolge sind **zu prüfende Begrenzungen**, keine ausgeführten Produkt-/Itementscheidungen. Die vorgeschriebenen Kernfunktionen und der bestehende Hauptplan bleiben unangetastet.

## Quellenarbeit und tatsächlich gelesener Umfang

[methoden-quellen.json](../../../data/methoden-quellen.json) enthält 17 Quellen mit 17 Aussage-IDs L-METH-001 bis L-METH-017; jede Quelle hat DOI beziehungsweise Original-URL, Abruf, Originalcachehash, den selbst gelesenen Bereich und Gegenbelege/Geltungsgrenzen. Fünf zusätzliche erfolglose oder nicht verwendete Abrufe sind ausdrücklich keine Verfahrensevidenz. Sämtliche Originalcaches und PDF-Renderings liegen ausschließlich unter `outputs/loop/methods/`, außerhalb von Git. Alle 17 angegebenen Originalcachehashes wurden gegen die tatsächlichen Dateien geprüft.

Gelesen wurden die lokalen Aufgaben-/Regeldokumente: AGENTS, `docs/project.md`, `docs/arbeitsloop.md`, dauerhafter Auftrag, gesichertes Issue, Analyseplan/-anforderungen, Prüfregeln sowie Quellen-/Beleg-, Lizenz- und Entscheidungsregister. In umfangreichen Registern wurden die für diesen Auftrag benötigten Abschnitte gelesen; keine Vollständigkeit über nicht benutzte Literatur wird behauptet. Keine aktuellen Reviewerurteile, anderen Autorenbewertungen, ESS-Rohantworten, Personenfelder, B, Wahl-/LR-Werte, Verteilungen oder Portal-Analysis wurden geöffnet.

Die zugänglichen Originalabschnitte von Wu/Estabrook wurden aus genau der vom Koordinator autorisierten datierten öffentlichen HTML-Kopie selbst gelesen. SHA-256 `32cf963946fa00970a18612d37c5bbc49347fd244329a1ee832b82eea9575730`, Abruf `2026-10-03T00:43:38.838623+00:00`. Die Live-PMC-Seite war durch reCAPTCHA begrenzt; der Publisher zeigte nur Abstract/Abonnement. Keine andere Datei aus dem früheren Jurorverzeichnis wurde gelesen. Dieser Herkunftsweg ist kein Reviewerurteil und ersetzt keine eigene Quellenlektüre.

Tse/Lai/Zhang war als Original-Publisher-HTML in den behaupteten Abschnitten vollständig lesbar; der PDF-Abruf scheiterte. Green/Yang war nur als Abstract zugänglich. Gleichung 21 und die Erweiterung für ungleiche Kompositgewichte sind deshalb **nicht** als selbst geprüfte Primärverfahren ausgegeben. Die Einschränkungen stehen sowohl im Entwurf als auch im Quellenregister.

## Softwarefähigkeit und Grenzen

Mplus dokumentiert gewichtete ordinale EFA/COMPLEX/WLSMV, Stratum/Cluster und passende CFA-/Invarianzwerkzeuge. Die konkret erforderliche Modellidentifikation, Designkompatibilität und Syntax müssen trotzdem ausführbar getestet werden. Hier wurden weder `mplus` noch `Rscript` gefunden. Es wurden keine Programme oder Pakete installiert und keine Sicherheitsgrenzen umgangen.

Die aktuellen offiziellen lavaan-/semTools-/survey-Dokumentationen wurden in den angegebenen Abschnitten gelesen. lavaan 0.7-2 hat gewichtete ordinale WLS-Unterstützung; diese Fähigkeit darf nicht veraltet bestritten werden. Die gesamte ESS-Stratum-/PSU-Invarianz-Kette ist damit noch nicht nachgewiesen. semTools erwartet ein lavaan-Objekt; ein zuverlässiger Transfer von Mplus-Parametern für die passende beobachtete Score-Reliabilität fehlt. Für PPS ist ein generischer survey-Bootstrap laut eigener Dokumentation nicht streng begründet. Deshalb setzt der Entwurf ihn nicht als fertige ESS-Lösung ein.

## Tatsächlich durchgeführte synthetische Kalibrierung

[methoden_kalibrierung.py](../../../pipeline/synthetic/methoden_kalibrierung.py) akzeptiert keine Eingabepfade oder Argumente und erzeugt ausschließlich numerische Pseudoitems. [LOOP-002-methoden-kalibrierung.json](../synthetic/LOOP-002-methoden-kalibrierung.json) enthält nur aggregierte Resultate. Status `SYNTHETIC_CALIBRATION_ONLY`, reale ESS-Daten `false`; Seed `2026100302`, Python 3.14.7, NumPy 2.5.3/PCG64.

Sechs Szenarien mit je 1.000 Wiederholungen: acht Strata, je zehn PSUs und zwanzig synthetische Beobachtungen; symmetrische normale Cluster-/Individualterme mit latenten Clusterfraktionen 0 / 0,25 / 0,5; unabhängige Gewichte mit CV 0 / 1; fünf numerische Ordinalkategorien; zwei innerhalb PSU vertretene synthetische Domänen. Keine PPS-Auswahl, keine Nichtantwortkalibrierung, keine realen Fragen oder Gruppen.

Unter diesen Szenarien zeigte ein Zeilensplit bei gemeinsamer Clusterkomponente die erwartete starke Abhängigkeit der Arm-Mittelwerte, der ganze-PSU-Split deutlich geringere Korrelation. Bei Clusterfraktion 0,5 und konstanten Gewichten lagen die Korrelationen bei 0,893 und 0,047. Die diagonale Varianzrechnung ohne gemeinsame Kovarianz war in diesem Szenario rund 9,24-mal so groß wie die gemeinsame Kontrastvarianz. Andere Szenarien sind vollständig in der JSON erhalten; diese Zahlen sind keine universellen Garantien.

Die Taylor-Varianz-/Abdeckungswerte gelten ausschließlich für diese dokumentierten Szenarien mit Normalintervallen. Sie sind keine ESS-Abdeckungsprüfung. Deterministische Gegenbeispiele zeigen gleichermaßen die mögliche Varianzdominanz eines gleichgewichteten Items und die Nichtgleichwertigkeit verschiedener gleich großer Antwortmasken. Technische Assertions prüfen gemeinsame Gewichtsskalierungsinvarianz, nichtnegative Kovarianz-Eigenwerte im numerischen Test, bekannte Dominanz und positive Kontrastvarianz. Keine EFA/CFA-, Invarianz-, Reliabilitäts- oder persönliche Fehlermodellsimulation wurde ausgeführt.

## Ist jeder Parameter wirklich entscheidungsreif?

| Parameter | Status                                       | Konkret noch fehlend                                                                                                       |
| --------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| P01       | Teilweise konkret, nicht entscheidungsreif   | Edition-/DOI-Abgleich, vollständiges deutsches Design, offizielles Codes-/Filtermanifest                                   |
| P02       | Nicht entscheidungsreif                      | Fachliches Inventar/Polung, unabhängige Erstbewertungen, PVQ-Vertragsentscheidung                                          |
| P03       | Konkret vorgeschlagen, nicht real prüfbar    | PSU-/Stratum-Metadaten; Behandlung kleiner/Certainty-Strata vor dem Split                                                  |
| P04       | Dokumentierte Softwarekandidaten, blockiert  | Laufzeit/Lizenz, Identifikation, Ordinal-/Designkalibrierung der Auswahl-/Fitregeln                                        |
| P05       | Reviewfähige Begrenzung, offen               | Vollmaskenentscheidung; Selektionsannahmen und spätere Fehlanteile; Populationstransfer                                    |
| P06       | Messziel präzisiert, blockiert               | Reliabilitäts-Primärvolltexte, ungleiche Gewichte, Design-/Softwaretransfer, persönliches Fehlermodell                     |
| P07       | Gemeinsame Formel konkret, nicht freigegeben | Vollständiges DE-Design, geringe Domänen-/df-Unterstützung, Gewichtskonstruktionsgrenzen                                   |
| P08       | Score/CDF formal, teilweise offen            | Inventarfreigabe und geprüfte Brücke zur persönlichen Unsicherheit                                                         |
| P09       | Konkrete Vorschlagsziele, blockiert          | Fehlerbudgetabnahme, identifizierte ordinale Invarianzmodelle, designgerechte simultane Äquivalenz-/Präzisionskalibrierung |
| P10       | Domänenvorschläge, nicht entschieden         | Offizielle Crosswalks, fachliche Gruppendefinitionen/Berlin, jedes Domänengate                                             |
| P11       | Begründete Aussetzung vorgeschlagen          | Begrenzungsentscheidung; gemeinsames nichtlineares und persönliches Fehlermodell                                           |
| P12       | Folgenregeln konkret, offen                  | Vollständige freigegebene Variantenliste; reale Sensitivität noch nicht zulässig                                           |
| P13       | Reproduktionsanforderungen konkret, offen    | Ausführbares Paket, unabhängige Gegenprüfungen und geprüfte Interpretationstexte                                           |

Kein Parameter ist durch diesen Lauf insgesamt entscheidungsreif oder empirisch bestanden. Das Fehlen eines persönlichen Intervalls oder einer Rangmethode wurde nicht durch einen ungeeigneten Ersatz kaschiert. Die vorgeschlagenen Zahlen sind prüfbare eigene Verlust-/Auflösungsziele, keine Primärquellenkonventionen.

## Technische Prüfung und Artefaktidentität

Ausgeführt: Python-Syntaxprüfung; synthetischer Lauf mit Assertions; JSON-Parse; Prüfung aller 17 Originalcachehashes; Prüfung des in der Ergebnis-JSON enthaltenen Skripthashes. Eigene Markdown-/JSON-Artefakte wurden gezielt mit Prettier formatiert. Der Ergebnis-Hash unten bezeichnet die normalisierte Ausgabe nach Prettier; Reproduktion benötigt den Skriptlauf und dieselbe Formatierung.

Reproduktion aus dem Arbeitsort:

```bash
python pipeline/synthetic/methoden_kalibrierung.py
pnpm exec prettier --write reports/loop/synthetic/LOOP-002-methoden-kalibrierung.json
```

Der Koordinator hat zusätzliche globale `pnpm check`-Läufe ausdrücklich untersagt und übernimmt den gemeinsamen Techniklauf. Dieser Autorenbericht behauptet deshalb keinen eigenen bestandenen Gesamtcheck. Eine vom Koordinator mitgeteilte Handbuchverletzung in einem anderen Paket ist kein Methodenbefund und wurde hier nicht bewertet. Keine UI-Dateien wurden geändert; kein Browser-Abnahmelauf war Teil dieser Autorenarbeit.

| Artefakt                                                     | SHA-256                                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------------ |
| `docs/analyseplan-methoden.entwurf.md`                       | `37bcaa35d82d3db20b21fce05881b36063f5ac40ba7fa5f3300fdd3c9fb5df0c` |
| `data/methoden-quellen.json`                                 | `1799311500570a85c31ad2f9d1d09c6402b30925fd1cc527f03e8e653d268c52` |
| `pipeline/synthetic/methoden_kalibrierung.py`                | `42349e34f5529026e2b067d9986200031110846f105860d301588d58bcc37fc3` |
| `reports/loop/synthetic/LOOP-002-methoden-kalibrierung.json` | `fe5ae8294b90b3621ce91a13217e4ddd341bea557ff80011548ef73cfbd6a45b` |
| `reports/loop/authors/LOOP-002-methoden-auftrag.txt`         | `3ae87d12e09fc20c868122c8f7ece7a08672355b7a92240b937f1c759eda3f08` |

Der abschließende Berichtshash wird dem Koordinator separat gemeldet, um keinen zyklischen Selbsthash zu erzeugen. Kein öffentlicher Tag, keine empirische Analyse, kein Produktstart und keine wissenschaftliche Freigabe wurden vorgenommen.

## Wortgetreuer Startauftrag

Die zusätzliche `.txt`-Kopie wird durch die bestehende Repository-Ignore-Regel ausgeblendet. Deshalb ist derselbe erhaltene Spawnwortlaut auch hier vollständig gesichert:

```text
Du bist ein abgegrenzter Methoden-/Statistikautor für LIFE-93, kein Reviewer. CWD ausdrücklich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Lies AGENTS, docs/arbeitsloop.md, dauerhaften Auftrag, gesichertes Issue und docs/analyseplan.md, docs/analyseanforderungen.md sowie Quellen-/Belegregister. Keine aktuellen Reviewerurteile oder anderen Autorenbewertungen. Keine ESS-Rohantworten, Personenfelder, B, Wahl-/LR-Werte, Verteilungen, Portal-Analysis. Nur offizielles Design-/Variablenmetadatenmaterial und Primärmethodenliteratur. Erstelle docs/analyseplan-methoden.entwurf.md, eigenes data/methoden-quellen.json und reports/loop/authors/LOOP-002-methoden.md; ggf ausdrücklich synthetische Kalibrierungsskripte unter pipeline/synthetic/ und aggregate synthetische Resultate unter reports/loop/synthetic/. Bestehenden Analyseplan/Quellenkatalog/andere gemeinsame Dateien nicht ändern. Ziel: P01–P13 zu konkreten, begründeten, prüfbaren Vorschlägen ausarbeiten, nicht pauschale Konventionen. Zufallssplit mit Clusterabhängigkeit, Gewichtung/Design in ordinaler EFA/CFA und Invarianz, fehlende Werte und erlaubte Itemmasken, beobachteter 0–1-Score vs latenter, passende Reliabilität und persönliche Unsicherheit, designgerechte Referenzunsicherheit/gemeinsame Kovarianz, Itemdominanz/Stabilität und Mindestfallzahl plus Präzision mit Konsequenzen. Falls begründeter Ausschluss einer optionalen Rangfunktion/Teilantworten/PVQ einfacher tragfähig ist, als zu prüfende Begrenzung kennzeichnen, keine vorgeschriebenen Kernfunktionen oder Itemauswahl eigenmächtig ändern. Konkrete Parameter, Eingaben, Regel, Folge bei Scheitern/Nichtprüfbarkeit, Annahmen, Primärfundstellen und Softwarefähigkeit je Entscheidung. Überprüfe tatsächlich unterstützte Tools/Software an offiziellen Dokumenten; nichts global installieren, keine Sicherheitsumgehung. Reale Verfahren nicht als bestanden, synthetische Simulationen nur als Kalibrierungsbeleg unter dokumentierten Szenarien. Fehlende Evidenz/Konflikte ausdrücklich offen; keine passende Methode erfinden, nur um Tabelle fertig zu füllen. Originalquellen vollständig im behaupteten Umfang selbst lesen; nicht zugängliche Volltexte unvollständig geprüft. Aussage-IDs L-METH-001 etc., DOI/URL, Fundstelle/Geltungsbereich/Gegenbeleg und Cachehash. Caches ausschließlich outputs/loop/methods/, keine Fremdvolltexte in Git. Im Report festhalten, ob jeder Planparameter wirklich entscheidungsreif ist und was konkret fehlt; kein öffentlicher Tag/empirischer Analysebeginn oder wissenschaftliche Freigabe. Keine weitere Agents, kein Commit/Push und keine Website oder zentralen Zustandsdateien ändern. Konkrete substanzielle Artefakte erstellen und mit Hashes melden.
```
