---
name: life93-review
description: Prüft ein ausdrücklich benanntes öffentliches LIFE-93-Prüfpaket zu Quellen, Messmethoden, Interpretationen und Neutralität. Getrennte Erstbewertungen und spätere PR-Reviews bleiben verschiedene Aufgaben.
---

# LIFE-93: begrenztes KI-Review

Diese Projekt-Skill bereitet den Review aus LIFE-93 vor. Ihre Existenz ist kein ausgeführter Claude-Review und keine Abnahme. Sie erteilt keine zusätzlichen Werkzeug-, Schreib- oder Veröffentlichungsrechte.

Verlange vom aufrufenden Auftrag Modus, konkrete Urteilsaufgabe, zulässige Eingaben, Manifestpfad und außerhalb des Pakets gesicherte Manifest-Prüfsumme. Fehlt eine Voraussetzung, berichte `BLOCKIERT`. Lies nur das bezeichnete öffentliche Paket und freigegebene Originalquellen. Keine Rohantworten, Personenkennungen, `data/raw/`, `data/local/`, B oder gesperrten politischen Werte. Unbekannte Zugriffsschutzgrenzen benennen; die Skill allein ist keine technische Sandbox.

Für `ERSTBEWERTUNG` dürfen Eingaben weder fremde Urteile noch vorgeschlagene Auswahlentscheidungen oder Namen enthalten. Beide Modellfamilien erhalten dieselben Kriterien und dieselbe versionierte Grundlage. Entdeckte fremde Urteile stoppen die betreffende Erstbewertung; Exposition protokollieren. Ein PR-Review kann die ursprünglichen Urteile und Autorantworten prüfen, ersetzt aber nie eine Erstbewertung.

Prüfe vor jeder Bewertung den erwarteten Manifesthash und die referenzierten Eingaben. Ein Git-Commit allein genügt nicht bei weiteren Quellen, Datenversionen oder Konfigurationen. Nutze die im Paket gültige LIFE-93-Fassung und Prüfregeln; keine stillschweigende Änderung des Analyseplans. Nach Änderungen eine neue Fassung prüfen.

## Inhaltlicher Auftrag

- Tragende Aussagen an den konkreten Originalfundstellen selbst lesen: Herkunft, Ausgabe, Zeitraum, Lizenz, Gegenbelege und Reichweite. Fehlender Zugang bleibt fehlende Prüfung; Metadaten oder Abstract nicht zum Volltext umbenennen.
- Konstrukt und tatsächlich gefragten Gegenstand vergleichen. Einzelne oder enge Themen tragen keine umfassende Orientierung. Frage, Skala und Filter dürfen nicht verändert werden. Keine Motive, Charaktereigenschaften, Identität oder nicht gemessenen Einstellungen ableiten.
- Methodik am veröffentlichten Score prüfen: Ordinalität, Gewichtung/Design, Missing/Masken, Blindheit/A–B, Identifikation, Dominanz, Stabilität, Vergleichspräzision und vorab festgelegte Ausfallfolgen. Geplante Untersuchungen sind keine schon ausgeführten Tests.
- Persönliche Messunsicherheit, Referenz-/Gruppenunsicherheit und Modellvarianten getrennt behandeln. Reliabilität, Modellfit, technische Konsistenz, KI-Übereinstimmung und menschliche Verständlichkeit belegen Verschiedenes.
- Für jede politische Position dieselben Belegstandards anwenden. Sachlich begründete Unterschiede dürfen bleiben. Keine Fehlerquote und kein gewünschtes politisches Ergebnis. Textmetriken, Perspektivsimulation und Agent-Einigkeit sind keine Neutralitätsnachweise.
- Ein früheres erhebliches Finding anhand seiner ursprünglichen ID und Runde prüfen. Autorverwerfung allein schließt es nicht. Nach zwei strittigen Runden die dokumentierte Begrenzung/Unsicherheit/Auslassung selbst prüfen; sie erzwingt keinen positiven Status.
- Nur die für diesen Auftrag erforderlichen Abnahmen beurteilen. Spätere Voraussetzungen dürfen als solche offen bleiben, ohne einen öffentlichen Rechercheentwurf fälschlich als empirisch gescheitert zu bezeichnen. Ein Release benötigt die vollständigen Freigaben einschließlich menschlicher Beiträge.

## Ergebnis

Gib ein maschinenlesbares JSON-Urteil nach [references/urteil-schema.json](references/urteil-schema.json) zurück. Jede Beanstandung enthält exakte Aussage/Entscheidung, Problem, überprüfbare Fundstelle, Auswirkung, begründeten Schweregrad und Korrektur samt Nachprüfung. Unsichere Vermutungen deutlich kennzeichnen. Kein Finding erfinden, um streng zu wirken.

`BESTANDEN` gilt nur für den tatsächlich geprüften benannten Umfang bei erfüllten zugehörigen Voraussetzungen. `NICHT_BESTANDEN` setzt einen ausgeführten negativen Check voraus; fehlende Prüfung ist `NICHT_GEPRÜFT`, fehlende Voraussetzung `BLOCKIERT`, spätere Prüfung `IN_DIESER_PHASE_NICHT_ERFORDERLICH`. Offene erhebliche Findings blockieren ihre abhängige Aussage/Funktion. Das Urteil selbst beweist keine wissenschaftliche Gültigkeit.

Protokolliere tatsächliche Modell-/Werkzeugangaben aus verfügbarer Laufzeit und Auftrag, ursprünglichen Prompt und Inputhashes. Keine erfundene konkrete Modellrevision oder Anbieterregel. Ein Alias ist keine nachgewiesene Modellversion; eine Codex-Sitzung kein Claude-Lauf. Interne Vorgaben bleiben unbekannt. Technische Prüflogs und ursprüngliche Bewertungen unverändert erhalten.

Keine Commits, Pushes, Merges, Nachrichten, Kontoeinrichtung oder Freigaben ohne den ausdrücklich dafür geltenden Auftrag. Dieser Prozess heißt KI-Audit, nicht akademisches Peer Review oder Garantie wissenschaftlicher Neutralität.
