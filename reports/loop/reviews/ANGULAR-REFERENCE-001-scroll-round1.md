# ANGULAR-REFERENCE-001: gezielte Scrollkorrektur, Runde 1

Urteil: **ACCEPTED_BOUNDED** für die technische Korrektur von **AUI-ROOT-01 / AR-L01** und die geprüften Ziel-/Ansichtsregressionen. Die tatsächliche Browsergeometrie bleibt separat bei Root. Dieses Urteil bestätigt weder eine gesamte Browser- oder WCAG-Abnahme noch eine methodische, Design- oder Releasefreigabe.

## Prüffassung und erhaltene Ausgangsbelege

Geprüft am 3. Oktober 2026 anhand `reports/loop/packages/ANGULAR-REFERENCE-001/v2/manifest.json`. Tatsächlicher Manifest-SHA-256: `b4d85aac82317c7c44c502340f7809b2c9e9ebab6aa66281f2950b7492468ff8`. Alle 48 tatsächlichen Artefakthashes stimmen. Die Datei bezeichnet sich intern weiterhin als Paket `ANGULAR-REFERENCE-001/v1`, Revision 3, mit Vorgängermanifest `c9607fd59ddfcdd20ece679240f283e9a4e53e79293e08919a73ab07310fff9a`; die geprüfte Ablagefassung ist ausdrücklich `/v2/`. Diese Benennung ist eine Nachvollziehbarkeitsnotiz, kein fachlicher Fehler.

Die zwei Korrekturpins sind:

- `policy-draft.ts`: `fa926ffbdbff04c6efc9fd059b839c03c0e1e02fdda14b4cbfa5338154b798be`.
- `policy-draft.spec.ts`: `4cd1041e00e19175da2bb382ada5ebd6f6c447ea5def6822b72af1ae4eb60661`.

Der eigene unveränderte Erstbericht wurde gelesen und erhalten. Sein tatsächlicher SHA-256 ist vor und nach dieser Prüfung `79215f8591f42fb8b9602f2c32256740fd203fdd41795abe85660bea39eff8f8`. Der genannte historische Commit wurde nicht über Git geöffnet. Die ursprünglichen Forschungs-/Quellenbefunde wurden nicht neu beurteilt.

Der ausdrücklich erlaubte Rootbeleg `reports/loop/angular-preview-initial-technical.json` dokumentiert den Ausgangsfehler: Beim Bearbeiten des letzten Ergebnisses war Frage 43 fokussiert, ihre Überschrift lag aber oberhalb des Viewports. Das ist eine gelesene Rootbeobachtung, keine eigene Browsermessung. Andere Reviewerurteile und Autorenberichte wurden nicht gelesen. Upstream Erstberichte wurden wiederum nur als Bytes für den Pinabgleich gehasht.

## Gezielte Befunde

- **AR-SC-01 — Tatsächliche Korrekturpins: bestanden.** Das explizit benannte Manifest und alle 48 Bytes stimmen. Die neuen Code-/Specpins sind eindeutig gebunden; die Referenz-, Zustands-, Template-, Style- und Routingpins entsprechen den bereits geprüften Eingaben. Keine numerischen Referenztabellen wurden ausgegeben.
- **AR-SC-02 — Zielbindung und Reihenfolge: bestanden.** `policy-draft.ts:191–203` löst die aktuelle Seiten- oder Fragenüberschrift innerhalb von `afterNextRender` auf. Es hält keinen vor dem Ansichtswechsel aufgenommenen DOM-Knoten fest. Fehlt das gewünschte Ziel, endet der Callback. Andernfalls erhält dieselbe gerenderte Überschrift zunächst den nativen Fokus mit `preventScroll: true` und anschließend `scrollIntoView({ block: 'start', inline: 'nearest', behavior: 'instant' })`. Damit fordert der Code die bisher fehlende Sichtpositionierung ausdrücklich an. Die Bewegung ist unmittelbar; die Callbacks entstehen aus den vorhandenen, durch Bedienaktionen ausgelösten Ansichts- und Fragenwechseln.
- **AR-SC-03 — Wechselregressionen: bestanden in Angular/jsdom.** Tatsächlich ausgeführt wurde ausschließlich der gezielte Angular-Test für `policy-draft.spec.ts`: eine Datei, 21 Tests bestanden, keine Fehler oder übersprungenen Tests. Darunter sind Vorwärts-, Rückwärts- und Skipwechsel; alle sechs gerichteten Ansichtswechsel; letzte Übersichtsfrage; nativer E35-Ergebnis-Edit zurück zu Frage 43; Ergebnisaufruf und Skip nach Frage 43. Die Prüfungen binden die gerenderte Überschrift, bestätigen den tatsächlichen Fokus und verlangen den Scrollaufruf auf genau diesem Ziel nach dem Fokus. Die Radioauswahl allein fordert weder Fokus noch Scrollen neu an. Die vorhandenen Tests für Antworten, Editieren, Skip/unberührt, Teilresultat, Originalcodes, Referenzzurückhaltung und fehlende Antwortspeicherung/-übertragung bleiben in dieser Datei grün.

## Tatsächliche Checks und Grenzen

Ausgeführt wurden der SHA-256-Abgleich des expliziten Korrekturmanifests und aller 48 Pins sowie:

`NG_PERSISTENT_BUILD_CACHE=0 pnpm exec ng test --watch=false --include=src/app/policy-draft/policy-draft.spec.ts`

Der Angular-Testbuild und alle 21 Tests bestanden. Der eigene Prüfstand liegt in `outputs/loop/angular-reference-review/scroll-round1-qa.json`. Kein ausgeführter Check schlug fehl. Der Erstbericht bleibt unverändert.

**Erhebliche Code- oder Zielbindungsfehler der begrenzten Korrektur:** keine festgestellt. **Stilwünsche:** keine als Annahmebedingung erhoben.

- **AR-SC-L01 — Browsergeometrie bleibt offen:** jsdom hat keine Layout-/Scrollgeometrie. Der Spec ersetzt `scrollIntoView` ausdrücklich durch eine Aufzeichnung von Ziel, Optionen und tatsächlich fokussiertem Element. Die grüne Prüfung belegt den korrekten nativen Aufruf, keine sichtbare Position. Root muss E35-Edit sowie relevante Ansichtswechsel in echten Desktop-/Smartphone-Viewports separat nachprüfen. AUI-ROOT-01 wird durch diesen Bericht deshalb nicht eigenständig als browserseitig geschlossen erklärt.
- **AR-SC-L02 — Begrenzte Regression:** Diese Runde führt keine neue Gesamtmethodik-, Quellen-, Datenschutz-, Routing-, Build-/Release- oder Handbuchgesamtprüfung aus. Sie verändert keine gemeinsamen Quellen, Referenzen, Routen oder Services. Es gab keine Git-, Netzwerk-, Installations-, Server- oder Browserdienstaktion und keinen Rohdaten-/Privatdateizugriff. Vorherige Begrenzungen des Erstberichts gelten weiter.
- **AR-SC-L03 — Keine persönliche oder externe Abnahme:** Gleiche Codex-Modellfamilie. Menschliche Verständlichkeit, methodische Entscheidung, Design-, persönliche Release- und gegebenenfalls externe Schlusskontrolle bleiben ausstehend.
