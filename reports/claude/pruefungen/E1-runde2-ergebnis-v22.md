# E1 Runde 2: Ergebnisprüfung v2.2

Stand: 3. Oktober 2026. Prüfer: OpenAI Codex, gpt-6.1-sol, high reasoning effort. Begrenztes KI-Review im Modus NACHPRUEFUNG.

## Gesamturteil

**BESTANDEN für den benannten Prüfgegenstand.** E1-V22-F01, F02 und F03 sind in der neuen Kandidatenfassung korrigiert. Kein neues offenes Finding. Ich empfehle alle 59 vorbereiteten Einzelreferenzen und 96 vorbereiteten Gruppenpaare für eine ausdrückliche Exportentscheidung. Drei Einzelreferenzen und 194 Paare bleiben ausgeschlossen und ohne Zahlen. Dies ist keine Veröffentlichung oder Freigabe durch Steven.

## Umfang und Bindung

Der Manifesthash wurde vor der inhaltlichen Prüfung berechnet und stimmt mit dem außerhalb der Datei übermittelten SHA-256 überein: `ce6aa5b35684f40d666743da866aa34af34a7d51b9fd3c5bf98fc99646c5458a`. Arbeitsbaum beim Start sauber; HEAD `3be8c4e846199255cfb4d24d232263e05ea5eaf4`, Branch `research/life-93-claude-20261003`.

Alle sechs Sollhashes der Kandidatenfassung stimmen. Der Zellnachweis bindet beide privaten Läufe und alle fünf numerischen Kandidatendokumente. Die sechs eingefrorenen Artefakte Plan, Ergänzung, Analysevertrag, Gruppenvertrag, run_v22.py und survey.py stimmen bytegenau mit dem Tag `analyseplan-v2.2` überein. Tagziel lokal und auf origin: `b6af9a472c71ade865543cf75100c44a164ee12d`. Die neuen SDDF-/SAV-Dateien stimmen mit den Softwarehashes im Designlaufbeleg überein. Die überarbeitete Exportdatei wird als neue, separat gehashte Fassung geprüft.

Die privaten Laufbytes wurden nicht geöffnet. Ihre Hashangaben werden zwischen Manifestpaket, Kandidaten, Zellnachweis, Laufbeleg und Gegenprobenbericht abgeglichen. Laufbeleg und Gegenprobenbericht hatten keinen separat extern übermittelten Sollhash; ihre Isthashes stehen unten.

## Nachprüfung der Findings

| Finding | Ergebnis in Runde 2 | Beleg |
| --- | --- | --- |
| E1-V22-F01 | KORRIGIERT | Alle 155 numerischen Referenzen bleiben prepared_pending_result_review. Alle 197 anderen Einträge haben reference=null. release prüft beide privaten Laufhashes und alle fünf Kandidatenhashes, bevor nur ausdrücklich genannte vorbereitete Einträge reviewed_historical_reference erhalten. |
| E1-V22-F02 | KORRIGIERT | Alle 914 Kategorien folgen exakt apiValidCodeOrder für neue Fragen bzw. categoryCodes für v2-Fragen. Die Anteile der 104 bisher numerischen Kandidatenreferenzen sind codeweise exakt unverändert. |
| E1-V22-F03 | KORRIGIERT | Genau 155 eindeutige Nachweis-IDs, dieselbe Menge wie die vorbereiteten Referenzen; gültige Fallzahlen und Kategorienzahlen stimmen. Mindestbasis 108, kleinste positive Zelle laut Nachweis 5; alle Summenbestätigungen wahr. Keine gesperrte Referenz im Nachweis. |

Der aggregierte Nachweis ist der in Runde 1 verlangte Prüfnachweis. Er enthält keine vollständigen Kategoriehäufigkeiten. Ich habe die Summenbestätigungen und Mindestwerte gegen Kandidaten und Erzeugungslogik geprüft, die Zählungen aber nicht aus Privatdaten erneut berechnet. `cell_evidence` bildet Minimum und Summenprüfung aus ungewichteten categoryCounts und verweigert den Export bei einer verletzten 100/5-Regel. Die Zahl positiver Kategorien passt zu den positiven exportierten Anteilen.

Der Release-Kontrollfluss wurde zusätzlich in sechs Szenarien im Speicher geprüft. Beide Laufhashfehler, ein Kandidatenhashfehler und die Freigabe einer gesperrten Referenz werden abgewiesen. Eine vollständige positive Liste setzt die 59/96 erlaubten Status; leere Listen entfernen sämtliche Zahlen. Privatleser, Kandidatenerzeugung und Schreibmethoden waren gemockt. Das ist keine Ausführung des tatsächlichen Exports. release bindet die fünf Kandidatendokumente, lädt die öffentliche Zellnachweisdatei nicht und berechnet deren Zellenprüfung über candidates erneut. Die Exportentscheidung sollte auch den unten angegebenen Zellnachweishash als Reviewbeleg festhalten.

## ESS5 und ESS8: Design und SPSS-Leser

`read_design` verweigert doppelte kanonische IDs, fehlende Designfelder und ungültige IDs/PSUs. Die ESS5-Länderdatei darf nur DE enthalten; beim ESS8-CSV werden DE-Zeilen ausgewählt. `linked_design` verlangt eindeutige IDs der deutschen Hauptdatei und Mengenidentität mit der Designdatei. Fehlende, zusätzliche oder doppelte IDs führen zu keinem Bereich; ein ungültiger Designimport bricht ab. Der synthetische Test deckt fehlende/zusätzliche IDs und die Dublette 2/2.0 ab.

Die Varianz nutzt vollständige Stratum/PSU-Paare. PSU-Codes werden innerhalb ihres Stratums behandelt; PSUs ohne gültige Domänenantwort bleiben mit Nullbeitrag erhalten. Gewichtet wird weiter mit pspwght. Singleton-Strata verhindern Bereiche; weniger als 20 Freiheitsgrade ebenfalls. Diese Regeln entsprechen Plan 4.1 und 4.2. Der Laufbeleg meldet für beide neuen Studien keine Singleton-Strata. Die behauptete tatsächliche Zuordnung habe ich ohne Privatdaten nicht erneut kontrolliert.

| Studie | Deutsche Fälle laut Laufbeleg | Strata | PSUs | Freiheitsgrade |
| --- | --- | --- | --- | --- |
| ESS5e03_6 | 3031 | 2 | 168 | 166 |
| ESS8e02_3 | 2852 | 20 | 180 | 160 |

**PROB nicht zu nutzen ist planmäßig.** Der festgelegte Schätzer nimmt pspwght; die Taylor-Varianz benötigt Strata und PSUs, keine zusätzliche Gewichtung aus PROB und keine Endlichkeitskorrektur. Die Vermutung im Laufbeleg, PROB sei bei ESS5 vermutlich keine Gesamtauswahlwahrscheinlichkeit, ist dafür nicht notwendig und wird hier nicht als bewiesene Semantik übernommen. Die dort genannten Korrelationen wurden nicht nachgerechnet. Der Unterschied zwischen ESS8-Dateiname Ausgabe 1.1 und dem berichteten Editionsfeld 1.2 ist dokumentiert; die genaue Datei ist über ihren Hash gebunden. Eine offizielle Versionsklärung wurde nicht neu vorgenommen.

Der SAV-Leser unterstützt little-endian, bekannte Fallzahl und Kompression 0/1. Er liest numerische Werte einschließlich System-Missing sowie kurze und mehrsegmentige Strings, überspringt Dictionary-Metadaten nach ihren Längen und erkennt die komprimierten Codes 252 Ende, 253 Rohwert, 254 Leerstring und 255 System-Missing. Numerische Kurzwerte ergeben Code minus Bias. Der Round-trip-Test prüft beide Kompressionsarten, numerische Werte außerhalb der Kurzwerte, System-Missing, DE, leere Strings und eine mehrsegmentige Stratumzeichenfolge. Der Leser ist für die beschriebenen genutzten Merkmale tragfähig; die echte ESS5-Datei und übersprungene Dictionary-Metadaten sind damit nicht unabhängig validiert. Big-endian, ZLIB-Kompression und allgemeine SPSS-Sonderfälle erhalten keine Freigabe.

## Bereiche und grobe Plausibilität

Alle 155 numerischen Referenzen haben Designmetadaten. Von 914 Kategorien tragen 889 einen Bereich; bei den übrigen 25 ist der Anteil 0 und lower/upper fehlen. Keine fehlenden Grenzen bei einem Anteil zwischen 0 und 1. Alle vorhandenen Grenzen liegen in [0,1], enthalten den Anteil und sind auf der Logitskala symmetrisch. Überall gilt df=PSUs−Strata und df≥20; ESS5-/ESS8-Metadaten stimmen mit dem Designlaufbeleg überein. ESS9 bleibt bei 89/178/89, ESS10-SC bei 89/179/90 und ESS11 bei 25/500/475.

Wie in E1 wird aus dem Logitintervall SE=(logit(U)−logit(L))·p(1−p)/(2·t(.975,df)) rückgerechnet und SE²/[p(1−p)/n_gültig] als grober Designeffekt beschrieben. Keine neue Schwelle.

| Referenzen | Breite min/median/max in Prozentpunkten | Grober Designeffekt min/median/max |
| --- | --- | --- |
| ESS5e03_6 singles | 0.88 / 3.13 / 6.11 | 1.06 / 1.77 / 5.92 |
| ESS5e03_6 pairs | 1.93 / 8.06 / 16.83 | 0.86 / 1.32 / 2.51 |
| ESS8e02_3 singles | 0.33 / 3.03 / 5.53 | 0.96 / 1.48 / 2.41 |
| ESS8e02_3 pairs | 1.35 / 9.21 / 25.36 | 0.64 / 1.33 / 3.97 |
| ESS9e03_3 singles | 0.46 / 3.54 / 5.61 | 0.65 / 1.52 / 3.05 |
| ESS9e03_3 pairs | 1.73 / 11.04 / 23.00 | 0.78 / 1.12 / 1.94 |
| ESS10SCe03_2 singles | 0.22 / 1.33 / 3.72 | 0.90 / 1.41 / 4.60 |
| ESS11e04_2 singles | 1.49 / 4.78 / 7.76 | 1.60 / 2.95 / 4.54 |

Die breiteren Gruppenbereiche passen zu den kleineren gültigen Basen. Der maximale ESS5-Einzelwert des groben Designeffekts von 5,92 ist als stärkere Designeinwirkung plausibel, kein neues Ausschlusskriterium. Die Diagnose zeigt keinen groben Widerspruch, garantiert aber keine nominale 95-%-Abdeckung bei seltenen oder stark gewichteten Kategorien.

## Gegenprobe und bekannte Werte

Die Gegenprobe nutzt für Einlesen, Kodierung und Gruppenbildung den getrennten Kontrollrechnungsweg V1 und für Anteile/Taylor-Standardfehler die eigenständige Funktion policy_reference_v2.categorical_reference. ESS8 liest seine SDDF separat als CSV. Für ESS5 wird derselbe sav.py genutzt. Diese Gemeinsamkeit kann identische Dekodierungsfehler in beiden Rechnungen verursachen; vollständige ID-Deckung allein prüft weder Stratum noch PSU.

Der gehashte Bericht nennt ESS5 mit 32 Referenzen/202 Kategorien und ESS8 mit 79/407, maximale Anteilsabweichung 1,11e-16 und Standardfehlerabweichung 0. Diese Zahlen decken genau die 32 und 79 numerischen Referenzen der neuen Kandidaten in diesen Studien. Die Gegenprobe vergleicht keine Logitgrenzen oder t-Quantile und prüft nicht unabhängig die vollständige Designzuordnung, SPSS-Dekodierung, offizielle Designsemantik, Publikationszellen oder nominale Abdeckung. Ihre Ausführung wurde nicht wiederholt. Für die eng benannte arithmetische Gegenrechnung ist die Implementierung ausreichend getrennt; eine vollständig unabhängige Prüfung der ESS5-SDDF ist sie nicht.

Alle **42 veröffentlichten Einzelreferenzen und 63 veröffentlichten Gruppenpaare** wurden gegen data/reference-v2 und data/reference-groups-v21 abgeglichen, jetzt einschließlich ESS5 und ESS8. Maximale Anteilsdifferenz jeweils 1,11e-16; numerisch/null und Unterdrückungsstatus gleich. Gruppen-IDs, deklarierte Reihenfolge, Parteicodes, Art und veröffentlichte Bezeichnungen passen zum unveränderten v2.1-Vertrag. Die Gruppenbildung verlangt Wahlteilnahme und einen gültigen Zweitstimmencode; keine heutigen Parteianhängerschaften oder Programme werden daraus abgeleitet. Tatsächliche Fallzugehörigkeit wurde nicht neu gerechnet. Bei 77 Missing-Gründen mit ein bis vier Fällen fehlt planmäßig die Gewichtssumme; Nennerbilanzen der numerischen Referenzen stimmen.

Plan 4.1 umfasst ausdrücklich jeden veröffentlichten Einzel- und Gruppenanteil mit vollständigem Design. Deshalb sind auch die 51 gegenüber der ersten Kandidatenfassung zusätzlich numerisch enthaltenen, bereits veröffentlichten ESS5-/ESS8-v2.1-Paare mit Bereich planmäßig. Die in diesen Studien insgesamt 84 numerischen Paare bestehen aus 51 alten und 33 neuen Paaren. Neue Kategorien- oder Gruppenschwellen wurden dafür nicht eingeführt.

## Exportempfehlung

Die folgenden Listen können in approvedQuestionIds und approvedPairs einer ausdrücklichen Exportentscheidung übernommen werden; die vollständigen Einzelobjekte einschließlich negativer Listen stehen in ratings[0] des JSON-Urteils. Beide privaten Laufhashes, alle fünf Kandidatenhashes und der Zellnachweishash sind dort angegeben. Das Urteil führt keine Entscheidung aus.

### Empfohlene 59 Einzelreferenzen

- ESS5e03_6: bplcdc, dpcstrb, hrshsnta, dbctvrd, lwstrob, rgbrklw, prtyban.
- ESS8e02_3: gvslvol, gvslvue, gvcldcr, bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgcoal, elgngas, elgsun, elgwind, elgbio, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb.
- ESS9e03_3: sofrdst, sofrwrk, sofrpr, sofrprv.
- ESS10SCe03_2: fairelc, dfprtal, medcrgv, rghmgpr, votedir, gptpelc, gvctzpv, grdfinc, viepol, wpestop, scchpldm, vteurmmb, keydec, imsmetn, imdfetn, impcntr, panpriph, panmonpb, freehms, hmsacld, accalaw, loylead.
- ESS11e04_2: gincdif, euftf, eqparep, eqparlv, freinsw, fineqpy.

Grund für jede: vorbereiteter Status, gebundener 100/5-Nachweis, korrekte Kategorienordnung, unveränderte bzw. konsistente Anteile und planmäßige Bereiche bestehen den begrenzten Review.

### Empfohlene 96 Gruppenpaare

Jede Zeile bezeichnet genau die genannten Fragevariablen innerhalb der angegebenen Gruppe aus dem v2.1-Vertrag.

| Gruppen-ID | Fragevariablen |
| --- | --- |
| ESS5e03_6:second_vote:1 | bplcdc, hrshsnta, dbctvrd, rgbrklw, prtyban |
| ESS5e03_6:second_vote:2 | bplcdc, dpcstrb, hrshsnta, dbctvrd, lwstrob, rgbrklw, prtyban |
| ESS5e03_6:second_vote:3 | dpcstrb, hrshsnta, dbctvrd, lwstrob, rgbrklw, prtyban |
| ESS5e03_6:second_vote:4 | dbctvrd, rgbrklw, prtyban |
| ESS5e03_6:second_vote:5 | bplcdc, hrshsnta, dbctvrd, rgbrklw |
| ESS8e02_3:second_vote:1 | bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgngas, elgsun, elgwind, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb |
| ESS8e02_3:second_vote:2 | gvslvue, bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgngas, elgwind, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb |
| ESS8e02_3:second_vote:3 | bnlwinc, eduunmp, inctxff, banhhap, imsclbn, wrkprbf, gvrfgap, rfgbfml, basinc, eusclbf |
| ESS8e02_3:second_vote:4 | bnlwinc, eduunmp, inctxff, banhhap, elgcoal, gvrfgap, basinc, eusclbf |
| ESS8e02_3:second_vote:5 | bnlwinc, eduunmp, inctxff, banhhap, wrkprbf, elgngas, elghydr, elgsun, elgbio, gvrfgap, rfgbfml |
| ESS9e03_3:second_vote:1 | sofrdst, sofrprv |
| ESS9e03_3:second_vote:2 | sofrdst, sofrprv |
| ESS9e03_3:second_vote:3 | sofrdst |
| ESS9e03_3:second_vote:4 | sofrdst |
| ESS9e03_3:second_vote:5 | sofrdst, sofrwrk, sofrprv |
| ESS9e03_3:second_vote:6 | sofrdst, sofrwrk, sofrprv |

Grund für jedes Paar: dieselben geprüften Publikations- und Bereichsregeln; Gruppendefinition unverändert. Insbesondere gibt eine freigegebene Gruppenreferenz wie ESS8:second_vote:5/elghydr nicht die gesperrte Einzelreferenz elghydr frei. Jede Domäne behält ihren eigenen Status.

### Ausgeschlossene Einzelreferenzen und 194 Paare

Einzelreferenzen: ESS10SCe03_2:cttresa, ESS8e02_3:elghydr und ESS8e02_3:elgnuc. Für jede gilt withheld_base_or_cell_count, reference=null. Keine genaue Ursache aus privaten Werten erschlossen.

Auch für jedes der folgenden Paare gilt derselbe dokumentierte Status und dieselbe negative Empfehlung. ESS10-/ESS11-Gruppen bleiben insgesamt außerhalb des geplanten Exports.

| Gruppen-ID | Ausgeschlossene Fragevariablen |
| --- | --- |
| ESS5e03_6:second_vote:1 | dpcstrb, lwstrob |
| ESS5e03_6:second_vote:3 | bplcdc |
| ESS5e03_6:second_vote:4 | bplcdc, dpcstrb, hrshsnta, lwstrob |
| ESS5e03_6:second_vote:5 | dpcstrb, lwstrob, prtyban |
| ESS5e03_6:second_vote:6 | bplcdc, dpcstrb, hrshsnta, dbctvrd, lwstrob, rgbrklw, prtyban |
| ESS5e03_6:second_vote:7 | bplcdc, dpcstrb, hrshsnta, dbctvrd, lwstrob, rgbrklw, prtyban |
| ESS5e03_6:second_vote:8 | bplcdc, dpcstrb, hrshsnta, dbctvrd, lwstrob, rgbrklw, prtyban |
| ESS8e02_3:second_vote:1 | gvslvol, gvslvue, gvcldcr, elgcoal, elghydr, elgnuc, elgbio |
| ESS8e02_3:second_vote:2 | gvslvol, gvcldcr, elgcoal, elghydr, elgnuc, elgsun, elgbio |
| ESS8e02_3:second_vote:3 | gvslvol, gvslvue, gvcldcr, sbsrnen, elgcoal, elgngas, elghydr, elgnuc, elgsun, elgwind, elgbio, mnrgtjb |
| ESS8e02_3:second_vote:4 | gvslvol, gvslvue, gvcldcr, sbsrnen, imsclbn, wrkprbf, elgngas, elghydr, elgnuc, elgsun, elgwind, elgbio, rfgbfml, mnrgtjb |
| ESS8e02_3:second_vote:5 | gvslvol, gvslvue, gvcldcr, sbsrnen, imsclbn, elgcoal, elgnuc, elgwind, basinc, eusclbf, mnrgtjb |
| ESS8e02_3:second_vote:6 | gvslvol, gvslvue, gvcldcr, bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgcoal, elgngas, elghydr, elgnuc, elgsun, elgwind, elgbio, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb |
| ESS8e02_3:second_vote:7 | gvslvol, gvslvue, gvcldcr, bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgcoal, elgngas, elghydr, elgnuc, elgsun, elgwind, elgbio, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb |
| ESS8e02_3:second_vote:8 | gvslvol, gvslvue, gvcldcr, bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgcoal, elgngas, elghydr, elgnuc, elgsun, elgwind, elgbio, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb |
| ESS8e02_3:second_vote:9 | gvslvol, gvslvue, gvcldcr, bnlwinc, eduunmp, inctxff, sbsrnen, banhhap, imsclbn, wrkprbf, elgcoal, elgngas, elghydr, elgnuc, elgsun, elgwind, elgbio, gvrfgap, rfgbfml, basinc, eusclbf, mnrgtjb |
| ESS9e03_3:second_vote:1 | sofrwrk, sofrpr |
| ESS9e03_3:second_vote:2 | sofrwrk, sofrpr |
| ESS9e03_3:second_vote:3 | sofrwrk, sofrpr, sofrprv |
| ESS9e03_3:second_vote:4 | sofrwrk, sofrpr, sofrprv |
| ESS9e03_3:second_vote:5 | sofrpr |
| ESS9e03_3:second_vote:6 | sofrpr |
| ESS9e03_3:second_vote:7 | sofrdst, sofrwrk, sofrpr, sofrprv |
| ESS9e03_3:second_vote:8 | sofrdst, sofrwrk, sofrpr, sofrprv |
| ESS9e03_3:second_vote:9 | sofrdst, sofrwrk, sofrpr, sofrprv |

## Grenzen

- Begrenztes KI-Review durch OpenAI Codex; keine akademische Begutachtung, empirische Gesamtvalidierung, Neutralitätsgarantie oder Freigabe durch Steven.
- Nichts unter data/raw/ oder data/local/ gelesen, gehasht oder ausgeführt. Beide privaten Laufhashes und die SDDF-Dateiangaben sind übereinstimmende Belegangaben, keine von diesem Prüfer kontrollierten privaten Bytes.
- Der Auftrag erlaubt aggregierte Laufbelege und synthetische Tests. Tatsächliche Eins-zu-eins-Zuordnung, Gewichte, Strata und PSU-Inhalte wurden nicht neu aus Originalfällen geprüft.
- Der Zellnachweis berichtet Minimum und Summenbestätigung; seine private Herkunft wurde nicht unabhängig neu gezählt. Dies erfüllt die verlangte aggregierte Nachprüfung, nicht eine Rohdatenreproduktion.
- Die Gegenprobe wird nur anhand ihres Codes und gehashten Berichts beurteilt, nicht erneut ausgeführt. ESS5 teilt den SPSS-Leser mit dem Hauptlauf; übereinstimmende IDs beweisen keine korrekt gelesenen Strata/PSUs. ESS8 nutzt einen getrennten CSV-Weg.
- Die Gegenprobe kontrolliert Anteile und Taylor-Standardfehler, keine Logitgrenzen, t-Quantile, nominale Abdeckung, Rechte oder gegen Originaldokumentation geprüfte SDDF-Semantik. Derselbe Vertragsbestand kann gemeinsame Fehler enthalten.
- Der SPSS-Leser ist auf den beschriebenen ESS5-Fall begrenzt: little-endian, bekannte Fallzahl, Kompression 0/1, numerische Werte und Stringsegmente. Round-trip-Tests sind keine unabhängige Validierung der realen SPSS-Datei; keine allgemeine SPSS-Formatfreigabe.
- PROB wird planmäßig nicht genutzt. Die im Laufbeleg genannte Vermutung zu seiner Bedeutung und die dortigen Gewichtskorrelationen wurden nicht selbst nachgerechnet oder durch zusätzliche Quellen geklärt.
- Der externe Manifesthash bindet sechs Kandidatenhashes. Laufbeleg und Gegenprobenbericht hatten keine separat extern übermittelten Sollhashes; ihre Isthashes werden dokumentiert.
- Keine Fragenauswahl, Polung, Themenzuordnung oder Veröffentlichung geändert. E1 Runde 1 wurde im ausdrücklich erlaubten Nachprüfmodus gelesen; andere Urteile nicht neu geöffnet. Historische Reviewzusammenfassungen im Pflichtplan sind bekannte Kontextinformation.
- Kein pnpm check: Der Build schreibt weitere Dateien und überschreitet die explizite Beschränkung auf zwei Ergebnisdateien. Die erlaubten unittest-Tests nutzen ausschließlich synthetische temporäre Dateien und wurden mit deaktiviertem Bytecode ausgeführt.
- Breitendiagnostik ist keine neue Schwelle und kein Nachweis nominaler 95-%-Abdeckung. Zeit-/Moduswechsel, Nichtteilnahme und individuelle Messfehler bleiben außerhalb der Bereiche.
- Kein Commit, Push, Tag, Nachricht an Dritte, Export, Deployment oder zusätzlicher Prüfagent. Dieser Prüfer schrieb ausschließlich die zwei beauftragten Ergebnisdateien.

- Während der Prüfung änderte parallele Arbeit HEAD auf 028c07fffdd4d91fe1a63b10725ebbea8e221faf. Alle 49 dokumentierten Eingabehashes wurden danach erneut geprüft und sind unverändert. Der zusätzliche unversionierte Bericht reports/claude/agenten/R5-wvs.md stammt nicht aus diesem Review und wurde nicht geöffnet oder verändert.

## Gelesene Dateien mit SHA-256

Hashes der tatsächlich gelesenen Arbeitsbaumdateien. Module mit Privatlesefunktionen wurden nur als Code gelesen oder von synthetischen Tests importiert; ihre Hauptprogramme wurden nicht gestartet. kontrolle.py wurde ausschließlich in den für die Gegenprobe importierten Bereichen Einlesen/Kodierung gelesen; policy_reference_v2.py als Testabhängigkeit und Varianzimplementierung. Alle übrigen JSON-Prüfeingaben wurden vollständig im Speicher eingelesen.

| Datei | SHA-256 |
| --- | --- |
| .agents/skills/unslop/SKILL.md | c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56 |
| .claude/skills/life93-review/SKILL.md | 90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6 |
| .claude/skills/life93-review/references/urteil-schema.json | 5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9 |
| data/analysevertrag.v2.entwurf.json | 8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b |
| data/gruppenvertrag.v2.1.entwurf.json | 9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702 |
| data/politikprofil-v2.2.ergaenzung.json | c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac |
| data/reference-groups-v21/ESS5e03_6.json | 343d06f921f5a943e742f304255726302b71162fb55d8c73b73d11f2f184b19a |
| data/reference-groups-v21/ESS8e02_3.json | fda4e3dab0546ba25ebb2c265d0d930830615697b023fce2075e41c6a562ff3a |
| data/reference-groups-v21/ESS9e03_3.json | a1e7f8b116da9d055ffffb2dc5eb2af04e43524962433a9b032f09cbd8b5d093 |
| data/reference-v2/ESS10SCe03_2.json | e75dfbadcf68c14dce9d13c8a8a2dd1abc6e8a6e96618f960c8cd61c54bc3184 |
| data/reference-v2/ESS11e04_2.json | 453d8ce3273c9e29bb08a49be6e69da46591e3d1ed89f306051b085c511ec721 |
| data/reference-v2/ESS5e03_6.json | e489fe013d1cbd3d72b9ae816e422757ce8d34ae575d09f64df13a1750dc4bc6 |
| data/reference-v2/ESS8e02_3.json | fb720cc18049f037ed86670bd76a51c3c1770342a61f5627b7afbfb127898ad7 |
| data/reference-v2/ESS9e03_3.json | 34e71b448c0c315cf9f19bda30628874c95464faf661813a65f25a3f9ad82be2 |
| docs/abdeckung-v2.2.md | f3f03912f38dc7149b73739bc18fa9bcec59c65f6cb77edfd130be3c8e2d1b10 |
| docs/analyseplan-v2.2.md | 13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8 |
| docs/profilregeln-v1.md | 3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23 |
| docs/project.md | 7cfa1d4046eb30ae4b29728c49fa90baff89f40e56199b8eff0a738ca004e270 |
| docs/pruefregeln.md | 29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233 |
| outputs/claude/v22-candidate-2/ESS10SCe03_2.json | 2f79c5def38e0dc4a9bb8c199256e939a713f745b5e8b4db97ec4339aa069c42 |
| outputs/claude/v22-candidate-2/ESS11e04_2.json | 5e8acdee4c151d9e223828d7b6ac49a885a5903f58965b281d22d40397375af3 |
| outputs/claude/v22-candidate-2/ESS5e03_6.json | 454e500f7642a3abc138b121305e929265a8019f426fe8ddd0728ab6fdc74bb7 |
| outputs/claude/v22-candidate-2/ESS8e02_3.json | b61d3f66ee660bcbc062c0b7278dbb9f507f9df58fea4f7ca8c6663d0d8b5d4b |
| outputs/claude/v22-candidate-2/ESS9e03_3.json | de294c01a673878cdca7f9a24c7c3574ab913178247a00c2500be79fc8427c2e |
| outputs/claude/v22-candidate-2/zellnachweis.json | 67d03502b85ad0f8b01f7cf9ae28dc4bfa5977c6ad322337c8ef883afbbcd2b9 |
| outputs/claude/v22-candidate/ESS10SCe03_2.json | b73b9dd089a51d9bb63c90ead09600de6547125f568d851eab97b2d3f6154baf |
| outputs/claude/v22-candidate/ESS11e04_2.json | c5e20b9f5ae6bb20ce606c52066dc608db8e3c061217b8eefbbd121da5b5a0ac |
| outputs/claude/v22-candidate/ESS5e03_6.json | 5fa548f650a481d70662c88a1ef904ad7b11319c2e03b64b4d52ca40bb096500 |
| outputs/claude/v22-candidate/ESS8e02_3.json | 203a95505a1305dfc2b6c3541730faf0719f82451189de045d4c3b0793c6c714 |
| outputs/claude/v22-candidate/ESS9e03_3.json | 6a2acd3cd3cf6b42fec51e3e1a9b99f796d0af80900711452a8069004af87829 |
| package.json | 451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7 |
| pipeline/policy_reference_v2.py | bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b |
| pipeline/v22/export_v22.py | de0cd64d93e1bd0744029ef764cfb9226cfec4902a04c3c42ba015f8645fd34b |
| pipeline/v22/run_v22.py | b07d5bd8e9306dc7db2b0f1e72af9207d00ca255ea3b0c3c2f58d9f87925e1fd |
| pipeline/v22/run_v22_sddf.py | 60d6904c421b8b9bee0408b8c803a43f7783025ba50661e9a63454c1d87ddf66 |
| pipeline/v22/sav.py | 2783682169b5f62a354b5384f758327aa86e6e8a7dd1e3ccd6b682d174c54216 |
| pipeline/v22/survey.py | ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc |
| pipeline/v22/test_export_v22.py | ed9039cf2a5b0df6381649edbe098cc419597e38380ec5b9297a16b85018d4ee |
| pipeline/v22/test_run_v22.py | e893eadbf46c64c0b96739dff16105be7f83529d3c1cc317df546ab44f46667c |
| pipeline/v22/test_run_v22_sddf.py | 906fd5f0a7c4bf6222a99238b77f8c7ce999149f975c90b009d5c28f394336d3 |
| pipeline/v22/test_survey.py | dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011 |
| reports/claude/auftraege/E1-runde2-ergebnispruefung-v22.md | ce6aa5b35684f40d666743da866aa34af34a7d51b9fd3c5bf98fc99646c5458a |
| reports/claude/kontrollrechnung/kontrolle.py | 53c0de1ed255f03fa77ffbddb1027a7e351bd77326b8c430820fd16dc7649246 |
| reports/claude/kontrollrechnung/sddf-gegenprobe.json | 4d03c326a14dd254046948f14f625651193d59286e5aeae4af592d7d45ead87e |
| reports/claude/kontrollrechnung/sddf_gegenprobe.py | c19acfb12d12e30f2af135b213a7f8f1b6391cb0a1345dba309732421035bccd |
| reports/claude/pruefungen/E1-ergebnis-v22.json | 005c82ca3e11905b918dd43a70521627021472f04bb990d9025a92a4ab88580e |
| reports/claude/pruefungen/E1-ergebnis-v22.md | 11241aa1acc153b8dd5df96fde077fc24b1c9edd2367ccc4b286ffde905593a4 |
| reports/claude/v22-laufbeleg.json | 9eeab05e98c51a98bede3e262c83be15381a273e3524a3284d9ff80fdcde59db |
| scripts/check-review-schema.mjs | 2575997f720f0c440fc54a9ccc15a2bd8c8fb69638dab8c03cf8b9fdaf810166 |

## Ausgeführte Befehle und Modell

- pwd; git status --short; git branch --show-current; git rev-parse HEAD.
- sha256sum und cat des Umfangsmanifests; cat der beiden Skills und des Urteilsschemas; cat/sed/nl für die oben dokumentierten Regeln, Code- und Berichtseingaben.
- rg -n 'LIFE-93|life93|v2.2|E1' /home/stevenh/.codex/memories/MEMORY.md: nur Hinweise auf einen anderen angehaltenen Worktree gefunden; keine Gedächtnisangabe als Reviewbeleg übernommen.
- wc -l für die benannten Python-Module und Testdateien.
- git rev-parse analyseplan-v2.2^{}; git ls-remote origin refs/tags/analyseplan-v2.2 refs/tags/analyseplan-v2.2^{}; git show analyseplan-v2.2:<Pfad> über Python subprocess für die sechs eingefrorenen Dateien.
- PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pipeline/v22 -t .: **21 Tests, OK**.
- Python 3 über stdin: explizit erlaubte JSONs einlesen, SHA-256 und Bindungen, Inventare, Status/Nullschutz, Kategorienordnung, Bilanzen, Publikationsnachweise, alte/neue Anteile, veröffentlichte 42/63 Referenzen und Intervalle prüfen. Ergebnis: keine Abweichungen.
- Python 3 über stdin mit unittest.mock: sechs Release-Kontrollfluss-Szenarien ohne Privatlese- oder Schreibzugriff; alle bestanden.
- apply_patch: ausschließlich die beiden beauftragten Berichtsdateien erzeugen. Python 3 über stdin: ausschließlich diese beiden Dateien um die belegte parallele HEAD-Änderung und das Ergebnis der Abschlussprobe ergänzen.
- pnpm exec prettier --write und --check ausschließlich für die beiden Ergebnisdateien; Node/Ajv2020 gegen das unveränderte Urteilsschema; abschließende Hash-/Git-Statuskontrolle.

Die erste Abschlussprobe stoppte an der zusätzlichen Assertion eines unveränderten HEAD. Ursache war der parallel fortgeschriebene Branch, kein Eingabehashfehler. Die wiederholte Prüfung bestätigte alle 49 Eingabehashes. Das neue unversionierte R5-Artefakt wurde ausschließlich im Git-Status gesehen. Format- und Urteilsschemaprüfung bestehen.

Laufzeitmodell laut T3-Code-Runtime: **gpt-6.1-sol**, OpenAI Codex, **high** reasoning effort. Interne Modellrevision unbekannt. Prompt ist im JSON unter execution.prompt wörtlich protokolliert; das vollständig gelesene Umfangsmanifest ist über execution.inputHashes gebunden. Format- und Schemaprüfung sind technische Prüfungen und keine methodische Abnahme.

