# Analyseplan: Vorbereitung

Arbeitsfassung 0.1 vom 2026-10-03. **Nicht eingefroren, nicht methodisch freigegeben, kein Tag `analyseplan-v1`.** Noch keine ESS-Antwortdaten ausgewertet. Nach dem Dateieingang wurden ausschließlich Datei-Hash, Header und festgelegte globale Metadaten lokal geprüft; der [Dateieingangsbericht](../reports/phasen/00-dateieingang-2026-10-03.md) protokolliert diesen vorbereitenden Zugriff. Diese Datei dokumentiert den vorgesehenen Ablauf und die Entscheidungen, die vor dem Start noch fehlen.

## Fragestellung und Reichweite

Welche begrenzten Einstellungsdimensionen lassen sich aus geeigneten deutschen ESS-Fragen bilden, und tragen ihre vorab festgelegten Prüfungen ein erklärendes Profil mit historischen Bevölkerungs- und Wählergruppenvergleichen? Die Untersuchung darf auch ergeben, dass ein Thema, eine Dimension oder ein Vergleich für die Webapp ungeeignet ist. Zwölf Dimensionen sind keine Zielzahl.

ESS11, integrierte Ausgabe 4.2, ist der recherchierte Datenkandidat (B-ESS-001). Die Auswahl bleibt vor Analyse zu prüfen und festzulegen. Der spätere Vergleich gilt für die dokumentierte ESS-Referenzpopulation und den Befragungszeitraum, nicht für aktuelle Wahlabsichten. [Datenlage](datenlage.md) und [Prüfregeln](pruefregeln.md) sind Teil des Plans.

## Reihenfolge und Zugriff

1. Öffentliche Rechte, Fragebögen, Kodierungen, Stichprobendesign und Literatur prüfen. Katalog und konkurrierende Erwartungen vor Ergebniszugriff erstellen; keine eigens erfundenen Items.
2. Alle unten offenen Parameter samt Begründungen, Entscheidungskonsequenzen und erforderlichen Bewertungen vervollständigen. Plan und Erwartungsmodelle in der vorgesehenen Reihenfolge öffentlich einfrieren. Ein lokaler Entwurf genügt nicht als öffentliche Präregistrierung.
3. Originaldatei lokal importieren: Version/Hash protokollieren, Deutschland filtern, Import-/Kodierungsprüfungen ohne Einstellungsverteilungen. Technische Verarbeitung von Rohdaten bleibt lokal; keine Personenzeilen in Agent-Ausgaben.
4. Vorab definierten Split erzeugen. Messdaten enthalten ausschließlich freigegebene Items und notwendige Designinformationen. B sowie Wahl-/Links-rechts-Felder bleiben gesperrt. Grenzen technischer Abschirmung und jeder unerwartete Zugriff werden offengelegt.
5. In A die vorab definierten Modelle entwickeln und vergleichen. Zuordnung, Polung, zulässige Anpassungen und Modellartefakt vor B einfrieren.
6. B einmal nach festgelegtem Verfahren öffnen und das eingefrorene Modell prüfen. Änderungen infolge dieser Prüfung sind explorativ; keine erneute unabhängige Bestätigung am selben B behaupten.
7. Benennung und Vergleichsregeln einfrieren, dann die vorgesehenen Wahl-/Lagerfelder entblinden. Invarianz, Dominanz und weitere Sensitivitäten durchführen; Konsequenzen nach Plan anwenden.
8. Nur freigegebene aggregierte Artefakte exportieren. Webauswertung gegen Python mit synthetischen Fällen prüfen. Texte, Quellen und Veröffentlichungsrechte am tatsächlich exportierten Stand gegenprüfen.

Die öffentliche Metadaten-Recherche kennt bereits Wahljahr und Parteikodierungen. Ein Suchtreffer zeigte zudem eine öffentliche aggregierte Variable (siehe [KI-Protokoll](ki-protokoll.md)). Es wird keine vollständige Unkenntnis politischer Inhalte behauptet. Die noch mögliche Trennung betrifft empirische Modellbefunde, B und spätere Gruppen-/Lagerzusammenhänge.

## Bereits begründeter Ausgangspunkt

Für Gewichtung ist `anweight` der ESS-Ausgangspunkt; Stichprobenunsicherheit muss zusätzlich Cluster und Schichten berücksichtigen. Grundlage: Kaminska, Gewichtungsleitfaden V1.2, Abschnitte 3 und 4.3 (B-METH-001). Ungewichtete Rechnungen dienen als Sensitivität, nicht als gleichwertige Hauptnorm.

Ordinale CFA-Verfahren werden anhand geeigneter Forschung und der vorgesehenen Items gewählt. Flora/Curran untersuchen robuste WLS-Verfahren in Simulationen (B-METH-002); daraus folgt noch keine fertige Verfahrensentscheidung für diesen Datensatz. Gruppenvergleiche brauchen eigene Messvergleichbarkeitsprüfungen (B-METH-003). Reliabilität wird anhand des konkreten Messmodells beurteilt; die Literatur zu Alpha enthält auch begründete Gegenpositionen (B-METH-004).

## Vor Freigabe auszufüllen

Jede Entscheidung nennt Quellenfundstelle, Annahmen, Anwendungsbereich, konkrete Parameter, Prüfbericht und Konsequenz bei Nichterfüllung. Eine übliche Konvention ohne Eignungsbegründung reicht nicht.

| ID  | Fehlende Entscheidung                                                                                                      | Benötigte Grundlage                                                                                                                                                             |
| --- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P01 | Datenversion, Referenzpopulation, Ausschlüsse, gültige Kodierungen und Analysefallzahlen.                                  | Versionshinweise, deutscher Katalog, Filter/Missing-Codes; Importvertrag. Keine politische Vorauswahl der Fälle.                                                                |
| P02 | Vollständige Item-Eignung, Polung, theoretische Themenabdeckung und konkurrierende Erwartungen.                            | Literatur-Bezugsrahmen für Deutschland, Originalquellen, getrennte Erstbewertungen und vorab definierte Dissensbehandlung.                                                      |
| P03 | A/B-Aufteilung, Seed, Schutz von B und zurückgehaltene Variablen; Umgang mit Design-Clustern im Split.                     | Begründete Informations-/Präzisionsplanung vor Datenblick. Eine zufällige Zeilenteilung beweist bei gemeinsamem Cluster keine statistische Unabhängigkeit.                      |
| P04 | Ordinale EFA/CFA, Faktorzahlauswahl, Rotation, Identifikation und zulässige Anpassungen in A.                              | Passende Primärliteratur, Softwarefähigkeit einschließlich Gewichtung/Design; Diagnosen und Konsequenzen bei Nichtkonvergenz.                                                   |
| P05 | Missing-Behandlung in EFA/CFA, Normierung und Gruppenschätzung; Mindestantworten im Webtest.                               | Itemfilter, Missing-Mechanismen/Annahmen und vorab geplante Sensitivitäten. „Weiß nicht“ und Verweigerung sind keine Skalenmitte.                                               |
| P06 | Ladungen, Kreuzladungen, Reliabilität samt Unsicherheit, Fit, Itemdominanz und Tragfähigkeit einer Dimension.              | Messmodellbezogene Kriterien und ergänzende Simulationen mit ausdrücklich synthetischen Daten; keine pauschalen Cutoffs.                                                        |
| P07 | Designgerechte Varianz-/Intervallschätzung, Gewichtsbehandlung, einzelne PSUs und verfügbare Freiheitsgrade.               | ESS-Leitfaden und konkrete Designinformationen; geprüfte Implementierung einschließlich Einfluss von Gewichten, Clustern und Schichten.                                         |
| P08 | Rohscore, Perzentildefinition mit Bindungen, Normpopulation und begründbare persönliche Unsicherheit.                      | Gleichgewichtete 0–1-Auswertung als Vorgabe aus LIFE-93; gleiche Abstände zwischen ordinalen Kategorien als eigene zu prüfende Modellannahme. Normierungs- und Faktorvarianten. |
| P09 | Gruppenbildung, valide Wahlvariable, Mindestfallzahl **und** Präzision, Invarianzverfahren für ordinale Items.             | Historische Kodierung, Schätzbarkeit, öffentlich vorab bestimmter Genauigkeitsanspruch. Der Vorschlag 50 Fälle aus LIFE-93 ist noch kein akzeptierter Grenzwert.                |
| P10 | Alters-/Bildungs-/Geschlechts-/Ost-West-/Lagergruppen und Interpretation bei unzureichender Invarianz.                     | Gruppen vorab definieren, Berliner Zuordnung ausdrücklich regeln, kleine Gruppen nicht als bestanden werten. Bundesland-Repräsentativität nicht voraussetzen.                   |
| P11 | Distanz und Bedingungen einer Nähe-Reihenfolge; fehlende Dimensionen und Unsicherheit.                                     | Vorab definierte Gewichtung/Distanz, Rangstabilitätsverfahren und Unterdrückungsregel. Kein Gesamt-Match in Prozent.                                                            |
| P12 | Sensitivitätsumfang und Grenzen: Itemausschluss, z-/Faktorwerte, Normen, Gewichte, Missing, andere Runde, Modellvarianten. | Verfahren und Schwellen vor Entblindung; Regeln für engere Aussage, Warnung, Ausschluss oder neue explorative Version. Mehrfachprüfungen transparent behandeln.                 |
| P13 | Review-/Abnahmeverfahren und vollständige Reproduktionsumgebung.                                                           | R08/R24, bekannte tatsächliche Reviewer und Zugangsvoraussetzungen; Pipeline noch nicht eingerichtet.                                                                           |

## Bedingung für den Analysestart

Alle P-Entscheidungen sind vollständig begründet, ihre relevanten Gegenprüfungen liegen vor, offene wesentliche Findings sind bearbeitet, Rechte und Zugriff sind geklärt und der Plan ist öffentlich eingefroren. Die gegenwärtige Entscheidung „nur CodeRabbit; methodische Freigabe offen“ erfüllt diese Bedingung noch nicht. Recherche an Originalunterlagen und Literatur kann bis dahin weitergehen.
