# INVENTORY-003-C: unabhängiger Erstbericht zur Reproduzierbarkeit

Datum 2026-10-03. Frischer Codex-Subagent mit fork_turns="none", begrenztem Auftrag und eigener Ausgabe. Gegenstand ist das eingefrorene öffentliche Dokumentationspaket v1, Manifest-SHA-256 14a87ba5148fba5e640e8164ea06d7ff34cbc2893117dc6baf3eee91f96be7cb. Dieser Erstbericht wird nach Übergabe nicht geändert.

Beide kontrollierten Neubauten sind bytegleich mit dem Frozen JSON. Die Originalzuordnungen C1–C43 passen zu den selbst gelesenen deutschen Fragebogen- und Listenseiten. Ein geringes Finding betrifft die Abgrenzung eines Codebook-Metadatenfelds. Kein erhebliches Finding blockiert weitere öffentliche Quellenarbeit. Wissenschaftliche, methodische und empirische Abnahmen bleiben offen.

## Getrennte Prüfergebnisse

| Prüfumfang | Status | Nachweis und Grenze |
| --- | --- | --- |
| Manifest und zehn Frozen Files / 95 SourceInputs vor und nach | BESTANDEN | Kein Hashunterschied; Pfade innerhalb des Worktrees; kein Raw-/Local-Pfad. |
| JSON zweimal aus kontrollierten Builderkopien | BESTANDEN | Beide und Frozen JSON SHA-256 ff26fe1d0c426005f394127d894e3dea61ffbf1deec283b19e8cc8fc159d4768; direkter Bytevergleich. |
| Deutsche Kategorien, Wortlaut, Nichtantworten, geerbter Kontext, Routing, Listen und Codebook-Locations C1–C43 | BESTANDEN | Originalseiten selbst gesehen; alle Belegverweise auflösbar. Keine 4.2-Antwortprüfung. |
| Metadatenabgrenzung gegenüber Lookupzeilen | NICHT_BESTANDEN | C-R01, gering: zehn Sprachlookupzeilen innerhalb eines Kopf-/Metadatenfelds. |
| Acht tatsächlich mutierte Autoren-Gegenfälle | BESTANDEN | Alle acht verworfen; umgebundene Kopie tatsächlich ausgeführt. |
| Elf zusätzliche tatsächlich mutierte Reviewer-Gegenfälle | BESTANDEN | Alle elf im eigenen Vergleich verworfen; fünf passieren den engeren Autorvalidator. |
| Originalautorindex und Tabellenformatübertragung | BESTANDEN | 41 Tabellen-Inhalts-/Kopfzeilen, gleiche Zellen; Nichttabellenbytes gleich; ursprünglicher Indexhash am Archiv aufgelöst. |
| Originalinventar 296/205 und geschützte Artefakte | BESTANDEN | Gleiche 205 Pending-Einträge nach Originalregeln, 296 CSV-Zeilen. 34 zusätzliche Schutzdateien vor/nach gleich; historische Autoren-Inputhashes alle aktuell gleich. Kein Originalparser-Lauf. |
| Projektprüfung pnpm check | NICHT_GEPRÜFT | Reviewer hat keinen Gesamtlauf gestartet; Integrationsprüfung liegt beim Koordinator. |
| Browser und UI | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Keine Oberfläche oder sichtbarer Testablauf geändert. |
| ESS-4.2-Antwort-/Missing-/Anonymisierungsabgleich | NICHT_GEPRÜFT | Keine ESS-Personendaten oder Portal-Analysen. |
| Eignung, Polung, Score, Neutralität und wissenschaftliche Inventarabnahme | NICHT_GEPRÜFT | Öffentliche Quellenannotation ist keine Messmodell- oder Güteprüfung. |
| Andere Modellfamilie oder akademisches Peer Review | NICHT_GEPRÜFT | Gleiche Codex-Modellfamilie, keine Fachbegutachtung. |

## Anforderungen und Quellen

Gelesen wurden alle zehn Frozen Files, darunter LIFE-93, AGENTS.md, Projektstand, Dauerauftrag, Prüfregeln, Analyseanforderungen, Lizenzen, Autorenbericht und Prüfauftrag. Der zusätzlich gelesene Live-Prüfauftrag ist bytegleich mit seiner gefrorenen Fassung. Die Skills unslop und pdf wurden vor ihrer Anwendung gelesen.

| Originaldokument | Gepinnter SHA-256 | Offizielle Quelle |
| --- | --- | --- |
| Deutscher ESS11-Fragebogen 2023 | be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75 | https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf |
| Deutsches ESS11-Listenheft 2023 | 786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca | https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf |
| Integriertes Codebook, Ausgabe 4.1 | b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35 | https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf |

Eigene neue Renderings der Original-PDFs mit 110 dpi wurden tatsächlich mit view_image gesehen: deutsche Fragebogen-PDF-Seiten 17–31, Listenheft-PDF-Seiten 21–33 und Codebook-PDF-Seiten 70, 71, 72, 73, 74, 77, 78, 88, 92, 103, 104, 105, 106, 107, 108, 117, 132, 147, 156, 165, 166, 167, 168, 169, 170, 171. Das sind alle Codebookseiten mit Belegverweisen dieser Annotation. Gedruckte Codebookseiten liegen eins unter den PDF-Seiten. Die gesamten langen internationalen Lookup-Listen wurden nicht gelesen; keine komplette Ausgabe-/Anonymisierungsklärung wird behauptet. Ein Netzrefresh wurde nicht ausgeführt, weil Gegenstand die gepinnten Frozen Bytes sind.

## Kontrollierter Nachbau

Kopiert wurden build_c.py, source_geometry.py und read_tests.py aus den erlaubten Autoreninputs. Ausschließlich feste Pfadziele wurden umgebunden: OWN nach outputs/loop/inventory003-c-repro/, TARGET auf einen eigenen Standardoutput, der Leser des Autorvalidators auf das Frozen JSON. Die fachliche Auswahlkonfiguration blieb gleich; source_geometry.py blieb bytegleich. Alle Kopien schreiben nur im eigenen Outputordner.

Der erste Builderlauf schrieb reproduced-1.json mit eigenen BBox-Zwischenständen, der zweite reproduced-2.json mit getrennten BBox-Zwischenständen. Beide extrahierten die gepinnten öffentlichen PDFs neu. Der direkte Vergleich zum Frozen JSON und untereinander war bytegleich. Die ursprünglichen Livebuilder, reproduce.sh und Autorentests wurden nie direkt gestartet. Originaldaten, Parser und andere Pakete blieben unverändert.

## Alle 43 Originalketten

Pro Zeile wurden Wortlaut, Labels, Codes, Nichtantworten, Originalkontext und gedruckte Wege gegen die selbst gesehenen deutschen Seiten verfolgt. Zugehörige Listen wurden selbst gelesen. Codebookkandidaten und Locations wurden an den selbst dargestellten Originalseiten geprüft. Unbeschriftete innere Zahlenplätze bleiben null. Die folgende Tabelle ist ein Nachweis des Umfangs, keine Gütemessung.

| Identität | Deutsche Q-PDF-Seite | Exakte gedruckte Codefolge | Deutsche LISTE / PDF-Seite | Kandidat / Location / Codebookfundstelle | Gedrucktes Routing |
| --- | --- | --- | --- | --- | --- |
| C1 | 17 | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 88 | 20 / PDF 21 | happy @ C1 / PDF 70, Druck 69 | kein eigener Drucktext |
| C2 | 17 | 01, 02, 03, 04, 05, 06, 07, 77, 88 | 21 / PDF 22 | sclmeet @ C2 / PDF 71, Druck 70 | kein eigener Drucktext |
| C3 | 17 | 00, 01, 02, 03, 04, 05, 06, 77, 88 | 22 / PDF 23 | inprdsc @ C3 / PDF 71, Druck 70 | kein eigener Drucktext |
| C4 | 18 | 1, 2, 3, 4, 5, 7, 8 | 23 / PDF 24 | sclact @ C4 / PDF 71, Druck 70 | kein eigener Drucktext |
| C5 | 18 | 1, 2, 7, 8 | keine | crmvct @ C5 / PDF 72, Druck 71 | kein eigener Drucktext |
| C6 | 18 | 1, 2, 3, 4, 7, 8 | keine | aesfdrk @ C6 / PDF 72, Druck 71 | kein eigener Drucktext |
| C7 | 19 | 1, 2, 3, 4, 5, 7, 8 | keine | health @ C7 / PDF 72, Druck 71 | kein eigener Drucktext |
| C8 | 19 | 1, 2, 3, 7, 8 | keine | hlthhmp @ C8 / PDF 73, Druck 72 | kein eigener Drucktext |
| C9 | 19 | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 88 | 24 / PDF 25 | atchctr @ C9 / PDF 73, Druck 72 | kein eigener Drucktext |
| C10 | 20 | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 88 | 24 / PDF 25 | atcherp @ C10 / PDF 73, Druck 72 | kein eigener Drucktext |
| C11 | 20 | 1, 2, 7, 8 | keine | rlgblg @ C11 / PDF 74, Druck 73 | ['1'] → C12; ['2', '7', '8'] → C13 |
| C12 | 20 | 01, 02, 21, 22, 03, 04, 05, 06, 07, 08, 09, 77 | keine | rlgdnade @ C12DE / PDF 77, Druck 76 | ['01', '02', '21', '22', '03', '04', '05', '06', '07', '08', '09', '77'] → C15 |
| C13 | 21 | 1, 2, 7, 8 | keine | rlgblge @ C13 / PDF 88, Druck 87 | ['1'] → C14; ['2', '7', '8'] → C15 |
| C14 | 21 | 01, 02, 21, 22, 03, 04, 05, 06, 07, 08, 09, 77 | keine | rlgdeade @ C14DE / PDF 92, Druck 91 | ['01', '02', '21', '22', '03', '04', '05', '06', '07', '08', '09', '77'] → C15 |
| C15 | 21 | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 88 | 25 / PDF 26 | rlgdgr @ C15 / PDF 103, Druck 102 | kein eigener Drucktext |
| C16 | 22 | 01, 02, 03, 04, 05, 06, 07, 77, 88 | 26 / PDF 27 | rlgatnd @ C16 / PDF 103, Druck 102 | kein eigener Drucktext |
| C17 | 22 | 01, 02, 03, 04, 05, 06, 07, 77, 88 | 26 / PDF 27 | pray @ C17 / PDF 104, Druck 103 | kein eigener Drucktext |
| C18 | 22 | 1, 2, 7, 8 | keine | dscrgrp @ C18 / PDF 104, Druck 103 | ['1'] → C19; ['2', '7', '8'] → C20 |
| C19 | 23 | 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 88 | keine | dscrrce @ C19 / PDF 104, Druck 103; dscrntn @ C19 / PDF 104, Druck 103; dscrrlg @ C19 / PDF 105, Druck 104; dscrlng @ C19 / PDF 105, Druck 104; dscretn @ C19 / PDF 105, Druck 104; dscrage @ C19 / PDF 105, Druck 104; dscrgnd @ C19 / PDF 106, Druck 105; dscrsex @ C19 / PDF 106, Druck 105; dscrdsb @ C19 / PDF 106, Druck 105; dscroth @ C19 / PDF 106, Druck 105; dscrdk @ C19 / PDF 107, Druck 106; dscrref @ C19 / PDF 107, Druck 106; dscrnap @ C19 / PDF 107, Druck 106; dscrna @ C19 / PDF 107, Druck 106 | kein eigener Drucktext |
| C20 | 23 | 1, 2, 7, 8 | keine | ctzcntr @ C20 / PDF 108, Druck 107 | kein eigener Drucktext |
| C21 | 23 | 1, 2, 7, 8 | keine | brncntr @ C21 / PDF 108, Druck 107 | ['1'] → C24; ['2'] → C22; ['7', '8'] → C24 |
| C22 | 24 | 7777, 8888 | keine | cntbrthd @ C22 / PDF 108, Druck 107 | kein eigener Drucktext |
| C23 | 24 | 7777, 8888 | keine | livecnta @ C23 / PDF 117, Druck 116 | kein eigener Drucktext |
| C24 | 24 | 777, 888 | keine | lnghom1 @ C24 / PDF 117, Druck 116; lnghom2 @ C24 / PDF 132, Druck 131 | kein eigener Drucktext |
| C25 | 24 | 1, 2, 7, 8 | keine | feethngr @ C25 / PDF 147, Druck 146 | kein eigener Drucktext |
| C26 | 25 | 1, 2, 7, 8 | keine | facntr @ C26 / PDF 147, Druck 146 | ['1'] → C28; ['2'] → C27; ['7', '8'] → C28 |
| C27 | 25 | 7777, 8888 | keine | fbrncntc @ C27 / PDF 147, Druck 146 | kein eigener Drucktext |
| C28 | 25 | 1, 2, 7, 8 | keine | mocntr @ C28 / PDF 156, Druck 155 | ['1'] → C30; ['2'] → C29; ['7', '8'] → C30 |
| C29 | 25 | 7777, 8888 | keine | mbrncntc @ C29 / PDF 156, Druck 155 | kein eigener Drucktext |
| C30 | 26 | 01, 02, 03, 04, 05, 55, 77, 88 | 27 / PDF 28 | ccnthum @ C30 / PDF 165, Druck 164 | ['01', '02', '03', '04', '05'] → C31; ['55'] → EINLEITUNG VOR C43; ['77', '88'] → C31 |
| C31 | 26 | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 88 | 28 / PDF 29 | ccrdprs @ C31 / PDF 166, Druck 165 | kein eigener Drucktext |
| C32 | 26 | 1, 2, 3, 4, 5, 7, 8 | 29 / PDF 30 | wrclmch @ C32 / PDF 166, Druck 165 | kein eigener Drucktext |
| C33 | 27 | 1, 2, 3 | keine | admrclc @ C33 / PDF 167, Druck 166 | ['1'] → C34; ['2'] → C37; ['3'] → C40 |
| C34 | 27 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 88 | 30 / PDF 31 | testjc34 @ C34 / PDF 167, Druck 166 | kein eigener Drucktext |
| C35 | 28 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 88 | 30 / PDF 31 | testjc35 @ C35 / PDF 168, Druck 167 | kein eigener Drucktext |
| C36 | 28 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 88 | 30 / PDF 31 | testjc36 @ C36 / PDF 168, Druck 167 | None → EINLEITUNG VOR C43 |
| C37 | 29 | 1, 2, 3, 4, 5, 7, 8 | 31 / PDF 32 | testjc37 @ C37 / PDF 169, Druck 168 | kein eigener Drucktext |
| C38 | 29 | 1, 2, 3, 4, 5, 7, 8 | 31 / PDF 32 | testjc38 @ C38 / PDF 169, Druck 168 | kein eigener Drucktext |
| C39 | 29 | 1, 2, 3, 4, 5, 7, 8 | 31 / PDF 32 | testjc39 @ C39 / PDF 169, Druck 168 | None → EINLEITUNG VOR C43 |
| C40 | 30 | 0, 1, 2, 3, 4, 77, 88 | 32 / PDF 33 | testjc40 @ C40 / PDF 170, Druck 169 | kein eigener Drucktext |
| C41 | 30 | 0, 1, 2, 3, 4, 77, 88 | 32 / PDF 33 | testjc41 @ C41 / PDF 170, Druck 169 | kein eigener Drucktext |
| C42 | 30 | 0, 1, 2, 3, 4, 77, 88 | 32 / PDF 33 | testjc42 @ C42 / PDF 170, Druck 169 | kein eigener Drucktext |
| C43 | 31 | 1, 2, 33, 44, 55, 65, 77, 88 | keine | vteurmmb @ C43 / PDF 171, Druck 170 | None → MODUL D |

Die Einleitung vor C1 gilt nach Original und Codebook für C1–C29, die persönliche Einleitung vor C7 für C7–C29, die Verbundenheitseinleitung für C9/C10. C6/C7 behalten ihre Vorleseanweisungen getrennt. C8 behält die bedingte Nachfrage im Wortlaut. C11/C12 und C13/C14 bewahren die verschachtelten Filter und gedruckten Zellenziele. C12/C14 drucken 21/22 und allein 77 als Nichtantwort. Codebook 4.1 zeigt bei C12DE/C14DE 291/290 samt Anonymisierungshinweis; das ist keine geprüfte Rekodierung.

C18=1 aktiviert C19 als Mehrfachnennung mit Nachfragen und Mehrfachanweisung. Die 14 Codebook-Indikatoren für Gründe und Nichtantwortzustände tragen Location C19 und 0/1-Markierung. Sie ersetzen nicht die Original-Mehrfachcodes. AN-ALLE-Marker vor C15, C20, C24, C28, C30 und C43 sowie die geografischen Anweisungen C21/C23/C26/C28 bleiben erhalten. C22/C23/C24/C27/C29 behalten offene Länder-, Jahr- und Spracheingaben, ISO- und Eintragsanweisungen; keine Kategorien werden erfunden.

C30=55 springt vor C43 und überspringt C31–C42. 01–05 und 77/88 führen C31; der not55-Filter bleibt für C31–C42 erhalten. 55/77/88 werden nicht als strukturelle Nullen festgelegt. Bei C31 bilden beide vertikalen 8-Tokens den gedruckten Code 88. C33 ist CAPI-Zuteilung, keine Befragtenfrage. Die ausdrückliche Nichtanzeige-/Nichtfrageanweisung steht in Codebook PDF 167/Druck 166 und wurde selbst gesehen.

C34–C36 tragen Gruppe 1 und 0–10; C37–C39 Gruppe 2 und 1–5 mit der gedruckten Labelrichtung; C40–C42 Gruppe 3 und 0–4. Gemeinsame Zuteilung mit Modul I ist belegt. C36/C39 drucken einen Sprung vor C43. Die vollständige Seite nach C42 druckt keinen. C43 bewahrt 33/44/55/65 neben 1/2 und 77/88.

Offen bleiben ausdrücklich der Abgleich zur Datenausgabe 4.2 für alle 43 Identitäten, getrennte Eignungs-/Polungsurteile, methodische Abnahmen, C12/C14-Rekodierung, C19-Indikatoren und strukturelles Nichtzutreffen, ISO-/Anonymisierungsklärung C22/C27/C29, Jahr/Sprache C23/C24, bedingte Klimaantworten, Experimentalgruppen, Sonderantwortrollen im Auswertungsvertrag, Export/Lizenzprüfung und Zusammenführung mit dem Originalinventar. Der ursprüngliche Bestand bleibt 296/205; kein Abzug einer vermeintlichen Zahl von 53 C-Fragen.

## Ausgeführte Gegenfälle

Die acht benannten Gegenfälle wurden tatsächlich von der umgebundenen Autorvalidator-Kopie mutiert und ausgeführt.

| Autorengegenfall | Tatsächlich mutierte vollständige Codefolge | Ergebnis |
| --- | --- | --- |
| C30 mutated code sequence | 01, 02, 03, 04, 05, 77, 88 | REJECTED |
| C31 mutated code sequence | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 77, 8 | REJECTED |
| C37 mutated code sequence | 0, 1, 2, 3, 4, 77, 88 | REJECTED |
| C43 mutated code sequence | 1, 2, 77, 88 | REJECTED |
| C12 mutated code sequence | 01, 02, 21, 22, 03, 04, 05, 06, 07, 08, 09, 77, 88 | REJECTED |
| C30 01/05 labels swapped while all tokens remain present | 01, 02, 03, 04, 05, 55, 77, 88 | REJECTED |
| C32 inherited not55 filter omitted | 1, 2, 3, 4, 5, 7, 8 | REJECTED |
| C37 falsely linked to LISTE 32 instead of LISTE 31 | 1, 2, 3, 4, 5, 7, 8 | REJECTED |

Die elf zusätzlichen Mutationen entstanden in independent_checks.py. Dessen Originalerwartungen wurden nach eigener Seitenlektüre festgelegt. Die folgenden Ergebnisse sind tatsächliche Läufe.

| Eigener Gegenfall | Codefolgen der betroffenen Identitäten nach Mutation | Autorvalidator | Eigener Originalvergleich |
| --- | --- | --- | --- |
| C30 code55 falsely routes C31 | C30: 01, 02, 03, 04, 05, 55, 77, 88 | REJECTED | REJECTED |
| C34 exact group1 filter omitted, not55 preserved | C34: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 77, 88 | ACCEPTED | REJECTED |
| C33 falsely described as respondent scale | C33: 1, 2, 3 | ACCEPTED | REJECTED |
| C43 special33 reclassified as ordinary response | C43: 1, 2, 33, 44, 55, 65, 77, 88 | ACCEPTED | REJECTED |
| C14 absent88 inserted preserving real categories | C14: 01, 02, 21, 22, 03, 04, 05, 06, 07, 08, 09, 77, 88 | REJECTED | REJECTED |
| C19 0/1 indicator values substitute interview multicodes | C19: 0, 1 | REJECTED | REJECTED |
| C22 ISO coding instruction omitted | C22: 7777, 8888 | REJECTED | REJECTED |
| C24 ISO coding instruction omitted | C24: 777, 888 | REJECTED | REJECTED |
| C39 real group exit removed | C39: 1, 2, 3, 4, 5, 7, 8 | ACCEPTED | REJECTED |
| C42 C39 exit falsely added | C42: 0, 1, 2, 3, 4, 77, 88 | REJECTED | REJECTED |
| C40-C42 coherent endpoint and source-token swaps, genuine source tokens preserved | C40: 0, 1, 2, 3, 4, 77, 88; C41: 0, 1, 2, 3, 4, 77, 88; C42: 0, 1, 2, 3, 4, 77, 88 | ACCEPTED | REJECTED |

Beim konsistenten C40–C42-Endpunkttausch wurden Labelwerte, die entsprechenden Belegauszüge und Original-Token-BBox sowie die gemeinsamen LISTE-32-Endpunktbelege vertauscht. Alle Tokens existieren weiterhin im Original. Für genau diesen Fall wurde der Autorvalidator zusätzlich mit frisch extrahierten Originalseiten aufgerufen; er akzeptiert ihn. Die eigenen expliziten Originalendpunkte verwerfen ihn. Auch weggelassene C33-Gruppenfilter, falscher C33-Formattyp, umklassifizierte C43-Sonderantworten und ein entfernter C39-Sprung passieren den engeren Autorvalidator.

Das belegt seine Testgrenze, keine falsche Zuordnung im Frozen JSON: dessen Endpunkte und Gruppenabläufe stimmen mit der selbst gesehenen Quelle überein. Der Autorbericht erklärt die acht Gegenfälle bereits nicht als allgemeinen Validitätsnachweis. Für spätere automatische semantische Gates sollten tatsächliche Gruppenfilter, Routen, administrative Rollen und Code-Label-Zellen zusätzlich erwartet werden. Tokenmitgliedschaft, Eigenkonsistenz und Beleg-ID-Suffix reichen dafür nicht.

## Finding C-R01

Schwere gering. Status OFFEN.

Betroffen ist C24 → variable_zuordnung.quellen → lnghom2 → metadaten, Status DOKUMENTATION_4_1_TEILLEKTUERE_KOPF_FILTER_BESCHREIBUNG, mit Beleg CB41-lnghom2-metadata-132. Umfang und Fundstellenbeschreibung nennen Variablenkopf und Metadaten; codebook() kommentiert die Trennung von Kopf-/Filter-/Beschreibungstext und Lookup-Tabellen.

Originalbeleg: Codebook 4.1, SHA-256 b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35, PDF-Seite 132/Druckseite 131. Unter der abgeschlossenen lnghom2-Metadatentabelle folgt „Applies to variable lnghom2.“ und eine separate ISO-639-2-Lookuptabelle. Die zehn ersten Tabellenzeilen AAR/Afar, ABK/Abkhazian, ACE/Achinese, ACH/Acoli, ADA/Adangme, ADY/Adyghe, Adygei, AFA/Afro-Asiatic (Other), AFH/Afrihili, AFR/Afrikaans und AIN/Ainu stehen dennoch im Metadatenstring und zugehörigen Kopf-/Metadatenbeleg.

Problem: Die Stoppregel erkennt numerische Kategoriezeilen und einen International-Kopf, aber keine alphabetischen Sprachcodezeilen. Der Auszug ist reproduzierbar, reicht jedoch über seine deklarierte Feld- und Beleggrenze hinaus.

Wirkung: Nachnutzende können einen zufällig seitenbegrenzten Lookup-Anfang als reinen Variablenkopf behandeln. Deutsche Originalkategorien und Locations sind weiterhin richtig; keine vollständige Sprachcodetabelle oder 4.2-Rekodierung wird als geprüft ausgegeben. Deshalb gering, ohne Blockade weiterer Quellenarbeit.

Korrektur: Metadaten am Ende der Frage-/Post-Question-Zellen stoppen oder die Lookupzeilen ausdrücklich als separaten begrenzten Auszug markieren. Wenn der Vertrag reine Kopf-/Filter-/Beschreibungslektüre verlangt, reicht bloßes Umbenennen nicht. Builderkopie danach zweimal ausführen und neue Hashes sichern. Nachprüfung: C24-Wortlaut, beide Locations, ISO-/Anonymisierungshinweise und Bis-zu-zwei-Sprachen-Anweisung bleiben gleich; Lookupzeilen gehören nicht mehr zu metadaten. Originalfassung und Erstbericht erhalten.

## Originalindex und Tabellenformatierung

Die archivierte ursprüngliche Autorenfassung unter outputs/loop/inventory003-c-format-transfer/author-original.md hat 18854 Bytes und SHA-256 e1115c1db314202fe2468f9c95bb36d24408123f6e22e625de3873c7c3b08ca1. Der unveränderte output-index.json bindet diesen report_sha256 und denselben files-Eintrag. Die ausdrückliche preservedOriginalPath im Manifest löst beides auf das Archiv auf.

Die formatierte Frozen Autorenfassung hat separat SHA-256 743ba5394678f62c9d12b82b5518e3b60392ea59a8a727036114f209a02ad661. Eigene Prüfung: alle 41 Tabellen-Inhalts-/Kopfzeilen haben exakt gleiche Zellen, Nichttabellenzeilen inklusive Zeilenenden sind bytegleich. Nur Randabstände und Trennstrichbreiten der Tabellen ändern sich. Dies bestätigt keine Quellenbedeutung oder wissenschaftliche Güte.

## Laufzeit, Werkzeuge, Fehlversuche und Grenzen

Modell gpt-6.1-sol, Reasoning ultra, geerbt. Der Elternagent bestätigte nur T3-Laufzeitmetadaten: fork_turns="none", kein Modell-/Reasoning-Override. Interne Revision und nicht zugängliche Anbietervorgaben bleiben unbekannt. Organisatorisch getrennte Erstprüfung in derselben Codex-Modellfamilie; keine andere Modellfamilie, akademisches Peer Review oder Biasfreiheitsgarantie.

Das gesamte angebotene Toolverzeichnis mit Namen/Beschreibungen steht in tool-offers.json. Zusätzlich sichtbar waren functions.exec/wait/request_user_input, Clock, Collaboration und CUA. Tatsächlich genutzt wurden functions.exec, darin exec_command, write_stdin, apply_patch, view_image, sowie direkte collaboration.send_message für operative Status- und Runtime-Metadaten. Keine Agents gestartet oder Agentlisten gelesen, keine Peer-/Jurorberichte, Loopfindings oder Autorenverteidigungen gelesen.

Vollständige Shellbefehle und Exits stehen in command-exits-final.json. Frühere vollständige Toolausgaben stehen in command-exits.json; das Abschlusslog begrenzt große stdout-Auszüge und hält deren Länge fest. Poppler-Unterprozesse: subprocess-runs.json, tool-exits.jsonl, render-exits.json, codebook-render-exits.json. Tatsächlich gezeigte Seiten: visual-reading.json. Einmalige Berichtserstellung: python outputs/loop/inventory003-c-repro/write_report.py. Eigene Patches erzeugten nur Builderkopien, Originalerwartungen und Logs im eigenen Ordner.

Python 3.14.7; pdftotext und pdftoppm 26.08.0. Beide Builderläufe, Autorvalidator-Kopie, eigene Mutationen und alle Renderings endeten mit Exit 0. Der kombinierte Erstreade wurde im Tooloutput gekürzt; Anforderungen und Autorenbericht danach einzeln erneut gelesen. Ein sed-Aufruf hinter dem Dateiende lieferte bei Exit 0 nichts; der korrekte Schluss wurde anschließend gelesen.

Der erste Hilfszähler zählte 296 nichtleere offene_punkte statt der ursprünglichen Pending-Regel. Er bleibt als original-inventory-counts-first-inapplicable.json erhalten. Danach wurden die Originalregeln pipeline/inventar.py:610–628 gelesen und nachgezählt: 296 Gesamtzeilen und die exakt gleiche Pending-Liste mit 205 Einträgen. Dies ist kein zusätzlicher Originalparserlauf. Eine große Provenienz-Ausgabe wurde gekürzt; die benötigten Zählfelder wurden danach separat gelesen.

Zwei operative Abschlussfehler blieben ohne Artefaktänderung: Ein functions.exec-Berichtsgenerator scheiterte vor Toolausführung an JavaScript-Syntax mit unescaped Markdown-Backticks. Ein nachfolgender Log-Schreibversuch wurde vor Prozessstart mit „Argument list too long“ abgewiesen. Das reduzierte Abschlusslog und ein korrekt gequoteter eigener Generator behoben dies. Es gab keine fachliche Berechnung aus fehlgeschlagenen Aufrufen.

Keine technisch getrennte Filesystem-Sandbox. Grenzen waren auftrags- und pfadbasiert; exec_command stets mit zugewiesenem workdir, alle Patchpfade absolut. Eigene Writes ausschließlich outputs/loop/inventory003-c-repro/ und dieser neue Bericht. Die anfängliche Git-Namenliste diente Branch-/Dirty-Prüfung; vorhandene fremde Änderungen blieben erhalten. Der Koordinator kann gemeinsame Zustandsdateien parallel ändern. Hashprüfungen behaupten deshalb keine unveränderliche Gesamtsitzung.

integrity-before.json und integrity-after.json prüfen Manifest und alle 105 Inputs. protected-before.json und protected-after.json ergänzen 34 Original-/A/B-/METHODS-Dateien. author-protected-hashes-current.json bestätigt sämtliche historischen Autoreninputs aktuell. Keine Abweichung. Die A/B-Datei ist öffentliche Quellenannotation, keine Personendatenhälfte. Kein Zugriff auf data/raw/, data/local/, ESS-Antwortdatenhälften, Personenkennungen, Wahl-/Parteiergebnisse, Selbsteinstufungswerte, Verteilungen, Portal-Analyse, Credentials oder Secrets. Keine Installation, Conda, Systemänderung, globale Writes, Commit/Push, fremde Formatierung oder pnpm-Gesamtlauf.

Die Frozen Lizenzakte trennt CC BY-SA 4.0 für ESS-Dokumentation und CC BY-NC-SA 4.0 für ESS-Daten. Quellenversionen, Attribution und Änderungsvermerke sind am Annotationartefakt vorhanden. Keine neue rechtsfachliche Freigabe, keine ESS-Billigung und keine konkrete spätere Exportfreigabe wird behauptet.

## Tatsächlicher Startauftrag im Wortlaut

```text
Du bist ein frischer unabhängiger Reproduzierbarkeitsreviewer im KI-Audit LIFE-93. Projekt ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, Branch research/life-93-night-20261003. WICHTIG tools.apply_patch verwendet sonst ursprüngliches CWD: ALLE Patchpfade absolut innerhalb dieses Worktrees; exec_command stets workdir. Eigene Outputs ausschließlich outputs/loop/inventory003-c-repro/, eigener unveränderlicher Erstbericht reports/loop/reviews/INVENTORY-003-C-repro.md. Keine anderen Reviewerberichte/Loopfindings/Agentlisten oder Verteidigungen lesen, keine weiteren Agents starten. Inhaltlich unverändertes Prüfpaket reports/loop/packages/INVENTORY-003-C/v1/manifest.json SHA25614a87ba5148fba5e640e8164ea06d7ff34cbc2893117dc6baf3eee91f96be7cb, 10files95SourceInputs; gefrorene Dateien im Unterordner files. Lies Anforderungen LIFE-93, AGENTS.md, Auftrag, Prüfregeln, Analyseanforderungen, Lizenzen aus Paket plus reports/loop/INVENTORY-003-C-pruefauftrag.md und gefrorenen Autorenbericht. Kontrolliere Paket/Sourcehashes vor/nach. Untersuche sämtliche43 öffentlichen C1–C43-Ketten (Kategorien, Missing, Listen/Codebook, geerbter Kontext/Filter), reproduziere mit Builderkopien, deren feste Ziele ausschließlich auf eigene Outputs umgebunden werden, zweimal bytegleich. Feste Livebuilder/reproduce.sh/Autorentests niemals direkt starten. Original296/205/CSV/Parser/AB/METHODS und alle Paketinputs unverändert lassen. Gegenfälle tatsächlich mutieren/ausführen, eigene zusätzliche Gegenfälle. Relevant C30=55 vorC43 vs01–05/77/88 C31, C31–C42 bedingt; C33 CAPI-Zuweisung keine Befragtenfrage; Gruppen C34–36/C37–39/C40–42, C42 kein gedruckterSprung; C43 33/44/55/65. C12/C14 nur77,21/22 nicht unbelegt291/290; C19 Mehrfachnennung nicht0/1Indikatoren; ISO/Jahr/Sprache offene Restpunkte. Original-Q17–31/Listenseiten21–33 und relevante Codebookfundstellen selbst prüfen; Tokenanwesenheit allein keine semantische Zellzuordnung. Originalautorindex bleibt originalen Reportbytes zugeordnet über ausdrücklich archivierte preservedOriginalPath im Manifest, aktuelle Reportbytes separat. Rootübertragung nur Tabellenformat, gleich geprüfteZellen/Nichttabellen; eigene Prüfung. Keine ESS Rohdaten/Local/A/B/Personen/Parteien/Selbsteinstufungswerte/Verteilungen/Secrets/Zugangsdaten/globalWrites/InstallConda/CommitPush/Gesamtformat. Öffentliche PDF/Metadaten erlaubt. Gegenwärtige Quellenannotation keine finale Eignungs-/Polungs-/Neutralitäts-/wissenschaftlicheInventarabnahme oder4.2-Antwortabgleich. Findings C-Rxx: exakt betroffeneAussage, belegteFundstelle, Problem, Wirkung, begründeteSchwere, konkreteKorrektur/Nachprüfung; keine Quote/erfundene Kritik, Vermutungen kenntlich. Vollständigen tatsächlichen Auftrag wortgetreu, Modell, angebotene/genutzteTools, Commands/Exits/Fehlläufe/SharedFS-Grenzen dokumentieren. Organisatorisch getrennter gleicher Codexmodellfamilie, keine unabhängige Modellfamilie/akademischesPeerReview. Bericht erst final dann Root melden; ursprüngliche Erstbewertung unverändert erhalten. Teile operative Hindernisse kurz mit; bearbeite autonom vollständig.
```

Diese Erstbewertung gilt allein für das genannte Manifest. Ergebniswirksame Korrekturen brauchen einen neuen prüfbaren Stand und gesonderten Nachbericht.
