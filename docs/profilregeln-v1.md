# Profilregeln v1: das erklärende Antwortprofil

Stand: 3. Oktober 2026. Verfasst von Claude. Diese Regeln setzen LIFE-93 Abschnitt 2a um. Sie folgen der Empfehlung im Bericht [R4](../reports/claude/agenten/R4-profilform.md), Abschnitt 4. Umgesetzt sind sie in `web/src/app/policy-draft/profile/`. Dort stehen auch die genauen Texte. Dieses Dokument beschreibt die Regeln und begründet sie.

## Warum ein beschreibendes Profil ohne Werte

Die Fragen stammen aus fünf Befragungen mit verschiedenen Personen und Jahren. Für keine Themenrubrik belegt die Literatur einen gemeinsamen Wert für genau diesen Fragenbestand (R4 Abschnitt 2.12). Für zwei Fragenblöcke sagen die ESS-Entwickler ausdrücklich, dass sie keinen gemeinsamen Faktor annehmen: ESS8 E33–E35 und ESS11 E19–E22 (R4 2.4, 2.11). Achsen und Karten in Wahlhilfen haben bekannte Probleme, wenn ihre Struktur nicht geprüft ist (R4 3.1). Ein formativer Index bräuchte einen vollständigen Konstruktrahmen und begründete Gewichte (R4 3.2). Beides fehlt.

Das Profil beschreibt deshalb, was die Antworten wörtlich sagen. Es ordnet sie nach Bereichen, beschreibt Muster innerhalb gleich formatierter Originalblöcke und stellt ausgewählte Fragen verschiedener Blöcke nebeneinander. Es misst keine Eigenschaft der Person.

## Stufe 1: Einzelaussage

Jede beantwortete Frage erhält genau eine Aussage. Sie hängt nur vom Antwortcode und einer festen Texttabelle ab. Dieselbe Eingabe ergibt denselben Text, unabhängig von der Reihenfolge der Antworten.

| Antworttyp                                         | Form der Aussage                                                                                                            |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Zustimmung, fünf Stufen                            | „Zustimmung zur Aussage ‚…‘“, „Ablehnung der Aussage ‚…‘“ oder „Weder Zustimmung noch Ablehnung …“, mit gewählter Kategorie |
| Befürwortung einer Maßnahme, vier oder fünf Stufen | „Dafür, dass …“ oder „Für …“, „Dagegen, dass …“ oder „Gegen …“, bei fünf Stufen auch „Weder dafür noch dagegen …“           |
| Skala 0 bis 10 mit einem Pol                       | Gegenstand, gewählte Zahl und beide Endbeschriftungen. Keine Stufen wie „eher hoch“                                         |
| Skala 0 bis 10 zwischen zwei Aussagen              | Zahl und „näher an“ der Aussage auf dieser Seite. Bei 5 „gleicher Abstand zu beiden Endpunkten“                             |
| Geordnete oder nominale Kategorien                 | Gegenstand und gewählte Kategorie im Originalwortlaut                                                                       |

Die Richtung einer Antwort kommt aus einer ausdrücklichen Tabelle je Frage, nicht aus der Codezahl. Code 1 heißt bei `bnlwinc` „Sehr dagegen“ und bei `inctxff` „Sehr dafür“ (R4 Nebenbefund 3). Jede Aussage trägt ein festes Kontextmerkmal aus dem Wortlaut der Frage, etwa „Wichtigkeit für die Demokratie im Allgemeinen“ oder „auch wenn das deutlich höhere Steuern für alle bedeuten würde“.

## Stufe 2: Blockmuster

Nur innerhalb von Originalblöcken mit derselben Einleitung und Antwortliste und nur ab zwei beantworteten Fragen:

| Block                               | Fragen         | Muster                                                             |
| ----------------------------------- | -------------- | ------------------------------------------------------------------ |
| Gerechtigkeitsprinzipien            | ESS9 G26–G29   | Aufzählung nach Zustimmung, Mitte und Ablehnung                    |
| Staatliche Verantwortung            | ESS8 E6–E8     | gleiche oder unterschiedliche Werte, höchster und niedrigster Wert |
| Merkmale der Demokratie             | ESS10 B1–B11   | wie oben                                                           |
| Pflichten gegenüber der Polizei     | ESS5 D18, D20  | wie oben                                                           |
| Gesetze und Gerichtsurteile         | ESS5 D34–D36   | Aufzählung nach Richtung, Hinweis auf Regel und Ausnahmefall       |
| Maßnahmen gegen den Klimawandel     | ESS8 D30–D32   | Aufzählung nach Richtung                                           |
| Strom aus sieben Energiequellen     | ESS8 D4–D10    | Aufzählung der Energiequellen je gewählter Menge                   |
| Zuwanderung nach Herkunftsgruppen   | ESS10 A54–A56  | gleiche Antwort oder Vergleich je Gruppenpaar                      |
| Asyl                                | ESS8 C42, C44  | Aufzählung nach Richtung                                           |
| Mittel der Gleichstellungspolitik   | ESS11 E19–E22  | Aufzählung nach Richtung, Hinweis zu Mittel und Ziel               |
| Rechte gleichgeschlechtlicher Paare | ESS10 A47, A49 | Aufzählung nach Richtung                                           |

ESS8 E33–E35 erhalten kein Blockmuster, weil jede Frage eine andere Bedingung enthält (R4 2.4). D33 gehört nicht zum Block D34–D36 (R4 Nebenbefund 2). Jeder Block nennt die Grundlage der Zusammenstellung mit Fundstelle.

## Stufe 3: Querbezüge

Querbezüge stellen Fragen aus verschiedenen Blöcken oder Studien nebeneinander. Sie erscheinen ab zwei beantworteten Fragen. Ein fester Kontextsatz erklärt, worin sich die Fragen unterscheiden. Sie rechnen nichts und bewerten keine Kombination. Jeder Querbezug trägt den Hinweis, dass er eine Zusammenstellung des Projekts ist und keine geprüfte gemeinsame Struktur.

| Querbezug                         | Fragen                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------ |
| Einkommensunterschiede            | `sofrdst` (ESS9), `gincdif` (ESS11), `grdfinc` (ESS10)                         |
| Absicherung bei Armut und Bedarf  | `sofrpr` (ESS9), `gvctzpv` (ESS10), `gvslvol`, `gvslvue`, `basinc` (ESS8)      |
| Gewicht der Bevölkerungsmehrheit  | `votedir`, `viepol`, `wpestop`, `scchpldm` (ESS10)                             |
| Recht, Gerichte und Polizei       | `cttresa` (ESS10), `dbctvrd`, `lwstrob`, `rgbrklw`, `bplcdc`, `dpcstrb` (ESS5) |
| Politische Führung und Recht      | `accalaw`, `loylead`, `cttresa` (ESS10), `prtyban` (ESS5)                      |
| Erwerbsarbeit und Kinderbetreuung | `gvcldcr`, `wrkprbf` (ESS8), `eqparlv` (ESS11)                                 |
| Europäische Union                 | `vteurmmb`, `keydec` (ESS10), `euftf` (ESS11), `eusclbf` (ESS8)                |

Nicht vorgesehen sind Querbezüge zwischen Zuwanderung und Minderheitenrechten oder zwischen Gleichheitsprinzip und Gleichstellungsmitteln. Die Gegenstände sind verschieden, und die Verbindung legte eine Deutung nahe, die keine Frage stellt (R4 4.2).

## Fehlende Antworten, Mitte und Nichtpositionen

- Übersprungene Fragen erzeugen keine Aussage und keinen Vergleich. Sie stehen in einer Liste ohne inhaltliche Antwort.
- Die mittlere Kategorie wird wörtlich wiedergegeben. Ein Satz erklärt einmal, dass sie Unentschiedenheit, eine fehlende Meinung oder die Zurückweisung einer Annahme ausdrücken kann (R4 4.4). Sie heißt nie „neutral“ oder „gemäßigt“ und zählt in Blockmustern als eigene Gruppe.
- Antworten wie „Würde nicht wählen“ oder „Nicht stimmberechtigt“ bei der EU-Abstimmung sind eigene Antworten und liegen nicht zwischen Verbleib und Austritt.
- Bei den Energiequellen bietet die Website die im Interview nicht vorgelesene Antwort „noch nie von dieser Energiequelle gehört“ nicht an.

## Historische Vergleiche

- Nur je Frage. Angezeigt wird die vollständige Verteilung der Originalkategorien mit markierter eigener Kategorie und der Anteil derselben Kategorie.
- Feste Begleitangaben: Studie, Ausgabe, Feldzeit, Population, Modus, Nenner nur gültige Antworten.
- Wo berechnet, ein 95-%-Bereich je Anteil nach [Analyseplan v2.2](analyseplan-v2.2.md), Abschnitt 4, mit Erklärung seiner Bedeutung und Grenzen.
- Keine Mengenwörter ohne Zahl, kein „typisch“ oder „ungewöhnlich“, kein Rang oder Perzentil, kein Vergleich über mehrere Fragen.

## Bereiche

Jeder Bereich nennt die Zahl beantworteter Fragen, „Erfasst“ und „Nicht erfasst“ aus der [Themenabdeckung v2.2](abdeckung-v2.2.md). Die Zahl ist eine Abdeckungsangabe, kein Wert.

## Nicht zulässig

Gesamtwerte, Themenwerte, Mittelwerte oder Summen über Fragen. Achsen, Karten, Netzdiagramme, Positionsbalken, Perzentile und Ränge. Lagerbezeichnungen und Ideologiebegriffe für Personen oder Antwortmuster, etwa links, rechts, liberal, konservativ, autoritär oder populistisch. Zuschreibungen von Motiven, Gefühlen oder Persönlichkeit. Die Wörter „Widerspruch“, „inkonsistent“, „neutral“ oder „gemäßigt“ als Beschreibung der Person. Ersatzwerte für fehlende Antworten. Verrechnung über Studien hinweg. Persönliche Messunsicherheit (R4 4.8).

## Prüfung

Die technischen Prüffälle T01–T29 aus R4 Abschnitt 5 sind als synthetische Tests in `profile-engine.spec.ts` umgesetzt, dazu Tests für die Blöcke und Querbezüge aus Plan v2.2. T30 betrifft die Anzeige historischer Vergleiche und ist im Komponententest zu `cttresa` in `policy-draft.spec.ts` abgedeckt. Ein weiterer Test prüft, dass jede angebotene Antwortkategorie jeder Frage einen Satz ohne verbotene Bezeichnungen und ohne direkte Anrede ergibt. Synthetische Antwortkombinationen sind keine empirischen Personen. Ob Menschen die Texte so verstehen wie beabsichtigt, kann nur der Verständnistest zeigen.
