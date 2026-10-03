# Gezielte Korrekturprüfung GBP-ROOT-01

Urteil: `ACCEPTED_BOUNDED` für die responsive CSS-Korrektur. Kein schwerer Befund und kein neuer Gesamtaudit. Die ursprüngliche Erstfassung bleibt unverändert. Die hier geprüfte Änderung begründet keine neue Inhalts-, Ergebnis-, Methoden-, Menschen-, Design- oder Releasefreigabe.

## Prüffassung und Integrität

Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Zugewiesener Branch: `research/life-93-night-20261003`. Keine Git-, Netzwerk-, Auth-, Claude-, Rohdaten- oder Privataggregataktion.

- v1-Manifest: `d95b3522fe1e16a82d093f74d79f85a4e89e93de484f188970e611d2d1ecc914`.
- v2-Manifest: `a96b12d423a27e3fe15f746b13f5885c882293f698c0846b4c1e76ecf3b07c99`.
- Der v2-Verweis `previousManifestSha256` bindet das tatsächliche v1-Manifest. Die Commitangabe `0afd0093b1bc90f651cf91baf3ef22459bca9965` wurde als deklarierte Herkunft gelesen, hier ohne Git nicht neu verifiziert.
- Beide Manifeste inventarisieren dieselben 86 Pfade. Exakt 85 Pins bleiben gleich; ausschließlich `web/src/app/policy-draft/policy-draft.scss` hat einen anderen Hash.
- Alle aktuellen 86 v2-Dateien stimmen vor und nach der gezielten Prüfung mit ihren Pins überein. Die vier fremden Reviewerberichte wurden weiterhin ausschließlich gehasht.
- Original-Erstbericht: SHA256 `36691737a4038f908c08e7ec8b914eb9a94ff363ab446c733f6fd50b38924866`, unverändert.
- Patch `v2/responsive-change.patch`: SHA256 `f244690c7abb511e67ed2df8200b58baa680ad355bc84f5c3874e011c5648b9f`.
- Altes CSS, ausschließlich im Arbeitsspeicher durch Rücknahme der zwei Deklarationen rekonstruiert: SHA256 `e4f914532aec5cf1e10e392b1a53229f934ceb9179775d2ca2097d0fd6161e30`, exakt der v1-Pin.
- Aktuelles CSS: SHA256 `a13b9138de8ac2086bff347f349494815c9eb7973b5c0d9f67696fce67776722`, exakt der v2-Pin.

Der tatsächliche Diff umfasst genau einen Hunk bei `.group-controls select` und ergänzt ausschließlich:

```scss
white-space: nowrap;
text-overflow: ellipsis;
```

Hunkposition, Kontextzeilen und Änderungsbytes stimmen mit dem übergebenen Patch überein. Ein erster wörtlicher Vergleich mit Python `difflib` unterschied sich nur durch Gits zusätzliche Hunk-Kontextüberschrift `legend span {`. Nach Entfernung genau dieser optionalen Überschrift war der Diff identisch. Das war eine Grenze des Vergleichsskripts, kein zusätzlicher CSS-Unterschied. Integritätsbeleg: `outputs/loop/group-presentation-review/responsive-integrity.json`.

## Geprüfte Wirkung

### GBP-ROOT-01-A – CSS-Umfang und Kaskade bestanden

Die allgemeine Regel `button, select` setzt weiterhin `white-space: normal`. Die spezifischere Regel `.group-controls select` überschreibt dies nur für die beiden historischen Gruppenauswahlen. Die Auswahl des Überspringgrunds und sämtliche Schaltflächen bleiben davon unberührt. `width: 100%`, `max-width: 100%`, Mindesthöhe, Padding, Schrift, Farben und Rahmen ändern sich nicht.

`nowrap` verhindert mehrzeiligen Text im geschlossenen Gruppen-Select. `text-overflow: ellipsis` fordert eine gekürzte einzeilige Darstellung an. Dies passt zum berichteten Anlass: Eine lange Studienbeschriftung war bei 320 Pixeln umgebrochen und vertikal angeschnitten. Die konkrete sichtbare Ellipsis und die Behebung dieses Browserbefunds werden weiterhin vom Koordinator beobachtet; aus der CSS-Lektüre allein folgt keine Browserabnahme.

### GBP-ROOT-01-B – Native Bedienung und vollständige Inhalte erhalten

Die unveränderten Template-, TypeScript- und Referenzpins belegen, dass der Eingriff keine Optionsbezeichnung, ID, Value, Auswahlhandlung, Antwort oder Quellenbindung verändert. Die native Auswahl bleibt ein beschriftetes `select` mit vollständigen ursprünglichen `option`-Texten. Es entsteht kein eigener verkürzter Labelwert und keine Umcodierung.

Die vollständige Studienidentität, erinnerte Wahl und Befragungszeit bleiben in den separaten Texten unter der Auswahl vorhanden. Nach Gruppenwahl wird auch die volle Gruppenbezeichnung dort wiederholt. Ellipsis kann die geschlossene Beschriftung an schmalen Breiten verkürzen; sie entfernt diese Angaben nicht aus den Optionen oder den ergänzenden Texten. Die bestehende Grenze zwischen eigener Antwort und historischer Vergleichswahl bleibt erhalten.

Studienreset, Bearbeiten, Ergebnisrückkehr und Remount erhalten dieselben Handler und Daten wie in v1. Die Korrektur liefert keinen Anlass, ihre unveränderten Tests erneut als neues Paket auszuführen.

### GBP-ROOT-01-C – Fokus und Abnahmegrenzen erhalten

Die vorhandene `select:focus-visible`-Regel mit zwei Pixeln Outline und vier Pixeln Abstand bleibt unverändert. Labels, IDs, `aria-describedby`, deaktivierter Anfangszustand, Reihenfolge und native Tastaturbedienung werden nicht bearbeitet. Tatsächliche Fokusdarstellung, offene native Optionsansicht, Smartphone-Layout und 200-Prozent-Zoom bleiben separate Browserprüfungen beim Koordinator.

Der ursprüngliche Erstbericht und die übrigen 85 Pins werden durch diese Nachprüfung nicht neu bewertet oder erweitert. Der prüfende Agent gehört weiterhin zur Codex-Modellfamilie; gemeinsame Fehler bleiben möglich. Technischer Diffabgleich ersetzt weder Menschenprüfung noch empirische Evidenz oder Neutralitätsabnahme.

## Ausgeführte und nicht ausgeführte Prüfungen

Ausgeführt: tatsächliche Manifestauthentisierung, vollständiger v1/v2-Pininventarvergleich, Vor-/Nachprüfung aller aktuellen v2-Pins, rein speicherbasierte Rekonstruktion des v1-CSS, genauer Patchabgleich, Hashprüfung des unveränderten Erstberichts sowie statische CSS- und Bedienwirkungsbeurteilung.

Nicht wiederholt: Angular-/Python-Tests, Adaptergeneratoren, Produktionsbuild und vollständiger Audit. Keine Änderungen an deren Inputs oder Verhalten rechtfertigen hier eine Wiederholung. Keine fremde Bewertungsprosa, keine Rohdaten, keine privaten Aggregate oder zusätzlichen historischen Berichte gelesen. Kein eigener Browserlauf. Der finale übergreifende `pnpm check` und konkrete Browserbeobachtungen werden von Root getrennt ausgeführt und dokumentiert.

Blocker der konkreten Korrektur: keine. `ACCEPTED_BOUNDED` gilt für die geprüften CSS-Bytes und den unveränderten Bedienvertrag. Browser-, Menschen-, Design- und Releaseabnahmen bleiben offen, soweit sie nicht separat tatsächlich durchgeführt und freigegeben werden. Diese Nachprüfungsfassung bleibt nach Abschluss unverändert.
