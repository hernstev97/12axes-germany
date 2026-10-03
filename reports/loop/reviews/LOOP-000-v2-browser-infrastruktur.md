# LOOP-000-v2: Browser und öffentliche Infrastruktur

Unabhängiger Nachprüfbericht vom 2026-10-03. Reviewer `/root/loop000_recheck_browser`. Die ursprünglichen Text- und Regelkonflikte sind in v2 korrigiert. Die Abnahme des gesamten Pakets bleibt offen: Die Infrastruktur erlaubt nachgewiesene Pfadumgehungen und einen unzureichend belegten Abschlussstatus. Der verbindliche technische Gesamtcheck scheitert außerdem an zwei Semikolons im neuen Lizenzsatz. Ein echter Browserzoom wurde nicht geprüft.

## Prüffassung und Trennung

- v2-Manifest: `reports/loop/packages/LOOP-000/v2/manifest.json`, SHA-256 `9ae58f200b4f559b951b95e90c713d6879284e1f31d572e0d9e17bbf9ff0ba00`. Alle 26 Datei-Hashes und Bytezahlen selbst geprüft; keine Abweichung.
- Ausgangspaket v1: Manifest-SHA-256 `ac9f8f5231f881c883e771cc50072e43a20b6db8519db06ca76453ddc45a2496`. Alle 27 Datei-Hashes erneut geprüft; keine Abweichung. Die zwei abgeschlossenen Erstberichte stimmen mit ihren v2-Pakethashes überein.
- Codegrundlage: `9db0bf14902f83aed922fb8be0e0f2ff8ef8b6c1`. Vor dem Browserlauf waren die drei geänderten Webdateien bytegleich mit v2. Die übrigen 58 Webdateien waren bytegleich mit dem Commit. Wiederholung um `2026-10-03T02:15:11Z` ergab erneut keine Abweichung.
- Plan: Entwurf 0.2, Quellenkatalog laut Manifest 0.2, Modellkonfiguration `null`. Den Rohdatenhash ausschließlich als Paketmetadatum übernommen, keine Rohdatei geöffnet oder selbst gehasht.
- Dokumentfundstellen dieses Berichts meinen stets die eingefrorenen Dateien unter `reports/loop/packages/LOOP-000/v2/files/`. Die zusätzlichen Fundstellen in `docs/belegregister.md` und `docs/entscheidungen.md` stammen aus dem genannten Git-Commit. Aktuelle Autorenentwürfe und andere v2-Nachprüfberichte wurden nicht gelesen.

Gelesen wurden Auftrag, Issue, AGENTS, Projektstand, das vollständige Handbuch, Prüfregeln, Analyseplan, Review-Regeln, Lizenzakte, eingefrorener Zustand, die beiden v1-Erstberichte und die v2-Autorentscheidungen. Der Bezug auf frühere Auditberichte ist keine eigene Wiederholung des damaligen Forschungsreviews. Die v2-Finding-IDs und ihre Reparaturrunde 1 bleiben erhalten; I01 und P01 sind weiterhin als derselbe Konflikt erkennbar. Ich habe keine weiteren Agents gestartet.

Die Kontexttrennung ist eine Auftragsgrenze. Gemeinsame Dateirechte erlauben technisch weitere Zugriffe; eine Sicherheitssandbox oder eine andere Modellfamilie ist dadurch nicht belegt. Die beobachtete Browserkollision ist unten gesondert protokolliert.

## Nachprüfung der ursprünglichen Findings

### L000-I01 und L000-P01: Ergebnisstatus

**Aussage und ursprüngliches Problem.** Die alten Prüfregeln erlaubten ausschließlich vier Bearbeitungsbegriffe, der neue Auftrag dagegen fünf Ergebnisstatus. Das war kein einheitliches Abnahmeschema.

**Beleg der Korrektur.** `docs/pruefregeln.md:9` nennt jetzt dieselben fünf Status wie `docs/auftrag-life-93-2026-10-03.md:133` und `docs/arbeitsloop.md:22`. Ausführung und Bestehen bleiben getrennt. Fehlender Zugang begründet keine Einstufung als nicht erforderlich. Historische Wörter bleiben erhalten und werden nur anhand tatsächlicher Belege eingeordnet; „durchgeführt“ wird ausdrücklich nicht automatisch `BESTANDEN`. Der eingefrorene Zustand führt noch ungeprüfte beziehungsweise blockierte wissenschaftliche Voraussetzungen. Die fünf zulässigen Werte bestehen die synthetische Statusprüfung; „durchgeführt“ als neuer Prüfstatus wird zurückgewiesen.

**Ergebnis und Folge.** `BESTANDEN` für die formale Regelkorrektur. Beide ursprünglichen IDs und ihre erste Reparaturrunde bleiben erhalten. Das belegt weder empirische Prüfungen noch eine Phasenfreigabe. Die neue DONE-Lücke unter B03 ist ein eigener Infrastrukturfehler, keine erneut gezählte Reparaturrunde des alten Wortlautkonflikts.

**Schwere und Nachprüfung.** Der ursprüngliche mittlere Regelkonflikt ist im geprüften Umfang aufgelöst. Der direkte Vergleich der genannten Stellen und die erhaltenen v1-Hashes tragen dieses Urteil.

### L000-I02: Umfang methodischer KI-Reviews

**Aussage und ursprüngliches Problem.** Das Handbuch schloss zuvor auch tatsächlich ausgeführte, begrenzte Methodenreviews durch KI pauschal von der Beschreibung als methodische Prüfung aus.

**Beleg der Korrektur.** `docs/handbuch.md:263` erlaubt jetzt die Benennung des tatsächlich geprüften Umfangs und Befunds. Technische Prüfungen, CI und KI-Übereinstimmung ersetzen ausdrücklich keine methodische Evidenz oder Abnahme. Ein Methodenreview ersetzt weder empirische Nachweise noch die vorgeschriebenen getrennten Erstbewertungen und Reviews. Das passt zu `docs/pruefregeln.md:61`, dem methodischen Reviewerauftrag und der Trennung in LIFE-93.

Im tatsächlichen Browser steht auf der Startseite „KI-Audit durchgeführt. Empirische Modellprüfung noch offen.“ Die Projektseite sagt „Ein KI-Audit hat Teile des Rechercheentwurfs geprüft. Eine empirische Modellprüfung fehlt.“ Unter der Faktenliste steht die vorgeschriebene Formel zur fehlenden Validierung, Fachprüfung und Neutralitätsgarantie. Belege sind `home.html:123–124`, `project.ts:24–27`, `project.html:107–108`, die eigenen nativen DOM-Beobachtungen und die gespeicherten Chromium-Screenshots.

**Ergebnis und Folge.** `BESTANDEN` für Regel und sichtbaren Wortlaut. Der begrenzte Review bleibt beschreibbar; die UI behauptet keine empirische Modellabnahme. Claude-Prüfungen, methodischer Freigabeprozess und menschliche Verständlichkeitsprüfung werden nicht nachträglich als erfüllt ausgegeben.

**Schwere und Nachprüfung.** Der ursprüngliche mittlere Widerspruch ist aufgelöst. Dies ist ein Abgleich der Berichtssprache mit dem dokumentierten Prüfbereich, keine neue Bestätigung des gesamten früheren Audits.

### L000-I03: nächster Arbeitsschritt

**Aussage und ursprüngliches Problem.** Die UI beschrieb das erstmalige Festlegen von Prüfregeln als bevorstehend, obwohl Regel- und Planentwürfe bereits vorlagen.

**Beleg der Korrektur.** `home.html:127–128` nennt jetzt „Originalfragen dokumentieren und Analyseplan begründen“. `project.html:119–122` benennt vorhandene Entwürfe, Originalfragenbestand und Themenabdeckung sowie begründete Methodenparameter. Endgültige Auswahl und empirische Untersuchung warten auf erforderliche Abnahmen. Dieser Wortlaut entspricht dem eingefrorenen Projektstand und Analyseplan. Er wurde im nativen Tab und in Chromium bei Desktop- und Smartphonebreiten tatsächlich ausgelesen und angesehen.

**Ergebnis und Folge.** `BESTANDEN` für die Korrektur der Fortschrittsaussage und die geprüften Navigationsabläufe. Die vollständige technische/UI-Abnahme ist weiterhin offen, weil B04 den Zoomnachweis betrifft und B05 `pnpm check` blockiert. Der behobene alte Wortlautfehler wird deshalb nicht als Freigabe des gesamten Pakets verwendet.

**Schwere und Nachprüfung.** Der ursprüngliche niedrige Fortschrittsfehler ist aufgelöst. Die verlangten technischen und Browserkontrollen wurden ausgeführt; ihre unterschiedlichen Ergebnisse stehen unten.

### L000-A01: Lizenzbegründung für den Rohdatenausschluss

**Aussage und ursprüngliches Problem.** Die übernommene UI begründete den Rohdatenausschluss pauschal mit der Lizenz, obwohl die offizielle Dokumentation bedingte Weitergabe und getrennte Lizenzen beschreibt.

**Eigene Originalprüfung.** Der ESS-Disclaimer wurde um `2026-10-03T02:02:40.675440Z` direkt per HTTP mit Status 200 abgerufen. 168665 Bytes, SHA-256 `8e0ded72241b48a730b9ac7f85508f0198407a4d43dcb1f14a0a159744db586d`; identisch mit dem eingefrorenen Autorenbeleg. Unter „Conditions of use“ unterscheidet er Daten unter CC BY-NC-SA 4.0 und Dokumentation unter CC BY-SA 4.0. Der vorhergehende Absatz empfiehlt Portalverweise und beschreibt Angaben bei extern gespeicherten beziehungsweise veränderten Fassungen. Das ist kein pauschales Lizenzverbot. Der unabhängig gelesene CC-Lizenztext erlaubt unter seinen Bedingungen nichtkommerzielle Weitergabe; maßgeblich sind §2(a)(1), §3 und §4. [ESS-Original](https://www.europeansocialsurvey.org/contact/disclaimer), [CC-Lizenztext](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en).

Der Webtoolabruf des ESS-Originals scheiterte zuvor mit 502. Dieser Fehlabruf wird nicht als erfolgreiche Prüfung gezählt. Die erfolgreiche HTTP-Fassung samt Textauszug und Zugriffsdaten liegt ausschließlich im ausgeschlossenen eigenen Outputordner.

**Beleg der Korrektur.** Beide sichtbaren Sätze lauten jetzt „Die ESS-Rohdaten veröffentlicht das Projekt nicht; es verweist auf das ESS-Portal.“ Sie benennen die Projektentscheidung. `docs/lizenzen.md:13,25`, B-LIZ-001 und E-20261003-04 trennen bereits Rechtebefund und zusätzliche Projektregel. Die tatsächliche UI enthält keinen pauschalen Lizenzverbotsgrund mehr. Der vorhandene ESS-Link führt zur ESS-Hauptseite; ein direkter Link auf das Datenportal ist in den beiden Absätzen nicht vorhanden.

**Ergebnis und Folge.** `BESTANDEN` für die Korrektur der Lizenzbegründung. Keine Freigabe eines konkreten Datenexports und keine rechtsfachliche Freigabe. Der Semikolonfehler ist B05; er hebt die belegte Lizenzunterscheidung nicht auf.

**Schwere und Nachprüfung.** Der ursprüngliche mittlere Transparenzfehler ist im benannten Umfang korrigiert. Originalquelle, beide tatsächlichen Browsertexte und die Lizenzakte wurden direkt abgeglichen.

## Neue Findings

### L000-B01: interne Symlinks umgehen den Ausschluss geschützter Eingaben

**Betroffene Aussage.** `pipeline/loop.py:18–31` soll öffentliche Eingaben von `data/raw`, `data/local`, `outputs`, `.git`, verwalteten Verzeichnissen und Umgebungsdateien trennen.

**Problem und Beleg.** Die Verbote prüfen den angefragten Pfad. Nach Auflösen eines Links prüft der Code nur noch, ob das Ziel irgendeine Datei im Projekt ist. Im ausschließlich synthetischen Gegenbeispiel verweist `docs/raw-alias.md` relativ auf `../data/raw/synthetic.txt`, `docs/env-alias.md` auf `../.env.synthetic`. Beide Eingaben werden akzeptiert. `freeze` kopiert den erfundenen geschützten Platzhalter tatsächlich in das öffentliche Paket. Direkte Raw-/Env-Pfade, `./`-/Doppelslash-Varianten und ein externer Dateisymlink werden dagegen zurückgewiesen. Der zulässige interne Link auf `docs/public.md` wird ebenfalls akzeptiert.

Reproduktion: `python outputs/loop/recheck-browser/infrastructure.py`, eingefrorenes Modul aus v2, Fälle „public_input docs/raw-alias.md“, „public_input docs/env-alias.md“ und „freeze internal protected alias“. Das gespeicherte Ergebnis enthält `copiedSyntheticProtectedPlaceholder: true`. Fundstellen sind `loop.py:24–30,47`; die drei vorhandenen Unit-Tests enthalten diesen internen Umweg nicht.

**Folge.** Ein äußerlich öffentlicher Dateiname kann geschützte Inhalte in ein Prüfmanifest und dessen Dateien übernehmen. Der Direktpfadschutz genügt dafür nicht. Eine tatsächliche Rohdaten- oder Secret-Exposition im geprüften Paket wurde nicht nachgewiesen; dafür wurden keine echten geschützten Inhalte geöffnet.

**Schwere: hoch.** Die Umgehung betrifft die ausdrücklich verlangte Trennung öffentlicher Pakete und geschützter Eingaben. Sie blockiert den Einsatz dieses Guards als Schutz vor solchen Kopien.

**Korrektur und Nachprüfung.** Aufgelöste Ziele relativ zur realen Projektwurzel bestimmen und dieselben Verbote auch auf diese Ziele anwenden. Alternativ Symlinks ausdrücklich ausschließen, wenn das der festgelegte Eingabevertrag sein soll. Erlaubte interne Links, geschützte interne Ziele, Verzeichnissymlinks und externe Ziele getrennt testen. Danach müssen die geschützten Fälle vor Paketerstellung scheitern. Prüfungen gegen einen gleichzeitig Dateien austauschenden Benutzer bleiben eine gesonderte, hier nicht untersuchte Grenze.

### L000-B02: Verzeichnisumleitungen schwächen Output- und Archivgrenzen

**Betroffene Aussage.** `freeze` begrenzt Ausgaben auf `reports/loop/packages`; `verify` begrenzt Dateien auf den Archivbereich (`loop.py:40,62`).

**Problem und Beleg.** Die erlaubte Basis wird selbst mit `resolve()` aufgelöst. Ist `reports/loop/packages` ein Symlink nach außerhalb der synthetischen Projektwurzel, akzeptiert `freeze` das ebenfalls dort aufgelöste Ziel und schreibt tatsächlich außerhalb dieser Wurzel. Ein direktes externes Outputziel ohne diese Basisumleitung wird korrekt verworfen. Im zweiten Gegenbeispiel ist `package/files` ein Link nach außerhalb des Pakets; `verify` akzeptiert den passenden Hash der externen Platzhalterdatei und meldet `allPassed: true`.

Belege: synthetische Fälle „symlink packages root redirects output“ und „verify symlink files root“ in `infrastructure.json`, mit `resolvedOutsideSyntheticProjectRoot: true` beziehungsweise `allPassed: true`. Alle beteiligten Verzeichnisse liegen im eigenen Outputordner; kein fremdes Projekt wurde verändert. Die vorhandenen Tests untersuchen diese Basisumleitungen nicht.

**Folge.** Die Funktion kann außerhalb ihres zugesagten Projektbereichs schreiben. Ein als geprüft bezeichnetes Archiv kann seine Bytes außerhalb seines eigenen Dateibaums beziehen. Hashgleichheit bleibt in diesem Gegenbeispiel wahr, die behauptete räumliche Grenze trägt aber nicht.

**Schwere: mittel.** Reproduzierbare Lücke in Schreibbegrenzung und Archivabgrenzung; keine tatsächliche Fremddateiüberschreibung nachgewiesen. Sie blockiert die Abnahme dieser Grenzen.

**Korrektur und Nachprüfung.** Die erlaubte Paketbasis selbst gegen die reale Projektwurzel prüfen und umleitende Vorfahren ausschließen oder nach einem ausdrücklich festgelegten Vertrag behandeln. Den realen `files`-Baum an die reale Paketwurzel binden. Positive Pakete innerhalb der Wurzel und beide Umleitungstypen unabhängig nachprüfen. Passende externe Hashes dürfen diese Grenze nicht aufheben.

### L000-B03: DONE akzeptiert unzureichende formale Abschlussbelege

**Betroffene Aussage.** `validate_state` verlangt einen „manifestegebundenen Abschluss“ für Setup, Release und Phasen 0–9 (`loop.py:76–87`). Der Auftrag erlaubt `DONE` erst nach den tatsächlichen erforderlichen Abnahmen (`auftrag:151`).

**Problem und Beleg.** Die Funktion prüft für jeden Abschluss nur `status == BESTANDEN` und die Länge der Hashzeichenfolge. Ein synthetischer DONE-Zustand mit zwölf Einträgen und jeweils 64 Buchstaben `z` besteht ohne Fehler, obwohl dies kein SHA-256 in Hexdarstellung ist. Es werden keine Manifest- oder Berichtsreferenzen geprüft. Derselbe Zustand besteht weiterhin mit einem aktuellen Check `empirical: NICHT_GEPRÜFT` und einer Abschlussabhängigkeit, deren Status `IN_DIESER_PHASE_NICHT_ERFORDERLICH` oder ein unbekannter Wert ist. Die Abhängigkeitsstatus werden außerhalb der drei explizit verbotenen Werte nicht validiert.

Beleg sind die fünf akzeptierten DONE-Fälle in `infrastructure.json`. Gegenfälle ohne Abschlussbelege, mit `BLOCKIERT` als Abhängigkeit oder mit blockierendem Finding werden korrekt verworfen. Die vorhandenen Tests lassen bei ihren negativen DONE-Fällen zugleich alle Abschlussbelege fehlen; sie prüfen die Umgehung mit vollständig belegten Pflichtfeldern deshalb nicht.

**Folge.** Der maschinelle Statuscheck kann formal ungeprüfte beziehungsweise ungültig referenzierte Abschlüsse akzeptieren. Der eingefrorene reale Zustand ist weiterhin `RUNNING`; ein tatsächlich falsch vergebener wissenschaftlicher Abschluss wurde nicht festgestellt.

**Schwere: mittel.** Fehler in einer künftig abnahmesteuernden Protokollprüfung. Die Tatsache, dass sie keine wissenschaftliche Garantie verspricht, ersetzt weder Hashsyntax noch Statuskohärenz.

**Korrektur und Nachprüfung.** Schema und Hashsyntax prüfen. Abschlussbelege mit existierenden, hashgeprüften Manifest-/Berichtsreferenzen verknüpfen. Abschlussrelevante Checks und Abhängigkeiten ausdrücklich kennzeichnen und für DONE konsistent prüfen; unbekannte Status verwerfen. Auch ein formal korrekt referenzierter Bericht beweist seine inhaltlichen Abnahmen nicht automatisch. Nachprüfung mit sonst vollständigen synthetischen Abschlussbelegen und jeweils nur einem ungültigen Hash, fehlenden Ziel, ungeprüften Pflichtcheck oder noch erforderlichen menschlichen Beitrag.

### L000-B04: Reflowprüfung wird als echter 200-%-Zoom ausgegeben

**Betroffene Aussage.** `scripts/check-browser.mjs:104–110,175` nennt die 640×400-Prüfung mit `deviceScaleFactor: 2` einen 200-%-Zoomtest und gibt diesen als bestanden aus.

**Problem und Beleg.** Der Code verkleinert den CSS-Viewport und ändert die Pixeldichte; er betätigt keinen tatsächlichen Seitenzoom des Browsers. Der eigene Lauf hat diese Konfiguration bestanden und exakt den entsprechenden Zoom-Erfolgssatz ausgegeben. `docs/handbuch.md:351` verlangt aber den tatsächlichen 200-%-Fall. Eine Zoomsteuerung wurde in dieser Nachprüfung nicht ausgeführt.

**Folge.** Der Reflownachweis wird weiter ausgelegt, als das Verfahren trägt. Es wurde kein Layoutfehler bei echtem Zoom nachgewiesen; der Zoomfall bleibt `NICHT_GEPRÜFT`.

**Schwere: niedrig.** Überzogener technischer Prüfwortlaut, ohne gefundenen Layoutdefekt. Die vollständige Handbuchabnahme bleibt dennoch offen.

**Korrektur und Nachprüfung.** Konfiguration und Erfolgssatz als Reflow-/Pixeldichteprüfung benennen. Für den Pflichtzoom einen tatsächlichen Browserzoom ausführen und dessen wirklichen Zustand, Fokus, Bedienung und Überlauf dokumentieren. Ein ungeprüfter Zoom darf im Abschlussprotokoll nicht `BESTANDEN` werden.

### L000-B05: neuer Lizenzsatz stoppt den Handbuchcheck

**Betroffene Aussage.** Die neue A01-Fassung soll dem Handbuch entsprechen und die erforderliche technische Prüfung bestehen.

**Problem und Beleg.** `home.html:83` und `project.html:88` verbinden „veröffentlicht das Projekt nicht“ und „es verweist auf das ESS-Portal“ mit einem Semikolon. `docs/handbuch.md:295` verlangt zwei Sätze. Der unveränderte eingefrorene Handbuchcheck meldet genau diese zwei Verstöße. Im isolierten `pnpm check` ist die Formatierung grün, danach stoppt die Kette mit Exitcode 1; Typprüfung, Tests und Build werden in diesem Gesamtlauf nicht erreicht.

Beleg: `outputs/loop/recheck-browser/pnpm-check-final.log`. Die separat ausgeführten Komponentenläufe haben jeweils Exitcode 0, einschließlich neun Tests in zwei Dateien. Sie machen den fehlgeschlagenen Pflichtlauf nicht nachträglich grün.

**Folge.** Die korrigierte Lizenzbegründung bleibt inhaltlich richtig, ihre konkrete Textfassung verletzt die verbindliche Stilregel und blockiert den technischen Gesamtcheck.

**Schwere: niedrig.** Begrenzter und leicht reparierbarer Textfehler, keine neue wissenschaftliche oder juristische Falschaussage. Die technische Paketabnahme ist bis zur Korrektur nicht bestanden.

**Korrektur und Nachprüfung.** Den Semikolon in beiden Sätzen durch einen Punkt ersetzen. Neue Fassung einfrieren, `pnpm check` vollständig wiederholen und die beiden tatsächlichen sichtbaren Sätze nochmals prüfen. Kein Layout- oder Produktwechsel nötig.

## Tatsächliche Browserkontrolle

Der Server auf `http://127.0.0.1:4313` lief im isolierten Worktree; Prozess `ng serve --host 127.0.0.1 --port 4313`, CWD `.../web`, Unixbenutzer `stevenh`. Er wurde vom Koordinator bereitgestellt und von diesem Reviewer weder gestartet noch beendet.

Native T3-Kontrolle begann mit `status` und `open`. Der tatsächliche gemessene Viewport betrug 1402×876 CSS-Pixel, bei angefordertem Setting 1280×800. Ein Freeform-Wechsel auf 390×844 und ein korrigierter iPhone-12-Pro-Preset brachen nach jeweils 15000 ms ab. Nach Feststellung des gemeinsam benutzten Defaulttabs wurde ein eigener Tab `tab_a` erzeugt. Ein letzter korrigierter Versuch mit expliziter Tab-ID scheiterte ebenso. Keiner dieser Versuche wird als Smartphoneansicht gezählt.

Ein Default-Snapshot zeigte zwischenzeitlich die öffentliche ESS-Studienseite statt der zuvor geöffneten Website. Der Koordinator bestätigte, dass er inzwischen einen anderen expliziten Tab verwendete. Diese Default-Snapshots sind kein isolierter Websitebeleg. Alle folgenden nativen Aktionen verwendeten ausdrücklich `tab_a`. Dort bestätigten tatsächliche Navigation, Sprungziel und DOM-Wortlaut `/projekt#naechster-schritt`, die Startseitenfakten und den Lizenzsatz. Die Galerie wechselte bei manueller Bedienung von `2 / 6` zu `3 / 6` und zurück; Pause blieb gesetzt.

Die native Tastaturaktion fokussierte den Sprunglink, ihr ausgelesener Outline-Stil war jedoch `none`. Enter fokussierte `main-content`. Die eigene projektlokale Chromium-Tastaturkontrolle zeigte dagegen einen sichtbaren soliden Rahmen, auch im gespeicherten Smartphone-Screenshot. Diese Abweichung wird als offene Werkzeug-/Browsergrenze protokolliert. Aus der nativen Beobachtung allein folgt kein bestandener Fokusnachweis und auch kein gesicherter Websitefehler.

Die ergänzende Projektprüfung lief mit Playwright-Core 1.62.1, axe-core 4.13.0 und dem bereits installierten Chromium 151.0.7922.34. Die Kopie des eingefrorenen Skripts änderte ausschließlich Projektwurzel und Screenshotpfad für die getrennte Ablage. Sie prüfte `/`, `/projekt` und `/gibt-es-nicht` bei 1440×1000, 1024×768, 768×1024, 390×844 und 320×720. Exitcode 0. Dabei keine axe-Verstöße unter den konfigurierten WCAG-/Best-Practice-Tags, kein Überlauf, keine kaputten Bilder, keine protokollierten externen Anfragen oder Laufzeitfehler. Der Reflowfall ist B04, kein echter Zoomnachweis.

Eigene Screenshots der Startseite und des geänderten Projektabschnitts wurden bei allen fünf Breiten angesehen. Die Gestaltung bleibt im bestehenden Raster: große Serifen, unverdeckte Texte, unter 860 px gestapelte Bereiche, vollständig sichtbare Gemälde mit getrennten Bildunterschriften und erreichbarer Steuerung. Bei 320 px blieb die Wortmarke in einer Zeile; Texte wurden innerhalb des Viewports umbrochen. Keine sichtbare Teststartaktion und kein Ergebnis wurden gefunden.

Der zusätzliche gezielte Chromiumlauf enthält 51 Beobachtungen. Alle sechs Inhaltsverzeichnislinks führten bei 1440, 390 und 320 px zum richtigen `/projekt#…`-Ziel und fokussierten dessen Element. Wortmarke, Sprunglink und Galerielink zu den Bildnachweisen funktionierten; neun Bildnachweise waren erreichbar. GitHub-Linkziel direkt per HTTP mit Status 200 geprüft. Der lokale Schriftlizenztext war bei allen drei Größen mit Status 200 erreichbar und enthielt den OFL-Text. Externe Bildnachweisziele wurden als tatsächliche URLs dokumentiert; deren vollständige Rechteprüfung wurde nicht wiederholt.

Vor-/Zurück-Steuerung der Galerie änderte den Zähler und stellte ihn wieder her. Aktuell sichtbar war jeweils eine aktive Folie, fünf andere waren `inert` und `aria-hidden`; in Pause war die Beschriftung `aria-live="polite"`. Die Projektprüfung beobachtete mindestens drei automatische Wechsel und zehn Sekunden Stillstand bei reduzierter Bewegung. Im eigenen Lauf blieben manuelle Pause und dauerhafte Tastaturpause jeweils neun Sekunden stabil. Die Steuerung hatte sichtbaren Fokus.

Ein erster zusätzlicher Lauf las nach Galerieaktionen zu früh vor dem Angular-Renderschritt und protokollierte noch alte Zählerstände. Dieses ursprüngliche Protokoll bleibt erhalten. Der korrigierte Lauf wartet vor der Messung auf den nachfolgenden Renderschritt; Vor/Zurück und Tastaturpause stimmen dort überein. Die erste Messung wird nicht als bestätigter Anwendungsfehler ausgegeben.

In den gezielten lokalen Abläufen wurden je Breite 31 Anfragen protokolliert, sämtlich an den lokalen Server, ohne Anfragekörper. Keine Laufzeit- oder fehlgeschlagenen Anfragen. `localStorage`, `sessionStorage`, Cookies, IndexedDB, CacheStorage und Service-Worker-Registrierungen waren leer. Es gibt keine Eingabefelder. Das gilt für die vorhandene Informationswebsite; eine Antwortdatenübertragung eines zukünftigen Testablaufs wurde damit nicht geprüft.

## Prüfstatus und Grenzen

| Prüfung                                                                          | Status                             | Umfang                                                                               |
| -------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------ |
| v1/v2-Hashes und Zuordnung der sichtbaren Website                                | BESTANDEN                          | Fassungsintegrität; kein Gütenachweis                                                |
| I01/P01, I02, I03 und A01 als Regel-/Wortlautkorrekturen                         | BESTANDEN                          | Grenzen oben; keine Gesamtfreigabe                                                   |
| Bestehende drei eingefrorene Infrastrukturtests                                  | BESTANDEN                          | Drei Tests mit synthetischen Dateien; ihre Gegenbeispielabdeckung ist unvollständig  |
| Öffentliche Eingabe- und Archivgrenzen                                           | NICHT_BESTANDEN                    | B01 und B02                                                                          |
| Formale DONE-Kontrolle                                                           | NICHT_BESTANDEN                    | B03; realer Paketstatus weiterhin RUNNING                                            |
| Eingefrorenes `status`                                                           | BESTANDEN                          | Exit 0, Zustand ohne Schemafehler                                                    |
| Eingefrorenes `all`                                                              | BLOCKIERT                          | Exit 2, wissenschaftliche Reproduktion ausdrücklich blockiert; keine Analyse erzeugt |
| Isolierter `pnpm check`                                                          | NICHT_BESTANDEN                    | Formatierung grün, Handbuchcheck mit zwei Semikolons fehlgeschlagen                  |
| Separate Typprüfung, Unit-Tests und Build                                        | BESTANDEN                          | Je Exit 0, neun Tests; ersetzt den fehlgeschlagenen Gesamtcheck nicht                |
| Lokale Chromiumrouten, fünf Breiten, axe und zusätzliche Bedienabläufe           | BESTANDEN                          | Beobachteter Chromiumumfang; keine vollständige WCAG-Konformitätsgarantie            |
| Nativer T3-Smartphonewechsel                                                     | BLOCKIERT                          | Resize-Timeouts; keine bestätigte native Smartphonebreite                            |
| Tatsächlicher 200-%-Browserzoom                                                  | NICHT_GEPRÜFT                      | Reflow nicht gleichgesetzt                                                           |
| Ergebnisrechnung und Python-/Browserparität                                      | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Kein freigegebenes Modell, kein Test oder Ergebnis vorhanden; später Pflicht         |
| Antwortdatenübertragung im vollständigen Testablauf                              | IN_DIESER_PHASE_NICHT_ERFORDERLICH | Kein solcher Ablauf vorhanden; tatsächlicher zukünftiger Ablauf NICHT_GEPRÜFT        |
| Empirische Güte, Claude-/Setup-/Releaseabnahmen und menschliche Verständlichkeit | NICHT_GEPRÜFT                      | Nicht durch dieses technische KI-Review ersetzt                                      |

Für den technischen Komponentenlauf wurde eine separate öffentliche Fassung im eigenen Outputordner aus dem angegebenen Commit plus den v2-Overrides hergestellt. Daten, Berichte und verwaltete Skills wurden dort nicht als Prüfinhalte kopiert; sie sind auch im technischen Formatcheck ausgeschlossen. Bereits vorhandene Abhängigkeiten wurden verknüpft. Keine aktuellen Forschungsentwürfe wurden dadurch zum Prüfgegenstand.

Zwei anfängliche pnpm-Aufrufe versuchten wegen der neuen Arbeitswurzel eine automatische Abhängigkeitsaktualisierung. pnpm verweigerte dies mit `ERR_PNPM_UNSAFE_MODULES_DIR`; keine erfolgreiche Installation oder Entfernung gemeinsamer Abhängigkeiten. Ein versuchter direkter CLI-Schalter war unbekannt. Nach Lesen der installierten pnpm-Implementierung wurde ausschließlich für diese Prüfprozesse `pnpm_config_verify_deps_before_run=false` gesetzt. Danach lief der eigentliche Check und zeigte B05. Alle abgebrochenen Aufrufe bleiben als separate Logs erhalten. Systemweite Einstellungen wurden nicht verändert.

## Werkzeuge, Zeit und Belege

Erste eigene UTC-Messung: `2026-10-03T01:58:34.328972Z`. Abschluss der inhaltlichen Nachprüfung und erneuter Paketkontrolle: `2026-10-03T02:15:11Z`; danach nur Bericht, gezielte Formatprüfung und Hashabschluss. Modelleinstellung ohne eigenen Override; das eingefrorene Arbeitsloop-Dokument nennt `gpt-6.1-sol` als Laufzeitfamilie. Eine interne Modellrevision oder das Modell über eine separate API konnte ich nicht überprüfen. Kein Claude-Review und kein akademisches Peer Review.

Genutzt wurden `functions.exec`, `exec_command`, Python-Standardbibliothek, Git-Objektlesen, `rg`, Node, pnpm, lokales Playwright/axe, native T3-Browserwerkzeuge, Webtool, HTTP-Abruf öffentlicher Originalquellen, `view_image`, `apply_patch` und Nachrichten an den Koordinator. `unslop` wurde für den Bericht angewandt. Keine weitere Delegation, keine Nachrichten an Dritte, kein Commit, Push, Merge, Deployment oder Rohdatenzugriff. Gemeinsame Forschungs-, Web-, Pipeline-, Erstbericht- und Paketdateien wurden nicht verändert.

Der tatsächliche Startauftrag ist wortgetreu in `outputs/loop/recheck-browser/startauftrag.txt` gesichert. Sämtliche eigenen synthetischen Dateien, Browserbilder, Logs und Abrufe liegen unter diesem ausgeschlossenen Outputordner. Zentrale Belege:

- `package-verification.json`: beide Pakete und Webzuordnung.
- `infrastructure.py`, `infrastructure.json`, `frozen-tests.log`, `frozen-status.json`, `frozen-all.json`: ausgeführte formale und synthetische Prüfungen.
- `native-browser.json`, `native-gallery.json`: explizite Tab-ID, tatsächliche Viewports, Wortlaut und native Bedienung.
- `broad-browser.log`, `check-browser-copy.mjs`, `broad-screenshots/`: bestehende Prüfung mit getrennten Ablagepfaden.
- `targeted-browser.json` und `targeted-settled/targeted-browser.json`: erste und korrigierte gezielte Beobachtungen; die erste Datei liegt direkt im Outputordner.
- `home-1024-top.png`, `home-768-top.png`, zugehörige Projektbilder und Bilder unter `targeted-settled/`: tatsächlich angesehene Größen und Textabschnitte.
- `ess-source.json`, `ess-disclaimer.html`, `ess-disclaimer.txt`, `github-target.json`: Originalfundstelle und Linkzugang.
- `technical-inputs.json`, `pnpm-check-final.log`, `technical-components.json`, Komponentenlogs: genaue technische Fassung und tatsächliche Ergebnisse.

Dieser Erstbericht wird vor Abschluss ausschließlich selbst formatiert und anschließend gehasht. Nach Abschluss bleibt er unverändert. Weitere Korrekturen benötigen eine neue Fassung und einen getrennten Nachprüfbericht. Die offenen B01–B05 sowie die ungeprüften Pflichtbereiche erlauben hier keine vollständige LOOP-000-, wissenschaftliche oder Releaseabnahme.
