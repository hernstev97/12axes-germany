# Erste Quellenprüfung vor der historischen v2-Ausführung

3. Oktober 2026. Rolle: Quellen, Konstrukte, Interpretation und politische Fairness. Prüfer: Codex, GPT-6.1-sol. Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`; Branchbezeichnung `research/life-93-night-20261003` vom Auftrag übernommen, wegen des Git-Verbots nicht selbst abgefragt.

Ich habe zwei fehlerhafte CAWI-Quellenbindungen gefunden. Sie betreffen ESS10 B3 und B6. Die 43 ausgewählten Export-Codelisten stimmen mit den gebundenen öffentlichen API-Originalen und dem Analysevertrag überein. Der erhebliche Befund betrifft die genaue nationale Kontext-/Modusbindung dieser beiden Angaben; er erklärt weder die übrigen Angaben noch das gesamte Einzelmessmodell für ungültig.

## Kontext, Grenzen und Identität

Zuerst gelesen: Paketmanifest und `scope.md`, anschließend den unslop-Skill und die aktuellen Worktree-Anweisungen. Kein Parentverlauf, keine anderen Ersturteile, Autorenberichte, Zustands-/Handoffdateien oder alten empirischen Ergebnisse wurden geöffnet. Die in den erlaubten Dokumenten enthaltenen Verweise und historischen Prüfstatus habe ich nicht als eigenes Urteil übernommen. Keine weiteren Agents, Git-, Auth-, Installations-, Claude- oder Serveraktionen.

Der Scope berichtet bereits bekannte v1-A/B-Neunerantworten und eine tatsächlich erfolgte B-Ausführung. Das ist die zugelieferte Expositionsgrenze, kein von mir rekonstruierter Zugriffsverlauf. Die sechs ausgewählten ESS11-Felder sind für historische deskriptive Sekundärauswertung vorgesehen. Andere Fragen derselben Studie erzeugen keine unabhängige Bestätigungsstichprobe. Ich behaupte keine unangetastete Bestätigung.

Roh-/Privatdateien und wirkliche CSV-Header habe ich weder geöffnet noch mit `stat` geprüft oder angefragt. Die Eingangsidentitäten stammen ausschließlich aus dem erlaubten `input-identity-context.json` und dem gepinnten Vertragsentwurf. Auch deren opaque Hashes beweisen keinen unabhängigen offiziellen Downloadweg. Keine Antworten, Frequenzen, Crosstabs oder tatsächlichen Analysen. Die vorliegende Prüfung schließt keinen Datenzugriffsgate und erlaubt keinen öffentlichen Export.

Manifest-SHA256 vor und nach der Prüfung: `eeae3bc1b81463b51ce2c0a1bf90f12b08aa01f125064e680d1f983df60c62f4`. Alle **20** manifestierten Artefakte stimmen bei beiden Durchgängen mit ihren Pins überein. Beide Prüfungen endeten mit Exit 0. Der spätere Durchgang erfolgte am 3. Oktober 2026, 13:54:13 UTC. Einzelpfade, Soll- und Ist-Hashes stehen in [pins-before.json](../../../outputs/loop/empirical-v2-001-sources-review/pins-before.json) und [pins-after.json](../../../outputs/loop/empirical-v2-001-sources-review/pins-after.json).

Zusätzlich stimmen die Hashes aller **29** als `source.cachedPath` gebundenen PDF-/API-Originale vor und nach dem Quellenabgleich. Das ist eine Identitätskontrolle, keine vollständige inhaltliche Lektüre aller 29 Dateien. Bestehende HTML-Caches und aus fremden Arbeitsläufen abgeleitete Texte habe ich nicht gelesen. Eigene Textauszüge und Renderings stammen unmittelbar aus den zugelassenen Original-PDFs. Alle neuen Dateien liegen im eigenen Outputordner oder in diesem Bericht; gemeinsame Forschungsdateien und ursprüngliche Reports blieben unverändert.

## Tatsächlicher Quellenabgleich

Gelesen und abgeglichen wurden die 43 Einträge des Fragenkatalogs, die zugehörigen Vertragsfelder, der Empirieplan, die Themenmatrix, der Messformenentwurf und die Lizenzdokumentation. Aus `docs/quellen.json` habe ich die einschlägigen Quelleneinträge gelesen; aus dem Belegregister die Zuordnung der v2-Methodenbelege. Die Methodenliteratur wurde hier nicht erneut vollständig begutachtet. Insbesondere ist der dort dokumentierte Abstractzugang zu Bollen/Lennox kein von mir gelesener Volltext.

Die deutschen Originalfragen, lokalen Einleitungen, Szenarien, Skalen und nationalen Nummern wurden anhand dieser physischen, 1-basierten PDF-Seiten geprüft:

| Original | Gelesene Seiten und Gegenstände |
| --- | --- |
| [ESS5 Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf) | PDF24–25: D18/D20 samt Polizeipflichten-Stamm; PDF27: D33–D36 samt historischem Deutschland-heute-Kontext. |
| [ESS8 Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf) | PDF33: D30–D32; PDF36: E6–E8; PDF37: E15; PDF42: E33–E35, einschließlich festem Arbeitslosenbudget und Steuerfolge. |
| [ESS8 Listenheft](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_showcards_DE.pdf) | PDF45/49/51/54: Listen44/48/50/53. Fragebogen PDF36 und Liste48 PDF49 zusätzlich visuell nebeneinander geprüft. |
| [ESS9 Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf) | PDF97: G26–G29, vollständiger Gerechtigkeitsstamm und fünf Zustimmungskategorien. |
| [ESS10 Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf) | Papier PDF7/10–12; alle ausgewählten CAWI-Fragen und Einleitungen auf PDF93–96/135–148/162 visuell gelesen. B3/B4/B5/B6/B7/B10 zusätzlich vergrößert gerendert. |
| [ESS11 Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf) | PDF13/14/51/52: B33/B37 und E19–E22, einschließlich Bundestag, Doppelverdiener-/Neugeborenen-/Elternzeit-Szenario und genauer Vergleichsrichtung beim Lohn. |

Das [43-Einträge-Protokoll](../../../outputs/loop/empirical-v2-001-sources-review/item-coverage.md) ordnet jeden Eintrag seinen nationalen Nummern und Quellenfundstellen zu. Bei Tabellen dienten Textauszüge zur Lektüre; bei den bildbasierten CAWI-Seiten die gerenderten Originalseiten. Ich habe keine nicht vorliegenden separaten Listenbilder für ESS5/9/11 bestätigt. Die dafür im Katalog angegebenen Grenzen bleiben bestehen.

Der eigene [Metadatenabgleich](../../../outputs/loop/empirical-v2-001-sources-review/source_probes.py) prüft pro ausgewähltem Feld die öffentliche Variablen-ID/-Version, Namen, vollständige Code-/Label-/Missing-Zuordnung, Reihenfolge und die Übernahme in den Vertrag. Ergebnis: 43 von 43 stimmen überein, genau acht Primärrubriken, identische Auswahl in Katalog und Vertrag, Exit 0. Fundstellen sind die gebundenen `*-original-codelists-direct.json` sowie `nine-fields-original-codelists.json`, jeweils unter `data.search` und der im Katalog angegebenen Feld-ID. Es handelt sich um deklarierte Metadaten des [öffentlichen ESS-API](https://api.nsd.no/graphql), keine beobachteten Antworten. [metadata-probes.json](../../../outputs/loop/empirical-v2-001-sources-review/metadata-probes.json) enthält die Einzelprüfungen.

Der erste PDF-Hilfsversuch scheiterte mit Exit 1, weil `fitz` fehlt. Ich habe nichts installiert und stattdessen `pdftotext`/`pdftoppm` genutzt; Extraktion und Rendering endeten mit Exit 0. Die eigenen Metadatenproben benötigten Korrekturen am Hilfsskript: falscher Elternpfad, unterschiedliche API-Schemata und die vom API gemeinsam gelieferten Gewicht-/Designfelder führten zunächst zu Exit 1. Nach Trennung der tatsächlich gebundenen Gewichte und Designfelder besteht der Quellenabgleich. Diese Hilfsskriptfehler sind keine nachgewiesenen Fehler der Projektpipeline.

Ein zusätzlicher OCR-Versuch für sechs CAWI-Renderings endete jeweils mit Exit 1, weil Tesseract keine Sprachdaten laden kann. Daraus entstand keine OCR-Bestätigung. Die Befunde unten beruhen auf visueller Lektüre; [ocr-tool-limit.json](../../../outputs/loop/empirical-v2-001-sources-review/ocr-tool-limit.json) hält die Grenze fest. Die automatische Wortfolgensuche fand 35 von 43 Fragen; acht Tabellen-/Zeilenumbruchfälle wurden anhand der Originalauszüge manuell geprüft. Dieser Hilfsabgleich ist kein Beweis vollständiger Transkriptionsgenauigkeit.

Keine Pipeline-Tests und kein `pnpm check` ausgeführt: Auftrag und Urteil bleiben auf Quellen und geplante Interpretation begrenzt. Die zehn gepinnten Python-/Testdateien wurden nur für die Pinprüfung byteweise gehasht. Ihre Berechnungen, Fehlerpfade, Gate-Implementierung und Exportguards wurden hier nicht als bestanden bewertet. Technische Synthetik wäre ohnehin keine Empirie.

## Befunde

### EV2-SRC-F01 – Falscher CAWI-Stamm bei B3 und B6

**Blocker für die betroffenen Quellenbindungen.** Stelle: `data/politikprofil-v2.fragen.entwurf.json`, `ESS10SCe03_2:medcrgv.modeBinding.cawiWordingDe` in Zeile3564 und `ESS10SCe03_2:cttresa.modeBinding.cawiWordingDe` in Zeile4551, außerdem jeweils `cawiDifferenceFromPapi`.

Beleg: Im [offiziellen deutschen ESS10-Original](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf), physische PDF139 für B3 und PDF142 für B6, steht auch im individuellen CAWI-Fragetext der Stamm „für die Demokratie im Allgemeinen“. Im Katalog fehlt diese Passage; der Begleittext behauptet ausdrücklich eine Verkürzung im Original. Das widerspricht den lesbaren Originalseiten. Originalhash `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425`; visuelle Nachweise [PDF139](../../../outputs/loop/empirical-v2-001-sources-review/ess10-page-139-large.png) und [PDF142](../../../outputs/loop/empirical-v2-001-sources-review/ess10-page-142-large.png).

Auswirkung: Die behauptete exakte Modus-/Kontextbindung ist für diese beiden Angaben falsch. Allgemeine persönliche Wichtigkeit und Wichtigkeit eines Prinzips für Demokratie dürfen nicht stillschweigend gegeneinander ausgetauscht werden. Der Papierstamm und die Kategorien sind korrekt gebunden; ich habe keine falschen Antwortcodes oder berechneten Anteile nachgewiesen. Die Kontextbindung muss nach der eigenen Vorabregel trotzdem vor abhängiger Interpretation stimmen.

Minimale überprüfbare Korrektur: Die beiden CAWI-Fragen vollständig vom gerenderten Original transkribieren und die unbelegte Verkürzungsbehauptung entfernen. Anschließend Katalog-/Vertrags-/Paketpins erneuern und genau diese Quellenbindung nachprüfen. Dieselbe behauptete Kürzung steht bei B4/B5/B7/B10; diese vier Einträge gezielt mit PDF140/141/143/146 prüfen. Ihre teilweise schwer lesbaren Rasterzeilen rechtfertigen hier keinen zusätzlichen sicher behaupteten Einzelbefund und erst recht keine erfundene saubere Originalfassung. Eine Korrektur dieser Bindungen verlangt weder Antworten noch neue Items oder eine Modellgesamtvalidierung.

### EV2-SRC-F02 – B25 hat zwei verschiedene Geltungsbereiche

**Hinweis, kein zusätzlicher Blocker der historischen Einzelfrage.** Stelle: `remainingBindings[].blocks = this_item_only` im Katalog, Zeilen10542–10555, gegenüber `boundaries.B25Scope` im Vertrag und Empirieplan Zeile30.

Beleg: [ESS10 Deutschland](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf), Papier PDF12 und CAWI PDF162. Beide statischen Formen enthalten die Mehrheit-/Regierungspläne-Einleitung und dieselben zwei Alternativen. Papier führt nach Antwort1 zu B26 und nach Antwort2 zu B28. Der CAWI-Screenshot weist keinen operativen Nachlauf nach. Ein vorgeschalteter Filter ist an den geprüften Stellen nicht sichtbar. Die öffentliche API-Codeliste deklariert für `scchpldm` 1/2 und Missing9; das stimmt mit dem Vertrag überein.

Auswirkung: Der unbekannte nachgelagerte CAWI-Ablauf ist keine hinreichende Begründung, die historische deskriptive B25-Einzelfrage pauschal zu verwerfen. Er erlaubt aber auch keine Originaläquivalenz des verkürzten neuen Webablaufs. Der Vertrag trifft diese Unterscheidung bereits; der unspezifische Katalogmarker bleibt für spätere Gates missverständlich. Tatsächliche Administration, Missingness und Nenner sind weiterhin ungeprüft.

Minimale überprüfbare Präzisierung: Den offenen Marker ausdrücklich auf die Reproduktion des Originalnachlaufs und die neue Webadministration beziehen. Die historische statische Einzelbindung gesondert beschreiben, ohne die offene CAWI-Operation als erledigt zu markieren. Die bereits geplante menschliche Prüfung des veränderten Webkontexts bleibt offen. Ich fordere keinen zusätzlichen operativen Nachlaufnachweis als allgemeine Voraussetzung einer historischen Kategorienbeschreibung.

### EV2-SRC-F03 – Acht Rubriken sind eine begrenzte Auswahl

**Inhaltsgrenze, kein Gesamtblocker der historischen Rechnung.** Stelle: Primärthemen im Katalog und Empirieplan Zeilen9/18–25; Abdeckungsmatrix Zeilen19–27.

Beleg: Die tatsächlichen Fragen erschließen folgende Inhalte. Dieselben Anforderungen an deutsche Originale, Kontext und API-Codes wurden über alle acht Rubriken angewandt.

| Primärrubrik | Zahl | Tatsächlich erschlossene Aussage und zentrale Auslassung |
| --- | ---: | --- |
| Wirtschaft/Verteilung | 5 | ESS9 G26–29 und ESS11 B33 betreffen Verteilungsprinzipien und Einkommensverringerung. Markt-/Eigentumsordnung, Wettbewerb und konkrete Steuerarten sind damit nicht umfassend erschlossen. |
| Sozialstaat | 5 | ESS8 E6–8/E33–34 betreffen Zuständigkeit, Zielgruppe und einen Budgettradeoff. Gesundheit, Pflege, Bildung und Wohnen bleiben als eigenständige Leistungsgegenstände offen. |
| Demokratie/Autorität | 12 | ESS10 B1–11 plus B25 betreffen normative Wichtigkeit und Mehrheitsresponsivität/Planbindung. Keine gemessene objektive Demokratiequalität, kein persönlicher Populismus-/Autoritarismuswert. |
| Bürgerrechte/Sicherheit | 6 | ESS5 D18/D20/D33–36 betreffen Polizei-, Gerichts- und Gesetzesbindung sowie relative Strafverschärfung im historischen Kontext. Protestfreiheit, Überwachung und konkrete Sicherheitsanlässe sind damit nur unvollständig erschlossen. |
| Europa | 3 | ESS10 A90/B12 und ESS11 B37 unterscheiden Mitgliedschaft, Zuständigkeit im Demokratiekontext und Integrationsumfang. Keine gemeinsame EU-Gesamtposition. |
| Klima/Energie | 3 | ESS8 D30–32 betreffen drei konkrete Instrumente. Versorgungssicherheit und Energieträgerwahl bleiben offen. |
| Migration | 4 | ESS10 A54–56 und ESS8 E15 betreffen Zulassungsgruppen und Sozialansprüche. Schutz-/Asyl-, Grenz-, Abschiebungs- und Teilhabepolitik werden dadurch nicht umfassend beschrieben. |
| Gleichstellung/Familie | 5 | ESS11 E19–22 und ESS8 E35 betreffen konkrete Eingriffe und Finanzierung. Andere Lebensformen, reproduktive Selbstbestimmung und weitere Diskriminierungsgründe bleiben unvollständig. |

Konkrete Originalfundstellen: [ESS9 PDF97](https://stessrelpubprodwe.blob.core.windows.net/data/round9/fieldwork/germany/ESS9_questionnaires_DE.pdf), [ESS5 PDF24–25/27](https://stessrelpubprodwe.blob.core.windows.net/data/round5/fieldwork/germany/ESS5_main_questionnaire_DE.pdf), [ESS8 PDF33/36–37/42](https://stessrelpubprodwe.blob.core.windows.net/data/round8/fieldwork/germany/ESS8_questionnaires_DE.pdf), [ESS10 PDF7/10–12](https://stessrelpubprodwe.blob.core.windows.net/data/round10/fieldwork/germany/ESS10_questionnaires_DE.pdf), [ESS11 PDF13–14/51–52](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf).

Auswirkung: Eine größere Zahl von Demokratiefragen darf keine größere politische Bedeutung im Gesamtprofil erzeugen. Mehrere normative Verteilungsfragen ersetzen keine breite Wirtschaftsordnung. Zugang und ESS-Nachnutzbarkeit erklären die Auswahl, belegen aber keine vollständige oder neutrale politische Themenwahl. Außen-/Verteidigungs-/Friedenspolitik ist in den 43 Angaben nicht enthalten. Die Quellenbindung sagt auch nichts über Motive oder Charakter aus. Unterstützung einer Paritätsregel ist beispielsweise kein allgemeines moralisches Gleichstellungsurteil.

Minimale überprüfbare Konsequenz: Die im Plan bereits ausgesprochenen Inhaltsgrenzen bei späteren Ausgaben an den betroffenen Rubriken erhalten. Nur konkrete Antworten benennen; keine vollständige politische Identität, aktuelle Bevölkerungsnorm, Parteienlabels, moralischen Personennamen oder Neutralitätsbescheinigung ableiten. GLES/ISSP bleiben begrenzte, noch nicht ausführbare Ergänzungswege. Deren Dokument-/Datenrechte und Originalfassungen habe ich mangels entsprechender zugelassener Katalogoriginale hier nicht erneut unabhängig geprüft. Die vorgesehene ESS-Ausführung benötigt dafür keine erfundenen Pflichtitems, Drei-Item-Regel, formative Gesamtsumme oder neue latente Gesamtmodellprüfung.

## Nenner, Referenzen und Rechte

Die API-Originale stützen die Trennung gültiger Kategorien und Missinggründe. Keine der 43 deklarierten Listen enthält einen eigenen Not-asked-Code. Ein nuller API-Filter beweist trotzdem keine tatsächliche Volladministration. Der Vertrag darf später nur die tatsächlich geprüfte Antwortbasis beschreiben. Exportleere hat den gesonderten unbekannten Grund; sie darf nicht als Verweigerung, Unwissen oder strukturelle Nichtstellung umbenannt werden.

Bei ESS10 A90 sind 33/44/55/65 gültige nominale Kategorien. 65 bedeutet Nichtstimmberechtigung und ist keine EU-Gegenposition. Der Anteil für Mitgliedschaft hat im geplanten vollständigen Kategorienvektor den Nenner aller gültigen Antworten einschließlich dieser Kategorien, keinen stillschweigend bereinigten Wählernenner. Der deutsche Papierdruck1–6 darf nicht als CSV-Code übernommen werden. Bei ESS5 D18/D20 bildet der Katalog gedrucktes Weiß-nicht98 auf API88 ab. Bei ESS8 E6–8 ist das fehlende gedruckte10 in der Fragebogenmatrix dokumentiert; Einleitung und originale Liste48 sowie API binden0–10. Ich sehe hier keinen Codingblocker.

Die getrennten deutschen öffentlichen Studien-/Dateimetadaten stimmen in den geprüften Feldern mit ESS5e03_6, ESS8e02_3, ESS9e03_3, ESS10SCe03_2 und ESS11e04_2 überein. ESS5/8/9/11 sind CAPI-Referenzen; ESS10 Deutschland nutzt Papier/CAWI. Feldzeiten reichen über Jahresgrenzen: 2010/11, 2016/17, 2018/19, 2021/22 sowie 2023. Die Zielpopulation ist jeweils15+ in Privathaushalten unabhängig von Staatsangehörigkeit; das ist keine Aussage über alle erwachsenen Wahlberechtigten oder heutige Webbesucher. ESS8s Ausschluss Münchens steht ausdrücklich in den öffentlichen deutschen Sampling-Metadaten und im gebundenen Studiensatz. Gewichtung stellt diese ausgelassene Stadt nicht empirisch wieder her. ESS10-SCs dokumentierte Inkonsistenz zwischen Datei3.2 und älterem Zitationstext3.1 bleibt erhalten; eine Face-to-face-Datei ist keine deutsche Ersatzreferenz.

Primär `pspwght`, getrennte Design-/ungewichtete Sensitivität und fehlende persönliche/Design-Konfidenzintervalle sind hier als geplante Aussagen gelesen. Ihre tatsächliche Rechnung habe ich nicht überprüft. Die Schwellen100/5 sind ausdrücklich Darstellungsheuristiken. Daraus folgen keine validierte Präzision oder Anonymität. Originalkategorien, Zustimmung, Wichtigkeit und nominale Wahl bleiben getrennt; keine metrische Mittelung, studienübergreifende Personenmatrix, Kovarianz oder formative Gesamtpunktzahl.

Der [ESS-Disclaimer](https://europeansocialsurvey.org/contact/disclaimer) wurde live direkt abgerufen: HTTP200 am 3. Oktober2026, 13:52:17 UTC; SHA256 `b5201b2deefd86d7f87a8dfb11dfdd30fd4f9afb8cbbb51b9254dd58bfa5ab8a`. Zuvor scheiterte derselbe Zugriff über das Webtool mit502 beziehungsweise einem Zugangsfehler; der Direktabruf löste diese Zugriffsgrenze. Er nennt Daten CC BY-NC-SA4.0 und Dokumentation CC BY-SA4.0 getrennt. Auch die offiziellen [BY-SA-Bedingungen §§2–3](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) und [BY-NC-SA-Bedingungen §§1–3](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en) wurden über das Webtool gelesen. Attribution, Versions-/Änderungsangaben und einschlägige Weitergabebedingungen bleiben erforderlich; diese Lizenzbefunde ersetzen keine konkrete rechtliche Veröffentlichungsprüfung. Der Katalog enthält dafür Urheber-/Archiv-, Lizenz- und Änderungsangaben. Kommerzieller Umfang, besondere nationale Rechtehinweise und konkrete Exportartefakte bleiben vor Veröffentlichung zu prüfen. Kein allgemeines legal release.

## Entscheidung zur gepinnten Ausführung

Für die vollständige geplante historische Ausführung mit allen43 gebundenen Angaben fehlt wegen EV2-SRC-F01 die korrekte genaue Quellenbindung zweier Fragen. Die minimale Abhilfe ist eine Quellenkorrektur mit erneuter Pinbindung und gezielter Nachprüfung vor abhängiger Interpretation. Die übrigen historischen Einzelangaben haben aus dieser Quellenrolle keinen weiteren festgestellten erheblichen Blocker; EV2-SRC-F02/F03 sind begrenzte Hinweise und erzeugen keinen pauschalen Forschungsstopp.

Beide getrennten Rollen und die Autoren gehören zur selben Codex-Modellfamilie. Gemeinsame Trainings-, Transkriptions-, Quellen- und Interpretationsfehler bleiben möglich. Die gleiche Paketidentität verbessert Vergleichbarkeit, macht ihre Urteile aber weder familienunabhängig noch zu einem Neutralitätsnachweis. Dieses Ersturteil beansprucht keine wissenschaftliche Gesamtvalidität, Fachbegutachtung, empirische Websiteäquivalenz, menschliche Verständnis-/Gestaltungsabnahme oder Releasefreigabe. Es verändert keinen Datenzugriffsgate und keine angehaltene v1-Folge.

NOT_ACCEPTED
