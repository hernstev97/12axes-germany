# Vorschläge für offene Beschriftungen und Pflichttexte

ENTWURF 1, 4. Oktober 2026, verfasst von Claude. Nichts davon ist umgesetzt. Steven entscheidet, weil es Pflichttexte aus LIFE-93, Regeln des Handbuchs oder die Benennung von Bereichen betrifft. Jeder Vorschlag nennt die Fundstelle, das Problem mit Beleg, Varianten und eine Empfehlung. Grundlage sind die Findings V2-F04, V2-F11 und V2-F15 (`reports/claude/agenten/V2-urteil.json`) und T1 Abschnitt 4 (`reports/claude/agenten/T1-technik-browser.md`).

## 1 Statushinweis auf Ergebnisseiten (V2-F11)

**Fundstelle.** LIFE-93, Phase 6, im Wortlaut übernommen in `web/src/app/policy-draft/policy-draft.html` (Abschnitt „Status und Grenzen“): „Forschungsprototyp. Fragen und Vergleichsdaten stammen aus dem European Social Survey, Dimensionen und Auswertung sind ein eigenes Modell dieses Projekts. Analyse und Website wurden mit KI erstellt und nicht von Fachleuten begutachtet. Code und Auswertung sind öffentlich.“

**Problem.** Das Profil berechnet keine Dimensionen (Profilregeln v1, Plan v2.2 Abschnitt 2). Zwei Absätze weiter steht im selben Abschnitt: „Es berechnet keine Dimension und keinen politischen Gesamtwert.“ Der Pflichttext kündigt damit etwas an, das es nicht gibt. Kommen später Fragen aus anderen Quellen hinzu, stimmt auch „stammen aus dem European Social Survey“ nicht mehr.

**Varianten.**

- A (kleinste Änderung): „Forschungsprototyp. Fragen und Vergleichsdaten stammen aus dem European Social Survey, Auswahl, Ordnung und Auswertung sind ein eigenes Modell dieses Projekts. Analyse und Website wurden mit KI erstellt und nicht von Fachleuten begutachtet. Code und Auswertung sind öffentlich.“
- B (offen für weitere Quellen): „Forschungsprototyp. Fragen und Vergleichsdaten stammen aus wissenschaftlichen Befragungen, derzeit dem European Social Survey. Auswahl, Ordnung und Auswertung sind ein eigenes Modell dieses Projekts. Analyse und Website wurden mit KI erstellt und nicht von Fachleuten begutachtet. Code und Auswertung sind öffentlich.“

**Empfehlung.** A jetzt. B erst, wenn eine weitere Quelle tatsächlich freigegeben ist.

## 2 Meta-Beschreibung (T1 Abschnitt 4)

**Fundstelle.** `web/src/index.html`: „12 Axes Deutschland plant einen Test, der aus Antworten ein Profil politischer Einstellungen mit mehreren Dimensionen bilden soll. Er ist noch nicht verfügbar.“

**Problem.** Wie Punkt 1: Die aktuelle Fassung hat keine Dimensionen. Handbuch 7.6 verlangt höchstens 160 Zeichen, den Namen am Anfang und den Status.

**Varianten.**

- A (141 Zeichen): „12 Axes Deutschland plant einen Test zu politischen Einstellungen, der die Antworten Frage für Frage beschreibt. Er ist noch nicht verfügbar.“
- B (151 Zeichen): „12 Axes Deutschland plant einen Test zu politischen Einstellungen in Deutschland. Er beschreibt Antworten Frage für Frage und ist noch nicht verfügbar.“

**Empfehlung.** B, weil sie Deutschland nennt.

## 3 Begriffe „Profil“ und „Dimension“ im Handbuch

**Fundstelle.** `docs/handbuch.md` 7.3: „Profil – Ergebnis mit mehreren Dimensionen“, „Dimension – Teil des Profils“.

**Problem.** Die Begriffstabelle setzt Dimensionen voraus. Die Website und der Forschungsentwurf beschreiben das Profil ausdrücklich ohne Dimensionen. Der Begriff „Bereich“ fehlt in der Tabelle, obwohl er auf allen Seiten vorkommt.

**Vorschlag.**

| Begriff   | Verwendung                                                                                           | Nicht                   |
| --------- | ---------------------------------------------------------------------------------------------------- | ----------------------- |
| Profil    | Ergebnis: Beschreibung der eigenen Antworten mit historischen Vergleichen                            | Typ, Persönlichkeit     |
| Bereich   | Ordnung der Fragen für Lesende, mit „Erfasst“ und „Nicht erfasst“                                    | Dimension, Achse, Skala |
| Dimension | nur für eine geprüfte gemeinsame Messung nach eigenem Plan. In der aktuellen Fassung nicht vorhanden | Bereich, Rubrik         |

**Empfehlung.** Übernehmen, weil das Handbuch sonst eine Struktur vorschreibt, die das Projekt begründet nicht verwendet.

## 4 „Repräsentative wissenschaftliche Befragung“ (V2-F15)

**Fundstelle.** Handbuch 7.3 schreibt diese Formel beim ersten Vorkommen des ESS vor. Sie steht auf Startseite, Methodikseite und im Forschungsentwurf.

**Problem.** „Repräsentativ“ ist eine Eigenschaft, die das Projekt für die erreichten Stichproben nicht selbst prüft. Der Katalog vermerkt, dass die erreichte Abdeckung nicht geprüft ist. ESS8 hat München im tatsächlichen Stichprobendesign ausgelassen. Prüfbar ist dagegen das Verfahren. Die [ESS-Seite zur Stichprobenziehung](https://www.europeansocialsurvey.org/methodology/ess-methodology/sampling) verlangt „strict random probability methods at every stage“ und schließt Quotenstichproben und Ersatz von Ausfällen aus (abgerufen am 4. Oktober 2026). Dieselbe Seite nennt als Ziel, dass Stichproben „representative of all persons aged 15 and over“ in Privathaushalten sind. Das ist ein Anspruch des Designs, kein geprüftes Ergebnis für die erreichte Stichprobe.

**Varianten.**

- A: „eine wissenschaftliche Befragung auf Grundlage von Zufallsstichproben“
- B: unverändert, mit dem Zusatz an der Stelle der Grenzen: „Die erreichte Abdeckung der Bevölkerung hat das Projekt nicht selbst geprüft.“

**Empfehlung.** A, weil sie nur behauptet, was die ESS-Dokumentation belegt. Der Handbuchtext müsste dann mitgeändert werden.

## 5 Untertitel der Bereiche (V2-F04)

**Fundstelle.** `web/src/app/policy-draft/policy-catalogue.ts` (`POLICY_RUBRICS`) und `profile/area-scope.ts`.

**Problem.** Die Bereichsnamen beschreiben ein ganzes Politikfeld. Die Fragen decken jeweils nur einen Teil ab. Die Ansicht zeigt das bereits mit „Erfasst“ und „Nicht erfasst“. Der Name allein kann trotzdem mehr versprechen, etwa „Wirtschaft und Verteilung“ für vier Gerechtigkeitsprinzipien und eine Umverteilungsfrage.

**Varianten.** A: Namen behalten und einen Untertitel ergänzen, der den tatsächlichen Inhalt nennt. B: Namen durch engere Namen ersetzen. A hält die Namen der Themenabdeckung stabil, auch wenn später Fragen hinzukommen.

| Bereich                              | Vorgeschlagener Untertitel                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| Wirtschaft und Verteilung            | Gerechtigkeitsprinzipien und Umverteilung                                      |
| Sozialstaat                          | Staatliche Verantwortung, Zielgruppen von Leistungen, Grundeinkommen           |
| Demokratie und politische Autorität  | Demokratieverständnis, Mehrheit und Regierung, Führung und Gesetz              |
| Bürgerrechte und Sicherheit          | Pflichten gegenüber Polizei und Gesetz, Strafen, Abwägungen in einer Pandemie  |
| Europäische Integration              | Mitgliedschaft, Entscheidungsebene, Richtung der Einigung, EU-Sozialprogramm   |
| Klima und Energie                    | Klimamaßnahmen und Energiequellen für Strom                                    |
| Migration                            | Zuwanderung nach Herkunft, Sozialrechte, Asyl                                  |
| Gleichstellungs- und Familienpolitik | Gleichstellungsmittel, Familienleistungen, Rechte gleichgeschlechtlicher Paare |

**Empfehlung.** A. Umsetzung als zusätzliche Zeile unter dem Bereichsnamen im Forschungsentwurf, ohne neue Gestaltungsmuster.

## 6 Schon umgesetzt, zur Bestätigung

- Restgruppe der Parteiliste: „Andere Partei (heterogener Rest)“ statt „Other“, mit Erklärung beider Bezeichnungen (V2-F13). Umgesetzt am 3. Oktober 2026. Steven kann das zurücknehmen.
- Erklärung der 95-%-Bereiche einmal je Ansicht statt an jeder Referenz (Plan v2.2, 4.3). Umgesetzt am 4. Oktober 2026.
