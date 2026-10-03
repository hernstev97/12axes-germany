# Gezielte Korrekturprüfung des Reset-Fokus

3. Oktober 2026. Getrennter Codex-Agent; ausschließlich TFZ-S04 und dessen neue Regression. Dieser separate Round-2-Bericht ist die erste Korrekturrunde für TFZ-S04. Es gab hier keinen zweiten erfolglosen Korrekturzyklus. Die bisherigen Berichte bleiben unverändert.

Root meldet als tatsächlichen Chromiumbefund: Nach Radioauswahl, Tab zum Reset-Button, Enter und abgewartetem Disabled-Render fiel `document.activeElement` auf `BODY`; `:focus-visible` war falsch. Eine frühere Probe vor dem Rendern war dafür nicht aussagekräftig. Dieser Agent hat diese Laufzeitbeobachtung nicht selbst ausgeführt.

## Ergebnis

Die Korrektur behebt die statisch erkennbare Ursache. `web/src/app/policy-draft/policy-draft.ts:136–142` ruft nach dem Zurücksetzen und `update()` jetzt `this.focus('question')` auf. Der schon vorhandene Helfer wartet mit `afterNextRender` auf die aktualisierte Oberfläche, fokussiert die Fragenüberschrift und scrollt sie ins Bild. Der neue Fokus wird damit erst nach dem Rendern des deaktivierten Reset-Buttons angefordert. Auswertung und Antwortstatus ändern sich dadurch nicht.

Der neue Test in `policy-draft.spec.ts:106–117` beginnt mit einer Auswahl, fokussiert den Reset-Button, setzt die Interaktionsaufzeichnung zurück und aktiviert Reset. Nach `whenStable()` prüft er den deaktivierten Button, fehlende ausgewählte Radios sowie die fokussierte Fragenüberschrift und die vorhandene Scrollanforderung. Das prüft den konkreten Ablauf, der bisher keinen anschließenden Fokus anforderte. Es enthält keinen behaupteten Nachweis für sichtbare Browserrahmen oder native Tabbewegungen.

Die Änderung ist eng begrenzt. Entfernt man den einen neuen Fokusaufruf und den einen neuen Testblock, entsprechen TS und Spec bytegenau ihren im Erstbericht dokumentierten SHA-256. Sonstiger Code, Fokushelfer und Tests dieser Dateien sind damit unverändert. Keine weitere statische Korrektur ist für diesen Befund erforderlich.

## Prüfumfang und Grenze

Gelesen wurden ausschließlich die betreffenden TS-/Spec-Ausschnitte. Beide vollständigen Dateien wurden zusätzlich zur Identitätsprüfung gehasht; das ist kein erneuter Gesamtaudit. Die Bytes des Zusatzes und die Dateihashes wurden beim Abgleich gemessen.

- TS: 8.812 Bytes, Zusatz 28 Bytes; SHA-256 `da3a08b61dd077c28bef3f1a38942b666bfb93afc4a1858498d9c302278aaace`.
- Spec: 23.164 Bytes, Zusatz 556 Bytes; SHA-256 `a92b1c21d02e295154b71201f3fc864d770a69df46d5a04ec419eb9072ab031b`.

Root muss den tatsächlichen Chromiumablauf nach dem Rendern bestätigen: Fragenüberschrift als Fokusziel, dann mit Tab zum ersten Radio und sichtbar gerahmte native Auswahl. Ein jsdom-Test ersetzt diese Beobachtung nicht. Dieser Agent hat keine Tests, Browser-, Netzwerk-, Server-, Git-, Rohdaten-, privaten Antwort- oder Outputzugriffe ausgeführt. Er hat nur diesen neuen Bericht geschrieben. Der Befund begründet keine wissenschaftliche oder methodische Freigabe.
