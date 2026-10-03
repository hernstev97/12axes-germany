# ESS-Datenlage für Deutschland

Stand 2026-10-03. Öffentliche Metadaten-Recherche und technische Dateierfassung, noch keine Antwortdatenanalyse. Fundstellen und Grenzen sind im [Belegregister](belegregister.md) verzeichnet; die abgerufenen Dokumente in [quellen.json](quellen.json).

## Recherchierter Datenkandidat

Das [ESS-11-Portal](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b) führt als Hauptdatei **ESS11, integrierte Ausgabe 4.2**, DOI [10.21338/ess11e04_2](https://doi.org/10.21338/ess11e04_2), veröffentlicht am 2. Juli 2026. Die deutsche `stratum`-Korrektur ist beim Übergang von 3.0 auf 4.0 dokumentiert. Ausgaben vor 4.0 enthalten diese dokumentierte Korrektur noch nicht; daraus folgt keine pauschale Untauglichkeit von 4.0 oder 4.1. Die Hinweise zu 4.1 und 4.2 nennen keine weitere deutschlandbezogene Änderung. Das beweist keine Gleichheit der deutschen Dateien. 4.2 bleibt als neueste veröffentlichte Ausgabe der recherchierte Kandidat. Quelle: [Dateiseite](https://ess.sikt.no/en/datafile/242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef), Abschnitt DOI and version information (B-ESS-001).

Die ESS-Mitteilung vom 30. September 2026 kündigt die erste Veröffentlichung von Runde 12 für Januar 2027 an. Runde 12 ist damit derzeit kein verfügbarer Ersatz. Quelle: [ESS-Mitteilung](https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027). Ein späterer Versionswechsel braucht eine protokollierte Entscheidung vor Analyse.

## Deutschland und Vergleichsbezug

| Merkmal            | Öffentliche Dokumentation                                                                         | Grenze                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Erhebung           | 09.05.–21.12.2023, 2.420 gültige Interviews; Portal-Rücklaufquote 26,7 %.                         | Metadaten, nicht im Rohdatensatz nachgerechnet. Keine heutige Momentaufnahme.                                            |
| Modus              | Persönliche computergestützte Interviews.                                                         | Übertragung auf Selbstbeantwortung im Web ist nicht empirisch geprüft.                                                   |
| Referenzpopulation | Personen ab 15 Jahren in Privathaushalten, unabhängig von Nationalität/Staatsangehörigkeit.       | Nicht identisch mit Wahlberechtigten oder deutschen Staatsbürgern. Erreichbarkeit/Teilnahme bleiben zusätzliche Grenzen. |
| Design             | Deutsches Wahrscheinlichkeitsdesign mit zwei Domänen, Schichtung und teilweise Gemeinde-Clustern. | Gewichtete Mittel allein liefern noch keine designgerechten Unsicherheiten.                                              |
| Region             | Länder-Dokumentation verneint Repräsentativität auf Bundeslandebene.                              | Ost-West-Prüfung braucht eigens definierte Gruppen; keine Bundesland-Ranglisten daraus ableiten.                         |
| Wahlbezug          | Deutscher Fragebogen B13: Bundestagswahl September 2021; B14a Erst-, B14b Zweitstimme.            | Historisch selbst berichtete Wahlentscheidung. Keine aktuellen Parteipositionen.                                         |

Fundstellen: Portalabschnitte **Universe, scope and method** sowie **Country documentation → Germany**; Länderbericht S. 79–80, 86, 88; deutscher Fragebogen S. 7–8 (B-ESS-002 bis B-ESS-005).

## Dokumente und Kodierungen

Der deutsche Fragebogen und das Listenheft sind öffentlich ohne Account zugänglich. Sie wurden als Quellen abgerufen; ihre vollständige Itemprüfung steht aus. Die englische Quelle ersetzt den deutschen Wortlaut nicht.

Das Portal verlinkt neben Hauptdatei 4.2 einen Codebook-Stand 4.1 und Länderbericht 4.0. Diese Dokumentausgaben werden mit ihrer tatsächlichen Version geführt. Änderungen gegenüber dem Codebook sind mit den Hauptdatei-Versionshinweisen abzugleichen.

Im Codebook ist `prtvgde1` der Kandidat für Erststimmen- und `prtvgde2` für Zweitstimmenvergleiche (PDF-S. 21–22, gedruckte S. 20–21). Die dokumentierte Nachkodierung stimmt nicht überall mit den Zahlen auf dem Interviewbogen überein. Parteikodierungen dürfen nicht aus dem Fragebogen allein übernommen werden. Vor Gruppenbildung sind Mapping, Filter und Missing-Codes der verwendeten Ausgabe abzugleichen (B-ESS-006). Noch wurde keine Gruppenentscheidung getroffen.

Der aktuell im Portal verlinkte Gewichtungsleitfaden ist V1.2 vom 6. Juli 2023. Eine Websuche fand zuerst V1.1; V1.2 ist der dokumentierte Ausgangspunkt. Die erforderlichen Designvariablen werden beim späteren Import gegen die aktuelle Datei geprüft.

## Später benötigter Download

**Inzwischen lokal vorhanden:** `data/raw/ess11-ed4.2/ESS11e04_2.csv`, von Steven bereitgestellt. Die erste CSV-Zeile enthält 691 Spalten; die ausschließlich ausgelesenen globalen Metadaten nennen Runde 11, Ausgabe 4.2 und Produktionsdatum 02.07.2026. SHA-256: `4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8`.

Die Datei ist von Git ausgeschlossen und nicht getrackt. Der Header enthält die erwarteten Gewichts-/Designfelder. Antworten, Personenkennungen und politische Verteilungen wurden nicht an den Agenten ausgegeben; es gab keine Deutschland-Selektion oder Analyse. Die vollständige CSV-Prüfung, der Abgleich mit einer Portal-Prüfsumme und die Downloadbedingungen sind noch nicht geprüft. Die bisherigen Downloadvorgaben bleiben für spätere erneute Bezüge erhalten. Details im [Dateieingangsbericht](../reports/phasen/00-dateieingang-2026-10-03.md).

Steven hat am 2026-10-03 einen ESS-Account gemeldet. Die gemeinsame Rechercheansicht ist weiterhin nicht eingeloggt; Zugangsdaten werden nicht benötigt.

Für den geplanten Import wird die **vollständige, unveränderte Hauptdatei ESS11 Ausgabe 4.2 im CSV-Format samt mitgelieferten Metadaten** benötigt: [Portal-Dateiseite](https://ess.sikt.no/en/datafile/242aaa39-3bbb-40f5-98bf-bfb1ce53d8ef) → Download nach persönlichem Login. Das heruntergeladene Originalpaket gehört nach `data/raw/ess11-ed4.2/`. Originalnamen beibehalten, keine Bearbeitung in einer Tabellenkalkulation. Datum, Ausgabe, Bedingungen und SHA-256 beim Import protokollieren; Dateiname allein beweist keine Version.

Die Deutschland-Selektion erfolgt später reproduzierbar durch die lokale Pipeline. B sowie Wahl-/Lagerinformationen werden getrennt bereitgestellt; es gibt jetzt noch keine Zugriffssperre oder Analysepipeline. Interviewer-, Kontakt- und Alkohol-Dateien sind für den gegenwärtigen Plan nicht als Analyse-Eingaben vorgesehen. Falls spätere Untersuchungen zusätzliche Dateien brauchen, wird das begründet.

Der Account bereitet den Download vor. Er erteilt keine methodische Freigabe und ändert die Reihenfolge aus dem [Analyseplan](analyseplan.md) nicht.

Korrektur der Versionswarnung nach R1-F01 im [KI-Audit](../reports/audit-recherche/README.md). Der erneute Originalabruf mit Zeit und Hash ist in [quellenbelege.json](../reports/audit-recherche/quellenbelege.json) erfasst.
