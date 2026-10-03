# Policy Reference v2: gezielte Korrekturrunde 1, WIP

Stand: 3. Oktober 2026. Bearbeitet wurde ausschließlich PRV2-F01 aus dem ausdrücklich freigegebenen unabhängigen Erstbericht. Die vorhandene Rechenbibliothek hat bei subnormalen positiven Floatgewichten vor der Normierung unterlaufende Residualbeiträge erzeugt und trotzdem einen berechneten Standardfehler gemeldet. Die Korrektur ändert die Rechenreihenfolge, keine fachliche Auswahl oder Eingabegrenze.

Vor der ersten Codeänderung hielt Root die Arbeit zur Sicherung der ursprünglichen Prüffassung an. Zu diesem Zeitpunkt waren beide Code-Dateien unverändert; nur die Vorherpins waren im eigenen Ausgabeordner festgehalten. Root gab die Änderung nach seiner lokalen Sicherung im Commit `c72d465` ausdrücklich frei. Der Commitnachweis stammt von Root; diese Autorenrolle hat keinen Git-Aufruf ausgeführt.

## Änderung

In `pipeline/policy_reference_v2.py` wird pro gültiger Beobachtung jetzt zuerst `row.weight / valid_weight` berechnet und dann mit `indicator - proportion` multipliziert. Die bereits normierten Beiträge werden je PSU mit `fsum` summiert. Die bisherige zusätzliche Division nach der PSU-Summe entfällt.

In exakter Arithmetik bleibt dies derselbe Quotientenschätzer:

```text
u_hj = Summe_PSU[(w / W) * (I_c - p_c)]
     = Summe_PSU[w * (I_c - p_c)] / W
```

Der Float-Unterlauf im bestätigten Befund entsteht damit nicht mehr vor der Normalisierung. Stratum-Zentrierung, vollständige übergebene PSU-Basis, Nenner, getrennte Missing-/Nichtgestellt-Angaben, Gewichtszulassung und Statusregeln sind unverändert. Es wurden keine Untergrenze für Gewichte, Ersatz-SE, Intervalle, Designrekonstruktion oder Daten-/CLI-Funktion ergänzt. Die bestehenden fachlichen WIP-Grenzen gelten weiter.

## Neue Handorakel und tatsächliche Prüfung

Die reguläre synthetische Suite erhielt drei zusätzliche Methoden. Die ersten beiden nutzen feste Bruchresultate; die dritte prüft die gemeinsame Skalierung bereits handgerechneter relativer Gewichte.

| Synthetischer Fall | Unabhängiges Handresultat |
| --- | --- |
| Zwei PSUs, A und B jeweils mit `math.nextafter(0.0, 1.0)` | `p_A=p_B=1/2`; PSU-Beiträge `(1/4,-1/4)`; Varianz `1/4`, Standardfehler `1/2`. |
| Zwei PSUs, Gewichte kleinster Float und dessen Doppeltes | `p_A=1/3`, `p_B=2/3`; A-Beiträge `(2/9,-2/9)`; Varianz `16/81`, Standardfehler `4/9`. B hat die gleichen Varianz-/SE-Werte. |
| Gemeinsame Faktoren kleinster Float, `1e-200`, `1`, `1e100`, `1e306` für Verhältnisse 1:1 und 1:2 | Anteile, Varianzen und Standardfehler bleiben innerhalb der verwendeten Float-Toleranz gleich. Die Gewichtssummen dürfen sich erwartungsgemäß verändern. |

Eigene korrigierte Suite: 22 Methoden bestanden, tatsächlicher Exitcode 0. Die unveränderte Reviewer-Suite: 29 Methoden bestanden, tatsächlicher Exitcode 0; auch deren zwei zuvor fehlgeschlagene subnormale Unterfälle bestanden. Keine Tests wurden übersprungen. Der erneute Aufruf der bereitgestellten Reviewer-Tests durch den Autor ist keine neue unabhängige Nachprüfung. Root lässt denselben Reviewer den Befund gezielt nachprüfen.

Die Aufrufe erfolgten ausschließlich im beauftragten Worktree mit `PYTHONDONTWRITEBYTECODE=1` und Python 3.14.7. Protokolle liegen unter `outputs/loop/policy-reference-v2/round1/`:

- `author-unittest.log`: `python3 -m unittest pipeline.tests.test_policy_reference_v2 -v`, Start `2026-10-03T12:43:35.816694+00:00`, Ende `2026-10-03T12:43:35.882449+00:00`.
- `reviewer-unittest.log`: `python3 -m unittest discover -s outputs/loop/policy-reference-v2-review -p reviewer_tests.py -v`, Start `2026-10-03T12:43:35.882469+00:00`, Ende `2026-10-03T12:43:36.017637+00:00`.
- `run-evidence.json`: vollständige Aufrufe, Interpreterversion, UTC-Zeiten, Laufzeiten und tatsächliche Exitcodes.

Beide synchronen Testprozesse sind beendet. Dieser Auftrag startete keine Hintergrundprozesse. Keine Rohdaten, Authentifizierung, Installation, Git-, pnpm-, Claude- oder weiteren Agent-Aktionen; keine empirischen Aufrufe oder neuen Quellenrecherchen.

## Pins und erhaltene Erstfassungen

`pins-before.json` dokumentiert die ursprüngliche Prüffassung vor der Codeänderung. `pins-after.json` bindet die korrigierte Fassung nach den Testläufen. Die erwartete Änderung betrifft ausschließlich Bibliothek und reguläre Tests:

| Datei | SHA-256 vorher | SHA-256 nachher |
| --- | --- | --- |
| `pipeline/policy_reference_v2.py` | `17ab6f73fd6eab365000161b719a5994f7e07b8988a58165febc5698b73c76e4` | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `pipeline/tests/test_policy_reference_v2.py` | `910cab1e3365103226030f6e575f84c1a1cbf601d2852e0b0a50ae66c37b5cf8` | `01ddfaa79b3fedf1cc10d79b547a38622827fa218a29bd921f896e39568d5ad8` |

Die folgenden drei Erstberichte wurden vor und nach der Korrektur bytegleich geprüft:

- `POLICY-REFERENCE-V2-WIP.md`: `32bb7cc12e0f4f9437e80e7d2fe9ad6aff26a7ab95b3f14b957a06c9111c910a`.
- `BREADTH-TOPICS-001-first.md`: `f9dfe17df6795d0a7b82918c5d956421645249036e3ee22257a88a1044d58f5b`.
- Reviewer-Erstbericht `POLICY-REFERENCE-V2-first.md`: `d3aa9f4fe5721facef4a733679a6ed841f54f4c414f91b7c83038304dc7c3618`.

Die Reviewer-Testdatei wurde vom Autor nicht verändert; ihre verwendete Fassung hat SHA-256 `c1bf85546ef65f3f55e67f88f952babd90307d978824dbf5ec67c5c622ea93ad`. Die zusätzliche Rundenakte steht getrennt von den unveränderten Erstfassungen. Abschlusshashes und die letzte Erhaltungsprüfung stehen im eigenen `completion.json`.

PRV2-F01 ist in den beauftragten synthetischen Fällen korrigiert. Dies bleibt generische Rechenvorbereitung. Weder die Tests noch diese Korrektur prüfen tatsächliche Referenzpopulationen, Quellgewichte, Eligibility, vollständige reale Designs, empirische Eignung oder Produktdarstellung. Die gezielte unabhängige Korrekturprüfung und der quellspezifische v2-Plan bleiben Root-Aufgaben.
