# Erste Methoden- und Reproduzierbarkeitsprüfung vor v2-Empirie

3. Oktober 2026. Prüferrolle `methods_reproducibility`, frische getrennte Codex-Prüfung des Pakets `EMPIRICAL-V2-001/v1`. Worktree `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Branch laut Auftrag `research/life-93-night-20261003`; wegen des ausdrücklichen Git-Verbots nicht selbst geprüft.

Für die festgelegte historische deskriptive Ausführung habe ich keinen erheblichen Methoden-, Codierungs-, Rechen- oder Guard-Blocker gefunden. Die Software kann die fünf Studien und ihre 43 gebundenen Fragen getrennt vorbereiten. Dieses Urteil betrifft die Planung und die synthetisch geprüfte Umsetzung. Es bescheinigt keine tatsächlichen Daten, Ergebnisse, Inhaltsvollständigkeit, wissenschaftliche Gesamtvalidität oder menschliche beziehungsweise persönliche Releasefreigabe. Das Urteil allein öffnet kein Zugriffsgate.

## Prüffassung und Zugriffsgrenzen

Zuerst gelesen wurden Manifest und `scope.md`. Der erwartete und tatsächlich berechnete Manifest-SHA256 lautet:

`eeae3bc1b81463b51ce2c0a1bf90f12b08aa01f125064e680d1f983df60c62f4`

Alle 20 Manifestpins stimmen vor und nach der Prüfung. Der letzte Abgleich erfolgte am `2026-10-03T13:55:51.889916+00:00`, jeweils mit Exitcode 0. Die vollständigen Pfad-/Soll-/Ist-Hashes stehen in [hashes-before.json](../../../outputs/loop/empirical-v2-001-methods-review/hashes-before.json) und [hashes-after.json](../../../outputs/loop/empirical-v2-001-methods-review/hashes-after.json). Damit sind auch alle fünf Bibliotheken und alle fünf Testmodule an dieselbe Prüffassung gebunden. Die Katalogbindung des Vertrags stimmt ebenfalls.

Ich habe keine anderen Ersturteile, Autorenberichte, Zustands-/Handoff-Dateien oder alten empirischen Ergebnisse geöffnet und keine Autorenverteidigung eingeholt. Verweise und historische Prüfstatus innerhalb der erlaubten Manifestdokumente habe ich nicht als unabhängiges Urteil übernommen. Keine weiteren Agents, Git-, Auth-, Claude-, Installations-, Server- oder Browseraktionen. Keine gemeinsame Forschungsdatei wurde geändert. Die Schreibausgaben beschränken sich auf diesen Bericht und den eigenen Outputbereich.

Keine tatsächliche Roh-/Privatdatei wurde geöffnet, gehasht, mit `stat` geprüft oder angefragt; auch keine wirklichen CSV-Header. Die ausgeführten Testläufe sperrten zusätzlich `open`, `stat`, `lstat` und Verzeichnislesezugriffe auf die echten Worktree-Verzeichnisse `data/raw` und `data/local`. Synthetische Dateibäume lagen ausschließlich unter `outputs/loop/empirical-v2-001-methods-review/`. Ihre nachgebildeten `data/raw`-/`data/local`-Unterordner enthalten nur Testdaten.

Die im Scope erklärte v1-A/B-Exposition einschließlich des früheren B-Laufs bleibt eine bekannte Grenze. Ich habe sie nicht unabhängig rekonstruiert. Die sechs zusätzlichen ESS11-Fragen sind historische Sekundärauswertung derselben Studie, keine unangetastete Bestätigung. Der automatische Webabruf des ESS-Gewichtungsleitfadens lieferte außerdem eine bereits veröffentlichte österreichische Lehrbeispieltabelle mit. Deren Zahlen wurden weder übernommen noch zur Auswahl oder Rechnung genutzt. Keine projektbezogenen Deutschland-Antwortresultate und keine Frequenz-/Crosstab-Abfragen wurden gelesen oder ausgeführt; vollständige Freiheit von öffentlicher Ergebnisexposition wird dennoch nicht behauptet.

## Tatsächliche Lektüre und Primärbelege

Gelesen wurden die aktuellen Worktree-AGENTS, der `unslop`-Skill, der Empirieplan, Messformenentwurf, Lizenzakte und die relevanten Abschnitte von Abdeckungsmatrix, Belegregister und Quellenkatalog. Alle fünf Pythonbibliotheken und ihre fünf Testmodule wurden gelesen. Im Fragenkatalog wurden sämtliche 43 Kennungen, Wortlaut-/Kontextfelder, Antwortkategorien, Missing-Gründe und die relevanten Modus-/Routinggrenzen geprüft. Der ausführbare Vertrag einschließlich der fünf Studien und Publikations-/Interpretationsregeln wurde mit dem Katalog abgeglichen. Das ist keine vollständige visuelle Prüfung sämtlicher nationaler Fragebogen-PDFs.

Die katalogisierten öffentlichen Original-Codelist- und Dateimetadaten wurden über ihre konkret angegebenen Cachepfade gelesen, gegen ihre Originalhashes geprüft und für den eigenen Nachweis kopiert. Alle 43 Feldkennungen, Metadatenversionen, gültigen Codefolgen, englischen Kategorienbezeichnungen sowie Missing-Codes/-Gründe passen. Auch die fünf Dateiidentitäten, ausgewählten Felder, Gewichts-/Identitätsfelder und die Vertragsprovenienz passen zu diesen Metadaten. Nachweis: [public-source-checks.json](../../../outputs/loop/empirical-v2-001-methods-review/public-source-checks.json). Die fünf Dateimetadaten wurden in diesem Schritt aus den gebundenen Originalcaches geprüft, nicht erneut vom API-Endpunkt abgerufen.

Zusätzlich wurden alle 43 ausgewählten, versionierten Codelisten am `2026-10-03T13:54:10.253262+00:00` direkt von [Sikts öffentlichem Metadatenendpunkt](https://api.nsd.no/graphql) abgefragt. Die explizite GraphQL-Auswahl enthält ausschließlich deklarierte Variablen-/Codelistfelder, keine Antworten, Häufigkeiten oder Kreuztabellen. HTTP 200, keine GraphQL-Fehler, alle 43 Bindungen stimmen. Request-SHA256 `647fac0a113ffa4d283a31a5532f0b428b9f9598db9414d38a90e1c8361cee54`, Response-SHA256 `53e64ddd8a4a3bbbd749b62cc0554f2642f72494eba4df088c2aa63820698c5b`. [Anfrage](../../../outputs/loop/empirical-v2-001-methods-review/live-43-request.json) und [Abgleich](../../../outputs/loop/empirical-v2-001-methods-review/live-43-receipt.json) sind gespeichert.

Ein vorausgehender Gewichtsmetadatenversuch scheiterte an fehlenden Pflichtargumenten. Eine begrenzte Typabfrage klärte `instance`/`agencyId`; ein Versuch mit zwei Agency-Aliassen lieferte wegen des unzutreffenden `NO_NSD`-Alias einen GraphQL-Fehler. Diese HTTP-200-Antworten waren keine erfolgreichen Metadatenprüfungen. Die Fehlerbelege bleiben unter `weight-live-receipt.json`, `metadata-argument-types.json` und `weight-live-corrected-receipt.json` im eigenen Outputbereich erhalten. Der anschließende 43-Felder-Aufruf mit `PUBLISHED`/`INT_ESSERIC` gelang.

Der [ESS-Gewichtungsleitfaden V1.2 vom 6. Juli 2023](https://stessrelpubprodwe.blob.core.windows.net/data/methodology/ESS_weighting_data_1_2.pdf), Abschnitt 3 auf physischer PDF-Seite 6 und Abschnitt 4.2 auf Seiten 7–8, stützt `pspwght` für Einzellandanalysen: Das Gewicht enthält bereits die Designkomponente; `anweight` ergänzt die Bevölkerungsgrößenkomponente. Die aktuelle Fassung wurde ohne Authentifizierung mit HTTP 200 abgerufen; SHA256 `6b9c04b70b8f231de1b9040e4afcfc9387fc95e4a1d15ec0496aa7638f8528e5` stimmt mit `quellen.json`. Daraus folgt keine beobachtete Verhältnisäquivalenz der fünf tatsächlichen Dateien.

Der aktuelle [ESS-Disclaimer, Conditions of use](https://europeansocialsurvey.org/contact/disclaimer), wurde ebenfalls ohne Authentifizierung mit HTTP 200 gelesen. Er unterscheidet Daten unter CC BY-NC-SA 4.0 und Dokumentation unter CC BY-SA 4.0. Der erste Abruf über das Webwerkzeug mit `www` scheiterte an HTTP 502; der GET der exakt katalogisierten Adresse gelang. Die Lizenzbedingungen wurden hier nicht als rechtsfachliche, kommerzielle oder konkrete Veröffentlichungsfreigabe bewertet. Originale und Abrufbelege liegen im eigenen Outputbereich.

## Rechen- und Protokollprüfung

| Prüffeld | Tatsächlicher Befund und Beleg |
| --- | --- |
| Auswahl und Studiengrenzen | `policy_access_v2.py:209–283` bindet genau fünf bekannte Datei-/Studienidentitäten, Editionen, DE und 43 einmalige Fragen an den Katalog. Eigene Vertragsprobe bestätigt 6/10/4/17/6 Fragen je ESS5/8/9/10-SC/11 und acht Primärbereiche mit 5/5/12/6/3/3/4/5 Angaben. Es werden keine Personen, Kovarianzen oder Nenner studienübergreifend zusammengeführt. |
| Metadaten vor Antworten | `policy_access_v2.py:349–390` prüft Runde/Edition sämtlicher DE-Zeilen, bevor irgendeine ausgewählte Antwort normalisiert wird. Dezimal gleiche Editionen sind zugelassen; Rundentexte erlauben Integer oder genau `.0`. Ein später Metadatenfehler verhindert auch die Normalisierung früherer Zeilen. Nicht-DE-Felder bleiben semantisch uninterpretiert. |
| CSV und unbekannte Codes | Ausgewählte Antwortcodes erlauben kanonische nichtnegative Integer mit ausschließlich nullwertigem optionalem Bruchteil. Vorzeichen, führende Nullen, Exponenten, Whitespace und nichtnullige Bruchteile werden nicht erraten. Unbekannte Codes scheitern wertfrei. Doppelte/fehlende Header, falsche Zeilenbreite, fehlende oder exakt doppelte DE-Schlüssel und unbrauchbare Gewichte scheitern ebenfalls. IDs bleiben ausdrücklich exakte Strings; keine numerische Identitätsnormalisierung wird behauptet. |
| Kategorien und Missing | Gültige Originalkategorien bleiben erhalten, auch bei null Beobachtungen. `vteurmmb` 33/44/55/65 bleiben gültige benannte Antworten. Exportleere hat den separaten Grund `export_blank_unclassified`; sie wird nicht zur Verweigerung oder zum API-„No answer“. Alle 43 aktuellen Not-asked-Codelisten sind leer. Strukturell nicht gestellte Antworten werden zusätzlich in den generischen synthetischen Tests getrennt geprüft; damit ist keine tatsächliche Vollbefragung belegt. |
| Vier getrennte Rechnungen | `policy_analysis_v2.py:238–299` berechnet `pspwght`, `dweight`, ungewichtet und `anweight` separat. Keine zweite Designgewichtmultiplikation. Kategorieanteile verwenden pro Frage nur gültige Antworten; Missing-/Not-asked-Abrechnung bezieht sich auf alle DE-Fälle und behält ihre Gewichtsbasen. Keine gemeinsame Komplettfallliste. |
| Sensitivität | Die maximalen absoluten Kategorieabweichungen stimmen mit unabhängigen Bruchsummen überein. Die `anweight/pspwght`-Extrema umfassen alle DE-Fälle, auch Missing/Not-asked. Eine nichtkonstante synthetische Relation bleibt eine Diagnose und erhält keinen automatischen Äquivalenz- oder Gütestempel. Die Statusvorbereitung ersetzt den späteren Ergebnisreview nicht. |
| SE und Darstellung | Der aktuelle Runner übergibt immer `design=None`/`design_basis=None`. Keine SE, CI oder persönlichen Unsicherheiten. Die festgelegten Grenzen 100 gültige Fälle und 5 positive Zellfälle werden in Analyse und Export erneut geprüft. 99/100 und 4/5 sind getestet; Nullzellen bleiben null, kein gültiger Nenner bleibt `no_valid_answers`. Die Grenzen sind Darstellungsheuristiken, keine Präzisions- oder Anonymitätsnachweise. |
| Gate vor Raw-I/O | `policy_access_v2.py:286–346,435–487` prüft das eigene v2-Gate, Rollen, Reportbytes, Freeze, Manifest, sämtliche gelisteten Artefakte und die ausführenden Bibliotheksquellen vor dem Raw-Pfad. Erst danach folgen tatsächlicher Inputhash/Bytezahl und Metadatenprüfung. Der alte v1-Gatepfad wird nicht konsultiert. Eine zusätzliche Probe erfasst schon das Erreichen eines synthetischen Raw-Pfads; bei falscher Kategorienbindung waren es null Aufrufe. |
| Private Ausgabe und Fehler | Der Runner schreibt nur private, unreviewte Aggregate samt Input-/Gate-/Freeze-/Vertragspins. Verzeichnisse 0700, Datei 0600, atomarer Austausch; Symlinks und unpassende Berechtigungen werden abgewiesen. Tests prüfen wertfreie Fehler, fehlende Kennungs-/Zeilen-/unselektierte Inhalte und Erhalt einer früheren Ausgabe bei atomarem Schreibfehler. Ein tatsächlicher Metadatenfehler einer synthetischen ESS9-Datei sperrt deren Lauf; der getrennte ESS5-Lauf bleibt möglich. |
| Export | `policy_export_v2.py:125–448` hat geschlossene Kandidaten-, Vertrags- und Entscheidungsformen. Kategorien, Nenner, vier Rechnungen, Missing-Gründe, Status und Diagnosen werden erneut geprüft. Entscheidung bindet kanonische Kandidaten-/Studienvertragshashes, zwei unterschiedliche Rollen/Reportpfade und explizite Fragefreigaben. Ein bloß geänderter Status öffnet keine Referenz. Unterdrückte oder nicht freigegebene Fragen bleiben vorhanden und tragen keine Referenz. Keine Personen-/Gruppenwerte oder privaten Bindungsdateien im öffentlichen Rückgabewert. |

Die optionale generische WRT-Varianz ist in dieser geplanten Ausführung ausgeschaltet. Ihre vorhandenen synthetischen Tests liefen als Teil des ausdrücklich erlaubten Referenzmoduls mit; daraus folgt weder eine Anwendungsentscheidung noch die geprüfte Eignung einer tatsächlichen Designbasis. Weitere Varianzdetailprüfungen werden hier nicht zur Voraussetzung der historischen Kategorienrechnung gemacht.

## Befunde mit Korrekturumfang

Keine erheblichen Blocker für die spezifische historische Ausführung. Zwei Hinweise bleiben abgegrenzt:

### M-H01 – Der B25-Sperrbereich ist im Katalog mehrdeutig

**Stelle:** `data/politikprofil-v2.fragen.entwurf.json:10542–10555`, `remainingBindings[].blocks="this_item_only"`; daneben `data/analysevertrag.v2.entwurf.json:1274–1277` und Empirieplan Zeile 30.

**Beleg:** Der Katalog erhält beide unvollständigen Bindungen für den neuen Nachlauf und das ursprüngliche operative CAWI-Routing. Scope, Plan und Vertrag erlauben ausdrücklich nur die historische deskriptive Zweikategorienauswertung und beschreiben den neuen Websiteablauf als verändert und noch menschlich ungeprüft. Der Zugriffscode vergleicht Kategorien, ersetzt diese Grenzen aber nicht durch eine Routingprüfung.

**Auswirkung:** Ein späterer Verbraucher des Katalogfeldes allein könnte den historischen Teil unnötig sperren oder die zugelassene historische Rechnung mit einer Website-/Originaläquivalenzfreigabe verwechseln. Im identischen vorliegenden Paket ist die enge historische Ausnahme hinreichend erklärt. Der Hinweis ist deshalb kein Gesamtblock und keine Behauptung ursprünglicher CAWI-Äquivalenz.

**Minimale überprüfbare Korrektur:** Bei der nächsten eigenen Katalogfassung den Sperrbereich ausdrücklich nach historischer Deskription und neuer Websiteadministration kennzeichnen. `incomplete` und die unbekannte operative Durchführung erhalten. Für diese festgelegte historische Ausführung ist keine zusätzliche Routingrekonstruktion verlangt; Website- und Modusäquivalenz bleiben offen.

### M-H02 – Der Exportbuilder authentifiziert keine Ergebnisreviews

**Stelle:** `pipeline/policy_export_v2.py:1–6,369–405`; `pipeline/policy_access_v2.py:3–5,286–346`.

**Beleg:** Der Accessrunner prüft tatsächliche Reportbytes gegen Gatepins. Der rein speicherbasierte Exportbuilder prüft Rollen/Pfade/Hashform und bindet Kandidat und Studienvertrag; er liest weder Reviewmanifest noch Ergebnisberichte. Das Modul benennt diese Grenze ausdrücklich. Die synthetischen Exportentscheidungen sind formale Fixtures, keine echten Urteile.

**Auswirkung:** Formal passende erfundene Reviewhashes wären für den Builder allein ausreichend. Ein Repositoryeigentümer wird durch diesen Protokollguard nicht authentifiziert oder technisch isoliert. Die dokumentierte separate Root-Prüfung der tatsächlichen Ergebnisreviews ist deshalb Teil des Exportwegs; Kandidatenstatus oder erfolgreiche Tests ersetzen sie nicht.

**Minimale überprüfbare Korrektur:** Keine Codekorrektur innerhalb dieses erklärten Protokollumfangs nötig. Beim späteren Export müssen die tatsächlichen zwei Ergebnisberichte und ihr Reviewmanifest gegen die gebundenen Hashes geprüft und der konkrete Frageentscheid belegt werden. Das ist die vorhandene Exportanforderung, keine neue Vor-Empirie-Voraussetzung.

## Tatsächlich ausgeführte Tests

Mit `PYTHONDONTWRITEBYTECODE=1`, unveränderten Testmodulen und einem Reviewerwrapper, der nur das Fixtureverzeichnis ins eigene Outputverzeichnis verlegt:

| Modul | Tests | Fehler / Fehlschläge / ausgelassen | Exitcode |
| --- | ---: | --- | ---: |
| `test_policy_reference_v2` | 22 | 0 / 0 / 0 | 0 |
| `test_policy_adapter_v2` | 17 | 0 / 0 / 0 | 0 |
| `test_policy_analysis_v2` | 16 | 0 / 0 / 0 | 0 |
| `test_policy_access_v2` | 26 | 0 / 0 / 0 | 0 |
| `test_policy_export_v2` | 17 | 0 / 0 / 0 | 0 |
| Eigene Methoden-/Scopeproben | 6 | 0 / 0 / 0 | 0 |

Zusammen 98 bestehende Modultests und sechs eigene Proben. Die eigenen `Fraction`-Oracles prüfen 172 Quotienten über alle 43 Fragen, alle gebundenen Kategorien und Missing-Gründe, getrennte Nenner, Sensitivitätsmaxima und Verhältnisextrema. Synthetischer Exportabgleich für jede der fünf Studien, Zurückweisung eines alten Kandidatenhashes, verspäteter Metadatenfehler vor Antwortnormalisierung, Sourceguard vor Raw-Pfad, Studienfehlerisolation und Statusbypass sind geprüft. Die eigene Probenfassung wurde nach Ergänzung der Studienfehlerisolation erneut ausgeführt, Exitcode 0.

Befehle:

```sh
PYTHONDONTWRITEBYTECODE=1 python outputs/loop/empirical-v2-001-methods-review/run_targeted_tests.py
PYTHONDONTWRITEBYTECODE=1 python outputs/loop/empirical-v2-001-methods-review/review_probes.py
PYTHONDONTWRITEBYTECODE=1 python outputs/loop/empirical-v2-001-methods-review/check_public_sources.py
```

Testcode, Einzelprotokolle und Zusammenfassungen: [eigener Outputbereich](../../../outputs/loop/empirical-v2-001-methods-review/), insbesondere `unit-summary.json`, `probes.json`, `probes.txt` und `public-source-checks.json`. Der Quellenabgleich hatte Exitcode 0. Keine komplette Repositorysuite, kein `pnpm check` und kein Browseraudit, entsprechend dem ausdrücklichen Prüfauftrag. Die Quellenzugriffsfehler sind oben getrennt von erfolgreichen Prüfungen aufgeführt.

## Gebundenes Urteil

Die geplante historische Ausführung darf aus Sicht dieser Methodenrolle unter ihrem festgelegten v2-Gate und den bestehenden Ergebnis-/Exportgrenzen weiter vorbereitet werden. Für einen tatsächlichen Zugriff bleiben die zweite getrennte Rolle, die versionierte Planfestschreibung und der positive, exakt gebundene Zugriffsentscheid erforderlich. Dieses Ersturteil ist kein Ersatz dafür.

Beide Rollen gehören derselben Codex-Modellfamilie an. Getrennte Ersturteile verhindern Kenntnis des jeweils anderen Urteils; sie beseitigen gemeinsame Wissenslücken, politische Auswahlmuster, Fehler bei Quelleninterpretation oder ähnliche Rechenannahmen nicht. Synthetische Übereinstimmung ist keine Empirie. Agentenkonsens ist kein Neutralitätsnachweis und keine Fachbegutachtung.

ACCEPTED_BOUNDED
