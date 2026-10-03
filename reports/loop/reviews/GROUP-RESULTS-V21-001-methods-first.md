# Ersturteil GROUP-RESULTS-V21-001, Methoden und Reproduzierbarkeit

Rolle: `methods_reproducibility`. Urteil: `NOT_ACCEPTED` für die Ergebnis-/Exporttransition dieser Prüffassung. Die drei tatsächlichen sicheren Aggregate bestehen mein unabhängiges Rechenorakel. Die neue Exportbibliothek lässt aber eine aus Aggregaten nachweisbar unmögliche Eligibility-Konfiguration durch. Das blockiert hier die Exportfreigabe; es ist kein Befund eines falschen tatsächlichen Antwortanteils.

Prüfmanifest: `reports/loop/packages/GROUP-RESULTS-V21-001/v1/manifest.json`, SHA-256 `dddbcda2fe8a18f46a45ee812100508d9c3ed10c5cca8c8d391be648e474b13a`. Alle 64 öffentlichen Pins und genau die drei darin bezeichneten privaten Aggregate wurden als Bytes geprüft. Tatsächliche Resultatscope: `ESS5e03_6`, `ESS8e02_3`, `ESS9e03_3`. Die allgemeinen öffentlichen Verträge enthalten weitere Studien; deren synthetische Softwarefälle erweitern diesen Resultatscope nicht.

Ich habe keine anderen Ergebnisurteile, Eltern-/Koordinationszustände oder Verteidigung gelesen. Die gebundenen Vorzugriffs-Erstberichte wurden ausschließlich als Bytes gehasht, ihre Urteilsprosa nicht gelesen. Allgemeine Repositoryregeln und `unslop` wurden gelesen. Deklarierte Zugangstatsachen aus öffentlichen Verträgen bleiben deklarierte Tatsachen. Ich habe keine tatsächlichen Rohdatenpfade aufgelöst, gelistet, stattiert, geöffnet, gehasht oder auf Header geprüft und keine andere private Arbeitsdatei gelesen. Kein Netz, Auth, Installation, Git, Server oder tatsächlicher Gruppenlauf wurde ausgeführt.

## GR21-M-001: Fehlende Machbarkeitsbedingung in der neuen Exportbibliothek

Blockierend für diese Ergebnis-/Exporttransition. `pipeline/policy_group_export_v21.py:220` prüft die getrennten Zustandsachsen und einige kombinierte Zähler. Am Ende von `_eligibility` fehlt die Bedingung, dass der noch nicht erklärte Teil von `vote=yes` in den verbleibenden Parteizuständen Platz haben muss.

Mit `Y = vote_states.yes`, `E = eligible_group_case_count`, `A = yes_vote_with_party_not_asked_count`, `M = party_states.source_missing` und `B = party_states.technical_export_blank` muss gelten:

```text
0 <= Y - E - A <= M + B
```

Dies ist eine notwendige gemeinsame Machbarkeitsbedingung der bereits publizierbar beschreibbaren Aggregatstruktur. Sie verlangt keine Personenzeilen und verwechselt die zwei Zustandsachsen nicht mit disjunkten Gesamtkategorien.

Mein ausschließlich synthetischer Gegenfall nutzt den öffentlichen Test-Fixture mit unveränderten Frageverteilungen. Ich erhöhe `de_case_count`, `vote_states.yes` und `party_states.structurally_not_asked` um jeweils zehn synthetische Fälle und lasse `yes_vote_with_party_not_asked_count` bei null. In diesem Fixture haben weiterhin alle synthetischen Fälle `vote=yes`, die hinzugefügten Party-NotAsked-Fälle müssten also ebenfalls `yes+NotAsked` sein. Es gibt keine Party-Missing- oder Blank-Fälle für den unerklärten Rest. `validate_group_reference_candidate` akzeptiert dennoch. Der synthetisch gültige Gegenfall, bei dem diese zusätzlichen Fälle stattdessen Party-Blank sind, wird ebenfalls akzeptiert und soll zulässig bleiben.

Reproduktion ohne tatsächliche Kandidaten: `outputs/loop/group-results-v21-methods/synthetic_boundary_checks.py`. Ergebnis: `syntheticImpossibleEligibilityRejected = false`, `syntheticValidEligibilityResidualAccepted = true`. Zahlen und Artefakte dieses Beispiels sind synthetisch und keine tatsächlichen Gruppenbasen.

Erforderliche begrenzte Korrektur: die Restbedingung vor der Freigabe ergänzen und einen ablehnenden synthetischen Regressionsfall sowie zulässige Missing-/Blank-Restfälle prüfen. Kein neuer Gesamtaudit der unveränderten v2-Fragenauswahl ist dafür nötig. Die tatsächlich geprüften Aggregate erfüllen diese stärkere Bedingung bereits.

## GR21-M-002: Tatsächliche Aggregatarithmetik bestanden

Mein eigenes Skript `outputs/loop/group-results-v21-methods/independent_aggregate_oracle.py` nutzt unabhängige Decimal-Arithmetik und ruft für das Rechenurteil keine Pipeline-Prüffunktion auf. Es prüft jedes vorhandene Studien-/Gruppen-/Fragepaar und jede der vier Gewichtsvarianten, auch zurückgehaltene und leere Referenzen. Sämtliche damit überprüfbaren Identitäten bestehen:

- Originalcodeinventar und Reihenfolge, feste 100/5-Kriterien aus ungewichteten gültigen Fällen, echte Nullzellen und Nullanteile bei positivem Nenner; fehlende gültige Antworten behalten Null-Anteile als `null`.
- Kategoriegewichte geteilt durch den jeweils eigenen gültigen Fragegewichtssummen-Nenner, Summen der Kategorien, Count- und Gewichtspartitionen sowie identische Fallscope über `pspwght`, `dweight`, `unweighted` und `anweight`.
- Ungewichtete Gewichtssummen entsprechen Counts. Alle Gruppenfälle bleiben in den fragenspezifischen Gesamt-/Missing-/NotAsked-Partitionen; kein gemeinsamer Nenner über unterschiedliche Fragen. Gruppen-Gesamtgewichte bleiben über Fragen stabil.
- Fehlgründe samt technischem Export-Blank bleiben getrennt und summieren sich zum Frage-Missing. NotAsked bleibt außerhalb des gültigen und des Missing-Nenners. Kein Imputieren, Zusammenlegen von Antwortkategorien oder Selektieren aufgrund von Gewichtssensitivität.
- Beide Eligibility-Achsen summieren sich jeweils zum selben DE-Fallbestand. Die unzulässige Summe beider Achsen wird nicht gebildet. Gruppenfälle, benannte Kategorien, heterogenes Other, Non-Yes-Inkonsistenzen und die stärkere gemeinsame Machbarkeitsbedingung sind konsistent.
- `all_eligible_group_cases`, Diagnose-Fallzahlbindung, deklariertes Ratio-Status-/Extrema-Verhältnis und die aus Gewichtssummen ableitbaren Ratio-Schranken stimmen überein. Die Maximaldifferenzen der drei Sensitivitätsvergleiche wurden aus den vier gewichteten Kategorieverteilungen neu gerechnet.
- Design, Standardfehler und Varianzen bleiben `null`; daraus entsteht weder Konfidenzintervall noch Norm oder Score.

Die numerischen Einzelprüfungen und Paarbewertungen stehen ausschließlich in `outputs/loop/group-results-v21-methods/aggregate-oracle-results.json`. Keine tatsächlichen Anteile, kleinen Zellzahlen, Gruppenbasen, Gewichtssummen oder Ratios stehen in diesem öffentlichen Bericht. Als zusätzliche Implementierungsprüfung akzeptiert der neue Kandidatenvalidator alle drei tatsächlichen Kandidaten; das ist von meinem unabhängigen Orakel getrennt.

## GR21-M-003: Bindungen bestanden, Provenienzgrenzen bleiben

Die tatsächlichen Run-Envelopes, vollständigen Inventare, Editionen, Studien-, Gruppen- und Fragenidentitäten, Originalcode-/Missing-/NotAsked-Definitionen, vollständigen Vertragsbytes, öffentlichen Quellenpins, ausführenden Bibliotheksbytes, Vorzugriffsmanifest, Freeze, Gate, Run-Receipts und inneren kanonischen Kandidatenhashes sind konsistent gebunden. Die Gate-Freigabe umfasst ausschließlich die drei zugelassenen Studien. Alle benannten Gruppen und das heterogene Other bleiben im Inventar und erhalten dieselben Regeln.

Dies bestätigt Byte- und Aggregatkonsistenz. Kopierte Rohdatenhashes, Zeitangaben, Freeze-/Tagbelege und öffentliche Zugangserklärungen beweisen in diesem Review weder tatsächlichen Downloadweg noch offizielle Rohdatei-Authentizität oder einen aus Rohbytes unabhängig wiederholten Lauf. Einzelgewichte, tatsächliche individuelle Ratioextrema, die Vergleichsbasis gegen den ersten individuellen Ratio und die ursprüngliche Zuordnung einzelner Fälle lassen sich aus diesen Aggregaten nicht unabhängig rekonstruieren. Ich habe diese Grenzen nicht durch tatsächlichen Rohzugriff überschritten.

## GR21-M-004: Synthetische Softwareprüfungen und CLI-Grenze

Die 92 bestehenden Tests zu Gruppenarithmetik, bewachtem Zugriff und Pure Export bestehen. Die Zugriffstests laufen ausschließlich in eigenen synthetischen Temporärrepositories unter dem geschützten QA-Ordner; sie lesen oder statten keine tatsächliche Roh-/Privatdatei. Der zusätzliche unabhängige Gegenfall GR21-M-001 scheitert trotz der grünen bestehenden Suite. Grüne synthetische Tests ersetzen daher weder die tatsächliche Aggregatprüfung noch die fehlende Guard-Bedingung.

Die Exportbibliothek führt keine Anwendungs-I/O, CLI, Gate-Lesung oder Veröffentlichung aus. Sie bindet vollständige Vertragsobjekte, Kandidatenhash und formal ausdrückliche eindeutige Paare. Nicht ausdrücklich genehmigte vorbereitete Paare werden zu `result_review_withheld`; null-Referenzen geben keine privaten Zahlen weiter. Formale Reviewer-/Manifest-/Decision-Strings beweisen weder die Existenz tatsächlicher Berichtsbytes noch Reviewerwillen oder eine Rootannahme. Das bleibt außerhalb der Pure API nachzuweisen.

Die CLI wurde ausschließlich als gebundener Quelltext geprüft und nicht aufgerufen. Sie beschreibt einen separaten Privatlauf, prüft lokale/ferne Tagbindung und erhält vorhandene Privatläufe. Sie enthält keinen Public-Export-Aufruf. Synthetische fünf-Studien-Fälle erweitern die tatsächliche Drei-Studien-Berechtigung nicht.

## GR21-M-005: Urteil und Freigabegrenze

Für diese Prüffassung genehmige ich kein Paar zur Veröffentlichung. `approvedGroupQuestionIdsByStudy` ist deshalb für jede der drei zugelassenen Studien leer. Die privat gespeicherten, einzeln neu berechneten Schwellenbewertungen sind keine automatische Publikationsliste. Nach der begrenzten Korrektur von GR21-M-001 muss eine neue festgelegte Exportfassung konkret geprüft werden; eine neue Rootentscheidung darf nicht aus synthetischen Decision-Strings entstehen.

Das Hauptproduktziel bleibt das breite Politikprofil mit 43 Originalfragen und acht Themen. Dieser Schritt betrifft optionale, getrennte historische Deskriptionen nach erinnerter Bundestags-Zweitstimme. Er beweist keine aktuellen Parteipositionen, Wahlprognose, Normen, Personen-/Studienkombination oder wissenschaftliche Güte. Die 100/5-Regel ist eine festgelegte Darstellungsheuristik; ihre Präzision oder Anonymität wurde hier nicht validiert. Quellen-/Konstrukt-/Fairnessurteil, menschliche Annahme, Claude-Kontrolle, Release-, Merge- und Deploymentfreigabe sind durch diese Methodenrolle nicht erteilt. Dieselbe Codex-Familie kann gemeinsame Fehler teilen.

Eigenes QA liegt ausschließlich unter dem laut `.gitignore` ausgeschlossenen `outputs/loop/group-results-v21-methods`, Ordner mit 0700, Dateien mit 0600. Keine gemeinsame Forschungs-, Pipeline-, Vertrags- oder Paketdatei wurde geändert. Es erfolgte kein allgemeines `pnpm check` und keine UI-Prüfung; dies ist ein ausschließliches Review mit den genannten begrenzten Tests.

Abschließender Integritätscheck: Manifest, sämtliche gemeinsamen öffentlichen Pins und die drei tatsächlichen privaten Aggregatpins unverändert bestätigt.
