# BREADTH-INTEGRATION-002: gezielte Korrekturprüfung Runde2

Paket `BREADTH-INTEGRATION-002/v3`. Prüfungsbeginn 2026-10-03T13:03:49.613437+00:00; Urteil abgeschlossen 2026-10-03T13:04:50.071721+00:00. Arbeitsort `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`.

## Urteil

BI-004 ist behoben. Die zusätzliche ESS5-D36-Paraphrase entspricht dem deutschen Original an der erlaubten Fundstelle. In diesen beiden Änderungen und ihrem unmittelbaren Zellenkontext habe ich keinen neuen relevanten Quellen- oder Bedeutungsfehler festgestellt. Für diesen begrenzten Korrekturauftrag bleibt keine weitere Textkorrektur offen.

Das ist eine lokale Quellen-/Benennungsprüfung. Sie erteilt keine Itemauswahl-, Interpretationsgüte-, Plan-, Empirie-, Wissenschafts-, Neutralitäts-, Website- oder Releaseabnahme. Die außerhalb dieser Runde liegenden Anforderungen und Grenzen bleiben offen. BI-001 bis BI-003 werden nicht erneut geprüft; die eigene Runde1 hatte sie als behoben beurteilt.

## BI-004: q51b-Benennung

Die aktuelle Matrix, `docs/abdeckung-v2.md:21`, nennt nun „Entscheidungen durch das Volk/Willensfolge“. Der vorherige Ausdruck „Volksentscheid“ wird diesem GLES-Anker nicht mehr zugeschrieben.

Im deutschen GLES2025-Original ZA10100, Fragebogendokumentation1.3, Nw578/F66, physische PDF153, fordert q51b Entscheidungen des Volkes anstelle der Politiker bei den wichtigsten politischen Fragen. Ein bestimmtes Referendums- oder Abstimmungsverfahren legt die Aussage nicht fest. Die neue kurze Benennung erhält die normative Forderung ohne diese zusätzliche Verfahrensfestlegung. Der danebenstehende Begriff „Willensfolge“ fasst die eigene q51c-Forderung zusammen. Die bereits korrigierte Trennung von q51d/e/f bleibt in derselben Zeile sichtbar; daraus entsteht hier kein neues Missverständnis.

Status BI-004: geschlossen für die geprüfte Matrixfassung. Kein empirisches Urteil folgt daraus.

## ESS5 D36: enger Quellenabgleich

Die aktuelle Matrix, `docs/abdeckung-v2.md:22`, ersetzt „rechtsverletzende Ausnahme“ durch „Gesetzesbruch, um das Richtige zu tun“. Die getrennte ESS5-Identität D33–36/PDF27 bleibt erhalten.

Das tatsächlich gelesene deutsche Original zeigt auf physischer Seite27 D36 mit dem Variablenanker `RGBRKLW`. Der Quellensatz lautet:

> Manchmal muss man das Gesetz brechen, um das Richtige zu tun.

Die neue Matrixparaphrase beschreibt den Gegenstand dieses Satzes zutreffend. Sie ist eine kurze Inhaltsangabe, kein neu formuliertes Testitem. Bei einem späteren wörtlichen Einsatz wären insbesondere „Manchmal muss man“ und die Originalantwortskala Teil der Frageidentität. Diese Runde prüft weder einen solchen Einsatz noch seine Eignung.

Die Originalseite nennt hier keinen Terrorverdacht, keine Überwachung und keine staatliche Sonderbefugnis. Auch eine bestimmte Grundrechtsverletzung wird in D36 nicht formuliert. Die in derselben Matrixzeile separat genannten ISSP-Kontexte werden nicht in den ESS5-Satz übertragen. Die neue Paraphrase bleibt dadurch enger am Quellensatz als die bisherige Formulierung. Die allgemeine Zustimmung/Ablehnung zu diesem Satz begründet in dieser Prüfung kein Personenlabel oder umfassendes Sicherheits-/Autoritätsurteil.

Ergebnis dieses zusätzlichen Quellenabgleichs: passende Präzisierung; kein neuer Befund und keine weitere lokale Korrektur nötig.

## Prüffassung und Erhaltung

| Geprüfter Eingang | SHA-256 |
| --- | --- |
| v3-Manifest | `d6d7dbc13a920395a92f65eb9b173fbab0462e359ea8e124e5558cb10185e8dd` |
| Aktuelle Matrix | `6b7143e8e18b1f541bcfa5d68921ab1b91a412456854e89f852a348a1121e99a` |
| Eigener Erstbericht | `e5fb9424e78ac81a19eb80a584fd52dcad7b525d08d2ff008c1dfeadf0f2114a` |
| Eigener Runde1-Bericht | `bf01e79391664b6acd1c0549ccaf7409f191360224ef6f3606baf90de4b92051` |
| ESS5 deutsches Original, nur physische Seite27 gelesen | `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf` |
| GLES2025 deutsches Original, nur physische Seite153 gelesen | `d6e0a07b7690449e19f56d8c78055ee2f150cfaeb6681f96ba14c5802c895404` |

Alle Eingänge stimmten vor der Lektüre mit ihren Manifest-/Auftrags- beziehungsweise eigenen Abschlussbindungen überein. Unmittelbar vor Erstellung dieses Berichts wurden diese Hashes erneut geprüft. Der vollständige Vorher-/Nachherbeleg samt UTC und neuem Berichtshash liegt in [pins-before.json](../../../outputs/loop/breadth-integration-002-review/round2/pins-before.json) und [pins-after.json](../../../outputs/loop/breadth-integration-002-review/round2/pins-after.json). Die originale Erst- und Runde1-Fassung sowie beide PDF-Originalbytes bleiben unverändert; dieser Bericht wird getrennt exklusiv neu angelegt.

Die tatsächliche lokale Seitenlektüre ist in [targeted-originals.json](../../../outputs/loop/breadth-integration-002-review/round2/targeted-originals.json) mit URLs, Originalhashes, Seiten und Prüf-UTC gebunden. Der lokale Lesezeitpunkt ist kein neu ermittelter Downloadzeitpunkt. Original-Abrufbelege oder Quellenkataloge wurden in dieser Runde nicht geöffnet.

Die Sicherung der v2-Matrix, des v2-Manifests und der alten Urteile im Commit `88eb7db56f00101cf76d46019661076d15deed70` ist eine Auftrags-/Manifestangabe. Die Branchangabe `research/life-93-night-20261003` stammt aus dem Auftrag. Beides wurde wegen des Gitverbots nicht technisch nachgeprüft. Die lokale Byteerhaltung der eigenen alten Urteile wurde dagegen tatsächlich geprüft.

## Arbeitsgrenze

Gelesen wurden nur das aktuelle Manifest, der unmittelbare Matrixkontext, relevante Abschnitte der eigenen bisherigen Urteile sowie die beiden ausdrücklich erlaubten deutschen Originalseiten. Es gab keine neue Grundlagenrecherche und keinen Vergleich mit einer Root-Verteidigung. Keine Autorenberichte, anderen Reviews, Zustände, Handoffs, Roh-/lokalen Daten, Antworten oder Authentifizierungsquellen wurden geöffnet. Keine Netz-, Git-, pnpm-, Installations-, Claude-, Download-/Export-, Analyse- oder Agentenaktion.

Geschrieben wurden ausschließlich dieser neue Bericht und eigene Belege unter `outputs/loop/breadth-integration-002-review/round2/`. Die bereits gelesenen unslop-Regeln gelten weiter. Die ausgeführten Checks sind Hashvergleich, Erhaltungsprüfung und enger Quellen-/Textabgleich. Alle weitergehenden Forschungs- und Freigabeprüfungen liegen außerhalb dieser Runde; ihr Bestehen wird nicht behauptet.
