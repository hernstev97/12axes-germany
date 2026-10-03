# P1: Methoden und Reproduzierbarkeit, Plan v2.2

Gesamturteil: **NICHT_BESTANDEN** für die Festschreibung von PLAN-V22-001. Die angegebenen Hashes stimmen. Taylor-Linearisierung und xlogit-Formel sind für die ausdrücklich vereinfachten Annahmen korrekt. Der Runner verletzt jedoch mehrere übernommene Vertrags- und Zugriffsschutzregeln; Katalog- und Profilzusagen sind nicht vollständig erfüllt.

Prüfdatum: 3. Oktober 2026. Branch bei Prüfung: `research/life-93-claude-20261003`. Ausgangsarbeitsbaum war sauber. Modus: getrennte Erstbewertung vor Festschreibung. Keine Empirie gerechnet.

## Tragfähige Teile

- Der Quotient nutzt pspwght unter gültigen Domänenantworten. Alle deutschen PSUs bleiben einschließlich Nullbeiträgen erhalten; Stratum-/PSU-Paare verhindern versehentliche Zusammenlegung. Taylor-Zentrierung, WR-Faktor und df = PSUs − Strata stimmen mit dem Originalmanual überein. Singletonstrata verhindern die Varianz; zu geringe df und Randanteile erhalten fehlende Intervalle.
- Der zitierte survey-Manualcache enthält svyciprop tatsächlich auf PDF-S. 93–94; xlogit, t-Freiheitsgrade und fehlende Randintervalle sind dort beschrieben. S. 101 belegt PSU-Summen/Zentrierung/Nullbeiträge, S. 104 die WR-Erststufenannahme ohne FPC. Feste Gewichte und nicht modellierte Poststratifikation sind benannt, ebenso Transfer-, Nonresponse- und Messfehlergrenzen. F09 ergänzt eine verbleibende Einschränkung.
- Deutschlandfilter, Inputdatei-Hash, Runde, numerisch gleiche Edition und Duplikatprüfung sind vorhanden. Antwort-Missing-Gründe, Nichtgestellt und Exportleere werden getrennt geführt. Die 100/5-Statusregeln sind korrekt gesetzt; Intervalle entstehen nur für PREPARED-Referenzen mit Design. WITHHELD-Zahlen bleiben im privaten Aggregat, nicht automatisch im öffentlichen Export.
- Der Katalogcheck liest echte PDF-Textschichten und öffentliche ESS-Codeinventare. Er ist kein Selbstvergleich. `--check` reproduziert die committed Ergänzung; F06 betrifft die konkrete Ausnahmelücke.
- Profiltexte sind reine Funktionen fester Tabellen und gewählter Codes. Antwort-Map-Reihenfolge hat keinen Einfluss. Zahlenvergleiche dienen nur Originalblock-Minima/Maxima bzw. ordinalen Vergleichen; kein versteckter Gesamt-/Themenwert. Diese Zusage betrifft Antwortreihenfolge bei festem Katalog, nicht eine beliebige Neuordnung des Katalogs.
- Die Auswahlregeln sind explizit inhaltsbezogen und enthalten begründete Ausschlüsse. Frühere v1-/v2-Kenntnis wird im Text genannt; ein Wechsel nach ESS10 wird nicht als neue unabhängige Erhebung ausgegeben. Die tatsächliche Zugriffsbiographie ist hier nicht unabhängig geprüft.

## Findings

### P1-V22-F01 (erheblich; blockiert Festschreibung)

**Geprüfte Zusage:** Der Runner übernimmt die v2.1-Gruppenzuordnung und deren Eingangsprüfung.

Nur vote == 1 wird geprüft. Unbekannte Wahl-/Parteicodes und Literale werden still als außerhalb der Gruppen behandelt. Die vorgeschriebene getrennte Wahl-/Parteistatusbilanz einschließlich Inkonsistenzen fehlt.

**Fundstellen:** pipeline/v22/run_v22.py:228-244; data/gruppenvertrag.v2.1.entwurf.json:3369-3425; Synthetische Gegenproben unknown_vote und unknown_party: run() akzeptiert jeweils 999; keine eligibilityAccounting-Ausgabe.

**Auswirkung:** Fehlerhafte Gruppeneingänge bleiben unbemerkt; die Zuordnung ist bei bekannten gültigen Codes richtig, ihre Voraussetzungen und Ausschlüsse sind jedoch nicht nachprüfbar.

**Schweregradbegründung:** Betrifft die vertragliche Grundlage aller neuen Gruppenreferenzen.

**Korrektur:** Wahl und Partei für alle deutschen Fälle mit vollständigen Vertragsinventaren validieren; unbekannte Literale/Codes mit festem Fehler abbrechen. Missing-Gründe, Nichtwahl, Nichtberechtigung, Nichtanwendbarkeit, technische Leere und Inkonsistenzen getrennt privat bilanzieren.

**Nachprüfung:** Synthetisch sämtliche Zustände, unbekannte Werte auch bei Nichtwählenden, gültige Partei bei vote != 1 und Other prüfen; feste Fehlermeldungen und getrennte Bilanzen verlangen.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F02 (mittel; blockiert Festschreibung)

**Geprüfte Zusage:** Gewichtsprüfungen und Diagnostik aus v2/v2.1 bleiben erhalten.

anweight wird weder gelesen noch auf positive endliche Werte geprüft. Die Konstanzdiagnose anweight/pspwght entfällt ohne dokumentierte Änderung des Vertrags.

**Fundstellen:** pipeline/v22/run_v22.py:202-217; docs/empirie-plan-v2.entwurf.md:42; data/gruppenvertrag.v2.1.entwurf.json:3430-3457; Synthetische Gegenprobe invalid_anweight: -1 wird akzeptiert.

**Auswirkung:** Die Primäranteile mit pspwght sind dadurch nicht automatisch falsch; eine zugesagte Importprüfung und Reproduzierbarkeitsdiagnose fehlt.

**Schweregradbegründung:** Klarer Vertragsverstoß, ohne Beleg eines falschen Primäranteils.

**Korrektur:** anweight gemäß Vertrag validieren und Verhältnisdiagnose privat protokollieren; nichtkonstante Verhältnisse als Diagnose erhalten, ohne Primärgewicht oder Auswahl zu ändern.

**Nachprüfung:** Tests für fehlende, negative, nullwertige und nichtendliche Gewichte sowie konstante und nichtkonstante Verhältnisse mit 1e-12-Toleranz.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F03 (mittel; blockiert Festschreibung)

**Geprüfte Zusage:** Die Serialisierung akzeptiert keine Whitespace-Abweichungen.

CANON.match mit $ akzeptiert einen abschließenden Zeilenumbruch. code_of("1\n") liefert den gültigen Code 1. Ein entsprechend quotiertes synthetisches CSV-Feld wird ausgewertet.

**Fundstellen:** pipeline/v22/run_v22.py:36,57-61; docs/empirie-plan-v2.entwurf.md:48; data/gruppenvertrag.v2.1.entwurf.json:3369-3378; Synthetische Gegenprobe newline_question: ACCEPTED.

**Auswirkung:** Ein vertraglich unbekanntes Literal wird still in eine gültige Antwort umgewandelt.

**Schweregradbegründung:** Direkt reproduzierbare Abweichung von der vorab gebundenen Parserregel.

**Korrektur:** re.fullmatch oder einen absoluten Endanker verwenden, ohne trim/strip; dieselbe vollständige Prüfung auch für Wahl-/Parteifelder verwenden.

**Nachprüfung:** Gültige 1/1.0/1.00 und ungültige Endzeilenumbrüche, führende/nachfolgende Leerzeichen, Tabulatoren, Vorzeichen, Exponenten und führende Nullen testen.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F04 (erheblich; blockiert Festschreibung)

**Geprüfte Zusage:** Der Lauf schreibt ausschließlich eine private Ausgabe unter data/local/v22.

--out wird uneingeschränkt mit ROOT kombiniert; absolute Pfade und .. sind zulässig. Somit können auch Aggregate kleiner Zellen in Git-/Web-Verzeichnissen landen. 0600 schützt nicht vor Git-Aufnahme. Zudem chmod erfolgt vor einer Pfadgrenzenprüfung.

**Fundstellen:** pipeline/v22/run_v22.py:11-13,257-267,275-280; pipeline/v22/run_v22.py:147-167; data/gruppenvertrag.v2.1.entwurf.json:3489-3503 (privacyAndOutputs)

**Auswirkung:** Der deklarierte private Ausgabekanal ist nicht erzwungen. Private WITHHELD-Anteile und kleine Zellzahlen sind tatsächlich im internen Ergebnis enthalten. Keine beobachtete Veröffentlichung oder tatsächliche Datenexposition wird behauptet.

**Schweregradbegründung:** Erreichbarer Ausgabepfad verletzt die zentrale Trennung privater Aggregate von öffentlichen Artefakten.

**Korrektur:** Ausgabe fest auf den privaten Pfad beschränken oder aufgelöste Pfade inklusive Symlink-Zielen streng innerhalb eines eigens gebundenen privaten Verzeichnisses prüfen; vor mkdir/chmod abbrechen. Keine vorhandenen fremden Verzeichnisrechte ändern.

**Nachprüfung:** Nur synthetisch: absoluter Pfad, .., Symlink-Flucht und Web-/Git-Pfad werden vor jeder Mutation abgelehnt; gültige Ausgabe erhält 0700/0600 und bleibt gitignored.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F05 (erheblich; blockiert Festschreibung)

**Geprüfte Zusage:** Das Tag analyseplan-v2.2 bindet die geprüfte Festschreibung vor der Rechnung.

plan_tag_present prüft nur, ob irgendein auflösbares Git-Objekt unter diesem Namen existiert. Der Lauf prüft nicht, ob aktueller Plan, Verträge, Ergänzung und Rechencode zur eingefrorenen Fassung gehören. Die drei Vertrags-Hashes werden lediglich protokolliert, nicht gegen einen Gate-Sollwert geprüft.

**Fundstellen:** pipeline/v22/run_v22.py:184-200,249-261; docs/analyseplan-v2.2.md:118-120; .claude/skills/life93-review/SKILL.md: Manifest-/Eingabebindung vor Bewertung und neue Fassung nach Änderungen.

**Auswirkung:** Die CLI verweigert ohne Tag korrekt; ein vorhandenes, veraltetes oder unpassendes Tag autorisiert dagegen auch eine ungeprüfte Arbeitsfassung. run() ist eine importierbare Bibliothek und selbst kein Zugriffsgate.

**Schweregradbegründung:** Existenz allein sichert die zentrale Reihenfolge Prüfung/Festschreibung/abhängige Analyse nicht.

**Korrektur:** Ein positives, versionsgebundenes Gate mit eingefrorenen Plan-/Vertrags-/Softwarehashes prüfen. Bei Tag-Ziel oder Arbeitsdatei-Abweichung vor Datenöffnung abbrechen; autorisierten Bibliothekseinstieg ausdrücklich vom synthetischen Testweg unterscheiden.

**Nachprüfung:** Ohne echte Daten: fehlendes/falsches Tag, passendes Tag mit verändertem Plan/Vertrag/Code und korrekt gebundenes Paket testen. Keine Tags im Projekt für diese Prüfung anlegen.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F06 (mittel; blockiert Festschreibung)

**Geprüfte Zusage:** Jeder deutsche Katalogtext wird automatisch mit dem Original-PDF abgeglichen.

extraValid-Labels werden nach dem verify-Durchlauf angehängt. Der deutsche Text für Code 55 wird daher nicht geprüft. Außerdem wird der explizite Code aus extraValid ignoriert; Zuordnung erfolgt allein durch zip(valid, labels).

**Fundstellen:** pipeline/v22/catalogue_v22.py:77,285-300; docs/analyseplan-v2.2.md:59,63; Synthetische In-memory-Mutation extraValid[0] auf SYNTHETISCHER NICHTQUELLENTEXT: build() akzeptiert sie.

**Auswirkung:** Die Aussage eines vollständigen automatischen Abgleichs ist zu weit. Dies ist kein Beleg, dass der derzeitige Code-55-Wortlaut falsch ist.

**Schweregradbegründung:** Nachgewiesene Lücke in einer ausdrücklich zugesagten Quellenprüfung.

**Korrektur:** Auch zusätzliche gültige Labels gegen ihre echte PDF-Fundstelle prüfen und ihren Code explizit binden. Für alle Labels eine nachvollziehbare Code-/Beschriftungszuordnung statt bloßer Mengen-/Positionsgleichheit absichern.

**Nachprüfung:** Manipuliertes Code-55-Label und falscher extraValid-Code müssen scheitern; Originalfassung muss bestehen. Andere bereits geprüfte Wortlaute unverändert lassen.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F07 (mittel; blockiert Festschreibung)

**Geprüfte Zusage:** Der Querbezug Absicherung bei Armut und Bedarf enthält basinc; Plan und Profilregeln nennen dieselbe feste Struktur.

Die Dokumentation nennt fünf Fragen einschließlich basinc, die Implementierung nur vier ohne basinc. Mit ausschließlich basinc und sofrpr entsteht trotz zweier dokumentierter Antworten kein Querbezug. Der Plan nennt sechs Querbezüge, Tabelle und Code tatsächlich sieben.

**Fundstellen:** docs/profilregeln-v1.md:46-57; web/src/app/policy-draft/profile/profile-structure.ts:160-165,152-224; docs/analyseplan-v2.2.md:100; Synthetische TS-Gegenprobe basinc+sofrpr: need_security present false.

**Auswirkung:** Die eingefrorene erklärende Profilstruktur wäre uneinheitlich; derzeitige deterministische Ausführung erfüllt diesen dokumentierten Fall nicht.

**Schweregradbegründung:** Konkrete Abweichung des vorab festzulegenden Profilvertrags.

**Korrektur:** Vor Festschreibung entweder basinc samt passendem Kontext ergänzen oder seine Auslassung in der verbindlichen Regel begründen; Zahl der Querbezüge einheitlich auf sieben setzen, sofern diese Struktur bleibt.

**Nachprüfung:** Zwei-Antwort-Fall basinc+sofrpr und vollständigen need_security-Inhalt testen; dokumentierte Mitglieder mit Regelmitgliedern maschinell vergleichen.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F08 (mittel; blockiert Festschreibung)

**Geprüfte Zusage:** T01–T30 sind in profile-engine.spec.ts umgesetzt.

T14 fehlt als zugesagter Zwei-Format-Querbezug. T30 fehlt vollständig; die reine Profilfunktion nimmt keinen historischen Referenzstatus entgegen. Neue Blöcke und neue Grenzfälle haben überwiegend nur den generischen Einzelkategorietest. Der Allkategorietest nimmt auch das auf der Website nicht angebotene Code-55-Label auf.

**Fundstellen:** docs/profilregeln-v1.md:83-85; web/src/app/policy-draft/profile/profile-engine.spec.ts:123-343 (gesamte Testliste); reports/claude/agenten/R4-profilform.md:349,365; web/src/app/policy-draft/profile/profile-engine.ts:337-380

**Auswirkung:** Die behauptete Testabdeckung ist nicht vorhanden. Bestehende Tests bestehen, sichern aber keine Unterdrückung historischer Vergleiche für WITHHELD/NO_VALID.

**Schweregradbegründung:** Konkrete falsche Abdeckungsbehauptung im Planprüfpaket; technische Tests und spätere Anzeigeprüfung müssen getrennt werden.

**Korrektur:** T14 ergänzen; T30 an der tatsächlich zuständigen Vergleichsfunktion testen oder hier ausdrücklich als noch offene Anzeigeprüfung ausweisen. Neue Blockmuster/Grenzfälle gezielt prüfen und answerable/offered-Kategorien korrekt benennen.

**Nachprüfung:** Testfälle dokumentierten Kriterien zuordnen; T14 mit scchpldm=1 und wpestop=0; T30 für beide unterdrückten Status und fortbestehende eigene Aussage. Kein Browser-/Verständnistest daraus ableiten.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F09 (mittel; offene Methodengrenze)

**Geprüfte Zusage:** Der 95-%-xlogit-Bereich beschreibt die Stichprobenunsicherheit unter dokumentierten Annahmen.

Das zitierte Originalhandbuch warnt zusätzlich vor Unterdeckung bei Anteilen nahe 0 oder 1. Diese Einschränkung fehlt in Abschnitt 4. Mindestfallzahlen 100/5 und globale Design-df >=20 garantieren weder ausreichende effektive Zellinformation noch nominale 95-%-Abdeckung.

**Fundstellen:** outputs/loop/methods/SURVEY-MANUAL.pdf: PDF S.94, Details, Absatz All methods undercover; docs/analyseplan-v2.2.md:79-88; pipeline/v22/survey.py:169-180,183-202

**Auswirkung:** Die Formel ist korrekt für die deklarierte Approximation; ihre nominale Abdeckung darf nicht als gesichert verstanden werden, besonders bei seltenen oder stark gewichteten Kategorien.

**Schweregradbegründung:** Dokumentationsgrenze eines vertretbaren Standardverfahrens, kein nachgewiesener Rechenfehler.

**Korrektur:** Nahe-Rand-Unterdeckung und mögliche geringe effektive Information ausdrücklich als offene Grenze nennen. 100/5/20 als Projektkriterien bezeichnen, ohne neue ergebnisabhängige Schwellen zu erfinden.

**Nachprüfung:** Korrigierte Methodenerklärung gegen S.94 lesen; synthetische Rand-/Gewichtskonstellationen ergänzen. Eine neue Methode wäre separat vor abhängigen Ergebnissen festzulegen.

Status: OFFEN. Gewissheit: BELEGT.

### P1-V22-F10 (mittel; blockiert Festschreibung)

**Geprüfte Zusage:** Das Manifest bindet die vollständigen Eingaben des reproduzierbaren Prüfpakets.

Der Kataloggenerator liest zusätzlich ess10sc-file-metadata.json; dieser Cache ist im Manifest nicht enthalten. Auch die technischen Tests bzw. Profilprüfung benötigen nicht manifestierte Hilfsdateien. Die angegebenen Hashes sind alle richtig, doch das Manifest ist kein vollständiger Abhängigkeitsverschluss.

**Fundstellen:** pipeline/v22/catalogue_v22.py:257-262; reports/claude/pruefungen/PLAN-V22-001-manifest.json: localPublicCaches; pipeline/v22/test_survey.py:15-17; web/src/app/policy-draft/policy-catalogue.ts:1-5

**Auswirkung:** Metadatenversion und Reproduktionsgrundlage können außerhalb der eingefrorenen Eingaben wechseln. Der eigene Bericht ergänzt tatsächliche Hashes, ersetzt damit aber nicht das festzuschreibende Manifest.

**Schweregradbegründung:** Fehlende verbindliche Quellen-/Softwarebindung trotz korrekter Hashes der gelisteten Artefakte.

**Korrektur:** Den tatsächlich gelesenen ESS10-Dateimetadatencache und benötigte Reproduktionsabhängigkeiten ins neue Manifest aufnehmen; Sollhashes beim Build prüfen, nicht nur neu berechnen. Prüfpaket nach Korrekturen neu versionieren.

**Nachprüfung:** Katalogbuild mit unverändertem Cache muss reproduzieren; Änderung der Dateimetadaten muss an der Eingabebindung scheitern. Neue Manifestbindung gezielt nachprüfen.

Status: OFFEN. Gewissheit: BELEGT.

## Vor Festschreibung und später offen

F01–F08 und F10 müssen vor der Festschreibung korrigiert oder im verbindlichen Umfang ausdrücklich begrenzt werden. Kein neuer Item-/Modellentscheid wird durch dieses Urteil getroffen. Nach Korrekturen neue Hashbindung und gezielte Nachprüfung dieser Findings; kein erneutes Gesamtaudit verlangt. F09 darf als offen benannte Methodengrenze bleiben, ohne nominale 95-%-Abdeckung als empirisch gesichert auszugeben.

Die spätere echte Rechnung, Ergebnisprüfung, Exportentscheidung, SDDF-Bindung und menschliche Verständnis-/Releaseprüfung bleiben getrennte Voraussetzungen. Der feste private Bericht darf kleine Aggregate enthalten; der öffentliche Export braucht eigene Allowlist und Unterdrückungsprüfung. Ein positives Planurteil wäre keine Freigabe dieser späteren Schritte.

## Ausführungsgrenzen

- Frischer Codex-Methodenprüfer, OpenAI, gpt-6.1-sol, medium laut injizierter T3-Laufzeit. Keine konkrete interne Revision bekannt. Zweiter Codex-Prüfer gehört derselben Modellfamilie an; gemeinsame mögliche Fehlerquellen bleiben. Keine Agentenübereinstimmung als Neutralitätsnachweis.
- Keine Antwortdaten, data/raw oder data/local, keine gesperrten Verteilungen, keine P2-Urteile gelesen. R1-R3, V2-Quellenurteil und Kontrollrechnungsbericht nur binär gehasht; Inhalte nicht gelesen. R4 ist der im Auftrag gebundene Profilautorbericht, nur relevante Ausschnitte/Prüffälle gelesen, kein fremdes P1/P2-Ersturteil.
- Kein run_v22.py-CLI-/Echtlauf, kein Tag/Commit/Push, keine Nachrichten an Dritte. Nur synthetische run()-Funktionsaufrufe mit CSV/Verträgen in temporären /tmp-Verzeichnissen.
- Code enthält keine Serialisierung von Antwortzeilen, Kennungen oder Einzelgewichten. Private Aggregatdatei enthält kleine Zellen und WITHHELD-Anteile. Das ist intern zulässig; ihre öffentliche Weitergabe wurde nicht getestet oder freigegeben. Plan erlaubt kleine Missing-Anzahlen ohne Gewichtssumme, weshalb sie allein kein Finding darstellen.
- Kein unabhängiger Zugriffsaudit der behaupteten neuen Ergebnisblindheit; Textdarstellung geprüft, tatsächliche frühere Kenntnis nicht bewiesen. Alte Referenzzahlen und tatsächliche Designzahlen nicht gelesen oder unabhängig bestätigt.
- Keine empirische Varianz-/Abdeckungsvalidierung oder direkte R-survey-Kontrollrechnung. Synthetischer Vergleich zur vorhandenen Codex-Bibliothek bleibt ein Vergleich innerhalb derselben Modellfamilie.
- Profiltests mit TypeScript-transpileModule und eigenem Assertion-Adapter im Speicher ausgeführt, nicht mit Vitest. Kein Browserlauf, keine menschliche Verständnisprüfung, keine UI- oder Releaseabnahme.
- SDDF-Integration ist noch nicht implementiert: run() liest keine separate SDDF, und neue ESS5/ESS8-Gruppen erhalten mit_interval=False. Vor dem im Plan eröffneten späteren SDDF-Weg sind Hash-/Edition-/Schlüsselbindung, vollständiger Join und Gruppenintervalle synthetisch vorzubereiten; aktuelle fehlende Intervalle bleiben fehlend.
- Keine neuen Rechts-/Quellen-/Fairnessurteile über GESIS oder ESS12; diese Rolle prüft Methoden. Keine eigenständige rechtliche Freigabe aus dem Plantext abgeleitet.
- pnpm check nicht ausgeführt: es umfasst einen Build mit zusätzlichen Dateien und überschreitet den ausdrücklich auf zwei Berichtsdateien begrenzten Schreibauftrag. Bericht-/JSON-Prüfung separat; keine technischen Gesamtchecks als bestanden ausgegeben.

## Ausgeführte Befehle und Gegenproben

- `cat reports/claude/auftraege/P1-plan-v22-methoden.md` zuerst vollständig; anschließend `sha256sum` des Auftrags.
- `cat`, `nl -ba`, `sed`, `head` und `rg` ausschließlich für die hier aufgeführten öffentlichen Methoden-/Instrument-/Softwareeingaben; keine rekursiven Rohdaten-/Ergebnissuchen.
- Python/hashlib: Manifesthash gegen Auftrag und alle Artefakt-/Cachehashes gegen Manifest geprüft. Alle stimmen. Nur Hashprüfung fremder Berichte, kein Lesen ihres Inhalts.
- `pdftotext -f 93 -l 94 -layout outputs/loop/methods/SURVEY-MANUAL.pdf -`; zusätzlich S.100–101 und S.103–105, sowie begrenzte Textsuche im Manual. Kein Layouturteil.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest pipeline/v22/test_survey.py pipeline/v22/test_run_v22.py`: 11 Tests, OK.
- `PYTHONDONTWRITEBYTECODE=1 python3 pipeline/v22/catalogue_v22.py --check`: committed Ergänzung bytegleich verifiziert. Das liest nur öffentliche PDF-/Metadatencaches und schreibt nichts.
- Python-Inline-Gegenproben: `synthetic(Path(tmp))` aus test_run_v22, CSV-Zeile 5 jeweils mit vote=999, vote=1/party=999, idno leer, new="1\n" oder anweight=-1 ändern; `run(*paths, verify_hashes=False)`. Alle fünf akzeptiert. Leerkennung ist als Beobachtung dokumentiert, nicht zusätzlich als Vertragsfinding gewertet. Alle Fixtures in TemporaryDirectory(dir="/tmp").
- Python-Inline-Katalogprobe: nur im Speicher `ITEMS[0]["extraValid"]=[("55","SYNTHETISCHER NICHTQUELLENTEXT")]`, anschließend `build()`; falscher Text akzeptiert. Kein Katalogfile geschrieben.
- Node-Inline-Test: TypeScript-transpileModule, CommonJS-Module im Speicher, Allowlist ausschließlich policy-catalogue/public-catalogue/public-catalogue-v22/catalogue-types sowie vier profile-Dateien. assert-Adapter für describe/it/expect; alle 19 Originaltests bestanden. Zusätzlicher Fall basinc=1/sofrpr=1 ergibt keinen need_security-Querbezug. Kein Vitest und keine Dateiausgabe.
- `git branch --show-current` und `git status --short`: erwarteter Branch, vor Berichtserstellung sauber.
- Berichtserstellung mit Python; anschließend ausschließlich Berichtformat- und JSON-Schemaprüfung. Kein pnpm-Gesamtcheck wegen enger Schreibgrenze.

- Python-jsonschema war nicht installiert (`ModuleNotFoundError`); keine Installation vorgenommen. Anschließend JSON mit installiertem Ajv 2020 gegen das unveränderte Skill-Schema validiert: gültig.
- Prettier zunächst mit Formatabweichungen; ausschließlich beide Berichte mit `pnpm exec prettier --write` formatiert und danach mit `--check` geprüft.

## Gelesene Eingaben mit SHA-256

Die folgenden Hashes bezeichnen tatsächliche Inhaltszugriffe, einschließlich indirekter Reads durch synthetische Tests/Katalogbuild. R4 und einige Hilfsdateien wurden nur in relevanten Ausschnitten gelesen; PDFs als Text der benötigten Seiten. Die übrigen Manifestberichte wurden ausschließlich gehasht und sind keine Bewertungsgrundlage. Die gesamte Manifestliste wurde zusätzlich vollständig auf Hashgleichheit geprüft.

| Eingabe                                                              | SHA-256                                                            |
| -------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `reports/claude/auftraege/P1-plan-v22-methoden.md`                   | `a34d402aab03ad89aa27349e3bdfb1b50006a66c464b9423f4cc32c25fb0a374` |
| `reports/claude/pruefungen/PLAN-V22-001-manifest.json`               | `1d269e9ab4fa49d3ba5beec17a600d5b9bd58f3998611f2ffe5e8f842d739639` |
| `.claude/skills/life93-review/SKILL.md`                              | `90e44b1ce3aa31f5c7e00a91af7516e06a2dec930ba83e0ea1cd5b51714255a6` |
| `.claude/skills/life93-review/references/urteil-schema.json`         | `5d36a1dfca3bc656a4b38d8da25051173aaaafebbaff7ed27e3c30451148dba9` |
| `.agents/skills/unslop/SKILL.md`                                     | `c72b079bfa1f6be1df92c73f4599fee23d911270b7424aa92f5f03f1cf61fa56` |
| `docs/project.md`                                                    | `f8e512e64f05f03ce2eb78a854fb5e4b5ba707876feb9136fcfef8c939f892c8` |
| `docs/analyseplan-v2.2.md`                                           | `a08c2447ba33842e25a8c710217bc271a1528434f273de566a584da2ff3bfb0d` |
| `docs/profilregeln-v1.md`                                            | `13a59f9d0a3535d15577df9d7500cfffef379f5c90cda638543bd6c6d9a90da9` |
| `docs/abdeckung-v2.2.md`                                             | `ac945bf3ade6a068d87212eb9cc0ca4085770692e656905815fde2bc6539e244` |
| `docs/empirie-plan-v2.entwurf.md`                                    | `2b0cd26f8fba81bbf520b9ae3411d623f9299c9ff707aacf681bde4c65a0439f` |
| `data/analysevertrag.v2.entwurf.json`                                | `8e3d1c006bf8d7a568e37b358c3dce14e49b7feed6ae8a8d82f6f1f9e0935e6b` |
| `data/gruppenvertrag.v2.1.entwurf.json`                              | `9cd6b94e0f8edeb861d008a31c87439304cc71839a6348f1415b12ba30ef4702` |
| `data/politikprofil-v2.2.ergaenzung.json`                            | `f96fa667d78a84c9e039b7fad641616270ec4a57d207133624ca6a59d9733eb0` |
| `pipeline/v22/survey.py`                                             | `ef9011c5a9b9792373f7c9395d4e5db17a4381dab648480b2276ddac15a982bc` |
| `pipeline/v22/run_v22.py`                                            | `46f5b31e792d411182d123ca1f8d2042e02d52f8e48de39c1719c0ac0c5576ca` |
| `pipeline/v22/catalogue_v22.py`                                      | `c103dc092dbeb85ac557d39cd75bd0745fbbde0805ad8391a732b22cdefb6d83` |
| `pipeline/v22/test_survey.py`                                        | `dacdde363044981d575636447f6e206f89a0325353c8cc7b9a7898e1ca8ed011` |
| `pipeline/v22/test_run_v22.py`                                       | `5e1c4317e6f3d2d0aec62dacd672a019be8f95e36e403f5ac81ab95ff279db03` |
| `pipeline/v22/fetch_ess_metadata.py`                                 | `82952e3d660b75d4540b6b5a1a136e4dc7c26899294f0d96aeb22fd600bd6da5` |
| `pipeline/policy_reference_v2.py`                                    | `bc06e5c06935e3ff492543bdca986ebca823ec962eab8e6321ff2bf19ee83d2b` |
| `reports/claude/agenten/R4-profilform.md`                            | `8ea2b9ff837b6431d55acd051b45d5cba69eea3df1049878f748fe0655eddfa2` |
| `web/src/app/policy-draft/profile/profile-rules.ts`                  | `de5c1909621d5d5b4a164e8315fa302b0976ebacc0a126e26fdd3e655d06b589` |
| `web/src/app/policy-draft/profile/profile-structure.ts`              | `2ca2cae570714e0474fdff76355492e7ec179316bb64d9598ec8c780392bc622` |
| `web/src/app/policy-draft/profile/profile-engine.ts`                 | `1b11d598a1743b611d2359fd354a03fc8bd90522293c6fa89c23c928b0b897fa` |
| `web/src/app/policy-draft/profile/profile-engine.spec.ts`            | `0ae5022b17365a8a10051bc53dca6bc3b057e9db3ef02e510194d5cc2b0babf5` |
| `web/src/app/policy-draft/policy-catalogue.ts`                       | `78bd51603c0ebfce8966e34c99d80f1e08f3b63bde742b3283371747821c5e2d` |
| `web/src/app/policy-draft/public-catalogue.ts`                       | `7a6a3a1ffeba3a976f9c1e07fb1dbd061098e5c5ea347f80303f1750a0fdf8e6` |
| `web/src/app/policy-draft/public-catalogue-v22.ts`                   | `736f37d90c1005824b2958dac9b1e8fb7f4b965309a7ecfb7066363fb2ee5a9a` |
| `web/src/app/policy-draft/catalogue-types.ts`                        | `2599cfdf5c77ed912a85926b4e37a025b7d3661d1085749d27dbb5dc8be42822` |
| `package.json`                                                       | `451c9de3c5e0b647361bfbc749717712b895b822a04f84433288d19eb29a27f7` |
| `web/package.json`                                                   | `77db8383e6c64f65fe04638c46ba3b7f9b40040d95f0ad3ced1471fb475d60f7` |
| `outputs/loop/methods/SURVEY-MANUAL.pdf`                             | `87b0ea7088e0dfd587b4c4efacd38db68db8268a986a130c1a868ce2088bac2c` |
| `outputs/loop/breadth-data-001/sources/ess5-de-questionnaire.pdf`    | `24b5d2599e6d30dc02a6d835f5f80b5bcecf8f6014ee8f4670a703c25d3c3cbf` |
| `outputs/loop/breadth-data-001/sources/ess8-de-questionnaire.pdf`    | `977475c18d2adebea6ccb7695f377fb6ed500ef087b077086305f9a2e4a7b239` |
| `outputs/loop/breadth-data-001/sources/ess8-de-showcards.pdf`        | `dde02b5336b2d960c2900a8fcf5e2a0f0d254b46dcce1d9ffb785a830e096bc0` |
| `outputs/loop/breadth-data-001/sources/ess10-de-questionnaire.pdf`   | `158004a89b1821e5202e6faf3c2101eae5e56e794d7c3fdbc3dca1c9d67c8425` |
| `outputs/claude/sources/ess5-candidates.json`                        | `4b0247142d37697b4193e3373a37174849bcc16552d9764e34a51169170795a8` |
| `outputs/claude/sources/ess8-candidates.json`                        | `279f9c31b4236b71f4a820de7a2b519989ec796ad49ba4f2bde210c108d94168` |
| `outputs/claude/sources/ess10sc-candidates.json`                     | `2a5927d1ec1d322b2a127ff0c2c35862cbae8fc1ae39767aee410ff910ef8394` |
| `outputs/claude/sources/ess10sc-candidates-2.json`                   | `9ed9a9739dfe64b2cd8ebf2cc4cec8960ce29179b25d2013e90ff0dac53a038a` |
| `outputs/loop/breadth-access-002/sources/ess10sc-file-metadata.json` | `d9e6d606fb3b897d33d04f3247dbe5160d11f108a76fca6547a773e2c1ba0a57` |

Modell laut Laufzeit: OpenAI Codex über T3 Code, `gpt-6.1-sol`, Reasoning `medium`. Konkrete interne Revision und interne Anbietervorgaben unbekannt. Gleiche Modellfamilie wie der andere Codex-Prüfer; gemeinsame Fehlerquellen sind möglich.
