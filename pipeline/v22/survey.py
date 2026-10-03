"""Design-based uncertainty for weighted category shares (Analyseplan v2.2).

Standard library only. Pure functions without file access.

Estimator: p_c = sum(w * 1[y = c]) / sum(w) over valid answers of one question
in one domain (all respondents, or one historical vote group).

Variance: first-order Taylor linearisation of the ratio with a with-replacement
first-stage approximation. Weights are treated as fixed; post-stratification is
not modelled. All PSUs of the complete German design enter the sum, including
PSUs without valid answers in the domain (zero contributions).

    z_i  = w_i * (1[y_i = c] - p_c) / W        for valid answers in the domain, else 0
    z_hj = sum of z_i in PSU j of stratum h
    v(p) = sum_h n_h / (n_h - 1) * sum_j (z_hj - mean_h(z))^2

Interval: "xlogit" in the R survey manual 4.5 (svyciprop, PDF p. 93-94): logit of
the estimate, delta-method standard error, t quantile with design degrees of
freedom (#PSU - #strata), back-transformed. Not defined for p = 0 or p = 1.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, fsum, isfinite, lgamma, log, sqrt
from typing import Hashable, Sequence


@dataclass(frozen=True)
class Unit:
    """One respondent of the complete German sample."""

    weight: float
    stratum: Hashable
    psu: Hashable
    in_domain: bool
    response: Hashable | None  # valid category code, or None if no valid answer


@dataclass(frozen=True)
class ShareEstimate:
    category: Hashable
    share: float
    standard_error: float | None
    lower: float | None
    upper: float | None


@dataclass(frozen=True)
class DesignSummary:
    strata: int
    psus: int
    degrees_of_freedom: int
    singleton_strata: int


class DesignError(ValueError):
    pass


def design_summary(units: Sequence[Unit]) -> DesignSummary:
    strata: dict[Hashable, set[Hashable]] = {}
    for unit in units:
        strata.setdefault(unit.stratum, set()).add((unit.stratum, unit.psu))
    psus = sum(len(members) for members in strata.values())
    singletons = sum(1 for members in strata.values() if len(members) == 1)
    return DesignSummary(len(strata), psus, psus - len(strata), singletons)


def _check(units: Sequence[Unit]) -> None:
    if not units:
        raise DesignError('empty design')
    for unit in units:
        if not (isfinite(unit.weight) and unit.weight > 0):
            raise DesignError('weights must be positive and finite')
        if unit.response is not None and not unit.in_domain:
            raise DesignError('a response outside the domain must be None')


def weighted_shares(units: Sequence[Unit], categories: Sequence[Hashable]) -> dict[Hashable, float]:
    valid = [u for u in units if u.in_domain and u.response is not None]
    total = fsum(u.weight for u in valid)
    if total <= 0:
        raise DesignError('no valid answers in the domain')
    unknown = {u.response for u in valid} - set(categories)
    if unknown:
        raise DesignError('unexpected category code')
    return {c: fsum(u.weight for u in valid if u.response == c) / total for c in categories}


def taylor_variance(units: Sequence[Unit], category: Hashable, share: float) -> float:
    valid_total = fsum(u.weight for u in units if u.in_domain and u.response is not None)
    contributions: dict[tuple[Hashable, Hashable], list[float]] = {}
    strata: dict[Hashable, set[tuple[Hashable, Hashable]]] = {}
    for unit in units:
        key = (unit.stratum, unit.psu)
        strata.setdefault(unit.stratum, set()).add(key)
        values = contributions.setdefault(key, [])
        if unit.in_domain and unit.response is not None:
            indicator = 1.0 if unit.response == category else 0.0
            values.append(unit.weight / valid_total * (indicator - share))
    total = []
    for members in strata.values():
        n = len(members)
        if n < 2:
            raise DesignError('singleton stratum')
        sums = [fsum(contributions[key]) for key in members]
        mean = fsum(sums) / n
        total.append(n / (n - 1) * fsum((value - mean) ** 2 for value in sums))
    return fsum(total)


def _betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for the regularised incomplete beta function."""
    tiny = 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 400):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c if abs(1.0 + aa / c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c if abs(1.0 + aa / c) > tiny else tiny
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            return h
    raise ArithmeticError('incomplete beta did not converge')


def _betainc(a: float, b: float, x: float) -> float:
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    front = exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * log(x) + b * log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def t_cdf(t: float, df: int) -> float:
    x = df / (df + t * t)
    tail = 0.5 * _betainc(df / 2.0, 0.5, x)
    return 1.0 - tail if t > 0 else tail


def t_quantile(probability: float, df: int) -> float:
    """Quantile of Student's t by bisection; probability in (0.5, 1)."""
    if not 0.5 < probability < 1 or df < 1:
        raise ValueError('unsupported quantile request')
    low, high = 0.0, 1000.0
    for _ in range(200):
        middle = (low + high) / 2.0
        if t_cdf(middle, df) < probability:
            low = middle
        else:
            high = middle
    return (low + high) / 2.0


def logit_interval(share: float, standard_error: float, df: int, level: float = 0.95):
    """xlogit interval; None at the boundaries where it is undefined."""
    if not 0.0 < share < 1.0:
        return None
    q = t_quantile(1.0 - (1.0 - level) / 2.0, df)
    centre = log(share / (1.0 - share))
    half = q * standard_error / (share * (1.0 - share))

    def expit(value: float) -> float:
        return 1.0 / (1.0 + exp(-value))

    return expit(centre - half), expit(centre + half)


def estimate(units: Sequence[Unit], categories: Sequence[Hashable], level: float = 0.95,
             min_df: int = 20) -> tuple[list[ShareEstimate], DesignSummary]:
    """Shares with design-based standard errors and xlogit intervals."""
    _check(units)
    summary = design_summary(units)
    shares = weighted_shares(units, categories)
    if summary.singleton_strata:
        raise DesignError('singleton stratum')
    results = []
    for category in categories:
        share = shares[category]
        variance = taylor_variance(units, category, share)
        se = sqrt(max(variance, 0.0))
        interval = None
        if summary.degrees_of_freedom >= min_df:
            interval = logit_interval(share, se, summary.degrees_of_freedom, level)
        results.append(ShareEstimate(category, share, se,
                                     None if interval is None else interval[0],
                                     None if interval is None else interval[1]))
    return results, summary

