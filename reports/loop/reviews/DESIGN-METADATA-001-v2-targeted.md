# DESIGN-METADATA-001 v2: gezielte Nachprüfung Runde 1

Urteil: **BESTANDEN** im begrenzten technischen Umfang. Die vier Ursachen DM-R01–04 sind in v2 korrigiert. In den eigenen gezielten Gegenfällen wurde kein Restfinding festgestellt. Der Root kann genau den im v2-Vertrag begrenzten privaten Metadatenimport durchführen, ohne diesen technischen Schritt vom vollständigen Antwortanalyseplan abhängig zu machen.

Das ist keine empirische oder methodische Freigabe. Keine Antworten, tatsächliche A/B-Aufteilung oder wissenschaftliche Auswertung sind damit freigegeben. Das reale Ergebnis und die richtige Zuordnung des deutschen Designs wurden nicht geprüft.

## Prüfgrenze

Gezielte Nachprüfung durch denselben unabhängigen Codex-Prüfer aus derselben Codex-Modellfamilie wie der Root. Geprüft wurden der v2-Code, v2-Vertrag und die erhaltenen eigenen Erstbefunde. Keine anderen Reviewerberichte, Autorenbelege oder Autorenverteidigung gelesen. Der im Manifest genannte Autoren-Ergebnisordner wurde nicht geöffnet. Keine tatsächlichen Dateien unter Repository-`data/raw/` oder `data/local/` gelesen. Keine reale ESS-Ausführung, Installation, Authentifizierung, Commit oder weiterer Agent.

Eigene neue CSVs und künstliche CLI-Projekte liegen ausschließlich unter `outputs/loop/resume-design-meta-review-v2/`. Der Originalcode wurde unverändert importiert; für CLI-Fälle wurden `__file__` und der erwartete Hash auf das jeweilige künstliche Projekt abgebildet. Ein `Path.mkdir`-Hook protokollierte ausschließlich während der CLI-Aufrufe die tatsächlich versuchten Verzeichnisanlagen. Diese Anpassungen und künstlichen Inputdateien stehen im ausführbaren Prüfbefehl. V1 und Erstbericht wurden nicht verändert.

## Pins und eigene Ausführung

Manifest-SHA256 vor und nach Prüfung: `449aca3652efa5c2e7846ab56ad4402b8c5345abf3e39ff69a7cbbaad9aadcae`.

| Gebundene Datei | SHA256 vor und nach Prüfung |
| --- | --- |
| `pipeline/design_audit_v2.py` | `da9a7fbed839ce7d8bf708b6533bb521b7553ba6339a2343205cd0774eeab335` |
| `docs/designaudit-v2-vertrag.md` | `90a1dd9ca57bcc8b9ff58a157b4d38e9a49c9ca7c87e692b673ecbff0ba0c70d` |
| V1-Manifest | `00987d0f54b8cfcf8d313272893e542625854cf6d0dfdc60b780077f10581ddf` |
| Eigener Erstbericht | `9099938774e771f93e48af043dcf35a61e7b04def36bb15c5eda7827249802b4` |

Auch die drei ursprünglichen V1-Sachdateien stimmen weiterhin mit ihren V1-Pins überein. Der vollständige Nachweis steht in `outputs/loop/resume-design-meta-review-v2/pins.json`.

Eigener Befehl: `python outputs/loop/resume-design-meta-review-v2/check_synthetic.py`. 89 Assertions bestanden, keine fehlgeschlagen. Ein vollständiger Wiederholungslauf erzeugte ein bytegleiches `result.json`, SHA256 `ea726d667be8dd574aa287bf574b86fc195d7beffd4562f2f6d256e7a93583d2`. Skript-SHA256: `5b53e24c41fc85cfce4cbbc8a9dc98ccc05940ba2d1a3965125184419b493188`.

Die absichtlich fehlerhaften CLI-Läufe wurden tatsächlich ausgeführt und gestoppt: 13 unzulässige Pfad-/Ordner-/Quellfälle mit `ValueError`, ein abweichender Inputhash mit `ValueError`, ein ungültiges Gewicht mit Exitstatus 2 und `metadataUsable=false`. Diese erwarteten Fehlerstopps zählen als bestandene Prüfungen; es gab keinen unerwarteten Prüfungsabbruch.

## Ergebnisse zu den vier Ursachen

| Finding | Eigener Gegenfall und Ergebnis | Bewertung |
| --- | --- | --- |
| DM-R01 | `1.0000000000000001` wird jetzt für PSU und Stratum als `invalidDesignCode` zurückgewiesen. Vier benachbarte exakte Codes ab `9007199254740992` bleiben vier unterschiedliche Schlüssel, getrennt für beide Felder geprüft. Gleichwertige Integerdarstellungen `1`, `1.0`, `+1`, `1e0` werden korrekt zusammengeführt. | Korrigiert durch exaktes `Decimal`-Parsing, Code Zeilen 63–68. |
| DM-R02 | Neue Datei erhält unter `umask 022` `0600`, neuer fester Ordner `0700`. Ein vorhandener sicherer Ordner wird akzeptiert. Ein vorhandener `0755`-Ordner wird vor Metadatenzugriff und `mkdir` abgelehnt und bleibt `0755`. Auch ein absichtlich fehlerhaftes Metadatenergebnis bleibt `0600`/`0700`. | Korrigiert durch Vorprüfung und explizite Erzeugungsrechte, Code Zeilen 123–135. |
| DM-R03 | Ein eigener `read_bytes`-Hook liest die vier künstlichen Zeilen einmal, ersetzt anschließend die Quelldatei durch sieben Zeilen und liefert die ursprünglichen Bytes zurück. `audit()` interpretiert weiterhin vier Zeilen und meldet deren passenden Hash. Ein nachfolgender Lauf gegen die geänderte Quelle mit dem alten Hash stoppt. Ein künstlicher Rohdatenlink funktioniert mit passendem Bytehash. | Korrigiert durch genau eine unveränderliche Bytefassung für Hash und Parser, Code Zeilen 27–37. Zulässiger Eingabelink ist im v2-Vertrag ausdrücklich festgelegt. |
| DM-R04 | Traversalziel, fremder Zielordner, nicht genehmigter Unterordner, Dateisymlink, Ordnersymlink, gebrochener Ordnersymlink sowie fehlender, dateiförmiger und symlinkgebundener `data/local`-Eingang werden abgelehnt. Alle protokollierten `mkdir`-Listen bleiben dabei leer, Metadatenzugriffe bleiben null. Es entsteht keine Datei und kein Verzeichnis außerhalb der Ablagegrenze. | Korrigiert durch vollständige Vorprüfung vor dem einzigen `mkdir`, Code Zeilen 124–132. |

Eine vorhandene Ergebnisdatei wird ebenfalls vor `mkdir`/Metadatenzugriff zurückgewiesen und unverändert erhalten. Der feste Eingang akzeptiert keinen alternativen Pfad mit identischen künstlichen Bytes. Die bestehenden normalen Symlink- und Überschreibungsgrenzen bleiben damit erhalten.

## Erhaltene Feldgrenze und Fehlerstopps

Die positive Liste bleibt exakt `cntry`, `essround`, `edition`, `proddate`, `psu`, `stratum`, `anweight`, `pspwght`, `dweight`. Eine zusätzliche künstliche Spalte einschließlich Komma/Zeilenumbruch gelangt nicht ins Ergebnis. Der Code verarbeitet technisch die ganzen CSV-Bytes und interpretiert nur die ausgewählten neun Felder. Keine Personen-ID, Antwort-, Wahl- oder LR-Spalte wird ausgewählt; Originalschlüssel, Einzelzeilen und A/B-Zuordnungen werden nicht ausgegeben.

Globale Versionsabweichungen wurden für jedes der drei Felder in einer Nicht-DE-Zeile geprüft und führen jeweils zu `globalVersionMismatch`. Nicht eindeutiger Header, fehlende Pflichtfelder, fehlerhafte Zeilenbreite und fehlende Deutschlandzeilen behalten ihre Fehlergrenzen. Nicht positive, nicht endliche und ungültige Werte wurden für alle drei Gewichte geprüft; entsprechende Fälle sind unbrauchbar. Die üblichen ungültigen und fehlenden PSU-/Stratum-Werte werden weiterhin zurückgewiesen.

Verschachtelte PSU-Zählung, mehrfach verwendete PSU-Codes und Histogramm stimmen in den künstlichen gewöhnlichen Fällen. Vier PSUs liefern die vereinbarte technische Feasibilitätsmarkierung; drei und eine PSU in getrennten Strata liefern `false`. Daraus entsteht keine tatsächliche Aufteilung oder Ersatzregel. Gewichtsverhältnisse mit gewöhnlichen gleichen und unterschiedlichen Werten behalten ihre geprüfte Kennzeichnung.

## Begrenzte Freigabe

Keine Restfindings in dieser gezielten Nachprüfung. Zulässig ist ausschließlich der technisch begrenzte Import mit v2-Code, festem Hash/Eingang, vorhandenem unsymlinkgebundenem `data/local`, frischem Ergebnis direkt im festen privaten Unterordner und den geprüften Eigentümerrechten. Ein Fehlerergebnis oder Exitstatus 2 darf nicht als erfolgreicher Designnachweis verwendet werden.

Ob die echten Metadaten verwendbar sind und die Vier-PSU-Bedingung erfüllen, bleibt bis zur tatsächlichen Root-Ausführung offen. Auch ein technisch fehlerfreier Import bestätigt weder die richtige deutsche Designkodierung noch den vollständigen Analyseplan, Quellen-/Gesamtdesignvalidität oder empirische Güte. Diese Fragen wurden nicht in die gezielte Nachprüfung hineingezogen.
