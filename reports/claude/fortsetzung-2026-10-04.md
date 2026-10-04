# Fortsetzungsbericht LIFE-93 vom 4. Oktober 2026

Verfasst von Claude (Modellkennung laut Laufzeit `claude-opus-5-5[1m]`). Branch `research/life-93-claude-20261003`, Ausgangsstand `b5a53ff`, Endstand: der Commit, der diesen Bericht abschließt, direkt nach `c171e7d`. Auftrag: Stevens Nachricht vom 4. Oktober 2026 (Wortlaut in `docs/ki-protokoll.md`), ohne seine Mitwirkung weiterzuarbeiten. Dieser Bericht ergänzt den [Abschlussbericht](abschlusspruefung.md), der unverändert bleibt. Er ist ein KI-Bericht, keine Begutachtung durch Fachleute und keine Freigabe. Nichts wurde gemergt, veröffentlicht oder versendet.

## 1 Ergebnis in Kürze

- **Technische Prüfgrenzen geschlossen.** Die ESS5-Designdatei ist zum zweiten Mal unabhängig dekodiert, mit ReadStat statt des eigenen Lesers: alle Felder in allen 3031 Zeilen gleich, Standardfehler ohne Abweichung. Der Produktionsbuild ist im Browser geprüft, die öffentlichen Seiten mit echtem 200-%-Zoom. Der Forschungsentwurf ist zusätzlich in Firefox geprüft. WebKit ließ sich ohne Systemänderung nicht starten.
- **Forschungsentwurf verbessert.** Die Erklärung der 95-%-Bereiche steht einmal je Ansicht, wie Plan v2.2 es verlangt. Fehlende Bereiche sind je Kategorie und bei Gruppenvergleichen markiert. Die Erklärung nennt auch Messfehler einzelner Antworten.
- **Erweiterungspaket 2025/26 vorbereitet, nicht umgesetzt.** Für keinen der sechs fehlenden Bereiche gibt es außerhalb von GESIS eine Zufallsstichprobe der Jahre 2024 bis 2026 mit öffentlichem deutschem Wortlaut zu einer nationalen Streitfrage. Möglich sind neun Eurobarometer-Fragen, die meisten zu Entscheidungen auf EU-Ebene, nach Freigabe und Klärung der Fragebasis, und ESS12 mit Wählergruppen nach der Bundestagswahl 2025, sobald die deutsche Ausgabe veröffentlicht ist. Der [Analyseplan v2.3](../../docs/analyseplan-v2.3.entwurf.md) hat in Fassung 0.4 beide Planprüfungen bestanden, nach drei Runden. Er bleibt ein Entwurf und ist keine Freigabe zur Auswertung.
- **Quellenblocker präzisiert.** Je Quelle und Nutzung steht fest, ob sie ausdrücklich verboten, ungeklärt oder durch eine Lizenz erlaubt ist (R10).
- **Für Steven vorbereitet:** Entscheidungsvorlage mit fünf Entscheidungen, vier Anfrageentwürfe, fünf Textvorschläge. Die Textvorschläge haben nach einer Korrekturrunde eine inhaltliche KI-Prüfung bestanden.

## 2 Technische Prüfgrenzen

| Grenze aus dem Abschlussbericht              | Ergebnis                                                                                                                                                                                                                                                                                               | Beleg                                                        |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| SPSS-Leser ohne zweite Dekodierung (Punkt 7) | Zweite Dekodierung mit pyreadstat 1.3.6 (ReadStat) in isolierter Umgebung. Alle sechs Felder in allen 3031 Zeilen gleich, Eins-zu-eins-Zuordnung, 32 ESS5-Referenzen mit ReadStat-Design: Standardfehler ohne Abweichung. Ausdrücklicher Status mit Toleranz 1e-12, alle drei Gegenproben `BESTANDEN`. | `reports/claude/kontrollrechnung/sav-gegenprobe.md`, `.json` |
| Produktionsbuild nicht im Browser            | Lokal ausgeliefert, vier Seiten in fünf Breiten bestanden. Die Forschungsroute fehlt im Produktionsbuild.                                                                                                                                                                                              | `docs/validation.md`, Abschnitt vom 4. Oktober 2026          |
| Echter 200-%-Zoom der öffentlichen Seiten    | Vier Seiten bei 1440, 1280, 1024 und 768 Pixeln mit `chrome.tabs.setZoom`: kein Überlauf, axe ohne Verstoß, jeder Tab-Stopp sichtbar                                                                                                                                                                   | `scripts/check-public-zoom.mjs`                              |
| Nur Chromium                                 | Firefox 155 und Chromium 151, Desktop und Smartphone-Breite: alle 62 Fragen, Antwortänderung, Zurücksetzen, Überspringen, Ergebnis, Gruppenvergleich, Fokus, keine Anfrage und kein Schreiben in Speicher                                                                                              | `scripts/check-research-engines.mjs`                         |
| WebKit und Safari                            | Nicht prüfbar: fehlende Systembibliotheken, Installation wäre eine Systemänderung                                                                                                                                                                                                                      | `docs/validation.md`                                         |

Codex hat das technische Paket geprüft (T2). Runde 1 war nicht bestanden: Fokus- und Speicherprüfung im Skript schwächer als dokumentiert, fehlende Markierung fehlender Bereiche, kein Fehlerstatus der Gegenproben, ein fehlender Satzteil. Alle fünf Befunde sind behoben, Runde 2 ist bestanden (`reports/claude/pruefungen/T2-*.md`).

Nicht durchführbar bleiben physische Smartphones, Touch auf echten Geräten, Screenreader mit Menschen und Hochkontrastmodus.

## 3 Erweiterungspaket 2025/26

**Recherche.** Drei ergebnisblinde Claude-Subagents (R8 Außen-, Digital- und Bildungspolitik; R9 Arbeit und Rente, Gesundheit und Pflege, Wohnen, Wählergruppen; R10 Nutzungsbedingungen) und eine getrennte technische Rolle (S1) für die Struktur veröffentlichter Eurobarometer-Tabellen. S1 hat Tabellen geöffnet, aber nur Struktur, Basen und Methodenangaben gemeldet. Die Auswahl im Plan entstand ohne Kenntnis von Ergebnissen.

**Befunde.**

1. Für die sechs Bereiche fehlen außerhalb von GESIS aktuelle Zufallsstichproben zu nationalen Streitfragen. GESIS-Bestände (GLES 2025, Politbarometer, ISSP 2024, ZMSBw) enthalten solche Fragen, bleiben aber gesperrt.
2. Das Eurobarometer liefert aktuelle Fragen mit Zufallsstichprobe, die meisten zu Entscheidungen auf EU-Ebene. Neun Fragen erfüllen die Auswahlregeln und die Tabellenstruktur: gemeinsame Verteidigungs- und Außenpolitik, Zusammenarbeit und Ausgaben für Verteidigung in der EU, EU-Finanzierung militärischer Ausrüstung für die Ukraine, Beitritt der Ukraine, KI-Regulierung, Plattformregulierung, gemeinsame Gesundheitspolitik. Jede Frage trägt ihren Geltungsbereich: sechs Entscheidungen auf EU-Ebene, der Beitritt der Ukraine als EU-Entscheidung mit Zustimmung Deutschlands, KI-Regulierung ohne Ebene, Verteidigungsausgaben „in der EU“ mit offener Ebene. Zwei Forschungsfragen brauchen noch eine Strukturprüfung.
3. ESS12 enthält keine Frage zu den sechs Bereichen, aber die Rückerinnerung an die Bundestagswahl vom 23. Februar 2025. Die erste Datenveröffentlichung ist voraussichtlich für Januar 2027 angekündigt. Ob Deutschland dazugehört, ist nicht bestätigt.
4. Online-Quotenstichproben (OECD Risks that Matter) decken Rente, Gesundheit, Pflege und Wohnen ab, aber nur mit Zahlungsbereitschaft, englischem Wortlaut und ohne Zufallsstichprobe. Die zehn inhaltlich passenden Items sind zurückgestellt, solange kein deutscher Feldwortlaut belegt ist.
5. Die Rechtslage hat sich seit der Matrix geändert, etwa neues Wehrdienstgesetz, neue Grundsicherung, Mindestlohn 13,90 Euro. Nachgetragen in `docs/abdeckung-v2.2.md`.

**Plan.** [Analyseplan v2.3, Entwurf 0.4](../../docs/analyseplan-v2.3.entwurf.md): Quellenklassen Z, T und Q mit eigenen Anzeigeregeln, getrennte Populationen, keine Trendaussagen zwischen historischen und aktuellen Vergleichen, Rollen für Auswahl und Struktur, Regeln für Wählergruppen 2025, Optionen zur Sichtbarkeit der Gruppenvergleiche, Kandidaten in vier Stufen.

**Planprüfung.** Zwei getrennte Codex-Rollen (P4 Methoden und Reproduzierbarkeit, P5 Quellen, Konstrukte und Fairness) in drei Runden:

| Runde | Fassung | P4                             | P5                                      | Offene Punkte danach                                                                                                                         |
| ----- | ------- | ------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | 0.2     | nicht bestanden, sechs Befunde | nicht bestanden, vier Befunde           | alle in Fassung 0.3 bearbeitet                                                                                                               |
| 2     | 0.3     | nicht bestanden, F01 teilweise | nicht bestanden, F02 teilweise, F05 neu | Nennerangabe im Ausnahmeweg, pauschale „EU-Ebene“ in der Entscheidungsvorlage, OECD-Items trotz fehlendem deutschem Wortlaut „vorgeschlagen“ |
| 3     | 0.4     | bestanden                      | bestanden                               | keine                                                                                                                                        |

Runde 3 war eine gezielte Nachprüfung der verbliebenen Befunde, keine neue Gesamtprüfung. Berichte: `reports/claude/pruefungen/P4-*-v23.*` und `P5-*-v23.*`. Der Plan bleibt ein Entwurf ohne Tag. Festgeschrieben wird er erst nach Stevens Quellenfreigabe und mit einem geprüften Itemregister (Plan 4.6).

## 4 Forschungsentwurf und Texte

- Erklärung der 95-%-Bereiche einmal je Ansicht, fehlende 95-%-Bereiche markiert, Messfehler genannt.
- [Textvorschläge](../../docs/vorschlaege-texte-v1.entwurf.md) für Statushinweis, Meta-Beschreibung, Handbuchbegriffe, „repräsentativ“ und Untertitel der Bereiche. Nicht umgesetzt. Codex hat den Inhalt geprüft (K1): Entwurf 1 war nicht bestanden, mit fünf Befunden. Zwei Untertitel ließen gemessene Gegenstände weg oder verengten sie, eine Handbuchzeile nannte noch Dimensionen, die Zukunftsvariante des Statushinweises nannte die Quellen unvollständig, die Meta-Beschreibung stellte den geplanten Test ins Präsens. Entwurf 2 hat die gezielte Nachprüfung bestanden (`reports/claude/pruefungen/K1-*`).
- Analyse der Sichtbarkeit: Die Regel 100/5 lässt bei Skalen von 0 bis 10 nur 6 von 43 Gruppenpaaren mit Zahlen, bei vier oder fünf Stufen deutlich mehr. Optionen im Planentwurf, Abschnitt 8.

## 5 Datenzugriff

Neue Rohdatenzugriffe: zweite Dekodierung der ESS5-Designdatei und Wiederholung der drei Gegenproben (`reports/claude/datenzugriff.md`). Die privaten Läufe wurden nur gelesen. Keine Auswertung neuer Fragen.

## 6 Grenzen dieser Fortsetzung

- Alle Prüfungen sind KI-Reviews. Die Recherche stammt von Claude-Subagents, die Prüfungen von Codex.
- R8 startete einen eigenen Unteragenten zur Rechtslage. Zeitweise liefen dadurch vier statt höchstens drei Agenten.
- Die deutschen Eurobarometer-Wortlaute im Plan stammen aus R6, das sie aus GESIS-Fragebögen übernommen hat. Der deutsche Datenanhang der Kommission enthält dieselben Texte nach einer Stichprobe; je Frage ist das noch zu prüfen. Das Itemregister (Plan 4.6) braucht diesen Anhang. Er enthält auch Ergebnisse, deshalb wartet das Register auf Stevens Entscheidung zum Tabellenweg.
- Der Ausschluss von SP568 QC9 stützt sich nur auf die Formatangabe in R6 und R8, nicht auf den deutschen Originalfragebogen.
- WebKit, physische Geräte und menschliche Screenreader-Tests fehlen.
- Die Rechtslage in R8 und R9 beruht teils auf Fachpresse und ist dort markiert. Das ist keine Rechtsberatung.

## 7 Entscheidungen, die danach von Steven gebraucht werden

1. **GESIS um eine Ausnahme nach § 4 bitten** (Entwurf 1 in `docs/quellenanfragen-v1.entwurf.md`). Empfehlung: ja. Nur das kann nationale Fragen zu Verteidigung, Rente, Pflege und Wohnen öffnen.
2. **Eurobarometer-Tabellen der Kommission für neun Fragen zulassen.** Empfehlung: ja, als getrennter Bevölkerungsvergleich mit dem Geltungsbereich jeder Frage, zusammen mit der Anfrage an das Eurobarometer-Team (Entwurf 3). Ohne dessen Antwort zur Fragebasis keine Zahlen.
3. **Online-Quotenstichproben.** Empfehlung: vorerst nein.
4. **Textvorschläge** annehmen oder ändern (Statushinweis, Meta-Beschreibung, Handbuchbegriffe, „repräsentativ“, Untertitel).
5. Unverändert offen: Gestaltung von Test und Ergebnis, Verständnistest mit fünf Personen, Setup-Abnahme, Freigabe von Merge und Deployment.

Alles Weitere steht in der [Entscheidungsvorlage](../../docs/entscheidungsvorlage-erweiterung-v1.entwurf.md).
