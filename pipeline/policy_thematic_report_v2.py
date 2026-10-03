"""Pure semantic Markdown presentation of separately reviewed public v2 exports.

No IO or new estimator. The unchanged technical renderer checks every public
export first. Catalogue authenticity and actual review bytes belong to the
external pinned build, not to this in-memory API or a status string.
"""

from enum import Enum
from html import escape
import re
from urllib.parse import quote, urlsplit

from pipeline.policy_export_v2 import _json_values, ExportErrorCode
from pipeline.policy_report_v2 import (
    PolicyReportError, render_historical_report, _VARIABLES, _decimal,
    _percentage,
)


def _md(value):
    # These values enter Markdown text, never HTML attributes. Encode HTML
    # delimiters while keeping quote characters literal: numeric quote entities
    # would have their '#' escaped by the Markdown layer and become visible.
    text = escape(str(value), quote=False).replace("\r", " ").replace("\n", " ")
    return re.sub(r"([\\`*_{}\[\]()|#+.!-])", r"\\\1", text)


THEMES = (
    ("economy_distribution", "Wirtschaft und Verteilung", ("sofrdst", "sofrwrk", "sofrpr", "sofrprv", "gincdif"),
     "Gleichheit, Leistung, Bedarf, Herkunftsprivileg und staatliche Einkommensverringerung bleiben getrennte Gegenstände. Keine Gesamtposition zur Wirtschaft.",
     "Markt- und Eigentumsordnung, Wettbewerb, Steuerarten, Arbeits- und Industriepolitik bleiben unvollständig."),
    ("welfare", "Sozialstaat", ("gvslvol", "gvslvue", "gvcldcr", "bnlwinc", "eduunmp"),
     "Staatliche Verantwortung, Leistungszielgruppe und der feste Ausbildungs-/Leistungsbudgetkonflikt werden unterschieden. Kinderbetreuung zählt hier einmal als Primärgegenstand.",
     "Gesundheit, Pflege, Wohnen und konkrete Leistungserbringung sind nicht ausreichend erschlossen."),
    ("democracy_authority", "Demokratie und politische Autorität", ("fairelc", "dfprtal", "medcrgv", "rghmgpr", "votedir", "cttresa", "gptpelc", "gvctzpv", "grdfinc", "viepol", "wpestop", "scchpldm"),
     "Normative Wichtigkeit für Demokratie im Allgemeinen und die einzelne Regierungsreaktion bei Mehrheitskonflikt sind keine wahrgenommene Umsetzung und keine objektive Demokratiequalität. Kein Populismus- oder Autoritarismuslabel für Personen.",
     "Föderalismus, kommunale Mitbestimmung, Parteienfinanzierung und weitere konkrete Machtkonflikte bleiben offen."),
    ("rights_security", "Bürgerrechte und Sicherheit", ("bplcdc", "dpcstrb", "hrshsnta", "dbctvrd", "lwstrob", "rgbrklw"),
     "Pflichtgefühl gegenüber Polizei, Strafverschärfung und Rechtsbindung sind einzelne historische Gegenstände. Bei härteren Strafen bezeichnet ‚heute‘ den damaligen Kontext 2010/2011.",
     "Digitale Überwachung, Datenschutz, konkrete Sicherheitsanlässe und Strafverfahrensgarantien sind nicht umfassend enthalten."),
    ("europe", "Europäische Integration", ("vteurmmb", "keydec", "euftf"),
     "Mitgliedschaftsszenario, nationale Zuständigkeit als Demokratieprinzip und Integrationsumfang bleiben getrennt. Leerer/ungültiger Stimmzettel, Nichtwahl und Nichtstimmberechtigung sind gültige Originaloptionen, keine politische Mitte und kein EU-Gesamtscore.",
     "Gemeinsame Fiskal-, Sozial- und Außenpolitik sowie institutionelle Gestaltung und Solidarität sind unvollständig."),
    ("climate_energy", "Klima und Energie", ("inctxff", "sbsrnen", "banhhap"),
     "Drei konkrete Instrumente: fossile Abgabe, Erneuerbarenförderung und Verkaufsverbot. Unterstützung eines Instruments bedeutet keine gesamte Energieposition.",
     "Versorgungssicherheit, Netze, Speicher und Energieträgerwahl bleiben offen."),
    ("migration", "Migration", ("imsmetn", "imdfetn", "impcntr", "imsclbn"),
     "Zulassungsumfang für die ausdrücklich genannten Gruppen und Bedingungen gleicher Sozialleistungsrechte bleiben verschieden. Historische Gruppenbegriffe werden zitiert; keine Motive oder tatsächlichen Migrationsfolgen daraus ableiten. Die nominalen Bedingungen werden nicht zu Aufenthaltsdauer oder Ideologiepunkten umgerechnet.",
     "Schutz-/Asylpolitik, Staatsbürgerschaft, Teilhabe und konkrete Grenz-/Abschiebemaßnahmen bleiben unvollständig."),
    ("equality_family", "Gleichstellungs- und Familienpolitik", ("eqparep", "eqparlv", "freinsw", "fineqpy", "wrkprbf"),
     "Konkrete Eingriffe und Erwerbs-/Familienfinanzierung bleiben Einzelmaßnahmen. Elternzeit enthält das vollständige Doppelverdiener-, Verdienst-, Neugeborenen- und Anspruchsszenario; Familienleistungen behalten die ausdrücklich höhere Steuerlast.",
     "Reproduktive Selbstbestimmung, vielfältige Lebensformen, Behinderung und weitere Diskriminierungsgründe sind unvollständig."),
)

_THEME_BY_VARIABLE = {var: key for key, _, variables, _, _ in THEMES for var in variables}


class ThematicErrorCode(str, Enum):
    INVALID_INPUT = "invalid_input"
    CATALOGUE_BINDING = "catalogue_binding"
    INVALID_SOURCE = "invalid_source"


class PolicyThematicReportError(ValueError):
    def __init__(self, code):
        self.code = code
        super().__init__(f"policy_thematic_report_error: {code.value}")


def _require(condition, code=ThematicErrorCode.CATALOGUE_BINDING):
    if not condition:
        raise PolicyThematicReportError(code) from None


def _text(value, nullable=False):
    _require((nullable and value is None) or (type(value) is str and bool(value)))


def _texts(value):
    _require(type(value) is list)
    for text in value:
        _text(text)


def _https(value):
    _text(value)
    p = urlsplit(value)
    _require(p.scheme == "https" and bool(p.hostname) and not p.username and not p.password
             and not any(c.isspace() for c in value), ThematicErrorCode.INVALID_SOURCE)
    return quote(value, safe=":/?&=%#@+;,-._~")


def _sources_and_items(catalogue, contracts):
    _json_values(catalogue, ExportErrorCode.INVALID_CONTRACT)
    _require(type(catalogue) is dict and catalogue.get("schemaVersion") == 1)
    sources = {}
    for source in catalogue["sources"]:
        _text(source["id"])
        _require(source["id"] not in sources)
        _https(source["publicUrl"])
        _text(source["kind"])
        _text(source["licenseId"], nullable=True)
        _text(source["retrievedUtc"])
        _require(re.fullmatch(r"[0-9a-f]{64}", source["originalBytesSha256"]) is not None)
        _require(type(source["httpStatus"]) is int and source["httpStatus"] == 200)
        sources[source["id"]] = source
    _require(type(catalogue["studies"]) is list and len(catalogue["studies"]) == 5)
    study_map = {s["id"]: s for s in catalogue["studies"]}
    _require(len(study_map) == 5 and set(study_map) == set(_VARIABLES))
    definitions = {}
    for study in contracts:
        meta = study_map[study["study_id"]]
        _require(meta["edition"] == study["edition"] and meta["country"] == "DE")
        for key in ("dataDoi", "documentationDoi", "populationDeclaredEn", "fieldwork", "versionNotes"):
            _require(meta[key] == study["provenance"][key])
        definitions.update({q["question_id"]: q for q in study["adapter"]["questions"]})
    items = {}
    _require(type(catalogue["items"]) is list and len(catalogue["items"]) == 43)
    for item in catalogue["items"]:
        qid = item["id"]
        _require(type(qid) is str and qid in definitions and qid not in items)
        _require(qid == item["studyId"] + ":" + item["variable"]
                 and item["primaryTheme"] == _THEME_BY_VARIABLE[item["variable"]])
        _text(item["originalQuestionId"])
        _text(item["wordingDe"])
        _texts(item["introductionsDe"])
        for key in ("responseStemDe", "situationDe", "instructionDe"):
            _text(item[key], nullable=True)
        definition = definitions[qid]
        _require([c["code"] for c in item["categories"]] == definition["categoryCodes"]
                 == item["apiValidCodeOrder"])
        for category in item["categories"]:
            _text(category["labelDe"])
            _text(category["printedCodeDe"], nullable=True)
            _require(category["isMissingApi"] is False and category["labelSourceRef"] in sources)
        _require({m["code"]: m["reasonApi"] for m in item["missingCodes"]}
                 == {c: r for c, r in definition["missingCodes"].items() if c != ""})
        _require(len({m["code"] for m in item["missingCodes"]}) == len(item["missingCodes"])
                 and item["notAskedCodes"] == definition["structurallyNotAskedCodes"])
        for missing in item["missingCodes"]:
            _require(missing["isMissingApi"] is True)
            _text(missing["labelDe"], nullable=True)
            _text(missing["printedCodeDe"], nullable=True)
        _texts(item["mappingNotes"])
        _require(type(item["sourceRefs"]) is list and bool(item["sourceRefs"]))
        for ref in item["sourceRefs"]:
            _require(ref["sourceId"] in sources)
            if "pdfPages" in ref:
                _require(type(ref["pdfPages"]) is list and bool(ref["pdfPages"])
                         and all(type(n) is int and n > 0 for n in ref["pdfPages"]))
        mode = item["modeBinding"]
        _text(mode["boundOriginalForm"])
        if mode["cawiWordingDe"] is not None:
            _text(mode["cawiWordingDe"])
            _texts(mode["cawiIntroductionsDe"])
            _require(mode["cawiSourceRef"] in sources
                     and [c["code"] for c in mode["cawiCategories"]] == definition["categoryCodes"])
            for category in mode["cawiCategories"]:
                _text(category["labelDe"])
                _text(category["displayedCodeDe"], nullable=True)
            _texts([mode["cawiDifferenceFromPapi"]])
        items[qid] = item
    _require(set(items) == set(definitions))
    group = catalogue["groups"]
    expected = ["ESS10SCe03_2:" + var for var in _VARIABLES["ESS10SCe03_2"][:11]]
    expected.append("ESS10SCe03_2:keydec")
    _require(type(group) is list and len(group) == 1 and group[0]["itemIds"] == expected
             and group[0]["originalQuestionRange"] == "B1–B12")
    _text(group[0]["introductionDe"])
    _text(group[0]["responseStemDe"])
    return sources, items


def _link(source, pages=None):
    url = _https(source["publicUrl"])
    if pages and not urlsplit(url).fragment:
        url += "#page=" + str(pages[0])
    return "[" + _md(source["id"]) + "](" + url + ")"


def _source_refs(item, sources):
    lines = []
    for ref in item["sourceRefs"]:
        pages = ref.get("pdfPages")
        details = "physische PDF-Seite(n) " + ", ".join(map(str, pages)) if pages else "API-Metadaten"
        for key in ("originalForm", "originalQuestionId", "sourceFieldId", "sourceFieldMetadataVersion",
                    "dataFileMetadataId", "dataFileMetadataVersion", "listLabelDe", "contentCorrespondenceToPapi"):
            if key in ref:
                details += "; " + key + "=" + str(ref[key])
        lines.append(_link(sources[ref["sourceId"]], pages) + ": " + _md(details) + ".")
    return lines


def _context(item):
    lines = []
    for text in item["introductionsDe"]:
        lines.extend(["**Originaleinleitung:** " + _md(text), ""])
    for key, label in (("responseStemDe", "Antwortstamm"), ("situationDe", "Situation"),
                       ("wordingDe", "Originalfrage / Aussage"), ("instructionDe", "Originalinstruktion")):
        if item[key] is not None:
            lines.extend(["**" + label + ":** " + _md(item[key]), ""])
    return lines


def _question(item, question, sources, study):
    reference = question["reference"]
    lines = ["### `" + item["id"] + "` — " + _md(item["originalQuestionId"]), "",
             "Quelle: " + _md(study["study_id"]) + ", Ausgabe " + _md(study["edition"]) + ". "
             "Antwortform: " + _md(item["responseType"]) + "; Gegenstand: " + _md(item["responseContentType"]) + ".", ""]
    lines += _context(item)
    mode = item["modeBinding"]
    lines += ["**Gebundene Form:** " + _md(mode["boundOriginalForm"]) + ".", ""]
    if mode["cawiWordingDe"] is not None:
        for intro in mode["cawiIntroductionsDe"]:
            lines += ["**CAWI-Originaleinleitung:** " + _md(intro), ""]
        lines += ["**CAWI-Originalfrage:** " + _md(mode["cawiWordingDe"]), "",
                  "**Dokumentierte Formabweichung/-gleichheit:** " + _md(mode["cawiDifferenceFromPapi"]), ""]
    lines += ["**Originalrouting:** " + _md(item["routing"]["originalObservedRoutingDe"]), ""]
    if item["variable"] == "scchpldm":
        lines += ["B25 ist ausschließlich als statische historische Einzelfrage gebunden. PAPI: Antwort 1 → B26 (PDF12), "
                  "Antwort 2 → B28 (PDF13). B26–B29 fehlen in der Auswahl. Die CAWI-Seite PDF162 belegt keinen operativen "
                  "bedingten Nachlauf. Eine neue Webfolge zur nächsten ausgewählten Frage bleibt unvalidiert und benötigt "
                  "menschliche Gestaltung und Verständnisprüfung; keine Originaladministrationsäquivalenz.", ""]
    if reference is None:
        lines += ["**Weiterhin nicht freigegeben:** `" + question["status"] + "`. Keine Zahlenreferenz. "
                  "Null bedeutet keine verfügbare Referenz und niemals einen Anteil von null.", ""]
    else:
        lines += ["**Historische Einzelreferenz im Export freigegeben; Themenbericht weiterhin WIP.**", "",
                  "Gültiger Antwortnenner: **" + str(reference["validCount"]) + "**; alle deutschen Studienfälle: "
                  + str(reference["totalCount"]) + "; fehlend: " + str(reference["missingCount"])
                  + "; strukturell nicht gestellt: " + str(reference["notAskedCount"]) + ". "
                  "Primärgewicht: pspwght. Der Quotient bezieht sich ausschließlich auf die Gewichte gültiger Antworten "
                  "dieser Frage; deren Gewichtssumme ist im öffentlichen Export nicht separat ausgewiesen.", ""]
    lines += ["Exportcodes und Druckcodes sind getrennt; Zwischenzahlen erhalten keine erfundenen verbalen Anker. "
              "Alle gültigen Originalkategorien einschließlich unbeobachteter Kategorien bleiben erhalten.", "",
              "| Exportcode | Originallabel (Deutsch) | PAPI-/CAPI-Druckcode | Historischer Anteil (%) |",
              "| --- | --- | --- | --- |"]
    for index, category in enumerate(item["categories"]):
        printed = category["printedCodeDe"] if category["printedCodeDe"] is not None else "nicht gedruckt / nicht separat gebunden"
        fraction = _percentage(reference["categories"][index]["proportion"]) if reference else "keine Referenz"
        lines.append("| " + _md(category["code"]) + " | " + _md(category["labelDe"]) + " | " + _md(printed) + " | " + fraction + " |")
    lines.append("")
    if mode["cawiWordingDe"] is not None:
        lines += ["**CAWI-Kategorienbindung** (angezeigte Nummern sind keine ersatzweisen Exportcodes):", "",
                  "| Exportcode | CAWI-Originallabel | Angezeigter Code |", "| --- | --- | --- |"]
        for category in mode["cawiCategories"]:
            lines.append("| " + _md(category["code"]) + " | " + _md(category["labelDe"]) + " | "
                         + _md(category["displayedCodeDe"] if category["displayedCodeDe"] is not None else "keiner gedruckt") + " |")
        lines.append("")
    lines += ["**Technischer Missing-Kontext, keine politischen Antwortoptionen:**", "",
              "| Exportcode | API-Grund | Deutsches Original-Missinglabel | Druckcode |", "| --- | --- | --- | --- |"]
    for missing in item["missingCodes"]:
        lines.append("| " + _md(missing["code"]) + " | " + _md(missing["reasonApi"]) + " | "
                     + _md(missing["labelDe"] or "nicht gedruckt / nicht gebunden") + " | "
                     + _md(missing["printedCodeDe"] or "nicht gedruckt") + " |")
    lines += ["| leere Exportzelle | export\\_blank\\_unclassified | Bedeutung nicht weiter klassifiziert | kein Druckcode |", "",
              "Strukturelle Nichtgestellt-Codes: " + (", ".join(_md(c) for c in item["notAskedCodes"]) or "keine im gebundenen Adapter")
              + ". Eine gültige Antwort ‚Nicht stimmberechtigt‘ bleibt davon getrennt.", ""]
    if reference:
        lines += ["**Missing-Abrechnung auf alle deutschen Studienfälle:**", "",
                  "| Grund | Anzahl | Summe der primären Gewichte |", "| --- | --- | --- |"]
        for reason in sorted(reference["missingReasons"], key=lambda r: r["reason"]):
            lines.append("| " + _md(reason["reason"]) + " | " + str(reason["count"]) + " | " + _decimal(reason["primaryWeightSum"]) + " |")
        lines += ["", "Primäre fehlende Gewichtssumme: " + _decimal(reference["missingWeight"]) + "; primäre Gewichtssumme aller "
                  "deutschen Studienfälle: " + _decimal(reference["allDEWeight"]) + ". Keine Imputation und keine Missing-Mitte.", ""]
        sensitivity, diagnostic = reference["sensitivity"], reference["anweightEquivalenceDiagnostic"]
        lines += ["**Vorab gebundene Gewichtsvergleiche:** maximale absolute Differenz zur Primärrechnung, in Prozentpunkten: "
                  "ungewichtet " + _percentage(sensitivity["maxAbsUnweighted"]) + "; dweight "
                  + _percentage(sensitivity["maxAbsDweight"]) + "; anweight-Diagnose " + _percentage(diagnostic["maxAbsDifference"]) + ". "
                  "anweight/pspwght-Verhältnis: Minimum " + _decimal(diagnostic["ratioMin"]) + ", Maximum "
                  + _decimal(diagnostic["ratioMax"]) + "; Scope `all_de_cases` (alle deutschen Studienfälle, nicht nur gültige Frageantworten). "
                  "Keine nachträgliche Auswahlentscheidung oder wissenschaftliche Äquivalenzbescheinigung.", ""]
    lines += ["**Erlaubte Interpretation:** getrennte Antwort auf genau den zitierten Gegenstand unter dem vollständig "
              "genannten historischen Kontext. Antworttyp und Rubrik erzeugen keine allgemeine Personeneigenschaft, "
              "keine Latentskala und keine neue Politikposition.", ""]
    for note in item["mappingNotes"]:
        lines += ["Quellen-/Codegrenze: " + _md(note), ""]
    lines += ["**Konkrete Fundstellen** (PDF-Seiten physisch, 1-basiert):", ""]
    for ref in _source_refs(item, sources):
        lines += [ref, ""]
    return lines


def render_thematic_report(study_exports, analysis_contract, catalogue) -> str:
    """Render all 43 original items under eight non-latent thematic rubrics.

    Public numbers are copied/formatted only; no raw/private statistics are
    inferred. Built-in JSON inputs are not mutated. Input hashes/review truth
    require the external fixed build; this pure API cannot certify them.
    """
    try:
        _require(type(analysis_contract) is dict, ThematicErrorCode.INVALID_INPUT)
        _require(analysis_contract["catalog"]["path"] == "data/politikprofil-v2.fragen.entwurf.json"
                 and re.fullmatch(r"[0-9a-f]{64}", analysis_contract["catalog"]["sha256"]) is not None)
        rules = analysis_contract["publicationRules"]
        expected_rules = {"minimumValidCount": 100, "minimumPositiveCellCount": 5,
                          "arithmeticTolerance": 1e-12, "primaryWeight": "pspwght",
                          "sensitivityWeights": ["dweight", "unweighted"], "equivalenceDiagnostic": "anweight",
                          "descriptiveDesignVariance": False, "websiteConfidenceIntervals": False,
                          "personalUncertainty": False, "allOriginalCategoriesRetained": True,
                          "itemSelectionAfterResults": False}
        _require(all(type(rules[key]) is type(value) and rules[key] == value
                     for key, value in expected_rules.items()))
        contracts = analysis_contract["studies"]
        render_historical_report(study_exports, contracts)  # unchanged closed public validator
        sources, items = _sources_and_items(catalogue, contracts)
        study_map = {s["study_id"]: s for s in contracts}
        question_map = {q["id"]: q for export in study_exports for q in export["questions"]}
        available = sum(q["reference"] is not None for q in question_map.values())
        lines = ["# 12 Axes Deutschland: Politikprofil v2 — Methoden und historische Einzelreferenzen", "",
                 "**WIP / Entwurf für eine gezielte unabhängige Präsentationsprüfung.** "
                 "Die öffentliche Exportentscheidung betrifft " + str(available) + " historische Einzelreferenzen; "
                 "alle 43 Originalfragen aus fünf getrennten Studien bleiben im Inhaltsbestand. "
                 "Die Themenordnung ist keine Abnahme des Hauptprodukts, einer neuen Webadministration oder eines Releases.", "",
                 "## Methode und Geltungsbereich", "",
                 "Acht Rubriken ordnen konkrete Präferenzen, Prinzipien, Wichtigkeitsurteile und nominale Antworten. "
                 "Sie sind keine empirischen Dimensionen. Es gibt keine gemeinsame Personenmatrix, keinen Faktor, "
                 "Gesamtscore, persönlichen Rang, keine Partei-Gesamtübereinstimmung und keine aktuelle Bevölkerungsnorm. "
                 "Die historische Referenz beantwortet allein, wie die gebundene Originalfrage in ihrer Erhebung beantwortet wurde.", "",
                 "Primär: Summe der pspwght gültiger Antworten einer Kategorie geteilt durch die Summe der pspwght "
                 "aller gültigen Antworten derselben Frage. pspwght wird nicht nochmals mit dweight multipliziert. "
                 "Nach dem gebundenen [ESS-Gewichtungsweg](https://www.europeansocialsurvey.org/methodology/ess-methodology/data-processing-and-archiving/weighting) "
                 "kombiniert pspwght Designgewicht und Poststratifikation; anweight enthält zusätzlich die "
                 "Bevölkerungsgrößenkomponente. Ein konstanter positiver Landesfaktor ändert Quotienten nicht. "
                 "Jede Frage hat ihren eigenen gültigen Nenner. Fehlende und nichtgestellte Angaben sind ausgeschlossen "
                 "und separat abgerechnet; eine leere Exportzelle heißt export_blank_unclassified. Ungewichtete und "
                 "dweight-Rechnungen dienen getrennten Sensitivitäten, anweight einer Diagnose. Die maximale absolute "
                 "Differenz wird in Prozentpunkten dargestellt; das Gewichtsverhältnis gilt für alle deutschen Studienfälle.", "",
                 "Die vorab festgelegte 100/5-Darstellungsheuristik sperrt eine Referenz unter 100 gültigen Antworten "
                 "oder bei einer positiven ungewichteten Kategorie mit 1–4 Fällen; 100 und 5 liegen auf der zulässigen "
                 "Seite der Grenze. Keine gültigen Antworten erzeugen ebenfalls keine Referenz. Nullbesetzte Originalkategorien "
                 "bleiben erhalten. Dies sind projektspezifische Darstellungsregeln, keine wissenschaftlichen Präzisions- "
                 "oder Anonymitätsgarantien. Der öffentliche Export enthält keine Zellcounts; diese Bedingung wird hier "
                 "nicht unabhängig neu aus Rohdaten bewiesen. Keine Kategorienzusammenlegung und kein Itemausschluss nach Ergebnissen.", "",
                 "Die erste v2-Ausführung berechnet keine Standardfehler. Unsicherheit bleibt ausdrücklich nicht berechnet: "
                 "keine Konfidenzintervalle und keine persönliche Messunsicherheit; fehlender SE bedeutet niemals SE=0. "
                 "Gewichtung behebt Auswahl-, Nonresponse-, Kontext- und Modusverzerrungen nicht automatisch. "
                 "Prozentdarstellungen sind gerundet; Kategorienanteile summieren sich vor Darstellung innerhalb 1e-12 auf eins.", "",
                 "Historische v1-A/B-Antworten des Neunermoduls waren bekannt. Die sechs zusätzlichen ESS11-Felder stammen "
                 "aus derselben Erhebung und sind deskriptive Sekundärangaben, keine unangetastete Bestätigung. "
                 "Die tatsächlichen v2-Aggregate sind diesem Berichtsautor nun bekannt. Die beiden frischen Ergebnisrollen "
                 "arbeiteten getrennt, aber in derselben Codex-Modellfamilie; gemeinsame Fehler bleiben möglich und "
                 "Agentenübereinstimmung ist kein Neutralitätsbeweis. Ihre Kontrolle war eine Aggregatreproduktion, "
                 "keine unabhängige Rohdaten-/Downloadreproduktion oder erneute Berechnung individueller Ratioextrema.", "",
                 "Root dokumentiert die tatsächliche vorgelagerte Prüfung der öffentlichen und privaten Pins und hat die "
                 "Fragefreigaben gebunden. Dieser Build prüft veröffentlichte Quellen-, Vertrags-, Export-, Entscheidungs- "
                 "und Berichtbytes; er liest keine privaten Kandidaten oder Rohdaten. Formale Statusstrings und Hashsyntax "
                 "sind allein kein Wissenschaftsnachweis. Menschliche Verständlichkeit, Fairness, Gestaltung, Claudes "
                 "Schlusskontrolle, Rechte-/kommerzielle Nutzung und persönlicher Release bleiben offen.", "",
                 "## Verbindliche Kriterien und Belege", "",
                 "[Empirieplan v2](../../docs/empirie-plan-v2.entwurf.md#deskriptive-auswertung) und "
                 "[Analysevertrag](../../data/analysevertrag.v2.entwurf.json) binden Primärgewicht, Kategorien, "
                 "Nenner, Serialisierung, Missing, Sensitivitäten und feste Darstellungsfolgen. "
                 "[Messformen](../../docs/messformen-v2.entwurf.md#begrenzte-einzelangaben-als-ausführbarer-weg) "
                 "trennen Einzelangaben von formativen und reflektiven Formen. "
                 "[Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) verlangt Binnenabdeckung, "
                 "gleiche Belegmaßstäbe und offengelegte Auslassungen; Rubriken sind keine Faktoren.", "",
                 "B-V2-M01: [Bollen/Lennox 1991, DOI 10.1037/0033-2909.110.2.305](https://doi.org/10.1037/0033-2909.110.2.305), "
                 "im Methodenentwurf nur Abstract geprüft. B-V2-M02: [OECD/JRC 2008, gedruckte S.15–16/31–35, "
                 "PDF17–18/33–37](https://www.oecd.org/content/dam/oecd/en/publications/reports/2008/08/handbook-on-constructing-composite-indicators-methodology-and-user-guide_g1gh9301/9789264043466-en.pdf): transparente Auswahl/"
                 "Aggregation; Übertragung auf Personenprofile ist begrenzte methodische Ableitung. B-V2-M03: "
                 "[Krosnick 1999, gedruckte S.37/40](https://web.stanford.edu/dept/communication/faculty/krosnick/docs/1999/1999%20Maximizing%20questionnaire%20quality.pdf): "
                 "Antwortformat und Durchführung können Antworten beeinflussen. Keine Gleichwertigkeit einer neuen Website daraus ableiten.", "",
                 "[Kriesi et al. 2006, DOI 10.1111/j.1475-6765.2006.00644.x](https://doi.org/10.1111/j.1475-6765.2006.00644.x) "
                 "begründet im Themenentwurf eine Suchgliederung, keine heutige deutsche Personenstruktur. "
                 "[ESS6-Demokratieantrag, PDF8–16](https://www.europeansocialsurvey.org/sites/default/files/2023-06/ESS6_democracy_proposal.pdf) "
                 "trennt Prinzipien und Umsetzung. [Walgrave et al. 2009, S.1161–1163/1166–1168](https://medialibrary.uantwerpen.be/oldcontent/container2608/files/Walgrave%20et%20al%202009%20-%20voting%20aid%20applications.pdf) "
                 "begründet Auswahlfolgenprüfungen; belgische VAA-Befunde sind kein deutscher Fairnessnachweis. "
                 "Diese Literaturfundstellen stammen aus den gebundenen öffentlichen Methodenakten; keine neue Literaturprüfung in diesem Build.", "",
                 "Begrenzte Ergebnisentscheidungen: [Methoden](../loop/reviews/RESULTS-V2-001-methods-first.md), "
                 "[Quellen/Konstrukte/Fairness](../loop/reviews/RESULTS-V2-001-sources-first.md) und "
                 "[Root-Exportentscheidung](../loop/policy-v2-export-decisions.json). "
                 "Deren offene Darstellungsbedingungen werden hier bearbeitet, nicht eigenständig für abgenommen erklärt.", "",
                 "## Getrennte Studien und historische Referenzpopulationen", ""]
        for identity in _VARIABLES:
            study = study_map[identity]
            provenance = study["provenance"]
            lines += ["### " + _md(identity) + " — Ausgabe " + _md(study["edition"]), "",
                      "European Social Survey European Research Infrastructure (ESS ERIC); Sikt – Norwegian Agency for "
                      "Shared Services in Education and Research. [Daten-DOI](" + provenance["dataDoiUrl"] + ") "
                      + _md(provenance["dataDoi"]) + "; [Dokumentations-DOI](" + provenance["documentationDoiUrl"] + ") "
                      + _md(provenance["documentationDoi"]) + ". Deutschland (DE), ESS-Runde " + str(study["round"]) + ".", "",
                      "Deklarierte Zielpopulation: " + _md(provenance["populationDeclaredEn"]) + ". "
                      "Die gemeinsame ESS-Zielbeschreibung betrifft Personen ab 15 in Privathaushalten unabhängig von "
                      "Staatsangehörigkeit, Sprache oder Rechtsstatus; sie ist keine vollständige realisierte Abdeckung. "
                      + _md(provenance["populationCoverageLimit"]), ""]
            for period in provenance["fieldwork"]:
                lines += ["Historische Feldzeit: " + _md(period["start"]) + " bis " + _md(period["end"]) + "; "
                          "deklarierter Modus: " + _md("; ".join(period["modesDeclaredEn"])) + ".", ""]
            if identity == "ESS8e02_3":
                lines += ["**ESS8-München-Grenze:** München nahm an der Stichprobenziehung nicht teil; dort wurden keine "
                          "Befragten gewonnen. Diese Referenz ist keine vollständig räumlich abdeckende Deutschlandnorm.", ""]
            for note in provenance["versionNotes"]:
                lines += ["Versionsgrenze: " + _md(note), ""]
            lines += ["Datenlizenz: " + _md(provenance["dataLicenseId"]) + "; Dokumentationslizenz: "
                      + _md(provenance["documentationLicenseId"]) + ". "
                      "Primärgewicht pspwght; Sensitivitäten und Frage-Nenner werden je Einzelangabe geführt. "
                      "Keine Übertragung auf heutige Websitebesucher.", ""]
        group = catalogue["groups"][0]
        lines += ["## Originalblock und neue Zusammenstellung", "",
                  "ESS10 B1–B12 fragt nach Demokratie im Allgemeinen. Originalreihenfolge: "
                  + ", ".join("`" + qid + "`" for qid in group["itemIds"]) + ". "
                  "B12/keydec gehört im Originalblock an die letzte Stelle und erhält unten die primäre EU-Rubrik. "
                  "Die Themenordnung dieses Berichts ist keine neue Administration des Blocks.", "",
                  "**Originaleinleitung B1–B12:** " + _md(group["introductionDe"]), "",
                  "**Originalantwortstamm:** " + _md(group["responseStemDe"]), "",
                  "B13–B24 (wahrgenommene Umsetzung) werden ausgelassen. B25 ist die gesonderte historische Frage "
                  "zum Mehrheitskonflikt; ihre Originalweiterleitungen B26–B29 sind ausgelassen. B30 ist ebenfalls "
                  "nicht Bestandteil dieser festen Auswahl. Die neue Website-Zusammenstellung verändert Fragebogenkontext "
                  "und Publikum; die operative CAWI-Folge ist nicht belegt und neue Webadministration ist unvalidiert.", ""]
        for key, title, variables, meaning, gaps in THEMES:
            lines += ["## " + title, "", meaning, "", "**Inhaltslücken:** " + gaps + " "
                      "Bezug: [Themenmatrix](../../docs/abdeckung-v2.md#abdeckungsmatrix) und "
                      "[feste Auswahl](../../docs/empirie-plan-v2.entwurf.md#konkrete-auswahl-vor-abhängigen-analysen).", ""]
            for variable in variables:
                item = next(i for i in items.values() if i["variable"] == variable)
                lines += _question(item, question_map[item["id"]], sources, study_map[item["studyId"]])
        lines += ["## Quellen- und Nachnutzungsregister", "",
                  "Originalwortlaute, Instruktionen und Kategorien sind Transkriptionen aus den benannten deutschen "
                  "ESS-Instrumenten. Layoutumbrüche und Trennungen am Zeilenende werden nach der Katalogregel normalisiert; "
                  "Einleitungen, Ellipsen, Stämme, Szenarien und nationale Anpassungen bleiben erhalten. "
                  "Die hier dargestellte Zusammenstellung, Methodenprosa, Rubriken und Tabellen sind Projektbearbeitungen, "
                  "keine unveränderte Neuauflage eines ESS-Fragebogens. Dokumentation: "
                  "[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en); Datenableitungen: "
                  "[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.en). "
                  "ESS ERIC/Sikt sind Quellengeber, keine Billigung dieses Projekts. "
                  "[Lizenzakte](../../docs/lizenzen.md) und [Datenattribution](../../data/reference-v2/README.md) bleiben maßgeblich; "
                  "keine pauschale Rechts- oder kommerzielle Nutzungsfreigabe.", "",
                  "Gebundener Katalog: `" + analysis_contract["catalog"]["path"] + "`, SHA256 `"
                  + analysis_contract["catalog"]["sha256"] + "`. "
                  "Abrufzeit und HTTP-Status unten stammen aus früheren Quellenbindungen; dieser Build führt keinen Netzwerkabruf durch.", ""]
        for sid in sorted(sources):
            source = sources[sid]
            lines += [_link(source) + ": " + _md(source["kind"]) + "; früherer Abruf UTC "
                      + _md(source["retrievedUtc"]) + "; HTTP " + str(source["httpStatus"]) + "; SHA256 `"
                      + source["originalBytesSha256"] + "`; Lizenzkennung "
                      + _md(source["licenseId"] or "keine eigene Kennung gebunden") + ".", ""]
        lines += ["## Reproduktion und offene Voraussetzungen", "",
                  "Der lokale Build `PYTHONDONTWRITEBYTECODE=1 python scripts/build-policy-v2-report.py` bindet "
                  "ausschließlich die fest gepinnten veröffentlichten Exporte, Katalog-/Quellen-/Methodenbytes und "
                  "RESULTS-V2-001-Berichte/Entscheidungen. `--check` prüft Bytegleichheit des erzeugten Artefakts. "
                  "Der unveränderte technische Renderer prüft die geschlossene öffentliche Exportform. "
                  "Das ist reproduzierbare Darstellung veröffentlichter Aggregate, keine neue unabhängige Rohreproduktion.", "",
                  "Marktordnung, Außen-/Verteidigungs-/Friedenspolitik und die oben genannten Binnenfacetten bleiben "
                  "Quellen-/Produktlücken. GLES und ISSP bleiben mögliche getrennte Ergänzungswege mit eigenen Rechten, "
                  "Populationen und Versionen; hier entsteht keine neue Referenz dafür. "
                  "Der Themenbericht bleibt bis zur gezielten unabhängigen Präsentationsprüfung WIP. "
                  "Hauptproduktbreite, menschlicher Verständnistest, endgültige Gestaltung, Claude-Schlusskontrolle "
                  "und persönlicher Release sind weiterhin offen.", ""]
        return "\n".join(lines)
    except (PolicyThematicReportError, PolicyReportError):
        raise
    except Exception:
        raise PolicyThematicReportError(ThematicErrorCode.INVALID_INPUT) from None
