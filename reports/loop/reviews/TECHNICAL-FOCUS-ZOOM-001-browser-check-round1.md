# TECHNICAL-FOCUS-ZOOM-001: gezielte Code-Nachprüfung, Runde 1

Datum: 2026-10-03, 18:27:04 UTC. Prüferrolle: derselbe getrennte Codex-Subagent für den technischen Browser-Prüflauf. Keine andere Modellfamilie und keine methodische Gegenprüfung.

Geprüfte Datei: `scripts/check-research-browser.mjs`.

SHA-256: `9d436aa1fa8547acd9a77d94953a15b151af5271be925d0c446491200d17b8e6`.

## Urteil

Die vier konkreten Befunde des Erstberichts sind im begrenzten technischen Prüfumfang behoben. Die Code-Nachprüfung besteht. Es gibt keinen weiteren blockierenden Codebefund zu diesen Korrekturen.

Der unveränderte Erstbericht bleibt unter `TECHNICAL-FOCUS-ZOOM-001-browser-check-first.md` erhalten. Diese Runde prüft nur seine vier Befunde und die ausdrücklich gemeldeten Ergänzungen für Radio-, Zurücknavigation und Screenshots. Ich habe keine anderen Reviewerberichte gelesen und keinen Browser, Server oder Testlauf gestartet. Ob die neue Skriptfassung tatsächlich durchläuft und die Bilder brauchbar sind, bleibt Gegenstand der unabhängigen Ausführung und Sichtprüfung des Koordinators.

## Die vier Korrekturen

| Erstbefund | Codebeleg in der neuen Fassung | Ergebnis |
| --- | --- | --- |
| Fehlende Prüfung der normalen Fokusübergabe nach Next/Skip | `291–305` wartet bei Fragen zwei bis 43 auf die fokussierte, passend beschriftete Frageüberschrift. Ihre vertikalen Grenzen müssen innerhalb des Viewports liegen. Erst danach folgen Layoutmessung und weitere Tab-Ereignisse. `358–362` wartet beim Ergebniswechsel auf die fokussierte H1 „Ergebnisentwurf“. | Behoben. Ein Tab-Umlauf kann die ausgefallene Übergabe nun nicht mehr verdecken. Der Skip-Wechsel nach Frage drei wird am Anfang des Durchlaufs für Frage vier direkt erfasst. |
| „Expanded“ ohne nachgewiesenen offenen Quellenzustand | `264` prüft den offenen äußeren Fragequellenabschnitt. `265–270` öffnet alle darin gefundenen verschachtelten Quellenabschnitte per Tastatur und prüft jeweils `open`. `276` bestätigt das Schließen des äußeren Abschnitts. `393` und `398` prüfen Öffnen und Schließen der Gruppenquellen. `405–410` prüft die geöffneten Ergebnisquellen vor Layout, axe und Screenshot. | Behoben für die getesteten Quellenabschnitte. Die Etiketten „expanded“ beruhen nun auf einem tatsächlichen offenen Zustand. |
| Gruppenauswahl ohne belegten Renderzustand | `372–382` wartet auf einen nichtleeren Gruppenwert und den zum gewählten Optionslabel passenden gerenderten Gruppenhinweis. `383–389` wartet auf eine sichtbare `.group-reference` und kontrolliert darin die gewählte Studie und das gewählte Gruppenlabel. | Behoben. Eine Auswahl mit wirkungslosem Change-Handler besteht nicht mehr allein wegen der vorhandenen Studienquellen. |
| Transparenter oder kontrastloser Fokusrahmen konnte bestehen | `103–129` erfasst Rahmenalpha und berechnet den Kontrast zum nächsten nichttransparenten Elternhintergrund. `141–142` verlangt Alpha eins und mindestens 3:1 Kontrast. | Behoben für die vorhandenen opaken RGB-Farbflächen und die benannte Farbheuristik. Sichtbarkeit und Überdeckung des gezeichneten Rahmens bleiben Teil der visuellen Prüfung. |

Die Ergebnis-H1 erhält eine direkte Fokusprüfung. Das Skript prüft ihre Viewportgrenzen nicht ausdrücklich. Die Bounds-Prüfung für die 42 normalen Frageübergänge erfasst die vertikale Lage der Überschrift; Dokumentüberlauf wird davon getrennt kontrolliert. Diese Reichweite passt zur begrenzten Aussage des Prüflaufs und ist kein Nachweis vollständiger Sichtbarkeit aller Bedienelemente.

Die Ergebnisquellen werden nach dem Screenshot mit Enter geschlossen, ohne zusätzlich `open === false` zu prüfen (`414`). Damit besteht die neue Assertion für „expanded“; eine ausdrücklich bestandene Ergebnisquellen-Schließprüfung darf daraus nicht abgeleitet werden.

## Ergänzte Bedienung und Screenshots

`226–240` wählt per Space eine Radiooption, verändert die Auswahl mit ArrowDown und stellt sie mit ArrowUp wieder her. Der Code vergleicht die ausgewählten Originalcodes und prüft anschließend den Tastaturfokus. Diese Ergänzung nutzt echte Keyboard-Ereignisse und erweitert den früheren reinen Space-Durchlauf sinnvoll.

`314–335` erreicht „Zur vorherigen Frage“ per Tab und Enter. Es wartet beim Rückweg von Frage zwei auf die fokussierte Überschrift von Frage eins und anschließend wieder auf die fokussierte Überschrift von Frage zwei. Die neue Rückwärtsnavigation ist direkt belegt. Die früheren Grenzen einer vollständigen Prüfung aller Tab-Zwischenziele bleiben bestehen.

`48` erzeugt eine CDP-Sitzung für dieselbe Seite. `173–184` speichert Screenshots über `Page.captureScreenshot` mit `fromSurface: false` und `captureBeyondViewport: false`. Der Screenshotweg nutzt keine CSS-Clipberechnung aus Playwright und nimmt den aktuellen Viewport auf. Dies ist ein nachvollziehbarer Codewechsel für den vom Koordinator gemeldeten Fehler, dass Surface-Aufnahmen bei tatsächlichem Tab-Zoom leer waren. Ich habe weder die leere Probe noch die neuen Bilder selbst angesehen und bestätige hier keine Pixelbeobachtung.

Eine geringe Diagnosegrenze bleibt: Der Fehlerpfad nutzt für `failure.png` weiterhin `page.screenshot()` (`456`). Bei einem Fehler im 200-Prozent-Lauf kann diese Aufnahme laut der gemeldeten Surface-Beobachtung leer sein. Der Lauf erhält trotzdem Exitcode eins, Fehlertext und einen FAIL-Bericht; die Erfolgsentscheidung wird dadurch nicht verfälscht. Ein Wechsel auch dieser Diagnoseaufnahme auf den neuen CDP-Weg wäre konsistent.

## Reichweite und offene Abnahmen

Die Bedingungen sind unverändert: fünf Fenstergrößen bei 100 Prozent und vier Desktop-/Tabletfenster bei echtem 200-Prozent-Browserzoom (`186–196`). Ein 200-Prozent-Mobilfenster oder mobiles Pinch-Zoom wird nicht geprüft. Chrome-Zoom, DPR, CSS-Zoom und Visual-Viewport-Scale bleiben getrennt beobachtet.

Der Kontrastwert bezieht sich auf den nächsten Elternhintergrund, dessen berechnete Farbe nicht vollständig transparent ist. Er ist keine Pixelmessung des tatsächlichen Rahmens und keine allgemeine Behandlung von halbtransparenten Flächen, überlagernden Elementen oder Hintergrundbildern. `inViewport` verlangt weiterhin nur eine Überschneidung des Bedienelements mit dem Viewport. Der Bericht muss diese automatische Kontrolle von der visuellen Sichtbarkeit unterscheiden.

Die Einzelquellen betreffen weiterhin die erste Frage und den ersten Ergebniseintrag. Die verschachtelten Quellen der ersten Frage sind nun zusätzlich offen. Weitere Quellen-/Gruppenvarianten, komplette Tastaturpfade und eine vollständige WCAG-Abnahme werden damit nicht für bestanden erklärt. axe-`incomplete` braucht weiterhin Bewertung.

Nur dieser neue Nachprüfbericht wurde geschrieben. Keine Rohdaten oder privaten Analyseausgaben wurden gelesen. `pnpm check`, tatsächliche Browserausführung und die Sichtprüfung liegen beim Koordinator. Wissenschaftliche und menschliche Abnahmen bleiben von dieser Code-Nachprüfung getrennt.
