"""WIP in-memory export protocol guard; no IO or scientific approval.

Root must verify the immutable source/catalog manifest and both report byte pins
before calling this builder. A privileged caller can forge a formally valid
decision; this module cannot authenticate reviewers, provenance or intentions.
Count thresholds are project display heuristics, not anonymity guarantees.
"""

from enum import Enum
from hashlib import sha256
import json
from math import fsum, isclose, isfinite
import re

from pipeline.policy_analysis_v2 import PolicyAnalysisError, _validate_reference
from pipeline.policy_reference_v2 import (
    Accounting, CategoricalReference, CategoryEstimate, VarianceStatus,
)


TOLERANCE = 1e-12
_STUDIES = {
    "ESS5e03_6": ("3.6", 5), "ESS8e02_3": ("2.3", 8),
    "ESS9e03_3": ("3.3", 9), "ESS10SCe03_2": ("3.2", 10),
    "ESS11e04_2": ("4.2", 11),
}
_PREFIXES = ("total", "eligible", "valid", "missing", "not_asked")
_ACCOUNTING_KEYS = {f"{p}_{kind}" for p in _PREFIXES for kind in ("count", "weight")}
_ROLES = {"pspwght": "primary", "dweight": "sensitivity",
          "unweighted": "sensitivity", "anweight": "equivalence_diagnostic"}
_PREPARED = "prepared_pending_result_review"
_WITHHELD = "withheld_base_or_cell_count"
_NO_VALID = "no_valid_answers"


class ExportErrorCode(str, Enum):
    INVALID_CONTRACT = "invalid_contract"
    INVALID_CANDIDATE = "invalid_candidate"
    INVALID_DECISION = "invalid_decision"
    HASH_MISMATCH = "hash_mismatch"


class PolicyExportError(ValueError):
    def __init__(self, code: ExportErrorCode):
        self.code = code
        super().__init__(f"policy_export_error: {code.value}")


def _require(condition: bool, code: ExportErrorCode) -> None:
    if not condition:
        raise PolicyExportError(code) from None


def _object(value, keys, code):
    _require(type(value) is dict and all(type(k) is str for k in value)
             and set(value) == set(keys), code)
    return value


def _array(value, code):
    _require(type(value) is list, code)
    return value


def _text(value, code, *, empty=False):
    _require(type(value) is str and (empty or bool(value))
             and (empty or value.strip() == value), code)
    return value


def _strings(value, code, *, empty=False, unique=False):
    values = _array(value, code)
    for item in values:
        _text(item, code, empty=empty)
    _require(not unique or len(values) == len(set(values)), code)
    return values


def _count(value, code):
    _require(type(value) is int and value >= 0, code)
    return value


def _number(value, code):
    _require(type(value) in (int, float), code)
    result = float(value)
    _require(isfinite(result) and result >= 0, code)
    return result


def _hash(value, code):
    _require(type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None, code)


def _close(first, second):
    return isclose(first, second, rel_tol=TOLERANCE, abs_tol=0.0)


def _canonical_hash(value):
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def _json_values(value, code, ancestors=None):
    """Reject custom objects and cyclic containers before schema operations."""
    ancestors = set() if ancestors is None else ancestors
    if type(value) in (dict, list):
        identity = id(value)
        _require(identity not in ancestors, code)
        ancestors.add(identity)
        if type(value) is dict:
            _require(all(type(key) is str for key in value), code)
            children = value.values()
        else:
            children = value
        for child in children:
            _json_values(child, code, ancestors)
        ancestors.remove(identity)
    else:
        _require(value is None or type(value) in (str, bool, int, float), code)
        if type(value) is float:
            _require(isfinite(value), code)


def _contract(study):
    code = ExportErrorCode.INVALID_CONTRACT
    _object(study, {"study_id", "edition", "round", "country", "input", "adapter",
                    "metadata", "responseSerialization", "provenance"}, code)
    identity = _text(study["study_id"], code)
    _require(identity in _STUDIES, code)
    edition, round_number = _STUDIES[identity]
    _require(type(study["edition"]) is str and study["edition"] == edition
             and type(study["round"]) is int and study["round"] == round_number
             and study["country"] == "DE", code)
    input_meta = _object(study["input"], {"path", "sha256", "bytes", "editionEvidence"}, code)
    _text(input_meta["path"], code)
    _hash(input_meta["sha256"], code)
    _require(_count(input_meta["bytes"], code) > 0, code)
    _text(input_meta["editionEvidence"], code)
    metadata = _object(study["metadata"], {"round_column", "edition_column", "expected_round",
                                          "expected_edition", "normalizationRule"}, code)
    _require(metadata == {"round_column": "essround", "edition_column": "edition",
                          "expected_round": str(round_number), "expected_edition": edition,
                          "normalizationRule": "integer_round_optional_dot_zero_decimal_edition_v1"}, code)
    serialization = _object(study["responseSerialization"], {"rule", "emptyCellReason"}, code)
    _require(serialization == {"rule": "canonical_nonnegative_integer_optional_zero_fraction_v1",
                              "emptyCellReason": "export_blank_unclassified"}, code)
    provenance = _object(study["provenance"], {
        "dataDoi", "dataDoiUrl", "documentationDoi", "documentationDoiUrl",
        "populationDeclaredEn", "populationCoverageLimit", "fieldwork",
        "samplingProceduresDeclaredEn", "dataLicenseId", "documentationLicenseId",
        "versionNotes", "sourceRefs"}, code)
    for key in set(provenance) - {"fieldwork", "sourceRefs", "samplingProceduresDeclaredEn", "versionNotes"}:
        _text(provenance[key], code)
    sampling = _array(provenance["samplingProceduresDeclaredEn"], code)
    _require(bool(sampling), code)
    for statement in sampling:
        # Source prose is copied as metadata, never normalized for identity.
        _require(type(statement) is str and bool(statement.strip()), code)
    _strings(provenance["versionNotes"], code)
    _require(bool(_strings(provenance["sourceRefs"], code, unique=True)), code)
    _require(bool(_array(provenance["fieldwork"], code)), code)
    for fieldwork in provenance["fieldwork"]:
        _object(fieldwork, {"start", "end", "modesDeclaredEn"}, code)
        _text(fieldwork["start"], code)
        _text(fieldwork["end"], code)
        _require(bool(_strings(fieldwork["modesDeclaredEn"], code, unique=True)), code)
    adapter = _object(study["adapter"], {"study_id", "edition", "country", "country_column",
                                        "id_column", "weight_columns", "questions", "design_columns"}, code)
    _require(adapter["study_id"] == identity and adapter["edition"] == edition
             and adapter["country"] == "DE" and adapter["country_column"] == "cntry"
             and adapter["id_column"] == "idno", code)
    weights = _object(adapter["weight_columns"], {"primary", "sensitivities"}, code)
    _require(weights["primary"] == "pspwght" and _strings(weights["sensitivities"], code)
             == ["dweight", "anweight"], code)
    if adapter["design_columns"] is not None:
        design = _object(adapter["design_columns"], {"psu", "stratum"}, code)
        _require(_text(design["psu"], code) != _text(design["stratum"], code), code)
    questions = _array(adapter["questions"], code)
    _require(bool(questions), code)
    ids, variables = set(), set()
    for question in questions:
        _object(question, {"question_id", "variable", "categoryCodes", "missingCodes",
                           "structurallyNotAskedCodes"}, code)
        variable = _text(question["variable"], code)
        qid = _text(question["question_id"], code)
        _require(qid == f"{identity}:{variable}" and qid not in ids and variable not in variables, code)
        ids.add(qid)
        variables.add(variable)
        categories = _strings(question["categoryCodes"], code, unique=True)
        _require(bool(categories), code)
        missing = question["missingCodes"]
        _require(type(missing) is dict and all(type(k) is str for k in missing), code)
        for reason in missing.values():
            _text(reason, code)
        _require(missing.get("") == "export_blank_unclassified", code)
        not_asked = _strings(question["structurallyNotAskedCodes"], code, empty=True, unique=True)
        _require(not(set(categories) & set(missing)) and not(set(categories) & set(not_asked))
                 and not(set(missing) & set(not_asked)), code)
    return questions


def _accounting(value):
    code = ExportErrorCode.INVALID_CANDIDATE
    _object(value, _ACCOUNTING_KEYS, code)
    for prefix in _PREFIXES:
        count = _count(value[f"{prefix}_count"], code)
        weight = _number(value[f"{prefix}_weight"], code)
        _require((count == 0) == (weight == 0), code)
    _require(value["total_count"] > 0
             and value["total_count"] == value["eligible_count"] + value["not_asked_count"]
             and value["eligible_count"] == value["valid_count"] + value["missing_count"], code)
    _require(_close(value["total_weight"], fsum((value["eligible_weight"], value["not_asked_weight"])))
             and _close(value["eligible_weight"], fsum((value["valid_weight"], value["missing_weight"]))), code)
    return Accounting(**{key: float(val) if key.endswith("_weight") else val for key, val in value.items()})


def _counts(accounting):
    return tuple(getattr(accounting, f"{prefix}_count") for prefix in _PREFIXES)


def _reference(value, definitions, study_id, question_id, primary, category_counts):
    code = ExportErrorCode.INVALID_CANDIDATE
    _object(value, {"variance_status", "estimates", "sensitivity", "anweight_equivalence_diagnostic"}, code)
    _require(value["variance_status"] == "no_design_basis", code)
    estimates = _object(value["estimates"], _ROLES, code)
    references = {}
    for weight, role in _ROLES.items():
        estimate = _object(estimates[weight], {"role", "accounting", "categories"}, code)
        _require(estimate["role"] == role, code)
        accounting = _accounting(estimate["accounting"])
        _require(_counts(accounting) == _counts(primary), code)
        if weight == "pspwght":
            _require(accounting == primary, code)
        categories = _array(estimate["categories"], code)
        _require(len(categories) == len(definitions["categoryCodes"]), code)
        converted = []
        for category, expected_code, expected_count in zip(
                categories, definitions["categoryCodes"], category_counts, strict=True):
            _object(category, {"code", "count", "weight_sum", "proportion"}, code)
            _require(category["code"] == expected_code
                     and _count(category["count"], code) == expected_count, code)
            amount = _number(category["weight_sum"], code)
            proportion = _number(category["proportion"], code)
            _require(proportion <= 1 and abs(proportion - amount / accounting.valid_weight) <= TOLERANCE, code)
            converted.append(CategoryEstimate(expected_code, expected_count, amount, proportion, None, None))
        reference = CategoricalReference(study_id, question_id, accounting, tuple(converted),
                                         VarianceStatus.NO_DESIGN_BASIS, None)
        _validate_reference(reference, study_id, question_id)
        if weight == "unweighted":
            _require(all(getattr(accounting, f"{prefix}_weight") == getattr(accounting, f"{prefix}_count")
                         for prefix in _PREFIXES)
                     and all(cat.weight == cat.count for cat in converted), code)
        references[weight] = reference
    sensitivity = _object(value["sensitivity"], {"max_abs_primary_unweighted", "max_abs_primary_dweight"}, code)
    diagnostic = _object(value["anweight_equivalence_diagnostic"], {
        "max_abs_primary_anweight", "ratio_scope", "anweight_pspwght_ratio_min",
        "anweight_pspwght_ratio_max"}, code)
    for weight, holder, key in (
        ("unweighted", sensitivity, "max_abs_primary_unweighted"),
        ("dweight", sensitivity, "max_abs_primary_dweight"),
        ("anweight", diagnostic, "max_abs_primary_anweight"),
    ):
        difference = max(abs(a.proportion - b.proportion) for a, b in zip(
            references["pspwght"].estimates, references[weight].estimates, strict=True))
        supplied = _number(holder[key], code)
        _require(supplied <= 1 and abs(supplied - difference) <= TOLERANCE, code)
    minimum = _number(diagnostic["anweight_pspwght_ratio_min"], code)
    maximum = _number(diagnostic["anweight_pspwght_ratio_max"], code)
    _require(diagnostic["ratio_scope"] == "all_de_cases" and 0 < minimum <= maximum, code)
    # Aggregate bounds can detect contradictions, never certify row extrema.
    pairs = [(getattr(references["anweight"].accounting, f"{p}_weight"),
              getattr(primary, f"{p}_weight")) for p in _PREFIXES]
    pairs.extend((a.weight, p.weight) for a, p in zip(
        references["anweight"].estimates, references["pspwght"].estimates, strict=True))
    for numerator, denominator in pairs:
        if denominator:
            ratio = numerator / denominator
            _require(isfinite(ratio) and (minimum <= ratio or _close(minimum, ratio))
                     and (ratio <= maximum or _close(ratio, maximum)), code)
    return references


def _candidate(candidate, study, definitions):
    code = ExportErrorCode.INVALID_CANDIDATE
    _object(candidate, {"schema", "study_id", "edition", "questions"}, code)
    _require(candidate["schema"] == "policy-reference-candidate-v2-wip"
             and candidate["study_id"] == study["study_id"] and candidate["edition"] == study["edition"], code)
    questions = _array(candidate["questions"], code)
    _require(len(questions) == len(definitions), code)
    totals, ratios, estimate_totals = [], [], {weight: [] for weight in _ROLES}
    prepared_ids = set()
    for question, definition in zip(questions, definitions, strict=True):
        _object(question, {"source", "status", "category_counts", "primary_accounting",
                           "missing_reasons", "not_asked", "reference"}, code)
        source = _object(question["source"], {"study_id", "edition", "question_id"}, code)
        _require(source == {"study_id": study["study_id"], "edition": study["edition"],
                            "question_id": definition["question_id"]}, code)
        accounting = _accounting(question["primary_accounting"])
        totals.append((accounting.total_count, accounting.total_weight))
        categories = _array(question["category_counts"], code)
        _require(len(categories) == len(definition["categoryCodes"]), code)
        counts = []
        for category, expected_code in zip(categories, definition["categoryCodes"], strict=True):
            _object(category, {"code", "count"}, code)
            _require(category["code"] == expected_code, code)
            counts.append(_count(category["count"], code))
        _require(sum(counts) == accounting.valid_count, code)
        expected_status = (_NO_VALID if accounting.valid_count == 0 else
                           _WITHHELD if accounting.valid_count < 100 or any(0 < n < 5 for n in counts)
                           else _PREPARED)
        _require(type(question["status"]) is str and question["status"] == expected_status, code)
        reasons = _array(question["missing_reasons"], code)
        seen, reason_counts, reason_weights = set(), [], []
        for reason in reasons:
            _object(reason, {"reason", "count", "primary_weight_sum"}, code)
            name = _text(reason["reason"], code)
            _require(name not in seen, code)
            seen.add(name)
            count = _count(reason["count"], code)
            amount = _number(reason["primary_weight_sum"], code)
            _require((count == 0) == (amount == 0), code)
            reason_counts.append(count)
            reason_weights.append(amount)
        _require(seen == set(definition["missingCodes"].values())
                 and sum(reason_counts) == accounting.missing_count
                 and _close(fsum(reason_weights), accounting.missing_weight), code)
        not_asked = _object(question["not_asked"], {"count", "primary_weight_sum"}, code)
        _require(_count(not_asked["count"], code) == accounting.not_asked_count
                 and _number(not_asked["primary_weight_sum"], code) == accounting.not_asked_weight
                 and (bool(definition["structurallyNotAskedCodes"]) or accounting.not_asked_count == 0), code)
        if expected_status == _PREPARED:
            prepared_ids.add(definition["question_id"])
            references = _reference(question["reference"], definition, study["study_id"],
                                    definition["question_id"], accounting, counts)
            for weight, reference in references.items():
                estimate_totals[weight].append(reference.accounting.total_weight)
            diag = question["reference"]["anweight_equivalence_diagnostic"]
            ratios.append((diag["anweight_pspwght_ratio_min"], diag["anweight_pspwght_ratio_max"]))
        else:
            _require(question["reference"] is None, code)
    _require(all(count == totals[0][0] and _close(weight, totals[0][1]) for count, weight in totals), code)
    _require(all(pair == ratios[0] for pair in ratios), code)
    _require(all(all(_close(value, values[0]) for value in values) for values in estimate_totals.values()), code)
    return prepared_ids


def validate_reference_candidate(candidate, study_contract) -> None:
    """Validate closed JSON structure and aggregate consistency, without IO.

    Exact built-in dict/list/scalar inputs only. Finite JSON integers/floats are
    accepted for numeric weights; bool is never a count or weight. Hashing keeps
    the supplied numeric representation. No isolation from hostile Python code.
    Global 43-selection, authentic sources and actual row extrema stay external.
    """
    try:
        _json_values(study_contract, ExportErrorCode.INVALID_CONTRACT)
        _json_values(candidate, ExportErrorCode.INVALID_CANDIDATE)
        definitions = _contract(study_contract)
        _candidate(candidate, study_contract, definitions)
        _canonical_hash(study_contract)
        _canonical_hash(candidate)
    except PolicyExportError:
        raise
    except (PolicyAnalysisError, ValueError, TypeError, AttributeError, ArithmeticError, RecursionError):
        raise PolicyExportError(ExportErrorCode.INVALID_CANDIDATE) from None


def _decision(decision, candidate, study, prepared_ids):
    code = ExportErrorCode.INVALID_DECISION
    _json_values(decision, code)
    _object(decision, {"schemaVersion", "decision", "studyId", "edition", "candidateSha256",
                       "sourceContractSha256", "approvedQuestionIds", "reviewManifestSha256", "reviewers"}, code)
    _require(type(decision["schemaVersion"]) is int and decision["schemaVersion"] == 1
             and decision["decision"] == "ALLOW_REVIEWED_HISTORICAL_REFERENCE_V2"
             and decision["studyId"] == study["study_id"] and decision["edition"] == study["edition"], code)
    for key in ("candidateSha256", "sourceContractSha256", "reviewManifestSha256"):
        _hash(decision[key], code)
    _require(decision["candidateSha256"] == _canonical_hash(candidate)
             and decision["sourceContractSha256"] == _canonical_hash(study), ExportErrorCode.HASH_MISMATCH)
    approved = _strings(decision["approvedQuestionIds"], code, unique=True)
    _require(set(approved) <= prepared_ids, code)
    reviewers = _array(decision["reviewers"], code)
    _require(len(reviewers) == 2, code)
    roles, paths = set(), set()
    for reviewer in reviewers:
        _object(reviewer, {"role", "reportPath", "sha256", "decision"}, code)
        role, path = _text(reviewer["role"], code), _text(reviewer["reportPath"], code)
        _require(role not in roles and path not in paths
                 and re.fullmatch(r"reports/loop/reviews/[A-Za-z0-9][A-Za-z0-9_.-]*\.md", path) is not None
                 and reviewer["decision"] == "ACCEPTED_BOUNDED", code)
        _hash(reviewer["sha256"], code)
        roles.add(role)
        paths.add(path)
    _require(roles == {"methods_reproducibility", "sources_constructs_fairness"}, code)
    return set(approved)


def build_reviewed_reference_export(candidate, study_contract, decision) -> dict:
    """Build a detached public allowlist under a separately verified Root gate.

    This validates formal hash/ID/role binding; it does not read or authenticate
    reports, manifests or source files. Source attribution remains in the pinned
    public catalog. Subset approval limits references, never removes questions.
    """
    validate_reference_candidate(candidate, study_contract)
    try:
        prepared_ids = {q["source"]["question_id"] for q in candidate["questions"] if q["status"] == _PREPARED}
        approved = _decision(decision, candidate, study_contract, prepared_ids)
        questions = []
        for question in candidate["questions"]:
            qid, status = question["source"]["question_id"], question["status"]
            reference = None
            if status == _PREPARED and qid in approved:
                status = "reviewed_historical_reference"
                private = question["reference"]
                primary = private["estimates"]["pspwght"]
                accounting = question["primary_accounting"]
                diagnostic = private["anweight_equivalence_diagnostic"]
                reference = {
                    "weight": "pspwght", "validCount": accounting["valid_count"],
                    "totalCount": accounting["total_count"], "missingCount": accounting["missing_count"],
                    "notAskedCount": accounting["not_asked_count"],
                    "categories": [{"code": cat["code"], "proportion": cat["proportion"]}
                                   for cat in primary["categories"]],
                    "missingReasons": [{"reason": r["reason"], "count": r["count"],
                                        "primaryWeightSum": r["primary_weight_sum"]} for r in question["missing_reasons"]],
                    "missingWeight": accounting["missing_weight"], "allDEWeight": accounting["total_weight"],
                    "sensitivity": {"maxAbsUnweighted": private["sensitivity"]["max_abs_primary_unweighted"],
                                    "maxAbsDweight": private["sensitivity"]["max_abs_primary_dweight"]},
                    "anweightEquivalenceDiagnostic": {
                        "maxAbsDifference": diagnostic["max_abs_primary_anweight"], "ratioScope": "all_de_cases",
                        "ratioMin": diagnostic["anweight_pspwght_ratio_min"],
                        "ratioMax": diagnostic["anweight_pspwght_ratio_max"]},
                    "uncertainty": None,
                }
            elif status == _PREPARED:
                status = "result_review_withheld"
            questions.append({"id": qid, "status": status, "reference": reference})
        return {"schemaVersion": 2, "status": "reviewed_historical_descriptive_reference",
                "studyId": study_contract["study_id"], "edition": study_contract["edition"],
                "sourceContractSha256": decision["sourceContractSha256"],
                "candidateSha256": decision["candidateSha256"],
                "reviewManifestSha256": decision["reviewManifestSha256"], "questions": questions}
    except PolicyExportError:
        raise
    except (ValueError, TypeError, AttributeError, ArithmeticError, RecursionError):
        raise PolicyExportError(ExportErrorCode.INVALID_DECISION) from None
