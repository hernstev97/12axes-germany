"""SYNTHETIC ONLY: bounded ordinal scores, clusters, and joint linearisation.

No input files, ESS variables, item words, or real observations are accepted.
This script calibrates examples. It does not validate an ESS method or model.
Run from the repository root with Python and the already available NumPy.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import statistics
import sys
from pathlib import Path

import numpy as np


SEED = 2026100302
REPETITIONS = 1000
STRATA = 8
PSUS_PER_STRATUM = 10
OBSERVATIONS_PER_PSU = 20
THRESHOLDS = np.array([-1.0, -0.3, 0.3, 1.0])
GROUP_SHIFT = 0.2
Z_975 = statistics.NormalDist().inv_cdf(0.975)


def population_mean(shift: float) -> float:
    normal = statistics.NormalDist()
    return sum(1.0 - normal.cdf(float(t) - shift) for t in THRESHOLDS) / 4.0


def ratio_vector_and_covariance(scores: np.ndarray, weights: np.ndarray):
    """WR ultimate-PSU Taylor approximation, keeping all strata and PSUs.

    Targets: all-score mean, domain-0 mean, domain-1 mean, fixed-score
    midrank CDF at 0.5. The same cluster contributions give joint covariance.
    """
    shape = scores.shape
    groups = np.broadcast_to(np.arange(shape[2]) % 2, shape)
    denominators = np.stack(
        [np.ones(shape), groups == 0, groups == 1, np.ones(shape)], axis=-1
    ).astype(float)
    midrank = (scores < 0.5).astype(float) + 0.5 * (scores == 0.5)
    numerators = denominators * np.stack(
        [scores, scores, scores, midrank], axis=-1
    )
    totals_b = (weights[..., None] * denominators).sum(axis=(0, 1, 2))
    estimate = (weights[..., None] * numerators).sum(axis=(0, 1, 2)) / totals_b
    influence = weights[..., None] * (
        numerators - estimate * denominators
    ) / totals_b
    psu_contributions = influence.sum(axis=2)
    centered = psu_contributions - psu_contributions.mean(axis=1, keepdims=True)
    covariance = np.einsum("hmi,hmj->ij", centered, centered)
    covariance *= shape[1] / (shape[1] - 1)
    return estimate, covariance


def synthetic_scenario(icc: float, weight_cv: float, seed: int):
    rng = np.random.default_rng(seed)
    shape = (STRATA, PSUS_PER_STRATUM, OBSERVATIONS_PER_PSU)
    groups = np.broadcast_to(np.arange(shape[2]) % 2, shape)
    truth0, truth1 = population_mean(0.0), population_mean(GROUP_SHIFT)
    truth = (truth0 + truth1) / 2.0
    estimates, row_pairs, cluster_pairs = [], [], []
    variances, contrast_variances, diagonal_variances = [], [], []
    matrices = []
    coverage_normal = []
    for _ in range(REPETITIONS):
        cluster_effect = rng.normal(size=shape[:2])[..., None]
        latent = (
            math.sqrt(icc) * cluster_effect
            + math.sqrt(1.0 - icc) * rng.normal(size=shape)
            + GROUP_SHIFT * groups
        )
        scores = np.searchsorted(THRESHOLDS, latent, side="right") / 4.0
        sigma = math.sqrt(math.log(1.0 + weight_cv**2))
        weights = np.exp(sigma * rng.normal(size=shape) - sigma**2 / 2.0)
        estimate, covariance = ratio_vector_and_covariance(scores, weights)
        estimates.append(estimate[0])
        variances.append(covariance[0, 0])
        contrast_variances.append(
            covariance[1, 1] + covariance[2, 2] - 2.0 * covariance[1, 2]
        )
        diagonal_variances.append(covariance[1, 1] + covariance[2, 2])
        matrices.append(covariance)
        coverage_normal.append(
            abs(estimate[0] - truth) <= Z_975 * math.sqrt(covariance[0, 0])
        )
        row_a = np.zeros(shape, dtype=bool)
        for h in range(STRATA):
            for p in range(PSUS_PER_STRATUM):
                row_a[h, p, rng.permutation(OBSERVATIONS_PER_PSU)[:10]] = True
        cluster_a = np.zeros(shape, dtype=bool)
        for h in range(STRATA):
            cluster_a[h, rng.permutation(PSUS_PER_STRATUM)[:5], :] = True
        for mask, target in [(row_a, row_pairs), (cluster_a, cluster_pairs)]:
            target.append(
                [
                    float(np.sum(weights[mask] * scores[mask]) / weights[mask].sum()),
                    float(np.sum(weights[~mask] * scores[~mask]) / weights[~mask].sum()),
                ]
            )
    empirical_variance = float(np.var(estimates, ddof=1))
    return {
        "latent_cluster_variance_fraction": icc,
        "independent_weight_cv": weight_cv,
        "population_observed_mean": truth,
        "mean_estimate": float(np.mean(estimates)),
        "empirical_variance": empirical_variance,
        "mean_linearised_variance": float(np.mean(variances)),
        "linearised_to_empirical_variance_ratio": float(np.mean(variances)) / empirical_variance,
        "asymptotic_normal_interval_coverage": float(np.mean(coverage_normal)),
        "coverage_mc_standard_error": math.sqrt(0.95 * 0.05 / REPETITIONS),
        "row_split_shared_psu_fraction": 1.0,
        "whole_psu_split_shared_psu_fraction": 0.0,
        "row_split_means_correlation_across_samples": float(np.corrcoef(np.array(row_pairs).T)[0, 1]),
        "whole_psu_split_means_correlation_across_samples": float(np.corrcoef(np.array(cluster_pairs).T)[0, 1]),
        "mean_joint_covariance": np.mean(matrices, axis=0).tolist(),
        "joint_covariance_order": ["all_mean", "domain_0_mean", "domain_1_mean", "midrank_cdf_at_0_5"],
        "mean_domain_difference_variance_joint": float(np.mean(contrast_variances)),
        "mean_domain_difference_variance_diagonal_only": float(np.mean(diagonal_variances)),
        "diagonal_only_to_joint_contrast_variance_ratio": float(np.mean(diagonal_variances)) / float(np.mean(contrast_variances)),
    }


def main():
    if len(sys.argv) != 1:
        raise SystemExit("Synthetic-only script accepts no arguments or input paths.")
    scenarios = [
        synthetic_scenario(icc, cv, SEED + 10 * i + j)
        for i, icc in enumerate([0.0, 0.25, 0.5])
        for j, cv in enumerate([0.0, 1.0])
    ]
    # Deterministic examples; these are numerical pseudoitems, not questions.
    profiles = np.array([[0.0, 0.5, 0.5], [1.0, 0.5, 0.5]])
    full = profiles.mean(axis=1)
    variances = np.var(profiles, axis=0)
    covariance_with_sum = ((profiles - profiles.mean(axis=0)) * (full - full.mean())[:, None]).mean(axis=0)
    share = covariance_with_sum / 3.0 / np.var(full)
    assert np.allclose(share, [1.0, 0.0, 0.0])
    assert abs(population_mean(0.0) - 0.5) < 1e-12
    assert all(s["mean_domain_difference_variance_joint"] > 0 for s in scenarios)
    # Ratios and their Taylor covariance must be invariant to common weight scaling.
    probe = np.arange(8 * 4 * 6).reshape(8, 4, 6) % 5 / 4.0
    probe_weights = 1.0 + np.arange(probe.size).reshape(probe.shape) % 3
    estimate_a, covariance_a = ratio_vector_and_covariance(probe, probe_weights)
    estimate_b, covariance_b = ratio_vector_and_covariance(probe, 7.0 * probe_weights)
    assert np.allclose(estimate_a, estimate_b)
    assert np.allclose(covariance_a, covariance_b)
    assert np.linalg.eigvalsh(covariance_a).min() >= -1e-12
    result = {
        "status": "SYNTHETIC_CALIBRATION_ONLY",
        "uses_real_ess_data": False,
        "seed": SEED,
        "rng": "NumPy default_rng / PCG64",
        "repetitions_per_scenario": REPETITIONS,
        "environment": {"python": platform.python_version(), "numpy": np.__version__},
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scenario_design": {
            "strata": STRATA,
            "psus_per_stratum": PSUS_PER_STRATUM,
            "observations_per_psu": OBSERVATIONS_PER_PSU,
            "independent_symmetric_normal_cluster_and_individual_terms": True,
            "ordinal_category_scores": [0.0, 0.25, 0.5, 0.75, 1.0],
            "thresholds": THRESHOLDS.tolist(),
            "domain_latent_shift": GROUP_SHIFT,
            "weights_independent_of_latent_values": True,
            "pps_sampling_or_nonresponse_calibration": False,
            "normal_instead_of_t_interval": True,
        },
        "scenarios": scenarios,
        "bounded_score_precision_planning": {
            "basis": "Own worst-case variance bound Var(S)<=1/4; normal approximation, not design guarantee",
            "target_95_percent_half_width": 0.05,
            "required_srs_effective_n_ceiling": math.ceil((Z_975 * 0.5 / 0.05) ** 2),
            "half_width_at_n_50": Z_975 * 0.5 / math.sqrt(50),
        },
        "equal_weight_dominance_example": {
            "synthetic_item_variances": variances.tolist(),
            "contribution_shares": share.tolist(),
            "maximum_leave_one_out_score_change": float(np.max(np.abs(full - profiles[:, 1:].mean(axis=1)))),
        },
        "same_count_different_masks_example": {
            "synthetic_profile": [0.0, 1.0],
            "mask_a": [0], "mask_b": [1], "answer_count_each": 1,
            "subset_scores": [0.0, 1.0],
        },
        "limits": [
            "No ordinal EFA/CFA, invariance, reliability, or personal-error-model fit was run.",
            "No empirical precision, threshold, item mask, or design validity for ESS was established.",
            "The bootstrap/PPS and post-stratification problems are not solved by this experiment.",
            "Correlations across repeated synthetic samples are scenario-dependent; whole-PSU allocation is not a universal independence proof.",
        ],
    }
    out = Path("reports/loop/synthetic/LOOP-002-methoden-kalibrierung.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"artifact": str(out), "sha256": hashlib.sha256(out.read_bytes()).hexdigest(), "status": result["status"]}))


if __name__ == "__main__":
    main()
