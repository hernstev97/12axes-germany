# Konkreter Gestaltungsentwurf v2

Stand: 2026-10-03. Autor: Codex, gpt-6.1-sol, ultra. Unveröffentlichter Vorschlag für menschliche Gestaltungs- und Verständnisabnahme, kein freigegebener Test und kein Forschungsentscheid.

Arbeitsverzeichnis: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`.

## Artefakt und gelesene Grundlage

Der statische Entwurf liegt vollständig unter `outputs/loop/policy-ui-design-v2/`. Einstieg: `index.html`. Root kann genau diesen Ordner mit seinem vorgesehenen statischen Server auf Port 4313 bereitstellen. Alle automatisch geladenen Skripte, Styles und Schriften liegen innerhalb dieses Ordners und verwenden relative Pfade. Für die geplante Browserprüfung ist bei dieser Ordnerbindung `http://127.0.0.1:4313/index.html` der Einstieg; ein Server wurde hier nicht gestartet.

Das aktuelle `docs/handbuch.md` wurde erneut vollständig gelesen, alle 378 Zeilen. Berücksichtigt wurden auch der bereits gelesene `unslop`-Skill und die vorhandene globale Gestaltung in `web/src/styles.scss`. Fachinhalt stammt aus dem öffentlichen `data/politikprofil-v2.fragen.entwurf.json`. Seine SHA-256-Bindung lautet `38e68b2edfc0ecf9c0b1071bf7283d0ff2f366d3492afd0e71388432415195b9`; der abschließende Abgleich ergab denselben Wert. Der Katalog ist ein Entwurf und keine Zugriffserlaubnis. Keine Rohdateien, Header, lokalen Antwortdaten, Reviewerberichte, empirischen Ergebnisse oder Koordinations-/Handoffdateien wurden herangezogen.

`prepare.py` projiziert ausschließlich öffentliche Instrumenttexte, gültige Originalkategorien, Quellen, Studienmetadaten und die B1–B12-Gruppe nach `catalogue.js`. Missing-Code-Listen, Zugriffs-/Gatezustand und Samplingstatistiken werden nicht in das Artefakt übernommen. Eine abgeleitete Frage-/Kategorie-Datei enthält keine Befragtenantworten. Die vorhandene Libre-Baskerville-WOFF2 und ihr Lizenztext wurden unverändert in den eigenen Assetordner kopiert. `foundation.css` übernimmt das vorhandene globale Stylesheet; lediglich die Paket-Fontimporte entfallen zugunsten der lokalen Fontdatei. `source-binding.json` hält diese Herkunft und Hashes fest.

## Fragenablauf und konkrete Entscheidungen

Der Entwurf öffnet unmittelbar die erste Frage. Es gibt keine Startaufforderung eines veröffentlichten Tests. Kopf und beide Ansichten tragen den Status „Gestaltungsentwurf · Prüfung ausstehend“. Die Standardformel zum nicht validierten, nicht wissenschaftlich geprüften Projekt steht sichtbar im Fußbereich.

Eine Einzelansicht zeigt Originaleinleitung, gegebenenfalls Situation, Fragestamm, Frage und alle gültigen Originalkategorien. Papier-/Interviewanweisungen erscheinen mit ihrer Katalogherkunft in den Quelldetails. Politische Formulierungen und Kategorien werden nicht umgeschrieben. Die Originalanker und Zwischenkategorien bleiben sichtbar. Zahlen in Antwortlisten sind als Kategorien bezeichnet, nicht als Punkte. Natives Radioverhalten gibt genau eine Auswahl je Frage vor.

Die Sitzung kennt drei passive Zustände:

- **Unberührt:** keine Radioauswahl und kein bewusstes Überspringen. Der Fortgang ohne Auswahl belässt diesen Zustand.
- **Beantwortet:** eine gültige Originalkategorie ausgewählt. Änderungen ersetzen die frühere Auswahl in der flüchtigen Sitzung.
- **Übersprungen:** ausdrücklich „Frage überspringen“ gewählt. Ein optionaler Sitzungsgrund nennt keine Angabe, Unwissen oder Ablehnung einer Antwort. Diese Gründe werden nicht zu Studienmissing umkodiert.

Zurück erhält den Zustand. Der einzige primäre Fortgang führt zur nächsten Frage, bei der letzten Frage zum Ergebnisentwurf. Eine Frage lässt sich später über Übersicht oder Ergebnis erneut öffnen. Die Übersicht enthält alle 43 Originalfragen samt Zustand. Direkte Sprünge sind ausdrücklich Entwurfsprüfung, keine Behauptung einer ursprünglichen Studiendurchführung. Vorheriges Antworten und Überspringen können durch eine neue Radioauswahl verändert werden; die Sitzung wird weder gespeichert noch exportiert.

Der normale Ablauf folgt dem Katalog mit einer erforderlichen Ausnahme: B12 `keydec` wird unmittelbar hinter B11 eingefügt. Dadurch bleibt die vollständige B1–B12-Gruppe in Originalreihenfolge zusammen. Ihre vollständige Einleitung und Skalenanker stehen in jeder betroffenen Einzelansicht. B12 zählt im Ergebnis primär zu europäischer Integration. Der Hinweis auf den bewusst ausgelassenen Performanceblock B13–B24 ist vor der Auswahl sichtbar. Die neue Einzelansicht und der geänderte Gesamtfragebogenkontext werden benannt.

B25 übernimmt den gebundenen Papierwortlaut und beide Alternativen. Die ursprünglichen Papierwege nach B26 beziehungsweise B28 sind als Originalkontext erläutert. Der Entwurf geht nach B25 unabhängig von der Auswahl zur nächsten gewählten Frage und lässt B26–B29 aus. Das ist ein ausdrücklich neuer Entwicklungsfortgang. Die ursprüngliche operative Weiterleitung oder CAWI-Äquivalenz gilt dadurch nicht als nachgewiesen.

## Ergebnis und Quellen

Der Ergebnisentwurf zeigt sämtliche 43 Einzelangaben unter den acht vorhandenen Themenrubriken. Auch unberührte und übersprungene Angaben bleiben sichtbar. Bei beantworteten Fragen stehen die tatsächlich gewählte Originalkategorie und eine konkrete, eng auf den Gegenstand bezogene eigene Erläuterung. Es werden keine thematischen Gesamtaussagen aus mehreren Antworten berechnet. Die Erläuterungen sind Bestandteil dieses Entwurfs und brauchen die inhaltliche sowie menschliche Prüfung.

Besondere Grenzen bleiben erkennbar: Wichtigkeit eines Demokratieprinzips ist keine Umsetzungsbewertung; Familienpolitik behält den Doppelverdiener-/Elternzeitkontext; der historische Strafvergleich bezeichnet die damalige Praxis; hypothetische EU-Nichtwahl, ungültiger/leerer Stimmzettel und Nichtberechtigung bleiben gültige Originalkategorien. Nominale Sozialleistungsbedingungen werden nicht in eine Zeitposition umgerechnet.

Jeder Ergebnisblock enthält „Historische Referenz noch nicht freigegeben“. Es gibt keine Vergleichszahlen, Beispielverteilungen, Scores, Polung, persönlichen Intervalle, Links-/Rechtspositionen oder Zuordnungen zu Parteien und Personen. Ein späterer Pfad `actualReviewedReferences` müsste als eigener geprüfter Import-/Exportvertrag gebunden werden. Dieser Entwurf implementiert weder diesen Pfad noch einen Zahlenersatz oder eine automatische Freischaltung.

Jede Frage und jede Ergebnisangabe bietet Ausgabe, deutschen Erhebungszeitraum, Originalmodus, deklarierte Population, Dokument-/Daten-DOIs, konkrete PDF-Fundstellen, getrennte Dokumentations- und Datenlizenzen sowie die originale Zitationsvorgabe aus dem Katalog. Die Abweichung der ESS10-SC-Zitation zwischen 3.2-Bindung und teilweise überliefertem 3.1-Text wird sichtbar erhalten. Deklarierte Population wird nicht als nachgewiesene erreichte Abdeckung bezeichnet. Historische Referenzen werden nicht als aktuelle 2026-Norm ausgegeben. Die Quellenlinks sind passive Links; keine Quelle wurde durch diesen Auftrag im Netz abgerufen.

## Gestaltung, Alternative und nötige Abnahme

Papier-/Ink-Werte, Libre Baskerville, Zwölfspaltenraster, Dokumentabstände, Linien, rechteckige Schaltflächen und Fokusrahmen stammen aus der bestehenden Gestaltung. Keine Gemälde, neuen Farben, Karten, Icons, 3D oder Animationen. Die eigenen ergänzenden Styles umfassen 3209 Bytes. Die veränderte Wortmarke bleibt bei den bestehenden Schriftgewichten. Die neue Fragen- und Ergebnisanordnung ist nur ein Vorschlag und ändert das Handbuch nicht.

Die Einzelansicht macht lange Antwortlisten und ihre vollständigen Anker auf kleinen Breiten bedienbar, verändert aber die Präsentation gegenüber einem Originalmatrixblock. Als zu entscheidende Alternative kann B1–B12 gemeinsam auf einer Seite stehen. Ob die Einzelansicht Kontext und Lesbarkeit ausreichend erhält, muss die menschliche Verständnisprüfung klären. Das Ergebnis listet sämtliche Originalangaben statt einer zusammenfassenden Themenbewertung. Eine kürzere Ergebnisdarstellung wäre eine weitere menschliche Gestaltungsentscheidung und dürfte Antworten oder offene Zustände nicht verdecken.

Vor einer Übernahme sind die inhaltliche Prüfung der eigenen Erläuterungen, Browserbeobachtungen und menschliche Freigabe der konkreten Test-/Ergebnisgestaltung erforderlich. Verständnistests müssen insbesondere Skalenanker, nominelle Nichtpositionskategorien, Originaleinleitungen, die geänderte Weiterleitung, drei Zustände und historische Vergleichsgrenzen prüfen. Technische Syntax, spätere KI-Übereinstimmung und Browserfunktion sind keine methodische Validierung. Die abschließende Claude-Kontrolle veranlasst Steven; sie wurde hier nicht durchgeführt.

## Technische Belege und verbleibende Prüfungen

`node --check outputs/loop/policy-ui-design-v2/prototype.js` und `node --check outputs/loop/policy-ui-design-v2/catalogue.js` endeten jeweils mit Exitcode 0. Die Hashliste aller eigenen Artefaktdateien steht in `outputs/loop/policy-ui-design-v2/manifest.json`.

| Datei | SHA-256 |
| --- | --- |
| `index.html` | `1270f0c5faaeb3a1ba206f17c15a538206a475b3c9b4ca0332f4f7b6c69500f7` |
| `prototype.js` | `1d56dbdc63cde53d3732c484bbb49c770a5b8fe295140d4290245faff14bea05` |
| `prototype.css` | `f0c0fde17a0a882a6899dcd10a98fc33376a3a6bbc9faad18f9415c6320aff73` |
| `catalogue.js` | `3b897bad81058fbd525a1cf9fa04354f8d48ccc8ae5892e89496ad1552411785` |
| `manifest.json` | `8beaf71937ec09a50d2fe571453a1378b826d15fe39f985fa82727f001707b40` |

Alle dynamischen Original- und Antworttexte werden mit `textContent` beziehungsweise Textknoten aufgebaut. Keine HTML-Interpolation, Speicherung, Cookies, Tracker, Authentifizierung oder Antwortübertragung. Das Modul hält ausschließlich Auswahlindex beziehungsweise Überspringgrund im Arbeitsspeicher. Die Content-Security-Policy sperrt Verbindungen, Formübertragung, externe eingebundene Ressourcen und Bilder.

Browsertools wurden gemäß Root-Koordination nicht verwendet. Deshalb liegen keine Behauptungen zu tatsächlich beobachtetem Laufzeitverhalten, Bildschirmbreiten, Fokus, Zoom oder Barrierefreiheit vor. Root prüft den eigenen statischen Server, lokale Assetauflösung, alle relevanten Breiten, native Tastaturbedienung, Zustandswechsel, vollständigen B1–B12-Fortgang, Ergebnisvollständigkeit und Sitzungsverlust nach Neuladen.

Geschrieben wurden ausschließlich der eigene Outputordner und dieser Bericht. Hauptapp, öffentliche Routen, Navigation, Forschungsdateien und vorhandene Methodik-Erstautorberichte bleiben unverändert. Kein Git, keine Installation, Server, Auth-, Claude- oder Netzarbeit, keine anderen Agents, kein Vollcheck und keine Veröffentlichung. Eine Integration oder wissenschaftliche Freigabe wird nicht erteilt.
