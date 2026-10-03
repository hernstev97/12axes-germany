# RESULTS-V2-PRESENTATION-001/v2 — gezielte Quellen-Nachprüfung P01/P02

Datum: 2026-10-03. Rolle: `sources_constructs_fairness`. Geprüft werden ausschließlich SCF-P01, SCF-P02 und der damit verbundene authentische Frontendbindungsschritt. Grundlage des Befundvergleichs ist mein eigener unverändert erhaltener Bericht `RESULTS-V2-001-sources-presentation-round1.md`, SHA256 `010c73e3934e40645928a24dc6a2ec54ace2085eb2db28414616e7343a3c8640`.

**Urteil: ACCEPTED_BOUNDED. SCF-P01 und SCF-P02 sind in der festen v2-Prüffassung geschlossen. Die geprüfte öffentliche Frontend-Artefaktbindung erhält die zuvor angenommenen 42 Einzelreferenzen und `ESS10SCe03_2:cttresa` null.** Es entsteht keine neue Fragefreigabe, Auswahl, Schätzung, Gewichtung oder numerische Gesamtbewertung. Die bisherigen gültigen Ergebnisurteile und die fachliche Schließung von SCF-R01 werden im unveränderten Umfang weiterverwendet.

Das Urteil stammt weiterhin aus derselben Codex-Modellfamilie. Es bescheinigt keine Neutralität, vollständige wissenschaftliche Validität, menschliche Verständlichkeit, Instrumentgleichwertigkeit, Rechts- oder Releaseabnahme.

## Feste Bytes und Zugriffsgrenze

Zuerst gelesen und gegen den vorgegebenen Hash geprüft: `reports/loop/packages/RESULTS-V2-PRESENTATION-001/v2/manifest.json`.

Erwarteter und tatsächlicher SHA256: `744edecd3e4072b34e4c7b2408b77236dc40525e0fdb693e4f682cc1d3fc973e`.

Alle **65 öffentlichen Pins** wurden als tatsächliche Bytes vor und nach den gezielten Prüfungen verifiziert. Die 30 öffentlichen Originalcaches wurden erneut nur gehasht; für P02 wurde der bereits gebundene ESS11-Zitationstext gezielt gelesen. Eine neue allgemeine Quellenlektüre fand nicht statt.

Andere Rollenberichte und Entscheidungsdateien wurden ausschließlich für die tatsächliche Hashbindung als Bytes gelesen, nicht als Reviewerprosa oder Urteil dekodiert. Mein eigener früherer Quellenentscheid wurde als bestehende Itemfreigabeliste verwendet. Kein neuer Methodenbericht, keine Autorenverteidigung, kein Root-Handoff, keine Agenten-, Elternhistorien- oder State-Datei wurde gelesen.

Keine Rohdaten, privaten Aggregate oder Antwortdateien wurden geöffnet, gehasht, aufgelistet oder auf Dateimetadaten geprüft. Insbesondere kein Zugriff auf `data/raw/` oder `data/local/`; private Pfadbezüge im alten gepinnten Manifest bleiben Metadaten und werden nicht traversiert. Keine Netzwerk-, Auth-, Installations-, Server-, Browser-, Datenrunner-, Claude-, Delegations- oder Git-Aktion.

## SCF-P01 — geschlossen für den aktuellen thematischen Bericht

**Fundstelle der Korrektur:** `pipeline/policy_thematic_report_v2.py:20`–`25`. Der neue lokale Textformatter verwendet HTML-Escaping mit `quote=False` und erhält anschließend das Markdown-Escaping. Apostrophe und Anführungszeichen bleiben Text; HTML-Begrenzer, Ampersand und Markdown-Syntax bleiben abgesichert. Die Missingtabellen verwenden diesen Formatter, unter anderem Zeile 253. Gepinnter Bibliotheks-SHA256: `7436cf96cffbf83d6dfdbedf5a320326b0c702037cc24e36e019264519f353bb`.

**Tatsächlicher Anzeigevergleich:** Der frühere Formatter liefert weiterhin sichtbaren Entitytext `Don&#x27;t know`. Der neue Formatter liefert unter dem tatsächlich vorhandenen CommonMark-Parser sichtbaren Text `Don't know`. Die tatsächlichen Missing-Kontexttabellen des aktuellen Berichts wurden gegen die gebundenen API-Gründe geprüft; das Apostroph ist erhalten, die frühere beschädigte Folge fehlt. Erste Fundstelle im Bericht: Zeile 136. Es genügte nicht allein die Suche nach einer passenden Quellzeichenfolge.

Zusätzliche ausdrücklich **SYNTHETISCHE** Textproben prüfen Apostrophe, doppelte Anführungszeichen, Ampersand, Backslash, HTML-/Bild-/Scriptfragmente, Link-/Bild-/Betonungssyntax und Entitytext. Der Parser gibt jeweils den ursprünglichen Text zurück und erzeugt aus diesen Fragmenten keine aktiven HTML-, Link-, Bild- oder Betonungselemente. Die zwei gezielt ausgewählten gepinnten Tests zur CommonMark-Anzeige und zur sicheren HTML-/Markdown-/Linkbehandlung bestehen; der optionale CommonMark-Test wurde tatsächlich ausgeführt, nicht übersprungen.

Der reine Renderer erzeugt aus den authentischen öffentlichen Exporten, dem unveränderten Vertrag und Katalog exakt die aktuellen Berichtsbytes, SHA256 `470c73eb0cb3c2fa6569773035fbe5444507a7c15fd11253b306c7120d07dc7f`. Die Eingaben bleiben unverändert. Wird ausschließlich der Textformatter im Arbeitsspeicher durch den früheren Formatter ersetzt, entsteht wieder der zuvor geprüfte Bericht-SHA256 `72b87cf11270a968abbb1d6b0cf89b742c893657d6162351b4d45be7b92aaf74`. Dieser Vergleich bestätigt die isolierte Darstellungsänderung; kein neuer empirischer Bericht wurde geschrieben.

**Befundschluss und Grenze:** Der offene Apostrophfehler im aktuellen thematischen Bericht ist behoben, ohne die getestete Absicherung des Markdowntexts aufzugeben. Der alte technische Formatter in `pipeline/policy_report_v2.py` ist unverändert; eine globale Reparatur aller möglichen Aufrufer wird nicht behauptet. Seine fortbestehende alte Anzeige wurde als Kontrollbeobachtung erhalten. Diese gezielte Korrektur ist keine allgemeine Sicherheits- oder Browserdarstellungsabnahme.

## SCF-P02 — geschlossen als Übereinstimmung mit der Primär-Zitationsvorgabe

**Fundstelle der Korrektur:** `data/reference-v2/README.md:11`, aktueller SHA256 `eb3d13cf1a423c3db43315a268eafa429ba92f8a579a89fe70f650c689fbd9d8`. Der ESS11-Dokumentationslink lautet jetzt `https://doi.org/10.21338/ess11-2023`.

**Primärbeleg:** `outputs/loop/breadth-data-001/sources/ess11-study-access-metadata.json:1`, unveränderter SHA256 `19736f79eeabef664298fb1d0b23a94007716d7a41d1e7f84679e85797963430`. Das Feld `data.search.studyMetadata.archive.citationRequirement.en` bindet genau diese Dokumentations-DOI. Studymetadaten-ID `412db4fe-c77a-4e98-8ea4-6c19007f551b`, Version 226. Vertrag, Quellenkatalog und Ergebnisbericht waren bereits passend gebunden und bleiben es.

Der aktuelle README-Link stimmt mit dieser tatsächlichen Primärangabe überein. Ersetzt man allein diesen Link im Arbeitsspeicher wieder durch die frühere `nsd-ess11-2023`-Variante, erhält man exakt den alten README-SHA256 `a2917e6b57c59e96298345e526e9311de82b1422cfbb9a8bb1cfabc0684ba57c`. Damit ist auch die Begrenzung der README-Änderung auf diesen einen Link nachgewiesen.

**Befundschluss und Grenze:** Die konkrete Attributionsabweichung ist geschlossen. Die ursprüngliche Daten-DOI `10.21338/ess11e04_2` bleibt unverändert und mit der Primärquelle übereinstimmend. Die fünf numerischen Exportdateien sind gegenüber der vorherigen Prüffassung vollständig bytegleich. Aus diesem Metadatenvergleich folgt keine Aussage zur Erreichbarkeit des DOI-Resolvers oder zum möglichen Aliasstatus der früheren Variante. Dafür wurden keine neuen Webabrufe vorgenommen und frühere erfolglose Abrufe nicht als Gültigkeitsprüfung übernommen.

## Verbundene authentische Frontendbindung

Geprüft wurden die neu gepinnten Dateien `generate-reviewed-references.mjs`, `reviewed-historical-references.ts`, `reference-generator.test.mjs`, `reference-binding.ts` und `public-catalogue.ts` unter `web/src/app/policy-draft/`.

Die feste öffentliche Generator-Allowlist, ab Zeile 19, stimmt vollständig mit den aktuellen Manifestpins überein. Sie enthält die korrigierte README, die unveränderten fünf Exportdateien sowie die gebundenen alten Entscheidungs-/Berichtbytes und den öffentlichen Katalog. Der Generator öffnet keine aus einer Entscheidung übernommenen privaten Pfade. Die Herkunftsmetadaten des tatsächlich generierten Moduls übernehmen genau diese Pins. Die Originalberichte werden dadurch authentifiziert, ihre Prosa wurde nicht als Argument für mein Urteil gelesen.

Der reine Projektor, `reference-binding.ts:103`, prüft unter anderem Edition, Kandidatenbindung, gleiche Freigabeinventare, Originalcodes und das zurückgehaltene Item. Die Verbindung einer nicht angenommenen Frage mit Referenzzahlen wird ab Zeile 247 zurückgewiesen. Die Projektion ab Zeile 308 kopiert veröffentlichte Werte nach Frage-ID und Originalcode; sie schätzt keine neuen Ergebnisse.

Meine unabhängige Probe vergleicht den tatsächlich geladenen öffentlichen Frontend-Katalog mit dem unveränderten Fragenkatalog: alle 43 Original-IDs, die im Adapter enthaltenen Originalfragen, Einleitungen, Stamm-/Situations-/Instruktionsfelder, Kategorien mit ihren Bedeutungen und Druck-/Exportcodes, Missingbindung, Studienangaben und Instrument-/API-Feldbindungen stimmen überein. Das Modul enthält genau die 42 IDs aus meinem bestehenden Quellenentscheid und den ausdrücklichen Null-Eintrag für `cttresa`. Seine veröffentlichten Werte sind nach Originalfrage und Code exakt kopiert. Dies ist ein Übertragungsabgleich, keine erneute numerische Güteprüfung.

Zusätzlich lässt sich das tatsächliche generierte Modul aus diesen authentischen öffentlichen Eingaben und der bereits bestehenden eigenen Itemfreigabeliste **bytegenau** unabhängig ableiten, SHA256 `d1f0e17dcffe6b40df3664ed6ddbe34cb849a456d036af1c6ab607ab0dad03f2`. Es wurden weder eine zweite Rollenfreigabe erfunden noch Builder mit erfundener Zustimmung aufgerufen.

Vier gezielt ausgewählte gepinnte Authentifizierungstests bestehen: in-memory veränderte Export-, Exportentscheid-, alte Entscheidungs- beziehungsweise eigene Erstberichtbytes werden vor dem JSON-Dekodierungsschritt zurückgewiesen. Die übrigen Generator-Tests und der erfolgreiche echte CLI-Build wurden nicht ausgeführt, weil sie die andere Rollenentscheidung dekodieren. Die tatsächliche öffentliche Bindung und die Modulbytegleichheit wurden wie beschrieben unabhängig geprüft. Ungeprüfte erfolgreiche Receipt-Dekodierung wird nicht als durchgeführt ausgegeben.

**Grenze:** Diese Annahme betrifft die authentische, deterministische öffentliche Artefaktprojektion. Sie beweist keine vollständige Originaladministration im Frontend, operative CAWI-/B25-Folge, neue Modusäquivalenz oder Verständlichkeit einer laufenden Website. Nicht gepinnte App-Helfer wurden nicht gelesen; für die reine Datenauswertung wurde der Freeze-Import ausschließlich im Arbeitsspeicher durch eine Identitätsfunktion ersetzt. Keine Website wurde gestartet oder bedient. Die ursprünglichen Zeit-, Populations-, Themen- und statischen B25-Grenzen bleiben bestehen.

## Tatsächlich ausgeführte Checks und erhaltene Originale

| Check | Ergebnis |
| --- | --- |
| Manifest und sämtliche 65 öffentlichen Pins vor/nach | PASS, tatsächliche Bytes. |
| Aktueller CommonMark-Text und sichere Textfragmente | PASS; tatsächliche Missinglabels plus ausdrücklich synthetische Proben. |
| Zwei gezielt ausgewählte gepinnte Python-Tests | PASS, Exitcode 0, kein ausgewählter Test übersprungen; synthetische Inputs. |
| README gegen gepinnte ESS11-Primärangabe | PASS; exakt eine Dokumentationslinkänderung, Daten-DOI erhalten. |
| Fünf numerische Exporte | Vorherige Bytehashes unverändert; keine Neuschätzung oder neue Auswahl. |
| Reine tatsächliche Bericht-/Modulreproduktion | PASS, Bytegleichheit; nur im Arbeitsspeicher, keine gemeinsamen Ausgaben geschrieben. |
| Vier gezielt ausgewählte gepinnte Node-Authentifizierungstests | PASS, Exitcode 0; Byteveränderungen ausschließlich im Arbeitsspeicher. |
| Eigene unabhängige Frontendprobe | PASS nach Korrektur eines eigenen relativen Importpfads. Der erste QA-Aufruf scheiterte mit `ERR_MODULE_NOT_FOUND`; das war ein Probeeinrichtungsfehler und kein Fehler der geprüften Repositorydateien. |

Eigene QA liegt ausschließlich unter `outputs/loop/result-v2-001-sources-presentation-p01-p02-round1/`, Verzeichnis `0700`, Dateien `0600`. Als neuer öffentlicher Rollenbericht wird ausschließlich diese Datei geschrieben. Mein vorheriger Präsentationsbericht bleibt SHA256 `010c73e3934e40645928a24dc6a2ec54ace2085eb2db28414616e7343a3c8640`; ursprünglicher Erstbericht und Entscheidungs-JSON behalten ebenfalls ihre Pins. Keine gemeinsame Forschungs-, Code-, Vertrags-, Gate-, Paket-, State- oder Git-Datei wurde geändert.

Es gibt in diesem engen Prüfumfang keinen neu offenen Quellenbefund. Die fehlende unabhängige Rohreproduktion, politische Neutralität, empirische Gesamtvalidität, heutige Bevölkerungsnorm, gemeinsame Skalenstruktur, menschliche Abnahme und Release bleiben außerhalb dieses Urteils. Gleiche Modellfamilie und authentische Herkunftsbytes heben diese Grenzen nicht auf.
