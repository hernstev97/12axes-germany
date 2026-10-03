# P4: Methoden und Reproduzierbarkeit des Planentwurfs v2.3

Begrenztes KI-Review durch Codex/OpenAI am 4. Oktober 2026. Paket PLAN-V23-001, Entwurf 0.2. Modus ERSTBEWERTUNG vor Festschreibung.

## Gesamturteil

NICHT_BESTANDEN für die vorliegende Festschreibungsfassung. Sechs mittlere Findings, keine erheblichen Findings. F01–F04 und F06 brauchen Korrekturen vor Festschreibung. F05 betrifft ausschließlich die unbeschlossenen Optionen B/C und blockiert den empfohlenen A-Weg nicht. Keine Auswertungs- oder Veröffentlichungsfreigabe.

Manifest und alle 19 Artefakthashes stimmen vor und nach der fachlichen Prüfung. Ausgangs-HEAD 6e164209ac2872447c2b5353f64ba5c6b6294fb3; nach Prüfung 578adaed884a87fb0a6a1ee4137bf98547861f42 durch parallele Arbeit. Branch unverändert research/life-93-claude-20261003. Der Paketcommit im Manifest ist älter als HEAD; maßgeblich bleiben die geprüften Datei-Bytes. Keine fremde P5-Datei geöffnet.

## Antworten auf die Prüffragen

### 1 Quellenklassen und Anzeige

Z, T und Q trennen die relevanten Datenwege sinnvoll. Tabellenanteile ohne Mikrodaten erlauben keinen eigenen Wählergruppenvergleich. Online-Quotenstichproben tragen ohne zusätzliche Modellannahmen keine designbasierten Bereiche. Die Einordnung muss je Erhebung am tatsächlichen Auswahlverfahren hängen, nicht am Namen Eurobarometer oder am Online-Modus allein.

Der Verzicht auf einen eigenen 95-%-Bereich bei T ist vertretbar. Es fehlen die nötigen Varianz-/Designinformationen; eine allgemeine Beschreibung der Zufallsauswahl ersetzt sie nicht. Ein vorab festgelegter SRS-/Wilson-Bereich oder eine Rechnung mit angenommenem Designeffekt wäre als ausdrücklich hypothetische Modell-/Sensitivitätsrechnung möglich. Sie ermittelt den unbekannten Designeffekt jedoch nicht und sichert keine tatsächliche Abdeckung. Bei unbekannter ungewichteter Fragebasis und gewichteten, gerundeten Tabellenanteilen wäre auch die Eingabe nur näherungsweise. Ein solcher zusätzlicher Bereich ist hier nicht erforderlich und darf nicht als gleichwertiger designbasierter ESS-Bereich erscheinen. Ein fehlender Bereich bedeutet zu Recht keine Unsicherheit von null.

Die Interviewzahl darf als Wellenmetadatum erscheinen. Sie darf ohne weiteren Beleg nicht zur auswertbaren Fragebasis werden. Genau dies bleibt in S1 offen. Gleiches gilt für Item-Missing trotz eigener Weiß-nicht-Zeile. F01 begrenzt diese Aussagen. F02 fordert einen überprüfbaren Ablauf für die zweite unabhängige Übertragung.

### 2 Auswahl und Rollentrennung

Die Auswahlregeln sind vor neuen Ergebnissen geschrieben und überwiegend an Dokumenten prüfbar. Die getrennte Strukturrolle ist sinnvoll: festes Formular ohne Ergebnisse, keine gefilterten Basen, Wertübertragung erst nach Festschreibung. S1 dokumentiert solche Maßnahmen. Tatsächliche technische Isolation habe ich nicht geprüft; das S1-Skript ist nicht manifestgebunden, Originaltabellen sind für diesen Review gesperrt.

Abschnitt 11 enthält konkrete Vorschläge und Ausschlussgründe, aber nicht durchgehend dieselben ausdrücklich genannten Kriterien. ST0939 wird wegen eines Anlasses ausgeschlossen, während ST0350-2 mit kontextsetzender Einleitung bleibt. Auch die Dreierauswahl braucht eine nachvollziehbare Begründung. F03 verlangt begrenzte Kriterien-/Entscheidungskorrekturen und die Bindung von Texten, Wellen und Kategorien vor Übertragung. Tatsächliche ergebnisabhängige Auswahl ist nicht nachgewiesen.

Die Formulierung „niemand im Projekt“ ist nicht als geprüfte Zugriffshistorie bestätigt. R8/R9/R10 und S1 melden ungefragte Ergebnisberührungen. S1 war technische Rolle; das allein widerlegt die Blindheit der Auswahlrolle nicht. Zugriffsaussagen müssen auf konkrete Rollen, Kandidaten und tatsächlich geprüfte Inhalte begrenzt bleiben. Datenzugang, lexikalischer Parserdurchlauf und semantische Einsicht unterscheiden sich.

### 3 Historische Vergleiche und Populationen

BESTANDEN im Textumfang. Abschnitte 3 und 5 verlangen Population, Quelle, Welle, Feldzeit, Stichprobenart und Modus. Quellen und Runden werden weder zusammengelegt noch gemittelt oder verrechnet. Historische und aktuelle Referenzen bleiben gekennzeichnet; Veränderungen, Trends und Signifikanztests sind verboten. Die Profilregeln verbieten einen studienübergreifenden Gesamtwert. Diese Vorgaben verhindern die genannten Fehldeutungen auf Planebene; eine spätere Ansicht muss sie tatsächlich umsetzen.

### 4 Wählergruppen 2025

Zweitstimmenrückerinnerung, Vorrang berichteter Wahlteilnahme, vollständige Codeinventare und Vertrag vor Einsicht sind geeignete Voraussetzungen. Der Original-Quellfragebogen bestätigt A26 als vorgeschaltete Teilnahmefrage und A27 als nationale Parteifrage mit Modusunterschieden. Er belegt keine deutsche Zweitstimmenliste. Der deutsche Wahlbezug bleibt zu Recht bis zum nationalen Fragebogen offen. Erinnerte Wahlteilnahme ist kein überprüftes Wahlregister; die Gruppen beschreiben Befragte nach eigener Angabe, keine Parteiprogramme oder Einstellungen am Wahltag.

F04 betrifft die nicht ausdrücklich gebundene Entscheidung zur Trennung oder Zusammenfassung der ESS12-Modi. Deutsche Codes oder eine empirische Effektgröße müssen jetzt nicht erfunden werden. Vor dem späteren Lauf braucht der eigenständig geprüfte, eingefrorene Vertrag auch diese Analyseentscheidung, Gewichte, Design, Nenner und Ausfallregeln.

Originalfundstelle: [ESS12-Quellfragebogen](https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf), PDF-Seiten 16–17, gedruckte Seiten 15–16, SHA-256 d5f768fa3988bdf5ddc761175de7637905a916f1b94fbd9b3ae00297f6a430aa. Nur diese Originalseiten inhaltlich gelesen.

### 5 Sichtbarkeit und Optionen

Alle vier Statuszählungen stimmen:

| Kategorienzahl | reviewed_historical_reference | withheld_base_or_cell_count | Gruppenpaare insgesamt |
| --- | ---: | ---: | ---: |
| 11, Skala 0 bis 10 | 6 | 37 | 43 |
| 4 | 22 | 23 | 45 |
| 5 | 58 | 81 | 139 |
| 6 | 10 | 53 | 63 |

Das sind Anzahlen öffentlicher Status, keine Fallzahlen von Befragten. Kategorienzahlen stammen ausschließlich aus den Katalogen und enthalten gültige Originalkategorien. Gruppenpaare wurden über Fragekennung verknüpft und auf doppelte Paar-IDs geprüft. Keine Anteile, Bereiche, Zell- oder Befragtenfallzahlen aus Referenzen ausgewertet oder ausgegeben.

F06 begrenzt die Ursachenbehauptung: Der kombinierte Sperrstatus unterscheidet kleine Basis und kleine Zellen nicht. Verfügbarkeit nach Kategorienzahl ist beobachtet; Gruppengröße und Sperrursache sind nicht isoliert geprüft.

A ist als Beibehaltung einer bekannten gleichen Regel vertretbar. Eine Verfügbarkeitszählung macht den unterschiedlichen Umfang sichtbar, beseitigt ihn aber nicht und garantiert keine neutrale Sichtbarkeit. B erkennt die Komplementproblematik. F05 zeigt, warum eine zweite unterdrückte Zelle allein nicht reicht und warum gewichtete Anteile und ungewichtete Fallzahlen getrennt werden müssen. C kann eine begründete Präzisionsregel entwickeln, ersetzt damit aber kein Offenlegungskonzept. B/C bleiben bis zu einem neuen geprüften Plan unbeschlossen.

### 6 Festschreibung und offene Grenzen

Vor Festschreibung F01–F04 und F06 korrigieren und gezielt nachprüfen. Dafür sind keine Rohdaten oder neuen Ergebnistabellen nötig. Konstrukte und politische Eignung gehören zusätzlich zur getrennten Quellen-/Fairnessrolle, deren Urteil mir nicht vorliegt.

Offen bleiben dürfen: ESS12-Veröffentlichungstermin, deutsche Instrumente und Codes, endgültiger ESS12-Vertrag, Rechte-/Quellenfreigaben, fehlende Varianzinformationen bei T, SP557-Strukturprüfung und ausdrücklich zurückgestellte Quellen. Reale Daten-/Tabellenübertragung, Ergebnisprüfung und Exportentscheidung sind spätere gesperrte Schritte. B/C müssen für einen unveränderten A-Weg nicht entwickelt werden.

## Findings

### P4-V23-F01 (mittel)

Status OFFEN. Blockiert die Festschreibung dieses Scopes.

Geprüfte Aussage: Klasse T: Die Interviewzahl gilt als ungewichtete Basis; die Anteile beziehen sich auf alle Befragten einschließlich Weiß nicht.

Problem: Die Zahl aller Interviews und das Frageuniversum belegen weder die ungewichtete auswertbare Basis dieser Frage noch den Umgang mit Verweigerungen und sonstigem Item-Missing. Der Plan leitet aus fehlender Dokumentation eine gesicherte Nennerregel ab. Die vorgesehene Beschriftung der Interviewzahl ist sinnvoll, löst diese zusätzliche Gleichsetzung aber nicht.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:68-72
- reports/claude/agenten/S1-strukturpruefung-eurobarometer.md:12-14,158-163
- reports/claude/agenten/S1-strukturpruefung-eurobarometer.json: eintraege, QB2_1 (SE037), Welle Eurobarometer 105.2, Felder offen und rundung

Auswirkung: Die Anzeige könnte eine unbekannte Fragebasis und einen nicht belegten Missing-Umgang als bekannt darstellen. Aus Interviewzahl und gerundeten gewichteten Anteilen dürfen auch keine Zellfallzahlen abgeleitet werden.

Schweregrad: Belegbarer Fehler der vorgesehenen Metadaten und ihrer Interpretation; noch keine Übertragung oder Veröffentlichung neuer Zahlen.

Korrektur: Interviewzahl nur als Wellenmetadatum führen. Frageuniversum, Tabellenbasis, gewichtete Basis, ungewichtete auswertbare Basis und Missing-Regel getrennt benennen. Den Nenner nur so weit beschreiben, wie dokumentiert: publizierte Kategorien einschließlich Weiß nicht, Umgang mit weiteren fehlenden Antworten und genaue ungewichtete Fragebasis unbekannt. Die Übernahme veröffentlichter Anteile unter dieser Grenze ausdrücklich erlauben oder bis zur Klärung sperren; keine implizite Gleichsetzung.

Nachprüfung: Den korrigierten Abschnitt 6 gegen die bereits gepinnten S1-Felder prüfen. Ein synthetischer Fall mit allen Befragten als Frageuniversum, aber Item-Verweigerungen muss die Unterscheidung erhalten.

Sicherheit: BELEGT

### P4-V23-F02 (mittel)

Status OFFEN. Blockiert die Festschreibung dieses Scopes.

Geprüfte Aussage: Die technische Rolle überträgt die Werte zweimal unabhängig; beide Übertragungen müssen übereinstimmen.

Problem: Unabhängigkeit und die Prüfeinheit sind nicht operationalisiert. Zwei Kopien derselben Extraktion würden den Wortlaut erfüllen, aber einen gemeinsamen Spalten-, Wellen- oder Kategorienfehler nicht erkennen. Nicht festgelegt sind Blindheit gegenüber der ersten Übertragung, Herkunftsbindung, Abgleich der Metadaten, Behandlung von Abweichungen und Rundung sowie das Verbot stiller Reparaturen.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:73-76,109-112
- docs/entscheidungsvorlage-erweiterung-v1.entwurf.md:33
- reports/claude/agenten/S1-strukturpruefung-eurobarometer.md:30-50,158-164

Auswirkung: Die angekündigte Gegenkontrolle ist nicht reproduzierbar. Übereinstimmende falsch zugeordnete Werte könnten den Export erreichen.

Schweregrad: Der zentrale Kontrollschritt des neuen Tabellenwegs bleibt trotz konkreter Ankündigung unbestimmt.

Korrektur: Vor Festschreibung ein Verfahren definieren: zwei getrennte Übertragungen aus denselben gepinnten Originaldateien, zweite ohne Einsicht in die erste; möglichst andere Extraktionsmethode. Je Zelle Quelle und Hash, Welle, Land DE, Frage/Item, Kategorie, Blatt/Seite und Originaldarstellung binden. Vollständigkeit, Basisangaben und Kategorienzuordnung mit abgleichen. Jede Abweichung blockiert die Frage bis zur belegten Auflösung mit erhaltenen Fassungen. Rundung nur nach Quellenformat; keine Normierung auf 100, keine Handkorrektur.

Nachprüfung: Protokoll an synthetischen Tabellen mit DE/DEE-Verwechslung, vertauschten Kategorien, fehlender Weiß-nicht-Zeile und Rundungssumme ungleich 100 prüfen. Reale Tabellenübertragung erst nach den Freigaben.

Sicherheit: BELEGT

### P4-V23-F03 (mittel)

Status OFFEN. Blockiert die Festschreibung dieses Scopes.

Geprüfte Aussage: Abschnitt 11 wendet alle vorab genannten Auswahlregeln auf die Kandidaten an.

Problem: Die Ausschlussentscheidung für ST0939 wird allein mit einem Anlass im Fragetext begründet, obwohl Regel 4 nicht wertende Prämissen und Begründungen mit Kennzeichnung zulässt. Gleichzeitig wird ST0350-2 mit einer solchen Einleitung vorgeschlagen. Weitere Kriterien in den Ausschlüssen, etwa abstrakter Begriff oder zwei Gegenstände, sind in Abschnitt 4 nicht ausdrücklich definiert. Bei mehr als drei Fragen zum engen Gegenstand fehlt ein nachvollziehbarer Prioritätsentscheid. Ich bewerte hier die fehlende Regelbindung, nicht die politische Eignung der beiden Fragen.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:45-56,124-138,150
- reports/claude/agenten/R6-eurobarometer.md:176-191
- reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.md:222-242

Auswirkung: Ein zweiter Bearbeiter kann die Auswahl aus den genannten Regeln nicht vollständig nachvollziehen. Offene Wortlaut- und Zuordnungsfragen schaffen spätere Ermessensschritte bei einer technischen Rolle mit Ergebniszugriff.

Schweregrad: Konkrete Abweichung zwischen Auswahlregel und dokumentiertem Ausschluss; tatsächliche ergebnisabhängige Auswahl ist damit nicht nachgewiesen.

Korrektur: Die Kriterien und begründeten Ausnahmen vor Ergebnissen präzisieren. ST0939 mit einem tatsächlich zutreffenden Kriterium begründen oder als zurückgestellt führen; ST0350-2 am selben Kriterium prüfen. Die gewählte Dreierauswahl inhaltlich begründen, ohne zwangsläufig einen automatischen Rang zu erfinden. Für die Forschungsstufen den Zustand vorgeschlagen/zurückgestellt/ausgeschlossen und offene Bedingungen eindeutig binden. Vor Übertragung ein eingefrorenes Itemregister mit Welle, Frage/Item, vollständigem deutschem Wortlaut, Einleitung, Kategorien, Kontext und Entscheidung vorsehen. Ergebnisexponierte technische Rollen dürfen nur vorab definierte Strukturfehler melden; neue Inhaltsentscheidungen brauchen eine neue blinde Prüfung.

Nachprüfung: Die betroffenen Kandidaten und Grenzen erneut allein aus Kriterien und dokumentierten Fragewortlauten nachvollziehen; keine Verteilungen öffnen. Eindeutige Abbruchregel für fehlenden Wortlaut oder nicht passende Welle prüfen.

Sicherheit: BELEGT

### P4-V23-F04 (mittel)

Status OFFEN. Blockiert die Festschreibung dieses Scopes.

Geprüfte Aussage: ESS12: Prüfung von Wortlaut, Parteiliste und Codes je Modus, danach Gruppenvertrag v2.3; Klasse Z nutzt das Verfahren v2.2.

Problem: Die Prüfung der Code-Konkordanz entscheidet nicht, ob persönlich erhobene und selbst ausgefüllte Antworten getrennte Referenzen bilden oder zusammengefasst werden. Diese Entscheidung samt Gewicht-/Designbindung fehlt als ausdrückliche Voraussetzung des späteren Gruppenvertrags. Der vererbte Vertrag v2.1 enthält historische studienspezifische Regeln, aber keine Entscheidung für das neue ESS12-Modusexperiment.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:33,67,82-85,142-145
- reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md:183-185,315-321
- data/gruppenvertrag.v2.1.entwurf.json:3419-3455,3520-3540
- ESS12-source-questionnaire.pdf, SHA-256 d5f768fa3988bdf5ddc761175de7637905a916f1b94fbd9b3ae00297f6a430aa, PDF-Seiten 16-17: A26/A27, Modusspalten und nationale Spezifikation

Auswirkung: Ein späterer Lauf könnte Codegleichheit als ausreichenden Grund für eine gemeinsame Referenz behandeln. Das verändert Zielgröße, Nenner und Unsicherheitsrechnung und darf nicht nach Verteilungseinsicht entschieden werden.

Schweregrad: Fehlende vorab gebundene Analyseentscheidung für die ausdrücklich bekannte Änderung des Erhebungsmodus; konkrete deutsche Instrumente fehlen noch.

Korrektur: Jetzt in Abschnitt 7/11.2 verbindlich verlangen, dass der spätere versionierte, separat geprüfte und getaggte ESS12-Vertrag vor Einsicht in neue Antworten Modustrennung oder begründete Zusammenfassung festlegt. Dazu Zielpopulation, Design-/Poststratifikationsgewichte, Missing/Filter pro Modus, ausreichende Kategorienidentität und Ausfallregel binden. Das gilt auch für die aktualisierten Einzelreferenzen. Deutsche Codes, tatsächliche Gewichte und konkretes Verfahren dürfen bis zur Dokumentveröffentlichung offen bleiben. Kein Befund zur Effektgröße eines Moduseffekts.

Nachprüfung: Den ergänzten Stopp im Plan prüfen. Später den ESS12-Vertrag vor jeder Antwort-/Parteiinspektion gesondert prüfen; A27 darf ohne belegte nationale Zweitstimmenfrage keinen Ersatz über Parteinähe oder Erststimme bilden.

Sicherheit: BELEGT

### P4-V23-F05 (mittel)

Status OFFEN. Blockiert den aktuellen A-Weg nicht; vor späterer Aktivierung behandeln.

Geprüfte Aussage: Option B braucht eine zweite unterdrückte Zelle oder eine Begründung der Unerheblichkeit; Option C ersetzt die Zellregel durch eine Präzisionsregel.

Problem: Eine zweite unterdrückte Zelle ist keine allgemeine Schutzgarantie. Totale, weitere Veröffentlichungen, Rundung und die Information 1 bis 4 können die verbleibenden Werte weiter eingrenzen oder bestimmen. Außerdem rekonstruiert ein Komplement gewichteter Anteile zunächst einen gewichteten Anteil, nicht zwingend die ungewichtete Fallzahl. Präzision und Offenlegungsschutz sind verschiedene Ziele; eine Intervallbreitenschwelle ersetzt kein Schutzkonzept. Öffentliche Einzeldaten sind keine automatische Begründung für jede zusätzliche Aggregatveröffentlichung.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:91-97
- data/gruppenvertrag.v2.1.entwurf.json:3420-3427,3457-3471
- Synthetische Gegenprobe dieses Reviews: Gesamtzahl 100, sichtbare Zelle 98, zwei unterdrückte positive Zellen jeweils 1 bis 4; einzige zulässige Lösung 1 und 1. Keine ESS-Fälle verwendet.

Auswirkung: Bei späterer Wahl von B oder C könnte eine unzureichende Schutzregel als ausreichend gelten. A ist empfohlen, B/C sind ausdrücklich unbeschlossen; deshalb blockiert dieser Punkt den aktuellen A-Weg nicht.

Schweregrad: Das Risiko betrifft eine konkret beschriebene, aber noch nicht aktivierte Alternative. Kein aktueller Datenabfluss nachgewiesen.

Korrektur: B als offenen Verfahrensentwurf kennzeichnen und eine Prüfung aller veröffentlichten Randinformationen und komplementären Angaben verlangen; sekundäre Unterdrückung kann dazugehören, ist allein nicht hinreichend. Anteil, Gewichtssumme und ungewichtete Fallzahl unterscheiden. C nur nach getrennt begründetem Präzisions- und Offenlegungskonzept erwägen. Vor jeder Umstellung einen eigenen eingefrorenen Plan und Exportprüfungen verlangen. A darf unverändert bleiben.

Nachprüfung: Vor einer Aktivierung B/C mit synthetischen Gegenproben für kleine Restsummen, mehrere Tabellen, Intervalle und Rundung prüfen; bestehende öffentliche ESS-Verteilungen in dieser Nachprüfung weiterhin nicht lesen.

Sicherheit: BELEGT

### P4-V23-F06 (mittel)

Status OFFEN. Blockiert die Festschreibung dieses Scopes.

Geprüfte Aussage: Die Zählungen aus öffentlichen Status zeigen, dass kleine Gruppen und lange Skalen wegen einer einzelnen kleinen Kategorie häufiger ihre Vergleiche verlieren.

Problem: Die vier Zählungen stimmen. Der verwendete Status withheld_base_or_cell_count bündelt aber die zu kleine Gesamtbasis und kleine positive Zellen. Aus Status und Kategorienzahl allein kann weder der konkrete Sperrgrund noch ein Effekt der Gruppengröße isoliert werden. Die Zählungen enthalten zudem verschiedene Fragen/Studien und keine kontrollierte Variation der Skalenlänge.

Fundstellen:

- docs/analyseplan-v2.3.entwurf.md:89
- data/gruppenvertrag.v2.1.entwurf.json:3457-3470
- Erlaubte Projektion von data/reference-v2.2/*.json: je Gruppenpaar ausschließlich Fragekennung, status und Kategorienzahl aus den zwei Katalogen; 4 Kategorien 22/45, 5 Kategorien 58/139, 6 Kategorien 10/63, 11 Kategorien 6/43.

Auswirkung: Eine plausible Folge der Regel würde als empirisch nachgewiesene Ursache der beobachteten Sichtbarkeit dargestellt. Dieser Review kann sie mit dem erlaubten Korpus nicht bestätigen.

Schweregrad: Die Auswertung selbst ist korrekt, ihre kausale Erklärung überschreitet die Information der erlaubten Statusfelder.

Korrektur: Beobachtung und Regelmechanismus trennen: Die Verfügbarkeit unterscheidet sich zwischen diesen Kategorienzahlen; Regel 100/5 kann eine Referenz wegen Gesamtbasis oder einzelner positiver Zellen sperren. Gruppenstärke und Skalenlänge sind plausible Einflussgrößen, aber mit dieser Statuszählung nicht getrennt geprüft. Keine weitere Datenöffnung nötig.

Nachprüfung: Korrigierten Absatz gegen dieselbe reine Status-/Kategorienzählung prüfen. Es dürfen keine gruppenspezifischen Größen oder konkreten Zell-Sperrgründe aus den kombinierten Status abgeleitet werden.

Sicherheit: BELEGT

## Checks

| ID | Status | Für aktuellen Scope erforderlich |
| --- | --- | --- |
| P4-PIN | BESTANDEN | ja |
| P4-Q1 | NICHT_BESTANDEN | ja |
| P4-Q2 | NICHT_BESTANDEN | ja |
| P4-Q3 | BESTANDEN | ja |
| P4-Q4 | NICHT_BESTANDEN | ja |
| P4-Q5-COUNT | BESTANDEN | ja |
| P4-Q5-INTERPRETATION | NICHT_BESTANDEN | ja |
| P4-Q5-BC | NICHT_BESTANDEN | nein |
| P4-Q6 | NICHT_BESTANDEN | ja |
| P4-LATER | IN_DIESER_PHASE_NICHT_ERFORDERLICH | nein |

Ausführliche Belege stehen im JSON-Urteil.

## Grenzen und tatsächlicher Zugriff

- Begrenztes KI-Review des manifestgebundenen Entwurfs 0.2, keine wissenschaftliche Validierung, Neutralitäts-, Produkt- oder Releasefreigabe.
- Keine Dateien unter data/raw/, data/local/ oder outputs/ geöffnet. Keine externen Ergebnistabellen, keine lokalen Verteilungstabellen oder reviewed-* Dateien inhaltlich gelesen.
- Die Ausnahme zu Prüffrage 5 wurde ausschließlich für IDs zur Verknüpfung, status und Kategorienzahl genutzt. JSON-Decoder und Hashfunktion lesen Datei-Bytes einschließlich übriger Felder; diese wurden nicht inhaltlich ausgewertet oder ausgegeben. Schemaerkundung zeigte nur Schlüssel und Typstruktur, keine Feldwerte. Keine absolute OS-Blindheit oder technische Sandbox behauptet.
- Kein Urteil der parallelen Quellen-/Fairnessrolle gelesen. Manifestgebundene Rechercheberichte und historische Plantexte sind Prüfgegenstände, keine unabhängigen Urteile zu diesem Plan. Ein früher Memory-Register-Suchlauf zeigte Paketbezeichnungen/Statuslabels älterer, anderer Prüfungen; keine alten Prüfberichte geöffnet und keine Übernahme ihrer Urteile.
- Originalquellenkontrolle in diesem Lauf beschränkt sich auf ESS12-Quellfragebogen PDF-Seiten 16-17. Eurobarometer-Struktur nur am gepinnten S1-Bericht/Formular geprüft; keine Originaltabellen geöffnet. Tatsächliche Blindheit der Auswahlhistorie und Maskierung des nicht manifestgebundenen S1-Skripts nicht unabhängig geprüft.
- Web-Abruf des ESS12-PDF scheiterte mit 502; derselbe Originalabruf per urllib gelang und bestätigte den bekannten Hash. Die Eurobarometer-About-Seite lieferte im Webwerkzeug keinen lesbaren Text und trägt kein bestandenes Quellenurteil.
- Mehrere Sammelausgaben wurden gekürzt; Hauptplan und relevante Fundstellen danach gezielt gelesen. Gruppenvertrag und Rechercheberichte selektiv gelesen. R5/R7 und R10-JSON ausschließlich gehasht.
- Kein pnpm check und kein Pipeline-/Browserlauf: nur zwei Prüfberichte geschrieben; allgemeine Projektchecks würden den ausdrücklich ausgeschlossenen Lese-/Schreibumfang überschreiten können. Stattdessen JSON-Schema, Urteilslogik, Berichtskonsistenz und Hashbindung gezielt geprüft. Das ist nur formale Prüfung.
- Keine Commits, Pushes, Tags, Nachrichten an Dritte oder Delegation. Kein technischer Schutz oder künftige Gate-Implementierung vorgetäuscht.
- Erster Berichtserstellungsversuch brach vor jeder Schreiboperation ab, weil eine Zusatzassertion den inzwischen durch parallele Arbeit geänderten Ausgangs-HEAD verlangte. Nachprüfung bestätigte alle 19 Artefakthashes. Ein weiterer functions.exec-Aufruf hatte einen JavaScript-Syntaxfehler durch eingebettete Markdown-Codezäune und wurde gar nicht ausgeführt.

## Gelesene und gebundene Eingaben mit Hash

Die 19 Manifestartefakte wurden vor und nach der fachlichen Prüfung gehasht. Hauptplan, Entscheidungsvorlage, Quellenanfragen und Profilregeln vollständig gelesen; Abdeckung und Plan v2.2 als Kontext. Rechercheberichte R8/R9/R10 und Gruppenvertrag selektiv an relevanten Fundstellen. S1 als Strukturbericht mit gezielten Formularfeldern. R5/R7 und R10-JSON nur gehasht. R8-JSON: Schema und Kandidatenkennungen; R9-JSON zusätzlich Kontexte R9-19/20/25/26. Kataloge und Referenzen nur Schema und erlaubte Status-/Kategorienprojektion. Memory-Register nur prozeduraler Kurzblick; keine alten Prüfberichte geöffnet. Hashprüfung ist keine Inhaltsprüfung.

| Eingabe | SHA-256 |
| --- | --- |
| reports/claude/pruefungen/PLAN-V23-001-manifest.json | c2c05725351ff209af158704d0896693fd480be66f4027b22125d97066566c89 |
| docs/analyseplan-v2.3.entwurf.md | f708729867aec9ca187fe7646b21a69d2f4b89e5cdf831d3146051e06018fd94 |
| docs/entscheidungsvorlage-erweiterung-v1.entwurf.md | b40c52f3bfbf0e8f5ed3ca2b7937c8d2d94b3949132273cd360c3aafba5e6de6 |
| docs/abdeckung-v2.2.md | 618012f903783c749b751cb32c8acffab1e7ca09765cd80a26a2a2c1cbeb8b70 |
| docs/quellenanfragen-v1.entwurf.md | 066be958b89b9dc198202c3599001b20d2f61c33d8b846ba8cc3e1405da708ca |
| docs/analyseplan-v2.2.md | 13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8 |
| docs/profilregeln-v1.md | 3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23 |
| reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.md | 6830b4172d606b47fc6f00214fba09d776790143c85c01529b7c33256691c24b |
| reports/claude/agenten/R8-erweiterung-aussen-digital-bildung.json | 23e27dd8c2c1e359fe62ff5df058fef4de749dce95ca1e6da44cec6839e49fa2 |
| reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.md | 42aaa648a36557d33b6bb316aff007f5f79f92779aa4875acdc74516c70ba5c3 |
| reports/claude/agenten/R9-erweiterung-sozial-wohnen-gruppen.json | 71e012d3b460917269153d261a4565f6bfbb34627220ee2cf14d8abf1af272d6 |
| reports/claude/agenten/R10-quellenblocker.md | 65d79b32748197923c9614c7e8e85f19b06f516fa0cff869dbb7d3cf2f228885 |
| reports/claude/agenten/R10-quellenblocker.json | 8e15381892d91f62094c68573bb32148a5df21daf24ad11415549ef94861439a |
| reports/claude/agenten/S1-strukturpruefung-eurobarometer.md | 15b2851d4e383a50ae064b566b1f2d6419180d3899f20007b49c07fe607295c0 |
| reports/claude/agenten/S1-strukturpruefung-eurobarometer.json | f563bc2f138d67a00a9cf8fbfd80580dd3e842108d17231b44efb241edbc9575 |
| reports/claude/agenten/R5-wvs.md | a163be6d448ab5f9e14b54293f355a2e0cea3c19d37e92a4d0021e8af7afc969 |
| reports/claude/agenten/R6-eurobarometer.md | 58b08b2af20d70261e95e7d0d815d4c083d95e0879cef5ee864c6ee05e84e8bb |
| reports/claude/agenten/R7-weitere-quellen.md | 4e795f355ccd359613949a2e307f46150f31506cf817b51f1a4e232405f6fcd5 |
| reports/claude/auftraege/R-erweiterung-gemeinsam.md | 56970a37d162e3996cace441b4f41c44d7e4e3bfd408d008c13e3f9ba0898ccd |
| data/gruppenvertrag.v2.1.entwurf.json | 9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702 |
| reports/claude/auftraege/P4-plan-v23-methoden.md | 8dc91913011c4713d86b1bbada75570307f2d446247f9d2fb5a748510b85bed2 |
| .claude/skills/life93-review/SKILL.md | 90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6 |
| .claude/skills/life93-review/references/urteil-schema.json | 5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9 |
| .agents/skills/unslop/SKILL.md | c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56 |
| docs/project.md | 2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a |
| docs/pruefregeln.md | 29ea917323119b70cf39aae8db9560e435efbcaba4827df4f837be4d2f28d233 |
| /home/stevenh/.codex/memories/MEMORY.md | 76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9 |
| data/politikprofil-v2.fragen.entwurf.json | 5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4 |
| data/politikprofil-v2.2.ergaenzung.json | c4b0d97aeaf10868001199cb3f7f135a6fb8ec28d63b58f7f222ff7e0acd71ac |
| data/reference-v2.2/ESS10SCe03_2.json | 43322d3d8de64b106b7b4336215c30e9575ba58654224cfba860ab97ebfa7a2a |
| data/reference-v2.2/ESS11e04_2.json | a9955368600a474ca40cf71b8d58c0cdf7eccaf6c6f73c7fe724540ab82916da |
| data/reference-v2.2/ESS5e03_6.json | 77012bf09c1994e1414104408d01c8d132c2778c1bc18ce3b4e60ddcf520bc34 |
| data/reference-v2.2/ESS8e02_3.json | 93191d2e37f1bd4ab114c41f25bfcc5ce77d5d2ed83a74a2cfd5a8be103e6ef4 |
| data/reference-v2.2/ESS9e03_3.json | ef93e28ae52592a6d90499017d6c89ab35c78d7205b1573377874774d5dbe9c7 |
| https://www.europeansocialsurvey.org/sites/default/files/2026-01/ESS12-source-questionnaire.pdf | d5f768fa3988bdf5ddc761175de7637905a916f1b94fbd9b3ae00297f6a430aa |

## Ausgeführte Befehle und Werkzeugläufe

Alle Shellbefehle über functions.exec/exec_command; kein Skript als dritte Datei gespeichert.

- cat des P4-Auftrags, unslop-Skills, life93-review-Skills und urteil-schema.json.
- sha256sum des Manifests, cat des Manifests; Python-Hashvergleich sämtlicher artifacts vor Beginn und nach Abschluss, ALL_PINS_OK 19 beziehungsweise ALL_19_ARTIFACTS_STILL_MATCH.
- git status --short, git branch --show-current, git rev-parse HEAD. Ausgangsstatus sauber; später HEAD-Wechsel und fremde untracked P5-JSON nur als Pfad sichtbar.
- rg -n im Memory-Register zu bounded/Prüf/PLAN-V23/frisch/Pins; sed -n 50,54p für prozedurale Grenzen. Keine Rollouts gelesen.
- cat, nl -ba und sed der genannten Pläne/Kontextdateien. Gezielte Bereiche: Plan v2.3 1–86; Prüfregeln 1–160; Abdeckung 1–26; Gruppenvertrag 3368–3544; S1 78–111 und 153–197; R8 1–45 und 214–256; R9 178–207, 285–331 und 421–427; R6 173–206 und 270–290; R10 397–470 und 440–457. Mehrere Sammelausgaben gekürzt, relevante Stellen danach eng erneut gelesen.
- wc -l der manifestgebundenen Rechercheberichte; rg -n für Überschriften und relevante Themen in R8/R9/R10, später nur Überschriften in R9/R6. Keine Inhaltsuche in gesperrten Verzeichnissen.
- rg --files auf data/reference-v2.2 und data, anschließender Pfadfilter auf reference-v2.2/*.json und die beiden Katalogdateien. Nur Dateinamen ausgegeben.
- Inline-Python zur Schemaerkundung von Agenten-JSONs, Referenzen und Katalogen: nur Schlüssel/Struktur, keine Verteilungswerte.
- Zwei Inline-Python-Statuszählungen. Lauf 1 zählte korrekt, scheiterte danach an einer falschen Hilfsassertion, dass jede Einzelreferenz-Kategorienzahl auch Gruppenpaare haben müsse. Skriptfehler dieses Reviews. Lauf 2 entfernte die Annahme, prüfte alle vier Zählungen und bestand mit ALL_GROUP_COUNTS_MATCH.
- Python-Projektion von S1-Feldern zu Filter, Kategorien, Rundung, Zuordnung und offenen Grenzen. Erster Filter mit exaktem Wellentext gab [] zurück; korrigierter Filter nutzte die beschreibenden Wellen-/Erhebungsfelder. Keine Verteilungen ausgegeben.
- Python-Projektion der Kandidatenkennungen aus R8/R9 sowie Kontexte R9-19/20/25/26.
- Synthetische Unterdrückungsprobe: Ganzzahlpaare a,b jeweils 1 bis 4 mit a+b=2; einziges Paar (1,1). Keine ESS-Daten verwendet.
- web.run open des ESS12-PDF: 502 Bad Gateway; open der Eurobarometer-About-Seite: kein lesbarer Text. Ersatzabruf desselben ESS-PDF per urllib.request, SHA-256 und pdftotext -f 16 -l 17 -layout - - per In-Memory-Pipe erfolgreich, keine Download-Datei geschrieben.
- PYTHONDONTWRITEBYTECODE=1 python3, importlib.util.find_spec: jsonschema nicht installiert. Kein Installationsversuch. Beide P4-Ausgabedateien vorher nicht vorhanden.
- Erster Berichtserstellungsversuch brach wegen geändertem HEAD vor jeder Schreiboperation ab. Weiterer functions.exec-Aufruf scheiterte bereits beim JavaScript-Parsing wegen eingebetteter Markdown-Codezäune. Anschließend ausschließlich die zwei autorisierten Dateien geschrieben.
- Abschließend Inline-Python gegen das vollständige urteil-schema.json, zusätzliche Urteils-/Finding-Konsistenzprüfung, Berichtskonsistenz, Hashvergleich aller lokalen Eingaben und git status --short. Nur formale Prüfung; kein pnpm-, Pipeline- oder Browserlauf.

### Reproduktion der erlaubten Statuszählung

```python
import json
from pathlib import Path
from collections import Counter, defaultdict
cats = {}
for name in ['data/politikprofil-v2.fragen.entwurf.json',
             'data/politikprofil-v2.2.ergaenzung.json']:
    for q in json.loads(Path(name).read_bytes())['items']:
        assert q['id'] not in cats
        cats[q['id']] = len(q['categories'])
groups = defaultdict(Counter)
seen = set()
for path in sorted(Path('data/reference-v2.2').glob('*.json')):
    data = json.loads(path.read_bytes())
    for group in data['groups']:
        for pair in group['pairs']:
            key = (group['groupId'], pair['questionId'])
            assert key not in seen
            seen.add(key)
            groups[cats[pair['questionId']]][pair['status']] += 1
expected = {11: (6, 43), 4: (22, 45), 5: (58, 139), 6: (10, 63)}
for size, (available, total) in sorted(expected.items()):
    assert groups[size]['reviewed_historical_reference'] == available
    assert sum(groups[size].values()) == total
    print(size, dict(groups[size]), total)
assert set(groups) == set(expected)
```

Der tatsächliche zweite Lauf zählte zusätzlich Einzelreferenzstatus nach Kategorienzahl, ohne die reference-Felder zu nutzen. Nicht jede Einzelreferenz-Kategorienzahl besitzt Gruppenpaare; diese Hilfsausgabe trägt keine inhaltliche Planentscheidung.

## Modell laut Laufzeit

OpenAI, Codex-Harness in T3 Code, gpt-6.1-sol, high reasoning effort laut Laufzeitmetadaten. Konkrete interne Anbieterrevision unbekannt. Keine Claude-Ausführung oder zusätzliche Prüferdelegation. Originalprompt und vollständiger Auftragsinhalt stehen in execution.prompt des JSON-Urteils.
