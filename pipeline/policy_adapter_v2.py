"""WIP in-memory CSV preparation for separate study/question references.

Only caller-supplied text and a synthetic or later source-bound contract are
accepted. This module performs no file, network, CLI or persistence operations.
Returned records contain private identifiers and must not be logged or exported.
Observed design identifiers never establish a complete survey design basis.
"""

import csv
from dataclasses import dataclass
from enum import Enum
from io import StringIO
from math import isfinite


class AdapterErrorCode(str, Enum):
    INVALID_CONTRACT = "invalid_contract"
    INVALID_TEXT = "invalid_text"
    EMPTY_CSV = "empty_csv"
    INVALID_CSV = "invalid_csv"
    EMPTY_HEADER = "empty_header"
    DUPLICATE_HEADER = "duplicate_header"
    MISSING_REQUIRED_COLUMN = "missing_required_column"
    INVALID_ROW_WIDTH = "invalid_row_width"
    INVALID_DE_ID = "invalid_de_id"
    DUPLICATE_DE_ID = "duplicate_de_id"
    INVALID_WEIGHT = "invalid_weight"
    UNKNOWN_DE_CODE = "unknown_de_code"
    NO_DE_ROWS = "no_de_rows"


class PolicyAdapterError(ValueError):
    """A value-free error code: no row, code, header or identifier is included."""

    def __init__(self, code: AdapterErrorCode):
        self.code = code
        super().__init__(f"policy_adapter_error: {code.value}")


class AdapterDesignStatus(str, Enum):
    NO_DESIGN_DECLARED = "no_design_declared"
    INCOMPLETE_IDENTIFIERS = "incomplete_identifiers"
    IDENTIFIERS_COMPLETE_UNVERIFIED_BASIS = "identifiers_complete_unverified_basis"


@dataclass(frozen=True, slots=True)
class QuestionCounts:
    # Corresponds to contract question order; no question/record keys are public.
    valid_count: int
    missing_count: int
    not_asked_count: int


@dataclass(frozen=True, slots=True)
class AdapterDesignDiagnostics:
    status: AdapterDesignStatus
    identifiers_complete: bool
    se_available: bool
    # Counts refer only to valid observed DE pairs, never a certified full basis.
    observed_strata_count: int
    observed_psu_count: int


@dataclass(frozen=True, slots=True)
class AdapterDiagnostics:
    de_row_count: int
    question_counts: tuple[QuestionCounts, ...]
    design: AdapterDesignDiagnostics


class _PrivateRepr:
    __slots__ = ()

    def __repr__(self) -> str:
        return f"{type(self).__name__}(<private in-memory data>)"


@dataclass(frozen=True, slots=True, repr=False)
class _QuestionContract(_PrivateRepr):
    _question_id: str
    _variable: str
    _category_codes: tuple[str, ...]
    _missing_codes: tuple[tuple[str, str], ...]
    _not_asked_codes: tuple[str, ...]


@dataclass(frozen=True, slots=True, repr=False)
class _StudyContract(_PrivateRepr):
    _study_id: str
    _edition: str
    _country: str
    _country_column: str
    _id_column: str
    _primary_weight: str
    _sensitivity_weights: tuple[str, ...]
    _questions: tuple[_QuestionContract, ...]
    _design_columns: tuple[str, str] | None  # (stratum column, PSU column)


@dataclass(frozen=True, slots=True, repr=False)
class _PrivateAnswer(_PrivateRepr):
    _raw_code: str
    _response: str | None
    _eligible: bool
    _missing: bool
    _missing_reason: str | None


@dataclass(frozen=True, slots=True, repr=False)
class _PrivateDesignIdentifiers(_PrivateRepr):
    _stratum: str
    _psu: str


@dataclass(frozen=True, slots=True, repr=False)
class _PrivateDERecord(_PrivateRepr):
    _idno: str
    _weights: tuple[tuple[str, float], ...]
    _answers: tuple[_PrivateAnswer, ...]
    _design: _PrivateDesignIdentifiers | None


@dataclass(frozen=True, slots=True, repr=False)
class PrivateStudyCsv(_PrivateRepr):
    """Private payload. Only ``diagnostics`` is a value-free summary.

    ``_records`` and ``_contract`` are intentionally private attributes for a
    later controlled caller. Their fields must not enter logs, UI or reports.
    A redacted repr is a convenience, not an access-control boundary.
    """

    _contract: _StudyContract
    _records: tuple[_PrivateDERecord, ...]
    diagnostics: AdapterDiagnostics


def _fail(code: AdapterErrorCode) -> None:
    raise PolicyAdapterError(code) from None


def _mapping(value: object, required: set[str], optional: set[str] | None = None) -> dict:
    if type(value) is not dict:
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    if any(type(key) is not str for key in value):
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    allowed = required | (optional or set())
    if set(value) - allowed or not required <= set(value):
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    return value


def _label(value: object) -> str:
    if type(value) is not str or not value or value.strip() != value:
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    return value


def _codes(value: object, *, allow_empty_list: bool) -> tuple[str, ...]:
    if type(value) is not list or (not value and not allow_empty_list):
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    if any(type(code) is not str or code == "" for code in value):
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    if len(set(value)) != len(value):
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    return tuple(value)


def _contract(value: object) -> _StudyContract:
    inputs = _mapping(
        value,
        {"study_id", "edition", "country", "country_column", "id_column", "weight_columns", "questions"},
        {"design_columns"},
    )
    study_id = _label(inputs["study_id"])
    edition = _label(inputs["edition"])
    fixed = tuple(_label(inputs[key]) for key in ("country", "country_column", "id_column"))
    if fixed != ("DE", "cntry", "idno"):
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    weights = _mapping(inputs["weight_columns"], {"primary", "sensitivities"})
    if _label(weights["primary"]) != "pspwght":
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    sensitivities = _codes(weights["sensitivities"], allow_empty_list=False)
    if set(sensitivities) != {"dweight", "anweight"}:
        _fail(AdapterErrorCode.INVALID_CONTRACT)

    supplied_questions = inputs["questions"]
    if type(supplied_questions) is not list or not supplied_questions:
        _fail(AdapterErrorCode.INVALID_CONTRACT)
    used_columns = {"cntry", "idno", "pspwght", "dweight", "anweight"}
    question_ids: set[str] = set()
    questions: list[_QuestionContract] = []
    for supplied in supplied_questions:
        question = _mapping(
            supplied,
            {"question_id", "variable", "categoryCodes", "missingCodes", "structurallyNotAskedCodes"},
        )
        question_id = _label(question["question_id"])
        variable = _label(question["variable"])
        if question_id in question_ids or variable in used_columns:
            _fail(AdapterErrorCode.INVALID_CONTRACT)
        question_ids.add(question_id)
        used_columns.add(variable)
        categories = _codes(question["categoryCodes"], allow_empty_list=False)
        not_asked = _codes(question["structurallyNotAskedCodes"], allow_empty_list=True)
        missing = question["missingCodes"]
        if type(missing) is not dict:
            _fail(AdapterErrorCode.INVALID_CONTRACT)
        for code, reason in missing.items():
            if type(code) is not str:
                _fail(AdapterErrorCode.INVALID_CONTRACT)
            _label(reason)
        groups = [set(categories), set(missing), set(not_asked)]
        if any(groups[left] & groups[right] for left, right in ((0, 1), (0, 2), (1, 2))):
            _fail(AdapterErrorCode.INVALID_CONTRACT)
        questions.append(_QuestionContract(question_id, variable, categories, tuple(missing.items()), not_asked))

    design_columns = None
    supplied_design = inputs.get("design_columns")
    if supplied_design is not None:
        design = _mapping(supplied_design, {"psu", "stratum"})
        stratum_column = _label(design["stratum"])
        psu_column = _label(design["psu"])
        if stratum_column in used_columns or psu_column in used_columns or stratum_column == psu_column:
            _fail(AdapterErrorCode.INVALID_CONTRACT)
        design_columns = (stratum_column, psu_column)
    return _StudyContract(study_id, edition, "DE", "cntry", "idno", "pspwght", sensitivities, tuple(questions), design_columns)


def _weight(value: str) -> float:
    try:
        converted = float(value.strip())
    except (ValueError, OverflowError):
        _fail(AdapterErrorCode.INVALID_WEIGHT)
    if not isfinite(converted) or converted <= 0:
        _fail(AdapterErrorCode.INVALID_WEIGHT)
    return converted


def _identifier_present(value: str) -> bool:
    # Check presence without trimming, parsing or rewriting an identifier.
    return bool(value) and any(not character.isspace() for character in value)


def parse_study_csv(csv_text: str, contract: dict) -> PrivateStudyCsv:
    """Validate an in-memory CSV, retaining only selected DE fields privately.

    The contract has explicit question identities and disjoint original valid,
    missing-reason and structurally-unasked code groups. Empty responses require
    an explicit empty-string missing code. All required columns must be present
    exactly once; every row, including non-DE rows, must match the header width.
    Non-DE field contents are otherwise uninterpreted.

    CSV identifiers and responses stay exact strings. Only weight text is
    stripped before conversion to a positive finite float. No data version,
    population filter, rights, question context or full design is verified.
    Design identifiers are only observed metadata: ``se_available`` stays false
    until a later source-specific caller establishes a complete basis and gates.
    """
    selected = _contract(contract)
    if type(csv_text) is not str:
        _fail(AdapterErrorCode.INVALID_TEXT)
    records: list[_PrivateDERecord] = []
    seen_ids: set[str] = set()
    observed_pairs: set[tuple[str, str]] = set()
    incomplete_design = False
    counts = [[0, 0, 0] for _ in selected._questions]
    weight_columns = (selected._primary_weight, *selected._sensitivity_weights)
    required = {selected._country_column, selected._id_column, *weight_columns}
    required.update(question._variable for question in selected._questions)
    if selected._design_columns is not None:
        required.update(selected._design_columns)
    category_sets = [set(question._category_codes) for question in selected._questions]
    missing_maps = [dict(question._missing_codes) for question in selected._questions]
    not_asked_sets = [set(question._not_asked_codes) for question in selected._questions]

    with StringIO(csv_text, newline="") as stream:
        reader = csv.reader(stream, strict=True)
        try:
            try:
                header = next(reader)
            except StopIteration:
                _fail(AdapterErrorCode.EMPTY_CSV)
            if not header or any(not _identifier_present(name) for name in header):
                _fail(AdapterErrorCode.EMPTY_HEADER)
            if len(set(header)) != len(header):
                _fail(AdapterErrorCode.DUPLICATE_HEADER)
            if not required <= set(header):
                _fail(AdapterErrorCode.MISSING_REQUIRED_COLUMN)
            indices = {column: index for index, column in enumerate(header)}
            for cells in reader:
                if len(cells) != len(header):
                    _fail(AdapterErrorCode.INVALID_ROW_WIDTH)
                if cells[indices[selected._country_column]] != selected._country:
                    continue
                identity = cells[indices[selected._id_column]]
                if not _identifier_present(identity):
                    _fail(AdapterErrorCode.INVALID_DE_ID)
                if identity in seen_ids:
                    _fail(AdapterErrorCode.DUPLICATE_DE_ID)
                seen_ids.add(identity)
                weights = tuple((column, _weight(cells[indices[column]])) for column in weight_columns)
                answers: list[_PrivateAnswer] = []
                for index, question in enumerate(selected._questions):
                    raw = cells[indices[question._variable]]
                    if raw in category_sets[index]:
                        answers.append(_PrivateAnswer(raw, raw, True, False, None))
                        counts[index][0] += 1
                    elif raw in missing_maps[index]:
                        answers.append(_PrivateAnswer(raw, None, True, True, missing_maps[index][raw]))
                        counts[index][1] += 1
                    elif raw in not_asked_sets[index]:
                        answers.append(_PrivateAnswer(raw, None, False, False, None))
                        counts[index][2] += 1
                    else:
                        _fail(AdapterErrorCode.UNKNOWN_DE_CODE)
                design_identifiers = None
                if selected._design_columns is not None:
                    stratum_column, psu_column = selected._design_columns
                    stratum = cells[indices[stratum_column]]
                    psu = cells[indices[psu_column]]
                    if _identifier_present(stratum) and _identifier_present(psu):
                        design_identifiers = _PrivateDesignIdentifiers(stratum, psu)
                        observed_pairs.add((stratum, psu))
                    else:
                        incomplete_design = True
                records.append(_PrivateDERecord(identity, weights, tuple(answers), design_identifiers))
        except csv.Error:
            _fail(AdapterErrorCode.INVALID_CSV)
    if not records:
        _fail(AdapterErrorCode.NO_DE_ROWS)
    if selected._design_columns is None:
        status = AdapterDesignStatus.NO_DESIGN_DECLARED
    elif incomplete_design:
        status = AdapterDesignStatus.INCOMPLETE_IDENTIFIERS
    else:
        status = AdapterDesignStatus.IDENTIFIERS_COMPLETE_UNVERIFIED_BASIS
    diagnostics = AdapterDiagnostics(
        de_row_count=len(records),
        question_counts=tuple(QuestionCounts(*question_counts) for question_counts in counts),
        design=AdapterDesignDiagnostics(
            status=status,
            identifiers_complete=selected._design_columns is not None and not incomplete_design,
            se_available=False,
            observed_strata_count=len({stratum for stratum, _ in observed_pairs}),
            observed_psu_count=len(observed_pairs),
        ),
    )
    return PrivateStudyCsv(selected, tuple(records), diagnostics)
