# DESIGN-003: unabhängiger Quellenreview, Erstbericht

Reviewer: /root/design003_sources. Datum: 2026-10-03. Dieser Erstbericht bleibt unverändert. Korrekturen und Nachprüfungen benötigen neue Artefakte.

Der Quellenabgleich des eingefrorenen Pakets ist **NICHT_BESTANDEN**. Zehn der elf eng gefassten Aussage-IDs stimmen mit den kontrollierten Originalstellen überein. D-DE-010 ist falsch: Sachsen steht sowohl im gebundenen deutschen Portaltext als auch im unabhängig neu geöffneten Original. Zusätzlich widerspricht die Quellenzuschreibung in P07 des Methodenentwurfs der richtigen Abgrenzung in D-DE-005. Es liegen zwei Findings mittleren Schweregrads vor. Das Urteil betrifft diese Quellenakte, keine empirische Analyse, Phasenabnahme oder Freigabe des Projekts.

## Prüffassung und Integrität

Geprüft wurde ausschließlich DESIGN-003/v1, Manifest SHA-256 `adc655d01e9cb538d091ba6d7810dfe5212353b4fc39e8e98c5e07f35759cad1`, Code-Commit laut Manifest `60414205eba970c5832e8ad130bb43215f0a7da6`. Dieser Commit wurde nicht als alleiniger Integritätsnachweis behandelt.

Die eigene Kontrolle vom 07:08:31.884834 UTC und vom 07:16:23.620246 UTC umfasst zwölf eingefrorene Paketdateien, ihre zwölf Originaldateien und 43 ausdrücklich öffentliche SourceInputs. Alle 67 Datei-/Byte-/Hashvergleiche stimmen in beiden Durchgängen. Vorher-/Nachher-Einträge sind identisch. Relative Eingabepfade, Auflösung innerhalb des Worktrees, reguläre Dateien und sämtliche Pfadkomponenten wurden geprüft; keine Symlinks oder Pfadausbrüche. Die Manifest-Prüfsumme stimmt ebenfalls zweimal.

Belege im eigenen Outputordner:

| Artefakt | SHA-256 |
| --- | --- |
| integrity-before.json | be4a5c20270bc45eb80ec87a61a509d5027101d6fa082213a0ab24a3c101c7b7 |
| integrity-after.json | f776af50cddbb3be91caa60b320eb5e7d5b6f5de3b9959544ba8fc09354a30af |
| source-access-independent.json | 093d478190485dcea9b9e47750915f87517bd2b4ce3376b71242a1e28d943308 |
| germany-independent.json | 20760f3b335d2ecaacad5bb26b4fa9fbff2cabe53125595b9c3c540a72ea894e |
| universe-independent.json | eacc939066557f025f1544c8d688d5cdd45ed3157005008ce4b0565c1caac685 |
| documents-independent.json | 7ac359a567b0c4d35cc87d7d55aaa7f7873820cdb91eca7c29dc1987d7331396 |
| render-log.json | f5ef1603282ba818e496b2bbd193b39bd29eecc2f848a041212864e11e6c0e8e |

Alle genannten relativen Outputnamen beziehen sich auf `outputs/loop/design003-sources/` im beauftragten Worktree. Maschinenlesbare Einzelurteile stehen in `claim-results.json`. Der abschließende Outputindex bindet auch Skripte, Textableitungen, Raster und diesen Bericht.

## Tatsächlicher Lesebereich

Alle zwölf gefrorenen Dateien wurden gelesen: AGENTS.md, project.md, dauerhafter Auftrag, gespeicherter Issue, Prüfregeln, Analyseanforderungen, Lizenzakte, Methodenentwurf, Deutschland-Designakte, das Register der elf Aussagen, Quellenbericht und Prüfauftrag. Das eingebettete Register und Quellenbericht wurden anschließend ausdrücklich aus der gefrorenen Fassung nachgelesen. Einige erste Textlektüren betrafen die Originalpfade; die eigenständige Hashkontrolle bestätigt deren Übereinstimmung mit der gefrorenen Fassung.

Die Original-PDFs wurden selbst von ihren offiziellen URLs erneut abgerufen und selbst mit pdftotext extrahiert. Alle fünf HTTP-Abrufe erhielten Status 200, alle fünf Extraktionen Exit 0. Jeder erneute PDF-Hash ist bytegleich mit seinem gefrorenen SourceInput. Der Codebook-Befund hängt damit nicht mehr allein von der Cachebeschreibung des Autors ab.

| Original | Edition und selbst gelesene Bereiche | Eigener erneuter Abrufbeginn UTC |
| --- | --- | --- |
| [Country Documentation Report](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_country_documentation_report_e04.pdf) | 4.0. Titelseite und Versionsnotiz PDF4 nennen die Edition und Veröffentlichung am 19.11.2025. Deutsches Kapitel PDF/gedruckt79–88 vollständig textlich gelesen. | 07:09:47.437195 |
| [Guide to Using Weights and Sample Design Indicators](https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf) | V1.2, 06.07.2023. Titelseite; §§2–4.3, PDF4–10 / gedruckt2–8, vollständig im behaupteten Bereich. | 07:09:48.089984 |
| [ESS11 Sampling Guidelines](https://www.europeansocialsurvey.org/sites/default/files/2023-06/Round-11-ESS-sampling-guidelines_0.pdf) | 04.07.2022. Titelseite; §1.2 PDF3–4 / gedruckt2–3, §1.3 PDF5/4, §3.2 PDF13–14/12–13, §3.3 PDF14–15/13–14; Annex2 PDF24–29/A2-1–A2-6. | 07:09:48.256672 |
| [ESS11 Data Protocol](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/source/ESS11_data_protocol_e01_5.pdf) | 1.5, Oktober2023. Titelseite; B5/B5.1 PDF/gedruckt12 und F4.1/F4.2 PDF/gedruckt95–96. | 07:09:48.539007 |
| [ESS11 Appendix A7 Codebook](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) | 4.1. Titelseite; PDF484/gedruckt483, PDF551–552/gedruckt550–551. | 07:09:49.132556 |

Die jeweiligen vollständigen Original-Hashes stehen im gefrorenen Manifest und im eigenen Abrufprotokoll. Es wurde keine vollständige allgemeine Lektüre aller fünf Dokumente behauptet.

Neunzehn Seiten wurden neu aus den unabhängig abgerufenen PDFs gerendert und tatsächlich über view_image visuell gelesen: Country79/80/86; Weights6/7/10; Guidelines4/5/13/14/15/25/28; Protocol12/95/96; Codebook484/551/552. Alle neunzehn pdftoppm-Aufrufe erhielten Exit0. Insbesondere wurden der mehrspaltige Protocol-Widerspruch, die Annex2-Randnotiz, das konkrete R-Beispiel und der Sachsen-Katalogeintrag visuell gelesen. Reiner Textextrakt oder vorhandenes Autorenraster ersetzte diese Kontrolle nicht.

## Eigenständige Portalprüfung

Ein neuer T3-Hintergrundtab `tab_j` öffnete die [öffentliche ESS11-Studienseite](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b). Geöffnet wurden ausschließlich die sichtbaren Abschnitte Universe, scope and method, Country documentation mit Germany-Dialog und Documents. Der Studienseite bereits sichtbare Datafiles-Bereich wurde als Link-/Versionsliste gelesen; kein Datafile-Link wurde geöffnet.

Der Germany-Dialog wurde über die beobachtete Germany-Tabellenzeile geöffnet. Sein vollständiger gerenderter Text wurde aus dem öffentlichen Dialog-DOM gelesen, gespeichert und mit dem gebundenen Autorcapture verglichen: exakt gleich. Der Samplingabschnitt, Modus/Feldzeit und die vollständige Geographical-unit-Liste wurden zusätzlich in tatsächlichen T3-Screenshots visuell gelesen. Die Screenshots wurden im Tool gesehen, nicht außerhalb des erlaubten Outputordners gespeichert.

Der genaue Listenvergleich liefert fünfzehn separate Einträge. Sachsen steht einmal als eigener Eintrag darin, Sachsen-Anhalt ebenfalls einmal. Bremen steht in dieser Liste nicht. Der Zähler trennt ganze Listenelemente; er leitet Sachsen nicht aus dem Teilwort in Sachsen-Anhalt ab. Dies ist ein Befund über zwei öffentliche Metadatenfassungen. Er belegt weder eine reale sächsische noch eine reale bremische Stichprobenlücke.

Die sichtbaren Dokumentlinks nennen CountryReport4.0, Codebook4.1 und DataProtocol1.5. Die sichtbare Hauptdatei ist als Edition4.2 bezeichnet. Die allgemeine Studien-DOI und Capturezeiten liefern hier keine unveränderliche Revision des dynamischen Germany-Textes. Gleichheit der Texte und Hashes ist ein überprüfbarer Aufnahmebefund, kein Autoritäts- oder Vollständigkeitsbeweis für alle gegenwärtigen Metadaten.

## Einzelurteile für die elf Aussagen

BESTANDEN bedeutet in dieser Tabelle ausschließlich: die konkrete Aussage stimmt im genannten Geltungsbereich mit den tatsächlich kontrollierten Originalstellen überein.

| Aussage-ID | Urteil | Originalfundstelle und Ergebnis | Grenze |
| --- | --- | --- | --- |
| D-DE-001 | BESTANDEN | Öffentliche Studie, Universe. Alter ab15 und Privathaushalte sowie Unabhängigkeit von Staatsangehörigkeit werden ausdrücklich genannt. | Deklarierte Zielpopulation; tatsächliche Registerabdeckung und deutsche Sprachzugänglichkeit wurden nicht untersucht. |
| D-DE-002 | BESTANDEN | Germany / Sampling procedure. Kommunale Personenregister; in den fünfzehn größten Gemeinden direkt systematisch und ungeclustert ausgewählte Personen, proportional nach Gemeinde geschichtet; im Restland166 Gemeinden als PSUs per PPS nach Bevölkerung15+, danach zufällig gleich viele Personen je gezogener Gemeinde. | Kein Zurücklegen-/Paarwahrscheinlichkeitsnachweis, keine exakte integrierte4.2-Kodierung. Die knappe Gesamtbezeichnung zweistufig darf den konkret einstufigen ersten Domänenteil nicht verdecken. |
| D-DE-003 | BESTANDEN | Country79/80 und Germany / Mode of collection/Data collection period. Feldzeit09.05.–21.12.2023; persönlicher Interviewmodus, Portal präzisiert CAPI/CAMI. | CAMI ist hier das mobile Eingabegerät der Interviewperson. Daraus folgt keine Selbstausfüllung und keine Äquivalenz zum späteren Webtest. |
| D-DE-004 | BESTANDEN | Country86: NUTS1, regionale Inferenz dort verneint; nationale Gruppierung empfohlen, Bundeslandrepräsentativität ausdrücklich verneint. | Der vorgeschlagene begrenzte Domänenweg ist eine eigene zu prüfende methodische Alternative. Die Quelle gewährt dafür keine pauschale Freigabe. |
| D-DE-005 | BESTANDEN | Weights§3 PDF6/4 empfiehlt anweight; §4.1 PDF7/5 beschreibt integrierte Indikatoren; §4.3/Box5 PDF8–10/6–8 enthält psu/stratum/anweight und keine FPC-, Paarwahrscheinlichkeits- oder nest-Spezifikation. | Keine Bestätigung des geplanten Splits, ordinalen Messmodells oder einer konkreten Intervallabdeckung. P07-Zuschreibung bleibt FindingD-S02. |
| D-DE-006 | BESTANDEN | Guidelines§1.3 PDF5/4 verlangt den SDS-Detailteil je Samplingdomäne; §3.3 PDF14–15/13–14 trennt explizite unabhängige Auswahl je Schicht und implizite systematische Auswahl aus geordneten Listen; Annex2 PDF25/A2-2 und28/A2-5 präzisiert Stufen und unterschiedliche Domänendefinitionen. | Allgemeines Dokument und unausgefülltes Formular; keine deutsche Zuordnung von numerischen integrierten Feldern. |
| D-DE-007 | BESTANDEN | Protocol95, psu-Zeile, fordert PSU=idno für einstufige Designs; Example1 auf96 nennt psu unter den für alle Records leeren Feldern. Beide Seiten enthalten tatsächlich diese Aussagen. | Generischer SDDF-Depositwiderspruch. Keine Aussage darüber, welche deutschen integrierten Werte verarbeitet wurden oder fehlen. |
| D-DE-008 | BESTANDEN | ProtocolB5/B5.1 auf12 nennt nicht öffentliche, nicht anonyme SDDF-Deposits; Weights§4.1 auf7/5 nennt veröffentlichte integrierte Designindikatoren abRunde9. | Die Unterscheidung folgt aus dem Abgleich beider Quellen, nicht aus einer ausdrücklichen Vergleichspassage nur in B5. Keine pauschale Lizenzbehauptung. |
| D-DE-009 | BESTANDEN | Codebook551–552/550–551 benennt domain/prob/stratum/psu und numerische Typen, ohne dort einen deutschen Domänen-Crosswalk oder verarbeitete Kodierungsableitung zu geben. | Aussage über genau diese Seiten der Edition4.1; keine Abwesenheitsaussage über sämtliche anderen Dokumente oder Prüfung der Datei4.2. |
| D-DE-010 | NICHT_BESTANDEN | Germany / Geographical unit enthält Sachsen ausdrücklich, sowohl im gebundenen Capture als auch im eigenen neuen Original; Codebook484/483 enthält DED Sachsen. | Der behauptete Gegensatz fehlt bereits innerhalb der eingefrorenen Quellenakte. FindingD-S01. |
| D-DE-011 | BESTANDEN | Eigener Documents-DOM und sichtbare Datafiles-Liste bestätigen Dokumenteditionen4.0/4.1/1.5 neben Hauptdateilabel4.2. | Link-/Dokumentbefund, keine Prüfung der Hauptdatei oder ihrer Kategorien. Verschiedene Editionsnummern allein beweisen keinen Fehler. |

## Findings

### D-S01 — D-DE-010 widerspricht dem gebundenen Originaltext

**Schweregrad MITTEL.** Der Tatsachenfehler betrifft einen eigenen publizierbaren Quellenbefund und sein Warnsignal für regionale Analysen. Er muss vor Abnahme der Quellenakte korrigiert werden. Eine hohe Schwere durch bereits erfolgte falsche Datenausschlüsse wäre unbelegt: Der Entwurf behauptet selbst keine reale Stichprobenlücke und hier wurde keine Analyse durchgeführt.

Betroffen sind das gefrorene Register `data/design-quellen.entwurf.json:159`, `docs/design-deutschland.entwurf.md:17` und `reports/loop/authors/DESIGN-003.md:11`. Die Aussage lautet, die deutsche Geographical-unit-Liste nenne Sachsen-Anhalt, aber kein Sachsen.

Das Original `outputs/loop/design003/germany-modal.json`, gebunden mit SHA-256 `206891436109a642cdfb9a1d012c615ed67a8bb94c7e819442308698f7a5271c`, enthält Sachsen als eigenes Listenelement. Mein unabhängiger neuer Germany-Dialogtext ist mit dem eingefrorenen Text exakt identisch. Die gesamte Liste wurde auch visuell kontrolliert. Der Codebook-Eintrag DED Sachsen auf PDF484/483 ist richtig, erzeugt damit aber keinen Gegensatz zur Portal-Liste.

Die Wirkung ist ein erfundenes regionales Warnsignal, das als belastbare neue Evidenz erscheint und weitere Gegenprüfung auf die falsche Region lenkt. Die defensive Einschränkung „kein Beweis einer Stichprobenlücke“ heilt den falschen Ausgangsbefund nicht.

Korrektur: D-DE-010 und alle sachlichen Wiederholungen in einer neuen Fassung berichtigen. Die Ausgangsfassung und der Erstbericht bleiben erhalten. Falls das tatsächlich fehlende Bremen als Metadatenauffälligkeit untersucht werden soll, braucht dieser neue Befund eine eigene genaue Gegenquelle und eigene Reichweite. Aus der Listenlücke allein weder fehlende Befragte noch einen zulässigen Crosswalk folgern.

Nachprüfung: Neue Aussage gegen die vollständig gespeicherte Originalliste und einen erneuten öffentlich geöffneten Germany-Dialog prüfen; exakte Tokenzählung und visuelle Kontrolle wiederholen. Wiederholungen in Designakte, Register und zugehörigem neuen Quellenbericht auf dieselbe geprüfte Aussage bringen. Keine Antwortdaten nötig.

### D-S02 — P07 bezeichnet eine eigene Ergänzung noch als ESS-Empfehlung

**Schweregrad MITTEL.** Die Quellenzuschreibung eines geplanten Varianzverfahrens ist innerhalb des Prüfpakets widersprüchlich. Das Finding belegt keinen Rechenfehler und erklärt nest=TRUE nicht als fachlich unzulässig. Es blockiert die Abnahme dieser Zuschreibung, keinen bereits geprüften Survey-Lauf.

Betroffen ist `docs/analyseplan-methoden.entwurf.md:87`, P07, Primärvorschlag. Der vollständige svydesign-Aufruf einschließlich nest=TRUE wird dort als „offizielle ESS-Empfehlung“ bezeichnet. Demgegenüber kennzeichnen D-DE-005 und `docs/design-deutschland.entwurf.md:9` nest=TRUE ausdrücklich als eigene Zusatzoption.

Die Originalfundstelle ist [WeightsV1.2, Box5, PDF10/gedruckt8](https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf). Das R-Beispiel enthält ids, strata, weights und data, ohne nest-Argument. Es wurde selbst extrahiert und visuell gelesen. Auch FPC und PPS-Paarwahrscheinlichkeiten stehen nicht im Originalbeispiel. Das Original nennt in dieser Box den hier verwendeten Namen „Ultimate-PSU-Taylor-Approximation“ ebenfalls nicht; diese methodische Einordnung ist von der wörtlichen ESS-Spezifikation zu unterscheiden.

Die Wirkung ist ein unzutreffender Autoritätsanspruch für eine Implementierungsoption. Bei späterer Übertragung aus P07 kann der Unterschied zwischen Quellenempfehlung und eigener begründungsbedürftiger Entscheidung wieder verloren gehen.

Korrektur: P07 in einer neuen Methodenfassung an D-DE-005 angleichen. Die originale ESS-Basisspezifikation, die eigene nest-Option und die methodische Einordnung/Approximation getrennt benennen. Falls nest gewählt wird, seine konkrete Anwendung und Voraussetzungen separat nachweisen. Das Finding verlangt weder pauschale Entfernung der Option noch einen Softwarelauf mit echten Daten.

Nachprüfung: Neue P07-Passage mit dem gesamten Box5-Original und dem Register vergleichen; keine Formulierung darf nest oder die zusätzlichen methodischen Begriffe als dortigen Originalwortlaut darstellen. Eine spätere eigene Implementierungsprüfung bleibt ein getrennter Nachweis.

## Welche Grenzen sachlich tragen

Die zwei deutschen Samplingdomänen sind Auswahlwege. Spätere Wählergruppen, Ost/West oder andere Auswertungsgruppen sind analytische Domänen. Aus der Existenz des numerischen Feldes domain lässt sich ohne passenden deutschen Crosswalk keine konkrete Zuordnung ableiten. Ebenso dürfen die fünfzehn großen Gemeinden nicht allein wegen ihrer Gemeindezugehörigkeit zu fünfzehn gezogenen Clustern erklärt werden: Der öffentlich dokumentierte Weg wählt dort Personen direkt und ungeclustert aus.

Der PPS-Weg im Restland belegt die Größenbasis15+ und gleiche Personenzahl je ausgewählter Gemeinde. Er belegt in den kontrollierten Stellen nicht die genaue PPS-Algorithmusvariante, Zurücklegen, Paarwahrscheinlichkeiten, alle Schichtungsmerkmale oder die verarbeitete4.2-Feldkodierung. Die hier mögliche Einsicht endet an der Dokumentation, nicht an irgendwelchen aus Daten abgeleiteten PSUs.

Guidelines§1.2 und Annex2 begründen, dass ein endgültiger SDS die tatsächlich durchgeführten Auswahlwege beschreibt. Weights§4.1 sagt zugleich, dass notwendige Indikatoren in integrierten Dateien bereitgestellt werden. Ein vollständiges nicht öffentliches SDDF-Deposit ist deshalb keine aus diesen Quellen ableitbare allgemeine Zugangsvoraussetzung jeder Sekundäranalyse. Für den eigenen Cluster-/Personensplit P03 braucht das Projekt allerdings eine passende, belegte Zuordnung der verarbeiteten Felder zu seinen zwei Auswahlwegen. „SDS oder gleichwertige Dokumentation der verarbeiteten Indikatoren“ ist eine vertretbare offene Anforderung; ausschließlicher Zwang zu einem nicht verfügbaren Originaldeposit wäre überstreng.

Ebenso braucht eine autoritative Dokumentation der tatsächlichen verarbeiteten deutschen Einstufenindikatoren nicht zwingend jede widersprüchliche generische Protocol-Passage historisch zu reparieren. Sie muss den konkreten Übertrag belegen. Die offene Anforderung zum Protocol-Widerspruch sollte entsprechend verstanden werden. Die vorliegende Akte liefert diesen konkreten Übertrag noch nicht, daher wurde keine integrierte Einstufen-PSU-Kodierung angenommen.

Die fehlende FPC im offiziellen Beispiel ist ein Merkmal der dokumentierten Basisspezifikation. Sie macht diese Standardapproximation für sich allein nicht unzulässig. Sie belegt umgekehrt auch nicht jede gewünschte exakte Varianz oder deren Abdeckung im konkreten deutschen Design. Die eigene Verfahrenswahl und Reichweite bleiben prüfpflichtig. Ein pauschaler Bedarf an sämtlichen Paarwahrscheinlichkeiten schon für jede Guide-Auswertung wäre durch dieses Beispiel nicht gestützt.

Die Quelle legt keine A/B-Aufteilung, keine ordinal gewichtete Faktorenanalyse und kein individuelles Fehlermodell fest. Zusätzliche Voraussetzungen für P03/P04 und die konkreten späteren Ziele von P07 sind daher sachlich von der einfachen Guide-Anwendung zu unterscheiden. Die vorhandenen synthetischen Befunde wurden nicht nachgerechnet und gelten hier nicht als Realdesignnachweis.

Die nationale Empfehlung in Country86 trägt eine sichtbare Einschränkung für Bundeslandrepräsentativität. Sie ist kein unmittelbarer Nachweis eines pauschalen Verbots jedes größeren, vorab begründeten Domänenkontrasts. Ebenso ist eine beliebige eigene Ost/West-Auswertung dadurch nicht freigegeben. Offizieller Regionsbezug, Anonymisierung, Design und konkrete zulässige Aussage müssen später passend geprüft werden.

## Nicht geprüft und Vermutungen

NICHT_GEPRÜFT bleiben sämtliche tatsächlichen ESS-Antwort-/Designzeilen, Personenkennungen, A/B, Partei-/Selbsteinstufungswerte, Item-/Gruppenverteilungen, die Hauptdatei4.2 und ihre verarbeitete Kodierung. Hier wurde keine endgültige Verfahrenswahl vorgenommen, kein Split gebildet und keine empirische Analyse ausgeführt. EFA/CFA, Reliabilität, Intervallabdeckung, persönliche Messunsicherheit, regionale oder Gruppenpräzision sind weder bestanden noch durch dieses Audit als gescheitert erklärt.

Die zusätzlichen Fachquellen L-METH-003 bis L-METH-017 des Methodenentwurfs wurden in diesem engen Quellenauftrag nicht eigenständig geprüft. Die Lizenzakte wurde als gefrorene Anforderung gelesen; eine neue rechtsfachliche oder aktuelle vollständige Lizenzprüfung wurde nicht durchgeführt. D-DE-008 ist nur der nachgeprüfte Unterschied zwischen Deposit und bereitgestellten integrierten Indikatoren.

Die originale Abrufhistorie des Codebook-Caches und der genaue ursprüngliche Protocol-Abrufzeitpunkt sind aus den gebundenen Metadaten nicht vollständig rekonstruierbar. Die neue eigene Abrufserie belegt unabhängige Erreichbarkeit, Editionen und Bytegleichheit zu ihren erfassten Zeitpunkten. Sie datiert den ursprünglichen Abruf nicht nachträglich.

Warum Bremen in der Portal-Liste nicht steht, ist unbekannt. Ein redaktioneller Fehler, ein Metadatenprozess oder eine andere Erklärung sind bloße Möglichkeiten. Sie werden hier nicht zu Findings über reale Teilnahme oder Abdeckung. Die tatsächliche verarbeitete Einstufen-PSU-Kodierung bleibt ebenfalls unbekannt; keiner der zwei generischen Protocol-Wortlaute erhielt durch Vermutung Vorrang.

Das Fehlen eigener Rohdatenzugriffe ist für diesen Reviewer belegt durch die ausgeführten beschränkten Befehle und Toolzugriffe. Vollständige historische Prozesskontrolle sämtlicher Autorenaktionen wurde nicht behauptet; deren Berichtsangaben wurden nicht mit privaten oder kompletten Sitzungshistorien überprüft.

## Unabhängigkeit, Modell und Werkzeuge

Der Reviewer startete als bislang unbeteiligter Subagent mit dem begrenzten Prüfauftrag. Keine aktuellen Peerberichte, Loopfindings, Agentlisten oder zusätzliche Autorenverteidigung wurden gelesen. Kein weiterer Agent wurde gestartet. Die Quellen wurden vor Abschluss der Bewertung unabhängig verfolgt. Dieser Bericht ist keine gemeinsame Bewertung mit dem zweiten Reviewer.

Das Dateisystem ist geteilt. Zugriffsbeschränkung und Schreibtrennung waren organisatorische Vorgaben, keine technische OS-Sandbox. Die unabhängige Vorher-/Nachher-Prüfung sichert den kontrollierten Dateistand, garantiert aber keine vollständige Isolation oder epistemische Unabhängigkeit der gleichen Modellfamilie. Die breite technische Werkzeugverfügbarkeit ist im Angebot ausdrücklich sichtbar und wurde für diesen Auftrag eingegrenzt.

Modell-/Reasoningangabe laut tatsächlichem Auftrag: gpt-6.1-sol, ultra geerbt. Eine interne Modellrevision und nicht zugängliche interne Anbietervorgaben sind unbekannt. Kein anderer Modellfamiliennachweis, akademisches Peer Review, politische Neutralitätsnachweis oder empirische Freigabe wird beansprucht.

Das vollständige angebotene Werkzeug-Namensinventar liegt in `tool-offer.json`: Funktionen-/Shell-/Patch-/Dateibildwerkzeuge, Web, Imagegen, Apps/Connectors einschließlich T3-Preview sowie die direkt angebotenen Collaboration-, Clock- und CUA-Namespaces. Tatsächlich genutzt wurden functions.exec, exec_command, apply_patch, write_stdin, view_image und T3 preview_open/snapshot/click/evaluate/scroll/press. Die vorhandenen Kollaborations-/Web-/Installations-/Kontowerkzeuge wurden nicht genutzt.

Alle exec_command-Aufrufe nennen den Worktree als workdir ausdrücklich. apply_patch-Schreibziele sind absolute Pfade im erlaubten eigenen Outputordner oder der neue Erstbericht. Keine gemeinsamen Forschungsartefakte, Skills, globalen Einstellungen oder anderen Repositories wurden geschrieben. Die für die Anwendung erforderlichen Skills unslop und pdf wurden ausschließlich gelesen und nicht geändert. Deren Regeldateien liegen außerhalb des Worktrees; eigene Projektänderungen blieben im Worktree.

T3-DOM-Lektüre beschränkte sich auf gerenderte öffentliche Texte, Links, die beobachtete Germany-Tabellenzeile und den sichtbaren Dialog/Scrollcontainer. Kein Login, keine Cookies, Storage, Auth, Credentials, versteckter Applikations-/Datenzustand, Analysis oder private API wurde geöffnet. Öffentliche Dokumenttabellen enthalten veröffentlichte Feldarbeitszahlen; das ist kein Zugriff auf Antwortmikrodaten oder politische Verteilungen. Ein anfänglicher T3-Snapshot zeigte automatisch Rendererfehler und eine fehlgeschlagene Analytics-Anfrage. Solche Nebeninformationen wurden nicht als Forschungsbelege oder als gespeicherte Nutzerkennungen in eigene Artefakte übernommen.

## Ausführung, Exits und Fehler

`command-ledger.json` enthält die28 ausgeführten Shell-Aufrufe C01–C28 im tatsächlichen Wortlaut, explizites workdir und Exitcode. Sämtliche abgeschlossenen Shell-Aufrufe erhielten Exit0. Die zwei zunächst laufenden Aufrufe für unabhängige PDF-Abrufe und Raster wurden über write_stdin abgeschlossen; ihre finalen Exits waren0. Die fünf internen pdftotext-Exits und neunzehn pdftoppm-Exits sind separat in den Abruf-/Renderprotokollen erfasst. Nach Erstellung des Erstberichts folgen ausschließlich lokale Abschlusskontrollen und ein Outputindex, deren Befehle das eigene Abschlussprotokoll dokumentiert.

Eigene begrenzte Fehler: Die erste Sammelausgabe war durch ein zu umfangreiches Werkzeugangebot abgeschnitten; Manifestdetails wurden separat und per Hashkontrolle erneut gelesen. Eine kombinierte Anforderungslektüre war am Ende abgeschnitten; analyseanforderungen wurde vollständig separat nachgelesen. Die kombinierte Guidelinesausgabe verlor einen Teil von Annex2; PDF25/26 wurden danach separat vollständig gelesen. Kein fehlender Textbereich wurde als geprüft gezählt.

Ein functions.exec-Aufruf scheiterte beim anschließenden Aufbau von tool-offer.json mit ReferenceError wegen einer falsch geschriebenen JavaScript-Zuweisung. Der zuvor erfolgreiche Scrollaufruf und drei Codebook-Bildansichten blieben durchgeführt. Der fehlerhafte Ausdruck schrieb keine Datei; tool-offer.json wurde im nächsten Aufruf korrekt erstellt. Die Quellen und gemeinsamen Artefakte wurden dadurch nicht geändert.

Keine Quelle innerhalb der elf Aussageprüfungen blieb unzugänglich. Nicht durchgeführte außerhalb liegende Kontrollen stehen oben ausdrücklich offen. Browserbefunde besitzen keine Shell-Exitcodes; die genannten T3-Operationen meldeten keinen Toolfehler. Ein direkt nach dem Country-Klick noch nicht gefüllter Snapshot wurde später erneut gelesen, ohne Datenzustand oder Login auszulesen.

Es wurden keine Installationen, Conda-, Commit-/Push-, Gesamtformatierungs- oder pnpm-Gesamtläufe durchgeführt. Der enge Prüfauftrag untersagt diese Operationen. reports/loop/reviews und outputs sind laut Prüfauftrag bei Prettier ignoriert; deshalb wäre selbst ein ignorierter Exit0 kein Formatierungsbeleg. Hier wurde überhaupt kein Prettier-Erfolg behauptet. PDF-/JSON-/Hash-/Lesekontrollen sind technische Quellenkontrollen, keine wissenschaftliche Abnahme.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Du bist ein frischer unabhängiger Quellenreviewer DESIGN-003, bisher unbeteiligt. Ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, exec_command workdir explizit, apply_patch alle Ziele ABSOLUT im Worktree. Eigene Outputs outputs/loop/design003-sources/, unveränderlicher Erstbericht reports/loop/reviews/DESIGN-003-sources.md. Prüfpaket reports/loop/packages/DESIGN-003/v1/manifest.json SHA256adc655d01e9cb538d091ba6d7810dfe5212353b4fc39e8e98c5e07f35759cad1,12files43SourceInputs. Lies alle gefrorenen Anforderungen, Issue, Auftrag, Prüfauftrag, 11 Aussagen/Belegregister, Quellenbericht und Methodenentwurf. Keine aktuellen Peerberichte/Loopfindings/Agentlisten/weitere Verteidigung lesen. Verfolge alle elf Aussage-IDs zu Originalen, wichtige Seiten visuell selbst lesen, nicht nur Rootextrakte. Public ESS-Studie Universe/Country Germany/Documents darf per T3-Preview neu selbst geöffnet werden, kein Analysis/Login/Cookies/storage/Auth/verborgener Datenzustand. Quellenversionen und unterschiedliche Geltungsbereiche kritisch: CountryReport4.0, Codebook4.1, Protocol1.5, Guidelines2022, WeightGuide1.2, liveStudy4.2Link. Sampling- und Erhebungsmodus,15großeGemeinden/166PPS, genaue Auswahlstufen, generischer PSU95 vsExample96, SDDF-Deposit vsverarbeitetePublicIndikatoren, Sachsenlistencounter und Guideapproximation/fpc/nestOriginalwortlaut prüfen. Keine exakte integrierte Kodierung oder echte SachsenStichprobenlücke erfinden. Grenzen können überstreng sein; sachlich mit Quellen begründen. Nicht zugängliche Quellen NICHT_GEPRÜFT, keine Findingquote. Originalfiles12+Source43vor/nachHashes/SafePath/Symlinks selbst. Keine ESSraw/local/Designzeilen/PersonenIDs/A/B/Partei-/LRwerte/Verteilungen/PortalAnalysis/Secrets/Userfile/globalWrites/InstallConda/CommitPush/Gesamtformat/pnpmGesamtlauf/andereAgents. GemeinsameArtefakte während Erstprüfung unverändert. Findings D-Sxx genauAussage/Originalfundstelle, Problem/Wirkung/begründeteSchwere/Korrektur/Nachprüfung, Vermutungen gesondert. Geplante spätere Analyse nicht als gescheitert/bestanden. Bericht vollständiger tatsächlicher Auftrag wortgetreu, gpt-6.1-sol ultra geerbt, interneRevision/Vorgaben unbekannt, angebotene/genutzteTools/CommandsExits/Fehler/SharedFS. Reportsreviews/Outputs ignoriert beiPrettier, ignoriertesExit0 kein Formatbeweis. Enges KI-Audit, kein andererModellfamiliennachweis/akademischesPeerReview oder empirischeFreigabe. Vollständig unabhängig abschließen mit PfadSHA und konkreten Resultaten.
```

Der übergeordnete dauerhafte Auftrag ist zusätzlich ungekürzt Teil des gelesenen, gefrorenen Pakets unter docs/auftrag-life-93-2026-10-03.md. Die konkreten Grenzen dieses Erstauftrags wurden nicht durch dessen allgemeinere Commit-/Arbeitsloopanweisungen erweitert.
