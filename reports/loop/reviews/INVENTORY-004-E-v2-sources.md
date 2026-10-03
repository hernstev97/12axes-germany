# INVENTORY-004-E v2: unabhängige Quellen- und Inhaltsnachprüfung

Nachbericht vom 2026-10-03, Reviewer `inventory004_e_v2_sources`, frischer organisatorischer Kontext. Geprüftes Manifest: `reports/loop/packages/INVENTORY-004-E/v2/manifest.json`, SHA-256 `e1e184883b5f2ca04f729b2c2383777070601af6eba049c72e040aa1e1f56ca2`. Der Bericht bleibt nach seiner abschließenden individuellen Formatierung unverändert. Er verändert weder Paket noch Autorenfassung.

## Urteil für die Korrekturrunde 1

E-S01/E-R03 ist im beschriebenen sichtbaren Quellenumfang repariert. Die beiden zusätzlichen Schlusszeichen auf Liste 58 wurden entfernt; mein eigener frischer Originalrender zeigt an dieser Stelle keinen Punkt. Der originale Textlayerbeleg mit Punkt bleibt unverändert.

E-R01 ist für die ursprünglich beanstandeten vertauschten Fragebogenlabelobjekte und sichtbaren Listenwerte repariert. Alle 32 aktuellen Code-/Labelbindungen und alle 18 sichtbaren Listenfassungen stimmen mit meiner Originallektüre überein. Neue kohärente Vertauschungen scheitern am erweiterten Prüfer. Ein zusätzlicher geringer Befund E2-S01 betrifft die weiterhin ungeschützte Belegreferenz der sichtbaren Listenlesefassung, nicht deren derzeit richtigen Wortlaut.

E-R02 ist teilweise repariert und bleibt in Runde 1 offen. Der Prüfer verwirft einfache Kontextentfernungen und gemeinsam verfälschte Varianten-/Codebookfilter. Er akzeptiert aber zwei eigene Kandidaten, in denen der erforderliche Filter beziehungsweise die erforderliche Einleitung als tatsächlicher Kontext fehlen. Eine bloß als zweiter Beleg an den allgemeinen E-Einleitungstext angehängte Pflicht-ID genügt dem Vollständigkeitscheck. Das ist ein weiterer Gegenfall zur bereits beanstandeten Kontextvollständigkeit und kein zurückgesetztes oder neu nummeriertes E-R02.

Die aktuelle Quellenannotation bleibt im selbst gelesenen Umfang richtig. Der Anspruch, dass der Zusatzvertrag die Kontextvollständigkeit zuverlässig schützt, erhält wegen des mittleren Restbefunds `NICHT_BESTANDEN`. Dies ist keine empirische Inventar-, Messmodell-, Neutralitäts- oder Releaseabnahme.

## Eingaben, Trennung und Integrität

Vollständig gelesen wurden die eingefrorenen AGENTS, der Nacht-/Dauerauftrag, das gesicherte LIFE-93-Issue, Prüfregeln, Analyseplan, Analyseanforderungen, Lizenzen, beide E-Prüfaufträge, der vollständige ursprüngliche Autorenbericht, beide vollständigen v1-Erstberichte, die Annahmeentscheidung, der Korrekturbericht und der reine Zusatzcode. Beide vollständigen JSON-Fassungen wurden geladen. Alle Fragen wurden mit Wortlaut, Kontext, Kategorien, Listenobjekt, Codebookzuordnung und Antwortgegenstand ausgelesen. Die 808 Belege wurden im ausschließlich eigenen Validatorlauf vollständig gegen frisch gewonnene Originaltokens, Extrakte und Hashes geprüft. Eine anfänglich übergroße Metadatenausgabe war gekürzt; sie zählt nicht als vollständige Lesung. Die Metadaten und notwendigen Anforderungen wurden danach gezielt vollständig ausgegeben.

Hinzu kamen die vorgeschriebenen lokalen Dateien `docs/project.md`, `docs/belegregister.md` und `docs/entscheidungen.md` sowie die PDF- und unslop-Skills. Aktuelle andere Nachberichte, Loop-Findings, Agentlisten und zusätzliche Autorenverteidigung wurden nicht gelesen. Die erlaubten alten Berichte sind ausdrücklich Teil des eingefrorenen Nachprüfpakets. Die Autorenprovenienz beschreibt die Adoption des früheren Reviewercodes zutreffend als jetzige Autorenarbeit; daraus entsteht keine zusätzliche unabhängige Bewertung.

Alle 17 Paketdateien und alle 130 öffentlichen SourceInputs wurden vor und nach der Arbeit gegen SHA-256, Bytezahl, relative SafePaths, aufgelöste Zielpfade und erlaubten öffentlichen Pfadbereich geprüft. Alle 147 Pins und der Manifesthash stimmen. Die Typprüfung der 130 Inputs erfasste 30 öffentliche Dokumentationsannotation-JSON, 23 Audit-/Log-/Manifest-JSON, 12 PDF, 38 PNG, 12 HTML, sieben Python-, sieben Text- und eine Markdown-Datei. Dies ist eine begrenzte Quellen-/Artefaktkontrolle, keine allgemeine Inhaltsgarantie für das Repository. Die Quelleninputs enthalten in diesem Paket öffentliche Dokumentation, Extrakte, Renderings, synthetische Annotationen und Prüfprotokolle, keine ESS-Antwortdatei.

Der eigene vollständige Strukturvergleich der alten und neuen JSON ergibt genau fünf Änderungen:

| Art            | JSON-Pfad                                              | Tatsächliche Änderung                                                              |
| -------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Inhalt         | `/fragen/15/listenheft/sichtbare_kategorien_de/wert/2` | E12: ausschließlich Schlusszeichenpunkt entfernt                                   |
| Inhalt         | `/fragen/16/listenheft/sichtbare_kategorien_de/wert/2` | E13: ausschließlich Schlusszeichenpunkt entfernt                                   |
| Administration | `/korrekturprovenienz`                                 | Korrekturrolle, Umfang, Textlayergrenze und noch fehlende Nachprüfung dokumentiert |
| Administration | `/zugriffsgrenzen/loopFindingsRead`                    | `false` auf `true`, bezogen auf den korrigierenden Koordinator                     |
| Administration | `/zugriffsgrenzen/peerOrJurorReportsRead`              | `false` auf `true`, bezogen auf den korrigierenden Koordinator                     |

Alle 808 vollständigen Belegobjekte, alle übrigen Fragefelder und alle sieben vollständigen offenen Punkte sind strukturell identisch. Die alte JSON, beide Erstberichte, Originalpakete und Quellenbytes bleiben gehasht unverändert. Das technische Basis-CSV enthält 296 Zeilen und 32 E-Identitäten. Die gelesene Pending-Regel in `pipeline/inventar.py:610–628` ergibt 205 Zeilen. Dabei wurden ausschließlich öffentliche Inventarmetadaten geprüft. CSV, Provenienz, Parser und vorhandene AB-/C-/C-v2-Ergänzungen blieben unverändert; der eigene Schutzvergleich dokumentiert ihre Hashes. Diese anderen Module wurden nicht inhaltlich neu bewertet.

## Eigene Originallektüre

Die drei gepinnten öffentlichen Original-PDFs wurden bytegleich in meinen eigenen Ordner kopiert. Daraus entstanden neue Layout- und BBox-Extrakte sowie frische Renderings. Selbst gelesen wurden sämtliche Fragebogenseiten 43–54, sämtliche Listen 50–67 auf PDF-Seiten 51–68 und die relevanten E-Abschnitte auf sämtlichen Codebook-PDF-Seiten 208–218. Alle 41 Seiten wurden visuell und textuell gelesen. Der Standardrender nutzt `-scale-to 1700`; zusätzliche Ausschnitte betreffen Liste 58 und die E26-Tabelle. Es gab keinen eigenen neuen Netzabruf. Die Prüfung betrifft diese eingefrorenen Originalbytes.

| Quelle                      | Original-SHA-256                                                   | Eigene Fundstellen                                             |
| --------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------- |
| ESS11_questionnaires_DE.pdf | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` | PDF und gedruckte Seiten 43–54                                 |
| ESS11_showcards_DE.pdf      | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` | Listen 50–67, PDF51–68; hier keine eigene gedruckte Seitenzahl |
| ESS11_appendix_a7_e04_1.pdf | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` | PDF208–218, gedruckte Seiten jeweils eins darunter             |

Die Einzelabdeckung aller 32 Identitäten steht im eigenen `baseline-source-contract-result.json`: Originalfrageposition, Listennummer, Original-Codezeilenzahl und Pflichtkontextbelege. Diese automatisch geprüfte Tabelle wurde mit meiner gesamten visuellen und textuellen Originallektüre verglichen. Der Prüfer gewinnt die Codezeilen aus den gedruckten Fragekennungen und den tatsächlichen Code-Tokens; die Labelregion reicht links der konkreten Codezelle bis zur nächsten Codezeile. Leere Zwischenlabels bleiben leer. Die im Sourcevertrag festgelegten X-Grenzen und die mehrzeiligen Fortsetzungen passen zum gelesenen deutschen Tabellenlayout. Dieser technische geometrische Nachweis ist keine allgemein einsetzbare Semantikprüfung.

E1 druckt im Fragebogen 1, 2, 3 und 8. Liste 50 nennt „Möchte nicht antworten“ ohne numerischen Code. Der Zusatzvertrag erfindet dafür keinen Code. Codebook-PDF208 beschreibt die deutsche Anonymisierung; deren Umsetzung in Ausgabe 4.2 bleibt offen.

E2–E5 behalten ihre gemeinsame Selbstbeschreibungseinleitung und die bedingten Intervieweranweisungen. E6/E7 behalten getrennte Selbstwahrnehmungsfragen sowie die gedruckte zufällige Reihenfolgeanweisung. Ich habe deren Druck gelesen, kein CAPI-Programm oder tatsächliches Interviewprotokoll. Die Annotation behauptet keine ausgeführte Randomisierung.

E8M/E8W und E9–E11M/W behalten die richtigen deutschen Filter E1 = 1 beziehungsweise E1 = 2. Der gemeinsame E8-Zugang und die Einleitung auf DE46, die direkten Filter auf DE46/47 sowie die geerbten persönlichen Erfahrungsfilter auf DE47/48 stimmen. Codebook-PDF211 druckt für alle vier gemeinsamen Variablen die entsprechenden Variantenfilter. Die ergänzte feste Variante und der extraktgebundene Codebookfilter schließen die ursprüngliche gemeinsam falsche Zuweisung im getesteten Umfang aus.

E9–E11 drucken vier sachliche Erfahrungsalternativen sowie Sonderantworten 7/8. Kategorie 4 ist kein „Nein“, keine Skalenmitte und keine Verweigerung. Beim medizinischen Original bleibt das auffällige „oder habe versucht“ erhalten. Die englische Codebook-Kategorie nennt fehlenden Arztbesuch beziehungsweise Behandlungsversuch. Die gedruckte Referenz 86 ist sichtbar; ihr zugehöriger Erläuterungstext wurde in diesem Auftrag nicht aufgelöst. Beide offenen Grenzen bleiben ausdrücklich bestehen.

E12/E13 behalten die gemeinsame Einleitung zur aktuellen Lage in Deutschland und den Wechsel „AN ALLE“. E14 bleibt die allgemeine Polizeifrage. Die Codes 1/2/3 beschreiben zwei Richtungsangaben und Gleichbehandlung; der Zusatzvertrag bildet keine ordinale Einstellungsachse daraus. E15–E18 betreffen bewertete Gleichstellungsfolgen. E19–E22 betreffen konkrete Maßnahmen oder Sanktionen. Die vollständige E20-Vignette enthält Vollzeitarbeit beider Personen, ungefähr gleiches Einkommen, das neugeborene Kind und Anspruch beider auf bezahlte Elternzeit.

E23–E28 behalten die gemeinsame gesellschaftliche Einleitung, aber unterschiedliche Antwortgegenstände. E25-Lohnwahrnehmung, E27-Schutzforderung und E28-moralische Zuschreibung bleiben getrennt. E26 enthält die vollständige Definition von Liste 66, einschließlich verbalem, nonverbalem und körperlichem Verhalten. Die E26-Tabelle war in meiner ersten verkleinerten Mehrbilddarstellung nicht vollständig erkennbar. Der eigene 200-dpi-Einzelausschnitt zeigt alle Code-/Labelzeilen 1–5/7/8; der anfängliche Eindruck wird verworfen und begründet kein Finding.

Die sichtbaren Listenfassungen 50–67 stimmen mit den Originalrenderings überein. Doppelte oder versetzte Textlagen bei einigen Listen bleiben in den Roh-Tokens erhalten, während die Lesefassung jede sichtbare Kategorie einmal nennt. Das Codebook druckt Zwischenlabels als Ziffern und keine vollständigen Sonder-/Missingcodes in diesen Variablenabschnitten. Beides bleibt getrennt vom deutschen Fragebogen. `CanCalculateMean` wird nicht als fachliche Freigabe behandelt.

Der eingefrorene ESS-Abschnitt „Conditions of use“ und die gebundene HTML-Fassung wurden gelesen. Sie tragen die getrennten dokumentierten Daten- und Dokumentationslizenzen. Die JSON behält Attribution, Original-URLs, Ausgaben, Hashes und Bearbeitungshinweis. Die Prüfung bestätigt den eingefrorenen Quellenbefund, keine aktuelle rechtsfachliche oder konkrete spätere Veröffentlichungsfreigabe.

## Fortführung E-S01/E-R03: sichtbarer Punkt korrekt entfernt

Liste 58/PDF59 wurde vollständig und zusätzlich in einem eigenen 300-dpi-Ausschnitt gelesen. Die sichtbare dritte Kategorie endet mit „behandelt“ ohne Punkt. Die v2-Werte bei E12/E13 passen dazu. Der originale Beleg `SC-L58-page` endet weiterhin mit `behandelt.`; sein Extrakt-SHA-256 ist unverändert `10f7b86996e12b65eed6e6d8b313cfe5f34df03828a99104c64b38c08cadedd1`. Alle Tokens und Belegfelder sind gegenüber v1 gleich. Der Ursprung dieses PDF-Unterschieds bleibt unbekannt. Nachprüfung dieser konkreten Korrektur: `BESTANDEN`. Kein anderer Wortlaut wurde daraus redaktionell verändert.

## Fortführung E-R01: ursprüngliche Bedeutungsvertauschungen abgefangen

Die vollständigen ursprünglichen falschen Labelobjekte und vertauschten sichtbaren Listenwerte werden jetzt tatsächlich abgewiesen. Mein zusätzlicher Gegenfall tauscht die beiden vollständigen E14-Labelobjekte mit ihren echten Belegverweisen. Obwohl beide Extrakte für sich richtig bleiben, verwirft die konkrete Original-Codezeilenbindung den Kandidaten mit `E14: Labelbeleg gehört nicht zur Original-Codezeile 1`. Ebenso scheitert eine umgekehrte sichtbare Liste 64 bei E22. Die aktuelle Zuordnung aller 32 Identitäten und die 18 Lesefassungen sind richtig. Die ursprüngliche E-R01-Reparatur ist in diesem Umfang `BESTANDEN`; E2-S01 benennt unten eine gesonderte geringe Referenzlücke.

## Fortführung E-R02: fehlender Kontext lässt sich durch eine unbenutzte Pflicht-ID verdecken

Betroffene Aussage ist die behauptete Prüfung notwendiger direkter und übernommener Kontexte durch `e_semantic_contract_v2.py`. Originalfundstellen sind DE-Fragebogen47, E8W-Direktfilter `QCTX-E8W-filter`, sowie DE49, gemeinsame E12/E13-Einleitung `QCTX-E12-E13-current`. Beide stehen als tatsächlicher Originaltext im aktuellen Paket und wurden von mir selbst gelesen.

Der Zusatzcode sammelt in Zeilen 107–108 sämtliche Beleg-IDs sämtlicher Nicht-Listen-Kontexte und prüft lediglich, ob die Pflichtmenge darin vorkommt. Zeilen 109–111 vergleichen anschließend den Kontexttext nur mit dem jeweils ersten Beleg. Auch der erweiterte Ausgangsprüfer nutzt in `run-1/read-tests-v2.py:87–90` nur die erste Referenz für diesen Vergleich. Eine angehängte zweite Referenz kann deshalb die Pflichtmenge erfüllen, ohne dass ihr Filter- oder Einleitungstext irgendwo im Kontext vorhanden ist.

Zwei vollständige eigene Kandidaten wurden tatsächlich erzeugt und durch den gesamten erweiterten Prüfer, einschließlich aller 808 unveränderten Belegketten, akzeptiert:

| Kandidat                             | Tatsächliche Änderung                                                                                                         | Gesamter erweiterter Autorenprüfer |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `E8W-filter-absent-ref-padded`       | E8W-Direktfilterobjekt entfernt; dessen Pflicht-ID als zweiter Beleg am unveränderten allgemeinen E-Intro angehängt           | `AKZEPTIERT`                       |
| `E13-introduction-absent-ref-padded` | Gemeinsamen E12/E13-Einleitungskontext bei E13 entfernt; dessen Pflicht-ID als zweiter Beleg am allgemeinen E-Intro angehängt | `AKZEPTIERT`                       |

Die Kandidaten verändern weder Quellenbytes noch Originalbelege. Sie verlieren trotzdem die tatsächliche Filterbedingung beziehungsweise den aktuellen Deutschland-/Zweiersituationskontext. Der separate eigene Bindungscheck verwirft beide und akzeptiert die unveränderte v2-Basis. Hashes, vollständige Kandidaten und Deltas stehen im eigenen `own-countercases-result.json`; die zusätzlichen unabhängigen Fehlermeldungen stehen in `independent-binding-result.json`.

Wirkung: Ein späterer Schritt könnte aus einem grünen Lesetest fälschlich auf vollständigen Kontext schließen. Das verändert die dokumentierte Antwortpopulation oder den Antwortgegenstand. Die aktuelle JSON enthält diese Fehler nicht. Schwere bleibt mittel wie bei E-R02, weil der Schutz eine bedeutungstragende Kontextentfernung passieren lässt. Die reparierte einfache Entfernung ist kein ausreichender Abschluss des ursprünglichen Vollständigkeitsbefunds. Runde 1 bleibt erhalten.

Konkrete Korrektur: Pflichtkontexte an tatsächliche Kontextobjekte mit zugehörigem Originaltext und Geltung binden. In dieser Fassung hat jeder solche Kontext einen einzelnen Quellenbeleg; die Pflicht-ID muss diesen tatsächlichen Text belegen. Falls künftig mehrere Belege erlaubt werden, muss die Zuordnung jedes benötigten Textsegments ausdrücklich geprüft werden. Eine Mengenmitgliedschaft in unbenutzten Sekundärreferenzen reicht nicht. Eine gezielte Begrenzung des behaupteten Prüfumfangs bleibt möglich, erklärt diese Kontextvollständigkeit dann aber nicht für bestanden.

Nachprüfung: Beide erhaltenen neuen Kandidaten müssen scheitern. Direkte und geerbte Filter, E12/E13-Einleitung, „AN ALLE“, E6/E7-Anweisung, E20-Vignette und E26-Definition bleiben im Originalumfang erhalten. Alle 32 aktuellen Identitäten und alle 19 bisherigen Korrekturgegenfälle müssen weiterhin bestehen beziehungsweise erwartungsgemäß scheitern. Keine CAPI-Ausführung oder Webübertragung darf daraus behauptet werden. Urteil E-R02-Rest: `NICHT_BESTANDEN`.

## E2-S01: sichtbarer Listenwortlaut kann einen falschen Seitenbeleg tragen

Betroffene Aussage ist die Quellenbindung der sichtbaren Listenlesefassung. Originalfundstellen: Liste 64/PDF65 für E19 mit „Sehr dafür“ bis „Sehr dagegen“ und Liste 67/PDF68 mit „Stimme stark zu“ bis „Lehne stark ab“. Beide habe ich selbst visuell und textuell gelesen. Der richtige E19-Wortlaut ist im aktuellen Paket an `SC-L64-page` gebunden.

Der eigene Kandidat `E19-visible-card-evidence-from67` verändert ausschließlich `/fragen/22/listenheft/sichtbare_kategorien_de/belege/0` von `SC-L64-page` auf `SC-L67-page`. Der aktuelle sichtbare Wortlaut und alle Originalbelege bleiben unverändert. Der gesamte erweiterte Prüfer akzeptiert ihn. `e_semantic_contract_v2.py:112–114` prüft feste Position und Wortlaut, aber nicht die Referenz des sichtbaren Kategorienobjekts. Der vorherige Lesetest prüft den separaten vollständigen Seitenbeleg und den Header, ohne die abweichende Referenz dieses Kategorienobjekts zu erkennen.

Wirkung ist ein falscher konkreter Quellenverweis an einem richtigen Text. Ein Nutzer des Belegfeldes würde zu einer anderen Antwortskala geführt. Dies ist keine bereits falsche v2-Lesefassung und keine weitere empirische Fehlentscheidung. Schwere gering: Der Wortlaut und die Position bleiben vom Zusatzvertrag geschützt; der Nachweis am konkret exportierten Feld ist trotzdem falsch.

Konkrete Korrektur: Die Referenzen der sichtbaren Kategorien an die erwartete Showcardquelle, richtige PDF-Seite und den geprüften vollständigen Seitenbeleg binden. Für die gegenwärtige Struktur muss das sichtbare Kategorienobjekt dieselbe `SC-L<nummer>-page`-Referenz tragen wie sein vollständiger Seitenbeleg. Bei einer späteren Aufteilung braucht jedes Segment eine entsprechende Originalregion.

Nachprüfung: Der erhaltene Kandidat muss scheitern; alle 18 derzeit richtigen Listenfassungen samt ihren eigenen Belegreferenzen müssen bestehen. Der unabhängige eigene Bindungscheck weist den falschen Referenzfall ab und akzeptiert die unveränderte Basis. Kein Umformulieren der Listen oder Entfernen von Textlayergrenzen ist nötig.

## Ausgeführte Validatorläufe und Gegenfälle

Kein Originalbuilder und kein Originallesetest wurde an seinem Livepfad gestartet. Der vollständige erweiterte Lesetest wurde zuerst ganz gelesen, dann in meinen Ordner kopiert. Seine ROOT-/PUBLIC-/Importpfade wurden vor dem Import auf die eigene `scope-copy/`, die gefrorene Lesefassung und die eigene bytegleiche Zusatzmodulkopie gesetzt. OUT, BBox-Inputs, PDF-Caches, Kandidaten-/Logziele und Python-Bytecodeverhalten wurden vor der Ausführung dokumentiert. `sys.dont_write_bytecode = True`; kein Cache entsteht am Originalmodul. Der `__main__`-Block der Kopie wurde nicht gestartet. Sein `validate` wurde ausschließlich auf öffentliche JSON geladen und eigene beziehungsweise gefrorene synthetische Kandidaten angewandt.

Alle Kopier- und Schreibziele liegen unter `outputs/loop/inventory004-e-v2-sources/`. Die technischen CSV-/Provenienz- und PDF-Eingaben wurden bytegeprüft in die eigene Pfadkopie übertragen. Die eigene Kontrolle nennt ROOT, OUT, PUBLIC, Importpfad, BBox-Inputs und alle Kopien in `execution-path-preflight.json`. Diese Pfadkopie ist keine Betriebssystem-Sandbox.

Die unveränderte Basis besteht den vollständigen erweiterten Validator mit 32 Identitäten und 808 Quellenketten. Alle sieben alten und zwölf neuen gefrorenen Autorenkandidaten wurden zusätzlich erneut geladen, gehasht, tatsächlich gegen die Basis verändert gefunden und durch dieselbe ausschließlich eigene Kopie abgewiesen. Ergebnis: 19 von 19, `frozen-19-cases-recheck.json`. Diese Wiederprüfung erfindet keine neuen unabhängigen Autorenbauten. Zwei eigene vollständige Nachbauten wurden von diesem Quellenreviewer nicht ausgeführt und bleiben hier `NICHT_GEPRUEFT`; sie gehören zum getrennten Reproduktionsauftrag.

Meine acht zusätzlichen vollständigen synthetischen Kandidaten sind tatsächlich verändert. Fünf werden abgewiesen und drei akzeptiert:

| Eigener Gegenfall                                                          | Ergebnis und Bedeutung                                   |
| -------------------------------------------------------------------------- | -------------------------------------------------------- |
| E14 vollständige Labelobjekte samt Belegen getauscht                       | Abgewiesen an Original-Codezeile; E-R01-Schutz bestätigt |
| E8W Direktfilter entfernt, Pflicht-ID als Sekundärbeleg angehängt          | Akzeptiert; verbleibender E-R02-Fall                     |
| E13 gemeinsame Einleitung entfernt, Pflicht-ID als Sekundärbeleg angehängt | Akzeptiert; verbleibender E-R02-Fall                     |
| E19 sichtbare Kategorien auf Liste-67-Beleg verwiesen                      | Akzeptiert; E2-S01                                       |
| E11W gesamtes Listenobjekt durch E10W ersetzt                              | Abgewiesen am Originalheader                             |
| E22 sichtbare Liste-64-Reihenfolge umgekehrt                               | Abgewiesen an sichtbaren Listenlabels                    |
| E11M geerbten Filter entfernt                                              | Abgewiesen wegen fehlendem Pflichtkontext                |
| E9W Variante und Codebookfilter gemeinsam auf E1 = 1 verändert             | Abgewiesen am Originalvariantenfilter                    |

Zusätzlich unterscheidet mein separater Bindungscheck die unveränderte Basis von den drei akzeptierten falschen Kandidaten. Er verändert den Autorenvalidator nicht und erteilt keine allgemeine Selbstfreigabe. Die Tests suchen konkrete Fehler ohne Sollzahl oder gewünschtes inhaltliches Ergebnis.

## Statusgrenzen

| Prüfung                                                                  | Ergebnis dieses Berichts                                    |
| ------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Alle 17+130 Pins, SafePaths und begrenzter öffentlicher Scope            | `BESTANDEN`                                                 |
| Vollständiger Diff mit zwei Inhalts- und drei administrativen Änderungen | `BESTANDEN`                                                 |
| 808 Belege, übrige Fragefelder und sieben offene Grenzen erhalten        | `BESTANDEN`                                                 |
| Aktuelle deutsche Wortlaute, Code-/Labelzellen, Filter und Kontexte      | `BESTANDEN` im beschriebenen Originalumfang                 |
| 18 sichtbare Listenwerte einschließlich Liste 58                         | `BESTANDEN` im beschriebenen sichtbaren Umfang              |
| E-R01-Reparatur der ursprünglich falschen Bedeutungsbindungen            | `BESTANDEN` für diese Fälle                                 |
| E-S01/E-R03-Korrektur                                                    | `BESTANDEN`                                                 |
| E-R02-Reparatur der Kontextvollständigkeit                               | `NICHT_BESTANDEN`, mittlerer Restbefund in Runde 1          |
| Sichtbares Listenobjekt an seinen konkreten Beleg gebunden               | `NICHT_BESTANDEN` als Validatorumfang, geringer E2-S01      |
| 19 gefrorene Korrekturgegenfälle erneut wirklich abgewiesen              | `BESTANDEN`                                                 |
| Zwei eigene vollständige Neubauten                                       | `NICHT_GEPRUEFT` durch diesen Quellenreviewer               |
| Ausgabe 4.2, Anonymisierungsumsetzung, E1-Refusal-Mapping                | `NICHT_GEPRUEFT`                                            |
| Auflösung von E9-medizinischer Formulierung und Referenz 86              | `NICHT_GEPRUEFT`                                            |
| Tatsächliche CAPI-Ausführung                                             | `NICHT_GEPRUEFT`                                            |
| Eignung, Polung, Konstrukte, Neutralität, empirische Güte                | `NICHT_GEPRUEFT`, außerhalb dieses Auftrags                 |
| UI, Browser, Deployment, Merge und Release                               | `IN_DIESER_PHASE_NICHT_ERFORDERLICH` für diesen Nachbericht |

Die sieben unveränderten Restpunkte sind `OPEN-E-42`, `OPEN-E-ITEMURTEILE`, `OPEN-E-CAPI`, `OPEN-E1-REFUSAL`, `OPEN-E1-ANON`, `OPEN-E9-MEDICAL-WORDING` und `OPEN-E9-FOOTNOTE86`. Sie werden weder geschlossen noch als heute gescheiterte empirische Untersuchungen umgedeutet. Der Entwurf bleibt Entwurf.

## Modell, Werkzeuge, Befehle und Fehlläufe

Modell gemäß geerbtem Startauftrag: Codex `gpt-6.1-sol`, Reasoning `ultra`, keine Überschreibung. Interne Revision und nicht offengelegte Anbieter-/Modellvorgaben sind unbekannt. Das Angebot umfasst Shell/Datei- und Bildanzeigewerkzeuge, Web, Bildgenerierung, Computer Use, Zeit, MCP-/Ressourcen-/Pluginwerkzeuge, Zielverwaltung und Collaboration. Tatsächlich genutzt wurden `functions.exec` mit `exec_command`, `write_stdin`, `apply_patch` und `view_image` sowie `collaboration.send_message` für die operative Fortschritts-/Abschlussmeldung. Keine weiteren Agents wurden gestartet; keine andere Modellfamilie wurde eingerichtet oder beauftragt.

Jeder Shellaufruf nutzte den ausdrücklich gesetzten Worktree-CWD `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Alle Patchziele waren absolute eigene Worktreepfade. Die drei länger laufenden Python-Aufrufe wurden über ihre tatsächlichen `session_id` bis zum bestätigten Exit 0 abgeholt. Alle 48 anfänglichen Poppler-Aufrufe und der zusätzliche E26-Ausschnitt endeten mit Exit 0. Die vollständigen konkreten Poppler-Befehle, stdout/stderr und Exits stehen in `reading-command-log.json` beziehungsweise `E26-render-command.json`. Eigene Skripte und Ergebnisse bleiben über den Index gehasht erhalten.

Die substantiven Shellaufrufe waren:

| Aufruf                                                                                                    | Tatsächlicher Exit / Grenze                                                                                     |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `cat` der PDF-/unslop-Skills                                                                              | 0; vollständig gelesen                                                                                          |
| `rg -n '12axes\|INVENTORY-004\|LIFE-93' /home/stevenh/.codex/memories/MEMORY.md`                          | 1; keine Treffer, keine relevante Erinnerung verwendet                                                          |
| `cat` Manifest                                                                                            | 0; Ausgabe gekürzt, anschließend vollständige strukturelle Pinprüfung                                           |
| `cat` Projektstand, Belegregister, Entscheidungen und zunächst falsch angesetzte Paketpfade ohne `files/` | 1; zwei Pfade fehlten, danach richtige eingefrorene Pfade vollständig gelesen                                   |
| `cat` aller eingefrorenen Anforderungen, Berichte, Entscheidungen und Zusatzcode                          | 0; gekürzte Sammelausgabe von Analyseplananfang später gezielt vollständig gelesen                              |
| `python3 outputs/loop/inventory004-e-v2-sources/preflight.py pins-before.json`                            | 0; alle 17+130 Pins                                                                                             |
| `python3 outputs/loop/inventory004-e-v2-sources/read_originals.py`                                        | 0; 48 protokollierte Unterbefehle mit Exit 0                                                                    |
| Inline-Python: vollständiger Strukturvergleich und Auslesung aller 32 Fragen                              | 0; fünf Deltas und aktueller Originalvergleich                                                                  |
| Inline-Python: erste übergroße Metadatenauslesung mit falschem Schlüssel `belege` statt `belegregister`   | 1, `KeyError`; gekürzte Ausgabe nicht als vollständige Lektüre gewertet, gezielt korrigiert nachgelesen         |
| `cat` eigener Layout-Extrakte und des vollständigen erweiterten Lesetestcodes                             | 0; Originalseiten und Laufpfade gelesen                                                                         |
| Inline-Python: zusätzlicher E26-Renderbefehl                                                              | 0; voller Aufruf in eigenem Protokoll                                                                           |
| `python3 outputs/loop/inventory004-e-v2-sources/countercases.py`                                          | 0; Basis und acht eigene echte Kandidaten                                                                       |
| Inline-Python: Basisschutz und öffentliche technische 296/205-Zählung; `sed` der Pending-Regel            | 0; kein Antwortdatenzugriff                                                                                     |
| `python3 outputs/loop/inventory004-e-v2-sources/recheck_frozen_cases.py`                                  | 0; 19 echte gefrorene Gegenfälle abgewiesen                                                                     |
| Inline-Python: erster Dateityp-Scopecheck                                                                 | 1, `ValueError` für die erlaubte `plan.md`, weil `.md` zunächst in der Typ-Allowlist fehlte; kein Quellenfehler |
| Inline-Python: Scopecheck mit ausdrücklich hinzugefügtem Markdown-Typ                                     | 0; alle 130 Inputs erfasst                                                                                      |
| Inline-Python: vollständige JSON-Metadaten und Liste-58-Rohbeleg                                          | 0; korrigierte, begrenzte Ausgabe                                                                               |
| `nl -ba`/`sed` der konkreten Validatorfundstellen und vollständige SourceInput-Pfadliste                  | 0                                                                                                               |
| `python3 outputs/loop/inventory004-e-v2-sources/independent_binding_checks.py`                            | 0; Basis akzeptiert, drei falsch gebundene Kandidaten abgegrenzt                                                |
| `python3 outputs/loop/inventory004-e-v2-sources/preflight.py pins-after.json`                             | 0; alle Pins unverändert                                                                                        |

Der eigene Index und das Abschlussprotokoll halten die tatsächlich ausgeführten individuellen Formatbefehle und abschließenden Hashvergleiche fest. Die Formatprüfung hebt Ignorepfade explizit mit `--ignore-path /dev/null` auf und verarbeitet ausschließlich ausdrücklich benannte eigene Dateien. Kandidatenbytes werden nach den Mutationstests nicht formatiert. Ein Exit auf ignorierten Pfaden wird nicht als Formatnachweis ausgegeben. Kein Gesamtformatlauf und kein `pnpm check` wurden gestartet; der engere Nachprüfauftrag untersagt beides.

Es gab keine Installation, globale Änderung, Commits, Pushes, UI-Arbeit, Auth-/Cookie-/Storage-Aktion oder Portal-Analysis. ESS-Rohdaten, `data/local/`, Personenkennungen, A/B-Antwortdaten, Partei-/Links-Rechts-Antwortwerte, Verteilungen und Zugangsdaten wurden nicht gelesen oder ausgegeben. Meine synthetischen Kandidaten enthalten nur öffentliche Dokumentationsannotation. Die gemeinsamen Forschungsartefakte und Erstbewertungen bleiben unverändert.

Die Rollen sind frisch und organisatorisch getrennt; das Shared Filesystem bietet keine technische Zugriffssperre. Alle Urteile beziehen sich auf die kontrollierten Dateihashes. Dieser Quellen-/Inhaltsreview gehört zu einem KI-Audit derselben Codex-Familie. Er ist kein akademisches Peer Review, keine Prüfung durch eine andere Modellfamilie und keine Garantie von wissenschaftlicher Gültigkeit, Neutralität oder Biasfreiheit.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger Quellen-/Inhalts-Nachprüfer INVENTORY-004-E/v2, keinAutor und bislang unbeteiligt. Ausschließlich Worktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, Shellworkdir explizit, apply_patchABSOLUT. Paket reports/loop/packages/INVENTORY-004-E/v2/manifest.json SHA e1e184883b5f2ca04f729b2c2383777070601af6eba049c72e040aa1e1f56ca2,17files130sourceInputs. Vollständig gefrorene AGENTS/Issue/Nachtauftrag/Prüfregeln/Analyseplan/Anforderungen/Lizenzen/Prüfaufträge/beidevollständigenv1Erstberichte/Annahmeentscheidung/Korrekturbericht/neueJSON/PureZusatzcode lesen. Keine aktuellen anderenNachberichte/Loopfindings/Agentlisten/Verteidigung, keine weiterenAgents. E-S01/E-R03Runde1 an eigener frisch gerenderterOriginalListe58PDF59 visuell selbst prüfen: zwei sichtbareSchlusspunkteentfernt,原originalTextlayerbelegunverändert. E-R01/R02 ergänzterCode sourcezellen-Code/LabelGeometrie, erforderlicheKontexte/Filter,Codebookfilterbeleg+Variante,18sichtbareLesefassungen tragen dieReparatur? Alle32OriginalFragebogenCode-/Labelzellen undKontexte anDEQ43–54,18Listen50–67PDF51–68,CodebookE208–218 selbsttextlich+visuellrelevantlesen. AdoptiertReviewerCodeistnunAutorenarbeitkeinweiterunabhängigerReview. SichtfassungTextlayergrenzen, E9MedicalOriginalCode4/Footnote86imPaketoffen/E1Anonymisierung/keinCAPIvollzogennichtumdeuten. Nur eigene neue Quellen/Gegenfälle outputs/loop/inventory004-e-v2-sources/, vollständiger unveränderlicher Nachbericht reports/loop/reviews/INVENTORY-004-E-v2-sources.md. Alle17+130Pins/SafePath/PublicscopeVorNach, kompletterDiff genau2Inhalt+3Adminpfade;808Belege/anderenFragefelder/7offeneGrenzen unverändert. Eigene konkrete kohärente LabelBeleg-/FilterKontext-/ListeGegenfälle gegenüberSourceContract wennsinnvoll; keineSollbeanstandung/Quote. Originalbuilder/Lesetests nieanLivepfadenstarten; Ownkopien alleROOTOUTPUBLICLogsCachesMutationen preflight bevorStart. Eignung/Polung/Neutralität/Konstrukt/4.2/empirischesInventar nichtAuftrag, späteresNICHTGEPRUEFTnichtempirischgescheitert. KeineESSraw/local/Personen/DesignoderAntwortzeilen/A/B/PartyLR/Verteilungen/PortalAnalysis/AuthCookieStorageCredsSecrets/globalWrites/InstallConda/CommitPush/Gesamtformat/pnpmcheck/weitereAgents. ExistingEFindingsRunde1fortführen, neueE2-SxxpräziseAussageProblemBelegFundstelleWirkungbegründeteSchwerekonkreteKorrekturNachprüfung. PDF/unslopSkillsvorAnwendunglesen, indivFormatnurwirklichverarbeitetcounts. TatsächlichenvollständigenAuftragwortgetreu/Toolsangebot+NutzungCommandsExitsFehlläufe/Modellgpt-6.1-solultra geerbtInternUnknownSharedFSkeineSandbox dokumentieren. GleicheCodexfamilieKI-AuditkeinakademischesPeerReview/Garantie. AlleForschungsartefakteundErstbewertungenimmutable. AbschließendReportSHA+OwnIndexmelden.
```
