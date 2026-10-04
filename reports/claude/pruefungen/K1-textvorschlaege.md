# K1: Inhaltliche Prüfung der Textvorschläge

4. Oktober 2026. Gesamturteil: **NICHT_BESTANDEN**. Das Urteil gilt ausschließlich für die vorgegebene Fassung `bb760f3cbbe38f1173b96bca4d0537233cfb36a8`. Zwei mittlere Findings blockieren die unveränderte Übernahme des Pakets. Drei niedrige Findings brauchen kleinere Korrekturen. Keine erheblichen Findings. Das ist ein begrenztes KI-Review, keine Abnahme.
## Auftrag und Prüffassung

Geprüft wurde ausschließlich der Inhalt von `docs/vorschlaege-texte-v1.entwurf.md`, Entwurf 1. Die übrigen Manifestdateien sind Grundlagen oder wurden nur gehasht. Der vollständige ursprüngliche Aufrufer-Prompt steht in `execution.prompt` des JSON-Urteils. Der Auftragstext ist über seinen vor Beginn bestätigten Hash gebunden.

Auftrag: `646923d8007cc843204996d8d643b52cb2776130bc231041da3b68665aca4e45`. Manifest: `db73175592234f12bd366857b7597f5db5ec8254189da6f7e2ab6908ff8dd2a8`. Tatsächlicher HEAD und erwarteter Branch-Stand: `bb760f3cbbe38f1173b96bca4d0537233cfb36a8`, Branch `research/life-93-claude-20261003`. Die Arbeitskopie war zu Beginn sauber. Alle elf Artefakthashes stimmen. Der frühere Commit im Manifest bezeichnet den Paketursprung; die aktuelle Bindung wird über die bestätigten Datei-Hashes hergestellt.

Der Auftragsmodus lautet Paketprüfung. Das Schema bietet diesen Modus nicht an. `PR_REVIEW` bildet hier das Review des vorhandenen Textpakets ab. Es wurde keine konkrete Pull Request geprüft und keine wissenschaftliche Erstbewertung behauptet. Die erwähnten fremden Berichte V2 und T1 wurden nicht inhaltlich gelesen.
## Prüfresultate

- K1-C01: BESTANDEN – Auftrag, Manifest, Branch-Stand und alle elf gebundenen Artefakte.
- K1-C02: NICHT_BESTANDEN – Sachliche Richtigkeit und tatsächliche Behebung der Textprobleme.
- K1-C03: BESTANDEN – Begründung zur ESS-Stichprobenziehung anhand der ausdrücklich erlaubten Originalseite.
- K1-C04: NICHT_BESTANDEN – Alle acht vorgeschlagenen Bereichsuntertitel anhand von policy-catalogue.ts, area-scope.ts und Plan v2.2.
- K1-C05: NICHT_BESTANDEN – Handbuch, Status, Sprache, Typografie und Metadaten der vorgeschlagenen öffentlichen Texte.
- K1-C06: BESTANDEN – Grenzen des Vorschlags, Entscheidungshoheit und Einführung neuer Messformen oder Gestaltung.
- K1-C07: BLOCKIERT – Die abschließende Live-Arbeitskopie entspricht dem ursprünglichen Prüfpaket nicht vollständig. Dieser Check ist für das Urteil über die ausdrücklich verlangte alte Fassung nicht erforderlich.

## Findings
### K1-F01 – mittel

Abschnitt 5, Zeile 77: „Gleichstellungsmittel, Familienleistungen, Rechte gleichgeschlechtlicher Paare“.

Der Untertitel verengt freie Lebensführung von Schwulen und Lesben auf Paarrechte. Außerdem fehlt das normative Prinzip zum Vorrang von Männern bei knappen Arbeitsplätzen. Dieses Prinzip ist kein Gleichstellungsmittel und keine Familienleistung.

Belege: `docs/vorschlaege-texte-v1.entwurf.md:77`; `web/src/app/policy-draft/profile/area-scope.ts:69–74`; `docs/analyseplan-v2.2.md:44 (freehms, hmsacld, mnrgtjb)`; `web/src/app/policy-draft/policy-catalogue.ts:177 (Einfügung dieser drei Fragen)`.

Auswirkung: Der Untertitel beschreibt einen vorhandenen Gegenstand zu eng und verdeckt eine eigenständige Frage zur Gleichberechtigung. Schweregrad: Direkt vorgeschlagener sichtbarer Text verschiebt die Reichweite einer Frage und lässt ein zusätzlich aufgenommenes politisches Prinzip weg. Die Originalfragen und die Auswertung bleiben unberührt.

Korrektur: Die Zeile ersetzen durch: „Gleichstellungsmittel, Gleichberechtigung bei knappen Arbeitsplätzen, Familienleistungen, freie Lebensführung von Schwulen und Lesben, Adoptionsrecht gleichgeschlechtlicher Paare“. Eine kürzere Fassung muss dieselben Gegenstände erhalten.

Nachprüfung: Die neue Zeile gegen area-scope.ts und Plan 3.2 prüfen: freie Lebensführung darf keine Partnerschaft voraussetzen, mnrgtjb muss erkennbar sein, hmsacld muss als Adoptionsrecht erhalten bleiben.

Status: OFFEN. Sicherheit: BELEGT. Blockiert den Paketumfang: ja.
### K1-F02 – mittel

Abschnitt 5, Zeile 72: „Demokratieverständnis, Mehrheit und Regierung, Führung und Gesetz“.

Das Verbot demokratiefeindlicher Parteien fehlt als eigener Gegenstand. „Demokratieverständnis“ benennt im bestehenden Bereich die Wichtigkeit von Demokratiemerkmalen und macht diese zusätzliche Maßnahme nicht erkennbar.

Belege: `docs/vorschlaege-texte-v1.entwurf.md:72`; `web/src/app/policy-draft/profile/area-scope.ts:30–35`; `docs/analyseplan-v2.2.md:45 (ESS5 B32 prtyban)`; `web/src/app/policy-draft/policy-catalogue.ts:164 (prtyban wird eingefügt)`.

Auswirkung: Der Untertitel erfüllt seine vorgesehene Funktion als Beschreibung des tatsächlich erfassten Inhalts nur teilweise. Schweregrad: Die Auslassung betrifft einen eigenständigen Gegenstand der Erweiterung v2.2, nicht bloß eine Detailbedingung innerhalb eines schon benannten Fragenblocks.

Korrektur: Den Untertitel ersetzen durch: „Wichtigkeit von Demokratiemerkmalen, Regierung und Mehrheitsmeinung, Führung, Loyalität und Gesetz, Verbot demokratiefeindlicher Parteien“.

Nachprüfung: Mit area-scope.ts und der Einfügung von accalaw, loylead und prtyban abgleichen. Die Formulierung muss eine Frage nach Parteienverboten nennen, ohne eine politische Position zu bewerten.

Status: OFFEN. Sicherheit: BELEGT. Blockiert den Paketumfang: ja.
### K1-F03 – niedrig

Abschnitt 3 empfiehlt die drei neuen Begriffszeilen als Korrektur des Handbuchs ohne Dimensionen.

Die unmittelbar betroffene Zeile „eigenes Modell“ bleibt unerwähnt und schreibt weiterhin „Auswahl, Dimensionen, Auswertung und Deutung durch das Projekt“. Nach Übernahme der drei vorgeschlagenen Zeilen bliebe damit eine widersprüchliche Vorgabe in derselben Begriffstabelle stehen.

Belege: `docs/vorschlaege-texte-v1.entwurf.md:31–45`; `docs/handbuch.md:278`; `docs/profilregeln-v1.md, Abschnitt „Warum ein beschreibendes Profil ohne Werte“`; `docs/vorschlaege-texte-v1.entwurf.md:13 (Auswahl, Ordnung und Auswertung)`.

Auswirkung: Der Vorschlag behebt den benannten Widerspruch des Handbuchs nicht vollständig. Schweregrad: Eine zusätzliche Begriffszeile ist zu korrigieren. Der empfohlene Ergebnis-Statushinweis selbst enthält bereits keine Dimensionen mehr.

Korrektur: Abschnitt 3 um eine vierte Zeile ergänzen: „eigenes Modell | Auswahl, Ordnung, Auswertung und Deutung durch das Projekt | Modell des ESS“.

Nachprüfung: Die vollständige Tabelle 7.3 nach der vorgeschlagenen Übernahme lesen. Dimensionen dürfen nur als bedingte, in dieser Fassung nicht vorhandene Messform beschrieben sein.

Status: OFFEN. Sicherheit: BELEGT. Blockiert den Paketumfang: nein.
### K1-F04 – niedrig

Abschnitt 1, Variante B, Zeilen 14–16: „wissenschaftlichen Befragungen, derzeit dem European Social Survey“; B erst nach Freigabe einer weiteren Quelle.

Die für mehrere Quellen gedachte Variante benennt nach ihrer eigenen Übernahmebedingung weiterhin nur den ESS als aktuelle Herkunft. Sobald Fragen oder Vergleichsdaten einer weiteren Quelle tatsächlich einfließen, ist diese Herkunftsangabe unvollständig. Eine bloße Freigabe einer Quelle sagt außerdem noch nicht, dass sie im gezeigten Bestand verwendet wird.

Belege: `docs/vorschlaege-texte-v1.entwurf.md:9–16`; `docs/analyseplan-v2.2.md:29 (Herkunft der gegenwärtigen Fragen)`; `docs/project.md, Abschnitt „Aktueller Stand“, Fragen und offene Quellenentscheidungen`.

Auswirkung: Die Zukunftsvariante löst das ausdrücklich benannte Problem einer späteren Herkunft außerhalb des ESS nicht zuverlässig. Schweregrad: Die empfohlene gegenwärtige Variante A ist richtig. Betroffen ist eine ausdrücklich zurückgestellte Alternative.

Korrektur: B als auszufüllende Vorlage kennzeichnen: „Fragen und Vergleichsdaten stammen aus den jeweils angegebenen wissenschaftlichen Befragungen.“ Als Übernahmebedingung tatsächliche Einbindung freigegebener Quellen nennen. Werden Quellen stattdessen im Pflichttext aufgezählt, dort alle tatsächlich verwendeten Quellen nennen.

Nachprüfung: Bei späterer Übernahme die Herkunftsangabe gegen den dann gebundenen Fragen- und Referenzbestand prüfen. Eine Quellenfreigabe allein darf keine Nutzung behaupten.

Status: OFFEN. Sicherheit: BELEGT. Blockiert den Paketumfang: nein.
### K1-F05 – niedrig

Abschnitt 2, empfohlene Variante B, Zeile 27: „Er beschreibt Antworten Frage für Frage und ist noch nicht verfügbar.“

„Er“ bezieht sich auf den geplanten Test. Dessen beabsichtigtes Verhalten steht im Präsens, obwohl Handbuch 7.2 geplante Funktionen mit „soll“, „geplant“ oder „vorgesehen“ verlangt. Der vorhandene Forschungsentwurf wird in dieser Meta-Beschreibung nicht als Bezug genannt.

Belege: `docs/vorschlaege-texte-v1.entwurf.md:27–29`; `docs/handbuch.md:260 (7.2: Präsens nur für Vorhandenes)`; `docs/project.md, Abschnitt „Aktueller Stand“ (lokaler Forschungsentwurf, Test in Vorbereitung)`.

Auswirkung: Die empfohlene Meta-Beschreibung hält die Statusregel für den noch nicht verfügbaren Test nicht durchgehend ein. Schweregrad: Name, Nichtverfügbarkeit und Zeichengrenze sind korrekt. Eine kleine sprachliche Änderung genügt.

Korrektur: B ersetzen durch: „12 Axes Deutschland plant einen Test zu politischen Einstellungen in Deutschland. Er soll Antworten Frage für Frage beschreiben und ist noch nicht verfügbar.“ Diese Fassung hat 157 Zeichen.

Nachprüfung: Unicode-Zeichen ohne äußere Anführungszeichen zählen: 157, also höchstens 160. Namen am Anfang, Nichtverfügbarkeit und „soll“ für die geplante Beschreibung prüfen.

Status: OFFEN. Sicherheit: BELEGT. Blockiert den Paketumfang: nein.
## Abgleich aller Bereichsuntertitel

| Bereich | Befund |
| --- | --- |
| Wirtschaft und Verteilung | Gerechtigkeitsprinzipien und Umverteilung tragen den vorhandenen engen Inhalt. Keine neue Messform. |
| Sozialstaat | Staatliche Verantwortung, Leistungszielgruppen und Grundeinkommen sind vorhanden. Zielgruppen fasst auch die Umschichtung zwischen Leistungsgruppen knapp zusammen. Konkrete Bedingungen bleiben bei Erfasst und den Originalfragen. |
| Demokratie und politische Autorität | K1-F02: Parteienverbot als eigenständigen Gegenstand ergänzen. |
| Bürgerrechte und Sicherheit | Pflichten, Strafen und Pandemieabwägungen sind vorhanden. Die Pandemiebegrenzung bleibt erhalten. |
| Europäische Integration | Mitgliedschaft, Entscheidungsebene, Einigungsrichtung und EU-Sozialprogramm sind vorhanden. Das Programm wird nicht zur umfassenden EU-Sozialpolitik erklärt. |
| Klima und Energie | Klimamaßnahmen und Stromquellen sind vorhanden; die Begrenzung auf Strom bleibt sichtbar. |
| Migration | Herkunftsgruppen, Sozialrechte und Asyl sind vorhanden. Asyl ist hier der knappe Oberbegriff für Asylprüfung und den Familiennachzug von Geflüchteten; keine Aussage über umfassende Migrationspolitik. |
| Gleichstellungs- und Familienpolitik | K1-F01: freie Lebensführung als individuellen Gegenstand erhalten und Gleichberechtigung bei knappen Arbeitsplätzen ergänzen. |

Die acht Untertitel sind sachliche Gegenstandslisten, keine politischen Wertungen. Unterschiedliche Listenlängen ergeben sich aus dem Bestand. Eine Stichwortliste muss nicht alle Bedingungen der Einzelfragen wiederholen, aber eigenständige Gegenstände erkennbar halten. Die vorhandenen Angaben Erfasst/Nicht erfasst müssen bestehen bleiben.
## Tragfähige Vorschläge und ESS-Abgleich

Statushinweis A ersetzt die unzutreffende Dimensionsankündigung durch Auswahl, Ordnung und Auswertung. Das stimmt mit dem beschreibenden Profil überein. Die vorgeschlagenen Begriffe Profil und Bereich erhalten die Trennung zwischen Einzelfragen, Leseordnung und einer möglichen späteren Messform. Die Dimension-Zeile führt keine aktuelle Dimension ein. Der verbleibende Widerspruch in der Zeile eigenes Modell steht in K1-F03.

Meta A und B haben tatsächlich 141 beziehungsweise 151 Zeichen ohne äußere Anführungszeichen. Beide beginnen mit dem Namen und nennen den Status. Meta A beschreibt die geplante Funktion innerhalb des Planungssatzes. Für das empfohlene B ist K1-F05 zu korrigieren.

Die [ESS-Seite zur Stichprobenziehung](https://www.europeansocialsurvey.org/methodology/sampling) ist nach Weiterleitung direkt zugänglich. Sie beschreibt Zufallsauswahl in jeder Stufe, untersagt Quoten und das Ersetzen nicht teilnehmender Haushalte oder Personen und nennt Anforderungen an die Zielpopulation ab 15 Jahren in Privathaushalten. Die vorgeschlagene Formulierung A über Zufallsstichproben ist damit belegt. Die Unterscheidung zwischen Verfahrensanforderung und eigener Prüfung der erreichten Abdeckung ist sachlich richtig. Die Seite belegt keine eigene Repräsentativitätsprüfung des Projekts. Den gesonderten Satz über München in ESS8 habe ich nicht anhand des ursprünglichen Stichprobendokuments bestätigt.

Die Statusleiste, Fußzeile und Standardformel werden durch den Entwurf nicht verändert. Der vorgeschlagene neue Ergebnis-Pflichttext ist bis zu Stevens Entscheidung keine zulässige Ersetzung der geltenden Wortlautvorgabe. Kein Vorschlag führt Gesamtwerte, Achsen oder politische Personenetiketten ein. Die zusätzliche Untertitelzeile ist beschreibender Text und erlaubt keine eigenmächtige neue Gestaltung.
## Abweichung während der Prüfung

Bei der Abschlusskontrolle war HEAD bereits `5a6485964026a25f8ee7d149570ba0a16223dce3`. `docs/project.md` hatte nun SHA-256 `a4a5736e1e2263bfbcbec82ade86e1190540a9523fe96e1214fb2e008b5c1c5e`, statt des manifestgebundenen `2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a`. Ein nur lesender Diff zeigte eine Ergänzung zum Stand des Plans v2.3. Die neue Aussage wurde nicht als Prüfgrundlage übernommen.

Auftrag, Manifest und die zehn übrigen Artefakte blieben unverändert. Alle elf Artefakte des ausdrücklich angeforderten unveränderlichen Git-Stands wurden danach über `git show bb760f3cbbe38f1173b96bca4d0537233cfb36a8:<Pfad>` erneut gehasht. Sie stimmen vollständig mit dem Manifest überein. Die anfangs gelesene Projektdatei war diese alte gebundene Fassung. Daher bleibt die Inhaltsprüfung ausführbar und das Gesamturteil NICHT_BESTANDEN für diese Fassung. Es gilt nicht für den späteren Live-Stand. Ein Review des neuen Stands braucht eine neue Paketbindung. Keine fremde Änderung wurde zurückgesetzt.

## Grenzen und Zugriffe

Begrenztes KI-Review der Textvorschläge, keine methodische Validierung, Begutachtung durch Fachleute, Neutralitätsgarantie, Abnahme oder Veröffentlichungsfreigabe.

Der Auftrag nennt den Modus Paketprüfung. Das Urteilsschema enthält diesen Wert nicht. PR_REVIEW ist die hier verwendete Schema-Kategorie für das Review eines bestehenden Pakets, ohne Prüfung einer konkreten Pull Request und ohne Umdeutung in eine unabhängige wissenschaftliche Erstbewertung.

Die elf Manifestartefakte wurden gehasht. V2-urteil.json und T1-technik-browser.md wurden ausschließlich zur Hashprüfung als Bytes gelesen, nicht als Bewertungsgrundlage. Die im Entwurf und Plan selbst erwähnten früheren Findings sind sichtbar, wurden aber nicht als eigene Prüfergebnisse übernommen.

policy-catalogue.ts bindet Fragen durch Imports. Die importierten öffentlichen Kataloge und die Originalfragebögen gehören nicht zum Manifest und wurden nicht geöffnet. Der Inhaltsabgleich nutzt die gebundene Bereichsbeschreibung und Plan 3.2; keine erneute Prüfung sämtlicher Originalwortlaute.

Kein Zugriff auf data/raw/, data/local/, outputs/ oder data/reference-*, keine Antwortverteilungen und keine GESIS-Server. Die Aussage zu München in ESS8 wurde nicht anhand des ursprünglichen Stichprobendokuments nachgeprüft. Die erfolgreiche ESS-Seitenprüfung betrifft das allgemeine Verfahren.

LIFE-93 wurde nicht live abgerufen. Der Pflichttextabgleich verwendet die im Prüfpaket überlieferte Fassung und Handbuch 7.7. Eine spätere Änderung des Wortlauts benötigt Stevens Entscheidung.

Abschnitt 6 ist eine Statusnotiz, kein neuer Textvorschlag. Die Erklärung der 95-%-Bereiche ist in der gebundenen HTML-Vorlage erkennbar; die konkrete historische Umsetzung der Restgruppenbeschriftung und ihr Datum sind ohne die nicht freigegebenen Adapter/Verlaufsquellen nicht vollständig nachgeprüft.

Ein vorgeschriebener Memory-Suchlauf zeigte Einträge früherer begrenzter Reviews und einzelne historische Statusangaben. Keine verlinkte Reviewdatei wurde geöffnet, kein früheres Urteil für diesen Befund verwendet. Memory diente nur als Erinnerung an Hashbindung und Schreibgrenzen; alle aktuellen Feststellungen wurden am Paket geprüft.

Nur die zwei verlangten Berichte werden geschrieben. Keine Commits, Tags, Pushes, externen Nachrichten oder Implementierungsänderungen. Keine pnpm-/Browser-/Pipelineprüfung, weil der Auftrag nur Berichtsausgaben erlaubt und keine Implementierung oder sichtbare Seite geändert wird.

jsonschema ist nicht installiert. Das JSON wird mit einem eigenen nur lesenden Python-Validator gegen die im vorgegebenen Schema verwendeten Schlüsselwörter geprüft. Dies ist eine formale Kontrolle, keine zusätzliche inhaltliche Prüfung.

Die ersten umfangreichen Sammelausgaben waren vom Werkzeug teilweise abgeschnitten. Handbuch, HTML und die für Findings nötigen Plan-/Katalogabschnitte wurden anschließend in kleineren Ausgaben gelesen. Das Handbuch wurde vollständig gelesen. Bei Plan und HTML wurden keine fehlenden Textteile als gelesen ausgegeben.
## Ausgeführte Befehle und Werkzeugaufrufe

Die folgenden Befehle wurden im vorgegebenen Arbeitsverzeichnis ausgeführt. Python-Skripte liefen aus Here-Documents ohne Skriptdatei. Kein Skript öffnete einen verbotenen Datenordner.

- `sha256sum reports/claude/auftraege/K1-textvorschlaege.md reports/claude/pruefungen/TEXTE-V1-001-manifest.json`.
- `cat` für Auftrag, Review-Skill, Urteilsschema, Unslop-Skill, Manifest, project.md, handbuch.md, profilregeln-v1.md und analyseplan-v2.2.md.
- `rg -n` im Memory-Register mit Suchmustern bounded, Prüf, K1 und TEXTE. Keine verlinkten Memory-Berichte geöffnet.
- `git rev-parse HEAD`, `git branch --show-current`, `git status --short`.
- Python: Manifest einlesen, SHA-256 aller elf aufgeführten Artefakte berechnen und mit den Sollwerten vergleichen.
- `nl -ba` für Textentwurf, area-scope.ts, policy-catalogue.ts, policy-draft.html und index.html. Kleinere Nachlesungen: `sed -n` mit Handbuch 1–210 und 211–460, HTML 1–210 und 200–260, Plan 20–95 und 95–220, Handbuch 275–350, policy-catalogue.ts 1–220.
- Python: Meta-Varianten auslesen und Unicode-Zeichen zählen; korrigierte Meta B zählen; zusätzliche Steuerdateien hashen; jsonschema-Verfügbarkeit und Existenz der beiden Berichtspfade prüfen. jsonschema ist nicht installiert; beide Berichtspfade waren vorher nicht vorhanden.
- `web.run.open` für die im Entwurf genannte ESS-URL: Werkzeugfehler. `web.run.search_query` mit zwei auf diese ESS-Stichprobenseite bezogenen Suchanfragen: Suchergebnisse, kein Ersatz für die Originalseite. `web.run.open` für die weitergeleitete URL: 502. Keine Suchergebniszahlen oder fremden Webseiten als sachliche Grundlage verwendet.
- Python `urllib.request.urlopen` mit benanntem Review-User-Agent: Original-ESS-URL erfolgreich geöffnet, Weiterleitung auf `/methodology/sampling`, HTML nur im Speicher gelesen, SHA-256 berechnet und die Sampling-Grundsätze textlich geprüft. Keine Webdatei gespeichert.
- Zusätzliche Nachlesung der Belegzeilen: Handbuch 242–260, policy-catalogue.ts 173–200 und 158–179. `git diff bb760f3cbbe38f1173b96bca4d0537233cfb36a8 -- docs/project.md` für die festgestellte Live-Abweichung. Python/subprocess mit `git show` des vorgegebenen Git-Stands für alle elf Manifestartefakte, ohne Dateien zu schreiben.
- `PYTHONDONTWRITEBYTECODE=1 python3`: ausschließlich die beiden Berichtdateien schreiben; anschließend JSON parsen, mit eigenem Validator gegen das vorgegebene Schema prüfen, Hashes und Git-Status erneut kontrollieren.

Kein `pnpm check`, keine Pipeline-Tests und kein Browserlauf: Dies ist eine Prüfung eines unveränderten Entwurfs mit ausschließlich zwei erlaubten Berichtausgaben. Solche Prüfungen würden keine wissenschaftliche Abnahme ergeben und können zusätzliche Dateien schreiben.
## Dateien und Hashes

Manifestartefakte: vor Beginn in der Arbeitskopie und nach Abschluss im expliziten ursprünglichen Git-Stand bestätigte SHA-256. Am Ende stimmen zehn Artefakte auch in der Live-Arbeitskopie; für project.md gilt die gesondert dokumentierte Abweichung:

| Datei | SHA-256 | Zugriff |
| --- | --- | --- |
| `docs/vorschlaege-texte-v1.entwurf.md` | `f1ed0b3844096c9af5e0c56064ed75b6b2b1918be7a6223053e3d829f82b2b2a` | Text und Hashprüfung |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` | Text und Hashprüfung |
| `docs/profilregeln-v1.md` | `3f235f026588baba350a477012be9c29d533d397e58ec813572a3d5475b4bc23` | Text und Hashprüfung |
| `docs/analyseplan-v2.2.md` | `13b052a9e58fac20f55b21a430a3d92738b1be6e1da5648c8ac3c6f9a87638d8` | Text abschnittsweise und Hashprüfung |
| `docs/project.md` | `2ff27e5aa553ea2307bd4d28da436991c5ebb3b019f316d9aae95ee81d57696a` | Text und Hashprüfung |
| `web/src/index.html` | `d3dcf44566fd2c05d92b9acdf0c9d0e570b472abd3edfa7ac4face20fc15657c` | Text und Hashprüfung |
| `web/src/app/policy-draft/policy-draft.html` | `f25712dc8d6fbd85c5d93fa4c6db8c006fe5132282db06f922733fd9e2c94b2a` | Text abschnittsweise und Hashprüfung |
| `web/src/app/policy-draft/policy-catalogue.ts` | `acde504fa6f0b815d93c66a842d1a25270092713ea898df97b9e8617388a6193` | Text und Hashprüfung |
| `web/src/app/policy-draft/profile/area-scope.ts` | `4ed439fd3a1d9b9d030f8ed33b9a4d55916d07cc694bcf8a3aec6f86d338a1b1` | Text und Hashprüfung |
| `reports/claude/agenten/V2-urteil.json` | `622e6961b36655943f126ffa25eb7758e3d7b025fa3a1b6275630beb673d02cf` | nur Hashprüfung |
| `reports/claude/agenten/T1-technik-browser.md` | `3bba4b1112db99f9938104ba82b17fdfb552d57657a5440ea4827ce7f88e3636` | nur Hashprüfung |

Zusätzlich gelesene Steuerdateien und Memory-Suchlauf:

| Datei | SHA-256 |
| --- | --- |
| `reports/claude/auftraege/K1-textvorschlaege.md` | `646923d8007cc843204996d8d643b52cb2776130bc231041da3b68665aca4e45` |
| `reports/claude/pruefungen/TEXTE-V1-001-manifest.json` | `db73175592234f12bd366857b7597f5db5ec8254189da6f7e2ab6908ff8dd2a8` |
| `.claude/skills/life93-review/SKILL.md` | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json` | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md` | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `/home/stevenh/.codex/memories/MEMORY.md` | `76f2f657085b44e17509620a780b027f403f3a78b1071635fd413784c995f9e9` |

Abschließend gelesene Live-Fassung von `docs/project.md`: `a4a5736e1e2263bfbcbec82ade86e1190540a9523fe96e1214fb2e008b5c1c5e`. Sie wurde nur zur Abweichungsdiagnose gelesen, nicht als neue Grundlage übernommen.

ESS-HTML, einmal direkt abgerufen und nur im Arbeitsspeicher: `b590ff5edc7a0c260be9e6c76c4b3063b1b2d69d98b4c40d87242777d4595cd3`. Dieser Hash bindet den tatsächlich gelesenen Abruf, nicht eine vorab gesicherte Websitefassung.

## Formale Kontrolle und Laufzeit

JSON-Parsing und die Kontrolle gegen alle im vorgegebenen Schema verwendeten Schlüsselwörter bestanden. Zwei Negativproben wiesen ein BESTANDEN trotz negativer erforderlicher Checks und ein KORRIGIERT mit blocksScope=true ab. Der erste Abschlusslauf der Artefaktprüfung endete mit AssertionError für docs/project.md; die Abweichung und die erneute Bindung des ursprünglichen Git-Stands stehen oben. Die endgültigen Berichte wurden danach erneut formal kontrolliert. Modell laut T3-Laufzeit: OpenAI `gpt-6.1-sol`, high reasoning effort, Codex harness. Interne Modellrevision und nicht belegbare Anbieterangaben sind unbekannt.
