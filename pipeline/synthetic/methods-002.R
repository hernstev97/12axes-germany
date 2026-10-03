#!/usr/bin/env Rscript
# New invented complete responses only. No ESS data or installed library edits.
options(warn = 1, digits = 16)
args <- commandArgs(trailingOnly = TRUE)
stopifnot(length(args) == 3L)
project <- normalizePath(args[[1]], mustWork = TRUE)
own <- normalizePath(args[[2]], mustWork = TRUE)
stopifnot(identical(own, file.path(project, 'outputs/loop/methods002')))
suppressPackageStartupMessages(library(lavaan))
suppressPackageStartupMessages(library(jsonlite))
stopifnot(as.character(packageVersion('lavaan')) == '0.7.2')
warnings_seen <- character()
record <- list(package = 'METHODS-002', scope = 'Synthetic interface feasibility only',
               seed = 2026100307L, criteria = 'reports/loop/METHODS-002-vorabplan.md')
checks <- list()
check <- function(id, actual, expected = TRUE, detail = NULL) {
  ok <- isTRUE(actual == expected)
  checks[[id]] <<- list(status = if (ok) 'BESTANDEN' else 'NICHT_BESTANDEN',
                       observed = actual, expected = expected, detail = detail)
  cat(id, checks[[id]]$status, '\n')
}
maxdiff <- function(a, b) max(abs(as.numeric(a) - as.numeric(b)))
stratified_cov <- function(psi, clusters, strata) {
  stopifnot(is.matrix(psi), all(is.finite(psi)), length(clusters) == nrow(psi),
            length(strata) == nrow(psi), !anyNA(clusters), !anyNA(strata))
  mapping <- split(strata, clusters)
  if (any(vapply(mapping, function(x) length(unique(x)) != 1L, logical(1))))
    stop('Cluster belongs to more than one stratum')
  totals <- rowsum(psi, clusters, reorder = FALSE)
  cluster_strata <- strata[match(rownames(totals), clusters)]
  result <- matrix(0, ncol(psi), ncol(psi))
  for (h in unique(cluster_strata)) {
    block <- totals[cluster_strata == h, , drop = FALSE]
    g <- nrow(block)
    if (g < 2L) stop('Singleton stratum has no authorized variance rule')
    centered <- sweep(block, 2L, colMeans(block))
    result <- result + g / (g - 1L) * crossprod(centered)
  }
  result
}
run <- function() {
  RNGkind('Mersenne-Twister', 'Inversion', 'Rejection')
  set.seed(record$seed)
  n <- 1440L; g <- 96L
  clusters <- rep(sprintf('C%03d', seq_len(g)), each = 15L)
  strata <- rep(rep(sprintf('H%d', 1:4), each = 24L), each = 15L)
  latent <- rep(rnorm(g, sd = 0.5), each = 15L) + rnorm(n, sd = sqrt(0.75))
  items <- paste0('y', 1:4)
  dat <- as.data.frame(setNames(lapply(c(0.65, 0.70, 0.75, 0.80), function(l) {
    z <- l * latent + rnorm(n, sd = sqrt(1 - l * l))
    as.integer(cut(z, c(-Inf, -1.2, -0.4, 0.4, 1.2, Inf), labels = FALSE))
  }), items))
  dat$w <- runif(n, 0.5, 1.5)
  dat$cluster <- clusters
  model <- 'f =~ y1 + y2 + y3 + y4'
  base <- list(model = model, data = dat, ordered = items, estimator = 'WLSMV',
               parameterization = 'theta', std_lv = TRUE, sampling_weights = 'w',
               sampling_weights_type = 'design', sampling_weights_normalization = 'group')
  native <- do.call(lavaan::cfa, c(base, list(cluster = 'cluster')))
  wt <- dat$w * n / sum(dat$w)
  m84 <- getFromNamespace('muthen1984', 'lavaan')
  inverse_b <- getFromNamespace('lav_m84_b_inv', 'lavaan')
  moments <- function(weights) m84(data_1 = as.matrix(dat[items]), ov_names = items,
                                  ov_types = rep('ordered', 4), ov_levels = rep(5L, 4),
                                  wt = weights, sampling_weights_type = 'design',
                                  cluster_idx = as.integer(factor(clusters)))
  transform <- function(m) {
    b <- inverse_b(a11 = m$A11, a21 = m$A21, a22 = m$A22)
    if (b$ginv_a11 || b$ginv_a22) stop('Generalized inverse: not authorized by this trial')
    m$SC %*% t(b$b_inv) %*% t(m$H)
  }
  m <- moments(wt)
  psi <- transform(m)
  psu <- rowsum(psi, clusters, reorder = FALSE)
  gamma_native <- n * g / (g - 1) * crossprod(psu)
  native_difference <- maxdiff(gamma_native, lavInspect(native, 'gamma'))
  check('full_native_gamma', native_difference <= 1e-7, detail = native_difference)
  covariance <- stratified_cov(psi, clusters, strata)
  gamma_stratified <- n * covariance
  labels <- names(lavInspect(native, 'wls.obs'))
  dimnames(gamma_stratified) <- list(labels, labels)
  dimnames(gamma_native) <- list(labels, labels)
  check('finite_dimension', identical(dim(gamma_stratified), c(22L, 22L)) &&
          all(is.finite(gamma_stratified)))
  check('symmetry', maxdiff(gamma_stratified, t(gamma_stratified)) <= 1e-7)
  # Separately expressed marginal probability/delta contributions for all thresholds.
  oracle <- do.call(cbind, lapply(items, function(item) do.call(cbind, lapply(1:4, function(k) {
    indicator <- as.numeric(dat[[item]] <= k)
    probability <- sum(dat$w * indicator) / sum(dat$w)
    dat$w * (indicator - probability) / (sum(dat$w) * dnorm(qnorm(probability)))
  }))))
  # Separate explicit per-stratum, per-cluster loops; not the candidate aggregator.
  oracle_cov <- matrix(0, 16L, 16L)
  for (h in unique(strata)) {
    cs <- unique(clusters[strata == h])
    totals <- t(vapply(cs, function(c) colSums(oracle[clusters == c, , drop = FALSE]), numeric(16L)))
    total_sum <- colSums(totals)
    outer_sum <- matrix(0, 16L, 16L)
    for (row in seq_len(nrow(totals))) outer_sum <- outer_sum + tcrossprod(totals[row, ])
    oracle_cov <- oracle_cov + length(cs) / (length(cs) - 1) *
      (outer_sum - tcrossprod(total_sum) / length(cs))
  }
  threshold_difference <- maxdiff(covariance[1:16, 1:16], oracle_cov)
  check('threshold_covariance_oracle', threshold_difference <= 1e-7, detail = threshold_difference)
  observed_thresholds <- lavInspect(native, 'th')
  expected_thresholds <- unlist(lapply(items, function(item) vapply(1:4, function(k)
    qnorm(sum(dat$w * (dat[[item]] <= k)) / sum(dat$w)), numeric(1))))
  check('all_weighted_thresholds', maxdiff(observed_thresholds, expected_thresholds) <= 1e-7,
        detail = maxdiff(observed_thresholds, expected_thresholds))
  external <- function(gamma) do.call(lavaan::cfa, c(base, list(nacov = gamma,
                                     wls_v = native@SampleStats@WLS.V[[1L]])))
  fit_native_input <- external(gamma_native)
  fit_stratified <- external(gamma_stratified)
  check('external_native_gamma_import', maxdiff(lavInspect(fit_native_input, 'gamma'), gamma_native) <= 1e-7)
  check('external_stratified_gamma_import', maxdiff(lavInspect(fit_stratified, 'gamma'), gamma_stratified) <= 1e-7)
  point_difference <- maxdiff(coef(native), coef(fit_stratified))
  check('same_dwls_point_estimates', point_difference <= 1e-7, detail = point_difference)
  # Sorted first-item cluster means creates a second fixed alternative partition.
  # It is an adversarial synthetic check, never a permissible empirical design reconstruction.
  cluster_means <- rowsum(dat$y1, clusters, reorder = FALSE)[, 1L] / 15
  rank_h <- rep(1:4, each = 24L)[order(order(cluster_means))]
  changed_h <- sprintf('S%d', rank_h[match(clusters, names(cluster_means))])
  changed_gamma <- n * stratified_cov(psi, clusters, changed_h)
  changed_difference <- maxdiff(changed_gamma, gamma_stratified)
  check('stratum_change_changes_covariance', changed_difference > 1e-7, detail = changed_difference)
  changed_fit <- external(changed_gamma)
  check('stratum_change_keeps_points', maxdiff(coef(changed_fit), coef(fit_stratified)) <= 1e-7)
  renamed_gamma <- n * stratified_cov(psi, paste0('renamed_', clusters), paste0('renamed_', strata))
  check('renaming_invariant', maxdiff(renamed_gamma, gamma_stratified) <= 1e-7)
  scaled_psi <- transform(moments((7 * dat$w) * n / sum(7 * dat$w)))
  scaled_gamma <- n * stratified_cov(scaled_psi, clusters, strata)
  check('weight_scale_invariant', maxdiff(scaled_gamma, gamma_stratified) <= 1e-7,
        detail = maxdiff(scaled_gamma, gamma_stratified))
  singleton <- strata; singleton[clusters == 'C001'] <- 'SINGLETON'
  singleton_error <- tryCatch({stratified_cov(psi, clusters, singleton); NULL}, error = conditionMessage)
  check('singleton_rejected', identical(singleton_error, 'Singleton stratum has no authorized variance rule'))
  crossing <- strata; crossing[1L] <- 'H2'
  crossing_error <- tryCatch({stratified_cov(psi, clusters, crossing); NULL}, error = conditionMessage)
  check('cross_stratum_cluster_rejected', identical(crossing_error, 'Cluster belongs to more than one stratum'))
  pe <- parameterEstimates(fit_stratified)
  record$configuration <<- list(n = n, clusters = g, strata = 4L, casesPerCluster = 15L,
    rng = RNGkind(), model = model, items = items, missing = 'none',
    fpc = 'none', pps = 'not modeled', target = 'N times covariance of 22 sample moments')
  record$observations <<- list(sampleMoments = lavInspect(native, 'wls.obs'),
    caseContributionColumnSums = colSums(psi),
    gammaNative = gamma_native, gammaStratified = gamma_stratified,
    gammaEigenvalueRange = range(eigen(gamma_stratified, symmetric = TRUE, only.values = TRUE)$values),
    vcovEigenvalueRange = range(eigen(lavInspect(fit_stratified, 'vcov'), symmetric = TRUE, only.values = TRUE)$values),
    parameters = pe, pointDifference = point_difference,
    vcovDifferenceNativeExternal = maxdiff(lavInspect(native, 'vcov'), lavInspect(fit_native_input, 'vcov')),
    vcovDifferenceStratumAlternative = maxdiff(lavInspect(changed_fit, 'vcov'), lavInspect(fit_stratified, 'vcov')),
    converged = lavInspect(fit_stratified, 'converged'),
    admissible = lavInspect(fit_stratified, 'post.check'),
    test = lavInspect(fit_stratified, 'test'),
    singletonError = singleton_error, crossingError = crossing_error)
  check('finite_estimates_and_se', all(is.finite(pe$est)) && all(is.finite(pe$se)))
  check('converged_and_admissible', isTRUE(record$observations$converged) && isTRUE(record$observations$admissible))
}
failure <- tryCatch(withCallingHandlers(run(), warning = function(w) {
  warnings_seen <<- c(warnings_seen, conditionMessage(w)); invokeRestart('muffleWarning')
}), error = function(e) conditionMessage(e))
record$warnings <- warnings_seen
record$error <- if (is.character(failure)) failure else NULL
record$checks <- checks
record$technicalStatus <- if (is.null(record$error) && length(checks) &&
  all(vapply(checks, function(x) x$status == 'BESTANDEN', logical(1)))) 'BESTANDEN' else 'NICHT_BESTANDEN'
record$scientificStatus <- 'NICHT_GEPRÜFT'
write_json(record, file.path(own, 'trial-001-result.json'), pretty = TRUE, auto_unbox = TRUE,
           digits = 16, null = 'null', dataframe = 'rows', matrix = 'rowmajor')
cat('technicalStatus', record$technicalStatus, '\n')
if (record$technicalStatus != 'BESTANDEN') quit(status = 1L)
