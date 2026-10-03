# Politikprofil v2.2: neue Fragen und Stichprobenunsicherheit

Erzeugt von `scripts/build-v22-report.py` aus den geprüften Exporten unter `data/reference-v2.2/`. Alle Zahlen stammen aus diesen Dateien. Plan: [Analyseplan v2.2](../../docs/analyseplan-v2.2.md), festgeschrieben mit dem Tag `analyseplan-v2.2` (Commit `b6af9a472c71ade865543cf75100c44a164ee12d`).

Die Werte beschreiben historische Befragte in Deutschland zur jeweiligen Feldzeit. Sie sind keine aktuelle Bevölkerungsnorm, keine Parteipositionen und keine Bewertung einer Antwort. Das Projekt ist weder validiert noch wissenschaftlich geprüft und kann keine Neutralität garantieren.

## Eingaben und Prüfungen

- Privater Lauf: SHA-256 `0ebe86b22cb3795ea232c9f0e645e6893d7355d47c842b7f8f10cb4ad6554001`, Exitcode 0.
- Abgleich mit v2: Alle 42 veröffentlichten Einzelreferenzen und 63 Gruppenpaare erneut berechnet: Abweichung höchstens 1e-12, gleiche Status.
- Unabhängige Gegenprobe der Anteile: 19 neue Fragen mit der unabhängigen Implementierung der Kontrollrechnung V1 (reports/claude/kontrollrechnung/kontrolle.py): 17 vorbereitete Referenzen, maximale Abweichung 0, Status gleich.
- Unabhängige Gegenprobe der Standardfehler: 32 Einzelreferenzen aus ESS9, ESS10-SC und ESS11 mit pipeline/policy_reference_v2.categorical_reference (Codex): maximale Abweichung der Standardfehler 0. Jeder Bereich enthält seinen Schätzwert.
- Designlauf für ESS5 und ESS8 mit den SDDF-Dateien: SHA-256 `821c8db3bdf783c3ecfeddf0462f39efc875953611d70ae9edbc7c92c951827c`, Exitcode 0.
- Unabhängige Gegenprobe der ESS5/ESS8-Bereiche: reports/claude/kontrollrechnung/sddf_gegenprobe.py mit pipeline/policy_reference_v2.categorical_reference (Codex) und dem Einlesen der Kontrollrechnung V1: ESS5 32 Referenzen und 202 Kategorien, ESS8 79 Referenzen und 407 Kategorien. Größte Abweichung der Anteile 1,1e-16, der Standardfehler 0. Ergebnis in sddf-gegenprobe.json.
- Ergebnisprüfungen vor dem Export (KI-Reviews, Codex): `reports/claude/pruefungen/E1-ergebnis-v22.md` und `reports/claude/pruefungen/E1-runde2-ergebnis-v22.md`.

Exportdateien:

- `data/reference-v2.2/ESS5e03_6.json`: `77012bf09c1994e1414104408d01c8d132c2778c1bc18ce3b4e60ddcf520bc34`
- `data/reference-v2.2/ESS8e02_3.json`: `93191d2e37f1bd4ab114c41f25bfcc5ce77d5d2ed83a74a2cfd5a8be103e6ef4`
- `data/reference-v2.2/ESS9e03_3.json`: `ef93e28ae52592a6d90499017d6c89ab35c78d7205b1573377874774d5dbe9c7`
- `data/reference-v2.2/ESS10SCe03_2.json`: `43322d3d8de64b106b7b4336215c30e9575ba58654224cfba860ab97ebfa7a2a`
- `data/reference-v2.2/ESS11e04_2.json`: `a9955368600a474ca40cf71b8d58c0cdf7eccaf6c6f73c7fe724540ab82916da`

## Stichprobenunsicherheit

Für Befragungen mit vollständigem Stichprobendesign in den Daten oder in der Designdatei (SDDF) enthält jede veröffentlichte Kategorie einen 95-%-Bereich (Taylor-Linearisierung, Logit-Intervall, Design-Freiheitsgrade). Er beschreibt nur die Unsicherheit durch die damalige Zufallsstichprobe unter vereinfachenden Annahmen, nicht den Zeitabstand, den Modus, Nichtteilnahme oder den neuen Fragekontext. Nahe 0 und 100 % kann er die tatsächliche Unsicherheit unterschätzen.

| Befragung | Stichprobendesign | Strata | PSUs | Freiheitsgrade | Einzelreferenzen mit Bereich |
| --- | --- | --- | --- | --- | --- |
| ESS5 (2010/11, persönliches Interview) | SDDF-Datei `ESS5_DE_SDDF.sav` | 2 | 168 | 166 | 7 |
| ESS8 (2016/17, persönliches Interview) | SDDF-Datei `ESS8SDDFe01_1.csv` | 20 | 180 | 160 | 20 |
| ESS9 (2018/19, persönliches Interview) | in den Daten | 89 | 178 | 89 | 4 |
| ESS10 Self-completion (2021/22, Papier und Web) | in den Daten | 89 | 179 | 90 | 22 |
| ESS11 (2023, persönliches Interview) | in den Daten | 25 | 500 | 475 | 6 |

## Neue Fragen

Anteile unter gültigen Antworten, gewichtet mit `pspwght`. Zurückgehaltene Referenzen (weniger als 100 gültige Antworten oder eine beobachtete Kategorie mit ein bis vier Fällen) erscheinen ohne Zahlen.

### B32 `prtyban` (ESS5 (2010/11, persönliches Interview))

„Politische Parteien, die die Demokratie abschaffen wollen, sollten verboten werden“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| stimme stark zu | 42,6 % | 39,8 % bis 45,4 % |
| stimme zu | 32,6 % | 29,9 % bis 35,3 % |
| weder noch | 11,2 % | 9,9 % bis 12,7 % |
| lehne ab | 10,0 % | 8,7 % bis 11,5 % |
| lehne stark ab | 3,6 % | 2,8 % bis 4,6 % |

Gültige Antworten: 2927. Basis Deutschland: 3031. Fehlende Antworten: 104. Nicht gestellt: 0.

### D4 `elgcoal` (ESS8 (2016/17, persönliches Interview))

„Wie viel des Stroms, der in Deutschland verbraucht wird, sollte aus Kohle erzeugt werden?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Eine sehr große Menge | 0,9 % | 0,5 % bis 1,5 % |
| Eine große Menge | 4,2 % | 3,3 % bis 5,3 % |
| Eine mittelgroße Menge | 16,3 % | 14,9 % bis 17,9 % |
| Eine kleine Menge | 50,6 % | 48,2 % bis 53,0 % |
| Überhaupt nichts | 27,9 % | 25,7 % bis 30,1 % |
| Ich habe noch nie etwas von dieser Energiequelle gehört | 0,2 % | 0,1 % bis 0,4 % |

Gültige Antworten: 2817. Basis Deutschland: 2852. Fehlende Antworten: 35. Nicht gestellt: 0.

### D5 `elgngas` (ESS8 (2016/17, persönliches Interview))

„Und wie viel aus Erdgas?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Eine sehr große Menge | 1,9 % | 1,2 % bis 2,8 % |
| Eine große Menge | 16,2 % | 14,6 % bis 17,9 % |
| Eine mittelgroße Menge | 41,5 % | 39,4 % bis 43,6 % |
| Eine kleine Menge | 33,7 % | 31,7 % bis 35,7 % |
| Überhaupt nichts | 6,8 % | 5,8 % bis 7,9 % |
| Ich habe noch nie etwas von dieser Energiequelle gehört | 0,0 % | – |

Gültige Antworten: 2802. Basis Deutschland: 2852. Fehlende Antworten: 50. Nicht gestellt: 0.

### D6 `elghydr` (ESS8 (2016/17, persönliches Interview))

„Und wie viel aus Wasserkraft, also aus Flüssen, Stauseen oder dem Meer?“

Keine Zahlen: Status `withheld_base_or_cell_count`.

### D7 `elgnuc` (ESS8 (2016/17, persönliches Interview))

„Wie viel des Stroms, der in Deutschland verbraucht wird, sollte aus Atomkraft bzw. Kernkraft erzeugt werden?“

Keine Zahlen: Status `withheld_base_or_cell_count`.

### D8 `elgsun` (ESS8 (2016/17, persönliches Interview))

„Und wie viel aus Sonnenenergie?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Eine sehr große Menge | 47,2 % | 44,9 % bis 49,6 % |
| Eine große Menge | 39,8 % | 37,7 % bis 41,9 % |
| Eine mittelgroße Menge | 9,8 % | 8,6 % bis 11,1 % |
| Eine kleine Menge | 2,8 % | 2,2 % bis 3,6 % |
| Überhaupt nichts | 0,5 % | 0,3 % bis 0,8 % |
| Ich habe noch nie etwas von dieser Energiequelle gehört | 0,0 % | – |

Gültige Antworten: 2832. Basis Deutschland: 2852. Fehlende Antworten: 20. Nicht gestellt: 0.

### D9 `elgwind` (ESS8 (2016/17, persönliches Interview))

„Und wie viel aus Windkraft?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Eine sehr große Menge | 36,1 % | 33,4 % bis 39,0 % |
| Eine große Menge | 39,5 % | 37,2 % bis 41,7 % |
| Eine mittelgroße Menge | 17,2 % | 15,6 % bis 18,9 % |
| Eine kleine Menge | 6,1 % | 5,1 % bis 7,3 % |
| Überhaupt nichts | 1,1 % | 0,7 % bis 1,5 % |
| Ich habe noch nie etwas von dieser Energiequelle gehört | 0,0 % | – |

Gültige Antworten: 2830. Basis Deutschland: 2852. Fehlende Antworten: 22. Nicht gestellt: 0.

### D10 `elgbio` (ESS8 (2016/17, persönliches Interview))

„Und wie viel Strom sollte aus Biomasse wie Holz, Pflanzen oder Tiermist gewonnen werden?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Eine sehr große Menge | 10,9 % | 9,6 % bis 12,3 % |
| Eine große Menge | 26,2 % | 24,2 % bis 28,2 % |
| Eine mittelgroße Menge | 28,7 % | 27,0 % bis 30,5 % |
| Eine kleine Menge | 26,3 % | 24,5 % bis 28,2 % |
| Überhaupt nichts | 6,7 % | 5,5 % bis 8,2 % |
| Ich habe noch nie etwas von dieser Energiequelle gehört | 1,1 % | 0,7 % bis 1,8 % |

Gültige Antworten: 2799. Basis Deutschland: 2852. Fehlende Antworten: 53. Nicht gestellt: 0.

### C42 `gvrfgap` (ESS8 (2016/17, persönliches Interview))

„Bei der Prüfung von Asylanträgen sollte der Staat großzügig sein.“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Stimme stark zu | 6,2 % | 5,2 % bis 7,4 % |
| Stimme zu | 20,7 % | 18,8 % bis 22,8 % |
| Weder noch | 23,2 % | 21,4 % bis 25,0 % |
| Lehne ab | 37,1 % | 34,9 % bis 39,5 % |
| Lehne stark ab | 12,7 % | 11,3 % bis 14,3 % |

Gültige Antworten: 2835. Basis Deutschland: 2852. Fehlende Antworten: 17. Nicht gestellt: 0.

### C44 `rfgbfml` (ESS8 (2016/17, persönliches Interview))

„Asylbewerber, deren Anträge bewilligt wurden, sollten das Recht haben, ihre engen Familienangehörigen nach Deutschland zu holen.“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Stimme stark zu | 8,5 % | 7,3 % bis 9,9 % |
| Stimme zu | 49,8 % | 47,4 % bis 52,2 % |
| Weder noch | 15,3 % | 13,8 % bis 17,0 % |
| Lehne ab | 20,7 % | 18,9 % bis 22,7 % |
| Lehne stark ab | 5,6 % | 4,5 % bis 6,9 % |

Gültige Antworten: 2827. Basis Deutschland: 2852. Fehlende Antworten: 25. Nicht gestellt: 0.

### E36 `basinc` (ESS8 (2016/17, persönliches Interview))

„Alles in allem, wären Sie gegen oder für ein solches Grundeinkommen in Deutschland?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Sehr dagegen | 12,2 % | 10,7 % bis 13,9 % |
| Dagegen | 41,7 % | 39,2 % bis 44,3 % |
| Dafür | 37,8 % | 35,4 % bis 40,3 % |
| Sehr dafür | 8,2 % | 7,2 % bis 9,5 % |

Gültige Antworten: 2765. Basis Deutschland: 2852. Fehlende Antworten: 87. Nicht gestellt: 0.

### E37 `eusclbf` (ESS8 (2016/17, persönliches Interview))

„Alles in allem, wären Sie gegen oder für ein solches EU-weites Sozialleistungsprogramm?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Sehr dagegen | 6,8 % | 5,8 % bis 8,1 % |
| Dagegen | 31,8 % | 29,7 % bis 34,0 % |
| Dafür | 54,7 % | 52,1 % bis 57,2 % |
| Sehr dafür | 6,7 % | 5,6 % bis 8,0 % |

Gültige Antworten: 2752. Basis Deutschland: 2852. Fehlende Antworten: 100. Nicht gestellt: 0.

### B33A `mnrgtjb` (ESS8 (2016/17, persönliches Interview))

„Wenn Arbeitsplätze knapp sind, sollten Männer eher einen Anspruch auf einen Arbeitsplatz haben als Frauen.“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Stimme stark zu | 1,6 % | 1,1 % bis 2,4 % |
| Stimme zu | 6,7 % | 5,5 % bis 8,2 % |
| Weder noch | 17,1 % | 15,5 % bis 19,0 % |
| Lehne ab | 33,7 % | 31,6 % bis 35,8 % |
| Lehne stark ab | 40,8 % | 38,3 % bis 43,4 % |

Gültige Antworten: 2841. Basis Deutschland: 2852. Fehlende Antworten: 11. Nicht gestellt: 0.

### A1 `panpriph` (ESS10 Self-completion (2021/22, Papier und Web))

„Ist es bei der Bekämpfung einer Pandemie wichtiger, die Gesundheit der Bevölkerung oder die Wirtschaft vorrangig zu berücksichtigen?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Viel wichtiger, die Gesundheit der Bevölkerung vorrangig zu berücksichtigen | 20,7 % | 19,5 % bis 21,9 % |
| 1 | 5,5 % | 5,0 % bis 6,1 % |
| 2 | 11,9 % | 11,1 % bis 12,7 % |
| 3 | 16,6 % | 15,6 % bis 17,6 % |
| 4 | 9,1 % | 8,4 % bis 10,0 % |
| 5 | 24,0 % | 22,8 % bis 25,2 % |
| 6 | 3,2 % | 2,8 % bis 3,6 % |
| 7 | 3,4 % | 3,0 % bis 3,9 % |
| 8 | 2,4 % | 2,1 % bis 2,7 % |
| 9 | 1,2 % | 1,0 % bis 1,6 % |
| Viel wichtiger, die Wirtschaft vorrangig zu berücksichtigen | 2,0 % | 1,6 % bis 2,4 % |

Gültige Antworten: 8594. Basis Deutschland: 8725. Fehlende Antworten: 131. Nicht gestellt: 0.

### A2 `panmonpb` (ESS10 Self-completion (2021/22, Papier und Web))

„Ist es bei der Bekämpfung einer Pandemie wichtiger, dass Regierungen die Bevölkerung überwachen und nachverfolgen oder die Privatsphäre des Einzelnen bewahren?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Viel wichtiger, die Bevölkerung zu überwachen und nachzuverfolgen | 8,6 % | 7,9 % bis 9,4 % |
| 1 | 3,8 % | 3,4 % bis 4,2 % |
| 2 | 8,4 % | 7,7 % bis 9,1 % |
| 3 | 10,8 % | 10,0 % bis 11,6 % |
| 4 | 6,8 % | 6,3 % bis 7,4 % |
| 5 | 19,1 % | 18,1 % bis 20,2 % |
| 6 | 5,8 % | 5,2 % bis 6,4 % |
| 7 | 8,5 % | 7,8 % bis 9,2 % |
| 8 | 8,5 % | 7,8 % bis 9,3 % |
| 9 | 3,5 % | 3,2 % bis 3,9 % |
| Viel wichtiger, die Privatsphäre des Einzelnen zu bewahren | 16,3 % | 15,2 % bis 17,4 % |

Gültige Antworten: 8588. Basis Deutschland: 8725. Fehlende Antworten: 137. Nicht gestellt: 0.

### A47 `freehms` (ESS10 Self-completion (2021/22, Papier und Web))

„Schwule und Lesben sollten ihr Leben so führen dürfen, wie sie es wollen.“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Stimme stark zu | 52,3 % | 50,6 % bis 54,1 % |
| Stimme zu | 37,0 % | 35,5 % bis 38,4 % |
| Weder noch | 7,1 % | 6,4 % bis 7,8 % |
| Lehne ab | 2,2 % | 1,9 % bis 2,7 % |
| Lehne stark ab | 1,4 % | 1,1 % bis 1,7 % |

Gültige Antworten: 8646. Basis Deutschland: 8725. Fehlende Antworten: 79. Nicht gestellt: 0.

### A49 `hmsacld` (ESS10 Self-completion (2021/22, Papier und Web))

„Schwule und lesbische Paare sollten die gleichen Rechte haben, Kinder zu adoptieren, wie Paare, die aus Mann und Frau bestehen.“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Stimme stark zu | 37,1 % | 35,6 % bis 38,6 % |
| Stimme zu | 33,6 % | 32,4 % bis 34,8 % |
| Weder noch | 13,4 % | 12,5 % bis 14,4 % |
| Lehne ab | 10,3 % | 9,6 % bis 11,1 % |
| Lehne stark ab | 5,6 % | 4,9 % bis 6,4 % |

Gültige Antworten: 8612. Basis Deutschland: 8725. Fehlende Antworten: 113. Nicht gestellt: 0.

### A51 `accalaw` (ESS10 Self-completion (2021/22, Papier und Web))

„Wie akzeptabel wäre es für Sie, wenn Deutschland eine starke Führungsperson hätte, die über dem Gesetz steht?“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Überhaupt nicht akzeptabel | 61,2 % | 59,5 % bis 62,9 % |
| 1 | 6,3 % | 5,7 % bis 6,9 % |
| 2 | 6,7 % | 6,1 % bis 7,4 % |
| 3 | 4,9 % | 4,4 % bis 5,6 % |
| 4 | 2,7 % | 2,3 % bis 3,2 % |
| 5 | 7,9 % | 7,2 % bis 8,6 % |
| 6 | 2,2 % | 1,9 % bis 2,7 % |
| 7 | 2,5 % | 2,1 % bis 3,0 % |
| 8 | 2,1 % | 1,7 % bis 2,5 % |
| 9 | 0,9 % | 0,6 % bis 1,2 % |
| Voll und ganz akzeptabel | 2,6 % | 2,2 % bis 3,1 % |

Gültige Antworten: 8457. Basis Deutschland: 8725. Fehlende Antworten: 268. Nicht gestellt: 0.

### A53 `loylead` (ESS10 Self-completion (2021/22, Papier und Web))

„Was Deutschland am meisten braucht, ist Loyalität gegenüber der politischen Führung.“

| Antwortkategorie | Anteil | 95-%-Bereich |
| --- | --- | --- |
| Stimme stark zu | 3,3 % | 2,8 % bis 3,8 % |
| Stimme zu | 31,3 % | 29,8 % bis 32,8 % |
| Weder noch | 41,4 % | 40,2 % bis 42,7 % |
| Lehne ab | 17,2 % | 16,0 % bis 18,4 % |
| Lehne stark ab | 6,8 % | 6,0 % bis 7,8 % |

Gültige Antworten: 8399. Basis Deutschland: 8725. Fehlende Antworten: 326. Nicht gestellt: 0.

## Gruppenpaare

Wählergruppen nach erinnerter Zweitstimme der jeweils letzten Bundestagswahl vor der Befragung, wie in v2.1. Keine Parteipositionen und kein Abstand zu Parteien.

| Befragung | Veröffentlichte Paare | Zurückgehaltene Paare | Paare mit Bereich |
| --- | --- | --- | --- |
| ESS5 (2010/11, persönliches Interview) | 25 | 31 | 25 |
| ESS8 (2016/17, persönliches Interview) | 59 | 139 | 59 |
| ESS9 (2018/19, persönliches Interview) | 12 | 24 | 12 |
