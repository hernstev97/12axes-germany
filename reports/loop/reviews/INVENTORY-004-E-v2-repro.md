# INVENTORY-004-E v2: unabhängige Reproduktionsnachprüfung

Nachbericht vom 2026-10-03, Reparaturrunde 1. Rolle: frischer methodischer und Reproduktionsnachprüfer, kein Autor, zuvor an diesem Paket unbeteiligt. Die beiden abgeschlossenen v1-Erstberichte gehören zum ausdrücklich freigegebenen Nachprüfkontext. Aktuelle andere Nachberichte, Loop-Findings, Agentlisten und zusätzliche Verteidigungen wurden nicht gelesen.

Die zwei eigenen vollständigen Nachbauten sind untereinander und mit der gefrorenen v2-JSON bytegleich. Der vollständige Diff enthält genau zwei sichtbare Punktkorrekturen und drei administrative Änderungen. Alle 808 Belege, die übrigen Fragefelder und sieben offenen Punkte bleiben unverändert. Alle sieben früheren und zwölf neuen benannten Gegenfälle sind tatsächlich verändert und werden erneut abgewiesen.

E-R01 und E-S01/E-R03 sind im beschriebenen Reparaturumfang erfolgreich nachgeprüft. E-R02 bleibt in Runde 1 offen: Der zusätzliche Kontextvertrag prüft die Anwesenheit eines Belegnamens, bindet den notwendigen Kontext aber nicht ausreichend an dessen primäre Originalstelle. Eigene kohärente Gegenfälle verändern den E8W-Filter oder entfernen den maßgeblichen E13-Einleitungstext und passieren trotzdem die vollständige erweiterte Autorenprüfung. Eine zusätzliche, kleine Provenienzlücke erhält E2-R01. Die gegenwärtige JSON enthält diese falschen eigenen Gegenfälle nicht.

## Gefrorener Gegenstand und Urteile

Manifest `reports/loop/packages/INVENTORY-004-E/v2/manifest.json`, SHA-256 `e1e184883b5f2ca04f729b2c2383777070601af6eba049c72e040aa1e1f56ca2`. Das Manifest bindet 17 Dateien und 130 öffentliche SourceInputs, Code-Commit `5d3a945768874875c1b5bbca770b56148c3ac636`, die ursprüngliche v1-Fassung und Reparaturrunde 1. Der dort genannte Analyseplan bleibt ein gefrorener Entwurf ohne wissenschaftliche Abnahme.

Geprüfte neue JSON: `data/inventar-e.v2.ergaenzung.entwurf.json`, 2.066.030 Bytes, SHA-256 `0c031abd7be58e14c91360db4e2a438b0b211e1116dd2f1b84ebab612931f6de`. Zusatzvertrag: `pipeline/annotations/e_semantic_contract_v2.py`, SHA-256 `740598c0f64f9a426db978bf4199f877b79ad24d9c68e7bae1eac2affa8c7c07`. Alle positiven Ergebnisse gelten nur für diese Pins und den benannten Umfang.

| Prüfgegenstand                                                                             | Tatsächliches Urteil                                 | Grenze                                                                                                                   |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 17 gefrorene Dateien, 130 SourceInputs, SafePath und Scope                                 | BESTANDEN                                            | Vor-/Nachhashes, Bytezahlen, erlaubte relative und aufgelöste Pfade                                                      |
| Zwei eigene vollständige Nachbauten                                                        | BESTANDEN                                            | Identische Bytes zur v2-JSON; keine ESS-Antwortanalyse                                                                   |
| Vollständiger Diff                                                                         | BESTANDEN                                            | Genau fünf Pfade; 808 Belege und sieben offene Punkte unverändert                                                        |
| Alle Quellenrechtecke, Tokens, Extrakte, Hashes und Referenzen                             | BESTANDEN                                            | 808 Ketten und 1.772 auflösbare Verweise; richtige Quellenkette allein beweist keine richtige semantische Zuordnung      |
| Tatsächliche deutsche Code-/Labelzellen, notwendige Kontexte und Listen der aktuellen JSON | BESTANDEN                                            | 32 Identitäten; eigene Originallektüre und begrenzte Zusatzkontrollen                                                    |
| E-R01, Bindung der deutschen Code-/Labelzellen und sichtbaren Listenwerte                  | BESTANDEN für Reparaturumfang                        | Vollständige Labelobjektvertauschung und weitere E14-Verwechslung scheitern; E2-R01 betrifft getrennt den Quellenverweis |
| E-S01, Duplikat E-R03, sichtbare Liste-58-Punktkorrektur                                   | BESTANDEN                                            | Eigenes frisches Raster; Roh-Tokenpunkt unverändert; Ursache des PDF-Unterschieds unbekannt                              |
| E-R02, ausreichender Schutz notwendiger Filter/Einleitungen                                | NICHT_BESTANDEN                                      | Benannte Fälle repariert, zusätzliche kohärente falsche Bindungen akzeptiert                                             |
| 7 frühere und 12 neue Autorenmutationen                                                    | BESTANDEN                                            | Alle 19 Deltas, Kandidatenhashes und tatsächlichen Fehler nachgeprüft                                                    |
| Individuelle Formatprüfung                                                                 | BESTANDEN nach tatsächlich verarbeitetem Schlusslauf | Nur eigener Bericht und eigene Zusammenfassung; Ignoreliste ausdrücklich aufgehoben                                      |
| Gesamtprüfung `pnpm check`                                                                 | NICHT_GEPRUEFT                                       | Durch den engeren Nachprüfauftrag untersagt                                                                              |
| UI und Browser                                                                             | IN_DIESER_PHASE_NICHT_ERFORDERLICH                   | Kein UI-Artefakt geändert oder freigegeben                                                                               |
| Empirie, Edition 4.2, CAPI-Ausführung, Eignung, Polung, Konstrukte und Neutralität         | NICHT_GEPRUEFT                                       | Keine Antwortdaten, Laufprotokolle oder erforderlichen Folgeabnahmen untersucht                                          |

## Reproduktion und Schutz der Originale

Eigene Dateien liegen ausschließlich in `outputs/loop/inventory004-e-v2-repro/` und diesem Nachbericht. `recheck.py` prüfte alle Manifestpins vor Beginn. Absolute Pfade müssen innerhalb des erlaubten Worktrees liegen; Paketdateien innerhalb des gefrorenen Paketbereichs. Absolute Einträge, `..`, Symlinks sowie `raw`-/`local`-Pfadbestandteile sind ausgeschlossen. Die SourceInputs bestehen im tatsächlichen Paket aus öffentlichen Dokumenten, Text-/BBox-Extrakten, Renderings, öffentlichem Lizenz-HTML, Annotationen, Skripten, technischen Protokollen und synthetischen Dokumentationsgegenfällen. Das ist keine Prüfung beliebiger anderer Repositorydateien.

Die originalen Builder, Lesetests und Reproduktionsskripte wurden vollständig als Text gelesen, niemals am Livepfad ausgeführt. Der ursprüngliche und korrigierte Builder wurden zusätzlich vollständig verglichen. Die einzige Änderung meiner beiden ausführbaren Builderkopien ist die ROOT-Umleitung auf `outputs/loop/inventory004-e-v2-repro/replica/`. Der korrigierte Autorbuilder und dessen `run-1/build.py` sind bytegleich. Auch bei der eigenen erweiterten Lesetestkopie ist ausschließlich ROOT umgebunden. Der importierte Zusatzvertrag ist eine bytegleiche Kopie der gefrorenen Paketdatei; Bytecode-Schreiben ist abgeschaltet.

Vor dem ersten Builderstart wurden ROOT, OUT, PUBLIC, importierter Zusatzcode, ursprüngliche PDF-Pfade, eigene PDF-Kopien, alle drei BBox-Ziele, Default- und explizites Buildziel, Testresultat, die sieben Kandidatenziele und PNPM-CWD vollständig auf eigene absolute Pfade aufgelöst. `preflight.json` hält die tatsächlichen Pfade und die vollständigen Umleitungsdiffs fest. Log- und Ergebnisziele liegen ebenfalls im eigenen Ordner. Zusätzliche eigene Kandidatenpfade werden vor ihrem Schreiben ausdrücklich auf diesen Bereich geprüft. Der vorhandene Formatter wird aus dem expliziten eigenen ROOT aufgerufen; es wurde nichts installiert.

Jeder Nachbau verwendet einen getrennten neuen `run-1/` beziehungsweise `run-2/`-Ordner. Beide erzeugen die drei BBox-Dateien aus den drei bytegeprüften Originalkopien neu. Beide Builderprozesse endeten mit Exit 0. Der eigene erweiterte Lesetest endete mit Exit 0. `command-log.json` enthält exakte Argumentlisten, Arbeitsverzeichnisse, stdout, stderr und Exits dieser drei ausgeführten Prozesse. `reproduction-result.json` bindet die beiden vollständigen Nachbauergebnisse und ihre Bytegleichheit.

Die technische Grundlage enthält unverändert 296 CSV-Zeilen und 205 Pending-Zeilen. 205 ist das Ergebnis der bestehenden Pending-Regel in `pipeline/inventar.py:610–628`, keine zweite CSV. Die Zählung nutzte nur technische Status-/Locatorfelder und die Prüfung eines leeren Dokumentationswortlauts, keine Antwort- oder Designzeilen. Der Bestand wurde nicht neu bewertet. CSV, Provenienz, Parser, dessen bestehende Tests, AB-/C-/C-v2-Ergänzungen, beide E-JSON und der tatsächliche Zusatzcode sind vor/nach separat geschützt. Alle existieren; ihre individuellen Hashes stehen im Schutzprotokoll. Der CSV-Hash bleibt `8c73adb8b361db2992f5fe9e321e0c5b978afdc41ba22c1cbb471f92e60057c1`, der Provenienz-Hash `533a12c517ac49f869aea1fbc09dc86e3c1dfe7ef9bc7b05018b5a49ba753aa6`.

Der eigene Diff wurde rekursiv aus beiden gefrorenen JSON berechnet, unabhängig vom Autoren-Diffprotokoll. Seine vollständigen fünf Pfade sind:

```text
/fragen/15/listenheft/sichtbare_kategorien_de/wert/2
/fragen/16/listenheft/sichtbare_kategorien_de/wert/2
/korrekturprovenienz
/zugriffsgrenzen/loopFindingsRead
/zugriffsgrenzen/peerOrJurorReportsRead
```

Die zwei Inhaltswerte verlieren jeweils nur den Schlusszeichenpunkt. Kein Rohbeleg wird geändert. `diff.json` bestätigt vollständige Gleichheit aller 808 Belegobjekte, aller sieben offenen Punkte und aller übrigen Fragefelder.

## Eigene Originallektüre und tatsächliche Bindungen

Die drei öffentlichen Originalbytes wurden aus dem gepinnten Autorenbestand kopiert. Es gibt keinen eigenen Netzabruf und keine behauptete Aktualitätskontrolle über diese Fassung hinaus.

| Original                                     | SHA-256                                                            |
| -------------------------------------------- | ------------------------------------------------------------------ |
| `ESS11_questionnaires_DE.pdf`, deutsch, 2023 | `be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75` |
| `ESS11_showcards_DE.pdf`, deutsch, 2023      | `786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca` |
| `ESS11_appendix_a7_e04_1.pdf`, Ausgabe 4.1   | `b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35` |

Vollständig textuell gelesen wurden deutsches Q43–54, Listen 50–67 auf PDF51–68 und Codebook-PDF208–218. Alle 41 Seiten wurden frisch gerendert. Tatsächlich selbst visuell gelesen wurden sämtliche 12 deutschen Fragebogenseiten, alle 18 Listen und Codebook 208/211/215/217, also 34 vollständige Seiten. Liste 58/PDF59 wurde zusätzlich als eigener 300-dpi-Ausschnitt gelesen. Sieben weitere Codebookseiten sind gerendert und textuell, aber nicht als visuell gelesen ausgewiesen. Die 45 tatsächlichen Extraktions-/Renderbefehle, Pfade und Einzel-Exits stehen in `reading-command-log.json`; alle endeten mit Exit 0.

Die Zusatzfunktion ermittelt E-Fragepositionen an den Originaltokens, grenzt die konkrete Frage und ihre Codezeilen ab und vergleicht die Code-/Labeltokengeometrie. Ihre Regeln `original_positions` und `validate_semantics`, gefrorene Codezeilen 61–106, stimmen für die aktuelle JSON mit meinen selbst gelesenen deutschen Tabellen überein. Die vollständige ursprüngliche Labelvertauschung und eine eigene vollständige E14-Labelvertauschung scheitern an der zugehörigen Originalcodezeile. Sie prüfen mehr als die Anwesenheit eines beliebigen Labels auf derselben Seite.

`independent.py` verwendet die zweite frisch erzeugte BBox-Serie und importiert keinen Autorenvalidator. Es verfolgt sämtliche 808 Ketten, Quellenhashes und gedruckten Seiten erneut. Ein zusätzlicher, aus der eigenen Originallektüre festgehaltener Kontextvertrag bindet primären Verweis, Quelle, Originalseite, tatsächliche Tokens, Text und Kontexttyp. Die unveränderte Basis besteht; die maßgeblichen akzeptierten falschen Filter-/Einleitungsgegenfälle scheitern dort. Dieser eigene Vorschlag wurde nicht in die gemeinsame Forschungsfassung übernommen und ist ebenfalls kein universeller semantischer Beweis. `reference-check.json` erfasst 1.772 Belegverweise einschließlich Abschnitts-, Tabellen- und Ganzseitenverweisen. Die anfängliche engere Zählung von 1.728 wurde um 44 Abschnittsverweise ergänzt; 1.728 wird nicht als vollständige Zahl ausgegeben.

Alle 18 sichtbaren Listenwerte des Zusatzvertrags stimmen mit meinen frischen vollständigen Seitenansichten überein. Die doppelte oder versetzte PDF-Textlage einzelner Skalen wird nicht als zweimal sichtbare Kategorie ausgegeben. Bei Liste 58 endet die dritte sichtbare Kategorie ohne Punkt. Der PDF-Token und `SC-L58-page` enthalten weiterhin `behandelt.`. Diese beiden Prüfgegenstände bleiben getrennt; die Ursache des Unterschieds ist unbekannt. Genau die sichtbaren E12-/E13-Felder wurden repariert. E-S01 und Duplikat E-R03 sind in Runde 1 damit nachgeprüft.

Die aktuelle JSON behält die erforderlichen deutschen Kontexte und Originalgrenzen:

- E1 auf Q43 druckt 1/2/3/8. Liste50 enthält eine Verweigerungsoption ohne gedruckte Zahl; es wird kein Code erfunden. Codebook 208 nennt deutsche Anonymisierung, ohne hier die Umsetzung in 4.2 zu belegen.
- Q45 druckt eine Randomisierungsanweisung für E6/E7. Sie belegt eine Anweisung, keine ausgeführte CAPI-Zuweisung, keine komplementäre Skala und keine politische Bedeutung.
- Q46/47 und Codebook 211 unterscheiden E8M mit E1=1 und E8W mit E1=2. Q47/48 und dieselben Codebookfilter tragen die Varianten E9–E11. Die gegenwärtigen Zuweisungen und extraktgebundenen Codebookfilter stimmen; die zusätzliche Filtermutation wird tatsächlich abgewiesen.
- E9–E11 behalten die fehlende einschlägige Erfahrung als eigene Antwort 4. Die auffällige deutsche medizinische Formulierung bleibt original. Der englische Codebookwortlaut und die sichtbare Fußnotenreferenz 86 sind keine fertige Bedeutungsauflösung.
- Q49 bindet den aktuellen Deutschlandbezug und die beiden Situationen an E12/E13. E14 hat den eigenen Polizeigegenstand. Die Codefolge begründet hier keine ordinale Einstellungsachse.
- Q52 enthält die vollständige E20-Vignette. Liste66/PDF67 enthält die vollständige Definition bei E26. Entfernte Vignette, Definition und Randomisierungsanweisung werden in den tatsächlich ausgeführten benannten Fällen abgewiesen.
- Selbstbeschreibungen, persönliche Behandlungserfahrungen, wahrgenommene gesellschaftliche Lage, Gleichstellungsfolgen, Maßnahmen/Sanktionen und geschlechtsbezogene Zuschreibungen bleiben unterschiedliche Antwortgegenstände. Gemeinsame Skalen und Einleitungen werden nicht zur umfassenden Gender-Dimension erklärt.

Die öffentliche ESS-Lizenz-HTML wurde selbst gelesen, mit dem gefrorenen Hash `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d`. Der tatsächliche HTML-Abschnitt „Conditions of use“ unterscheidet Daten CC BY-NC-SA 4.0 und Dokumentation CC BY-SA 4.0. Der zugehörige Dokumentations-DOI und die Attribution werden getrennt vom 4.1-Datenzitationsbeispiel geführt. `license-section.txt` ist ein abgeleiteter Extrakt; die HTML-Lektüre zählt als Originalfundstelle. Das ist eine begrenzte Quellenkontrolle der dokumentierten Lizenzbehauptung, keine aktuelle rechtsfachliche oder spätere Exportfreigabe.

Der Quellenvertrag setzt hashgeprüfte Original-PDFs und daraus erzeugte `pages` voraus. Die reine Funktion liest selbst keine Dateien. In meinen Läufen ist diese Voraussetzung mit eigenen PDF-Kopien und frischen Extrakten tatsächlich erfüllt. Ein alleiniger erfolgreicher Funktionsaufruf mit beliebigen `pages` würde sie nicht belegen. Die Adoption des früheren Reviewercodes wird in Moduldocstring, Korrekturbericht und neuer JSON zutreffend als Autorenarbeit bezeichnet; daraus wird keine zusätzliche Unabhängigkeit abgeleitet.

## Tatsächlich nachgeprüfte sieben frühere und zwölf neue Gegenfälle

Die sieben früheren Mutationen wurden durch die eigene umgeleitete Lesetestkopie vollständig erzeugt. Ihre Bytes stimmen mit den gepinnten v2-Autorenkandidaten überein. Die tatsächlichen Deltapfade stimmen mit den entsprechenden ursprünglichen v1-Mutationen überein, jeweils gegen ihre eigene Version verglichen. Damit wird die v1-Punktabweichung nicht als vermeintlicher Grund einer v2-Mutationsabweisung vorgeschoben.

Die zwölf neuen vollständigen eingefrorenen Kandidaten wurden bytegleich in meinen eigenen Ordner kopiert, rekursiv gegen v2 verglichen und durch den eigenen Import der umgeleiteten erweiterten Autorenprüfung erneut geprüft. Alle zwölf tatsächlichen Fehlermeldungen stimmen mit dem Autorenprotokoll überein. `case-results.json` enthält die vollständigen Kandidatpfade, Hashes, Deltas und Fehler; die folgende Tabelle kürzt nur die Anzeige.

| Fall                                 | Tatsächlicher Abweisungsgrund                    |
| ------------------------------------ | ------------------------------------------------ |
| E19-antwortcode-1-zu-5               | Antwortcode widerspricht Originalzelle           |
| E8W-filter-E1-2-zu-1                 | Kontext/Filter widerspricht Original             |
| E11M-liste57-zu56                    | Frage fehlt im Original-Listenheader             |
| E8M-variantenzuweisung-1-zu2         | Variante widerspricht offiziellem Codebookfilter |
| E26-definition-entfernt              | Definition fehlt                                 |
| E12-label1-durch-label2              | Label widerspricht Originalzelle                 |
| E1-extrakthash-null                  | Extrakt/Hash stimmt nicht                        |
| coherent-label-and-evidence-swap     | Label gehört nicht zur Original-Codezeile 1      |
| direct-filter-removed                | Notwendiger E8W-Kontext fehlt                    |
| visible-poles-swapped                | Sichtbare E19-Listenlabels falsch                |
| coherent-variant-and-codebook-filter | E8M-Originalvariantenfilter falsch               |
| inherited-filter-removed             | Notwendiger E10M-Filter fehlt                    |
| shared-introduction-removed          | Gemeinsame E13-Einleitung fehlt                  |
| filter-reset-removed                 | E12-Filteraufhebung fehlt                        |
| vignette-removed                     | E20-Vignette fehlt                               |
| definition-removed                   | E26-Definition fehlt                             |
| random-order-instruction-removed     | E6-Reihenfolgeanweisung fehlt                    |
| old-visible-period-restored          | E13-sichtbare Listenlabels falsch                |
| coherent-whole-list-replaced         | E11W fehlt im Original-Listenheader              |

## Zusätzliche eigene Gegenfälle

13 vollständige eigene Kandidaten wurden tatsächlich verändert, gespeichert und durch die unveränderte erweiterte Autorenprüfung getestet. Es gibt keine vorgeschriebene Fehlerquote. Alle Deltapfade, SHA-256 und Ergebnisse liegen in `own-cases.json`. Der begrenzte eigene Kontext-/Provenienzprüfer prüft zusätzliche Gegenstände; ein von ihm nicht beanstandeter Fall bedeutet keine umfassende Freigabe.

| Eigener Fall                                                                     | Erweiterter Autorenprüfer | Bedeutung                                                                                           |
| -------------------------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------- |
| E8W falscher primärer Männerfilter, richtiger Frauenfilter nur zweiter Verweis   | AKZEPTIERT                | E-R02, primäre Kontextbindung fehlt                                                                 |
| E8W-Belegobjekt samt Kontext kohärent auf originale E8M-Filterstelle umgebunden  | AKZEPTIERT                | E-R02, notwendiger Belegname schützt keine Originalposition                                         |
| E13-Einleitung durch Modul-Einleitung ersetzt, notwendige ID nur zweiter Verweis | AKZEPTIERT                | E-R02, tatsächlicher gemeinsamer Einleitungstext fehlt                                              |
| E12/E13-Einleitungsbeleg gemeinsam auf Modul-Einleitung umgebunden               | ABGEWIESEN                | E12-eigene Listenanweisung fehlt; kein erfolgreicher Bypass                                         |
| E8W-Filtertyp zu Einleitung geändert                                             | AKZEPTIERT                | E-R02, notwendiger Filter wird nicht als Filter gebunden                                            |
| E10M-übernommener Filter als direkt bei E10M bezeichnet                          | AKZEPTIERT                | Provenienzmetadaten derzeit außerhalb wirksamer Kontrolle                                           |
| E8W um zusätzlichen widersprechenden Männerfilter ergänzt                        | AKZEPTIERT                | E-R02, richtige Anwesenheit schützt nicht vor widersprechender Ergänzung                            |
| Sichtbarer E19-Listenwert mit Ganzseitenbeleg von Liste65 verknüpft              | AKZEPTIERT                | E2-R01, falscher Quellenverweis                                                                     |
| Auch vollständiger E19-Seitenbeleg auf Liste65 gewechselt                        | ABGEWIESEN                | Original-Listennummer fehlt                                                                         |
| Ganze E6-Liste durch E7-Liste ersetzt                                            | ABGEWIESEN                | Frage fehlt im Original-Listenheader                                                                |
| Vollständige E14-Labelobjekte zu Code1/2 vertauscht                              | ABGEWIESEN                | Falsche Originalcodezeile; E-R01 bestätigt                                                          |
| Vollständige gedruckte Codebook-E12-Zeilen1/2 in der Arrayreihenfolge vertauscht | AKZEPTIERT                | Zeilenobjekte bleiben intern richtig; ursprüngliche Reihenfolge ist außerhalb dieses Zusatzvertrags |
| E8M-Codebookfilter durch echten E9-Codebookfilter ersetzt                        | ABGEWIESEN                | Fragegebundene Filterbedingung falsch                                                               |

Die akzeptierte Codebook-Zeilenreihenfolge wird als tatsächliche Reichweitengrenze dokumentiert, nicht als Beweis schon falsch gebundener Code-/Labelpaare oder fehlender wissenschaftlicher Güte. Der Zusatzvertrag beansprucht keinen universellen Semantikschutz. Anders liegt E-R02: Hier ändern die eigenen akzeptierten Fälle genau die notwendigen Filter- und Einleitungsbedeutungen, deren Schutz Gegenstand der angenommenen Reparatur ist.

## E-R02 bleibt in Reparaturrunde 1 offen

Betroffene Aussage ist der Korrekturbericht, Absatz zum neuen Zusatzvertrag: Er „fordert notwendige direkte und übernommene Kontexte“. Betroffene Umsetzung sind die gefrorenen Codezeilen 107–111. Der Prüfer bildet `refs` aus allen Verweisen aller noch vorhandenen nicht als Listenanweisung bezeichneten Kontexte. Danach genügt `expected_context(qid) <= refs`. Den Wortlaut vergleicht er dagegen ausschließlich mit dem ersten Verweis. Die Pflicht-ID kann deshalb als zweiter Verweis bloß genannt werden, obwohl der primär ausgegebene Text aus einer anderen Originalstelle stammt. Zudem sind die Pflicht-IDs nicht an die unveränderte Originalgeometrie gebunden.

Der konkret erhaltene Kandidat `own-cases/E8W-wrong-primary-filter-with-required-secondary-ref.json` ersetzt ausschließlich den direkten E8W-Kontexttext durch den originalen Männerfilter und setzt seine Verweise auf `QCTX-E8M-filter`, `QCTX-E8W-filter`. Alle 808 registrierten Originalbelege bleiben unverändert und richtig. Der erweiterte Autorenprüfer gibt trotzdem `BESTANDEN_AUTOR_TECHNIK_KEINE_FREIGABE` zurück. Originalgegenbeleg: Q47, Filter unmittelbar vor E8W, E1=2; Q46 vor E8M, E1=1; Codebook 211, zu `impbemw` beide unterschiedlichen Varianten. Diese Stellen wurden selbst textuell und visuell gelesen.

Ein zweiter eigener Kandidat `own-cases/E8W-filter-evidence-retargeted-to-E8M.json` ersetzt das unter `QCTX-E8W-filter` gespeicherte vollständige Belegobjekt durch die echte Originalstelle von E8M, behält nur die ID und passt den Text an. Die gesamte Token-/Extrakt-/Hashprüfung besteht weiterhin, weil die neue Stelle tatsächlich existiert. Die falsche Zuordnung zu E8W wird aber nicht geprüft. Damit genügt auch ein bloßer Verzicht auf Zweitverweise nicht als vollständige Korrektur.

Der unabhängige Fall `own-cases/E13-shared-intro-secondary-ref-only.json` ersetzt bei E13 den Text zur aktuellen Deutschlandlage und beiden Situationen durch die Modul-Einleitung. Der notwendige Beleg bleibt lediglich als zweiter Verweis stehen; der volle erweiterte Autorenprüfer akzeptiert. Originalgegenbeleg: Q49, E12/E13-Einleitung vor dem medizinischen Beispiel. Der eigene Originalpositionsprüfer weist alle drei Kandidaten nachweislich ab; genaue Fehler stehen in `independent-results.json`. Auch der Filtertypwechsel und der zusätzliche widersprechende Männerfilter werden akzeptiert.

Wirkung: Der neue Schutz kann falsche Zugangsbedingungen oder fehlenden gemeinsamen Antwortkontext als bestanden ausgeben. Das kann eine spätere Übertragung der Fragen verändern. Die richtige Variante in `formulierung_variante` beseitigt nicht den gleichzeitig falschen deutschen Filtertext. Ich behaupte keinen solchen Fehler in der gegenwärtigen JSON und keine tatsächliche falsche Web- oder CAPI-Ausführung.

Schwere bleibt mittel. Betroffen ist ein für spätere Verwendung notwendiger Kontext; der aktuelle Entwurf ist noch richtig und ohne wissenschaftliche Freigabe. Die bisherigen 19 Gegenfälle wurden erfolgreich repariert, reichen aber nicht für den angenommenen Anspruch. Die Kennung E-R02 und Rundenzählung 1 bleiben erhalten; kein neuer Name und keine neue Runde verbergen den Rest.

Konkrete Korrektur: Je Pflichtkontext eine primäre, eindeutig passende Bindung an Quellenart, Originalseite, Originaltokens/Text und Kontexttyp fordern. Belegidentitäten brauchen eine unabhängige Originalpositionsbindung. Zusätzliche Verweise dürfen Pflichttexte nicht ersetzen. Widersprechende zusätzliche Filter, falscher Ursprung und Geltung müssen entweder geprüft oder ausdrücklich als ungeschützter Teil ausgeschlossen werden. Den Codebookfilter weiterhin separat an Originalextrakt und Frage-/Variantenbedingung binden.

Nachprüfung: Die drei erhaltenen kohärenten Hauptkandidaten, Typwechsel und widersprechende Ergänzung müssen scheitern, während die aktuelle richtige Basis und alle 32 Identitäten weiter bestehen. Alle 19 benannten Fälle wiederholen; Vignette, Definition, Reihenfolgeanweisung und gemeinsame Einleitung im Originalumfang erhalten. Zwei vollständige Nachbauten müssen weiterhin bytegleich sein. Eine engere Aussage über den Validator muss die tatsächliche ungeschützte Kontextzuordnung nennen und darf E-R02 nicht als vollständig repariert darstellen.

## E2-R01: sichtbarer Listenwert kann den falschen Ganzseitenbeleg tragen

Neue Kennung, Schwere niedrig. Betroffene Aussage ist die nachvollziehbare Belegkette der sichtbaren Listenlesefassung. In der aktuellen JSON verweist E19 zutreffend auf `SC-L64-page`; der akzeptierte eigene Kandidat `own-cases/E19-visible-list-proof-swapped-to-list65.json` verändert ausschließlich `/fragen/22/listenheft/sichtbare_kategorien_de/belege/0` zu `SC-L65-page`.

Originalbelege: Liste64/PDF65 gehört zu E19–E22 und enthält die Dafür-/Dagegenkategorien. Liste65/PDF66 gehört zu E23–E25 und enthält Häufigkeitskategorien. Beide vollständigen Originalseiten wurden frisch gerendert und selbst gelesen. Der erhaltene Kandidat behält den richtigen E19-Listenwert, Listenheader, Nummer und Ganzseitenhauptbeleg, verweist aber für dessen sichtbare Kategorien auf die falsche Liste. Er wird durch den vollständigen erweiterten Autorenprüfer akzeptiert. Codezeilen 112–114 prüfen Position und erwarteten sichtbaren Wert, aber nicht dessen Belegverknüpfung. Die Quellenhash-/Tokenprüfung aller808 registrierten Belege kann diese falsche Referenz nicht auflösen, weil beide Originalbelege für sich richtig sind.

Wirkung ist ein falscher Nachweis für ansonsten richtigen sichtbaren Text. Dadurch könnte eine spätere Quellenanzeige die falsche Seite öffnen. Ein bereits falscher sichtbarer Kategorienwert oder eine falsche tatsächliche Liste in der gefrorenen Basis wird nicht behauptet. Deshalb ist die Schwere niedrig und wird nicht zur empirischen Gütebehauptung hochgestuft.

Korrektur: Den sichtbaren Listenwert zusätzlich an den zur tatsächlichen Nummer gehörenden Ganzseitenbeleg binden und dessen Quelle/PDF-Seite kontrollieren. Der Roh-Textlayer bleibt als eigener Prüfgegenstand erhalten; sichtbare Transkription braucht weiterhin Originalrenderlektüre. Nachprüfung: Der erhaltene Einzelfeldgegenfall muss scheitern; alle 18 richtigen sichtbaren Fassungen und die Liste 58-Punktkorrektur müssen bestehen. Der eigene begrenzte Prüfer `check_visible_proofs` zeigt diese Abweisung bereits, wurde jedoch nicht in die Autorenfassung übernommen.

## Anforderungen und nicht ausgeführte Folgeprüfungen

Sämtliche gefrorenen Anforderungen wurden gelesen: AGENTS, vollständiges LIFE-93-Issue und Nachtauftrag, Prüfregeln, Analyseplan, Analyseanforderungen, Lizenzen, beide Prüfaufträge, vollständiger ursprünglicher Autorenbericht, beide vollständigen v1-Erstberichte, Annahmeentscheidung, Korrekturbericht, beide JSON und neuer Zusatzcode. Die JSON wurden vollständig strukturell geladen; sämtliche Identitäten, Code-/Label-/Kontext-/Listenfelder und registrierten Belege wurden verfolgt. Die ursprünglichen Berichte und Ausgangsfassung wurden nicht verändert oder formatiert.

Die Standards verlangen richtige konkrete Fundstellen, vollständige Originalkontexte, getrennte Urteile, nachvollziehbare Gegenfälle und Freigaben für eine bestimmte Fassung. Paketintegrität und grüner Nachbau erfüllen nur technische Teile. Ein Quellenrechteck mit echtem Text ist noch kein Beweis seiner Geltung für das bezeichnete Item. Das ist der hier nachgewiesene Rest bei E-R02.

Edition 4.2, E1-Anonymisierung und Verweigerungszuordnung, E9-Wortlaut-/Fußnotenauflösung, tatsächliches CAPI, endgültige Eignung/Ausschlüsse/Polung, Konstruktbreite, Neutralität, Messmodell, empirische Prüfungen, Webmodusübertragung und konkrete Veröffentlichung bleiben NICHT_GEPRUEFT. Die erforderliche andere Modellfamilie und menschliche Abnahmen werden durch diesen Nachbericht nicht ersetzt. Spätere abhängige Arbeit kann deshalb blockiert sein; keine dieser nicht ausgeführten Untersuchungen wird als heute gescheiterte Analyse bewertet. Planfestschreibung setzt keine zusätzliche persönliche Statistik-Abnahme Stevens voraus.

## Werkzeuge, Befehle und Grenzen

Modell gemäß tatsächlichem Startauftrag: geerbtes Codex `gpt-6.1-sol`, Reasoning ultra. Es gab keine Modellüberschreibung. Interne Anbieterrevision, nicht zugängliche interne Vorgaben und eine gesonderte Laufzeitbestätigung der API-Kennung sind unbekannt. Dies ist ein organisatorisch frischer Nachreview innerhalb derselben Codex-Familie, ein KI-Audit, kein akademisches Peer Review, keine Prüfung durch eine andere Modellfamilie und keine wissenschaftliche oder Neutralitätsgarantie.

Angeboten waren `functions.exec` und Shell-/Dateiwerkzeuge, Web-/Bild-/Audioausgabe, Bildgenerierung, Computer Use, Zeitwerkzeuge, MCP-Ressourcen-/Pluginwerkzeuge, Zielverwaltung und Collaboration einschließlich Agentverwaltung. Tatsächlich benutzt wurden `functions.exec` mit `exec_command`, `write_stdin`, `apply_patch` und `view_image`. Die Abschlussübergabe nutzt die vorhandene Agentkommunikation. Es wurden keine weiteren Agents gestartet oder Listen abgefragt. Web, Computer Use, Bildgenerierung, Ressourcen, Plugins und Zielverwaltung wurden nicht benutzt.

Alle Shell-Werkzeugaufrufe hatten das explizite erlaubte Worktree-Arbeitsverzeichnis. Eigene Unterprozesse hatten explizites eigenes CWD. Alle Patchziele waren absolute Pfade im erlaubten Worktree. Das Shared Filesystem ist keine technische Reviewer-Sandbox; die Zugriffstrennung beruht auf Auftrag, umgeleiteten Pfaden und kontrollierten Hashes.

Die ausgeführten Shell-Lesungen waren `pwd`, `rg --files reports/loop/packages/INVENTORY-004-E/v2`, `wc -l` der beiden Erstberichte, Autorenberichte und gepinnten Skripte, `cat` der oben einzeln benannten gefrorenen Anforderungen/Skills/Skripte, `sed -n` für die vollständigen Erstberichte und Builderhälften sowie `pipeline/inventar.py:600–635`, `nl -ba` für den vollständigen Zusatzvertrag und Inline-Python für Manifest-/Strukturanzeige, vollständige Skriptdiffs, technische Schutz-/Pendingzählung, einzelne Originaltextseiten, alle 32 öffentlichen Dokumentationszellen und Lizenz-HTML. Diese Shell-Lesungen endeten mit Exit 0. Kein Rohdaten- oder Antwortdump erfolgte.

Zwei anfängliche umfangreiche Toolausgaben wurden durch das äußere Ausgabebudget gekürzt. Betroffene Annahmeentscheidung, Korrekturbericht und Anforderungen wurden danach in getrennten vollständigen Ausgaben gelesen. Manifest und sämtliche Pins wurden zusätzlich vollständig maschinell verarbeitet; eine gekürzte Anzeige wird nicht als vollständige Textausgabe bezeichnet. Die anfängliche Referenzzählung ließ Abschnittsverweise aus und wurde im eigenen Skript korrigiert und erneut ausgeführt. Das änderte kein Originalartefakt.

Die substantiellen eigenen Shellstarts waren `python3 outputs/loop/inventory004-e-v2-repro/recheck.py`, zweimal `python3 outputs/loop/inventory004-e-v2-repro/cases.py` und `python3 outputs/loop/inventory004-e-v2-repro/independent.py`, jeweils Exit 0. Der zweite Gegenfalllauf ergänzt die vollständige Referenzzählung; dieselben 13 eigenen Kandidaten bleiben erhalten. Asynchron gestartete Prozesse wurden über ihre tatsächlichen Session-IDs bis Exit 0 abgefragt. Alle 45 frischen Extraktions-/Renderprozesse endeten mit Exit 0. Erwartete Gegenfall-ValueErrors wurden kontrolliert aufgefangen und als tatsächliche Abweisungen protokolliert; akzeptierte Falschkandidaten sind keine technischen Skriptabbrüche. Es gab keinen fehlgeschlagenen Builderlauf und keine Installation zur Fehlerumgehung.

Der abschließende individuelle Prettier-Aufruf hebt die Ignoreliste mit `--ignore-path /dev/null` auf und nennt ausschließlich diesen Bericht und die eigene `summary.json`. Der eigene Formatlog enthält die tatsächlichen Aufrufe, ausgegebenen verarbeiteten Pfade und Exits. Ein Exit 0 auf ignorierten Dateien wird nicht als Prüfung gewertet. Weitere JSON-, Skript- und Bilddateien sind über den Index gehasht; sie sind nicht pauschal als individuell formatiert erklärt.

Keine ESS-Rohdaten, `data/local`, Personenkennungen, Antwort-/Designzeilen, A/B-Hälften, Partei-/Links-Rechts-Antwortwerte, Verteilungen, Portal-Analysis, Authentifizierung, Zugangsdaten oder Secrets wurden gelesen oder ausgegeben. Keine Installation, globalen Änderungen, Commits, Pushes, Gesamtformatierung, `pnpm check`, Veröffentlichung oder UI-Änderung. Die eigenen Kandidaten enthalten nur öffentliche Dokumentationsannotation. Das endgültige Vor-/Nachprotokoll bestätigt unveränderte 17+130 Pins und die technische Grundlage. Dieser Bericht wird nach seinem tatsächlichen Schlussformatcheck samt SHA-256 eingefroren; der eigene Index bindet ihn ohne Selbstreferenz.

## Vollständiger tatsächlicher Startauftrag im Wortlaut

```text
Frischer unabhängiger methodischer/Reproduktions-Nachprüfer INVENTORY-004-E/v2, keinAutor, bislangunbeteiligt. Ausschließlich Worktree /home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003, Shellworkdir explizit, apply_patchABSOLUT. Paket reports/loop/packages/INVENTORY-004-E/v2/manifest.json SHA e1e184883b5f2ca04f729b2c2383777070601af6eba049c72e040aa1e1f56ca2,17files130sourceInputs. Vollständig gefrorene AGENTS/Issue/Nachtauftrag/Prüfregeln/Analyseplan/Anforderungen/Lizenzen/Prüfaufträge/beidevollständigenv1Erstberichte/Annahmeentscheidung/Korrekturbericht/neueJSON/PureZusatzcode lesen. Keine aktuellen anderenNachberichte/Loopfindings/Agentlisten/Verteidigung, keineweiterenAgents. NachprüfungE-R01/E-R02/E-S01/E-R03Runde1: zwei eigene vollständige bytegleicheBuilderläufe aus exaktOwnumgebundenenKopien, alleROOT/OUT/PUBLIC/PDFPaths/PNPMCWD/BBox/Log/KandidatenWritepfadevollständigpreflight vorStart. Originalbuild/readtests neverLiveausführen. Nur outputs/loop/inventory004-e-v2-repro/ und reports/loop/reviews/INVENTORY-004-E-v2-repro.md schreiben. Original17+130Pins/SafePath/ScopeVorNach, Basiscsv296/205(205PendingkeinezweiteCSV) unverändert. VollständigerDiff genau2sichtbarePunktfelder+3Adminpfade,808BelegealleanderenFragefelder/7offeneGrenzen unverändert. ZusatzcodeBindung an tatsächlicheOriginalCodezeilen, notwendigeFilter/EinleitungsVollständigkeit,Codebookfilterbeleg+Variante,18sichtbareListenfassungen, übernommenesReviewercodejetztAutorenarbeit ehrlich. Alle7früherenund12neuenGegenfälletatsächlichMutation/Delta/Fehlernachprüfen; eigene weiterekohärenteFilter/Labels/ListenGegenfälle aktivsuchen ohneQuote/Sollurteil. Original DEQ43–54/List50–67PDF51–68/CodebookE208–218 selbsttextuellundwesentlicheOriginalseitenvisuell, insbesondereE12/13Liste58frischesRastervsPDFTokenpunkt, E8Filter46/47+CB211, E20Vignette/E26Definition/Randominstruction/CAPIunexecuted unterscheiden. Keine empirischeScience/Eignung/Polung/Konstrukte/Neutralität/4.2Abgleich/CAPIBehauptung, späterePflichtenNICHTGEPRUEFTnichtgescheiterteAnalysen. SourceChainundStandardsumfangkorrekt, keinUniversalsemantikbeweis. NeueE2-RxxFindings genaueAussageProblemBelegFundstelleWirkungbegründeteSchwerekonkreteKorrekturNachprüfung, existingIDs/Runde1behalten. KeinESSraw/local/AntwortoderDesignzeilen/Personen/A/B/ParteiLR/Verteilungen/PortalAnalysis/AuthSecrets/globalWrites/InstallConda/CommitPush/Gesamtformat/pnpmcheck/weitereAgents. PDF/unslop vorAnwendunglesen.IndividuelleFormatchecks ignorierterDateien nur tatsächlicheVerarbeitungzählen. VollständigentatsächlichenStartauftragwortgetreu, Modellgpt-6.1-solultra geerbtInternUnknown,Toolsangebot+NutzungCommandsExitsFehlläufe/SharedFSkeinSandbox dokumentieren. GleicheCodexfamilie KI-AuditnichtakademischesPeerReview/Garantie. VollständigenNachberichtabschließenimmutableSHA+OwnIndexmelden.
```
