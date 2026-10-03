# Erstprüfung FINAL-DOSSIER-HUMAN-V21-001/v1

Datum: 3. Oktober 2026. Rolle: normale sachliche Erstprüfung des Schlussdossiers und des Human-Zusatzes. Entscheidung: `ACCEPTED_BOUNDED`. Keine sachliche Änderungspflicht im geprüften Dokumentationsgegenstand; keine offenen blockierenden Findings.

Ich habe die beiden neuen Dokumente `docs/reproduktion-life93-v2.md` und `docs/claude-schlusskontrolle-v2.md` sowie `docs/verstaendnistest-v2.1.entwurf.md` geprüft. Der unveränderte `docs/verstaendnistest-v2.entwurf.md`, Entwurf 0.1, ist der Vertrag für die übernommenen Humanregeln. Diese Annahme betrifft die Vorbereitung und ihre Aussagen. Sie ist weder ein erfolgreich ausgeführter Reproduktionslauf noch eine methodische Gesamt-, Human-, Gestaltungs-, Rechts- oder Releaseabnahme.

## Kontext und Bindung

Der neue Prüfauftrag gab einen begrenzten Kontext vor. Ich habe keine Autorenverteidigung, keinen Rootstate oder Handoff und keine Prosa anderer Reviewer gelesen. Rollen, Entscheidungen und Wiederverwendung eines Quellenurteils in den gelisteten öffentlichen JSON-Dateien wurden ausschließlich als deklarierte Metadaten gelesen. Deren Berichtpfade und private Pfadstrings blieben Metadaten und wurden nicht geöffnet, geprüft oder verfolgt. Alle folgenden Aussagen beziehen sich auf das feste Paket und den Dokumentstand darin, nicht auf später fertiggestellte UI-Arbeit.

Manifest: `reports/loop/packages/FINAL-DOSSIER-HUMAN-V21-001/v1/manifest.json`, SHA256 `6c63a6c53a86169c4dcd921349ad7d671a0fcd7a09f3ec58d2bc4a251223733c`. Alle 40 gelisteten öffentlichen Dateien wurden zu Beginn und nach der Sachprüfung tatsächlich gehasht. Beide Prüfungen ergaben 40/40 Übereinstimmungen; der Manifesthash blieb gleich. Die vollständigen aktuellen Hashes stehen in `outputs/loop/final-dossier-human-review/pins-before.json` und `pins-after.json`.

| Hauptartefakt | Tatsächlicher SHA256 vor und nach der Prüfung |
| --- | --- |
| `docs/reproduktion-life93-v2.md` | `d2fcd882085cccac2c5a3fcc0f192b421c54f8b8bf07f4a8e8b553e428151efe` |
| `docs/claude-schlusskontrolle-v2.md` | `e7892c5eeacb3f8a5c0be43310496739afe390284b0d8cfce8204fde97dcb67f` |
| `docs/verstaendnistest-v2.1.entwurf.md` | `3bcbb52603058146b050afdb417e7b0803ae3652e3cab769cec3c7ed31fa4d47` |
| Humanvertrag `docs/verstaendnistest-v2.entwurf.md` | `deaf970f15970f3bd68a3bd0494c5a304e611c491a79950ddfaa642e95e85a68` |

Die Prüfung stammt aus derselben Codex-Modellfamilie wie die übrigen deklarierten Rollen. Getrennte Aufgaben und ein frischer begrenzter Kontext schließen gemeinsame Fehler nicht aus. Meine Annahme und Übereinstimmung anderer Rollen belegen keine politische Neutralität oder externe Fachvalidierung.

## Durchgeführt

- Vollständige Lektüre der drei Prüfgegenstände und des Humanvertrags 0.1; sachlicher Abgleich mit den relevanten Abschnitten der gelisteten Auftrags-, Plan-, Abdeckungs-, Handbuch- und Lizenzdateien.
- Statische Lektüre der beiden CLI-Runner, der beiden Zugriffshüllen und des öffentlichen Berichtbuilders. Die festen Runnerparameter wurden zusätzlich ohne Import oder Ausführung per AST ausgelesen und mit den tatsächlich gehashten Freeze-Metadaten verglichen.
- Abgleich von Zeiten, Studienumfang, Plan-/Commit-/Hashbindungen, deklarierten Zugriffsgrenzen und Exportentscheidungen anhand der gelisteten öffentlichen JSON-Dateien.
- Abgleich aller fünf öffentlichen Einzel- und drei öffentlichen Gruppenexporte mit den in den Rootentscheidungen deklarierten Dateihashes, Kandidaten- und Reviewmanifest-Metadaten, zugelassenen IDs beziehungsweise Paaren und vollständiger Gruppenreihenfolge. Gezählt wurden öffentliche Inventare und Freigabe-IDs; Anteile oder private Zahlen wurden nicht neu berechnet.
- Auszählen der `outputs/`-Metadaten im 51-Pin-Gruppenmanifest und der Quellenmetadaten im Fragenkatalog. Keine der dort benannten Originalcachedateien wurde geöffnet.
- Formulierung des eigenen Berichts nach dem gelesenen `unslop`-Skill. Gemeinsame Dokumente, Code, Zustand, Manifest und Originale wurden nicht verändert.

Der maschinenlesbare Abgleich steht in `outputs/loop/final-dossier-human-review/public-metadata-and-static-checks.json`.

## Sachbefunde mit Kennungen

Die folgenden Kennungen dokumentieren geprüfte Sachpunkte. Sie sind keine Fehlerkennungen; aus ihnen entsteht keine Änderungspflicht.

### FDH-001: Laufstand, Zeit und Veröffentlichung bleiben getrennt

`docs/reproduktion-life93-v2.md:3–11` nennt seinen datierten WIP-Stand, die spätere Gruppenentscheidung und die früheren Bibliotheksläufe getrennt. Die fünf Einzelreceipts reichen tatsächlich von `2026-10-03T14:25:06.762321+00:00` bis `14:25:18.739475+00:00`; die drei Gruppenreceipts von `15:24:22.211025+00:00` bis `15:24:28.088629+00:00`. Alle enthalten Exitcode 0. Das sind öffentliche Laufmetadaten, kein von mir beobachteter Datenlauf. Die Einzelentscheidung ist auf `14:39:28.054249+00:00`, die Gruppenentscheidung auf `15:54:40.395473+00:00` datiert. Frühere `pending`-Status in Receipts und Zugriffserklärungen werden im Dossier nicht zur Behauptung fehlender späterer Exporte umgedeutet.

### FDH-002: Reproduktionsparameter und lokale Eingaben sind konkret gebunden

Die in `docs/reproduktion-life93-v2.md:17–24` genannten 22- und 51-Pin-Manifeste, Freezehashes, Vertragsbindungen und Commits passen zu den festen `PINS` in `scripts/run-policy-v2.py:19–24` und `scripts/run-policy-groups-v21.py:19–26`. Der statische AST-Abgleich ergibt für beide vollständige Übereinstimmung mit den Freeze-Metadaten. Die dargestellten Editions-/Eingabepfade stimmen mit dem öffentlichen Analysevertrag und `pipeline/policy_access_v2.py:45–51` überein. Diese Pfade wurden nur als veröffentlichte Metadaten gelesen.

Das Gruppenmanifest enthält genau 51 Artefakte, darunter genau 36 `outputs/`-Einträge. Der Hinweis auf alle 36 lokalen öffentlichen Voraussetzungen ist deshalb sachlich richtig. `pipeline/policy_group_access_v21.py:288–338,341–414` bindet Quellen und prüft die Manifestartefakte vor Rohzugriff. Die dokumentarischen ESS10/ESS11-Bindungen erweitern weder die drei CLI-Studien noch die Gate-Liste. Das Dossier stellt die Caches als gesondert bereitzustellende Originalbytes dar und behauptet keinen automatischen Download oder vollständige Eingaben in einem Gitclone. Deren tatsächliche Präsenz, Ignorezustand und Originalbytes habe ich nicht geprüft.

### FDH-003: CLI-Anleitung beschreibt einen künftigen Lauf

`docs/reproduktion-life93-v2.md:58–83` stimmt mit den gebundenen Runnern überein. `--study` ist Pflicht. Der Einzelrunner erlaubt fünf Studien und `all`; der Gruppenrunner nur ESS5e03_6, ESS8e02_3, ESS9e03_3 und `all`. `all` ruft die Studien einzeln auf. Nach der Argumentverarbeitung prüfen beide Runner die lokalen und entfernten Plantagbindungen mittels Git, weshalb ein wirklicher Datenlauf Git und Zugang zum konfigurierten `origin` benötigt. Die Wrapper weisen bereits vorhandene ausgewählte private `run.json` mit `existing_private_run_use_fresh_checkout` ab. Die beschriebenen Berechtigungen 0700/0600 stehen in den Zugriffshüllen.

Das Dossier erklärt ausdrücklich, dass der alte Plantag allein die später ergänzten CLI-Dateien nicht liefert und ein geeigneter vollständiger Forschungssnapshot samt lokalen Eingaben erforderlich ist. Es erklärt den erfolgreichen Fresh-checkout-CLI-Lauf ausdrücklich für noch nicht durchgeführt. Hilfeausgabe, synthetische Prüfung und Bibliotheksreceipts werden nicht als Ersatz ausgegeben. Ich habe keinen dieser Läufe wiederholt. Insbesondere habe ich auch `--help` nicht ausgeführt: Das Laden der Gruppenhülle hasht weitere öffentliche Bibliotheken außerhalb der 40-Dateien-Grenze. Die statische Parameterprüfung genügt für diesen optionalen Sachpunkt. Die berichtete historische Help-Ausführung und Pythonversion habe ich nicht unabhängig beobachtet; das ist kein alleiniger Dokumentationsblocker.

### FDH-004: Öffentliche Exportbehauptungen entsprechen den vorhandenen öffentlichen Bindungen

Die fünf tatsächlich gehashten Einzeldateien enthalten 6/10/4/16/6 nichtleere Referenzen; ihre freigegebenen Frage-ID-Mengen passen zu den deklarierten Rootentscheidungen. `ESS10SCe03_2:cttresa` ist die verbleibende Nullreferenz. Die drei Gruppendateien enthalten genau die 21/30/12 zugelassenen nichtleeren Frage-Gruppen-Paare. Ihre gesamten Gruppenreihenfolgen passen zum Gruppenvertrag, einschließlich Other und aller 8/9/9 deklarierten Gruppen. Kandidatenhash und Reviewmanifesthash passen als Metadaten zur jeweiligen Entscheidung. Private Kandidatenbytes wurden dabei nicht geprüft.

`docs/reproduktion-life93-v2.md:85–99` unterscheidet diese begrenzten öffentlichen Freigaben von UI, neuem privatem Lauf und erneutem Export. Die Beschreibung von GR21-M-001 und der begrenzten Wiederverwendung des Quellenurteils passt zur deklarierten `sourceFirstReuse` und zum gelisteten Ergebnismanifest v2 mit `targetedFindingIds: ["GR21-M-001"]`. Ich bestätige damit die konsistente Wiedergabe der Entscheidung, nicht den Inhalt anderer Reviewerberichte oder die private Ergebnisprüfung.

Der Berichtbuilder akzeptiert statisch ausschließlich keine Argumente oder `--check`; mit `--check` vergleicht er Bytes, ohne das Ziel zu schreiben. Seine Quellenliste stammt aus dem Katalog mit genau 30 Quellenmetadaten. Das Dossier nennt diese zusätzlichen Caches und Methoden-/Review-/Entscheidungsbytes und begrenzt den Bytevergleich auf die öffentliche Darstellung. Ich habe den Builder und den außerhalb dieses Pakets liegenden thematischen Bericht nicht ausgeführt beziehungsweise gelesen.

### FDH-005: Claude-Checkliste bleibt Vorbereitung

`docs/claude-schlusskontrolle-v2.md:3,11,39–50` bezeichnet sich als datierte Checkliste, verlangt einen tatsächlich gesicherten späteren UI-/Dateistand, schließt private Daten aus und überlässt die Veranlassung Steven. Sie startet oder legitimiert keine Verbindung, Anmeldung, Einrichtung, Ausführung oder ein Urteil. Die Prüfpunkte trennen historische Kategorienanteile, gruppenkonditionale Nenner, Gewichtssensitivität, fehlende Unsicherheit, Missing und Modus-/Kontextübertragung. Die Rollenbegrenzung steht ausdrücklich in Zeile 35. Der Hinweis in Zeile 17 auf Roots private Pinprüfung bleibt eine Wiedergabe deklarierter Metadaten, keine Prüfung durch diesen Agenten.

Das Dokument bindet menschliches Verständnis, Fokus, echten 200%-Zoom, konkrete Gestaltung, Rechte und persönlichen Release als offene Voraussetzungen. Sein Verweis auf den alten Humanplan verlangt für Gruppenanzeigen noch die ergänzten Erinnerungs-/Nennerpunkte. Der neue Zusatz legt genau diese Ergänzung vor; die später gemeinsam gebundene Fassung ist weiter offen. Ein zusätzlicher Link wäre redaktionell nützlich, aber kein sachlicher Blocker.

### FDH-006: Neue Humanfragen erklären Gruppen und Nenner ohne neue Wertung

`docs/verstaendnistest-v2.1.entwurf.md:13–27` erhält F1, F3, F5 und F6 und ergänzt F2/F4 vor der ersten Person. Der F2-Schlüssel unterscheidet `pspwght`-Nenner und ungewichtetes gültiges N, dieselbe historische Studie, ausgewählte Gruppe und gültige Antworten genau dieser Frage. Das passt zu `questionDenominators` und `eligibilityAccounting` im Gruppenvertrag. Der Zusatz verwechselt Befragungszeit nicht mit Wahltag und behandelt die Gruppenzuordnung als erinnerte Zweitstimme. F4 schließt aktuelle Norm, Parteiprogramm, persönliche Parteizuschreibung, Match, Pooling und Unsicherheitsfreiheit aus.

H3/H4 werden vorab als neue Kennungen festgelegt. Unterschiedliche konkrete Fehler unter derselben Kennung werden ausdrücklich nicht allein wegen der Kennung zusammengezählt. Die beratungsfreie Ansicht, heterogenes Other, fehlende Referenzen und Ausschluss von ESS10/ESS11-Gruppen bleiben erhalten. Die Erläuterungen behaupten weder Neutralität noch empirische Validierung der neuen Websiteadministration.

### FDH-007: Die festgelegten Fünf-Personen-Regeln und Datenminimierung bleiben wirksam

Der unveränderte Plan 0.1 enthält in `docs/verstaendnistest-v2.entwurf.md:21–27,42–75` Freiwilligkeit, dieselbe Vorführung, Nachlesbarkeit statt Gedächtnistest, getrennte Nachfrage, fünf reale Personen, die festen Bewertungsarten, keinen Gesamtwert und keinen persönlichen Bestandenstatus. Er verlangt Überarbeitung bei mindestens zwei Personen mit derselben konkret belegten Fehlinterpretation sowie Klärung eines schweren Einzelmissverständnisses. Fehlende, teilweise und nicht einordenbare Antworten verkleinern den festen Nenner fünf nicht. Inhaltliche Änderungen verlangen eine neue Version und neue Fünf-Personen-Runde; wiederholte Teilnahme muss Lern- und Erinnerungseffekte begrenzen.

Der Zusatz übernimmt diese Regeln ausdrücklich und präzisiert die schwere Einzelregel für Parteizuschreibungen und Empfehlungen. Er führt keine Summe, neue Erfolgsquote oder Mehrheitsfreigabe ein. F5/F6 bleiben getrennte Rückmeldungen; Mehrheit und KI-Übereinstimmung belegen keine Fairness. Namen, eigene politische Antworten, Parteipräferenzen, Kontakte, Zuordnungsliste, Audio/Video und Gerätekennungen bleiben ausgeschlossen. T1–T5 dienen dem anonymisierten Erklärungsprotokoll. Es wurden von mir keine Personen angesprochen oder befragt.

### FDH-008: Vorführskript ist vorbereitet, die tatsächliche UI-Bindung bleibt später

`docs/verstaendnistest-v2.1.entwurf.md:29–45` bewahrt die deterministischen vier Antwortzustände aus 0.1. Es verlangt echte freigegebene Exportwerte, eine fehlende Einzelreferenz, eine ausgewählte freigegebene Gruppenreferenz, Other, eine Nullreferenz und einen Studienwechsel ohne passende Gruppenreferenz. Wahljahr, Befragungszeit, Frage-Nenner, Erinnerung und Quellen bleiben nachlesbar. Die Auswahlregeln werden vor der ersten Person in konkrete Studien-, Gruppen- und Frage-IDs aufgelöst und mit den tatsächlich gezeigten Exportbytes gebunden.

Das spätere Paket `COMPREHENSION-V21-001` soll erst nach Abschluss der laufenden UI-Arbeit entstehen und UI-/Komponenten-/Katalogbytes, beide Humanpläne, Entscheidungen, angezeigte Referenzen, Beispiel-IDs, Erläuterungen und Gerätebreite erfassen. Weder eine bereits aufgelöste ID-Liste noch ein fertiges Humanpaket wird behauptet. Die Durchführung braucht weiterhin Stevens gebilligte Vorführung, Einverständnis und fünf reale Personen. Der dokumentierte Nullstand menschlicher Durchläufe ist kein von mir ausgeführter Humanbeleg.

## Grenzen und verbleibende Voraussetzungen

Kein Zugriff auf `data/raw/` oder `data/local/`: kein Stat, Listing, Hash, Read, dynamische Traversal oder Zahlenneuberechnung. Kein Öffnen zusätzlicher Originalcaches oder anderer Reviewerprosa. Kein Git-, Netz-, Auth-, Server-, Installations-, Claude- oder Kontaktvorgang. Keine Runner- oder Builderausführung, kein Browsertest und kein neues Gesamtquellen-/Statistikaudit. `pnpm check` wurde in dieser ausschließlich dokumentarischen, auf die 40 gelisteten Eingabedateien begrenzten Reviewerrolle nicht ausgeführt; gemeinsamer Code und Produktdokumente wurden nicht geändert.

Unabhängiger offizieller Download-/Rohnachweis, positiver vollständiger CLI-Lauf aus frischem Checkout, menschlich gebilligte und gebundene UI/Vorführung, fünf echte Verständnistests, Gestaltungszustimmung, Fokus-/Zoombelege, konkrete Rechteprüfung, tatsächliche Claude-Schlusskontrolle und persönliche Releaseentscheidung bleiben außerhalb dieser Annahme. Die Lizenzpassagen wurden auf Konsistenz zur gelisteten Lizenzakte geprüft; ich habe keine rechtliche Nutzungsfreigabe erteilt.

`ACCEPTED_BOUNDED` erlaubt, diese Dokumentationsfassung als sachlich geprüfte Vorbereitung zu verwenden. Es erklärt keine dieser offenen Voraussetzungen für erledigt.
