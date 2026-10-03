# FOUNDATION-001 v3: begrenzte Quellen- und Antworttypprüfung

Datum: 2026-10-03. Reviewer: Codex-Subagent `/root/foundation_v3_types`, kein Autor und kein Juror. N-F01 bleibt dieselbe Finding-ID, Reparaturrunde 2. Dies ist ein KI-Audit einer eingefrorenen Entwurfsfassung.

## Urteil

**BESTANDEN für die benannte N-F01-Typkorrektur in D2–D19.** Ich habe alle 19 tatsächlich vorhandenen Frage-/Verwaltungslabels einschließlich D10a und D10b auf den deutschen Originalseiten 32–39 selbst textuell und visuell gelesen. Die 18 neuen Antworttypen treffen die jeweilige Aufgabe. Der D9-Verwaltungszweig ist erreichbar; Körpermerkmale und Versorgungsantworten erhalten keinen pauschalen Verhaltensausschluss mehr. D2 und D17 bleiben zutreffend verhaltensbezogen. D14 ist als Versorgungserfahrung weiterhin unverändert.

Die ursprüngliche mittlere Schwere und die niedrige Restschwere aus Runde 1 bleiben in der Historie. Für den hier benannten Mechanismus habe ich keine ungelöste semantische Restbeanstandung gefunden. Das Urteil umfasst Entwurfsannotation und Korrekturbegrenzung. Endgültige Aufnahme, Ausschluss, Polung, vollständige Kategorien-/Routingprüfung, Konstruktvalidität und Phasenabnahmen folgen daraus nicht.

Eine getrennte technische Paketgrenze bleibt sichtbar: Alle 47 eingefrorenen Dateien passen zum v3-Manifest, aber bei 4 von 157 `sourceInputs` zeigen historische Livepfade noch v2-Hashes. Vorher und nachher sind alle tatsächlich gelesenen Paket-/Inputbytes unverändert. Deshalb behaupte ich keine vollständige Übereinstimmung aller `sourceInputs` mit ihren alten `sha256`-Feldern.

## Prüfbasis und Trennung

Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`.

Manifest: `reports/loop/packages/FOUNDATION-001/v3/manifest.json`, SHA256 `b590aaa05137b86e44854468324c85e5aef34718677216db18aeaefaf8d83df4`. Die wissenschaftliche Fassung sind die Kopien unter `v3/files/`; der dortige Code-Commit ist zusätzliche Provenienz, kein Ersatz für die eingefrorenen Bytes. v2 wurde nur für den Änderungsvergleich benutzt. Datenversionen im Manifest wurden als fremde Provenienz gelesen; ich habe keinen Rohdatenhash erneut erhoben.

Gelesen wurden die eingefrorenen AGENTS, der dauerhafte Auftrag, LIFE-93, die drei Runde-2-Dokumente, Prüfregeln, Analyseplan, Belegregister und Lizenzakte. `docs/project.md` wurde als operative Anweisung vor eigenen Schreibaktionen gelesen. Bei einigen gebündelten frühen Toolausgaben trat Kürzung auf; Mandat, Issue, Prüfregeln, Analyseplan und der vollständige relevante Originaltext wurden danach in kleineren vollständigen Ausgaben gelesen. Aus den zulässigen alten Berichten wurden die einschlägigen N-F01-Passagen des ursprünglichen Neutralitäts-Erstberichts sowie beider abgeschlossener v2-Nachberichte gelesen. Die alten Urteile wurden als Geschichte des Findings behandelt. Die Originallektüre und Gegenfälle unten begründen mein Urteil.

Kein neuer v3-FOUNDATION-Bericht wurde geöffnet oder angefordert. Kein PREP-, SOFTWARE-, Loop-Findings- oder Agentregister wurde als Datei gelesen; keine zusätzliche Autorenverteidigung angefordert. Das Dateisystem bleibt gemeinsam und technisch nicht isoliert. Der anfängliche `git status --short` machte Dateinamen anderer Arbeiten sichtbar.

Eine tatsächliche Trennungsverletzung muss ich gesondert nennen: Ein späterer `collaboration.list_agents`-Aufruf lieferte unerwartet abgeschlossene SOFTWARE-Kurzantworten im Tooloutput. Damit wurden fremde, außerhalb des Auftrags liegende Urteilszusammenfassungen sichtbar. Ich habe keine zugehörige Datei geöffnet und verwende diese Aussagen nicht als FOUNDATION-Evidenz. Den Einblick meldete ich dem Koordinator sofort. Eine vollständig technisch erzwungene Kontexttrennung wird daher nicht behauptet. Es fand kein Austausch über die Bewertung der D-Fragen mit einem anderen Reviewer statt.

Geschrieben wurden ausschließlich dieser Bericht und Dateien unter `outputs/loop/foundation-v3-types/`. Python lief mit `-B` oder `dont_write_bytecode`; Inventarcode und Tests wurden bytegleich in einen eigenen Unterordner kopiert. Ihre temporären und Extraktionsausgaben liegen dort. Keine gemeinsamen Parseroutputs wurden überschrieben. Keine weiteren Agents, globalen Installationen, Conda-Aktionen, Commits oder Pushes.

Nicht gelesen oder genutzt wurden `data/raw/`, `data/local/`, ESS-Antworten, A/B, Partei-/Links-Rechts-Antwortwerte, Personenkennungen, Cookies, Credentials oder Storagewerte. Öffentliche Frage-, Code- und Variablendokumentation ist davon getrennt.

## Eigene Originallektüre

Quelle: [deutscher ESS11-Fragebogen 2023](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf), SHA256 `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75`. PDF- und gedruckte Seiten stimmen für 32–39 überein. Ich las die vollständigen acht relevanten Seiten einschließlich Einleitungen, Intervieweranweisungen, sichtbarer Antwortreihen und Routingtext. Der Textauszug und die acht gerenderten Seiten liegen im eigenen Outputordner. Der spätere frische offizielle Abruf lieferte dieselben Originalbytes.

| ID   | PDF-/Druckseite | Selbst rekonstruierte Aufgabe und maßgeblicher Originalbereich                          | Antworttyp in v3                                                     | Gegenüber v2 |
| ---- | --------------- | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------ |
| D2   | 32              | Obst essen, keine Fruchtsäfte; gefrorene Früchte zählen                                 | Selbstberichtete Obstkonsumhäufigkeit                                | geändert     |
| D3   | 33              | Gemüse/Salat essen, keine Kartoffeln; gefrorenes Gemüse zählt                           | Selbstberichtete Gemüse- oder Salatkonsumhäufigkeit                  | geändert     |
| D4   | 33              | Tage mit mindestens 30 Minuten körperlicher Betätigung in sieben Tagen                  | Selbstberichtete körperliche Betätigung                              | geändert     |
| D5   | 33              | Aktuelles, früheres oder nie erfolgtes Zigarettenrauchen                                | Selbstberichtetes gegenwärtiges oder früheres Zigarettenrauchen      | geändert     |
| D6   | 34              | Häufigkeit alkoholischer Getränke in zwölf Monaten                                      | Selbstberichtete Alkoholkonsumhäufigkeit                             | geändert     |
| D7   | 34              | Getränkemenge am letzten Konsumtag aus Montag bis Donnerstag, keine Wochensumme         | Selbstberichtete alkoholische Getränkemenge an Montag bis Donnerstag | geändert     |
| D8   | 35              | Getränkemenge am letzten Konsumtag aus Freitag bis Sonntag, keine Wochensumme           | Selbstberichtete alkoholische Getränkemenge an Freitag bis Sonntag   | geändert     |
| D9   | 35              | Interviewer codiert männlich/weiblich als D10-Zuweisung, keine Selbstbeschreibung       | Administrative Interviewercodierung                                  | geändert     |
| D10a | 35              | Häufigkeit mindestens der Beispiele aus Liste 38 je Gelegenheit in zwölf Monaten        | Selbstberichtete Häufigkeit hoher Alkoholmenge                       | geändert     |
| D10b | 36              | Häufigkeit mindestens der Beispiele aus Liste 39 je Gelegenheit in zwölf Monaten        | Selbstberichtete Häufigkeit hoher Alkoholmenge                       | geändert     |
| D11  | 36              | Körpergröße ohne Schuhe; Schätzung erlaubt                                              | Selbstberichtetes Körpermerkmal: Größe                               | geändert     |
| D12  | 36              | Körpergewicht ohne Schuhe; Schätzung erlaubt                                            | Selbstberichtetes Körpermerkmal: Gewicht                             | geändert     |
| D13  | 37              | Eigene Gesundheitskommunikation mit Haus-/Facharzt in zwölf Monaten; mehrere Nennungen  | Selbstberichteter Kontakt zu ärztlicher Versorgung                   | geändert     |
| D14  | 37              | Nicht erhaltener Arzttermin/benötigte Behandlung aus genannten Gründen in zwölf Monaten | Eigene Versorgungserfahrung oder Versorgungsereignis                 | unverändert  |
| D15  | 37              | Mehrfachgründe fehlender Versorgung, auch Geld/Zeit/regionales Angebot/Warten/Termine   | Selbstberichtete Gründe nicht erhaltener medizinischer Versorgung    | geändert     |
| D16  | 38              | Erhaltene benötigte Versorgung versus in zwölf Monaten kein Bedarf                      | Selbstberichteter Versorgungserhalt oder fehlender Versorgungsbedarf | geändert     |
| D17  | 38              | Eigene unbezahlte Betreuung oder Hilfe aus Liste-42-Gründen                             | Selbstberichtete unbezahlte Betreuung oder Hilfe                     | geändert     |
| D18  | 38              | Wöchentliche durchschnittliche Zeit der D17-Tätigkeit, Sonderantwort unter einer Stunde | Selbstberichteter Zeitumfang unbezahlter Betreuung oder Hilfe        | geändert     |
| D19  | 39              | Eigene Inanspruchnahme genannter Behandlungen in zwölf Monaten, mehrere Nennungen       | Selbstberichtete Nutzung genannter Gesundheitsbehandlungen           | geändert     |

D7/D8 erfragen die Menge an einem letzten Konsumtag aus den jeweils genannten Tagen. Sie erfragen keine ganze Wochenmenge. Die Sonderantwort, an diesen Tagen nie zu trinken, bleibt eine eigene Antwort. Die präzisierten Bezeichnungen Montag–Donnerstag und Freitag–Sonntag sind enger als ein alltagssprachlicher Wochentag-/Wochenendbegriff.

D10a/D10b berichten tatsächlichen Konsum mindestens der jeweils gezeigten Beispielmenge bei einer Gelegenheit. Der Verweis auf unterschiedliche Listen 38/39 und auf D9=1 beziehungsweise D9=2 bleibt in den Begründungen erhalten. Gleiche Häufigkeitsoptionen beweisen keine identische Alkoholschwelle. Die Listeninhalte selbst habe ich in dieser Prüfung nicht abschließend nachgeprüft.

D9 auf S.35 ist ausdrücklich eine Interviewercodierung. D11/D12 auf S.36 fragen nach Größe und Gewicht ohne Schuhe; die erlaubte Schätzung macht daraus kein Verhalten. D15 auf S.37 umfasst mehrere unterschiedliche Gründe nicht erhaltener Versorgung, darunter Geld, Verpflichtungen und fehlendes Angebot. D16 auf S.38 unterscheidet Versorgungserhalt und fehlenden Bedarf. Diese Angaben können mit Verhalten zusammenhängen, ihre Antwortaufgabe ist dadurch aber keine pauschale Verhaltensangabe. D13, D17, D18 und D19 berichten dagegen Kommunikation, Hilfezeit und Inanspruchnahme; ein Verwaltungs-/Versorgungs-/Gesundheitsthema ist allein kein Grund, sie anders zu typisieren.

Die Originalseiten erlauben diese Aufgabenbeschreibung. Sie liefern keine endgültige Eignungsentscheidung für politische Skalen.

## Code, CSV, Status und Belegregionen

Dateifundstellen beziehen sich auf v3/files: `pipeline/inventar.py:138–156` nennt die einzelnen D-Aufgaben. `judgement` in Zeilen 273–280 prüft D9 zuerst, danach eine explizite Menge verhaltensbezogener IDs, dann die weiteren gelesenen Antwortaufgaben. Die pauschale Zahlenbereichsregel D2–D19 ist entfernt. `annotation_evidence` in Zeilen 332–340 bindet die Notiz an Quellenhash und erwartete Originalseite, hält die unabhängige semantische Abnahme jedoch ausdrücklich offen.

Der strukturierte v2/v3-Vergleich ergibt 296 Zeilen in beiden Fassungen und genau 18 geänderte Zeilen. Alle Änderungen betreffen die benannten Typ-/Beleg-/Ausschlussfelder. Alle Wortlaute und großen Originalkontextblöcke bleiben bytegleich. D14 wurde in Runde 2 nicht neu geändert. Vollständiger Feldvergleich: `v2-v3-diff.json`.

Die fünf geänderten Eignungsstatus sind D9, D11, D12, D15 und D16. D9 wechselt von einem vorläufigen Verhaltensausschluss zu `ENTWURF_KONTEXT_ODER_VERWALTUNG`; die vier anderen wechseln zu `ENTWURF_OFFEN` mit leerem Ausschlussgrund. Die übrigen verhaltensbezogenen Einträge behalten `ENTWURF_AUSSCHLUSS_NACH_ISSUE`, jetzt mit der ausdrücklich offenen unabhängigen Einzelabnahme. Das ist ein begründeter Entwurfspfad, keine finale Einzelentscheidung. Bei allen gelesenen D-Einträgen bleibt `polung=OFFEN_NICHT_BESTIMMT`.

Die Antworttypnotizen tragen `ENTWURF_ORIGINALLEKTUERE_AUTOR_NACHPRUEFEN` und `unabhaengige_semantische_abnahme=NICHT_GEPRUEFT`. Mein externer Bericht ersetzt diese historische Autorenstatusangabe nicht. Ich verglich die gespeicherten Wortlautregionen unabhängig mit den frischen Poppler-XML-Tokens samt Koordinaten; sie stimmen überein. Zur präzisen Auffindbarkeit nennt die folgende Tabelle die jeweilige Wortlautregion in PDF-Punkten. Alle x-Grenzen und vollständigen Tokens liegen in `own-probes.json` beziehungsweise im CSV.

| ID   | PDF-Seite | y-Bereich der gespeicherten Wortlautregion | Tokens |
| ---- | --------- | ------------------------------------------ | ------ |
| D2   | 32        | 296.728–334.370                            | 26     |
| D3   | 33        | 50.128–75.050                              | 22     |
| D4   | 33        | 322.048–410.330                            | 47     |
| D5   | 33        | 470.368–495.410                            | 23     |
| D6   | 34        | 62.728–125.690                             | 42     |
| D7   | 34        | 383.968–484.850                            | 54     |
| D8   | 35        | 50.128–125.690                             | 49     |
| D9   | 35        | 296.728–309.050                            | 2      |
| D10a | 35        | 437.368–538.250                            | 52     |
| D10b | 36        | 62.728–138.290                             | 48     |
| D11  | 36        | 372.688–448.250                            | 36     |
| D12  | 36        | 558.568–621.410                            | 27     |
| D13  | 37        | 50.128–125.690                             | 55     |
| D14  | 37        | 271.528–321.770                            | 38     |
| D15  | 37        | 461.248–511.490                            | 30     |
| D16  | 38        | 62.728–75.050                              | 6      |
| D17  | 38        | 239.848–277.490                            | 30     |
| D18  | 38        | 508.048–545.570                            | 17     |
| D19  | 39        | 62.728–125.690                             | 35     |

Eine Wortlautregion ist nicht immer die ganze semantisch nötige Fundstelle. Bei D9 enthält sie nur die Codieranweisung, bei D16 nur den kurzen Fragebeginn. Für meine Typentscheidung wurden zusätzlich die Antwortreihen und der Kontext auf der jeweiligen Originalseite gelesen. Ich behaupte daher nicht, diese kurzen Tokens allein belegten männlich/weiblich oder die Versorgungserhalt-/Bedarf-Unterscheidung. Die manuelle Lektüre des vollständigen Originalbereichs ist hier Teil des Nachweises. Kategorien- und Routingfelder bleiben getrennte, nicht vollständig abgenommene Artefakte.

## Tatsächlich ausgeführte Gegenfälle und Neuaufbau

Die eigenen Erwartungen in `own-probes.py` wurden aus der Originallektüre formuliert, anschließend mit Code und CSV verglichen. Alle 19 D-Aufgaben stimmen im geprüften Umfang überein. Bei jeder Aufgabe wurde die falsche Originalseite als Gegenfall ausgeführt; alle wurden mit `RuntimeError` abgewiesen. Die nicht vorhandenen Labels D10, D2a, D19a und D999 bleiben ausdrücklich unbekannt. Sie erhalten keinen stillen Verhaltensstatus. Damit prüfen die Gegenfälle auch die Entfernung der früheren Bereichsregel. D2/D17 sind positive Kontrollen für wirklichen Verhaltensbezug; D9/D11/D12/D15/D16 die Gegenkontrollen für andere Aufgaben.

Als weitere Grenze änderte ich für D9/D11/D12/D15/D16 jeweils nur den Antworttyp in einer Speicher-Kopie zurück auf den falschen generischen Typ. Der technische Validator meldete weiterhin `BESTANDEN`. Das ist ein tatsächlich ausgeführter negativer Kontrollfall für die Aussagekraft des Checks. Der Code und sein Prüfresultat beanspruchen ausdrücklich keine vollständige Antwortsemantikabnahme. Deshalb ist dies keine erneute ungelöste N-F01-Korrekturbehauptung; es bestätigt, dass technische Checks die manuelle Quellenprüfung nicht ersetzen.

Die Inventartests liefen in der eigenen Kopie: 16 Tests, Exit 0, einschließlich des neuen D-Verwaltungs-/Körper-/Versorgungsgegenfalls. Ich führte keine empirische Rechnung und keinen statistischen Softwarecheck durch.

Ein eigener zunächst leerer öffentlicher Cache wurde mit den vier offiziellen gepinnten Inputs befüllt. Fetch, Build und Check liefen mit ausdrücklichen eigenen Cache-, CSV- und Provenienzpfaden, jeweils Exit 0. Die erzeugten Bytes sind identisch mit v3:

| Artefakt                        | Eigener SHA256                                                     | Vergleich mit v3/files |
| ------------------------------- | ------------------------------------------------------------------ | ---------------------- |
| `data/inventar.entwurf.csv`     | `8c73adb8b361db2992f5fe9e321e0c5b978afdc41ba22c1cbb471f92e60057c1` | byteidentisch          |
| `data/inventar.provenienz.json` | `533a12c517ac49f869aea1fbc09dc86e3c1dfe7ef9bc7b05018b5a49ba753aa6` | byteidentisch          |

Der Check berichtet 296 Zeilen und weiterhin 205 technische Restzeilen. Er meldet keine finale Itementscheidung und keine vollständige semantische Inventarabnahme. Das Ergebnis reproduziert den jetzigen öffentlichen Aufbau; es beweist nicht nachträglich alle historischen Autorenaufrufe.

Vollständige argv, Arbeitsverzeichnisse, UTC-Start-/Endzeiten, tatsächliche Exitcodes und Loghashes der maßgeblichen fünf Prüfaufrufe stehen in `execution.json`. Die vollständigen Skriptbytes liegen daneben. Die echten inneren Kommandos waren:

| Lauf                 | Tatsächlicher argv                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Exit | Log-SHA256                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------ |
| `inventory-tests`    | `/usr/bin/python -B -m unittest pipeline.tests.test_inventar -v`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0    | `325edcb68099512548b025e5752c0a31a8dc508f94598abe7f7fa0c7e14872cf` |
| `fresh-public-fetch` | `/usr/bin/python -B /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/isolated/pipeline/inventar.py fetch --cache /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/fresh-public-cache`                                                                                                                                                                                                                                                                        | 0    | `8d4eea722c2e19d7c4db3510bfd4afd725aef299497e49979a5bbaf8cfeed87e` |
| `fresh-public-build` | `/usr/bin/python -B /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/isolated/pipeline/inventar.py build --cache /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/fresh-public-cache --csv /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/rebuilt.csv --provenance /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/rebuilt.provenance.json` | 0    | `5d8ee58a077d8855b8220d38c5b9a9bfb0ac4b331925ac395886c0c3a34c5b82` |
| `fresh-public-check` | `/usr/bin/python -B /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/isolated/pipeline/inventar.py check --cache /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/fresh-public-cache --csv /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/rebuilt.csv --provenance /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/rebuilt.provenance.json` | 0    | `84b1ebdc6f8699e0a9d9b065b8333519daae0a6fa9495e8bebc598729318404d` |
| `own-probes`         | `/usr/bin/python -B /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/outputs/loop/foundation-v3-types/own-probes.py`                                                                                                                                                                                                                                                                                                                                                                                                                                 | 0    | `9ce76eb72c50f59342f28746346872f6a0d2c13942f83c84e997c6cc6e1f1a94` |

Weitere tatsächliche Shellaufrufe zur Lektüre und Identität waren `cat` auf den oben genannten eingefrorenen Dokumenten und Skills, `rg --files` auf Paket/operativen Dokumentnamen/eigenen Outputs, `rg -n` auf D-Code und zulässigen N-F01-Berichtspassagen sowie `sed -n` auf den im Bericht genannten Code-/Berichtsabschnitten. Diese endeten mit Exit 0. Vor-/Nachhashes und CSV-Diff wurden mit `python -B` ausgeführt; der Nachlauf lautet `python -B outputs/loop/foundation-v3-types/check-hashes.py`, Exit 0.

Die Originalextraktion war `pdftotext -f 32 -l 39 -layout outputs/loop/theory/ESS11_questionnaires_DE.pdf outputs/loop/foundation-v3-types/original-D2-D19-pages32-39.txt`, anschließend `pdftoppm -f 32 -l 39 -scale-to 1600 -png -r 100 outputs/loop/theory/ESS11_questionnaires_DE.pdf outputs/loop/foundation-v3-types/DE-Q-page`, beide Exit 0. Ein erster `view_image`-Aufruf mit ungepolstertem Dateinamen scheiterte, weil Poppler dreistellige Seitennamen erzeugt. Danach wurden alle acht tatsächlich erzeugten Dateien `DE-Q-page-032.png` bis `DE-Q-page-039.png` erfolgreich geöffnet und gelesen. Der Fehler bleibt Teil des Toolverlaufs; er ist kein fehlgeschlagener Quellenabruf.

`python -V` und `pdftotext -v` ergaben Python 3.14.7 und Poppler 26.08.0, Exit 0. Ein gemeinsames `pnpm check` wurde von diesem Reviewer nicht ausgeführt: Der enge Auftrag erlaubt ausschließlich eigene Report-/Outputschreibpfade, während der Gesamtcheck gemeinsame Buildartefakte erzeugt. Der Koordinator erhielt diese Grenze zur zentralen Prüfung. Die Berichtformatprüfung wird separat in `report-format.json` protokolliert; sie ist keine wissenschaftliche Abnahme. Der erste Standardaufruf gab Exit 0 aus, prüfte den Bericht wegen einer Ignore-Regel aber nicht. Die explizite Prüfung mit `--ignore-path /dev/null` fand zunächst Formatabweichungen, Exit 1. Anschließend wurde ausschließlich die eigene, noch nicht versiegelte Berichtdatei formatiert und mit derselben ausdrücklichen Ignore-Umgehung geprüft, Exit 0. Kein bestehender fremder Erstbericht wurde formatiert.

## Identitätsprüfung und offene Manifestreferenzen

Vorprüfung: 2026-10-03T04:19:32.726134+00:00; Nachprüfung: 2026-10-03T04:33:18.862396+00:00. Beide Listen enthalten 47 Dateieinträge und 157 Inputeinträge, mit erwarteten und tatsächlich berechneten Hashes. `changedSinceBefore` ist leer. Alle v3/files-Hashes passen. 153 Inputreferenzen passen unmittelbar zu ihrem `sha256`; die folgenden vier tun das nicht:

| Livepfad in sourceInputs          | Erwarteter historischer SHA256                                     | Tatsächlicher v3-SHA256 vorher/nachher                             |
| --------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `pipeline/inventar.py`            | `84ff2e1c2868170ef6cf9ecdb050d2d26a802e57c7c324ae938bb8fa951c615e` | `548109c85300e6a0ecee57e92af7acc5ec9e748e9d8bf7ee5daeba18e8580190` |
| `pipeline/tests/test_inventar.py` | `0d61d2d42ddc16f8ca8d6ff3b9155e14a0ae1c903ffc2027ad0fc23235914e85` | `86fea4e04c2f19ea5e3b8de6b72d6ef7f869194faf0ab27df4f5e6b6b3b9f07e` |
| `data/inventar.entwurf.csv`       | `89d2c4611d44faee3e44d27e66e5e68550a5611112cf2cf63f96fa5d8a8b84f3` | `8c73adb8b361db2992f5fe9e321e0c5b978afdc41ba22c1cbb471f92e60057c1` |
| `data/inventar.provenienz.json`   | `89c75a95f2da2610396d25fd7428f51d213a71446a5abba50eed73a28fd4ecb7` | `533a12c517ac49f869aea1fbc09dc86e3c1dfe7ef9bc7b05018b5a49ba753aa6` |

Ich habe die vier historischen Hashes gegen die zulässigen v2/files berechnet: Sie passen dort exakt. Die tatsächlichen Livebytes passen dagegen jeweils zu v3/files. Die vier `sourceInputs`-Objekte haben kein eigenes `actualSha256AtFreeze`-Feld und keinen Versionspfad, der den alten Hash auf v2 bindet. Dies ist eine reproduzierbare Grenze der Paketprovenienz. Sie verfälscht den hier ausgeführten Typvergleich nicht, weil dessen Basis die vier eindeutig gehashten v3-Kopien und der passende öffentliche Originalfragebogen sind. Sie verhindert aber die pauschale Aussage „alle 157 sourceInput-Hashes stimmen mit dem Manifest überein“.

Zur Behebung kann der Koordinator historische Inputreferenzen ausdrücklich an v2/files binden oder alte erwartete und aktuelle Hashes in einer neuen Manifestfassung getrennt ausweisen. Das jetzige Manifest darf dabei nicht still geändert und dieser Bericht nicht auf einen neuen Hash übertragen werden. Der Befund ist eine technische Verweisgrenze, keine neue empirische oder politische Fehlerbehauptung. Er wurde dem Koordinator vor dem semantischen Urteil gemeldet; gemeinsame Dateien wurden nicht verändert.

## Status und Grenzen

| Gegenstand                                                                 | Status          | Umfang                                                                             |
| -------------------------------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------- |
| N-F01, Runde 2: benannte D2–D19-Antworttypen und Korrekturbegrenzung       | BESTANDEN       | Eigene Originallektüre aller tatsächlichen Labels, Code-/CSV-Abgleich, Gegenfälle. |
| Identität des v3-Manifests und der eingefrorenen Dateien                   | BESTANDEN       | Erwarteter Manifesthash und alle v3/files passen.                                  |
| Unverändertheit aller Paket-/Inputbytes über diese Prüfung                 | BESTANDEN       | Vollständige Vor-/Nachlisten; keine Änderung.                                      |
| Pauschale Identität aller sourceInputs mit ihrem eigenen sha256-Feld       | NICHT_BESTANDEN | Vier eindeutig festgestellte alte Livepfad-Verweise.                               |
| Eigene Inventartests und frischer öffentlicher Neuaufbau                   | BESTANDEN       | Technische Prüfschritte, gleiche Bytes in derselben Python-/Popplerumgebung.       |
| Vollständige Kategorien-, Missing-, Kontext-, Routing- und Inventarabnahme | NICHT_GEPRÜFT   | Dafür reichen weder Typkorrektur noch technische Gegenfälle.                       |
| Endgültige Itemauswahl, Ausschlüsse und Polung                             | NICHT_GEPRÜFT   | Unabhängige Einzelabnahmen bleiben offen.                                          |
| Empirische Validität, Invarianz, Score-/Vergleichs-/Unsicherheitsbefunde   | NICHT_GEPRÜFT   | Keine Antwortdaten, keine empirische Auswertung.                                   |
| Phasen- oder öffentliche Freigabe                                          | NICHT_GEPRÜFT   | Dieser Bericht erteilt keine solche Freigabe.                                      |

Fehlende vorgeschriebene Claude-/andere-Modellfamilienurteile werden durch diesen Codex-Bericht nicht erfüllt. Fehlende künftige Empirie und menschliche Prüfungen werden hier auch nicht als gescheiterte Studien ausgegeben. Es wird weder politische Biasfreiheit noch ein gerichteter politischer Effekt behauptet.

## Modell, Werkzeuge und tatsächlicher Startauftrag

Anbieter-/Agentfamilie: OpenAI Codex. Die Modellbezeichnung GPT-6.1-Sol ist die Laufzeitangabe im tatsächlichen Startauftrag. Ein gesonderter Provider-/API-Nachweis der internen Modellrevision lag mir nicht vor; interne Revision, weitere Anbieterinstruktionen und eine separat überprüfte Reasoning-Konfiguration bleiben unbekannt. Keine andere Modellfamilie wurde aufgerufen.

Die Laufzeit bot Shell-/Datei-/Bildwerkzeuge über `functions.exec`, Web-, Bildgenerierungs-, Clock-, Collaboration- und CUA-Werkzeuge sowie weitere lazy-discoverable Tools an. Tatsächlich genutzt wurden `functions.exec`, `exec_command`, `apply_patch`, `write_stdin`, `view_image`, `collaboration.send_message` und der oben dokumentierte einzelne `collaboration.list_agents`-Aufruf. Keine Browsersteuerung oder Connector-/Credentialabfrage. Die einzige externe Kommunikation dieser Prüfung bestand aus Koordinatornachrichten im Agentkanal. Die frischen öffentlichen Dokumente wurden durch das gepinnte Parser-Fetch mit Python HTTPS abgerufen.

Gelesene Skills: Unslop für den eigenen deutschen Bericht und PDF für die textuelle/visuelle Originallektüre. Keine Skilldatei wurde geändert. Der vollständige tatsächlich erhaltene Startauftrag ist zusätzlich unter `startauftrag.txt` gesichert. Wortlaut:

```text
Unabhängige begrenzte FOUNDATION-N-F01-Korrekturprüfung, Runde2, kein Autor/Juror. Worktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003 explizit. Dasselbe Paket für zwei Reviewer: reports/loop/packages/FOUNDATION-001/v3/manifest.json SHA256 b590aaa05137b86e44854468324c85e5aef34718677216db18aeaefaf8d83df4,47Dateien/157öffentliche/synthetischeSourceInputs. Lies eingefrorene AGENTS/Auftrag/Issue und FOUNDATION-001-runde2-pruefauftrag/-entscheidungen/-korrekturbericht. Zulässig v1/v2-Ausgang und ursprüngliche abgeschlossene FOUNDATION-Erstberichte+v2-Nachberichte, keine neuen v3-Prüferurteile, kein PREP/SOFTWARE/Loopfindings/Agentregister oder Autorenverteidigung. Schwerpunkt Quellen/Antwortsemantik: ALLE tatsächlichen D2–D19-Fragen einschließlich D10a/b an DE-Q OriginalPDF32–39 selbst lesen; neue18Typen/Codebranch/gegenüber v2 geänderte Status überprüfen. D9 Verwaltung, D11/12 Körpermerkmale, D15/16 Versorgung, D2/D17 tatsächliches Verhalten; keine gewünschte Zahl Findings. Keine definitive Itemauswahl/Polung/Kategorien-/Routing-Gesamtabnahme aus engem Prüfumfang ableiten. Eigene relevante Gegenfälle tatsächlich ausführen, Originalfundstellen präzise. 47Datei+157Inputhashesvor/nach. Nur eigene reports/loop/reviews/FOUNDATION-001-v3-types.md und outputs/loop/foundation-v3-types/ schreiben. Keine gemeinsamen Artefakte/SourceInputs überschreiben; keine globalen Installs/Conda/Commit/Push/weitereAgents. Kein data/raw/local/ESSantworten/A/B/Partei/LR/Personendaten, Cookie-/Credential-/Storagewerte. Öffentliches DokumentationPDF erlaubt. Python -B/dont_write_bytecode oder eigene Kopien; nicht Standardparseroutputs überschreiben. Vollständiger tatsächlicher Startauftrag wortgetreu, tatsächliche Tools/Modellnachweis(GPT-6.1-Sol laut Runtime; interne unbekannt), echte Kommandos/Exitcodes/Originallektüre/Grenzen dokumentieren. Gleiche Probleme N-F01/Runde2 behalten. Prüferstatus nur benannteKorrektur/Begrenzung, keine Phasen- oder empirische Freigabe. Bericht vollständig versiegeln und SHA+Kurzbefund melden.
```

## Abschluss

Die benannte N-F01-Korrektur ist im engen geprüften Umfang bestätigt. Der Bericht, eigene Kommandologs, Quellenableitungen, Gegenfälle und Hashlisten werden mit einem abschließenden `final-artifacts.json` samt separater SHA256-Datei versiegelt. Dieses Manifest enthält den endgültigen Bericht-Hash; der Bericht enthält keinen selbstreferenziellen Hash. Nach der Versiegelung wird diese ursprüngliche Prüferfassung nicht geändert.
