# Arbeit in diesem Repository

Lies vor Änderungen `docs/project.md`. Vor jeder Arbeit an Oberfläche, Bedienung, Bildern oder sichtbaren Texten `docs/handbuch.md` vollständig lesen und befolgen; es regelt Gestaltung, Texte, Bilder, Barrierefreiheit und den Prüfablauf.

Der aktuelle Auftrag umfasst Recherche, empirische Analyse, Messmodell, Methodenbericht und Website bis zum vorbereiteten Stand für die abschließende Claude-Kontrolle. Maßgeblich sind der aktuelle `docs/auftrag-life-93-breite-2026-10-03.md` und die nicht widersprechenden Regeln des vorherigen Fortsetzungsnachtrags. Lies dafür zusätzlich `docs/pruefregeln.md`, `docs/analyseplan.md`, `docs/belegregister.md` und `docs/entscheidungen.md`.

Claude entfällt als Voraussetzung der Hauptarbeit. Keine weiteren Claude-Zugriffsversuche, Authentifizierungsarbeiten oder Wartezeiten. Steven veranlasst die abschließende Kontrolle. Fehlende Claude-Prüfungen bleiben verschoben und niemals bestanden. Zwei getrennte Codex-Erstbewertungen ersetzen in diesem Durchlauf die früheren Codex-/Claude-Erstbewertungen. Gleiche Modellfamilie und gemeinsame mögliche Fehlerquellen ausdrücklich nennen.

Keine Fragen, Dimensionen, Scores, Vergleichswerte oder wissenschaftlichen Güteaussagen erfinden. Kein sichtbarer Teststart, bevor ein tatsächlich freigegebener Test existiert. Geplante Funktionen als geplant beschreiben. CodeRabbit-Reviews und technische CI nicht als methodische Validierung ausgeben.

ESS-Rohdaten gehören nur nach `data/raw/`. Sie werden weder committed noch in die Webapp oder CI kopiert. Keine Rohdatenzeilen oder Personenkennungen in Agent-Aufträge, Tool-Ausgaben oder PR-Kommentare übernehmen. Auch lokale Zwischendaten bleiben außerhalb von Git, bis ihre Veröffentlichung ausdrücklich geprüft wurde. Lizenzbedingungen für Daten und Dokumentation unterscheiden; `docs/lizenzen.md` beachten.

Öffentliche Dokumentation und Literatur dürfen recherchiert werden. Keine endgültige Item-/Modellentscheidung, ESS-Analyse, Entblindung oder Präregistrierungs-/Modell-Tags, bevor die erforderlichen Entscheidungen und Abnahmen vorliegen. Der alte Empirieplanv1 ist unverändert historische Festschreibung. Für Erweiterungen gilt `docs/erweiterungsplan-v2.entwurf.md` als Entwurf ohne Datenfreigabe. Quellenversionen, präzise Fundstellen, Zugriffe und Grenzen im Belegregister, Quellenkatalog und KI-Protokoll festhalten. Ausgefallene oder nicht durchgeführte Prüfungen bleiben offen.

`skills.yaml` und `.agents/skills/` werden durch die persönliche Skills CLI verwaltet. Synchronisierte Skills hier nicht von Hand bearbeiten. Relevante Skills vor ihrer Anwendung lesen.

Nach Änderungen `pnpm check` ausführen. UI-Änderungen zusätzlich im Browser auf Desktop- und Smartphone-Breite prüfen. Technische Checks, Browserbeobachtungen und wissenschaftliche Abnahmen getrennt berichten.

Änderungen an Designrichtung oder Produktumfang mit Steven abstimmen. Keine Deployment- oder Merge-Freigabe aus dem Auftrag zur lokalen Repository-Grundlage ableiten.

Das historische Fünf-Agent-Audit und der Jurorbericht bleiben unverändert erhalten. Für die Fortsetzung gilt: normale inhaltliche Pakete erhalten einen passenden Codex-Prüfagenten; vor empirischer Entwicklung, vor B-Zugriff und vor Ergebnisaussagen zwei getrennte Agents für Methoden/Reproduzierbarkeit und Quellen/Konstrukte/Interpretationen/politische Fairness. Kein dauerhaftes Fünfergremium oder zusätzlicher Juror. Frischer begrenzter Kontext, gleiche Prüffassung, keine anderen Ersturteile oder vorweggenommene Verteidigung. Reviewer schreiben keine gemeinsamen Forschungsdateien. Gezielte Korrekturprüfung statt erneutem Gesamtaudit; reiner Zustand/Format/Commit/Dokumentationsabgleich löst keine fachliche Neuprüfung aus. Nach höchstens zwei erfolglosen Runden betroffene Aussage/Funktion begründet begrenzen oder entfernen, sonst genau diesen Teil blockiert lassen.

Vor Fortsetzung `docs/auftrag-life-93-2026-10-03.md`, den datierten Nachtrag, `docs/arbeitsloop.md` und den Checkpoint lesen. Historische Vorgaben bleiben Belege, der Nachtrag hat bei Widerspruch Vorrang. Die Phase-0-Festschreibung darf nach den vorgesehenen Codex-Prüfungen ohne Claude oder zusätzliche persönliche Statistik-Abnahme erfolgen. Plan und Kriterien vor abhängigen Analysen fixieren. B und gesperrte Vergleichsvariablen bis zum vorgesehenen Schritt zurückhalten, auch gegenüber Subagents.

Nur ein schreibender Koordinator. Eigene Änderungen im bestätigten Worktree; nach Paketen und spätestens alle 30 Minuten mit Änderungen committen und den eigenen Branch verifiziert pushen. WIP kennzeichnen. Kein Push auf main, Force-Push, automatischer Merge oder Deployment ohne Freigabe.

## Aktuelle Breitenpriorität vom 3. Oktober2026

Das Hauptprodukt muss ein thematisch breites Politikprofil für Deutschland tragen. Das Neunermodul erfüllt dieses Ziel nicht allein. Wirtschaft/Verteilung und Demokratie/politische Autorität ausdrücklich untersuchen; weitere unterschiedliche Gegenstände substanziell abdecken. ESS11 ist keine Produktobergrenze: GLES, weitere ESS-Runden und gegebenenfalls ISSP samt tatsächlichen Fragen/Versionen/Rechten/Eignung prüfen. Themenrubriken sind keine automatisch beschlossenen Dimensionen. Begründete Einzelpräferenzen und formative Ansätze zulassen; keine allgemeine Drei-Item-Mindestregel. Verschiedene Studien nicht zu gemeinsamen Personen oder ungeprüften Gesamtfaktoren zusammenfügen.

Die Fortsetzung der alten B-/FULL-/Norm-/Gruppenfolge ist angehalten; alte Gates verleihen keine aktuelle Erlaubnis. Historische Forschungsartefakte/Tags unverändert erhalten. Neue Abdeckung, Auswahl und Bewertung bekommen einen separaten v2-Plan vor ihren abhängigen Analysen; vorherige Einsicht darf nicht als unberührt umbenannt werden. Fehlende Gesamtbreite bleibt ungelöstes Produktziel.

Zunächst zwei frische getrennte Autoren für Daten/Instrumente und Themenrahmen/Auswahlverzerrungen. Sie erhalten begrenzten Quellenkontext ohne Antwortergebnisse oder vorgegebene Schlussfolgerungen; Koordinationszustand, Zugriffsbericht und frühere empirische Ergebnisse liest nur Root. Danach vereinfachten Prüfloop weiterführen. Agentenübereinstimmung ist kein Neutralitätsnachweis.
