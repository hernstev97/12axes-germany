# Technischer Designimport: Korrektur v2

Vor tatsächlichem ESS-Zugriff, 2026-10-03. [Erstvertrag](designaudit-vorabvertrag.md) und v1-Erstbericht bleiben erhalten. Aktueller ausführbarer Code: `pipeline/design_audit_v2.py`. DM-R01–04 angenommen, Runde1; keine reale Ausführung in der Korrektur.

Ganzzahlige Designcodes werden mit Decimal exakt geprüft und ohne Float-Rundung normalisiert. Die interpretierten Bytes werden einmal in eine unveränderliche Python-Bytes-Fassung im Arbeitsspeicher gelesen, genau diese Fassung wird gehasht und tokenisiert. Ein nachfolgender Pfadtausch ändert die interpretierten Bytes nicht; ein nicht passender Bytestand stoppt. Der vorhandene Rohdatenlink bleibt zulässig, kein lokaler Datensatz wird dafür kopiert. Ganze CSV-Bytes werden technisch verarbeitet; nur die festgelegten neun Metadatenfelder werden interpretiert.

Das frische Ergebnis muss direkt unter `data/local/design-metadata-v2/` liegen. Pfadnormalisierung und Symlinkgrenzen werden vor Verzeichniserzeugung geprüft. Der neue Ordner erhält0700, die Datei0600; ein bestehender unsicherer Ordner wird zurückgewiesen, nicht verändert. Keine Überschreibung. Der Ordner ist eine eigene private technische Ablage, kein öffentlicher Datenexport.

Alle fachlichen Grenzen des Erstvertrags gelten weiter: keine Antwortanalyse, keine A/B-Zuordnung, keine erfundene Designkodierung oder Ersatzaufteilung. Gezielte Nachprüfung derselben vier Ursachen einschließlich echter synthetischer Gegenfälle vor tatsächlichem Import. Der vollständige Antwortplan und zwei Übergangsprüfungen bleiben erforderlich.
