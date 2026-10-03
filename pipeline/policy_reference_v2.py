"""WIP arithmetic for one study and one categorical question at a time.

This module does not read files, select questions/categories, reconstruct survey
designs, or establish the suitability of a population reference.  Callers must
justify source-specific weights, eligibility, missingness and design before an
empirical use.  A ``None`` response is an explicit absent-response marker, never
a valid category or an inferred political midpoint.

Optional uncertainty is the with-replacement Taylor variance of a ratio using
the complete caller-supplied stratum/PSU basis.  It has no FPC or confidence
interval interpretation.  A missing design or a singleton stratum yields no SE.
"""

from dataclasses import dataclass
from enum import Enum
from math import fsum, isfinite, sqrt
from numbers import Real
from typing import Iterable


Code = str | int | float


class VarianceStatus(str, Enum):
    COMPUTED_WRT_TAYLOR = "computed_wrt_taylor"
    NO_DESIGN_BASIS = "no_design_basis"
    INCOMPLETE_DESIGN_IDENTIFIERS = "incomplete_design_identifiers"
    SINGLETON_STRATUM = "singleton_stratum"
    NO_VALID_RESPONSES = "no_valid_responses"


@dataclass(frozen=True, slots=True)
class DesignUnit:
    stratum: Code
    psu: Code


@dataclass(frozen=True, slots=True)
class Observation:
    response: Code | None
    weight: Real
    eligible: bool
    missing: bool
    design: DesignUnit | None = None


@dataclass(frozen=True, slots=True)
class Accounting:
    total_count: int
    total_weight: float
    eligible_count: int
    eligible_weight: float
    valid_count: int
    valid_weight: float
    missing_count: int
    missing_weight: float
    not_asked_count: int
    not_asked_weight: float


@dataclass(frozen=True, slots=True)
class CategoryEstimate:
    category: Code
    count: int
    weight: float
    proportion: float | None
    variance: float | None
    standard_error: float | None


@dataclass(frozen=True, slots=True)
class DesignSummary:
    # Every supplied PSU survives, including PSUs with no supplied observations.
    basis: tuple[DesignUnit, ...]
    stratum_psu_counts: tuple[tuple[Code, int], ...]
    singleton_strata: tuple[Code, ...]
    observations_without_design: int


@dataclass(frozen=True, slots=True)
class CategoricalReference:
    study_id: str
    question_id: str
    accounting: Accounting
    estimates: tuple[CategoryEstimate, ...]
    variance_status: VarianceStatus
    design: DesignSummary | None


def _validate_code(code: object, label: str) -> None:
    if isinstance(code, bool) or not isinstance(code, (str, int, float)):
        raise ValueError(f"{label} must be a string or finite numeric code")
    if isinstance(code, float) and not isfinite(code):
        raise ValueError(f"{label} must be finite")


def _validate_unit(unit: DesignUnit) -> None:
    if not isinstance(unit, DesignUnit):
        raise ValueError("design identifiers must be DesignUnit instances")
    _validate_code(unit.stratum, "stratum")
    _validate_code(unit.psu, "PSU")


def _positive_weight(weight: Real) -> float:
    if isinstance(weight, bool) or not isinstance(weight, Real):
        raise ValueError("weight must be a positive finite real number")
    try:
        converted = float(weight)
    except (OverflowError, ValueError) as exc:
        raise ValueError("weight must be representable as a finite float") from exc
    if not isfinite(converted) or converted <= 0:
        raise ValueError("weight must be a positive finite real number")
    return converted


def _finite_sum(values: Iterable[float]) -> float:
    try:
        total = fsum(values)
    except OverflowError as exc:
        raise ValueError("weight total must be representable as a finite float") from exc
    if not isfinite(total):
        raise ValueError("weight total must be representable as a finite float")
    return total


def categorical_reference(
    *,
    study_id: str,
    question_id: str,
    categories: Iterable[Code],
    observations: Iterable[Observation],
    design_basis: Iterable[DesignUnit] | None = None,
) -> CategoricalReference:
    """Calculate weighted category shares with an explicit valid denominator.

    ``categories`` contains caller-specified original valid codes, in output
    order.  Missing/structurally unasked responses must have ``response=None``.
    Eligible missing observations require ``missing=True``; ineligible
    observations require ``missing=False``.  Contradictory flags and unexpected
    codes raise ``ValueError``.  Weights must be positive and finite for all
    observations, including missing and unasked ones.  Totals must fit a float.

    The API is intentionally limited to one supplied study/question label per
    call.  It cannot verify the provenance of supplied records.  It offers no
    combined-study reference, person linkage, factor, overall score, percentile,
    interval or personal uncertainty.

    A provided ``design_basis`` must list unique stratum/PSU pairs from the full
    survey design, not only the selected domain.  Every supplied observation
    needs a pair for a variance estimate, even when missing or ineligible.  A
    pair outside the supplied basis is an error.  A missing pair yields an
    incomplete-design status.  Observation pairs without a design basis do not
    cause this function to reconstruct one.
    """
    for label, identifier in (("study_id", study_id), ("question_id", question_id)):
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError(f"{label} must be a nonempty string")

    category_order = tuple(categories)
    if not category_order:
        raise ValueError("categories must contain at least one original valid code")
    for code in category_order:
        _validate_code(code, "category")
    if len(set(category_order)) != len(category_order):
        raise ValueError("categories must be unique")
    valid_codes = set(category_order)

    basis = None if design_basis is None else tuple(design_basis)
    strata: dict[Code, list[DesignUnit]] = {}
    if basis is not None:
        if not basis:
            raise ValueError("a supplied design basis must contain at least one PSU")
        for unit in basis:
            _validate_unit(unit)
            strata.setdefault(unit.stratum, []).append(unit)
        if len(set(basis)) != len(basis):
            raise ValueError("design basis must contain unique stratum/PSU pairs")
    basis_set = None if basis is None else set(basis)

    normalized: list[Observation] = []
    for row in observations:
        if not isinstance(row, Observation):
            raise ValueError("observations must be Observation instances")
        if type(row.eligible) is not bool or type(row.missing) is not bool:
            raise ValueError("eligibility and missingness must be explicit booleans")
        weight = _positive_weight(row.weight)
        if row.response is not None:
            _validate_code(row.response, "response")
            if row.response not in valid_codes:
                raise ValueError(f"unexpected response code: {row.response!r}")
        if not row.eligible:
            if row.response is not None or row.missing:
                raise ValueError("an unasked observation must have no response and missing=False")
        elif row.missing:
            if row.response is not None:
                raise ValueError("an explicitly missing response must be None")
        elif row.response is None:
            raise ValueError("an eligible absent response requires missing=True")
        if row.design is not None:
            _validate_unit(row.design)
            if basis_set is not None and row.design not in basis_set:
                raise ValueError("observation design pair is outside the supplied full basis")
        normalized.append(Observation(row.response, weight, row.eligible, row.missing, row.design))

    eligible = [row for row in normalized if row.eligible]
    valid = [row for row in eligible if not row.missing]
    missing = [row for row in eligible if row.missing]
    not_asked = [row for row in normalized if not row.eligible]
    total_weight = _finite_sum(row.weight for row in normalized)
    valid_weight = _finite_sum(row.weight for row in valid)
    accounting = Accounting(
        total_count=len(normalized),
        total_weight=total_weight,
        eligible_count=len(eligible),
        eligible_weight=_finite_sum(row.weight for row in eligible),
        valid_count=len(valid),
        valid_weight=valid_weight,
        missing_count=len(missing),
        missing_weight=_finite_sum(row.weight for row in missing),
        not_asked_count=len(not_asked),
        not_asked_weight=_finite_sum(row.weight for row in not_asked),
    )

    missing_design_count = sum(row.design is None for row in normalized)
    singleton_strata = tuple(label for label, units in strata.items() if len(units) == 1)
    design = None if basis is None else DesignSummary(
        basis=basis,
        stratum_psu_counts=tuple((label, len(units)) for label, units in strata.items()),
        singleton_strata=singleton_strata,
        observations_without_design=missing_design_count,
    )
    if not valid:
        status = VarianceStatus.NO_VALID_RESPONSES
    elif basis is None:
        status = VarianceStatus.NO_DESIGN_BASIS
    elif missing_design_count:
        status = VarianceStatus.INCOMPLETE_DESIGN_IDENTIFIERS
    elif singleton_strata:
        status = VarianceStatus.SINGLETON_STRATUM
    else:
        status = VarianceStatus.COMPUTED_WRT_TAYLOR

    estimates: list[CategoryEstimate] = []
    for code in category_order:
        category_rows = [row for row in valid if row.response == code]
        category_weight = _finite_sum(row.weight for row in category_rows)
        proportion = None if not valid else category_weight / valid_weight
        variance = None
        if status is VarianceStatus.COMPUTED_WRT_TAYLOR:
            assert basis is not None and proportion is not None
            # Initialize from the full basis, preserving zero-contributing PSUs.
            residuals: dict[DesignUnit, list[float]] = {unit: [] for unit in basis}
            for row in valid:
                assert row.design is not None
                indicator = 1.0 if row.response == code else 0.0
                residuals[row.design].append(row.weight * (indicator - proportion))
            linearized = {
                unit: fsum(contributions) / valid_weight
                for unit, contributions in residuals.items()
            }
            stratum_variances = []
            for units in strata.values():
                psu_count = len(units)
                mean = fsum(linearized[unit] for unit in units) / psu_count
                squared_deviations = fsum((linearized[unit] - mean) ** 2 for unit in units)
                stratum_variances.append(psu_count / (psu_count - 1) * squared_deviations)
            variance = fsum(stratum_variances)
        estimates.append(CategoryEstimate(
            category=code,
            count=len(category_rows),
            weight=category_weight,
            proportion=proportion,
            variance=variance,
            standard_error=None if variance is None else sqrt(variance),
        ))
    return CategoricalReference(study_id, question_id, accounting, tuple(estimates), status, design)
