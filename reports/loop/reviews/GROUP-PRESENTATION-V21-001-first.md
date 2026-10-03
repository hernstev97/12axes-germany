# Erstprüfung GROUP-PRESENTATION-V21-001

Urteil: `ACCEPTED_BOUNDED`.

Ich akzeptiere die konkrete öffentliche Darstellungsübertragung in diesem Paket. Sie übernimmt die festgeschriebenen historischen Einzel- und Gruppenreferenzen korrekt und hält ihre Grenzen sichtbar. Es gibt keinen schweren Befund, der ein betroffenes Darstellungsartefakt blockiert. Dieses Urteil erteilt keine neue Ergebnis-, Rohdaten-, Methoden-, Neutralitäts-, Menschen-, Design- oder Releasefreigabe.

## Prüffassung und Unabhängigkeit

- Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`.
- Zugewiesener Branch: `research/life-93-night-20261003`. Keine Git-Aktion zur Prüfung oder Veränderung des Branches.
- Paket: `reports/loop/packages/GROUP-PRESENTATION-V21-001/v1/manifest.json`.
- Manifest-SHA256: `d95b3522fe1e16a82d093f74d79f85a4e89e93de484f188970e611d2d1ecc914`.
- Alle 86 öffentlichen Pins stimmten vor und nach der Prüfung. Die Schlussprüfung bestätigte reguläre Dateien ohne Symlink-Komponenten. Es entstand keine Verzeichniskopie.
- `AGENTS.md`, `docs/project.md` und `docs/handbuch.md` vollständig gelesen. Zusätzlich die benötigten festgeschriebenen Verträge, öffentlichen Referenzen, Implementierungen, Tests, Statusdateien, Lizenzakte und den Breitennachtrag geprüft. „unslop“ auf den eigenen Bericht angewandt.

Ich bin ein frischer normaler Codex-Prüfer dieses zusammengehörigen Darstellungs-/Berichtpakets. Keine zweite Rolle oder neues Gesamtaudit. Ich habe weder fremde Reviewerprosa noch Autorenberichte, Rootverteidigung, Zustand, Handoff, Arbeitsloophistorie oder Erinnerungsdateien gelesen. Die vier `upstreamReportBytesOnly`-Dateien wurden ausschließlich als Bytes gehasht. Auch der öffentliche Themenbericht 02 wurde hier nur gehasht, nicht als Urteil gelesen.

Historische Entscheidungs-JSON, Rootexport und alte Manifeste wurden nur für deklarierte Hash-, Identitäts- und Paarbindungen verarbeitet. Die enthaltenen Urteilsstrings begründen kein neues unabhängiges Ergebnisurteil. Keine darin genannte Rohdaten-, Privataggregat- oder Outputdatei wurde verfolgt. Kein Netzwerk, Claude, Authzugriff, Rohdatenlauf oder neuer Ergebnisexport.

Alle beteiligten KI-Rollen einschließlich dieses Prüfers gehören zur Codex-Modellfamilie. Frischer Kontext reduziert die Übernahme fremder Urteile, beseitigt gemeinsame mögliche Fehler aber nicht. Agentenübereinstimmung und synthetische Tests ersetzen keine empirische Evidenz oder menschliche Abnahme.

## Befunde mit konkreten Belegen

### GPV21-01 – Geschlossene Authentisierung und genaue Übertragung bestanden

`group-reference-generator.mjs:66` authentisiert genau 13 feste öffentliche Inputs. Die Projektion öffnet keine von JSON gelieferte Pfadangabe. Das eigene Orakel verglich alle drei öffentlichen Gruppen-JSONs mit der Projektion: Studien-/Ausgabeidentität, Feldzeiten, DOI, Attribution, Lizenzkennungen, Gruppencode und Labels, Reihenfolge sowie jedes vollständige Fragen-/Referenzobjekt stimmen überein. Die Ausgabe ist zusätzlich bytegleich zur eingecheckten TypeScript-Datei.

Die 13 einzeln veränderten Byteinputs wurden sämtlich mit SHA256-Fehler verworfen. Ein zusätzlicher sowie ein fehlender Input scheiterten an der geschlossenen Eingabemenge. Fremde Urteilsstrings können die festgeschriebenen Originalbytes nicht ersetzen. Die beiden historischen Ergebnisfassungen und ihre verschiedenen Manifestbindungen werden technisch verbunden, ohne das Quellenurteil als neues Urteil auszugeben.

Belege: `web/src/app/policy-draft/group-reference-generator.mjs:78`, `:260`, `:320`; eigenes `outputs/loop/group-presentation-review/independent-projection.json`; beide Adapter-`--check`-Aufrufe.

### GPV21-02 – Vollständiger Bestand, Nulls und Originalkategorien bestanden

ESS5/8/9 behalten 8/9/9 Gruppen. Keine benannte Partei und kein Other wird entfernt oder nach veröffentlichter Verfügbarkeit umsortiert. Die historischen Codes bleiben studienspezifisch, etwa SPD als ESS5-Code 1 und CDU/CSU als ESS8/9-Code 1. Other bleibt heterogen und ohne konkrete Parteizuordnung.

Alle 174 Gruppen-/Fragepaare sind vorhanden. 63 haben veröffentlichte Referenzen, 111 bleiben `null`. Die 63 Referenzen enthalten zusammen 337 Originalkategorieanteile, darunter sechs echte Nullkategorien. Diese Nullkategorien bleiben erhalten. Zurückgehaltene Paare enthalten ausschließlich ID, Status und `reference: null`, keine kleine Basis, Anteile oder Gewichtssummen. Der eigene Lauf prüfte alle 174 Zustände und für jede der 26 Gruppen die Trennung zu einer fremden Studie.

Belege: die drei `data/reference-groups-v21/*.json`; `group-reference-generator.mjs:234`, `:260`, `:273`, `:299`; `group-reference.ts:30`; `policy-draft.html:261`, `:499`. Die 26 Berichtstests vergleichen außerdem die gesamte aktuelle öffentliche Tabellenübertragung mit einem separaten Decimal-Orakel.

### GPV21-03 – Nenner und Fallzahlen bestanden, ursprüngliche Zellprüfung hier offen

Die Projektion und der Bericht übernehmen `pspwght`, gültige ungewichtete Fragefallzahl, Gesamtbasis, Missing und Nichtgestellt unverändert. Die Zählungen summieren sich zur Gesamtbasis; Kategoriecodes folgen der jeweiligen Originalordnung. Anteile werden weder über Fragen oder Studien gepoolt noch nach Anzeige-Rundung auf 100 Prozent umgerechnet. Der gültige gewichtete Frage-Nenner bleibt von der ungewichteten Gruppenbasis getrennt.

Der Gruppenbericht zeigt sechs Nachkommastellen und benennt dies ausdrücklich als Formatierung ohne Präzisionsnachweis. Die Oberfläche rundet auf höchstens eine Nachkommastelle. In den aktuellen Gruppenreferenzen wird dadurch kein positiver Anteil zu null gerundet. `uncertainty: null` bedeutet ausdrücklich fehlende Standardfehler und Konfidenzintervalle. Fehlende Referenz bedeutet weder null Prozent noch Mitte.

Die öffentliche Ableitung enthält keine ursprünglichen positiven Zellcounts. Die Fünferregel konnte hier daher nicht empirisch nachgeprüft werden. Der Bericht benennt diesen Vorbehalt selbst. Die 100/5-Grenzen bleiben Darstellungsheuristiken und werden nicht als Präzisions- oder Anonymitätsvalidierung ausgegeben.

Belege: `pipeline/policy_group_report_v21.py:172`, `:191`; `policy-draft.html:469`, `:480`; Gruppenbericht 03, Absätze zu Nenner, 100/5-Regel und Unsicherheit.

### GPV21-04 – Historische Quelle, politische Zuordnung und Rechte bestanden im Übertragungsumfang

Wahl- und Antwortzeiten bleiben getrennt: ESS5 erinnert September 2009 bei Feldzeit 15. September 2010 bis 3. Februar 2011; ESS8 erinnert September 2013 bei Feldzeit 23. August 2016 bis 26. März 2017; ESS9 erinnert September 2017 bei Feldzeit 29. August 2018 bis 4. März 2019. Die Darstellung ordnet politische Antworten der späteren Befragung zu, nicht dem Wahltag, aktuellen Parteiprogrammen oder extern verifizierter Stimmabgabe.

Die Bevölkerung ab 15 Jahren in Privathaushalten wird nicht als verifizierte Wahlbevölkerung ausgegeben. Die fehlende Erfassung Münchens in ESS8 bleibt ausdrücklich sichtbar. Ebenso die schwächere ESS5/8-Zweitstimmenbindung anhand geordneter Originalfragen und API-Labels gegenüber dem ausdrücklichen ESS9-Appendixtext auf PDF-Seite 21. Druckcode `01` und API-/Dateicode `1` in ESS9 bleiben verschieden; Other erhält seinen gesonderten Druckcode. Eine allgemeine numerische Umcodierung wird nicht behauptet. ESS10-SC und ESS11 erhalten keine Gruppenfreigabe.

Die Quellenansicht und der Bericht behalten ESS ERIC/Sikt, Studienausgaben, Daten-/Dokumentations-DOI, Originalbelege und Änderungskennzeichnung. Daten unter CC BY-NC-SA 4.0 und Dokumentation unter CC BY-SA 4.0 bleiben getrennt; Softwarelizenz, Quellenangabe und Forschungssicherung verleihen keine kommerzielle oder Produktfreigabe. Das ist eine Prüfung der gebundenen Darstellung, keine neue rechtsfachliche Beurteilung oder Onlineprüfung der Quellen.

Belege: `policy-draft.html:249`, `:274`, `:280`, `:299`; `data/gruppenvertrag.v2.1.entwurf.json`, `sourceRights` und `boundaries`; `data/reference-groups-v21/README.md`; `docs/lizenzen.md`; Gruppenbericht 03, Studien- und Quellenabschnitte.

### GPV21-05 – Breite, Bedeutung und politische Fairness bestanden im begrenzten Darstellungsumfang

Der Quellkatalog und seine Projektion enthalten 43 Originalfragen mit 315 gültigen Kategoriebindungen. Die acht Rubriken umfassen 5/5/12/6/3/3/4/5 Fragen in der deklarierten Rubrikreihenfolge. Wirtschaft/Verteilung und Demokratie/politische Autorität sind ausdrücklich enthalten. Originalkontexte, Demokratiefolge B1–B12, Familien-/Elternzeitszenario, gedruckte Kategorien und API-Codes bleiben in der UI nachvollziehbar. Der neue B25-Nachlauf wird als veränderte Durchführung mit fehlenden Anschlussfragen gekennzeichnet.

Die 42 öffentlichen Einzelreferenzen bleiben unabhängig von der optionalen Gruppenwahl. `ESS10SCe03_2:cttresa` bleibt ohne Zahlen. Rubriken erhalten keinen gemeinsamen Wert und werden nicht als latente Dimensionen ausgegeben. Die Erklärtexte beschreiben die jeweilige Originalaussage ohne Personenetikett, Links-/Rechtswert, Parteimatch oder Wahlempfehlung. Alle historischen Originalgruppen haben dieselbe Auswahlmöglichkeit und Darstellung. Unveröffentlichte Paare werden als fehlende Grundlage erklärt, nicht als schwache oder mittlere politische Position.

Die öffentlichen Statusdateien in `app.html`, `home.html`, `project.html` samt `project.ts` und `methodology.html` stimmen im geprüften Umfang mit den öffentlichen Forschungsartefakten überein. Der Test bleibt öffentlich nicht verfügbar. Inhaltslücken, Menschenprüfung, Test-/Ergebnisgestaltung, Claude-Schlusskontrolle und Veröffentlichung bleiben offen. Die Aussagen über frühere Ergebnisprüfungen wurden hier nur anhand festgeschriebener Herkunfts- und Paarmetadaten geprüft.

Das ist kein Neutralitätsnachweis und keine neue vollständige Quellen-/Konstrukt- oder Auswahlprüfung. Der breite Entwurf wird nicht allein aufgrund seiner Fragezahl als umfassend fertig erklärt.

Belege: `verify-public-catalogue.mjs`; `policy-catalogue.ts`; `item-meanings.ts`; `policy-source-details.html`; `policy-draft.html:172`, `:243`; die vier genannten öffentlichen Statusbereiche.

### GPV21-06 – Bedienzustände und Produktionsgrenze technisch bestanden

Die Studie und danach ihre Vergleichsgruppe werden über native beschriftete Selects gewählt. Initial bleibt beides leer, die Gruppe ist ohne Studie deaktiviert. Ein Studienwechsel setzt die Gruppe zurück. Bearbeiten und Rückkehr zum Ergebnis erhalten Antworten und Vergleichswahl, ein neuer Komponentenmount beginnt ohne Antworten und Wahl. Radioauswahl, Überspringen und Unberührt bleiben getrennt. Gruppenwahl löst keine politische Antwort oder Parteizuweisung aus.

Die 47 gezielten Angular-Tests bestanden einschließlich Originalkontext, Einzelreferenzen, verworfenen Gruppenclones, Auswahl/Reset, Bearbeiten, Ergebnisrückkehr und Remount. Storage-, Fetch- und URL-Beobachtungen prüfen die RAM-Grenze technisch im Testdom. Das eigene Runtime-Orakel verwarf vier fremde/gekoppelte Clone-/Proxy-Eingaben, ohne deren Felder lesen zu müssen, und bestätigte die tiefe Gefrierung des echten Gruppenmoduls.

Der separat erzeugte Produktionsbuild enthält sechs JavaScript-Dateien ohne Forschungsroute, Gruppenauswahltexte, Gruppenreferenzstatus oder ausgewählte Forschungsfragekennung. Die Produktionsroute ist leer; nur die ausdrückliche Research-Konfiguration ersetzt sie durch `/forschungsentwurf`. Dieser Build und die Testdom-Beobachtungen sind keine echte Browser-, Tastatur-, Layout- oder Barrierefreiheitsabnahme.

Belege: `policy-draft.ts:186`; `policy-draft.html:209`; `group-reference.ts:14`; `research-preview.routes.ts`, `research-preview.routes.dev.ts`, `web/angular.json`; eigene `runtime-oracle.json` und `production-isolation.json` im QA-Ordner.

## Ausgeführte Prüfungen

- Vor-/Nachauthentisierung des Manifests und aller 86 öffentlichen Pins: bestanden.
- `node web/src/app/policy-draft/group-reference-generator.mjs --check`: bestanden, 3 Studien, 26 Gruppen, 63 Referenzen, erzeugte Adapterbytes identisch.
- `node web/src/app/policy-draft/generate-reviewed-references.mjs --check`: bestanden, 42 unverändert übertragene Einzelreferenzen und explizites cttresa-Null.
- `node web/src/app/policy-draft/verify-public-catalogue.mjs`: bestanden, 43 Fragen und 315 gedruckte/API-Bindungen.
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build-policy-group-report-v21.py --check`: bestanden. Bericht-SHA256 `ecb731bc5caca8f554fd60be4f1176f021350b290d5dea2713fd4c0e48eed504`.
- `pipeline.tests.test_policy_group_report_v21` über `unittest` mit ausschließlich auf den eigenen QA-Ordner umgebogenem synthetischen Ausgabepfad: 26 Tests bestanden. Öffentliche aktuelle Werte-/Null-Übertragung, synthetische Negativfälle, Hash-, Pfad-, Symlink- und Fehlergrenzen getrennt geprüft.
- Angular `ng test --watch=false` mit genau `group-reference.spec.ts`, `policy-draft.spec.ts`, `historical-reference.spec.ts`, `policy-catalogue.spec.ts`: 4 Dateien, 47 Tests bestanden.
- Eigene reine JavaScript-Orakel gegen die tatsächlichen festgeschriebenen öffentlichen Module: alle 174 Paarzustände, 26 Fremdstudienfälle, vollständige öffentliche Projektion, 13 mutierte Pins, Zusatz-/Fehleingaben, vier fremde Clone-/Proxy-Eingaben und tiefe Gefrierung bestanden.
- `ng build --configuration production --output-path ../outputs/loop/group-presentation-review/production`: bestanden. Eigene Prüfung der sechs JavaScript-Ausgaben auf Forschungsroute/-inhalte bestanden.

## Nicht ausgeführte Prüfungen und verbleibende Grenzen

- Kein Rohdatenlauf, keine private Aggregatprüfung, keine Nachrechnung ursprünglicher Zellcounts, Gewichte oder empirischer Schätzer. Öffentliche Reproduktion prüft Darstellung und Herkunftsbytes.
- Keine Liveabfrage offizieller Quellen oder externer Links. Kein neues Quellen-, Rechts- oder Releaseurteil.
- Kein unveränderter Lauf von `group-reference-generator.test.mjs`: Eine Testmutation decodiert fremde Berichtbytes in UTF-8. Die eigene gleichwertige Hash-Negativprüfung verwendet `Buffer.concat` und liest keine Reviewerprosa.
- Kein breites `pnpm check`, das nicht benötigte und nicht freigegebene Review-/Repositorybereiche lesen könnte. Die paketbezogenen Tests und der isolierte Produktionsbuild sind oben vollständig aufgeführt. Der Koordinator führt übergreifende technische Checks getrennt durch.
- Kein eigener echter Browserlauf. Desktop-/Smartphone-Beobachtung, Tastatur, Fokus, reduzierte Bewegung, Zoom und axe bleiben beim Koordinator getrennt zu dokumentieren. Testdom und Build ersetzen das nicht.
- Kein menschlicher Verständnistest, keine Designabnahme, keine Claude-Schlusskontrolle und keine Veröffentlichung. Englische Metadatenstatus und die dichten Tabellen bleiben Gegenstände der Menschenprüfung; kein schwerer Übertragungsfehler folgt daraus.

Blocker für dieses konkrete Darstellungs-/Berichtpaket: keine. Die genannten offenen Abnahmen werden durch `ACCEPTED_BOUNDED` weder aufgehoben noch als bestanden gewertet. Diese Erstfassung bleibt nach Abschluss unverändert.
