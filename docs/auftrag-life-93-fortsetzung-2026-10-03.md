# LIFE-93: Nachtrag zur Fortsetzung am 2026-10-03

Steven hat nach dem Haltepunkt `610543fa34d3a9772403c8e38f34f23645d692d8` die Fortsetzung im bestehenden Thread und Worktree beauftragt. Dieser Nachtrag ersetzt die widersprechenden Ablaufvorgaben des [historischen Vollauftrags](auftrag-life-93-2026-10-03.md). Der historische Auftrag, Erstberichte, Findings und Korrekturrunden bleiben erhalten.

## Umfang und Koordination

Der Auftrag umfasst Recherche, empirische Analyse, Messmodell, Methodenbericht und die darauf aufbauende Website bis zum vollständig vorbereiteten Stand für Claudes abschließende Gesamtkontrolle. Nur ein Koordinator schreibt die gemeinsamen Forschungsdateien. Der vorherige Lauf ist laut Checkpoint angehalten; bei Wiederaufnahme waren Worktree und Remote sauber auf dem genannten Commit und im aktuellen Agentregister nur der Koordinator aktiv.

Arbeitsfassung: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`, Branch `research/life-93-night-20261003`, Thread `6975a99d-529e-40d2-b9ec-e06c85c1dc94`. Werkzeugaufrufe verwenden explizite Worktree-Pfade; die T3-Threadbindung zeigt weiterhin den ursprünglichen Checkout. Sie wird nicht durch Shell-`cd` geändert. Die dort vorhandenen fremden Änderungen bleiben unberührt.

## Geänderte Prüfregeln

- Claude ist keine Voraussetzung der Hauptarbeit. Keine weiteren Claude-Aufrufe, Zugriffsversuche, Authentifizierungsarbeiten oder Wartezeiten. Steven veranlasst die Schlusskontrolle selbst. Alle noch fehlenden Claude-Prüfungen sind **verschoben und nicht bestanden**.
- Die zuvor verlangten getrennten Codex-/Claude-Erstbewertungen werden in diesem Durchlauf durch zwei getrennte Codex-Erstbewertungen ersetzt. Beide gehören derselben Modellfamilie an und können gemeinsame Fehlerquellen haben. Getrennter Kontext garantiert weder unabhängige Modellvorgaben noch absolute politische Neutralität.
- Normale inhaltliche Pakete erhalten einen passenden Codex-Prüfagenten. An drei Übergängen prüfen zwei getrennte Agents: vor empirischer Entwicklung, vor Zugriff auf bestätigende Daten und vor Übertragung der Analyse in Ergebnisaussagen. Rollen: Methoden/Reproduzierbarkeit sowie Quellen/Konstrukte/Interpretationen/politische Fairness. Das dauerhafte Fünfergremium und der zusätzliche Juror entfallen.
- Reviewer erhalten frischen, begrenzten Kontext, konkrete Prüffassung und Anforderungen. Ersturteile ohne andere Reviewerurteile oder vorweggenommene Autorenverteidigung. Kein Schreiben gemeinsamer Forschungsdateien. Originalberichte bleiben erhalten. Das gemeinsame Dateisystem ist keine technische Isolation.
- Korrekturen gezielt nachprüfen, gegebenenfalls beim bisherigen Reviewer. Neue Gesamtaudits nur bei wesentlichen Methoden- oder Aussagenänderungen. Zustandsupdates, Commitnummern, Formatierung und reine Dokumentationskorrekturen lösen keine fachliche Neuaudits aus. Gültige vorhandene Reviews weiterverwenden. Kompakte Prüfpakete mit notwendigen Artefakten und Versionsreferenzen statt vollständiger Verzeichniskopien.
- Erhebliche Fehler blockieren nur betroffene Aussagen/Funktionen. Stil und zusätzliche Wunschprüfungen blockieren den Fortschritt nicht. Nach höchstens zwei erfolglosen Reparaturrunden die betroffene Aussage/Funktion begründet begrenzen oder entfernen; andernfalls genau diesen Teil blockiert lassen. Kein weiterer Zyklus ohne neue Evidenz oder überprüfbare Verbesserung.

## Wissenschaftlicher Ablauf

Vorhandene Inventare und Quellenprüfungen nutzen. Vor Empirie die Entscheidungen zu Version, Design, Gewichten, Missing, Konstrukten und Verfahren schließen. Die einfachste vertretbare und tatsächlich ausführbare Lösung wählen. Zusätzliche Dimensionen/Funktionen nur mit ausreichender Evidenz; begründeter Ausschluss aus der ersten Fassung bleibt möglich. Quellen, Ergebnisse und Validierung niemals erfinden.

Nach den vorgesehenen Codex-Prüfungen darf der Plan ohne Claude oder zusätzliche persönliche Statistik-Abnahme festgeschrieben werden. Plan, Bewertungskriterien und Erwartungsmodell vor abhängiger Analyse fixieren. B und gesperrte Vergleichsvariablen bis zum vorgesehenen Schritt zurückhalten, auch gegenüber Subagents. Änderungen nach Dateneinsicht kennzeichnen. Synthetische Tests ersetzen keine empirischen Untersuchungen. Unsicherheit nur mit begründeter Berechnung und Bedeutung anzeigen.

Überprüfbare Maßnahmen für politische Fairness sind vollständige Quellenzuordnung, begründete Ein-/Ausschlüsse, getrennte Item-/Texturteile, Gegenbelege, unveränderte Originalformulierungen und benannte Interpretationsgrenzen. Diese Maßnahmen beweisen keine absolute Neutralität oder Unabhängigkeit von unbekannten Modellvorgaben.

Vor Website-Arbeit `handbuch.md` vollständig lesen, Gestaltung erhalten, nur tragfähige Ergebnisse übertragen. Berechnung, Bedienung, Desktop-/Smartphone-Browser und Barrierefreiheit passend prüfen. Offene Designentscheidungen, reale menschliche Verständnistests und persönliche Releasefreigaben bleiben ausstehend; unabhängige Aufgaben währenddessen weiterbearbeiten.

## Sicherung und Abschluss

Nach abgeschlossenen Paketen und spätestens alle 30 Minuten bei Änderungen Zustand aktualisieren, eigene Änderungen committen, regulär auf den Arbeitsbranch pushen und den Remote-Commit prüfen. Unfertiges als WIP. Keine Secrets, privaten Antworten oder unveröffentlichten Rohdaten in Commits. Keine globalen Installationen, destruktiven Bereinigungen, Force-Pushes, automatischen Merges, Deployments ohne Freigabe oder Änderungen anderer Projekte.

Bei Nutzungslimit soweit möglich sichern und einen eindeutigen nächsten Schritt hinterlassen. Bei unterstützter T3-Fortsetzung zuerst Checkpoint lesen, nicht neu beginnen. Den Lauf fortsetzen, bis alle derzeit ausführbaren Aufgaben abgeschlossen sind oder nur echte externe Voraussetzungen verbleiben. Der Abschluss benennt reproduzierbare Ergebnisse, Grenzen, erforderliche Freigaben sowie ausstehende Claude- und Menschenprüfungen. Dokumentation bleibt knapp, tragende Aussagen führen zu Fundstelle oder reproduzierbarer Auswertung.
