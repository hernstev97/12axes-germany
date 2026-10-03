# COMPREHENSION-V2-WIP

2026-10-03. Eigenständiger Vorbereitungsbericht; keine menschlichen Befunde und keine Durchführung, Empirie- oder Releasefreigabe.

Neu erstellt wurde `docs/verstaendnistest-v2.entwurf.md`, Entwurf 0.1. Er enthält sechs feste Fragen für fünf reale Personen: vier Bedeutungsfragen sowie getrennte Fragen zu Unklarheit und möglicher Benachteiligung. F1–F4 haben vorab festgelegte Kernpunkte, fünf Urteilsarten und zehn konkrete Fehlinterpretationskennungen. Es gibt keinen Gesamtwert und keinen persönlichen Bestanden-Status.

Die Fragen behandeln Originalkategorien, Themen als Ordnung, getrennte historische Studie-/Itemreferenzen und ihren gültigen gewichteten Nenner, lokale Skips und historische Missing-Gründe. Die Grenzen zu heutiger Norm, gemeinsamer latenter Position, persönlicher Unsicherheit und Partei-Gesamtübereinstimmung sind ausdrücklich enthalten. Eine fehlende Referenz liefert keine Zahlen und ersetzt keine eigene Antwort. Die gültige Originaloption „Nicht stimmberechtigt“ wird nicht zum Skip umgedeutet.

Eine deterministische Zustandsvorführung nutzt erste/letzte Originalkategorien sowie einen übersprungenen und einen unberührten Zustand, ohne politische Personenbeschreibung oder erfundene empirische Zahlen. Sie reicht nicht zur Prüfung angezeigter Anteile: F2 benötigt später eine tatsächlich getrennt freigegebene historische Referenz in der von Steven gebilligten, fest protokollierten UI. Fehlende Voraussetzungen werden nicht durch das technische Beispiel ersetzt. Layout, Farben, konkrete UI und deren Billigung bleiben außerhalb dieses Auftrags.

Zwei von fünf Personen mit derselben belegten Fehlinterpretation lösen eine Überarbeitung aus. Unter einer groben Kennung zusammengefasste unterschiedliche Fehler werden dafür nicht gleichgesetzt. Ein schweres Einzelmissverständnis wird unabhängig von der Mehrheit geklärt. Diese qualitativen Regeln sind keine statistischen Gütegrenzen. F5/F6, fehlende oder nicht einordenbare Erklärungen und offene Codierungen bleiben getrennt sichtbar. Namens-, Kontakt-, politische Antwort- und Parteifelder sind nicht vorgesehen; in diesem Arbeitsschritt wurde nichts erhoben.

## Tatsächlich gelesener Kontext und Bytepins

Handbuch, Projektauftrag und historischer Entwurf wurden vollständig gelesen, ebenso der reine Exportvertrag. Der öffentliche Katalog wurde vollständig als JSON geladen; gelesen wurden Studien-/Quellenmetadaten, alle 43 Wortlaute, Einleitungen, Situationen, Antwortformate und Kategorien sowie Missing-, Modus-, Routing- und Begrenzungsauszüge. Wiederholte Inhalte wurden dedupliziert ausgegeben; gekürzte große Tool-Ausgaben wurden für die benötigten Inhalte durch kleinere Auszüge ergänzt. Keine im Katalog verlinkten Originalcaches oder tatsächlichen Referenzexporte wurden geöffnet. Damit wird keine neue Originalquellenprüfung behauptet.

| Unveränderter Kontext | Bytes | SHA-256 vor und nach |
| --- | ---: | --- |
| `docs/handbuch.md` | 36004 | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` |
| `docs/project.md` | 9151 | `50fd74dc5612293f22591e679856dbb09745ef2ff9a217ff5583b219cf224328` |
| `docs/verstaendnistest.entwurf.md` | 7330 | `3264a72db722ac573595bcbcc8a03e299727aaa184abe6b31a60c74e2212c1a3` |
| `data/politikprofil-v2.fragen.entwurf.json` | 389900 | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` |
| `pipeline/policy_export_v2.py` | 24107 | `27b225b5975f0c321f08adbfa7ccab4e03dae8421f3987d0e104cf4945d0437a` |

Entwurf: 15633 Bytes, 83 Zeilen; SHA-256 `28312072050bc6914b33e8ac39fe7aab3575621039ede8491844649a0d7ed9c3`.

Der neue Plan übernimmt die historische Dimensionen-/Intervalle-/Wählergruppenlogik nicht. Er benennt die Abweichung von älteren Handbuchbegriffen und folgt dem aktuellen Auftrag zu getrennten Kategorien. Historische Dateien wurden nicht korrigiert oder umformatiert. Der katalogisierte ESS8-München-Ausfall, ursprüngliche Erhebungszeit/Modus und die begrenzte B25-Administrationsbindung bleiben Voraussetzungen der später gewählten Fassung. Der Katalogstatus `DRAFT_NOT_GATE` ist keine Nutzungserlaubnis.

## Eigene Prüfungen und Prozesse

Reine lokale Lese- und Strukturaufgaben, keine Netzaufrufe. Ein begrenzter Katalog-/Zeitaufruf mit `PYTHONDONTWRITEBYTECODE=1 python` endete am 2026-10-03T14:27:00.759049+00:00, PID 3110667, Exit 0; er bestätigte die dokumentierte Katalogstruktur von fünf Studien, 43 eindeutigen IDs und acht Themen sowie leere Nicht-gestellt-Codelisten. Das sind Metadaten, keine Antwortbefunde.

Die eigene Dokumentprüfung lief mit `PYTHONDONTWRITEBYTECODE=1 python`, PID 3125302, UTC 2026-10-03T14:29:01.622169+00:00 bis 14:29:01.624147+00:00, tatsächlicher Exit 0. Geprüft wurden sechs einmalige Fragenzeilen F1–F6, fünf Bewertungsetiketten, zehn einmalige Fehlerkennungen, auflösbare lokale Links, UTF-8/LF/Schlusszeilenumbruch sowie Gleichheit der fünf Vor-/Nachpins. Nachweis: `outputs/loop/comprehension-v2-wip/structure-and-pin-check.json`. Diese Prüfung betrifft Dokumentstruktur, nicht menschliches Verständnis.

Alle eigenen Aufrufe sind abgeschlossen; kein eigener Server oder Hintergrundprozess wurde gestartet. Kein Git, pnpm, Browserlauf, Installations-, Auth-, Kontakt- oder Agentenauftrag. Keine Antworten, Roh-/lokalen Daten, Header, Zustands-/Handoffdateien, Reviewerberichte oder neuen Empiriedateien gelesen oder erzeugt. Kein gesamter 22-Pin-Paketaudit; die Gleichheitsbehauptung betrifft die fünf oben benannten Kontexte. `unslop` wurde auf den neuen Text angewandt. Keine Bestandsdatei wurde geschrieben.

## Offene menschliche Voraussetzungen

Steven muss UI und Vorführung auswählen und billigen. Root muss die tatsächlichen Quellen-/Review-/Exportpins und zulässige Nutzung separat binden. Noch fehlen die fünf Personen und ihr Einverständnis, die tatsächlichen Erklärungen, die begründete Auswertung, gegebenenfalls eine überarbeitete und erneut geprüfte Version sowie jede spätere Freigabeentscheidung. Fünf zutreffende Erklärungen oder KI-Übereinstimmung wären weder ein Neutralitätsbeweis noch eine methodische oder Produktfreigabe.
