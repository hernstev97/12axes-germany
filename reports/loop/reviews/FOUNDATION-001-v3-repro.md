# FOUNDATION-001 v3: unabhängige Reproduktions- und Typprüfung

Abgeschlossen am 2026-10-03. Gegenstand ist ausschließlich N-F01 in Reparaturrunde 2. Ich bin frischer Prüfer, kein Autor dieser Reparatur. Ergebnis: **BESTANDEN für die begrenzte Korrektur** am Manifest `b590aaa05137b86e44854468324c85e5aef34718677216db18aeaefaf8d83df4`. Keine Inventar-Gesamtabnahme, keine endgültige Eignung oder Polung, keine empirische oder Phasenfreigabe.

Die fünf beanstandeten Ausnahmen und sämtliche tatsächlich vorhandenen Fragen D2–D19 einschließlich D10a/b sind an den deutschen Originalseiten 32–39 nachgelesen. Die 18 Typänderungen sind begründet; D14 bleibt unverändert. Zwei eigene frische Vierquellen-Caches reproduzieren die v3-CSV und -Provenienz bytegleich. Alle 296 Original-/Kontextfelder außerhalb der ausdrücklich geänderten Annotationen bleiben identisch. Die unveränderte technische Restliste enthält weiterhin 205 Zeilen.

## Prüffassung und Trennung

Arbeitsverzeichnis bei allen Shellaufrufen: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Gelesene Forschungsfassung: `reports/loop/packages/FOUNDATION-001/v3/files/`. Der Manifestcommit `edd48c36fdc434a05053721822508c19cbf64be1` identifiziert den angegebenen Codekontext; geprüft wurden die eingefrorenen Datei-Bytes, nicht aus dem Commit abgeleitete Identitätsbehauptungen.

Gelesen wurden Auftrag, AGENTS, LIFE-93-Issue, Arbeitsloop, Projektstand, Prüfregeln, Analyseplan, Belegregister, Lizenzakte und Entscheidungen; der Runde-2-Vorabauftrag, Runde-2-Entscheidungen und Runde-2-Korrekturbericht; Parser und einschlägige eingefrorene Tests; die N-F01-Passagen des ursprünglichen Neutralitätsberichts und beider abgeschlossenen v2-Nachberichte. Die v2-Dateifassung wurde für Differenz- und historische Gegenprüfungen genutzt. Bei den Live-Dokumenten `docs/project.md` und `docs/entscheidungen.md` handelt es sich um ergänzende Projektanweisungen, nicht um an ihrer Stelle geprüfte Frozen-Forschungsoutputs.

Keine anderen v3-Berichte, PREP-/SOFTWARE-Berichte oder aktuellen Autorverteidigungen wurden gelesen. Keine globale Agent-Auflistung, Browser-/Cookie-/Zugangsinformation oder Portal-Analysis. Ich habe keine weiteren Agents gestartet, keine gemeinsamen Forschungsdateien geändert und keine Commits oder Pushes durchgeführt. Eine kurze Befundmitteilung an den Koordinator ersetzt diesen vollständigen Bericht nicht. Gleichzeitige Dateirechte bestehen technisch; die Kontexttrennung ist durch den eingehaltenen Zugriffsumfang gewährleistet, nicht durch eine Betriebssystem-Isolation.

Eigene Schreiborte sind dieser Bericht und `outputs/loop/foundation-v3-repro/`. Die Ausführung verwendet den eingefrorenen Parser mit ausdrücklich gesetzten Cache-/CSV-/Provenienzpfaden. Bei den importierten Autorentests wurde ausschließlich der in-memory-Wert `ROOT` auf meinen Outputordner gesetzt, damit deren temporäre synthetische Dateien unter meinem Schreibort bleiben. Kein Parserbyte wurde dazu verändert. Bytecodeerzeugung war bei den importierenden Läufen abgeschaltet. Öffentliche PDF-/HTML-Volltexte, Extraktionen und Renderbilder liegen nur unter meinem ausgeschlossenen Outputordner.

Laufzeitmodell laut Startauftrag: `gpt-6.1-sol`, geerbtes Reasoning `ultra`. Eine eigene technische Abfrage der internen Modellrevision fand nicht statt. Nicht zugängliche Anbieter- und interne Modellvorgaben bleiben unbekannt. Verwendete Werkzeuge: `functions.exec` mit `exec_command` und `view_image`, Python-Standardbibliothek, Poppler `pdftotext`/`pdftoppm`, `rg`, `sha256sum`; außerdem `collaboration.send_message` für die kurze Mitteilung. Skills `unslop` und `pdf` wurden gelesen und angewandt. Kein Review einer anderen Modellfamilie und kein akademisches Peer Review.

## Hashbindung vor und nach der Ausführung

Eigene Vollaufstellungen: `outputs/loop/foundation-v3-repro/hash-before.json` und `hash-after.json`; wiederholbares Prüfskript `verify_bound_inputs.py`.

| Kontrolle | Ergebnis |
| --- | --- |
| Manifest vor/nach | SHA-256 jeweils `b590aaa05137b86e44854468324c85e5aef34718677216db18aeaefaf8d83df4` |
| 47 eingefrorene Dateien | Alle Soll-/Ist-Hashes passen, vor/nach identische Bytes |
| 157 `sourceInputs` an heutigen Pfaden | 153 passen unmittelbar; vier nennen historische v2-Bytes an wiederverwendeten Livepfaden |
| Vier historische Inputs | Alle vier Erwartungshashes passen exakt zur jeweils eingefrorenen v2-Datei |
| Während meiner Prüfung | Keine Änderung an einer der 47 Dateien oder an den 157 gelesenen Inputbytes |

Die vier historischen Einträge sind `pipeline/inventar.py`, `pipeline/tests/test_inventar.py`, `data/inventar.entwurf.csv` und `data/inventar.provenienz.json`. Ihre erwarteten Hashes lauten in dieser Reihenfolge `84ff2e1c2868170ef6cf9ecdb050d2d26a802e57c7c324ae938bb8fa951c615e`, `0d61d2d42ddc16f8ca8d6ff3b9155e14a0ae1c903ffc2027ad0fc23235914e85`, `89d2c4611d44faee3e44d27e66e5e68550a5611112cf2cf63f96fa5d8a8b84f3` und `89c75a95f2da2610396d25fd7428f51d213a71446a5abba50eed73a28fd4ecb7`.

Für diese vier Einträge gibt es im tatsächlich gelesenen v3-Manifest kein separates `actualSha256AtFreeze` und keinen eintragsspezifischen historischen Hinweis. Ich erfinde diese Felder nicht. Die historische Herkunft lässt sich aber unmittelbar durch die v2-Snapshotbytes nachweisen. Der v2-Manifesthash `10157ee7bca65ca0b92707e673bc75c3698c4d1acc6664da421b7b218e7a1988` passt außerdem zum v3-Feld `previousManifestSha256`. Die aktuellen v3-Bytes sind getrennt im v3-Feld `files` gebunden. Deshalb sind die vier heutigen Pfadabweichungen kein Nachweis einer Veränderung der eingefrorenen v3-Prüffassung. Eine pauschale Aussage „157 aktuelle Livepfade passen zum historischen Erwartungshash“ wäre falsch; sie wird hier nicht erhoben.

Der Rohdatenhash wurde ausschließlich als vorhandenes Manifestmetadatum gelesen. Weder die Rohdatei noch ihre Bytes wurden geöffnet oder neu gehasht. Die offizielle Downloadidentität dieser Datei ist außerhalb meiner Prüfung.

## N-F01: Problem, Korrektur und Originalnachprüfung

Die ursprüngliche Finding-ID und Rundenzählung bleiben bestehen. Historischer Schweregrad: mittel. Die in v2 zusätzlich belegte Restbeanstandung war niedrig, weil falsche Entwurfsmetadaten vorlagen, aber kein freigegebener Score. Beide Größen werden durch mein Korrektururteil nicht rückwirkend gelöscht.

Die zu prüfende Behauptung steht im eingefrorenen `reports/loop/FOUNDATION-001-runde2-korrekturbericht.md:5–11`: Die breite D2–D19-Verhaltensregel entfällt; D9 erhält eine vorgelagerte administrative Behandlung; Körpermerkmale und Versorgung werden getrennt; 18 Typen ändern sich, Originaltexte und 205 offene Restzeilen bleiben erhalten.

Das belegte frühere Problem ist in der eingefrorenen v2-Fassung von `pipeline/inventar.py` und im v2-Quellenbericht, Abschnitt „Restfinding N-F01“, nachvollziehbar: Der breite Verhaltenszweig wurde vor der bereits genannten D9-Verwaltungsausnahme ausgeführt. D11/D12/D15/D16 erhielten denselben Verhaltenslabel und Ausschlussgrund. Falsche Gegenstandslabels können spätere Itemurteile vorstrukturieren; ein endgültig falscher Ausschluss, gerichteter politischer Bias oder empirischer Schaden war daraus nicht belegt.

Original: [deutscher ESS11-Fragebogen 2023](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), SHA-256 `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`. Ich las PDF-/gedruckte Seiten 32–39 vollständig als eigenen Layoutauszug und als acht gerenderte Originalseiten. Ablage ausschließlich unter `outputs/loop/foundation-v3-repro/original-pages32-39.layout.txt` und `original-page-032.png` bis `original-page-039.png`. Die folgende Kontrolle ist eine begrenzte Quellen-/Typgegenprüfung; sie nimmt keine Kategorien-, Missing-, Routing- oder Eignungsgesamtprüfung vorweg.

| Frage | Originalseite | Nachgelesene Antwortaufgabe und v3-Beurteilung |
| --- | --- | --- |
| D2 | 32 | Eigene Obstkonsumhäufigkeit. Verhalten; Fruchtsäfte ausgeschlossen, tiefgefrorene Früchte eingeschlossen. |
| D3 | 33 | Gemüse-/Salatkonsumhäufigkeit. Verhalten; Kartoffeln ausgeschlossen. |
| D4 | 33 | Tage körperlicher Betätigung von mindestens 30 Minuten in den letzten sieben Tagen. Verhalten. |
| D5 | 33 | Gegenwärtiges oder früheres Zigarettenrauchen einschließlich Nichtrauchen. Verhaltensauskunft. |
| D6 | 34 | Eigene Alkoholkonsumhäufigkeit in zwölf Monaten. Verhalten. |
| D7 | 34 | Getränkemenge beim letzten Konsum an Montag bis Donnerstag; kein allgemeiner Werktagsdurchschnitt. |
| D8 | 35 | Getränkemenge beim letzten Konsum an Freitag bis Sonntag; kein bloßer Samstag-/Sonntagblock. |
| D9 | 35 | Interviewercodierung männlich/weiblich für D10a/b. Verwaltung; kein Selbstbericht über Verhalten oder Geschlechtsidentität. |
| D10a | 35 | Häufigkeit hoher Alkoholmenge bei einer Gelegenheit, Liste 38, D9-Code 1. Verhalten. |
| D10b | 36 | Entsprechende Häufigkeit, Liste 39, D9-Code 2. Verhalten. |
| D11 | 36 | Körpergröße ohne Schuhe; Schätzung zulässig. Körpermerkmal. |
| D12 | 36 | Körpergewicht ohne Schuhe; Schätzung zulässig. Körpermerkmal. |
| D13 | 37 | Kommunikation mit genannten Ärzten über Gesundheit im letzten Jahr. Konkreter eigener Versorgungskontakt. |
| D14 | 37 | Nicht erhaltener Termin oder benötigte Behandlung. Versorgungsereignis; schon in v2 korrekt präzisiert. |
| D15 | 37 | Bei D14-Code 1 mehrere Gründe für fehlende Versorgung. Barrieren/Gründe, einschließlich finanzieller, zeitlicher und angebotsbezogener Umstände. |
| D16 | 38 | Bei D14-Code 2 oder 8 Versorgung erhalten versus keinen Bedarf gehabt. Erhalt/Bedarf, keine pauschale Handlung. |
| D17 | 38 | Eigene unbezahlte Betreuung oder Hilfe. Tatsächliche Tätigkeit; bezahlte Arbeit ausgeschlossen. |
| D18 | 38 | Allgemeiner wöchentlicher Zeitumfang dieser Tätigkeit bei D17-Code 1. Verhalten, mit besonderer Antwort unter einer Stunde. |
| D19 | 39 | Im letzten Jahr genutzte genannte Gesundheitsbehandlungen, Mehrfachnennung. Verhalten. |

Die Originalanweisung bei D9 lautet „INTERVIEWER CODIEREN“. In v3 ist der D9-Zweig in `pipeline/inventar.py:275–276` erreichbar und steht vor dem konkreten Verhalten-Set in Zeile 277. Die benannten D-Annotationen stehen in Zeilen 138–156. Der frühere pauschale D2–D19-Zweig ist entfernt. Es gibt weiterhin andere D-Regeln für D20–D33; diese sind keine behauptete Korrektur oder Vollabnahme des gesamten Gesundheitsmoduls.

D11/D12/D15/D16 und der schon reparierte D14 behalten `ENTWURF_OFFEN` ohne Ausschlussgrund. Administrative und konkrete Verhaltensauskünfte sind als vorläufige Entwürfe gekennzeichnet und verlangen unabhängige Einzelabnahme. Bei allen 19 hier kontrollierten Fragen ist Polung `OFFEN_NICHT_BESTIMMT`. Dass ein Körpermerkmal kein Verhalten ist, entscheidet noch nicht abschließend über politische Itemeignung.

Alle 18 neuen Typbelege tragen den Originalfragebogenhash und exakt dieselbe Wortlautregion wie die zugehörige Inventarzeile. D14 trägt weiterhin seinen vorhandenen Regionsbeleg. Der Parser verweigert eine Bindung an die falsche Originalseite. Die gespeicherte unabhängige semantische Abnahme bleibt in diesen Autorenartefakten `NICHT_GEPRUEFT`; mein Bericht dokumentiert die begrenzte frische Nachprüfung gesondert, ohne gemeinsame Artefakte umzuschreiben.

Korrektur und Nachprüfung: **BESTANDEN im vorgenannten Umfang.** Kein neuer belegter Restfehler dieser D2–D19-Typkorrektur wurde gefunden. Ein vollständiges Inventarurteil folgt daraus nicht.

## Differenzkontrolle aller 296 Zeilen

Eigener maschinenlesbarer Vergleich: `outputs/loop/foundation-v3-repro/v2-v3-diff.json`; zusätzliche unabhängige Testprüfung aller Felder.

Gegenüber v2 ändern sich genau die Typen D2, D3, D4, D5, D6, D7, D8, D9, D10a, D10b, D11, D12, D13, D15, D16, D17, D18 und D19. D14 ist unverändert. Die 296 IDs stehen in identischer Reihenfolge. Die einzigen geänderten Feldnamen sind `antworttyp`, `antworttyp_status`, `antworttyp_beleg_json`, `eignungsstatus` und `ausschlussgrund_entwurf`.

Alle anderen Felder jeder Zeile sind v2/v3 identisch, einschließlich `wortlaut_de`, `originalblock_de`, `originalblock_sha256`, `filter_einleitung_de`, Wortlaut-, Kontext- und Originalblockregionen, Kategorien und Kategorienbelegen. Das bestätigt Unverändertheit dieser vorhandenen Extraktionen, nicht ihre vollständige semantische Richtigkeit. Originalgetreue Token/Regionen und vollständige Fragebedeutung bleiben verschiedene Prüfgegenstände.

Die v2- und v3-Listen `checks.pending_rows` sind vollständig identisch: 205 technische Restzeilen. Auch die Identitäten und Begründungen sind unverändert, nicht nur die Anzahl. `semanticInventoryAcceptance` bleibt `NICHT_GEPRUEFT`; `claimsFullStructuredInventory` bleibt `false`.

## Eigene frische Reproduktion und Gegenfälle

Python: `3.14.7 (main, Aug 14 2026, 06:38:32) [GCC 16.2.1 20260810]`. Poppler `pdftotext version 26.08.0`. Das entspricht dem manifestierten technischen Reproduktionsrahmen. Provenienz enthält diese Softwareangaben; abweichende Versionen wurden nicht ausprobiert.

`execute_reproduction.py` führte nacheinander für zwei anfangs leere eigene Caches `fetch`, `build` und `check` aus. Vollständige argv, CWD, UTC-Start-/Endzeiten, Exitcodes und Loghashes stehen in `outputs/loop/foundation-v3-repro/execution.json`. Alle sechs Aufrufe enden mit Exit 0. Erste Ausführung 04:29:03.884614 UTC, letzte beendet 04:29:10.750342 UTC am 2026-10-03. Das sind meine tatsächlich ausgeführten Läufe, getrennt von den früheren Autorenläufen.

Vier Pflichtinputs wurden in beiden Caches direkt von den offiziellen gepinnten URLs heruntergeladen, nicht aus einem Autorencache kopiert:

| Pflichtinput | SHA-256 |
| --- | --- |
| Deutscher Fragebogen 2023 | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| Deutsches Listenheft 2023 | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| Codebook 4.1 | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |
| ESS Conditions of use HTML | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` |

Die Fetchlogs enthalten URL, finale URL, erhaltene Größe und Hash. Die Inhalte wurden hashgeprüft; für diesen Bericht erfolgte keine erneute vollständige Listenheft-, Codebook- oder juristische Einzelprüfung. Der Fragebogen wurde im oben benannten Seitenbereich selbst gelesen.

Beide Neuaufbauten und die eingefrorene v3-Fassung sind bytegleich:

- CSV: `8c73adb8b361db2992f5fe9e321e0c5b978afdc41ba22c1cbb471f92e60057c1`.
- Provenienz: `533a12c517ac49f869aea1fbc09dc86e3c1dfe7ef9bc7b05018b5a49ba753aa6`.

Eigener Testaufruf: `PYTHONDONTWRITEBYTECODE=1 python outputs/loop/foundation-v3-repro/test_response_contract.py`. Exit 0, 26 Tests, `OK`; vollständiges Log unter `tests.log`. Es sind 16 vorhandene eingefrorene Inventartests und zehn eigene Prüfmethoden. Subfälle wurden nicht als zusätzliche unabhängige Tests gezählt.

Die eigenen Prüfungen kontrollieren sämtliche 19 Originalantwortaufgaben samt vorläufigem Status; exakte D7/D8-Tage; Regions-/Hashbindung aller betroffenen Annotationen; Verweigerung aller falschen Seitenbindungen; unbekannte ähnliche IDs statt Bereichsfallback; alle 296 unveränderten sonstigen Felder; fehlende und veränderte Inputs jeder der vier synthetisch dargestellten Quellen mit Abbruch vor Poppler; veränderte CSV mit Abbruch vor Extraktion; die vollständige unveränderte Restliste und die ausgewiesene fehlende Semantikabnahme.

Der zehnte eigene Gegenfall setzt in einer reinen In-memory-Kopie D9 absichtlich auf den alten falschen Antworttyp. `validate` meldet weiterhin `BESTANDEN` für seinen technischen Bereich und `NICHT_GEPRUEFT` für semantische Inventarabnahme. Das ist die erwartete, ausdrücklich beschriebene Validatorgrenze. Es wird nicht als semantischer Erfolg behandelt. Kein absichtlich falsches Inventar wurde in gemeinsame Artefakte geschrieben.

Zusätzlich wurden sieben Originalkontrakte gegen die eingefrorenen v2- und v3-Module ausgeführt: D9, D11, D12, D15, D16, D7 und D8. Die früheren ungenauen Typen werden in v2 als Abweichungen erkannt; in v3 passen die Kontrakte. Beleg: `historical-counterprobes.json`. Diese Prüfung zeigt, dass die gezielten Erwartungen die dokumentierte alte Fehl-/Ungenauigkeit erkennen; sie ist keine Fehlerquote für das Gesamtinventar.

Die sieben Autorenläufe aus `outputs/loop/inventory-round2b/execution.json` wurden separat auf vorhandene Logs, aufgezeichnete Hashes und Exitcodes geprüft. Alle sieben Loghashes passen, alle Exitcodes sind 0; das Testlog dokumentiert 30 Tests. Eigener Beleg `author-log-verification.json`. Ich führe diese 30 nicht als meine Ausführung auf. Meine frischen Neuaufbauten und Tests bestätigen heutige Reproduzierbarkeit; sie beweisen historische Trennung oder Lektüre nicht rückwirkend. Unbeteiligte Loop-/Planvertragstests wurden in diesem eng begrenzten Typaudit nicht erneut ausgeführt.

## Status und verbleibende Grenzen

| Gegenstand | Status | Reichweite |
| --- | --- | --- |
| N-F01, Reparaturrunde 2, D2–D19-Typkorrektur | BESTANDEN | Originallektüre, konkrete Annotationen, Zweigreihenfolge und Gegenfälle |
| Frische öffentliche Reproduktion | BESTANDEN | Zwei Vierquellen-Caches; CSV und Provenienz bytegleich zu v3 |
| Unverändertheit Originalfelder/296 Zeilen | BESTANDEN | Byte-/Feldvergleich gegen v2; kein Gesamtrichtigkeitsnachweis |
| Eigene 26 technische/gezielte Tests | BESTANDEN | Die beschriebenen positiven und negativen Fälle |
| Historischer Fehler in v2 | NICHT_BESTANDEN | Als frühere Fassung erhalten; kein rückwirkendes Umschreiben |
| Ganze Inventarsemantik, Kategorien, Missing, Routing | NICHT_GEPRÜFT | 205 technische Restzeilen; weitere semantische Einzelprüfungen fehlen |
| Andere elf FOUNDATION-Korrekturen in diesem Bericht | NICHT_GEPRÜFT | Außerhalb meines N-F01-Nachprüfauftrags; fremde frühere Urteile nicht als eigene Prüfung übernommen |
| Endgültige Item-/Modellentscheidung und abhängige empirische Entwicklung | BLOCKIERT | Erforderliche Inventar-, getrennte Erstbewertungs-/Claude- und weitere Plan-/Design-/Unsicherheitsvoraussetzungen bleiben offen |
| ESS-Antwortanalyse, A/B, Partei-/LR-Zugriff und Modell-/Präregistrierungstags | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Für die öffentliche Typ- und Reproduktionsprüfung kein zulässiger oder notwendiger Input |
| Website-/Browser-/Releaseabnahme | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Keine UI- oder Ergebnisänderung durch diesen Reviewer; keine Releasefreigabe |

Es gibt keinen neuen belegten erheblichen Befund innerhalb der geprüften Reparatur. Deshalb wird keine neue Finding-ID erzeugt. Das begrenzte Bestehen schließt die Forschungsphase nicht. Der getrennte Juror und die anderen erforderlichen Abnahmen bleiben eigenständige Arbeit.

`pnpm check` wurde von diesem Reviewer nicht erneut ausgeführt. Es wurde ausschließlich ein Bericht und eigene Prüfbelege geschrieben; Appcode und gemeinsame Forschungsartefakte wurden nicht geändert. Die App-Prüfbehauptung des Koordinators ist keine eigene App- oder Methodenabnahme dieses Berichts. Die allgemeinen wissenschaftlichen Voraussetzungen werden durch Berichtformatierung oder technische Tests nicht erfüllt.

## Vollständiger tatsächlicher Startauftrag

Der folgende Auftrag wurde vom Koordinator als mein tatsächlicher Startauftrag übermittelt. Er wird wortgetreu aufbewahrt; er ist kein nachträglich rekonstruierter Prompt.

```text
Du bist frischer unabhängiger Reproduzierbarkeits-/Typprüfer der zweiten Reparatur FOUNDATION-001, kein Autor. Shell-CWD ausschließlich /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003. Prüfpaket reports/loop/packages/FOUNDATION-001/v3/manifest.json SHA b590aaa05137b86e44854468324c85e5aef34718677216db18aeaefaf8d83df4, 47 files/157 sourceInputs. Lies dort Auftrag, AGENTS, Issue, Runde2-Vorabkriterien, Entscheidungen und Korrekturbericht. Frühere v1/v2-Snapshots, fünf Erstberichte und beide abgeschlossenen v2-Berichte sind erlaubt; keine anderen v3-Berichte, PREP-/SOFTWARE-Berichte, aktuellen Autorverteidigungen oder globalen Agent-Auflistungen lesen. Prüfe hashgebundene Eingaben vor und nach; historische sourceInputs können expectedSha/actualAtFreeze samt Notice auf ältere v2-Livepfade beziehen, verifiziere und bezeichne das korrekt statt historische Bytes mit heutigen gleichzusetzen. Auftrag: N-F01 gleiche ID/Reparaturrunde2 kontrollieren. Lies deutsche Originalfundstellen D2–D19 PDF32–39 selbst, überprüfe die18 Typänderungen gegenüber v2, keine breite D2–19-Verhaltensregel, D9 Kontext vor Typentscheidung, D11/12 Körpermerkmale, D15/16 Versorgung, exakte D7/8-Tage, Originalwortlaut/Kontexte aller296 unverändert, 205 technische Restzeilen weiterhin offen. Eigene frische Vierquellen-Cachereproduktion und tatsächliche passende synthetische Tests inkl Gegenfälle; keine Inventar-Gesamtabnahme oder empirischen Schlüsse. Quellenkopien nur eigener Cache outputs/loop/foundation-v3-repro/, keine Fremdvolltexte in Git. Schreiborte ausschließlich dieser eigene Outputordner und reports/loop/reviews/FOUNDATION-001-v3-repro.md. Gemeinsame Forschungsartefakte/Snapshots/Logs nicht ändern. Kein ESS-Rohdaten-/IDs/A/B-/Partei-/LR-Zugriff oder Portal-Analysis; öffentliche Fragebogen/Metadaten erlaubt. Jeder Finding benennt genaue Aussage, Problem, prüfbare Fundstelle, Wirkung, begründeten Schweregrad, Korrektur und Nachprüfung; keine Fehlerquote, Vermutungen sichtbar. Unterschied BESTANDEN/NICHT_BESTANDEN/NICHT_GEPRÜFT/BLOCKIERT/IN_DIESER_PHASE_NICHT_ERFORDERLICH und begrenzte Korrektur vs gesamte Phasenfreigabe. Modell gpt-6.1-sol/ultra geerbt, interne Vorgaben unbekannt; Werkzeuge/Kommandos/Ergebnisse/Trennungsgrenzen dokumentieren. Vollständigen tatsächlichen Startauftrag wortgetreu im eigenen Bericht speichern. Keine zusätzlichen Agents, Commits/Pushes oder globalen Browser-/Agent-Introspektionen. Bericht nach Abschluss unverändert; Pfad/SHA/kurzer Abschluss senden.
```
