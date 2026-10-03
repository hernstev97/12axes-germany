# GROUP-RESULTS-V21-001: getrenntes Quellen-Ersturteil

Rolle: `sources_constructs_fairness`. Urteil: `ACCEPTED_BOUNDED`.
Prüffassung: `GROUP-RESULTS-V21-001/v1`.
Manifest-SHA256: `dddbcda2fe8a18f46a45ee812100508d9c3ed10c5cca8c8d391be648e474b13a`.

Ich gebe ausschließlich die im [Entscheidungs-JSON](GROUP-RESULTS-V21-001-sources-decision.json) einzeln aufgeführten `{groupId, questionId}`-Paare für die begrenzte historische Deskription frei. Diese Entscheidung entstand nach der eigenen Prüfung der Quellenbindung, Gruppenidentität, Kategorien und des tatsächlichen Aggregatstatus. Der Status `prepared_pending_group_result_review` war eine Prüfbedingung, keine automatische Publikationsfreigabe. Alle nicht aufgeführten Paare behalten `reference: null`. Die einzelnen ursprünglichen Gruppen und Fragen bleiben auch dann im Inventar erhalten.

Das Urteil betrifft nur `ESS5e03_6`, `ESS8e02_3` und `ESS9e03_3`. Es ist keine Freigabe weiterer Studien, einer Weboberfläche, eines Teststarts oder eines Releases. Das breite Hauptprodukt mit den gebundenen Originalfragen und Themen bleibt ein eigener Gegenstand. Das Gruppenmodul ersetzt seine Breite nicht.

## Zugang und Verfahren

Ich las das Manifest selbst und prüfte die tatsächlichen Bytes aller 64 öffentlichen Pins und exakt der drei dort genannten geschlossenen privaten `run.json`-Aggregate. Alle Pins und die kanonischen inneren Kandidaten-Hashes stimmten. Die zusätzlichen, im Fragenkatalog gebundenen ESS5-/ESS8-/ESS9-Codeverzeichnisse und das ESS8-Listenheft stimmten ebenfalls mit ihren Quellen-Hashes überein. Den Abschlussvergleich der gemeinsamen Pins dokumentiere ich unten.

Die beiden Vorzugriffs-Erstberichte wurden ausschließlich als Bytes gehasht. Ihre Urteilsprosa, andere Ergebnisrollen, Autorenberichte und der gespeicherte Loopzustand wurden nicht gelesen. Beim ausdrücklich zugelassenen 005-Erratum wurden nur die korrigierten Zugangsfakten herangezogen. Sie sind eine berichtete Statuskorrektur und kein unabhängiges Zugriffsaudit. Übergeordnete Repositoryregeln wurden gelesen; darin enthaltene Verweise auf andere Berichte wurden nicht verfolgt.

Kein Zugriff auf `data/raw/` fand statt, auch keine Verzeichnisliste, Dateistatistik, Header- oder Prüfsummenprüfung. Keine anderen privaten Dateien wurden geöffnet. Es gab keinen Netz-, Auth-, Installations-, Git-, Server- oder Kontaktzugriff und keinen neuen Datenlauf. Die Prüfungen am reinen Exporter verwendeten nur die zugelassenen, bereits geschlossenen Aggregate. Die hierfür erzeugten Entscheidungen mit synthetischen Reviewerpfaden waren QA-Eingaben und keine tatsächlichen Veröffentlichungsentscheidungen. Die zahlenhaltigen, abgetrennten QA-Ausgaben liegen ausschließlich unter `outputs/loop/group-results-v21-sources/` mit Verzeichnisrechten `0700` und Dateirechten `0600`.

Ich renderte die unten angegebenen Original-PDF-Seiten und las die Bilder. Textauszüge dienten nur dazu, die Deutschlandseiten der Appendices zu finden. Bei deren Sichtprüfung waren öffentliche historische Wahlanteile und politische Beschreibungen sichtbar. Ich nutzte beides weder als Auswahlkriterium noch zur Deutung der Aggregate. Private Anteiltabellen, Zellzahlen, Gruppenbasen, Gewichtssummen und Ratios werden in diesem Bericht nicht wiedergegeben.

## Originalbindung und begrenzte Befunde

### GR21-SRC-01: unterschiedlich starke Alias-Konkordanz

`BESTANDEN` für die gebundene, ausdrücklich begrenzte Zuordnung; verbleibende Beleggrenze.

- ESS5: Der [deutsche Originalfragebogen](../../../outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf), PDF- und Druckseiten 7–8, nennt September 2009. B12A und B12B trennen Erst- und Zweitstimme. B12B trägt den gedruckten Alias `PRTVDE2`. Die aktuelle öffentliche Datei- und Variablenmetadatenbindung identifiziert `prtvcde2` als „Germany 2“ in genau `ESS5e03_6`. Die [ESS5-Appendix](../../../outputs/loop/breadth-group-binding-006/sources/ess5-political-parties-appendix.pdf), PDF- und Druckseite 20, bestätigt das historische Wahljahr und die Liste, liefert dort aber keine ausdrückliche Konkordanz zum aktuellen Exportalias.
- ESS8: Der [deutsche Originalfragebogen](../../../outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf), PDF- und Druckseiten 8–9, nennt September 2013. B14B ist die Zweitstimme mit `PRTVDE2`. Die öffentlichen Metadaten binden `prtvede2`, „Germany 2“, an `ESS8e02_3`. Die [ESS8-Appendix](../../../outputs/loop/breadth-group-binding-006/sources/ess8-political-parties-appendix.pdf), PDF-Seite 16, Druckseite 15, nennt das gleiche Wahljahr und Inventar, aber ebenfalls keine ausdrückliche aktuelle Alias-Konkordanz.
- ESS9: Der [deutsche Originalfragebogen](../../../outputs/loop/breadth-data-001/sources/ess9-de-questionnaire.pdf), PDF- und Druckseiten 8–9, nennt September 2017 und trennt B14a/B14b. Die [ESS9-Appendix](../../../outputs/loop/breadth-group-binding-006/sources/ess9-political-parties-appendix.pdf), PDF-Seite 21, Druckseite 20, ordnet `prtvede2` ausdrücklich der Zweitstimme zu. Dokumentationsausgabe 3.0 und Datendateiausgabe 3.3 bleiben verschiedene Versionsangaben.

Für ESS5 und ESS8 genügt die zusammenpassende Quellenfolge aus nationalem Original, geordnetem Erst-/Zweitstimmenpaar, API-Label und gebundener Dateivariablenidentität für die hier beschränkte Beschreibung. Sie ist schwächer als der ausdrückliche ESS9-Aliastext. Ich erkläre die fehlende zusätzliche Konkordanz nicht für gefunden oder erledigt. Der Vertrag und `_source()` des reinen Exporters erhalten genau diese Unterschiede und Grenzen. Eine spätere Darstellung muss sie mitführen.

### GR21-SRC-02: Befragungszeit und Zielpopulation begrenzen jede Aussage

`BESTANDEN` für getrennte historische Studienkontexte; keine Norm- oder Transferfreigabe.

Die öffentlichen Studienzugangsmetadaten geben als Zielpopulation Bewohner privater Haushalte ab 15 Jahren an, unabhängig von Staatsangehörigkeit. Die gebundenen Deutschland-Erhebungsmetadaten nennen CAPI/CAMI und folgende Feldzeiten: ESS5 vom 15.09.2010 bis 03.02.2011, ESS8 vom 23.08.2016 bis 26.03.2017, ESS9 vom 29.08.2018 bis 04.03.2019. Vertragsprovenienz und Exportquelle stimmen damit überein.

Die Antworten beschreiben die spätere Befragung, gruppiert nach erinnerter vergangener Zweitstimme. Sie beschreiben weder Einstellungen am Wahltag noch Parteiprogramme. Wahlrecht und tatsächliche Stimmabgabe sind nicht extern verifiziert. Die Intervieweranweisung zum absichtlich ungültigen oder unmarkierten Stimmzettel ist in den Originalen erhalten; eine separate Gruppe ungültiger Stimmen ist daraus nicht identifizierbar. Der Export behauptet weder eine unabhängige Bevölkerungsnorm noch aktuelle Parteipositionen, Parteiscores oder gemeinsame Personen über Studien hinweg.

Die deklarierte Zielpopulation ist keine bestätigte erreichte Vollabdeckung. In den öffentlichen ESS8-Samplingangaben ist die fehlende Mitwirkung Münchens dokumentiert. Dieser konkrete bekannte Abdeckungshinweis gehört zum Interpretationskontext; ein Leser darf aus dem Zielpopulationstext keine flächendeckend erreichte Deutschlandabdeckung ableiten. Der reine Export trägt den allgemeinen Vorbehalt zur nicht geprüften erreichten Abdeckung, kopiert aber nicht die gesamte Samplingbeschreibung. Der vorliegende Quellenbericht und die gebundene Studienprovenienz erhalten den konkreten Hinweis. Auch die unterschiedlichen Rückerinnerungsabstände und die unterschiedlichen Listen erlauben keine zusammengefasste aktuelle „Wählerlandschaft“.

### GR21-SRC-03: Druckcodes, Dateicodes und politische Kategorien bleiben getrennt

`BESTANDEN` für vollständige Inventare, gleiche Regeln und Nullgrenzen.

Die öffentlichen API-Codeverzeichnisse, die Dateivariablenmetadaten und die nationalen Originale stimmen für die benannten Gruppen und ihre Reihenfolge überein. ESS5 erhält auch REP und NPD; ESS8 und ESS9 erhalten auch AfD, Piratenpartei und NPD. Ursprüngliche Labels werden nicht mit heutigen Namen oder Programmen ersetzt. „Other“ bleibt in jeder Studie ein heterogener, unbenannter Rest. Freitext wird nicht gelesen, politisch homogenisiert oder zu einer Partei umgedeutet. Keine Gruppe wird wegen Appendix-Beschreibung oder öffentlichem Wahlanteil entfernt.

Die Druck-/Dateiunterschiede werden nicht umcodiert: ESS5 druckt bei Parteien Verweigerung/Weiß-nicht anders als die API. ESS9 druckt die Parteicodes mit führenden Nullen. Die API stellt außerdem eigene Missing- und Nichtanwendbarkeitscodes bereit. Der Vertrag dokumentiert diese Unterschiede; der Parser akzeptiert allein die erklärte Dateicode-Serialisierung. Leere Exportzellen bleiben technisch unklassifiziert. Es entsteht keine erfundene Antwortkategorie aus einem Missinggrund.

Die Quellenblöcke der tatsächlich gebundenen Fragen wurden visuell gegengeprüft: ESS5 D18/D20 auf PDF-/Druckseiten 24–25 und D33–D36 auf Seite 27; ESS8 D30–D32 auf Seite 33, E6–E8 auf Seite 36, E15 auf Seite 37 und E33–E35 auf Seite 42; ESS9 G26–G29 auf Seite 97. Beim [ESS8-Listenheft](../../../outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf) wurden zusätzlich PDF-Seiten 45, 49, 51 und 54 mit den Listen 44, 48, 50 und 53 gelesen. Die Bedingungen bei E15 bleiben nominale Originalalternativen. Sie werden nicht in einen Zeit- oder Migrationsscore verwandelt. Die Zustimmung zu verschiedenen Gerechtigkeitsprinzipien wird nicht zu einer latenten Achse erklärt. Die vorgesehenen Einzelbeschreibungen bewahren auch den Wortlautkontext, etwa relative Strafhärte und die feste Geldsumme bei der Bildungs-/Arbeitslosenunterstützungsfrage.

Automatische Einzelprüfungen bestätigten für jedes erlaubte Gruppen-Fragen-Paar die unveränderte Kategorieinventarliste, Fragezuordnung, gleichen Zählgrundlagen über die Gewichte und den fragebezogenen gültigen Nenner. Der Darstellungsstatus wurde unabhängig vom gelieferten Status aus dem Aggregat geprüft. Die vorab gebundene Heuristik gilt gleich für jede benannte Gruppe und „Other“; Sensitivitätsgewichte entscheiden nicht über Gruppenauswahl. Nullkategorien bleiben erhalten. Bei fehlenden gültigen Antworten bleiben die Anteile null. Unterdrückte oder nicht ausdrücklich freigegebene Paare geben im reinen Export keine private Basis, keine Anteile, Gewichte, Ratios oder Missinggrunddetails preis.

Für ausdrücklich freigegebene Referenzen enthält der festgelegte Export nur das öffentliche Accounting, die primär mit `pspwght` gewichteten Originalkategorieanteile und `uncertainty: null`. Kategorie-Zellzahlen, Gewichtssummen, Sensitivitäten, Ratio- und Eligibilitydiagnostik bleiben draußen. Die Heuristik wird weder als geprüfte Präzision noch als Anonymitätsnachweis bezeichnet. Die erfolgreiche Softwareprüfung belegt keine Repräsentativität und keine unabhängige Rohdatenreproduktion.

### GR21-SRC-04: Daten- und Dokumentationsrechte sind getrennt

`BESTANDEN` für den gebundenen Lizenzbefund; konkrete Website-/Releaseprüfung bleibt offen.

Der unveränderte öffentliche ESS-Disclaimer und die aktuellen Studienmetadaten nennen für Daten CC BY-NC-SA 4.0 und für Dokumentation CC BY-SA 4.0. Der Export erhält getrennte Lizenz-IDs, editionsbezogene Daten-DOIs und Dokumentations-DOIs, den ESS-Disclaimer als Dokumentquelle sowie Attribution und die Kennzeichnung der normalisierten Quellenzusammenstellung. Dokumentationszugang erteilt keine Datenfreigabe. Nichtkommerzialität und ShareAlike werden nicht aufgehoben.

Diese Ergebnisfreigabe bestätigt die Quellenbasis der aufgeführten Deskriptionen. Sie ersetzt weder die konkrete Lizenz-/Attributionsdarstellung am veröffentlichten Artefakt noch eine spätere kommerzielle Prüfung. Der reine JSON-Exporter trägt Lizenz-IDs und die Disclaimerquelle; verständliche Lizenzlinks und die konkrete Quellenangabe müssen in der späteren Veröffentlichungsdarstellung erhalten sein. Eine rechtsfachliche oder Produktfreigabe wird hier nicht behauptet.

## Tatsächlich freigegebene Paare

Die folgende Tabelle ist eine lesbare Darstellung meines Entscheidungs-JSON. Die Frage-IDs werden jeweils mit demselben Studienpräfix gelesen. Die dort explizit gelisteten Paarobjekte sind maßgeblich. Eine fehlende Paarung hat keine Veröffentlichungserlaubnis.

| Studie | Gruppen-ID | Fragevariablen mit ausdrücklicher Quellenfreigabe |
| --- | --- | --- |
| `ESS5e03_6` | `ESS5e03_6:second_vote:1` | `bplcdc`, `hrshsnta`, `dbctvrd`, `rgbrklw` |
| `ESS5e03_6` | `ESS5e03_6:second_vote:2` | `bplcdc`, `dpcstrb`, `hrshsnta`, `dbctvrd`, `lwstrob`, `rgbrklw` |
| `ESS5e03_6` | `ESS5e03_6:second_vote:3` | `dpcstrb`, `hrshsnta`, `dbctvrd`, `lwstrob`, `rgbrklw` |
| `ESS5e03_6` | `ESS5e03_6:second_vote:4` | `dbctvrd`, `rgbrklw` |
| `ESS5e03_6` | `ESS5e03_6:second_vote:5` | `bplcdc`, `hrshsnta`, `dbctvrd`, `rgbrklw` |
| `ESS8e02_3` | `ESS8e02_3:second_vote:1` | `bnlwinc`, `eduunmp`, `inctxff`, `sbsrnen`, `banhhap`, `imsclbn`, `wrkprbf` |
| `ESS8e02_3` | `ESS8e02_3:second_vote:2` | `gvslvue`, `bnlwinc`, `eduunmp`, `inctxff`, `sbsrnen`, `banhhap`, `imsclbn`, `wrkprbf` |
| `ESS8e02_3` | `ESS8e02_3:second_vote:3` | `bnlwinc`, `eduunmp`, `inctxff`, `banhhap`, `imsclbn`, `wrkprbf` |
| `ESS8e02_3` | `ESS8e02_3:second_vote:4` | `bnlwinc`, `eduunmp`, `inctxff`, `banhhap` |
| `ESS8e02_3` | `ESS8e02_3:second_vote:5` | `bnlwinc`, `eduunmp`, `inctxff`, `banhhap`, `wrkprbf` |
| `ESS9e03_3` | `ESS9e03_3:second_vote:1` | `sofrdst`, `sofrprv` |
| `ESS9e03_3` | `ESS9e03_3:second_vote:2` | `sofrdst`, `sofrprv` |
| `ESS9e03_3` | `ESS9e03_3:second_vote:3` | `sofrdst` |
| `ESS9e03_3` | `ESS9e03_3:second_vote:4` | `sofrdst` |
| `ESS9e03_3` | `ESS9e03_3:second_vote:5` | `sofrdst`, `sofrwrk`, `sofrprv` |
| `ESS9e03_3` | `ESS9e03_3:second_vote:6` | `sofrdst`, `sofrwrk`, `sofrprv` |

## Prüfergebnis und offene Grenzen

- `BESTANDEN`: Bytes der gebundenen öffentlichen und erlaubten privaten Artefakte, kanonische Kandidatenbindung, öffentliche API-/Datei-/Originalform-Inventare, unabhängige Aggregat-Kategorien- und Statuschecks sowie die QA am reinen Exporter für genau die erlaubten Studien.
- `NICHT_GEPRÜFT`: neue Rohdatenläufe, unabhängiger Originaldownloadnachweis, externe Verifikation der Erinnerung an die Stimmabgabe und tatsächlich erreichte Bevölkerungsabdeckung. Für diese Rolle gab es keine Rohdatenberechtigung.
- `NICHT_GEPRÜFT`: konkrete Webdarstellung und Verständnisprüfung, rechtsfachliche/kommerzielle Beurteilung, die von Steven veranlasste Claude-Schlusskontrolle sowie Human- und Releaseabnahmen.

Ich habe keinen blockierenden Quellenfehler in der festen Ergebnisfassung gefunden. GR21-SRC-01 bis GR21-SRC-04 sind konkrete, weiterhin zu erhaltende Grenzen meiner Annahme. Das Urteil erteilt keine Freigabe von Normen, Scores, aktuellen Parteiprofilen, Wahlprognosen oder einem „KI-Wähler“. Gleiche Regeln für unterschiedliche Positionen sind hier nachvollziehbar geprüft. Mehrere Codex-Rollen können dennoch gemeinsame Fehler teilen; das ist kein wissenschaftlicher Neutralitätsnachweis.

Abschluss: Das Manifest und sämtliche 64 öffentlichen sowie exakt drei privaten Pins wurden nach der Berichtserstellung nochmals gegen die tatsächlichen Bytes geprüft und waren unverändert. Andere Ergebnisberichte wurden auch für diesen Vergleich nicht gelesen.
