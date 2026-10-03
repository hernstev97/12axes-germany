# Korrekturrunde 1, GROUP-RESULTS-V21-001, Methoden und Reproduzierbarkeit

Rolle: `methods_reproducibility`. Urteil zur gezielt korrigierten Fassung: `ACCEPTED_BOUNDED`. GR21-M-001 ist geschlossen. Diese Korrekturrunde ist keine neue Erstbewertung und kein Gesamtaudit der unveränderten v2-Auswahl. Mein ursprünglicher Erstbericht und dessen damaliger `NOT_ACCEPTED`-Entscheid bleiben bytegenau erhalten.

Neue feste Prüffassung: `reports/loop/packages/GROUP-RESULTS-V21-001/v2/manifest.json`, SHA-256 `47aa3e3f3cf6043cc81bf25bf6b1228bc007f4a12c3e2866337d91161f114382`. Tatsächlich geändert sind ausschließlich `pipeline/policy_group_export_v21.py` und `pipeline/tests/test_policy_group_export_v21.py`. Die übrigen 62 öffentlichen Pins und alle drei tatsächlichen privaten Aggregatpins entsprechen der Erstfassung. Resultatscope bleibt ausschließlich `ESS5e03_6`, `ESS8e02_3`, `ESS9e03_3`.

## GR21-M-001: gezielt geschlossen

`pipeline/policy_group_export_v21.py:254` berechnet jetzt den nach `yes+valid-party` und `yes+NotAsked` verbleibenden Yes-Rest. Die anschließende Prüfung verlangt genau die fehlende notwendige gemeinsame Machbarkeitsbedingung:

```text
0 <= vote_yes - eligible_group_cases - yes_party_not_asked
   <= party_source_missing + party_technical_blank
```

Mein ursprünglicher ausschließlich synthetischer Gegenfall wird nun mit dem statischen Fehler `invalid_candidate` zurückgewiesen. Die neue Prüfung bewahrt die Trennung der zwei Zustandsachsen und fügt sie nicht als disjunkte Gesamtkategorien zusammen.

Mein unabhängiger synthetischer Gegencheck zählt mögliche Belegungen der Yes-Zeile für die Missing- und Blank-Spalten auf. Er berechnet das Sollurteil durch Existenz einer zulässigen gemeinsamen Belegung, ohne die Produktions-Restungleichung als Sollfunktion aufzurufen. Die 1920 ausschließlich synthetischen Fälle umfassen leere und besetzte Gruppen, negative Reste, fehlende Kapazität, Nullreste, beide Kapazitätsgrenzen, zulässige Teilbelegungen, Party-NotAsked sowie die drei ursprünglichen Source-Missing-Gründe. Alle Erwartungen stimmen mit der korrigierten Prüfung überein. Reine Missing-, reine Blank- und gemischte zulässige Reste bleiben erlaubt.

Die 38 aktuellen Exporter-Tests bestehen. Die unveränderten Gruppen-/Zugriffstests aus dem Erstbericht wurden in dieser gezielten Runde nicht erneut ausgeführt; ihre damals berichtete synthetische Evidenz bleibt erhalten. Synthetische Fallzahlen sind keine tatsächlichen ESS-Gruppenbasen.

## GR21-M-002: tatsächliche sichere Aggregate erneut nachgerechnet

Das eigene Decimal-Orakel wurde für die neue Manifestbindung erneut ausgeführt. Es liest ausschließlich die drei ausdrücklich zugelassenen geschlossenen Aggregatdateien und nutzt für sein Rechenurteil keine Pipeline-Prüffunktion. Alle einzeln geprüften Studien-/Gruppen-/Fragepaare bestehen erneut die aus Aggregaten überprüfbaren Rechnungen und Invarianten aus GR21-M-002, einschließlich der stärkeren gemeinsamen Eligibility-Machbarkeit.

Die vier Gewichtsvarianten, ursprünglichen Kategorien und echte Nullzellen, feste 100/5-Regeln, jeweilige Frage-Nenner, Missing-/NotAsked-Partitionen, getrennte Eligibility-Achsen, Gruppen-/Frageninventare, Sensitivitäten und `all_eligible_group_cases`-Bindung bleiben rechnerisch konsistent. Quellen, Verträge, Schwellen und Paarregeln sind unverändert. Der korrigierte Kandidatenvalidator akzeptiert zusätzlich alle drei tatsächlichen sicheren Kandidaten. Diese Implementierungsprüfung bleibt vom unabhängigen Rechenorakel getrennt.

Numerische QA liegt ausschließlich in `outputs/loop/group-results-v21-methods/round1-aggregate-oracle-results.json`. Der synthetische Prüfer liegt in `outputs/loop/group-results-v21-methods/round1_targeted_probes.py`. Keine tatsächlichen Anteile, kleinen Zellzahlen, Gruppenbasen, Gewichtssummen, Ratios oder Personeninformationen stehen im öffentlichen Bericht.

## GR21-M-003 und GR21-M-004: Bindungen und Grenzen fortgeführt

Manifest und sämtliche tatsächlichen öffentlichen und privaten Pins wurden am Anfang und abschließend geprüft. Die drei Aggregatbytes, vollständigen Inventare, Studien-/Edition-/Kandidatenbindungen und die zuvor geprüften Ausführungsbindungen sind unverändert. Die neue Pure Exportbibliothek und ihre synthetischen Tests entsprechen ihren neuen Pins. Beide ursprünglichen eigenen Reviewdateien bleiben unverändert.

Kein tatsächlicher Rohdatenpfad wurde gelistet, stattiert, geöffnet, gehasht, auf Header geprüft oder ausgeführt. Keine andere Datei unter `data/local` wurde gelesen. Kein tatsächlicher Gruppenlauf oder tatsächlicher Public Export wurde gebaut. Es gab keine Git-, Netz-, Auth-, Installations-, Server-, Kontakt- oder Claude-Aktion. Keine andere Reviewerprosa, Autorenverteidigung oder Koordinationsdatei wurde gelesen. Die gebundenen Vorzugriffsberichte wurden wiederum ausschließlich als Bytes gehasht.

Dieses Urteil bestätigt weiterhin interne Aggregatarithmetik und Bytebindungen. Individuelle Gewichte, individuelle Ratioextrema, die Vergleichsbasis gegen den ersten individuellen Ratio, individuelle Gruppenzuordnung und Downloadprovenienz sind aus den sicheren Aggregaten nicht unabhängig bewiesen. Es erfolgte keine unabhängige Rohdaten-/Downloadreproduktion. Darstellungsheuristiken wurden nicht als Präzisions- oder Anonymitätsvalidierung ausgegeben.

## GR21-M-005: ausdrücklich begrenzte Paarfreigaben

Ich genehmige aus Sicht dieser Methodenrolle genau die einzeln bezeichneten Paare im neuen `GROUP-RESULTS-V21-001-methods-round1-decision.json`. Die folgende Liste ist dieselbe ausdrücklich beschlossene Zuordnung. Sie entstand aus den erneut geprüften Einzelrechnungen und meinem konkreten Rollenurteil, nicht durch Übernahme von `prepared`-Statusfeldern oder einer Rootliste. Alle nicht genannten Paare erhalten keine Methoden-Publikationsfreigabe. Alle benannten Gruppen und das heterogene Other bleiben im Inventar; ihre wissenschaftliche Einordnung oder politische Kategorie wurde nicht als zusätzlicher Auswahlfilter benutzt.

| groupId | Genehmigte questionIds |
| --- | --- |
| `ESS5e03_6:second_vote:1` | `ESS5e03_6:bplcdc`, `ESS5e03_6:hrshsnta`, `ESS5e03_6:dbctvrd`, `ESS5e03_6:rgbrklw` |
| `ESS5e03_6:second_vote:2` | `ESS5e03_6:bplcdc`, `ESS5e03_6:dpcstrb`, `ESS5e03_6:hrshsnta`, `ESS5e03_6:dbctvrd`, `ESS5e03_6:lwstrob`, `ESS5e03_6:rgbrklw` |
| `ESS5e03_6:second_vote:3` | `ESS5e03_6:dpcstrb`, `ESS5e03_6:hrshsnta`, `ESS5e03_6:dbctvrd`, `ESS5e03_6:lwstrob`, `ESS5e03_6:rgbrklw` |
| `ESS5e03_6:second_vote:4` | `ESS5e03_6:dbctvrd`, `ESS5e03_6:rgbrklw` |
| `ESS5e03_6:second_vote:5` | `ESS5e03_6:bplcdc`, `ESS5e03_6:hrshsnta`, `ESS5e03_6:dbctvrd`, `ESS5e03_6:rgbrklw` |
| `ESS8e02_3:second_vote:1` | `ESS8e02_3:bnlwinc`, `ESS8e02_3:eduunmp`, `ESS8e02_3:inctxff`, `ESS8e02_3:sbsrnen`, `ESS8e02_3:banhhap`, `ESS8e02_3:imsclbn`, `ESS8e02_3:wrkprbf` |
| `ESS8e02_3:second_vote:2` | `ESS8e02_3:gvslvue`, `ESS8e02_3:bnlwinc`, `ESS8e02_3:eduunmp`, `ESS8e02_3:inctxff`, `ESS8e02_3:sbsrnen`, `ESS8e02_3:banhhap`, `ESS8e02_3:imsclbn`, `ESS8e02_3:wrkprbf` |
| `ESS8e02_3:second_vote:3` | `ESS8e02_3:bnlwinc`, `ESS8e02_3:eduunmp`, `ESS8e02_3:inctxff`, `ESS8e02_3:banhhap`, `ESS8e02_3:imsclbn`, `ESS8e02_3:wrkprbf` |
| `ESS8e02_3:second_vote:4` | `ESS8e02_3:bnlwinc`, `ESS8e02_3:eduunmp`, `ESS8e02_3:inctxff`, `ESS8e02_3:banhhap` |
| `ESS8e02_3:second_vote:5` | `ESS8e02_3:bnlwinc`, `ESS8e02_3:eduunmp`, `ESS8e02_3:inctxff`, `ESS8e02_3:banhhap`, `ESS8e02_3:wrkprbf` |
| `ESS9e03_3:second_vote:1` | `ESS9e03_3:sofrdst`, `ESS9e03_3:sofrprv` |
| `ESS9e03_3:second_vote:2` | `ESS9e03_3:sofrdst`, `ESS9e03_3:sofrprv` |
| `ESS9e03_3:second_vote:3` | `ESS9e03_3:sofrdst` |
| `ESS9e03_3:second_vote:4` | `ESS9e03_3:sofrdst` |
| `ESS9e03_3:second_vote:5` | `ESS9e03_3:sofrdst`, `ESS9e03_3:sofrwrk`, `ESS9e03_3:sofrprv` |
| `ESS9e03_3:second_vote:6` | `ESS9e03_3:sofrdst`, `ESS9e03_3:sofrwrk`, `ESS9e03_3:sofrprv` |

Die Freigaben betreffen ausschließlich historische, getrennte kategoriale Antworten derselben Studie nach erinnerter Bundestags-Zweitstimme. Sie autorisieren keine aktuellen Parteipositionen, Normen, Scores, Konfidenzintervalle, Personen-/Studienkombination, Wahlprognose oder wissenschaftliche Güteaussage. Das Hauptproduktziel mit 43 Originalfragen und acht Themen wird durch diese optionale Gruppendeskription nicht ersetzt.

Die vollständige tatsächliche Rootannahme mit authentischen Reviewerberichten und ausdrücklicher Paarbindung muss außerhalb der Pure API gesondert entstehen. Formale synthetische Decision-/Reviewerstrings sind dafür kein Beleg. Die getrennte Quellen-/Konstrukt-/Fairnessrolle wird hier nicht vertreten. Beide Rollen gehören zur selben Codex-Familie und können gemeinsame Fehler teilen. Menschliche Annahme, Claude-Kontrolle und Release-/Merge-/Deploymentfreigabe sind nicht erteilt.

Nur dieser neue Bericht, der neue eigene Entscheid und eigene ignorierte QA wurden geschrieben. Allgemeines `pnpm check` und UI-Prüfungen wurden in dieser ausschließlich begrenzten Reviewrunde nicht ausgeführt. Der QA-Ordner bleibt über `outputs/` ausgeschlossen, mit 0700 für Ordner und 0600 für Dateien.

Abschließend: neue Manifestbytes, sämtliche gemeinsamen öffentlichen Pins, alle drei tatsächlichen privaten Aggregatpins und beide ursprünglichen eigenen Reviewdateien unverändert bestätigt.
