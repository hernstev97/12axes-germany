# POLICY-REFERENCE-V2: reine Rechenvorbereitung, WIP

Stand: 3. Oktober 2026. Dies ist ein eigener technischer Folgeauftrag. Der unabhängige Themen-Erstbericht wurde weder ergänzt noch verändert. Keine tatsächlichen Studienantworten, keine neuen Originalkategorien oder Fragen und keine anderen Autorenurteile wurden für diese Arbeit gelesen.

## Umfang

Neu sind ausschließlich `pipeline/policy_reference_v2.py`, `pipeline/tests/test_policy_reference_v2.py`, dieser Bericht und eigene ignorierte Prüfprotokolle unter `outputs/loop/policy-reference-v2/`. Die Bibliothek nutzt nur die Python-Standardbibliothek. Sie enthält keine Dateioperationen, keinen Programmeinstieg, keine Daten-CLI und keine Quellauswahl. Es wurden keine Installation, Git-, pnpm-, Claude-, Produkt- oder Deploymentaktionen ausgeführt. Keine Subagents wurden eingesetzt.

Root autorisierte ausdrücklich die reine synthetische unittest-Ausführung. Der Aufruf war `python3 -m unittest pipeline.tests.test_policy_reference_v2 -v` im beauftragten Worktree, mit `PYTHONDONTWRITEBYTECODE=1`. Ein synchroner Python-Helfer hielt Ausgabe, Exitcode, Interpreterversion, UTC-Zeitpunkte und Laufzeit in `unittest-v1.log` und `unittest-v1.json` fest. Der Prüfprozess ist abgeschlossen; es läuft kein Hintergrundprozess dieses Auftrags.

## Schnittstelle und Annahmen

`categorical_reference` erhält genau ein Studienkennzeichen, ein Fragekennzeichen, vorgegebene gültige Originalkategorien, Beobachtungen und optional eine vollständige Designbasis. Das Ergebnis behält Studien- und Fragekennzeichen. Es gibt keine Funktion zum Zusammenführen von Studienpersonen, keine Faktoren, Gesamtpunkte, Perzentile, Intervalle oder persönlichen Unsicherheitsangaben. Der Aufrufer muss die Herkunft der übergebenen Beobachtungen prüfen; die Bibliothek kann deren tatsächliche Studienidentität nicht feststellen.

Gültige Kategorie- und Designcodes sind Zeichenketten, Integer oder endliche Floatwerte. Boolesche Werte sind keine Codes. Gleichwertige Codes wie `1` und `1.0` dürfen nicht doppelt vorkommen. Kategorien behalten die vorgegebene Ausgabeordnung, einschließlich vorgegebener Kategorien ohne Beobachtung. Die synthetischen Buchstaben `A`, `B` und `C` in den Tests haben keine politische Bedeutung.

Gewichte müssen für jede übergebene Beobachtung positiv und endlich sein. Die Implementierung rechnet mit Floatwerten und verlangt auch darstellbare endliche Gewichtssummen. Sie verwirft Überläufe ausdrücklich. Sie normiert, kalibriert oder ersetzt keine Gewichte. Quellspezifische Gewichtsauswahl und ihre Bedeutung sind offen.

Eligibility und Missing sind verpflichtende boolesche Angaben. In diesem begrenzten Entwurf bedeutet `eligible=False` ausdrücklich „Frage strukturell nicht gestellt“; dann sind Antwort `None` und `missing=False` erforderlich. Eine gestellte, fehlende Antwort verlangt `eligible=True`, `missing=True` und Antwort `None`. Eine gültige Antwort verlangt `eligible=True`, `missing=False` und einen vorgegebenen Originalcode. Unbekannte Codes und widersprüchliche Kennzeichnungen erzeugen Fehler. `None` ist keine gültige Kategorie und wird niemals als Mitte gewertet. Original-Missingcodes müssen vor einem späteren Aufruf anhand der Quelle ausdrücklich klassifiziert werden; dafür enthält diese Bibliothek keinen Import oder Parser.

Diese Eligibility-Konvention darf nicht ungeprüft für andere Domänenbeschränkungen genutzt werden: Ein bereits beantworteter Fall außerhalb einer Zielgruppe ist nicht automatisch „nicht gestellt“. Wenn eine spätere Referenz eine andere Domänendefinition benötigt, muss Root die Schnittstelle und die Zählbedeutung vorher im quellspezifischen Plan prüfen oder erweitern. Die Rechenvorbereitung trifft diese fachliche Auswahl nicht.

## Schätzer und getrennte Nenner

Für jede Originalkategorie berechnet die Bibliothek den gewichteten Anteil innerhalb der gültigen Antworten:

`p_c = Summe[w * eligible * valid * I(response=c)] / Summe[w * eligible * valid]`.

Das Ergebnis weist gültigen Nenner, Kategoriegewicht und ungewichtete Anzahl aus. Gesamtbasis, Eligible-Basis, Missing und nicht gestellte Fragen behalten jeweils getrennte Gewichtssummen und Anzahlen. Missing und nicht gestellte Fragen gehen nicht in den gültigen Nenner ein.

Ohne gültige Antwort ist der Anteil `None` mit Status `no_valid_responses`. Eine vorgegebene, unbeobachtete Kategorie hat bei vorhandenem gültigen Nenner dagegen Anteil null. Diese Fälle werden nicht gleichgesetzt.

## Optionale WRT-Taylor-Varianz

Die Designbasis besteht aus eindeutigen Stratum/PSU-Paaren. Gleiche PSU-Kennzeichen in verschiedenen Strata bleiben verschiedene Einheiten. Die Bibliothek initialisiert die Rechnung aus der gesamten übergebenen Basis. Sie erhält PSUs mit ausschließlich fehlenden oder nicht gestellten Antworten sowie PSUs ohne jede übergebene Beobachtung. Die Basis und Stratum-PSU-Anzahlen bleiben im Ergebnis nachvollziehbar.

Bei vollständigen Kennungen und mindestens zwei PSUs in jedem Stratum nutzt die Bibliothek für jede Kategorie:

`u_hj = Summe_PSU[w * eligible * valid * (I(response=c) - p_c)] / gültiger gewichteter Nenner`

`Var(p_c) = Summe_h { G_h/(G_h-1) * Summe_j[(u_hj - Mittel_h)^2] }`.

Der Standardfehler ist die Quadratwurzel dieser Varianz. Die Implementierung behauptet keine FPC, keine zurückgewonnene Stichprobenstruktur und keine Intervallbedeutung. Ihre Angemessenheit für eine konkrete Studie, deren Stichprobendesign oder Gewichtsart bleibt ungeprüft.

Ohne ausdrücklich übergebene Designbasis lautet der Status `no_design_basis`. Vorhandene Kennungen einzelner Beobachtungen lösen keine Rekonstruktion der Basis aus. Eine fehlende Kennung bei einer übergebenen Beobachtung führt zu `incomplete_design_identifiers`; diese vorsichtige Regel gilt auch für fehlende/nicht gestellte Antworten. Ein Paar außerhalb der gegebenen Basis ist ein Fehler. Ein Singleton-Stratum führt zu `singleton_stratum`, auch wenn es für die betrachtete Frage keinen gültigen Beitrag liefert. In diesen Fällen bleiben Varianz und Standardfehler `None`; es gibt keine Ersatzregel für Singleton-Strata.

## Synthetische Handrechnungsorakel

Alle 19 Tests bestanden mit Exitcode 0. Die erwarteten Werte stammen aus festen Bruchrechnungen, nicht aus einem zweiten Nachbau des implementierten Algorithmus.

| Beispiel | Unabhängig festgelegtes Ergebnis |
| --- | --- |
| Gültige Gewichte 1 für A und 3 für B; Missinggewicht 5; nicht gestellt 7 | Gültiger Nenner 4; Eligible-Gewicht 9; Gesamtgewicht 16; Anteile A=1/4, B=3/4. Missing und nicht gestellt bleiben getrennt. |
| Ein Stratum mit vier PSUs; dieselben gültigen Gewichte; zwei nullbeitragende PSUs | Linearisierten Totals `(3/16, -3/16, 0, 0)`; Varianz `3/32`, gegenüber `9/64` beim falschen Weglassen der Null-PSUs. |
| Ein Stratum mit fünf PSUs; nur die ersten beiden enthalten Beobachtungen | Linearisierten Totals `(3/16, -3/16, 0, 0, 0)`; Varianz `45/512`. Auch gänzlich unbeobachtete PSUs bleiben erhalten. |
| Zwei Strata mit zwei bzw. drei PSUs und Gewichten 1/1 sowie 2/2/0 | Anteil A=1/2; Stratumbeiträge `1/36` und `1/12`; Gesamtvarianz `1/9`, Standardfehler `1/3`. |
| Nicht nullzentrierte Stratum-Totals: A-Gewichte 1/1 in X; B-Gewichte 1/3 in Y | Anteil A=1/3; X-Totals `(1/9,1/9)` ergeben nach Zentrierung Beitrag null. Y-Totals `(-1/18,-1/6)` ergeben Varianz `1/81`, Standardfehler `1/9`. |
| Zwei getrennte Studien-/Frageaufrufe mit Gewichten 1/3 bzw. 3/1 | Anteile A=1/4 bzw. 3/4, getrennte Kennzeichen und Nenner. Keine gemeinsame Referenz. |

Weitere Prüfungen betreffen fehlende Designbasis/-kennung, nullbeitragendes Singleton-Stratum, leere oder vollständig fehlende Antwortbasis, unbeobachtete vorgegebene Kategorien, unbekannte Codes, widersprüchliches Missing, doppelte/ungültige Kategorien und Designpaare, fehlende Studien-/Frageidentität sowie nullwertige, negative, nicht endliche und überlaufende Gewichte.

## Grenze für die nächste Übergangsprüfung

Die synthetischen Tests prüfen definierte Rechenfälle und Fehlerverhalten. Sie sind keine Empirie, keine Repräsentativitätsprüfung und keine wissenschaftliche Produktabnahme. Es wurden keine echten Kategorien, Fragen, Referenzpopulationen, Gewichtsversionen, Eligibility-Regeln oder Designs freigegeben. Keine datenabhängigen Schwellen oder Auswahlregeln wurden ergänzt.

Root muss den WIP-Entwurf prüfen und vor tatsächlichen Aufrufen in einen eigenen v2-Plan mit zwei frischen Übergangsrollen binden. Erst dort können quellspezifische Eingabebedeutung, vollständige Designbasis, zulässiger Schätzer und Darstellungsgrenze begründet werden. Dieser Bericht ist eine getrennte technische Erstfassung und wird nach der Übergabe nicht überschrieben. Datei- und Protokollhashes sowie der erneute bytegleiche Nachweis des historischen Themenberichts stehen im eigenen `completion.json`.
