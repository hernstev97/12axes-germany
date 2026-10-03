# E1: Ergebnisprüfung v2.2 vor dem Export

Stand: 3. Oktober 2026. Prüfer: OpenAI Codex, gpt-6.1-sol, medium reasoning effort. Eigenständiges begrenztes KI-Review.

## Gesamturteil

**NICHT_BESTANDEN. Kein Export dieser Kandidatenfassung.** Die Anteile und vorhandenen Intervalle bestehen die durchführbaren Rechenkontrollen. Drei Hindernisse bleiben: vorzeitig gesetzter Reviewstatus, falsche Kategorienreihenfolge bei 20 Referenzen und fehlender unabhängig prüfbarer Nachweis der Fünf-Fälle-Regel. Keine Aussage, dass die Fallzahlregel tatsächlich verletzt wurde.

## Umfang und Bindung

Der vom Auftraggeber extern gehashte Auftrag dient als Umfangsmanifest. Sein SHA-256 stimmt. Alle fünf Kandidaten stimmen mit candidateExport im Laufbeleg überein. Der Laufbeleg selbst war nicht mit einem separat übermittelten Sollhash gesichert; sein Isthash wird unten dokumentiert. Die Bindung an den privaten Lauf ist eine übereinstimmende Hashangabe, keine Prüfung der privaten Bytes.

Das annotierte Tag analyseplan-v2.2 hat den Objekt-Hash 76ce19dce5b34d44249a8e095fb55e0fa0d4383f und zeigt lokal sowie auf origin auf b6af9a472c71ade865543cf75100c44a164ee12d. Plan, Katalogergänzung, Analyse-/Gruppenvertrag und run_v22.py/survey.py/export_v22.py stimmen bytegenau mit dem Tag überein. HEAD beim Prüfstart: 57e315c67bc2ea7edaac14d1c8d42be9c10e9419; Arbeitsbaum beim Start sauber.

Die private Ausgabe und Rohdaten wurden nicht geöffnet. Frühere Prüferurteile wurden nicht gelesen. Der vorgeschriebene Plan enthält historische Reviewzusammenfassungen; sie wurden nicht als Beleg für diese Ergebnisprüfung übernommen. Fragenauswahl ist nicht Gegenstand dieses Reviews.

## Ergebnisse der sieben Prüffragen

| Prüfung | Ergebnis |
| --- | --- |
| Status und 100/5 | 104 numerische Referenzen vorzeitig reviewed; Mindestbasis 100 überall eingehalten, Fünf-Fälle-Regel nicht unabhängig prüfbar. |
| Missing | 45 Gründe mit 1–4 Fällen ohne Gewichtssumme; Bilanz konsistent. |
| Anteile und Kategorien | 637 Kategorien, Summe jeweils 1 bis auf höchstens 1.11e-16; alle Codeinventare einschließlich 55 korrekt. Reihenfolge bei 20 Referenzen falsch. |
| Bekannte Werte | 42 Einzelreferenzen: maximale Differenz 1.11e-16; zwölf ESS9-Paare: 0; bekannte Werte, keine unabhängige Bestätigung. |
| Intervalle | 300 Bereiche in 32 Einzelreferenzen und zwölf Paaren, nur ESS9/ESS10SC/ESS11; Struktur und grobe Plausibilität bestanden. |
| Gruppen | Nur neue ESS5/8-Fragen und ESS9-Intervalle; alle Gruppen-IDs und Quellvariablen passen zu v2.1. Tatsächliche Fallzuordnung nicht neu gerechnet. |
| Kodierung/Polung | Kein belegter Fehler der Code-Anteil-Zuordnung oder Polumkehr. Belegter Sortierungsfehler; nicht zu einer politischen Ergebnisbewertung erweitert. |

Drei Einzelreferenzen und 107 Paare sind withheld_base_or_cell_count und reference=null. Ihre Verteilungen, Fallzahlen und genaue Unterdrückungsursache wurden nicht erschlossen.

### Intervalle und grober Designeffekt

Designangaben: ESS9 89 Strata/178 PSUs/89 Freiheitsgrade, ESS10 Self-completion 89/179/90, ESS11 25/500/475. Überall df=PSUs−Strata und df≥20. Alle vorhandenen Grenzen liegen in [0,1], enthalten den Anteil und sind auf der Logitskala symmetrisch. Null-/Einsanteile und ESS5/8 haben keine Grenzen. Diese Prüfung bestätigt die exportierten Metadaten, nicht die vollständigen privaten Designfelder oder PSU-Zuordnungen.

Aus dem Logitintervall wurde SE=(logit(U)−logit(L))·p(1−p)/(2·t(.975,df)) rückgerechnet. Der grobe Designeffekt ist SE²/[p(1−p)/n_gültig]. Keine neue Schwelle und keine Qualitätsfreigabe aus diesem Diagnosewert.

| Referenzen | Breite min/median/max in Prozentpunkten | Designeffekt min/median/max |
| --- | --- | --- |
| ESS10SCe03_2 singles | 0.22/1.33/3.72 | 0.90/1.41/4.60 |
| ESS11e04_2 singles | 1.49/4.78/7.76 | 1.60/2.95/4.54 |
| ESS9e03_3 singles | 0.46/3.54/5.61 | 0.65/1.52/3.05 |
| ESS9e03_3 groups | 1.73/11.04/23.00 | 0.78/1.12/1.94 |

Die breiteren ESS9-Gruppenbereiche sind angesichts der kleineren gültigen Basen plausibel. Auch die Einzelbereiche liefern keinen groben Widerspruch zur Fallzahl. Besonders seltene oder stark gewichtete Kategorien bleiben durch diese Kontrolle nicht validiert; nominale 95-%-Abdeckung wird nicht behauptet.

### Wortlaut und Richtung

Der Export bindet Werte an Originalcodes, ohne neue Polung. basinc und eusclbf laufen von 1 „Sehr dagegen“ bis 4 „Sehr dafür“. Energie läuft von 1 „Eine sehr große Menge“ bis 5 „Überhaupt nichts“; 55 bleibt eine gültige unaufgeforderte Antwort im historischen Nenner. Bei panpriph bedeutet 0 Gesundheit und 10 Wirtschaft; bei panmonpb 0 Überwachung und 10 Privatsphäre. Zustimmungscodes der neuen Asyl-, Gleichstellungs- und Loyalitätsfragen werden nicht umgekehrt. item_specs/classify übernehmen diese Inventare. Verteilungen allein beweisen keine korrekte Rohcodierung. Für neue Fragen waren die im Laufbeleg behaupteten privaten Gegenrechnungen nicht unabhängig zugänglich.

## Findings

### E1-V22-F01 — mittel

Alle 59 numerischen Einzelreferenzen und 45 numerischen Gruppenpaare tragen bereits reviewed_historical_reference. Die Dateientscheidung lautet gleichzeitig CANDIDATE-FOR-RESULT-REVIEW.

**Beleg:** outputs/claude/v22-candidate/ESS10SCe03_2.json#/questions/0/status: reviewed_historical_reference; /decision: CANDIDATE-FOR-RESULT-REVIEW; pipeline/v22/export_v22.py: export(), include führt unabhängig von einem Prüfurteil zu reviewed_historical_reference; reports/claude/auftraege/E1-ergebnispruefung-v22.md: Prüffrage 1; docs/analyseplan-v2.2.md: Abschnitte 6 und 8.3

**Auswirkung:** Der Kandidat behauptet einen bereits abgeschlossenen Prüfschritt. Keine Ergebnis- oder Exportfreigabe für diese Kandidatenfassung.

**Schweregrad:** Der Status ist eine relevante Freigabeangabe; die Zahlen werden dadurch nicht rechnerisch falsch.

**Korrektur:** Kandidaten in einer neuen Exportfassung mit prepared_pending_result_review und unveränderten Anteilen erzeugen. reviewed_historical_reference erst mit einer ausdrücklichen, an Lauf und geprüfte Kandidaten gebundenen Entscheidung setzen.

**Nachprüfung:** Neue Hashes sichern; sämtliche 104 numerischen Einträge auf Kandidatenstatus und zurückgehaltene Einträge auf reference=null prüfen. Keine historischen Artefakte überschreiben.

Status: OFFEN; belegt; blocksScope=true.

### E1-V22-F02 — mittel

20 Einzelreferenzen der Skala 0–10 exportieren die Reihenfolge 0,1,10,2,3,4,5,6,7,8,9 statt 0,1,2,3,4,5,6,7,8,9,10.

**Beleg:** outputs/claude/v22-candidate/ESS10SCe03_2.json#/questions/0/reference/categories/2/code: 10 (accalaw); data/politikprofil-v2.2.ergaenzung.json: items[id=ESS10SCe03_2:accalaw].apiValidCodeOrder; pipeline/v22/run_v22.py: main(), json.dumps(..., sort_keys=True); pipeline/v22/export_v22.py: public_reference(), Iteration über ref[shares].items(); data/gruppenvertrag.v2.1.entwurf.json: questionDefinitionPolicy, exact_category_order

**Auswirkung:** Bei Ausgabe nach Arrayreihenfolge rückt der obere Skalenpol zwischen 1 und 2. Die Anteile bleiben ihren Codes korrekt zugeordnet; ein Polungsfehler der Rechnung ist damit nicht belegt. Die 20 betroffenen Referenzen nicht in dieser Form exportieren.

**Schweregrad:** Gebundene Originalreihenfolge verletzt, mit möglicher falscher Darstellung ordinaler Kategorien.

**Korrektur:** Neue Exportfassung ausdrücklich nach apiValidCodeOrder des gebundenen Katalogs ordnen. Keine bloße Stringsortierung und keine Änderung der Zahlen.

**Nachprüfung:** Alle 62 Fragen und 152 Paare strukturell mit dem Katalog vergleichen; bei vorhandenen Referenzen Arrayreihenfolge exakt prüfen. Anteilvergleich nach Code erneut ausführen.

Status: OFFEN; belegt; blocksScope=true.

### E1-V22-F03 — mittel

validCount ist prüfbar und überall mindestens 100. Ungewichtete Kategoriehäufigkeiten beziehungsweise ein an die Kandidaten gebundener Nachweis der Mindesthäufigkeit positiver Zellen fehlen jedoch in allen 104 numerischen Referenzen. Der Laufbeleg enthält nur Statuszahlen und Autorangaben zu Gegenrechnungen.

**Beleg:** pipeline/v22/export_v22.py: public_reference() exportiert validCount und Kategorienanteile, jedoch keine categoryCounts; reports/claude/v22-laufbeleg.json: statuses und independentCrossCheck ohne überprüfbaren Zellschwellennachweis; pipeline/v22/run_v22.py: reference(), private categoryCounts und Prüfung 1 <= counts[c] < 5

**Auswirkung:** Die Fünf-Fälle-Regel lässt sich mit den erlaubten Eingaben nicht unabhängig nachprüfen. Das ist eine fehlende Prüfung, kein Beleg für eine verletzte Fallzahlregel. Exportempfehlung bleibt für alle numerischen Kandidaten gesperrt.

**Schweregrad:** Eine ausdrücklich verlangte Publikationsvoraussetzung bleibt unbelegt; der Code enthält die richtige Regel, beweist aber nicht die tatsächlichen Laufzellen.

**Korrektur:** Ein geprüftes, an privateRunSha256 und Kandidatenhashes gebundenes aggregiertes Prüfarbeitsprodukt für ausschließlich vorbereitete Referenzen bereitstellen, etwa Minimum der positiven Kategoriehäufigkeiten und Summenabgleich je Referenz. Keine Rohzeilen, Einzelgewichte oder Häufigkeiten zurückgehaltener Referenzen öffnen.

**Nachprüfung:** Frischer Prüfer verifiziert für jede numerische Referenz Mindestbasis 100, jede positive Kategorie mindestens 5 sowie unveränderte Kandidatenanteile. Die gesperrten Referenzen bleiben reference=null.

Status: OFFEN; belegt; blocksScope=true.

## Exportempfehlung je Frage und Paar

Aktuell darf keine numerische Referenz dieses v2.2-Kandidatenpakets exportiert werden: approvedQuestionIds=[] und approvedPairs=[]. Das ändert keine bereits veröffentlichten v2/v2.1-Dateien.

Die folgenden 59 Einzelreferenzen und 45 Paare sind Kandidaten für eine spätere Freigabe, wenn F01 und F03 nachgeprüft geschlossen sind. Für die 20 danach separat genannten Einzelreferenzen muss zusätzlich F02 geschlossen sein. Sie sind hier ausdrücklich nicht freigegeben.

### Einzelreferenzen mit offenen Voraussetzungen

- ESS10SCe03_2: accalaw, dfprtal, fairelc, freehms, gptpelc, grdfinc, gvctzpv, hmsacld, imdfetn, impcntr, imsmetn, keydec, loylead, medcrgv, panmonpb, panpriph, rghmgpr, scchpldm, viepol, votedir, vteurmmb, wpestop.
- ESS11e04_2: eqparep, eqparlv, euftf, fineqpy, freinsw, gincdif.
- ESS5e03_6: bplcdc, dbctvrd, dpcstrb, hrshsnta, lwstrob, prtyban, rgbrklw.
- ESS8e02_3: banhhap, basinc, bnlwinc, eduunmp, elgbio, elgcoal, elgngas, elgsun, elgwind, eusclbf, gvcldcr, gvrfgap, gvslvol, gvslvue, imsclbn, inctxff, mnrgtjb, rfgbfml, sbsrnen, wrkprbf.
- ESS9e03_3: sofrdst, sofrpr, sofrprv, sofrwrk.

### Zusätzlich betroffene Kategorienreihenfolge

- ESS10SCe03_2: accalaw, dfprtal, fairelc, gptpelc, grdfinc, gvctzpv, keydec, medcrgv, panmonpb, panpriph, rghmgpr, viepol, votedir, wpestop.
- ESS11e04_2: euftf.
- ESS5e03_6: bplcdc, dpcstrb.
- ESS8e02_3: gvcldcr, gvslvol, gvslvue.

### Paare mit offenen Voraussetzungen

Jede Zeile bezeichnet exakt die genannten Paare. second_vote:<Code> ist die Gruppendefinition im unveränderten v2.1-Vertrag, keine heutige Parteianhängerschaft.

| Gruppen-ID | Fragevariablen |
| --- | --- |
| ESS5e03_6:second_vote:1 | prtyban |
| ESS5e03_6:second_vote:2 | prtyban |
| ESS5e03_6:second_vote:3 | prtyban |
| ESS5e03_6:second_vote:4 | prtyban |
| ESS8e02_3:second_vote:1 | basinc, elgngas, elgsun, elgwind, eusclbf, gvrfgap, mnrgtjb, rfgbfml |
| ESS8e02_3:second_vote:2 | basinc, elgngas, elgwind, eusclbf, gvrfgap, mnrgtjb, rfgbfml |
| ESS8e02_3:second_vote:3 | basinc, eusclbf, gvrfgap, rfgbfml |
| ESS8e02_3:second_vote:4 | basinc, elgcoal, eusclbf, gvrfgap |
| ESS8e02_3:second_vote:5 | elgbio, elghydr, elgngas, elgsun, gvrfgap, rfgbfml |
| ESS9e03_3:second_vote:1 | sofrdst, sofrprv |
| ESS9e03_3:second_vote:2 | sofrdst, sofrprv |
| ESS9e03_3:second_vote:3 | sofrdst |
| ESS9e03_3:second_vote:4 | sofrdst |
| ESS9e03_3:second_vote:5 | sofrdst, sofrprv, sofrwrk |
| ESS9e03_3:second_vote:6 | sofrdst, sofrprv, sofrwrk |

### Weiterhin ausgeschlossen

- Einzelreferenzen: ESS10SCe03_2:cttresa, ESS8e02_3:elghydr, ESS8e02_3:elgnuc. Grund für jede: withheld_base_or_cell_count; Referenz bleibt null. Keine Entscheidung zwischen niedriger Basis und kleiner Zelle aus den nicht geöffneten Privatwerten abgeleitet.
- Gruppenpaare: alle 107 in ratings[0].excludedPairs des JSON-Urteils vollständig aufgelisteten IDs. Für jedes gilt derselbe dokumentierte Unterdrückungsstatus. Keine numerische Freigabe. ESS10/11-Gruppen bleiben insgesamt außerhalb des geplanten Exports.

Eine neue geprüfte Kandidatenfassung kann dieselben Anteile verwenden. Die Korrektur der Exportreihenfolge darf die Zahlen nicht verändern. Der zusätzliche Schwellenbeleg darf nur vorbereitete Referenzen betreffen. Kein Grund zur politischen Auswahl oder Entfernung einzelner Fragen aus dem Profil.

## Grenzen und technische Prüfungen

- Begrenztes KI-Review durch OpenAI Codex, keine akademische Begutachtung, Neutralitätsgarantie oder Freigabe durch Steven.
- Keine Frage neu ausgewählt, entfernt, umgepolt oder thematisch umgeordnet. Die Auswahl ist festgeschrieben.
- Nichts unter data/raw/ oder data/local/ gelesen, gehasht oder ausgeführt; kein Rechenlauf, Export, Commit, Tag, Push, Nachrichtenversand oder Deployment.
- privateRunSha256 sowie private Gegenrechnungen sind Angaben des Laufbelegs, keine unabhängig geprüften Privatbytes.
- Der extern gesicherte Hash bindet den Prüfauftrag, nicht separat die Laufbelegbytes. Kandidatenhashes wurden gegen den darin benannten Laufbeleg geprüft; eingefrorene Regeln zusätzlich gegen den Tag.
- Keine fremden P1/P2/P3-Urteile oder Kontrollrechnungsberichte als Bewertungshilfe geöffnet. Der verpflichtend gelesene Plan enthält historische Reviewzusammenfassungen; das ist protokollierte Kontextinformation und ersetzt kein eigenes Urteil.
- Intervallplausibilität nutzt nur vorhandene nicht zurückgehaltene Anteile, Grenzen und gültige Fallzahlen. Keine Designzuordnung, Gewichte oder Varianz aus Originalfällen kontrolliert.
- Keine externen Quellenrecherchen: Fragenauswahl und Quellenbindung sind festgeschrieben; Ergebnisprüfung gegen die ausdrücklich erlaubten lokalen Artefakte.
- pnpm check nicht ausgeführt: Der enthaltene Build schreibt weitere Dateien. Vollständige unittest-Discovery ebenfalls nicht ausgeführt, weil test_run_v22.py synthetische temporäre Dateien schreibt. Der ausdrückliche Auftrag erlaubt ausschließlich zwei Berichtsdateien. Acht rein rechnerische survey-Tests liefen mit ausgeschaltetem Bytecode.
- UI/Browser, Rechte, Teststart, wissenschaftliche Gesamtfreigabe und Veröffentlichung außerhalb dieses Auftrags.

Technisch ausgeführt: acht Tests in pipeline.v22.test_survey, alle bestanden. Der anfängliche Ad-hoc-Abgleich stoppte genau am Kategorienreihenfolgevergleich; nach Erfassung als Finding statt Abbruch lief die vollständige Prüfung erfolgreich durch. Statusabweichungen wurden ebenfalls gesammelt, nicht ausgeblendet. Die formale JSON-Prüfung mit dem unveränderten Urteilsschema und der gezielte Prettier-Check beider Berichte sind bestanden.

## Gelesene Dateien mit SHA-256

Die Hashes beziehen sich auf die tatsächlich gelesenen Arbeitsbaumbytes. Auftragsdatei zuerst vollständig gelesen und anschließend gegen den mitgeteilten Hash geprüft. Das aufgeführte policy_reference_v2.py wurde durch den synthetischen Test importiert; die ausführbaren Module wurden nicht mit realen Daten gestartet.

| Datei | SHA-256 |
| --- | --- |
| .agents/skills/unslop/SKILL.md | c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56 |
| .claude/skills/life93-review/SKILL.md | 90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6 |
| .claude/skills/life93-review/references/urteil-schema.json | 5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9 |
| AGENTS.md | 6d405f6baff0b692edf657dae09c933b3ef978e2f3a98d3caaf14dc7666f627f |
| data/analysevertrag.v2.entwurf.json | 8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b |
| data/gruppenvertrag.v2.1.entwurf.json | 9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702 |
| data/politikprofil-v2.2.ergaenzung.json | c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac |
| data/politikprofil-v2.fragen.entwurf.json | 5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4 |
| data/reference-groups-v21/ESS5e03_6.json | 343d06f921f5a943e742f304255726302b71162fb55d8c73b73d11f2f184b19a |
| data/reference-groups-v21/ESS8e02_3.json | fda4e3dab0546ba25ebb2c265d0d930830615697b023fce2075e41c6a562ff3a |
| data/reference-groups-v21/ESS9e03_3.json | a1e7f8b116da9d055ffffb2dc5eb2af04e43524962433a9b032f09cbd8b5d093 |
| data/reference-v2/ESS10SCe03_2.json | e75dfbadcf68c14dce9d13c8a8a2dd1abc6e8a6e96618f960c8cd61c54bc3184 |
| data/reference-v2/ESS11e04_2.json | 453d8ce3273c9e29bb08a49be6e69da46591e3d1ed89f306051b085c511ec721 |
| data/reference-v2/ESS5e03_6.json | e489fe013d1cbd3d72b9ae816e422757ce8d34ae575d09f64df13a1750dc4bc6 |
| data/reference-v2/ESS8e02_3.json | fb720cc18049f037ed86670bd76a51c3c1770342a61f5627b7afbfb127898ad7 |
| data/reference-v2/ESS9e03_3.json | 34e71b448c0c315cf9f19bda30628874c95464faf661813a65f25a3f9ad82be2 |
| docs/abdeckung-v2.2.md | f3f03912f38dc7149b73739bc18fa9bcec59c65f6cb77edfd130be3c8e2d1b10 |
| docs/analyseplan-v2.2.md | 13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8 |
| docs/profilregeln-v1.md | 3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23 |
| docs/project.md | 7cfa1d4046eb30ae4b29728c49fa90baff89f40e56199b8eff0a738ca004e270 |
| docs/pruefregeln.md | 29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233 |
| outputs/claude/v22-candidate/ESS10SCe03_2.json | b73b9dd089a51d9bb63c90ead09600de6547125f568d851eab97b2d3f6154baf |
| outputs/claude/v22-candidate/ESS11e04_2.json | c5e20b9f5ae6bb20ce606c52066dc608db8e3c061217b8eefbbd121da5b5a0ac |
| outputs/claude/v22-candidate/ESS5e03_6.json | 5fa548f650a481d70662c88a1ef904ad7b11319c2e03b64b4d52ca40bb096500 |
| outputs/claude/v22-candidate/ESS8e02_3.json | 203a95505a1305dfc2b6c3541730faf0719f82451189de045d4c3b0793c6c714 |
| outputs/claude/v22-candidate/ESS9e03_3.json | 6a2acd3cd3cf6b42fec51e3e1a9b99f796d0af80900711452a8069004af87829 |
| package.json | 451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7 |
| pipeline/policy_reference_v2.py | bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b |
| pipeline/v22/export_v22.py | 839765b1a8287141f8176ab988e86ab4deca7d712d84d53287b943c164d6eee1 |
| pipeline/v22/run_v22.py | b07d5bd8e9306dc7db2b0f1e72af9207d00ca255ea3b0c3c2f58d9f87925e1fd |
| pipeline/v22/survey.py | ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc |
| pipeline/v22/test_survey.py | dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011 |
| reports/claude/auftraege/E1-ergebnispruefung-v22.md | d347d6ef1d3a7614a06dc8bdf005ec9f7e0d2799dba11aa66cc3cb7f2c1346bf |
| reports/claude/v22-laufbeleg.json | 931d11ef811fa157e819ab5bc962a5c3a59b257274c8587467bb01a076bcd639 |
| scripts/check-review-schema.mjs | 2575997f720f0c440fc54a9ccc15a2bd8c8fb69638dab8c03cf8b9fdaf810166 |

## Ausgeführte Befehle und Modell

- cat / sha256sum reports/claude/auftraege/E1-ergebnispruefung-v22.md; cat der beiden Skills und des Urteilsschemas.
- cat bzw. sed: docs/project.md, docs/analyseplan-v2.2.md, docs/abdeckung-v2.2.md, docs/profilregeln-v1.md, docs/pruefregeln.md; Laufbeleg, Export-/Survey-Code, synthetische Testdatei und package.json.
- git status --short; git rev-parse HEAD; git rev-parse analyseplan-v2.2; git rev-parse analyseplan-v2.2^{}; git show analyseplan-v2.2:<Pfad> für die sieben gebundenen Regel-/Codeartefakte.
- git ls-remote origin refs/tags/analyseplan-v2.2 refs/tags/analyseplan-v2.2^{}.
- rg: gezielte Suche nach Status-, Zell-, Gruppen- und Sortierungslogik in pipeline/v22/run_v22.py, Testdateien und Gruppenvertrag; Schema-Prüfskript gelesen.
- Python 3 über stdin: ausdrücklich benannte JSON-Dateien einlesen; SHA-256, Fragen-/Gruppeninventare, Status/Nullschutz, Nenner/Missing, Kategorien, codebezogene Parität und Intervalle prüfen. Kein Skript in einer weiteren Datei gespeichert.
- PYTHONDONTWRITEBYTECODE=1 python3 -m unittest pipeline.v22.test_survey: 8 Tests, OK.
- Python 3 über stdin: genau diese zwei Berichtsdateien schreiben; keine weiteren Artefakte.
- node --input-type=module über stdin: Ajv2020 gegen .claude/skills/life93-review/references/urteil-schema.json für dieses JSON-Urteil; pnpm exec prettier --check auf genau diese Berichtsdateien; git status --short zur Abschlusskontrolle.

Laufzeitmodell laut T3-Code-Runtime: **gpt-6.1-sol**, OpenAI Codex, **medium** reasoning effort. Interne Modellrevision nicht bekannt. Werkzeugangaben sind tatsächliche lokale Prüfwerkzeuge; keine erfundene Anbieter- oder Modellrevision.
