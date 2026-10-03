"""Private WIP aggregation of one validated in-memory study at a time.

No file/CLI/network operations, study joins, item selection or publication gate.
The display counts below are project heuristics, not precision/privacy claims.
All estimates omit design and SE; a full source-bound basis remains external.
"""

from dataclasses import dataclass
from enum import Enum
from math import fsum, isclose, isfinite

from pipeline.policy_adapter_v2 import (
    AdapterDiagnostics,
    PrivateStudyCsv,
    _PrivateAnswer,
    _PrivateDERecord,
    _PrivateDesignIdentifiers,
    _QuestionContract,
    _StudyContract,
    _contract as validate_adapter_contract,
)
from pipeline.policy_reference_v2 import (
    Accounting,
    CategoricalReference,
    CategoryEstimate,
    Observation,
    VarianceStatus,
    categorical_reference,
)


MIN_VALID_COUNT = 100
MIN_POSITIVE_CELL_COUNT = 5
# Fixed floating arithmetic tolerance, unrelated to result/display thresholds.
ARITHMETIC_TOLERANCE = 1e-12


class AnalysisErrorCode(str, Enum):
    INVALID_PARSED_INPUT = "invalid_parsed_input"
    ARITHMETIC_FAILURE = "arithmetic_failure"
    INVALID_PREPARED_INPUT = "invalid_prepared_input"


class PolicyAnalysisError(ValueError):
    def __init__(self, code: AnalysisErrorCode):
        self.code = code
        super().__init__(f"policy_analysis_error: {code.value}")


class PreparationStatus(str, Enum):
    NO_VALID_ANSWERS = "no_valid_answers"
    WITHHELD_BASE_OR_CELL_COUNT = "withheld_base_or_cell_count"
    PREPARED_PENDING_RESULT_REVIEW = "prepared_pending_result_review"


class _PrivateAggregateRepr:
    __slots__ = ()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(<private unreviewed aggregates>)"


@dataclass(frozen=True, slots=True, repr=False)
class PreparedWeightReference(_PrivateAggregateRepr):
    weight: str
    role: str
    reference: CategoricalReference


@dataclass(frozen=True, slots=True, repr=False)
class MissingReasonAggregate(_PrivateAggregateRepr):
    reason: str
    count: int
    primary_weight_sum: float


@dataclass(frozen=True, slots=True, repr=False)
class NotAskedAggregate(_PrivateAggregateRepr):
    count: int
    primary_weight_sum: float


@dataclass(frozen=True, slots=True, repr=False)
class WeightDiagnostics(_PrivateAggregateRepr):
    max_abs_primary_unweighted: float | None
    max_abs_primary_dweight: float | None
    max_abs_primary_anweight: float | None
    all_de_anweight_pspwght_ratio_min: float
    all_de_anweight_pspwght_ratio_max: float


@dataclass(frozen=True, slots=True, repr=False)
class PreparedQuestionReferences(_PrivateAggregateRepr):
    question_id: str
    status: PreparationStatus
    estimates: tuple[PreparedWeightReference, ...]
    missing_reasons: tuple[MissingReasonAggregate, ...]
    not_asked: NotAskedAggregate
    weight_diagnostics: WeightDiagnostics


@dataclass(frozen=True, slots=True, repr=False)
class PrivateStudyReferences(_PrivateAggregateRepr):
    """Copied aggregate payload, still private and pending external review."""

    study_id: str
    edition: str
    questions: tuple[PreparedQuestionReferences, ...]


_WEIGHT_ROLES = (
    ("pspwght", "primary"),
    ("dweight", "sensitivity"),
    ("unweighted", "sensitivity"),
    ("anweight", "equivalence_diagnostic"),
)


def _fail(code: AnalysisErrorCode) -> None:
    raise PolicyAnalysisError(code) from None


def _require(condition: bool, code: AnalysisErrorCode) -> None:
    if not condition:
        _fail(code)


def _tuple(value: object, code: AnalysisErrorCode) -> tuple:
    _require(type(value) is tuple, code)
    return value


def _copy_contract(value: object) -> _StudyContract:
    """Revalidate the known parser schema; no arbitrary mapping is accepted."""
    code = AnalysisErrorCode.INVALID_PARSED_INPUT
    _require(type(value) is _StudyContract, code)
    sensitivities = _tuple(value._sensitivity_weights, code)
    questions = _tuple(value._questions, code)
    definitions = []
    for question in questions:
        _require(type(question) is _QuestionContract, code)
        categories = _tuple(question._category_codes, code)
        missing = _tuple(question._missing_codes, code)
        not_asked = _tuple(question._not_asked_codes, code)
        for pair in missing:
            _require(type(pair) is tuple and len(pair) == 2 and type(pair[0]) is str, code)
        missing_map = dict(missing)
        _require(len(missing_map) == len(missing), code)
        definitions.append({
            "question_id": question._question_id,
            "variable": question._variable,
            "categoryCodes": list(categories),
            "missingCodes": missing_map,
            "structurallyNotAskedCodes": list(not_asked),
        })
    design = value._design_columns
    if design is not None:
        _require(type(design) is tuple and len(design) == 2, code)
    supplied = {
        "study_id": value._study_id,
        "edition": value._edition,
        "country": value._country,
        "country_column": value._country_column,
        "id_column": value._id_column,
        "weight_columns": {"primary": value._primary_weight, "sensitivities": list(sensitivities)},
        "questions": definitions,
        "design_columns": None if design is None else {"stratum": design[0], "psu": design[1]},
    }
    return validate_adapter_contract(supplied)


def _checked_records(parsed: PrivateStudyCsv, contract: _StudyContract) -> tuple[_PrivateDERecord, ...]:
    code = AnalysisErrorCode.INVALID_PARSED_INPUT
    records = _tuple(parsed._records, code)
    _require(bool(records) and type(parsed.diagnostics) is AdapterDiagnostics, code)
    seen_ids = set()
    categories = [set(question._category_codes) for question in contract._questions]
    missing = [dict(question._missing_codes) for question in contract._questions]
    not_asked = [set(question._not_asked_codes) for question in contract._questions]
    for record in records:
        _require(type(record) is _PrivateDERecord, code)
        identity = record._idno
        _require(type(identity) is str and any(not char.isspace() for char in identity), code)
        _require(identity not in seen_ids, code)
        seen_ids.add(identity)
        weights = _tuple(record._weights, code)
        _require(len(weights) == 3, code)
        for pair in weights:
            _require(type(pair) is tuple and len(pair) == 2 and type(pair[0]) is str, code)
            _require(type(pair[1]) is float and isfinite(pair[1]) and pair[1] > 0, code)
        _require({pair[0] for pair in weights} == {"pspwght", "dweight", "anweight"}, code)
        answers = _tuple(record._answers, code)
        _require(len(answers) == len(contract._questions), code)
        for index, answer in enumerate(answers):
            _require(type(answer) is _PrivateAnswer and type(answer._raw_code) is str, code)
            _require(type(answer._eligible) is bool and type(answer._missing) is bool, code)
            raw = answer._raw_code
            if raw in categories[index]:
                _require(type(answer._response) is str and answer._response == raw
                         and answer._eligible and not answer._missing
                         and answer._missing_reason is None, code)
            elif raw in missing[index]:
                _require(answer._response is None and answer._eligible and answer._missing
                         and type(answer._missing_reason) is str
                         and answer._missing_reason == missing[index][raw], code)
            elif raw in not_asked[index]:
                _require(answer._response is None and not answer._eligible and not answer._missing
                         and answer._missing_reason is None, code)
            else:
                _fail(code)
        _require(record._design is None or type(record._design) is _PrivateDesignIdentifiers, code)
    # These temporary records never become part of the prepared result.
    return records


def _finite_sum(values) -> float:
    total = fsum(values)
    _require(isfinite(total), AnalysisErrorCode.ARITHMETIC_FAILURE)
    return total


def _difference(first: CategoricalReference, second: CategoricalReference) -> float | None:
    if first.accounting.valid_count == 0:
        return None
    return max(abs(left.proportion - right.proportion)
               for left, right in zip(first.estimates, second.estimates, strict=True))


def _status(unweighted: CategoricalReference) -> PreparationStatus:
    if unweighted.accounting.valid_count == 0:
        return PreparationStatus.NO_VALID_ANSWERS
    if (unweighted.accounting.valid_count < MIN_VALID_COUNT
            or any(0 < estimate.count < MIN_POSITIVE_CELL_COUNT for estimate in unweighted.estimates)):
        return PreparationStatus.WITHHELD_BASE_OR_CELL_COUNT
    return PreparationStatus.PREPARED_PENDING_RESULT_REVIEW


def prepare_study_references(parsed: PrivateStudyCsv) -> PrivateStudyReferences:
    """Compute four separate references per question, without any design/SE.

    Only exact parser dataclasses are accepted; used fields and their relations
    are revalidated. This is a typed data boundary, not proof that the caller ran
    the parser or that its study provenance is authentic. Parser diagnostic
    values are not treated as authoritative; accounting is recomputed from rows.
    """
    try:
        _require(type(parsed) is PrivateStudyCsv, AnalysisErrorCode.INVALID_PARSED_INPUT)
        contract = _copy_contract(parsed._contract)
        records = _checked_records(parsed, contract)
    except PolicyAnalysisError:
        raise
    except (ValueError, TypeError, AttributeError, OverflowError):
        _fail(AnalysisErrorCode.INVALID_PARSED_INPUT)
    try:
        ratios = [dict(record._weights)["anweight"] / dict(record._weights)["pspwght"]
                  for record in records]
        _require(all(isfinite(ratio) and ratio > 0 for ratio in ratios), AnalysisErrorCode.ARITHMETIC_FAILURE)
        ratio_min, ratio_max = min(ratios), max(ratios)
        prepared_questions = []
        for index, question in enumerate(contract._questions):
            estimates = []
            for weight, role in _WEIGHT_ROLES:
                observations = tuple(Observation(
                    response=record._answers[index]._response,
                    weight=1.0 if weight == "unweighted" else dict(record._weights)[weight],
                    eligible=record._answers[index]._eligible,
                    missing=record._answers[index]._missing,
                    design=None,
                ) for record in records)
                reference = categorical_reference(
                    study_id=contract._study_id,
                    question_id=question._question_id,
                    categories=question._category_codes,
                    observations=observations,
                    design_basis=None,
                )
                estimates.append(PreparedWeightReference(weight, role, reference))
            primary, dweight, unweighted, anweight = [estimate.reference for estimate in estimates]
            reasons = tuple(dict.fromkeys(reason for _, reason in question._missing_codes))
            missing_reasons = tuple(MissingReasonAggregate(
                reason=reason,
                count=sum(record._answers[index]._missing_reason == reason for record in records),
                primary_weight_sum=_finite_sum(dict(record._weights)["pspwght"] for record in records
                                               if record._answers[index]._missing_reason == reason),
            ) for reason in reasons)
            prepared_questions.append(PreparedQuestionReferences(
                question_id=question._question_id,
                status=_status(unweighted),
                estimates=tuple(estimates),
                missing_reasons=missing_reasons,
                not_asked=NotAskedAggregate(primary.accounting.not_asked_count, primary.accounting.not_asked_weight),
                weight_diagnostics=WeightDiagnostics(
                    _difference(primary, unweighted), _difference(primary, dweight),
                    _difference(primary, anweight), ratio_min, ratio_max,
                ),
            ))
        prepared = PrivateStudyReferences(contract._study_id, contract._edition, tuple(prepared_questions))
        _validate_prepared(prepared)
        return prepared
    except PolicyAnalysisError:
        raise
    except (ValueError, TypeError, AttributeError, ArithmeticError):
        # Never forward generic-library text containing a response or other value.
        _fail(AnalysisErrorCode.ARITHMETIC_FAILURE)


def _count(value: object) -> bool:
    return type(value) is int and value >= 0


def _nonnegative(value: object) -> bool:
    return type(value) is float and isfinite(value) and value >= 0


def _close(first: float, second: float) -> bool:
    return isclose(first, second, rel_tol=ARITHMETIC_TOLERANCE, abs_tol=0.0)


def _validate_reference(reference: object, study_id: str, question_id: str) -> None:
    code = AnalysisErrorCode.INVALID_PREPARED_INPUT
    _require(type(reference) is CategoricalReference, code)
    _require(type(reference.study_id) is str and type(reference.question_id) is str
             and reference.study_id == study_id and reference.question_id == question_id
             and reference.design is None, code)
    accounting = reference.accounting
    _require(type(accounting) is Accounting, code)
    for prefix in ("total", "eligible", "valid", "missing", "not_asked"):
        count, weight = getattr(accounting, f"{prefix}_count"), getattr(accounting, f"{prefix}_weight")
        _require(_count(count) and _nonnegative(weight) and ((count == 0) == (weight == 0)), code)
    _require(accounting.total_count == accounting.eligible_count + accounting.not_asked_count, code)
    _require(accounting.eligible_count == accounting.valid_count + accounting.missing_count, code)
    _require(_close(accounting.total_weight, fsum((accounting.eligible_weight, accounting.not_asked_weight))), code)
    _require(_close(accounting.eligible_weight, fsum((accounting.valid_weight, accounting.missing_weight))), code)
    estimates = _tuple(reference.estimates, code)
    _require(bool(estimates), code)
    category_codes = []
    for estimate in estimates:
        _require(type(estimate) is CategoryEstimate and type(estimate.category) is str and estimate.category != "", code)
        category_codes.append(estimate.category)
        _require(_count(estimate.count) and _nonnegative(estimate.weight)
                 and ((estimate.count == 0) == (estimate.weight == 0)), code)
        _require(estimate.variance is None and estimate.standard_error is None, code)
        if accounting.valid_count == 0:
            _require(estimate.proportion is None, code)
        else:
            _require(_nonnegative(estimate.proportion) and estimate.proportion <= 1, code)
            _require(_close(estimate.proportion, estimate.weight / accounting.valid_weight), code)
    _require(len(set(category_codes)) == len(category_codes), code)
    _require(sum(estimate.count for estimate in estimates) == accounting.valid_count, code)
    _require(_close(fsum(estimate.weight for estimate in estimates), accounting.valid_weight), code)
    expected_variance_status = VarianceStatus.NO_VALID_RESPONSES if accounting.valid_count == 0 else VarianceStatus.NO_DESIGN_BASIS
    _require(reference.variance_status is expected_variance_status, code)
    if accounting.valid_count:
        _require(abs(fsum(estimate.proportion for estimate in estimates) - 1.0) <= ARITHMETIC_TOLERANCE, code)


def _validate_prepared(prepared: object) -> None:
    code = AnalysisErrorCode.INVALID_PREPARED_INPUT
    _require(type(prepared) is PrivateStudyReferences, code)
    for identifier in (prepared.study_id, prepared.edition):
        _require(type(identifier) is str and bool(identifier) and identifier.strip() == identifier, code)
    questions = _tuple(prepared.questions, code)
    _require(bool(questions), code)
    seen = set()
    total_counts = []
    for question in questions:
        _require(type(question) is PreparedQuestionReferences, code)
        _require(type(question.question_id) is str and bool(question.question_id)
                 and question.question_id.strip() == question.question_id and question.question_id not in seen, code)
        seen.add(question.question_id)
        estimates = _tuple(question.estimates, code)
        _require(len(estimates) == len(_WEIGHT_ROLES), code)
        for estimate, (weight, role) in zip(estimates, _WEIGHT_ROLES, strict=True):
            _require(type(estimate) is PreparedWeightReference and type(estimate.weight) is str
                     and type(estimate.role) is str and estimate.weight == weight and estimate.role == role, code)
            _validate_reference(estimate.reference, prepared.study_id, question.question_id)
        primary, dweight, unweighted, anweight = [estimate.reference for estimate in estimates]
        primary_codes_counts = tuple((estimate.category, estimate.count) for estimate in primary.estimates)
        counts = (primary.accounting.total_count, primary.accounting.eligible_count, primary.accounting.valid_count,
                  primary.accounting.missing_count, primary.accounting.not_asked_count)
        total_counts.append(primary.accounting.total_count)
        _require(primary.accounting.total_count > 0, code)
        for reference in (dweight, unweighted, anweight):
            _require(tuple((estimate.category, estimate.count) for estimate in reference.estimates) == primary_codes_counts, code)
            _require((reference.accounting.total_count, reference.accounting.eligible_count, reference.accounting.valid_count,
                      reference.accounting.missing_count, reference.accounting.not_asked_count) == counts, code)
        for prefix in ("total", "eligible", "valid", "missing", "not_asked"):
            _require(getattr(unweighted.accounting, f"{prefix}_weight") == getattr(unweighted.accounting, f"{prefix}_count"), code)
        _require(all(estimate.weight == estimate.count for estimate in unweighted.estimates), code)
        _require(type(question.status) is PreparationStatus and question.status is _status(unweighted), code)
        missing_reasons = _tuple(question.missing_reasons, code)
        reasons = set()
        for reason in missing_reasons:
            _require(type(reason) is MissingReasonAggregate and type(reason.reason) is str
                     and bool(reason.reason) and reason.reason.strip() == reason.reason and reason.reason not in reasons, code)
            reasons.add(reason.reason)
            _require(_count(reason.count) and _nonnegative(reason.primary_weight_sum)
                     and ((reason.count == 0) == (reason.primary_weight_sum == 0)), code)
        _require(sum(reason.count for reason in missing_reasons) == primary.accounting.missing_count, code)
        _require(_close(fsum(reason.primary_weight_sum for reason in missing_reasons), primary.accounting.missing_weight), code)
        _require(type(question.not_asked) is NotAskedAggregate and _count(question.not_asked.count)
                 and _nonnegative(question.not_asked.primary_weight_sum)
                 and question.not_asked.count == primary.accounting.not_asked_count
                 and question.not_asked.primary_weight_sum == primary.accounting.not_asked_weight, code)
        diagnostics = question.weight_diagnostics
        _require(type(diagnostics) is WeightDiagnostics, code)
        for value, expected in (
            (diagnostics.max_abs_primary_unweighted, _difference(primary, unweighted)),
            (diagnostics.max_abs_primary_dweight, _difference(primary, dweight)),
            (diagnostics.max_abs_primary_anweight, _difference(primary, anweight)),
        ):
            _require(value is None if expected is None else _nonnegative(value) and value <= 1 and _close(value, expected), code)
        _require(_nonnegative(diagnostics.all_de_anweight_pspwght_ratio_min)
                 and _nonnegative(diagnostics.all_de_anweight_pspwght_ratio_max)
                 and 0 < diagnostics.all_de_anweight_pspwght_ratio_min <= diagnostics.all_de_anweight_pspwght_ratio_max, code)
    _require(len(set(total_counts)) == 1, code)


def _accounting_candidate(accounting: Accounting) -> dict:
    return {
        "total_count": accounting.total_count, "total_weight": accounting.total_weight,
        "eligible_count": accounting.eligible_count, "eligible_weight": accounting.eligible_weight,
        "valid_count": accounting.valid_count, "valid_weight": accounting.valid_weight,
        "missing_count": accounting.missing_count, "missing_weight": accounting.missing_weight,
        "not_asked_count": accounting.not_asked_count, "not_asked_weight": accounting.not_asked_weight,
    }


def expose_prepared_candidate(prepared: PrivateStudyReferences) -> dict:
    """Build a detached allowlisted JSON shape, never a final/reviewed export.

    Private estimates remain available internally even when withheld. Candidate
    fractions and sensitivity metadata appear only when the fixed count
    heuristics pass. All questions remain present regardless of result/status.
    """
    try:
        _validate_prepared(prepared)
    except PolicyAnalysisError:
        raise
    except (ValueError, TypeError, AttributeError, ArithmeticError):
        _fail(AnalysisErrorCode.INVALID_PREPARED_INPUT)
    questions = []
    for question in prepared.questions:
        primary = question.estimates[0].reference
        candidate_reference = None
        if question.status is PreparationStatus.PREPARED_PENDING_RESULT_REVIEW:
            diagnostics = question.weight_diagnostics
            candidate_reference = {
                "variance_status": "no_design_basis",
                "estimates": {
                    estimate.weight: {
                        "role": estimate.role,
                        "accounting": _accounting_candidate(estimate.reference.accounting),
                        "categories": [{
                            "code": category.category, "count": category.count,
                            "weight_sum": category.weight, "proportion": category.proportion,
                        } for category in estimate.reference.estimates],
                    } for estimate in question.estimates
                },
                "sensitivity": {
                    "max_abs_primary_unweighted": diagnostics.max_abs_primary_unweighted,
                    "max_abs_primary_dweight": diagnostics.max_abs_primary_dweight,
                },
                "anweight_equivalence_diagnostic": {
                    "max_abs_primary_anweight": diagnostics.max_abs_primary_anweight,
                    "ratio_scope": "all_de_cases",
                    "anweight_pspwght_ratio_min": diagnostics.all_de_anweight_pspwght_ratio_min,
                    "anweight_pspwght_ratio_max": diagnostics.all_de_anweight_pspwght_ratio_max,
                },
            }
        questions.append({
            "source": {"study_id": prepared.study_id, "edition": prepared.edition, "question_id": question.question_id},
            "status": question.status.value,
            "category_counts": [{"code": category.category, "count": category.count} for category in primary.estimates],
            "primary_accounting": _accounting_candidate(primary.accounting),
            "missing_reasons": [{"reason": reason.reason, "count": reason.count,
                                 "primary_weight_sum": reason.primary_weight_sum} for reason in question.missing_reasons],
            "not_asked": {"count": question.not_asked.count, "primary_weight_sum": question.not_asked.primary_weight_sum},
            "reference": candidate_reference,
        })
    return {"schema": "policy-reference-candidate-v2-wip", "study_id": prepared.study_id,
            "edition": prepared.edition, "questions": questions}
