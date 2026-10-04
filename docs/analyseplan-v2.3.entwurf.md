# Analyseplan v2.3: Erweiterung 2025/26 (Entwurf)

ENTWURF 0.3 vom 4. Oktober 2026, verfasst von Claude (Anthropic) im Auftrag von Steven. Fassung 0.1 entstand aus den Rechercheberichten R8 bis R10. Fassung 0.2 legte nach der Strukturprüfung S1 (`reports/claude/agenten/S1-strukturpruefung-eurobarometer.md`) Regeln für Tabellen ohne Basis je Frage fest. Fassung 0.2 erhielt zwei getrennte Codex-Prüfungen (Prüfpaket `PLAN-V23-001`, `reports/claude/pruefungen/P4-methoden-v23.*` und `P5-quellen-fairness-v23.*`). Beide waren nicht bestanden. Fassung 0.3 setzt ihre Korrekturen um; Abschnitt 13 nennt sie. S1 hat nur Struktur, Basen und Methodenangaben gemeldet. Ergebniswerte kennt die Auswahlrolle weiterhin nicht.

Dieser Entwurf ist nicht festgeschrieben. Er erlaubt keine Auswertung, keinen Datenabruf und keine Aufnahme neuer Fragen in den Test. Voraussetzungen für jede Auswertung nach diesem Plan:

1. bestandene Prüfungen dieses Entwurfs (Methoden und Reproduzierbarkeit; Quellen, Konstrukte und Fairness),
2. Stevens Freigabe jeder einzelnen Quelle nach der [Entscheidungsvorlage](entscheidungsvorlage-erweiterung-v1.entwurf.md),
3. Festschreibung mit dem Tag `analyseplan-v2.3`.

Der [Analyseplan v2.2](analyseplan-v2.2.md), seine Exporte und Prüfberichte bleiben unverändert. Dieser Entwurf ergänzt sie. Grundlage sind die ergebnisblinden Rechercheberichte R1 bis R3 und R5 bis R10 unter `reports/claude/agenten/`. Alle stammen von Claude-Subagents, also derselben Modellfamilie wie dieser Entwurf.

## 1 Was vor diesem Entwurf bekannt war

- Die Referenzen v2, v2.1 und v2.2 sind veröffentlicht und bekannt. Nichts in diesem Entwurf ist eine unberührte Bestätigung dieser Werte.
- Für die Kandidaten in Abschnitt 11 hat niemand in der Auswahlrolle Antwortverteilungen gelesen. Die technische Rolle S1 hat Tabellen geöffnet und nur Struktur, Basen von Fragen an alle Befragten und Methodenangaben gemeldet. Die Rechercheberichte R8 bis R10 nennen die Fälle, in denen Suchmaschinen oder Webseiten ungefragt Ergebniszahlen anzeigten. Diese Zahlen wurden nicht verwendet.
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
| T      | Zufallsstichprobe, aber nur veröffentlichte Tabellen ohne Einzeldaten | Eurobarometer-Tabellen der EU-Kommission      | nur unter den Bedingungen in Abschnitt 6. Kein Bereich, solange kein Design veröffentlicht ist. Keine Wählergruppen                           |
| Q      | Keine Zufallsstichprobe (Quote, Online-Panel)                         | OECD Risks that Matter, ifo Bildungsbarometer | Keine Zahlen, bis Steven Vergleiche mit nicht zufallsbasierten Stichproben grundsätzlich zulässt. Dann nur mit Kennzeichnung und ohne Bereich |

Regeln für Populationen:

- Jeder Vergleich nennt seine Population. ESS: Menschen ab 15 Jahren in Privathaushalten unabhängig von der Staatsangehörigkeit. Eurobarometer: Staatsangehörige von EU-Staaten ab 15 Jahren mit Wohnsitz in Deutschland. Andere Quellen nach ihrer Dokumentation.
- Populationen verschiedener Quellen werden nie zusammengelegt, gemittelt oder gegeneinander verrechnet. Dasselbe gilt für verschiedene Runden derselben Quelle.
- Fehlende Wählergruppen schließen eine Quelle nicht aus. Ein Bevölkerungsvergleich ohne Gruppen ist ein begrenzter, eigener Vergleichstyp.

## 4 Auswahlregeln

### 4.1 Bedingungen

Eine Frage kommt als Kandidat in Betracht, wenn sie alle Bedingungen erfüllt:

1. Sie erfragt eine politische Präferenz, ein politisches Prinzip oder eine ausdrücklich so bezeichnete Zahlungsbereitschaft für öffentliche Leistungen. Wahrnehmungen, Vertrauen, Bewertungen der Regierung, Wissen und eigenes Verhalten scheiden aus.
2. Sie verkleinert eine dokumentierte Lücke aus der [Themenabdeckung v2.2](abdeckung-v2.2.md) (Spalte „Nicht erfasst“ oder einer der sechs Bereiche). Der Gegenstand der Frage muss diese Lücke betreffen. Ein Kontext, der den Gegenstand auf einen anderen Anlass einengt, erfüllt die Bedingung nicht.
3. Ihr deutscher Originalwortlaut, die vollständige Antwortliste einschließlich ausdrücklicher „Weiß nicht“-Kategorien und der Fragekontext sind aus der Quelle oder ihrer offiziellen Dokumentation belegt.
4. Ihr Fragetext besteht die Regel für Rahmungen in Abschnitt 4.2 und die Ausschlusskriterien in Abschnitt 4.3.
5. Ihr Geltungsbereich ist nach Abschnitt 4.4 gekennzeichnet.
6. Die Feldzeit liegt in den Jahren 2024 bis 2026. Ältere Fragen nur mit ausdrücklicher Begründung und Zeitvermerk.
7. Der Zugang ist nach dem Quellenbericht R10 durch eine vorhandene Lizenz erlaubt (Klasse C) oder von Steven ausdrücklich freigegeben. Ausdrücklich verbotene Nutzungen (Klasse A) scheiden aus. Ungeklärte Bedingungen (Klasse B) werden vor jeder Datenverarbeitung geklärt.
8. Sie ist kein Zweig einer Zufallsvignette mit eigenem Nenner und steht nicht nach einem randomisierten Informationsexperiment, das ihre Antworten beeinflussen kann.

### 4.2 Rahmungen im Fragetext

Jeder Bestandteil des Fragetexts, der über den Gegenstand hinausgeht, gehört genau einer Art an:

| Art                                     | Beschreibung                                                                                                             | Folge                                                       | Beispiele                                                                                                                                                                    |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| a Sachlicher Anlass                     | Überprüfbare Feststellung einer bestehenden Lage oder Entscheidung, ohne Wertung und ohne Grund für eine Antwortrichtung | zulässig, mit der Frage gezeigt                             | ST0350-Einleitung: „Die EU hat als Reaktion auf die russische Invasion in der Ukraine eine Reihe von Maßnahmen ergriffen.“                                                   |
| b Zweck oder Begründung für eine Option | Satzteil, der einen Grund für eine Antwortrichtung angibt („um …“, „weil …“, „as …“, „to provide …“)                     | Ausschluss, weil er ein Argument nur für eine Seite liefert | ST0939 „um ihre Interessen zu verteidigen“; OECD Q20, Q27 f, Q34 a                                                                                                           |
| c Wertende Zielformel oder Wort         | Wertender Begriff oder ein als gut gesetztes Ziel im Gegenstand                                                          | Ausschluss                                                  | ST0359 „bis dauerhaft gerechter Frieden herrscht“; SE035 „gerechte Besteuerung“                                                                                              |
| d Bedingung                             | Die Präferenz gilt unter einer genannten Bedingung                                                                       | zulässig, Bedingung mit der Frage gezeigt                   | SP564 QC5 „sobald sie alle Bedingungen für die Mitgliedschaft erfüllt haben“                                                                                                 |
| e Zweiseitige Abwägung                  | Beide Antwortrichtungen nennen ihren Preis                                                                               | zulässig                                                    | SP572 QB12 („auch wenn … Einschränkungen“ / „auch wenn … Sicherheitsrisiken“); OECD Q19 (eigene Kosten von 2 % des Einkommens für bessere Leistungen, für jedes Item gleich) |
| f Einengender Kontext                   | Die Frage gilt nur für einen bestimmten Anlass, der nicht der Gegenstand der Lücke ist                                   | Ausschluss nach 4.1 Nr. 2                                   | OECD Q27 e (Arbeitszeitbegrenzung „as a response to digitalisation“)                                                                                                         |

Der Unterschied zwischen ST0350 Item 2 und ST0939: Die ST0350-Einleitung stellt fest, dass die EU Maßnahmen ergriffen hat; das Item selbst nennt keinen Grund für Zustimmung. Das ST0939-Item nennt den Zweck „um ihre Interessen zu verteidigen“ und damit einen Grund für eine Antwortrichtung.

### 4.3 Weitere Ausschlusskriterien

- **Zwei Gegenstände:** Das Item fragt nach zwei Maßnahmen oder Objekten, die man verschieden beantworten könnte (ST0350 Item 1: Sanktionen und eingefrorene Vermögenswerte; Item 4: finanzielle und humanitäre Hilfe).
- **Format ohne Gegenposition:** Wichtigkeit oder Dringlichkeit einer Maßnahme, bei der Ablehnung nicht ausdrückbar ist (SP566 QE4, QE6, SP554 QB11), oder eine Prioritätenliste ohne Richtung (SP546 QB4).
- **Unerklärter Fachbegriff:** Der Gegenstand ist ein Fachbegriff, dessen Inhalt aus dem Wortlaut nicht hervorgeht (SE037 „digitaler Binnenmarkt“).
- **Überholter Gegenstand:** Die Frage betrifft eine abgeschlossene Entscheidung, zu der eine neuere Frage vorliegt (ST0350 Item 5, Bewerberstatus der Ukraine von 2022; ersetzt durch SP564 QC5).
- **Wortlaut fehlt:** Der deutsche Wortlaut ist nicht belegt (SP568 QC9).

### 4.4 Geltungsbereich

Jede Frage erhält genau eine Kennzeichnung nach ihrem Wortlaut, nicht nach der Erhebung, aus der sie stammt:

- **Entscheidung auf EU-Ebene:** Die Frage nennt die EU oder ihre Mitgliedstaaten als Handelnde. Deutschland wirkt im Rat mit.
- **EU-Entscheidung mit Zustimmung Deutschlands:** Die Entscheidung braucht die Ratifikation durch alle Mitgliedstaaten (Beitritte, Art. 49 EUV).
- **Ohne Ebene:** Die Frage nennt keine handelnde Ebene. Sie misst eine allgemeine Präferenz oder ein Prinzip.
- **Ebene offen:** Der Wortlaut lässt mehrere Ebenen zu. Die Ansicht nennt die Mehrdeutigkeit.
- **Entscheidung Deutschlands:** Die Frage nennt Deutschland, Bund oder Bundesregierung als Handelnde.

### 4.5 Auswahl bei mehr als drei Fragen zum selben engen Gegenstand

Vorrang haben Fragen, die verschiedene Seiten des Gegenstands abdecken, vor Fragen zu Einzelheiten desselben Instruments. Bei der Verteidigungszusammenarbeit der EU sind das das Ziel einer gemeinsamen Politik (SE037), das Maß der Zusammenarbeit (ST0359 „Zusammenarbeit“) und die Ausgaben (ST0359 „Geld“). Die Items zu Beschaffung und Produktionskapazitäten betreffen Instrumente derselben Zusammenarbeit und treten zurück.

### 4.6 Status und Itemregister

Jeder Kandidat hat genau einen Status: **vorgeschlagen** (alle Bedingungen erfüllt, Freigaben offen), **zurückgestellt** (eine benannte Bedingung ist noch nicht geprüft) oder **ausgeschlossen** (mit Regel). Vor jeder Übertragung von Werten entsteht ein eingefrorenes Itemregister je vorgeschlagenem Kandidaten mit Welle, Frage- und Itemnummer, vollständigem deutschem Wortlaut, Einleitung, Antwortkategorien, Kontext nach 4.2, Geltungsbereich nach 4.4 und Status. Das Register wird mit dem Plan geprüft und festgeschrieben.

Die Auswahl ist ergebnisblind. Die Auswahlrolle liest nur Fragebögen, Methoden- und Rechtsdokumente. Enthält eine Quelle die Fragen nur zusammen mit Ergebnissen, prüft eine getrennte technische Rolle die Struktur nach Abschnitt 10. Technische Rollen, die Ergebnisse gesehen haben, melden nur vorab festgelegte Strukturfehler und treffen keine Inhaltsentscheidung. Neue Inhaltsentscheidungen brauchen eine neue ergebnisblinde Prüfung. Keine Frage wird nach Sichtung ihrer Ergebnisse aufgenommen, entfernt, umgepolt oder einem anderen Bereich zugeordnet.

## 5 Historische und aktuelle Vergleiche

- Jeder Vergleich nennt Quelle, Ausgabe oder Welle, Feldzeit, Population, Stichprobenart und Modus.
- Historische Vergleiche (ESS 2010 bis 2023) und aktuelle Vergleiche (2024 bis 2026) stehen getrennt und gekennzeichnet nebeneinander, wenn eine Frage in beiden vorkommt. Sie werden nicht gemittelt und nicht als Entwicklung gedeutet. Keine Aussagen über Veränderungen, keine Signifikanztests.
- Zeitbezogene Formulierungen („heute“, „schon jetzt“, „derzeit“) erhalten wie in v2.2 einen Hinweis auf den Bezugspunkt der damaligen Befragten.
- Kontextangaben trennen drei Ebenen: geltende Rechtslage mit Fundstelle und Stand, politische Vorschläge mit Urheber und Datum, gemessene Einstellungen. Vorschläge erscheinen nie als geltendes Recht.

## 6 Publikations- und Anzeigeregeln

- **Klasse Z:** unverändert nach Plan v2.2 Abschnitte 4 und 6 (mindestens 100 gültige Antworten, keine beobachtete Kategorie mit eins bis vier Fällen, 95-%-Bereiche).
- **Klasse T:** Die Strukturprüfung S1 zeigt, dass die Tabellen der Kommission je Frage eine Spalte für Deutschland, alle Kategorien einzeln und „Don't know“ als eigene Zeile enthalten. Was sie über Basis und Nenner sagen, wird getrennt benannt:

  | Angabe                                             | Stand nach S1                                                       |
  | -------------------------------------------------- | ------------------------------------------------------------------- |
  | Frageuniversum                                     | in der Tabelle („Base: All respondents“ oder Filter)                |
  | gewichtete Tabellenbasis                           | in der Tabelle                                                      |
  | Interviews in Deutschland                          | Technische Spezifikation der Welle, eine Angabe für die ganze Welle |
  | ungewichtete auswertbare Basis je Frage            | nicht dokumentiert                                                  |
  | Umgang mit Verweigerung und sonstigem Item-Missing | nicht dokumentiert. Eine Zeile für Verweigerung gibt es nicht       |
  | Gewichtungsvariable und Zusammenführung West/Ost   | nicht dokumentiert. Die Spezifikation beschreibt nur das Verfahren  |

  Die Interviewzahl ist nur ein Merkmal der Welle. Sie wird nicht als Basis der einzelnen Frage ausgegeben. Daraus folgt:
  1. Nur Fragen, die laut Tabelle allen Befragten gestellt wurden, aus Wellen mit persönlichem Interview in Deutschland. Gefilterte Fragen und Online-Befragungen (etwa Flash-Eurobarometer) scheiden aus.
  2. **Standard: keine Zahlen**, solange die ungewichtete Basis je Frage und der Umgang mit fehlenden Antworten nicht geklärt sind. Die Anfrage an das Eurobarometer-Team (Entwurf 3 in `docs/quellenanfragen-v1.entwurf.md`) soll das klären.
  3. Ohne Klärung darf Steven die Übernahme der veröffentlichten Anteile ausdrücklich unter dieser Grenze freigeben. Dann nennt die Ansicht: „Anteile wie veröffentlicht, bezogen auf alle Befragten einschließlich ‚Weiß nicht‘. Wie viele Befragte diese Frage tatsächlich beantwortet haben und wie fehlende Antworten behandelt wurden, ist nicht veröffentlicht.“ Der Nenner unterscheidet sich vom ESS, wo nur gültige Antworten zählen. Kein Umrechnen auf gültige Antworten.
  4. Die Tabellen speichern ganze Prozentpunkte. Die Ansicht zeigt sie ohne Nachkommastelle und nennt das. Keine Normierung auf 100.
  5. Der deutsche Wortlaut stammt aus dem deutschen Datenanhang der Kommission zur selben Welle und wird je Frage im Itemregister (4.6) festgehalten. Fehlt er dort, ist die Frage zurückgestellt, bis die Rechte am Wortlaut geklärt sind.
  6. Je Frage gilt die jüngste Welle mit persönlichem Interview, in der die Tabelle eindeutig zur Fragenummer des deutschen Fragebogens passt.
  7. **Doppelte Übertragung.** Zwei getrennte Übertragungen aus denselben gepinnten Originaldateien (SHA-256). Die zweite entsteht ohne Einsicht in die erste und möglichst mit einer anderen Methode (etwa Volume A und Volume C für Deutschland oder Tabelle und Datenanhang). Jede Zelle ist gebunden an Datei und Hash, Welle, Spalte Deutschland, Frage und Item, Kategorienbeschriftung, Blatt und Zeile sowie die Originaldarstellung. Abgeglichen werden Werte, Vollständigkeit der Kategorien, Frageuniversum und gewichtete Basis. Jede Abweichung sperrt die Frage, bis sie mit erhaltenen Fassungen belegt aufgelöst ist. Keine Handkorrektur.
  8. Kein 95-%-Bereich und keine selbst berechnete Unsicherheit ohne veröffentlichtes Design. Die Ansicht sagt das: Ein fehlender Bereich bedeutet keine Unsicherheit von null.
  9. Gliederungen aus Volume C, etwa nach Links-Rechts-Einstufung, gehören nicht zu diesem Plan.

- **Klasse Q:** keine Zahlen bis zu Stevens Grundsatzentscheidung. Bei Mehrfachauswahl (OECD Q19) gilt: Ein nicht ausgewähltes Item bedeutet weder Ablehnung noch fehlende Zahlungsbereitschaft für diesen Bereich.

## 7 Wählergruppen nach der Bundestagswahl 2025

- Quelle nur Klasse Z mit Rückerinnerung an die Zweitstimme. Wahlabsicht und Parteinähe sind andere Merkmale und bilden keine Wählergruppen im Sinne von v2.1.
- Gruppendefinition, Vorrang der Teilnahme an der Wahl, Prüfung der Codeinventare, Bilanz und Regel 100/5 wie im Gruppenvertrag v2.1.
- Ein eigener, versionierter, getrennt geprüfter und mit Tag festgeschriebener ESS12-Vertrag legt vor jeder Einsicht in neue Antworten fest: Modustrennung oder begründete Zusammenfassung von persönlichem Interview und Selbstausfüller, Zielpopulation, Design- und Poststratifikationsgewichte, Missing- und Filterregeln je Modus, ausreichende Identität der Kategorien je Modus, Parteiliste und Codes, und eine Ausfallregel, falls eine Bedingung nicht erfüllt ist. Das gilt für Wählergruppen und für aktualisierte Einzelreferenzen. Deutsche Codes, Gewichte und das konkrete Verfahren dürfen bis zur Veröffentlichung der Dokumente offen bleiben.
- Gruppen verschiedener Wahlen werden nicht verglichen oder als Entwicklung dargestellt.
- Kandidat ist ESS Runde 12, sobald Daten und deutscher Fragebogen tatsächlich veröffentlicht sind (Abschnitt 11.2). Bis dahin entsteht nichts.

## 8 Sichtbarkeit der Gruppenvergleiche

**Beobachtung.** Von den Wählergruppenpaaren der Referenzen v2.2 tragen Zahlen: 6 von 43 bei Skalen von 0 bis 10, 22 von 45 bei vier Antwortstufen, 58 von 139 bei fünf und 10 von 63 bei sechs Kategorien. Grundlage sind nur die öffentlichen Status in `data/reference-v2.2/`; die Methodenprüfung P4 hat die Zählungen bestätigt.

**Mechanismus.** Die Regel 100/5 sperrt eine Referenz, wenn die Gesamtbasis unter 100 liegt oder eine beobachtete Kategorie eins bis vier Fälle hat. Der Status `withheld_base_or_cell_count` unterscheidet beide Gründe nicht. Gruppengröße und Skalenlänge sind plausible Einflussgrößen. Mit den Statuszählungen allein sind sie nicht getrennt geprüft, und die Zählungen vergleichen verschiedene Fragen und Studien.

**Optionen**, keine beschlossen:

- **A Status quo.** Regel bleibt, die Ansicht nennt je Gruppe die Zahl der verfügbaren Vergleiche (seit dem 3. Oktober 2026 umgesetzt).
- **B Unterdrückung einzelner Zellen.** Offener Verfahrensentwurf. Kategorien mit eins bis vier Fällen zeigten „unter 5 Fälle“. Gesamtbasis, übrige Anteile, Rundung und weitere Veröffentlichungen können die verdeckten Werte eingrenzen; eine zweite verdeckte Zelle allein schützt nicht. B bräuchte eine Prüfung aller veröffentlichten Rand- und Ergänzungsangaben und müsste Anteil, Gewichtssumme und ungewichtete Fallzahl unterscheiden.
- **C Präzisionsregel.** Ein Kriterium für die Breite der 95-%-Bereiche betrifft die Präzision, nicht den Schutz vor Rückrechnung. C käme nur mit getrennt begründetem Präzisions- und Offenlegungskonzept in Frage.

**Empfehlung:** A. B und C nur mit eigenem, festgeschriebenem Plan und eigenen Exportprüfungen, dann für alle Studien gleich.

## 9 Integration in das Antwortprofil

- Neue Fragen nutzen die vorhandenen Satzformen der [Profilregeln v1](profilregeln-v1.md) mit eigener Richtungstabelle je Frage.
- Neue Blockmuster nur für Originalblöcke mit gleicher Einleitung und Antwortliste. Neue Querbezüge nur, wenn dieser Plan sie vor der Festschreibung nennt.
- Die Ansicht nennt den Geltungsbereich nach 4.4 und zeigt Anlass und Bedingungen nach 4.2 mit der Frage.
- Die Themenabdeckung wird nach der Aufnahme neu bewertet. Eine Lücke gilt erst als verkleinert, wenn eine Frage tatsächlich im Profil steht.

## 10 Rollen, Prüfungen und Freigaben

1. Auswahlrolle: ergebnisblind, liest nur Fragebögen, Methoden und Bedingungen. Erstellt das Itemregister (4.6).
2. Technische Rolle: prüft bei Klasse T die Struktur veröffentlichter Tabellen und meldet nur ein vorab festgelegtes Formular ohne Werte. Sie überträgt Werte erst nach Festschreibung nach Abschnitt 6 Nr. 7.
3. Zwei getrennte Planprüfungen durch frische Prüfagenten: Methoden und Reproduzierbarkeit; Quellen, Konstrukte und Fairness. Danach Korrekturen und gezielte Nachprüfung.
4. Stevens Freigabe je Quelle. Die Entscheidungsvorlage nennt Empfehlung und Folgen.
5. Festschreibung mit Tag `analyseplan-v2.3`, danach Datenabruf, Ergebnisprüfung vor dem Export und ausdrückliche Exportentscheidung wie in v2.2.

## 11 Kandidaten

Grundlage: `reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json` (37 Kandidaten), `R9-erweiterung-sozial-wohnen-gruppen.json` (37 Kandidaten) und der OECD-Fragebogen 2024 (SHA-256 `5672381901f57dcc2ee3e76a9b0716b6c418c3a69e1e85b804e29bb2c343ae10`). Die Auswahl wendet Abschnitt 4 an, ohne Kenntnis von Ergebnissen. Alle Kandidaten sind Forschungsentwürfe. Keiner ist in den Test aufgenommen.

### 11.1 Stufe 1: Eurobarometer-Tabellen der Kommission (Klasse T)

Voraussetzungen: Stevens Freigabe des Tabellenwegs, Klärung oder ausdrückliche Freigabe nach Abschnitt 6 Nr. 2 und 3, deutscher Wortlaut nach Abschnitt 6 Nr. 5. Nach S1 sind die Fragen der Wellen 104.1, 103.2, 105.1 und 105.2 unten an alle Befragten gestellt und eindeutig zugeordnet. Für SE037 gilt die Welle 105.2 (Frage QB2), für ST0350 und ST0359 die Welle 104.1, weil ihre Zuordnung in 105.2 unklar ist.

| Kandidat               | Bereich                                    | Welle, Feldzeit Deutschland             | Gegenstand                                                                             | Geltungsbereich (4.4)                          | Rahmung (4.2)                  | Status                                |
| ---------------------- | ------------------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------ | ------------------------------------- |
| R8-EB-SE037-GSVP       | Außen-, Verteidigungs- und Friedenspolitik | EB 105.2, 12. März–1. April 2026        | gemeinsame Verteidigungs- und Sicherheitspolitik der EU-Mitgliedstaaten, dafür/dagegen | Entscheidung auf EU-Ebene                      | –                              | vorgeschlagen                         |
| R8-EB-SE037-GASP       | Außen-, Verteidigungs- und Friedenspolitik | EB 105.2, 12. März–1. April 2026        | gemeinsame Außenpolitik der Mitgliedstaaten der EU, dafür/dagegen                      | Entscheidung auf EU-Ebene                      | –                              | vorgeschlagen                         |
| R8-EB-ST0359-ZUS       | Außen-, Verteidigungs- und Friedenspolitik | EB 104.1, 9.–29. Oktober 2025           | Zusammenarbeit auf EU-Ebene bei Verteidigungsfragen verstärken, Zustimmung             | Entscheidung auf EU-Ebene                      | –                              | vorgeschlagen                         |
| R8-EB-ST0359-GELD      | Außen-, Verteidigungs- und Friedenspolitik | EB 104.1, 9.–29. Oktober 2025           | mehr Geld für Verteidigung „in der EU“, Zustimmung                                     | Ebene offen (EU-Haushalt oder Mitgliedstaaten) | –                              | vorgeschlagen                         |
| R8-EB-ST0350-2         | Außen-, Verteidigungs- und Friedenspolitik | EB 104.1, 9.–29. Oktober 2025           | EU-Finanzierung militärischer Ausrüstung für die Ukraine, Zustimmung                   | Entscheidung auf EU-Ebene                      | a, bereits ergriffene Maßnahme | vorgeschlagen                         |
| R8-EB-SP564-QC5-UA     | Europäische Integration                    | EB 103.2, 19. Februar–10. März 2025     | Beitritt der Ukraine, dafür/dagegen                                                    | EU-Entscheidung mit Zustimmung Deutschlands    | d                              | vorgeschlagen                         |
| R8-EB-SP572-QB12-KI    | Medien und Digitalpolitik                  | EB 105.1, 5.–24. Februar 2026           | KI sorgfältig regulieren oder möglichst wenig einschränken                             | ohne Ebene                                     | e                              | vorgeschlagen                         |
| R8-EB-SP572-QB5-6      | Medien und Digitalpolitik                  | EB 105.1, 5.–24. Februar 2026           | Regulierung von Online-Plattformen stärken, Zustimmung                                 | Entscheidung auf EU-Ebene                      | –                              | vorgeschlagen                         |
| R9-21                  | Gesundheit und Pflege                      | EB 105.2, 12. März–1. April 2026        | gemeinsame EU-Gesundheitspolitik, dafür/dagegen                                        | Entscheidung auf EU-Ebene                      | –                              | vorgeschlagen                         |
| R8-EB-SP557-QA7-OA     | Bildung und Forschung                      | EB 102.1, 13. September–4. Oktober 2024 | Ergebnisse öffentlich finanzierter Forschung kostenlos online, Zustimmung              | ohne Ebene                                     | –                              | zurückgestellt: Strukturprüfung fehlt |
| R8-EB-SP557-QA7-GRENZE | Bildung und Forschung                      | EB 102.1, 13. September–4. Oktober 2024 | keine Grenze für wissenschaftliche Forschung, Zustimmung                               | ohne Ebene                                     | –                              | zurückgestellt: Strukturprüfung fehlt |

Ausgeschlossen, mit Regel: ST0350 Item 1 und Item 4 (4.3 zwei Gegenstände), ST0350 Item 5 (4.3 überholter Gegenstand), ST0359 „bis dauerhaft gerechter Frieden herrscht“ (4.2 c), ST0359 Beschaffung und Produktion (4.5), ST0939 Gegenzölle (4.2 b, Zweckangabe), SE035 Item 5 (4.2 c, „gerechte“), SE037 digitaler Binnenmarkt (4.3 Fachbegriff), SP566 QE4 und QE6, SP554 QB11, SP546 QB4 (4.3 Format ohne Gegenposition), SP568 QC9 (4.3 Wortlaut fehlt).

Reichweite: Sechs vorgeschlagene Fragen betreffen Entscheidungen auf EU-Ebene, eine eine EU-Entscheidung mit Zustimmung Deutschlands, eine nennt keine Ebene, eine ist mehrdeutig. Die zurückgestellten SP557-Fragen nennen keine Ebene. Keine dieser Fragen schließt eine nationale Kernlücke: Wehrdienst, deutscher Verteidigungshaushalt, deutsche Waffenlieferungen, Rüstungsexporte, Rundfunkbeitrag, IP-Adressen, Gesichtserkennung, Mindestalter für soziale Medien, Bildungsföderalismus, BAföG, Kita, Rente, Pflege, Mieten und Grundsteuer bleiben offen.

### 11.2 Stufe 2: ESS Runde 12 (Klasse Z)

Die ESS kündigt die erste Datenveröffentlichung der Runde 12 voraussichtlich für Januar 2027 an. Ob Deutschland und der deutsche Fragebogen dazugehören, ist nicht bestätigt (R9). Der Beginn hängt an der tatsächlich veröffentlichten deutschen Ausgabe. Voraussetzung ist der ESS12-Vertrag nach Abschnitt 7.

- Aktuelle Referenzen für Profilfragen, die ESS12 wiederholt: laut R3 und R9 `gincdif`, `euftf`, `imsmetn`, `imdfetn`, `impcntr`, `hmsacld`, `vteurmmb`. Sie stehen getrennt neben den historischen Referenzen (Abschnitt 5).
- Wählergruppen nach der Rückerinnerung an die Bundestagswahl vom 23. Februar 2025 (Quellfragebogen A26 und A27). Der Bezug auf diese Wahl folgt aus dem Feldfenster und ist am deutschen Wortlaut noch zu prüfen.
- ESS12 enthält keine Präferenzfrage für die sechs Bereiche (R8 Abschnitt 7, R9 Abschnitt 6.1).

### 11.3 Stufe 3: Online-Quotenstichproben (Klasse Q), nur nach Stevens Grundsatzentscheidung

OECD Risks that Matter 2024: Deutschland November bis Dezember 2024, 18 bis 64 Jahre, Online-Quote, Fragebogen nur englisch. Kandidat ist Q19 mit dem gemeinsamen Stamm „Would you be willing to pay an additional 2% of your income in taxes/social contributions to benefit from better provision of and access to:“ als Mehrfachauswahl, Items in zufälliger Reihenfolge (Rahmung e). Vorgeschlagen sind die Items, die eine Lücke betreffen:

| Item | Gegenstand                                | Bereich                     |
| ---- | ----------------------------------------- | --------------------------- |
| b    | Education services and supports           | Bildung und Forschung       |
| c    | Employment supports                       | Arbeit und Rente            |
| d    | Unemployment supports                     | Arbeit und Rente            |
| e    | Income supports (minimum-income benefits) | Arbeit und Rente            |
| f    | Housing supports                          | Wohnen                      |
| g    | Health services                           | Gesundheit und Pflege       |
| h    | Disability/incapacity-related supports    | Gesundheit und Pflege       |
| i    | Old-age pensions                          | Arbeit und Rente            |
| j    | Long-term care services for older people  | Gesundheit und Pflege       |
| l    | Public transportation                     | Klima und Energie (Verkehr) |

Ausgeschlossen nach 4.1 Nr. 2: a (Familienleistungen, keine dokumentierte Lücke) und k (öffentliche Sicherheit, keine dokumentierte Lücke). Q19 misst eine Zahlungsbereitschaft für bessere Leistungen, keine Haltung zu einem deutschen Gesetz. Ein nicht ausgewähltes Item ist keine Ablehnung (Abschnitt 6). Ausgeschlossen: Q20 (4.2 b, „in order to support the poor“), Q23 a (4.2 b, Begründung mit dem Fachkräftemangel im Stamm), Q27 e (4.2 f), Q27 f (4.2 b), Q34 a (4.2 b und 4.1 Nr. 8) und Q34 j (4.1 Nr. 8, nach Informationsexperiment). Reuters Digital News Report 2025 und 2026 nur, wenn ein deutscher Wortlaut belegt ist.

### 11.4 Stufe 4: GESIS-Bestände, nur nach einer Ausnahme nach § 4

GLES Querschnitt 2025 Nachwahl q27e (Waffenlieferungen an die Ukraine), q27o (Waffen an Israel), q170 (Gesellschaftsdienst statt Wehrpflicht), q27i (Mietregulierung); GLES-Panel 2025/26 (Quotenstichprobe, Klasse Q) zu Verteidigungsausgaben, Wehrpflicht, Russland, Mindestlohn; Politbarometer 2024/25; ISSP 2024 „Digital Societies“; ZMSBw-Daten 2025. GLES q27k („Das Bürgergeld sollte deutlich abgesenkt werden.“) bezieht sich seit dem 1. Juli 2026 auf einen überholten Rechtsstand und wäre nur mit Zeitvermerk denkbar. Diese Fragen sind erst nach einer Ausnahme nach Abschnitt 4 zu prüfen.

### 11.5 Nicht weiter verfolgt

SOEP (KI-Verarbeitung ausdrücklich untersagt), ifo Bildungsbarometer (Vertrag nur für wissenschaftliche Einrichtungen, Daten bis 2021), EIB (Veröffentlichung ohne Erlaubnis untersagt), ZQP (automatisiertes Lesen untersagt), Quellen, die Fragen nur mit Ergebnissen veröffentlichen (ZMSBw-Bericht, Berlin Pulse, Pew, DAK-Pflegereport, ver.di, SozialstaatsRadar), solange Steven sie nicht ausdrücklich zulässt.

## 12 Stopps

- Keine Quelle mit Klasse A. GESIS-Bestände bleiben gesperrt, bis Steven die Ausnahme nach § 4 geklärt hat.
- Fehlt für eine Quelle die Freigabe, bleibt ihr Bereich sichtbar als Lücke.
- Zeigt die technische Prüfung, dass eine Tabelle die Bedingungen aus Abschnitt 6 nicht erfüllt, entfällt die Frage ohne Ersatz aus derselben Quelle nach Ergebnissicht.

## 13 Korrekturen nach der Prüfung von Fassung 0.2

| Finding    | Korrektur in Fassung 0.3                                                                                                                                                                                                                                                      |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P4-V23-F01 | Abschnitt 6: Frageuniversum, Tabellenbasis, Interviewzahl, ungewichtete Fragebasis und Missing-Regel getrennt benannt. Interviewzahl nur als Wellenmerkmal. Standard: keine Zahlen bis zur Klärung; sonst nur nach ausdrücklicher Freigabe mit wörtlich festgelegtem Hinweis. |
| P4-V23-F02 | Abschnitt 6 Nr. 7: Verfahren der doppelten Übertragung mit Blindheit, anderer Methode, Bindung je Zelle, Abgleich, Sperre bei Abweichung, keine Handkorrektur, keine Normierung.                                                                                              |
| P4-V23-F03 | Abschnitte 4.2 bis 4.6: Rahmungsregel, weitere Ausschlusskriterien, Vorrangregel bei mehr als drei Fragen, Status und eingefrorenes Itemregister, Grenzen der technischen Rolle. ST0939 und ST0350 an derselben Regel begründet.                                              |
| P4-V23-F04 | Abschnitt 7: ESS12-Vertrag mit Modustrennung oder begründeter Zusammenfassung, Gewichten, Missing je Modus, Kategorienidentität und Ausfallregel, auch für Einzelreferenzen.                                                                                                  |
| P4-V23-F05 | Abschnitt 8: B als offener Verfahrensentwurf mit Prüfung aller Randangaben; Anteil, Gewichtssumme und Fallzahl unterschieden; C nur mit getrenntem Präzisions- und Offenlegungskonzept.                                                                                       |
| P4-V23-F06 | Abschnitt 8: Beobachtung und Mechanismus getrennt, keine Ursachenaussage aus den Statuszählungen.                                                                                                                                                                             |
| P5-V23-F01 | wie P4-V23-F03; die Rahmungsregel ordnet Anlass, Zweck, wertende Zielformel, Bedingung, zweiseitige Abwägung und einengenden Kontext und begründet ST0350, ST0939, QB12, Q19 und Q27 e.                                                                                       |
| P5-V23-F02 | Abschnitte 4.4 und 11.1: Kennzeichnung nach Wortlaut statt nach Herkunft, Reichweite der Kandidaten nach Geltungsbereich aufgeschlüsselt.                                                                                                                                     |
| P5-V23-F03 | Abschnitt 11.3: alle Items von Q19 nach denselben Regeln geprüft, zehn Items vorgeschlagen, zwei mit Grund ausgeschlossen; Mehrfachauswahl nicht als Ablehnung auszulegen.                                                                                                    |
| P5-V23-F04 | Abschnitt 11.2: erste ESS12-Veröffentlichung voraussichtlich Januar 2027, Deutschland nicht bestätigt; Beginn an die tatsächliche deutsche Ausgabe gebunden.                                                                                                                  |
