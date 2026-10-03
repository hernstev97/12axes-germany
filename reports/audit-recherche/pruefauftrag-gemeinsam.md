# Gemeinsame Prüfgrundlage für das KI-Audit LIFE-93

Auftrag vom 2026-10-03. Alle fünf Erstprüfer erhalten diese Datei, dieselbe aktuelle Issue-Beschreibung und dieselbe eingefrorene Forschungsfassung. Dies ist ein KI-Audit, kein akademisches Peer Review und keine Garantie wissenschaftlicher Gültigkeit.

## Eingaben und Grenzen

- Forschungsgrundlage: `reports/audit-recherche/ausgangsfassung/`. Die gleichnamigen Dokumente dort sind die alleinige zu prüfende Ausgangsfassung. Prüfsummen: `reports/audit-recherche/ausgangsmanifest.json`.
- Aktuelles Issue: `reports/audit-recherche/issue-LIFE-93.md` und das unveränderte API-Objekt in `issue-LIFE-93.json`. Der Issue-Stand wird mit aktualisiertem Zeitstempel und Hash gesichert.
- Frühere Nutzerentscheidung: vorerst nur CodeRabbit, methodische Freigabe offen, kein Claude-Setup. Der aktuelle explizite Auftrag autorisiert diese Subagents; er ersetzt keine andere Modellfamilie und keine späteren getrennten Item-Erstbewertungen.
- Ausgangslage: öffentliche Quellenrecherche, Prüfregeln und Analyseplan-Entwurf. Noch kein Fragenkatalog, endgültiges Modell, ESS-Auswertung oder Testergebnis. Dateieingang beschränkte sich auf Hash, Header und globale Metadaten. Spätere Analysen sind spätere Anforderungen, keine bereits gescheiterten Prüfungen.
- Zugriff nur auf öffentliche Originalquellen und diese Forschungsfassung. ESS-Rohantworten und Personenkennungen nicht lesen oder ausgeben. Keine statistische Antwortanalyse, kein Split, keine Tags, kein PR, keine externe Nachricht.
- Während der unabhängigen Erstprüfung die Forschungsgrundlage und andere Projektdateien nicht ändern. Nur deine eigene Berichtsdatei unter `reports/audit-recherche/` schreiben. Zusätzliche Downloads/Arbeitsdateien ausschließlich unter deinem eigenen `/tmp/life93-audit-reviewer-N/`.
- Die anderen Reviewerberichte, eine spätere Autorantwort und Korrekturen nicht lesen. Keine Nachrichten an andere Reviewer, keine gemeinsame Diskussion und keine eigenen Subagents. Nutze einen isolierten Erstauftrag ohne Gesprächshistorie.
- Das Tool erlaubt einschließlich Hauptagent vier gleichzeitig aktive Agents. Die fünf Erstprüfer laufen deshalb in zwei Wellen, sehen aber dieselbe eingefrorene Fassung. Zeitlich versetzte Ausführung ist keine inhaltliche Unabhängigkeitsgarantie.
- Geerbtes Elternmodell laut zugänglicher Laufzeit: GPT-6.1-Sol, Slug `gpt-6.1-sol`, Reasoning `ultra`. Keine andere Modellfamilie wird behauptet. Nicht zugängliche interne Modellvorgaben/Versionen sind unbekannt. Dokumentiere die tatsächlich verfügbare Modellangabe, Werkzeuge und benutzten Werkzeuge in deinem Bericht.

## Prüfprinzipien

Suche aktiv Fehler und Gegenbelege. Erfinde keine Kritik, um streng zu wirken. Es gibt keine Sollzahl an Findings und keine gewünschte politische Schlussfolgerung. Übereinstimmung zwischen Agents ist kein Wahrheitsbeweis.

Prüfe zentrale Originalquellen selbst. Quellenzugang, geprüfte Seiten/Abschnitte, aktuelle Version, Datum und Einschränkungen dokumentieren. Nicht zugängliche Volltexte nicht als vollständig geprüft behandeln. Technische Konsistenz, Reliabilität, Validität, Neutralität und Verständlichkeit unterscheiden. Textmetriken oder simulierte Perspektiven beweisen keine Neutralität. Vergleichsfälle müssen inhaltlich vergleichbar sein; sachlich begründete Unterschiede bleiben möglich.

Eine Prüfung darf nur als bestanden gelten, wenn du sie wirklich ausgeführt hast und ein Ergebnis dokumentierst. Trenne Quellenbefund, eigene Modellannahme, empirisches Ergebnis, Interpretation, Vermutung, offene Frage, spätere Anforderung und tatsächlich ausgeführte Prüfung. Fehlende Evidenz nicht durch sprachliche Sicherheit ersetzen.

## Berichtsformat

Schreibe auf Deutsch. Benutze die lokale unslop-Skill, falls nötig; Änderungen nur in deiner Berichtsdatei. Dein Bericht enthält:
1. Identität/Rolle, Beginn/Ende, tatsächliche Modellinformationen und unbekannte interne Vorgaben.
2. Verwendete Eingabefassung/Hashprüfung, verfügbare und benutzte Werkzeuge, selbst geprüfte Quellen mit präzisen Fundstellen und Zugangsstatus.
3. Tatsächlich ausgeführte Untersuchungen mit Ergebnis; glaubwürdige Aussagen, offene Evidenz und spätere Anforderungen klar getrennt.
4. Findings mit stabilen IDs `R<N>-F<NN>`. Für jedes Finding:
   - exakt betroffene Aussage/Entscheidung mit Dateipfad und Zeile bzw. ID;
   - Status (nachgewiesenes Problem / begründete Unsicherheit / offene Frage / spätere Anforderung);
   - Problem und überprüfbarer Beleg mit Originalquelle/Fundstelle bzw. reproduzierbarem Befehl und Ergebnis;
   - Schweregrad und Begründung: erheblich blockiert eine darauf aufbauende Aussage/Funktion, mittel beeinträchtigt Nachprüfbarkeit oder begrenzte Aussage, gering redaktionell;
   - Folgen für Forschung oder Testergebnis;
   - konkrete Korrektur;
   - konkrete erneute Prüfung, die die Korrektur bestätigen kann.
5. Grenzen deiner Prüfung und begründete nächste erlaubte Arbeit. Keine Gesamtfreigabe, falls entscheidende Evidenz fehlt.

Schließe den Bericht vollständig ab und sende dem Hauptagent erst danach den Pfad, SHA-256, Kurzbefund und offen gebliebene Prüfungen. Der Hauptagent führt Findings erst zusammen, wenn alle fünf unabhängigen Berichte abgeschlossen sind.

