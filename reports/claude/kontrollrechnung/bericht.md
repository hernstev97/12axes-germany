# Kontrollrechnung V1: unabhängige Nachrechnung der v2-Einzel- und v2.1-Gruppenreferenzen

Stand: 3. Oktober 2026, 19:20 UTC. Ausgangsstand: Branch `research/life-93-claude-20261003`, Commit `e9898fb423a3ba9fbe6387ed9215dbe83666aedc`. Erstellt von einem getrennten Claude-Subagenten im Auftrag `reports/claude/auftraege/V1-kontrollrechnung.vollstaendig.md`.

Dieser Bericht prüft den Rechenweg. Er ist keine methodische Validierung, keine Prüfung der Fragenauswahl, Konstrukte oder Neutralität und keine Veröffentlichungs- oder Releasefreigabe.

## Kurzfassung

- Eine eigene, einfache Implementierung (`kontrolle.py`, nur Python-Standardbibliothek) hat alle 43 Fragen und alle 174 Frage-Gruppen-Paare aus den fünf lokalen CSV-Dateien nach der Spezifikation neu berechnet. Den vorhandenen Rechencode habe ich erst gelesen, als die eigene Rechnung und der Vergleich fertig waren.
- Die 42 veröffentlichten Einzelreferenzen stimmen bis auf Gleitkommarundung überein: maximale absolute Abweichung eines Anteils 1,1e-16. Gleich sind auch Nennerbasis, Missing-Gründe samt Gewichtssummen, Gewicht aller deutschen Fälle, beide Sensitivitätsmaße und die anweight-Diagnose. `ESS10SCe03_2:cttresa` wird von beiden Rechnungen zurückgehalten, und zwar wegen der Zellregel, nicht wegen der Basisregel.
- Auch die 63 veröffentlichten Frage-Gruppen-Paare stimmen überein (maximal 1,1e-16; Nenner gleich). Die 111 zurückgehaltenen Paare tragen in beiden Rechnungen denselben Status; 70 scheitern an der Basisregel, 41 an der Zellregel. Die veröffentlichten Paare sind genau die Paare, die die 100/5-Regel bestehen.
- Befund zur Gewichtsdiagnose: Innerhalb Deutschlands ist `anweight/pspwght` nur in ESS11 innerhalb der Vertragstoleranz 1e-12 konstant. In ESS5, ESS8, ESS9 und ESS10-SC beträgt die relative Spannweite etwa 1,9e-7 bis 2,1e-7. Auf die Anteile wirkt sich das mit höchstens 8,9e-10 aus. Die veröffentlichten Dateien nennen Minimum und Maximum des Verhältnisses. Eine ausdrückliche Aussage, dass die im Plan angekündigte Konstanzprüfung bei 1e-12 nicht besteht, habe ich in meiner begrenzten Suche nicht gefunden.
- Stichprobendesign: ESS9, ESS10-SC und ESS11 enthalten `psu`, `stratum` und `prob` für alle deutschen Fälle und haben keine Strata mit nur einer PSU. ESS5 und ESS8 enthalten keine Designfelder und bräuchten eine zusätzliche SDDF-Datei.

## 1. Umfang und Reihenfolge

1. Ich habe zuerst nur die Spezifikation gelesen (19:04 bis 19:09 UTC): `docs/empirie-plan-v2.entwurf.md`, `data/analysevertrag.v2.entwurf.json`, `data/gruppenvertrag.v2.1.entwurf.json`, `data/politikprofil-v2.fragen.entwurf.json`, die ESS-Gewichtungsseite und den dort verlinkten Leitfaden. Für die Dateipfade habe ich außerdem `docs/reproduktion-life93-v2.md` gelesen, für das Dateiformat der Vergleichsdateien die beiden README-Dateien und die Schlüsselstruktur der Referenz-JSON-Dateien, aber ohne Zahlen.
2. Anschließend habe ich `reports/claude/kontrollrechnung/kontrolle.py` geschrieben, ausgeführt und mit den veröffentlichten Dateien verglichen. Erster vollständiger Vergleich: 19:11:43 UTC. Die erweiterten Diagnosen zu Gewichten und veröffentlichten Dateien liefen bis 19:13:40 UTC.
3. **Den vorhandenen Rechencode habe ich ab 19:13:47 UTC gelesen**, also nach Abschluss der eigenen Rechnung und des Vergleichs. Gelesen habe ich `scripts/run-policy-v2.py`, `scripts/run-policy-groups-v21.py`, `pipeline/policy_analysis_v2.py` und `pipeline/policy_adapter_v2.py` vollständig, aus `pipeline/policy_access_v2.py`, `pipeline/policy_groups_v21.py` und `pipeline/policy_export_v2.py` nur Ausschnitte und Suchtreffer.
4. Nach dem Codelesen habe ich am Skript nur Folgendes geändert (19:15 bis 19:16 UTC): sparsamere Terminalausgabe (siehe Abschnitt 11), eine zeilenweise Plausibilitätsprüfung der Filterführung `vote`/`party2`, den gruppenspezifischen Statusnamen aus dem Gruppenvertrag und eine Zusammenfassung je Frage in `vergleich.json`. Berechnung von Anteilen, Nennern, Missing-Gründen und Status blieb unverändert. Die Ausgaben zu Einzelfragen und Paaren waren vor und nach der Änderung zeichengleich.

Für die Gruppen habe ich nur ESS5, ESS8 und ESS9 gerechnet. Nur für diese Studien gibt es veröffentlichte Gruppendateien; der Gruppenrunner lässt laut `docs/reproduktion-life93-v2.md` (Abschnitt „Künftiger lokaler Datenlauf“) nur diese drei Studien zu, und `data/reference-groups-v21/README.md` nennt Quellenlücken als Grund für den Ausschluss von ESS10-SC und ESS11. Parteiangaben aus ESS10-SC und ESS11 habe ich nicht ausgewertet. Ob der Ausschluss sachlich richtig ist, habe ich nicht geprüft.

## 2. Tatsächlich verwendete Eingaben

Spezifikation (SHA-256 selbst berechnet):

| Datei | SHA-256 | Bindung |
| --- | --- | --- |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` | entspricht `catalog.sha256` im Analysevertrag |
| `data/analysevertrag.v2.entwurf.json` | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` | entspricht `references.analysisContract.sha256` im Gruppenvertrag und `studyContractSha256` der Gruppendateien |
| `data/gruppenvertrag.v2.1.entwurf.json` | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` | entspricht `groupContractSha256` der Gruppendateien |

`sourceContractSha256` in `data/reference-v2/*.json` ist der kanonische JSON-Hash (sortierte Schlüssel, kompakte Trennzeichen) des jeweiligen Studieneintrags im aktuellen Analysevertrag; alle fünf Werte habe ich nachgerechnet und gleich gefunden. Kategorien, Missing-Codes und nicht gestellte Codes im Katalog und im Analysevertrag stimmen für alle 43 Fragen überein.

CSV-Dateien. `data/raw/<ordner>` sind Symlinks auf `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003/data/raw/<ordner>`:

| Studie | Pfad | SHA-256 (selbst berechnet) | Bytes | Vertrag |
| --- | --- | --- | --- | --- |
| ESS5 3.6 | `data/raw/ess5-ed3.6/ESS5e03_6.csv` | `bd93e915c2033a43bc41328fc3f4df13278b8079f8e071f98a11770f25b4022e` | 69880337 | gleich |
| ESS8 2.3 | `data/raw/ess8-ed2.3/ESS8e02_3.csv` | `5112f64fd65df229e353c82ef0f3593b568654ea76f854639f6527bca8db3684` | 47692954 | gleich |
| ESS9 3.3 | `data/raw/ess9-ed3.3/ESS9e03_3.csv` | `499dffc823859b621902b23859dc456e214772e97158bbd01cdb8eff93b1adaa` | 59670184 | gleich |
| ESS10-SC 3.2 | `data/raw/ess10-sc-ed3.2/ESS10SCe03_2.csv` | `9a04d8d52b53cfe8136d0cb238d21647fcd3539d21b339498a38035aec22ec6b` | 27241140 | gleich |
| ESS11 4.2 | `data/raw/ess11-ed4.2/ESS11e04_2.csv` | `4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8` | 82693775 | gleich |

Vergleichsdateien: `data/reference-v2/{ESS5e03_6,ESS8e02_3,ESS9e03_3,ESS10SCe03_2,ESS11e04_2}.json` und `data/reference-groups-v21/{ESS5e03_6,ESS8e02_3,ESS9e03_3}.json` im Stand des Ausgangscommits.

Die Kontrollrechnung nutzt **dieselben Bytes** wie die bisherige Wiederholung. Unabhängig ist der Rechenweg, nicht die Datenquelle. Einen offiziellen Download oder Prüfsummenabgleich mit dem ESS-Portal habe ich nicht durchgeführt.

## 3. Datei-, Runden- und Editionsangaben in den Daten

Geprüft habe ich alle Zeilen mit `cntry == "DE"`:

| Studie | Spalten | Zeilen alle Länder | DE-Zeilen | `name` | `essround` | `edition` | `proddate` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ESS5e03_6 | 675 | 52458 | 3031 | ESS5e03_6 | 5 | 3.6 | 18.08.2025 |
| ESS8e02_3 | 535 | 44387 | 2852 | ESS8e02_3 | 8 | 2.3 | 23.11.2023 |
| ESS9e03_3 | 575 | 49519 | 2358 | ESS9e03_3 | 9 | 3.3 | 26.01.2026 |
| ESS10SCe03_2 | 429 | 22074 | 8725 | ESS10SCe03_2 | 10 | 3.2 | 09.12.2025 |
| ESS11e04_2 | 691 | 50116 | 2420 | ESS11e04_2 | 11 | 4.2 | 02.07.2026 |

Jede DE-Zeile hat genau einen Wert je Metadatenfeld, und alle Werte passen zum Vertrag. In keiner Datei gibt es doppelte Spaltennamen, Zeilen mit falscher Feldzahl, abweichende Schreibweisen von `DE` oder doppelte `idno` innerhalb Deutschlands. `pspwght`, `dweight`, `anweight` und `pweight` sind für alle DE-Fälle positiv und endlich. ESS5 und ESS8 enthalten `anweight` bereits, obwohl der Leitfaden für die Runden 1 bis 8 die eigene Bildung beschreibt (V1.1/V1.2, gedruckte Seite 5, Abschnitt 4.2). Die Dateien folgen damit offenbar späteren Editionen; aus den Daten selbst lässt sich das nicht weiter belegen.

## 4. Eigener Berechnungsweg

Umgesetzt nach `docs/empirie-plan-v2.entwurf.md` (Abschnitte „Deskriptive Auswertung“ und „Auswahl-, Qualitäts- und Publikationsentscheidungen“), `publicationRules` und `adapter.questions` des Analysevertrags sowie `eligibilityPredicate`, `questionDenominators`, `weightPolicy` und `displayPolicy` des Gruppenvertrags:

- Filter `cntry == "DE"`. Antwortzellen werden nur als kanonische nichtnegative Ganzzahl mit optionalem nullwertigem Bruchteil gelesen (`^(0|[1-9][0-9]*)(\.0+)?$`). Eine leere Zelle gilt als `export_blank_unclassified`, jeder andere Text als unbekanntes Literal.
- Jeder Wert fällt in genau eine Klasse: gültige Kategorie, Missing-Code mit Grund, strukturell nicht gestellt oder unbekannt.
- Anteil der Kategorie c = Σ Gewichte gültiger Antworten in c / Σ Gewichte aller gültigen Antworten. Gerechnet wird mit `pspwght` (primär), `dweight` und ungewichtet (Sensitivitäten) sowie `anweight` (Diagnose). Die Summen bildet `math.fsum`.
- Sensitivität je Frage: maximale absolute Anteilsdifferenz zwischen primärer und Vergleichsrechnung.
- Status: 0 gültige → `no_valid_answers`; unter 100 gültigen oder eine beobachtete Kategorie mit 1–4 ungewichteten Fällen → `withheld_base_or_cell_count`; sonst `prepared_pending_result_review` (bei Gruppen `prepared_pending_group_result_review`).
- Gruppen: `vote == 1` und gültiger `party2`-Code des Vertrags (`prtvcde2` in ESS5, `prtvede2` in ESS8/ESS9), Gruppe = Parteicode. Fälle mit gültiger Partei, aber `vote ≠ 1` zählen als inkonsistent und keiner Gruppe zu. Pro Gruppe und Frage gelten dieselben Nenner- und Statusregeln.
- Konstanztest für `anweight/pspwght`: absolute oder relative Toleranz 1e-12 gegenüber dem ersten Verhältnis, über alle DE-Fälle beziehungsweise alle berechtigten Gruppenfälle.

## 5. Ergebnis je Frage (Einzelreferenzen)

„Max. Abw.“ ist die größte absolute Differenz eines Kategorienanteils (Skala 0 bis 1). „Nenner“ vergleicht `validCount`, `totalCount`, `missingCount` und `notAskedCount`. „Missing“ vergleicht Gründe und Anzahlen; die Gewichtssummen der Gründe, `missingWeight` und `allDEWeight` waren bei allen 42 Fragen ohne Abweichung (0). „Sens.“ ist die größte Differenz der beiden veröffentlichten Sensitivitätsmaße zu meinen, „anweight“ die größte Differenz bei `maxAbsDifference`, `ratioMin` und `ratioMax`.

| Frage | Veröffentlicht | Eigener Status | Max. Abw. | Nenner | Missing | Sens. | anweight | Ergebnis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ESS5e03_6:bplcdc` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS5e03_6:dpcstrb` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS5e03_6:hrshsnta` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS5e03_6:dbctvrd` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS5e03_6:lwstrob` | ja | prepared | 0 | gleich | gleich | 0 | 2,8e-17 | Übereinstimmung |
| `ESS5e03_6:rgbrklw` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:gvslvol` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:gvslvue` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:gvcldcr` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:bnlwinc` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:eduunmp` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:inctxff` | ja | prepared | 5,6e-17 | gleich | gleich | 5,6e-17 | 2,8e-17 | Übereinstimmung |
| `ESS8e02_3:sbsrnen` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:banhhap` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS8e02_3:imsclbn` | ja | prepared | 0 | gleich | gleich | 0 | 1,1e-16 | Übereinstimmung |
| `ESS8e02_3:wrkprbf` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS9e03_3:sofrdst` | ja | prepared | 0 | gleich | gleich | 0 | 1,4e-17 | Übereinstimmung |
| `ESS9e03_3:sofrwrk` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS9e03_3:sofrpr` | ja | prepared | 0 | gleich | gleich | 0 | 1,4e-17 | Übereinstimmung |
| `ESS9e03_3:sofrprv` | ja | prepared | 0 | gleich | gleich | 1,1e-16 | 0 | Übereinstimmung |
| `ESS10SCe03_2:fairelc` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:dfprtal` | ja | prepared | 0 | gleich | gleich | 5,6e-17 | 0 | Übereinstimmung |
| `ESS10SCe03_2:medcrgv` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:rghmgpr` | ja | prepared | 0 | gleich | gleich | 0 | 1,4e-17 | Übereinstimmung |
| `ESS10SCe03_2:votedir` | ja | prepared | 1,1e-16 | gleich | gleich | 1,1e-16 | 1,1e-16 | Übereinstimmung |
| `ESS10SCe03_2:cttresa` | nein, `withheld_base_or_cell_count` | withheld (Zellregel) | – | – | – | – | – | Status gleich; keine Zahlen zu vergleichen |
| `ESS10SCe03_2:gptpelc` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:gvctzpv` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:grdfinc` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:viepol` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:wpestop` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:scchpldm` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:vteurmmb` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:keydec` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:imsmetn` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:imdfetn` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS10SCe03_2:impcntr` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS11e04_2:gincdif` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS11e04_2:euftf` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS11e04_2:eqparep` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS11e04_2:eqparlv` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |
| `ESS11e04_2:freinsw` | ja | prepared | 0 | gleich | gleich | 0 | 4,2e-17 | Übereinstimmung |
| `ESS11e04_2:fineqpy` | ja | prepared | 0 | gleich | gleich | 0 | 0 | Übereinstimmung |

Ursache der Restdifferenzen: Gleitkommarundung. Alle Werte liegen höchstens bei 1,1e-16, also beim halben Maschinen-Epsilon für Werte nahe 1; das bleibt weit unter der Vertragstoleranz 1e-12. Ein Unterschied in Rechenweg, Nennern, Kategorienordnung oder Gewichten zeigt sich nicht.

Die Sensitivitäten selbst (veröffentlicht und von mir bestätigt): Die maximale Anteilsdifferenz zwischen `pspwght` und ungewichteter Rechnung liegt je Frage zwischen 0,003 und 0,038, zwischen `pspwght` und `dweight` zwischen 0,002 und 0,039. Zwischen `pspwght` und `anweight` liegt sie höchstens bei 8,9e-10.

## 6. Ergebnis Frage-Gruppen-Paare

| Studie | Paare | veröffentlicht | zurückgehalten | Status gleich | max. Abw. veröffentlichter Anteile | Nenner gleich |
| --- | --- | --- | --- | --- | --- | --- |
| ESS5e03_6 (8 Gruppen × 6 Fragen) | 48 | 21 | 27 | 48/48 | 0 | 21/21 |
| ESS8e02_3 (9 × 10) | 90 | 30 | 60 | 90/90 | 1,1e-16 | 30/30 |
| ESS9e03_3 (9 × 4) | 36 | 12 | 24 | 36/36 | 0 | 12/12 |
| Summe | 174 | 63 | 111 | 174/174 | 1,1e-16 | 63/63 |

Von den 111 zurückgehaltenen Paaren scheitern nach meiner Rechnung 70 an der Basisregel (unter 100 gültige Antworten in der Gruppe) und 41 an der Zellregel; eine Aufteilung je Paar gebe ich bewusst nicht an. Kein Paar wurde trotz bestandener 100/5-Regel zurückgehalten, und kein Paar wurde veröffentlicht, obwohl es eine Regel verletzt.

Je Frage, über die veröffentlichten Gruppen:

| Frage | veröffentlichte Paare | zurückgehaltene Paare | max. Abw. | Status gleich | Nenner gleich |
| --- | --- | --- | --- | --- | --- |
| `ESS5e03_6:bplcdc` | 3 | 5 | 0 | ja | ja |
| `ESS5e03_6:dpcstrb` | 2 | 6 | 0 | ja | ja |
| `ESS5e03_6:hrshsnta` | 4 | 4 | 0 | ja | ja |
| `ESS5e03_6:dbctvrd` | 5 | 3 | 0 | ja | ja |
| `ESS5e03_6:lwstrob` | 2 | 6 | 0 | ja | ja |
| `ESS5e03_6:rgbrklw` | 5 | 3 | 0 | ja | ja |
| `ESS8e02_3:gvslvol` | 0 | 9 | – | ja | – |
| `ESS8e02_3:gvslvue` | 1 | 8 | 0 | ja | ja |
| `ESS8e02_3:gvcldcr` | 0 | 9 | – | ja | – |
| `ESS8e02_3:bnlwinc` | 5 | 4 | 5,6e-17 | ja | ja |
| `ESS8e02_3:eduunmp` | 5 | 4 | 0 | ja | ja |
| `ESS8e02_3:inctxff` | 5 | 4 | 5,6e-17 | ja | ja |
| `ESS8e02_3:sbsrnen` | 2 | 7 | 0 | ja | ja |
| `ESS8e02_3:banhhap` | 5 | 4 | 5,6e-17 | ja | ja |
| `ESS8e02_3:imsclbn` | 3 | 6 | 0 | ja | ja |
| `ESS8e02_3:wrkprbf` | 4 | 5 | 1,1e-16 | ja | ja |
| `ESS9e03_3:sofrdst` | 6 | 3 | 0 | ja | ja |
| `ESS9e03_3:sofrwrk` | 2 | 7 | 0 | ja | ja |
| `ESS9e03_3:sofrpr` | 0 | 9 | – | ja | – |
| `ESS9e03_3:sofrprv` | 4 | 5 | 0 | ja | ja |

Die Werte je Paar stehen in `vergleich.json`. Bei veröffentlichten Paaren reicht die maximale Anteilsdifferenz zwischen `pspwght` und ungewichteter Rechnung von 0,007 bis 0,054, zwischen `pspwght` und `dweight` von 0,005 bis 0,053. Diese Gruppensensitivitäten stehen nicht in den öffentlichen Gruppendateien; ich nenne nur ihre Spannweite.

Gruppenzuordnung: In keiner der drei Studien gibt es einen Fall mit gültiger Partei und `vote ≠ 1`. Unbekannte `vote`- oder `party2`-Codes kommen nicht vor. Der Code „nicht gestellt“ (66) bei `party2` trifft in allen drei Studien genau die Fälle mit `vote ≠ 1`, also mit Nein, nicht wahlberechtigt oder Quellen-Missing. Das passt zur dokumentierten Filterführung. Die Gruppenbestände in den Dateien entsprechen `groupsInDeclaredApiOrder` des Vertrags, einschließlich „Other“ und vollständig zurückgehaltener Gruppen.

## 7. Zurückhalteregeln, leere Exportzellen, nicht gestellte Fragen

- **Zurückhalteregeln.** Beide Wege wenden sie gleich an (Abschnitte 5 und 6). Bei `cttresa` entscheidet eine beobachtete Kategorie mit 1–4 Fällen, obwohl die gültige Basis groß ist. Das folgt der vorab festgelegten Regel (keine Zusammenlegung, kein automatischer Ausschluss) und ist kein Rechenfehler.
- **Leere Exportzellen.** Bei keiner der 43 Fragen gibt es eine leere Zelle unter den DE-Fällen. Der Grund `export_blank_unclassified` steht in allen veröffentlichten Referenzen mit Anzahl 0 und wird nicht als Verweigerung oder „weiß nicht“ umgedeutet.
- **Nicht gestellte Fragen.** Der Vertrag sieht für keine der 43 Fragen einen Nicht-gestellt-Code vor. In den DE-Daten gibt es keinen solchen Code und auch keinen unbekannten Code oder unbekanntes Literal. Daher ist `notAskedCount` überall 0, auch in allen veröffentlichten Gruppenpaaren.
- **Nullkategorien.** Unbeobachtete Originalkategorien bleiben mit Anteil 0 erhalten (1 Kategorie bei den Einzelreferenzen, 6 bei den veröffentlichten Gruppenpaaren). Die Kategorienlisten entsprechen überall dem Vertrag.
- **Formale Prüfung der veröffentlichten Dateien.** Je Referenz weicht die Summe der Anteile höchstens um 2,2e-16 von 1 ab; kein Anteil liegt außerhalb von [0, 1]; `uncertainty` ist überall `null`.

## 8. Gewichtsdiagnose `anweight/pspwght`

| Studie | Konstant bei 1e-12 | Relative Spannweite des Verhältnisses | Max. rel. Abweichung `anweight` gegenüber `pspwght·pweight` | Max. Wirkung auf einen Anteil |
| --- | --- | --- | --- | --- |
| ESS5e03_6 | nein | 2,10e-7 | 1,21e-7 | 6,3e-10 |
| ESS8e02_3 | nein | 1,90e-7 | 1,21e-7 | 8,9e-10 |
| ESS9e03_3 | nein | 1,91e-7 | 1,06e-7 | 5,8e-10 |
| ESS10SCe03_2 | nein | 2,01e-7 | 1,21e-7 | 4,5e-10 |
| ESS11e04_2 | ja | 3,0e-16 | 0 | 2,8e-17 |

`pweight` hat in jeder Studie genau einen Wert für Deutschland. In ESS11 gilt exakt `anweight = pspwght · pweight`. Das entspricht Box 1 und Box 3 beider Leitfadenfassungen und Box 2 in V1.2 (gedruckte Seite 6); Box 2 (R) in V1.1 multipliziert zusätzlich mit `10e3`. In den anderen vier Dateien lässt sich die Abweichung nicht allein durch die gespeicherten Dezimalstellen erklären (`anweight` hat dort höchstens 7 beziehungsweise 8 Nachkommastellen). Ihre Größe von etwa 1,1e-7 bis 1,2e-7 relativ entspricht ungefähr einer Einheit einfacher Gleitkommagenauigkeit (2^-23 ≈ 1,19e-7). Meine Vermutung: `anweight` wurde in diesen Editionen mit einfacher Genauigkeit erzeugt. Belegt ist das nicht.

Einordnung: Der Leitfaden sagt, dass `pspwght` bei Einlandanalysen dieselben Schätzungen liefern sollte wie `anweight` (V1.1 und V1.2, gedruckte Seite 4, Abschnitt 3). Praktisch trifft das hier bis auf höchstens 9e-10 zu. Der Empirieplan (Abschnitt „Deskriptive Auswertung“) kündigt an, die Konstanz beim Import zu prüfen. Im Gruppenvertrag stehen dafür die Toleranz 1e-12 und die Regel, einen nicht konstanten Wert nur privat zu protokollieren. Der vorhandene Einzelweg legt Minimum und Maximum offen (`ratioMin`, `ratioMax`), urteilt aber nicht nach Toleranz. Laut gelesenem Code (`pipeline/policy_groups_v21.py`, Verhältnisdiagnose) klassifiziert der Gruppenweg das Ergebnis privat als `nonconstant_ratio`. In `reports/phasen/02-politikprofil-v2-technischer-anhang.md` (Absatz zu Sensitivitäten, Zeile 15) und in einer Stichwortsuche über `reports/phasen` und `reports/loop` habe ich keine ausdrückliche Aussage gefunden, dass die Konstanz bei 1e-12 in vier von fünf Studien nicht gegeben ist. Eine vollständige Durchsicht aller Berichte war das nicht.

## 9. Voraussetzungen für Stichprobenunsicherheit (nur Anzahlen, keine Standardfehler)

| Studie | `psu`/`stratum`/`prob` in der Hauptdatei | Strata (DE) | PSUs (DE) | Strata mit nur einer PSU | PSUs je Stratum (Min/Median/Max) | PSU in mehreren Strata | leere `psu`/`stratum` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ESS5e03_6 | nein | – | – | – | – | – | – |
| ESS8e02_3 | nein | – | – | – | – | – | – |
| ESS9e03_3 | ja | 89 | 178 | 0 | 2/2/2 | 0 | 0 |
| ESS10SCe03_2 | ja | 89 | 179 | 0 | 2/2/3 | 0 | 0 |
| ESS11e04_2 | ja | 25 | 500 | 0 | 2/18/82 | 0 | 0 |

Welche Studien eine zusätzliche Designdatei (SDDF) brauchen:

- ESS8 braucht eine. Laut Leitfaden stehen die Designindikatoren für die Runden 7 und 8 in der integrierten SDDF-Datei (V1.1/V1.2, gedruckte Seite 5, Abschnitt 4.1). Der Katalog bindet als Metadaten `ESS8SDDFe01_1`, die Gewichtungsseite verlinkt „ESS8 - Integrated Sample data edition 1.1“. Daten aus dieser Datei habe ich weder geöffnet noch geladen.
- ESS5 braucht eine. Für die Runden 1 bis 6 liegen die Indikatoren laut Leitfaden je Land in eigenen Dateien und fehlen für manche Länder (gleiche Fundstelle). Ob eine deutsche ESS5-Datei existiert und zugänglich ist, habe ich nicht geprüft; der Katalog nennt den Weg „unbound“.
- ESS9, ESS10-SC und ESS11 brauchen keine: Ab Runde 9 stehen die Indikatoren laut Leitfaden in der Hauptdatei, und die Daten bestätigen das.

Grenzen: Ob `stratum` und `psu` die ursprünglichen Auswahlschichten und Primäreinheiten bezeichnen oder für die Varianzschätzung gebildete Einheiten, habe ich nicht geprüft. Die genaue Paarung von je zwei PSUs je Stratum in ESS9 könnte auf gebildete Varianzstrata hindeuten; das ist eine Vermutung. Leere PSUs innerhalb einzelner Frage- oder Gruppendomänen habe ich nicht gezählt. Nach dem Plan bleiben sie als Nullbeiträge erhalten.

## 10. Abgleich mit dem vorhandenen Code (nach der eigenen Rechnung gelesen)

Der vorhandene Weg nutzt dieselben Definitionen: DE-Filter, exakter Codevergleich nach Normalisierung, `fsum`, Status mit `0 < count < 5`, Sensitivitäten als maximale absolute Anteilsdifferenz, Verhältnis über alle DE-Fälle beziehungsweise über berechtigte Gruppenfälle. Kleine Unterschiede ohne Auswirkung auf diese Daten:

- `pipeline/policy_access_v2.py` lässt für `essround` nur den Bruchteil `.0` zu (`_ROUND`), meine Prüfung auch `.00…`. Die Daten enthalten nur ganze Zahlen.
- Der vorhandene Weg prüft die Spalte `name` nicht. Ich habe sie geprüft; sie passt.
- Der Einzelweg berichtet beim Verhältnis nur Minimum und Maximum, der Gruppenweg testet zusätzlich auf Konstanz (siehe Abschnitt 8).

Mir sind keine Abweichungen begegnet, die die veröffentlichten Werte ändern würden.

## 11. Befunde und offene Punkte

1. **Rechenweg bestätigt.** Für die 42 veröffentlichten Einzelreferenzen und die 63 veröffentlichten Paare ergibt eine unabhängige Implementierung dieselben Anteile, Nenner und Status. Das belegt rechnerische Reproduzierbarkeit aus denselben Bytes, nicht deren Herkunft, nicht die Eignung der Fragen und keine Präzision.
2. **Konstanzdiagnose ausdrücklich berichten.** In vier von fünf Studien besteht das Verhältnis den Test bei 1e-12 nicht (Abschnitt 8). Für die Ergebnisse ist das praktisch folgenlos, die Wirkung liegt bei höchstens 9e-10. Weil der Plan eine Prüfung ankündigt, wäre ein klarer Satz zum Ergebnis sinnvoll. Ob und wo er stehen soll, entscheidet der Koordinator.
3. **Kleine Missing-Besetzungen in öffentlichen Dateien.** Die 1–4-Regel gilt nur für gültige Kategorien. In den öffentlichen Einzeldateien gibt es Missing-Grund-Einträge mit 1–4 Fällen samt `primaryWeightSum`: 5 in ESS8, 3 in ESS11, keine in ESS5, ESS9 und ESS10-SC. Von den veröffentlichten Gruppenpaaren haben 31 einen `missingCount` von 1–4 (9 in ESS5, 15 in ESS8, 7 in ESS9). Das entspricht der Spezifikation („je Grund mit Anzahl und gewichteter Nennerbasis“). Bei einem Eintrag mit genau einem Fall wäre die Gewichtssumme aber ein Einzelgewicht, was mit der allgemeinen Projektregel „keine einzelnen Gewichte“ kollidiert. Ob es solche Einträge gibt, nenne ich bewusst nicht. Entscheidung offen; das Risiko schätze ich als gering ein, denn die ESS-Mikrodaten sind registrierten Nutzern ohnehin zugänglich. Das ist eine Einschätzung, keine geprüfte Anonymitätsaussage.
4. **Version des Gewichtungsleitfadens.** Die im Plan verlinkte Seite (Weiterleitung auf `/methodology/weighting`) verlinkt den Leitfaden V1.1 vom 07.07.2020. Andere Projektdokumente zitieren V1.2 vom 06.07.2023. Für die hier relevanten Aussagen (Seite 4: `pspwght` = `anweight` bei Einlandanalysen; Seite 5: Designindikatoren je Runde) sind beide gleich. Verschieden ist die R-Syntax für `anweight` (V1.1 mit `* 10e3`, V1.2 ohne). Die Daten stützen die Formel ohne Faktor. Empfehlung: die verwendete Version mit Prüfsumme binden.
5. **Gleiche Eingabebytes.** Unabhängig ist hier nur die Implementierung. Die CSVs sind Symlinks in einen anderen Worktree; eine offizielle Download- oder Prüfsummenkontrolle beim ESS fehlt weiterhin.
6. **SDDF für ESS8 und ESS5.** Ohne diese Dateien gibt es für diese Studien keine Designbasis. Für ESS9, ESS10-SC und ESS11 sind die Identifikatoren vollständig und ohne Singleton-Strata. Ob sie eine geeignete Varianzbasis sind, bleibt eine eigene Entscheidung; der Plan sieht ohnehin keine Standardfehler in der ersten Fassung vor.

## 12. Nicht unabhängig prüfbar

- Herkunft und Echtheit der CSV-Bytes: kein eigener Download, kein Abgleich mit ESS-Prüfsummen.
- Richtigkeit der Codebindungen (Kategorien, Missing-Codes, Parteicodes, Zuordnung der Dateivariable zur Zweitstimme) gegenüber den Originalfragebögen: Ich habe sie als Spezifikation übernommen und nur auf innere Stimmigkeit zwischen Katalog, Verträgen und Daten geprüft.
- Inhaltliche Bedeutung von `stratum`/`psu` und Verfügbarkeit der SDDF-Dateien.
- Gruppenwege für ESS10-SC und ESS11, die bewusst nicht gerechnet wurden.
- Ursache der Nichtkonstanz von `anweight/pspwght` (nur Vermutung).
- Methodische Fragen wie Eignung der 100/5-Heuristik, Neutralität, Konstruktgültigkeit oder Übertragbarkeit auf heutige Websitebesucher waren nicht Gegenstand dieser Kontrolle.

## 13. Datenschutz und Grenzen dieser Prüfung

- Das Skript gibt keine Zeilen, keine `idno`, keine Einzelgewichte und keine Zählwerte 1–4 aus; Fehlermeldungen unterdrücken Zellinhalte. `vergleich.json` enthält nur IDs, Status, maximale Abweichungen und Gleichheitsflags, keine Anteile, keine Zählwerte und keine Werte zurückgehaltener Referenzen.
- **Vorfall in der Terminalausgabe.** Die ersten drei Läufe (19:11 bis 19:13 UTC) gaben je Gruppenstudie die Verteilung der `vote`- und `party2`-Zustände sowie die Gesamtzahl berechtigter Gruppenfälle aus. Ein maskierter Wert 1–4 (ESS9, `vote` Quellen-Missing) ließ sich daraus per Differenz erschließen. Nach Anzahlen nicht veröffentlichter Gruppen ließen sich zusammengefasst eingrenzen. Diese Ausgaben gingen in keine Berichtsdatei. Ich habe die Ausgabe des Skripts korrigiert und meine temporären Protokolle unter `/tmp/v1k/` gelöscht. Die Ausgabe des ersten Laufs hat aber die Laufzeitumgebung gespeichert, unter `/home/stevenh/.claude/projects/-home-stevenh--t3-worktrees-12axes-germany-t3code-794dd32c/23e53461-cc4f-47ca-9cef-78e24a932ce9/tool-results/b0g1bwjlv.txt`; diese Datei habe ich nicht verändert. Über ihre Löschung sollte der Koordinator oder Steven entscheiden.
- Dateien unter `data/local/` habe ich nicht gelesen. Außerhalb von `reports/claude/kontrollrechnung/` habe ich im Repository nichts geschrieben. Temporär habe ich die öffentlichen ESS-Dokumente und Laufprotokolle unter `/tmp/v1k/` abgelegt und anschließend gelöscht.
- Die Prüfung hängt an derselben Python-Laufzeit (3.14.7) und Maschine wie die frühere Wiederholung.

## Anhang A: Tatsächlich geöffnete Quellen (Zeiten in UTC, 3. Oktober 2026)

| Quelle | Zeit | Umfang |
| --- | --- | --- |
| `reports/claude/auftraege/V1-kontrollrechnung.vollstaendig.md` | 19:04 | vollständig |
| `AGENTS.md` (Systemkontext), `docs/project.md` | 19:05 | vollständig |
| `docs/empirie-plan-v2.entwurf.md` | 19:05 | vollständig |
| `docs/reproduktion-life93-v2.md` | 19:05 | vollständig (Dateipfade) |
| `data/analysevertrag.v2.entwurf.json` | 19:05–19:06 | Struktur, `publicationRules`, `boundaries`, alle Studien und Fragen |
| `data/gruppenvertrag.v2.1.entwurf.json` | 19:06 | Struktur, Studien, Gruppen, `responseSerialization`, `eligibilityAccounting`, `weightPolicy`, `privacyAndOutputs` |
| `data/politikprofil-v2.fragen.entwurf.json` | 19:06 | Struktur, Studien (Design-/Gewichtsfelder), Kategorien aller 43 Fragen |
| https://www.europeansocialsurvey.org/methodology/ess-methodology/data-processing-and-archiving/weighting (Weiterleitung auf https://www.europeansocialsurvey.org/methodology/weighting) | 19:06:33 | HTTP 200, HTML-SHA-256 `4efe293daaee7f7401a151b40820978e8df2f0ac7dd49dbf2fcbce6bca812a2f`; Abschnitte „Using the ESS survey weights“, „Which weighting variables are there?“, Liste der SDDF-Dokumente |
| https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS_weighting_data_1_1.pdf | 19:06:42 | V1.1 vom 07.07.2020, SHA-256 `d1d958814ad6376a7e3a19f89e265c8f8069c1e43deb35a397bda2bdb6469560`, vollständig als Text; zitiert: gedruckte S. 4 (= PDF-S. 6) Abschnitt 3, S. 5 (= PDF-S. 7) Abschnitte 4.1/4.2, S. 6 (= PDF-S. 8) Box 1–3 |
| `data/reference-v2/README.md`, `data/reference-groups-v21/README.md` | 19:08 | vollständig |
| `data/reference-v2/*.json`, `data/reference-groups-v21/*.json` | 19:08 (Struktur), 19:11 (Werte, nur maschinell im Skript) | alle |
| Die fünf CSV-Dateien unter `data/raw/` | 19:11–19:16 | nur maschinell im Skript, nur DE-Zeilen und die benötigten Spalten |
| `scripts/run-policy-v2.py`, `scripts/run-policy-groups-v21.py`, `pipeline/policy_analysis_v2.py`, `pipeline/policy_adapter_v2.py` | 19:13:47–19:15 | vollständig, **nach** eigener Rechnung |
| `pipeline/policy_access_v2.py` (Z. 345–395 und Suchtreffer), `pipeline/policy_groups_v21.py` (Suchtreffer), `pipeline/policy_export_v2.py` (Z. 95–104, 399–450) | 19:14–19:15 | Ausschnitte, nach eigener Rechnung |
| `reports/phasen/02-politikprofil-v2-technischer-anhang.md` | 19:15 | Z. 1–36 |
| https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf | 19:14:40 | V1.2 vom 06.07.2023, SHA-256 `6b9c04b70b8f231de1b9040e4afcfc9387fc95e4a1d15ec0496aa7638f8528e5`; abgerufen, weil Projektdokumente V1.2 zitieren; gleiche Fundstellen auf PDF-S. 6–8 |
| Stichwortsuche nach `anweight`/`nonconstant`/`konstant` in `docs/`, `reports/phasen/`, `reports/loop/` | 19:15 | nur Suchtreffer (u. a. `docs/claude-schlusskontrolle-v2.md` Z. 24, `docs/analyseplan-methoden.v2.entwurf.md` Z. 87) |

Die ESS8-SDDF-Daten, nationale Fragebögen und Originaldokumente zu Strata und PSUs habe ich nicht geöffnet.

## Anhang B: Ausgeführte Befehle (Kurzform)

- `git log -1`, `ls`, `wc -l`, `stat -L`, `sha256sum` für Spezifikation und CSVs.
- Python-Einzeiler zur Struktur und Kreuzprüfung von Katalog und Verträgen sowie zur Schlüsselstruktur der Referenzdateien, ohne Zahlenwerte.
- Nur Kopfzeilen der CSVs mit `head -1 | python3 csv` auf Spaltenvorhandensein geprüft, ohne Datenzeilen.
- `curl` für Gewichtungsseite und Leitfäden, `pdftotext`, `pdfinfo`.
- `PYTHONDONTWRITEBYTECODE=1 python3 reports/claude/kontrollrechnung/kontrolle.py`, fünf Läufe; Laufzeit unter 3 s je Lauf.
- Ad-hoc-Aggregatprüfung der float32-Vermutung zu `anweight` (nur Trefferquoten und Maxima ausgegeben).
- Python-Auswertung von `vergleich.json` für die Tabellen dieses Berichts.
- `grep` und `sed` zum Lesen des vorhandenen Codes und zur Suche in Berichten (nach der eigenen Rechnung).

Prüfsummen der Ergebnisdateien zum Berichtszeitpunkt: `kontrolle.py` `53c0de1ed255f03fa77ffbddb1027a7e351bd77326b8c430820fd16dc7649246`. `vergleich.json` enthält einen Zeitstempel und ändert seinen Hash bei jedem Lauf.

## Anhang C: Modell

Laut Systemangabe der Laufzeitumgebung: Claude Opus 5.5, Modell-ID `claude-opus-5-5[1m]`, eingesetzt als Claude-Code-Subagent. Eine darüber hinausgehende technische Bestätigung der Modellversion liegt mir nicht vor.
