# Unabhängige Item-Erstbewertung 2

Paket `ITEM-FIRST-001/v1`, 2026-10-03. Ich habe alle 296 gelieferten Identitäten anhand der gebundenen Originalsicht und der öffentlichen ESS11-Fragebogendokumentation beurteilt. Die Initial-CSV enthält 88 JA, 182 NEIN und 26 UNKLAR. Das sind Urteilszahlen über Dokumentenidentitäten, keine Häufigkeiten politischer Antworten. JA bedeutet ausschließlich inhaltliche Grundeignung nach dem gebundenen Vertrag. Keine endgültige Itemaufnahme, Dimension, Messlogik oder wissenschaftliche Abnahme folgt daraus.

## Unabhängigkeit und Auftrag

Diese Erstbewertung entstand in einem eigenen Codex-Unteragenten mit frischem Auftragskontext. Ich habe keine Autorenauswahl, Autorenpolung, vorgeschlagenen Konstruktnamen, Verteidigung, Pläne oder fremden Erstberichte gelesen. Die bestehende CSV und die drei Ergänzungsdateien wurden nur als Bytefolgen gegen ihre Paketpins gehasht. Für die inhaltliche Arbeit habe ich ausschließlich die ausgewählten Original-/Provenienzfelder aus `originalitems.json` genutzt. Eine Git-Statusabfrage zeigte Dateinamen im Autorenordner, keine Dateiinhalte.

Ich gehöre derselben Codex-Modellfamilie wie die andere Erstbewertung und der Koordinator. Getrennte Kontexte verhindern Einsicht in fremde Urteile, beweisen aber keine unabhängigen Denkfehler, Neutralität oder Richtigkeit. Ich habe keine weitere Modellfamilie und keinen Subagenten beauftragt. Für die Berichtssprache wurde die lokale `unslop`-Skill gelesen.

Die Bewertung richtet sich nach `docs/itemerstbewertung-vertrag.md`, SHA256 `ee2460223083cc910515b3c7fac890fff9433c7b3d414fb8786f9ed3d021f55d`. Die Detailurteile stehen in [ITEM-FIRST-001-methods.csv](ITEM-FIRST-001-methods.csv). Jede der 296 Zeilen enthält Eignung, Antworttyp, Geltung, Originalstatus, Fundstelle, Begründung, Ordnungsrichtung und einen eigenen sachlichen höheren Polinhalt. Für nicht geordnete Originalcodes steht kein erfundener politischer Pol darin.

## Quellenzugriff und Originalstatus

Die gebundenen lokalen Original-PDFs tragen dieselben Hashes wie das Manifest. Der Manifesthash ist `6d6bad17cd27ee92dc402cf5e7ef67df4de582a50a3dcdbc3aacb76c4d883501`. Alle sechs gebundenen Dateien und vier Quellenpins stimmten vor und nach der Erstbewertung. Die vollständigen Prüfprotokolle liegen in `outputs/loop/item-first-methods/pins-before.json` und `pins-after.json`.

Ich habe sämtliche Originalformulierungen der 296 Identitäten modulweise gelesen. Den Fragebogen-Textlayer habe ich von PDF-Seite 2 bis 100 in begrenzten Batches gelesen, einschließlich Antwortblöcken, gemeinsamer Vorspänne und Routingangaben. Die frische lokale `pdftotext -layout`-Extraktion entspricht bytegenau dem gepinnten Fragebogen-Textlayer, SHA256 `c466be8a95f486c4e5913d769942477fa618575531d6e6a27e42c69e342af224`. Die Quellen bleiben die deutsche ESS11-Dokumentation, keine ESS-Antwortdaten. [Originalfragebogen](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf).

Die für gesellschaftliche/wertebezogene Urteile tragenden Listenheftskalen wurden gelesen. Zusätzlich habe ich Fragebogen-PDF-Seite 49, Seite 89 und Listenheft-PDF-Seite 97 als Bild geprüft. Die erste zeigt die drei nominalen Gerechtigkeitskategorien E12–E14, die zweite die H2-Portraits mit der Ähnlichkeitsskala, die dritte die im Textlayer schlecht erkennbare Liste 92. Es gab keine vollständige Bildprüfung aller Seiten. [Originallistenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf).

Einige Listenheftseiten enthalten überlagerte alte und neue Textobjekte. Eine automatisch eindeutige Textausgabe ist dort keine verlässliche zellenweise Abnahme. Die komplexen Ausbildungs-/Berufskarten 82a–86a wurden nicht vollständig als eigene Karten abgenommen; ihre Fragebogenblöcke wurden gelesen und tragen die NEIN-Urteile. Bei F41 bleibt die Prüfung der genauen Eurogrenzen offen. Die geordnete Abfolge der Einkommensklassen trägt allein den berichteten Größeninhalt, keine hier geprüften Grenzbeträge. Die CSV benennt diese Quellenprüfung getrennt. Fehlende finale Variablenzuordnungen der Originalsicht wurden nicht ergänzt.

Der gebundene Codebook-PDF wurde lokal in Text extrahiert. Ich habe nur Metadaten und das Vorkommen einschlägiger Variablenlabels abgefragt, unter anderem `testji9`; keine Antwortverteilungen oder Personenwerte. Dieser begrenzte Abgleich ersetzt keine zeilenweise Adapter-/Variablenabnahme. [ESS11 Codebook 4.1](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf).

Der zusätzliche automatisierte Abgleich findet bei 242 von 296 Identitäten den whitespace-normalisierten Anfang des Originaltexts in den gebundenen Seiten. Bei 54 Tabellenidentitäten unterbrechen Skalenwerte und Zellaufteilungen diesen einfachen 35-Zeichen-Abgleich. Das ist ein technischer Textabgleich, keine inhaltliche Bestätigung und kein Beweis eines Quellenfehlers. Die manuell gelesenen Originalblöcke tragen die Urteile. Die vollständigen Ergebnisse liegen in `automatic-original-crosscheck.json`, die Seitengeometrie in `source-geometry.json`, die Identitätszuordnung in `original-index.json` und `showcard-index.json`.

Zwei zunächst zu große Toolausgaben wurden gekürzt. Die betroffenen Originalpassagen B18 sowie Fragebogenseiten 64–65 wurden gezielt ungekürzt erneut gelesen. Die gekürzte Zusatzlektüre einiger komplexer F-Listenheftkarten wurde nicht nachträglich als vollständige Kartenabnahme ausgegeben. Daraus entsteht keine tragende Quellenlücke für die NEIN-Begründung dieser Lebensangaben; ihre Originalfrageblöcke liegen vor.

European Social Survey ERIC ist der Herausgeber. Die Dokumentation ist laut gebundenem Quellenhinweis CC BY-SA 4.0; die Originalquelle und Lizenz wurden beibehalten. Diese Auswertung strukturiert und beurteilt öffentliche Frageformulierungen; sie ist keine ESS-Billigung. Es gab keinen Live-Neudownload und keine Behauptung, die gepinnte Ausgabe sei die heute neueste Ausgabe. [Lizenz CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Anwendung derselben Grundregel

Eigenes Handeln, Fähigkeiten, Gesundheit, Haushalts- und Berufsbiografie bleiben ausgeschlossen. Deshalb werden beispielsweise B3/B5, E4/E5, alle D-/F-Gegenstände und K4 nicht allein wegen eines gesellschaftlich relevanten Themas zu politischen Einstellungen.

Generalisierte soziale Wahrnehmung ist kein automatischer Wissensausschluss. A4–A6, B6–B9/B11/B12, B28/B30–B32 und E12–E14/E23–E26 tragen allgemeine evaluative Vorstellungen über Menschen, öffentliche Institutionen, gesellschaftliche Zustände oder Geschlechterverhältnisse. Diese JA-Urteile belegen keine Kausalrichtigkeit und keine politische Skala. E12–E14 bleiben trotz JA nominal. C30 wird als Tatsachen-/Ursachengegenstand ausgeschlossen, weil die Frage ausdrücklich nach der tatsächlichen Ursache des Klimawandels fragt. Bei subjektiven Klimaeffekt- und Handlungsprognosen C34–C42/I1–I9 bleibt dagegen die Grenze zwischen gesellschaftlicher Überzeugung und Prognose/Wirklichkeitsbehauptung offen. Keine Prüfung tatsächlicher Häufigkeiten wurde vorgenommen.

B29 nennt die amtierende Bundesregierung und erhält NEIN. B10 nennt Parteien und erhält NEIN. B25 übernimmt die konkrete Partei aus B23/B24 und bleibt ebenfalls NEIN. B9 bezeichnet dagegen die allgemeine Personengruppe Politikerinnen und Politiker; weder eine Partei noch ein Kabinett ist im Originalgegenstand benannt. B39 ist eine allgemeine normative Loyalitätsforderung an politische Führung und wird nicht zur Zustimmung zum aktuellen Kabinett umgedeutet. B2 bleibt UNKLAR, weil der Originalgegenstand Systemmitsprache, Menschen wie die befragte Person und das Regierungshandeln verbindet. B4 nennt die gesellschaftliche Offenheit des politischen Systems ohne diesen Regierungsbezug und erhält JA.

C43 erhält NEIN wegen der ausdrücklich hypothetischen Referendumswahlabsicht. Eine gewünschte EU-Mitgliedschaft lässt sich im Original zwar als politische Sachposition erkennen, der gebundene Vertrag schließt Wahlangaben jedoch aus. Die Referendumsantwort darf außerdem wegen der weiteren Nichtwahl-/Berechtigungskategorien nicht ohne gesonderte Regel in eine numerische Zweipolskala überführt werden.

C9/C10/C15, E2/E3 und E8M/E8W bleiben echte inhaltliche Grenzfälle. Verbundenheit, Religiosität, Vorlieben und Identitätswichtigkeit können persönliche Orientierungen oder beschreibende Identitäts-/Persönlichkeitsmerkmale sein. Der kurze Originalwortlaut entscheidet diese Grenze nicht. Diese Fälle wurden weder pauschal ausgeschlossen noch zugunsten einer gewünschten Achse zugelassen.

Jedes H-Portrait erhält JA als persönliche Wert-/Wunschorientierung. Der sachliche höhere Pol ist ausschließlich stärkere Ähnlichkeit mit der beschriebenen Person; dafür fällt der Originalcode von 6 nach 1. Keine relative Wichtigkeit gegenüber anderen Werten, keine gegenteilige Ideologie und keine normierte Achse wurde daraus abgeleitet. Die Blockköpfe H1/H2 sind Anweisungen ohne eigene Einzelantwort und erhalten NEIN.

## Erhebliche Befunde für die Weiterarbeit

| ID | Betroffene Identitäten und Originalstellen | Befund und Folge |
| --- | --- | --- |
| IM-R01 | B24/B25, Q9–10 | Partei ist ein geerbter semantischer Bezug. „Welcher?“ und „dieser Partei“ lassen sich nicht unabhängig von B23/B24 bewerten. Eine Weiterverarbeitung als parteifreie Wertorientierung wäre sachlich falsch. |
| IM-R02 | E12–E14, Q49; Listen 58/59 auf S59/60 | Originalcodes 1/2/3 stehen für Benachteiligung von Frauen, von Männern und Gleichbehandlung. Die Zahlen tragen keine lineare Haltungsskala. JA ist keine Freigabe einer 0–1-Ordnung. |
| IM-R03 | C34–C42, Q27–30; I1–I9, Q93–96; Listen 30–32/90–92 | Derselbe Inhalt erhält drei Antwortskalen; 1–5 läuft gegenläufig zu 0–4/0–10. C33 teilt Zufallsgruppen zu, und Modul I übernimmt die Gruppe. Ein Zusammenwerfen als unabhängige Items oder identische Rohpolung wäre falsch. Die Grundeignung dieser Prognose-/Wirksamkeitsgegenstände bleibt UNKLAR. |
| IM-R04 | C30, C43, D18, F29, Q26/31/38/67 | 55, 33/44/55/65 und 555 können substantielle Sonderkategorien sein, keine hohen Skalenwerte und keine pauschalen Missingcodes. Besonders D18=55 bedeutet geringe Betreuungszeit; der gesamte Originalcode ist daher nicht monoton. |
| IM-R05 | H1.A–U/H2.A–U, Q85–92; Liste 89, S94 | 42 Inventaridentitäten enthalten 21 parallele Portraitinhalte. Die Antwort misst Ähnlichkeit, keine bereits geprüfte relative Wertpriorität. H1/H2-Blockköpfe sind keine Zusatzitems. Das Routing ist ausdrücklich E1=1 beziehungsweise E1=2; für E1=3 ist hier kein H-Alternativweg belegt. |
| IM-R06 | C44/R/V1, Q2/31–32/96–100 | C44 und R sind in dieser Ausgabe nur im Inhaltsverzeichnis angekündigt. V1 ist tatsächlich auf Q98 vorhanden, fehlt aber im gelieferten 296-Zeilenbestand. Inventarvollständigkeit und inhaltliche Grundeignung sind getrennt zu korrigieren; kein Wortlaut für C44/R darf ergänzt werden. |
| IM-R07 | E1, Q43; Liste 50, S51 | Das Listenheft zeigt „Möchte nicht antworten“, der Fragebogen zeigt dort keinen gedruckten eigenen Code. Die Codierung dieser Nichtantwortdarstellung bleibt offen. Das NEIN-Urteil zur Geschlechtsbezeichnung ändert sich dadurch nicht. |
| IM-R08 | B2; C9/C10/C15; E2/E3/E8M/E8W; C-/I-Klimavarianten | Die oben begründeten Grenzfälle tragen keine eindeutige Grundregelentscheidung. Ein Koordinator muss die konkreten Originalgegenstände klären oder die Unsicherheit auf den betroffenen Kandidaten begrenzen. Ein Mehrheitsurteil oder eine gewünschte Dimensionszahl löst diese Grenze nicht. |

Die Befunde benennen konkrete Quellen-, Gegenstands- und Ordnungsprobleme. Sie sind keine Stilwünsche und keine Behauptung, dass ein nicht gelesenes Autorenmodell den jeweiligen Fehler bereits macht. Sie blockieren jeweils die beschriebene fehlerhafte Weiterverarbeitung, nicht pauschal sämtliche spätere Forschung.

## Zusätzliche Inventargrenzen

C44 besitzt keinen belegten Originalblock in diesem gepinnten Fragebogen. Q31 enthält C43 und routet ausdrücklich nach Modul D; Q32 beginnt mit D1. R besitzt ebenfalls keinen belegten Originalblock: Q96 enthält I9, Q97 K1–K4 und Q98–100 Interviewverwaltung. Beide stehen außerhalb der 296 bewerteten Identitäten und wurden nicht mit erfundenem Inhalt ergänzt.

V1 steht auf Q98 vor J1. Es erfasst persönlich in der Wohnung/im Haus, persönlich außerhalb oder per Video durchgeführtes Interview. Das ist eine nominale Verwaltungsangabe, Grundeignung NEIN, Ordnungsrichtung KEINE. Die Dokumentation steht separat in `outputs/loop/item-first-methods/inventory-boundaries.json`; die 296-Zeilen-CSV wurde nicht künstlich erweitert.

## Initialdateien und Prüfung

Die erste CSV wurde nach vollständiger Zuordnung geschrieben und anschließend unverändert geprüft. Sie enthält exakt 296 eindeutige Identitäten in der Reihenfolge der Originalsicht. Keine Pflichtzelle ist leer. Zulässige Eignungs- und Richtungswerte sowie alle Pins wurden geprüft. Diese Strukturprüfung beurteilt nicht die methodische Richtigkeit meiner Urteile.

- Initial-CSV SHA256: `c5a0be5ffffbe65bafca137f882514e4a2a89c43bbb52b83031da890d67c6921`.
- Eigene Initialurteilsdatei `judgments-initial.json` SHA256: `e53374bd2000a47792c6048de30f9cf3837fb3ac4cb2a31541685be08faa2938`.
- Der Initialhash dieses Markdownberichts wird nach seinem ersten Schreiben separat in `outputs/loop/item-first-methods/initial-hashes.json` festgehalten; ein Selbsthash im Bericht wäre zirkulär.

Ich habe keine ESS-Antworten, Personenkennungen, tatsächlichen politischen Antwortverteilungen, Entblindung, empirischen Modelle, Authentifizierungen, Installationen, Commits oder Änderungen unter `data/raw/` beziehungsweise `data/local/` vorgenommen. Es wurde kein Kappa zwischen Ersturteilen berechnet und kein Abgleich mit fremden Erstbewertungen ausgeführt. CodeRabbit, technische CI und Browserbeobachtung sind keine methodische Validierung dieser Erstbewertung.
