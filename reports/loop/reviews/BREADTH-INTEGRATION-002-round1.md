# BREADTH-INTEGRATION-002: gezielte Korrekturprüfung Runde1

Paket `BREADTH-INTEGRATION-002/v2`. Prüfungsbeginn 2026-10-03T12:45:00.221765+00:00; Urteil abgeschlossen 2026-10-03T12:46:22.442257+00:00. Prüffassung der Matrix: SHA-256 `5cd0a1bdff8d9c442cc90e9106f25fbf409d348f9b32066429ff518a985d2a7d`. Manifest-SHA-256 `f847bb82f83b3a20fed19bd04f943bbe7a97e6da9e3096c235855fc60c975720`.

## Urteil

BI-001, BI-002 und BI-003 sind in der geprüften Matrix behoben. Die Korrektur der Antwortarten und Bedeutungsrichtungen trägt. Es bleibt eine unmittelbar in der umgeschriebenen q51-Zeile entstandene Überpräzisierung, BI-004: „Volksentscheid“ bezeichnet ein konkreteres Verfahren als q51b tatsächlich fragt. Eine lokale Wortkorrektur reicht. Sie begrenzt diese Benennung, nicht die übrigen Forschungswege oder das ganze Projekt. Die drei ursprünglichen Findings werden dadurch nicht wieder geöffnet.

Dieses Urteil gilt ausschließlich für die Korrekturen und ihre unmittelbaren neuen Missverständnisse. Es wiederholt keine Gesamtprüfung und ersetzt keine Item-, Plan-, Empirie-, Neutralitäts-, Website- oder Releaseabnahme.

## Prüfung der drei ursprünglichen Findings

| Finding | Befund in der aktuellen Matrix | Gezieltes Urteil |
| --- | --- | --- |
| BI-001 | Zeile26 benennt q27g als Urteil, bestehende Gleichstellungsmaßnahmen gingen bereits zu weit, und q27b als Bewertung der Sinnhaftigkeit geschlechtergerechter Sprache. Die Messformzelle unterscheidet Maßnahmenbewertungen und konkrete Maßnahmen; q27g wird keine zusätzliche Maßnahme, q27b keine gesetzliche Sprachpflicht zugeschrieben. Zeile31 schließt aus Ablehnung von q27g allein einen Ausbauwunsch ausdrücklich aus. | Behoben. Die Richtung der negativ formulierten Übermaßbewertung ist erkennbar. Beide Anker bleiben eng an ihre Gegenstände gebunden. Es wird keine Kodierungs- oder empirische Prüfung als bestanden behauptet. |
| BI-002 | Zeile21 trennt q51d/f als Elite-/Leistungswahrnehmungen und q51e als hypothetische Vertretungserwartung von den normativen Ankern. Die Messformzelle und Zeile31 halten fest, dass q51d/e/f keine fehlende konkrete Ordnungspräferenz ersetzen. | Behoben. Die bisher fehlende Unterscheidung ist in Quellen- und Interpretationszelle vorhanden. Die Originalstelle PDF153 bestätigt die Klassifikation. Ein ungeprüfter gemeinsamer Demokratie-/Populismusscore wird weiterhin ausgeschlossen. |
| BI-003 | Zeile22 nennt J001–004/PDF6–7 und J011–014/PDF13–15. Der Hinweis auf J012 mit 0–10 bleibt erhalten. | Behoben. Die getrennten Bereiche entsprechen den im Ersturteil tatsächlich gelesenen deutschen Originalseiten. Kein zusätzlicher ISSP-Abruf war erforderlich. |

q27b erhält durch die Korrektur keine Aussage über eine gewünschte staatliche Pflicht oder gesamte Familienpolitik. Die Formulierung zur Sinnhaftigkeit ist eine hinreichend enge Zusammenfassung für diese Matrix. Die q27g-Korrektur ist eine semantische Bindung; sie erteilt keine Erlaubnis, die Antwort zu einem breiteren Gleichstellungslabel umzudeuten.

## Unmittelbarer neuer Befund

### BI-004: „Volksentscheid“ präzisiert q51b über den Originalgegenstand hinaus

Gewicht gering; lokale Wortkorrektur vor Verwendung dieser Benennung.

Fundstelle `docs/abdeckung-v2.md:21`. Die neu getrennte Gruppe `q51a–c/g–i/F66/PDF153–154` wird unter anderem mit „Volksentscheid/Willensfolge“ zusammengefasst. Das deutsche GLES-Original ZA10100, Fragebogendokumentation1.3, Nw578/F66, physische PDF153, verlangt in q51b, dass das Volk statt der Politiker die wichtigsten politischen Entscheidungen treffen solle. Die Aussage legt kein bestimmtes Abstimmungs- oder Referendumsverfahren fest. „Volksentscheid“ kann hier als konkrete Präferenz für dieses Verfahren gelesen werden. Das ist enger als die tatsächlich gestellte normative Forderung.

Minimale Korrektur: „Volksentscheid/Willensfolge“ durch „Entscheidungen durch das Volk/Willensfolge“ ersetzen oder q51b einzeln als Forderung benennen, das Volk solle die wichtigsten Entscheidungen treffen. Die korrigierte Trennung von q51d/e/f bleibt erhalten. Es ist keine weitere Grundlagenrecherche oder neue empirische Prüfung für diese Textpräzisierung nötig.

Für diesen unmittelbaren Befund wurde ausschließlich die bereits im Ersturteil gelesene deutsche Originalseite153 nochmals geöffnet. Die vorhandenen Originalbytes stimmen mit SHA-256 `d6e0a07b7690449e19f56d8c78055ee2f150cfaeb6681f96ba14c5802c895404` überein. URL, ursprüngliche Abruf-UTC und Prüf-UTC stehen in [targeted-original.json](../../../outputs/loop/breadth-integration-002-review/round1/targeted-original.json). Die Korrektur der deutschen ISSP-Seiten wurde gegen die ursprüngliche eigene Originallektüre beurteilt, nicht erneut recherchiert.

## Arbeitsgrenze und Erhaltung

Arbeitsort `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Branch `research/life-93-night-20261003` und Erhaltung der v1-Matrix/des v1-Manifests im Commit `c72d465b7a226356dfca09ae48e83273ee2dfc03` sind Auftragsangaben; keine Gitabfrage wurde ausgeführt. Eine technische Verifikation dieses Commits wird nicht behauptet.

Gelesen wurden das neue v2-Manifest, die aktuelle Matrix, die relevanten Finding-Abschnitte meines eigenen Erstberichts und gezielt die bereits gelesene GLES-Originalseite153. Die schon gelesenen unslop-Regeln gelten für die Berichtssprache weiter. Keine anderen neuen Berichte, Zustände, Handoffs, Antwortresultate, Roh-/lokalen Daten, Authentifizierungsquellen oder fremden Urteile wurden geöffnet. Keine neue Suche, allgemeine Quellenrecherche, Delegation oder Root-Verteidigung. Es gab keine Git-, pnpm-, Installations-, Konto-, Claude-, Download-/Export- oder Analyseaktion.

Geschrieben wurden nur dieser neue Bericht und eigene Belege unter `outputs/loop/breadth-integration-002-review/round1/`. Die Matrix und Autoren-Erstberichte wurden nicht bearbeitet. Mein Erstbericht bleibt bytegleich mit SHA-256 `e5fb9424e78ac81a19eb80a584fd52dcad7b525d08d2ff008c1dfeadf0f2114a`; er wurde nicht um ein späteres Urteil ergänzt oder überschrieben. Sein Hash stimmte zu Beginn mit dem v2-Manifest und dem ursprünglichen Abschluss überein.

Der Vorherabgleich ist in [pins-before.json](../../../outputs/loop/breadth-integration-002-review/round1/pins-before.json) gebunden. Vor Erstellung dieses Berichts wurden Matrix, Manifest und eigener Erstbericht nochmals geprüft. Der Nachherabgleich mit UTC, Erhaltungsnachweis und Hash dieses Rundenergebnisses steht in [pins-after.json](../../../outputs/loop/breadth-integration-002-review/round1/pins-after.json). Der neue Bericht wurde exklusiv angelegt und anschließend unverändert gehasht.

Die Quellenhashes und die semantische Textprüfung sind die tatsächlich ausgeführten Checks. Die Ergebnisblindheits- und Modellfamiliengrenzen des Ersturteils werden nicht rückwirkend aufgehoben. Offen bleiben die außerhalb dieser Runde liegenden Auswahl-, Referenz-, Rechte-, empirischen und menschlichen Prüfungen. Diese Runde liefert dazu keine neuen Abnahmen.
