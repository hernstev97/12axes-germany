# CONFIRM-PUBLICATION-001 – unabhängige technische Erstprüfung

3. Oktober 2026. Prüfer: Codex-Subagent `/root/confirm_export_review`. Urteil: **NICHT_BESTANDEN**.

Geprüft wurde die unveränderte Fassung `v1` des kompakten Pakets mit neun Pins. Der neue Exportguard hat drei erhebliche technische beziehungsweise Vertragsfehler. Ein echter B-/FULL-Export ist damit nicht angenommen. Dieses Urteil bewertet weder das Messmodell noch ein empirisches Ergebnis.

## Umfang und Unabhängigkeit

Arbeitswurzel: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Branchangabe des Koordinators: `research/life-93-night-20261003`; kein Git-Aufruf durch diesen Prüfer.

Gelesen wurden `AGENTS.md`, `docs/project.md`, das Paketmanifest, `pipeline/confirm_publication.py`, die dort gepinnten unveränderten Abhängigkeiten, der ESS-Veröffentlichungsvertrag und die als Autorenbelege freigegebenen Unterlagen. Der Autorenbericht und seine sechs/72 Eigenchecks wurden nicht als bestandene unabhängige Prüfung übernommen. Keine aktuellen fremden Reviewerurteile wurden gelesen. Die Quellenanalyse oder Messabnahme wurde nicht neu eröffnet.

Keine echte Datei unter `data/raw/` oder `data/local/`, kein echter privater Receipt, keine echte Assignment-Datei und kein echter politischer B-/FULL-/C-Eingang wurde geöffnet. Die sechs freigegebenen Aggregate unter `outputs/loop/r-runtime/confirm-runtime-author-002/*aggregate.synthetic.json` stammen aus erfundenen Eingaben. Alle selbst erzeugten Dateien und Kopierziele liegen ausschließlich unter `outputs/loop/confirm-publication-review/`. Dortige Unterpfade namens `data/local` sind eigens erfundene IO-Mocks, keine Zugriffe auf die private Arbeitswurzel.

Codex-Erstprüfer und Autor gehören derselben Modellfamilie an. Diese Unabhängigkeit verhindert die gemeinsame Nutzung von Ersturteilen, beseitigt aber keine gemeinsamen Modellfehler.

## Tatsächliche Checks

Der unveränderte Manifestinhalt war vor und nach der Prüfung bei **9/9 Pins identisch**. Belege: `outputs/loop/confirm-publication-review/pins-before.json` und `pins-after.json`. Die Forschungs- und Pipeline-Dateien wurden nicht verändert.

Ausgeführt wurde:

```text
python -B outputs/loop/confirm-publication-review/review_checks.py
Exitcode 1
87 Fälle/Assertions, 81 bestanden, 6 legitime Confirm-Fehlerformen zurückgewiesen
reviewOutcome NICHT_BESTANDEN
```

Die sechs fehlgeschlagenen Kompatibilitätsfälle sind ausdrücklich fehlgeschlagen. Die beiden CP-01-Gegenfälle bestätigen mit erfolgreichen eigenen Assertions, dass unerwünschte Veröffentlichungen stattfinden; solche erfolgreichen Nachweisassertions sind keine bestandenen Produktanforderungen.

Eigene Belege: `review_checks.py`, `checks.json`, `execution.json` sowie die erhaltenen Mocks unter `outputs/loop/confirm-publication-review/io-mocks-v2/`. Die exklusive Fixture-Erzeugung bewahrt bereits vorhandene Nachweise. Eine Wiederholung benötigt einen frischen eigenen Fixturepfad.

Bestanden haben insbesondere:

- Alle sechs freigegebenen synthetischen M2-/M3-/FULL-Aggregate, einschließlich tatsächlicher R-JSON-Einzelscoreunterdrückung.
- Legitime `FAILED`-/`UNAVAILABLE`-Formen mit dem bisherigen Fehlerpräfix, ein fehlgeschlagener EFA-Lauf, `INCONCLUSIVE`-RMS und ein einzelner bestandener, dennoch unterdrückter Score als Zeichenkette.
- 23 gezielte Injektionen oder Abweichungen. Dazu gehören respondentförmige Extrafelder, Anzahlen als Arrays, falsche Ladungs-/Korrelations-/Schwellendimensionen, leere Pins, verschobene Scorekeys, falsche Bestätigungsentscheidungen und nicht endliche Zahlen.
- Vollständige `export_confirmation`-IO-Läufe für B und FULL auf erfundenen Dateien, einschließlich echter exklusiver Ausgabe und Hashprüfung. Wiederholtes Schreiben wird abgewiesen; die erste Ausgabe bleibt erhalten.
- Exportcodeänderung, fehlender Codepin und privater Reviewpfad werden vor dem ersten privaten Pfadcheck abgewiesen. Die instrumentierten privaten Checks blieben jeweils bei null.
- Falsche Lauf-/Probe-Exitcodes, Arm-/Labelabweichungen, falsche Autorisierung und Code-/Runtimepins werden abgewiesen. Entry-, Autorisierungs- und Aggregatbytes werden gegen ihre Receipt-Hashes geprüft.
- Runtimeänderung, nach erfolgreichem Aggregathash weiterhin schemawidrige Nutzlast, private Eingangsänderung und Receiptänderung vor dem Kopieren werden abgewiesen.
- Ein ausdrücklich gepinnter Veröffentlichungsvertrag verhindert dessen Änderung. Ein Zielsymlink wird abgewiesen, sein Ziel bleibt unverändert.
- Ein tatsächlicher CLI-Aufruf mit ungültigem Label endet mit Exitcode 2, ohne Standardausgabe und mit dem festen Fehler `CONFIRM_PUBLICATION_REJECTED`.

Die IO-Mocks lassen den echten Exportguard, Stage-/Runtime-Preflight, Datei-/Hash-/Receiptprüfungen und Schemavalidator arbeiten. Nur Git-Tagzugriffe sind durch deterministische Assertions auf den erfundenen öffentlichen Fixturebestand ersetzt; kein Git lief. Erwartete eingefrorene Code- und Softwarepins werden innerhalb des Mock-Kontexts an erfundene Dateibytes gebunden. Das prüft die Guardlogik, belegt aber keinen echten R-Lauf, keine echte Softwareinstallation und keine tatsächliche Tagveröffentlichung. Es wurde kein R-Prozess gestartet.

## CP-01 – Veröffentlichungsvertrag und Attribution umgehen die geschlossene Ausgabeform

Schwere: erheblich. Fundstellen: `pipeline/confirm_publication.py:23`, `:128`, `:153` und `:154`.

`public_export_preflight` verlangt nur die drei Einträge in `CODE`. Der ESS-Veröffentlichungsvertrag ist kein obligatorischer Gatepin. Nach `validate_confirmation` übernimmt der Export `contract['source']` vollständig in `attribution`; dieses neu hinzugefügte Objekt wird nicht mehr durch eine geschlossene Ausgabeform geprüft. Der abschließende Preflight kann einen nie verlangten Vertragspin auch nicht nachprüfen.

Zwei vollständige Exportmocks besitzen sämtliche verlangten Codepins und sonst gültige erfundene Stage-/Runtime-/Receiptbindungen, lassen jedoch den Vertragspin im Exportgate weg:

1. `unguarded-contract-missing-license`: Der Vertrag enthält nur einen erfundenen Creator und einen leeren Änderungshinweis. `export_confirmation` schreibt die öffentliche JSON-Datei erfolgreich, obwohl `attribution` keine ESS-Zitation, Lizenz oder Lizenz-URL mehr enthält.
2. `unguarded-contract-respondent-shaped-attribution`: `contract.source.respondents` enthält einen erfundenen Identitäts-/Antwortvektor. Der Export schreibt diesen zusätzlichen Pfad unverändert in die öffentliche Datei. Es handelt sich ausschließlich um einen erfundenen Nachweisvektor.

Assertions `confirmed_contract_bypass_missing-license` und `confirmed_contract_bypass_respondent-shaped-attribution` bestehen. Beide erfundenen Ausgaben sowie ihre Rückgabehashes sind erhalten. Der Nachweis benötigt weder eine gleichzeitige Dateisystemänderung noch eine echte private Eingabe. Dass mutable Gates keine unforgeable authority sind, erklärt diese fehlende verpflichtende Bindung nicht.

Minimal korrigieren: Den Veröffentlichungsvertrag als obligatorischen öffentlichen Eingabepin vor privaten Reads und erneut vor der Kopie verlangen. Seine Herkunfts-, Lizenz- und Änderungshinweise mit einer festen, geschlossenen Form prüfen. Auch die endgültige Ausgabe einschließlich `attribution` muss nur die ausdrücklich erlaubten Quellenfelder enthalten; `**contract['source']` darf keine ungeprüften Zusatzfelder weitergeben. Einen fehlenden Lizenz-/Änderungshinweis und einen respondentförmigen Attributionspfad jeweils mit einem eigenen Gegenfall abweisen.

## CP-02 – Neue Confirm-Fehlercodes fehlen im geerbten Schema

Schwere: erheblich. Fundstellen: `pipeline/confirm_publication.py:65` und `:76`; `pipeline/ordinal/confirm.R:6`, `:17` und `:143`; Schemaäste `$defs.model2`, `$defs.model3`, `$defs.efa2` und `$defs.efa3`.

Die geerbten Codepatterns erlauben `ESS_DEVELOPMENT_*`, `ORDINAL_ADAPTER_*` und `ORDINAL_SUPPORT_*`. `confirm.R` erzeugt bei eigenen Warnungen beziehungsweise unbekannten Bibliotheksfehlern dagegen unter anderem `ESS_CONFIRMATORY_LIBRARY_WARNING` und `ESS_CONFIRMATORY_LIBRARY_ERROR`. Diese Codes sind feste, datenfreie Runtimecodes. Die neue Funktion erweitert ihre übernommenen Fehleräste nicht.

Vier legitime synthetische Formen werden deshalb durch `validate_confirmation` mit `A_AGGREGATE_SCHEMA` zurückgewiesen: zwei `model.status=FAILED`-Formen, `diagnostics.status=UNAVAILABLE` und ein fehlgeschlagener EFA-Lauf. Alle übrigen Formen und Bestätigungsentscheidungen passen zum jeweiligen Status. Das Verfahren fällt geschlossen aus, kann aber legitime, offen zu berichtende Bestätigungsfehler nicht veröffentlichen.

Minimal korrigieren: Die neuen Confirm-spezifischen Fehlercodes in allen betroffenen neuen Model-/Diagnostik-/EFA-Fehlerpfaden ausdrücklich zulassen, weiterhin nur als begrenzte feste Codeform. Die bereits geprüfte A-Schemadatei muss dafür nicht global geöffnet werden. Die vier fehlgeschlagenen Kompatibilitätsfälle müssen anschließend angenommen werden; freier Fehlertext bleibt abzulehnen.

## CP-03 – EFA-Mappingfehler haben keinen erlaubten Statusast

Schwere: erheblich. Fundstellen: `pipeline/ordinal/confirm.R:101`, `pipeline/confirm_publication.py:76` und die übernommenen EFA-Äste.

Wenn alle drei EFA-Fits ausgeführt wurden, die nachfolgende Ausrichtung beziehungsweise erwartete Zuordnung aber scheitert, liefert `ec_selected_efa` ein Objekt mit `runs`, `factor_count`, `rotation_se`, `eligible=false` und `mapping_failure`. Die Erfolgsfelder `repeat_alignment`, `expected_mapping`, `reproduced` und `expected_mapping_passed` fehlen in diesem legitimen Fehlerfall.

Der übernommene Erfolgsast fordert diese Erfolgsfelder; die übrigen Äste erwarten mindestens einen fehlgeschlagenen Fit. Es gibt keinen Ast für drei ausgeführte Fits mit fehlgeschlagenem Mapping. Zwei eigene Kompatibilitätsfälle werden mit `A_AGGREGATE_SCHEMA` abgewiesen. Einer nutzt `ESS_CONFIRMATORY_LIBRARY_ERROR`, der zweite das bereits zugelassene `ESS_DEVELOPMENT_LIBRARY_ERROR`. Der zweite Nachweis trennt diesen Formfehler von CP-02.

Minimal korrigieren: Einen geschlossenen EFA-Fehlerast für genau diese Form anlegen. Er muss drei ausgeführte, formgeprüfte Fits, das feste `factor_count`, den vorhandenen Rotationstext, `eligible=false` und einen begrenzten `mapping_failure`-Code verlangen. Auch dieser Fall darf keine Erfolgsfelder oder beliebigen Zusatzpfade vortäuschen.

## Grenzen und gesicherter Stand

Die gemeinsame veränderliche Dateisystem- und Receiptvertrauensgrenze bleibt bestehen. Die Mocks prüfen technische Bindungen, keine kryptografische Laufattestation oder atomare Transaktion. Weder eine echte B-Ausführung noch deren Ergebnis ist Gegenstand dieser Prüfung. Es gibt keine wissenschaftliche, allgemeine rechtliche oder Release-Abnahme. Lizenzangaben werden hier gegen den gepinnten Projektvertrag geprüft, nicht als Rechtsgutachten bestätigt.

Steven hat während dieser Prüfung die fachliche Priorität auf ein breites Politikprofil geändert. Auf Nachricht des Koordinators wurde nach Sicherung der vorhandenen Erstprüfung angehalten. Keine neue Korrekturrunde, keine weitere Datenprüfung und kein echter Export wurden begonnen. CP-01 bis CP-03 bleiben offene Befunde der ungeprüften Exportfunktion; sie sind kein Auftrag, die Neunerfassung fachlich weiterzuführen.

`pnpm check` wird zentral vom Koordinator geführt. Der Prüfer hat keinen eigenen pnpm-Lauf als bestanden ausgewiesen. Der zuletzt mitgeteilte vollständige zentrale Lauf `033` hatte Exitcode 0 vor diesem Bericht; neue WIP-Checks obliegen dem Koordinator. Keine eigenen Hintergrundsessions oder Prozesse sind noch aktiv.
