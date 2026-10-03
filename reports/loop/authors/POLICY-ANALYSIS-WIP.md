POLICY-ANALYSIS-WIP — reine Aggregationsvorbereitung, 2026-10-03

Autor: Codex-Unteragent `/root/breadth_topic_frame`. Root bleibt alleiniger Koordinator und bindet Studienprovenienz, Gates, tatsächliches I/O und spätere Exportentscheidungen. Die zwei neuen Python-Dateien und 16 eigene synthetische Tests sind fertig. Der gezielte unittest-Lauf endete mit Exit 0. Das ist private technische Vorbereitung, keine tatsächliche Analyse einer Studie und keine Empirie-, Veröffentlichungs-, Produkt- oder Releasefreigabe.

Arbeitsort: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der vom Koordinator bezeichnete Branch ist `research/life-93-night-20261003`; ich habe keinen Git-Befehl ausgeführt und keinen aktuellen Branch-/Commitstand selbst bestätigt. Geschrieben wurden ausschließlich `pipeline/policy_analysis_v2.py`, `pipeline/tests/test_policy_analysis_v2.py`, dieser Erstbericht und Dateien in `outputs/loop/policy-analysis-v2/`.

Für die Implementierung wurden nur die ausdrücklich erlaubten Adapter- und Kategorienbibliotheken inhaltlich gelesen/importiert. Die bestehenden eigenen Code-/Berichtspins wurden ohne inhaltliche Forschungs-/Urteilslektüre gehasht. Keine tatsächlichen Antworten, Roh-/lokalen Daten, Reviews, state-/handoff-Dateien, Forschungsdateien, Authinformationen oder v2-Entwürfe/Quellenkataloge wurden gelesen. Eine eingehende technische Nachfrage eines anderen Arbeitspakets zum API-/Hashstand wurde ausschließlich Root gemeldet; es gab keine direkte Abstimmung oder Delegation. Die API war zu diesem Zeitpunkt bereits nach dem bestandenen Testlauf fertig. Der zuvor gelesene `unslop`-Skill wurde für den Bericht weiter angewendet.

Die neuen Codepins sind:

| Datei | SHA-256 |
| --- | --- |
| `pipeline/policy_analysis_v2.py` | `d7d23c99b84d352f161ea607f575155594ecd1ff365ad89e8f2624b4f9500309` |
| `pipeline/tests/test_policy_analysis_v2.py` | `f6012546dcabb5912dd9faa889df8e78272043295b6a70a09d0425b7db907d45` |

Die reine API besteht aus `prepare_study_references(parsed: PrivateStudyCsv) -> PrivateStudyReferences` und `expose_prepared_candidate(prepared: PrivateStudyReferences) -> dict`. Die Kette `expose_prepared_candidate(prepare_study_references(parsed))` arbeitet ausschließlich im Speicher. Der neue Bibliothekscode enthält keine Datei-, CLI-, Netzwerk-, Druck-, Logging-, Storage- oder Authoperation. Python-Importmechanik und die separat autorisierten Test-/Evidenzprozesse sind davon zu unterscheiden. Es gibt keinen Programmeinstieg in der Bibliothek.

Die Eingabegrenze akzeptiert genau die konkreten Parser-Dataclasses. Der Vertrag wird anhand seines geschlossenen Adapterschemas neu kopiert und geprüft. Für verwendete Records werden konkrete Record-/Answer-Klassen, Tupelformen, eindeutige unveränderte IDs, positive endliche Floatgewichte, vollständige Gewichtskennungen sowie die Konsistenz von Originalcode, gültiger Antwort, Eligibility, Missing und Missing-Reason erneut geprüft. Fremde Dictionaries, Listen statt Parserrecords, unbekannte Antwortcodes, widersprüchliche Flags, fehlerhafte Gewichte und doppelte IDs führen zu einem statischen Fehler. Die Werte aus den Parserdiagnosen werden nicht als Autorität für die Aggregate behandelt; die Aufbereitung berechnet ihr Accounting aus den Records neu.

Diese Typ-/Datenprüfung ist keine Provenienzbescheinigung. Ein privilegierter Caller kann Python-Dataclasses selbst konstruieren; die Bibliothek kann nicht beweisen, dass ein bestimmter Parserlauf oder eine authentische Datei vorlag. Ebenso kann sie die Herkunft manuell zusammengesetzter, formal konsistenter Records nicht erkennen. Die Schnittstelle nimmt genau eine Parserausgabe entgegen und bietet selbst keine Zusammenführung verschiedener Studien oder Personen an. Root muss die Herkunft, Ausgabe/Dateiversion und die Zulässigkeit jedes tatsächlichen Aufrufs getrennt belegen.

Die zurückgegebene private Aufbereitung besteht ausschließlich aus neuen eingefrorenen Aggregat-Dataclasses. Sie enthält Studien-/Editions-/Fragenkennungen, ursprüngliche gültige Kategoriecodes, vier getrennte Referenzschätzungen, Missing-Reason-Aggregate, ein gesondertes Nichtgestelltenaggregat und Gewichtungsdiagnosen. Sie speichert keine IDs, einzelnen Recordobjekte, Roh-Missing-/Nichtgestelltencodes, Gewichtsvektoren oder Designschlüssel. Private Aggregatklassen haben einen redigierten `repr`. Die enthaltene generische Referenz führt nur die zulässigen Quellenkennungen, Originalkategorien und Aggregate; ihr Design ist immer `None`. Die Objekte sind weiterhin privat und unreviewed, nicht als veröffentlichbar bezeichnet.

Jede Frage bleibt mit ihrer eigenen Fragen-ID und den Originalkategorien in Vertragsreihenfolge erhalten. Es gibt vier getrennte Aufrufe der unveränderten Kategorienbibliothek: `pspwght` als `primary`, `dweight` als `sensitivity`, `unweighted` mit Gewicht 1.0 als `sensitivity` und `anweight` als `equivalence_diagnostic`. Alle vier benutzen dieselben Fälle und Fragezustände; gültige Countnenner und fehlende/nichtgestellte Counts stimmen deshalb überein. Ihre gewichteten gültigen Nenner sind ausdrücklich eigene Summen. Die gewählten Rollen liefern hier keine quellspezifische Gewichtungsbegründung.

Das Accounting trennt alle DE-Fälle, Eligible, gültig, Missing und nichtgestellt nach den bestehenden Regeln der generischen Bibliothek. Der gültige Anteil verwendet ausschließlich gültiges Gewicht derselben Frage. Nichtgestellte sind `eligible=False`; Missing ist getrennt `eligible=True, missing=True`. Es gibt keine Imputation, Polung, Ordinalwerte, Personenjoins, zusammengefassten Frage-/Studienreferenzen, Scores, Faktoren, Perzentile oder Intervalle. `total_count`/`total_weight` sind ausschließlich Accountingfelder je Frage für alle übergebenen DE-Fälle, kein Gesamtscore.

Kein beobachtetes Design wird rekonstruiert. Für alle temporären `Observation`-Objekte ist `design=None`; jeder Referenzaufruf erhält `design_basis=None`. Bei gültigen Antworten ist der generische Varianzstatus `no_design_basis`; bei vollständig fehlendem gültigem Nenner ist er `no_valid_responses`. Alle Varianzen und Standardfehler sind intern `None`. Der Kandidat enthält keine SE-/Varianzfelder und insbesondere keinen künstlichen Null-SE. Vollständige oder unvollständige beobachtete Parserkennungen verändern die Punktanteile nicht. Ein tatsächlich vollständiger, quellspezifisch geprüfter Designvertrag bleibt ein externer späterer Schritt.

Für jede im Vertrag benannte Missing-Reason werden über alle DE-Fälle die Anzahl und die Primärgewichtsumme aggregiert. Verschiedene Missing-Codes mit derselben Reason werden zusammengefasst; deklarierte Reasons ohne Beobachtung bleiben mit Count/Gewicht null enthalten. Die rohen Missing-Codes werden nicht übernommen. Nichtgestellte erhalten ihr eigenes Count-/Primärgewichtsaggregat. Die gewichteten Summen verwenden `fsum`; Integercounts verwenden exakte Integeraddition. Alle DE-Count-/Gewichtsnenner bleiben im Primäraccounting sichtbar, ohne Missing-Shares oder andere automatische Prozentprofile zu erzeugen.

Die Gewichtungsdiagnosen sind ausschließlich deskriptiv: je Frage das Maximum der absoluten kategorialen Differenz zwischen primär und ungewichtet, zwischen primär und `dweight` sowie zwischen primär und `anweight`. Ohne gültige Antworten sind diese Differenzen `None`. Hinzu kommen Minimum/Maximum der Verhältnisse `anweight/pspwght` über alle DE-Fälle, einschließlich Missing und nichtgestellt. Die Verhältnisse sind Metadatenaggregate, keine ausgegebenen Fallgewichte. Kein Unterschieds- oder Verhältnisschwellenwert wählt Items aus oder erklärt eine Gewichtung wissenschaftlich äquivalent. Nicht endlich oder nicht positiv darstellbare Verhältnisse und nicht darstellbare Summen werden als statischer Arithmetikfehler begrenzt.

Der Vorabdarstellungsstatus je Frage folgt exakt den vom Auftrag vorgegebenen Projektregeln:

- `valid_count == 0`: `no_valid_answers`; die privaten Originalkategorien bleiben mit Counts/Gewichten null und `proportion=None` erhalten.
- `valid_count < 100` oder mindestens ein positiver ungewichteter Kategoriecount kleiner als 5: `withheld_base_or_cell_count`.
- Sonst: `prepared_pending_result_review`.

Eine Originalkategorie mit Beobachtungszahl null löst die positive Zellcountregel nicht aus. Ihre Nullschätzung bleibt bei vorhandenem gültigem Nenner erhalten. Die Regeln basieren auf ungewichteten Counts, nicht auf gewichteten/effectiven Fallzahlen. Sie sind Projektheuristiken, keine Präzisions-, Repräsentativitäts-, Anonymitäts- oder wissenschaftlichen Gütegarantien. Es gibt keinen automatischen reviewed-, published- oder freigegeben-Status.

Auch zurückgehaltene Fragen behalten intern alle geschätzten Statistiken. Keine Frage oder Kategorie wird aufgrund dieser Ergebnisse aus dem Inhaltskatalog ausgewählt oder entfernt. Es wird kein persönlicher Antwortzustand gelesen oder bearbeitet. Der Kandidatenbuilder gibt jede Frage weiter; bei `no_valid_answers` und `withheld_base_or_cell_count` ist ausschließlich `reference: null` gesetzt. In diesen Kandidaten erscheinen keine Proportionen, Sensitivitätsdifferenzen oder Verhältnisextrema. Aggregierte Counts, Primäraccounting und Missing-/Nichtgestelltensummen bleiben als begrenzte Diagnosen erhalten. Diese Aggregate und Heuristiken ergeben keine Publikationserlaubnis.

`expose_prepared_candidate` ist ein strikter Builder aus den konkreten Aggregat-Dataclasses, kein Parser beliebiger Kandidaten-Dictionaries und kein Validator für Review-/Veröffentlichungsstatus fremder Artefakte. Die Funktion prüft die verwendeten Aggregatformen, Float-Finitheit, Countidentitäten, gemeinsame Kategorien/Counts der vier Schätzungen, fehlendes Design/SE, Missing-/Nichtgestelltenkonsistenz, berechnete Differenzen und den zu den Counts passenden Status. Ein externes Dictionary mit Zusatzfeldern oder behauptetem published-Status wird nicht kopiert. Ein formal konsistent selbst gebautes Dataclassobjekt ist dadurch weiterhin kein authentifiziertes Ergebnis; Root-Provenienz und Ergebnisreview bleiben notwendig.

Die feste Kandidaten-Allowlist lautet:

| Ebene | Erzeugte Felder |
| --- | --- |
| Gesamtobjekt | `schema='policy-reference-candidate-v2-wip'`, `study_id`, `edition`, `questions` |
| Jede Frage | `source`, `status`, `category_counts`, `primary_accounting`, `missing_reasons`, `not_asked`, `reference` |
| `source` je Frage | `study_id`, `edition`, `question_id` aus dem gebundenen Vertrag |
| `category_counts` | `code`, `count` für jede ursprüngliche gültige Kategorie in Originalreihenfolge |
| Jedes Accounting | `total_count/total_weight`, `eligible_count/eligible_weight`, `valid_count/valid_weight`, `missing_count/missing_weight`, `not_asked_count/not_asked_weight` |
| Missing-Reason | `reason`, `count`, `primary_weight_sum` |
| Nichtgestellt | `count`, `primary_weight_sum` |
| Nicht-null `reference` | `variance_status='no_design_basis'`, `estimates`, `sensitivity`, `anweight_equivalence_diagnostic` |
| `estimates` | Genau die Schlüssel `pspwght`, `dweight`, `unweighted`, `anweight`; jeweils `role`, `accounting`, `categories` |
| Geschätzte Kategorie | `code`, `count`, `weight_sum`, `proportion` |
| `sensitivity` | `max_abs_primary_unweighted`, `max_abs_primary_dweight` |
| `anweight_equivalence_diagnostic` | `max_abs_primary_anweight`, `ratio_scope='all_de_cases'`, `anweight_pspwght_ratio_min`, `anweight_pspwght_ratio_max` |

Der JSON-kompatible Kandidat ist eine neue, vom privaten Objekt getrennte Struktur. Änderungen am zurückgegebenen Dictionary ändern weder die private Aufbereitung noch einen später neu gebauten Kandidaten. Es werden keine Raw-/Personen-/Designfelder, Parteifarben, Polungen oder beliebigen Metadaten übernommen. Ausgegeben werden ausschließlich die genannten Kennungen, ursprünglichen gültigen Kategoriecodes, gebundenen Reason-Beschreibungen und Aggregate.

Für Floatkonsistenz ist vorab eine feste `ARITHMETIC_TOLERANCE=1e-12` festgelegt: `fsum` der gültigen Proportionen muss höchstens diesen absoluten Betrag von 1 abweichen; Gewichtsidentitäten und Quotienten werden relativ mit derselben Toleranz und ohne absoluten Offset geprüft. Das begrenzt Float-Rundung, nicht empirische Unterschiede oder die Darstellungsentscheidung. Proportionen müssen endlich in `[0,1]` liegen. Kategoriecounts müssen exakt zum gültigen Count aufsummieren; Missing-/Nichtgestellten- und Gesamtcounts müssen exakt zu ihrem Accounting passen. Es findet keine Nachnormalisierung oder Rundung auf Prozentwerte statt.

Die synthetischen Handorakel sind fest formuliert, keine aus dem eigenen Algorithmus erzeugten Erwartungswerte. Bei 100 Fällen mit 30/70 gültigen Kategorien und Primärgewichten 2/1 sind die gültigen Primärsummen 60 und 70: der erste Anteil ist `6/13`. Mit `dweight` 1/2 sind die Summen 30 und 140: `3/17`. Ungewichtet ist der Anteil `3/10`. Mit `anweight` 4/2 sind es 120 und 140: ebenfalls `6/13`. Der dritte deklarierte ursprüngliche Kategoriecode bleibt mit Nullcount und Nullanteil erhalten. Die festen maximalen Unterschiede sind `21/130` gegenüber ungewichtet, `63/221` gegenüber `dweight` und null gegenüber `anweight`; die Verhältnisextrema sind 2/2. Gleichheit hier ist nur die ausdrücklich synthetische Arithmetik, kein bestandenes Äquivalenzkriterium.

Ein zweites `anweight`-Orakel verwendet gültige Summen 90 und 280: `9/37`, mit maximaler Primärdifferenz `105/481`. Ein Missing-Fall und ein nichtgestellter Fall setzen die all-DE-Verhältnisextrema auf `1/4` und 10, ohne den gültigen Anteilsnenner zu verändern. Das prüft sowohl eine abweichende Diagnose als auch ihren tatsächlich vorgesehenen Metadatennenner.

Weitere feste Erwartungen prüfen 99 statt 100 gültige Fälle, positive Zellcounts 4 versus 5 und Nullcounts, vollständig fehlende gültige Antworten, mehrere Missing-Codes mit gleichen und getrennten Reasons, zwei Fragen mit gültigen Primärnennern 130 versus 90, getrennte Studien mit wiederholten Personen-/Fragenkennungen, unverwendete komplette und unvollständige Designkennungen, exakte Kategorien-/Gewichtsmetadatenreihenfolge, unveränderte Fraction-Ergebnisse bei gemeinsamer Gewichtsskalierung `0.25`, `3`, `1e-200`, `1e200` und bei Fallpermutation. Kandidaten-Allowlist, fehlende private Felder, eingefrorene Aufbereitung, getrennte Builderkopien, unbekannte/fabrizierte Payloads, fingierter Release-/Darstellungsstatus und nichtendliche Aggregate sind als Fehlergrenzen enthalten.

Der einzige Testlauf dieses Auftrags war:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest pipeline.tests.test_policy_analysis_v2 -v
```

Beginn: `2026-10-03T13:23:22.790874+00:00`, Ende: `2026-10-03T13:23:22.911092+00:00`. Wrapper-PID `2673818`, Test-PID `2673819`; das Kind wurde vollständig abgewartet. Ergebnis: 16 Tests bestanden, Exit 0. Der Testlauf importierte nur das neue gezielte Testmodul und die ausdrücklich erlaubten lokalen Bibliotheken samt Standardbibliothek. `PYTHONDONTWRITEBYTECODE=1` galt für diesen Prozess. Der echte Ausgabemitschnitt liegt in `outputs/loop/policy-analysis-v2/synthetic-unittest.log`; Aufruf, Zeitpunkte, PIDs und Exitcode liegen in `synthetic-unittest-run.json`. Kein Server oder eigener Hintergrunddienst wurde gestartet, kein fremder Prozess gesteuert.

Die Vorab-Pinkontrolle hatte PID `2636303`, UTC-Marker `2026-10-03T13:17:41.520470+00:00`, Exit 0. Sie bestätigte insbesondere die freigegebenen Bibliothekspins. Die Nachher-Codekontrolle hatte PID `2688566`, Marker `2026-10-03T13:25:32.479098+00:00`, Exit 0. Alle zwölf vorher gepinnten Bestandsdateien waren bytegleich:

| Bestandsdatei | Unveränderter SHA-256 |
| --- | --- |
| `pipeline/policy_reference_v2.py` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/tests/test_policy_reference_v2.py` | `01ddfaa79b3fedf1cc10d79b547a38622827fa218a29bd921f896e39568d5ad8` |
| `pipeline/policy_adapter_v2.py` | `3159243bc6f536359c896e414e8f418955b51e7504e38f3add62a811b0e5500e` |
| `pipeline/tests/test_policy_adapter_v2.py` | `43759f87d216d5c0f1c1ae28db60cf640b680f09913a56c8b0cd0c126ce5f829` |
| `web/src/app/research/policy-profile.ts` | `28906eb1533bb953b43bed75a4995c907b71398f1ffcd63271c82cfdace05998` |
| `web/src/app/research/policy-profile.spec.ts` | `6b2b3302afe308f28f65ec9aba76c7f1b8b6d14bf9ffa9b8fbc6508f9a1c22c1` |
| `reports/loop/authors/BREADTH-TOPICS-001-first.md` | `f9dfe17df6795d0a7b82918c5d956421645249036e3ee22257a88a1044d58f5b` |
| `reports/loop/authors/POLICY-REFERENCE-V2-WIP.md` | `32bb7cc12e0f4f9437e80e7d2fe9ad6aff26a7ab95b3f14b957a06c9111c910a` |
| `reports/loop/authors/POLICY-REFERENCE-V2-round1-WIP.md` | `97b90a494440388afb322bc11b6f53e84668ee1265317d67ea8dd6822ceb493e` |
| `reports/loop/authors/POLICY-PROFILE-WIP.md` | `f9c6e925472ef89e1cb74f3208b3954aa52a330bd464a5ba2bb8b137757f175f` |
| `reports/loop/authors/POLICY-ADAPTER-WIP.md` | `86b590f1cad8bd75a4b0eee4323afda2f91b0af4687ab67002300b5baa9bc3d5` |
| `reports/loop/authors/POLICY-PROFILE-round1-WIP.md` | `096b94ec16532bcf19b74b59996f48444251c873e02b1d4e936b59db62ad416c` |

Vorher-/Nachher-Pins sind in `pins-before.json` und `pins-after-code.json` im eigenen Outputordner gespeichert. Der abschließende Evidenzprozess ergänzt die neuen Codepins und diesen unveränderten Erstbericht. Die Bibliothek selbst erstellt keinerlei Datei oder Exportartefakt.

Offen bleiben die echte Studienprovenienz, genaue Datei/Edition/Hashbindung, Originalfragen und Fragekontext, Rechte/Lizenzen, Population-/Eligibility-/Missingbegründung, quellspezifische Gewichte und Filter, vollständige Surveybasis, unabhängige technische Prüfung, tatsächlicher v2-Plan/Gates, Ergebnisreview und jede Export-/Produktentscheidung. Ein Editionsstring oder ein typkorrektes Parserobjekt bestätigt diese Voraussetzungen nicht. Es gab keinen tatsächlichen Import, keine Empirie, keine Einstellungs-/Fragenentscheidung, keinen Netz-/Auth-/Claude-/Git-/pnpm-/Installations-/Server-/Agentenlauf und keinen Gesamtcheck. Synthetische Tests und dieselbe Codex-Modellfamilie liefern keine methodische oder menschliche Freigabe.
