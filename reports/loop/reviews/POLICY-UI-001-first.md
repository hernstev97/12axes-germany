# POLICY-UI-001 – unabhängige Erstprüfung

Entscheidung: **NOT_ACCEPTED** für den gepinnten lokalen Vorschlag `POLICY-UI-001/v1`.

Prüfdatum: 3. Oktober 2026. Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Prüfer: Codex, Laufzeitangabe `gpt-6.1-sol`, Reasoning `ultra`.

Die Fassung ist prüfbar. Der äußere Manifest-Pin und alle elf Artefakt-Pins stimmen vor und nach der Prüfung. Zwei eng begrenzte Textbefunde und ein widersprüchlicher interner Dateipin bleiben offen. Die Ablehnung betrifft die Ergebnisformulierungen und die Paketdokumentation dieses lokalen Vorschlags. Sie verlangt keine neue Quellenrecherche, keine ESS-Analyse und keine persönliche Statistik-Abnahme.

## Auftrag und Unabhängigkeit

Ich erhielt den Prüfauftrag und die aktuellen Useranweisungen zu AGENTS, keine Verteidigung der Fassung und keine vorangegangenen Urteile. Ich habe nur die elf Manifestartefakte semantisch gelesen, einschließlich des vollständigen `docs/handbuch.md`, sowie den verlangten unslop-Skill unter `/home/stevenh/projects/12axes-germany/.agents/skills/unslop/SKILL.md`. Der Katalog wurde vollständig gelesen: Metadaten und alle Felder sämtlicher 43 Items. Die Schriftdatei wurde gehasht und auf die WOFF2-Signatur geprüft; daraus folgt keine visuelle Schriftprüfung.

Andere Reports, Autorberichte, state, handoff und ältere Ergebnisse wurden nicht geöffnet. Kein Git, pnpm, Server, Browser, globaler Installationslauf, Authzugriff, Claude oder weiterer Subagent wurde genutzt. `prepare.py` wurde gelesen, nicht ausgeführt. Der Schreibbereich beschränkt sich auf diesen neuen Erstbericht und `outputs/loop/policy-ui-001-review/`. Die Ausgangsfassung wurde nicht verändert oder formatiert. Dieser Erstbericht wird nach Erstellung nicht überschrieben.

Root bleibt Koordinator und führt die tatsächliche Browserprüfung separat durch. Dieses Urteil ist keine Human-Design-, empirische Äquivalenz-, Produkt- oder Releaseabnahme.

Ich bin Codex; Root ist ebenfalls Codex. Damit fehlt eine Gegenprüfung durch eine andere Modellfamilie. Zwei gemeinsame Fehlerquellen bleiben: Wir können eine plausible deutsche Kurzfassung für semantisch gleichwertig halten, obwohl sie den Gegenstand erweitert. Wir können technische Konsistenz mit Quellen-/Datenidentität oder Erhebungsäquivalenz verwechseln. Getrennte Codex-Läufe beseitigen diese möglichen korrelierten Fehler nicht. Ein tatsächlicher Fehler von Root wurde hier nicht untersucht und wird nicht behauptet.

## Befunde mit begrenztem Blockerumfang

### PUI-R1 – „statt“ verändert den Mengenvergleich

- Stelle: `prototypes/policy-v2/prototype.js:23`; Original im lokalen Katalog `catalogue.js:963–965`.
- Evidenz: Der Ergebnistitel lautet „Ausbildung statt Arbeitslosenunterstützung“. Die Originalfrage verlangt **mehr** Aus- und Weiterbildung und dafür **weniger** Arbeitslosenunterstützung unter einer festen Geldsumme. Sie verlangt keinen vollständigen Ersatz der Unterstützung. Der Erläuterungssatz unter dem Titel enthält den richtigen Mengenvergleich.
- Auswirkung: Wer die Ergebnisüberschrift liest, kann eine Antwort zur Budgetverschiebung als Zustimmung oder Ablehnung einer Abschaffung der Unterstützung verstehen. Der richtige Absatz reduziert das Problem, macht die stärkere Überschrift aber nicht richtig.
- Minimale Korrektur: Etwa „Mehr Aus- und Weiterbildung, weniger Arbeitslosenunterstützung“. Originalfrage, Kategorien, Budgetkontext und bestehender Erläuterungssatz können bleiben.
- Blockerumfang: Diese eine Ergebnisbenennung. Kein Forschungs-, Daten-, Modell- oder Quellenblocker.

### PUI-R2 – Drei Gerechtigkeitsurteile werden zu allgemeiner Zustimmung verkürzt

- Stellen: `prototype.js:15–17`; Originalaussagen `catalogue.js:408`, `:463`, `:518`, jeweils mit Einleitung unmittelbar darunter.
- Evidenz: `sofrwrk`, `sofrpr` und `sofrprv` fragen danach, unter welcher Bedingung eine Gesellschaft gerecht ist. Die neuen Sätze nennen dagegen „Zustimmung zu höherem Einkommen“, „Zustimmung zur Fürsorge“ und „Zustimmung zu Privilegien“. Bei `sofrwrk` fehlt außerdem der Originalvergleich „mehr … als andere“. Der benachbarte Eintrag `sofrdst` wahrt mit „als Gerechtigkeitsprinzip“ diese Grenze bereits. Der vollständige Originalkontext ist in den aufklappbaren Ergebnisdetails vorhanden.
- Auswirkung: Die unmittelbaren Erläuterungen können ein Urteil über gesellschaftliche Gerechtigkeit als allgemeine Befürwortung einer Leistung oder eines Privilegs ausgeben. Das ist eine Bedeutungsverschiebung, keine bloße Stilfrage. Sie betrifft besonders die politisch empfindliche Familienprivilegien-Aussage. Eine konkrete Zustimmung oder Ablehnung der Originalaussage darf keine breitere Position erhalten.
- Minimale Korrektur: Die drei Sätze ausdrücklich auf Zustimmung oder Ablehnung des genannten Gerechtigkeitsprinzips beziehen. Bei `sofrwrk` „höheres Einkommen als andere für hart arbeitende Menschen“ erhalten. Keine Personenbezeichnungen ergänzen. Beispiele sind „Die Auswahl beschreibt Zustimmung oder Ablehnung der Aussage, dass eine Gesellschaft gerecht ist, wenn hart arbeitende Menschen mehr verdienen als andere.“ und die entsprechenden eng gebundenen Fassungen für Fürsorge und Familienprivilegien.
- Blockerumfang: Drei eigene Ergebnis-Erläuterungen. Die Originalformulierungen und Antwortkategorien werden damit nicht beanstandet. Keine empirische Prüfung oder Itemauswahl verlangt.

### PUI-R3 – Der interne Manifest-Pin für `prepare.py` ist falsch

- Stelle: `prototypes/policy-v2/manifest.json:30–32`.
- Evidenz: Dort steht `36a90d859e5b456e67085899262ed5f014130e76759a07f6f517841546a6d9aa`. Der tatsächliche SHA-256 ist `5dda504d26142be720f060756c300c24e2c7a06e1b0f169b292e8f4ebfb41900`. Dieser tatsächliche Hash stimmt mit dem äußeren Paketmanifest überein. Die Bytezahl 4046 stimmt in beiden Fassungen. Vor- und Nachprüfung zeigen denselben Widerspruch; die übrigen acht internen Dateipins stimmen.
- Auswirkung: Das Paket enthält zwei unterschiedliche Identitätsangaben für dieselbe Datei. Die äußere Prüffassung ist dadurch weiterhin eindeutig und prüfbar; die interne Integritätsdokumentation ist falsch.
- Minimale Korrektur: In einer neuen Fassung den internen `prepare.py`-Pin neu bilden und anschließend das äußere Paketmanifest neu pinnen. Das geprüfte v1-Paket und diesen Erstbericht nicht nachträglich umschreiben.
- Blockerumfang: Lokale Paketdokumentation. Kein Laufzeitfehler, kein Nachweis einer Datenabweichung, kein Forschungsblocker.

## Originalkontext, Modi und Zeitbasis

Der reguläre Fortgang stellt B1–B12 zusammenhängend in der angegebenen Reihenfolge dar. `keydec` wird unmittelbar hinter B11 eingefügt (`prototype.js:63–74`); B25 folgt danach. Die zwölf Wichtigkeitsfragen erhalten die gemeinsame Demokratieeinleitung, den jeweiligen Antwortstamm und die vollständigen 0-/10-Anker. Sie werden als Demokratie im Allgemeinen erläutert, nicht als Messung der tatsächlichen Demokratie in Deutschland. Der Hinweis auf die ausgelassenen B13–B24 steht sichtbar in der Entwicklungsnotiz (`:154–156`). Direkte Sprünge sind ausdrücklich als Entwurfsprüfung beschrieben; sie sind keine Zusage eines unveränderten Gesamtfragebogens.

B25 erhält den Konfliktkontext mit der großen Bevölkerungsmehrheit, beide nominalen Aussagen und die Einzelauswahlanweisung. Der sichtbare Hinweis nennt die ursprünglichen Papierweiterleitungen B26 oder B28, den neuen auswahlunabhängigen Fortgang und das Auslassen B26–B29 (`:158–159`). Die Codeprobe bestätigt denselben neuen Fortgang für beide Alternativen. Die historische operative Weiterleitung wird nicht heimlich ausgeführt oder als CAWI-äquivalent ausgegeben.

Der Katalog benennt CAPI/CAMI für ESS5/8/9/11 und Papier sowie CAWI für ESS10 Self-completion. Die Oberfläche zeigt Erhebungsmodi, gebundene Originalform, Erhebungszeit und Versionshinweise getrennt (`:166–220`). Ihre Radioauswahl und neue Zusammenstellung werden ausdrücklich als ungeprüfte Entwicklungsfassung bezeichnet. Die ESS10-Angaben 3.2 gegenüber 3.1 in überlieferter Zitationsvorgabe bleiben sichtbar widersprüchlich. Das Review bestätigt diese lokalen Angaben und ihre Darstellung, nicht die historische Quellenidentität.

Für `hrshsnta` erklärt sowohl die sichtbare Entwicklungsnotiz als auch die neue Ergebnis-Erläuterung, dass „heute“ die damalige Strafpraxis 2010/2011 meint (`:38`, `:161–162`). Die anderen historischen Fragen erhalten in ihren Details Erhebungszeiten und die Grenze „Keine aktuelle Bevölkerungsnorm für 2026“. Die UI berechnet keine historischen Referenzzahlen. Jede Ergebnisangabe nennt „Historische Referenz noch nicht freigegeben“ (`:316`). Erhebungsdaten, Skalenanker und Originalkategorien sind keine solchen Referenzwerte.

Die deklarierte Zielpopulation wird von erreichter deutscher Abdeckung getrennt. Es gibt weder eine Gleichsetzung der historischen Bevölkerung mit dem heutigen Publikum noch einen Beleg der erreichten Abdeckung aus diesem UI-Code.

## Sichtung aller 43 neuen Benennungen und Erläuterungen

Die Zuordnung erfolgt ausschließlich über das konkrete Item und seine gewählte Originalkategorie (`prototype.js:302–315`). Die Erläuterung erscheint nur bei `answered`. Übersprungene und unberührte Items erhalten keine politische Deutung. Die nachfolgende Sichtung beurteilt die Bindung an die lokalen Originalangaben; sie zertifiziert keine Neutralität oder empirische Fairness des gesamten Instruments.

| Variable | Befund zur neuen Ergebnisangabe |
| --- | --- |
| `sofrdst` | Verteilung von Einkommen und Vermögen bleibt ausdrücklich ein Gerechtigkeitsprinzip. |
| `sofrwrk` | PUI-R2: Gerechtigkeitsgegenstand und Vergleich mit anderen erhalten. |
| `sofrpr` | PUI-R2: Fürsorge unabhängig von Gegenleistung als Gerechtigkeitsurteil kenntlich machen. |
| `sofrprv` | PUI-R2: Privilegien wegen hoher Familienstellung als Gerechtigkeitsurteil kenntlich machen. |
| `gincdif` | Konkrete staatliche Verringerung der Einkommensunterschiede; keine Steuer- oder Eigentumsordnung abgeleitet. |
| `gvslvol` | Gewünschte staatliche Verantwortung für angemessenen Lebensstandard im Alter. |
| `gvslvue` | Entsprechende Verantwortung für Arbeitslose. |
| `gvcldcr` | Ausreichende Kinderbetreuung für berufstätige Eltern; Zuordnung zum Sozialstaat ist eine Themenordnung. |
| `bnlwinc` | Beschränkung auf niedrigste Einkommen samt Folge für mittlere/hohe Einkommen bleibt enthalten. |
| `eduunmp` | PUI-R1 im Titel; Absatz erhält feste Geldsumme und mehr/weniger. |
| `fairelc` | Wichtigkeit freier und fairer Parlamentswahlen; ausdrücklich keine tatsächliche Wahl bewertet. |
| `dfprtal` | Wichtigkeit inhaltlicher Parteiunterschiede im allgemeinen Demokratiekontext. |
| `medcrgv` | Wichtigkeit des Rechts zur Regierungskritik; keine Aussage zur tatsächlichen Medienpraxis. |
| `rghmgpr` | Wichtigkeit geschützter Minderheitenrechte; keine Personenbewertung. |
| `votedir` | Letztes Wort durch direkte Volksabstimmungen bei wichtigen Sachfragen bleibt erhalten. |
| `cttresa` | Wichtigkeit gleicher Behandlung durch Gerichte; keine Gleichsetzung mit Vertrauen in heutige Gerichte. |
| `gptpelc` | Wahlreaktion auf schlechte Regierungsarbeit; keine bestimmte Partei zugeordnet. |
| `gvctzpv` | Schutz aller Bürger vor Armut ausdrücklich als Demokratieprinzip. |
| `grdfinc` | Demokratieprinzip; ausdrücklich von Zustimmung zur staatlichen Maßnahme `gincdif` getrennt. |
| `viepol` | Vorrang der genannten Ansichten im Demokratiekontext; keine Zuschreibung „populistisch“ an Personen. |
| `wpestop` | „Immer“ bleibt erhalten; allgemeine Eigenschaft der Person ausdrücklich ausgeschlossen. |
| `scchpldm` | Beide Regierungsreaktionen im Mehrheitskonflikt; fehlende Anschlussfragen benannt. |
| `bplcdc` | Empfundenes Pflichtausmaß trotz eigenem Widerspruch; keine behauptete rechtliche Pflicht. |
| `dpcstrb` | Pflichtausmaß trotz missbilligter Behandlung; nicht mit der vorigen Frage verschmolzen. |
| `hrshsnta` | Wesentlich härtere Strafen gegenüber historischem Kontext; Zeitbasis ausdrücklich geklärt. |
| `dbctvrd` | Zustimmung zur Aussage über Akzeptanz abschließender Gerichtsurteile; keine moralische Personenbenennung. |
| `lwstrob` | Zustimmung zur Aussage über strikte Befolgung aller Gesetze. |
| `rgbrklw` | Genannter Ausnahmefall, Gesetzesbruch um das Richtige zu tun; kein Urteil darüber, was richtig ist. |
| `vteurmmb` | Hypothetisches Referendum; leere/ungültige Stimmzettel, Nichtwahl und fehlende Berechtigung bleiben getrennt. |
| `keydec` | Nationale statt EU-Entscheidungen als Demokratieprinzip; Ablauf bleibt B12, Ergebnisrubrik ist EU. |
| `euftf` | Eigenständige Richtung europäischer Einigung; keine Verrechnung mit Mitgliedschaft. |
| `inctxff` | Unterstützung der genannten Abgabenerhöhung auf fossile Brennstoffe. |
| `sbsrnen` | Unterstützung öffentlicher Gelder für die genannten erneuerbaren Energiequellen. |
| `banhhap` | Unterstützung des konkreten gesetzlichen Verkaufsverbots; keine Bewertung von Gerätekäufen der Person. |
| `imsmetn` | Gleiche Gruppe als historische Originalformulierung; keine Rassismus-/Moralbenennung der Person. |
| `imdfetn` | Andere Gruppe bleibt erhalten; tatsächliche Zuwanderungsfolgen werden nicht behauptet. |
| `impcntr` | Herkunft aus ärmeren Ländern außerhalb Europas bleibt der konkrete Gegenstand. |
| `imsclbn` | Konkrete nominale Anspruchsbedingungen; Aufenthalt, Arbeit/Steuern und Staatsbürgerschaft nicht in einen Zeitwert umgerechnet. |
| `eqparep` | Konkretes Gesetz zur gleichen Sitzverteilung zwischen Frauen und Männern; kein allgemeines Gleichstellungsetikett. |
| `eqparlv` | Gesetzliche Verpflichtung, gleich lange bezahlte Elternzeit im genannten Szenario; vollständiger Kontext enthält Vollzeit, ungefähr gleichen Verdienst, Neugeborenes und Anspruch beider Eltern. |
| `freinsw` | Kündigung im konkret genannten Arbeitskontext; keine allgemeine Aussage über Meinungsfreiheit oder Personentypen. |
| `fineqpy` | Unternehmensgeldstrafe, wenn Männer bei gleicher Arbeit besser bezahlt werden; Absatz wahrt die Richtung des Originals. |
| `wrkprbf` | Zusätzliche Leistungen für berufstätige Eltern mit genannter Steuerfolge; vollständige Frage enthält deutlich höhere Steuern für alle. |

Es gibt 43 passende Einträge im `meanings`-Objekt, keine fehlende oder zusätzliche Zuordnung. Der Code leitet keine Parteiposition, moralische Personenbenennung oder Gesamtwertung ab. Das bedeutet nicht, dass Wortwahl, Itemauswahl oder Themenabdeckung empirisch politisch fair geprüft wurden.

## Antwortzustände, Navigation und Vollständigkeit

Die drei Zustände sind `untouched`, `answered` und `skipped`. Fortgang ohne Auswahl lässt ein Item unberührt. Radioauswahl setzt es auf beantwortet. Überspringen ersetzt eine vorherige Auswahl und kann „Keine Angabe“, „Weiß nicht“ oder „Keine Antwort geben“ erhalten. Wiederbeantwortung ersetzt den Skip-Zustand. Diese Gründe werden keinem originalen Missing-Code gleichgesetzt (`index.html:50–64`, `prototype.js:76–80`, `:258–278`, `:355–363`).

Die nominalen EU-Kategorien „leerer Stimmzettel“, „ungültig wählen“, „nicht wählen“ und „nicht stimmberechtigt“ zählen als gewählte Originalkategorien, nicht als unbekannte Antwort oder Überspringen. `imsclbn` bleibt nominal. Die Zahl `categoryIndex` bezeichnet allein die Listenposition. Der Code vergibt daraus keine Punkte.

Die Übersicht enthält alle 43 Items mit Zustand und Direktzugang. Rücksprung, nächste Frage, Bearbeitung eines Ergebnisitems und frühzeitiger Wechsel in den Ergebnisentwurf sind möglich. Die letzte Frage nennt „Zum Ergebnisentwurf“. Auch eine unvollständige Sitzung zeigt alle 43 Ergebnisartikel, verteilt auf acht besetzte Themenrubriken. Die Rubriken erklären ausdrücklich, dass sie keine bestätigten Dimensionen sind und keinen gemeinsamen Score erhalten (`:329–344`). „Wirtschaft und Verteilung“ und „Demokratie und politische Autorität“ sind ausdrücklich enthalten. Diese Struktur belegt keine vollständige Abdeckung aller deutschen politischen Themen.

## Datenschutz und Textrenderung

Im geprüften JavaScript halten die Map und die aktive DOM-Darstellung die flüchtige Sitzung. Es gibt keine Storage-, Cookie-, Export-, Fetch-, Beacon-, WebSocket- oder URL-Antwortlogik. Die Browser-Neuinitialisierung wird in der reinen Probe durch einen frischen Skriptkontext ersetzt; dieser beginnt wieder mit 43 unberührten Items. Es wurde kein echter Reload beobachtet.

Die CSP nennt `connect-src 'none'`, `form-action 'none'`, lokale Skripte/Styles/Schrift und keine Bilder (`index.html:6`). `no-referrer` und `noopener noreferrer` stehen an den vorgesehenen Stellen. Quellenlinks entstehen aus den gebundenen öffentlichen URLs mit Seitenfragment; Antworten gehen nicht in Linkparameter ein. Absichtliche externe Quellennavigation ist damit nicht gleichbedeutend mit Übertragung der Antworten. Die Schriftdatei liegt lokal.

Dynamischer Text nutzt `textContent` und `createTextNode` (`prototype.js:85–107`), keine HTML-Parser-Sinks. Die kleine Markup-Probe erzeugte aus einem `<img>`-/`<script>`-ähnlichen Text keine Kindelemente. Die Linkfunktion verwirft ein `javascript:`-Ziel. Im Testkontext wurden keine gesperrten Network-/Storage-APIs angesprochen. Diese Evidenz betrifft die konkrete Codefassung. Browser-CSP-Durchsetzung, echte Netzwerkmitschnitte und Speichervorgänge des Browsers wurden nicht geprüft.

`source-binding.json` und `catalogue.js` nennen denselben Ursprungshash. Itemzahl, Themenmenge und die zwei Schriftpins stimmen lokal überein. Die bezeichnete Ursprungsdatei und das ursprüngliche Stylesheet liegen außerhalb der erlaubten Manifestartefakte und wurden nicht geöffnet. Die Aussagen `responseDataRead: false` und `networkRetrievals: false` sind lokale Bindungsangaben des Erstellers; dieser Review-Lauf beweist damit nicht rückwirkend dessen Arbeitsablauf. Quellen-/Datenidentität, Rohdatenabwesenheit im gesamten Repository und Quellenlizenzgültigkeit sind nicht durch die UI bewiesen.

## Konkrete Handbuchgrenzen

Das vollständige Handbuch ist Maßstab, aber der aktuelle Auftrag erlaubt einen unveröffentlichten lokalen Gestaltungsentwurf. `handbuch.md:146` und `:377` lassen Test- und Ergebnisgestaltung ausdrücklich offen. Deshalb wird aus diesem Review keine neue Handbuchregel und keine Designfreigabe abgeleitet.

Im Code eingehalten: bestehende Papier-/Tintenfarben, lokale Libre Baskerville, prozentuale Grundschrift, vorhandenes Raster und Umbruchpunkte, keine Gemälde, keine Antwort-/Ergebnisfarben von Parteien oder Flaggen, keine Animationen, eindeutiger Entwurfsstatus und die Standardformel zur fehlenden Validierung. Ein H1, deutsch benannte Navigation, Fieldset/Legend, sichtbare Fokusregeln und 48-px-Antwortzeilen sind vorhanden. Ob Fokus, Kontrast und Größen tatsächlich korrekt erscheinen, bleibt Browserarbeit.

Für eine spätere Integration bleiben konkrete Abweichungen offen: Wortmarke ohne Flagge/Startseitenlink (`index.html:16` gegenüber Handbuch 2), eigene Entwurfsstatuszeile statt regulärer Statusleiste (`:17–18` gegenüber Handbuch 5/7.7), helle reduzierte Fußzeile statt regulärer Hülle (`:85–90`), Vanilla-Modul statt Angular-Hülle (Handbuch 9), Primärschaltfläche zur nächsten Einzelansicht statt ausschließlich zu einer anderen Seite (Handbuch 5), fehlende Meta-Beschreibung (Handbuch 7.6), „ESS“ vor ausgeschriebenem ersten Vorkommen (Handbuch 7.3). Die offiziellen Originaltexte enthalten Sie-Anrede, Listen- und Interviewanweisungen. Das ist gekennzeichneter Originalkontext, keine neue Werbeansprache; ein automatischer unslop-Umschrieb dieser Formulierungen wäre falsch.

Die Fußzeile enthält die Standardformel und den institutionellen Pflichttext wortgleich (`index.html:86–87`). Der genaue LIFE-93-Phase-6-Ergebnishinweis steht nicht als Vergleichsvorlage im erlaubten Paket. Seine Wortgleichheit wurde daher nicht bestätigt. Die vorstehenden Integrations- und Stilfragen sind keine Forschungsblocker dieses lokalen Vorschlags. Sie ersetzen auch keine spätere Human-Design-Entscheidung.

## Tatsächlich ausgeführte Prüfungen

`node outputs/loop/policy-ui-001-review/probe.cjs` endete mit Exitcode 0. Zwölf Prüfgruppen bestanden, keine Laufzeit-/Assertionsfehler. Die Probe nutzt nur Node-Standardmodule und ein eigenes minimales DOM-Modell. Sie prüfte alle 315 öffentlichen Antwortkategorien, keine Antworten realer Befragter.

| Prüfung | Ergebnis und Grenze |
| --- | --- |
| Äußerer Paketmanifest-Pin | Erwarteter SHA stimmt vor/nach. |
| Elf äußere Artefaktpins | 11/11 vor/nach richtig und unverändert. |
| Neun interne Dateipins | 8/9 richtig; `prepare.py` vor/nach falsch, PUI-R3. |
| Lokale Bindungsfelder | Ursprungshash-Angaben, 43 Items, Themenmenge, Schrift/Schriftlizenz konsistent. Ursprungsidentität nicht extern geprüft. |
| Katalogabhängigkeiten | 43 eindeutige IDs, 43 Erläuterungen, acht besetzte Rubriken; Studien und referenzierte HTTPS-Quellen/Seiten intern vorhanden. Keine Quellenabrufe. |
| Anfang und Sprunglink | 43 unberührte Items; erste Rückwärtsschaltfläche deaktiviert; Fokusaufruf auf Hauptinhalt. |
| B1–B12 | Reihenfolge, Zusammenhalt, Vorwärts-/Rückwärtslogik, gemeinsame Einleitung und anschließendes B25 bestanden. |
| Kategorien | Alle 315 Listenpositionen rendern und liefern dieselbe gewählte Beschriftung im Ergebnis. Das belegt Darstellung, nicht historische Transkriptionsrichtigkeit. |
| Nominale EU-Sonderkategorien | Alle vier als beantwortete Originalkategorien erhalten. |
| Zustände und Bearbeitung | Unberührter Fortgang, alle Skipgründe, Ersetzen einer Antwort, Wiederbeantworten und Rücksprünge bestanden. |
| B25 | Beide Auswahlfälle nehmen den offen bezeichneten neuen Fortgang. |
| Teilergebnis | Eine beantwortete, eine übersprungene und 41 unberührte Angaben ergeben 43 Artikel in acht Rubriken; keine Deutung ohne Antwort. |
| Skalenanker | Die 18 ordinalen 0–10-Listen enthalten vollständige Endanker; nominale Anspruchsbedingungen bleiben ohne numerische Auswertung. |
| Text und Links | Markup bleibt Text; nicht-HTTPS-Quellenziel abgewiesen. |
| Network/Storage | Keine solche API im Code oder während der synthetischen Proben; CSP-/Referrer-Angaben vorhanden. Keine Browser-Netzwerkbeobachtung. |
| Neuinitialisierung | Frischer Skriptkontext beginnt mit 43 unberührten Zuständen. Kein echter Browserreload. |

Der erste große Tool-Auszug war teilweise abgeschnitten; `prototype.js` und `foundation.css` wurden anschließend vollständig erneut gelesen. Kein fehlender Auszug wurde als geprüft behandelt.

Nicht ausgeführt: pnpm/CI/Build, Browser, native Radio-/Tastaturbedienung, tatsächlicher Fokus/Scroll, Screenreader, axe, Responsive-Ansicht/200-%-Zoom, Browser-CSP, reale Network-/Storage-Beobachtung, Verständnisprüfung, Quellen-Vollrecherche, Rohdatei-/CSV-/Header-/Privatdatenzugriff, Frequenz-/Antwort-/Partyabfrage, ESS-Analyse und empirische Äquivalenzprüfung. Es wird weder deren Bestehen noch deren Scheitern behauptet.

## Hashes und eigene Evidenz

Paketmanifest: `reports/loop/packages/POLICY-UI-001/v1/manifest.json`, SHA-256 `3b878b3202e2c99a8c0dd13b5369b50cee576564531c2a2eea6dc41e24db2ea2`. Der Nachlauf vor Berichtserstellung ist unter `pins-after.json` mit `2026-10-03T14:06:42.869976+00:00` festgehalten.

| Artefakt relativ zum Worktree | Tatsächlicher SHA-256, vor/nach identisch |
| --- | --- |
| `prototypes/policy-v2/assets/libre-baskerville-latin-wght-normal.woff2` | `22219fb90e3b9bd28debd1825fe8d9a0154a0e31f8b3fa601ac1a0a5aa5e6d1b` |
| `prototypes/policy-v2/assets/libre-baskerville-license.txt` | `8490e863633e537100d6d18755d994ea30b0b44741876a17809d28becf45ce11` |
| `prototypes/policy-v2/catalogue.js` | `3b897bad81058fbd525a1cf9fa04354f8d48ccc8ae5892e89496ad1552411785` |
| `prototypes/policy-v2/foundation.css` | `97853bc6912eaa3a722b0ea3707f61aca418a77a7f69ec602aaca9a4a60dceca` |
| `prototypes/policy-v2/index.html` | `1270f0c5faaeb3a1ba206f17c15a538206a475b3c9b4ca0332f4f7b6c69500f7` |
| `prototypes/policy-v2/manifest.json` | `8beaf71937ec09a50d2fe571453a1378b826d15fe39f985fa82727f001707b40` |
| `prototypes/policy-v2/prepare.py` | `5dda504d26142be720f060756c300c24e2c7a06e1b0f169b292e8f4ebfb41900` |
| `prototypes/policy-v2/prototype.css` | `f0c0fde17a0a882a6899dcd10a98fc33376a3a6bbc9faad18f9415c6320aff73` |
| `prototypes/policy-v2/prototype.js` | `1d56dbdc63cde53d3732c484bbb49c770a5b8fe295140d4290245faff14bea05` |
| `prototypes/policy-v2/source-binding.json` | `06a63a0672ec7f05020d50ceff6c47d2a2633d5d15f9d2bd6fe77492ae782245` |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |

Eigene Evidenz liegt ausschließlich in `outputs/loop/policy-ui-001-review/`:

| Datei | SHA-256 |
| --- | --- |
| `probe.cjs` | `4442d27916eb107ba63962275d257bfdb2046113684788e08f09f87f55abbfb1` |
| `probe-result.json` | `ead64ef5ef4a22c9e62d6b0afc3dce8c9b2dd2d673af5574905456550771a092` |
| `pins-before.json` | `b59ca4a1adc49d884ec6d8f05cf6e1c7f8005e77fde30dd14fc325e60dd1e313` |
| `pins-after.json` | `0535979416d98455760f265b2de104e49b28a98e8e07b3f2e00e7168f9710beb` |

Zur erneuten lokalen Prüfung reichen die beiden semantischen Korrekturen, ein konsistenter interner Pin und eine neu gepinnte Fassung. Browserbeobachtung, Human-Design-Freigabe, Quellen-/Datenidentität und empirische Fragen behalten ihren getrennten Status.
