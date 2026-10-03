# Codex-Erstprüfung METHODOLOGY-PAGE-001/v1

Erstprüfung am 3. Oktober 2026, 13:17:41 bis 13:22:55 UTC. Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`; Branch laut Auftrag `research/life-93-night-20261003`, wegen des Git-Ausschlusses nicht unabhängig geprüft. Keine Autorenberichte, anderen Reviewer, Zustands-/Handoffdateien oder Antwortdaten als Grundlage.

**Ergebnis:** Kein blockierender inhaltlicher Widerspruch im begrenzten Scope. Zwei geringe Hinweise zur Quellenauffindbarkeit. Das ist keine methodische Validierung, empirische Abnahme oder Releasefreigabe.

## Befunde

### MP001 – gering, nicht blockierend: aktueller Planbeleg fehlt als Seitenlink

- Fundstelle: `web/src/app/pages/methodology/methodology.html:42–47`, `147–165`, `202–224`; Projektlink auf die Methodik in `web/src/app/pages/project/project.html:102`.
- Beleg: Die 43 Einzelangaben und das Auswertungsverfahren sind durch `docs/empirie-plan-v2.entwurf.md:15–26,40–50` gebunden. Die Methodikseite verlinkt Originalinstrumente und externe Methoden, aber weder diesen konkreten Entwurf noch die aktuelle Themenmatrix. Der Projektstand verlinkt bei `:216–220` den allgemeineren Erweiterungsplan. Die konkreten Entscheidungen sind dadurch aus der Methodikseite schwer nachzuprüfen. Die Zahl 43 ist korrekt; dies ist kein erfundener Inhaltsbefund.
- Minimale Korrektur: Einen beschreibenden Link zum konkreten Empirieentwurf ergänzen, gegebenenfalls daneben zur Themenmatrix. Beide weiterhin ausdrücklich als Entwurf kennzeichnen.

### MP002 – gering, nicht blockierend: Varianzfundstelle genauer bezeichnen

- Fundstelle: `web/src/app/pages/methodology/methodology.html:158–165`, Link auf `survey.pdf#page=100`.
- Beleg: Das live abgerufene CRAN-Manual ist tatsächlich Version 4.5. PDF-Seite 100 beginnt mit einem Beispiel der vorherigen Funktion; dort startet erst darunter `svyCprod`. Die Erklärung zu PSU-Summen, Stratumzentrierung und ursprünglicher Designbasis steht auf Seite 101. Der gebundene Plan nennt zusätzlich `surveysummary` und `svydesign` (`docs/empirie-plan-v2.entwurf.md:48`). Kein Widerspruch zum geplanten optionalen Verfahren festgestellt.
- Minimale Korrektur: Linktext etwa „survey-Manual v4.5, Abschnitt svyCprod, Seiten 100–101“ und Sprung auf Seite 101. Für die Quotientenlinearisierung können die weiteren bereits gebundenen Abschnitte genannt werden. Keine zusätzliche Güteaussage ergänzen.

## Inhalt und Gestaltung

- Die 43 Einzelangaben ergeben sich aus der gebundenen Auswahl. Acht Themen bleiben Ordnungsrubriken; die Seite behauptet keinen latenten Gesamtfaktor, fertigen Test oder Neutralitätsnachweis (`methodology.html:35–47,175–179`; Empirieplan `:7–26,54`).
- Die fünf historischen ESS-Referenzen, Ausgaben, Zeiten und Modi stimmen mit der gebundenen Matrix überein (`abdeckung-v2.md:38–43`). ESS10-SC bleibt von der Interviewausgabe getrennt. 15+ unabhängig von Staatsangehörigkeit, Wahlberechtigten-Abgrenzung, ESS8-Münchenlücke und fehlende 2026-Norm sind sichtbar. Die Feldangaben wurden gegen die Matrix geprüft, nicht erneut vollständig aus allen Länderberichten erhoben.
- Bekannte v1-A/B-Antworten gelten nicht als neue unabhängige Bestätigung. Wählergruppen werden als noch nicht freigegebener Weg mit eigenen Nachweisen beschrieben, nicht als unmöglich oder fertig. Keine neue Ergebnisbehauptung (`:182–191`; Empirieplan `:32–36`).
- Gewichtete Kategoriequotienten, gültige fragebezogene Nenner und getrennte Sensitivitäten passen zum Plan. Die öffentliche ESS-Gewichtungsanleitung bestätigt die Designanpassung innerhalb von `pspwght`; kein erneutes Multiplizieren mit `dweight`. Optionaler SE bleibt auf feste Gewichte/Designannahmen bedingt. Fehlender SE wird nicht als numerische Null behandelt; persönliche Intervalle sind ausgeschlossen. Die konkrete `standardError: null`-Implementierung war nicht Gegenstand dieses Pakets.
- ESS-Dokumentation CC BY-SA 4.0 und Daten CC BY-NC-SA 4.0 sind korrekt getrennt. Attribution und Veröffentlichung bleiben artefaktbezogen zu prüfen; keine pauschale juristische Freigabe. GLES/ISSP bleiben Ergänzungswege mit offenen konkreten Rechten (`lizenzen.md:7–29`; offizieller ESS-Disclaimer).
- Claude-Schlusskontrolle, Verständnistests und menschliche Gestaltung-/Releasefreigaben bleiben offen. Keine persönlich benannte Verantwortlichkeit wird neu eingeführt. Die eigene Auswahlverantwortung und Fehlergrenze derselben Codex-Modellfamilie sind sichtbar. Sachlicher Ton ohne Anrede, moralische Etikettierung oder amtliche Selbstzuschreibung; kein relevanter Unslop-Befund.
- Statisch entspricht die Komponente der vorhandenen Dokumentseitenart: ein H1, ein Lead, sechs passende ToC-Ziele, Routerfragmente, vorhandenes Raster, keine eigenen Farb-/Fontwerte, Flaggen, Antwortdaten oder Teststart-Steuerelemente. Die Route und der bestehende Navigationstest decken den Projektlink, Titel und Abschnittsfokus im Quelltext ab. Ihr Laufzeitergebnis wurde hier nicht geprüft.

## Ausgeführte Checks und Grenzen

Alle zwölf SHA-256-Pins stimmen vor und nach der Prüfung; das Manifest ist unverändert. Zeiten: vor `13:17:56.554142`, nach `13:22:55.028224` UTC. Manifest-SHA-256: `d3d10b2208688fccd770f9477c39a2ecd9f7fc3f44c087d1fbc02087b7f4b1b6`.

Prozesse: `pwd`, `nl`, `sed`, `cat`, `python3` für Hash-/HTML-/Katalogprüfungen und genaue HTTP-Abrufe, `pdftotext`, `pdftoppm`; zusätzlich Uhr-, Web- und Bildansichttools. Das Handbuch wurde vollständig gelesen, Unslop angewandt. Abrufe ab `13:19:16` UTC: fünf deutsche ESS-Fragebogen-PDFs alle HTTP 200 und bytegleich zu ihren Kataloghashes; Krosnick 1999 bytegleich zum Hash in `messformen-v2.entwurf.md:39`, nur die dort genannten Seiten geprüft; survey v4.5 nur Cover und genannte Varianzfundstelle. Lizenz-/Gewichtungsoriginale erfolgreich direkt abgerufen, nachdem der Webtransport 502 gemeldet hatte. Acht weitere genaue Primärlinks einschließlich beider DOI per HEAD erfolgreich; das ESS-Portal lieferte im Webtool keine lesbare Dokumentation. Keine neue DOI-/Portal-Inhaltsidentität daraus abgeleitet.

Artefakte stehen in `outputs/loop/methodology-page-001-review/`: Pinprüfungen, statische Quellenbindungen, HTTP-Belege, begrenzte Dokumentauszüge und `execution-scope.json`. Keine ESS-Frequenz-/Ergebnisbereiche oder privaten Datensätze abgefragt. Der bibliografische und Versionsabgleich ist kein vollständiger empirischer Gleichheitsnachweis. Kein Vollcheck, ausgeführter Navigationstest, Browseraudit, Server, Installation, Git oder weiterer Agent; diese technischen Arbeiten bleiben bei Root. Gemeinsame Fehler innerhalb der Codex-Modellfamilie bleiben möglich.
