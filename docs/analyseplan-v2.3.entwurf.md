# Analyseplan v2.3: Erweiterung 2025/26 (Entwurf)

ENTWURF 0.1 vom 4. Oktober 2026, verfasst von Claude (Anthropic) im Auftrag von Steven. Dieser Entwurf ist nicht festgeschrieben. Er erlaubt keine Auswertung, keinen Datenabruf und keine Aufnahme neuer Fragen in den Test. Voraussetzungen für jede Auswertung nach diesem Plan:

1. zwei getrennte Prüfungen dieses Entwurfs (Methoden und Reproduzierbarkeit; Quellen, Konstrukte und Fairness),
2. Stevens Freigabe jeder einzelnen Quelle nach der [Entscheidungsvorlage](entscheidungsvorlage-erweiterung-v1.entwurf.md),
3. Festschreibung mit dem Tag `analyseplan-v2.3`.

Der [Analyseplan v2.2](analyseplan-v2.2.md), seine Exporte und Prüfberichte bleiben unverändert. Dieser Entwurf ergänzt sie. Grundlage sind die ergebnisblinden Rechercheberichte R1 bis R3 und R5 bis R10 unter `reports/claude/agenten/`. Alle stammen von Claude-Subagents, also derselben Modellfamilie wie dieser Entwurf.

## 1 Was vor diesem Entwurf bekannt war

- Die Referenzen v2, v2.1 und v2.2 sind veröffentlicht und bekannt. Nichts in diesem Entwurf ist eine unberührte Bestätigung dieser Werte.
- Für die Kandidaten in Abschnitt 11 hat niemand im Projekt Antwortverteilungen gelesen. Die Rechercheberichte R8 bis R10 nennen die Fälle, in denen Suchmaschinen oder Webseiten ungefragt Ergebniszahlen anzeigten. Diese Zahlen wurden nicht verwendet.
- Die Auswahl in diesem Entwurf beruht nur auf Fragebögen, Methoden- und Rechtsdokumenten.

## 2 Ziel

Dieser Entwurf bereitet drei Erweiterungen vor:

1. Fragen für die sechs Bereiche ohne oder fast ohne eigene Frage und für die größten Lücken innerhalb der übrigen Bereiche, aus Erhebungen der Jahre 2024 bis 2026 (Abschnitt 11).
2. Aktualisierte Wählergruppen nach der Rückerinnerung an die Bundestagswahl vom 23. Februar 2025 (Abschnitt 7).
3. Eine Entscheidung über die ungleiche Sichtbarkeit von Gruppenvergleichen durch die Regel 100/5 (Abschnitt 8).

Das Profil bleibt ein Vektor getrennter Originalfragen. Keine Achsen, kein Gesamtwert, keine Perzentile, keine Lagerbezeichnungen.

## 3 Quellenklassen und Populationen

Jede Vergleichsquelle gehört genau einer Klasse an. Die Klasse bestimmt, was die Ansicht zeigen darf.

| Klasse | Beschreibung                                                          | Beispiele                                     | Erlaubte Anzeige                                                                                                                              |
| ------ | --------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Z      | Zufallsstichprobe mit Einzeldaten und dokumentiertem Design           | ESS                                           | Anteile, 95-%-Bereich nach Plan v2.2 Abschnitt 4, Wählergruppen nach Abschnitt 7                                                              |
| T      | Zufallsstichprobe, aber nur veröffentlichte Tabellen ohne Einzeldaten | Eurobarometer-Tabellen der EU-Kommission      | Anteile je Kategorie für Deutschland mit Basis und Feldzeit. Kein Bereich, solange kein Design veröffentlicht ist. Keine Wählergruppen        |
| Q      | Keine Zufallsstichprobe (Quote, Online-Panel)                         | OECD Risks that Matter, ifo Bildungsbarometer | Keine Zahlen, bis Steven Vergleiche mit nicht zufallsbasierten Stichproben grundsätzlich zulässt. Dann nur mit Kennzeichnung und ohne Bereich |

Regeln für Populationen:

- Jeder Vergleich nennt seine Population. ESS: Menschen ab 15 Jahren in Privathaushalten unabhängig von der Staatsangehörigkeit. Eurobarometer: Staatsangehörige von EU-Staaten ab 15 Jahren mit Wohnsitz in Deutschland. Andere Quellen nach ihrer Dokumentation.
- Populationen verschiedener Quellen werden nie zusammengelegt, gemittelt oder gegeneinander verrechnet. Dasselbe gilt für verschiedene Runden derselben Quelle.
- Fehlende Wählergruppen schließen eine Quelle nicht aus. Ein Bevölkerungsvergleich ohne Gruppen ist ein begrenzter, eigener Vergleichstyp.

## 4 Auswahlregeln

Eine Frage kommt als Kandidat in Betracht, wenn sie alle Bedingungen erfüllt:

1. Sie erfragt eine politische Präferenz oder ein politisches Prinzip. Wahrnehmungen, Vertrauen, Bewertungen der Regierung, Wissen und eigenes Verhalten scheiden aus.
2. Sie verkleinert eine dokumentierte Lücke aus der [Themenabdeckung v2.2](abdeckung-v2.2.md) (Spalte „Nicht erfasst“ oder einer der sechs Bereiche). Höchstens drei Fragen je engem Gegenstand.
3. Ihr deutscher Originalwortlaut, die vollständige Antwortliste einschließlich ausdrücklicher „weiß nicht“-Kategorien und der Fragekontext sind aus der Quelle oder ihrer offiziellen Dokumentation belegt.
4. Eine Begründung oder Prämisse im Fragetext, eingeblendete Beträge oder Informationen werden mit der Frage gezeigt und gekennzeichnet. Fragen mit wertender Prämisse scheiden aus.
5. Ihr Geltungsbereich ist gekennzeichnet: Entscheidung Deutschlands, der EU oder beider. Fragen zur EU-Ebene sind zulässig, wenn die Entscheidung Deutschland unmittelbar betrifft. Die Ansicht nennt dann „Entscheidung auf EU-Ebene“.
6. Die Feldzeit liegt in den Jahren 2024 bis 2026. Ältere Fragen nur mit ausdrücklicher Begründung und Zeitvermerk.
7. Der Zugang ist nach dem Quellenbericht R10 durch eine vorhandene Lizenz erlaubt (Klasse C) oder von Steven ausdrücklich freigegeben. Ausdrücklich verbotene Nutzungen (Klasse A) scheiden aus. Ungeklärte Bedingungen (Klasse B) werden vor jeder Datenverarbeitung geklärt.
8. Sie ist kein Zweig einer Zufallsvignette mit eigenem Nenner.

Die Auswahl ist ergebnisblind. Die Auswahlrolle liest nur Fragebögen, Methoden- und Rechtsdokumente. Enthält eine Quelle die Fragen nur zusammen mit Ergebnissen, prüft eine getrennte technische Rolle die Struktur nach Abschnitt 10 und gibt keine Verteilungen an die Auswahlrolle weiter. Keine Frage wird nach Sichtung ihrer Ergebnisse aufgenommen, entfernt, umgepolt oder einem anderen Bereich zugeordnet.

## 5 Historische und aktuelle Vergleiche

- Jeder Vergleich nennt Quelle, Ausgabe oder Welle, Feldzeit, Population, Stichprobenart und Modus.
- Historische Vergleiche (ESS 2010 bis 2023) und aktuelle Vergleiche (2024 bis 2026) stehen getrennt und gekennzeichnet nebeneinander, wenn eine Frage in beiden vorkommt. Sie werden nicht gemittelt und nicht als Entwicklung gedeutet. Keine Aussagen über Veränderungen, keine Signifikanztests.
- Zeitbezogene Formulierungen („heute“, „schon jetzt“, „derzeit“) erhalten wie in v2.2 einen Hinweis auf den Bezugspunkt der damaligen Befragten.
- Kontextangaben trennen drei Ebenen: geltende Rechtslage mit Fundstelle und Stand, politische Vorschläge mit Urheber und Datum, gemessene Einstellungen. Vorschläge erscheinen nie als geltendes Recht.

## 6 Publikations- und Anzeigeregeln

- **Klasse Z:** unverändert nach Plan v2.2 Abschnitte 4 und 6 (mindestens 100 gültige Antworten, keine beobachtete Kategorie mit eins bis vier Fällen, 95-%-Bereiche).
- **Klasse T:** Zahlen nur, wenn die Tabelle für Deutschland alle Antwortkategorien einschließlich „weiß nicht“, die ungewichtete Basis und die verwendete Gewichtung nennt. Die Werte überträgt die technische Rolle zweimal unabhängig. Beide Übertragungen müssen übereinstimmen. Kein 95-%-Bereich und keine selbst berechnete Unsicherheit ohne veröffentlichtes Design. Die Ansicht sagt das ausdrücklich: Ein fehlender Bereich bedeutet keine Unsicherheit von null.
- **Klasse Q:** keine Zahlen bis zu Stevens Grundsatzentscheidung.

## 7 Wählergruppen nach der Bundestagswahl 2025

- Quelle nur Klasse Z mit Rückerinnerung an die Zweitstimme. Wahlabsicht und Parteinähe sind andere Merkmale und bilden keine Wählergruppen im Sinne von v2.1.
- Gruppendefinition, Vorrang der Teilnahme an der Wahl, Prüfung der Codeinventare, Bilanz und Regel 100/5 wie im Gruppenvertrag v2.1. Ein neuer Gruppenvertrag v2.3 bindet die Parteiliste der neuen Erhebung vor jeder Dateneinsicht.
- Gruppen verschiedener Wahlen werden nicht verglichen oder als Entwicklung dargestellt.
- Kandidat ist ESS Runde 12, sobald Daten und deutscher Fragebogen veröffentlicht sind (Abschnitt 11). Bis dahin entsteht nichts.

## 8 Sichtbarkeit der Gruppenvergleiche

In den Referenzen v2.2 tragen von den Wählergruppenpaaren mit Zahlen 6 von 43 Paaren bei Skalen von 0 bis 10, 22 von 45 bei vier Antwortstufen, 58 von 139 bei fünf und 10 von 63 bei sechs Kategorien. Grundlage sind nur die öffentlichen Status in `data/reference-v2.2/`. Kleine Gruppen und lange Skalen verlieren ihre Vergleiche häufiger, weil eine einzelne Kategorie mit eins bis vier Fällen die ganze Referenz sperrt. Welche Parteien zu welchem Thema erscheinen, hängt dadurch von Gruppengröße und Skalenlänge ab (V2-F14).

Optionen, keine davon ist beschlossen:

- **A Status quo.** Regel bleibt, die Ansicht nennt je Gruppe die Zahl der verfügbaren Vergleiche (seit dem 3. Oktober 2026 umgesetzt).
- **B Unterdrückung einzelner Zellen.** Die Referenz erscheint, Kategorien mit eins bis vier Fällen zeigen „unter 5 Fälle“. Weil Summe und übrige Anteile bekannt sind, ließe sich die Zelle zurückrechnen. B braucht deshalb eine zweite unterdrückte Zelle oder eine Begründung, warum das bei öffentlich verfügbaren ESS-Einzeldaten unerheblich ist.
- **C Andere Präzisionsregel.** Statt der Zellregel ein Kriterium für die Breite der 95-%-Bereiche. Jede Schwelle wäre eine neue Projektentscheidung und bräuchte eine Begründung vor Sichtung.

Empfehlung: A beibehalten, B und C in der Planprüfung bewerten lassen. Eine Änderung gilt erst nach Festschreibung und dann für alle Studien gleich.

## 9 Integration in das Antwortprofil

- Neue Fragen nutzen die vorhandenen Satzformen der [Profilregeln v1](profilregeln-v1.md) mit eigener Richtungstabelle je Frage.
- Neue Blockmuster nur für Originalblöcke mit gleicher Einleitung und Antwortliste. Neue Querbezüge nur, wenn dieser Plan sie vor der Festschreibung nennt.
- Fragen zur EU-Ebene tragen den Kontext „Entscheidung auf EU-Ebene“. Fragen mit eingeblendeten Informationen zeigen diese Informationen.
- Die Themenabdeckung wird nach der Aufnahme neu bewertet. Eine Lücke gilt erst als verkleinert, wenn eine Frage tatsächlich im Profil steht.

## 10 Rollen, Prüfungen und Freigaben

1. Auswahlrolle: ergebnisblind, liest nur Fragebögen, Methoden und Bedingungen.
2. Technische Rolle: prüft bei Klasse T die Struktur veröffentlichter Tabellen (Kategorien, Basis, Gewichtung, Fußnoten) und meldet nur ein festes Formular ohne Werte an die Auswahlrolle. Die Übertragung der Werte erfolgt erst nach Festschreibung.
3. Zwei getrennte Planprüfungen durch frische Prüfagenten: Methoden und Reproduzierbarkeit; Quellen, Konstrukte und Fairness. Danach Korrekturen und gezielte Nachprüfung.
4. Stevens Freigabe je Quelle. Die Entscheidungsvorlage nennt Empfehlung und Folgen.
5. Festschreibung mit Tag `analyseplan-v2.3`, danach Datenabruf, Ergebnisprüfung vor dem Export und ausdrückliche Exportentscheidung wie in v2.2.

## 11 Kandidaten

KANDIDATEN

## 12 Stopps

- Keine Quelle mit Klasse A. GESIS-Bestände bleiben gesperrt, bis Steven die Ausnahme nach § 4 geklärt hat.
- Fehlt für eine Quelle die Freigabe, bleibt ihr Bereich sichtbar als Lücke.
- Zeigt die technische Prüfung, dass eine Tabelle die Bedingungen aus Abschnitt 6 nicht erfüllt, entfällt die Frage ohne Ersatz aus derselben Quelle nach Ergebnissicht.
