# Öffentliche C-Quellenannotation nachbauen

Das Skript bildet die historische C-v2-Dokumentannotation nach. Es analysiert keine ESS-Antworten und prüft weder Itemeignung noch ein Messmodell. Die unabhängige Prüfung dieses neuen ausführbaren Nachbaus steht zunächst aus; maßgeblich sind sein Prüfmanifest und die späteren Berichte.

Voraussetzungen sind Python 3 mit Standardbibliothek, Popplers `pdftotext` und Netzverbindung zu den drei offiziellen, im Skript festgelegten öffentlichen PDF-Adressen. Keine Anmeldung oder zusätzlichen Python-Pakete sind erforderlich. Im Projektverzeichnis ausführen:

```sh
python3 pipeline/reproduce_c_annotation.py --output-dir outputs/public-reproduction/mein-c-v2-lauf
```

Das neue Ziel enthält `annotation.json`, `reproduction.json`, die drei heruntergeladenen Original-PDFs und die eigenen Geometrie-/Text- und Prüfoutputs. Vorhandene Zielverzeichnisse werden nicht überschrieben. Ein erneuter Lauf braucht einen neuen Namen. Absolute Pfade, `..`, andere Ausgabeoberverzeichnisse und erkannte symbolische Links werden abgewiesen. Das ist eine begrenzte Pfadprüfung, keine Betriebssystem-Sandbox oder Garantie gegen gleichzeitige Dateimanipulation.

Die CSV und ihre Provenienz müssen mit den im Skript gebundenen öffentlichen Eingabehashes übereinstimmen. Jeder Download wird vor der Verarbeitung gegen seinen SHA-256 geprüft. Eine geänderte Quelle führt zum Abbruch; ihr Hash wird nicht automatisch übernommen. Der erwartete Annotationhash ist `70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e`. Die heruntergeladenen Fragebogen- und Listenbytes sowie Codebook-Ausgabe 4.1 ersetzen keinen Abgleich mit Datenedition 4.2.

`annotation.json` enthält **historische Metadaten**, darunter die ursprünglichen Autoren-/Korrekturrollen, Zeitangaben, damaligen Prüfstatus, Zugriffserklärungen und ursprünglichen Cachepfade. Diese Angaben werden für den exakten historischen Nachbau erhalten. Sie beschreiben nicht den neuen ausführenden Menschen oder Prozess und sind keine heutige Freigabe. Tatsächliche Downloadpfade, Zugriffszeiten, Hashes und Laufstatus stehen separat in `reproduction.json`. Die ursprünglichen Cachepfade in der Annotation sind keine beim Nachbau benötigten Eingaben.

Nach angelegtem Ziel wird auch ein Fehler im Laufprotokoll festgehalten. Frühe Pfad- oder Eingabehashfehler vor der Zielanlage werden auf stderr ausgegeben und erzeugen kein Zielprotokoll. Ein positiver Laufstatus bestätigt nur diesen Nachbau. Die sechs tatsächlich ausgeführten eigenen Gegenfälle und die beiden eigenen Nachbauten sind im [Autorenbericht](../reports/loop/authors/REPRO-003-C.md) beschrieben; sie sind kein allgemeiner semantischer Validator.

Die korrigierte Protokollfassung erfasst jeden Downloadversuch vor dem Zugriff mit Dateiname, URL, erwartetem Hash und Beginn. Sie ergänzt Ende und Erfolg oder Fehler sowie nur die tatsächlich bekannten HTTP-, Dateipfad- und Hashangaben. Unbekannte Werte bleiben `null`; `completeFileWritten` bezeichnet ausschließlich einen vollständig abgeschlossenen Dateischreibaufruf. Auch ein HTTP-Fehler vor dem Download bleibt damit einer konkreten Quelle zugeordnet. Der [Korrekturbericht](../reports/loop/authors/REPRO-003-C-korrektur.md) trennt eigene Nachtests von der noch erforderlichen unabhängigen Nachprüfung. Die ursprüngliche Fassung und Erstberichte bleiben erhalten.

Originaldokumentation und Daten haben unterschiedliche Bedingungen; siehe [Lizenzakte](lizenzen.md). Das Skript lädt öffentlich bereitgestellte Dokumentation lokal nach. Die PDF-Dateien und eigenen Laufoutputs gehören nicht in Git. Eine konkrete spätere Veröffentlichung von Annotationen, Modell- oder Webexporten braucht die vorgesehenen getrennten Abnahmen.
