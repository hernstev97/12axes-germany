# Review-Protokoll

Stand 2026-10-03: Der [dauerhafte Gesamtauftrag](../auftrag-life-93-2026-10-03.md) verlangt die Reviews aus LIFE-93 und wiederkehrende unabhängige Codex-Kontrollen. CodeRabbit bleibt technischer PR-Dienst. Die vorgeschriebenen Claude-Erstbewertungen und Claude-Reviews fehlen weiterhin. Ein vorhandener, angemeldeter Claude-CLI-Zugriff wurde geprüft, scheiterte aber am Providerlimit; [Beleg](../../reports/loop/claude-access.json). Dieses Format ersetzt keine getrennten Erstbewertungen.

## Auftrag an CodeRabbit

Prüfe den konkreten PR-Stand gegen `docs/pruefregeln.md`, den Analyseplan und die Beleg-IDs. Suche insbesondere nach unbelegten Schlussfolgerungen, Ergebniszugriff vor Festlegung der Regeln, irreführenden Freigaben, unberücksichtigtem Stichprobendesign und unterschiedlicher Behandlung politischer Gruppen. Prüfe Fundstellen soweit zugänglich. Ist eine Quelle oder erforderliche Prüfung nicht erreichbar, markiere sie offen.

Bewerte die Auswirkung auf eine konkrete Aussage oder Funktion. Allgemeine Empfehlungen ohne überprüfbaren Bezug begründen keine wissenschaftliche Freigabe. Liefere Findings nach folgendem Format; ein Kommentar ohne Finding ist kein Abnahmeprotokoll.

## Finding und Bearbeitung

| Feld         | Inhalt                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| ID           | Stabile ID, zum Beispiel `F-0001`; bei Folgerunden beibehalten.                                        |
| Gegenstand   | PR-URL, geprüfter Commit, Pfad/Fundstelle und gegebenenfalls Artefakt-Hash.                            |
| Umfang       | Technisch, methodisch, Quellen-/Lizenzprüfung oder Verständlichkeit.                                   |
| Bezüge       | Betroffene R-Regeln und Beleg-IDs.                                                                     |
| Problem      | Konkrete unzutreffende oder unzureichend gestützte Entscheidung/Aussage.                               |
| Nachweis     | Quelle, reproduzierbarer Test oder widersprüchliche Stelle. Vermutungen als solche kennzeichnen.       |
| Auswirkung   | Welche Entscheidung, Zahl oder Interpretation dadurch nicht trägt.                                     |
| Schwere      | Wesentlich/blockierend oder begrenzt; mit Begründung. Die Anbieter-Priorität allein entscheidet nicht. |
| Abhilfe      | Korrektur, zusätzliche Prüfung oder engerer Anspruch; erkennbares Kriterium für die Nachprüfung.       |
| Autorantwort | Annehmen, teilweise annehmen oder ablehnen, jeweils mit Beleg und vorgenommenen Änderungen.            |
| Nachprüfung  | Prüfer, Stand, Datum, Ergebnis und verbliebene Einschränkung.                                          |
| Status       | Offen, korrigiert und nachgeprüft, oder nachgeprüft gegenstandslos.                                    |

Wesentlich sind insbesondere Fehler, die Rechte, Datenzugriff, Aussagegehalt, Dimensionen, Gruppenzuordnung, Scores oder Unsicherheiten verändern. Diese blockieren den betroffenen Umfang. Ein stilistischer Befund kann begrenzt sein; unbelegte wissenschaftliche Versprechen sind kein bloßer Stilbefund.

Findings und vollständige Urteile liegen künftig unter `reports/reviews/` und werden vom Phasenbericht verlinkt. Modellkennung, verfügbare Anbieterangaben, Prompt, Input-Hashes und tatsächliche Prüfgrenzen werden protokolliert. Unbekannte Angaben bleiben unbekannt. Zugangsdaten und Rohdaten gehören nicht in diese Dateien.

Ein aktualisierter PR braucht eine erneute Prüfung der relevanten Änderungen und des aktuellen Stands. Ein grüner älterer Lauf, ein automatisch geschlossenes Kommentar-Thread oder die Autorantwort „erledigt“ genügen nicht. Nach zwei erfolglosen Runden gilt die engere Konsequenz aus R23/R24 und LIFE-93.

## Offene methodische Abnahme

Für die in LIFE-93 geforderten Urteilsaufgaben fehlen weiterhin überprüfbare Erstbewertungen aus einer anderen Modellfamilie und methodische Reviews. Der aktuelle Gesamtauftrag erlaubt die Vorbereitung der erforderlichen begrenzten Prüfpakete. Tatsächliche Erstbewertungen müssen R08 erfüllen; der GitHub-Review-Workflow und persönliche Setup-Schritte bleiben offene Voraussetzungen. Mehrere CodeRabbit-Kommentare oder Codex-Sessions werden nicht nachträglich als dieser Nachweis umbenannt.

## Lokales KI-Audit vom 2026-10-03

Der neuere ausdrückliche Auftrag autorisiert fünf isolierte Codex-Erstprüfer und einen anschließenden Juror. [Berichte und Aufträge](../../reports/audit-recherche/README.md) bleiben außerhalb der PR-Review-Historie erhalten. Dieses Audit ist ein tatsächlich ausgeführter begrenzter Review; es ersetzt weder CodeRabbit-Lauf noch andere Modellfamilie, Item-Erstbewertungen oder empirische Abnahmen. Die ursprünglichen Berichte werden nicht nach Korrekturen umgeschrieben.
