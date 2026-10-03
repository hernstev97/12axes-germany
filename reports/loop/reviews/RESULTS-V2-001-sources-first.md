# RESULTS-V2-001 — Quellen, Konstrukte und faire Interpretation

Datum: 2026-10-03. Rolle: `sources_constructs_fairness`. Unabhängiges Ersturteil innerhalb des ausdrücklich begrenzten Pakets, gleiche Codex-Modellfamilie.

**Entscheidung: ACCEPTED_BOUNDED.** Die unten ausdrücklich genannten Fragen dürfen aus Sicht dieser Rolle als getrennte, quellengebundene historische Kategorienreferenzen in den Ergebnisübergang eingehen. `ESS10SCe03_2:cttresa` erhält keine Freigabe. Keine Freigabe einer gemeinsamen politischen Struktur, eines Gesamtprofils mit empirisch belegter Vollständigkeit, aktueller Bevölkerungs-/Wählervergleiche, Parteienzuordnung oder neuer Webadministration. Der gegenwärtige codebasierte Renderer ist ein technischer Anhang; die geplante verständliche Darstellung unter acht Themenrubriken ist damit nicht fertig oder abgenommen. Befund SCF-R01 hält diese Grenze konkret fest.

Dies ist nur mein Rollenurteil. Es ersetzt weder das getrennte Methodenurteil noch Roots gebundenen Exportentscheid, eine tatsächliche Rohreproduktion, menschliche Verständnis-/Gestaltungsprüfung, wissenschaftliche Gesamtvalidität, Neutralität, Rechtsprüfung oder Releaseabnahme.

## Identität und tatsächlich geprüfte Eingänge

Erstes gelesenes Artefakt war `reports/loop/packages/RESULTS-V2-001/v1/manifest.json`. Erwarteter und tatsächlicher SHA256:

`3299ad658cca7cbb5621c6f062d4133b831e74d8bf4ca71bcb8e67fff56c4434`

Die tatsächlichen Bytes aller 29 `publicArtifacts` und aller fünf `privateAggregates` wurden vor und nach den Prüfproben gegen dieses Manifest geprüft: **PASS**. Die fünf exakt bezeichneten Aggregate sind ignored und haben Modus `0600`: **PASS**. Keine Rohdatei, kein Rohverzeichnis, Header, Personenkennungswert oder tatsächliches Parteifeld wurde gelesen. Es gab auch keine Aufzählung oder Dateimetadatenabfrage unter `data/raw/`. Der deklarierte Inputhash im jeweiligen Lauf wurde nur mit dem öffentlichen Studienvertrag verglichen; das ist kein neuer Rohdatei- oder Downloadnachweis.

| Studie | SHA256 der tatsächlichen Aggregate-Datei | Kanonischer Kandidaten-SHA256 |
| --- | --- | --- |
| ESS5e03_6 | b7a430ab14a9ae5b2f6537abd0fe968bb09d3b42bfdde9e21f0bba79d94426c6 | d29d4acc6ff1a973d8bb920b0ba02afbadc7e7bd378e53374a9363e752945e33 |
| ESS8e02_3 | 6ec04807e401aeb4c0c46dd833c676bb3700f235a5fdbb8c39cc7fd9f0e8d557 | 0ca02b80692de3b04ce7733c2aca09c1a70e7d85aafc40632d39d99f07d8bca0 |
| ESS9e03_3 | 2eda8b76f037fd089110dfe7412757a171d6eee7eed755aad78976a6e9c108a1 | 93258369d2f929aa990a11d6aae7dc442eb0d8525eaf6404290c2450f22fb125 |
| ESS10SCe03_2 | 1b9546154b2ed3daecebf787f24e709e6e6009e69715f20baae5c4788032c79d | e2916511e06254185d3d0394d37fd29e68d225ca6996c16a9a4ac8b42ee5de55 |
| ESS11e04_2 | ffce2bd934da6ca789be619a70283ec8afd3dc9c3bce994c7d1d7b16e5f1ee82 | f36960ab75a2ac357d92b373013f51767a88aff98759061511b86dff6c3e05c2 |

Auch die kanonischen Studienvertragshashes stimmen jeweils mit dem Manifest überein. Laufpins für den öffentlichen Vertrag, das vorgelagerte Manifest, Freeze und Gate stimmen mit den jeweiligen gepinnten Bytes überein. Keine daraus folgende Autorenverteidigung oder andere Rollenentscheidung wurde eingelesen oder als eigenes Urteil übernommen. Parent-Verlauf, Handoff, andere Rollenberichte und Autorenberichte wurden nicht gelesen.

## Prüfregeln und Befunde

Der tatsächlich geprüfte Katalog ist `data/politikprofil-v2.fragen.entwurf.json`, SHA256 `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4`; sein Pin im Vertrag stimmt. Der Vertrag ist `data/analysevertrag.v2.entwurf.json`, SHA256 `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b`.

Für jede ausgewählte Frage wurden Wortlaut, Einleitung, Antwortstamm, Situation, Antwortbedeutungen, Kategorie-/Missing-/Notasked-Codes, Originalfrage, nationale Seitenfundstellen, Metadatenversionen und Studienbindung im erlaubten Katalog geprüft. Die tatsächlichen Kandidaten wurden anschließend mit genau diesen Bindungen abgeglichen. Das gilt auch für die statischen PAPI-/CAWI-Wortlaut- und Kategorienzuordnungen des ESS10-SC-Instruments. Keine Quelle wurde neu abgerufen; die im Katalog aufgeführten ursprünglichen PDF-/API-Dateien liegen außerhalb dieses engen Byte-Manifests und wurden nicht zusätzlich geöffnet. Die Prüfung bestätigt daher die Übereinstimmung mit dem gepinnten Quellenkatalog, keinen unabhängigen Neuabgleich der Originaldateien.

| Kriterium | Status und Grenze |
| --- | --- |
| Studien-, Editions-, Kandidaten- und Vertragsidentität | PASS innerhalb der gepinnten Artefakte; kein unabhängiger offizieller Downloadchecksum-Nachweis. |
| Originalcodes einschließlich unbeobachteter gültiger Kategorien | PASS: Reihenfolge und vollständige Codes stimmen zwischen Katalog, Vertrag und tatsächlichem Kandidaten überein. Keine Polung, Kategorienzusammenlegung oder Mittelwertbildung. |
| Missing und Notasked | PASS: API-Gründe bleiben getrennt. Technische Leere bleibt `export_blank_unclassified`; keine erfundene Verweigerung, Mitte oder politische Gegenposition. Keine deklarierten Notasked-Codes in dieser Auswahl. |
| Vorab gebundene Referenzheuristik und Nullregel | PASS: aus den tatsächlichen Aggregaten eigenständig anhand der festen Basis-/Positivzellenregeln geprüft, nicht nur Statusstrings übernommen. Keine Validitäts-, Präzisions- oder Anonymitätsbescheinigung. |
| Tatsächliche Kandidatenstruktur und Aggregatekonsistenz | PASS in `validate_reference_candidate` für jede Studie; dies ist eine technische Prüfung mit der gepinnten Bibliothek, keine unabhängige Rohreproduktion und kein Ersatz für den Methodenreview. |
| Quellenjahr, Population, Modi und Kontext | PASS für die deklarierte historische Reichweite; tatsächliche vollständige Abdeckung oder Modusäquivalenz bleiben unbewiesen. |
| Rubriken und Benennungen im geplanten Messmodell | BOUNDED PASS: getrennte konkrete Präferenzen/Prinzipien, keine latenten Dimensionen oder Charakterurteile. Die verständliche Enddarstellung bleibt geplant. |
| Standalone-Interpretierbarkeit des aktuellen Renderers | OPEN, SCF-R01. Keine Abnahme der geplanten Darstellung unter acht Themenrubriken. |
| Neue Webinstrumentäquivalenz, unabhängige Bestätigungsdaten, Neutralität/Gesamtvalidität | Nicht nachgewiesen und nicht freigegeben. |

### SCF-R01 — Der Renderer ersetzt keine semantisch vollständige Ergebnisdarstellung

**Status:** offener Darstellungsbefund; kein Ausschluss der korrekt gebundenen historischen Zahlenreferenzen. Die Freigabe gilt für den quellengebundenen Referenzexport und einen technischen Anhang, nicht für einen bereits verständlichen eigenständigen Themenbericht oder Webtest.

**Fundstelle:** `pipeline/policy_report_v2.py:213`, insbesondere die Frageabschnitte ab Zeile 286 und die Code-/Anteilszeilen ab Zeile 301; `pipeline/policy_export_v2.py:391`. Vergleichsgrundlage: `reports/loop/packages/RESULTS-V2-001/v1/scope.md:3`, Katalogfelder `wordingDe`, `introductionsDe`, `responseStemDe`, `situationDe`, `categories[].labelDe` und `primaryTheme` sowie Vertrag `boundaries.B25Scope`.

**Beleg:** Die Exportform enthält Frage-IDs und Originalcodes; der Renderer bekommt nur Exporte und Studienverträge, nicht den semantischen Katalog. Er schreibt keine deutschen Originalfragen, Kategorienbedeutungen, Themenüberschriften oder spezifische B25-Geltungsgrenze. Eine ausdrücklich **SYNTHETISCHE**, ausschließlich nullhaltige Exportform mit den tatsächlichen öffentlichen Vertragsmetadaten bestätigt diese Auslassungen. Der Text wurde nur im Speicher geprüft, nicht als empirischer Bericht geschrieben oder ausgegeben; es gab weder erfundene Anteile noch einen Builder-Aufruf mit erfundener Freigabe.

**Auswirkung:** Codes allein erklären beispielsweise weder die gültigen EU-Nichtpositionsantworten noch den normativen Demokratiebezug oder das Paar-/Elternzeitszenario. Ein isolierter technischer Bericht darf deshalb nicht als die im Scope geplante verständliche Darstellung unter acht Themenrubriken ausgegeben werden. Der aktuelle Text behauptet diese Fertigstellung allerdings auch nicht und begründet keine gegenteilige inhaltliche Interpretation; die Zahlenreferenzen bleiben über den gepinnten Katalog zuordenbar.

**Minimale Korrektur für die spätere erklärende Darstellung:** den gepinnten Katalog ausdrücklich am Artefakt verknüpfen und je Frage Wortlaut/Kontext und Codebedeutungen zugänglich machen; die Rubriken als Inhaltsordnung kennzeichnen. Für B25 die begrenzte historische Verwendung und den unbelegten operativen CAWI-Nachlauf ausdrücklich nennen. Dafür keine neuen Kategorien, Scores, Freigaben oder empirischen Berichte erfinden. Bis dahin den Renderer als technischen Anhang behandeln und die Themen-/Webdarstellung als geplant beschreiben.

### SCF-R02 — B25 ist nur als historische statische Einzelfrage gebunden

**Status:** BOUNDED PASS für `ESS10SCe03_2:scchpldm`; neue Webadministration und Originalablaufreproduktion bleiben offen.

**Fundstelle:** Katalog `ESS10SCe03_2:scchpldm` ab Zeile 6336, `remainingBindings` ab Zeile 10544; Vertrag `boundaries.B25Scope` ab Zeile 1274.

**Beleg:** Die Einleitung zur Meinungsdifferenz zwischen Regierung und Bevölkerungsmehrheit, die Frage nach dem Besten für Demokratie im Allgemeinen und beide Antwortalternativen sind statisch gebunden. PAPI-PDF12/13 und CAWI-PDF162 werden präzise unterschieden. Fehlend sind nur die behauptete Reproduktion des B26–29-Nachlaufs beziehungsweise dessen operative CAWI-Ausführung. Der Kandidat stimmt bei den beiden gültigen Codes und den gesonderten Missing-Gründen mit dem Vertrag überein; die feste Referenzheuristik ist erfüllt. Die offenen Felder werden nicht als bestanden erklärt.

**Auswirkung:** Eine begrenzte historische Verteilung dieser Originalantwort ist zulässig; daraus folgt weder eine Demokratie-/Populismuseigenschaft noch empirische Gleichwertigkeit einer neuen Folge „Einzelfrage, dann nächste ausgewählte Frage“. Allein das pauschale Katalogfeld `bindingStatus=incomplete` rechtfertigt hier keinen Ausschluss der separat vollständigen statischen historischen Bindung.

**Minimale weitere Arbeit:** Die oben beschriebene Grenze bei erklärender Ausgabe mitführen; vor neuer Administration den geänderten Kontext/Nachlauf menschlich prüfen. Keine Nachlauf- oder Modusgleichwertigkeit aus der Quellenkorrespondenz ableiten.

### SCF-R03 — Die gesperrte Gerichtsfrage bleibt gesperrt

**Status:** WITHHELD; keine Freigabe für `ESS10SCe03_2:cttresa`.

**Fundstelle:** tatsächlicher gepinnter ESS10SCe03_2-Kandidat, Quellenfrage `ESS10SCe03_2:cttresa`; Vertrag ab Zeile 759 und Publikationsregeln; Katalog ab Zeile 4362.

**Beleg:** Eigenständige Auswertung der vorab gebundenen Heuristik ergibt `withheld_base_or_cell_count`; die Kandidatenreferenz ist tatsächlich null. Die Quellenbindung ist nicht das Problem. Dieser Bericht veröffentlicht keine zugrunde liegenden Häufigkeiten oder kleinen Zellen.

**Auswirkung:** Die Originalfrage und ihre Kategorien bleiben Teil des Inhaltsbestands, aber ohne Zahlenreferenz. Sie darf nicht automatisch freigegeben, zusammengelegt oder aus dem Modellbestand entfernt werden.

**Minimale Korrektur:** keine am Kandidaten nötig; die Nullreferenz und die fehlende Freigabe unverändert durch den Export führen.

### SCF-R04 — Unabhängige Roh- und Originalquellenreproduktion wurde nicht durchgeführt

**Status:** ausdrücklich nicht nachgewiesen, kein als bestanden umbenannter Prüfpunkt.

**Fundstelle:** Paket-Scope Zeilen 7–11; Quellennachweise im gepinnten Katalog; Laufpins in den fünf erlaubten Aggregaten.

**Beleg:** Die Prüfung nutzt tatsächliche sichere Aggregate, bytegeprüfte öffentliche Verträge und den gepinnten Quellenkatalog. Sie öffnet weder Rohdaten noch die zusätzlichen ursprünglichen PDF-/API-Caches. Die Bibliothekskonsistenzprüfung teilt Implementierung mit dem Exportpfad. Sie kann Auswahl-, Routing-, Gewichtungs- oder Importfehler auf Rohzeilenebene nicht unabhängig ausschließen.

**Auswirkung:** Keine Behauptung unabhängiger vollständiger Reproduktion, empirischer Instrumentvalidierung oder unangetasteter Bestätigung. Das begrenzte Rollenurteil ist trotzdem möglich, weil die überprüften tatsächlichen Kandidaten den festgelegten historischen Quellen-/Kategoriebedingungen entsprechen.

**Minimale Korrektur:** diese Grenze im späteren Methodenbericht erhalten. Eine echte unabhängige Roh-/Originaldateireproduktion wäre ein eigener ausdrücklich autorisierter Prüfauftrag; hier wurde sie nicht ausgeführt oder angefordert.

## Geltung, Breite und politische Fairness

Alle fünf Studienverträge deklarieren Personen ab 15 Jahren in Privathaushalten unabhängig von Staatsangehörigkeit; das ist keine reine Wahlberechtigten- oder heutige Wählerpopulation. Editions- und Provenienzfelder stimmen exakt mit dem gepinnten Katalog überein.

| Referenz | Gebundene deutsche Feldzeit und Modi | Maßgebliche Grenze |
| --- | --- | --- |
| ESS5, Edition 3.6 | 2010-09-15 bis 2011-02-03; CAPI | Historischer Polizei-/Rechtskontext. „Heute“ in der Strafverschärfungsfrage meint den damaligen Kontext. Keine umfassende heutige Bürgerrechts-/Sicherheitspolitik. |
| ESS8, Edition 2.3 | 2016-08-23 bis 2017-03-26; CAPI | München ist laut gebundener Designangabe ausgeschlossen. Gewichtung gilt nicht als Reparaturnachweis dieser Abdeckungslücke. |
| ESS9, Edition 3.3 | 2018-08-29 bis 2019-03-04; CAPI | Unterschiedliche Gerechtigkeitsprinzipien; keine gesamte Wirtschaftsordnung oder gemeinsame Skala. |
| ESS10-SC, Edition 3.2 | 2021-10-05 bis 2022-01-04; Papier und CAWI | Selbstadministration, kein deutscher Face-to-face-Ersatz. Der erhaltene Editionshinweis unterscheidet Datei/DOI von älterem Zitationstext. Statische Formkorrespondenz ist keine empirische Modusäquivalenz. |
| ESS11, Edition 4.2 | 2023-05-09 bis 2023-12-21; CAPI | Frühere v1-A/B-Neunerantworten sind bekannt; die zusätzlichen Fragen stammen aus derselben Erhebung. Keine unangetastete neue Bestätigung. |

Die Themenordnung trägt eine breite, aber unvollständige Auswahl getrennter Einzelangaben. Wirtschaft/Verteilung erfasst Gleichheit, Leistung, Bedarf, Herkunftsprivileg und staatliche Einkommensverringerung, ohne daraus Links-/Rechts- oder allgemeine Wirtschaftseigenschaften abzuleiten. Die fehlenden Markt-/Eigentums- und weiteren Wirtschaftsfragen bleiben Inhaltslücken. Demokratie B1–12 fragt die normative Wichtigkeit für Demokratie **im Allgemeinen**, keine wahrgenommene Umsetzung und keine objektive deutsche Demokratiequalität. Das vollständige Originalblockregister enthält `keydec` als B12; dessen primäre EU-Rubrik legitimiert keine verkürzte Neuadministration des Blocks. B25 bleibt die gesonderte historische Wahl zwischen Responsivität und Planbindung.

Sozialstaatfragen unterscheiden Aufgaben und konkrete Tradeoffs. Der feste Finanzierungsrahmen bei Ausbildung/Arbeitslosenleistungen bleibt erhalten. Klima/Energie behandelt konkrete Instrumente, keine allgemeine Energieträgerposition. Migration trennt Zulassungsgruppen und Bedingungen für Sozialansprüche, ohne aus Antwortgruppen eine Personenmotivation oder tatsächliche Migrationsfolge zu folgern. Gleichstellung/Familie enthält konkrete Eingriffe; die Elternzeitfrage behält das Doppelverdiener-/Verdienst-/Neugeborenen-/Anspruchsszenario, Familienleistungen behalten den Steuertradeoff. Kinderbetreuung zählt primär beim Sozialstaat, nicht doppelt als zusätzliche Breite.

Besonders geprüft wurden die gültigen nominalen EU-Optionen einschließlich leerem/ungültigem Stimmzettel, Nichtwahl und Nichtstimmberechtigung. Sie sind keine Missing-Antworten und keine skalierbaren politischen Zwischenpositionen. Die nominalen Bedingungen bei Sozialleistungsrechten werden ebenfalls nicht in einen Zeit- oder Ideologiescore umkodiert. Zustimmung, Wichtigkeit, Zuständigkeit und nominale Auswahl bleiben getrennt; unterschiedliche Codeorientierungen erhalten keine gemeinsame moralische oder politische Wertung.

Der geplante Aussageumfang beansprucht weder vollständig erfasste Politik noch eine empirisch belegte gemeinsame Struktur, ein Gesamtideologieprofil, Parteipositionen oder aktuelle Wähleranteile. Das ist eine zulässige begrenzte Beschreibung der Auswahl, keine Neutralitätsbescheinigung. Daten- und Dokumentationslizenzen bleiben getrennt, Attribution und konkrete Nutzungsprüfung offen; daraus wird keine Rechtsfreigabe abgeleitet.

## Explizite Fragefreigaben

Nur die folgenden vollständig überprüften und nach der tatsächlichen Kandidatenheuristik referenzfähigen IDs werden in der eigenen Entscheidung genannt. Das ist keine automatische Freigabe aller ausgewählten Fragen. `ESS10SCe03_2:cttresa` fehlt absichtlich; seine Referenz bleibt null.

- ESS5e03_6: `ESS5e03_6:bplcdc`, `ESS5e03_6:dpcstrb`, `ESS5e03_6:hrshsnta`, `ESS5e03_6:dbctvrd`, `ESS5e03_6:lwstrob`, `ESS5e03_6:rgbrklw`.
- ESS8e02_3: `ESS8e02_3:gvslvol`, `ESS8e02_3:gvslvue`, `ESS8e02_3:gvcldcr`, `ESS8e02_3:bnlwinc`, `ESS8e02_3:eduunmp`, `ESS8e02_3:inctxff`, `ESS8e02_3:sbsrnen`, `ESS8e02_3:banhhap`, `ESS8e02_3:imsclbn`, `ESS8e02_3:wrkprbf`.
- ESS9e03_3: `ESS9e03_3:sofrdst`, `ESS9e03_3:sofrwrk`, `ESS9e03_3:sofrpr`, `ESS9e03_3:sofrprv`.
- ESS10SCe03_2: `ESS10SCe03_2:fairelc`, `ESS10SCe03_2:dfprtal`, `ESS10SCe03_2:medcrgv`, `ESS10SCe03_2:rghmgpr`, `ESS10SCe03_2:votedir`, `ESS10SCe03_2:gptpelc`, `ESS10SCe03_2:gvctzpv`, `ESS10SCe03_2:grdfinc`, `ESS10SCe03_2:viepol`, `ESS10SCe03_2:wpestop`, `ESS10SCe03_2:scchpldm`, `ESS10SCe03_2:vteurmmb`, `ESS10SCe03_2:keydec`, `ESS10SCe03_2:imsmetn`, `ESS10SCe03_2:imdfetn`, `ESS10SCe03_2:impcntr`.
- ESS11e04_2: `ESS11e04_2:gincdif`, `ESS11e04_2:euftf`, `ESS11e04_2:eqparep`, `ESS11e04_2:eqparlv`, `ESS11e04_2:freinsw`, `ESS11e04_2:fineqpy`.

Maschinenlesbares Rollenurteil: `reports/loop/reviews/RESULTS-V2-001-sources-decision.json`, exakt SchemaVersion 1 mit Rolle, Manifesthash, Entscheidung und je Studie Kandidatenhash/vollständigen Frage-IDs. Keine Root- oder zweite Rollenentscheidung wurde erfunden.

## Durchgeführte Prüfungen und Grenzen

- Bytepins, Kandidaten-/Vertragshashes, Laufpinbezüge, Quellen-/Kategorie-/Missing-/Notasked-Crosswalk, statische ESS10-Formbindung und eigenständige feste Referenzheuristik: PASS; eigene Probe Exitcode 0. Evidenz ausschließlich unter `outputs/loop/result-v2-001-sources/`, Verzeichnis `0700`, Dateien `0600`; keine tatsächlichen Ergebniszahlen im Bericht oder Tooloutput.
- Gepinnte Reporttests: 14 Tests, Exitcode 0, PASS. **SYNTHETISCH**: In-memory-Formen und Bruchoracles, keine tatsächlichen Exporte, keine Rohdaten oder gespeicherten empirischen Berichte. Sie prüfen unter anderem Nullausgabe, Codes/Reihenfolge, getrennte Studien, Herkunft/Modus/München, historische ESS11-Grenze und Fehler bei sichtbaren Struktur-/Arithmetikänderungen.
- Eigene **SYNTHETISCHE** Null-Renderer-Probe: Quellen-/Nullgrenzen getragen; fehlende deutsche Itemsemantik, Themenordnung und konkrete B25-Prosa als tatsächlichen offenen Darstellungsbefund erhalten. Der Befund wurde nicht durch erfundene Freigaben oder Berichte kaschiert.
- Nicht durchgeführt: tatsächlicher Rohdatenrunner, unabhängige Roh-/Original-PDF-Reproduktion, anderer Modellfamilienreview, neue allgemeine Quellenrecherche, Exportbuilder mit erfundener Entscheidung, realer Statistikexport, Browser-/Serverprüfung, Repository-CI oder Produkt-/Releaseabnahme. Keine davon wird als bestanden behauptet. Getestet wurden nur die für diesen begrenzten Rollenauftrag erlaubten Artefakte.

Keine gemeinsame Forschungs-, Code-, Vertrags-, Gate-, Paket-, State- oder Git-Datei wurde verändert. Geschrieben wurden nur der eigene Erstbericht, die eigene Entscheidung und eigene geschützte Prüfproben. Die Freigabe betrifft die belegte historische Einzelfrage und ihre feste Kategorienreferenz; die offenen methodischen, gestalterischen und menschlichen Abnahmen bleiben offen.
