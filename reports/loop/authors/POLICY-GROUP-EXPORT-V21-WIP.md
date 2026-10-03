# POLICY-GROUP-EXPORT-V21-WIP

Stand: 2026-10-03, Abschluss des begrenzten Exportautorenauftrags. Die reine Bibliothek und 31 synthetische Tests sind fertig. Es gab keinen tatsächlichen Gruppenlauf, keinen Zugriff auf empirische Kandidaten und keine Veröffentlichung. Dieser Bericht ist eine Implementierungsbeschreibung, keine Quellen-, Ergebnis- oder Methodenannahme. Zwei frische Ergebnisrollen und die tatsächliche Rootentscheidung bleiben erforderlich.

Geschrieben wurden ausschließlich `pipeline/policy_group_export_v21.py`, `pipeline/tests/test_policy_group_export_v21.py`, dieser Bericht und eigene Dateien unter `outputs/loop/policy-group-export-v21/`. Bestehende Verträge, Bibliotheken und Berichte wurden nicht verändert. Die zwölf gelesenen öffentlichen Kontext-/Runtime-Dateien waren beim Nachvergleich am 2026-10-03 um 15:23:27.926480 UTC bytegleich; Einzelpins stehen in `pins-after.json`. Die erste Bindung erfolgte um 15:07:57.146444 UTC. Der zusätzliche transitive Import `policy_report_v2.py` wurde eigens gepinnt. Alte Autorenberichte, Reviewerberichte und Gates wurden nicht geöffnet.

Die drei öffentlichen Funktionssignaturen lauten:

```python
canonical_candidate_sha256(candidate) -> str
validate_group_reference_candidate(candidate, study_contract, group_contract) -> None
build_reviewed_group_reference_export(candidate, study_contract, group_contract, decision) -> dict
```

`candidate` ist genau das innere Objekt mit Schema `policy-group-reference-v21-wip`, nicht eine `run.json`-Hülle. Die beiden Vertragsargumente sind die vollständigen v2- bzw. v2.1-Vertragsobjekte. Die Bibliothek hat keine Datei-/Netz-I/O, CLI oder Veröffentlichungsfunktion. Insbesondere importiert sie keine Zugriffshülle: Deren Import würde öffentliche Quellenbytes lesen. Die reine Vertragsvalidierung aller fünf Studien ist keine Erlaubnis, sie empirisch auszuführen.

Die Entscheidung ist geschlossen: genau `schemaVersion`, `decision`, `studyId`, `edition`, `candidateSha256`, `groupContractSha256`, `studyContractSha256`, `reviewManifestSha256`, `approvedGroupQuestionIds`, `reviewers`. Erforderlich sind `schemaVersion=1`, `decision=ALLOW_REVIEWED_HISTORICAL_GROUP_REFERENCES_V21`, eine passende Studien-/Editionsidentität und eindeutige `{groupId, questionId}`-Paare. Jedes Paar muss tatsächlich den Status `prepared_pending_group_result_review` und die 100/5-Grenze erfüllen. Leere Paarfreigaben sind zulässig und erzeugen ausschließlich Nullreferenzen. Es gibt keine automatische Übernahme aller vorbereiteten Paare.

Genau zwei unterschiedliche direkte Berichtpfade unter `reports/loop/reviews/*.md` mit den Rollen `methods_reproducibility` und `sources_constructs_fairness`, je `decision=ACCEPTED_BOUNDED` und syntaktisch gültigem SHA256, sind erforderlich. Unbekannte Entscheidungsfelder, Rollen, Pfade, Statusstrings, doppelte oder fremde Paarfreigaben scheitern. Diese Formprüfung authentifiziert weder Berichtbytes noch Autorenabsicht. Root muss die tatsächlichen Manifest-, Vertrags-, Kandidaten- und Berichtsbytes sowie beide ausdrücklichen Paarfreigaben außerhalb der reinen API prüfen. Der Schutz gilt gegen versehentliche Protokollabweichungen, nicht gegen einen absichtlichen Python-/Root-Eingriff.

Kanonischer Kandidatenhash: SHA256 über UTF-8 von `json.dumps(candidate, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)`. Die Definition entspricht dem vorhandenen reinen v2-Exporter. Objekt-Schlüsselreihenfolge ist ohne Wirkung; Arrayreihenfolge und Zahlendarstellung bleiben relevant (`1` und `1.0` haben unterschiedliche Hashes). Gezählt wird das unveränderte innere JSON-Objekt. Die später zur typisierten Prüfung in Float umgesetzten Gewichtswerte verändern weder Kandidat noch Hash.

Die Entscheidungsfelder für Verträge binden tatsächliche ganze Dateibytes. Davon getrennte kanonische Vollobjektanker verhindern mutierte, zusätzliche oder ausgelassene Quellfelder auch außerhalb der ausgewählten Studie:

| Bindung | SHA256 |
| --- | --- |
| v2-Studienvertrag, ganze Bytes | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| v2.1-Gruppenvertrag, ganze Bytes | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| v2-Studienvertrag, kanonisches Vollobjekt | `aae9eaf00a9195334251e6788eeb60f1bdbc4e6737004be8eb9089e5999c3af4` |
| v2.1-Gruppenvertrag, kanonisches Vollobjekt | `dd799a7976404931a4ce13b8a483c6b05d526e85bd5edb8c51d42f31a78a1ec0` |

Ein Dictionary rekonstruiert keinen Originaldateihash; dessen tatsächliche Prüfung bleibt extern. Änderungen an diesen vollständigen Quellenfassungen benötigen neue Bindung und Prüfung. Ein caller darf die erwarteten Vertragsbytes nicht durch eigene kanonische Hashes ersetzen.

Die Kandidatenprüfung erhält alle Originalgruppen einschließlich unbenanntem `Other` und alle ausgewählten Fragen in der gebundenen Reihenfolge: ESS5 sechs, ESS8 zehn, ESS9 vier, ESS10SC siebzehn, ESS11 sechs, zusammen 43 getrennte Studienzuordnungen. Sie prüft exakte Partei-/Frage-/Kategorieidentitäten, native API-/Form-/Appendix-Labels, Status, vier Gewichtsvarianten, Zähler- und Gewichtssummen, Kategorieanteile, Missinggründe, Nichtgestellt-Zustände, Sensitivitätswerte, Gruppen-/Studienzuordnung und Ratio-Diagnose. Die Ratio-Diagnose hat den Scope `all_eligible_group_cases`, nicht alle deutschen Erhebungsfälle. Nichtwahl/Nichtberechtigung/Missing und inkonsistente Wahl-/Parteizustände werden über ihre geschlossenen Diagnoseidentitäten geprüft und nicht öffentlich ausgegeben.

Ganze nichtnegative Counts müssen echte Integer sein; boolesche Werte gelten nicht als Counts. Zahlen müssen endlich sein. Gewichtssummen und Anteile folgen derselben relativen Toleranz `1e-12` wie die vorhandenen reinen Aggregatvalidatoren. Die Basis muss je Frage mindestens 100 gültige ungewichtete Antworten haben; jede positive Originalkategoriezelle muss mindestens fünf Fälle haben. Echte Nullzellen bleiben bei gültigem Nenner nullwertige Anteile. Fehlende oder kleine Referenzen erhalten keine Ersatzanteile. SE/Varianz/Design und öffentliche Unsicherheit bleiben `null`; erfundene Präzisionsangaben scheitern. Die 100/5-Regeln sind gleichmäßige Projektanzeigeheuristiken, keine validierte Präzisions- oder Anonymitätsgarantie.

Der geschlossene öffentliche Aufbau hat elf Top-Level-Felder: `schemaVersion`, `status`, `studyId`, `edition`, `groupContractSha256`, `studyContractSha256`, `candidateSha256`, `reviewManifestSha256`, `source`, `scope`, `groups`. Die vollständige maschinenlesbare Fassung liegt in `public-schema.json` (JSON Schema 2020-12). Jede Gruppe enthält nur gebundene öffentliche Originalidentität, getrennte Labels, die Kennzeichnung `heterogeneousUnlabelledOther` und ihre Fragen. Jede Frage enthält `id`, `status`, `reference`.

Eine freigegebene Referenz enthält ausschließlich `weight="pspwght"`, die große gültige Einzelbasis `validCount`, deren `totalCount`, `missingCount`, `notAskedCount`, originalgeordnete `{code, proportion}` und `uncertainty=null`. Kategorie-Zellcounts, Gewichtssummen/-vektoren, Sensitivitäten, Ratios, Eligibility-Diagnosen und private Missinggrundsummen werden validiert und verworfen. Nicht freigegebene vorbereitete Paare heißen `result_review_withheld`; kleine und leere Paare behalten ihren technischen Grund. Ihre Referenz ist `null`, ohne Gruppenbasis oder Anteile. `Other` bleibt unbenannt und heterogen, ohne erfundene deutsche Parteiübersetzung. Die Ausgabe wird neu gebaut; Eingaben bleiben unverändert und teilen keine veränderbaren Teilobjekte mit ihr.

`source` bindet Bundestagswahl/Jahr, Erhebungszeit/-population, öffentliche Datei-/Variablen-/Versionsidentität, deutsche Originalfrage, API-Wortlaut, Alias-/Nachcodierungsgrenzen, Dokumentfundstellen und Originalhashes. Daten- und Dokumentationslizenz bleiben getrennt. Der öffentliche Fragenkatalog ist mit Pfad/Hash referenziert. Noch offene Formzuordnungen oder Nachcodierungswege werden damit nicht gelöst. Auch die im Vertrag gebundene B25-Grenze bleibt bestehen: historische statische Frageauswertung ist eine andere Entscheidung als eine neue Website-Administration; der ursprüngliche operative CAWI-Nachlauf ist nicht reproduziert oder validiert. Der Export gewährt keine neue Fragenadministration.

Die Ausgabe beschreibt historische Selbstberichte derselben Studie/Personengruppe, keine verifizierten Wahlergebnisse oder heutige Parteipositionen. Die Studienpopulation ist nicht identisch mit der Wahlbevölkerung. Es entstehen keine Gruppen-Scores, Gesamtentfernung, nächstgelegene Partei, Wahlvorhersage, Personenmatrix, gemeinsamen Fälle über Studien oder unabhängigen Normwerte.

Tatsächliche Prüfprozesse: Python 3.14.7, jeweils `PYTHONDONTWRITEBYTECODE=1 python -m unittest pipeline.tests.test_policy_group_export_v21 -v`. Der erste Lauf hatte 28 Tests, 12 Errors, Exit 1 (0,923 s). Der gesicherte Originaltrace zeigte die Typforderung des vorhandenen `_validate_reference`: synthetische JSON-Integergewichte waren noch nicht zu dessen Float-Dataclass-Typ umgesetzt. Die Korrektur betrifft nur die interne typisierte Prüfung. Danach bestanden 28/28, Exit 0 (1,997 s). Drei zusätzliche unabhängige Gegenfälle prüfen ungleiche primäre Gewichte, nichtkonstante `anweight`-Ratios und deutsche Nichtgruppenfälle bei anderer Gesamtbasis. Der endgültige Lauf bestand 31/31, Exit 0 (2,130 s). Original- und Erfolgslogs einschließlich Hashes sind gesichert; `validation.json` nennt die Befehle und Ergebnisse.

Die Tests decken insbesondere 99/100 gültige Antworten, positive Zellen vier/fünf, echte Nullzellen, leere/Missing-only-Referenzen, native Other-/Appendix-Identitäten, fehlende/doppelte/falsche Freigaben, Byte-/Objekthashverwechslung, vollständige Quellmutation, zusätzliche Kandidatenfelder, private Zeilenfelder, Status-/Zahlenpromotion, Anteil-/Gewichts-/Missing-/Nichtgestellt-Inkonsistenzen, Unsicherheitsbehauptungen, Ratio-Scope, NaN/Zyklen/Customobjekte und fehlende Anwendung-I/O ab. Alle Fixtures wurden aus öffentlichen Vertragsidentitäten und erfundenen Aggregatzahlen erstellt. Die Schemadatei wurde aus diesen synthetischen Ausgaben erzeugt; sie bindet Quellen-/Identitätskonstanten, keine synthetischen Anteils- oder Basiswerte. Arithmetische Identitäten prüft die Bibliothek, nicht JSON Schema allein.

Die Zugriffsspanne dieses Auftrags umfasst öffentliche lokale Anweisungen, Vertrags-/Katalogbytes und reine Pythonquellen per Shell/Python, eigene synthetische Testprozesse sowie eigene Logs/Schema/Hashdateien. Keine tatsächlichen `data/raw`-/`data/local`-Dateien wurden geöffnet oder gestattet, auch keine Header, Antwortwerte, IDs, privaten Kandidaten, Marginal- oder Gruppentabellen. Keine tatsächlichen Reviewerberichte, Gates oder fremden Autorenberichte wurden gelesen. Kein Git, pnpm, Installer, HTTP, Authzugriff, Server, Kontakt oder zusätzliche Agenten wurden eingesetzt. Dies behauptet keine umfassende historische Ergebnisblindheit: Der bekannte Kontext des gepinnten Gruppenvertrags und Roots Mitteilungen bleiben bekannt, darunter der vorangegangene private v2-Marginalsoftwarelauf; Zahlen wurden diesem Autor nicht zugeführt.

Roots Abschlussmitteilung zum Vorzugriffs-Quellenurteil erlaubt derzeit ESS5e03_6, ESS8e02_3 und ESS9e03_3; ESS10SCe03_2 und ESS11e04_2 sind als ganze Studien weiter offen. Diese Aussage stammt nur aus der Koordinatormitteilung, nicht aus einem hier gelesenen Urteil. Die fünf synthetisch getesteten Vertragsstudien ändern diesen Scope nicht. Eine tatsächliche Freigabe je Studie und Fragepaar bleibt Root vorbehalten. Der Autor ist Codex derselben Modellfamilie und liefert keinen zusätzlichen unabhängigen Erst- oder Ergebnisentscheid.

Finale Implementierungspins:

| Artefakt | SHA256 |
| --- | --- |
| `pipeline/policy_group_export_v21.py` | `56eafd87fa0855df11b23cad90e0f7dff3e6c13af3944f20cc430a09cd4509ba` |
| `pipeline/tests/test_policy_group_export_v21.py` | `17f1be3edcc4716acb43d93c8fa5945aa885f4b401d69e9efd494240edc34e7e` |
| `public-schema.json` | `9e2a85f8c18c9d7fcf413635bd0af9a480dde1782339dba1944c8e22112b81f6` |
| endgültiger Testlog | `7cca27669007ccc9f0b1ab25fa8bd2c59214803ce485a3f309630c2b3078327b` |

Runtimepins einschließlich aller transitiven reinen Bibliotheken stehen vollständig in `pins-after.json`. Bericht- und Outputhashes werden nach dem Schreibabschluss in `artifact-hashes.json` gesichert. Offene Abnahmen bleiben Quellen-/Ergebnisannahme, tatsächliche externe Gate-/Manifest-/Berichts-/Kandidatenbyteprüfung, ausdrückliche Paarfreigabe und Veröffentlichung; diese Implementierung ersetzt keine davon.
