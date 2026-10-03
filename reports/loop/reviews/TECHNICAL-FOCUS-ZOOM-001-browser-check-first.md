# TECHNICAL-FOCUS-ZOOM-001: Browser-Prüflauf, Ersturteil

Datum: 2026-10-03, 18:23:55 UTC. Prüferrolle: getrennter Codex-Subagent für den technischen Browser-Prüflauf. Keine andere Modellfamilie und keine methodische Gegenprüfung.

Geprüfte Datei: `scripts/check-research-browser.mjs`.

SHA-256: `f03b2431a4e47383da292d7aa53271be09d61faa316a64e7b029777a9ca63b77`.

## Urteil

Korrektur nötig. Das Skript nutzt tatsächlichen Browserzoom und echte Tastatureingaben. Es deckt die neue Fokusübergabe nach jedem Fragewechsel jedoch nicht zuverlässig ab. Außerdem können Prüfungen mit dem Etikett „expanded“ und der ausgewählte Gruppenvergleich bestehen, ohne dass der jeweils beabsichtigte Zustand nachgewiesen wurde. Ein erfolgreicher Skriptlauf belegt deshalb noch nicht alle benannten Bedienzustände.

Dies ist eine statische Codeprüfung. Ich habe keinen Browser, Server, Testlauf oder Installationsvorgang gestartet und keine Runtime-Ergebnisse anderer Agents gelesen. Ob die aktuelle Oberfläche diese Fehler tatsächlich zeigt, entscheidet der unabhängige Browserlauf des Koordinators.

## Befunde

### P2: Die Fokusübergabe nach „nächste Frage“ und „überspringen“ kann fehlen, ohne den Lauf zu stoppen

`scripts/check-research-browser.mjs:223–255` wartet nach jedem Wechsel nur auf den Text `Frage n von 43`. Es prüft weder `document.activeElement.id === 'draft-question-title'` noch die Lage dieser Überschrift im sichtbaren Bereich. Das nächste `tabTo()` drückt bis zu 180-mal Tab und akzeptiert den irgendwann erreichten Zielknopf (`121–129`). Ein vollständiger Tab-Umlauf kann eine ausgefallene Fokusübergabe verdecken.

Konkrete falsche Erfolgssituation: Die Oberfläche aktualisiert die Frage, lässt den Fokus aber auf „Zur nächsten Frage“. Der nächste Aufruf von `tabTo()` läuft durch die übrigen Bedienelemente und erreicht später denselben Knopf wieder. Überschrift, Layout und Fokus am Knopf bestehen weiterhin. Die fehlende Übergabe zur neuen Frage bleibt unentdeckt. Dasselbe gilt für den Wechsel nach Frage drei mit „Diese Frage überspringen“.

Die Oberfläche führt diese Übergabe ausdrücklich nach dem Rendern aus, `web/src/app/policy-draft/policy-draft.ts:150–158` und `230–239`. Gerade dieser technische Vertrag sollte der Browserlauf direkt prüfen. Der entfernte Übersichtssprung prüft Fokus und vollständig sichtbare Überschrift bereits (`304–313`); der normale Ablauf tut es nicht.

Korrektur: Nach jedem Fragewechsel Text und Fokus der neuen Überschrift gemeinsam abwarten und ihre Position prüfen, bevor weitere Tab-Ereignisse folgen. Nach dem letzten Wechsel entsprechend den Fokus auf der Ergebnisüberschrift prüfen. Eine beobachtete Überschrift allein belegt kein abgeschlossenes Fokus-/Scrollverhalten.

### P2: Als aufgeklappt bezeichnete Quellen werden nicht auf ihren offenen Zustand geprüft

Nach Enter führen `210–214`, `268–273` und `275–283` Layoutprüfung, axe und Screenshot unter Bezeichnungen wie `question sources expanded` aus. Kein Ausdruck prüft das `open`-Attribut des zugehörigen `details` oder die Sichtbarkeit seines Inhalts.

Konkrete falsche Erfolgssituation: Enter erreicht das `summary`, die Öffnung bleibt aber aus. Die geschlossene Seite hat weiterhin keinen Dokumentüberlauf und kann axe bestehen. Der Bericht protokolliert trotzdem „expanded“. Screenshots erlauben dem Koordinator, diese Abweichung zu sehen; die automatische Erfolgsentscheidung erkennt sie nicht.

Korrektur: Nach Enter auf `summary.closest('details').open === true` und einen konkreten sichtbaren Inhaltsknoten warten. Vor dem späteren Weitergehen auch das Schließen bestätigen. Native `details` ändern sich normalerweise direkt; die ausdrückliche Assertion belegt den beabsichtigten Zustand und schützt vor einer Bedienregression.

### P2: Die Auswahl einer historischen Vergleichsgruppe und ihr Renderzustand werden nicht nachgewiesen

`263–267` wählt mit ArrowDown eine Studie und eine Gruppe. Das Skript wartet lediglich darauf, dass der Gruppenselektor aktiviert ist. Danach fehlt eine Assertion für seinen gewählten Wert oder den gerenderten Gruppeninhalt.

`web/src/app/policy-draft/policy-draft.html:248–279` zeigt die Quellen bereits bei gewählter Studie. Eine gewählte Gruppe ist dafür keine Voraussetzung. Wenn `(change)="setGroup($event)"` wirkungslos wäre, könnten `group-sources` und alle anschließenden Prüfungen trotzdem bestehen. Gruppenbezogene Texte und Vergleiche wären dann ungetestet. Eine zeitverzögerte Gruppenaktualisierung könnte auch erst nach der Layoutmessung eintreffen.

Korrektur: Einen nichtleeren Gruppenwert und einen dazu passenden gerenderten Gruppenhinweis abwarten. Für die Layoutprüfung einen nachweislich dargestellten Gruppenvergleich oder einen ausdrücklich erwarteten Rückhaltehinweis prüfen. Kein Referenzwert und keine Personenangabe muss dafür in den Bericht übernommen werden.

### P2: `:focus-visible` plus Rahmenmaße beweisen noch keinen sichtbaren Fokusrahmen

`90–118` prüft echten Fokus, `:focus-visible`, irgendeine Überschneidung mit dem Viewport und die Rahmenwerte `solid`, `2px`, `4px`. Die Farbe wird aufgezeichnet, aber nicht geprüft. Ein transparenter oder zum Hintergrund gleicher Rahmen erfüllt diese Assertions. Auch ein teilweise außerhalb des Viewports liegendes Element besteht `inViewport`.

Korrektur: Mindestens Transparenz als automatischen Fehler behandeln und die Prüfung ausdrücklich als Prüfung von Fokuszustand und Rahmengeometrie benennen. Die Sichtbarkeit, Kontraste und mögliche Überdeckung des Rahmens bleiben eine konkrete visuelle Prüfung der Screenshots. Vollständige Sichtbarkeit dort prüfen, wo sie zum Vertrag gehört, etwa an den Überschriften nach Fragewechseln.

## Was der Code bereits angemessen prüft

- Der Zoom nutzt `chrome.tabs.setZoomSettings`, `setZoom` und `getZoom` im Extension-Worker (`53–65`). Er ersetzt Browserzoom weder durch CSS noch durch `deviceScaleFactor`. Faktor, `devicePixelRatio`, halbierte `innerWidth`, `visualViewport.scale === 1` und `html`-Zoom `1` werden kontrolliert (`63–64`, `68–84`, `182–184`). Die DPR-Annahme passt zum Kontext ohne eigenen `deviceScaleFactor`; sie ist keine geräteunabhängige allgemeine Zoomformel.
- Das Skript erzeugt Tab, Enter, Space und ArrowDown über `page.keyboard.press`. Es setzt den Fokus der geprüften Bedienelemente nicht selbst mit `element.focus()` und ersetzt die Eingaben nicht durch `dispatchEvent()`.
- Die neun Bedingungen umfassen die fünf Handbuchbreiten bei 100 Prozent sowie vier Desktop-/Tabletfenster bei echtem 200-Prozent-Zoom (`153–163`). Jede der 43 Frageansichten erhält eine Dokumentüberlaufprüfung. Ergebnisse und Übersicht werden ebenfalls erreicht.
- Zurücksetzen wartet auf die fokussierte Frageüberschrift und prüft den deaktivierten Reset-Knopf sowie die leere Auswahl (`197–208`). Der entfernte Übersichtssprung wartet auf die letzte fokussierte Frage und prüft ihre vollständige vertikale Sichtbarkeit (`304–316`).
- Der Bericht nennt `syntheticDemonstrationOnly: true` und `realPeople: 0` (`35–36`). axe-`incomplete` wird gespeichert. Der Code gibt weder eine wissenschaftliche Abnahme noch einen Nutzertest aus.

## Grenzen auch nach den Korrekturen

Der Lauf prüft ausgewählte Fokusziele. `tabTo()` kontrolliert die dazwischen durchlaufenen Elemente nicht. Vorherige Frage, Arrow-Navigation zwischen Radiooptionen und alle Ergebnis-/Übersichtsbearbeitungsziele werden nicht vollständig als Tastaturaktionen geprüft.

Die aufgeklappten Einzelquellen betreffen nur die erste Frage und den ersten Ergebniseintrag. Die verschachtelten Quellenabschnitte in `policy-source-details.html:105–149` bleiben geschlossen. Der Gruppenvergleich nutzt nur die zuerst erreichbare Studie und Gruppe. Diesen Umfang im Prüfbericht nennen; ein PASS darf keine vollständige Prüfung aller Quellen- und Gruppenvarianten behaupten.

`layout()` misst Dokumentüberlauf, keine abgeschnittenen Inhalte innerhalb einzelner Container. Die Screenshots zeigen jeweils den aktuellen Viewport. axe ohne `violations` belegt nur die ausgeführten automatischen Regeln; `incomplete` braucht weiterhin Bewertung. Browser- und Skriptversion lassen sich mit Browserversion und dem hier erfassten Datei-Hash zuordnen, der generierte Laufbericht enthält selbst noch keinen Skript-Hash.

## Arbeitsumfang und Abnahmen

Ich habe `AGENTS.md`, `docs/project.md`, `docs/handbuch.md` und `.agents/skills/unslop/SKILL.md` vollständig gelesen. Unterstützende öffentliche UI-Quelltexte dienten nur dazu, die Assertions des Skripts gegen die tatsächlich vorhandenen Zustände zu prüfen. Keine Rohdaten, Personenkennungen oder privaten Analyseausgaben wurden gelesen.

Nur dieser Erstbericht wurde neu geschrieben. Andere Erstberichte, wissenschaftliche Artefakte und synchronisierte Skills blieben unberührt. `pnpm check` und tatsächliche Browserläufe liegen beim Koordinator. Technische Erfolgsnachweise lassen methodische, menschliche Verständnis-, Design- und Releaseabnahmen offen.
