# Erstreview WEBSITE-METHODS-001/v1

Stand: 2026-10-03. Urteil: **PASS im begrenzten Paketumfang.** Keine erhebliche falsche Aussage, erfundene Auswertung oder politische Wertung gefunden. WM-R01 ist ein optionaler Hinweis zur Belegführung und blockiert das Paket nicht.

## Prüffassung und Grenzen des Reviews

Geprüft wurden die drei Seiten-/Textdateien aus dem Manifest, das vollständige Handbuch und die dort ausdrücklich aufgeführten sachlichen Quellenartefakte. Ausgangscommit: `3595c0a2e45c8ffbf4d047f7341e8761f5aa0d6d`; Branch: `research/life-93-night-20261003`. Manifest-SHA-256: `0897a2fd767c13e0acd28ab158d9a8427e8d07e3eeab78243dbdbfab2982d386`. Alle 14 Dateipins stimmten vor und nach der Lektüre überein. Die Nachkontrolle steht in `outputs/loop/website-methods-review/pins-after.json`.

Dieser Reviewer gehört ebenfalls zur Codex-Modellfamilie. Der frische begrenzte Kontext und drei getrennte Lesedurchgänge garantieren weder unabhängige Modellvorgaben noch politische Neutralität. Andere aktuelle Urteile zu diesem Websitepaket, ein Autorenreviewbericht und eine vorweggenommene Verteidigung wurden nicht gelesen. Die aufgeführten Quellenvorschläge wurden ausschließlich als sachliche Belegartefakte genutzt. Keine Antwortdaten, Rohdateien, Personenkennungen, gesperrten Vergleichswerte oder Dateien unter `data/raw/` und `data/local/` wurden geöffnet.

Das Urteil betrifft vorhandene Dokumentationstexte und Statusangaben. Es ist keine Freigabe des Analyseplans, der empirischen Methoden, des Tests oder einer Veröffentlichung. Eine vollständige Methodenprüfung war für dieses normale Websitepaket weder beauftragt noch erforderlich.

## Lesedurchgang 1: Tatsachen, Quellen, Versionen und Reichweite

Die Seiten wurden zunächst gegen die gepinnten Fakten gelesen. Die folgenden Aussagen sind im Paket passend begrenzt:

| Aussage und Ort | Beleg und Befund |
| --- | --- |
| Neun vorgeschlagene Originalfragen, kein freigegebener Test. `project.html:13–15, 98–108`, `project.ts:18`, `home.html:107–108`. | `data/item-core-v1.json` enthält genau B34–B36/B40–B45. Der Inventarabschluss, Zeilen 3, 47–69 und 118, beschreibt einen Vorschlag und offene Gates. Die Website gibt weder neun Dimensionen noch einen fertigen Score vor. |
| Deutsches ESS11, integrierte Ausgabe 4.2, Feldzeit 2023. `project.html:71–90`. | Das öffentliche Versionsbinding benennt 4.2 und seinen DOI. Der frisch abgerufene [Länderbericht 4.0, Seiten 79–80](https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_country_documentation_report_e04.pdf#page=79) bestätigt Feldzeit und persönliche Interviews. Die Website nennt ausdrücklich die historische Reichweite und den ungeprüften Wechsel zur Webantwort. |
| Bundestagswahl 2021 mit Zweitstimme; Einstellungen im Jahr 2023 statt heutiger Parteipositionen. `project.html:46–55`. | [Deutscher Fragebogen, Seiten 7–8](https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf#page=7): B13 nennt die Wahl im September 2021, B14b erfragt die Zweitstimme. Inhaltlich richtig; siehe WM-R01. |
| Fragebogen/Listenheft aus Runde 11 und gesondertes Codebook 4.1. `project.html:120–142`. | Frische GETs von Fragebogen, Listenheft und Codebook ergaben dieselben SHA-256 wie die Quellenpins des Kernvertrags. Der Codebooktitel trägt 4.1. Die Website vermischt diese Dokumentfassung nicht mit der Datenausgabe 4.2. |
| Öffentliche Metadatenbindung 4.2 statt Prüfung der tatsächlichen CSV. `project.html:137–142`. | `data/core-integrated-4.2-binding.json` meldet neun übereinstimmende öffentliche Feld-/Kodierungsbindungen und benennt ausdrücklich den fehlenden CSV-/Vorkommensabgleich. Die Website hält diese Grenze aufrecht. |
| 2.420 Fälle, 25 Schichten, 500 veröffentlichte primäre Auswahleinheiten; zwei Schichten mit je zwei Einheiten. `project.html:181–191`. | Metadatenbericht, Zeilen 16–21 und 43–45. Der Mindestumfang von vier Einheiten je Schicht ist dadurch nicht überall erreichbar. Die Seite behauptet weder einen bereits ausgeführten Split noch politische Antwortverteilungen. |
| Zwei getrennte Codex-Erstbewertungen, gemeinsame mögliche Fehler; Übereinstimmung ohne Gütenachweis. `project.html:193–205`, `project.ts:26–35`. | Das Agreement-Artefakt bezeichnet Dokumenturteile und nennt dieselbe Modellfamilie sowie Grenzen von Richtigkeit, Neutralität und Validität. Die Website übernimmt diese Einschränkungen statt Kappa als Gütesiegel zu zeigen. |
| Planentwurf und vollständige Antwortdomäne statt unbedingter Bevölkerungswerte. `project.html:215–230`. | `docs/empirie-plan-v1.entwurf.md:3, 35–39, 70, 74` trennt Entwurf, neun gültige Antworten, gewichtete vollständige Antwortdomäne und historische Referenz. Die Website verspricht daraus keine aktuelle Bevölkerungsnorm. |
| Daten- und Dokumentationslizenz getrennt; konkrete Veröffentlichungsprüfung offen. `project.html:144–155`. | Der frische Abruf der [ESS-Nutzungsbedingungen](https://www.europeansocialsurvey.org/contact/disclaimer) bestätigt CC BY-NC-SA 4.0 für Daten und CC BY-SA 4.0 für Dokumentation. `docs/lizenzen.md:15–29` begrenzt die artefaktbezogene Prüfung. Die Website behauptet kein allgemeines gesetzliches Rohdaten-Veröffentlichungsverbot und keine rechtsfachliche Freigabe. |
| Claude, Menschenprüfungen und Design-/Releasefreigaben fehlen. `project.html:232–236`. | Fortsetzungsauftrag, Zeilen 13–14, 24 und 28; Planentwurf, Zeilen 88–90. Die Website gibt keine fehlende Prüfung als bestanden aus. |

Die sieben hier geprüften öffentlichen GitHub-Beleglinks antworteten auf HEAD mit HTTP 200. Das belegt Erreichbarkeit, keine unveränderliche Version des Branchlinks. Originalabrufe, finale URLs, UTC-Zeiten, HTTP-Status und Hashes stehen in `outputs/loop/website-methods-review/source-access.json`; Link-/Strukturkontrollen in `static-structure-and-links.json` im selben Ordner.

Die verlinkte ESS-Studienseite und der DOI waren erreichbar, lieferten beim Textabruf aber nur die JavaScript-Hülle. Die Referenzbevölkerungsdefinition wurde deshalb gegen den gepinnten Planentwurf, Zeile 7, auf Konsistenz gelesen; eine neue vollständige Originalllektüre dieser Portalangabe wird nicht behauptet. Ebenso wurden die theoretischen Literaturtexte hinter dem Konstruktvorschlag nicht neu vollständig recherchiert. Die Website behauptet daraus ohnehin keinen deutschen empirischen Modellnachweis.

## Lesedurchgang 2: KI-Ton und Handbuch 7.2–7.7

Die Seiten und die Statuswerte in `project.ts` wurden danach erneut ohne Bewertung statistischer Güte gelesen. Ergebnis: **PASS für die Textregeln im Paket.**

- Vorhandenes steht im Präsens; Test, Modellbildung und Vergleiche werden als Vorhaben oder Entwurf benannt. Keine erfundenen Fragen, Dimensionsnamen, Scores, Bearbeitungszeiten oder Gütesiegel.
- Die Begriffe „Einstellungen“, „Dimensionen“, „Befragte“, „Wählergruppen“, „eigenes Modell“ und „technische Prüfungen“ entsprechen dem Handbuch. Keine direkte Anrede, Werbung, rhetorische Pointe oder politische Rangordnung.
- Kein erhebliches KI-Sprachmuster aus dem gelesenen `unslop`-Skill gefunden. Einzelne Fachbegriffe wie „Quellenvertrag“ und „primäre Auswahleinheiten“ könnten einfacher erklärt werden; das ist eine Stiloption, kein sachlicher oder materieller Zugänglichkeitsfehler.
- Die Datumsangaben, ausgeschriebenen kleinen Zahlen und Linktexte sind passend. Die Pflichtformel aus Handbuch 7.2/7.7 steht unverändert in `project.html:203–205`.

Die Inhaltsverzeichnisziele, internen Fragmente und Seiten-IDs sind gegenüber dem Ausgangscommit unverändert. Alle geprüften Fragmente haben Ziele; alle `aria-labelledby`-Verweise haben IDs, ohne doppelte IDs. Jede Seite hat eine H1 und keine übersprungene Überschriftenebene. Der begrenzte Diff enthält Texte, Absätze und Beleglinks, keine neue Navigation, Gestaltung oder sichtbare Testaktion. Statusleiste, Fußzeile, Metabeschreibung und gemeinsame Styles liegen außerhalb dieses Pakets; ihre Laufzeitdarstellung wurde nicht erneut geprüft.

## Lesedurchgang 3: Politische Fairness und Neutralitätsgrenzen

Die sichtbaren Texte wurden ein drittes Mal zusammenhängend gelesen, nun auf politische Zuschreibungen und Reichweitenverschiebungen. Ergebnis: **PASS für die begrenzten Aussagen.**

Die Beschreibung der neun Gegenstände bleibt bei Lebensführung, Adoptionsrechten, hypothetischer Scham, bezeichneten Aufnahmegruppen und wahrgenommenen Zuwanderungsfolgen. Sie macht daraus weder eine allgemeine Toleranz-, Moral-, Wirtschafts- oder Links-rechts-Dimension noch eine Aussage über tatsächliche Zuwanderungsfolgen. Das schmale Themenfeld wird ausdrücklich benannt; ein umfassendes politisches Profil wird aus diesem Bestand nicht abgeleitet.

Wählergruppen beruhen auf eigener Angabe zu einer historischen Zweitstimme. Kein Text setzt diese Gruppen mit Parteien, heutigen Wahlentscheidungen oder heutigen Parteiprogrammen gleich. Die ESS-Referenz wird nicht mit Wahlberechtigten gleichgesetzt. Der Hinweis zur vollständigen Antwortdomäne verhindert eine unbelegte Übertragung auf die gesamte Referenzbevölkerung. Diese Einschränkungen sind für die geplanten Vergleiche ausreichend sichtbar auf der Projektseite.

Eigene Auswahl, Auswertung und Interpretation bleiben Entscheidungen des Projekts. ESS, technische Checks und KI-Übereinstimmung werden nicht als Billigung oder Neutralitätsgarantie dargestellt. Der Review kann mögliche gemeinsame Modellfehler nicht ausschließen und bestätigt keine absolute politische Neutralität.

## Findings

### WM-R01: Zusätzlicher Sprung zur Zweitstimmenfrage wäre hilfreicher

Schweregrad: **Hinweis, nicht blockierend.** Ort: `web/src/app/pages/project/project.html:50–55`.

Der bestehende Link mit `#page=7` führt korrekt zu B13 und der Wahlzeit September 2021. Die zusätzliche Aussage zur Zweitstimme stammt aus B14b auf PDF-/Druckseite 8. Der Absatz ist sachlich richtig; die verlinkte Fundstelle verlangt für diesen Teil einen Seitenwechsel. Betroffen ist ausschließlich der Belegkomfort der Wählergruppendefinition.

Minimale optionale Korrektur: „Zweitstimme“ zusätzlich mit derselben Fragebogen-URL und `#page=8` verlinken. Der vorhandene Wahlzeit-Link kann bestehen bleiben. Kein neuer Inhalts-, Design- oder Methodenentscheid nötig; keine Korrektur Voraussetzung dieses PASS.

## Nicht durchgeführt und nicht bestanden erklärt

Kein `pnpm check`, Build, vollständiger Browserdurchgang, Tastatur-/Fokuslauf, axe-Test, Smartphone-/Zoomtest oder Screenreader-Test durch diesen Reviewer. Diese technischen und visuellen Prüfungen bleiben Aufgabe des Koordinators. Die statische Text-/Ankerkontrolle ist kein WCAG-Nachweis.

Keine reale Antwortanalyse, Nachrechnung des Rohdaten-Metadatenlaufs, Splitausführung, Messmodellprüfung, CAPI-/Webmodusabnahme, menschliche Verständlichkeitsprüfung, rechtsfachliche Freigabe oder Claude-Kontrolle. Keine persönliche Release-, Merge- oder Deploymentfreigabe abgeleitet. Keine gemeinsam genutzte Datei geändert, kein Commit, Tag, Push oder Paketinstallation.

Dieser Erstbericht bleibt nach dem ersten Schreiben unverändert. Sein endgültiger SHA-256 steht getrennt im eigenen Reviewindex unter `outputs/loop/website-methods-review/index.json`.
