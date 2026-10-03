# EMPIRICAL-V2-001 – methodische Nachprüfung, Runde 1

Rolle: `methods_reproducibility`, Codex. Prüfung am 2026-10-03; neue Proben 14:09:57 UTC, abschließende Pinprüfung 14:10:19 UTC. Gegenstand ist ausschließlich die gezielte Revision 2 des Pakets `EMPIRICAL-V2-001/v1`: 19 Quellen-/Scopefelder, die daraus folgende Kataloghashbindung und die Kompatibilität der 22 Artefakte mit dem bestehenden Guard. Das Urteil betrifft die bereits begrenzte geplante historische Ausführung mit fünf Studien und 43 getrennten kategorischen Fragen.

Arbeitsverzeichnis: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Branch laut Koordinator: `research/life-93-night-20261003`. Der vom Auftrag genannte Sicherungscommit `456cc2e18789a41b9e6f34e2dcdef495443b98a6` wurde ohne Git nicht verifiziert. Der Erstbericht wurde nicht überschrieben; sein Bytehash blieb vor und nach der Nachprüfung `50de767d6ebae82b42a80cc923be74a5b3d9d9af3c17ee216424f04faee8dd02`.

## Paketbindung und Änderungsnachweis

Das aktuelle Manifest wurde zuerst geprüft; alle 22 Pins stimmen vor und nach den Proben. [Pinliste vorher](../../../outputs/loop/empirical-v2-001-methods-review/round1/hashes-before.json) und [Pinliste nachher](../../../outputs/loop/empirical-v2-001-methods-review/round1/hashes-after.json) enthalten sämtliche Pfade und Hashes.

| Beleg | SHA256 |
| --- | --- |
| aktuelles `manifest.json`, Revision 2 | `c3abae78ae5425aa275ebd137a10c0a7d0c1cbb299828ba1f13d1789ac955f6c` |
| unverändertes `first-manifest.json`, 20 Pins | `eeae3bc1b81463b51ce2c0a1bf90f12b08aa01f125064e680d1f983df60c62f4` |
| `source-correction-round1.json` | `fe4b99cbe99a595924dc5228085d94f6c8b7df4a76483429c5f7cadd595568ed` |
| aktueller Katalog | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| aktueller Vertrag | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |

Die Änderungsbehauptung wurde eigenständig geprüft. Alle 19 JSON-Pointer sind eindeutig, entsprechen dem angeforderten Feldumfang und enthalten exakt die dokumentierten Nachherwerte. Ihre inverse Ersetzung im aktuellen Katalog rekonstruiert dessen ursprünglichen Bytehash `38e68b2edfc0ecf9c0b1071bf7283d0ff2f366d3492afd0e71388432415195b9`. Beim Vertrag rekonstruiert allein das Zurücksetzen von `catalog.sha256` den ursprünglichen Bytehash `4194f3bb530f036b72a49a81e339779d9d9eed5530a32843acbe6f9697c42e5d`. Die verwendete JSON-Serialisierung reproduziert auch beide aktuellen Dateien bytegleich.

Von den ursprünglichen 20 Artefakten bleiben 18 bytegleich; geändert sind ausschließlich Katalog und Vertrag. Hinzu kommen Originalmanifest und Korrekturbeleg. Alle fünf Bibliotheken und fünf Modultestdateien sind bytegleich. Damit sind innerhalb dieses Pakets keine weiteren Änderungen an Auswahl, Codes, Missing-/Not-asked-Regeln, Gewichten, Nennern, CSV-Normalisierung, country/edition/sourceGuard, vier getrennten Quotensensitivitäten, festem Verzicht auf SE, vorab gesetzten 100/5-Darstellungsregeln oder Exportsoftware verborgen. Die Erklärung `criteriaCodesSelectionSoftwareChanged: false` wurde folglich nicht bloß übernommen.

## Tatsächlich ausgeführte Nachprüfung

Gelesen wurden die beiden Manifeste, der Korrekturbeleg, der unveränderte Scope, die betroffenen Katalogfelder und Quellenverweise sowie die relevanten Access-/Export-Validatoren. Die Pinprüfung las die Bytes aller 22 ausdrücklich erlaubten Artefakte. Keine fremden Reviewer-/Autorenberichte, Zustand-/Handoff-Dateien oder alten fremden Ergebnisse wurden gelesen.

Die sechs neuen gezielten Proben wurden mit `PYTHONDONTWRITEBYTECODE=1` ausgeführt: **6 bestanden, 0 Fehler, 0 Fehlschläge, 0 übersprungen, Exitcode 0**. [Prüfskript](../../../outputs/loop/empirical-v2-001-methods-review/round1/review_round1.py), [Laufprotokoll](../../../outputs/loop/empirical-v2-001-methods-review/round1/targeted-probes.log) und [Ergebnisbeleg](../../../outputs/loop/empirical-v2-001-methods-review/round1/targeted-probes.json) dokumentieren die Durchführung.

Neben Rückrekonstruktion und Artefaktdifferenz prüfen sie die sechs CAWI-Fragestämme, die erhaltenen B25-Grenzen und die aktuelle Schema-Kompatibilität. Aus dem unveränderten `policy_access_v2.py` wurde ausschließlich der originale Manifest-/Artefakt-/Runtime-/Katalog-/Vertragsabschnitt, Zeilen 319–345, per AST isoliert ausgeführt. Seine Validierungslogik blieb unverändert; öffentliche Bytes wurden aus einer expliziten In-memory-Map bereitgestellt. Dieser Abschnitt akzeptierte alle 22 Artefakte und den Vertrag für fünf Studien/43 Fragen. Auch der bestehende Export-Vertragsvalidator akzeptierte alle fünf Studienverträge.

Fünf negative In-memory-Fälle wurden tatsächlich abgelehnt: veränderte Korrekturbelegbytes (`pin_mismatch`), ein doppelter Originalmanifest-Eintrag (`invalid_public_document`), Raw- und Privatpfade als reine Zeichenfolgen (`invalid_path`) sowie ein alter Kataloghash trotz dazu konsistent aktualisiertem Vertragspin (`pin_mismatch`). Es erfolgte kein Zugriff auf diese Pfade. Die Probe verzeichnete null verbotene I/O-/Stat-Versuche.

Der echte Gate-Einstieg und Freeze wurden weder aufgerufen noch geöffnet. Dateisystem-/Symlinkschutz, tatsächliche Gate-/Reporthashentscheidung und echte Raw-I/O wurden in dieser Nachprüfung nicht erneut ausgeführt. Die zusätzlichen Belege sind reguläre, vollständig gehashte Paketartefakte; sie erzeugen keine alternative Statusfreigabe. Dies ist eine Schema-/Pin-Kompatibilitätsprüfung, kein bestandener tatsächlicher Gatezugriff.

## Befunde im begrenzten Scope

**M-H01 – frühere B25-Scope-Unklarheit behoben.** Stelle: Katalog `/items/21/uncertainty/{0,1}/reason`, `/items/21/mappingNotes/0` und `/remainingBindings/{0,1}/{reason,blocks}`. Beleg: Beide Unsicherheiten bleiben `incomplete`; die Gründe stimmen zwischen Item und Restbindung überein. `blocks` nennt jetzt ausdrücklich nur die Reproduktion originaler Folgefragen oder eine neue Webadministration. Die Notiz unterscheidet B26 auf physischer PDF-Seite 12 von B28 auf Seite 13. Auswirkung: Die historische Einzelreferenz wird von der weiterhin offenen Administration getrennt, ohne Mode-Äquivalenz, reproduzierte Durchführung oder empirische-/Publikationsannahme zu behaupten. Minimale überprüfbare Korrektur: Die zuvor empfohlene Scope-Präzisierung ist vorhanden; für diesen Befund ist keine weitere Änderung erforderlich.

Die zwölf CAWI-Feldkorrekturen betreffen `medcrgv`, `rghmgpr`, `votedir`, `cttresa`, `gptpelc` und `viepol`. Ihre Nachhertexte ergeben jeweils exakt den bereits gebundenen PAPI-Antwortstamm plus Itemtext einschließlich „für die Demokratie im Allgemeinen“. Die Erläuterungen verweisen auf die vorhandenen physischen Seiten 139–143/146 und behalten die ausdrückliche Beschränkung auf statische Wortlautkorrespondenz. Der PDF-Hash `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` stimmt zwischen Katalog und Korrekturbeleg überein. Das PDF wurde hier nicht erneut geöffnet oder gehasht; eine erneute vollständige Originalwortlautbegutachtung wird nicht behauptet.

**M-H02 – unveränderte externe Reporthash-Verifikation bleibt erforderlich.** Stelle: `pipeline/policy_export_v2.py`, Modulvertrag, und der im Erstbericht dokumentierte Exportpfad. Beleg: Bibliothek und Studienverträge sind bytegleich; der Modulvertrag verlangt weiterhin die externe Prüfung von Manifest und tatsächlichen Reportbytes. Auswirkung: Formal passende ReviewHashDecision-Daten allein authentifizieren keine Reviewer oder Berichte. Minimale überprüfbare Korrektur: Keine neue Softwarekorrektur aus dieser Runde; die bereits dokumentierte externe Verifikation bleibt vor einem tatsächlichen Export erforderlich. Sie wurde hier nicht ausgeführt und wird nicht zum zusätzlichen Vorab-Prüfauftrag erweitert.

Neue erhebliche Beleg-, Coding-, Rechen- oder Guardfehler wurden in diesem Korrekturumfang nicht festgestellt. Die gültigen früheren 98 gezielten Modultests und sechs eigenen Proben einschließlich 172 Fraction-Oracles bleiben Belege des Erstlaufs für die unveränderten Rechen-/Ausführungsteile. **Sie wurden hier nicht erneut ausgeführt und zählen nicht zu den sechs neuen Proben.** Es wurde keine neue Berechnung von Antworten oder Verteilungen vorgenommen.

Die in `scope.md` offengelegte frühere echte B-Exposition besteht fort; eine unberührte Bestätigung wird nicht behauptet. In dieser Runde wurden keine echten Raw-/Privatdateien oder CSV-Header geöffnet, aufgelistet, angefragt oder per Stat geprüft. Keine Antwort-/Marginal-/Frequenzabfragen, Git-, Server-, Installations-, Claude-, Subagent- oder Browseraktionen. Eigene neue Dateien liegen ausschließlich im beauftragten Berichtspfad und unter `outputs/loop/empirical-v2-001-methods-review/round1/`.

Beide Rollen verwenden dieselbe Codex-Modellfamilie. Gemeinsame Trainings-, Begriffs-, Quellen- und Implementierungsfehler bleiben möglich; getrennte Rollen oder Übereinstimmung garantieren keine Neutralität. Technische und synthetische Proben sind keine Empirie. Dieses Urteil ist keine Gesamtvalidität, Fachbegutachtung, menschliche Abnahme oder Release-/Publikationsfreigabe und setzt keinen Zugriffsgatezustand.

Für die spezifische geplante historische Ausführung unter den unveränderten Scopegrenzen ist die tatsächlich nachgeprüfte **aktuelle 22-Pin-Fassung** mit dem oben genannten Manifesthash methodisch begrenzt akzeptiert. Das Urteil ist an diese Fassung und diesen Bericht gebunden.

ACCEPTED_BOUNDED
