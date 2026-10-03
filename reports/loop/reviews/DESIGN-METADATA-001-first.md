# DESIGN-METADATA-001: unabhängige technische Erstprüfung

Urteil: **NICHT_BESTANDEN** für die unveränderte Prüffassung v1. DM-R01 verletzt den festgelegten Vertrag für ganzzahlige Designcodes und kann die PSU-Aggregation ändern. Damit empfehle ich den tatsächlichen Import mit dieser Fassung noch nicht.

Ein auf die neun Felder begrenzter technischer Metadatenimport muss den vollständigen Antwortanalyseplan nicht ersetzen und wird hier auch nicht davon abhängig gemacht. Nach Korrektur und erneuter Paketprüfung kann seine technische Freigabe vor dem vollständigen Antwortanalyseplan liegen. Antwortanalysen, A/B-Aufteilung, empirische Entwicklung und methodische Gesamtfreigabe bleiben offen.

## Umfang und Unabhängigkeit

Frischer Codex-Subagent derselben Codex-Modellfamilie wie der Root, getrennte Prüfinstanz. Das ist keine Gegenprüfung durch eine andere Modellfamilie. Urteil ohne andere Reviewerberichte, Autorenverteidigung oder manifesteigene synthetische Autorenbelege.

Gelesen wurden das zugewiesene Manifest sowie ausschließlich dessen drei gebundene Sachdateien: `pipeline/design_audit.py`, `docs/designaudit-vorabvertrag.md` und `reports/phasen/00-dateieingang-2026-10-03.md`. Zusätzlich wurde der verpflichtende Schreibskill `unslop` für den Bericht gelesen; daraus wurden keine sachlichen Prüfkriterien abgeleitet. Keine Repository-Dateien unter `data/raw/` oder `data/local/` geöffnet. Keine reale ESS-Ausführung, kein Claude/Auth/Install/Commit, kein weiterer Agent. Die im Vertrag genannten methodischen Quellendateien wurden nicht geöffnet.

Alle Gegenfälle stammen aus eigenen künstlichen CSVs unter `outputs/loop/resume-design-meta-review/`. Für CLI-Prüfungen wurde `__file__` im importierten Modul auf einen dortigen künstlichen Projektpfad gesetzt und der erwartete Eingabedigest durch einen Wrapper auf den Digest der jeweiligen künstlichen Datei gesetzt. So liefen die Originalkontrollen von `main()` gegen synthetische Unterordner, ohne den echten Eingabepfad oder dessen Bytes zu öffnen. Die gemeinsame Code- und Forschungsfassung wurde nicht verändert.

## Pins und Reproduzierbarkeit

Manifest-SHA256 vor und nach Prüfung: `00987d0f54b8cfcf8d313272893e542625854cf6d0dfdc60b780077f10581ddf`.

| Gebundene Datei | SHA256 vor und nach Prüfung |
| --- | --- |
| `pipeline/design_audit.py` | `0a5ec52ec839c56fba55811b53671ec553dcd12374ccbf880f04574887281c62` |
| `docs/designaudit-vorabvertrag.md` | `d1e1e3047b053531db52524b2f7eba9f422909c30cec3c59831af40b8d1b9e79` |
| `reports/phasen/00-dateieingang-2026-10-03.md` | `814513213d10957063dc6a26a7f4d9c0086b75c99262c86b2993ac2075d46621` |

Prüfbefehl: `python outputs/loop/resume-design-meta-review/check_synthetic.py`. 62 Assertions, davon 60 bestanden und zwei fehlgeschlagen. Beide Fehler gehören zu DM-R01. Ein weiterer vollständiger Lauf ergab ein bytegleiches `result.json`, SHA256 `081a631ee8838ca5b6f05eac0e9b0156592f3b77201a84ce7903015329aa5e25`. CLI-Dateigrenzen und die kontrollierte Austauschsimulation stehen zusätzlich als Beobachtungen im Ergebnis, nicht als bestandene Assertions. Pins sind in `outputs/loop/resume-design-meta-review/pins.json` festgehalten.

## Bestätigtes Verhalten

- `FIELDS` enthält genau Land, drei globale Metadaten und fünf Design-/Gewichtsfelder. Der Code wählt keine Personen-ID, Antworten, Wahl- oder LR-Felder aus. Der CSV-Parser verarbeitet ganze Datensätze. Ein künstliches zusätzliches Feld einschließlich Komma/Zeilenumbruch gelangt weder als Feldname noch als Wert in das Ergebnis.
- Eine Digest-Abweichung, nicht eindeutiger Header und fehlende Pflichtfelder werden zurückgewiesen. Änderungen jedes globalen Versionsfeldes in einer Nicht-DE-Zeile erzeugen `globalVersionMismatch`. Eine fehlerhafte Zeilenbreite und fehlende Deutschlandzeilen verhindern `metadataUsable`.
- Null, negative Werte, NaN, Unendlich, Leerstring, ungültiger Text und Überlauf werden für alle drei Gewichte zurückgewiesen. Normale nicht positive, nicht ganzzahlige und nicht endliche Designcodes erzeugen Fehler. Fehlerausgabe im CLI hat `metadataUsable=false` und Exitstatus 2.
- Die Aggregation gewöhnlicher Codes zählt PSU innerhalb Stratum. Ein gleicher PSU-Code in zwei Strata wird als zwei verschachtelte Einheiten und als ein mehrfach verwendeter Code erfasst. Die Histogrammprüfung mit drei und einer PSU ergibt korrekt `splitFeasible=false`. Vier PSUs ergeben `true`. Es wird keine A/B-Zuordnung, kein Seed und keine Ersatzaufteilung ausgegeben.
- Ein Ergebnisziel außerhalb von `data/local`, ein vorhandenes Ergebnis, eine Ergebnisdatei als Symlink sowie ein symlinkgebundener Ergebnis-Elternpfad werden zurückgewiesen. Ein vorhandenes Ergebnis bleibt unverändert. Der geforderte Eingabepfad ist fest; ein alternativer Dateipfad wird trotz passender künstlicher Bytes zurückgewiesen.

Die Gewichtskonstantenprüfung funktioniert für die geprüften gewöhnlichen gleichen und unterschiedlichen Verhältnisse. Sie bestätigt keine richtige Zuordnung des deutschen Designs. Die hier bestätigten Prüfungen sind technische Codebeobachtungen an künstlichen Daten.

## Findings

### DM-R01: `float` verändert Designcodes vor Gültigkeitsprüfung und Aggregation

Erheblicher Vertragsfehler, freigabeblockierend. Beleg: `pipeline/design_audit.py:57-61` und `:79-80`; Vorabvertrag Zeilen 7 und 9. Der Code prüft die gerundete `float`-Darstellung und normalisiert danach mit `int`.

Eigener Gegenfall `fractional_code_must_reject`: `psu=1.0000000000000001` ist mathematisch nicht ganzzahlig. Der Code akzeptiert ihn als `1`; `errors={}` und `metadataUsable=true`. Eigener Gegenfall `exact_integer_cluster_identity`: die vier exakten positiven Integercodes `9007199254740992`, `9007199254740993`, `9007199254740994`, `9007199254740995` werden zu drei PSUs. Die gewünschte Vier-PSU-Bedingung wird dadurch fälschlich als nicht erfüllt ausgegeben.

Auswirkung: Ein ausdrücklich zugesicherter Fehlerstopp fehlt, und verschiedene PSU- oder Stratum-Schlüssel können zusammenfallen. Der tatsächliche deutsche Wertebereich wurde nicht gelesen; daraus wird kein realer ESS-Befund behauptet.

Prüfbare Korrektur: Designcodes exakt parsen, beispielsweise mit `Decimal`, auf Endlichkeit, Positivität und Gleichheit mit ihrem exakten ganzzahligen Wert prüfen und erst danach nach `int` normalisieren. Alternativ einen ausdrücklich begründeten engen Eingabevertrag ohne Rundung definieren. Der nicht ganzzahlige Gegenfall muss stoppen; vier große exakte Integercodes müssen vier verschiedene PSUs bleiben oder durch eine explizite Bereichsregel mit Fehler stoppen. Dieselben Regeln auf `stratum` anwenden.

### DM-R02: Private Ablage ist geprüft, private Dateirechte sind nicht zugesichert

Begrenzter Befund; kein behaupteter Zugriff auf reale lokale Dateien. Beleg: `pipeline/design_audit.py:116-125` und `cliObservations.good` im eigenen Ergebnis. Unter üblicher `umask 022` erzeugt der CLI die Ergebnisdatei mit `0644`, die künstlich erzeugten Verzeichnisse sind entsprechend nicht auf den Eigentümer beschränkt.

Auswirkung: Die geprüfte Pfadgrenze verhindert öffentliche Ablage außerhalb `data/local`. Der Ausdruck „private“ garantiert allein durch diesen Code keine Beschränkung auf den Dateieigentümer. Ob reale Elternverzeichnisse bereits ausreichend geschützt sind, wurde nicht geprüft. Der Vertrag nennt keine konkrete POSIX-Berechtigung; dieser Befund wird deshalb nicht als weiterer erheblicher Parserfehler gewertet.

Prüfbare Korrektur oder Ausführungsvoraussetzung: Vor dem tatsächlichen Lauf eine Eigentümerbeschränkung durch `umask 077` und geeignete Elternrechte sichern, oder Datei/Verzeichnis im Code explizit mit `0600`/`0700` erzeugen. Synthetischen CLI-Lauf unter `umask 022` wiederholen und die zugesicherte Beschränkung prüfen. Bis dahin darf „privat“ im Bericht nur die nachgewiesene Ablage- und Veröffentlichungsgrenze bezeichnen.

### DM-R03: Hashprüfung und Interpretation können unterschiedliche Dateistände treffen

Bedingter Integritätsbefund. Beleg: `pipeline/design_audit.py:24` und `:32`. Digestprüfung und CSV-Interpretation öffnen den Pfad separat. In der eigenen kontrollierten Austauschsimulation ruft der Hook den echten Digest auf, ersetzt danach ausschließlich die künstliche Datei und kehrt zum Original-`audit()` zurück. Das Ergebnis meldet den alten Digest, liest sieben statt vier Deutschlandzeilen und setzt `metadataUsable=true`. Dies ist eine nachgewiesene Eigenschaft bei Dateiaustausch, keine Behauptung über eine reale Änderung.

Auswirkung: Ohne gesicherte Unveränderlichkeit zwischen den beiden Öffnungen belegt `inputSha256` nicht zuverlässig die interpretierten Bytes. Auch ein symlinkgebundener fester Eingabepfad wird gegenwärtig akzeptiert, wenn seine Zielbytes den Digest erfüllen; der Code verspricht keine Symlinkfreiheit der Eingabe.

Prüfbare Korrektur oder Ausführungsvoraussetzung: Den interpretierten Bytestand selbst hashen, beispielsweise eine einmal gelesene unveränderliche Bytekopie hashen und daraus parsen, oder vor dem Lauf einen tatsächlich unveränderlichen Input sicherstellen. Eine bloße nachträgliche Hashprüfung des Pfadnamens deckt nicht jeden zwischenzeitlichen Austausch ab. Der Austauschgegenfall muss dann stoppen oder ausschließlich die geprüften vier Zeilen lesen. Falls die Eingabe symlinkfrei sein soll, dies explizit prüfen und mit einem künstlichen Quellsymlink testen. Dieser Befund verlangt keine zusätzliche wissenschaftliche Prüfung.

### DM-R04: Abgelehnter Traversalpfad erzeugt zuvor Verzeichnisse außerhalb der privaten Ablage

Geringer technischer Nebenwirkungsfehler, nicht eigenständig freigabeblockierend für den vorgeschlagenen festen Ergebnisnamen. Beleg: `pipeline/design_audit.py:118-122` und `cliObservations.parent_traversal`. Das künstliche Ziel `data/local/../../outside_created/deeper/result.json` wird vor dem Schreiben zurückgewiesen. `mkdir` hat aber bereits `outside_created/deeper` außerhalb von `data/local` angelegt. Keine Ergebnisdatei entkam der Ablagegrenze.

Prüfbare Korrektur: Normalisierte Pfadzugehörigkeit und Symlink-/Traversalgrenzen vor `mkdir` prüfen. Gegenfall wiederholen; weder Datei noch Verzeichnis außerhalb der zulässigen Ablage dürfen entstehen. Daraus wird kein Datenschutzvorfall und keine wissenschaftliche Sperre abgeleitet.

## Begrenzte Antwort auf die Freigabefrage

Die Beschränkung auf technische Designmetadaten ist im Paket nachvollziehbar. Der offen gebliebene vollständige Antwortanalyseplan ist für diese Prüfung kein eigener Ablehnungsgrund. Die unveränderte v1 erhält wegen DM-R01 dennoch keine Freigabe. Nach Korrektur und erneuter Prüfung bleibt ein Import nur als privater technischer Voraussetzungstest zulässig; die aus DM-R02 und DM-R03 benannten tatsächlichen Ausführungsvoraussetzungen müssen gesichert oder die Implementierung entsprechend korrigiert sein. DM-R04 ist für einen festen normalen Ergebnisnamen kein Hindernis.

Keine Aussage zur empirischen Tragfähigkeit des deutschen Designs, PPS-WOR-Inferenz, Messmodell, Dimensionen, Itemauswahl, Scores oder methodischer Gesamtvalidierung. Keine reale ESS-Datei ausgeführt und keine Prüfung durch CodeRabbit oder technische CI als methodische Abnahme ausgegeben.
