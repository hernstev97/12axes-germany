"""Pure WIP report renderer for five separately gated public study exports.

No IO, CLI, authentication or scientific/release certification. Root verifies
actual source/catalog/review/manifest bytes before this API. The public export
does not expose cell counts, weight vectors or the private candidate; this API
cannot independently recover or certify those upstream facts.
"""

from enum import Enum
from html import escape
from math import fsum, isclose, isfinite
import re
from urllib.parse import urlsplit

from pipeline.policy_export_v2 import (
    PolicyExportError, _canonical_hash, _contract, _json_values,
    ExportErrorCode,
)


_VARIABLES = {
    "ESS5e03_6": ("bplcdc", "dpcstrb", "hrshsnta", "dbctvrd", "lwstrob", "rgbrklw"),
    "ESS8e02_3": ("gvslvol", "gvslvue", "gvcldcr", "bnlwinc", "eduunmp", "inctxff", "sbsrnen", "banhhap", "imsclbn", "wrkprbf"),
    "ESS9e03_3": ("sofrdst", "sofrwrk", "sofrpr", "sofrprv"),
    "ESS10SCe03_2": ("fairelc", "dfprtal", "medcrgv", "rghmgpr", "votedir", "cttresa", "gptpelc", "gvctzpv", "grdfinc", "viepol", "wpestop", "scchpldm", "vteurmmb", "keydec", "imsmetn", "imdfetn", "impcntr"),
    "ESS11e04_2": ("gincdif", "euftf", "eqparep", "eqparlv", "freinsw", "fineqpy"),
}
_NULL_STATUSES = {"no_valid_answers", "withheld_base_or_cell_count", "result_review_withheld"}
_AVAILABLE = "reviewed_historical_reference"
_TOLERANCE = 1e-12


class ReportErrorCode(str, Enum):
    INVALID_INPUT = "invalid_input"
    INVALID_CONTRACT = "invalid_contract"
    INVALID_EXPORT = "invalid_export"
    SOURCE_BINDING = "source_binding"


class PolicyReportError(ValueError):
    def __init__(self, code: ReportErrorCode):
        self.code = code
        super().__init__(f"policy_report_error: {code.value}")


def _require(condition, code=ReportErrorCode.INVALID_EXPORT):
    if not condition:
        raise PolicyReportError(code) from None


def _object(value, keys, code=ReportErrorCode.INVALID_EXPORT):
    _require(type(value) is dict and set(value) == set(keys)
             and all(type(key) is str for key in value), code)
    return value


def _list(value, code=ReportErrorCode.INVALID_EXPORT):
    _require(type(value) is list, code)
    return value


def _count(value):
    _require(type(value) is int and value >= 0)
    return value


def _number(value, maximum=None):
    _require(type(value) in (int, float))
    converted = float(value)
    _require(isfinite(converted) and converted >= 0 and (maximum is None or converted <= maximum))
    return converted


def _hash(value):
    _require(type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None)


def _doi_link(value, doi):
    code = ReportErrorCode.INVALID_CONTRACT
    _require(type(value) is str and type(doi) is str, code)
    parsed = urlsplit(value)
    _require(parsed.scheme == "https" and parsed.netloc == "doi.org"
             and not parsed.query and not parsed.fragment and value == "https://doi.org/" + doi
             and re.fullmatch(r"10\.[0-9]+/[A-Za-z0-9._/-]+", doi) is not None, code)
    return value


def _reference(reference, definition):
    _object(reference, {"weight", "validCount", "totalCount", "missingCount", "notAskedCount",
                        "categories", "missingReasons", "missingWeight", "allDEWeight", "sensitivity",
                        "anweightEquivalenceDiagnostic", "uncertainty"})
    _require(reference["weight"] == "pspwght" and reference["uncertainty"] is None)
    valid, total, missing, not_asked = [_count(reference[key]) for key in
                                       ("validCount", "totalCount", "missingCount", "notAskedCount")]
    _require(valid >= 100 and valid + missing + not_asked == total)
    missing_weight, all_weight = _number(reference["missingWeight"]), _number(reference["allDEWeight"])
    # A tiny positive valid contribution can disappear in a large float total.
    # This public shape omits validWeight, so equality cannot refute it.
    _require(all_weight > 0 and missing_weight <= all_weight and ((missing == 0) == (missing_weight == 0)))
    _require(bool(definition["structurallyNotAskedCodes"]) or not_asked == 0)
    categories = _list(reference["categories"])
    _require(len(categories) == len(definition["categoryCodes"]))
    proportions = []
    for category, expected in zip(categories, definition["categoryCodes"], strict=True):
        _object(category, {"code", "proportion"})
        _require(type(category["code"]) is str and category["code"] == expected)
        proportions.append(_number(category["proportion"], 1))
    _require(abs(fsum(proportions) - 1) <= _TOLERANCE)
    reasons = _list(reference["missingReasons"])
    seen, counts, weights = set(), [], []
    for reason in reasons:
        _object(reason, {"reason", "count", "primaryWeightSum"})
        name = reason["reason"]
        _require(type(name) is str and name not in seen)
        seen.add(name)
        count, weight = _count(reason["count"]), _number(reason["primaryWeightSum"])
        _require((count == 0) == (weight == 0))
        counts.append(count)
        weights.append(weight)
    _require(seen == set(definition["missingCodes"].values()) and sum(counts) == missing
             and isclose(fsum(weights), missing_weight, rel_tol=_TOLERANCE, abs_tol=0))
    sensitivity = _object(reference["sensitivity"], {"maxAbsUnweighted", "maxAbsDweight"})
    for value in sensitivity.values():
        _number(value, 1)
    diagnostic = _object(reference["anweightEquivalenceDiagnostic"],
                         {"maxAbsDifference", "ratioScope", "ratioMin", "ratioMax"})
    _number(diagnostic["maxAbsDifference"], 1)
    minimum, maximum = _number(diagnostic["ratioMin"]), _number(diagnostic["ratioMax"])
    _require(diagnostic["ratioScope"] == "all_de_cases" and 0 < minimum <= maximum)


def _export(export, contract):
    _object(export, {"schemaVersion", "status", "studyId", "edition", "sourceContractSha256",
                     "candidateSha256", "reviewManifestSha256", "questions"})
    _require(type(export["schemaVersion"]) is int and export["schemaVersion"] == 2
             and export["status"] == "reviewed_historical_descriptive_reference")
    _require(export["studyId"] == contract["study_id"] and export["edition"] == contract["edition"],
             ReportErrorCode.SOURCE_BINDING)
    for key in ("sourceContractSha256", "candidateSha256", "reviewManifestSha256"):
        _hash(export[key])
    _require(export["sourceContractSha256"] == _canonical_hash(contract), ReportErrorCode.SOURCE_BINDING)
    definitions = contract["adapter"]["questions"]
    questions = _list(export["questions"])
    _require(len(questions) == len(definitions))
    totals, ratios = [], []
    for question, definition in zip(questions, definitions, strict=True):
        _object(question, {"id", "status", "reference"})
        _require(type(question["id"]) is str and question["id"] == definition["question_id"])
        status = question["status"]
        _require(type(status) is str and status in _NULL_STATUSES | {_AVAILABLE})
        if status == _AVAILABLE:
            _reference(question["reference"], definition)
            reference = question["reference"]
            totals.append((reference["totalCount"], reference["allDEWeight"]))
            diag = reference["anweightEquivalenceDiagnostic"]
            ratios.append((diag["ratioMin"], diag["ratioMax"]))
        else:
            _require(question["reference"] is None)
    _require(all(count == totals[0][0] and isclose(weight, totals[0][1], rel_tol=_TOLERANCE, abs_tol=0)
                 for count, weight in totals))
    _require(all(pair == ratios[0] for pair in ratios))


def _inputs(exports, contracts):
    _require(type(exports) is list and type(contracts) is list and len(exports) == len(contracts) == 5,
             ReportErrorCode.INVALID_INPUT)
    source_map, export_map = {}, {}
    for contract in contracts:
        _json_values(contract, ExportErrorCode.INVALID_CONTRACT)
        definitions = _contract(contract)
        identity = contract["study_id"]
        _require(identity not in source_map and identity in _VARIABLES, ReportErrorCode.INVALID_CONTRACT)
        _require([q["question_id"] for q in definitions] == [f"{identity}:{var}" for var in _VARIABLES[identity]],
                 ReportErrorCode.INVALID_CONTRACT)
        provenance = contract["provenance"]
        for prefix in ("data", "documentation"):
            _doi_link(provenance[prefix + "DoiUrl"], provenance[prefix + "Doi"])
        if identity == "ESS8e02_3":
            _require(any("Munich" in text or "München" in text
                         for text in provenance["samplingProceduresDeclaredEn"]), ReportErrorCode.INVALID_CONTRACT)
        source_map[identity] = contract
    _require(set(source_map) == set(_VARIABLES), ReportErrorCode.INVALID_CONTRACT)
    for export in exports:
        _json_values(export, ExportErrorCode.INVALID_CANDIDATE)
        _require(type(export) is dict and type(export.get("studyId")) is str)
        identity = export["studyId"]
        _require(identity not in export_map and identity in source_map)
        _export(export, source_map[identity])
        export_map[identity] = export
    _require(set(export_map) == set(source_map))
    return source_map, export_map


def _md(value):
    # Metadata is text, never caller-provided HTML/Markdown. Keep source words.
    text = escape(str(value), quote=True).replace("\r", " ").replace("\n", " ")
    return re.sub(r"([\\`*_{}\[\]()|#+.!-])", r"\\\1", text)


def _decimal(value):
    return format(value, ".12g").replace(".", ",")


def _percentage(value):
    return format(value * 100, ".6f").replace(".", ",")


def _source_id(value):
    # Only the fixed, schema-checked study/question IDs reach this helper.
    return "`" + value + "`"


def render_historical_report(study_exports, study_contracts) -> str:
    """Render deterministic Markdown after visible closed-schema checks.

    Two built-in lists, each containing five studies, and 43 fixed source IDs.
    No actual pin/authentication proof: only Root can supply previously checked
    public exports. Null references never receive counts or inferred fractions.
    Cell-five and private weight arithmetic are not recoverable from this shape.
    """
    try:
        sources, exports = _inputs(study_exports, study_contracts)
        lines = [
            "# Historische deskriptive Einzelreferenzen",
            "",
            "Dieser Bericht stellt 43 getrennte Fragen aus fünf gebundenen Studien für Deutschland dar. "
            "Die Angaben beziehen sich auf die jeweiligen historischen Erhebungen. Personen werden nicht über Studien verbunden; "
            "es entstehen kein Gesamtscore und kein gemeinsames Faktorenmodell.",
            "",
            "Die früheren v1-A/B-Antworten des Neun-Item-Moduls sind bekannt. Die sechs zusätzlich ausgewählten ESS11-Felder "
            "stammen aus derselben Studie und dienen als deskriptive Sekundärangaben; sie sind keine unberührte Bestätigung "
            "eines früheren Modells. Dieser Bericht wertet v1-A/B nicht neu aus.",
            "",
            "Primär werden pspwght-gewichtete Originalkategorienanteile unter den gültigen Antworten der jeweiligen Frage dargestellt. "
            "Fehlende und nichtgestellte Angaben gehören nicht zum gültigen Nenner. Fehlende Gründe bleiben getrennt; "
            "export_blank_unclassified bezeichnet eine leere Exportzelle ohne weiter belegte Bedeutung. "
            "Es gibt keine Einsetzung eines Mittelwerts und keine Polung oder Ordinalpunkte.",
            "",
            "Ungewichtete Anteile und dweight dienen getrennten Sensitivitätsangaben. Angegeben wird jeweils die maximale "
            "absolute Anteilsdifferenz zur Primärgewichtung auf dem Anteilsmaßstab von 0 bis 1. Anweight wird als diagnostischer Vergleich geführt; "
            "Ratiominimum und -maximum beziehen sich auf anweight/pspwght unter allen deutschen Fällen, einschließlich fehlender "
            "und nichtgestellter Antworten. Daraus folgt keine quellenübergreifende Äquivalenzentscheidung.",
            "",
            "Es werden keine Standardfehler oder Unsicherheitsintervalle berechnet. Die vorgelagerte Anzeigeheuristik verlangt "
            "mindestens 100 gültige Fälle und mindestens fünf Fälle je positiv besetzter Originalkategorie; Nullkategorien bleiben erhalten. "
            "Diese Projektgrenzen garantieren weder Präzision noch Anonymität. Der öffentliche Export enthält keine Kategoriencounts "
            "oder Sensitivitätsvektoren: Der Renderer kann deren vorgelagerte Prüfungen nicht wiederholen. "
            "Anteilswerte werden als Prozent auf sechs Nachkommastellen, sonstige Dezimalwerte auf zwölf signifikante Stellen gerundet.",
            "",
            "Root muss tatsächliche Quellen-, Katalog-, Review- und Manifestbytes vor dem Aufruf prüfen. Die Funktion prüft nur die "
            "sichtbare Exportstruktur, Arithmetik und Vertragshashbindung; sie bescheinigt keine Revieweridentität, Rechte, "
            "Ergebnisprüfung oder Veröffentlichung. Die historischen Angaben begründen keinen aktuellen Bevölkerungsvergleich für Webnutzer. "
            "Antwortverständnis und neue Webadministration bleiben gesonderte Aufgaben.",
        ]
        for identity in _VARIABLES:
            source, export = sources[identity], exports[identity]
            provenance = source["provenance"]
            lines += ["", f"## {_source_id(identity)} — Edition {_md(source['edition'])}", "",
                      f"Runde {_md(source['round'])}; Land DE. Quellen- und Modusangaben stammen aus dem gebundenen Studienvertrag.", ""]
            for fieldwork in provenance["fieldwork"]:
                lines.append(f"Erhebung: {_md(fieldwork['start'])} bis {_md(fieldwork['end'])}; deklarierte Modi: "
                             + "; ".join(_md(mode) for mode in fieldwork["modesDeclaredEn"]) + ".")
            lines += ["", "Deklarierte Zielpopulation (Originalangabe): " + _md(provenance["populationDeclaredEn"]),
                      "", "Abdeckungsgrenze (Vertragsangabe): " + _md(provenance["populationCoverageLimit"]),
                      "", "Datenlizenzkennung: " + _md(provenance["dataLicenseId"]) + "; Dokumentationslizenzkennung: "
                      + _md(provenance["documentationLicenseId"]) + ". Quellenrechte und Nutzungsumfang benötigen eine getrennte Prüfung."]
            for note in provenance["versionNotes"]:
                lines += ["", "Versionshinweis (Vertragsangabe): " + _md(note)]
            lines += ["", f"Datenquelle: [{_md(provenance['dataDoi'])}]({provenance['dataDoiUrl']}); "
                      f"Dokumentation: [{_md(provenance['documentationDoi'])}]({provenance['documentationDoiUrl']}).",
                      "", "Weitere Quellenkennungen: " + "; ".join(_md(ref) for ref in provenance["sourceRefs"]),
                      "", "Vertragshash: " + export["sourceContractSha256"] + "; Kandidatenhash: " + export["candidateSha256"]
                      + "; Reviewmanifesthash: " + export["reviewManifestSha256"] + ".",
                      "", "| Quellenfrage | Exportstatus | Gültig | Gesamt | Fehlend | Nicht gestellt | Fehlendes Gewicht | Gewicht aller DE-Fälle | Δ ungewichtet | Δ dweight | Δ anweight | Ratio min | Ratio max |",
                      "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
            for question in export["questions"]:
                reference = question["reference"]
                if reference is None:
                    lines.append(f"| {_source_id(question['id'])} | weiterhin nicht freigegeben: {_md(question['status'])} | — | — | — | — | — | — | — | — | — | — | — |")
                else:
                    sensitivity, diag = reference["sensitivity"], reference["anweightEquivalenceDiagnostic"]
                    values = [reference[key] for key in ("validCount", "totalCount", "missingCount", "notAskedCount")]
                    cells = [_md(str(n)) for n in values] + [_decimal(reference["missingWeight"]), _decimal(reference["allDEWeight"]),
                        _decimal(sensitivity["maxAbsUnweighted"]), _decimal(sensitivity["maxAbsDweight"]),
                        _decimal(diag["maxAbsDifference"]), _decimal(diag["ratioMin"]), _decimal(diag["ratioMax"])]
                    lines.append(f"| {_source_id(question['id'])} | Referenz im Export freigegeben | " + " | ".join(cells) + " |")
        lines += ["", "## Originalkategorien und getrennte fehlende Gründe", "",
                  "Die Reihenfolge entspricht dem Quellenvertrag. Gesperrte Fragen erhalten hier keine Zahlen und keinen abgeleiteten Anteilsvektor."]
        for identity in _VARIABLES:
            for question in exports[identity]["questions"]:
                lines += ["", "### " + _source_id(question["id"]), ""]
                reference = question["reference"]
                if reference is None:
                    lines.append("Weiterhin nicht freigegeben: " + _md(question["status"]) + ". Keine Zahlenreferenz.")
                    definition = next(q for q in sources[identity]["adapter"]["questions"] if q["question_id"] == question["id"])
                    lines += ["", "Originalcodes aus dem Quellenvertrag (keine Anteile): "
                              + "; ".join(_md(code) for code in definition["categoryCodes"]) + "."]
                    continue
                lines += ["| Originalcode | Gewichteter Anteil (%) |", "| --- | --- |"]
                for category in reference["categories"]:
                    lines.append(f"| {_md(category['code'])} | {_percentage(category['proportion'])} |")
                lines += ["", "| Fehlender Grund | Anzahl | Primäre Gewichtssumme |", "| --- | --- | --- |"]
                reasons_by_name = {r["reason"]: r for r in reference["missingReasons"]}
                definition = next(q for q in sources[identity]["adapter"]["questions"] if q["question_id"] == question["id"])
                for name in sorted(set(definition["missingCodes"].values())):
                    reason = reasons_by_name[name]
                    lines.append(f"| {_md(name)} | {reason['count']} | {_decimal(reason['primaryWeightSum'])} |")
        lines += ["", "## Quellenseitige Stichprobendesigns", "",
                  "Die folgenden Originalangaben stammen aus der Vertragsprovenienz. Sie werden hier nicht als nachgewiesene vollständige Designbasis behandelt."]
        for identity in _VARIABLES:
            lines += ["", "### " + _source_id(identity), ""]
            for statement in sources[identity]["provenance"]["samplingProceduresDeclaredEn"]:
                lines.append(_md(statement))
            if identity == "ESS8e02_3":
                lines += ["", "Der ESS8-Abdeckungshinweis zu München ist der vorstehenden Originalangabe zu entnehmen; er wird durch Gewichtung nicht als erledigt behandelt."]
        return "\n".join(lines) + "\n"
    except PolicyReportError:
        raise
    except PolicyExportError:
        raise PolicyReportError(ReportErrorCode.INVALID_INPUT) from None
    except (ValueError, TypeError, AttributeError, KeyError, ArithmeticError, RecursionError):
        raise PolicyReportError(ReportErrorCode.INVALID_INPUT) from None
