# Historische Gruppenreferenzen v2.1

Stand der gebundenen Rootentscheidung: 2026\-10\-03T15:54:40\.395473\+00:00. Darstellung: WIP, noch ohne eigene Darstellungsabnahme.

Die drei öffentlichen Ableitungen aus dem [European Social Survey (ESS)](https://www.europeansocialsurvey.org/) enthalten 63 begrenzt freigegebene Gruppen-/Fragepaare. Eine Gruppe umfasst Befragte, die nach eigener Angabe bei der jeweils genannten Bundestagswahl dieselbe Zweitstimmenkategorie gewählt haben. Alle 26 Originalgruppen einschließlich des unbenannten, heterogenen Other bleiben in API-Reihenfolge erhalten.

Die politischen Antworten stammen aus der jeweiligen Befragungszeit, nicht vom erinnerten Wahltag. Sie beschreiben weder aktuelle Parteiprogramme noch überprüfte Wahlergebnisse, heutige Wahlberechtigte oder eine unabhängige Norm. Es werden keine Personen oder Parteicodes über Studien verbunden. Es entstehen keine Scores, Ranglisten, Parteimatches, Konfidenzintervalle oder Wahlprognosen.

Jeder Anteil hat seinen eigenen gültigen Frage-Nenner innerhalb der betreffenden historischen Gruppe. `validCount` ist ungewichtet; die Kategorieanteile sind mit `pspwght` gewichtet. Gesamt-, Missing- und Nichtgestellt-Zahlen stammen unverändert aus der freigegebenen Einzelreferenz. Missing/Nichtgestellt gehen nicht in den gültigen Anteilsnenner ein. Sechs Nachkommastellen sind Anzeigeformat, kein Präzisionsnachweis; sichtbare gerundete Anteile werden nicht auf 100 % umgerechnet.

Eine Gruppe erfordert `vote=1` und einen gültigen nationalen Zweitstimmen-Dateicode. Nichtwahl, Nichtberechtigung, Partei-Missing, strukturelles Nichtgestellt und technische Exportleere bleiben unzugeordnet. Eine gültige Parteikategorie zusammen mit anderer Wahlteilnahme wird nicht korrigiert oder erraten und bildet keine Gruppe. Für diese unzugeordneten Zustände werden hier keine Fallzahlen veröffentlicht.

Die vorab festgelegten Grenzen von mindestens 100 gültigen Antworten und mindestens fünf Fällen in jeder positiven Originalkategoriezelle wurden vorgelagert geprüft. Die öffentliche Ableitung enthält keine Zellcounts, aus denen dieser Bericht die Fünferregel erneut prüfen könnte. Echte Nullkategorien bleiben erhalten. Nullreferenzen veröffentlichen keine kleinen Basen, Anteile oder Gewichtssummen. Die Grenzen sind Darstellungsheuristiken, keine validierte Präzisions- oder Anonymitätsgarantie. `uncertainty: null` bedeutet: keine Standardfehler oder Konfidenzintervalle berechnet.

Zielpopulation sind Personen ab 15 Jahren in privaten Haushalten der jeweiligen Erhebung, nicht die Wahlbevölkerung. ESS8 erfasste München nicht; Gewichtung ergänzt keine dort nicht erhobenen Antworten. ESS5/8 haben eine schwächere zusätzliche Alias-/Zweitstimmenkonkordanz als ESS9. Gedruckte Formcodes werden nicht automatisch zu Dateicodes umgedeutet. Other wird keiner konkreten Partei zugeordnet.

ESS10-SC und ESS11 sind für diesen Gruppenweg wegen offener Quellenbindungen ausgeschlossen. Ihre Einzelreferenzen bleiben getrennt davon. Das breite Hauptprodukt umfasst weiterhin 43 Originalfragen in acht Inhaltsrubriken. Vollständige Originalfragen, Einleitungen, Szenarien, Listen, Routing und Kategorien: [Fragenkatalog](../../data/politikprofil-v2.fragen.entwurf.json) und [vollständiger Themenbericht](02-politikprofil-v2-methoden-und-ergebnisse.md). Die folgenden Frageverzeichnisse wiederholen diese langen Kontexte nicht je Gruppe.

Die [Rootentscheidung](../loop/policy-group-v21-export-decisions.json) bindet die tatsächlichen öffentlichen Ableitungen und ausdrückliche Paarfreigaben beider KI-Rollen. [Methoden-Nachprüfung](../loop/reviews/GROUP-RESULTS-V21-001-methods-round1.md) und [Quellen-Ersturteil](../loop/reviews/GROUP-RESULTS-V21-001-sources-first.md) gehören zur gleichen Codex-Modellfamilie; gemeinsame Fehler bleiben möglich. Die engere Methoden-Korrekturfassung erweitert das unverändert weitergenutzte Quellenurteil nicht. Menschenprüfung, Websitegestaltung, Claude-Schlusskontrolle und Releasefreigabe stehen aus. Das Projekt ist weder validiert noch wissenschaftlich geprüft und kann keine Neutralität garantieren.

Datenquelle und Attribution: European Social Survey European Research Infrastructure (ESS ERIC); Archiv Sikt – Norwegian Agency for Shared Services in Education and Research. Die abgeleiteten Antworten unterliegen [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/), die Originaldokumentation getrennt [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Nichtkommerzielle Bedingung, Namensnennung und Weitergabe unter gleichen Bedingungen bleiben erhalten. Änderungen gegenüber dem ESS: Deutschland-/Fragenauswahl, Gruppierung nach erinnerter Zweitstimme und formatierte gewichtete Originalkategorieanteile. Die Softwarelizenz ersetzt keine Datenrechte. Details: [Lizenzakte](../../docs/lizenzen.md), [öffentliche Ableitungen](../../data/reference-groups-v21/README.md), [Gruppenvertrag](../../data/gruppenvertrag.v2.1.entwurf.json).

## Studien und Zeitbezüge

| Studie / Ausgabe | Befragungszeit | Erinnerte Bundestagswahl | Originalgruppen | Freigegebene Paare |
| --- | --- | --- | --- | --- |
| ESS5e03_6 / 3\.6 | 2010-09-15 bis 2011-02-03 | 2009 | 8 | 21 |
| ESS8e02_3 / 2\.3 | 2016-08-23 bis 2017-03-26 | 2013 | 9 | 30 |
| ESS9e03_3 / 3\.3 | 2018-08-29 bis 2019-03-04 | 2017 | 9 | 12 |

## ESS5e03_6 – Ausgabe 3\.6

[Daten-DOI](https://doi.org/10.21338/ess5e03_6) 10\.21338/ess5e03\_6; [Dokumentations-DOI](https://doi.org/10.21338/nsd-ess5-2010) 10\.21338/nsd\-ess5\-2010. Erinnerte Bundestagswahl: 2009.

Politische Antwortzeit: 2010\-09\-15T00:00:00Z bis 2011\-02\-03T00:00:00Z; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

Nationaler Gruppenanker: `vote=1` und gültiger Dateicode in `prtvcde2`. Originalfrage B12B: „Und welche Partei haben Sie mit Ihrer Zweitstimme gewählt?“. Wahlteilnahmefrage: „Manche Menschen gehen heutzutage aus verschiedenen Gründen nicht zur Wahl\. Wie ist das bei Ihnen? Haben Sie bei der letzten Bundestagswahl im September 2009 gewählt?“.

Parteifeld-UUID: `a4c2c9f4-5f55-47d2-8231-0c93e2c04e99`, Metadatenversion 4; Datei-ID: `0189b86b-8aa4-4be3-88ad-39c58b02f19f`, Metadatenversion 89.

Konkordanzstatus: WIP\_ORDERED\_FORM\_AND\_API\_LABEL\_ASSOCIATION. No separate official current export\-alias→German first/second question\-text concordance found in the queried metadata and national appendix\. Ordered questionnaire / paired API labels remain the association basis, not a newly retrieved alias\-explicit assertion\. Gedruckte Codes bleiben gesondert; automatische gedruckter-Code/Dateicode-Gleichsetzung: ausgeschlossen.

### Fragenverzeichnis

Originalfrage und gültige Kategorien gelten für alle folgenden Gruppen derselben Studie. Einleitungen, Bedingungen und vollständiger Kontext stehen im verlinkten Katalog und Themenbericht.

Nationaler Originalbeleg für `vote`: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=7), physische PDF-Seite(n) 7, 8.

Nationaler Originalbeleg für `prtvcde2`: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=8), physische PDF-Seite(n) 8.

#### `ESS5e03_6:bplcdc` – Original D18

„\.\.\.\.die Entscheidungen der Polizei zu akzeptieren, auch wenn Sie damit nicht einverstanden sind?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Voll und ganz meine Pflicht | 10 |

Fundstellen: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=24): physische PDF\-Seite\(n\) 24; originalQuestionId=D18. [ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=73c3aeb5\-3281\-47ef\-b23f\-46f648815110; sourceFieldMetadataVersion=2; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

#### `ESS5e03_6:dpcstrb` – Original D20

„\.\.\.\.zu tun, was die Polizei Ihnen sagt, auch wenn Sie die Art und Weise, wie die Polizei Sie behandelt, nicht gut finden?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Voll und ganz meine Pflicht | 10 |

Fundstellen: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=24): physische PDF\-Seite\(n\) 24, 25; originalQuestionId=D20. [ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=6fb0f716\-95a9\-43d4\-8d9e\-044e9c25462a; sourceFieldMetadataVersion=2; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

#### `ESS5e03_6:hrshsnta` – Original D33

„Menschen, die das Gesetz brechen, sollten viel härter bestraft werden, als sie heute bestraft werden\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | stimme stark zu | 1 |
| 2 | stimme zu | 2 |
| 3 | weder noch | 3 |
| 4 | lehne ab | 4 |
| 5 | lehne stark ab | 5 |

Fundstellen: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D33. [ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=fc7ed212\-da9f\-4e06\-a918\-43d6757dd3cc; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

#### `ESS5e03_6:dbctvrd` – Original D34

„Alle haben die Pflicht, ein abschließendes Gerichtsurteil zu akzeptieren\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | stimme stark zu | 1 |
| 2 | stimme zu | 2 |
| 3 | weder noch | 3 |
| 4 | lehne ab | 4 |
| 5 | lehne stark ab | 5 |

Fundstellen: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D34. [ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1f210987\-0fca\-4fbe\-aaef\-2ad611f0bad1; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

#### `ESS5e03_6:lwstrob` – Original D35

„Alle Gesetze müssen strikt befolgt werden\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | stimme stark zu | 1 |
| 2 | stimme zu | 2 |
| 3 | weder noch | 3 |
| 4 | lehne ab | 4 |
| 5 | lehne stark ab | 5 |

Fundstellen: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D35. [ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=955e2117\-2b74\-4632\-aba9\-0338fbff655f; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

#### `ESS5e03_6:rgbrklw` – Original D36

„Manchmal muss man das Gesetz brechen, um das Richtige zu tun\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | stimme stark zu | 1 |
| 2 | stimme zu | 2 |
| 3 | weder noch | 3 |
| 4 | lehne ab | 4 |
| 5 | lehne stark ab | 5 |

Fundstellen: [ess5\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf#page=27): physische PDF\-Seite\(n\) 27; originalQuestionId=D36. [ess5\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=d6c06eff\-700d\-438b\-ae82\-92f0238328c4; sourceFieldMetadataVersion=1; dataFileMetadataId=0189b86b\-8aa4\-4be3\-88ad\-39c58b02f19f; dataFileMetadataVersion=89.

### Gruppen in Originalreihenfolge

#### SPD – Dateicode 1

Gruppen-ID: `ESS5e03_6:second_vote:1`. API-Label: „Social Democratic Party \(SPD\)“. Deutsches Formlabel: SPD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Gültiger Frage-Nenner, ungewichtet: 503; Gesamtbasis dieser Frage: 507; Missing: 4; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 5,351733 % |
| 1 | 1 | 1,061124 % |
| 2 | 2 | 2,558519 % |
| 3 | 3 | 4,151125 % |
| 4 | 4 | 5,850597 % |
| 5 | 5 | 11,942041 % |
| 6 | 6 | 8,302989 % |
| 7 | 7 | 11,225227 % |
| 8 | 8 | 21,318941 % |
| 9 | 9 | 10,223068 % |
| 10 | Voll und ganz meine Pflicht | 18,014636 % |

Frage `ESS5e03_6:dpcstrb`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:hrshsnta`:

Gültiger Frage-Nenner, ungewichtet: 494; Gesamtbasis dieser Frage: 507; Missing: 13; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 16,132422 % |
| 2 | stimme zu | 42,393454 % |
| 3 | weder noch | 24,986506 % |
| 4 | lehne ab | 13,798452 % |
| 5 | lehne stark ab | 2,689165 % |

Frage `ESS5e03_6:dbctvrd`:

Gültiger Frage-Nenner, ungewichtet: 502; Gesamtbasis dieser Frage: 507; Missing: 5; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 13,862481 % |
| 2 | stimme zu | 48,425599 % |
| 3 | weder noch | 13,892812 % |
| 4 | lehne ab | 20,269332 % |
| 5 | lehne stark ab | 3,549777 % |

Frage `ESS5e03_6:lwstrob`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:rgbrklw`:

Gültiger Frage-Nenner, ungewichtet: 491; Gesamtbasis dieser Frage: 507; Missing: 16; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 6,432870 % |
| 2 | stimme zu | 40,456219 % |
| 3 | weder noch | 21,349303 % |
| 4 | lehne ab | 26,133811 % |
| 5 | lehne stark ab | 5,627798 % |

#### CDU/CSU – Dateicode 2

Gruppen-ID: `ESS5e03_6:second_vote:2`. API-Label: „Christian Democratic Union/Christian Social Union \(CDU/CSU\)“. Deutsches Formlabel: CDU/CSU. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Gültiger Frage-Nenner, ungewichtet: 611; Gesamtbasis dieser Frage: 616; Missing: 5; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 4,035455 % |
| 1 | 1 | 1,108020 % |
| 2 | 2 | 2,371778 % |
| 3 | 3 | 4,665507 % |
| 4 | 4 | 4,633509 % |
| 5 | 5 | 11,573411 % |
| 6 | 6 | 10,018824 % |
| 7 | 7 | 11,940290 % |
| 8 | 8 | 20,928968 % |
| 9 | 9 | 9,717168 % |
| 10 | Voll und ganz meine Pflicht | 19,007072 % |

Frage `ESS5e03_6:dpcstrb`:

Gültiger Frage-Nenner, ungewichtet: 607; Gesamtbasis dieser Frage: 616; Missing: 9; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 2,650081 % |
| 1 | 1 | 1,262956 % |
| 2 | 2 | 3,608461 % |
| 3 | 3 | 4,747103 % |
| 4 | 4 | 7,254003 % |
| 5 | 5 | 14,374873 % |
| 6 | 6 | 8,733427 % |
| 7 | 7 | 15,293634 % |
| 8 | 8 | 15,986055 % |
| 9 | 9 | 10,625635 % |
| 10 | Voll und ganz meine Pflicht | 15,463771 % |

Frage `ESS5e03_6:hrshsnta`:

Gültiger Frage-Nenner, ungewichtet: 603; Gesamtbasis dieser Frage: 616; Missing: 13; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 16,834043 % |
| 2 | stimme zu | 49,716801 % |
| 3 | weder noch | 22,767802 % |
| 4 | lehne ab | 9,290957 % |
| 5 | lehne stark ab | 1,390396 % |

Frage `ESS5e03_6:dbctvrd`:

Gültiger Frage-Nenner, ungewichtet: 612; Gesamtbasis dieser Frage: 616; Missing: 4; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 13,420616 % |
| 2 | stimme zu | 55,422659 % |
| 3 | weder noch | 12,102157 % |
| 4 | lehne ab | 16,527024 % |
| 5 | lehne stark ab | 2,527545 % |

Frage `ESS5e03_6:lwstrob`:

Gültiger Frage-Nenner, ungewichtet: 612; Gesamtbasis dieser Frage: 616; Missing: 4; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 17,507870 % |
| 2 | stimme zu | 60,996933 % |
| 3 | weder noch | 12,579654 % |
| 4 | lehne ab | 7,844977 % |
| 5 | lehne stark ab | 1,070566 % |

Frage `ESS5e03_6:rgbrklw`:

Gültiger Frage-Nenner, ungewichtet: 593; Gesamtbasis dieser Frage: 616; Missing: 23; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 4,791840 % |
| 2 | stimme zu | 42,006596 % |
| 3 | weder noch | 17,215316 % |
| 4 | lehne ab | 27,751720 % |
| 5 | lehne stark ab | 8,234528 % |

#### Bündnis 90/Die Grünen – Dateicode 3

Gruppen-ID: `ESS5e03_6:second_vote:3`. API-Label: „Alliance 90/The Greens \(Bündnis 90/Die Grünen\)“. Deutsches Formlabel: Bündnis 90/Die Grünen. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dpcstrb`:

Gültiger Frage-Nenner, ungewichtet: 263; Gesamtbasis dieser Frage: 267; Missing: 4; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 3,323072 % |
| 1 | 1 | 2,220801 % |
| 2 | 2 | 3,043814 % |
| 3 | 3 | 11,712178 % |
| 4 | 4 | 6,847969 % |
| 5 | 5 | 14,729452 % |
| 6 | 6 | 7,415749 % |
| 7 | 7 | 18,959500 % |
| 8 | 8 | 16,851468 % |
| 9 | 9 | 6,506643 % |
| 10 | Voll und ganz meine Pflicht | 8,389354 % |

Frage `ESS5e03_6:hrshsnta`:

Gültiger Frage-Nenner, ungewichtet: 259; Gesamtbasis dieser Frage: 267; Missing: 8; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 8,723308 % |
| 2 | stimme zu | 27,575248 % |
| 3 | weder noch | 33,934405 % |
| 4 | lehne ab | 24,242982 % |
| 5 | lehne stark ab | 5,524056 % |

Frage `ESS5e03_6:dbctvrd`:

Gültiger Frage-Nenner, ungewichtet: 264; Gesamtbasis dieser Frage: 267; Missing: 3; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 11,323750 % |
| 2 | stimme zu | 39,705170 % |
| 3 | weder noch | 23,104499 % |
| 4 | lehne ab | 22,223300 % |
| 5 | lehne stark ab | 3,643281 % |

Frage `ESS5e03_6:lwstrob`:

Gültiger Frage-Nenner, ungewichtet: 264; Gesamtbasis dieser Frage: 267; Missing: 3; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 7,906242 % |
| 2 | stimme zu | 53,858643 % |
| 3 | weder noch | 19,790741 % |
| 4 | lehne ab | 15,977610 % |
| 5 | lehne stark ab | 2,466764 % |

Frage `ESS5e03_6:rgbrklw`:

Gültiger Frage-Nenner, ungewichtet: 261; Gesamtbasis dieser Frage: 267; Missing: 6; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 7,074238 % |
| 2 | stimme zu | 47,720591 % |
| 3 | weder noch | 18,193518 % |
| 4 | lehne ab | 22,964708 % |
| 5 | lehne stark ab | 4,046945 % |

#### FDP – Dateicode 4

Gruppen-ID: `ESS5e03_6:second_vote:4`. API-Label: „Free Democratic Party \(FDP\) “. Deutsches Formlabel: FDP. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dpcstrb`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:hrshsnta`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dbctvrd`:

Gültiger Frage-Nenner, ungewichtet: 233; Gesamtbasis dieser Frage: 235; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 14,189085 % |
| 2 | stimme zu | 47,814738 % |
| 3 | weder noch | 15,666308 % |
| 4 | lehne ab | 19,052218 % |
| 5 | lehne stark ab | 3,277650 % |

Frage `ESS5e03_6:lwstrob`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:rgbrklw`:

Gültiger Frage-Nenner, ungewichtet: 229; Gesamtbasis dieser Frage: 235; Missing: 6; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 6,149048 % |
| 2 | stimme zu | 45,959877 % |
| 3 | weder noch | 16,689687 % |
| 4 | lehne ab | 23,635229 % |
| 5 | lehne stark ab | 7,566159 % |

#### Die Linke – Dateicode 5

Gruppen-ID: `ESS5e03_6:second_vote:5`. API-Label: „The Left \(Die Linke\)“. Deutsches Formlabel: Die Linke. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Gültiger Frage-Nenner, ungewichtet: 200; Gesamtbasis dieser Frage: 201; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 0 | Überhaupt nicht meine Pflicht | 3,950568 % |
| 1 | 1 | 0,000000 % |
| 2 | 2 | 6,423199 % |
| 3 | 3 | 7,455347 % |
| 4 | 4 | 4,297313 % |
| 5 | 5 | 15,838683 % |
| 6 | 6 | 8,482995 % |
| 7 | 7 | 10,462427 % |
| 8 | 8 | 18,644342 % |
| 9 | 9 | 9,429039 % |
| 10 | Voll und ganz meine Pflicht | 15,016086 % |

Frage `ESS5e03_6:dpcstrb`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:hrshsnta`:

Gültiger Frage-Nenner, ungewichtet: 196; Gesamtbasis dieser Frage: 201; Missing: 5; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 21,211206 % |
| 2 | stimme zu | 39,778930 % |
| 3 | weder noch | 22,914532 % |
| 4 | lehne ab | 13,069038 % |
| 5 | lehne stark ab | 3,026294 % |

Frage `ESS5e03_6:dbctvrd`:

Gültiger Frage-Nenner, ungewichtet: 200; Gesamtbasis dieser Frage: 201; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 14,979328 % |
| 2 | stimme zu | 41,464896 % |
| 3 | weder noch | 12,241377 % |
| 4 | lehne ab | 24,087411 % |
| 5 | lehne stark ab | 7,226989 % |

Frage `ESS5e03_6:lwstrob`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:rgbrklw`:

Gültiger Frage-Nenner, ungewichtet: 194; Gesamtbasis dieser Frage: 201; Missing: 7; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | stimme stark zu | 9,908267 % |
| 2 | stimme zu | 48,143129 % |
| 3 | weder noch | 15,419968 % |
| 4 | lehne ab | 20,868828 % |
| 5 | lehne stark ab | 5,659807 % |

#### Die Republikaner – Dateicode 6

Gruppen-ID: `ESS5e03_6:second_vote:6`. API-Label: „The Republicans \(REP\)“. Deutsches Formlabel: Die Republikaner. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dpcstrb`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:hrshsnta`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dbctvrd`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:lwstrob`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:rgbrklw`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### NPD – Dateicode 7

Gruppen-ID: `ESS5e03_6:second_vote:7`. API-Label: „National Democratic Party \(NPD\)“. Deutsches Formlabel: NPD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS5e03_6:bplcdc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dpcstrb`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:hrshsnta`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dbctvrd`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:lwstrob`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:rgbrklw`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### Other – Dateicode 8

Gruppen-ID: `ESS5e03_6:second_vote:8`. API-Label: „Other“. Deutsches Formlabel: nicht gebunden. Deutsches Appendix-Label: nicht gebunden.

Other ist die unbenannte, heterogene Originalkategorie; keine konkrete Partei und keine einheitliche politische Gruppe.

Frage `ESS5e03_6:bplcdc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dpcstrb`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:hrshsnta`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:dbctvrd`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:lwstrob`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS5e03_6:rgbrklw`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.


## ESS8e02_3 – Ausgabe 2\.3

[Daten-DOI](https://doi.org/10.21338/ess8e02_3) 10\.21338/ess8e02\_3; [Dokumentations-DOI](https://doi.org/10.21338/nsd-ess8-2016) 10\.21338/nsd\-ess8\-2016. Erinnerte Bundestagswahl: 2013.

Politische Antwortzeit: 2016\-08\-23T00:00:00Z bis 2017\-03\-26T00:00:00Z; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

Nationaler Gruppenanker: `vote=1` und gültiger Dateicode in `prtvede2`. Originalfrage B14B: „Und welche Partei haben Sie mit Ihrer Zweitstimme gewählt?“. Wahlteilnahmefrage: „Manche Menschen gehen heutzutage aus verschiedenen Gründen nicht zur Wahl\. Wie ist das bei Ihnen? Haben Sie bei der letzten Bundestagswahl im September 2013 gewählt?“.

Parteifeld-UUID: `ae314cc9-e923-4dfe-900c-75b5d2b646c7`, Metadatenversion 4; Datei-ID: `ffc43f48-e15a-4a1c-8813-47eda377c355`, Metadatenversion 98.

Konkordanzstatus: WIP\_ORDERED\_FORM\_AND\_API\_LABEL\_ASSOCIATION. No separate official current export\-alias→German first/second question\-text concordance found in the queried metadata and national appendix\. Ordered questionnaire / paired API labels remain the association basis, not a newly retrieved alias\-explicit assertion\. Gedruckte Codes bleiben gesondert; automatische gedruckter-Code/Dateicode-Gleichsetzung: ausgeschlossen.

### Fragenverzeichnis

Originalfrage und gültige Kategorien gelten für alle folgenden Gruppen derselben Studie. Einleitungen, Bedingungen und vollständiger Kontext stehen im verlinkten Katalog und Themenbericht.

Nationaler Originalbeleg für `vote`: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=8), physische PDF-Seite(n) 8.

Nationaler Originalbeleg für `prtvede2`: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=9), physische PDF-Seite(n) 9.

#### `ESS8e02_3:gvslvol` – Original E6

„…einen angemessenen Lebensstandard im Alter sicherzustellen?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 10 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=36): physische PDF\-Seite\(n\) 36; originalQuestionId=E6. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=7a2e25a8\-5d2b\-416a\-a77b\-9753aea54ee8; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=49): physische PDF\-Seite\(n\) 49; listLabelDe=Liste 48.

#### `ESS8e02_3:gvslvue` – Original E7

„…einen angemessenen Lebensstandard für Arbeitslose sicherzustellen?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 10 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=36): physische PDF\-Seite\(n\) 36; originalQuestionId=E7. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=962d9df9\-c6c6\-459e\-baba\-65fa16802b76; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=49): physische PDF\-Seite\(n\) 49; listLabelDe=Liste 48.

#### `ESS8e02_3:gvcldcr` – Original E8

„…ausreichende Kinderbetreuungsmöglichkeiten für berufstätige Eltern sicherzustellen?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 |
| 4 | 4 | 4 |
| 5 | 5 | 5 |
| 6 | 6 | 6 |
| 7 | 7 | 7 |
| 8 | 8 | 8 |
| 9 | 9 | 9 |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 10 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=36): physische PDF\-Seite\(n\) 36; originalQuestionId=E8. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=e07f9665\-727d\-4e02\-90d9\-cc833c1f76d6; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=49): physische PDF\-Seite\(n\) 49; listLabelDe=Liste 48.

#### `ESS8e02_3:bnlwinc` – Original E33

„Wären Sie dagegen oder dafür, dass nur noch die Personen mit den niedrigsten Einkommen staatliche Sozialleistungen erhalten würden, während Personen mit einem mittleren oder hohen Einkommen auf sich selbst gestellt wären?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sehr dagegen | 1 |
| 2 | Dagegen | 2 |
| 3 | Dafür | 3 |
| 4 | Sehr dafür | 4 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=42): physische PDF\-Seite\(n\) 42; originalQuestionId=E33. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=45ff83b1\-9869\-4e52\-944d\-9d41ef7cb451; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=54): physische PDF\-Seite\(n\) 54; listLabelDe=Liste 53.

#### `ESS8e02_3:eduunmp` – Original E34

„Wären Sie dagegen oder dafür, dass der Staat mehr für die Aus\- und Weiterbildung von Arbeitslosen ausgibt, aber dafür weniger Arbeitslosenunterstützung zahlt?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sehr dagegen | 1 |
| 2 | Dagegen | 2 |
| 3 | Dafür | 3 |
| 4 | Sehr dafür | 4 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=42): physische PDF\-Seite\(n\) 42; originalQuestionId=E34. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=17a2ea46\-23de\-438c\-80d1\-02d1915d4e26; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=54): physische PDF\-Seite\(n\) 54; listLabelDe=Liste 53.

#### `ESS8e02_3:inctxff` – Original D30

„Erhöhung der Abgaben auf fossile Brennstoffe wie Öl, Gas und Kohle\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sehr dafür | 1 |
| 2 | Eher dafür | 2 |
| 3 | Weder dafür noch dagegen | 3 |
| 4 | Eher dagegen | 4 |
| 5 | Sehr dagegen | 5 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=33): physische PDF\-Seite\(n\) 33; originalQuestionId=D30. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=d5cf7d14\-16c1\-42b7\-883b\-1f894d883fa9; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=45): physische PDF\-Seite\(n\) 45; listLabelDe=Liste 44.

#### `ESS8e02_3:sbsrnen` – Original D31

„Verwendung öffentlicher Gelder zur Förderung erneuerbarer Energiequellen wie Wind\- oder Sonnenenergie\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sehr dafür | 1 |
| 2 | Eher dafür | 2 |
| 3 | Weder dafür noch dagegen | 3 |
| 4 | Eher dagegen | 4 |
| 5 | Sehr dagegen | 5 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=33): physische PDF\-Seite\(n\) 33; originalQuestionId=D31. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=63374869\-47d9\-466e\-8478\-28e5df0fcaea; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=45): physische PDF\-Seite\(n\) 45; listLabelDe=Liste 44.

#### `ESS8e02_3:banhhap` – Original D32

„Ein gesetzliches Verbot für den Verkauf von Haushaltgeräten mit der schlechtesten Energieeffizienz\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sehr dafür | 1 |
| 2 | Eher dafür | 2 |
| 3 | Weder dafür noch dagegen | 3 |
| 4 | Eher dagegen | 4 |
| 5 | Sehr dagegen | 5 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=33): physische PDF\-Seite\(n\) 33; originalQuestionId=D32. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=c8bdf3e2\-f614\-4608\-bc3f\-b1f9a680898b; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=45): physische PDF\-Seite\(n\) 45; listLabelDe=Liste 44.

#### `ESS8e02_3:imsclbn` – Original E15

„Wenn Sie nun einmal an Menschen denken, die aus anderen Ländern nach Deutschland kommen, um hier zu leben\. Was glauben Sie: Wann sollten sie die gleichen Rechte auf Sozialleistungen bekommen wie die Bürger, die bereits hier leben? Bitte wählen Sie von Liste 50 die Antwortmöglichkeit, die Ihrer Sichtweise am nächsten kommt\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sofort bei ihrer Ankunft\. | 1 |
| 2 | Nachdem sie ein Jahr in Deutschland gelebt haben, unabhängig davon, ob sie gearbeitet haben oder nicht\. | 2 |
| 3 | Erst nachdem sie mindestens ein Jahr gearbeitet und Steuern bezahlt haben\. | 3 |
| 4 | Sobald sie deutsche Staatsbürger geworden sind\. | 4 |
| 5 | Sie sollten niemals die gleichen Rechte bekommen\. | 5 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=37): physische PDF\-Seite\(n\) 37; originalQuestionId=E15. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=53086955\-504b\-4fc0\-84f9\-96941928bf38; sourceFieldMetadataVersion=1; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=51): physische PDF\-Seite\(n\) 51; listLabelDe=Liste 50.

#### `ESS8e02_3:wrkprbf` – Original E35

„Wären Sie dagegen oder dafür, dass Staat und Regierung zusätzliche Sozialleistungen einführen, die es erwerbstätigen Eltern erleichtern, Arbeit und Familie zu vereinbaren, auch wenn das deutlich höhere Steuern für alle bedeuten würde?“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Sehr dagegen | 1 |
| 2 | Dagegen | 2 |
| 3 | Dafür | 3 |
| 4 | Sehr dafür | 4 |

Fundstellen: [ess8\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf#page=42): physische PDF\-Seite\(n\) 42; originalQuestionId=E35. [ess8\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=93a84094\-1c22\-476c\-9ed8\-41c96c142465; sourceFieldMetadataVersion=2; dataFileMetadataId=ffc43f48\-e15a\-4a1c\-8813\-47eda377c355; dataFileMetadataVersion=98. [ess8\-de\-showcards](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf#page=54): physische PDF\-Seite\(n\) 54; listLabelDe=Liste 53.

### Gruppen in Originalreihenfolge

#### CDU/CSU – Dateicode 1

Gruppen-ID: `ESS8e02_3:second_vote:1`. API-Label: „Christian Democratic Union/Christian Social Union \(CDU/CSU\)“. Deutsches Formlabel: CDU/CSU. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Gültiger Frage-Nenner, ungewichtet: 681; Gesamtbasis dieser Frage: 693; Missing: 12; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 13,853729 % |
| 2 | Dagegen | 47,716617 % |
| 3 | Dafür | 33,349800 % |
| 4 | Sehr dafür | 5,079854 % |

Frage `ESS8e02_3:eduunmp`:

Gültiger Frage-Nenner, ungewichtet: 677; Gesamtbasis dieser Frage: 693; Missing: 16; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 3,570234 % |
| 2 | Dagegen | 34,919333 % |
| 3 | Dafür | 54,201480 % |
| 4 | Sehr dafür | 7,308954 % |

Frage `ESS8e02_3:inctxff`:

Gültiger Frage-Nenner, ungewichtet: 689; Gesamtbasis dieser Frage: 693; Missing: 4; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 5,941505 % |
| 2 | Eher dafür | 27,486275 % |
| 3 | Weder dafür noch dagegen | 25,203921 % |
| 4 | Eher dagegen | 31,957935 % |
| 5 | Sehr dagegen | 9,410364 % |

Frage `ESS8e02_3:sbsrnen`:

Gültiger Frage-Nenner, ungewichtet: 692; Gesamtbasis dieser Frage: 693; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 33,355078 % |
| 2 | Eher dafür | 50,247741 % |
| 3 | Weder dafür noch dagegen | 7,052027 % |
| 4 | Eher dagegen | 7,525798 % |
| 5 | Sehr dagegen | 1,819356 % |

Frage `ESS8e02_3:banhhap`:

Gültiger Frage-Nenner, ungewichtet: 693; Gesamtbasis dieser Frage: 693; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 39,297208 % |
| 2 | Eher dafür | 34,132332 % |
| 3 | Weder dafür noch dagegen | 11,193172 % |
| 4 | Eher dagegen | 12,188647 % |
| 5 | Sehr dagegen | 3,188641 % |

Frage `ESS8e02_3:imsclbn`:

Gültiger Frage-Nenner, ungewichtet: 686; Gesamtbasis dieser Frage: 693; Missing: 7; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sofort bei ihrer Ankunft\. | 6,861564 % |
| 2 | Nachdem sie ein Jahr in Deutschland gelebt haben, unabhängig davon, ob sie gearbeitet haben oder nicht\. | 10,515869 % |
| 3 | Erst nachdem sie mindestens ein Jahr gearbeitet und Steuern bezahlt haben\. | 54,459263 % |
| 4 | Sobald sie deutsche Staatsbürger geworden sind\. | 25,626604 % |
| 5 | Sie sollten niemals die gleichen Rechte bekommen\. | 2,536700 % |

Frage `ESS8e02_3:wrkprbf`:

Gültiger Frage-Nenner, ungewichtet: 679; Gesamtbasis dieser Frage: 693; Missing: 14; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 2,676372 % |
| 2 | Dagegen | 36,815767 % |
| 3 | Dafür | 53,475916 % |
| 4 | Sehr dafür | 7,031945 % |

#### SPD – Dateicode 2

Gruppen-ID: `ESS8e02_3:second_vote:2`. API-Label: „Social Democratic Party \(SPD\)“. Deutsches Formlabel: SPD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Gültiger Frage-Nenner, ungewichtet: 506; Gesamtbasis dieser Frage: 507; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 0 | Der Staat sollte dafür überhaupt nicht verantwortlich sein | 1,206839 % |
| 1 | 1 | 0,959048 % |
| 2 | 2 | 1,056901 % |
| 3 | 3 | 8,787429 % |
| 4 | 4 | 7,824800 % |
| 5 | 5 | 22,148332 % |
| 6 | 6 | 15,633987 % |
| 7 | 7 | 18,184090 % |
| 8 | 8 | 13,530148 % |
| 9 | 9 | 4,816017 % |
| 10 | Der Staat sollte dafür voll und ganz verantwortlich sein | 5,852410 % |

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Gültiger Frage-Nenner, ungewichtet: 501; Gesamtbasis dieser Frage: 507; Missing: 6; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 17,747748 % |
| 2 | Dagegen | 40,370288 % |
| 3 | Dafür | 37,470331 % |
| 4 | Sehr dafür | 4,411632 % |

Frage `ESS8e02_3:eduunmp`:

Gültiger Frage-Nenner, ungewichtet: 496; Gesamtbasis dieser Frage: 507; Missing: 11; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 3,937253 % |
| 2 | Dagegen | 39,530627 % |
| 3 | Dafür | 50,493576 % |
| 4 | Sehr dafür | 6,038544 % |

Frage `ESS8e02_3:inctxff`:

Gültiger Frage-Nenner, ungewichtet: 505; Gesamtbasis dieser Frage: 507; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 7,523629 % |
| 2 | Eher dafür | 33,082115 % |
| 3 | Weder dafür noch dagegen | 23,351906 % |
| 4 | Eher dagegen | 27,310373 % |
| 5 | Sehr dagegen | 8,731977 % |

Frage `ESS8e02_3:sbsrnen`:

Gültiger Frage-Nenner, ungewichtet: 506; Gesamtbasis dieser Frage: 507; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 40,581688 % |
| 2 | Eher dafür | 48,283121 % |
| 3 | Weder dafür noch dagegen | 4,505950 % |
| 4 | Eher dagegen | 5,012968 % |
| 5 | Sehr dagegen | 1,616272 % |

Frage `ESS8e02_3:banhhap`:

Gültiger Frage-Nenner, ungewichtet: 507; Gesamtbasis dieser Frage: 507; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 37,514841 % |
| 2 | Eher dafür | 32,712148 % |
| 3 | Weder dafür noch dagegen | 10,863955 % |
| 4 | Eher dagegen | 14,064388 % |
| 5 | Sehr dagegen | 4,844668 % |

Frage `ESS8e02_3:imsclbn`:

Gültiger Frage-Nenner, ungewichtet: 505; Gesamtbasis dieser Frage: 507; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sofort bei ihrer Ankunft\. | 12,676917 % |
| 2 | Nachdem sie ein Jahr in Deutschland gelebt haben, unabhängig davon, ob sie gearbeitet haben oder nicht\. | 13,286675 % |
| 3 | Erst nachdem sie mindestens ein Jahr gearbeitet und Steuern bezahlt haben\. | 50,176243 % |
| 4 | Sobald sie deutsche Staatsbürger geworden sind\. | 22,543644 % |
| 5 | Sie sollten niemals die gleichen Rechte bekommen\. | 1,316521 % |

Frage `ESS8e02_3:wrkprbf`:

Gültiger Frage-Nenner, ungewichtet: 500; Gesamtbasis dieser Frage: 507; Missing: 7; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 3,175734 % |
| 2 | Dagegen | 32,088678 % |
| 3 | Dafür | 56,717782 % |
| 4 | Sehr dafür | 8,017807 % |

#### Die Linke – Dateicode 3

Gruppen-ID: `ESS8e02_3:second_vote:3`. API-Label: „The Left \(Die Linke\)“. Deutsches Formlabel: Die Linke. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Gültiger Frage-Nenner, ungewichtet: 190; Gesamtbasis dieser Frage: 193; Missing: 3; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 16,482295 % |
| 2 | Dagegen | 40,853123 % |
| 3 | Dafür | 30,849846 % |
| 4 | Sehr dafür | 11,814736 % |

Frage `ESS8e02_3:eduunmp`:

Gültiger Frage-Nenner, ungewichtet: 187; Gesamtbasis dieser Frage: 193; Missing: 6; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 8,862265 % |
| 2 | Dagegen | 44,705399 % |
| 3 | Dafür | 39,391606 % |
| 4 | Sehr dafür | 7,040729 % |

Frage `ESS8e02_3:inctxff`:

Gültiger Frage-Nenner, ungewichtet: 192; Gesamtbasis dieser Frage: 193; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 17,126548 % |
| 2 | Eher dafür | 23,944630 % |
| 3 | Weder dafür noch dagegen | 15,444056 % |
| 4 | Eher dagegen | 32,029218 % |
| 5 | Sehr dagegen | 11,455548 % |

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Gültiger Frage-Nenner, ungewichtet: 193; Gesamtbasis dieser Frage: 193; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 35,879319 % |
| 2 | Eher dafür | 34,772225 % |
| 3 | Weder dafür noch dagegen | 15,375185 % |
| 4 | Eher dagegen | 8,875977 % |
| 5 | Sehr dagegen | 5,097294 % |

Frage `ESS8e02_3:imsclbn`:

Gültiger Frage-Nenner, ungewichtet: 191; Gesamtbasis dieser Frage: 193; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sofort bei ihrer Ankunft\. | 15,318434 % |
| 2 | Nachdem sie ein Jahr in Deutschland gelebt haben, unabhängig davon, ob sie gearbeitet haben oder nicht\. | 13,685329 % |
| 3 | Erst nachdem sie mindestens ein Jahr gearbeitet und Steuern bezahlt haben\. | 45,815944 % |
| 4 | Sobald sie deutsche Staatsbürger geworden sind\. | 22,180801 % |
| 5 | Sie sollten niemals die gleichen Rechte bekommen\. | 2,999492 % |

Frage `ESS8e02_3:wrkprbf`:

Gültiger Frage-Nenner, ungewichtet: 191; Gesamtbasis dieser Frage: 193; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 5,553024 % |
| 2 | Dagegen | 29,513160 % |
| 3 | Dafür | 50,623024 % |
| 4 | Sehr dafür | 14,310793 % |

#### Bündnis90/Die Grünen – Dateicode 4

Gruppen-ID: `ESS8e02_3:second_vote:4`. API-Label: „Alliance 90/The Greens \(Bündnis 90/Die Grünen\)“. Deutsches Formlabel: Bündnis90/Die Grünen. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Gültiger Frage-Nenner, ungewichtet: 240; Gesamtbasis dieser Frage: 242; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 19,616272 % |
| 2 | Dagegen | 49,101257 % |
| 3 | Dafür | 27,475274 % |
| 4 | Sehr dafür | 3,807197 % |

Frage `ESS8e02_3:eduunmp`:

Gültiger Frage-Nenner, ungewichtet: 237; Gesamtbasis dieser Frage: 242; Missing: 5; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 4,309327 % |
| 2 | Dagegen | 31,223138 % |
| 3 | Dafür | 53,162754 % |
| 4 | Sehr dafür | 11,304781 % |

Frage `ESS8e02_3:inctxff`:

Gültiger Frage-Nenner, ungewichtet: 241; Gesamtbasis dieser Frage: 242; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 16,107308 % |
| 2 | Eher dafür | 41,837685 % |
| 3 | Weder dafür noch dagegen | 12,658416 % |
| 4 | Eher dagegen | 27,376306 % |
| 5 | Sehr dagegen | 2,020286 % |

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Gültiger Frage-Nenner, ungewichtet: 241; Gesamtbasis dieser Frage: 242; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 41,176685 % |
| 2 | Eher dafür | 33,129776 % |
| 3 | Weder dafür noch dagegen | 10,587009 % |
| 4 | Eher dagegen | 11,625891 % |
| 5 | Sehr dagegen | 3,480640 % |

Frage `ESS8e02_3:imsclbn`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:wrkprbf`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### FDP – Dateicode 5

Gruppen-ID: `ESS8e02_3:second_vote:5`. API-Label: „Free Democratic Party \(FDP\) “. Deutsches Formlabel: FDP. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Gültiger Frage-Nenner, ungewichtet: 108; Gesamtbasis dieser Frage: 110; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 15,041375 % |
| 2 | Dagegen | 46,246913 % |
| 3 | Dafür | 32,768136 % |
| 4 | Sehr dafür | 5,943577 % |

Frage `ESS8e02_3:eduunmp`:

Gültiger Frage-Nenner, ungewichtet: 110; Gesamtbasis dieser Frage: 110; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 8,918989 % |
| 2 | Dagegen | 33,955723 % |
| 3 | Dafür | 51,619633 % |
| 4 | Sehr dafür | 5,505655 % |

Frage `ESS8e02_3:inctxff`:

Gültiger Frage-Nenner, ungewichtet: 110; Gesamtbasis dieser Frage: 110; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 5,003779 % |
| 2 | Eher dafür | 34,146831 % |
| 3 | Weder dafür noch dagegen | 22,331906 % |
| 4 | Eher dagegen | 24,902145 % |
| 5 | Sehr dagegen | 13,615339 % |

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Gültiger Frage-Nenner, ungewichtet: 110; Gesamtbasis dieser Frage: 110; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dafür | 30,593562 % |
| 2 | Eher dafür | 42,455628 % |
| 3 | Weder dafür noch dagegen | 6,149051 % |
| 4 | Eher dagegen | 16,948553 % |
| 5 | Sehr dagegen | 3,853206 % |

Frage `ESS8e02_3:imsclbn`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:wrkprbf`:

Gültiger Frage-Nenner, ungewichtet: 109; Gesamtbasis dieser Frage: 110; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Sehr dagegen | 9,193028 % |
| 2 | Dagegen | 33,492173 % |
| 3 | Dafür | 49,235710 % |
| 4 | Sehr dafür | 8,079089 % |

#### AfD – Dateicode 6

Gruppen-ID: `ESS8e02_3:second_vote:6`. API-Label: „Alternative for Germany \(AFD\)“. Deutsches Formlabel: AfD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:eduunmp`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:inctxff`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:imsclbn`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:wrkprbf`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### Piratenpartei – Dateicode 7

Gruppen-ID: `ESS8e02_3:second_vote:7`. API-Label: „Pirate Party \(Piratenpartei\)“. Deutsches Formlabel: Piratenpartei. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:eduunmp`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:inctxff`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:imsclbn`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:wrkprbf`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### NPD – Dateicode 8

Gruppen-ID: `ESS8e02_3:second_vote:8`. API-Label: „National Democratic Party \(NPD\)“. Deutsches Formlabel: NPD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:eduunmp`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:inctxff`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:imsclbn`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:wrkprbf`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### Other – Dateicode 9

Gruppen-ID: `ESS8e02_3:second_vote:9`. API-Label: „Other“. Deutsches Formlabel: nicht gebunden. Deutsches Appendix-Label: nicht gebunden.

Other ist die unbenannte, heterogene Originalkategorie; keine konkrete Partei und keine einheitliche politische Gruppe.

Frage `ESS8e02_3:gvslvol`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvslvue`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:gvcldcr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:bnlwinc`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:eduunmp`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:inctxff`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:sbsrnen`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:banhhap`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:imsclbn`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS8e02_3:wrkprbf`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.


## ESS9e03_3 – Ausgabe 3\.3

[Daten-DOI](https://doi.org/10.21338/ess9e03_3) 10\.21338/ess9e03\_3; [Dokumentations-DOI](https://doi.org/10.21338/nsd-ess9-2018) 10\.21338/nsd\-ess9\-2018. Erinnerte Bundestagswahl: 2017.

Politische Antwortzeit: 2018\-08\-29T00:00:00Z bis 2019\-03\-04T00:00:00Z; deklarierter Modus: Face\-to\-face interview: Computer\-assisted \(CAPI/CAMI\).

Nationaler Gruppenanker: `vote=1` und gültiger Dateicode in `prtvede2`. Originalfrage B14b: „Und welche Partei haben Sie mit Ihrer Zweitstimme gewählt?“. Wahlteilnahmefrage: „Manche Menschen gehen heutzutage aus verschiedenen Gründen nicht zur Wahl\. Wie ist das bei Ihnen? Haben Sie bei der letzten Bundestagswahl im September 2017 gewählt?“.

Parteifeld-UUID: `8081ac23-287b-4548-8997-4dee9fb0463c`, Metadatenversion 6; Datei-ID: `b2b0bf39-176b-4eca-8d26-3c05ea83d2cb`, Metadatenversion 280.

Konkordanzstatus: OFFICIAL\_ALIAS\_EXPLICIT\_TEXT\_BOUND. Official national appendix explicitly supplies current alias and vote type; German original wording still comes from the separately bound national questionnaire\. Appendix edition3\.0 is a documentation edition, not a replacement for file edition3\.3\. Gedruckte Codes bleiben gesondert; automatische gedruckter-Code/Dateicode-Gleichsetzung: ausgeschlossen.

### Fragenverzeichnis

Originalfrage und gültige Kategorien gelten für alle folgenden Gruppen derselben Studie. Einleitungen, Bedingungen und vollständiger Kontext stehen im verlinkten Katalog und Themenbericht.

Nationaler Originalbeleg für `vote`: [ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=8), physische PDF-Seite(n) 8.

Nationaler Originalbeleg für `prtvede2`: [ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=9), physische PDF-Seite(n) 9.

#### `ESS9e03_3:sofrdst` – Original G26

„Eine Gesellschaft ist gerecht, wenn Einkommen und Vermögen gleichmäßig auf alle Menschen verteilt sind\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Stimme stark zu | 1 |
| 2 | Stimme zu | 2 |
| 3 | Weder noch | 3 |
| 4 | Lehne ab | 4 |
| 5 | Lehne stark ab | 5 |

Fundstellen: [ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G26. [ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=a0bf64ee\-18c0\-404b\-979a\-af7d87edebb2; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

#### `ESS9e03_3:sofrwrk` – Original G27

„Eine Gesellschaft ist gerecht, wenn hart arbeitende Menschen mehr verdienen als andere\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Stimme stark zu | 1 |
| 2 | Stimme zu | 2 |
| 3 | Weder noch | 3 |
| 4 | Lehne ab | 4 |
| 5 | Lehne stark ab | 5 |

Fundstellen: [ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G27. [ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=40963e60\-daf0\-43fc\-bd0d\-268d153e3c86; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

#### `ESS9e03_3:sofrpr` – Original G28

„Eine Gesellschaft ist gerecht, wenn sie sich um Arme und Bedürftige kümmert, unabhängig davon, was diese der Gesellschaft zurückgeben\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Stimme stark zu | 1 |
| 2 | Stimme zu | 2 |
| 3 | Weder noch | 3 |
| 4 | Lehne ab | 4 |
| 5 | Lehne stark ab | 5 |

Fundstellen: [ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G28. [ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1e28f946\-1481\-4f53\-bbc9\-e084e6a382e0; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

#### `ESS9e03_3:sofrprv` – Original G29

„Eine Gesellschaft ist gerecht, wenn Menschen aus Familien mit hoher gesellschaftlicher Stellung Privilegien in ihrem Leben genießen\.“

| Dateicode | Deutsches Original-Kategorielabel | Gedruckter Formcode |
| --- | --- | --- |
| 1 | Stimme stark zu | 1 |
| 2 | Stimme zu | 2 |
| 3 | Weder noch | 3 |
| 4 | Lehne ab | 4 |
| 5 | Lehne stark ab | 5 |

Fundstellen: [ess9\-de\-questionnaire](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf#page=97): physische PDF\-Seite\(n\) 97; originalQuestionId=G29. [ess9\-original\-codelists\-direct](https://api.nsd.no/graphql): API\-Metadaten; sourceFieldId=1b92f5da\-3d31\-468c\-a2be\-7d2bb0f37ad2; sourceFieldMetadataVersion=3; dataFileMetadataId=b2b0bf39\-176b\-4eca\-8d26\-3c05ea83d2cb; dataFileMetadataVersion=280.

### Gruppen in Originalreihenfolge

#### CDU/CSU – Dateicode 1

Gruppen-ID: `ESS9e03_3:second_vote:1`. API-Label: „Christian Democratic Union/Christian Social Union \(CDU/CSU\)“. Deutsches Formlabel: CDU/CSU. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Gültiger Frage-Nenner, ungewichtet: 556; Gesamtbasis dieser Frage: 558; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 3,130273 % |
| 2 | Stimme zu | 28,906902 % |
| 3 | Weder noch | 24,413301 % |
| 4 | Lehne ab | 33,000986 % |
| 5 | Lehne stark ab | 10,548538 % |

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Gültiger Frage-Nenner, ungewichtet: 551; Gesamtbasis dieser Frage: 558; Missing: 7; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 0,820811 % |
| 2 | Stimme zu | 15,198565 % |
| 3 | Weder noch | 23,157532 % |
| 4 | Lehne ab | 47,634354 % |
| 5 | Lehne stark ab | 13,188738 % |

#### SPD – Dateicode 2

Gruppen-ID: `ESS9e03_3:second_vote:2`. API-Label: „Social Democratic Party \(SPD\)“. Deutsches Formlabel: SPD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Gültiger Frage-Nenner, ungewichtet: 353; Gesamtbasis dieser Frage: 355; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 12,327116 % |
| 2 | Stimme zu | 33,006748 % |
| 3 | Weder noch | 23,238986 % |
| 4 | Lehne ab | 26,422454 % |
| 5 | Lehne stark ab | 5,004697 % |

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Gültiger Frage-Nenner, ungewichtet: 354; Gesamtbasis dieser Frage: 355; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 1,617285 % |
| 2 | Stimme zu | 11,618541 % |
| 3 | Weder noch | 15,782116 % |
| 4 | Lehne ab | 51,439479 % |
| 5 | Lehne stark ab | 19,542579 % |

#### Die Linke – Dateicode 3

Gruppen-ID: `ESS9e03_3:second_vote:3`. API-Label: „The Left \(Die Linke\)“. Deutsches Formlabel: Die Linke. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Gültiger Frage-Nenner, ungewichtet: 125; Gesamtbasis dieser Frage: 125; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 14,102151 % |
| 2 | Stimme zu | 39,537237 % |
| 3 | Weder noch | 17,733450 % |
| 4 | Lehne ab | 23,232819 % |
| 5 | Lehne stark ab | 5,394343 % |

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### Bündnis 90/Die Grünen – Dateicode 4

Gruppen-ID: `ESS9e03_3:second_vote:4`. API-Label: „Alliance 90/The Greens \(Bündnis 90/Die Grünen\)“. Deutsches Formlabel: Bündnis 90/Die Grünen. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Gültiger Frage-Nenner, ungewichtet: 287; Gesamtbasis dieser Frage: 289; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 8,811011 % |
| 2 | Stimme zu | 33,404430 % |
| 3 | Weder noch | 22,798102 % |
| 4 | Lehne ab | 31,777640 % |
| 5 | Lehne stark ab | 3,208816 % |

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### FDP – Dateicode 5

Gruppen-ID: `ESS9e03_3:second_vote:5`. API-Label: „Free Democratic Party \(FDP\) “. Deutsches Formlabel: FDP. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Gültiger Frage-Nenner, ungewichtet: 147; Gesamtbasis dieser Frage: 147; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 3,904230 % |
| 2 | Stimme zu | 22,910865 % |
| 3 | Weder noch | 23,452791 % |
| 4 | Lehne ab | 38,822023 % |
| 5 | Lehne stark ab | 10,910091 % |

Frage `ESS9e03_3:sofrwrk`:

Gültiger Frage-Nenner, ungewichtet: 147; Gesamtbasis dieser Frage: 147; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 32,276672 % |
| 2 | Stimme zu | 58,049883 % |
| 3 | Weder noch | 5,743535 % |
| 4 | Lehne ab | 3,929909 % |
| 5 | Lehne stark ab | 0,000000 % |

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Gültiger Frage-Nenner, ungewichtet: 146; Gesamtbasis dieser Frage: 147; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 0,000000 % |
| 2 | Stimme zu | 7,672086 % |
| 3 | Weder noch | 26,318566 % |
| 4 | Lehne ab | 51,799418 % |
| 5 | Lehne stark ab | 14,209930 % |

#### AfD – Dateicode 6

Gruppen-ID: `ESS9e03_3:second_vote:6`. API-Label: „Alternative for Germany \(AFD\)“. Deutsches Formlabel: AfD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Gültiger Frage-Nenner, ungewichtet: 109; Gesamtbasis dieser Frage: 111; Missing: 2; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 10,069910 % |
| 2 | Stimme zu | 31,596888 % |
| 3 | Weder noch | 22,770488 % |
| 4 | Lehne ab | 28,564364 % |
| 5 | Lehne stark ab | 6,998350 % |

Frage `ESS9e03_3:sofrwrk`:

Gültiger Frage-Nenner, ungewichtet: 111; Gesamtbasis dieser Frage: 111; Missing: 0; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 32,429933 % |
| 2 | Stimme zu | 56,333168 % |
| 3 | Weder noch | 11,236898 % |
| 4 | Lehne ab | 0,000000 % |
| 5 | Lehne stark ab | 0,000000 % |

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Gültiger Frage-Nenner, ungewichtet: 110; Gesamtbasis dieser Frage: 111; Missing: 1; nicht gestellt: 0. Kategorieanteile: `pspwght`; Unsicherheit: `null`.

| Original-Dateicode | Deutsches Original-Kategorielabel | Gewichteter Anteil |
| --- | --- | --- |
| 1 | Stimme stark zu | 0,000000 % |
| 2 | Stimme zu | 12,995069 % |
| 3 | Weder noch | 16,204205 % |
| 4 | Lehne ab | 46,521136 % |
| 5 | Lehne stark ab | 24,279590 % |

#### Piratenpartei – Dateicode 7

Gruppen-ID: `ESS9e03_3:second_vote:7`. API-Label: „Pirate Party \(Piratenpartei\)“. Deutsches Formlabel: Piratenpartei. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### NPD – Dateicode 8

Gruppen-ID: `ESS9e03_3:second_vote:8`. API-Label: „National Democratic Party \(NPD\)“. Deutsches Formlabel: NPD. Deutsches Appendix-Label: nicht gebunden.

Frage `ESS9e03_3:sofrdst`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

#### Other – Dateicode 9

Gruppen-ID: `ESS9e03_3:second_vote:9`. API-Label: „Other“. Deutsches Formlabel: nicht gebunden. Deutsches Appendix-Label: nicht gebunden.

Other ist die unbenannte, heterogene Originalkategorie; keine konkrete Partei und keine einheitliche politische Gruppe.

Frage `ESS9e03_3:sofrdst`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrwrk`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrpr`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

Frage `ESS9e03_3:sofrprv`:

Verteilung nach fester Basis-/Zellenregel zurückgehalten (`withheld_base_or_cell_count`); keine veröffentlichte Basis oder Anteile.

## Öffentliche Reproduktion

`PYTHONDONTWRITEBYTECODE=1 python scripts/build-policy-group-report-v21.py build` erzeugt ausschließlich diesen öffentlichen Bericht. `--check` vergleicht seine Bytes; `--help` liest keine Berichtseingaben. Feste lokale Pfade und Hashes binden drei öffentliche Exporte, Verträge, Katalog, Rootentscheidung, beide tatsächlichen Bericht-/Entscheidbytes und alle importierten Bibliotheken. Es werden keine Rohdaten oder privaten Aggregate nachgeladen. Diese Reproduktion prüft öffentliche Bytes und Formatierung, nicht die ursprüngliche Rohrechnung.

| Fester öffentlicher Input | SHA256 der ganzen Datei |
| --- | --- |
| Rootentscheidung | `544f31f83cac1e258ed13559c04373430a5ac0d792c4380421a32bb623ef42bc` |
| Studienvertrag v2 | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| Gruppenvertrag v2.1 | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| Originalfragenkatalog | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `data/reference-groups-v21/ESS5e03_6.json` | `343d06f921f5a943e742f304255726302b71162fb55d8c73b73d11f2f184b19a` |
| `data/reference-groups-v21/ESS8e02_3.json` | `fda4e3dab0546ba25ebb2c265d0d930830615697b023fce2075e41c6a562ff3a` |
| `data/reference-groups-v21/ESS9e03_3.json` | `a1e7f8b116da9d055ffffb2dc5eb2af04e43524962433a9b032f09cbd8b5d093` |

Die weiteren festen Bericht-/Entscheid- und Bibliothekspins stehen vollständig im [Reproduktionsskript](../../scripts/build-policy-group-report-v21.py). Von Metadaten genannte Roh-/Privatpfade sind keine Lesepfade dieses Schritts.
