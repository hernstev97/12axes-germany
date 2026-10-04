# P5 Runde 2: Quellen, Konstrukte und Fairness des Plans v2.3

4. Oktober 2026, Europe/Berlin. Gezielte Nachprüfung, PLAN-V23-002, Entwurf 0.3. Eigenes begrenztes KI-Review durch Codex/OpenAI.

## Gesamturteil

**NICHT_BESTANDEN für die Festschreibung im geprüften P5-Runde-2-Umfang.** F01, F03 und F04 sind korrigiert. F02 ist teilweise korrigiert und bleibt mittel/blockierend. Neu ist F05: Der eingeführte Kandidatenstatus widerspricht beim OECD-Weg der weiterhin fehlenden deutschen Originalfassung. F05 ist mittel/blockierend. Kein erhebliches Finding bleibt in diesem gezielten Umfang offen.

| Finding    | Stand Runde 2 | Schweregrad          | Blockiert diesen Umfang |
| ---------- | ------------- | -------------------- | ----------------------- |
| P5-V23-F01 | KORRIGIERT    | erheblich in Runde 1 | nein                    |
| P5-V23-F02 | TEILWEISE     | mittel               | ja                      |
| P5-V23-F03 | KORRIGIERT    | mittel in Runde 1    | nein                    |
| P5-V23-F04 | KORRIGIERT    | niedrig in Runde 1   | nein                    |
| P5-V23-F05 | OFFEN, neu    | mittel               | ja                      |

Das Urteil betrifft die Planregeln und ihre Quellen-/Interpretationsbindung. Es ist keine neue Gesamtprüfung und keine empirische, juristische, menschliche oder Releaseabnahme.

## Prüffassung und Zugriff

Start und letzte Kontrolle vor Berichtserstellung: HEAD `f2c8d0d7770a2df17ded4ccdbbd1e10d3d85ad67`, Branch `research/life-93-claude-20261003`, sauberer Worktree. Auftrag SHA-256 `7b57dc629bbbdfbfe0b80abf1475d53cb866a68574681ad148491c1dcf73750a`; Manifest SHA-256 `647b8d9c46d6d30aea2d89c1d4ab8762b5b8b13b3221c4c78ed70d711e49b50d`. Alle 23 Artefaktpins stimmten vor Bewertung und vor Schreiben. Der abschließende Check prüft sie erneut gegen das eigene JSON.

Das Manifest nennt als Commit `c7adf473b29343b86766eb25a87b9f752960616f` und in der Notiz noch Entwurf 0.2. Die tatsächlich gehashten Planbytes enthalten Entwurf 0.3 und die Korrekturen in Abschnitt 13. Bewertet wurden diese Bytes, keine aus dem Commit oder der Notiz abgeleitete Ersatzfassung. Die Notiz ist ungenau; die Identität des Prüfgegenstands ist dennoch gesichert.

P5-Runde-1-Findings gelesen. P4-Runde-1-Dateien nur gehasht, keine inhaltlichen Urteile gelesen. Keine andere Runde-2-Prüfung gelesen, keine Agenten gestartet und keine Nachrichten gesendet. Keine Antwortverteilungen, externen Ergebnistabellen, GESIS-Server oder Dateien unter `data/raw/`, `data/local/`, `outputs/` und `data/reference-*` geöffnet. Die Zahlen in Plan Abschnitt 8 wurden nicht unabhängig geprüft.

## Nachprüfung der Findings

### P5-V23-F01: KORRIGIERT

Runde 2: Die frühere unbegründete Unterscheidung ist korrigiert. 4.2 a trennt die Feststellung bereits ergriffener Maßnahmen von 4.2 b, einer einseitigen Zweckbegründung im Zollitem. QB12 nennt Kosten beider Alternativen. Q19 macht den eigenen Preis und den Leistungsgewinn ausdrücklich zum gemessenen Gegenstand. Q27 e wird nicht mehr wegen seiner Kosten-Nutzen-Abwägung ausgeschlossen, sondern wegen des engeren Digitalisierungsanlasses nach 4.1 Nr. 2/4.2 f. Dieser Anlass entspricht keiner eigens benannten Arbeitszeit-Unterlücke der Matrix. Damit sind die ursprünglich beanstandeten Unterschiede anhand einer gemeinsamen Regel nachvollziehbar. Die Neubewertung ist keine Schätzung eines Framingeffekts und kein Neutralitätsnachweis.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:60-73,188,190,196,210,225
- reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json: kandidaten[id=R8-EB-ST0350-2], kandidaten[id=R8-EB-ST0939-ZOLL], kandidaten[id=R8-EB-SP572-QB12-KI], jeweils wortlautDe/kontext
- reports/claude/agenten/R6-eurobarometer.md:176-198
- OECD-Kernfragebogen 2024, PDF-S. 7 und 10; https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf

### P5-V23-F02: TEILWEISE

**Mittel, weiterhin blockierend.** Plan 4.4/11.1 und Entscheidungsvorlage 2 nennen die Geltungsbereiche korrekt. Die Folge in `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:33` verlangt aber weiterhin die pauschale Einordnung als „EU-Ebene“. Die allgemeine KI-Präferenz und die mehrdeutige Ausgabenfrage dürfen diese Kennzeichnung nicht erhalten. Die Zahl und Einordnung der neun vorgeschlagenen sowie zwei zurückgestellten EB-Fragen stimmen im Plan.

In der Folge der Entscheidungsvorlage dieselben Geltungsbereiche wie in 4.4/11.1 verlangen. Allgemeine und mehrdeutige Fragen getrennt kennzeichnen. Die frühere pauschale Eurobarometer-Aussage der historischen Matrix für v2.3 ausdrücklich begrenzen; keine historische Fassung überschreiben.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:83-91,184-198
- docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:27-33
- docs/abdeckung-v2.2.md:83,94
- reports/claude/agenten/R6-eurobarometer.md:198,231

### P5-V23-F03: KORRIGIERT

Runde 2: b/c sind aufgenommen; die Liste enthält nun zehn Items b-j und l. a/k sind mit 4.1 Nr. 2 ausgeschlossen statt stillschweigend ausgelassen. Die Matrix benennt bei Familie bereits Kinderbetreuung/Elternleistungen, bei Sicherheit Polizei/Strafen; sie führt dort keine eigene Lücke für allgemeinen Ausbau dieser Leistungen. Die Kita-Pflicht in der Bildungslücke ist ein anderer Gegenstand als allgemeine Familienleistungen. Eine andere Auswahl wäre fachlich diskutierbar, aber der ursprüngliche unbegründete Fünfer- und Vollständigkeitsfehler ist behoben. Entscheidungsvorlage und Mehrfachauswahlgrenze sind angeglichen. Das bestätigt die inhaltliche Liste, nicht den neuen Status vorgeschlagen; dazu F05.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:210-225
- docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:37-41
- docs/abdeckung-v2.2.md:24-37
- OECD-Kernfragebogen 2024, PDF-S. 7, Q19 a-n; https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf

### P5-V23-F04: KORRIGIERT

Runde 2: Beide Dokumente nennen den erwarteten ersten Datenrelease, bestätigen Deutschland und deutschen Fragebogen zu diesem Termin ausdrücklich nicht und binden den Beginn an die tatsächlich veröffentlichte deutsche Ausgabe. Die Originalmeldung kündigt den Ersttermin an, ohne eine entsprechende deutsche Zusage. Korrigiert im benannten Umfang; keine Vorhersage eines tatsächlichen Releases.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:200-205
- docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:51-53
- ESS-Meldung vom 30.09.2026, Haupttext; https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027

### P5-V23-F05: OFFEN

**Mittel, neu und blockierend.** Neu eingeführter Statuswiderspruch: 4.1 Nr. 3 verlangt den belegten deutschen Originalwortlaut samt vollständiger Antwortliste und Kontext. 11.3 stellt zugleich fest, dass der Fragebogen nur englisch vorliegt. Die deutschen Originalfeldtexte fehlen weiterhin; das ist eine fehlende Sachvoraussetzung und keine bloß ausstehende Freigabe. Nach 4.6 wären diese inhaltlichen Kandidaten zurückgestellt.

Das neue Statusmodell stellt eine nicht erfüllte Wortlautbedingung als erfüllt dar und erschwert die spätere Prüfung des eingefrorenen Itemregisters. Die übergeordneten Auswertungs- und Quellenstopps bleiben bestehen; kein tatsächlicher unerlaubter Abruf oder Export wurde festgestellt.

Korrektur: Die zehn OECD-Items als inhaltlich geeignete, zurückgestellte Kandidaten mit fehlendem deutschen Feldwortlaut kennzeichnen. Alternativ den Status vorgeschlagen ausdrücklich nur als inhaltlichen Vorschlag definieren und jede offene Sachvoraussetzung separat binden. 4.1 Nr. 3 und die Aufnahmesperre erhalten; keine eigene Übersetzung zum Originalwortlaut erklären.

Nachprüfung: Neue gepinnte Fassung: Statusdefinition mit OECD-Liste und Entscheidungsvorlage abgleichen. Für jeden nicht belegten Wortlaut muss der offene Status sichtbar bleiben, bis ein vollständiges Originalregister tatsächlich geprüft ist.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:49-57,97-99,208-225
- docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:37-39
- docs/quellenanfragen-v1.entwurf.md:76-79

## Primärquellen und Prüfgrenzen

Der [OECD-Kernfragebogen 2024](https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf) wurde für Q19 und Q27 an PDF-Seiten 7 und 10 gelesen. Der direkte Bytehash stimmt mit dem Plan überein. Keine OECD-Ergebnisquelle geöffnet. Q19 ist eine Mehrfachauswahl mit exklusiven Optionen für generelle Nichtbereitschaft und Nichtwissen. Nichtauswahl eines Bereichs ist keine eigene Ablehnungsantwort. Vollständige deutsche Feldfassung und Antwortbindung bleiben vor Integration erforderlich.

Die [ESS-Meldung vom 30. September 2026](https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027) wurde direkt abgerufen; ihr HTML-Hash stimmt mit dem alten Quellenpin überein. Sie nennt den erwarteten ersten Release, aber keine Zusage für Deutschland oder den deutschen Fragebogen. Zwei Abrufversuche über das Webwerkzeug scheiterten mit `Internal Error`; derselbe HTTPS-Endpunkt war über `urllib.request` erreichbar. Downloads blieben im Arbeitsspeicher.

Die Eurobarometer-Fälle wurden semantisch gegen die ausdrücklich gepinnten R6-/R8-Texte und den Strukturbericht S1 geprüft. Deutsche Originaldateien der Kommission wurden nicht geöffnet, weil Datenanhänge zugleich Ergebnisse enthalten können; GESIS blieb ausgeschlossen. Das ist keine erneute Vollauthentifizierung der deutschen Feldtexte. S1 dokumentiert nur eine deutsche Wortlautstichprobe. Die positive F01-Nachprüfung betrifft die nachvollziehbare Anwendung der neuen Regel auf die dokumentierten Fälle, nicht die Größe eines Framingeffekts.

Nicht geprüft: neue vollständige Quellen-/Lizenz- und Gesetzesprüfung, sonstige P4-Methodenfindings, empirische Referenzen, Tabellenwerte, Webübertragung, Produktbrowser und menschliches Verständnis. Diese Teile sind außerhalb der gezielten Nachprüfung. Die bisher gültigen Urteilsteile werden dadurch weder aufgehoben noch als frisch geprüft ausgegeben.

Das Schema kennt keinen Finding-state `TEILWEISE`. Daher enthält das JSON bei F02 `state: OFFEN`, `blocksScope: true` und im zusätzlichen schemaerlaubten `ratings`-Eintrag `correctionStatus: TEILWEISE`. Die beiden Darstellungen widersprechen sich nicht. Die historischen Erstberichte bleiben bytegleich.

## Technische Kontrolle

Nur die beiden beauftragten Ergebnisdateien werden geschrieben. Anschließend wurden sie im Speicher mit Prettier formatiert, das JSON gegen das gelesene Draft-2020-12-Schema mit Ajv geprüft und alle gebundenen lokalen Eingabehashes erneut verglichen. Diese technischen Prüfungen bestätigen Form und Bindung; sie ersetzen keine fachliche Prüfung.

`pnpm check` wurde nicht ausgeführt. Laut `package.json` umfasst es globale Format-/Schema-Prüfungen, Produkttests und einen Build; das würde den strikt beschränkten Datei-, Ergebnis- und Schreibumfang verlassen. Die ausdrücklichen Grenzen dieses Auftrags gehen der allgemeinen Repository-Regel vor. Auch kein v2.2-Rechenwegtest und kein Browserlauf, da weder Rechenweg noch UI geändert wurden.

## Gelesene Dateien und SHA-256

Die Zugriffsart unterscheidet Inhaltslektüre von bloßer Pinprüfung. Teilweise gekürzte Werkzeugausgaben wurden für die bewertungsrelevanten Stellen und verpflichtenden Basisregeln gezielt wiederholt. Ein vollständiger Bytehash ist keine vollständige fachliche Lektüre. Der kurze Memory-Abgleich nutzte nur `MEMORY.md:52-55` für Isolation, Pins vorher/nachher und begrenzte Urteile, keine alten Sachurteile oder Rollouts.

| Datei oder Originalquelle                                                                              | SHA-256                                                            | Zugriff                                                   |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | --------------------------------------------------------- |
| `docs/analyseplan-v2.3.entwurf.md`                                                                     | `95ea58c0485b4acb980662cd1d5511d855b511ae0adce0c218a912bca205a5db` | gezielt inhaltlich gelesen                                |
| `docs/entscheidungsvorlage-erweiterung-v1.entwurf.md`                                                  | `dacfb5d58a1ce12f60cb3b244273dadd1388aaf1fb375e2e1bb5bae39cc6c66f` | gezielt inhaltlich gelesen                                |
| `docs/abdeckung-v2.2.md`                                                                               | `f9ec753734d4348728b15c5cd7f152fe15df2b7d8db4206c24ec898604a9ac9b` | gezielt inhaltlich gelesen                                |
| `docs/quellenanfragen-v1.entwurf.md`                                                                   | `d9a4b0b67a73a1669ad07fed7461237cb08c0df0b0f1eacb02b4918a2727e972` | gezielt inhaltlich gelesen                                |
| `docs/analyseplan-v2.2.md`                                                                             | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` | gezielt inhaltlich gelesen                                |
| `docs/profilregeln-v1.md`                                                                              | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` | gezielt inhaltlich gelesen                                |
| `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.md`                                      | `6830b4172d606b47fc6f00214fba09d776790143c85c01529b7c33256691c24b` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json`                                    | `23e27dd8c2c1e359fe62ff5df058fef4de749dce95ca1e6da44cec6839e49fa2` | gezielt inhaltlich gelesen                                |
| `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md`                                       | `42aaa648a36557d33b6bb316aff007f5f79f92779aa4875acdc74516c70ba5c3` | gezielt inhaltlich gelesen                                |
| `reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.json`                                     | `71e012d3b460917269153d261a4565f6bfbb34627220ee2cf14d8abf1af272d6` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/agenten/R10-quellenblocker.md`                                                         | `65d79b32748197923c9614c7e8e85f19b06f516fa0cff869dbb7d3cf2f228885` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/agenten/R10-quellenblocker.json`                                                       | `8e15381892d91f62094c68573bb32148a5df21daf24ad11415549ef94861439a` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/agenten/S1-strukturpruefung-eurobarometer.md`                                          | `15b2851d4e383a50ae064b566b1f2d6419180d3899f20007b49c07fe607295c0` | gezielt inhaltlich gelesen                                |
| `reports/claude/agenten/S1-strukturpruefung-eurobarometer.json`                                        | `f563bc2f138d67a00a9cf8fbfd80580dd3e842108d17231b44efb241edbc9575` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/agenten/R5-wvs.md`                                                                     | `a163be6d448ab5f9e14b54293f355a2e0cea3c19d37e92a4d0021e8af7afc969` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/agenten/R6-eurobarometer.md`                                                           | `58b08b2af20d70261e95e7d0d815d4c083d95e0879cef5ee864c6ee05e84e8bb` | gezielt inhaltlich gelesen                                |
| `reports/claude/agenten/R7-weitere-quellen.md`                                                         | `4e795f355ccd359613949a2e307f46150f31506cf817b51f1a4e232405f6fcd5` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/auftraege/R-erweiterung-gemeinsam.md`                                                  | `56970a37d162e3996cace441b4f41c44d7e4e3bfd408d008c13e3f9ba0898ccd` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `data/gruppenvertrag.v2.1.entwurf.json`                                                                | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/pruefungen/P4-methoden-v23.md`                                                         | `e1aecf135e7bb3cf3a56a55459b25f24f3f09a4349e788278fefc20568292355` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/pruefungen/P4-methoden-v23.json`                                                       | `2b6df5d37b09bc481cafce926e36e4827c842147910e93a51abe1c346d18462d` | nur vollständige Bytes gehasht, kein Inhaltsurteil        |
| `reports/claude/pruefungen/P5-quellen-fairness-v23.md`                                                 | `bbd1b5cd21370863d95bdb3d1056ae9634ed52554d253189d30fa0e05e69f25d` | gezielt inhaltlich gelesen                                |
| `reports/claude/pruefungen/P5-quellen-fairness-v23.json`                                               | `d5393faca0fdaf80ac906621b94fc0dad498b25ce1877d0220ef650d4f1d8878` | gezielt inhaltlich gelesen                                |
| `reports/claude/auftraege/P5-runde2-plan-v23.md`                                                       | `7b57dc629bbbdfbfe0b80abf1475d53cb866a68574681ad148491c1dcf73750a` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `reports/claude/pruefungen/PLAN-V23-002-manifest.json`                                                 | `647b8d9c46d6d30aea2d89c1d4ab8762b5b8b13b3221c4c78ed70d711e49b50d` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `.claude/skills/life93-review/SKILL.md`                                                                | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `.claude/skills/life93-review/references/urteil-schema.json`                                           | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `.agents/skills/unslop/SKILL.md`                                                                       | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `docs/project.md`                                                                                      | `2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `docs/pruefregeln.md`                                                                                  | `29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `reports/claude/auftraege/P5-plan-v23-quellen-fairness.md`                                             | `fc392d6199546c89eaafec41447ba5be0fdcf35bc78bcf045a0aef6868746fa1` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `package.json`                                                                                         | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `/home/stevenh/.codex/memories/MEMORY.md`                                                              | `76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9` | Anweisung/Schema/Betriebsgrundlage gelesen                |
| `https://webfs.oecd.org/els-com/RtM/OECD-Risks-That-Matter-2024-Core-Questionnaire.pdf`                | `5672381901f57dcc2ee3e76a9b0716b6c418c3a69e1e85b804e29bb2c343ae10` | Primärquelle, gezielter Inhalt und vollständiger Bytehash |
| `https://www.europeansocialsurvey.org/news/article/initial-round-12-data-release-scheduled-early-2027` | `fd1f7663ca6e3a2e5d1daacfa291b41f8804824c3e807b6c570554a793ea4b96` | Primärquelle, gezielter Inhalt und vollständiger Bytehash |

## Ausgeführte Befehle und Werkzeuge

- `pwd`, `git status --short`, `git branch --show-current`, `git rev-parse HEAD`; ausschließlich lesende Git-Befehle.
- `sha256sum reports/claude/auftraege/P5-runde2-plan-v23.md reports/claude/pruefungen/PLAN-V23-002-manifest.json`.
- `rg -n 'bounded|Prüf|PLAN-V23|immutable|pins' /home/stevenh/.codex/memories/MEMORY.md`; `sed -n '50,59p'` derselben Datei. Kein Rollout gelesen.
- `cat` für Auftrag, Manifest, Review-Skill, Urteilsschema, unslop-Skill, Projektstand, Basisregeln, beide alten P5-Urteilsdateien, ursprünglichen P5-Auftrag und `package.json`.
- `wc -l` für Analyseplan v2.2, Profilregeln, Prüfregeln und alten P5-Markdownbericht.
- `nl -ba`/`sed -n` für gezielte Ausschnitte aus Analyseplänen v2.2/v2.3, Entscheidungsvorlage, Abdeckung, Quellenanfragen, Profilregeln, Prüfregeln, S1, R6, R9 und altem P5-Bericht.
- Python-Here-Docs mit `json`, `pathlib` und `hashlib`: Prüfung aller 23 Manifestartefakte vor Bewertung und vor Schreiben; gezielte Ausgabe der R8-Kandidaten; Prüfung, dass die eigenen Ergebnisdateien noch nicht existieren; Erstellung ausschließlich dieser beiden Dateien.
- `web.run open`: OECD-Originalfragebogen und ESS-Originalmeldung; Folgeaufrufe für OECD Q19/Q27 und ein ESS-Wiederholungsversuch.
- `PYTHONDONTWRITEBYTECODE=1 python3`: `urllib.request`-Abruf der beiden Originalquellen, SHA-256, HTML-Textausschnitt; `pdftotext -f 7 -l 10 - -` über stdin/stdout, nur Fragebogenseiten, keine lokale Downloaddatei.
- `node --input-type=module`: ausschließlich eigene Ergebnisdateien im Speicher formatieren, Draft-2020-12-Schema validieren, Format und lokale Eingabepins prüfen; abschließend `git status --short` und `git rev-parse HEAD`.

Keine Commits, Pushes, Tags, Kontozustimmungen, Freigaben, Nachrichten oder zusätzlichen Ergebnisdateien. Keine Speicherung heruntergeladener Quellen.

## Modell laut Laufzeit

OpenAI, Codex-Harness in T3 Code, `gpt-6.1-sol`, Reasoning-Effort `high`, gemäß verfügbarer Laufzeitangabe. Keine unabhängig belegte interne Modellrevision. Das vollständige Nutzerprompt und der vollständige Datei-Auftrag sind in `execution.prompt` des JSON erhalten.

## Abschließender Prüfbeleg

JSON-Schema und Format beider Ergebnisdateien: BESTANDEN. Alle 33 lokalen Eingabehashes, darin alle 23 Manifestartefakte, sind nach Berichtserstellung unverändert. Die externen Originalhashes wurden beim direkten Abruf bestätigt. HEAD bleibt `f2c8d0d7770a2df17ded4ccdbbd1e10d3d85ad67`; der abschließende Git-Status nennt ausschließlich die beiden beauftragten neuen Ergebnisdateien. Das fachliche Urteil bleibt NICHT_BESTANDEN wegen F02 und F05.
