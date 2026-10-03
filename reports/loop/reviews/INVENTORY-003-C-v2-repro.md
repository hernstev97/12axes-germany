# INVENTORY-003-C v2: unabhängige Reproduzierbarkeits-Nachprüfung

Abgeschlossen am 2026-10-03. Frischer, bislang unbeteiligter Nachprüfer `inventory003_c_v2_repro`. Gegenstand ist C-R01, Reparaturrunde 1. Die Nachprüfung bestätigt die konkrete Korrektur. Sie ändert den ursprünglichen Erstbericht nicht und schließt keine wissenschaftliche Inventarabnahme ab.

Prüfpaket `reports/loop/packages/INVENTORY-003-C/v2/manifest.json`, SHA-256 `024cd9f143e353c17ffe1571c9b94a892bfe7c0bff36386488896a92a8db792b`, gefrorener Code-Commit `47e8cb564770d56ddf8d335ba1256f19a6de8b59`. Maßgeblich sind die bezeichneten Dateien und Quellenbytes. Das v2-JSON hat SHA-256 `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`.

## Ergebnis und Reichweite

| Tatsächlich ausgeführte Nachprüfung | Ergebnis |
| --- | --- |
| C-R01: ursprüngliche Metadatenzellen enden vor dem gesonderten Sprachlookup | BESTANDEN |
| Deutscher C24-Wortlaut, beide Locations, Originalsprache, ISO-/Anonymisierungshinweise, ASK ALL und bis zu zwei Sprachen erhalten | BESTANDEN |
| Vollständiger v1/v2-Diff: vier Inhaltsfelder und drei erklärte Provenienzpfade, keine weiteren Änderungen | BESTANDEN |
| Zwei eigene kontrollierte vollständige Nachbauten, mit Frozen v2 und untereinander bytegleich | BESTANDEN |
| Eigene Wiederherstellung der alten Lookupkontamination und eigener Metadatenerhaltungs-Gegenfall tatsächlich erzeugt, geprüft und abgewiesen | BESTANDEN |
| 16 Frozen Files und 117 öffentliche SourceInputs vor/nach; historische Indexbindung und geschützte Basis | BESTANDEN im unten dokumentierten Umfang |
| Ausgabe 4.2, endgültige Eignung/Polung/Neutralität, Messmodell und wissenschaftliche Abnahmen | NICHT_GEPRÜFT; kein Gegenstand dieses Nachberichts |
| `pnpm check`, Gesamt-CI und individueller Formatcheck | NICHT_GEPRÜFT durch diesen Nachprüfer; kein Gesamtlauf oder Formatlauf gestartet |
| UI und Browser | IN_DIESER_PHASE_NICHT_ERFORDERLICH; keine UI-Arbeit |

C-R01 bleibt dieselbe Kennung und dieselbe Reparaturrunde. Mein Urteil zur Reparatur ist BESTANDEN. Die koordinierte Entscheidung nach Sammlung beider vollständigen Nachberichte bleibt dem Koordinator vorbehalten. Ich fand kein neues belegtes C2-Rxx-Problem. Es gab kein Sollurteil und keine Fehlerquote. Die 15 offenen Grenzen bleiben ausdrücklich unverändert; spätere, hier nicht ausgeführte Anforderungen werden nicht als gescheitert dargestellt.

## Gelesene Grundlage und eigene Originallektüre

Ich las die gefrorenen Anforderungen, LIFE-93, AGENTS, Projektstand, Dauerauftrag, Prüfregeln, Analyseanforderungen, Lizenzakte, beide C-Prüfaufträge, vollständigen ursprünglichen Autorenbericht, beide vollständigen abgeschlossenen v1-Erstberichte, v1-Entscheidung und Korrekturbericht. Analyseplan, Belegregister und Entscheidungen wurden aus dem im Manifest bezeichneten Commit gelesen. Ihre Hashes passen zu den historischen Pins; `supplementary-requirement-pins.json` hält das fest. Der Analyseplan bleibt Arbeitsfassung, keine Präregistrierung oder methodische Freigabe. Verlinkte aktuelle Loopfindings, Agentlisten, andere Nachberichte und zusätzliche Autorenverteidigung wurden nicht geöffnet.

Die drei öffentlich gepinnten PDFs blieben unverändert. Beide Builderläufe extrahierten alle drei erneut. Zusätzlich habe ich Codebook PDF 117/Druck 116 und PDF 132/Druck 131 sowie deutschen Fragebogen PDF-/Druckseite 24 selbst mit Poppler als Layouttext und neue 130-dpi-Raster erzeugt und mit `view_image` gesehen. `original-extraction-runs.json` und `visual-reading.json` unterscheiden Erzeugung von tatsächlicher Sichtprüfung. Kein Netzrefresh, keine Portal-Analyse und keine PDF-Bearbeitung. Ich behaupte in dieser engen Nachprüfung keine neue vollständige Originallektüre von C1–C43 oder aller Lookup-/Country-documentation-Seiten.

Die Pins sind: Codebook 4.1 `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35`, deutscher Fragebogen `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`, Listenheft `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca`. Die Lizenzakte trennt Dokumentation unter CC BY-SA 4.0 von Daten unter CC BY-NC-SA 4.0. Diese Nachprüfung erteilt keine neue rechtliche Veröffentlichungsfreigabe.

## C-R01 am Original und am Feld

Codebook PDF 132/Druck 131 zeigt zuerst den Schluss des vorausgehenden Sprachlookups. Darunter stehen der `lnghom2`-Variablenkopf und eine abgeschlossene Metadatentabelle mit Type, Description, Location, postQTxt, Pre-Question Text und Question. Erst nach der geschlossenen Tabelle folgt die eigene Überschrift `Applies to variable lnghom2.` und ein eigener Sprachlookup.

Mein unabhängiger XML-Leser nutzt nach Rasterlektüre festgelegte tatsächliche Tabellenzellen. Er importiert weder Autorenbuilder noch Autorenchecker oder Geometriehelper. Die Metadaten einschließlich Kopf liegen in der vollständigen Originalregion x=72–540, y=360–495 PDF-Punkte. Der letzte Metadatentoken endet bei y=492,9185. Die Lookupüberschrift beginnt bei y=512,6226; die zehn ersten Lookupzeilen folgen darunter. Eigene rechte Wertzellen werden zusätzlich getrennt von ihren linken Feldüberschriften erwartet. Ein vorhandenes Wort irgendwo auf der Seite reicht nicht.

Der neue Beleg `CB41-lnghom2-metadata-132` hat exakt die 65 selbst extrahierten Kopf-/Metadatentokens, den vollständigen Originaltext und den daraus unabhängig errechneten Extrakthash `fa65412969e6e9152c81f0cedffdd997148fc8ed97ae6b60de59459e38a5eacd`. Feldwert, Belegbindung, Quelle und PDF-/Druckseite passen. V1 hat 91 Tokens: dieselben 65 plus die eigene Lookupüberschrift und zehn erste Lookupzeilen, zusammen 26 zusätzliche Tokens. Diese stehen in v2 nicht mehr im Metadatenfeld.

Die Description-Zelle behält ISO 639-2 und den Anonymisierungshinweis einschließlich Deutschland. postQTxt behält die Anweisung für höchstens zwei Sprachen. Pre-Question Text behält ASK ALL. Die vollständige englische Question-Zelle endet mit Language 2. `lnghom1` bleibt mit seiner Originalfrage für Language 1 und eigener Location C24 auf PDF 117/Druck 116 erhalten. Beide Location-Belege wurden als tatsächliche rechte C24-Wertzellen nachgeprüft.

Auf deutscher Q24 stimmen die drei Originalwortlautzeilen, die eigene ISO-Anweisung, AN ALLE und die Zwei-Sprachen-Eingabe mit zwei Eintragslinien. 777 und 888 bleiben ihren tatsächlichen Original-Labelzellen zugeordnet. Es werden keine Sprachkategorien ergänzt. `original-cell-expectations.json`, `own_checks.py` und `own-cell-check-results.json` halten Originalerwartungen, vollständige Token-BBox, Zellgrenzen und Ergebnisse fest.

## Vollständiger Diff und Erhaltung

Der eigene rekursive Strukturvergleich der vollständigen v1/v2-JSONs hat genau diese vier Inhaltsänderungen:

- `/belegregister/CB41-lnghom2-metadata-132/originalextrakt`
- `/belegregister/CB41-lnghom2-metadata-132/originalextrakt_sha256`
- `/belegregister/CB41-lnghom2-metadata-132/tokenauswahl`
- `/fragen/23/variable_zuordnung/quellen/1/metadaten/wert`

Die drei zusätzlichen Provenienzpfade sind `/zugriffsgrenzen/peerOrJurorReportsRead`, `/zugriffsgrenzen/loopFindingsRead` und das neu hinzugefügte Objekt `/korrekturprovenienz`. Die Korrektur bezeichnet ehrlich den Koordinator als Reparaturautor in Runde 1 und dessen bekannte Erstberichte/Loopfindings. Die ursprünglichen Zugriffsaussagen bleiben unter `originalAuthorAccessLimits` exakt erhalten. Das ist eine Aussage über den Reparaturautor; dieser Nachprüfer hat keine Loopfindings gelesen.

Alle 1525 übrigen vollständigen Belegobjekte sind gleich. Alle 43 vollständigen Frageobjekte sind nach Entfernen allein des bezeichneten Metadatenwert-Deltas gleich, einschließlich aller anderen C24-Felder, Kategorien, Nichtantworten, Kontexte, Filter, Listen und Weiterleitungen. Die 15 vollständigen offenen Einträge samt Identitäten, Gründen und Status sind gleich. `complete-structural-diff.json` enthält alle alten und neuen Werte der sieben Pfade. Die Zähler sind Umfangsnachweise, keine Gütewerte.

## Zwei eigene Builds und tatsächliche Gegenfälle

Vor dem Start habe ich die gesamte Korrektur-Builderfassung und den Helper statisch gelesen. Meine Builderkopie verändert ausschließlich OWN und TARGET. OWN, festes Unterprozesslog, beide BBox-Arbeitsverzeichnisse und beide Outputs liegen in `outputs/loop/inventory003-c-v2-repro/`. Der Helper ist bytegleich, sein Main-Zweig wurde nicht gestartet. Die erlaubten Reads sind die öffentliche Inventar-CSV, öffentliche Provenienz und drei gepinnte PDFs. `builder-preflight.json` hält konkrete Ziele, Hashes und geprüfte Schreibstellen fest.

Zwei vollständige Aufrufe meiner umgebundenen Kopie mit getrennten BBox-Arbeitsverzeichnissen enden mit Exit 0. Beide Outputs haben 3.418.839 Bytes und SHA-256 `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`. Der direkte Bytevergleich untereinander und mit Frozen v2 ist gleich. `build-command-1.json`, `build-command-2.json`, `tool-exits.jsonl` und `byte-reproduction.json` dokumentieren Aufrufe und tatsächliche Ergebnisse. Originalbuilder, `reproduce.sh` und Originalautorentests wurden niemals direkt gestartet.

Zwei eigene vollständige mutierte JSON-Kandidaten wurden geschrieben und tatsächlich gegen meine Originalzellerwartungen geprüft:

| Eigener Gegenfall | Tatsächliche Änderung | Ergebnis |
| --- | --- | --- |
| `old-lookup-contamination-restored.json` | V1-Metadatenbeleg und Feld vollständig wiederhergestellt, einschließlich 91 Tokens, zehn Lookupzeilen und passendem altem Extrakthash | Abgewiesen wegen falscher vollständiger Feldregion, Text-/Hash-/Feldabweichung und Tokens außerhalb der Metadatenzellen |
| `metadata-description-cell-removed.json` | Gesamte Description-Zelle konsistent entfernt; 39 Tokens, neuer dazu passender Extrakt/Hash/Feldwert; Location, Typ, ASK ALL, Zwei-Sprachen-Anweisung und Frage bleiben erhalten | Abgewiesen wegen fehlender Original-Description-Zelle und unvollständigem Gesamtfeld |

Der zweite Fall ergänzt den Autorencheck mit einer eigenen anderen Metadatenerhaltungsmutation. Überlebende Tokens stammen weiterhin aus dem Original; ein eigenkonsistenter Extrakthash genügt dem Prüfer trotzdem nicht. Die v2-Basis hat keine eigene Zellabweichung. Die tatsächlichen Fehlerlisten, Kandidathashes und vollständigen mutierten Pfade stehen in `own-cell-check-results.json`. Diese zwei Gegenfälle sind keine universelle Parservalidierung.

## Historische Indexbindung und Schutzbestand

Ich habe die Bindung ausdrücklich am v1-Manifest nachgeprüft. Das v2-Manifest bindet dessen SHA-256 `14a87ba5148fba5e640e8164ea06d7ff34cbc2893117dc6baf3eee91f96be7cb`. Beide Manifeste enthalten dieselbe ausdrückliche `preservedOriginalPath`-Regel. Der ursprüngliche unveränderte Autorenindex mit SHA `0cead9447e7010edade246c5177db750a2525994f8671a53784b15e8123ee7bd` bindet seinen Reporthash und die Report-Dateizeile mit `e1115c1db314202fe2468f9c95bb36d24408123f6e22e625de3873c7c3b08ca1` an das erhaltene Archiv. Alle 88 Originalindex-Dateizeilen passen nach genau dieser Umbindung zu Hash und Größe.

Die formatierte öffentliche Autorenfassung ist getrennt mit `743ba5394678f62c9d12b82b5518e3b60392ea59a8a727036114f209a02ad661` gebunden. Eigener vollständiger Formattransfervergleich: 41 Tabellen-Inhalts-/Kopfzeilen mit 123 gleichen Zellen und alle Nichttabellenbytes gleich. Der neue Korrekturbericht ist gesondert mit `eec4d3d008cf378adeeaf644bfb5692bec426d672f8cfb0c4141519ae5997c8b` gebunden; auch die 21 Korrekturindex-Dateien passen. Kein alter Reporthash wurde gegen den formatierten Livepfad geprüft. `index-and-format-check.json` enthält die Einzelbindungen. Dies ist ein Byte-/Formattransferbefund, kein wissenschaftlicher Beweis oder tatsächlich gestarteter Formatter.

Vor/nach passen Manifest, alle 16 Frozen Files und alle 117 SourceInputs zu Größe und SHA. Jede Zeile hat den dokumentierten öffentlichen Umfang und einen Pfad ohne Traversal/Symlink außerhalb des Worktrees. Der öffentliche Scope ist die Dateigrenze des Prüfpakets, keine aus Hashes abgeleitete Inhalts- oder Gütegarantie. Die 33 historischen Schutzinputs bleiben aktuell gleich. Ein weiterer Hashschutz über 614 vorhandene Forschungsgrundlagen-, Code- und Paketdateien zeigt keine Änderung. Andere Pakete wurden dabei nur gehasht, keine anderen Reviewinhalte gelesen. `integrity-before/after.json`, `historical-inputs-before/after.json`, `protected-before/after.json` und `protected-diff.json` dokumentieren den Umfang.

Ich habe die Originalregel `pipeline/inventar.py:609–628` gelesen und separat implementiert: 296 CSV-Identitäten und exakt dieselbe vollständige Pending-Liste mit 205 Einträgen wie `inventar.provenienz.json`. Kein Originalparserlauf. `original-counts.json` hält Regel und Einzelvergleich fest. Die Ergänzung wird nicht vom Basisbestand abgezogen.

## Werkzeuge, Fehlversuche und Trennung

Die Skills unslop und pdf wurden vor Anwendung gelesen. Laut tatsächlichem Startauftrag ist die zugängliche Modellkennung `gpt-6.1-sol`, Reasoning `ultra` geerbt. Interne Revision und nicht zugängliche Anbietervorgaben bleiben unbekannt. Ich gehöre organisatorisch derselben Codex-Modellfamilie an wie Autor und Erstprüfer. Das ist ein KI-Audit, kein akademisches Peer Review, keine andere Modellfamilienbestätigung und keine Garantie wissenschaftlicher Gültigkeit oder Biasfreiheit.

Das vollständige angebotene Metadatenverzeichnis steht in `tool-offers.json`. Tatsächlich genutzt wurden `functions.exec`, darin `exec_command`, `apply_patch` und `view_image`, sowie direkte `collaboration.send_message` für operative Elternmeldungen. Keine weiteren Agents, Agentlisten, CUA, Web oder Installationswerkzeuge. Python 3.14.7; Poppler 26.08.0. Vollständige Shellbefehle, beobachtete Exits und gekürzte Ausgaben stehen in `commands-and-exits.json` und ergänzend `commands-and-exits-late.json`; Poppler-Unterprozesse in den konkreten Extraktions-/Buildlogs. Die abschließende Indexbildung ist gesondert im Abschlussindex dokumentiert.

Drei eigene Vorbereitungsprobleme sind erhalten: Ein Apply-Patch-Hunk scheiterte vor jedem Dateischreiben an einer zusätzlichen unpräfixierten Schlussleerzeile. Die korrekt erzeugte absolute Patchfassung wurde danach angewendet. Der erste zusätzliche Hashschutz verweigerte `data/raw/.gitkeep` vor dessen Öffnung; die ursprüngliche Hilfsfassung bleibt unter `audit_support.first-refused-raw-marker.py`. Danach wurden Raw/Local-Namenspfade vor der Hashliste ausgeschlossen. Der erste Pending-Abgleich erwartete fälschlich den Provenienzschlüssel `pending` und meldete bei Exit 0 einen falschen Vergleich. 296/205 war bereits richtig; die originale Liste liegt unter `checks.pending_rows`. Die gezielte Korrektur bestätigt jetzt vollständige Listengleichheit, und `original-counts.first-wrong-provenance-key.json` bleibt erhalten. Daraus entstand kein Projektfinding.

Einige kombinierte Textausgaben waren gekürzt; erforderliche Dokumente, Erstberichte, Autorenbericht, Builder und Pending-Regel wurden anschließend vollständig oder in den erforderlichen einzelnen Abschnitten erneut gelesen. Eine breite initiale Dateinamenliste enthielt Namen anderer Berichte, keine Urteilsinhalte. Die Gedächtnissuche hatte Exit 1 ohne relevanten Treffer; keine Gedächtnisannahme wurde genutzt. Beide Builds, Originalextraktionen, abschließender eigener Zell-/Mutationslauf und Indexvergleich endeten mit Exit 0.

Das Dateisystem ist gemeinsam und keine technische Reviewer-Sandbox. Grenzen beruhen auf Auftrag, geprüften Pfaden und kontrollierten Schreibstellen. Jedes Shellwerkzeug hatte den zugewiesenen expliziten Worktree als Arbeitsverzeichnis; alle Apply-Patch-Ziele waren absolut im Worktree. Eigene Writes liegen ausschließlich im eigenen Outputordner und diesem Nachbericht. Forschungsartefakte, Originalautorenoutputs, Quellen und Pakete bleiben unverändert. Koordinatoränderungen außerhalb der benannten Hashschutzdateien werden dadurch nicht vollständig überwacht.

Kein Zugriff auf ESS-Roh-/Local-Dateien, Antwort- oder Designzeilen, Personenkennungen, zurückgehaltene A/B-Antworten, Partei-/Links-rechts-Werte, Verteilungen, Portal-Analysis oder Zugangsdaten/Secrets. Keine globalen Writes, Installation, Conda, Commit/Push, Gesamtformatierung oder pnpm-Gesamtprüfung. Es gab keinen individuellen Formatterlauf; ignorierte Output- oder Reviewpfade werden nicht als tatsächlich verarbeitet bezeichnet.

## Tatsächlicher vollständiger Startauftrag im Wortlaut

```text
Frischer unabhängiger Reproduzierbarkeits-Nachprüfer C-R01, bislang unbeteiligt. Worktree ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003; Shellworkdir explizit, alle apply_patch Ziele ABSOLUT im Worktree. Prüfpaket reports/loop/packages/INVENTORY-003-C/v2/manifest.json SHA256024cd9f143e353c17ffe1571c9b94a892bfe7c0bff36386488896a92a8db792b,16files117sources. Lies gefrorene Anforderungen/LIFE-93/AGENTS/Auftrag/Prüfregeln/Analyseplan/Lizenzen/Prüfauftrag, beide vollständigen abgeschlossenen v1-Erstberichte und Entscheidung/Korrekturbericht. Kein aktueller andererNachbericht, Loopfindings/Agentlisten oder zusätzlicheVerteidigung; keineweitereAgents. C-R01Runde1 prüfen: Codebook4.1 PDF132/Druck131 Originaltext undRaster selbst (PDFSkill); lnghom2 Header/Metadaten vor eigenerApplies-to Lookupüberschrift, 65statt91Tokens. C24DEOriginalQ24, beideLocations/Originalsprache/ISO/Anonymisierung/ASKALL/bis2Sprachen erhalten. VollständigerDiff v1/newJSON: exakt4Inhaltsfelder+3expliziteProvenienzpfade;1525andereBelege/43FragenalleanderenFelder/15offeneGrenzen unverändert. Zwei eigene vollständige bytegleicheNachbauten aus kontrolliertenOwnKopien, OWN/TARGET/festeLogs/helper prüfen bevorStart, OriginalautorenBuilder/reproduce/tests nie direktstarten. Eigene tatsächlich mutierte alteLookupkontamination + zusätzlicher eigenerMetadatenErhaltungsgegenfall, unabhängigeOriginalerwartungen und echteZellgrenzen stattTokenpresence. Index/archiveOriginalreportbindingv1explizitprüfen, alle16+117Hashes/SafePaths/PublicScopevor/nach. Nur outputs/loop/inventory003-c-v2-repro/ und reports/loop/reviews/INVENTORY-003-C-v2-repro.md schreiben; Forschungsgrundlage/Basis296Zeilen205PendingnachOriginalzählregel/Parser/anderenModule/Pakete/autorenoutputs unverändert. Keine ESSraw/local/AntwortoderDesignzeilen/Personen/A/B/ParteiLRwerte/Verteilungen/PortalAnalysis/CredsSecrets/globalWrites/CondaInstall/CommitPush/Gesamtformat/pnpmGesamtlauf/weitereAgents. KeinefinaleEignungPolungNeutralität4.2Messmodell/ScienceAbnahme; spätereAnforderungennichtalsgescheitertdarstellen. ExistingC-R01fortführen, neueC2-Rxx präziseAussage/Fundstelle/Problem/Wirkung/begründeteSchwere/KorrekturkonkreteNachprüfung, keinSollurteil/Fehlerquote. TatsächlichervollständigerStartauftragwortgetreu, Modellgpt-6.1-solultra geerbtinternunknown,ToolsangebotNutzung/CommandsExitsFehlläufe/SharedFSnichtSandbox. FrischorganisatorischgleicheCodexfamilieKI-AuditkeinakademischesPeerReview/Garantie. IndividuelleFormatchecks ignorierterOutputs/Reviewsnichtalswirklichverarbeitetbehaupten. Unveränderlichen vollständigenNachberichtabschluss mitSHA+OwnIndexmelden.
```

Dieser vollständige Nachbericht wird nach Übergabe nicht verändert. Sein Hash und die eigenen Outputhashes stehen nach Abschluss im eigenen `completion-index.json`; der Index schließt seinen eigenen Hash aus. Das Urteil gilt ausschließlich für dieses Manifest und C-R01 Runde 1.
