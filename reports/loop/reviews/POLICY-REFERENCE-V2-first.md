# Erstprüfung von Policy Reference v2

Die optionale Taylor-Varianz braucht eine Korrektur. Ein bestätigter Befund mittlerer Schwere verletzt den zugesagten Bereich positiver endlicher Float-Gewichte. Die übrigen untersuchten Rechen- und Fehlerpfade zeigen keine weiteren Befunde. Dieses Urteil betrifft einen generischen Python-Prototyp im WIP-Stand; es ist weder eine empirische Validierung noch eine Methoden-, Produkt- oder Releasefreigabe.

## Prüffassung und Kontextgrenze

Arbeitsverzeichnis war ausschließlich `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Der vorgegebene Branch heißt `research/life-93-night-20261003`; er wurde wegen des ausdrücklich ausgeschlossenen Git-Zugriffs nicht zusätzlich über Git geprüft. Beide SHA-256-Pins stimmten beim Einstieg sowie vor und nach dem synthetischen Testlauf überein:

| Datei | SHA-256 |
| --- | --- |
| `pipeline/policy_reference_v2.py` | `17ab6f73fd6eab365000161b719a5994f7e07b8988a58165febc5698b73c76e4` |
| `pipeline/tests/test_policy_reference_v2.py` | `910cab1e3365103226030f6e575f84c1a1cbf601d2852e0b0a50ae66c37b5cf8` |

Gelesen wurden die beiden Prüffassungen, `AGENTS.md` und `docs/project.md` für Regeln sowie der ausdrücklich genannte [unslop-Skill](/home/stevenh/projects/12axes-germany/.agents/skills/unslop/SKILL.md). Frühere Autoren- oder Reviewerberichte, Koordinationszustand und Handoff wurden nicht gelesen. Rohdaten, andere lokale Daten, Konten und Authentifizierung blieben unberührt. Keine Recherche, Installation, Git-, pnpm-, Claude- oder weiteren Agent-Aufrufe. Die expliziten Grenzen dieses Prüfauftrags haben Vorrang vor allgemeineren Repository-Abläufen. Geschrieben wurden nur dieser neue Bericht und eigene Artefakte im erlaubten Ausgabeordner. Die beiden Prüffassungen blieben unverändert.

Ich habe das Urteil ohne vorgegebenes Annahmeergebnis gebildet. Die Prüfung stammt aus der Codex-Modellfamilie. Getrennter Kontext schafft eine unabhängige Bearbeitung, beseitigt aber keine gemeinsamen Modellfehler und ersetzt keine Gegenprüfung durch eine andere Modellfamilie oder menschliche Methodenprüfung.

## PRV2-F01: Unterlauf vor der Normierung verfälscht die Taylor-Varianz

Schweregrad: P2, mittel. Fundstelle: `pipeline/policy_reference_v2.py`, Zeilen 253–259, insbesondere die Multiplikation in Zeile 256. Regressionen: [reviewer_tests.py](../../../outputs/loop/policy-reference-v2-review/reviewer_tests.py), Zeilen 94–108.

`_positive_weight` akzeptiert den kleinsten positiven Float `math.nextafter(0.0, 1.0)`, auf dieser Laufzeit `5e-324`. Bei zwei PSUs mit je einer gültigen Beobachtung, Kategorie A beziehungsweise B und diesem gleichen Gewicht sind Anteil und Nenner wohldefiniert. Für A ergibt die Handrechnung `p=1/2`, `u=(1/4,-1/4)`, `V=1/4` und `SE=1/2`.

Die Implementierung berechnet zuerst `weight * (indicator - proportion)`. Bei diesen Gewichten rundet der Beitrag auf null. Die spätere Division durch den gültigen Nenner kann ihn nicht wiederherstellen. Der Status bleibt `computed_wrt_taylor`, die ausgegebenen Werte sind `variance=0.0` und `standard_error=0.0`. Gleiche relative Gewichte mit dem gemeinsamen Faktor `5e-324` verändern damit die Varianz, obwohl die vorgegebene Quotientenformel gegenüber gemeinsamer Gewichtsskalierung invariant ist.

Ein zweiter Unterfall bestätigt auch eine Vergrößerung der Varianz: Für Gewichte im Verhältnis 1:2, also `5e-324` und `1e-323`, ist `p_A=1/3` korrekt, aber die Software gibt `V=4/9` und `SE=2/3` aus. Richtig sind `V=16/81` und `SE=4/9`. Mit Gewichten 1 und 2 liefert sie diese richtigen Werte. Beide Fehlschläge sind in [reviewer-tests.txt](../../../outputs/loop/policy-reference-v2-review/reviewer-tests.txt) dokumentiert; vier vollständige Vergleichsfälle stehen in [minimal-reproduction.json](../../../outputs/loop/policy-reference-v2-review/minimal-reproduction.json).

Die Randgewichte sind extrem klein. Eine tatsächliche Betroffenheit einer Studie wurde weder untersucht noch behauptet. Der Fehler ist trotzdem relevant für den deklarierten generischen Wertebereich: Alle Eingaben erfüllen die implementierte Gewichtsprüfung, die Gesamtgewichte sind endlich und positiv, und ein falscher SE wird als berechnet ausgegeben.

Minimaler Korrekturvorschlag: Den gültigen Gewichtsanteil zuerst berechnen, dann den Residualfaktor multiplizieren, also pro Zeile `(row.weight / valid_weight) * (indicator - proportion)`, anschließend mit `fsum` je PSU summieren. Die spätere Division je PSU entfällt dabei. Diese Reihenfolge liefert in den vier synthetischen Vergleichsfällen die erwartete Varianz. Eine entsprechende Produktionskorrektur wurde nicht vorgenommen und nicht als bestanden geprüft. Die beiden subnormalen Fälle sollten als Regressionen in die reguläre Suite aufgenommen werden; Kategorieanteile, Varianz und SE sowie gemeinsame Gewichtsskalierung gehören in die gezielte Korrekturprüfung. Eine bloße Untergrenze für zugelassene Gewichte würde den zugesagten Vertrag einschränken und wäre eine gesondert zu begründende Alternative.

## Algorithmus und überprüfte Anforderungen

Die Imports des Zielmoduls stammen ausschließlich aus `dataclasses`, `enum`, `math`, `numbers` und `typing`. Die vollständige Quelltextprüfung zeigt keinen File-, CLI-, Netz- oder sonstigen Datenzugriff. Die Rechenfunktion nimmt übergebene Objekte entgegen und liefert unveränderliche Ergebnisobjekte.

Kategorien sind vorab deklariert, ihre Reihenfolge und ursprünglichen Ausgabecodes bleiben erhalten. Ungenutzte Kategorien behalten bei vorhandenem Nenner Anteil null; ohne gültige Antworten bleiben Anteile undefiniert. String- und numerische Codes werden nicht zu einem Mittelwert oder Mittelpunkt umgerechnet. Python-gleiche numerische Deklarationen wie 1 und 1.0 werden als Duplikate abgewiesen. Die Eingabeobjekte blieben im Erhaltungstest unverändert. Studien- und Fragenkennungen werden pro Aufruf getrennt geführt und müssen nichtleere Strings sein. Ob die gelieferten Beobachtungen wirklich zu genau dieser Studie und Frage gehören, ist dadurch nicht belegt.

Der Nenner enthält ausschließlich gültige Antworten. Fehlende Antworten von Gefragten und strukturell nicht gefragte Beobachtungen bekommen getrennte Zähler und Gewichtssummen. Die Gesamtsummen im Accounting sind eine Aufschlüsselung der Beobachtungen, kein politischer Gesamtscore. Positive endliche Gewichte werden auch auf fehlenden und nicht gefragten Zeilen verlangt; boolesche, nichtnumerische, nichtpositive und nichtendliche Gewichte sowie nicht darstellbare Float-Summen führen zu Fehlern. Unbekannte Antwortcodes sind unter sämtlichen vier Flagkombinationen fatal. Widersprüchliche oder implizite Missingness wird ebenfalls abgewiesen.

`eligible=False` wird ausschließlich als strukturell nicht gefragt verbucht. Eine vorhandene gültige Antwort darf damit nicht als außerhalb einer allgemeinen Zielpopulation ausgefiltert werden; sie führt zu einem Fehler. Die API enthält keinen gesonderten Mechanismus für eine allgemeine Zielpopulationseinschränkung. Ob ein Caller eine tatsächlich nicht gefragte Person korrekt so markiert, kann die Funktion nicht prüfen.

Die vollständige deklarierte Designbasis initialisiert sämtliche PSU-Beiträge. Leere PSUs, PSUs mit ausschließlich fehlenden oder nicht gefragten Beobachtungen und vollständig leere Strata bleiben enthalten. Bei üblichen numerischen Größen entspricht die Rechnung der vorgegebenen Formel:

```text
W = sum(w * valid)
p = sum(w * valid * I) / W
u_hj = sum(w * valid * (I - p)) / W
V = sum_h G_h / (G_h - 1) * sum_j (u_hj - mean_h)^2
```

Die Mittelwerte werden innerhalb jedes Stratums gebildet. PSU-Kennungen sind als Stratum/PSU-Paare verschachtelt. Es gibt keine FPC, keine Rekonstruktion einer Basis aus vorhandenen Beobachtungen und keine Singleton-Korrektur. Fehlende Designbasis, fehlende Designkennungen und Singleton-Strata liefern keinen SE. Widersprüchliche beziehungsweise außerhalb der Basis liegende Kennungen führen zu Fehlern, auch bei Beobachtungen ohne gültige Antwort. Der Unterlauf in PRV2-F01 bleibt die belegte Abweichung im optionalen Varianzpfad.

Das Ergebnis enthält keine Faktoren, persönlichen Konfidenzintervalle, Perzentile, Mittel-/Gesamtwerte oder politischen Personenvergleiche. Ein numerisch berechneter Kategorien-SE ist weder eine individuelle Unsicherheit noch eine Aussage zur empirischen Eignung der Referenz.

## Tatsächliche Tests und offene Grenzen

Der Testlauf erfolgte mit `PYTHONDONTWRITEBYTECODE=1` und Python `3.14.7 (main, Aug 14 2026, 06:38:32) [GCC 16.2.1 20260810]`. [run-evidence.json](../../../outputs/loop/policy-reference-v2-review/run-evidence.json) enthält Prüfsummen, Zeiten, Laufzeit und Testergebnisse.

| Prüfung | Ergebnis |
| --- | --- |
| 19 Methoden der unveränderten vorhandenen unittest-Datei | 19 bestanden; keine Fehler oder übersprungenen Tests |
| 29 eigene unittest-Methoden | 28 Methoden bestanden; eine Methode enthält zwei fehlgeschlagene Unterfälle für PRV2-F01; keine Laufzeitfehler oder übersprungenen Tests |
| 240 deterministische synthetische Designfälle mit exakter Fraction-Quotientenrechnung | Anteile und Varianzen innerhalb der angegebenen Float-Toleranz korrekt |
| Eigenständige Handrechnung mit drei Kategorien, zwei Strata und einem leeren PSU | Korrekt: Anteile 1/10, 3/5, 3/10; Varianzen 149/10000, 191/2500, 801/10000 |
| Skalierung normaler Gewichte mit 1e-200, 1e-100, 1e100 und 1e306 | Anteile und Varianzen innerhalb der angegebenen Toleranz invariant |
| Zwei subnormale Handorakel sowie vier direkte Vergleichsfälle | Zwei bestätigte Varianzabweichungen; normale Vergleichsgewichte korrekt |
| Kategorien-/Eingabeerhaltung, Permutation, leere Strata, verschachtelte PSU-IDs, ungültige Flags/Codes/Gewichte/Designs, fehlender Nenner und fehlendes Design | Geprüfte Fälle bestanden |

Die eigene Suite ist mit folgendem Befehl erneut ausführbar. Er liefert wegen der beiden Unterfälle den unittest-Fehlerstatus:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s outputs/loop/policy-reference-v2-review -p reviewer_tests.py -v
```

`run_review.py` sammelt Evidenz und schreibt seine Artefakte ausschließlich neu. Sein Prozessstatus ist kein Test-Gate; maßgeblich sind die expliziten unittest-Ergebnisse und JSON-Felder. Vorhandene Protokolle werden nicht überschrieben.

Nicht getestet wurden echte Antwortdaten, Studien-/Fragenprovenienz, Quellenrechte, quellenspezifische Gewichtsentscheidungen, Instrumenteneignung, empirische Missingness, empirische Güte oder die tatsächliche Vollständigkeit eines Stichprobendesigns. Keine Softwareprüfung dieser Signatur kann solche Caller-Angaben zertifizieren. Eine unvollständige Basis ohne erkennbaren internen Widerspruch kann weiterhin einen numerischen Status „berechnet“ erhalten. Dieser Status ist keine Vollständigkeitsabnahme. Ebenfalls nicht durchgeführt: empirische Analysen, allgemeine Forschung, Website-/Browserprüfung, CI, andere Python-/Plattformversionen oder ein Vergleich mit einem externen Survey-Paket. Die synthetischen Fälle sind keine reale empirische Validierung und entscheiden keine Quellen-, Item- oder Modellwahl.

## UTC, Laufzeit und Prozessabschluss

- Einstieg und erste Pinprüfung: `2026-10-03T12:35:47.451541+00:00`.
- Synthetischer Hauptlauf: `2026-10-03T12:38:30.815398+00:00` bis `2026-10-03T12:38:30.898043+00:00`.
- Hauptlauf insgesamt: `0.082645` Sekunden; bestehende Suite `0.001146` Sekunden; eigene Suite `0.062475` Sekunden. Darin liegt ein einzelner regulärer Testlauf, keine empirische Rechenzeit.
- Bericht erstellt: `2026-10-03T12:40:45.969225+00:00`; seit Einstieg rund `298.5` Sekunden für Lesen, Entwurf, Tests und Dokumentation.
- Prüfprozess PID `2363660`: `test runner PID absent`. Der Runner startete keine Kindprozesse oder Hintergrunddienste. Kein Prozess musste beendet werden. [proc-cleanup.json](../../../outputs/loop/policy-reference-v2-review/proc-cleanup.json) belegt die Kontrolle.
- Eine erneute Pinprüfung nach dem Schreiben steht in `outputs/loop/policy-reference-v2-review/final-check.json`. Dieser Erstbericht wird nach seiner Anlage unverändert bewahrt.

Für das Paket ist eine gezielte Korrektur von PRV2-F01 mit anschließendem Regressionstest erforderlich. Weitergehende empirische oder öffentliche Freigaben werden aus dieser Prüfung nicht abgeleitet.
