# INVENTORY-004-E: unabhängige Quellen- und Inhaltsprüfung

Erstbericht vom 2026-10-03. Reviewer: `inventory004_e_sources`. Geprüft wurde ausschließlich Paket v1 mit Manifest-SHA-256 `0d124297e3410fd108dfeb1a676cb55a9562f4aa1b5e5adc52f8ddf95de66958`. Der Bericht wird nach seinem abschließenden Formatcheck nicht mehr verändert.

## Urteil und Reichweite

Die 32 technischen E-Identitäten, deutschen Frageformulierungen, gedruckten Code-/Labelzuordnungen, Variantenfilter, Listen, maßgeblichen Einleitungen und Codebook-4.1-Zuordnungen stimmen im geprüften Umfang mit den Originalen überein. Ein geringes Finding betrifft einen zusätzlichen Punkt in der als sichtbar bezeichneten Transkription von Liste 58. Keine erhebliche inhaltliche Beanstandung festgestellt. Die exakte sichtbare Transkription erhält wegen E-S01 `NICHT_BESTANDEN`; die übrige dokumentierte Quellenzuordnung erhält im unten begrenzten Umfang `BESTANDEN`.

Das ist eine Quellenprüfung eines Entwurfs. Eignung, Polung, Konstrukte, Datenedition 4.2, empirisches Antwortverhalten und wissenschaftliche Abnahmen erhalten dadurch keine Freigabe. Der Ausgangshash der gefrorenen E-JSON ist `2c7ef03dca2585bf6476eabf46f8508b3430666d30f07283bc84cd6b1978a224`.

## Tatsächliche Originallektüre

Die drei öffentlichen PDF-Originale wurden in eigene Dateien kopiert, mit Poppler textuell extrahiert und unabhängig neu gerendert. Selbst visuell gelesen wurden sämtliche deutschen Fragebogenseiten 43–54, sämtliche Listenheftseiten 51–68 mit Listen 50–67 und sämtliche Codebook-Seiten 208–218. Das sind 41 vollständige Seiten. Die Renderings haben maximal 1800 Pixel; Liste 58 wurde zusätzlich als Ausschnitt mit 300 dpi gelesen. Die Codebook-Seiten wurden außerdem vollständig im Layout-Extrakt gelesen. PDF- und gedruckte Fragebogenseiten stimmen hier überein; die gedruckten Codebook-Seiten liegen jeweils eins darunter. Auf den Listenheftseiten steht keine gesonderte Seitennummer.

Die drei offiziellen PDF-URLs und der ESS-Disclaimer wurden unabhängig per HTTP erneut abgerufen. Alle vier Abrufe lieferten Status 200 und bytegleiche Inhalte gegenüber den Pins. Der vorausgehende Web-Tool-Aufruf des Disclaimers scheiterte mit 502 und zählt nicht als erfolgreiche Lektüre. Die erfolgreiche HTML-Lektüre erfolgte an der selbst gespeicherten HTTP-Fassung.

| Quelle                      | Original-SHA-256                                                   | Eigene Lektüre                                                 |
| --------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------- |
| ESS11_questionnaires_DE.pdf | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` | PDF 43–54, vollständig visuell und textuell                    |
| ESS11_showcards_DE.pdf      | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` | PDF 51–68, vollständig visuell; Liste 58 zusätzlich vergrößert |
| ESS11_appendix_a7_e04_1.pdf | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` | PDF 208–218, vollständig visuell und textuell                  |
| ESS Conditions of use, HTML | `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d` | Originalabschnitt selbst gelesen                               |

Die komplette gefrorene AGENTS-Fassung, der Dauerauftrag, die gesicherte LIFE-93-Beschreibung, Prüfregeln, Analyseplan, Analyseanforderungen, Lizenzakte, E-Prüfauftrag und Autorenbericht wurden gelesen. Dazu kamen der aktuelle Projektstand, Belegregister und Entscheidungen, die gefrorene E-JSON sowie die PDF- und Unslop-Skills. Keine anderen Erstberichte, Jurorberichte, Loop-Findings, Agentlisten oder zusätzliche Autorenverteidigung wurden gelesen. Der erste `git status --short` zeigte fremde Dateinamen; deren Inhalte wurden nicht geöffnet.

## Abdeckung aller Identitäten

Die folgende Tabelle fasst die selbst kontrollierten Originalzuordnungen zusammen. „Stimmt“ betrifft Wortlaut, Quelle, Antwortzellen und den annotierten Antwortgegenstand; es ist kein Eignungs- oder Polungsurteil. Das gemeinsame Finding E-S01 bleibt bei E12/E13 gesondert offen.

| Identität | Deutscher Fragebogen | Liste / PDF-Seite | Variable, Codebook-PDF | Ergebnis                                           |
| --------- | -------------------- | ----------------- | ---------------------- | -------------------------------------------------- |
| E1        | 43                   | 50 / 51           | nobingnd, 208          | Stimmt; Verweigerungscode und Anonymisierung offen |
| E2        | 43                   | 51 / 52           | likrisk, 208           | Stimmt                                             |
| E3        | 44                   | 51 / 52           | liklead, 208–209       | Stimmt                                             |
| E4        | 44                   | 51 / 52           | sothnds, 209           | Stimmt                                             |
| E5        | 45                   | 51 / 52           | actcomp, 209           | Stimmt                                             |
| E6        | 45                   | 52 / 53           | mascfel, 210           | Stimmt; Reihenfolge nur als Anweisung belegt       |
| E7        | 46                   | 53 / 54           | femifel, 210           | Stimmt; Reihenfolge nur als Anweisung belegt       |
| E8M       | 46                   | 54 / 55           | impbemw, 210–211       | Stimmt; E1 = 1                                     |
| E8W       | 47                   | 54 / 55           | impbemw, 210–211       | Stimmt; E1 = 2                                     |
| E9M       | 47                   | 55 / 56           | trmedmw, 211           | Stimmt; E1 = 1, medizinische Kategorie offen       |
| E10M      | 47                   | 56 / 57           | trwrkmw, 211           | Stimmt; E1 = 1                                     |
| E11M      | 48                   | 57 / 58           | trplcmw, 211–212       | Stimmt; E1 = 1                                     |
| E9W       | 48                   | 55 / 56           | trmedmw, 211           | Stimmt; E1 = 2, medizinische Kategorie offen       |
| E10W      | 48                   | 56 / 57           | trwrkmw, 211           | Stimmt; E1 = 2                                     |
| E11W      | 48                   | 57 / 58           | trplcmw, 211–212       | Stimmt; E1 = 2                                     |
| E12       | 49                   | 58 / 59           | trmdcnt, 212           | Stimmt; E-S01 zur sichtbaren Listenfassung         |
| E13       | 49                   | 58 / 59           | trwkcnt, 212           | Stimmt; E-S01 zur sichtbaren Listenfassung         |
| E14       | 49                   | 59 / 60           | trplcnt, 212           | Stimmt                                             |
| E15       | 50                   | 60 / 61           | eqwrkbg, 213           | Stimmt                                             |
| E16       | 50                   | 61 / 62           | eqpolbg, 213           | Stimmt                                             |
| E17       | 51                   | 62 / 63           | eqmgmbg, 213–214       | Stimmt                                             |
| E18       | 51                   | 63 / 64           | eqpaybg, 214           | Stimmt                                             |
| E19       | 51                   | 64 / 65           | eqparep, 214           | Stimmt                                             |
| E20       | 52                   | 64 / 65           | eqparlv, 214–215       | Stimmt, einschließlich vollständiger Vignette      |
| E21       | 52                   | 64 / 65           | freinsw, 215           | Stimmt                                             |
| E22       | 52                   | 64 / 65           | fineqpy, 215–216       | Stimmt                                             |
| E23       | 53                   | 65 / 66           | wsekpwr, 216           | Stimmt                                             |
| E24       | 53                   | 65 / 66           | weasoff, 216           | Stimmt                                             |
| E25       | 53                   | 65 / 66           | wlespdm, 216–217       | Stimmt                                             |
| E26       | 54                   | 66 / 67           | wexashr, 217           | Stimmt, einschließlich Definition                  |
| E27       | 54                   | 67 / 68           | wprtbym, 217           | Stimmt                                             |
| E28       | 54                   | 67 / 68           | wbrgwrm, 217–218       | Stimmt                                             |

E1 druckt 1, 2, 3 und 8; Liste 50 druckt „Möchte nicht antworten“ ohne Zahl. Die JSON erfindet dafür keinen Code. Die Codebook-Beschreibung nennt für Deutschland Anonymisierung und verweist auf Country documentation. Deren konkrete Umsetzung, insbesondere in Ausgabe 4.2, ist hier nicht geprüft.

E2–E8 und E15–E18 drucken gültige Kategorien 0–6, mit verbal bezeichneten Enden und unbeschrifteten Zwischenkategorien im deutschen Fragebogen. Die Codebook-Zwischenlabels sind Ziffern. Der Fragebogen druckt 7 für Verweigerung und 8 für Weiß nicht. Diese Unterschiede sind getrennt erfasst. Die Einleitung und bedingte Intervieweranweisung bei E2–E5 sind erhalten. E6/E7 erhalten die Einleitung und die gedruckte Randomisierungsanweisung. Ein tatsächlicher CAPI-Lauf folgt daraus nicht.

Bei E8–E11 sind die Männer- und Frauenformulierungen, die gedruckten E1-Filter und die gemeinsamen Codebook-Locations korrekt getrennt. E9–E11 erhalten 1/2 für einmalige/mehrmalige Erfahrung, 3 für Nein und 4 als gesonderte Erfahrungsalternative. 4 wird nicht zur Skalenmitte, Verweigerung oder pauschal zu Nein gemacht. E10/E11 übernehmen den persönlichen Erfahrungskontext aus E9 in der jeweiligen Variante. Bei E9 bleibt der deutsche Wortlaut mit „oder habe versucht“ erhalten. Der englische Codebook-Wortlaut stützt den bezeichneten Antworttyp, löst die deutsche Formulierungsgrenze aber nicht auf. Die offenen Einträge zur medizinischen Kategorie und zu Fußnote 86 sind zutreffend als offen geführt.

E12/E13 erhalten die gemeinsame Einleitung zur aktuellen Lage in Deutschland. E14 nennt die allgemeine Behandlung durch die Polizei. Die Kategorien 1/2/3 enthalten zwei Richtungsangaben und Gleichbehandlung; sie begründen durch ihre Zahlenfolge keine ordinale Einstellungsachse. Die JSON bildet daraus keinen Score. E15–E18 betreffen bewertete Folgen bestimmter Gleichstellungszustände. E19–E22 betreffen konkrete Maßnahmen oder Sanktionen. Bei E20 sind Vollzeitarbeit beider Personen, ungefähr gleiches Einkommen, neugeborenes Kind und Anspruch beider auf bezahlte Elternzeit vollständig enthalten.

E23–E28 erhalten die gemeinsame Einleitung. Die Antwortgegenstände bleiben verschieden: Zuschreibungen, Lohnwahrnehmung, Schutzforderung und moralischer Vergleich. Die Definition sexueller Belästigung steht vollständig bei E26 und stammt aus Liste 66. Gemeinsames Thema und Skalenform werden nicht als umfassende Gender-Haltung oder fertige Dimension ausgegeben. Das Codebook-Metadatum `CanCalculateMean` wird zutreffend nicht als methodische Freigabe behandelt.

## E-S01: Textlagen-Punkt in der sichtbaren Transkription von Liste 58

Schwere: gering. Betroffen sind `/fragen/15/listenheft/sichtbare_kategorien_de/wert/2` und `/fragen/16/listenheft/sichtbare_kategorien_de/wert/2` der gefrorenen JSON, also E12/E13. Beide Werte enden mit `behandelt.` und tragen den Status `VISUELL_GELESENE_TRANSKRIPTION_REVIEW_OFFEN`.

Originalbeleg: ESS11_showcards_DE.pdf, PDF-Seite 59, Liste 58, dritte Kategorie. Die sichtbare Kategorie endet ohne Punkt. Der Poppler-Text-/Tokenextrakt enthält hingegen `behandelt.` bei X 209.07–293.13, Y 339.2583–363.8283. Die JSON bewahrt diesen Rohbefund korrekt in `SC-L58-page`; die Abweichung betrifft dessen Übernahme in die sichtbare Lesefassung. Die vollständige Seite und ein eigener Ausschnitt mit 300 dpi wurden visuell kontrolliert. Im Ausschnitt liegt nach dem letzten Buchstaben im Rechteck X 805–850 / Y 145–215 kein dunkles Pixel. Das unterstützt die visuelle Beobachtung; der Pixelcheck allein ist keine semantische Prüfung.

Problem und Wirkung: Die Datei unterscheidet sonst ausdrücklich zwischen Roh-Textlage und sichtbarer Transkription. Hier wird ein nur in der Textlage enthaltenes Satzzeichen zur sichtbaren Vorlage erklärt. Kategorienbedeutung, Codes und Filter werden dadurch nicht verändert. Der Befund ist deshalb gering und begründet keinen empirischen Fehler oder erheblichen Forschungsstopp.

Konkrete Korrektur: Nur den abschließenden Punkt in den beiden sichtbaren Kategorienwerten entfernen und die Abweichung zwischen Textlage und sichtbarer Lesefassung bei Liste 58 dokumentieren. Roh-Tokens, Originalextrakt und deren Prüfsummen unverändert erhalten. Falls eine andere Originaldarstellung einen sichtbaren Punkt zeigt, diese Darstellung mit Renderwerkzeug, Parametern und Hash belegen und den gewählten Darstellungsumfang kenntlich machen.

Nachprüfung: Liste 58 mit dem gepinnten Original neu rendern, die letzte Kategorie vergrößert lesen und beide sichtbaren JSON-Werte prüfen. Alle anderen Kategorien-/Filter-/Listenchecks erneut gezielt ausführen. Der eigene Prüfer zeigt für die Ausgangsfassung exakt die zwei betroffenen Werte; eine ausschließlich eigene, im Speicher um diese Punkte korrigierte Kandidatenfassung besteht dessen begrenzte Semantikchecks. Das ist keine Korrektur der gemeinsamen Autorenfassung und keine Autorenabnahme.

## Lizenzbefund

Der Originalabschnitt [Conditions of use](https://www.europeansocialsurvey.org/contact/disclaimer) sagt getrennt: „European Social Survey data is licensed under CC BY-NC-SA 4.0“ und „European Social Survey documentation is licensed under CC BY-SA 4.0“. Beide Aussagen wurden im selbst abgerufenen HTML gelesen. Der Abschnitt beginnt im UTF-8-Text bei Zeichenoffset 127912. Eigene HTML-Datei, Abschnitt und Fetchlog liegen im Reviewer-Verzeichnis.

Die JSON unterscheidet Dokumentation, Daten und eigene übrige Repositoryartefakte. Attribution, Quellen-URLs, Versionen, Dokumenthashes und Bearbeitungshinweis sind vorhanden. Es wird keine pauschale Repositorylizenz und keine abgeschlossene Veröffentlichungserlaubnis für spätere Web-/Modellexporte behauptet. Das 4.1-Zitationsbeispiel des Disclaimers wird nicht zur Datenzitation für 4.2 erklärt. Der Quellenbefund ist `BESTANDEN`; eine konkrete spätere Veröffentlichungsprüfung und rechtsfachliche Freigabe sind `NICHT_GEPRUEFT`.

## Eigene Prüfungen und Gegenfälle

`python3 outputs/loop/inventory004-e-sources/source_checks.py` endete mit Exit 0. Das eigene Skript verwendet manuell aus den Originalseiten festgehaltene Kategorien, Listen-, Variablen- und Filterzuordnungen sowie maßgebliche Kontexttexte. Es liest die gefrorene JSON; es importiert und startet keinen Autorbuilder und keinen Autorentest. Seine Originalkontrolle erfasst 32 Identitäten. Das Ergebnis nennt die beiden E-S01-Abweichungen ausdrücklich und erklärt sie nicht für bestanden.

Vier tatsächlich mutierte eigene Kandidatdateien wurden erzeugt. Ausgangspunkt ist nur für diese Gegenfälle eine eigene Kopie mit der genannten Punktkorrektur. Jeder Kandidat unterscheidet sich tatsächlich von dieser Kopie; jeder erzeugt genau den erwarteten Prüfverstoß:

| Gegenfall             | Änderung                                        | Tatsächliches Ergebnis                           |
| --------------------- | ----------------------------------------------- | ------------------------------------------------ |
| label_swap            | E12-Code 1 erhält das Richtungslabel von Code 2 | `E12:questionnaire_code_label_cells`, abgewiesen |
| variant_filter_wrong  | E8W erhält den Männerfilter E1 = 1              | `E8W:variant_filter`, abgewiesen                 |
| list_assignment_wrong | E11M erhält Listennummer 56                     | `E11M:showcard_assignment`, abgewiesen           |
| definition_removed    | E26 verliert den Kontext mit der Definition     | `E26:definition`, abgewiesen                     |

Die Originalzellenzuordnung wurde außerdem an den vollständigen gerenderten Tabellen selbst gelesen. Ein einzelnes Tokenvorkommen zählt nicht als semantischer Nachweis. Doppelte/versetzte Listen-Textlagen wurden mit den sichtbaren Seiten verglichen; die vorhandene Kennzeichnung dieser Grenze ist sachgerecht. Dieser Reviewer hat keine vollständige Wiederverfolgung aller 808 Extrakthashes, keinen zweimaligen Neubau und keine erneute Ausführung der sieben Autorentests durchgeführt. Diese Reproduktionsaufgaben bleiben in diesem Bericht `NICHT_GEPRUEFT` und gehören zum getrennten Reproduktionsauftrag.

## Eingabeintegrität und Statusgrenzen

Alle zehn gefrorenen Dateien und alle 74 öffentlichen SourceInputs wurden vor und nach der Prüfung gehasht. Alle 84 Pins stimmen; alle bleiben unverändert. Das Manifest bleibt ebenfalls unverändert. Der 296-Zeilen-Basisbestand, seine Provenienz, `pipeline/inventar.py`, dessen bestehende Tests und die bestehenden AB-/C-Ergänzungen wurden nur auf Integrität geprüft und nicht verändert. Für die zum Paket-Codecommit vorhandenen Basisdateien stimmen zusätzlich die Bytes mit `git show 60414205eba970c5832e8ad130bb43215f0a7da6:PFAD` überein. Eine eigene Neubewertung dieser anderen Module fand nicht statt.

| Prüfung                                                              | Status dieses Berichts                                              |
| -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Originalwortlaut, Antwortzellen, Listen-/Varianten-/Kontextzuordnung | `BESTANDEN` im beschriebenen Quellenumfang, E-S01 gesondert         |
| Exakte sichtbare Liste-58-Transkription                              | `NICHT_BESTANDEN`, geringes Finding E-S01                           |
| Original-Lizenzsätze und getrennte Behandlung                        | `BESTANDEN` als Quellenbefund                                       |
| Inputhashes, Unverändertheit, vier eigene Gegenfälle                 | `BESTANDEN` im beschriebenen technischen Umfang                     |
| 808 Belegketten, zwei Neubauten, sieben Autorentests                 | `NICHT_GEPRUEFT` durch diesen Reviewer                              |
| E4.2-Abgleich, E1-Anonymisierungsumsetzung, Refusal-Mapping          | `NICHT_GEPRUEFT`                                                    |
| Auflösung der E9-Formulierungsgrenze und Fußnote 86                  | `NICHT_GEPRUEFT`                                                    |
| Tatsächliches CAPI-Programm und Interviewausführung                  | `NICHT_GEPRUEFT`                                                    |
| Eignung, Polung, Konstrukte, Neutralität, empirische Validität       | `NICHT_GEPRUEFT`, außerhalb dieses Auftrags                         |
| UI-/Browserabnahme, Deployment, Merge, Release                       | `IN_DIESER_PHASE_NICHT_ERFORDERLICH` für diesen Quellen-Erstbericht |

Keine nicht ausgeführte Folgeprüfung wird als gescheiterte Analyse ausgegeben. Die offene E9-Wortlautfrage ist sichtbar; ihre Lösung wurde hier weder erfunden noch durch ein neues Missing-Mapping vorweggenommen. Die methodische Freigabe bleibt offen.

## Befehle, Werkzeuggrenzen und Fehlläufe

Alle Shell-Aufrufe nutzten ausdrücklich `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003` als `workdir`; alle `apply_patch`-Ziele waren absolute eigene Worktreepfade. Tatsächlich genutzt wurden `functions.exec` mit `exec_command`, `view_image`, `web__run` und `apply_patch`. Angeboten waren darüber hinaus Shell-/Dateiwerkzeuge, Browser/Computer Use, Bildgenerierung, MCP-Ressourcen-/Pluginwerkzeuge, Zeitwerkzeuge und Collaboration einschließlich Agentverwaltung. Weitere Agents wurden entsprechend dem engeren Auftrag nicht gestartet. Es wurden keine Installationen, globalen Änderungen, Commits, Pushes, Gesamtformatierung oder `pnpm check` ausgeführt.

Die substantiven CLI-Aufrufe waren `pdftotext -layout`, je Seite `pdftoppm -f N -l N -singlefile -scale-to 1800 -png`, für den vergrößerten Ausschnitt `pdftoppm -f 59 -l 59 -singlefile -r 300 -x 400 -y 1300 -W 1700 -H 500 -png`, die eigene Python-Semantikprüfung und der individuelle Prettier-Check. Die vollständigen Render-/Extraktionsargumente und Einzel-Exits stehen in `render-extract-command-log.json`; Fetchlog, Prüfergebnis, Eingabehashes und Werkzeug-/Befehlsverzeichnis sind über den eigenen Index gebunden. Inline-Python las öffentliche JSON-/CSV-Metadaten, berechnete Hashes, rief die offiziellen URLs per `urllib.request.urlopen` ab und schrieb ausschließlich eigene Outputs. Lesungen nutzten außerdem `cat`, `sed`, `rg` und `git branch --show-current`.

Alle 44 anfänglichen Render-/Extraktionsbefehle endeten mit Exit 0. Der äußere Renderaufruf lief zunächst asynchron; sein Abschluss wurde anhand des vollständigen eigenen Unterbefehlslogs mit 44 Exit-0-Einträgen festgestellt. Der ursprüngliche API-Sitzungsbezeichner wurde beim ersten Ausgeben nur des Textoutputs nicht mit erfasst. Es wird kein erfundener äußerer Abschluss-Exit nachgetragen.

Zwei `git show`-Diagnosen für die E-Ergänzung und C-v2 endeten mit Exit 128, weil diese Pfade im älteren Paket-Codecommit noch fehlen. Die vorhandenen Dateien wurden nicht ersetzt; für sie gilt der Datei-Hash. Zwei explorative CSV-Zählungen verwendeten zuerst ein nicht vorhandenes Feld beziehungsweise ungeeignete Trennzeichen. Ihre vermeintlichen Variablenzahlen werden nicht als Befund verwendet. Der gesicherte Zeilenumfang beträgt 296.

Ein anfänglicher visueller Verdacht zu E26 wurde nach erneuter Prüfung verworfen. Zunächst schien mir in der Mehrbildansicht die Antworttabelle zu fehlen. Renderings mit und ohne `-hide-annotations` sowie ein erneuter Abruf-/Renderlauf erwiesen sich als bytegleich mit SHA-256 `e12c3357cc2bc8ddad9d5d30b50f26d13717579c0c997b4fe6d3bf49fde015c8`. Die vollständige Einzelansicht zeigt die Tabelle. Die erste visuelle Lesung war unvollständig; daraus entsteht kein Finding. Ein zusätzlicher Cairo-Renderlauf endete mit Exit 0.

Eine explorative, nicht als Prüfverfahren eingesetzte stdlib-PDF-Objektdiagnose scheiterte zunächst mit `KeyError: 470`. Durch den anschließenden `sed`-Befehl meldete der kombinierte Shell-Aufruf trotzdem Exit 0; der Python-Fehler wird deshalb gesondert als Fehllauf dokumentiert. Weitere naive Objekt-/Objektstreamdiagnosen lieferten keinen belastbaren zusätzlichen Befund. Ihr Output wird nicht als Beweis einer abweichenden PDF-Schicht verwendet. Die Sichtprüfung und der bytegleiche Rendervergleich entscheiden über den verworfenen E26-Verdacht.

`fitz`, `pypdf`, `PyPDF2`, `pdfminer` und `pdfplumber` waren in der benutzten Python-Umgebung nicht verfügbar. Es wurde nichts installiert. Poppler war vorhanden. Die unterstützende Pixelzählung nutzte vorhandenes Pillow und endete mit Exit 0; `getdata` meldete eine DeprecationWarning. Diese Warnung ist kein Quellen- oder Prüffehler.

Modellmetadaten des Startauftrags: Codex `gpt-6.1-sol`, Reasoning `ultra`, geerbt. Die genaue interne Revision, interne Vorgaben und eine unabhängige Laufzeitbestätigung der API-Modellkennung sind hier unbekannt. Ich behaupte keine Prüfung durch eine andere Modellfamilie. Die Trennung ist frisch und organisatorisch; das gemeinsame Dateisystem ist keine technische Sandbox. Dieser KI-Audit ist kein akademisches Peer Review und keine Garantie von Biasfreiheit oder Neutralität.

ESS-Rohdaten, lokale Antwortdateien, A/B-Hälften, Personenkennungen, Partei-/Links-Rechts-Antwortwerte, Verteilungen, Portal-Analysis und Zugangsdaten wurden nicht gelesen oder ausgegeben. Die eigenen Mutationsdateien enthalten nur öffentliche Dokumentationsmetadaten. Kein gemeinsames Forschungsartefakt wurde verändert.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger Quellen-/Inhaltsreviewer INVENTORY-004-E, kein Autor. Ausschließlich Worktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, Branch research/life-93-night-20261003. Shell workdir explizit, alle apply_patch ABSOLUT im Worktree. Paket reports/loop/packages/INVENTORY-004-E/v1/manifest.json SHA2560d124297e3410fd108dfeb1a676cb55a9562f4aa1b5e5adc52f8ddf95de66958,10files74sources. Lies vollständig gefrorene AGENTS, LIFE-93, Auftrag, Prüfregeln, Analyseplan/anforderungen/Lizenzen/E-Prüfauftrag und Autorenbericht/JSON. Keine anderen Reviewer-/Jurorberichte/Loopfindings/Agentlisten oder Verteidigung lesen, keine weiterenAgents. Prüfe alle32 technischeEIdentitäten anOriginal: deutschesQ43–54, Listen50–67 aufPDF51–68,Codebook4.1E208–218. Wesentliche/gesamteDE-Frage- undListenseiten selbst visuell lesen, PDFSkill. Kategorien/Labels/Sondercodes, geerbteEinleitungen/Interviewer/Filter, E1Codes1/2/3/8 vsListe50nichtnumerischRefusal, AnonymisierungDEnichtungeprüfte4.2Regel, E8–11M/WOriginalvariantenE1=1/2, E6/7randomisierteReihenfolgeAnweisungnichtCAPIvollzogen; E9–11Code4NichtErfahrungnichtNein/Mitte, auffälligerOriginalE9WortlautgegenEN/Footnote86offen; E12/13DEEinleitung,E14Polizeisicht,DreikategoriennichtordinäreAchse, E20kompletteVignette, E26Liste66Definition, E23–28keineumfassendeGenderHaltung. Doppelte/versetztePDFTextlagen undvisuelleLesefassungkennzeichnen; TokenanwesenheitalleinkeineOriginalzellzuordnung. LizenzsätzeOriginalHTMLFundstelleCCDokumentationvsDatengetrennt. Aktive Suche nachFehler/Gegenbelegen, keineQuote oder erwünschtepolitischeSchlussfolgerung. Eigene Original- undsynthetischeGegenfälle nur outputs/loop/inventory004-e-sources/, eigenerErstbericht reports/loop/reviews/INVENTORY-004-E-sources.md. Autorbuilder/Test/reproduce niemalsdirekt aufLiveoutputs starten; falls nötig nurOwnumgebundeneKopien. Alle10+74publicInputsHashvor/nach, Grundlage296/205OriginalCSV/Parser undandereModuleunverändert; allesPaketimmutable. KeineESSraw/local/Personen/A/BParteiLRAntwortwerte/Verteilungen/PortalAnalysis/CredsSecrets/CondaInstall/globalWrites/CommitPush/Gesamtformat/pnpmGesamtlauf. E4.2Abgleich/ItemEignungPolung/Neutralität/Konstrukte/empirischeWissenschaftsfreigabe nichtAuftrag; fehlendeFolgeprüfungenNICHTGEPRUEFTnichtgescheiterteAnalysen. FindingE-Sxx präziseAussage/Fundstelle/Problem/Wirkung/begründeteSchwere/konkreteKorrekturNachprüfung; offeneVermutungenklar. Vollständiger tatsächlicherAuftragwortgetreu; angebotene undtatsächlicheTools,CommandsExitsFehlläufe, Modellgpt-6.1-solultra geerbtinternunknown, SharedFSnichttechnischeSandbox. Frischorganisatorisch getrennte gleicheCodexfamilie;KI-AuditnichtakademischesPeerreview/Biasgarantie. Keine gemeinsamenArtefakteändern; Erstbericht vollständigimmutable abschließenSHA+OwnIndexmelden.
```
