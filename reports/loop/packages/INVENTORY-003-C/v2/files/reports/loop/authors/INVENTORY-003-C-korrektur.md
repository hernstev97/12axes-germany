# INVENTORY-003-C: C-R01 in neuer Autorenfassung

Koordinator `/root`, 3. Oktober 2026. Runde 1, `ENTWURF_NICHT_UNABHAENGIG_GEPRUEFT`. Beide vollständigen Erstberichte wurden vor dieser Korrektur gelesen. Der Vorabplan liegt unter `outputs/loop/inventory003-c-correction/plan-before-correction.json`; die Ausgangsfassung und alle Erstberichte bleiben unverändert.

## Änderung und Originalbeleg

Codebook 4.1, SHA-256 `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35`, PDF 132/Druck 131, zeigt den `lnghom2`-Variablenkopf mit Metadatentabelle und danach eine separate Sprachcode-Lookuptabelle. Ich habe die Seite selbst textuell und visuell gelesen. Die Metadatentabelle endet mit der Frage nach Sprache 2. Die nachfolgende Zeile `Applies to variable lnghom2.` eröffnet den gesonderten Lookup. Die alte Stoppregel erfasste diesen Anfang und zehn Lookupzeilen zusätzlich.

Eine neue Builderkopie endet für `lnghom2` vor genau diesem Überschriftstext. Die übrigen Selektionsregeln werden nicht geändert. Die neue JSON heißt `data/inventar-c.v2.ergaenzung.entwurf.json`. Der alte Builder, die alte JSON und das v1-Paket werden nicht überschrieben.

Der vollständige strukturierte Diff enthält vier inhaltliche Pfade: Originalextrakt, Extrakthash und Tokenauswahl des einzigen betroffenen Metadatenbelegs sowie dessen Feldwert bei C24. Die Metadaten behalten 65 statt 91 Tokens. Alle 1525 anderen Belege, sämtliche übrigen Fragen und alle anderen C24-Felder sind exakt gleich. Beide Locations, bis zu zwei Sprachen, `ASK ALL`, ISO-Hinweis und Anonymisierung bleiben erhalten. Kategorien, Filter, offene Punkte, Parameter und Prüfanforderungen werden nicht gelockert.

Drei weitere Diffpfade betreffen ehrliche Korrekturprovenienz: Die neue Fassung benennt den Koordinator als Reparaturautor, seine tatsächlich gelesenen Peerberichte und Loop-Findings. Die ursprünglichen Zugriffsaussagen des Erstautors bleiben in der Korrekturprovenienz erhalten. Ein neuer Quellenautor ohne Kenntnis der Erstberichte wird nicht behauptet.

## Tatsächlich ausgeführte Kontrollen

Zwei vollständige Builds mit eigener Builderkopie und getrennten Eingabe-/Ausgabepfaden endeten mit Exit 0 und liefern dieselben Bytes: SHA-256 `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`. Die neue öffentliche JSON ist bytegleich damit. Der Builder liest nur die drei gepinnten öffentlichen PDFs und die ursprüngliche Inventarprovenienz. Aufrufe, Zeiten, Exits und Ausgaben stehen in `build-command-log.json`.

Ein zusätzlicher Originalvergleich wurde tatsächlich ausgeführt: Der aus der Original-Bounding-Box extrahierte Variablenkopf endet vor der eigenen Lookupüberschrift. Die neue Belegauswahl, Extrakt, Hash und Feldtext stimmen damit überein. Zwei vollständige mutierte Kandidaten wurden anschließend geprüft und abgewiesen: Wiederherstellung der alten Lookupkontamination sowie Entfernung der Anweisung für bis zu zwei Sprachen. Die Kandidatbytes, Hashes und tatsächlichen Fehlermeldungen stehen in `correction-check-results.json`. Der Originalvergleich bestätigt außerdem alle 1525 übrigen Belege und sämtliche übrigen Fragefelder. Die acht gebundenen Basis-/Erstberichtsinputs bleiben unverändert.

Das ist ein enger Autorencheck. Er belegt keine universelle Parservalidität, endgültige Itemeignung, Neutralität, Daten-4.2-Kodierung oder Messmodellgüte. Zwei frische unabhängige Nachprüfungen dieser konkreten Fassung fehlen noch. Der Findingstatus wird erst anhand ihrer vollständigen Ergebnisse entschieden.

## Verfahren, Werkzeuge und Grenzen

Der Koordinator hat den Korrekturschritt anhand C-R01 und der dokumentierten Abnahmekriterien begrenzt; es gibt keinen zusätzlichen Subagent-Autorenauftrag. Tatsächlich genutzt wurden `functions.exec`, darin `exec_command`, `apply_patch`, `view_image` und `write_stdin`, sowie operative Zeit-/Agentwerkzeuge. Python, die kontrollierte Builderkopie und Poppler erzeugten ausschließlich eigene öffentliche Quellenextrakte und synthetische Mutationen. Der Renderaufruf für PDF 132 hatte Exit 0. Es gab keinen fehlgeschlagenen fachlichen Korrekturlauf. Eine vorbereitende Dateisuche fand den vermuteten Ordner `outputs/loop/checkpoint019` nicht; daraus entstand kein Prüfbeleg oder Dateiänderung.

Modell `gpt-6.1-sol`, Reasoning `ultra`, interne Revision und nicht zugängliche Anbietervorgaben unbekannt. Das gemeinsame Dateisystem erzwingt keine technische Blindheit; der Reparaturautor kennt beide Erstberichte. Keine ESS-Rohantworten, Personenkennungen, A/B-Hälften, Partei-/Selbsteinstufungswerte, Verteilungen, Portal-Analysis, Zugangsdaten, Installationen oder globalen Änderungen. Die vorhandene UI und alle anderen Projektdateien bleiben für diesen Schritt unverändert. Ein KI-Audit ersetzt kein akademisches Peer Review oder wissenschaftliche Garantie.
