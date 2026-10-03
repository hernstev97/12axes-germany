# Angular-Bindung öffentlicher historischer Einzelreferenzen

Stand: 2026-10-03. Eigenständiger Codex-Autorauftrag nach dem gesicherten Checkpoint `7b12a62da2fa4b9d8be3e12fb0678daae45c2025`. WIP, unroutierte Angular-Vorbereitung. Keine Instrument-, Gestaltungs-, Verständnis-, rechtliche oder Veröffentlichungsfreigabe.

## Auftrag und Grenzen

Root autorisierte die technische Bindung der tatsächlich akzeptierten 42 öffentlichen historischen Einzelreferenzen. Die ursprüngliche Angular-Fassung und der erste Autorbericht bleiben nachvollziehbar erhalten. Geschrieben wurden nur Dateien in `web/src/app/policy-draft/` und dieser neue Bericht. `ANGULAR-POLICY-DRAFT-WIP.md` wurde weder überschrieben noch formatiert; sein unveränderter SHA-256 ist `a0f1474a8360045f7b5800c0a1b3f5dbf102dd15c7aa62cdf74bac8766a6425d`.

Zusätzlich persönlich gelesen wurden ausschließlich die fünf öffentlichen JSON-Dateien unter `data/reference-v2/`, deren README, `reports/loop/policy-v2-export-decisions.json` und beide `RESULTS-V2-001-*-decision.json`. Die konkreten Erstberichtbytes wurden nur für ihre SHA-256-Authentifizierung geöffnet. Keine privaten Kandidaten, Rohdaten, CSV-Dateien, Header, `data/raw/` oder `data/local/` gelesen. Keine neue ESS-Auswertung oder Referenzberechnung durchgeführt. Der schon gelesene öffentliche Originalkatalog und sein Adapter bleiben unverändert.

Root übernimmt den getrennten lokalen Forschungsharness, Integration, Browserprüfung und Git. Der Autor hat keine Browserdienste, Installationen, Gitaktionen, Produktionsrouten, App-Hülle oder öffentliche Navigation geändert.

## Nutzbare Eingabe und reproduzierbarer Generator

`REVIEWED_HISTORICAL_REFERENCES` aus `web/src/app/policy-draft/reviewed-historical-references.ts` ist die tatsächlich nutzbare Eingabe vom Typ `HistoricalReferenceInput`. Ihre Objekte, Arrays und Kategorieeinträge sind rekursiv eingefroren. Sie enthält alle 42 akzeptierten Verteilungen und den ausdrücklichen Eintrag `{ questionId: 'ESS10SCe03_2:cttresa', reference: null, reason: 'withheld_base_or_cell_count' }`. Für `cttresa` gibt es keine künstliche Verteilung und keine Ersatzfallzahl null oder null Prozent.

Der optionale Komponenteninput bleibt standardmäßig `null`. Ein separater autorisierter Wrapper kann die Eingabe als `[historicalReferences]="REVIEWED_HISTORICAL_REFERENCES"` binden. Die neue Datendatei aktiviert weder eine Route noch einen Teststart.

Reproduktion vom Repositorywurzelverzeichnis:

```sh
node web/src/app/policy-draft/generate-reviewed-references.mjs --write
node web/src/app/policy-draft/generate-reviewed-references.mjs --check
node --test web/src/app/policy-draft/reference-generator.test.mjs
```

Der Generator öffnet nur eine feste öffentliche Pfadliste. Er verwendet keinen aus einer Entscheidungsdatei übernommenen Dateipfad für zusätzlichen Dateizugriff. Alle tatsächlichen öffentlichen Inputbytes, die Exportentscheidung, beide Entscheidungsbelege, die ursprünglichen Berichtbytes und der unveränderte semantische Katalogadapter müssen ihren festen Pins entsprechen. Neue oder auch nur anders formatierte Inputs erfordern eine ausdrücklich neue Bindung. `--check` ist lesend und verlangt bytegenaue Gleichheit mit dem reproduzierten TypeScript-Modul. `--write` schreibt ausschließlich dieses Modul im eigenen Ordner.

`reference-binding.ts` prüft danach den begrenzten Exportstatus und Umfang, beide vorgeschriebenen Rollen, identische akzeptierte Fragen und Kandidaten, Manifestbindungen, Studienausgaben, Quellenvertrags-/Kandidatenhashes, sämtliche 43 Frageidentitäten, die 42 akzeptierten Referenzen und den zurückgehaltenen Eintrag. Die Kategoriezuordnung nutzt ausschließlich Originalexportcodes aus dem authentifizierten semantischen Katalog. Umgekehrte Reihenfolge einer Codeliste verändert die Projektion nicht. Druckcode `00` und Exportcode `0` bleiben ausdrücklich getrennt gebunden.

Die veröffentlichten Kategorieanteile und Fallzahlen werden unverändert kopiert. Summen- und Fallzahlzerlegungsprüfungen kontrollieren nur technische Vollständigkeit; sie erzeugen keine neuen statistischen Schätzer. Sensitivitätsdiagnosen, Gewichtssummen und Verhältnisse aus den öffentlichen Quelldateien werden nicht als neue Ergebnisse berechnet und nicht als persönliche Unsicherheit dargestellt. Standardfehler und Konfidenzintervalle bleiben ausgeschlossen.

`REVIEWED_REFERENCE_PROVENANCE` hält öffentliche Inputhashes, Kataloghash, begrenzten Exportumfang und den zurückgehaltenen Fragebezeichner am generierten Artefakt fest. Datenableitung unter CC BY-NC-SA 4.0, Originaldokumentation getrennt unter CC BY-SA 4.0; diese Bindung erweitert keine Nutzungsrechte.

## Anzeige und technischer Eingabevertrag

Die vorhandenen Referenztypen wurden um getrennte ungewichtete Fallzahlen für gültige Antworten, Gesamtbasis Deutschland, fehlende Antworten und nicht gestellte Fragen sowie eine optionale Liste ausdrücklich fehlender Referenzen erweitert. Die Laufzeitbindung prüft diese Zerlegung und verwirft numerische Ersatzwerte für den Null-Eintrag.

Jede eingebundene Einzelreferenz zeigt ihre Originalstudie und Ausgabe, historische Erhebungszeit, ursprünglichen Modus, Gewicht `pspwght` und die gültige Fallzahl `n`. Die Beschreibung unterscheidet die gewichteten Kategorieanteile von ungewichteten Fallzahlen: Der Nenner der Anteile ist die Summe der Gewichte gültiger Antworten dieser Frage. Gesamt-, Missing- und Nicht-gestellt-Fallzahlen stehen getrennt und werden nicht mit dem Überspringgrund einer Websitzung gleichgesetzt.

Für B6 `cttresa` zeigt die Oberfläche die zurückgehaltene historische Referenz wegen unzureichender Basis oder Zellbesetzung und keine Referenzzahlen. Die Originalfrage, eine gegebenenfalls eigene Auswahl und der Quellenkontext bleiben verfügbar. Ein späterer Wechsel des optionalen Inputs zurück auf `null` entfernt die eingebundenen Zahlen und den spezifischen Zurückhaltehinweis wieder.

Die bisherigen Grenzen bleiben sichtbar: historische Einzelstudien statt aktueller Norm, 15+-Zielpopulation statt ausschließlich Wahlberechtigten, ESS8 ohne München und ohne Wiederherstellung durch Gewichtung, ESS10 Self-completion statt einer ersatzweisen Interviewreferenz, neue Zusammenstellung und Durchführung. B25s historische Kategorieverteilung beweist weiterhin keine Gleichwertigkeit der neuen Webdurchführung oder ursprünglichen Anschlussfragen. Keine gemeinsamen Dimensionen, Scores, Parteipositionen oder Antwortspeicherung hinzugefügt.

## Authentifizierte öffentliche Inputpins

| Input | SHA-256 |
| --- | --- |
| `data/reference-v2/ESS5e03_6.json` | `e489fe013d1cbd3d72b9ae816e422757ce8d34ae575d09f64df13a1750dc4bc6` |
| `data/reference-v2/ESS8e02_3.json` | `fb720cc18049f037ed86670bd76a51c3c1770342a61f5627b7afbfb127898ad7` |
| `data/reference-v2/ESS9e03_3.json` | `34e71b448c0c315cf9f19bda30628874c95464faf661813a65f25a3f9ad82be2` |
| `data/reference-v2/ESS10SCe03_2.json` | `e75dfbadcf68c14dce9d13c8a8a2dd1abc6e8a6e96618f960c8cd61c54bc3184` |
| `data/reference-v2/ESS11e04_2.json` | `453d8ce3273c9e29bb08a49be6e69da46591e3d1ed89f306051b085c511ec721` |
| `data/reference-v2/README.md` | `a2917e6b57c59e96298345e526e9311de82b1422cfbb9a8bb1cfabc0684ba57c` |
| `reports/loop/policy-v2-export-decisions.json` | `a87f780a7219253f7f3773d051b7001f438b19b2fb2d0ee820fc22c1157a16df` |
| `reports/loop/reviews/RESULTS-V2-001-methods-decision.json` | `765db3005c736174a3d1f9819ab212917ce50d6143059b8cfce2dac3f6f67806` |
| `reports/loop/reviews/RESULTS-V2-001-sources-decision.json` | `e5c3a730dc6cf71e5b788d4251c109b86a7d510684bf945b17ceaa6e48306065` |
| `reports/loop/reviews/RESULTS-V2-001-methods-first.md` | `1bb14ba2dba3d57612d66c5a50c29ce049606e8fddb062ff6b616f56b60462ee` |
| `reports/loop/reviews/RESULTS-V2-001-sources-first.md` | `7a2814359b94ab3a73dd22a090b2a10c6b51db6cc243d8586e8ae15bfdc580e8` |
| `web/src/app/policy-draft/public-catalogue.ts` | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |

Der öffentliche semantische Quellkatalog bleibt an SHA-256 `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` gebunden. Er wird durch den vorhandenen unabhängigen Quellenabgleich mit 43 Fragen und 315 Codezuordnungen geprüft.

## Artefaktpins

| Datei unter `web/src/app/policy-draft/` | SHA-256 |
| --- | --- |
| `generate-reviewed-references.mjs` | `72d2970f297e860c7375bce2dbe3cf9d7a81cc28e40766f3af2bdc8861aa5e04` |
| `reference-binding.ts` | `07a928b852be0abb47025ecd2aa64af3c9db32fd36b3c564716dbed55ab69dfb` |
| `reference-generator.test.mjs` | `0165d5d945ec01061e87dfb5c40ba22b6efd758c308bf967ecd3090d437676f9` |
| `reviewed-historical-references.ts` | `4a305618c23d8f9059782b364387e741616b399961989a1bd6448b1014520bcb` |
| `historical-reference.ts` | `58eb05517a43a4d3ea0a62c20f06c39857ca242e50748d3bce1a0f17a33683ab` |
| `policy-draft.ts` | `cc5f6122faa183d9e9e46bb1bef65ae6d6d0831e91bfb1de257eba57d68ec725` |
| `policy-draft.html` | `4d8396cebf97fd60441c989dccd020a44369e089858ec2510c191a0a1dc628f5` |

## Tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| `node web/src/app/policy-draft/generate-reviewed-references.mjs --write` | BESTANDEN. Nur das eigene generierte Modul geschrieben. |
| `node web/src/app/policy-draft/generate-reviewed-references.mjs --check` | BESTANDEN. Reale Inputbytes authentifiziert und generiertes Modul bytegenau reproduziert. |
| `node --test web/src/app/policy-draft/reference-generator.test.mjs` | BESTANDEN, zehn Tests. |
| `pnpm --filter politikprofil test --watch=false --include 'src/app/policy-draft/*.spec.ts'` | BESTANDEN, drei Dateien und 26 Tests; Start 2026-10-03 um 14:55:53 UTC, Dauer 5,92 Sekunden. |
| `pnpm --filter politikprofil typecheck` | BESTANDEN, strenge Angular- und TypeScript-Prüfung. |
| `pnpm exec prettier --check web/src/app/policy-draft` | BESTANDEN. |
| `node web/src/app/policy-draft/verify-public-catalogue.mjs` | BESTANDEN, unveränderte 43 Originalfragen und 315 Codebindungen. |
| `pnpm check:handbuch` | BESTANDEN. Die präzise Originaltextausnahme wurde zuvor von Root außerhalb dieses Autorbereichs umgesetzt. |
| Vollständiger Repository-/Produktionsbuild-/Harnesscheck und Browserprüfung | Noch Root-Abgleich. Der Autor startete keinen Browserdienst. |
| Empirische Reanalyse, unabhängige Rohdatenreproduktion, methodische oder menschliche Abnahme | Nicht Gegenstand dieses technischen Autorauftrags, nicht durchgeführt. |

Neue Tests prüfen echte Eingabebindung mit 42 Referenzen und einem Null-Eintrag, rekursive Unveränderlichkeit, getrennte Fallzahlen in der Anzeige, weiterhin sichtbare historische Zeit-/Gewichtsbeschränkung, Entfernung bei Wechsel auf `null`, genaue öffentliche Zugriffsliste, Byte-Manipulation an Referenzen/Entscheidungen/Receipts/Originalberichten, Dissens der beiden Iteminventare, falsche Ausgabe/Kandidaten/Codes, numerische Einschleusung bei `cttresa`, unzulässige Unsicherheitswerte, falsche Fallzahlzerlegung und geänderte Kategorienreihenfolge. Manipulierte Fälle existieren nur als negative Testfälle im Arbeitsspeicher; sie werden nicht als Referenzartefakt geschrieben.

In diesem Ergänzungsschritt gab es keinen fehlgeschlagenen Prüflauf. Node meldet weiterhin die bekannte ExperimentalWarning für `stripTypeScriptTypes`; sie ist kein Fehler. Der Autor erklärt weder die wissenschaftliche Gültigkeit noch Neutralität oder eine Veröffentlichung der Website. Die beiden akzeptierenden Erstberichte stammen aus derselben Codex-Modellfamilie und können gemeinsame Fehler enthalten. Der neue Generator authentifiziert deren festgehaltene Bytes und begrenzte Entscheidung, er ersetzt ihre fachliche Prüfung nicht.

Root prüft als Nächstes die frische Integration und den realen Browserharness mit vorhandener App-Hülle. Die ursprüngliche öffentliche Navigation bleibt ohne Forschungsentwurf. Menschliche Gestaltung, Verständnistests, rechtliche Veröffentlichungskontrolle und Releasefreigabe bleiben offen.
