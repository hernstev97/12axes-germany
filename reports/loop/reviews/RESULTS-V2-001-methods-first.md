# RESULTS-V2-001 — frisches Ersturteil Methoden/Reproduzierbarkeit

Datum: 2026-10-03. Rolle: `methods_reproducibility`. Entscheidung: **ACCEPTED_BOUNDED**.

Dieses Urteil erlaubt aus Methodensicht ausschließlich die unten einzeln genannten historischen kategorialen Referenzen der exakt gepinnten Kandidaten. `ESS10SCe03_2:cttresa` bleibt gesperrt und erhält keine Zahlenreferenz. Die Entscheidung ist kein Exportauftrag: Das getrennte Quellenurteil und Roots tatsächliche Prüfung/Entscheidung fehlen dieser Rolle. Die Renderbibliothek besteht die geprüften technischen Grenzen als WIP-Referenzlisting; die vollständige geplante Darstellung unter acht Themenrubriken ist damit nicht fertig oder freigegeben.

Kein Rohdatenzugriff und keine unabhängige Rohreproduktion. Keine Neutralitäts-, Gesamtvaliditäts-, menschliche, rechtliche oder Releaseabnahme. Dieselbe Codex-Modellfamilie kann gemeinsame Fehlerquellen haben. ESS11 bleibt sekundär in derselben bereits für v1-A/B bekannten Erhebung; keine neue unangetastete Bestätigung, keine Wiederaufnahme der v1-Folge.

## Tatsächlich geprüfte Identität und Grenze

Zuerst wurden die tatsächlichen Manifestbytes geprüft. SHA256: `3299ad658cca7cbb5621c6f062d4133b831e74d8bf4ca71bcb8e67fff56c4434`. Danach wurden alle 29 öffentlichen Artefakte und ausschließlich die fünf aufgeführten privaten `run.json`-Dateien byteweise gegen ihre SHA256-Pins geprüft: **PASS**. Die fünf Dateien sind ignored und 0600. Eigene Aggregateprobes liegen ignored unter `outputs/loop/result-v2-001-methods/`, Verzeichnis 0700, Dateien 0600. Es wurden keine tatsächlichen Häufigkeiten, Anteile, Gewichtswerte oder kleinen Zellen in diesen Bericht übernommen.

Kein Lesen, Statten, Aufzählen oder Header-/Kennungs-/Parteifeldzugriff unter `data/raw/`; kein tatsächlicher Runner, Netzwerk, Browser, Server, Install, Auth, Git-Mutation oder Delegation. Nur die gepinnten Artefakte und freigegebenen Aggregate wurden als Belege benutzt. Fremde Erstberichte, Autorenberichte, Parent-History, State und Handoff wurden nicht geöffnet. Die formalen Rollen-/Hashattestationen im mitgelieferten Vorgate wurden nur als Pin-/Guardmetadaten betrachtet; sie ersetzen keine eigene Rechnung und liefern hier keine fremde Begründung. Der zusätzlich im vorgelagerten Manifest referenzierte, hier nicht freigegebene `first-manifest.json` wurde nicht geöffnet.

Die kanonischen Kandidaten- und Einzelstudienvertragshashes wurden unabhängig mit sortierten JSON-Schlüsseln, kompakten Separatoren, UTF-8, `ensure_ascii=False` und `allow_nan=False` berechnet. Sie stimmen mit dem Resultmanifest überein. Doppelte JSON-Schlüssel wurden beim privaten Oracle-Lesen zurückgewiesen.

| Studie | Tatsächliche Runbytes SHA256 | Kanonischer Kandidat SHA256 | Kanonischer Einzelstudienvertrag SHA256 |
| --- | --- | --- | --- |
| `ESS5e03_6` | `b7a430ab14a9ae5b2f6537abd0fe968bb09d3b42bfdde9e21f0bba79d94426c6` | `d29d4acc6ff1a973d8bb920b0ba02afbadc7e7bd378e53374a9363e752945e33` | `6779d181d7f42d3a76659ca0cd403960fd6fee893316dac2175542d18af77fe4` |
| `ESS8e02_3` | `6ec04807e401aeb4c0c46dd833c676bb3700f235a5fdbb8c39cc7fd9f0e8d557` | `0ca02b80692de3b04ce7733c2aca09c1a70e7d85aafc40632d39d99f07d8bca0` | `d40c4fbfbd66ee17cf066320b660210f4a0ff5b7c611915cd8785559beb2bbf0` |
| `ESS9e03_3` | `2eda8b76f037fd089110dfe7412757a171d6eee7eed755aad78976a6e9c108a1` | `93258369d2f929aa990a11d6aae7dc442eb0d8525eaf6404290c2450f22fb125` | `a900f578434f0eba135fefbdec7795326ae75140cbc220b4c30edf9b0f01ce9d` |
| `ESS10SCe03_2` | `1b9546154b2ed3daecebf787f24e709e6e6009e69715f20baae5c4788032c79d` | `e2916511e06254185d3d0394d37fd29e68d225ca6996c16a9a4ac8b42ee5de55` | `14875f845a20f2a048b75628ab98b13bb24863f73b51f50f95421fecc201d8ad` |
| `ESS11e04_2` | `ffce2bd934da6ca789be619a70283ec8afd3dc9c3bce994c7d1d7b16e5f1ee82` | `f36960ab75a2ac357d92b373013f51767a88aff98759061511b86dff6c3e05c2` | `3f7c6c5b3ccf6415cba5a998849067cb368b0045e22189c79e9cfd5f6097c440` |

## Prüfkriterien und Befunde

| Kriterium | Befund | Beleg/Grenze |
| --- | --- | --- |
| Manifest, Kandidat, Einzelstudienvertrag | PASS | Tatsächliche Bytes und eigene kanonische Hashrechnung; nicht aus Statusstrings abgeleitet. |
| Katalog/Vertrag/Quelle | PASS im Paket | Alle festen Frageidentitäten, Reihenfolgen, Originalcodes, Missinggründe und Notaskedcodes abgeglichen; Leerzelle nur `export_blank_unclassified`. Kein erneuter offizieller Downloadnachweis. |
| Laufprovenienz | PASS für interne Bindung | Runpins mit tatsächlichen Manifest-/Vertrags-/Freeze-/Gatebytes, Inputidentitätskontext und Receipts abgeglichen; Zeitstempel liegen im jeweiligen Laufintervall. Rawbytes und offizielle Ursprungsauthentizität nicht unabhängig geprüft. |
| Fixe Darstellungsregeln | PASS | Status unabhängig aus gültiger Basis und allen Originalkategorien hergeleitet: mindestens 100 gültige Antworten und mindestens fünf Fälle je positiv besetzter Kategorie; echte Nullkategorien bleiben erhalten. Nullstatus trägt keine Referenz. |
| Itemnenner und Partitionen | PASS | Kategoriecounts summieren zum gültigen Itemnenner; Gesamt = eligible + notasked, eligible = gültig + missing. Grundcounts/-gewichtssummen passen zum primären Missingaccounting; Notasked bleibt eigenständig. |
| Vier vorhandene Gewichtsvarianten | PASS | Alle vorhandenen `pspwght`-, `dweight`-, ungewichteten und `anweight`-Referenzen jeder freigabefähigen Frage mit unabhängigen rationalen Rechnungen geprüft; keine Schätzung für nullreferenzierte Fragen erzeugt. |
| Sensitivitätsmaxima | PASS | Kategorieweise Differenzen aus selbst neu berechneten Anteilsvektoren, anschließend unabhängiges Maximum. Für ungewichtet, dweight und anweight geprüft. |
| Ratio-Scope | PASS für Konsistenz, Rohextrema NICHT REPRODUZIERT | `all_de_cases`, positive geordnete Grenzen, identische Grenzen innerhalb der Studie, gemeinsame DE-Gesamtnenner über Fragen und Gewichte sowie alle nichtleeren Aggregatequotienten innerhalb der Grenzen. Aggregate können die tatsächlichen Einzelpersonenextrema nicht identifizieren. |
| Kein Design-SE/CI/Score/Norm | PASS im geprüften Pfad | `no_design_basis`, keine Unsicherheitswerte; getrennte Studien, keine gemeinsame Personen-/Kovarianzrechnung. Gewichtsrollen entsprechen pspwght primär, dweight/unweighted Sensitivität, anweight Diagnose; kein zusätzliches dweight-Produkt im geprüften Quellpfad. |
| Renderer und Exportgrenze | PASS technisch begrenzt | Closed shape, feste Auswahl, Vertragshash, feste Nullstatus, keine Promotion, deterministische Ausgabe, unveränderte Inputs und sichere Metadatendarstellung. Kandidaten-/Reviewhashsyntax allein authentifiziert keine Reviewer oder Dateien. |
| Acht Rubriken und B25-spezifische Berichtskontexte | OFFEN | Das aktuelle Listing ist keine vollständige Umsetzung der geplanten inhaltlichen Darstellung; siehe RV2-M-F03. |

Das private unabhängige Oracle verwendet `Fraction.from_float` für die exakt repräsentierten endlichen Aggregatefloats und exakte Integerbrüche für Counts. Es bildet gültige Gewichtssummen nochmals aus allen Kategoriegewichtssummen, prüft sie gegen den ausgewiesenen Itemnenner und berechnet Quotienten sowohl mit dem selbst gebildeten als auch mit dem ausgewiesenen Nenner. Proportions-/Maximendifferenzen werden auf dem Anteilsmaßstab mit der festgelegten Arithmetiktoleranz geprüft, Gewichtspartitionen relativ. Das ist eine Rechnung aus bereits gerundeten Aggregatsummen, keine Wiedergewinnung ursprünglicher Einzelgewichte. Rationale Prüfergebnisse stehen ausschließlich im geschützten `aggregate-oracle.json`.

### RV2-M-F01 — unabhängige Rohprovenienz und Ratioextrema bleiben offen

**Ort:** `pipeline/policy_access_v2.py:286`, `:349`, `:435`; `pipeline/policy_analysis_v2.py:255`; `pipeline/policy_export_v2.py:268`; die fünf Runpins und der gepinnte Inputidentitätskontext.

**Evidenz:** Der Quellpfad prüft vor Raw-I/O Gate-/Reportbytes, Freeze, Manifestartefakte, die tatsächlich ausgeführten Librarydateien und Vertrags-/Katalogidentität; Rawhash/Bytezahl liegen vor CSV-Decoding, alle deutschen Runden-/Editionsmetadaten vor ausgewählter Antwortnormalisierung. Die vorhandenen Aggregate und Receipts stimmen intern mit diesen Pins überein. Dieser Reviewer hat weder den Pfad mit tatsächlichen Rohdaten ausgeführt noch Rohbytes, Header, Kennungen, Downloadherkunft oder Einzelgewichte geprüft. Die zugelassene Form enthält nur Aggregate. Viele Einzelgewichtskonfigurationen können dieselben Summen haben; Aggregatequotienten erlauben Widerspruchsprüfungen der angegebenen Grenzen, keine unabhängige Berechnung ihres Min/Max.

**Auswirkung:** Die korrekten Aggregatrechnungen und tatsächlichen Hashbindungen tragen ein begrenztes historisch-deskriptives Urteil, keine unabhängige Raw-/Download- oder Probandenreproduktion. Nicht als empirisch bestandene Metadaten-/Einzelzeilenprüfung dieses Reviewers berichten.

**Minimalfix:** Keine Zahlenänderung erforderlich. Die Grenze in Exportbegründung und wissenschaftlichen Geltungsaussagen erhalten. Falls später unabhängige Raw-/Extremareproduktion behauptet werden soll, braucht sie einen gesondert erlaubten nachvollziehbaren Nachweis. Für dieses begrenzte Urteil kein Blocker.

### RV2-M-F02 — gesperrte Referenz darf nicht automatisch freigegeben werden

**Ort:** `data/local/policy-v2/ESS10SCe03_2/run.json`, Kandidatenfrage `ESS10SCe03_2:cttresa`; `pipeline/policy_export_v2.py:309`, `:381`, `:437`.

**Evidenz:** Eigene Auswertung der tatsächlichen Kategoriecounts und primären Accountingidentitäten ergibt den gesperrten festen Status; `reference` ist tatsächlich null. Nicht allein dem gespeicherten Status vertraut. In den synthetischen Grenzproben bleibt bei unzulässiger Basis/positiver Kategorie die Referenz null, und eine Freigabe nullreferenzierter Items wird zurückgewiesen.

**Auswirkung:** Das Item bleibt Teil der festen Auswahl, erhält aber keine Referenz, Sensitivität oder geschätzten Anteile und steht nicht in meinen `approvedQuestionIds`. Weder nachträglicher Itemausschluss noch Zusammenlegen/Ersetzen von Kategorien ist gerechtfertigt.

**Minimalfix:** Vorhandene Sperre erhalten; Root muss die konkreten Listen übernehmen beziehungsweise weiter einschränken. Kein Defekt der aktuellen Umsetzung und kein zusätzlicher Rechenblocker.

### RV2-M-F03 — Bericht ist technisch korrekt, geplante Inhaltsdarstellung noch unvollständig

**Ort:** `pipeline/policy_report_v2.py:213`, `:255`, `:287`; `data/politikprofil-v2.fragen.entwurf.json` Felder `primaryTheme`, Wortlaut/Kategorien und `ESS10SCe03_2:scchpldm.uncertainty`; `docs/empirie-plan-v2.entwurf.md`, Abschnitt „Konkrete Auswahl“; Resultpaket `scope.md`.

**Evidenz:** Die API bekommt fünf Einzelstudienverträge und öffentliche Exportshapes. Sie rendert Studien, Fragekennungen und Originalcodezahlen, aber keine acht Themenrubriken, Fragewortlaute oder deutschen Kategorienbezeichnungen. Die Kataloginformationen sind kein Rendererinput. Der synthetische Integrationstest bestätigt die fehlenden Themen und das Fehlen eines B25/B26–B29-/operativen-Nachlaufhinweises. Die allgemeinen Sätze zu Webadministration und Quellenrechten ersetzen den spezifischen B25-Kontext nicht. Der bekannte ESS11-v1-A/B-Kontext wird dagegen ausdrücklich dargestellt. Der B25-Katalogstatus bleibt administrativ unvollständig; seine statische Kategoriebindung und historische Einzelreferenz sind davon getrennt und werden hier nur rechnerisch zugelassen.

**Auswirkung:** Als WIP-Prüflisting ist die Ausgabe nachvollziehbar. Sie darf noch nicht als fertig umgesetztes verständliches Profil unter acht Themen oder als B25-Webadministrationsfreigabe bezeichnet werden. Insbesondere nominale Exportcodes benötigen ihre tatsächlichen Quellenbedeutungen in der späteren Inhaltsdarstellung. Dies ist kein Widerspruch in den Aggregaten, aber eine offene Bedingung für eine eigenständig verwendete endgültige Darstellung.

**Minimalfix:** Für die geplante Darstellung die tatsächlich authentifizierten Kataloglabels, Themenzuordnung und spezifischen Kontextgrenzen sichtbar anbinden; mindestens einen eindeutigen Katalogbezug und B25-Grenzhinweis mitführen. Nullfragen behalten ihre Originalcodes ohne abgeleitete Anteile. Kein neues Scoring, keine neuen Items und keine neue empirische Auswertung. Dieses Methodenurteil gibt das technische WIP-Listing begrenzt frei, nicht die noch fehlende Enddarstellung.

### RV2-M-F04 — sichtbare Hashsyntax ist keine Freigabeauthentifizierung

**Ort:** `pipeline/policy_report_v2.py:132`, `:164`, `:213`; `pipeline/policy_export_v2.py:369`, `:399`.

**Evidenz:** Der Renderer rechnet den vollständigen Einzelstudienvertragshash selbst nach. Kandidaten- und Reviewmanifesthash sind im öffentlichen Shape nur endliche Hexidentitäten, die er nicht aus privaten Kandidaten oder Reviewbytes nachprüfen kann. Die synthetische Probe akzeptiert andere syntaktisch korrekte Hashes, verweigert aber fehlerhafte Hashsyntax. Der Builder kontrolliert formal zwei Rollen/gebundene Kandidaten-/Vertragshashes und die Frageuntermenge, liest jedoch keine Reviewerberichte. Beides ist im Modultext zutreffend offengelegt.

**Auswirkung:** Ein privilegierter Aufrufer könnte formal korrekte Gate-/Exportobjekte konstruieren. Keine automatische Freigabe durch Renderer, Schema oder Statusstring ableiten. Er kann weder positive Kategoriencellcounts noch vier private Anteilsvektoren aus seinem öffentlichen Shape rekonstruieren.

**Minimalfix:** Roots tatsächliche Manifest-/Quellen-/Katalog-/Entscheidungs-/Reportbyteprüfung und explizite Frageuntermenge vor öffentlichem Export beibehalten. Keine neue Authfunktion in die reine Library nötig; für den ausdrücklich extern geprüften Aufruf kein Blocker.

## Tatsächlich ausgeführte technische Prüfung

Alle folgenden Bericht-/Grenzzahlen und Fixtures sind ausdrücklich **SYNTHETISCH** und keine ESS-Ergebnisse. Tatsächliche Aggregate wurden nur im getrennten geschützten Oracle und in Mutation-Rejection-Probes verwendet, nie zu einem scheinbar freigegebenen Export oder Bericht gerendert.

- `python -B -m unittest pipeline.tests.test_policy_report_v2 -v`: 14 neue Renderertests, Exit 0. Fraction-Ausgabe, alle festen Identitäten und Originalcodes, drei Nullstatus, Studien-/Quellenbindung, geschlossene Objektformen, statische Fehler, DOI-Linkregeln, Metadatenescaping, Reihenfolgen und Unveränderlichkeit geprüft.
- Gezielt drei vorhandene Exporttests zu 99/100-, 4/5- und null-Grenzen, verbotener Nullfreigabe sowie Untermenge ohne Zahlen: Exit 0. Keine breite Wiederholung des vorgelagerten Audits oder tatsächlicher Runner.
- Eigene `aggregate_oracle.py`: Exit 0 nach Korrektur eines eigenen initialen Probe-`KeyError` (`inputs` statt tatsächlichem `files` im Inputidentitätskontext). Der erste Probeabbruch war vor Aggregatarithmetik, blieb in `probe-notes.txt` dokumentiert und wurde nicht als Produktfehler ausgegeben. Alle abgeschlossenen tatsächlichen Studienprüfungen PASS; Einzelarithmetik, Regeln und freigegebene IDs im geschützten Oracle.
- Eigene `boundary_probes.py`: Exit 0. Synthetische komplette fünf-Studien-Export-/Rendererintegration mit echter Untermenge, keine Promotion nuller Referenzen, keine Inputmutation, deterministische Studienpermutation; Escaping in jeder gerenderten Metadatenfamilie und Hashtrust-Grenze geprüft. Getrennt tatsächliche Kandidatenkopien mit falscher Edition/Nullstatus, zusätzlichem Feld, entferntem Blankgrund, NaN-Proportion, falschem Ratioscope und falschem Sensitivitätsmaximum: alle korrekt und wertfrei zurückgewiesen; Originalkandidatenhash bleibt unverändert.
- Zusätzliche ausdrücklich synthetische Notaskedprobe: gültige und fehlende Itemnenner bleiben von einer separat nichtgestellten Antwort getrennt; falsche Gesamtpartition wird zurückgewiesen; Inputs bleiben unverändert. PASS.

Unveränderte vorgelagerte Libraries und ihre gepinnten Tests wurden für die relevanten Code-/Grenzbelege gelesen und per Artefakthash gebunden. Frühere Urteile oder angebliche Testausführungen wurden nicht übernommen. Der Vor-Raw-Guard wurde hier statisch geprüft und nicht mit fremden Reviewerdateien/Rohdaten neu ausgeführt. Kein `pnpm check`, Server oder Browserlauf: keine Forschungs-, Vertrags-, Code- oder UI-Datei geändert, nur der autorisierte eigene Review und geschützte Probes.

## Explizite Freigabe je Kandidat

Die folgende Liste betrifft nur die historische kategoriale Referenz der festgehaltenen Kandidatenbytes, ohne aktuelle Norm, SE/CI, Modusäquivalenz, politische Neutralität oder Webverständnis. Sie beruht auf tatsächlicher eigener Aggregatprüfung; kein automatischer Schluss aus vorbereiteten Statusstrings. Roots Exportliste darf nur diese Liste und das getrennte Quellenurteil schneiden, nicht um null/gesperrte Fragen erweitern.

**`ESS5e03_6`**, Kandidat `d29d4acc6ff1a973d8bb920b0ba02afbadc7e7bd378e53374a9363e752945e33`:

`ESS5e03_6:bplcdc`; `ESS5e03_6:dpcstrb`; `ESS5e03_6:hrshsnta`; `ESS5e03_6:dbctvrd`; `ESS5e03_6:lwstrob`; `ESS5e03_6:rgbrklw`.

**`ESS8e02_3`**, Kandidat `0ca02b80692de3b04ce7733c2aca09c1a70e7d85aafc40632d39d99f07d8bca0`:

`ESS8e02_3:gvslvol`; `ESS8e02_3:gvslvue`; `ESS8e02_3:gvcldcr`; `ESS8e02_3:bnlwinc`; `ESS8e02_3:eduunmp`; `ESS8e02_3:inctxff`; `ESS8e02_3:sbsrnen`; `ESS8e02_3:banhhap`; `ESS8e02_3:imsclbn`; `ESS8e02_3:wrkprbf`.

**`ESS9e03_3`**, Kandidat `93258369d2f929aa990a11d6aae7dc442eb0d8525eaf6404290c2450f22fb125`:

`ESS9e03_3:sofrdst`; `ESS9e03_3:sofrwrk`; `ESS9e03_3:sofrpr`; `ESS9e03_3:sofrprv`.

**`ESS10SCe03_2`**, Kandidat `e2916511e06254185d3d0394d37fd29e68d225ca6996c16a9a4ac8b42ee5de55`:

`ESS10SCe03_2:fairelc`; `ESS10SCe03_2:dfprtal`; `ESS10SCe03_2:medcrgv`; `ESS10SCe03_2:rghmgpr`; `ESS10SCe03_2:votedir`; `ESS10SCe03_2:gptpelc`; `ESS10SCe03_2:gvctzpv`; `ESS10SCe03_2:grdfinc`; `ESS10SCe03_2:viepol`; `ESS10SCe03_2:wpestop`; `ESS10SCe03_2:scchpldm`; `ESS10SCe03_2:vteurmmb`; `ESS10SCe03_2:keydec`; `ESS10SCe03_2:imsmetn`; `ESS10SCe03_2:imdfetn`; `ESS10SCe03_2:impcntr`.

**`ESS11e04_2`**, Kandidat `f36960ab75a2ac357d92b373013f51767a88aff98759061511b86dff6c3e05c2`:

`ESS11e04_2:gincdif`; `ESS11e04_2:euftf`; `ESS11e04_2:eqparep`; `ESS11e04_2:eqparlv`; `ESS11e04_2:freinsw`; `ESS11e04_2:fineqpy`.

**Ausdrücklich nicht freigegeben:** `ESS10SCe03_2:cttresa`. Referenz bleibt null.

**Endurteil:** ACCEPTED_BOUNDED für die genannten historischen Einzelreferenzen und die geprüften technischen WIP-Berichtsgrenzen. Keine unabhängige Rohreproduktion und keine vollständige Inhalts-, Human-, Rechts- oder Releasefreigabe.
