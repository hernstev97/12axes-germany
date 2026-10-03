# POLICY-GROUPS-V21-WIP

2026-10-03. Eigener technischer Erstbericht zur reinen In-Memory-Vorbereitung. Keine tatsächlichen Antworten, Gruppengrößen oder Referenzergebnisse gelesen oder berechnet; keine Empirie-, Quellen-, Produkt- oder Releasefreigabe.

## API und feste Grenze

Neu: `pipeline/policy_groups_v21.py` und `pipeline/tests/test_policy_groups_v21.py`. API: `prepare_group_references(csv_text, study_contract, group_study_contract) -> PrivateGroupStudyReferences`. Die Vertragsargumente sind jeweils **ein** `studies[n]`-Objekt aus v2 bzw. v2.1. Root hat diese Grenze ausdrücklich bestätigt; sein zukünftiger I/O-Guard muss die Bytes der vollständigen v2.1-Hülle und der Quellen getrennt binden. Die vorhandene reine `_validated_contracts(study, group_study)`-Vorprüfung prüft die Rechenfelder und liefert statische Fehler; sie ist kein Gate.

Serialisierung, Eligibility, Gewichte und Anzeigegrenzen entsprechen dieser Hülle als feste Regeln: vote `1` und gültige deklarierte Zweitstimmenkategorie, Primärgewicht `pspwght`, getrennte `dweight`-/unweighted-Sensitivitäten, `anweight`-Diagnose, 100 gültige Fälle und mindestens fünf Fälle in jeder positiv besetzten Originalkategorie. Es gibt kein Schwellenargument und keine nachträgliche Gruppenauswahl. Kategorien, Missing-Gründe und Nicht-gestellt-Codes stammen aus dem übergebenen v2-Adapter. Die bestehenden 43 Studien-/Fragenidentitäten werden über `_VARIABLES` der reinen v2-Berichtsbibliothek geprüft; diese technische Abhängigkeit gehört zum zu bindenden Paket.

Fünf Studien bleiben getrennt. Jede Anfrage behandelt genau eine Studie und deren vollständige vorher deklarierte Gruppen-/Fragenreihenfolge. Benannte Gruppen und `Other` werden gleichermaßen erhalten, auch ohne Fälle. Source-Labels und originale/unvollständige Formoptionen werden unverändert übernommen; kein politischer Einheits- oder Kohärenzanspruch. Insbesondere werden ESS11-API `8`/`9` nicht zu `Other` umbenannt und `55` bleibt `Other`; ESS10-API `7` wird nicht aus gedruckter `9` geraten.

Die Rückgabe enthält ausschließlich gefrorene Aggregate-Dataclasses: Schema `policy-group-reference-v21-wip`, Studienkennung, Edition, Gruppeninventur, pro Gruppe Fragen und vier getrennte Schätzungen, Missing-/Nicht-gestellt-Aggregate, Gewichtssensitivitäten sowie getrennte Eligibility- und Studien-Ratiodiagnosen. Es gibt keine Personen-/Zeilen-/Gewichtsvektoren, CSV-IDs, Designkennungen oder privaten Dateipfade in der Rückgabe. Die Repr der eigenen Aggregate ist verdeckt. Die reichhaltigen Anteile und kleinen Zellen bleiben **privat**, auch bei `withheld_base_or_cell_count`; kein Publicexport oder Statusübergang ist implementiert.

## Parsing, Domänen und Ratio

Nur übergebener Text wird mit Standardbibliothek `csv`/`StringIO` verarbeitet. Header müssen eindeutig und nicht leer sein, alle gewählten Spalten enthalten; alle Zeilen müssen die Headerbreite haben. Zusätzliche Spalten bleiben semantisch uninterpretiert. Nicht-DE-Inhalte werden ebenfalls nicht interpretiert. Originale DE-IDs bleiben exakte Strings und dienen intern allein der Dublettenprüfung über **alle** DE-Einheiten, auch ausgeschlossene. Sie werden nicht mit den Rechenzeilen gespeichert oder über Studien verbunden.

Alle gewählten DE-Antworten sowie vote/party müssen dem festen Muster für nichtnegative kanonische Ganzzahlen mit optionaler Null-Nachkommastelle entsprechen und deklarierte Codes treffen. `1.00` wird gemäß Serialisierungsregel zu `1`; führende Nullen, Exponentialschreibweise, Leerraum und gedruckte Codekonversionen werden nicht geraten. Leere Antworten sind nur als explizit gebundener technischer Blank erlaubt. Unbekannte Codes sind fatal. Fehlertext, Argumente, Repr, Cause und Context bleiben statisch; niedrigere werttragende Ausnahmen werden nicht weitergereicht.

Root bestätigte die **Gewichtsprüfung nur für eligible Gruppenfälle**. Ausgeschlossene DE-Gewichtszellen werden nicht interpretiert. Eligible Gewichte müssen positiv und endlich sein; gewichtete Summen nutzen die vorhandenen `fsum`-Rechnungen. Vote- und Parteizustände sind zwei getrennte Zählachsen mit expliziten Missing-Gründen/Blank/Nicht-gestellt/Nein/Nichtberechtigt. Jede Achse summiert separat zu DE; ihre Summen werden nicht addiert. Die deklarierte Inkonsistenz nonYesVote+validParty schließt die Einheit aus und wird gesondert gezählt. Der zusätzliche Zähler yesVote+partyNotAsked beschreibt nur diese beobachtete Kombination, keine Reparatur oder neue Eligibility-Regel.

Die Ratio-Diagnose wird **einmal über alle eligible Gruppeneinheiten derselben Studie** berechnet, einschließlich späterer Fragen-Missings und Nicht-gestellt-Angaben. Scope: `all_eligible_group_cases`; keine Übernahme von `all_de_cases` und keine Beschränkung auf gültige Antworten einer Frage. Berichtet werden Min/Max und der Vergleich jedes Verhältnisses mit dem ersten eligible Verhältnis mittels `math.isclose(rel_tol=1e-12, abs_tol=1e-12)`. Ohne eligible Fälle: `not_evaluable_no_eligible_group_cases`, Extremwerte und Vergleich `None`. Nichtkonstanz ändert weder Fälle noch Primärgewicht, Gruppen oder Anzeigegrenzen; das arithmetische Diagnoseurteil ist keine wissenschaftlich bestandene Äquivalenzprüfung.

Pro Gruppe/Frage wird die vorhandene `categorical_reference`-Rechnung mit expliziter Gültigkeit/Missing und `design_basis=None` genutzt und ihr Resultat mit `_validate_reference` geprüft. Jede Frage hat ihren eigenen gültigen gewichteten Nenner. Missing-Gründe/technischer Blank und strukturelles Nicht-gestellt werden getrennt gezählt/gewichtet. Nullkategorien bleiben enthalten; ohne gültige Antworten haben alle Kategorien Anteil `None`. Leere Gruppen, einschließlich eines gültigen CSV-Headers ohne DE-Fälle, liefern die volle Inventur ohne Adapterfehler oder Bescheinigung einer deutschen Datenbasis. Alle Varianzen/SE sind `None`, kein Design wird rekonstruiert.

## Synthetische Handorakel und tatsächliche Prüfungen

Die Tests verwenden ausschließlich explizit synthetische Vertrags-/CSV-Inhalte. Reale Studien-/Fragenkennungen dienen der technischen Bindungsprüfung, nicht als empirische Fälle oder neue Fragen. Feste, unabhängig angegebene Brüche sind die Orakel:

| Synthetischer Fall | Erwartung |
| --- | --- |
| 100 gültige Fälle: Kategorie A 30, B 70, C null; A-Gewichte primary/dweight/anweight 2/1/4, B 1/2/2 | Primary A `6/13`, dweight `3/17`, unweighted `3/10`, anweight `6/13`; gültige Gewichte 130/170/100/260. Maximaldifferenzen zu unweighted `21/130`, zu dweight `63/221`, zu anweight null. |
| Fünf zusätzliche Gruppenfälle: Refusal/Don't know/No answer/Blank mit Primärgewichten 3/5/7/11, Nicht-gestellt mit 13 | Q1 total 105 und Gewicht 169; valid 100/Gewicht 130, missing vier/Gewicht 26, Nicht-gestellt eins/Gewicht 13. Q2 hat nur 60 gültige Fälle/Gewicht 90, Kategorie A `2/3`, 40 Missing und fünf Nicht-gestellt. Ratio-Bereich behält alle 105 Gruppenfälle. |
| Zwei private Fälle primary 1/2, dweight 2/1, anweight 4/2 | Primary A `1/3`, dweight/anweight `2/3`, anweight-Differenz `1/3`; Studienratio-Min/Max 1/4, Status withheld. |
| Gleiche kleinste positive Float-Einheit mit Gewichten im Verhältnis 1:2 | Primary-Anteil `1/3`, kein Verlust des Anteils durch Subnormalität. |
| 99/100 gültige Fälle sowie positiv besetzte Zellen 4/5 | Exakte vorgegebene withheld/prepared-Grenzen, gleich für benannte und Other-Gruppen; Nullkategorie löst keine Zellgrenze aus. |

Weitere Regressionen prüfen Nullgruppen/all-missing/kein DE, Routingachsen und Gründe, Ratioextreme in anderer Gruppe bzw. bei Fragen-Missing, Skalierung und Zeilenumordnung, getrennte fünf Studien/43 IDs, unbekannte Codes, exakte Stringidentitäten, CSV-Quotes/Zeilenumbrüche, Dubletten auch außerhalb Eligibility, Header/Zeilenbreite, fehlerhafte Gewichte, statische Arithmetikfehler, Quellenauswahl/Other-Umetikettierung, fehlende I/O-Aufrufe und unveränderliche Rückgaben ohne IDs/private Pfade.

Alle eigenen unittest-Aufrufe nutzten `PYTHONDONTWRITEBYTECODE=1` und ausschließlich `pipeline.tests.test_policy_groups_v21`:

| Lauf | UTC Start / Ende | PID | Tests / tatsächlicher Exit |
| --- | --- | ---: | --- |
| 1 | 14:44:07.877466 / 14:44:08.153809 | 3229437 | 15 / 0 |
| 2 | 14:46:08.540914 / 14:46:08.826301 | 3243455 | 18 / 0 |
| 3, Abschlussstand | 14:48:28.350321 / 14:48:28.646884 | 3259078 | 18 / 0 |

Kein fehlgeschlagener Testlauf. Nach Lauf 1 wurden gezielte Regressionsfälle und die statische Vorprüfung ergänzt; nach Lauf 2 wurde die Fehlerweitergabe einschließlich Context begrenzt und die ESS10-Codekonversionsabwehr konkret geprüft. Die Wiederholungen hatten damit jeweils neue Änderungen als Anlass.

Eine separate Prüfung **nur öffentlicher Metadaten** lief 2026-10-03T14:46:08.581778+00:00 bis 14:46:08.588210+00:00, PID 3243445, Exit 0: voller Gruppenvertragpin, Konstanten, alle fünf einzelnen Vertragsvorprüfungen, globale 43 Frageidentitäten und exakte Kategorien-/Missing-/Nicht-gestellt-Übereinstimmung zwischen v2-Adapter und Katalog. Sie las keinen CSV-Text. Die Zahl deklarierter Gruppenkennungen ist ebenfalls 43; dies sind Katalogidentitäten, keine beobachteten Gruppengrößen.

Nachweise und Aufrufe: `outputs/loop/policy-groups-v21/test-run-{1,2,3}.{json,log}`, `metadata-compatibility.json`, `protected-before.json`, `code-and-protected-after.json`. Alle eigenen Prozesse sind abgewartet und beendet; kein Server oder Hintergrundprozess gestartet. Keine Installation, Netz-/Auth-/Git-/pnpm-/Gate-/Exportaktion oder Delegation.

## Gelesene Quellen und Pins

Der öffentliche v2.1-Gruppenvertrag wurde vollständig gelesen: nach zunächst gekürzter Gesamtausgabe alle fünf Studienobjekte und die übrige Hülle in ungekürzten Folgeauszügen. Sein Pin entsprach vor der Arbeit dem Root-Auftrag. Die Hülle enthält öffentliche Quellen-/Provenienzbehauptungen und einen eingebetteten Root-Zugangsstand; deren verlinkte Caches, Errata, Zustandsdateien, Rohdateien und tatsächlichen Ergebnisse wurden weder geöffnet noch per Dateistat untersucht. Ein vorheriger privater v2-Softwarelauf ist aus dieser Hülle als Zugangsmitteilung bekannt, ohne Empfang von Antwort- oder Gruppengrößenwerten. Kein umfassend unberührter Bestätigungsanspruch.

Weitere erlaubte Kontexte: aktueller öffentlicher v2-Analysevertrag und Katalog, reine v2-Adapter-/Analyse-/Kategorienbibliothek sowie deren technische Export-/Berichts-APIs; technische Testauszüge aus Analyse/Export. Keine Reviewerberichte, aktuellen Marginals, tatsächlichen Header, `data/raw`-/`data/local`-Dateien oder anderen Agentenberichte gelesen. Die drei öffentlichen Vertrags-/Katalogdateien und fünf Bibliotheken wurden vor Implementierung gepinnt; die fünf Bestandstestpins kamen vor dem eigenen Ersttest hinzu. Alle 13 geschützten Dateien waren im Abschlussstand bytegleich; historische Berichte und Frontenddateien wurden nicht geschrieben. Kein allgemeiner Repository- oder Gateaudit.

| Quelle / neue Datei | SHA-256 |
| --- | --- |
| `data/gruppenvertrag.v2.1.entwurf.json`, 135823 Bytes | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `data/analysevertrag.v2.entwurf.json` | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| Neue Bibliothek, 24391 Bytes | `9b680b07385cefc665a54e583cf4b44f03d1305b2829a724fb9afbd7103284b6` |
| Neue Tests, 27715 Bytes | `e60f7df0b3c5989d6fbc688358af8c7c0a93ef57ceb1b6caafbf8c062d3ebddd` |

Die zehn unveränderten v2-Code-/Testpins stehen vollständig im eigenen `code-and-protected-after.json`. `unslop` wurde auf diesen Bericht angewandt. Dieser Erstbericht wird nicht nachträglich zum Reviewerurteil umgeschrieben.

## Offene Schritte und Grenzen

Die API authentifiziert weder die Herkunft des CSV-Texts noch Dateiedition, tatsächliche Header, Population, vollständiges Design, Lizenz-/Quellenbedingungen oder die Absicht des Callers. Inerte Provenienzfelder werden nicht wissenschaftlich beurteilt und niemals in Aggregate kopiert; ihre Echtheit und Bindung bleiben beim Root-Guard der vollständigen Hülle. Die Gruppierung ist historischer Selbstbericht, kein geprüftes Wahlergebnis, heutiges Parteiprogramm oder aktuelle Wählerschaft. Die offenen Originalform-/Alias-/Other-Codierungsgeschichten und B25-Administration werden durch Rechnen nicht geschlossen.

Endliche positive Einzelgewichte garantieren keine als Float darstellbaren Summen oder Quotienten. Nicht darstellbare Summen/Quotienten oder auf null unterlaufende Quotienten scheitern statisch als Arithmetikfehler; es gibt kein stilles Entfernen solcher Fälle. Synthetische Schwellentests sind keine empirische Präzisions-, Anonymitäts- oder Fairnessgarantie. Repr/typisierte Dataclasses sind keine Zugriffskontrolle und isolieren keinen beliebigen Python-Code oder globale Manipulationen.

Noch fehlen die getrennten frischen Übergangsbewertungen, Root-Plan-/Bytebindung und Gruppen-I/O-Autorisierung, tatsächliche Metadaten-/Datenprüfung, Ergebnisbewertungen sowie ein gesondert geprüfter sicherer Publicexport. Keine v2-Marginalfreigabe wird als Gruppenfreigabe übernommen. Kein Pooling, latenter Score, Gesamtvergleich, nächste Partei, Intervall, persönliche Unsicherheit oder aktuelle Bevölkerungsnorm wird berechnet oder behauptet.
