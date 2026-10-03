# Statische Prüfung von Tastaturfokus und Zoomabdeckung

Prüfung am 3. Oktober 2026 durch einen getrennten Codex-Agenten. Auftrag: technische Nacharbeit an Frageablauf und Ergebnisentwurf, kein wissenschaftlicher Audit. Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Root hat Branch `research/life-93-night-20261003` und Ausgangs-HEAD `9de6ec5a31c365c898b45f4394d2cf1ff0052476` vorgegeben. Dieser Bericht beschreibt die tatsächlich gelesenen Arbeitsdateien vor einer Korrektur durch Root.

## Befunde

1. **TFZ-S01: Der Gruppenquellen-Summary fehlt der vorgeschriebene Fokusstil.** `web/src/app/policy-draft/policy-draft.html:279–280` enthält einen nativen `summary` außerhalb der SourceDetails-Komponente. `web/src/styles.scss:65–70` erfasst nur Links, Buttons und Elemente mit `tabindex`. `policy-draft.scss` enthält keinen Summary-Fokusstil. Die Regel in `policy-source-details.scss:15–18` gehört zur eigenen Komponente und erreicht den Gruppenquellen-Summary nicht. Damit fehlt hier der im Handbuch verlangte Rahmen mit 2 px und 4 px Abstand. Ob der Browser stattdessen einen sichtbaren Standardrahmen zeigt, wurde nicht beobachtet. Gezielte Korrektur: diesen nativen Summary in den gemeinsamen Fokusstil aufnehmen.

2. **TFZ-S02: Die automatisierte Browserprüfung erreicht die Forschungsansichten nicht.** `scripts/check-browser.mjs:23–27` extrahiert nur `path`-Literale aus `app.routes.ts`. Die Route `/forschungsentwurf` steht in `research-preview.routes.dev.ts:6`, wird aber lediglich importiert. Frageablauf, Übersicht und Ergebnisse fehlen deshalb in der ermittelten Routenliste. Der Tastaturdurchgang prüft ausschließlich `/projekt`, höchstens 25 Tabs und nur einen `solid`-Outline (`check-browser.mjs:114–146`). Er prüft weder die vollständige Tabfolge noch Farbe, Abstand, Clipping oder native Forschungscontrols. Ein grüner Lauf dieses Skripts belegt den angefragten Forschungsdurchgang nicht.

3. **TFZ-S03: Echter 200-%-Browserzoom bleibt im Skript ungeprüft.** Der zweite Durchgang nutzt einen 640 × 400 CSS-Pixel großen Viewport mit `deviceScaleFactor: 2` (`check-browser.mjs:103–112`). Das Skript benennt dies inzwischen korrekt als Reflow/Pixeldichte und meldet echten Browserzoom am Ende ausdrücklich `NICHT_GEPRÜFT` (`:175–177`). Es erzeugt keinen falschen Zoomnachweis. Für den aktuellen Auftrag fehlt in diesem Prüfweg dennoch die tatsächliche Browserzoombeobachtung.

4. **TFZ-S04: Fokus nach „Auswahl zurücksetzen“ ist zur Laufzeit offen.** Der Button wird bei `untouched` deaktiviert (`policy-draft.html:117–123`); `resetAnswer()` setzt genau diesen Zustand und fordert keinen anschließenden Fokus an (`policy-draft.ts:136–141`). Die Tastaturaktivierung kann damit den gerade fokussierten Button deaktivieren. Der Code allein belegt nicht, wo der Browser den Fokus danach hält. Root soll nach einer demonstrativen Auswahl mit Tab zum Reset-Button und Enter prüfen, ob der Fokus sichtbar und die nächste Tabposition nachvollziehbar bleibt. Dies ist ein gezielter Prüfpunkt, keine beobachtete Fehlfunktion.

## Was der Code bereits regelt

Links und native Buttons erhalten den gemeinsamen Fokusrahmen. Radios und Selects im Fragen-/Ergebnisentwurf erhalten zusätzlich den lokalen Rahmen (`policy-draft.scss:32–36`), alle Summarys der SourceDetails-Komponente ihren eigenen (`policy-source-details.scss:15–18`). Die native Radio-Gruppe benutzt einen gemeinsamen Namen und umschließende Labels; keine künstlichen Tabstopps oder positiven `tabindex` ändern ihre Reihenfolge (`policy-draft.html:82–104`). Die eigene Radiofläche ist 24 × 24 px; umgebende Optionen und Buttons sind mindestens 48 px hoch. Im gelesenen Bereich fand sich kein Überlauf-Clipping, das ihren Fokusrahmen unmittelbar abschneidet.

Fragen folgen im DOM auf die Ansichtsbuttons. Nach dem Radio-Gruppenstopp folgen Vorwärts-/Rückwärtsnavigation, gegebenenfalls Reset, Überspringgrund, Überspringbutton und Quellen-Summary. In Ergebnissen folgen auf die Ansichtsbuttons die Studien-/Gruppen-Selects, gegebenenfalls Gruppenquellen, dann je Originalangabe der Quellen-Summary und der Bearbeitungsbutton. Geschlossene Details verbergen ihre inneren Links. Deaktivierte Controls bleiben aus der nativen Tabfolge ausgeschlossen.

Vorwärts, rückwärts, Überspringen, Bearbeiten und Ansichtswechsel führen nach dem Rendern zur passenden Überschrift und scrollen sie ins Bild (`policy-draft.ts:143–170,229–241`). Diese Überschriften haben `tabindex="-1"`; ihr fehlender Rahmen entspricht der ausdrücklichen Sprungzielausnahme in `styles.scss:71–74`. Die Tests erfassen Fokusziel und angefordertes Scrollen. Sie erklären selbst, dass jsdom kein Layout und kein natives `scrollIntoView` besitzt (`policy-draft.spec.ts:36–49`). Sie belegen deshalb weder den sichtbaren Fokus noch dessen Lage im echten Browser. Die reine Gruppenauswahl fordert keinen Überschriftenfokus an; ein vorhandener Test prüft, dass sie den Select-Fokus behält.

Das globale Raster nutzt `minmax(0, 1fr)` und stapelt bei 860 px. Fieldsets und Komponentenhosts haben `min-width: 0`; Steuergruppen umbrechen, Buttons/Flächen erlauben Wortumbruch, Faktenlisten werden bei 640 px einspaltig. Dies spricht für Reflow, beweist ihn aber nicht. Insbesondere lange Originaltexte, aufgeklappte Quellen und native Selects müssen bei tatsächlich eingestelltem 200-%-Browserzoom angesehen werden.

## Grenzen und gelesener Umfang

Keine Browser-, Server-, Netzwerk-, Rohdaten-, privaten Antwort- oder Outputzugriffe; keine Tests ausgeführt. Keine Gitmutation und keine Änderung außerhalb dieses Berichts. Die tatsächliche Browserbeobachtung, Korrektur und Gesamtprüfung führt Root separat durch. Diese Prüfung erteilt keine methodische, menschliche oder Releasefreigabe.

Browserzoom, CSS-`zoom`, doppelte Pixeldichte, Pinch-Zoom und kleinere Viewports sind verschiedene Prüfbedingungen. `deviceScaleFactor` verändert die Pixelzuordnung. Ein kleinerer Viewport prüft responsive Umbrüche. CSS-`zoom` verändert das Seitenelement; Pinch-Zoom verändert die visuelle Vergrößerung. Keiner dieser Wege ersetzt den ausdrücklich verlangten, über die Browserfunktion eingestellten 200-%-Zoom. Dieser Agent behauptet für keinen dieser Wege einen tatsächlichen Browserbefund.

Die folgenden 20 Repositorydateien wurden vollständig als Text gelesen; Umfang beim anschließenden Bytes-Abgleich: 142.323 Bytes. `AGENTS.md`, `project.md` und `handbuch.md` wurden vollständig gelesen. Die unslop-Anleitung wurde vor dem Schreiben gelesen und angewandt. Der leichte Memory-Abgleich diente nur der Trennung technischer Prüfung und wissenschaftlicher Abnahme; aktuelle Codebefunde stammen aus diesen Dateien.

| Datei | Gelesene Bytes |
| --- | ---: |
| `AGENTS.md` | 6.291 |
| `docs/project.md` | 9.786 |
| `docs/handbuch.md` | 36.004 |
| `scripts/check-browser.mjs` | 6.939 |
| `web/src/styles.scss` | 6.542 |
| `web/src/app/policy-draft/policy-draft.html` | 24.952 |
| `web/src/app/policy-draft/policy-draft.scss` | 2.250 |
| `web/src/app/policy-draft/policy-draft.ts` | 8.784 |
| `web/src/app/policy-draft/policy-draft.spec.ts` | 22.608 |
| `web/src/app/policy-draft/policy-source-details.html` | 5.300 |
| `web/src/app/policy-draft/policy-source-details.scss` | 540 |
| `web/src/app/policy-draft/policy-source-details.ts` | 1.288 |
| `web/src/app/app.html` | 1.729 |
| `web/src/app/app.scss` | 2.512 |
| `web/src/app/app.ts` | 1.697 |
| `web/src/app/app.spec.ts` | 2.906 |
| `web/src/app/app.routes.ts` | 899 |
| `web/src/app/research-preview/policy-preview.ts` | 760 |
| `web/src/app/research-preview.routes.dev.ts` | 379 |
| `web/src/app/research-preview.routes.ts` | 157 |

Identitätsbeleg für die wichtigsten geprüften Dateien (SHA-256):

```text
scripts/check-browser.mjs ca46ebe7e23404972f6dcff9d3fe2b96c9335095a8919620e6ff90c7b65b3538
web/src/styles.scss 695afc2c43f15dcaf4ad0406a3bf9910d7b6b7f610e4e52516b72f624ba8cf11
web/src/app/policy-draft/policy-draft.html f556dbb8bf3d6a41503378fd53476356e29cd8b448f2a7e5544b5d695d8087b6
web/src/app/policy-draft/policy-draft.scss a13b9138de8ac2086bff347f349494815c9eb7973b5c0d9f67696fce67776722
web/src/app/policy-draft/policy-draft.ts ee0267535f812e572a9c15859722bd2449f7681a06f54f52aeece2fe3a09b0fc
web/src/app/policy-draft/policy-source-details.scss 98ba630fb6527743e449750fbffde418f28b5993a208e37455205aec2c997f8b
```
