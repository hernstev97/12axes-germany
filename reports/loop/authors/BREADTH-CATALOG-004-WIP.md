# BREADTH-CATALOG-004-WIP

Stand: 2026-10-03, UTC; genaue Bearbeitungs- und Prüfzeiten stehen in den JSON-Artefakten. Dies ist die Quellenbindung des vom Root vor Antwortanalysen festgelegten Entwurfs mit 43 Angaben. Es ist keine neue unabhängige Auswahl oder Erstbewertung. Autor: Codex, dieselbe Modellfamilie wie Root. Keine zusätzliche Autoren- oder Modellfamilienunabhängigkeit wird angerechnet.

Der neue [Fragenentwurf](../../../data/politikprofil-v2.fragen.entwurf.json) hat `schemaVersion: 1` und `status: DRAFT_NOT_GATE`. Er enthält 43 eindeutige `studyId:variable`-Einträge, acht Primärthemen und fünf getrennte historische Studienreferenzen. 42 Einträge sind innerhalb des ausdrücklich beschriebenen statischen Original-/API-Quellenumfangs vollständig; allein `ESS10SCe03_2:scchpldm` bleibt `incomplete`. Das ist weder eine wissenschaftliche Freigabe noch eine Aussage über tatsächlich erhobene Antworten, heutige Deutschlandwerte, gemeinsame Personen, Faktorstruktur oder Übertragbarkeit.

## Konkrete Originalbindung

Die Seiten sind durchgehend **1-basierte physische PDF-Seiten**, keine geschätzten Bereiche. Deutsche Texte wurden aus den nationalen Originalen übernommen; Layoutumbrüche und Trennstriche am Zeilenende sind normalisiert. Einleitungen, Stämme, Szenarien, Listennummern und die beobachteten Sprunganweisungen stehen getrennt im JSON. Die API-IDs und deren Metadatenversionen binden die exportierten Variablen und vollständigen Codelisten; die Zuordnung zu nationalen Frage-IDs ist ein dokumentierter Inhaltsabgleich, kein vom API gelieferter deutscher Frage-ID-Schlüssel.

| Datei | Angaben und deutsche Originalanker | Originalfundstellen |
| --- | --- | --- |
| ESS5e03_6 | `bplcdc` D18; `dpcstrb` D20; `hrshsnta/dbctvrd/lwstrob/rgbrklw` D33–D36 | Fragebogen 24; D20 24–25; Rechtsmatrix 27. Listen 33/41 und Originalkontext „Deutschland heute“ dokumentiert. |
| ESS8e02_3 | `inctxff/sbsrnen/banhhap` D30–D32; `gvslvol/gvslvue/gvcldcr` E6–E8; `imsclbn` E15; `bnlwinc/eduunmp/wrkprbf` E33–E35 | Fragebogen 33, 36, 37, 42; tatsächliche Antwortlisten 44/48/50/53 auf Showcard-PDF-Seiten 45/49/51/54. |
| ESS9e03_3 | `sofrdst/sofrwrk/sofrpr/sofrprv` G26–G29 | Fragebogen 97, gemeinsame Gerechtigkeitseinleitung und Liste 68. |
| ESS10SCe03_2 | `imsmetn/imdfetn/impcntr` A54–A56; `vteurmmb` A90; vollständige zwölf Normfragen B1–B12; `scchpldm` B25 | PAPI 7/10/10–11/12; CAWI Migrationseinleitung 93 und Fragen 94–96, EU 135, Demokratieeinleitung 136 und Fragen 137–148, B25 162. |
| ESS11e04_2 | `gincdif` B33; `euftf` B37; `eqparep` E19; `eqparlv/freinsw/fineqpy` E20–E22 | Fragebogen 13/14/51/52; Listen 13/14/64, einschließlich vollständigem Elternzeit-Paar-Szenario. |

Der ESS10-Block `democracy_norms` enthält B1–B12 in Originalreihenfolge und den gesamten gemeinsamen Allgemein-Demokratie-Kontext. `keydec` bleibt B12 in diesem Block und hat das Primärthema `europe`. Der Entwurf enthält keine Performance-Fragen, B26–B29, `impdema` oder Grundeinkommensfrage. Die ursprüngliche Position ausgelassener Nachbarfragen wird als Kontext festgehalten, daraus wird keine originalidentische Durchführung des gekürzten Entwurfs abgeleitet.

## Codes und Formvarianten

- EU-Abstimmung: PAPI `1/2/3/4/5/6` entspricht API-Dateicodes `1/2/33/44/55/65`. `55` ist Nichtwahl, `65` fehlende Stimmberechtigung. Das API deklariert beide als gültige Antwortoptionen; sie sind als eigene semantische Rollen gekennzeichnet und keine Ja/Nein-EU-Positionen. Aus der angebotenen Option `65` wird kein tatsächlicher Frageausfall abgeleitet.
- ESS5 Polizeipflicht: gedrucktes „Weiß nicht“ `98` entspricht API `88`. ESS11 EU-Skala: gedrucktes `00–09` entspricht API `0–9`; API `9` ist hier regulär. Fehlende Antworten stehen getrennt, mit unverändertem `reasonApi`; im Original nicht gedruckte Missing-Labels bleiben `null`.
- ESS8 Verantwortungsfragen: Die Fragebogentabelle auf Seite 36 lässt die 10 aus, während Einleitung und obere Beschriftung eine 0–10-Skala beschreiben. Die tatsächliche Liste 48 auf Showcard-Seite 49 **enthält 10**, ebenso die API-Codeliste. Diese Fundstelle trägt die Kategorie; sie wurde nicht erfunden.
- Direkter Originalabgleich korrigiert die frühere verkürzte BINDING003-Transkription der Zuwanderungsoption 3: Auf **PAPI-Seite 7 und CAWI-Seiten 94–96** steht „Ein paar wenigen erlauben“. Der alte Bericht bleibt unverändert; der neue Katalog nennt die Korrektur ausdrücklich. Die CAWI-Fragen A55/A56 wiederholen zudem „Sollte Deutschland es...“, das die Papierfassung aus A54 fortführt.
- CAWI B3–B7 und B10 verkürzen den einzelnen Fragesatz um „für die Demokratie im Allgemeinen“. Die vollständige Einleitung auf Seite 136 und beide Allgemeinen-Demokratie-Antwortanker bleiben sichtbar. B1/B2/B8/B9/B11/B12 enthalten den längeren Fragesatz. Diese Texte werden getrennt gespeichert; psychometrische oder empirische Gleichwertigkeit wird nicht behauptet.

Die CAWI-Screenshots drucken keine A/B-Fragenummern. Ihre Identitäten sind deshalb als Inhaltsentsprechungen zur PAPI-Fassung ausgewiesen, mit `printedId: null`. Bei unnummerierten Radiooptionen wird kein sichtbarer Dateicode behauptet; exportierte Codes und sichtbare Beschriftungen stehen getrennt. Die vollständige Zuordnung der 17 Felder liegt zusätzlich in [cawi-seventeen-crosswalk.json](../../../outputs/loop/breadth-catalog-004/cawi-seventeen-crosswalk.json).

## Verbleibende Bindungen

`remainingBindings` enthält zwei offene Felder, beide ausschließlich bei `scchpldm`:

1. `routing.draftPostItemRouting`: Die PAPI-Fassung leitet Antwort 1 zu B26 und Antwort 2 zu B28. B26–B29 sind im vorgegebenen Entwurf ausgelassen. Ein abgestimmter Ersatzablauf liegt nicht vor; das Feld bleibt `null`.
2. `modeBinding.cawiOperationalConditionalRouting`: Die CAWI-Seite 162 zeigt die zwei Alternativen und zurück/weiter, aber keine bedingte Ausführungsregel. Eine Screenshot-Reihenfolge beweist keinen tatsächlich programmierten Sprung. Die statischen Frage-/Antworttexte sind gebunden; die Ausführung bleibt offen.

Separat bleiben Zugangs-/Designgrenzen bestehen: Bei ESS5 ist im aktuellen Hauptdateikatalog kein `prob/psu/stratum` deklariert und kein konkreter deutscher Design-Dateiweg gesichert. ESS8 hat eine gesondert deklarierte SDDF-Datei. Katalogisierte Gewichts-/Designfelder sind kein Werte- oder Verfügbarkeitsnachweis. ESS10-Dateiidentität/DOI nennen SC 3.2, während die gespeicherte Zitier-/Historybeschreibung noch 3.1 nennt; diese Inkonsistenz wurde nicht still korrigiert. Eine neue öffentliche Datenübertragung wurde hier weder versucht noch als unmöglich behauptet. Der Root meldete inzwischen eine eigene reine Byteaufnahme bereitgestellter Dateien; diese Mitteilung ist keine von mir geprüfte Edition-, Header- oder Empiriebindung.

## Rechte, Provenienz und Grenzen

Die gesicherte [offizielle ESS-Rechtequelle](https://europeansocialsurvey.org/contact/disclaimer) trennt Dokumentation **CC BY-SA 4.0** von Daten **CC BY-NC-SA 4.0**. Der JSON-Entwurf enthält die ESS-ERIC-/Sikt-Zuschreibung, die offiziellen Studien- und Dokumentations-DOIs, die Layout-/Strukturierungsänderungsangabe und getrennte Lizenzidentitäten. Dokumentationsrechte ersetzen keine Freigabe eines adaptierten Tests oder einer aktuellen Bevölkerungsreferenz. Die tatsächlichen öffentlichen Original-URLs, Abruf-UTC, HTTP-Status und unveränderten Originalbyte-Hashes stehen unter `sources` und im eigenen [Quellenkatalog](../../../outputs/loop/breadth-catalog-004/sourcecatalog.json). Nicht eigens abgerufene aktuelle Studienseiten werden nicht durch erfundene URLs ersetzt.

Dieser Auftrag nutzte bestehende eigene öffentliche Originale, API-Codelisten und die ausdrücklich erlaubten ACCESS002/BINDING003-Quellen-Crosswalks. **Keine neuen Netzabrufe**, Rohdaten, Datenheader, Antworten, Frequenzen, Statistiken, fremden Urteile, `inventar.csv`, Authentifizierung, Kontakte oder Agentenaufträge. Für die bildbasierten ESS10-Instrumentseiten wurden vorhandenes `pdftoppm` und `tesseract` verwendet. OCR diente im begrenzten Original-Instrumentbereich 80–175 nur als Seitenlocator; dabei wurden auch benachbarte Frageformulierungen erkannt, keine Antwort-/Ergebnisabschnitte. Zur endgültigen Transkription wurden die 17 Ziel-Fragen und nötigen Einleitungsseiten visuell geprüft. Nicht benötigte Locator-Screens wurden aus dem eigenen neuen Output verworfen. Daraus wird keine absolute historische Ergebnisblindheit rekonstruiert.

Die [Prüfdatei](../../../outputs/loop/breadth-catalog-004/validation.json) bestätigt 43 eindeutige Einträge, die vorgegebene Variablenmenge, Studien-Trennung, disjunkte Codegruppen, lückenlose API-Codeabdeckung und gültige Original-Code-Reihenfolge, deutsche Druckcode-Abbildung, B1–B12-Kontext/Reihenfolge, `keydec`-Thema, unveränderte Originalbytes und die drei unveränderten historischen Berichte. Es wurden keine wissenschaftlichen, empirischen, Nutzungs- oder UI-Abnahmen und keine Plan-/Versions-Tags behauptet. Gemäß dem beschränkten Auftrag wurden weder Git noch `pnpm` ausgeführt.

Die abschließenden Artefakt-Hashes stehen in `outputs/loop/breadth-catalog-004/artifact-hashes.json`; dort wird dieser Bericht selbst nach seiner Erstellung gehasht.
