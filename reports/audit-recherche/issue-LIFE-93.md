# LIFE-93: Politiktest für Deutschland wissenschaftlich fundieren und transparent umsetzen

API-Stand `updatedAt 2026-10-02T22:07:24.510Z`. Live gelesen am 2026-10-03. URL: https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent

## Ziel

Ein eigenständiger deutschsprachiger Politiktest mit vollständigem Fokus auf Deutschland: ein verständlicher Frageablauf, ein anschauliches mehrdimensionales Einstellungsprofil, ausführliche Erklärungen und Vergleiche mit der Bevölkerung und realen Wählergruppen in Deutschland. Das Erlebnis eines erklärenden Politikprofils ist der Produktkern. Fragen und Daten stammen aus dem [European Social Survey](<https://www.europeansocialsurvey.org/>) (ESS), einer repräsentativen wissenschaftlichen Befragung. Auswahl der Fragen, Dimensionen, Auswertung und Interpretation sind ein eigenes Modell dieses Projekts und werden überall als solches ausgewiesen. Die Agents bauen und rechnen. Sie erfinden keine Fragen, schätzen keine Parteipositionen und vergeben keine Ideologie-Labels.

Der Test beschreibt Einstellungen. Er sagt nicht, welche Haltung richtig ist, und gibt keine Wahlempfehlung.

Umfang der ersten Version (Entscheidung Steven): Einstellungsprofil zu den Themen, die der ESS abfragt, mit Erklärungen und Vergleich zur Bevölkerung und zu realen Wählergruppen zum Zeitpunkt der Befragung. Ideologie-, Länder- und Personen-Matches gehören nicht zur ersten Version. Anzahl und Struktur der Dimensionen ergeben sich aus Theorie und Daten; zwölf Dimensionen sind keine Vorgabe. Das Profil ist keine umfassende politische Landkarte. Die Website nennt ausdrücklich, welche Themen fehlen oder nur teilweise abgedeckt sind.

Rollen: Codex ist der leitende Agent und übernimmt innerhalb des beauftragten Umfangs Recherche, Analyse, Dokumentation, Umsetzung und Koordination. Claude prüft als andere Modellfamilie: getrennte Erstbewertungen für die festgelegten Urteilsaufgaben und anschließend Reviews über eine GitHub Action. Ein PR-Review ersetzt keine getrennte Erstbewertung. Steven übernimmt die unten markierten Zugänge, organisatorischen Aufgaben, Stopp-Entscheidungen und Freigaben; politisches oder statistisches Fachwissen wird von ihm nicht vorausgesetzt.

## Todos für Steven

Insgesamt etwa 4–6 Stunden, verteilt über die Projektlaufzeit. Kein Schritt braucht politisches Fachwissen.

**Vor dem Start**

- [X] Öffentliches GitHub-Repo anlegen (5 min)
- [X] Codex CLI und GitHub CLI lokal installieren, `gh auth login` ausführen (10–15 min). Codex läuft lokal, weil die Rohdaten nicht ins Repo dürfen.
- [ ] ESS-Konto anlegen und Nutzungsbedingungen akzeptieren (5 min)
- [ ] Claude-Review einrichten (15–30 min): Claude Code installieren, im Repo `claude` starten, `/install-github-app` ausführen, als Anmeldung das Claude-Abo wählen, den Setup-PR mergen
- [ ] Codex mit dem Setup beauftragen, z. B. „Arbeite den Abschnitt Setup aus <issue id="853a10c7-1bfd-457f-b523-2a5bc7d3a6d6" href="https://linear.app/kiumu-app/issue/LIFE-93/politiktest-fur-deutschland-wissenschaftlich-fundieren-und-transparent">LIFE-93</issue> ab“
- [ ] Wenn Codex das Setup meldet: in den Repo-Einstellungen „Allow auto-merge“ aktivieren und für `main` Branch-Schutz setzen: PR Pflicht, Checks „CI“ und „Claude-Review“ Pflicht, kein Force-Push (10 min)

**Phase 0**

- [ ] Die von Codex gemeldeten ESS-Dateien herunterladen und in `data/raw/` legen (10–15 min)

**Laufend**

- [ ] Codex Phase für Phase beauftragen (insgesamt 1–2 h über zwei Tage)
- [ ] Stopp-Meldungen beantworten (voraussichtlich 0–3, je 5–15 min)

**Phase 6**

- [ ] Hosting verbinden, Vercel oder GitHub Pages (10–15 min)

**Deployment**

- [ ] Website durchklicken, Grenzen-Seite lesen, Freigabe geben (30–45 min)

**Nach dem Deployment (Phase 9, Pflicht)**

- [ ] Verständnistest: den von Codex vorbereiteten Text mit Link und Fragen an 5 Personen mit möglichst unterschiedlicher politischer Haltung schicken. Die Antworten ohne Namen in eine Datei kopieren und Codex übergeben (ca. 1 h, Wartezeit nicht eingerechnet)
- [ ] Überarbeitete Version durchklicken und freigeben (15 min)

## Grundsätze

**Nichts erfinden.** Jede Frage, jeder Vergleichswert und jede Wählergruppe lässt sich auf eine Variable im ESS und ein Skript im Repo zurückführen.

**Regeln vor Ergebnissen.** Auswahl- und Prüfregeln stehen vor der jeweiligen Untersuchung fest. Das aus Teil A entwickelte Modell wird vor Zugriff auf Teil B eingefroren. Alle Regeln für Partei- und Lagervergleiche sowie die Benennung stehen vor der Entblindung fest. Öffentliche Tags, zugehörige Commit-IDs und protokollierte Datenzugriffe machen diese Reihenfolge nachvollziehbar. Die Tag-Reihenfolge allein beweist weder tatsächliche Blindheit noch Biasfreiheit. Jede Abweichung vom vorgesehenen Ablauf wird mit ihren Folgen offengelegt.

**Gleiche Prüfmaßstäbe, keine ausbalancierten Ergebnisse.** Alle Richtungen werden nach denselben Regeln behandelt. Wenn die Daten Unterschiede zeigen, stellt der Test sie so dar, wie sie sind. Ergebnisse werden nicht künstlich angeglichen.

**Alles öffentlich, was öffentlich sein darf.** Code, Analyseplan, Entscheidungsprotokoll, Reviews, Agent-Aufträge, Modellversionen und aggregierte Ergebnisse liegen von Anfang an in einem öffentlichen Repo. Nicht öffentlich sind nur die ESS-Rohdaten (Lizenz). Antworten von Nutzern werden gar nicht erst gespeichert. Die Git-Historie wird nie umgeschrieben, verworfene Ansätze bleiben sichtbar.

**Vorwürfe überprüfbar machen.** Biasfreiheit lässt sich nicht garantieren. Jeder Vorwurf muss sich aber an veröffentlichten Regeln, Daten und Skripten prüfen lassen.

**Ehrlicher Status.** Das Projekt ist ein Forschungsprototyp auf Basis einer Sekundäranalyse, erstellt mit KI, ohne Begutachtung durch Fachleute. Es bezeichnet sich nicht als validiert, garantiert neutral oder wissenschaftlich geprüft.

12 Axes war Anregung für das Format (mehrdimensionales Ergebnis mit Erklärung). Code, Fragen, Texte und Daten von 12 Axes werden nicht übernommen ([Lizenz](<https://github.com/RomanCypherpunk/12axes/blob/main/LICENSE>)).

## Belegpflicht und Interpretationsgrenzen

* Jede tragende wissenschaftliche Aussage, Dimension und Ergebnisinterpretation erhält eine stabile ID in `docs/belegregister.md`. Der Eintrag verbindet die genaue Aussage mit Quelle und Fundstelle bzw. ESS-Variablen, Analyseskript, generiertem Bericht und Modellversion. Geltungsbereich, Einschränkungen, Gegenbelege und Prüfstatus gehören dazu.
* Quellenbefund, empirisches Analyseergebnis, eigene Modellentscheidung, Interpretation und offene Annahme werden unterschieden. Eine plausible KI-Erklärung oder die Übereinstimmung zweier Modelle ersetzt keine Evidenz.
* Jede Dimension benennt das tatsächlich erfasste Konstrukt, die abgedeckten Teilaspekte und ausdrücklich nicht gestützte Interpretationen. Wenige Fragen zu einem engen Thema dürfen ohne zusätzliche Evidenz keine umfassende politische Orientierung begründen. Reliabilität und Modellgüte allein tragen keine beliebige Interpretation.
* Die Belegpflicht gilt auch für Ergebnisüberschriften, Polbeschreibungen und erklärende Texte. Die Website darf aus dem Profil keine Motive, Charaktereigenschaften, politische Identität oder nicht gemessenen Haltungen ableiten.
* Der zweite Agent prüft die tragenden Quellen an der Originalfundstelle und die Verbindung zwischen Befund und Aussage. Fehlende oder nicht prüfbare Evidenz bleibt offen und begrenzt die zulässige Aussage.

## Autonomie und Phasenabnahmen

* Innerhalb des ausdrücklich beauftragten Umfangs arbeitet Codex selbstständig bis zur nächsten erfüllten Abnahme oder einer Stopp-Bedingung. Empfehlungen und Issue-Änderungen erweitern den Ausführungsauftrag nicht automatisch.
* Jede Phase liefert einen versionierten Abnahmebericht in `reports/phasen/`: Artefakte und Commit-IDs, tatsächlich ausgeführte Prüfungen mit Ergebnissen, offene Findings, Evidenzlücken, Abweichungen vom Plan und eine begründete Entscheidung über den nächsten Schritt.
* Technische Funktion, methodische Belege und Verständlichkeit werden getrennt beurteilt. Ein grüner Build, ein bestandener Rechentest oder ein KI-Review ersetzt keinen fehlenden methodischen Nachweis.
* Pflichtprüfungen dürfen bei fehlenden Daten, Werkzeugen oder Review-Zugängen nicht als bestanden behandelt werden. Die betroffene Abnahme bleibt offen; blockierte Arbeit wird nach den Stopp-Bedingungen gemeldet.
* Bei unzureichender Evidenz gelten die vorab festgelegten Folgen: engerer Geltungsbereich, sichtbare Unsicherheit oder Ausschluss. Erhebliche offene Probleme blockieren den nächsten davon abhängigen Schritt. Steven erhält eine konkrete Stopp-Meldung mit Problem, Belegen, Folgen und prüfbaren Optionen.

## Setup (vor Phase 0)

* Repo-Grundstruktur nach „Repo und Protokolle“ anlegen, `data/raw/` in `.gitignore` eintragen, `docs/ki-protokoll.md` beginnen.
* CI-Workflow mit Tests und allen Prüfungen, die ohne Rohdaten laufen. Der Check heißt fest „CI“.
* Review-Workflow aus Stevens Claude-Setup anpassen. Methodik, Belegpflicht, Interpretationsgrenzen und Neutralitätsprüfungen dieses Issues gehören ausdrücklich zum Review-Auftrag; ein reines Code-Review genügt nicht.
* Review-Skill: eigener Skill in `.claude/skills/` mit den Regeln aus Phase 7 und den Neutralitätsprüfungen. Er endet mit einem maschinenlesbaren Urteil, also Findings mit Schweregrad.
* Review-Check: Der Workflow schlägt fehl, solange ein erhebliches Finding, eine erforderliche Erstbewertung oder eine für den PR erforderliche Abnahme offen ist. Ein ausgefallenes oder übersprungenes Review gilt nicht als Erfolg. Der Check heißt fest „Claude-Review“.
* Review-Auslöser: bei jedem neuen Push auf einen PR, nicht nur beim ersten.
* Review-Modell: fest per `--model` gesetzt. Modell und Version landen im KI-Protokoll.
* Getrennte Erstbewertungen zusätzlich zum PR-Review einrichten: Codex und Claude bekommen dieselbe versionierte Prüfgrundlage und dieselben Kriterien in getrennten Sitzungen, ohne Zugriff auf die Urteile oder vorgeschlagenen Namen des anderen. Für Textprüfungen dürfen beide dieselbe zu prüfende Textfassung sehen, aber keine Bewertung des anderen. Aufträge, freigegebene Eingaben, Modelle, Zeitpunkte und Prüfsummen der abgeschlossenen Urteile werden protokolliert. Erst nach Abschluss beider Läufe werden Urteile und Abweichungen zusammengeführt und veröffentlicht.
* Review und Abnahmeberichte beziehen sich auf den aktuellen PR-Stand. Nach ergebniswirksamen Änderungen müssen die betroffenen Prüfungen erneut laufen; alte grüne Checks dürfen die geänderte Fassung nicht freigeben.
* Öffnet ein Bot die PRs, wird er in `allowed_bots` eingetragen.
* Codex merged per `gh pr merge --auto`. GitHub führt den Merge erst aus, wenn alle Pflicht-Checks grün sind.
* Setup per Kommentar in diesem Issue als erledigt melden, damit Steven Auto-Merge und Branch-Schutz aktivieren kann.

**Todo Steven:** Repo anlegen, lokale Tools installieren, Claude-Review einrichten, nach der Meldung Auto-Merge und Branch-Schutz aktivieren.

**Abnahme:** Nach Stevens Branch-Schutz wird ein Test-PR mit absichtlich eingebautem Verstoß (z. B. eine von Hand geschriebene Zahl in einem Text) vom Claude-Review blockiert. Ein sauberer Test-PR läuft durch und wird automatisch gemerged.

## Phase 0: Lizenzen, Datenlage, Analyseplan

* ESS-Nutzungsbedingungen prüfen für (a) Auswertung für eine öffentliche, nicht-kommerzielle Website, (b) Veröffentlichung aggregierter Ergebnisse, (c) Anzeige der deutschen Fragewortlaute auf der Website. Ergebnis mit wörtlichen Zitaten und Links in `docs/lizenzen.md`.
* Neueste ESS-Runde mit deutschen Daten bestimmen. Dokumentieren: Feldzeit, Fallzahl, Befragungsmodus und auf welche Bundestagswahl sich die Wahlfrage bezieht.
* Benötigte ESS-Dateien (Runden, Formate) per Kommentar in diesem Issue melden. Die Datenanalyse beginnt erst, wenn sie in `data/raw/` liegen. Ihre SHA-256-Prüfsummen kommen ins Repo.
* Analyseplan in `docs/analyseplan.md`: Auswahlkriterien für Fragen, Aufteilung und Schutz der Datenhälften, Methoden, Schwellenwerte, Umgang mit fehlenden Werten, Gewichtung und Berücksichtigung des Stichprobendesigns nach offizieller ESS-Anleitung, Mindestfallzahl und ausreichende Präzision für Wählergruppen und Gruppenprüfungen, Abstandsmaß, Benennungsregeln, Reihenfolge der Fragen und alle Prüfungen. Für jede Prüfung werden Eingaben, Entscheidungsregel und Folgen bei Nichtbestehen oder fehlender Prüfbarkeit vorab festgelegt. Dazu gehören Itemdominanz, Instabilität, Interpretationsgrenzen und die getrennte Berechnung der Unsicherheitsarten. Methodische Entscheidungen werden mit Fundstellen begründet; pauschale Konventionen allein genügen nicht.
* Der Analyseplan wird als Git-Tag `analyseplan-v1` veröffentlicht, bevor ein Analyse-Commit entsteht.

**Todo Steven:** Die gemeldeten ESS-Dateien herunterladen und in `data/raw/` legen.

**Abnahme:** Lizenzdokument mit zitierten Fundstellen. Tag `analyseplan-v1` liegt zeitlich vor allen Analyse-Commits.

## Phase 1: Frageninventar und Erwartungsmodell

* Alle Einstellungsfragen der gewählten Runde erfassen: Variable, deutscher Wortlaut aus dem offiziellen deutschen Fragebogen, Antwortskala, Codes für fehlende Werte, Fundstelle.
* Aufnahme: Einstellung zu einer politischen oder gesellschaftlichen Streitfrage oder zu einem Wert. Ausgeschlossen: Wissensfragen, eigenes Verhalten, Bewertungen der amtierenden Regierung, Fragen mit Parteibezug. Links-Rechts-Selbsteinstufung und Wahlfrage bleiben als Prüfvariablen außen vor.
* Deutschlandbezogene Themenabdeckung in `docs/themenabdeckung.md` dokumentieren: anhand benannter fachlicher Quellen relevante politische Themen erfassen und mit den verfügbaren ESS-Fragen sowie dem ausgewählten Frageninventar abgleichen. Je Thema: abgedeckt, teilweise abgedeckt oder nicht abgedeckt, zugehörige Fragen, Fundstellen und Begrenzung. Unterscheiden, ob ein Thema im ESS fehlt oder durch die eigene Auswahl eingeschränkt wird. Diese Übersicht begrenzt das Erwartungsmodell und erscheint verständlich auf der Website; Lücken werden nicht durch erfundene Fragen geschlossen.
* Doppelte Einstufung nach dem getrennten Verfahren aus Setup: Codex und Claude prüfen jede Frage gegen die Aufnahmekriterien und bestimmen ihre Polung, ohne das Urteil des anderen zu kennen. Die ursprünglichen Urteile bleiben unverändert erhalten. Übereinstimmung (Cohens Kappa) und Abweichungen werden veröffentlicht. Kappa beschreibt die Übereinstimmung dieses Verfahrens, nicht die Richtigkeit oder Neutralität der Auswahl. Wie bei Abweichungen entschieden wird, legt der Analyseplan vorab fest; jede Entscheidung wird begründet.
* Erwartungsmodell in `docs/erwartungsmodell.md`: Welche etablierten politikwissenschaftlichen Ansätze zu Einstellungsdimensionen in Deutschland und Westeuropa gibt es, einschließlich konkurrierender (z. B. eine Links-Rechts-Achse, getrennte wirtschaftliche und gesellschaftliche Achse, themenspezifische Dimensionen)? Welchem Konstrukt würde jeder Ansatz welche Frage zuordnen? Jede Quelle mit DOI oder Link und geprüfter Fundstelle. Kein Ansatz wird vorab bevorzugt.
* Das Erwartungsmodell wird als `erwartungsmodell-v1` getaggt, bevor Daten ausgewertet werden.

**Abnahme:** `data/inventar.csv` und belegte Themenübersicht. Jeder Wortlaut wird automatisch mit dem Fragebogen-PDF abgeglichen. Jeder Ausschluss ist einzeln begründet. Ursprüngliche getrennte Ersturteile, Übereinstimmungsbericht und dokumentierte Entscheidungen zu Abweichungen liegen vor.

## Phase 2: Messmodell (blind)

* Der Analysedatensatz enthält keine Wahl- oder Parteivariablen und keine Links-Rechts-Selbsteinstufung.
* Zufällige Aufteilung mit veröffentlichtem Seed in Teil A (explorativ) und Teil B (bestätigend). Teil B bleibt für explorative Entwicklung gesperrt. Zugriff, Zeitpunkt und Modellstand werden protokolliert; Auswertung erfolgt erst nach dem veröffentlichten Tag `modell-v1`.
* Teil A: explorative Faktorenanalyse mit Verfahren für ordinale Daten. Das Ergebnis wird mit dem Erwartungsmodell abgeglichen, jede Abweichung wird begründet.
* Dimensionen, die statistisch auftauchen, sich aber inhaltlich nicht schlüssig deuten lassen, werden nach den vorab festgelegten Regeln enger beschrieben, als unsicher markiert oder ausgeschlossen. Für jede vorgeschlagene Dimension werden Konstrukt, tatsächlich abgedeckte Teilaspekte, Belege und Interpretationsgrenzen im Belegregister festgehalten.
* Modell als `modell-v1` taggen, bevor Teil B ausgewertet wird.
* Teil B: konfirmatorische Faktorenanalyse des eingefrorenen explorativen Modells und der zuvor festgelegten konkurrierenden Ansätze aus dem Erwartungsmodell, Vergleich der Modellgüte, Reliabilität je Dimension. Folgen bei Nichtbestehen richten sich nach dem Analyseplan. Änderungen anhand von Teil B werden als erneute explorative Entwicklung ausgewiesen; Teil B gilt danach nicht als unabhängige Bestätigung dieser Änderungen.
* Benennung: Namen und Pole beschreiben fachlich zutreffend den Inhalt der Fragen, z. B. „mehr Zuwanderung befürworten – weniger Zuwanderung befürworten“. Angestrebt werden sachliche Bezeichnungen, die Menschen mit der jeweiligen Haltung als zutreffend erkennen können. Tatsächliche Akzeptanz darf aus einer KI-Simulation nicht behauptet werden; Bezeichnungen dürfen den Inhalt weder beschönigen noch abwerten. Codex und Claude schlagen Namen nach dem getrennten Verfahren aus Setup vor. Die Auswahl wird mit Belegen und Interpretationsgrenzen begründet und vor der Entblindung abgeschlossen.

**Abnahme:** Tag-Reihenfolge `analyseplan-v1` → `erwartungsmodell-v1` → `modell-v1` → Auswertung von Teil B. Alle Kennwerte stammen aus Skripten.

## Phase 3: Auswertung

* Skalenangleichung: Jede Antwort wird vor der Mittelung auf 0–1 umgerechnet ((Wert − Minimum) / (Maximum − Minimum), bei Bedarf umgepolt). So hat jede Frage denselben Wertebereich, unabhängig von der Länge ihrer Skala.
* Rohscore je Dimension: Mittelwert der umgerechneten Antworten mit gleichen Gewichten, Wertebereich 0–1.
* Ergebnis: Perzentil des Rohscores in der gewichteten Verteilung der ESS-Befragten in Deutschland.
* z-Standardisierung und Faktorwerte laufen als Varianten in den Sensitivitätsanalysen (Phase 4).
* Mindestzahl beantworteter Fragen je Dimension. Darunter wird die Dimension nicht angezeigt. Dieselbe Regel gilt für die ESS-Befragten.
* Unsicherheit getrennt behandeln: (a) Messunsicherheit des persönlichen Dimensionsscores, (b) Stichprobenunsicherheit der Bevölkerungs- und Wählergruppenvergleiche, (c) Unterschiede zwischen vertretbaren Modellentscheidungen aus den Sensitivitätsanalysen. Methoden, Voraussetzungen, Konfidenzniveau soweit anwendbar und Darstellungsregeln stehen vorab im Analyseplan. Für (b) werden Gewichte und Stichprobendesign berücksichtigt. Ein Modellvariantenbereich ist kein Messfehler- oder Konfidenzintervall. Für das persönliche Ergebnis wird ein methodisch begründeter Messunsicherheitsbereich angestrebt; fehlt dafür tragfähige Evidenz, wird kein scheinpräziser Bereich erzeugt. Geltungsbereich und Darstellung werden nach dem Analyseplan begrenzt, die fehlende Evidenz bleibt sichtbar und die betreffende Abnahme ist bis zu einer begründeten Entscheidung offen.
* Export als versioniertes `model/v1.json` (Fragen, Polung, Normtabellen, Unsicherheitsangaben, Interpretationsgrenzen, Beleg-IDs, Prüfsumme). Die Website nutzt ausschließlich diese Datei.

**Abnahme:** Tests für Spiegelsymmetrie der Rohscores (umgekehrte Antworten ergeben 1 − Rohscore), Monotonie der Perzentile (ein höherer Rohscore ergibt nie ein niedrigeres Perzentil), Determinismus und Parität zwischen Python-Pipeline und Website-Code auf synthetischen Antworten. Perzentile müssen nicht spiegelsymmetrisch sein, weil die Bevölkerung nicht symmetrisch verteilt ist.

## Phase 4: Entblindung und Prüfungen

* Erst jetzt kommen Wahlfrage und Links-Rechts-Selbsteinstufung dazu.
* Messinvarianz über Ost/West, Geschlecht, Altersgruppen, Bildung und politische Lager (Terzile der Links-Rechts-Selbsteinstufung). Fragen, die zwischen Lagern unterschiedlich funktionieren, werden gemeldet und nach den Regeln des Analyseplans behandelt.
* Gruppenprüfungen berichten die tatsächlich verfügbaren Fallzahlen, Präzision und Prüfbarkeit. Zu kleine Gruppen oder gescheiterte Modellschätzungen belegen keine Messinvarianz; die Prüfung bleibt offen und begrenzt die betroffene Aussage nach dem Analyseplan.
* Konsistenzlauf: alle deutschen ESS-Befragten durch den Website-Code. Prüft, dass Website und Pipeline identisch rechnen, und berichtet die Verteilungen je Dimension und je Wählergruppe. Das ist eine technische Prüfung und kein Neutralitätsnachweis, weil die Normwerte aus denselben Daten stammen.
* Sensitivitätsanalysen: z-Standardisierung und Faktorwerte statt 0–1-Umrechnung, anderer Umgang mit fehlenden Werten, ohne Gewichtung, andere ESS-Runden soweit vergleichbar. Zusätzlich Itemdominanz prüfen: Fragen einzeln weglassen und untersuchen, ob einzelne Fragen die Dimension, Interpretation oder Vergleichsreihenfolge unverhältnismäßig bestimmen. Bericht, wie stark sich Scores, Perzentile und Reihenfolgen verschieben. Der Analyseplan legt vorab fest, welche Instabilität einen engeren Geltungsbereich, sichtbare Unsicherheit, den Verzicht auf Ranglisten oder den Ausschluss verlangt.
* Jede Änderung nach der Entblindung wird eine neue Modellversion mit Begründung. Die alte Version bleibt öffentlich.

**Abnahme:** Berichte in `reports/`, vollständig aus Skripten erzeugt.

## Phase 5: Vergleich mit Wählergruppen

* Nur Parteien, deren Wählerschaft in der Stichprobe die Mindestfallzahl aus dem Analyseplan erreicht (Vorschlag: 50 ungewichtete Befragte). Alle anderen erscheinen gesammelt als „andere Parteien“.
* Je Dimension: gewichteter Mittelwert mit 95-%-Intervall und Verteilung jeder Wählergruppe. Gleiche Darstellung für alle Gruppen, alphabetische Reihenfolge.
* Kein Gesamtwert „Übereinstimmung in %“. Eine Liste der nächstgelegenen Gruppen gibt es nur, wenn ihre Reihenfolge in den Sensitivitätsanalysen stabil bleibt.
* Interpretationsgrenze: Der Vergleich beschreibt die gemessenen Einstellungen von Befragten mit berichteter Wahlentscheidung. Er wird nicht als Position der Partei, ihres Programms, ihrer Führung oder aller heutigen Menschen mit dieser Wahlpräferenz ausgegeben. Nähe zu einem Gruppenmittel begründet keine Parteizugehörigkeit und keine Wahlempfehlung. Grenzen und Belege des Vergleichs werden im Belegregister geführt.
* Bezeichnung mit Zeitbezug, z. B. „Befragte, die bei der Bundestagswahl 2021 Partei X gewählt haben (befragt 2023)“. Hinweis, dass berichtetes und tatsächliches Wahlverhalten abweichen können.

## Phase 6: Website

* Statische Seite. Die Auswertung läuft im Browser, Antworten verlassen das Gerät nicht. Kein Tracking, keine Cookies, keine externen Schriften oder CDNs.
* Fragen und Antwortskalen exakt wie im deutschen ESS-Fragebogen.
* Seiten: Test, Ergebnis, Methodik (kurz und ausführlich), Grenzen, Daten und Lizenzen, Versionen, Fehler melden.
* Ergebnisdarstellung: zuerst inhaltlich erklären, welche gemessenen Einstellungen eine Dimension beschreibt; anschließend den Bezug zur historischen Bevölkerungsverteilung und zu Wählergruppen erklären. Ein Perzentil wird nicht als Zustimmungsanteil, Intensität einer Ideologie oder politische Identität dargestellt. Jeder Unsicherheitsbereich bekommt eine Erklärung seiner konkreten Bedeutung und Grenzen.
* Erklärungen und Polbeschreibungen sind versionierte, geprüfte Texte mit Beleg-IDs. Der Ergebnistext bleibt innerhalb der freigegebenen Interpretationen; während des Tests werden keine neuen KI-Deutungen der Person erzeugt.
* Beispielergebnis-Seite mit einem fiktiven Antwortprofil nach fester Regel: auf jeder Dimension abwechselnd ein Wert am 25. und am 75. Perzentil, Reihenfolge per Zufall mit veröffentlichtem Seed. Sie dient zur Erklärung und für den Verständnistest in Phase 9.
* Die Grenzen-Seite nennt mindestens: Zeitabstand der Daten, anderer Befragungsmodus als im ESS, nicht abgedeckte Themen, berichtetes statt tatsächliches Wahlverhalten, fehlende Fachbegutachtung, KI-Beteiligung, Dimensionen und Auswertung als eigenes Modell des Projekts, Stand des Verständnistests aus Phase 9.
* Jedes Ergebniselement verlinkt auf Fragen-IDs, Modellversion und den zugehörigen Bericht. Fehlerberichte laufen über eine GitHub-Issue-Vorlage mit Bezug auf Frage, Dimension oder Berechnung.
* Gestaltung anschaulich, sachlich und an wissenschaftlichen Publikationen orientiert, barrierearm (WCAG 2.2 AA), mobil lesbar. Verständlicher Frageablauf, übersichtliche Dimensionen und zugängliche Erklärungen orientieren sich am Erlebnis der Inspiration und erhalten eine eigenständige Gestaltung. Die Darstellung darf Aussagekraft und Projektstatus nicht überzeichnen.
* Statushinweis auf jeder Ergebnisseite: „Forschungsprototyp. Fragen und Vergleichsdaten stammen aus dem European Social Survey, Dimensionen und Auswertung sind ein eigenes Modell dieses Projekts. Analyse und Website wurden mit KI erstellt und nicht von Fachleuten begutachtet. Code und Auswertung sind öffentlich.“
* Bis Phase 9 abgeschlossen ist, ergänzt der Statushinweis: „Texte und Ergebnisdarstellung wurden noch nicht mit Menschen auf Verständlichkeit getestet.“ Danach verlinkt er auf die Auswertung des Tests.

**Todo Steven:** Hosting verbinden (Vercel oder GitHub Pages).

**Abnahme:** Playwright-Tests für den Testablauf. Ein Test stellt sicher, dass keine Netzwerkanfrage Antwortdaten enthält. Automatischer Barrierefreiheitscheck.

## Phase 7: Reviews

* Jeder PR in Pipeline, Auswertung und nutzersichtbaren Texten bekommt ein Review durch eine andere Modellfamilie als der Autor.
* Jedes Finding nennt Aussage oder Entscheidung, Problem, Beleg, Auswirkung und eine überprüfbare Korrektur. Der leitende Agent entscheidet und begründet schriftlich, ob er es annimmt, teilweise annimmt oder verwirft. Offene erhebliche Findings blockieren den Release.
* KI-Reviews heißen KI-Reviews, nicht Peer Review. Übereinstimmung zwischen Modellen gilt nicht als Beleg. Getrennte Erstbewertungen und das anschließende PR-Review werden als unterschiedliche Verfahren protokolliert. Ein reines Code-Review erfüllt keine methodische Abnahme.
* Verworfene Findings stehen mit Begründung in `docs/reviews/`. Der Review prüft, ob die Antwort das belegte Problem auflöst; ein strittiges erhebliches Finding gilt nicht allein durch die Verwerfung des leitenden Agents als erledigt. Für den Abschluss gilt die nachfolgende Regel zu zwei Runden. Nach dokumentiertem Abschluss liest der Review-Skill diese Entscheidung und blockiert dasselbe Finding nur erneut, wenn er neue Belege bringt.
* Bleibt ein erhebliches Finding nach zwei Runden strittig, gilt die vorsichtigere Variante: Die betroffene Aussage, Dimension oder Funktion entfällt oder wird als unsicher markiert. Der Streit bleibt dokumentiert.
* Die technische Einrichtung des Reviews steht im Abschnitt Setup.

## Phase 8: Methodenbericht

* Wird aus den Pipeline-Ausgaben erzeugt. Zahlen setzt ein Skript ein, keine Zahl wird von Hand geschrieben.
* Inhalt: Daten, Methoden, Entscheidungen, Ergebnisse, Sensitivität, Grenzen, KI-Beteiligung, Themenabdeckung und zulässige Ergebnisinterpretationen. Technische Prüfergebnisse, methodische Evidenz und Stand des Verständnistests werden getrennt ausgewiesen. Aussagen verweisen auf das Belegregister; fehlende Evidenz und verworfene Interpretationen bleiben nachvollziehbar.
* Jede zitierte Quelle hat DOI oder Link und eine Fundstelle, die ein zweiter Agent geprüft hat.

## Phase 9: Verständnistest (nach dem Deployment, Pflicht)

* Beginnt, wenn die fertige Website deployed ist.
* Codex bereitet `docs/verstaendnistest.md` vor: kurzer Einladungstext mit Link, Hinweis, dass die Antworten ohne Namen veröffentlicht werden, und 4–6 feste Fragen.
* Die Fragen beziehen sich auf die Beispielergebnis-Seite, nicht auf das eigene Ergebnis. Der Test sammelt keine politischen Antworten, Ergebnisse oder Haltungen der Testpersonen.
* Inhalt der Fragen: Was bedeutet ein Wert auf einer Dimension? Was bedeutet der angezeigte Bereich? Was sagt der Vergleich mit Wählergruppen aus und was nicht? Welche Frage oder welcher Text war unklar? Wirkte eine Frage oder ein Text einseitig, und wenn ja, welche?
* Die Auswertungsregeln stehen vor dem Versand fest, z. B. gilt ein Text als missverständlich, wenn ihn mindestens 2 von 5 Personen falsch deuten.
* Die Antworten liegen anonymisiert in `reports/verstaendnistest/`. Codex wertet sie nach den Regeln aus und überarbeitet betroffene Texte in einer neuen Version. Review und Neutralitätsprüfungen laufen erneut.
* Danach nennt der Statushinweis: Verständlichkeit mit 5 Personen geprüft, mit Link zur Auswertung. Das ist ein Verständnistest, keine Validierung, und wird so bezeichnet.

**Todo Steven:** Einladung an 5 Personen mit möglichst unterschiedlicher politischer Haltung schicken, Antworten ohne Namen an Codex übergeben, überarbeitete Version freigeben.

**Abnahme:** Auswertung veröffentlicht, Korrekturen als neue Version deployed, Statushinweis aktualisiert.

## Neutralitätsprüfungen

Alle Schwellenwerte stehen im Analyseplan. Die Ergebnisse jeder Prüfung werden veröffentlicht.

* Blindanalyse und öffentliche Tag-Reihenfolge
* Doppelte KI-Urteile: Aufnahme und Polung von Fragen, Benennung von Dimensionen und Polen sowie Bewertungen nutzersichtbarer Texte erfolgen nach dem getrennten Verfahren aus Setup. Übereinstimmungsraten, ursprüngliche Urteile und Abweichungen werden veröffentlicht. Das ist eine Prüfung der Urteilskonsistenz, kein Nachweis von Richtigkeit oder Neutralität.
* Spiegelsymmetrie der Rohscores
* Messinvarianz zwischen politischen Lagern
* Asymmetrie-Kennzahlen für Texte zu beiden Polen: Länge, Einschränkungen und Relativierungen, wertende Begriffe (Wortliste im Repo, erweiterbar), Zuschreibungen von Motiven und Tatsachenbehauptungen. Das Verfahren legt offen, welche Kennzahlen deterministisch berechnet und welche inhaltlich durch KI beurteilt werden. Die Kennzahlen sind Warnsignale. Eine Schwellenüberschreitung erzeugt ein prüfpflichtiges Finding: Wortlaut, Belege, Gegenbelege, Bewertungsmaßstab und Auswirkung werden inhaltlich geprüft. Es folgt eine Korrektur oder eine belegte Begründung, warum der Unterschied sachlich gerechtfertigt ist. Zahlen oder Textlängen werden nicht allein zur Herstellung formaler Symmetrie angeglichen.
* Perspektivbewertung: Beide Modellfamilien bewerten jede Polbeschreibung aus Sicht einer Person mit dieser Haltung („Würde ich als zutreffende Beschreibung meiner Haltung akzeptieren“, Skala 1–5). Ein deutlicher Unterschied erzeugt ein prüfpflichtiges Finding. Die betroffene Textfreigabe bleibt bis zur dokumentierten inhaltlichen Klärung offen. Die Zahlen sind kein Akzeptanznachweis. Das Verfahren ist eine KI-Simulation, kein Ersatz für Menschen und kein Neutralitätsnachweis. Tatsächliches Verständnis wird in Phase 9 geprüft.
* Inhaltliche Prüfung eigener Texte: gleiche Beleganforderungen und Bewertungsmaßstäbe für alle Positionen, fachlich treffende Beschreibung, angemessene Berücksichtigung belegter Gegenpositionen, sichtbare Unsicherheit und keine unbelegten Motive oder Charakterurteile. Unterschiedlich starke Evidenz darf zu begründeten Unterschieden führen. Der geprüfte Geltungsbereich und die Kriterien für Beanstandungen stehen vorab fest.
* Austauschtest: Eine inhaltlich äquivalente Vertauschung der Pole ändert den Ton nicht.
* Sprache in eigenen Texten: neutrale Formen wie „Befragte“ oder „Wählerschaft“, weder Gender-Sonderzeichen noch generisches Maskulinum
* Gleiche Darstellung und alphabetische Reihenfolge aller Wählergruppen

Einen allgemeinen Politik-Verhaltenstest für Modelle gibt es bewusst nicht. Solche Tests schwanken stark je nach Prompt und messen das Modell, nicht dieses Projekt. Geprüft wird an den konkreten Stellen, an denen Modelle hier urteilen.

## Verboten

* Fragen erfinden, umformulieren, kürzen oder selbst übersetzen
* Parteipositionen schätzen, Ideologie-Labels vergeben, Wahlempfehlungen geben
* Entscheidungen nach Sichtung von Partei- oder Lagerergebnissen ändern, ohne neue Version mit Begründung
* Zahlen von Hand in Texte schreiben
* Quellen ohne geprüfte Fundstelle zitieren
* Antworten von Nutzern speichern oder übertragen
* Git-Historie umschreiben oder Berichte löschen
* Ergebnisinterpretationen über die belegten Konstrukte und Interpretationsgrenzen hinaus behaupten
* Technische Tests, KI-Übereinstimmung, Textkennzahlen oder simulierte Akzeptanz als Ersatz für methodische Evidenz ausgeben
* Den Test als validiert, garantiert neutral oder wissenschaftlich geprüft bezeichnen

## Stopp-Bedingungen

Der leitende Agent hält an und meldet sich per Kommentar in diesem Issue (ohne Linear-Zugriff als GitHub-Issue mit Label `stopp`), wenn:

* die ESS-Bedingungen die geplante Nutzung verbieten oder unklar sind
* weniger als zwei Dimensionen die Schwellen erreichen
* benötigte Daten oder Dokumente fehlen
* sich Vorgaben dieses Issues widersprechen
* sich ein strittiges erhebliches Finding nicht mit der vorsichtigeren Variante aus Phase 7 auflösen lässt

**Todo Steven:** Stopp-Meldungen beantworten.

## Repo und Protokolle

* `docs/analyseplan.md`, `docs/entscheidungen.md`, `docs/lizenzen.md`, `docs/reviews/`, `docs/belegregister.md`, `docs/themenabdeckung.md`
* `reports/phasen/`: versionierte Abnahmeberichte mit getrenntem technischen, methodischen und Verständlichkeitsstatus
* `docs/ki-protokoll.md`: je Auftrag Anbieter, Modell, Version, Datum, Auftragstext im Wortlaut, verfügbare Werkzeuge, zugehöriger PR. Nicht zugängliche interne Vorgaben der Anbieter werden als unbekannt ausgewiesen.
* `pipeline/` Analyse, `model/` versionierte Modelle, `reports/` generierte Berichte, `web/` Website
* `make all` erzeugt aus den Rohdaten alle Modelle, Berichte und Zahlen identisch neu

## Freigabe

Der erste öffentliche Prototyp geht online, wenn die Abnahmen aus Setup und Phasen 0–8 erfüllt sind, der Ablauf und die Auswertungsregeln für Phase 9 vorbereitet sind, keine erheblichen Findings offen sind, `make all` reproduzierbar läuft und Steven einmal durchgeklickt und freigegeben hat. Die fehlende Verständlichkeitsprüfung bleibt bis Abschluss von Phase 9 im Statushinweis sichtbar. Technische Abnahmen und KI-Reviews allein genügen nicht: Für die veröffentlichten Dimensionen und Interpretationen müssen die im Analyseplan festgelegten methodischen Abnahmen erfüllt sein.

**Todo Steven:** Website durchklicken, Grenzen-Seite lesen, Freigabe geben.

Nach dem Deployment folgt Phase 9. Das Projekt ist abgeschlossen, wenn der Verständnistest ausgewertet und die überarbeitete Version deployed ist.

## Änderungshistorie

* 2026-10-02: Fassung 2 ersetzt Fassung 1. Fassung 1 sah ein eigenes, literaturbasiertes Messmodell mit selbst formulierten Fragen vor (Anregung: 12 Axes). Sie setzte menschliche Fachreviews und eine eigene Pilotstudie voraus, die ohne Fachleute und eigene Erhebung nicht umsetzbar sind. Fassung 2 stützt Fragen, Dimensionen und Vergleichswerte auf vorhandene repräsentative Daten. Fassung 1 steht im Wortlaut als Kommentar unter diesem Issue.
* 2026-10-02: Abschnitt „Todos für Steven“ und Setup-Phase ergänzt (Claude-Review als GitHub Action, Auto-Merge, Branch-Schutz). Stevens Aufgaben sind in den Phasen als **Todo Steven** markiert. Regel für strittige Review-Findings ergänzt.
* 2026-10-02: Korrekturen nach einem externen KI-Review (GPT 6.1 sol, von Steven eingereicht; Wortlaut und Entscheidungen als Kommentar unter diesem Issue). Dimensionen und Auswertung als eigenes Modell ausgewiesen, Umfang präzisiert, 0–1-Skalenangleichung ergänzt, Spiegelsymmetrie auf Rohscores korrigiert, Erwartungsmodell mit konkurrierenden Ansätzen vor der Modellbildung ergänzt, doppelte KI-Urteile und messbare Asymmetrie-Prüfungen ergänzt, Bevölkerungslauf als technische Konsistenzprüfung eingeordnet.
* 2026-10-02: Verständnistest mit 5 Personen als verpflichtende Phase 9 nach dem Deployment ergänzt (Entscheidung Steven zu Punkt 9 des externen Reviews). Beispielergebnis-Seite und vorläufiger Statushinweis ergänzt.
* 2026-10-03: Nach der Vorbesprechung mit Steven geschärft. Erste Version als erklärendes Einstellungsprofil für Deutschland mit realen Wählergruppen bestätigt; keine Ideologie-, Länder- oder Personen-Matches. Belegregister und Interpretationsgrenzen, belegte Deutschland-Themenabdeckung, technisch getrennte KI-Erstbewertungen, inhaltliche Neutralitätsprüfung, vorab festgelegte Folgen instabiler Ergebnisse, getrennte Unsicherheitsarten und überprüfbare Phasenabnahmen ergänzt. Schutz von Teil B, Abschluss strittiger Findings und Freigabe vor dem nachgelagerten Verständnistest präzisiert.

