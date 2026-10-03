# POLICY-GROUP-EXPORT-V21-ROUND1

2026-10-03. Gezielte Korrektur zu GR21-M-001; keine eigene Freigabe. Die neue Fassung ergänzt in `_eligibility` die notwendige gemeinsame Machbarkeitsbedingung:

```text
0 <= vote_yes - eligible_group_cases - yes_party_not_asked
  <= party_source_missing + party_technical_blank
```

Nach den bereits zugeordneten `yes+gültige Partei`- und `yes+NotAsked`-Fällen müssen die übrigen Yes-Fälle in den beiden verbleibenden Parteizuständen Platz finden. Getrennt konsistente Zustandsachsen genügen dafür nicht. Die Prüfung läuft während der Kandidatenvalidierung, vor Entscheidung und Exportaufbau. Sie rekonstruiert keine individuellen Zustandszuordnungen.

Gelesen wurde ausschließlich der ausdrücklich beauftragte Methoden-Erstbericht `reports/loop/reviews/GROUP-RESULTS-V21-001-methods-first.md`, SHA256 `e0f34c45f6af49e597971fa089085b612b53d233118dc01f71afb182ba7e1c8c`. Damit sind dessen qualitative Aussagen über drei tatsächliche Aggregate und das unabhängige Methodenorakel bekannt. Private Zahlen oder Kandidaten wurden nicht zugeführt. Die dortige Aussage, dass tatsächliche Aggregate die stärkere Bedingung schon erfüllen, ist **keine eigene Empirienachprüfung** dieses Autors. Keine andere Reviewerprosa wurde gelesen.

Vor Änderung des Produktionscodes wurden sieben neue synthetische Tests ergänzt. Der Lauf mit dem ursprünglichen Codehash `56eafd87fa0855df11b23cad90e0f7dff3e6c13af3944f20cc430a09cd4509ba` reproduzierte zwei Fehler: Ein vollständig unerklärter positiver Yes-Rest trotz vorhandener Party-NotAsked-Fälle und ein Rest oberhalb der kombinierten Missing-/Blank-Kapazität wurden fälschlich akzeptiert. Beide Originaltraces sind gesichert. Negative Reste wurden bereits durch die vorhandene untere Bindung zurückgewiesen; der neue Test bewahrt auch diese Grenze.

Die zulässigen Gegenproben erhalten unveränderte Gruppen-/Frageverteilungen und setzen die beiden synthetischen Zustandsachsen getrennt: Rest ausschließlich in jedem der drei Original-Missinggründe, ausschließlich in technischem Blank, gemischter Rest mit null/teilweiser/voller Kapazitätsnutzung, vollständig erklärte NotAsked-Fälle, Nullkapazität, leere Gruppe und positive unzugeordnete Fälle bei leerem Gruppenbestand. Sie verwenden keine Personenzeilen und keinen Produktionsvalidator als erwartetes Rechenorakel. Zulässige Reste ändern weder öffentliche Gruppenbasen noch ausdrückliche Paarfreigabe oder Nullreferenzen.

Tatsächliche Prozesse: Python 3.14.7; zweimal `PYTHONDONTWRITEBYTECODE=1 python -m unittest pipeline.tests.test_policy_group_export_v21 -v`.

| Fassung / UTC | Ergebnis | Log-SHA256 |
| --- | --- | --- |
| Originalcode mit neuen Tests, 15:44:25.674851–15:44:28.441254 | 38 Tests, zwei Failures, Exit 1; 2,689 s | `d2e93ab025046c466118fc4621c57d9006935182322c56f8095dc87830ed2585` |
| Korrigierter Code, 15:44:40.897897–15:44:43.638637 | 38/38 bestanden, Exit 0; 2,665 s | `ca37cef805de77cb4814eaed53b3faf81665343c0068e61b5c3f758834175a3f` |

Eine anschließende Python-/AST-Prüfung bestätigt den Änderungsscope: Entfernen genau der fünf neuen Guard-Zeilen rekonstruiert den Originalcodehash; Entfernen ausschließlich des neuen Fixture-Helfers und der sieben Tests rekonstruiert den Originaltesthash. Alle 31 ursprünglichen Tests sind bytegleich erhalten. Vierzehn gebundene bestehende Dateien — zwölf öffentliche Kontext-/Runtime-Dateien, eigener ursprünglicher Bericht und beauftragter Methodenbericht — sind bytegleich geblieben. Das prüft diese konkrete Teilmenge, nicht sämtliche Pins des fremden Prüfpakets. Details, Diff, UTC, Vor-/Nachlaufmetadaten und Hashes liegen in `outputs/loop/policy-group-export-v21/round1/`.

Finale Pins:

| Datei | SHA256 |
| --- | --- |
| `pipeline/policy_group_export_v21.py` | `d566ccc82ac9909d3ae24aec35ce6eb3e196967b6efb192a487ee8ef999a0b56` |
| `pipeline/tests/test_policy_group_export_v21.py` | `a519f64f531daf45145bf698508ad381ff2ce2d66f0b647e0e32ec0399227e39` |
| unveränderter Gruppenvertrag | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| unveränderter Studienvertrag | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| unveränderter ursprünglicher Autorenbericht | `e20902dc6c36ad567f143ddc16fa7086ad6c4da90327e355f06a796b419f6373` |

Geschrieben wurden nur die zwei beauftragten Export-/Testdateien, dieser neue Bericht und eigene ignorierte QA. Keine Verträge, anderen Bibliotheken, Gates, Auswahlen, Schwellen oder Erstberichte wurden geändert. Quellen-/Schema-/Null-/100/5-/Publikationspaarregeln bleiben bytegleich im ursprünglichen Codeanteil; die erzeugte öffentliche Struktur bleibt unverändert. Keine tatsächlichen Roh-/Privatdateien, Header, IDs, Aggregate oder Kandidaten wurden geöffnet oder neu erzeugt. Keine Git-, Netz-, Server-, Installations- oder allgemeine pnpm-Aktion fand statt.

Die frische feste Fassung benötigt die angekündigte gezielte Methoden-Nachprüfung und Roots tatsächliche Entscheidung. Die Quellenannahme für unveränderten Gegenstand wird hier weder ersetzt noch erweitert. Diese Codex-Autorenkorrektur ist keine zusätzliche unabhängige Erstrolle, keine vollständige Ergebnisblindheit, keine Veröffentlichung und keine empirische Befugnis. Der neue Bericht bleibt getrennt vom unveränderten Erstbericht; sein Abschlussbytehash wird in der eigenen QA-Artefaktliste gesichert.
