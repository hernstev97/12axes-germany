# POLICY-THEMATIC-REPORT-V2 — begrenzter Autoren-Erstbericht

3. Oktober 2026. Autorrolle: thematische Darstellung und reproduzierbare öffentliche Berichtserzeugung. **WIP bis zur gezielten unabhängigen Präsentationsprüfung.** Keine neue empirische Auswahl, Berechnung aus Rohdaten, Gesamtvaliditäts-, Neutralitäts-, Human-, Rechts- oder Releaseabnahme.

Der neue Bericht stellt die 42 von Root gebundenen öffentlichen historischen Einzelreferenzen dar und behält alle 43 Originalfragen. `ESS10SCe03_2:cttresa` bleibt ohne Zahlenreferenz. Acht Rubriken ordnen Inhalte; sie sind keine Messdimensionen. Originalkontexte, deutsche Kategorienbedeutungen, Druck- und Exportcodes, Quellenfundstellen und Studienprovenienz werden zusammen mit den bereits veröffentlichten Zahlen zugänglich.

## Neue Dateien und API

Geschrieben wurden ausschließlich diese fünf neuen Dateien und eigene ignorierte Prüfnachweise unter `outputs/loop/policy-thematic-report-v2/`:

- `pipeline/policy_thematic_report_v2.py`: reine API `render_thematic_report(study_exports, analysis_contract, catalogue) -> str`, ohne IO, CLI oder neuen Schätzer.
- `pipeline/tests/test_policy_thematic_report_v2.py`: synthetische Rendering-, Quellen-/Codebindungs-, Null-, Fehler- und Buildguardtests. Keine tatsächlichen Befragungsantworten in Fixtures.
- `scripts/build-policy-v2-report.py`: fester lokaler Public-only-Aufruf; schreibt ausschließlich `reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md`. `--check` vergleicht stattdessen die vorhandenen Bytes. Keine frei wählbaren Eingabe-/Ausgabepfade.
- `reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md`: deterministisch erzeugter thematischer WIP-Bericht aus tatsächlich erlaubten öffentlichen Exporten.
- Dieser neue Autoren-Erstbericht. Frühere Autorenberichte wurden nicht bearbeitet.

Der reine Renderer ruft zuerst den **unveränderten** `render_historical_report` aus `pipeline/policy_report_v2.py` auf. Damit bleiben dessen geschlossene Exportprüfung, getrennte fünf Studien, feste 43 IDs, Studienvertragshashes, Kategorie-/Accountingbindungen und Nullstatusgrenzen wirksam. Die neue Schicht prüft zusätzlich Studien-/Edition-/DOI-/Zeit-/Populationsbindung zum Katalog, primäre Themenzuordnung, gültige Kategoriecodes und deren Reihenfolge, deutsche Labels, Missinggründe, Quellenkennungen, PDF-Seiten, CAWI-Kategoriebindung und den vollständigen Originalblock B1–B12.

Die publizierten Werte werden kopiert und formatiert. Prozentwerte und Prozentpunktdifferenzen sind Darstellungen bestehender Proportionen, keine neue Zielgröße. Für fehlende Referenzen erscheinen keine Nenner, Missing-Abrechnungszahlen oder Sensitivitäten; Originalwortlaut und Kategorien bleiben trotzdem erhalten. Ein beobachteter Nullanteil einer verfügbaren Originalkategorie wird als solcher dargestellt; `reference: null` wird ausdrücklich nicht zu einem Nullanteil.

Metadaten werden als Text escaped, einschließlich HTML, Markdown-Tabellenzeichen und Linkdelimitern. Quellenlinks müssen HTTPS ohne Zugangsdaten verwenden; URL-Delimiters werden kodiert. Fehler sind statische Codes ohne private Werte. Der Renderer ist kein Validator beliebiger politischer Freigabeabsichten und kein Authentifizierungs- oder Sicherheitsisolationssystem.

## Inhaltliche Darstellung

Jede Einzelangabe enthält ihre Studien-/Originalfragekennung, vollständige gebundene Einleitungen, Antwortstämme, Situationen, Frage beziehungsweise Aussage, Instruktionen und Kategorien. PAPI/CAPI-Druckcodes, Exportcodes und gegebenenfalls CAWI-Anzeigenummern stehen getrennt. Nicht gedruckte beziehungsweise nicht separat gebundene Codes werden nicht geraten. Deutsche und CAWI-Originalformulierungen sowie die dokumentierten statischen Formabweichungen werden getrennt geführt.

Die acht Themen behalten die feste Auswahl aus dem Empirieplan. Wirtschaft/Verteilung und Demokratie/Autorität sind ausdrücklich dargestellt. Binnenlücken werden je Thema benannt: unter anderem Markt-/Eigentumsordnung, Gesundheit/Pflege, digitale Überwachung, gemeinsame konkrete EU-Politik, Versorgungssicherheit, Asyl-/Schutzpolitik und weitere Diskriminierungsgründe. Außen-/Verteidigungs-/Friedenspolitik bleibt eine zusätzliche offene Produktlücke. GLES und ISSP bleiben getrennte Ergänzungswege, keine hier erfundenen Ersatzreferenzen. Fragen mit Nebenbezügen zählen nicht mehrfach als zusätzliche Breite.

B1–B12 beziehen sich auf **Demokratie im Allgemeinen**. B12/keydec bleibt in der dargestellten Originalblockreihenfolge zuletzt und erhält im Ergebnis die primäre EU-Rubrik. B13–B24 zur wahrgenommenen Umsetzung sind ausgelassen. B25 behält die Originaleinleitung und beide Alternativen; PAPI Antwort 1 führt zu B26 auf physischer PDF12, Antwort 2 zu B28 auf PDF13. B26–B29 fehlen in der Auswahl. Die statische CAWI-Seite PDF162 belegt keinen operativen bedingten Nachlauf. Die historische B25-Einzelreferenz wird von einer neuen, weiterhin unvalidierten Webadministration unterschieden.

Nominale EU-Nichtpositionsantworten und Bedingungen gleicher Sozialleistungsrechte bleiben eigene gültige Kategorien. Sie werden weder zu Missing noch zu einer Mitte, einer Aufenthaltsdauer oder Ideologiepunkten umgedeutet. Der Elternzeitkontext und die expliziten Budget-/Steuerfolgen bleiben sichtbar. Die historische Strafverschärfungsfrage verwendet „heute“ im Erhebungszusammenhang 2010/2011. Keine Person erhält aus diesen Angaben ein Motiv-, Autoritarismus- oder Populismuslabel.

Die Methodenprosa reproduziert die bestehenden Primär-/Sensitivitäts-/anweight-Regeln, den gültigen Frage-Nenner, getrennte Missinggründe einschließlich `export_blank_unclassified`, keine Imputation, keine Standardfehler und die festen 100/5-Darstellungsgrenzen. Die Schwellen sind ausdrücklich projektspezifische Anzeigeheuristiken, keine Präzisions- oder Anonymitätsgarantien. Der öffentliche Export enthält keine positive Kategoriecellcounts; deren vorgelagerte Prüfung wird nicht neu aus dem öffentlichen Shape behauptet. Die gültige primäre Gewichtssumme ist im Export nicht separat vorhanden; der Bericht erfindet keinen numerischen Gewichtsnenner durch Subtraktion gerundeter Summen.

Jede Studie führt Erhebungszeit, deklarierte Population, Modus, Ausgabe, Daten-/Dokumentations-DOI und Lizenzkennungen. ESS8s München-Auslassung und der ESS10-SC-Ausgabekonflikt zwischen gebundener 3.2 und älterer 3.1-Zitation bleiben sichtbar. Kein aktueller Deutschlandnorm-, Parteienmatch-, gemeinsamer Personen-, Struktur-, Gesamtscore-, Perzentil- oder CI-Anspruch.

## Tatsächlich gelesene Quellen und begrenzte Byteprüfung

Gelesen beziehungsweise für diese Arbeit intern verarbeitet wurden ausschließlich erlaubte öffentliche Materialien:

- `docs/project.md`, `docs/abdeckung-v2.md`, `docs/messformen-v2.entwurf.md`, `docs/empirie-plan-v2.entwurf.md`, `docs/lizenzen.md` und der einschlägige v2-Methodenabschnitt des `docs/belegregister.md`.
- Öffentlicher Fragenkatalog und öffentlicher v2-Analysevertrag; die Katalog-Originale bilden die Inhaltsbindung. `web/src/app/policy-draft/item-meanings.ts` wurde als erlaubter begrenzter Erklärungskontext gelesen, nicht als neue wissenschaftliche Quelle oder als ausführbarer Berichtseingang verwendet.
- `data/reference-v2/README.md` und die fünf tatsächlich veröffentlichten Einzelstudienexporte. Tatsächliche Anteile und Nenner wurden ausschließlich intern verarbeitet und im ausdrücklich beauftragten Berichtsartefakt dargestellt; keine Ergebnistabellen in Nachrichten oder Toolausgaben.
- `reports/loop/policy-v2-export-decisions.json`, der ausdrücklich erlaubte RESULTS-V2-001-Manifestinhalt, beide gebundenen Erstberichtbytes und beide Rollenentscheidungen. Die privaten Pfad-/Pinreferenzen im Manifest wurden nur als Metadaten gelesen und nie als Dateizugriff benutzt.
- Unveränderte technische Reportbibliothek und deren synthetische Testkonventionen; die bestehenden fünf reinen Bibliotheken wurden für tatsächliche Ausführung gegen die Manifestpins geprüft, nicht verändert.

Der Build prüft vor dem Import der unveränderten Bibliotheken deren tatsächliche öffentliche Codebytes und weitere fest erlaubte öffentliche Manifestartefakte. Er prüft den festen RESULTS-Manifesthash, Root-Exportentscheid, beide tatsächlichen Report-/Rollenentscheidungsbytes, alle fünf veröffentlichen Exporthashes, kanonische Einzelstudienvertragshashes, Kandidatenhashbindungen aus dem Rootentscheid, beide Rollen und die exakte Fragefreigabe. Die Referenzliste ist hier genau 42; die Originalinventarliste genau 43. Die Kandidatenhashes werden mit dem dokumentierten Rootentscheid abgeglichen; ihre privaten Ausgangsobjekte werden **nicht** erneut geöffnet oder unabhängig gehasht.

Zusätzlich werden die Bytes der 30 im gebundenen Katalog genannten öffentlichen Original-PDF-/API-/Lizenz-/Metadaten-Caches gegen deren ursprüngliche SHA256 geprüft. Zulässige Cachepfade sind auf drei konkrete öffentliche `sources/`-Verzeichnisse und PDF/JSON/HTML begrenzt. Symlink-Komponenten werden vor dem Lesen abgewiesen. Sämtliche verwendeten öffentlichen Abhängigkeiten werden nach dem Rendern nochmals geprüft. Die übrigen vorgelagerten Gate-/Receipt-/Privatreferenzen werden nicht traversiert.

Diese Prüfung bestätigt die benutzten veröffentlichten Bytes. Es gibt keinen neuen Netzabruf, keine erneute vollständige Original-PDF-Transkriptions-/Sichtprüfung und keine neue Literaturvolltextprüfung. Literaturfundstellen und ihre Lesegrenzen stammen aus den öffentlichen Methodenakten: B-V2-M01 nur Abstract, B-V2-M02 die genannten OECD/JRC-Abschnitte, B-V2-M03 Krosnick S.37/40; Themenmatrix mit Kriesi, ESS-Demokratieantrag und Walgrave. Die dort belegten Kriterien werden konkret verlinkt, nicht als bereits bestandene Inhalts-/Produktvalidität ausgegeben. `docs/quellen.json` wurde als gebundener öffentlicher Quellenregister-Byteeingang geprüft.

## Synthetische Orakel und tatsächliche öffentliche Reproduktion

14 gezielte synthetische Tests bestehen im letzten Lauf. Die bestehenden technischen Testfixtures werden ausschließlich als synthetische öffentliche Shapes verwendet; keine tatsächlichen Exporte werden in den unittest-Fixtures gelesen.

Die festen Handrechnungsorakel sind unabhängig vom Renderingalgorithmus: 30/70 gültige Fälle mit Gewichten 2/1 ergeben Gewichtssummen 60/70 und Anteile 6/13 sowie 7/13; ungewichtete Abweichung zu 3/10 ist 21/130. Synthetische dweight-Gewichte 1/2 und 1 ergeben Summen 15/70 und Anteil 3/17; die Abweichung zu 6/13 ist 63/221. Ein eigener zweiter Studienvektor mit Summen 50/60 ergibt 5/11 und 6/11. Weitere feste Missingangaben mit Gewichten 8 und 7 ergeben fehlende Summe 15; die leere Exportzelle bleibt gesondert. Unbeobachtete Originalkategorien bleiben 0; nullreferenzierte Fragen bekommen keine Zahlen.

Die Tests prüfen außerdem alle 43 Originalkontexte, acht Rubriken, unterschiedliche Frage-Nenner, EU-Export33/65 gegenüber Druck3/6, nicht gedruckte CAWI-Codes, unveränderte Eingaben und deterministische Eingangspermutationen, HTML/Markdown/Linkescaping sowie Ablehnung von Code-/Grund-/Quellen-/Studien-/Themenänderungen, privaten Extrafeldern, unbekannten Status, fehlerhaften Accounting- oder nichtendlichen Werten. Konträre 99/4-Schwellenaussagen werden nicht als neue Regeln akzeptiert.

Synthetische Buildguardtests prüfen Rollen-, Kandidaten-/Vertrags-, Fragefreigabe- und öffentliche Pfadbindungen, doppelte JSON-Schlüssel, nichtendliche JSON-Konstanten, tatsächlichen Hashvergleich an einer Fake-Dateisystemgrenze und Symlink-Abweisung vor Lesen. Die Buildstrukturtests mocken veröffentlichte Bytes ausdrücklich; sie sind kein echter Review-/Provenienznachweis. Ein synthetischer privater Manifestpfad wird nie aufgerufen.

Die tatsächliche positive Reproduktion liest nur die erlaubten **öffentlichen** Exporte/Metadaten. Der Build und `--check` bestehen im letzten Aufruf; beide erzeugen/vergleichen exakt dieselben Berichtbytes. Eine eigene öffentliche Inhaltsprobe bestätigt alle 43 Wortlaut-/Einleitungs-/Stamm-/Situations-/Instruktions- und Kategoriebindungen sowie die Nullgrenze von cttresa. Das ist eine Darstellungsprobe, keine unabhängige neue Schätzung aus Rohdaten. Nachweise: `public-semantic-conformance.json`, PID 3394192, UTC `2026-10-03T15:07:17.274825+00:00`, tatsächlicher Tool-Exitcode 0.

## Prozesse, echte Fehler und Exitcodes

Alle folgenden gestarteten Kindprozesse wurden mit `wait()` beendet; keine Hintergrundarbeit blieb laufen. Für sämtliche Python-Aufrufe war `PYTHONDONTWRITEBYTECODE=1` gesetzt. Die vollständigen Aufruf-/PID-/UTC-/Exitmetadaten und getrennten Logs liegen im eigenen ignorierten Outputs-Verzeichnis.

| Lauf | PID | UTC-Start | UTC-Ende | Exitcode |
| --- | --- | --- | --- | --- |
| Erster öffentlicher Build | 3346406 | 15:00:35.638225 | 15:00:35.749553 | 1 |
| Erste 9 synthetische Tests | 3362960 | 15:02:42.733180 | 15:02:42.916029 | 1 |
| Zweite 10 synthetische Tests | 3369907 | 15:03:43.809392 | 15:03:44.037876 | 0 |
| Zweiter öffentlicher Build | 3369924 | 15:03:44.038056 | 15:03:44.154761 | 0 |
| 14 Tests mit zusätzlichen Guardproben | 3383068 | 15:05:36.819443 | 15:05:37.132521 | 0 |
| Öffentlicher Build nach Guardproben | 3383085 | 15:05:37.132819 | 15:05:37.253273 | 0 |
| Bytecheck nach Guardproben | 3383102 | 15:05:37.253442 | 15:05:37.374096 | 0 |
| Letzte 14 Tests nach Prosaergänzung | 3392421 | 15:07:01.881662 | 15:07:02.187546 | 0 |
| Letzter öffentlicher Build | 3392438 | 15:07:02.187729 | 15:07:02.305689 | 0 |
| Letzter bytegleicher `--check` | 3392446 | 15:07:02.305902 | 15:07:02.431424 | 0 |

Datum für sämtliche Zeiten: 2026-10-03. Aufrufe: `python -m unittest pipeline.tests.test_policy_thematic_report_v2`; `python scripts/build-policy-v2-report.py`; derselbe Build mit `--check`. Die äußeren Logsammler hatten Tool-Exitcode 0 und berichten den echten Exitcode ihrer Kinder separat; ihre 0 wird nicht zum erfolgreichen ersten Build/Test umbenannt.

Der erste Build scheiterte an meinen angenommenen Feldnamen `reviewedCount`/`inventoryCount`; der tatsächliche öffentliche Entscheid verwendet `reviewedReferenceCount`/`questionInventoryCount`. Eine gezielte reine Diagnose endete äußerlich 0, fing aber den tatsächlichen KeyError ab. Danach zeigte eine weitere Diagnose die zulässige null-Lizenzkennung des Disclaimer-Nachweises; sie wird jetzt ausdrücklich als fehlende eigene Kennung dargestellt, statt eine Lizenz zu erfinden. Eine dritte Diagnose gab intern erfolgreiche Buildbytes zurück, ohne diese auszugeben. Diese Diagnoseaufrufe liefen im Vordergrund und wurden vom Tool vollständig beendet; separate PID-Belege dafür wurden nicht erfasst.

Der erste unittest-Lauf hatte einen Fehler in meiner Negativfixture: Die angeblich falsche erste Studien-ID war bereits die ursprüngliche ESS5-ID. Die Fixture wurde auf eine tatsächlich andere ESS11-ID geändert; keine Grenze wurde dafür gelockert. Anschließend bestanden alle Tests. Spätere Wiederholungen waren durch die neuen Guardtests und die abschließende Methoden-/Lizenzprosa begründet.

## Bytepins und unveränderter Bestand

`before-pins.json` und `after-pins.json` dokumentieren 31 erlaubte öffentliche beziehungsweise geschützte Bestandsartefakte. Der abschließende Vergleich ist für alle bytegleich. Keine Behauptung eines Git-/Repository-Gesamtaudits; Git wurde nicht benutzt.

| Neues Artefakt | Bytes | SHA256 |
| --- | --- | --- |
| `pipeline/policy_thematic_report_v2.py` | 34995 | `d63af6d4bc7e995fc4495601aa5acc5b41bd2bb30802611f5da5810bf8e9a8f3` |
| `pipeline/tests/test_policy_thematic_report_v2.py` | 22068 | `4dd80c7267c0100b65094a9464ae8c50f00efa7d7b3b506cbdc16a25c8241ed1` |
| `scripts/build-policy-v2-report.py` | 9970 | `b9b335233abf4fadd7b6e3fa82f0c88b9d0a925ea2eb56882108a2701435c25e` |
| `reports/phasen/02-politikprofil-v2-methoden-und-ergebnisse.md` | 239409 | `72b87cf11270a968abbb1d6b0cf89b742c893657d6162351b4d45be7b92aaf74` |

Zentrale unveränderte Pins:

- Analysevertrag `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b`; Katalog `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4`.
- Technischer Renderer `53d68f23f2bf7c57c95e2bdd55ae0059da4dfe8598bcbd12e2681206a9e4d6ea`; dessen Erstbericht `bcdfeda5152668953c2483e68cd145fbc741a6fd81c8f8c3f14b53e480fcb319`.
- Gruppenbibliothek `9b680b07385cefc665a54e583cf4b44f03d1305b2829a724fb9afbd7103284b6`; Gruppenerstbericht `cd9b43110b21195847a2cafc7675d5f2303e4b2001fc6f80faacd67083d110e7`.
- RESULTS-Manifest `3299ad658cca7cbb5621c6f062d4133b831e74d8bf4ca71bcb8e67fff56c4434`; Rootentscheid `a87f780a7219253f7f3773d051b7001f438b19b2fb2d0ee820fc22c1157a16df`.
- Methoden-Erstbericht `1bb14ba2dba3d57612d66c5a50c29ce049606e8fddb062ff6b616f56b60462ee`; Quellen-Erstbericht `7a2814359b94ab3a73dd22a090b2a10c6b51db6cc243d8586e8ae15bfdc580e8`.

Der Hash dieses neuen Erstberichts wird anschließend separat an Root übermittelt; kein selbstreferenzieller Hash im Bericht.

## Grenzen und nächster Übergang

Der Berichtsautor kennt nun die tatsächlich veröffentlichten v2-Einzelaggregate. Dies ist keine ergebnisblinde Auswahl-/Methodenrolle. Historische v1-A/B-Einsicht und dieselbe Codex-Modellfamilie der Ergebnisprüfer sind kenntlich. Die neue Darstellungsfassung braucht ihre gezielte unabhängige Präsentationsprüfung; dieser Erstbericht nimmt sie nicht vorweg.

Keine Roh-/lokalen Daten, CSVs, Header, Personenkennungen, privaten Kandidaten oder Gruppenantworten wurden geöffnet oder aufgezählt; dort wurden auch keine Dateimetadaten abgefragt. Keine neue Aggregatschätzung, Gateänderung, Datennachwahl, Kategorienänderung oder Quellenkorrektur. Kein Git, Netz, Auth, Install, Server, Browser, Screenshot, Kontakt, Claude, pnpm oder Agentenauftrag. Die vom Root ausdrücklich begrenzten Python-/Publicbuildprüfungen ersetzen keinen allgemeinen `pnpm check`, keine Produkt-, Human-, Lizenz- oder Releaseabnahme.

Root bleibt alleinige Annahmeautorität für tatsächliche Provenienz-/Reviewpins und spätere Veröffentlichung. Der feste Guard kann Änderungen an den gebundenen veröffentlichten Bytes erkennen; er kann privilegiert gefälschte Absichten, eine geänderte ausführbare Buildfassung oder einen kompromittierten Prozess nicht ausschließen. Hauptproduktbreite, Menschenverständnistest, endgültige UI-/Designzustimmung, Claudes Schlusskontrolle, Rechte-/Nutzungsentscheidung und persönlicher Release bleiben offen.
