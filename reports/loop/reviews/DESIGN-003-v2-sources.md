# DESIGN-003 v2: unabhängiger Quellen-Nachbericht

Reviewer /root/design003_v2_sources, 3. Oktober 2026. Der Bericht wird nach seinen Abschlusskontrollen unverändert erhalten.

Die beiden dokumentarischen Korrekturen sind **BESTANDEN**. D-S01/D-M01 und D-S02/D-M02 bleiben mit ihren bisherigen Kennungen in Reparaturrunde 1. Ich habe keine neuen D2-Sxx-Findings festgestellt. Das Urteil gilt ausschließlich für den nachgeprüften Quellenwortlaut und den angekündigten Änderungsumfang. Es ist keine Freigabe einer konkreten deutschen Designkodierung, eines Splits, einer Varianzrechnung oder des Modells.

## Eingefrorene Grundlage und tatsächlicher Lesebereich

Geprüft wurde DESIGN-003/v2, Manifest SHA-256 `fdfd7d4d2f24c80c6a93682477e03a90fcdfa0e90a1863ba1c5881b23dbe695f`, Code-Commit laut Manifest `47e8cb564770d56ddf8d335ba1256f19a6de8b59`. Entscheidend sind die gebundenen Dateien und Quellen, nicht der Commit allein.

Die gefrorenen AGENTS-, Projekt-, Auftrags-, Issue-, Prüfregel-, Analyseanforderungs- und Lizenztexte wurden gelesen. Beide v1-Erstberichte wurden vollständig gelesen; der beim ersten Sammelaufruf abgeschnittene Quellenbericht-Schluss wurde anschließend auf seinen tatsächlichen Zeilen 115–163 nachgelesen. Entscheidung und v2-Prüfauftrag, v1-Autorenbericht und ursprünglicher Prüfauftrag wurden ebenfalls vollständig gelesen. Andere Nachberichte, Loopfindings, Agentlisten und zusätzliche Autorenverteidigung wurden nicht geöffnet. Keine weiteren Agents wurden gestartet.

Beide Designtexte und das vollständige v2-Claimregister wurden gelesen. Das v1-Register wurde vollständig gegen v2 verglichen; alle unterschiedlichen Stellen wurden im vollständigen Diff gelesen. Der Methodenentwurf v1 wurde auf allen 181 Zeilen gelesen. Der einzige neue v2-Absatz auf Zeile 87 wurde vollständig gelesen; die gesamte davor- und danachliegende Fassung wurde bytegenau auf Gleichheit geprüft. Damit beruht der Änderungsbefund nicht auf einer selektiven Zeilensuche.

Die Integritätsprüfung umfasste vor und nach der Prüfung alle 19 gefrorenen Dateien und alle 50 SourceInputs. Beide Male stimmen Bytes, SHA-256, relative sichere Pfade und sämtliche Pfadkomponenten ohne Symlinks. Das Manifest stimmt ebenfalls. Die Nachprüfung um 07:56:43.743280 UTC bestätigt die identischen 69 Einträge der Startprüfung um 07:48:31.774180 UTC. Zusätzlich stimmen am Ende alle 19 ursprünglichen Worktree-Dateien mit dem Manifest, darunter die historischen Berichte. Detailbelege sind `integrity-before.json` und `integrity-after.json`.

Der Public-Scope wurde gegen die ausdrücklich gebundene Eingabeliste, ihre Scope-Felder, Pfadgrenzen und Ausschlüsse raw/local geprüft. Das ist keine allgemeine Inhaltsprüfung jeder Seite aller Dokumente und keine technische Zugriffssperre. Tatsächlich gelesen wurden die unten benannten öffentlichen Fundstellen; keine Antwortmikrodaten.

Alle relativen eigenen Outputnamen dieses Berichts beziehen sich auf `outputs/loop/design003-v2-sources/`.

## D-S01 / D-M01, Runde 1

Die Korrektur ist **BESTANDEN**. Die korrigierte Aussage D-DE-010 auf `data/design-quellen.v2.entwurf.json:159` lautet, dass die gebundene und erneut öffentlich gelesene Geographical-unit-Liste Sachsen und Sachsen-Anhalt als getrennte Einträge enthält. Der regionale Absatz `docs/design-deutschland.v2.entwurf.md:17` berichtigt den früher behaupteten Gegensatz ausdrücklich und begrenzt die Aussage.

Ich habe nach `preview_status` einen eigenen neuen T3-Hintergrundtab `tab_l` geöffnet. Auf der [öffentlichen ESS11-Studienseite](https://ess.sikt.no/en/study/412db4fe-c77a-4e98-8ea4-6c19007f551b) wurde nur Country documentation und die beobachtete Germany-Zeile mit Details geöffnet. Der vollständige öffentliche Dialogtext wurde um 07:50:12.298 UTC aus dem gerenderten Dialog gelesen und als `germany-independent.json` gespeichert. Die Geographical-unit-Liste wurde danach vollständig im tatsächlichen Browserbild gelesen. Screenshots wurden im Tool gesehen, nicht außerhalb des erlaubten Ordners gespeichert.

Die ganzen, durch Kommas getrennten Listenelemente der drei Aufnahmen sind exakt gleich:

Baden-Württemberg; Bayern; Berlin; Brandenburg; Hamburg; Hessen; Mecklenburg-Vorpommern; Niedersachsen; Nordrhein-Westfalen; Rheinland-Pfalz; Saarland; Sachsen; Sachsen-Anhalt; Schleswig-Holstein; Thüringen.

Es sind 15 Elemente. Sachsen und Sachsen-Anhalt stehen jeweils genau einmal als eigene Elemente darin. Die Ausgangsaufnahme `germany-modal.json` und die neue Autorenaufnahme `germany-modal-new.json` tragen denselben Befund. Der Gegenbeleg gegen v1 bestand damit bereits vor der Korrektur. Die Aussage war kein inzwischen behobener Portalzustand. Die dynamische Studie liefert hier keine auslesbare unveränderliche Studienrevision; Gleichheit der gespeicherten Aufnahmen ist ein Aufnahmebefund.

Das [Codebook4.1](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf) wurde selbst erneut von der offiziellen URL geladen, mit HTTP200 und dem gebundenen SHA-256 `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35`. Die Titelseite nennt Edition4.1. PDF484/gedruckt483 wurde selbst extrahiert, neu gerendert und über view_image vollständig angesehen. Dort steht DED Sachsen als eigener Katalogeintrag.

Die neue Entscheidung berichtigt auch die falsche Behauptung des erhaltenen historischen Autorenberichts ausdrücklich. Das ist die richtige historische Behandlung. Weder Claim noch Designabsatz behaupten tatsächliche regionale Teilnahme, regionale Repräsentativität oder einen offiziellen Region-Crosswalk. Aus dem fehlenden Bremen-Listenelement wird keine neue Datenausfallbehauptung gebaut. Warum Bremen dort nicht steht, bleibt unbekannt.

Die ursprüngliche mittlere Schwere in beiden Erstberichten bleibt erhalten. Der falsche Quellenbefund konnte nachgelagerte Arbeit fehlleiten; ein tatsächlicher Datenausschluss oder Ergebnisfehler ist damit weiterhin nicht nachgewiesen. Meine Schließung beruht auf dem Originalgegenbeleg, nicht auf übereinstimmenden Reviewerurteilen.

## D-S02 / D-M02, Runde 1

Die Zuschreibungskorrektur ist **BESTANDEN**. Der neue erste P07-Absatz `docs/analyseplan-methoden.v2.entwurf.md:87` trennt die ESS-Grundsyntax, den eigenen Projektvorschlag einer Ultimate-PSU-Taylor-Approximation und die zusätzliche nest-Option.

[WeightsV1.2](https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf) wurde selbst erneut von der offiziellen URL geladen, HTTP200, SHA-256 `6b9c04b70b8f231de1b9040e4afcfc9387fc95e4a1d15ec0496aa7638f8528e5`. Die Titelseite nennt 06.07.2023 und V1.2. Die gesamte Box5 auf PDF10/gedruckt8 wurde selbst extrahiert und im neu erzeugten Raster vollständig gelesen, einschließlich der Beispielschätzungen darunter. Der svydesign-Aufruf hat genau die Argumente ids, strata, weights und data. nest, fpc und pps sind nicht spezifiziert. Die Box verwendet den Namen Ultimate-PSU-Taylor-Approximation nicht.

Die aktuelle [survey-Originalhilfe](https://search.r-project.org/CRAN/refmans/survey/html/svydesign.html), Paket4.4-2, wurde im Web und aus einer eigenen vollständigen HTML-Aufnahme gelesen. Arguments nest und die vollständigen relevanten Details bestätigen die Umkennzeichnung für Stratumverschachtelung bei wiederverwendeten PSU-Kennungen. Die Hilfe nimmt standardmäßig globale Eindeutigkeit an. Ohne FPC verwendet sie die oberste Auswahlstufe mit Zurücklegen und nur diese Stufe für die Clustervarianz. Der neue P07-Absatz beschreibt diese Softwareannahme zutreffend als Begründung des eigenen Approximationsvorschlags.

Der eigene HTML-Abruf erhielt HTTP200 und ist bytegleich mit der gebundenen Hilfe: `8a4e855b86fbad2519c60555639981bf9da8fbb2ee634af42c97753d080c0997`. Es wurden keine Bibliothek und kein R installiert. Ein tatsächlicher R- oder ESS-Lauf wurde nicht durchgeführt und ist für diese Quellenzuschreibungskorrektur **IN_DIESER_PHASE_NICHT_ERFORDERLICH**. Reale Design-/Varianzprüfungen bleiben **NICHT_GEPRÜFT**.

Die Voraussetzung für nest bleibt korrekt begrenzt. Gleiche Kennungen in unterschiedlichen Strata müssen tatsächlich verschiedene, jeweils darin verschachtelte PSUs bezeichnen. Die offizielle Bedeutung der verarbeiteten Kennungen muss vor Anwendung geklärt werden. Relabelling erzeugt keine fehlende Designinformation und repariert keinen falsch identifizierten Cluster. Der neue Absatz erhebt keinen Anspruch auf eine exakte Varianz beliebiger deutscher PPS- oder systematischer Auswahl.

D-S02 war ursprünglich MITTEL, D-M02 NIEDRIG. Die Entscheidung erhält beide Bewertungen und begründet ihre operative mittlere Bewertung über die falsche Autoritätszuschreibung. Diese unterschiedlichen Bewertungen werden durch mein Quellenurteil nicht vereinheitlicht. Sie betreffen keine nachgewiesene falsche Rechnung. Beide ursprünglich beschriebenen Probleme werden durch die tatsächliche Textänderung aufgelöst.

## Vollständige Diffs und konkrete Gegenprüfungen

Die drei vollständigen Diffs wurden erzeugt und vollständig gelesen: `design-full.diff`, `claims-full.diff` und `methods-full.diff`. `diff-and-list-checks.json` enthält die Assertionsergebnisse.

- Im Claimregister ist ausschließlich D-DE-010 geändert. D-DE-001 bis D-DE-009 und D-DE-011 sind als vollständige Objekte exakt gleich. Auch alle übrigen Top-Level-Felder sind gleich; hinzugekommen ist nur das angekündigte correction-Objekt mit Runde1, den ursprünglichen IDs und noch offenem Status.
- Im Methodenentwurf ist ausschließlich der erste P07-Absatz auf Zeile87 anders. Der vollständige Text davor und danach ist exakt gleich. Das umfasst alle übrigen P01–P13-Passagen, Tabellen, Formeln, vorgeschlagenen Parameter und offenen Gates.
- Der Designbericht ändert nur Zeile3 mit Versions-/Belegverweis und vorläufigem Nachprüfstatus sowie Zeile17 mit der erklärten Sachsenkorrektur. Es gibt keine zusätzliche Designentscheidung.

Eigene Negativprüfungen stehen in `negative-checks.json`. Ein erfundenes einzelnes Metadatenlisten-Element Sachsen-Anhalt zählt nicht als Sachsen. Der tatsächliche v1-Claim wird durch das tatsächlich vorhandene Sachsen-Element widerlegt. Der Originalargumentvergleich von Box5 weist eine hineingeschriebene nest-Zuschreibung zurück. Das sind enge Text-/Quellenprüfungen, keine synthetischen ESS-Designzeilen oder Methodenvalidierung.

Zusätzliche konkrete Grenzfälle wurden anhand der Originalhilfe inhaltlich geprüft: Bei bereits global eindeutigen Kennungen macht die Hilfe nest nicht erforderlich. Würde derselbe reale Cluster irrtümlich über Strata verteilt, wäre sein Relabelling keine Reparatur. Der No-FPC-Weg belegt eine Softwareapproximation, keine tatsächliche PPS-Abdeckung. Dies sind hypothetische Grenzen, keine Aussagen über beobachtete deutsche Kennungen oder Ergebnisse.

## Offene Prüfungen und Reichweite

Offen bleiben konkrete Edition4.2-Design- und Regionszuordnungen, offizieller Crosswalk, Behandlung der beiden Auswahlwege, Splitunterstützung und Restabhängigkeit, Varianz-/Intervallabdeckung, ordinale Messmodellverfahren, persönliche Messintervalle, weitere Forschungsgates und Modellfreigaben. Keine davon wurde hier als bestanden oder empirisch gescheitert erklärt. Die zehn unveränderten Claims wurden in diesem Nachauftrag auf Unverändertheit geprüft; ihre Originalquellen wurden nicht alle erneut inhaltlich auditiert.

Die Lizenzakte wurde als eingefrorene Anforderung gelesen. Dieser Nachbericht führt keine neue Lizenzbehauptung und keine rechtsfachliche Freigabe ein. Der Unterschied zwischen Originaldokumentation und Antwortdaten bleibt bestehen. Ein vollständiges öffentliches Forschungs- oder Websiteaudit liegt mit diesem engen Bericht nicht vor.

Das ist ein KI-Audit derselben Codex-Modellfamilie. Es ist kein akademisches Peer Review, keine wissenschaftliche Garantie und kein Nachweis politischer Neutralität. Es ersetzt weder erforderliche andere Modellfamilienprüfungen noch menschliche Beiträge oder fachliche Abnahmen.

## Tatsächliche Werkzeuge, Exits und Grenzen

Das vollständige Werkzeugangebot ist in `tool-offer.json` dokumentiert, die tatsächliche Nutzung in `tool-usage.json`. Genutzt wurden functions.exec, exec_command, apply_patch, view_image, Web und die T3-Werkzeuge status/open/snapshot/click/evaluate. Systemwerkzeuge waren vorhandenes Python3 mit urllib/HTMLParser, Poppler, cat/sed/rg/nl/wc und das vorhandene Node/Prettier für die individuelle Berichtskontrolle. Die Skills unslop und pdf wurden gelesen und angewandt, nicht geändert.

`command-ledger.json` enthält die tatsächlichen Shellbefehle im Wortlaut mit explizitem Worktree und ihren Exits. Die internen Parser-/Renderbefehle stehen zusätzlich in `source-commands.json`: vier pdftotext- und zwei pdftoppm-Aufrufe, sämtlich Exit0. Alle drei eigenen erneuten Originalabrufe erhielten HTTP200. Die selbst ausgeführten Diff-, Listen-, Negativ- und Integritätsprüfungen endeten nach der unten benannten eigenen Syntaxkorrektur mit Exit0.

Die individuelle Formatkontrolle verarbeitet den eigenen Berichtstext ausdrücklich durch die vorhandene Prettier-API mit parser markdown. Sie vergleicht die tatsächlich formatierte Ausgabe byteweise mit dem Bericht und speichert Zeichen-/Bytezahlen, Version und Zielhash in `format-processing.json`. Sie verlässt sich nicht auf einen durch ignore-Regeln übersprungenen CLI-Exit0. Kein pnpm-Gesamtlauf und keine Gesamtformatierung wurden ausgeführt.

Begrenzte eigene Fehler und Ausfälle wurden nicht verschwiegen:

- Zwei Sammelausgaben wurden gekürzt. Der Quellenbericht-Schluss wurde auf echten Zeilen nachgelesen; das Manifest wurde vollständig maschinell verarbeitet. Ein zuerst zu hoher sed-Bereich lieferte nur leere Ausgabe bei Exit0 und wurde nicht als Lektüre gezählt.
- Der Codebook-Aufruf im Webtool lieferte Internal Error. Der anschließende eigene offizielle PDF-Direktabruf war erfolgreich; sein Ergebnis wurde selbst textlich und visuell geprüft.
- Ein functions.store-Aufruf versuchte nach dem bereits erfolgreichen PDF-Skript eine nicht vorhandene session_id als undefined zu speichern und scheiterte. Das Shellskript war zu diesem Zeitpunkt mit Exit0 fertig; alle Quellen und Raster lagen vor. Es gab keinen ausstehenden Prozess.
- Das erste eigene Diffskript hatte einen falschen schließenden Klammerntyp und endete mit SyntaxError/Exit1. Nur das eigene Skript wurde korrigiert. Der zweite Lauf und die vollständigen Diffs waren erfolgreich.
- T3-Snapshots gaben automatisch Electron-Rendererfehler zurück. Eine erste Bildaufnahme zeigte noch den Tabellenframe, obwohl der Dialog im semantischen Text schon erschien. Erst die folgenden Bilder des Dialogs und der ganzen Geographical-unit-Liste wurden als Sichtbeleg gezählt. Abgeschnittene Snapshottexte wurden durch die eng begrenzte öffentliche Dialog-DOM-Lektüre ergänzt. Die automatische Diagnostik wurde nicht als Forschungsevidenz ausgewertet.

Die Trennung ist auftrags- und pfadbasiert im Shared-FS, keine technische Sandbox. Sämtliche Shellaufrufe nennen den beauftragten Worktree. Alle apply_patch-Ziele sind absolute Pfade im eigenen Outputordner. Ausschließlich der eigene Bericht und eigene Outputs wurden geschrieben. Außerhalb des Worktrees wurden nur die erforderlichen Skilltexte und ein enges Memory-Registry-RG gelesen; letzteres lieferte keinen Treffer und keine verwendete Erinnerung.

Keine ESS-Rohdaten, lokalen Zwischendaten, Design-/Antwortzeilen, Personenkennungen, A/B-Hälften, Partei-/Links-Rechts-Werte, Verteilungen, Portal-Analysis, Kontoinhalte, Cookies, Storage, Auth, versteckter Applikationszustand oder Secrets wurden geöffnet. Kein Installer, Conda, globaler Write, Commit, Push oder Eingriff in gemeinsame Forschungs-, Quellen-, Paket- oder Parserdateien fand statt.

Laut tatsächlichem Startauftrag ist die Modell-/Reasoningkonfiguration gpt-6.1-sol, ultra geerbt. Die interne Revision und nicht zugängliche Modellvorgaben bleiben unbekannt; ich habe keine unabhängige Laufzeitattestierung dieser internen Angaben.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger Quellen-Nachprüfer DESIGN-003 v2, bislang unbeteiligt. Worktree ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, Shellworkdir explizit; alle apply_patch absolut im Worktree. Paket reports/loop/packages/DESIGN-003/v2/manifest.json SHA256fdfd7d4d2f24c80c6a93682477e03a90fcdfa0e90a1863ba1c5881b23dbe695f,19files50sourceInputs. Lies gefrorene Anforderungen/Issue/AGENTS/Auftrag/Prüfregeln/Analyseanforderungen/Lizenzen, vollständige beiden v1-Erstberichte, Entscheidung und v2-Prüfauftrag. Keine anderen Nachberichte/Loopfindings/Agentlisten oder Verteidigung, keineweiterenAgents. Historische v1-Dateien imPaket sind Ausgangsbelege; zu prüfende Korrekturtexte docs/design-deutschland.v2.entwurf.md,data/design-quellen.v2.entwurf.json,docs/analyseplan-methoden.v2.entwurf.md. D-S01/D-M01Runde1: Sachsen steht im gebundenen öffentlichen Germany-Original und erneuten Rootcapture; eigener neuer öffentlicherGermanyDialog viaT3 (erstpreview_status), genaueganzeListenelemente plusSichtprüfung, Codebook4.1PDF484/483 selbst. KeinDatenausfall/Regionalrepräsentativitäts-/Crosswalkbeweis, keineBremen-Ersatzbehauptung. D-S02/D-M02: ganzeWeights1.2Box5PDF10/8Originaltext+Sicht selbst, aktualle gebundene survey-Hilfe Argumentsnest/Details; neueP07SyntaxESSgrund vsEigeneUltimatePSUApprox+optionnestmitkorrekterVoraussetzung getrennt, keinrealerR-/ESSLauf als erwartet ausgeben. VollständigerDiff10andereClaims exaktgleich/P01–P13außererklärtemP07absatzexactgleich; DesigntextnurKorrektur+Versionsverweise. UnterschiedlicheSchwerebewertungenoriginalerhaltenEvidenceentscheidkeinMehrheit. EigeneOriginalgegenbelege und konkreteNegativfälle sinnvoll; keineQuote/Sollurteil. Alle19+50HashesPublicscopeSafePath/Symlinks vor/nach. Nur outputs/loop/design003-v2-sources/ und reports/loop/reviews/DESIGN-003-v2-sources.md schreiben. KeinebestehendenOutputs/Forschungsdateien/Quellen/Pakete/BasisCSVParserändern. Kein ESSraw/local/DesignoderAntwortzeilen/Personen/A/B/ParteiLRwerte/Verteilungen/PortalAnalysis/AuthCookiesStorageHiddenAppState/CredsSecrets/InstallConda/globalWrites/CommitPush/Gesamtformat/pnpmGesamtlauf. Forschungsgates/konkrete4.2DesignMapping/SplitCoverage/persönlicheCI/Modellfreigabe bleiben offen; spätereAnforderungennichtgescheiterteAnalysen. BestehendeIDs/Runde1behalten, neueD2-SxxFindings genaueAussage/Fundstelle/Problem/Wirkung/begründeteSchwere/KorrekturNachprüfung,Vermutungenkenntlich. Tatsächlichen vollständigenStartauftragwortgetreu, gpt-6.1-solultra geerbtinternunknown,Toolsangebot/Nutzung/CommandsExits/Fehlläufe/SharedFSkeinSandboxdokumentieren. EngerKI-AuditgleicheCodexfamiliekeinPeerReview/Garantie. Unveränderlichen vollständigenNachbericht mitSHA+OwnIndexmelden; individuelleFormatcheckwirklicheVerarbeitungnachweisen,ignorierteExit0keinNachweis.
```

Der ungekürzte dauerhafte Gesamtauftrag ist zusätzlich in der gelesenen gefrorenen Datei docs/auftrag-life-93-2026-10-03.md enthalten. Dessen allgemeiner Arbeitsloop erweitert die ausdrücklich engere Nachprüferbefugnis nicht.

Der abschließende `output-index.json` bindet diesen Bericht und alle eigenen gespeicherten Prüfartefakte. Bericht- und Indexhash werden dem Koordinator nach tatsächlicher Abschlusskontrolle übermittelt. Der Bericht wird danach weder überschrieben noch automatisch weiterformatiert.
