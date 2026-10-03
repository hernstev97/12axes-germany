#!/usr/bin/env Rscript
# Technical correction after original results/reviews. Invented data only.
options(warn = 1, digits = 16)
args <- commandArgs(trailingOnly = TRUE)
stopifnot(length(args) == 3L)
project <- normalizePath(args[[1]], mustWork = TRUE)
own <- normalizePath(args[[2]], mustWork = TRUE)
stopifnot(identical(own, file.path(project, 'outputs/loop/methods002-correction')),
          identical(args[[3]], '/home/stevenh'), identical(Sys.getenv('HOME'), args[[3]]))
script_arg <- grep('^--file=', commandArgs(), value = TRUE)
stopifnot(length(script_arg) == 1L)
run_label <- sub('[.]R$', '', basename(sub('^--file=', '', script_arg)))
stopifnot(run_label %in% c('correction-original', 'correction-counterseed'))
counterseed <- identical(run_label, 'correction-counterseed')
suppressPackageStartupMessages(library(lavaan))
suppressPackageStartupMessages(library(jsonlite))
stopifnot(as.character(packageVersion('lavaan')) == '0.7.2')
warnings_seen <- character()
record <- list(package = 'METHODS-002', version = 3L, run = run_label,
  scope = 'Synthetic technical target/import correction only; post original result knowledge',
  seed = if (counterseed) 734129L else 2026100307L,
  criteria = 'outputs/loop/methods002-correction/plan-before-run.md',
  tolerance = 1e-7, independentCorrectionReview = 'NICHT_GEPRÜFT',
  historicalMissingTargetEvidence = 'NICHT_BESTANDEN',
  runtime = list(R = R.version.string, lavaan = as.character(packageVersion('lavaan')),
                jsonlite = as.character(packageVersion('jsonlite')), HOME = Sys.getenv('HOME'),
                libraries = .libPaths(), session = capture.output(sessionInfo())))
original_check_ids <- c('full_native_gamma', 'finite_dimension', 'symmetry',
  'threshold_covariance_oracle', 'all_weighted_thresholds',
  'external_native_gamma_import', 'external_stratified_gamma_import',
  'same_dwls_point_estimates', 'stratum_change_changes_covariance',
  'stratum_change_keeps_points', 'renaming_invariant', 'weight_scale_invariant',
  'singleton_rejected', 'cross_stratum_cluster_rejected',
  'finite_estimates_and_se', 'converged_and_admissible')
extra_check_ids <- c('sample_moment_labels', 'sample_threshold_labels',
  'sample_moment_numeric_order', 'original_wls_v_null', 'external_weight_input_contract',
  'external_native_wls_v_import', 'external_stratified_wls_v_import',
  'external_same_sample_moments', 'changed_wls_v_import', 'changed_wls_v_changes_points',
  'doubled_nacov_import', 'doubled_nacov_fixed_wls_v', 'doubled_nacov_keeps_points',
  'doubled_nacov_scales_vcov', 'doubled_nacov_scales_se')
expected_before_complete <- c(original_check_ids, extra_check_ids,
  if (counterseed) 'counterseed_target_separation' else character())
expected_check_ids <- c(expected_before_complete, 'expected_checks_complete')
checks <- list()
check <- function(id, observed, passed, rule) {
  if (id %in% names(checks)) stop('Duplicate check ID')
  checks[[id]] <<- list(status = if (isTRUE(passed)) 'BESTANDEN' else 'NICHT_BESTANDEN',
                       observed = observed, rule = rule)
  cat(id, checks[[id]]$status, '\n')
}
maxdiff <- function(a, b) {
  if (length(a) != length(b) || !length(a) || any(!is.finite(a)) || any(!is.finite(b)))
    return(Inf)
  max(abs(as.numeric(a) - as.numeric(b)))
}
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
  if (!counterseed) {
    # Original generator unchanged, including RNG draw order.
    n <- 1440L; g <- 96L
    sizes <- rep(15L, g)
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
    cluster_variable <- 'cluster'
    model <- 'f =~ y1 + y2 + y3 + y4'
    limits <- rep(list(c(-1.2, -0.4, 0.4, 1.2)), 4L)
    generating_loadings <- c(0.65, 0.70, 0.75, 0.80)
    stratum_psus <- rep(24L, 4L)
  } else {
    # Accessible original reviewer generator, not a new searched seed.
    stratum_psus <- c(9L, 13L, 17L)
    g <- sum(stratum_psus)
    sizes <- rep(13:23, length.out = g)
    clusters <- rep(sprintf('own-%02d', seq_len(g)), sizes)
    strata <- rep(rep(c('own-alpha', 'own-beta', 'own-gamma'), stratum_psus), sizes)
    n <- length(clusters)
    latent <- rep(rnorm(g, sd = 0.43), sizes) + rnorm(n, sd = 0.89)
    items <- paste0('x', 1:4)
    limits <- list(c(-1.3, -0.55, 0.15, 1.05), c(-1.1, -0.2, 0.6, 1.4),
                   c(-1.5, -0.65, 0.35, 1.2), c(-0.95, -0.3, 0.45, 1.35))
    generating_loadings <- c(0.57, 0.64, 0.71, 0.77)
    dat <- as.data.frame(setNames(lapply(seq_len(4), function(j) {
      signal <- generating_loadings[j] * latent + rnorm(n, sd = sqrt(1 - generating_loadings[j]^2))
      as.integer(cut(signal, c(-Inf, limits[[j]], Inf), labels = FALSE))
    }), items))
    dat$w <- runif(n, 0.25, 2.3)
    dat$psu <- clusters
    cluster_variable <- 'psu'
    model <- 'latent =~ x1 + x2 + x3 + x4'
  }
  record$configuration <<- list(n = n, clusters = g, strata = length(stratum_psus),
    stratumPSUs = stratum_psus, casesPerClusterRange = range(sizes),
    clusterSizeSequence = sizes, rng = RNGkind(), model = model, items = items,
    generatingLoadings = generating_loadings, categoryCutpoints = limits,
    missing = 'none', fpc = 'none', pps = 'not modeled',
    target = 'N times covariance of 22 sample moments',
    generatorSource = if (counterseed) 'outputs/loop/methods002-statistics/statistics-004.R:73-97' else
      'reports/loop/packages/METHODS-002/v2/files/pipeline/synthetic/methods-002.R:46-60')
  base <- list(model = model, data = dat, ordered = items, estimator = 'WLSMV',
    parameterization = 'theta', std_lv = TRUE, sampling_weights = 'w',
    sampling_weights_type = 'design', sampling_weights_normalization = 'group')
  native <- do.call(lavaan::cfa, c(base, list(cluster = cluster_variable)))
  wt <- dat$w * n / sum(dat$w)
  m84 <- getFromNamespace('muthen1984', 'lavaan')
  inverse_b <- getFromNamespace('lav_m84_b_inv', 'lavaan')
  moments <- function(weights) m84(data_1 = as.matrix(dat[items]), ov_names = items,
    ov_types = rep('ordered', 4), ov_levels = rep(5L, 4), wt = weights,
    sampling_weights_type = 'design', cluster_idx = as.integer(factor(clusters)))
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
  check('full_native_gamma', native_difference, native_difference <= 1e-7, 'max absolute difference <= 1e-7')
  covariance <- stratified_cov(psi, clusters, strata)
  gamma_stratified <- n * covariance
  observed_moments <- lavInspect(native, 'wls.obs')
  labels <- names(observed_moments)
  threshold_labels <- paste0(rep(items, each = 4L), '|t', rep(1:4, times = 4L))
  pairs <- which(lower.tri(matrix(0, 4L, 4L)), arr.ind = TRUE)
  correlation_labels <- paste0(items[pairs[, 'col']], '~~', items[pairs[, 'row']])
  expected_labels <- c(threshold_labels, correlation_labels)
  labels_ok <- length(observed_moments) == 22L && identical(labels, expected_labels) && !anyDuplicated(labels)
  check('sample_moment_labels', list(actual = labels, expected = expected_labels), labels_ok,
        'all 22 names exactly identical; no duplicates')
  if (!labels_ok) stop('Sample moment label contract failed')
  threshold_indices <- match(threshold_labels, labels)
  threshold_labels_ok <- length(threshold_indices) == 16L && !anyNA(threshold_indices) &&
    identical(labels[threshold_indices], threshold_labels)
  check('sample_threshold_labels', labels[threshold_indices], threshold_labels_ok,
        'all 16 explicitly matched threshold names exactly identical')
  if (!threshold_labels_ok) stop('Threshold label contract failed')
  expected_moments <- c(unlist(m$TH), m$COR[lower.tri(m$COR)])
  moment_order_difference <- maxdiff(observed_moments, expected_moments)
  check('sample_moment_numeric_order', moment_order_difference, moment_order_difference <= 1e-7,
        '22 values match TH then columnwise lower correlation triangle, <= 1e-7')
  dimnames(gamma_stratified) <- dimnames(gamma_native) <- list(labels, labels)
  check('finite_dimension', list(dimension = dim(gamma_stratified), finite = all(is.finite(gamma_stratified))),
        identical(dim(gamma_stratified), c(22L, 22L)) && all(is.finite(gamma_stratified)), 'finite 22x22')
  symmetry_difference <- maxdiff(gamma_stratified, t(gamma_stratified))
  check('symmetry', symmetry_difference, symmetry_difference <= 1e-7, 'max symmetry difference <= 1e-7')
  oracle <- do.call(cbind, lapply(items, function(item) do.call(cbind, lapply(1:4, function(k) {
    indicator <- as.numeric(dat[[item]] <= k)
    probability <- sum(dat$w * indicator) / sum(dat$w)
    dat$w * (indicator - probability) / (sum(dat$w) * dnorm(qnorm(probability)))
  }))))
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
  threshold_difference <- maxdiff(covariance[threshold_indices, threshold_indices], oracle_cov)
  check('threshold_covariance_oracle', threshold_difference, threshold_difference <= 1e-7,
        'all 16x16 independently calculated delta/Taylor covariances <= 1e-7')
  observed_thresholds <- observed_moments[threshold_indices]
  expected_thresholds <- unlist(lapply(items, function(item) vapply(1:4, function(k)
    qnorm(sum(dat$w * (dat[[item]] <= k)) / sum(dat$w)), numeric(1))))
  threshold_value_difference <- maxdiff(observed_thresholds, expected_thresholds)
  check('all_weighted_thresholds', threshold_value_difference, threshold_value_difference <= 1e-7,
        'all 16 sample thresholds selected by labels vs marginal weighted qnorm <= 1e-7')
  implied_difference <- maxdiff(lavInspect(native, 'th'), expected_thresholds)
  if (counterseed) check('counterseed_target_separation', list(impliedDifference = implied_difference,
    sampleDifference = threshold_value_difference), implied_difference > 1e-7 && threshold_value_difference <= 1e-7,
    'same reviewer generator: implied difference > 1e-7, sample difference <= 1e-7')
  weight_input <- lavInspect(native, 'wls.v')
  slot_diagonal <- native@SampleStats@WLS.VD[[1L]]
  old_slot_is_null <- is.null(native@SampleStats@WLS.V[[1L]])
  check('original_wls_v_null', list(originalIsNull = old_slot_is_null, diagonalLength = length(slot_diagonal)),
        old_slot_is_null && length(slot_diagonal) == 22L, 'original DWLS WLS.V NULL and WLS.VD length 22')
  matrix_contract <- function(x) is.matrix(x) && identical(dim(x), c(22L, 22L)) &&
    all(is.finite(x)) && all(diag(x) > 0) && all(x[row(x) != col(x)] == 0) &&
    identical(rownames(x), expected_labels) && identical(colnames(x), expected_labels)
  weight_difference <- maxdiff(diag(weight_input), slot_diagonal)
  weight_contract_ok <- matrix_contract(weight_input) && length(slot_diagonal) == 22L && weight_difference <= 1e-7
  check('external_weight_input_contract', list(dimension = dim(weight_input), labels = rownames(weight_input),
    diagonalVsWlsVD = weight_difference, finite = all(is.finite(weight_input)),
    diagonal = diag(weight_input)), weight_contract_ok,
    'finite positive diagonal 22x22 with exact labels/order and WLS.VD agreement <= 1e-7')
  if (!weight_contract_ok) stop('External weight input contract failed')
  external <- function(gamma, weights = weight_input) {
    stopifnot(is.matrix(gamma), identical(dim(gamma), c(22L, 22L)), all(is.finite(gamma)),
      identical(rownames(gamma), expected_labels), identical(colnames(gamma), expected_labels),
      matrix_contract(weights))
    do.call(lavaan::cfa, c(base, list(nacov = gamma, wls_v = weights)))
  }
  fit_native_input <- external(gamma_native)
  fit_stratified <- external(gamma_stratified)
  imported_weight_check <- function(id, fit, requested) {
    stored <- lavInspect(fit, 'wls.v')
    difference <- maxdiff(stored, requested)
    check(id, list(difference = difference, dimensions = dim(stored), labels = rownames(stored)),
      matrix_contract(stored) && difference <= 1e-7 &&
        maxdiff(fit@SampleStats@WLS.VD[[1L]], diag(requested)) <= 1e-7,
      'actual public and version-bound stored weights match requested matrix/order <= 1e-7')
  }
  imported_weight_check('external_native_wls_v_import', fit_native_input, weight_input)
  imported_weight_check('external_stratified_wls_v_import', fit_stratified, weight_input)
  native_gamma_difference <- maxdiff(lavInspect(fit_native_input, 'gamma'), gamma_native)
  stratified_gamma_difference <- maxdiff(lavInspect(fit_stratified, 'gamma'), gamma_stratified)
  gamma_contract <- function(fit) {
    actual <- lavInspect(fit, 'gamma')
    identical(dim(actual), c(22L, 22L)) && all(is.finite(actual)) &&
      identical(rownames(actual), expected_labels) && identical(colnames(actual), expected_labels)
  }
  check('external_native_gamma_import', native_gamma_difference,
    gamma_contract(fit_native_input) && native_gamma_difference <= 1e-7, 'actual native Gamma import/order <= 1e-7')
  check('external_stratified_gamma_import', stratified_gamma_difference,
    gamma_contract(fit_stratified) && stratified_gamma_difference <= 1e-7, 'actual stratified Gamma import/order <= 1e-7')
  fit_moments <- lapply(list(fit_native_input, fit_stratified), function(fit) lavInspect(fit, 'wls.obs'))
  imported_moment_differences <- vapply(fit_moments, function(x) maxdiff(x, observed_moments), numeric(1))
  check('external_same_sample_moments', imported_moment_differences,
    all(imported_moment_differences <= 1e-7) &&
      all(vapply(fit_moments, function(x) identical(names(x), expected_labels), logical(1))),
    'both external fits have exact 22 labels and unchanged sample moments <= 1e-7')
  point_difference <- maxdiff(coef(native), coef(fit_stratified))
  check('same_dwls_point_estimates', point_difference, point_difference <= 1e-7, 'all DWLS points <= 1e-7')
  if (!counterseed) {
    cluster_means <- rowsum(dat$y1, clusters, reorder = FALSE)[, 1L] / 15
    rank_h <- rep(1:4, each = 24L)[order(order(cluster_means))]
    changed_h <- sprintf('S%d', rank_h[match(clusters, names(cluster_means))])
  } else {
    changed_h <- rep(sprintf('new-%d', ((seq_len(g) - 1) %% 3) + 1L), sizes)
  }
  changed_gamma <- n * stratified_cov(psi, clusters, changed_h)
  dimnames(changed_gamma) <- list(labels, labels)
  changed_difference <- maxdiff(changed_gamma, gamma_stratified)
  check('stratum_change_changes_covariance', changed_difference, changed_difference > 1e-7, 'Gamma change > 1e-7')
  changed_fit <- external(changed_gamma)
  changed_point_difference <- maxdiff(coef(changed_fit), coef(fit_stratified))
  check('stratum_change_keeps_points', changed_point_difference, changed_point_difference <= 1e-7, 'points <= 1e-7')
  renamed_gamma <- n * stratified_cov(psi, paste0('renamed_', clusters), paste0('renamed_', strata))
  rename_difference <- maxdiff(renamed_gamma, gamma_stratified)
  check('renaming_invariant', rename_difference, rename_difference <= 1e-7, 'renaming difference <= 1e-7')
  scaled_psi <- transform(moments((7 * dat$w) * n / sum(7 * dat$w)))
  scaled_gamma <- n * stratified_cov(scaled_psi, clusters, strata)
  scaled_difference <- maxdiff(scaled_gamma, gamma_stratified)
  check('weight_scale_invariant', scaled_difference, scaled_difference <= 1e-7,
        'original normalized factor-seven covariance check <= 1e-7')
  singleton <- strata; singleton[clusters == clusters[[1L]]] <- 'SINGLETON'
  singleton_error <- tryCatch({stratified_cov(psi, clusters, singleton); NULL}, error = conditionMessage)
  check('singleton_rejected', singleton_error,
    identical(singleton_error, 'Singleton stratum has no authorized variance rule'), 'exact original singleton error')
  crossing <- strata; crossing[1L] <- unique(strata)[[2L]]
  crossing_error <- tryCatch({stratified_cov(psi, clusters, crossing); NULL}, error = conditionMessage)
  check('cross_stratum_cluster_rejected', crossing_error,
    identical(crossing_error, 'Cluster belongs to more than one stratum'), 'exact original crossing error')
  pe <- parameterEstimates(fit_stratified)
  check('finite_estimates_and_se', list(estFinite = all(is.finite(pe$est)), seFinite = all(is.finite(pe$se))),
    all(is.finite(pe$est)) && all(is.finite(pe$se)), 'all estimates and SE finite')
  check('converged_and_admissible', list(converged = lavInspect(fit_stratified, 'converged'),
    admissible = lavInspect(fit_stratified, 'post.check')),
    isTRUE(lavInspect(fit_stratified, 'converged')) && isTRUE(lavInspect(fit_stratified, 'post.check')),
    'lavaan convergence and post.check TRUE; software observation only')
  altered_weight <- weight_input
  altered_indices <- match(c(correlation_labels[[1L]], correlation_labels[[6L]]), expected_labels)
  altered_weight[cbind(altered_indices, altered_indices)] <-
    weight_input[cbind(altered_indices, altered_indices)] * c(2, 13)
  weight_fit <- external(gamma_stratified, altered_weight)
  imported_weight_check('changed_wls_v_import', weight_fit, altered_weight)
  altered_point_difference <- maxdiff(coef(weight_fit), coef(fit_stratified))
  check('changed_wls_v_changes_points', altered_point_difference,
    altered_point_difference > 1e-7 && maxdiff(lavInspect(weight_fit, 'gamma'), gamma_stratified) <= 1e-7,
    'only first/last correlation weights x2/x13: point difference > 1e-7 at fixed Gamma')
  double_fit <- external(2 * gamma_stratified, weight_input)
  double_gamma_difference <- maxdiff(lavInspect(double_fit, 'gamma'), 2 * gamma_stratified)
  check('doubled_nacov_import', double_gamma_difference,
    gamma_contract(double_fit) && double_gamma_difference <= 1e-7, 'actual Gamma x2 import <= 1e-7')
  imported_weight_check('doubled_nacov_fixed_wls_v', double_fit, weight_input)
  double_point_difference <- maxdiff(coef(double_fit), coef(fit_stratified))
  check('doubled_nacov_keeps_points', double_point_difference, double_point_difference <= 1e-7, 'fixed actual WLS input points <= 1e-7')
  double_vcov_difference <- maxdiff(lavInspect(double_fit, 'vcov'), 2 * lavInspect(fit_stratified, 'vcov'))
  check('doubled_nacov_scales_vcov', double_vcov_difference, double_vcov_difference <= 1e-7,
        'Gamma x2 at fixed WLS produces parameter covariance x2 <= 1e-7')
  double_pe <- parameterEstimates(double_fit)
  pe_identity <- function(x) paste(x$lhs, x$op, x$rhs, sep = ':')
  positive_se <- pe$se > 0
  se_ratios <- double_pe$se[positive_se] / pe$se[positive_se]
  se_ratio_difference <- maxdiff(se_ratios, rep(sqrt(2), length(se_ratios)))
  check('doubled_nacov_scales_se', list(ratios = se_ratios, maximumDifference = se_ratio_difference,
    comparedCount = sum(positive_se)), identical(pe_identity(pe), pe_identity(double_pe)) &&
    all(is.finite(double_pe$se)) && sum(positive_se) > 0L && se_ratio_difference <= 1e-7,
    'all positive SE ratios sqrt(2) <= 1e-7; exact parameter order')
  record$observations <<- list(sampleMomentLabels = labels, sampleMoments = as.numeric(observed_moments),
    thresholdLabels = threshold_labels, thresholdIndices = threshold_indices,
    sampleThresholds = as.numeric(observed_thresholds), marginalQnormThresholds = expected_thresholds,
    modelImpliedThresholds = as.numeric(lavInspect(native, 'th')),
    sampleThresholdDifference = threshold_value_difference, modelImpliedThresholdDifference = implied_difference,
    modelImpliedScope = 'Separate diagnostic; not marginal target or acceptance rule except fixed reviewer counterexample',
    caseContributionColumnSums = colSums(psi), gammaNative = gamma_native, gammaStratified = gamma_stratified,
    externalWeightLabels = rownames(weight_input), externalWeightDiagonal = diag(weight_input),
    originalWlsVIsNull = old_slot_is_null, gammaEigenvalueRange =
      range(eigen(gamma_stratified, symmetric = TRUE, only.values = TRUE)$values),
    vcovEigenvalueRange = range(eigen(lavInspect(fit_stratified, 'vcov'), symmetric = TRUE, only.values = TRUE)$values),
    parameters = pe, pointDifference = point_difference,
    vcovDifferenceNativeExternal = maxdiff(lavInspect(native, 'vcov'), lavInspect(fit_native_input, 'vcov')),
    vcovDifferenceStratumAlternative = maxdiff(lavInspect(changed_fit, 'vcov'), lavInspect(fit_stratified, 'vcov')),
    alteredWeightLabels = expected_labels[altered_indices], alteredWeightFactors = c(2, 13),
    alteredWeightDiagonal = diag(altered_weight), alteredWeightPointDifference = altered_point_difference,
    doubledGammaPointDifference = double_point_difference, doubledGammaVcovDifference = double_vcov_difference,
    doubledGammaSeRatios = se_ratios, doubledGammaSeRatioDifference = se_ratio_difference,
    converged = lavInspect(fit_stratified, 'converged'), admissible = lavInspect(fit_stratified, 'post.check'),
    test = lavInspect(fit_stratified, 'test'), doubledGammaTest = lavInspect(double_fit, 'test'),
    changedWeightConverged = lavInspect(weight_fit, 'converged'),
    changedWeightAdmissible = lavInspect(weight_fit, 'post.check'),
    singletonError = singleton_error, crossingError = crossing_error)
  complete <- length(checks) == length(expected_before_complete) &&
    setequal(names(checks), expected_before_complete) && !anyDuplicated(names(checks))
  check('expected_checks_complete', list(expected = expected_before_complete, actual = names(checks)),
    complete, 'exact expected names and count; no duplicate/missing/unexpected checks')
  invisible(NULL)
}
failure <- tryCatch(withCallingHandlers(run(), warning = function(w) {
  warnings_seen <<- c(warnings_seen, conditionMessage(w)); invokeRestart('muffleWarning')
}), error = function(e) conditionMessage(e))
record$warnings <- warnings_seen
record$error <- if (is.character(failure)) failure else NULL
record$checks <- checks
record$expectedCheckNames <- expected_check_ids
record$actualCheckNames <- names(checks)
record$checkCompleteness <- length(checks) == length(expected_check_ids) &&
  setequal(names(checks), expected_check_ids) && !anyDuplicated(names(checks))
record$technicalAuthorStatus <- if (is.null(record$error) && record$checkCompleteness &&
  all(vapply(checks, function(x) x$status == 'BESTANDEN', logical(1)))) 'BESTANDEN' else 'NICHT_BESTANDEN'
record$scientificStatus <- 'NICHT_GEPRÜFT'
write_json(record, file.path(own, paste0(run_label, '-result.json')), pretty = TRUE, auto_unbox = TRUE,
           digits = 16, null = 'null', dataframe = 'rows', matrix = 'rowmajor')
cat('technicalAuthorStatus', record$technicalAuthorStatus, '\n')
if (record$technicalAuthorStatus != 'BESTANDEN') quit(status = 1L)
