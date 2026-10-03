# KI-Audit der Recherche zu LIFE-93

Abgeschlossen am 2026-10-03. Fünf echte Erstprüfer und ein anschließend gestarteter Juror haben gearbeitet. Die begrenzten Korrekturen sind bestätigt; wesentliche Anforderungen an spätere Messungen bleiben offen. Dieser Ordner dokumentiert ein KI-Audit. Es ist kein akademisches Peer Review und keine Garantie wissenschaftlicher Gültigkeit.

## Ausgangsfassung

Die [aktuelle Issue-Beschreibung](issue-LIFE-93.md) wurde live über Linear gelesen. Der API-Stand ist `2026-10-02T22:07:24.510Z`. Das [unveränderte API-Objekt](issue-LIFE-93.json) bleibt erhalten.

Die [Ausgangsfassung](ausgangsfassung/docs/project.md) umfasst 26 Dateien. [ausgangsmanifest.json](ausgangsmanifest.json) verzeichnet ihre SHA-256-Prüfsummen, den Foundation-Commit `1a7b0c38f28e27219d59380c039f9bb0446a71dd` und die Hashes von Issue und gemeinsamem Erstauftrag. Die 18 Hashes des bisherigen Forschungsmanifests wurden vor dem Kopieren verifiziert. Rohdaten wurden nicht kopiert. Schreibschutz schützt die Kopien gegen versehentliche Änderungen; gemeinsame Benutzerrechte erlauben technisch eine Aufhebung.

Die ursprüngliche Recherche enthält Quellenbefunde und Verfahrensentwürfe. Ein Frageninventar, empirische Modellbefunde und Ergebnisse eines Webtests liegen noch nicht vor.

## Tatsächliche Agent-Aufträge

[agent-protokoll.json](agent-protokoll.json) enthält die tatsächlichen Spawn-Aufträge im Wortlaut, zurückgegebene Task-Namen, zugängliche Modellinformationen und Berichtshashes. [pruefauftrag-gemeinsam.md](pruefauftrag-gemeinsam.md) ist die gemeinsame Prüfgrundlage. [werkzeuge.json](werkzeuge.json) verzeichnet die angebotenen Werkzeuge des Hauptagenten; die Reviewer berichten ihre eigene Werkzeugnutzung.

Das Tool erlaubt insgesamt vier gleichzeitig aktive Agents einschließlich Hauptagent. Die fünf Erstprüfer wurden deshalb in zwei Wellen mit höchstens drei gleichzeitig laufenden Reviewern gestartet. Alle Erstprüfer erhielten dieselbe gesicherte Forschungsfassung und separate Kontexte ohne Gesprächshistorie. Sie durften die anderen Berichte nicht lesen und nur ihren eigenen Bericht schreiben. Diese Trennung beruht auf Aufträgen und getrennten Gesprächen, nicht auf einer nachgewiesenen Dateisandbox.

Alle Agents erben laut zugänglicher Laufzeit GPT-6.1-Sol, `gpt-6.1-sol`. Interne Modellversionen und nicht zugängliche Anbieter-Vorgaben sind unbekannt. Unterschiedliche Modellfamilien werden nicht behauptet; Übereinstimmung beweist keine Wahrheit oder Neutralität.

Die Autorentscheidung begann erst nach Abschluss aller fünf Erstberichte. Danach prüfte der sechste Agent als Juror Ausgangsfassung, Erstberichte, Autorentscheidungen und Korrekturfassung. Während seiner Prüfung blieben diese Eingaben unverändert.

| Tatsächlicher Subagent                 | Auftrag und eigener Bericht                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------- |
| `/root/reviewer_1_quellen`             | [Quellen, Tatsachen und Rechte](reviewer-1-quellen.md)                        |
| `/root/reviewer_2_politikwissenschaft` | [Politikwissenschaft und Deutschlandbezug](reviewer-2-politikwissenschaft.md) |
| `/root/reviewer_3_statistik`           | [Messmethodik und Statistik](reviewer-3-statistik.md)                         |
| `/root/reviewer_4_neutralitaet`        | [Neutralität und Modellverhalten](reviewer-4-neutralitaet.md)                 |
| `/root/reviewer_5_reproduzierbarkeit`  | [Nachprüfbarkeit und Reproduzierbarkeit](reviewer-5-reproduzierbarkeit.md)    |
| `/root/juror_6`                        | [Unabhängige Nachprüfung der Entscheidungen und Korrekturen](juror-6.md)      |

„Unabhängig“ bezeichnet hier getrennte Aufträge und Kontexte. Alle sechs nutzten dieselbe angegebene Modellfamilie. Gemeinsame systematische Fehler bleiben möglich. Die in LIFE-93 vorgesehene andere Modellfamilie und methodische Gesamtfreigabe sind damit nicht nachgewiesen.

## Einzelentscheidungen und Korrekturen

[finding-entscheidungen.json](finding-entscheidungen.json) dokumentiert alle 14 Reviewerfindings und eine zusätzliche eigene Prozesskorrektur A-F01 mit Annahmeentscheidung, Begründung, Belegen, geänderten Stellen und Nachprüfung. R5-F01 und R5-F02 wurden teilweise angenommen; die übrigen 12 Reviewerfindings wurden angenommen. Kein Reviewerfinding wurde verworfen. Viele Findings sind Anforderungen an noch nicht vorhandene Modelle, keine nachgewiesenen empirischen Fehlbefunde.

Die nachvollziehbaren Korrekturen sind:

- **R1-F01:** Die pauschale Warnung vor älteren ESS-Ausgaben wurde eingeschränkt. Die deutsche `stratum`-Korrektur ist für 3.0 → 4.0 belegt. Die späteren Versionshinweise belegen keine generelle deutsche Untauglichkeit von 4.0/4.1. Fehlende Änderungseinträge beweisen auch keine Dateigleichheit. Die aktuelle Ausgabe 4.2 bleibt die recherchierte Ausgangskandidatin.
- **R4-F01 und R2-F02:** Parteibezug umfasst auch Parteien allgemein sowie Einleitungen und Filter. „Parteibenannt“ war dafür zu eng oder mehrdeutig. Forderungen, Wahrnehmungen, Bewertungen, Vertrauen und Wertprioritäten müssen bei der späteren Itemprüfung unterschieden werden. Noch wurde kein Item aufgenommen oder entfernt.
- **R2-F03/F04 und R3-F01–F04:** Die Regeln benennen jetzt Konstruktbreite, unipolare Bedeutung, die bedingte Auswertung relativer Wertprioritäten, beobachtete statt automatisch latente Zielgrößen, konkrete Antwortmasken, Itemdominanz und gemeinsame Schätzabhängigkeiten. Die jeweiligen Methoden und empirischen Nachweise sind weiterhin offen.
- **R4-F02 und R5-F03:** Vergleichstexte brauchen tatsächlich vergleichbare Inhalte. Persönliche Messunsicherheit, Referenzstichprobenunsicherheit und Unterschiede zwischen vertretbaren Modellentscheidungen haben getrennte Zielgrößen und Bedeutungen. Textmetriken, simulierte Perspektiven und Modellvarianten sind keine Neutralitäts- oder Messfehlernachweise.
- **R5-F01/F02:** Vorhandene historische Browserartefakte wurden mit Hashes registriert; zentrale aktuelle dynamische Quellen wurden datiert gesichert. Damit werden fehlende historische Laufprotokolle oder alte Seitenstände nicht nachträglich bewiesen. Eine neue technische Wiederholung hat ihren eigenen Prüfzeitpunkt.
- **A-F01:** Die eigene zusätzliche pauschale Startbedingung wurde präzisiert. Das Issue verlangt keine persönliche Statistik-Abnahme durch Steven. Auch der alte Plan benannte keinen persönlichen Freigebenden. Die Korrektur betrifft deshalb die eigene zu breite Auslegung; vollständiger Plan, Tags, Setup, getrennte Erstbewertungen, Phase-1-Artefakte und notwendige Reviews bleiben erforderlich.

Die [Korrekturfassung](korrekturfassung/docs/project.md) umfasst 28 gesicherte Dateien. [korrekturmanifest.json](korrekturmanifest.json) verbindet ihre Hashes mit Ausgangsfassung, fünf Erstberichten und den Autorentscheidungen. Die Ausgangsfassung bleibt erhalten. Beide Fassungen sind lokale Momentaufnahmen; sie ersetzen keine öffentliche Präregistrierung.

| Gesicherter Bezug   | SHA-256                                                            |
| ------------------- | ------------------------------------------------------------------ |
| Ausgangsmanifest    | `dab36982ce6aac113acc2f807611e8630b546ee451684d683a096e0b4fd23cd8` |
| Korrekturmanifest   | `c6fef40eff714e5e15bdf045c6e46f92b2e14bddda14a24148e56349c2439406` |
| Autorentscheidungen | `e4703993a389d19144b60623c92ac4690b008774b37f57fec124fa16656b63fc` |
| Jurorbericht        | `6beed214a6c22551317ed3e2aefcac92d33d7930d5545c4dd0649a3f1754ccd8` |

## Jurorurteil und offene Grenzen

Der Juror kontrollierte alle 15 Entscheidungen, beide Fassungen und zentrale Originalfundstellen selbst. Besonders geprüft wurden die teilweise angenommenen historischen Findings, die Prozesskorrektur A-F01, die Versionseinträge, Parteibezug-Grenzfälle und neue tragende Methodenquellen. Er bestätigt die begrenzten Korrekturen und fand keinen zusätzlichen belegten erheblichen Fehler im aktuellen Rechercheentwurf. Er erteilte keine wissenschaftliche Gesamtfreigabe und keine Phase-0-Abnahme. Seine Einschränkungen zu A-F01 und zur analytischen Herleitung bei Tse et al. bleiben verbindlich.

Quellen zu ESS-Ausgabe, Erhebung, Dokumentation und Nutzung stützen die jeweils begrenzten Aussagen im Belegregister. Die theoretische Kandidatenliteratur ist noch kein vollständiger Deutschland-Themenrahmen. Nicht zugängliche Volltexte bleiben unvollständig geprüft. Historische Quellenstände und vollständige ursprüngliche Ausführungsprotokolle sind teilweise nicht rekonstruierbar. Authentizität des ursprünglichen Rohdatendownloads und konkrete Veröffentlichungsrechte jedes späteren Artefakts sind nicht abschließend nachgewiesen.

Offene erhebliche Anforderungen blockieren die jeweils darauf aufbauende Aussage oder Funktion:

| Finding | Bis zur tatsächlichen Klärung blockiert                                                                |
| ------- | ------------------------------------------------------------------------------------------------------ |
| R2-F03  | Breite oder bipolare politische Interpretation ohne ausreichende Konstrukt- und Itembelege             |
| R3-F01  | Konstruktbezogene Gruppenvergleiche ohne passende ordinale Vergleichsvoraussetzungen                   |
| R3-F02  | Teilantwort-Perzentile ohne begründete zulässige Itemmasken und dazu passende Normen                   |
| R3-F04  | Reliabilitätsbehauptungen und persönliche Messbereiche ohne zum ausgegebenen Score passendes Verfahren |
| R5-F03  | Unsicherheitsanzeige ohne getrennte Herkunft, Zielgrößen und tragfähige Verfahren                      |

Auch der vollständige Fragenkatalog, die Deutschland-Themenabdeckung, konkurrierende Erwartungen, konkrete Planparameter und die erforderlichen getrennten Erstbewertungen fehlen. Keine Dimension, Norm, Wählergruppen-Distanz oder Ergebnisbeschreibung ist empirisch validiert. Keine politische Bevorzugung wurde belegt; daraus folgt kein Neutralitätsnachweis.

## Tatsächlich ausgeführte Nachprüfungen

| Prüfung                                                                                                    | Tatsächliches Ergebnis und Grenze                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Korrekturprüfung](04-korrekturpruefung.json)                                                              | Ausgeführt und bestanden: formale Korrekturbedingungen, Quellen-/Protokollbezüge, Schema, Hashes und dokumentierte Gegenrechnungen. Kein empirischer Methodenpass.                                   |
| [Synthetische Gegenbeispiele](synthetische-gegenbeispiele.log)                                             | Vom Reviewer gerechnet, vom Autor und Juror erneut ausgeführt; identischer Outputhash. Belegen konkrete mögliche Probleme, validieren keine Lösung.                                                  |
| [Technischer Lauf vor dem Juror](technische-pruefung.json)                                                 | `pnpm check`, Exit 0: Format, Typprüfung, zwei bestehende UI-Tests und Angular-Build. Eigener neuer Lauf mit dokumentiertem Eingabestand.                                                            |
| [Eigenständige Jurorkontrollen](juror-unabhaengige-pruefung.json.log)                                      | 21 dokumentierte Bedingungen bestanden. Der Juror prüfte zusätzlich Originalfundstellen, wiederholte Gegenrechnungen und validierte das Konfigurationsschema.                                        |
| [Späterer technischer Jurorlauf](juror-technische-pruefung.json.log)                                       | Exit 1 im Formatcheck für die neu angelegte Auditdatei `06-korrekturfassung-unchanged.json`. Typprüfung, Tests und Build liefen in diesem Lauf nicht. Der frühere erfolgreiche Lauf bleibt erhalten. |
| [Abschließender technischer Lauf](technische-pruefung-abschluss.json)                                      | Wiederholung nach Formatkorrektur und Wiederherstellung der eingefrorenen Ignorekonfiguration; maßgeblich sind der dokumentierte Exitcode und das vollständige Laufprotokoll.                        |
| [Abschlussintegrität](07-abschlusspruefung.json) und [zusätzlicher Hashabgleich](08-abschluss-hashes.json) | Erneute Kontrolle geschützter Eingaben, Forschungsfassungen, Entscheidungen und aller sechs Berichte. Inhaltliche Richtigkeit folgt nicht aus Hashgleichheit.                                        |

Die archivierten Fassungen und abgeschlossenen Agent-Berichte werden vom automatischen Formatierer ausgenommen, damit ihre Hashes erhalten bleiben. Sie zählen dadurch nicht als neu formatgeprüft. [juror-belegregister.json](juror-belegregister.json) dokumentiert die unverändert aus dem temporären Jurorordner übernommenen Laufbelege. [quellenbelege.json](quellenbelege.json) und [historische-belege.json](historische-belege.json) nennen die gesicherten lokalen Quellen und vorhandenen früheren Artefakte samt Grenzen. Lokale Quellenkopien liegen im Git-ausgeschlossenen `outputs/`.

Kein ESS-Antwortdatensatz wurde analysiert, kein Split oder Modell erzeugt, kein CodeRabbit-Review ausgeführt und keine geänderte Weboberfläche neu im Browser geprüft. Technische Checks schließen die offenen fachlichen Anforderungen nicht.

## Nächster durch die Belege gerechtfertigter Schritt

Den vollständigen deutschen Originalfragenbestand einschließlich Wortlaut, Antwortkategorien, Filtern und Antworttypen dokumentieren. Parallel den datierten Deutschland-Themenrahmen, konkurrierende Erklärungsmodelle und prüfbare Planparameter ausarbeiten. [docs/analyseanforderungen.md](../../docs/analyseanforderungen.md) hält die jetzt präzisierten Anforderungen fest. Diese öffentliche Quellenarbeit braucht keine zusätzliche persönliche Statistik-Abnahme; sie ersetzt keine erforderliche Gegenprüfung.

Erst nach tatsächlich erfüllten einschlägigen Voraussetzungen können Items und Erwartungen festgeschrieben und ESS-Analysen begonnen werden. Der heutige Stand rechtfertigt keine Datenanalyse, Entblindung oder Veröffentlichung eines validierten Tests. Änderungen und Auditbelege liegen lokal; dieses Audit hat keinen Commit, Push, PR oder Deployment ausgelöst.

## Ausgeführte Eingangsprüfungen

[00-eingangspruefung.json](00-eingangspruefung.json), [01-eingang-wiederholbar.json](01-eingang-wiederholbar.json) und [03-zwischenpruefung.json](03-zwischenpruefung.json) protokollieren Datei-/Hash- und Git-Ausschlussprüfungen. Alle dort aufgeführten Checks wurden ausgeführt und bestanden. Der Rohdatei-Hash stimmt mit dem Dateieingang überein; keine Antworten wurden für diese Prüfungen interpretiert.

Erneut ausführbar aus dem Repository:

```sh
python reports/audit-recherche/pruefe-audit.py --phase eingang --output reports/audit-recherche/eingang-neuer-lauf.json
```

Diese Prüfungen bestätigen Dateien und Protokollstruktur. Sie bestätigen weder Originaldownload-Authentizität noch vollständige Blindheit, Validität oder politische Neutralität. Wissenschaftliche Aussagen werden nach dem jeweils dokumentierten Prüfbereich beurteilt.

Der erste abschließende Hashlauf ([07-abschlusspruefung-erster-lauf.json](07-abschlusspruefung-erster-lauf.json)) meldete genau eine Abweichung: Der Autor hatte nach der Jurorprüfung zwei zusätzliche Format-Ausnahmen für kopierte Jurorbelege in `.prettierignore` ergänzt. Diese Änderung wurde zurückgenommen. Die ursprüngliche Korrekturfassung bleibt exakt erhalten; die Kopien tragen nun die Endung `.json.log`, wodurch ihre unveränderten Bytes auch ohne neue Ausnahme erhalten bleiben. Der erfolgreiche technische Lauf von 00:54 UTC ([technische-pruefung-final.json](technische-pruefung-final.json)) und seine damaligen Eingaben bleiben als eigener vorheriger Prüfstand erhalten. Der anschließend wiederholte Lauf und Hashabgleich beziehen sich auf den wiederhergestellten endgültigen Stand.
