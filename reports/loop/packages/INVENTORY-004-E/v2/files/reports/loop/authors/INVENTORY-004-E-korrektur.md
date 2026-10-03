# INVENTORY-004-E: Autorenkorrektur, Runde 1

2026-10-03, Koordinator `/root`. Vorabplan `outputs/loop/inventory004-e-correction/plan-before-correction.json` wurde vor Code- und Datenkorrektur gespeichert. Beide vollständigen unabhängigen v1-Berichte wurden zuvor gesammelt und gelesen; [Annahmeentscheidung](../INVENTORY-004-E-v1-entscheidung.md). Die Erstfassungen bleiben unverändert.

## Korrigierte Artefakte

Neue öffentliche JSON: `data/inventar-e.v2.ergaenzung.entwurf.json`, 2.066.030 Bytes, SHA-256 `0c031abd7be58e14c91360db4e2a438b0b211e1116dd2f1b84ebab612931f6de`. Der vollständige Strukturvergleich ergibt genau zwei Inhaltsänderungen: `/fragen/15/listenheft/sichtbare_kategorien_de/wert/2` und `/fragen/16/listenheft/sichtbare_kategorien_de/wert/2`. Sie entfernen ausschließlich den Schlusszeichenpunkt bei E12/E13. Die zwei Zugriffsfelder und der hinzugefügte Korrekturprovenienzblock sind gesonderte administrative Änderungen. Alle 808 vollständigen Belege, alle übrigen Fragefelder und sieben offene Punkte bleiben unverändert.

Liste 58 auf Original-PDF59 wurde vor der Korrektur selbst frisch mit 200 dpi gerendert und über `view_image` gelesen. Alle drei sichtbaren Kategorien wurden gesehen; die dritte endet ohne Punkt. Original-PDF-Pin, Renderbefehl, Exit 0 und tatsächliche Sichtlektüre stehen in `original-render-command.json` und `original-reading-and-contract-adoption.json`. Der originale Token-/Extraktbeleg mit Punkt bleibt exakt erhalten. Der Ursprung des Textlagenunterschieds ist unbekannt.

Der neue `pipeline/annotations/e_semantic_contract_v2.py` ergänzt den bisherigen Autorenvalidator. Er bindet Fragebogenlabels an die tatsächlich aus den Originalfragepositionen ermittelten Codezeilen, fordert notwendige direkte und übernommene Kontexte, bindet Codebookfilter an ihre Originalextrakte und kontrolliert Variantenbedingungen sowie alle 18 sichtbaren Listenfassungen. Die sichtbaren Erwartungen und die Geometrie stammen aus dem abgeschlossenen Reproduktionsaudit. Ihre Übernahme wird ausdrücklich dokumentiert: **Der übernommene Reviewercode ist jetzt Autorenarbeit und kein weiterer unabhängiger Review.** Der reine Zusatzvertrag setzt separat hashgeprüfte, aus den drei Original-PDFs erzeugte `pages` voraus; er liest selbst keine Dateien. Er ist kein universeller semantischer Validator.

## Tatsächlich ausgeführte Nachbauten und Gegenfälle

Zwei eigene vollständige Builderläufe in getrennten neuen Unterverzeichnissen `run-1/` und `run-2/` erzeugten ihre BBox-Eingaben neu und endeten mit Exit 0. Beide sind untereinander und mit der neuen öffentlichen JSON bytegleich. Die drei gepinnten PDF-Bytes wurden aus dem unveränderten öffentlichen Autorenbestand kopiert; kein eigener neuer Netzdownload wird behauptet. ROOT und OUT der Kopien wurden vor dem Start gezielt auf den erlaubten Worktree und eigene Unterverzeichnisse gesetzt. Historische Quellen-/Autorenfelder bleiben als ursprüngliche Metadaten erhalten; der separate Korrekturblock erklärt die aktuelle Rolle und Zugriffe.

Die eigene erweiterte Kopie des bisherigen Lesetests prüfte die neue Basis und alle sieben ursprünglichen echten Autorenmutationen erfolgreich: Exit 0, 32 Identitäten, 808 Belege. Zusätzlich wurden zwölf vollständige neue eigene Kandidaten tatsächlich verändert und abgewiesen:

| Gegenfall                                                    | Tatsächliches Ergebnis                     |
| ------------------------------------------------------------ | ------------------------------------------ |
| Vollständige E12-Labelobjekte samt echten Belegen vertauscht | Falsche Original-Codezeile, abgewiesen     |
| E8W-Direktfilter entfernt                                    | Notwendiger Kontext fehlt, abgewiesen      |
| Sichtbare E19-Listenpole vertauscht                          | Sichtbare Listenlabels falsch, abgewiesen  |
| E8M-Zuweisung und Codebookfilter gemeinsam falsch geändert   | Originalvariantenfilter falsch, abgewiesen |
| Geerbter E10M-Filter entfernt                                | Notwendiger Kontext fehlt, abgewiesen      |
| Gemeinsame E13-Einleitung entfernt                           | Notwendiger Kontext fehlt, abgewiesen      |
| E12-Filteraufhebung entfernt                                 | Notwendiger Kontext fehlt, abgewiesen      |
| E20-Vignette entfernt                                        | Notwendiger Kontext fehlt, abgewiesen      |
| E26-Definition entfernt                                      | Definition fehlt, abgewiesen               |
| E6-Reihenfolgeanweisung entfernt                             | Anweisung fehlt, abgewiesen                |
| Alter sichtbarer E13-Schlusspunkt wiederhergestellt          | Sichtbare Listenlabels falsch, abgewiesen  |
| Vollständige E11W-Liste durch E10W-Liste ersetzt             | Original-Listenheader falsch, abgewiesen   |

`additional-mutated-cases.json` enthält Kandidatpfade, SHA-256, echte Deltapfade und konkrete Fehlermeldungen. Die sieben früheren Fälle stehen getrennt im eigenen `run-1/read-tests-result.json`. `complete-structural-diff.json`, `byte-reproduction.json`, die zwei Buildbefehlsprotokolle und der erweiterte Testbefehl dokumentieren die wirklichen Ergebnisse. Alle acht im Vorabplan gebundenen Originaldateien stimmen nach der Korrektur weiterhin bytegleich; `original-protection-after.json`.

## Offene Abnahmen und Laufgrenzen

Zwei frische unabhängige Nachprüfungen der neuen JSON, des Zusatzvertrags und der behaupteten Reparaturen stehen aus. E-R01/E-R02 sowie E-S01/E-R03 bleiben bis dahin in Runde 1 offen. Die positive Autorenprüfung ist keine unabhängige oder wissenschaftliche Freigabe. Ausgabe 4.2, tatsächliches CAPI, E1-Mapping, E9-Formulierungs-/Fußnotengrenzen, Eignung, Polung, Neutralität, Konstrukte, Messmodell und empirische Analyse bleiben offen. Die neue Sourcefunktion prüft keine beobachtete Diskriminierung oder politische Identität.

Tatsächliche Laufzeit: T3 Code, `gpt-6.1-sol`, Reasoning ultra. Interne Revision und Vorgaben unbekannt. Benutzt wurden `functions.exec` mit Shell, `write_stdin`, `apply_patch` und `view_image`, Python-Standardbibliothek, vorhandenes Poppler und vorhandenes pnpm/Prettier zur JSON-Erzeugung. Keine Installation, globalen Änderungen, Authzugriffe, ESS-Roh-/Personen-/A-/B-/Partei-/LR-Antwortwerte, Verteilungen, Portal-Analysis oder Veröffentlichung. Eigene Writes liegen ausschließlich im Worktree; ursprüngliche gemeinsame Artefakte und Erstberichte wurden nicht überschrieben. Shared-FS und Pfadkopien sind keine OS-Sandbox. Dies ist Autorenarbeit innerhalb eines KI-Audits derselben Modellfamilie.
