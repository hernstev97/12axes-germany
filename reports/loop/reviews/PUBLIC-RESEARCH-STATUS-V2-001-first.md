# Erstprüfung PUBLIC-RESEARCH-STATUS-V2-001

**Urteil: CHANGES_REQUESTED_BOUNDED.** Ein konkreter Statusblocker in der festen Fassung. Das Urteil gilt ausschließlich für die öffentliche Inhaltskommunikation dieses Pakets. Es ist keine methodische, rechtsfachliche oder menschliche Freigabe und kein Neutralitätsnachweis.

Prüfer: frischer begrenzter Codex-Subagent, gleiche Codex-Modellfamilie wie die genannten Forschungsrollen. Gemeinsame Modellfehler bleiben möglich. Keine anderen Ersturteile oder Reviewerberichte gelesen; die im erlaubten Exportentscheid enthaltenen Rollen-, Hash- und Entscheidmetadaten wurden als deklarierte Entscheidmetadaten genutzt.

Paket: `PUBLIC-RESEARCH-STATUS-V2-001/v1`. Worktree: `/home/stevenh/projects/.worktrees/12axes-germany/life93-night-20261003`. Prüfabschluss UTC: 2026-10-03T15:44:12.384425+00:00.

Manifest SHA-256: `af0f915c6fde1bb53cea018085036abd59b3ae6b11a038f8e67b6c9afe74f7ac`. Manifest und alle 28 öffentlichen Artefaktpins stimmen bei Erstabgleich und unmittelbar vor dem Schreiben dieses Berichts. Keine Paketdatei verändert.

## Konkreter Blocker

### PRS-V2-001, P2: Abgeschlossene Gruppenläufe erscheinen als noch ausstehende Ergebnisrechnung

Fundstellen:

- `web/src/app/pages/project/project.html:235–237`: „Eine getrennte historische Gruppenanalyse läuft für ESS5, ESS8 und ESS9. Ihre Ergebnisse und Anzeige stehen noch aus.“
- `web/src/app/pages/methodology/methodology.html:227–228`: „Eine eigene historische Gruppenanalyse läuft derzeit nur für ESS5, ESS8 und ESS9. Ergebnisse und Anzeige stehen aus.“
- Mitbetroffen ist die verkürzte Statusangabe `web/src/app/pages/home/home.html:136`: „Die historische Gruppenanalyse läuft getrennt.“

Die gepinnten Belege melden dagegen bereits drei ausgeführte private Gruppenläufe: `reports/loop/group-v21-run-receipts.json:9–54` führt ESS5, ESS8 und ESS9 mit jeweils Abschlusszeit und `exit_code: 0`. `reports/loop/group-v21-access-disclosure.json:3–19` nennt ausdrücklich `THREE_PRIVATE_HISTORICAL_GROUP_RUNS_COMPLETE_PENDING_RESULT_REVIEW`, dieselben drei zugelassenen und die zwei ausgeschlossenen Studien. Laut deklariertem Laufintervall waren die Läufe am 3. Oktober 2026 um 15:24:28 UTC abgeschlossen. Die Kandidaten bleiben privat; Veröffentlichung und neue UI sind dadurch nicht erlaubt (`group-v21-access-disclosure.json:34–40`). Diese Metadaten wurden nicht durch privaten Datenzugriff reproduziert.

„Läuft“ allein könnte noch den gesamten Forschungsprozess meinen. Zusammen mit „Ergebnisse stehen aus“ verschiebt der Text aber die belegte Grenze: Private Ergebnisrechnung ist erfolgt; Ergebnisreviews und Veröffentlichung sind offen. Gerade die Statusseite soll diese beiden Zustände unterscheiden. Das ist ein Tatsachen-/Bedeutungsbefund, kein Stilwunsch.

Erforderliche Korrektur in den betroffenen öffentlichen Angaben, beispielsweise:

> Die drei getrennten historischen Gruppenläufe für ESS5, ESS8 und ESS9 sind ausgeführt. Ihre privaten Ergebnisfassungen warten auf zwei Ergebnisreviews. Veröffentlichung und Anzeige sind noch nicht freigegeben. Für ESS10-SC und ESS11 liegt daraus keine Gruppenfreigabe vor.

Für die kurze Startseitenzeile genügt entsprechend „Drei getrennte Gruppenläufe ausgeführt. Ergebnisreviews und Veröffentlichung offen.“ Die Formulierung darf keine bereits bestandenen Ergebnisreviews behaupten.

## Inhaltsabgleich ohne weitere Blocker

- **Auswahl und Referenzen:** Der gepinnte Katalog enthält tatsächlich 43 unterschiedliche Item-IDs aus fünf Studien und acht Primärrubriken. Die fünf öffentlichen Exporte führen zusammen dieselben 43 IDs. 42 haben `reviewed_historical_reference`, genau `ESS10SCe03_2:cttresa` hat `withheld_base_or_cell_count` und `reference: null`. Die 42 IDs stimmen exakt mit den freigegebenen IDs im konkreten Exportentscheid überein. Die Textangaben 43/5/8 und 42 sind damit im erlaubten Paket belegt. Daraus folgt kein wissenschaftlicher Gütewert.
- **Trennung der Messgegenstände:** Die Seiten behandeln Rubriken als Inhaltsordnung und verneinen gemeinsame Messdimensionen, gemeinsame Personen, Gesamtscores und Links-/Rechtspositionen. Zustimmung, Wichtigkeit und nominale Auswahl werden nicht gleichgesetzt. Die historischen neun Fragen erscheinen ausdrücklich als Teilmodul, das kein umfassendes Politikprofil trägt (`project.html:118–158`). Das passt zu Themenmatrix und Empirieplan; der alte Neunerbestand selbst wurde in diesem Auftrag nicht neu vollständig geprüft.
- **Historische Grenzen:** Ausgaben und Feldzeiten auf der Methodikseite stimmen mit den fünf Studienmetadaten des Katalogs und der gepinnten Themenmatrix überein: ESS5 3.6, 2010–2011; ESS8 2.3, 2016–2017; ESS9 3.3, 2018–2019; ESS10-SC 3.2, 2021–2022; ESS11 4.2, 2023. ESS10-SC bleibt Papier/CAWI und wird nicht durch CAPI ersetzt. Die ausgelassene Stadt München ist für ESS8 sichtbar; Gewichtung wird nicht als nachträgliche Erhebung fehlender Münchener Antworten ausgegeben. Keine heutige 2026-Norm wird behauptet.
- **Kontext und Webübertragung:** B1–B12-Originalfolge, B12 als primär europäische Integration, B25 ohne B26–B29 und der nicht belegte operative CAWI-Nachlauf werden offengelegt. Der Elternzeit-/Doppelverdienerkontext ist genannt. Die Website behauptet keine empirisch belegte Gleichwertigkeit einer neuen Administration. Das entspricht Kataloggruppen, den beiden verbleibenden Katalogbindungen, Empirieplan und Messformenentwurf. Die Krosnick-Fundstellen wurden aus dem gepinnten Messformenentwurf abgeglichen, nicht am Original-PDF erneut geprüft.
- **Auswertung:** `pspwght` ohne zusätzliche `dweight`-Multiplikation, Fragenenner und getrennte Missing-Gründe stimmen mit dem gepinnten Plan und der Exportstruktur überein. Alle 42 Referenzobjekte verwenden `pspwght`, haben die originalen Kategorie-IDs und dokumentieren die beiden vorgesehenen Sensitivitätsfelder. Ihre `uncertainty` ist null. Keine Neuschätzung oder erneute Prüfung der gewichteten Werte erfolgte. Der öffentliche Text verneint SE/CI und persönliche Unsicherheiten ausdrücklich. Die 100-/Ein-bis-vier-Fälle-Regel wird zutreffend als Projektheuristik ohne Präzisions- oder Anonymitätsgarantie beschrieben.
- **Fairness und Freigaben:** Teilabdeckung und offene Inhaltslücken bleiben sichtbar. Es gibt keine moralische Bewertung, Parteiprogrammbehauptung, Parteienzuordnung oder Gesamtmatch-Aussage. Bekannte v1-A/B-Antworten werden nicht als neue unberührte Bestätigung ausgegeben. Codex, CodeRabbit und technische Prüfungen werden von empirischer Evidenz, Fachbegutachtung und Abnahmen getrennt. Same-family-Grenzen stehen auf Projekt- und Methodikseite. Die Claude-Schlusskontrolle, Verständnistests mit Menschen, menschliche Test-/Ergebnisgestaltung und Veröffentlichung bleiben ausdrücklich offen. Ich habe diese offenen Prüfungen nicht durchgeführt.
- **Rechte und öffentlicher Status:** Dokumentations- und Datenlizenz werden getrennt beschrieben, GLES/ISSP als mögliche Ergänzungen mit offenen Nutzungswegen benannt und Rohdaten aus der Website ausgeschlossen. Dies ist ein Abgleich mit der gepinnten Lizenzakte, keine aktuelle rechtsfachliche Quellenprüfung. In den erlaubten Templates und im Shell gibt es keinen sichtbaren Teststart; die einzige Primärschaltfläche führt zum Projektstand. Die gepinnte öffentliche Preview-Routenliste ist leer.

Der konkrete Root-Exportentscheid erlaubt öffentliche historische Referenzableitungen auf dem Forschungsbranch, ausdrücklich ohne aktuelle Norm-, Instrument-, Design-, menschliche, rechtliche oder Releaseabnahme. Seine enthaltenen Angaben über bereits gelesene Berichte und private Byteprüfungen sind Deklarationen des Entscheids. Ich habe die dort genannten privaten Dateien und fremden Berichte nicht geöffnet und daraus keine eigene Rohreproduktion oder unabhängige Prüfung dieser Abläufe abgeleitet.

## Hinweise ohne Sperrwirkung

Die Formulierung „begrenzt geprüft“ könnte den tatsächlich geprüften Umfang noch verständlicher benennen, etwa als Prüfung der öffentlichen Referenzfassungen ohne unabhängige Rohreproduktion. Die benachbarten Vorbehalte verhindern bereits eine Behauptung methodischer Validierung. Dies ist deshalb kein zusätzlicher Blocker. Keine weiteren Stilwünsche.

## Tatsächliche Checks, Lesescope und Grenzen

Durchgeführt, jeweils erfolgreich:

1. SHA-256 des Manifests und aller 28 explizit gepinnten öffentlichen Dateien, zweimal. Kein Zugriff auf verbotene Pfade.
2. Lokaler JSON-Identitätsabgleich aller 43 Katalog-IDs, aller fünf öffentlichen Exporte, 42 zugelassenen Export-IDs, der einen zurückgehaltenen Referenz, Kategorie-IDs, Exporteditionen, Gewichts-/Sensitivitätsfeldern und null gesetzter Unsicherheit. Keine neuen statistischen Werte berechnet.
3. Statischer HTML-Abgleich der drei Seiten: jeweils eine H1; eine Primärschaltfläche auf der Startseite, keine auf Projekt-/Methodikseite; alle `routerLink`-Ziele und Fragmente der drei Templates finden ein Ziel in den gepinnten öffentlichen Seiten. Öffentliche Routenliste und Shell gelesen.
4. Vollständige Lektüre des Handbuchs und der vier Seitentextdateien, `docs/project.md`, Themenmatrix, Empirieplan, Messformenentwurf und Lizenzakte. Die übrigen gepinnten TS-/SCSS-/Shell-/Routendateien vollständig gelesen. Manifest, Exportentscheid und alle drei Run-/Zugriffsnachweise vollständig gelesen. Katalog vollständig als JSON geparst; alle 43 Frageformulierungen samt Einleitung, Stamm, Szenario, Anweisung, Primärthema und Bindungsstatus gelesen, dazu relevante Studien-/Gruppen-/Restbindungsmetadaten. Alle fünf Exporte vollständig geparst und im beschriebenen Identitäts-/Strukturumfang geprüft. Nicht jede einzelne veröffentlichte Zahlenzelle fachlich neu bewertet.

Nicht durchgeführt: `pnpm check`, Build, Browser, Accessibility-Lauf, Live-/GitHub-Linkprüfung, Netzabrufe, Authentifizierung, Git-Befehle, Installation, Serverstart, Kontakte, neue wissenschaftliche Schätzung, Gesamtquellenprüfung oder Prüfung privater Aggregate. Kein Lesen, Auflisten, Statten oder Hashen von `data/raw/` oder `data/local/`. Keine Autorenverteidigung, State-/Handoff-Datei, Elternkontext oder andere Reviewerprosa als Evidenz genutzt. Browserprüfung und integrierte technische Checks bleiben getrennte Aufgaben außerhalb dieses Urteils.

Einige zu große zusammengefasste Toolausgaben waren zunächst gekürzt. Fehlende Handbuch-/Projekt-/Themenmatrix-/Empirieplanpassagen und Seitentexte wurden danach in vollständigen beziehungsweise kleineren Ausgaben gelesen. Kein verbleibender Inhaltsblocker wurde durch einen ausgelassenen Test als behoben erklärt. Ausführbare lokale Abgleiche lieferten Exitcode 0; kein fehlgeschlagener oder behaupteter Browser-/CI-Test.

Verändert wird ausschließlich dieser eigene Bericht. Synchronisierte Skills und Ausgangsberichte bleiben unverändert. Die Schreibsprache wurde nach dem gelesenen `unslop`-Skill geprüft.

## Tatsächlich verifizierte öffentliche Pins

Die SHA-Spalte ist die jeweils tatsächlich berechnete Prüfsumme. Sie stimmt mit dem Manifest überein.

| Datei | Tatsächliche SHA-256 | Befund |
| --- | --- | --- |
| `web/src/app/pages/home/home.html` | `c2530f88e3e1491333c24e0ccb4e12341ac11a8de987e96ee8c71bbd99b510fc` | stimmt |
| `web/src/app/pages/home/home.scss` | `a9b8a777a5c46147547b215de18657be3b6c4e77a192273e9d24b7b8ee300b94` | stimmt |
| `web/src/app/pages/home/home.ts` | `cdc1ae74bfeef8880af8ae25f44db946f71c6508b937483b2e0fb1c42af7ae82` | stimmt |
| `web/src/app/pages/project/project.html` | `2fd16b5fecd8792804a4420985a5c6c837ea75c9e07bc048fda4fd726d13b137` | stimmt |
| `web/src/app/pages/project/project.scss` | `c4c50f7d7552e3978c02df643204217c0ddcb530044e7503099ef2d86d7dc6f2` | stimmt |
| `web/src/app/pages/project/project.ts` | `d7f09ba634b61f13c6f07657e78b05fb16a672a48d2eb0627d9b911c3e3cabcf` | stimmt |
| `web/src/app/pages/methodology/methodology.html` | `5bfb0ee79cd9dfd2714cd53492652281db562d4da907e70a3f6127dc73321f99` | stimmt |
| `web/src/app/pages/methodology/methodology.scss` | `ec2c89fde913caff741baa0b0f3cf68a9acb5e85467e4f21b6c824fdad201394` | stimmt |
| `web/src/app/pages/methodology/methodology.ts` | `c1a2819ed6486f13a28447b39ba3a0d0d57b8232da4cf80de024734117d3b317` | stimmt |
| `web/src/app/app.html` | `dac5494b1ad8339c9fca675ff09b243b4fb3dda9a286ab984f77bed40f6a56ac` | stimmt |
| `web/src/app/app.routes.ts` | `d1ad2dc6a5abd0f51aa0a14c79210d9709c19f272af0efca275719bf4cd925b1` | stimmt |
| `web/src/app/research-preview.routes.ts` | `d9bda2c42f9c8edec6f02ab7a3d5dd71df6c8e5afe91fe3f33f8b4e1d3bb341a` | stimmt |
| `docs/project.md` | `50fd74dc5612293f22591e679856dbb09745ef2ff9a217ff5583b219cf224328` | stimmt |
| `docs/handbuch.md` | `34e62abe5024bd035a52dd7efae3ca392f86422b298ef32ba720e12563dca17a` | stimmt |
| `docs/abdeckung-v2.md` | `77ae3d328c4862d1396e72207e5e1401dfa4da1f57580315e973943d3dfad945` | stimmt |
| `docs/empirie-plan-v2.entwurf.md` | `2b0cd26f8fba81bbf520b9ae3411d623f9299c9ff707aacf681bde4c65a0439f` | stimmt |
| `docs/messformen-v2.entwurf.md` | `0536441391becb9ac84e4b9596b20e2e0e4aab1a9aef827cbc162f8d7261238b` | stimmt |
| `docs/lizenzen.md` | `b5b0303ec23bc4bbc8dba1f59994c9ccd7cd90c76474157399cf78d616753dcb` | stimmt |
| `data/politikprofil-v2.fragen.entwurf.json` | `5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4` | stimmt |
| `reports/loop/policy-v2-export-decisions.json` | `a87f780a7219253f7f3773d051b7001f438b19b2fb2d0ee820fc22c1157a16df` | stimmt |
| `reports/loop/policy-v2-run-receipts.json` | `1d957ae0833f23ef34239f889bc9ce00771557c9e5ad096dfe6bd91f3709cfae` | stimmt |
| `reports/loop/group-v21-run-receipts.json` | `e7d2dd5db68f953649d63adb0a13da88373354b7c09158462884239d1873d4c9` | stimmt |
| `reports/loop/group-v21-access-disclosure.json` | `25476bdf5b6338e0c63ff6db050928c9a2859cbafcfe7b6a9b63af2e1db8dde6` | stimmt |
| `data/reference-v2/ESS5e03_6.json` | `e489fe013d1cbd3d72b9ae816e422757ce8d34ae575d09f64df13a1750dc4bc6` | stimmt |
| `data/reference-v2/ESS8e02_3.json` | `fb720cc18049f037ed86670bd76a51c3c1770342a61f5627b7afbfb127898ad7` | stimmt |
| `data/reference-v2/ESS9e03_3.json` | `34e71b448c0c315cf9f19bda30628874c95464faf661813a65f25a3f9ad82be2` | stimmt |
| `data/reference-v2/ESS10SCe03_2.json` | `e75dfbadcf68c14dce9d13c8a8a2dd1abc6e8a6e96618f960c8cd61c54bc3184` | stimmt |
| `data/reference-v2/ESS11e04_2.json` | `453d8ce3273c9e29bb08a49be6e69da46591e3d1ed89f306051b085c511ec721` | stimmt |
