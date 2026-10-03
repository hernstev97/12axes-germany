#!/usr/bin/env Rscript
# SOFTWARE-001. Only invented data; no file inputs except this script and packages.
# This checks software capabilities, not ESS measurement or interval coverage.
options(warn = 1, digits = 16)
args <- commandArgs(trailingOnly = TRUE)
project <- if (length(args)) normalizePath(args[[1]], mustWork = TRUE) else normalizePath('.')
output <- file.path(project, 'outputs/loop/software-author')
public_output <- if (length(args) > 1L) args[[2]] else file.path(project, 'reports/loop/synthetic/software-001.json')
stopifnot(dir.exists(output))
dir.create(dirname(public_output), recursive = TRUE, showWarnings = FALSE)
suppressPackageStartupMessages(library(lavaan))
suppressPackageStartupMessages(library(jsonlite))
stopifnot(as.character(packageVersion('lavaan')) == '0.7.2')

sha256 <- function(path) {
  text <- system2('sha256sum', shQuote(path), stdout = TRUE)
  stopifnot(length(text) == 1L)
  strsplit(text, ' ', fixed = TRUE)[[1L]][1L]
}
capture <- function(fun) {
  warnings <- character()
  messages <- character()
  error <- NULL
  value <- tryCatch(withCallingHandlers(fun(),
    warning = function(w) { warnings <<- c(warnings, conditionMessage(w)); invokeRestart('muffleWarning') },
    message = function(m) { messages <<- c(messages, conditionMessage(m)); invokeRestart('muffleMessage') }),
    error = function(e) { error <<- conditionMessage(e); NULL })
  list(value = value, error = error, warnings = warnings, messages = messages)
}

RNGkind('Mersenne-Twister', 'Inversion', 'Rejection')
seed <- 2026100304L
set.seed(seed)
n_strata <- 4L
clusters_per_stratum <- 24L
cases_per_cluster <- 15L
n_clusters <- n_strata * clusters_per_stratum
n <- n_clusters * cases_per_cluster
cluster_number <- rep(seq_len(n_clusters), each = cases_per_cluster)
stratum_number <- rep(rep(seq_len(n_strata), each = clusters_per_stratum), each = cases_per_cluster)
# Clusters are independent. Rows within a cluster share an invented latent effect.
cluster_effect <- rnorm(n_clusters, sd = sqrt(0.25))
latent <- cluster_effect[cluster_number] + rnorm(n, sd = sqrt(0.75))
loadings <- c(0.65, 0.70, 0.75, 0.80)
thresholds <- c(-1.2, -0.4, 0.4, 1.2)
items <- paste0('y', seq_along(loadings))
dat <- as.data.frame(setNames(lapply(loadings, function(loading) {
  response <- loading * latent + rnorm(n, sd = sqrt(1 - loading^2))
  as.integer(cut(response, breaks = c(-Inf, thresholds, Inf), labels = FALSE))
}), items))
dat$synthetic_cluster <- sprintf('C%03d', cluster_number)
dat$synthetic_stratum <- sprintf('H%02d', stratum_number)
# Weights are independent of all latent responses and residuals.
dat$w <- runif(n, 0.5, 1.5)
dat$w_uniform <- 1
dat$w_scaled <- 7 * dat$w
dat$cluster_permuted <- sample(dat$synthetic_cluster, replace = FALSE)
dat$stratum_permuted <- sample(dat$synthetic_stratum, replace = FALSE)
input_path <- file.path(output, 'synthetic-input.csv')
write.csv(dat, input_path, row.names = FALSE, quote = TRUE)

model <- 'f =~ y1 + y2 + y3 + y4'
base_args <- list(model = model, data = dat, ordered = items, estimator = 'WLSMV',
                  parameterization = 'theta', std_lv = TRUE,
                  sampling_weights_type = 'design', sampling_weights_normalization = 'group')
fits <- list()
cases <- list()
selected_options <- c('estimator', 'estimator.orig', 'se', 'test', 'information',
  'parameterization', 'sampling.weights.type', 'sampling.weights.normalization',
  '.categorical', '.clustered', '.multilevel')

fit_case <- function(name, extra = list(), data = dat, expect_error = FALSE) {
  call_args <- modifyList(base_args, extra)
  call_args$data <- data
  result <- capture(function() do.call(lavaan::cfa, call_args))
  case <- list(name = name, expected = if (expect_error) 'controlled_api_error' else 'numerical_cfa',
               warnings = result$warnings, messages = result$messages, error = result$error)
  if (is.null(result$error)) {
    fit <- result$value
    fits[[name]] <<- fit
    opt <- lavInspect(fit, 'options')
    pe <- parameterEstimates(fit)
    gamma <- lavInspect(fit, 'gamma')
    vcov <- lavInspect(fit, 'vcov')
    measures <- capture(function() fitMeasures(fit, c('chisq', 'df', 'pvalue', 'chisq.scaled', 'df.scaled', 'pvalue.scaled')))
    tests <- lavInspect(fit, 'test')
    tests <- lapply(tests, function(t) t[intersect(names(t), c('test', 'stat', 'df', 'pvalue',
                          'scaling.factor', 'shift.parameter', 'scaled.test.stat', 'scaled.test'))])
    case$options <- opt[intersect(selected_options, names(opt))]
    case$converged <- lavInspect(fit, 'converged')
    case$admissible_post_check <- lavInspect(fit, 'post.check')
    case$iterations <- lavInspect(fit, 'iterations')
    case$nobs <- lavInspect(fit, 'nobs')
    case$nclusters_lavInspect <- if (isTRUE(opt$.clustered)) lavInspect(fit, 'nclusters') else NULL
    # In pinned 0.7-2, this public getter returns 1 whenever nlevels == 1,
    # even with singlelevel robust clustering. Preserve it and check the
    # internal cluster count actually used by lav_samplestats for G/(G-1).
    case$nclusters_internal_Lp <- if (isTRUE(opt$.clustered)) fit@Data@Lp[[1L]]$nclusters[[2L]] else NULL
    case$nclusters_input <- if (isTRUE(opt$.clustered)) length(unique(data[[call_args$cluster]])) else NULL
    case$parameters <- pe[, intersect(c('lhs', 'op', 'rhs', 'est', 'se', 'z', 'pvalue', 'ci.lower', 'ci.upper'), names(pe))]
    case$sample_statistics <- lavInspect(fit, 'wls.obs')
    case$sample_statistics_labels <- names(case$sample_statistics)
    case$gamma_order <- case$sample_statistics_labels
    case$gamma <- gamma
    case$gamma_dimension <- dim(gamma)
    case$gamma_eigenvalue_range <- range(eigen(gamma, symmetric = TRUE, only.values = TRUE)$values)
    case$vcov_eigenvalue_range <- range(eigen(vcov, symmetric = TRUE, only.values = TRUE)$values)
    case$all_estimates_se_finite <- all(is.finite(pe$est)) && all(is.finite(pe$se))
    case$fit_measures <- if (!is.null(measures$value)) setNames(as.list(as.numeric(measures$value)), names(measures$value)) else NULL
    case$fit_measures_error <- measures$error
    case$fit_measures_warnings <- measures$warnings
    case$tests <- tests
    case$technical_status <- if (!expect_error && isTRUE(case$converged) &&
      isTRUE(case$admissible_post_check) && isTRUE(case$all_estimates_se_finite) &&
      all(is.finite(gamma)) && all(is.finite(vcov))) 'BESTANDEN' else 'NICHT_BESTANDEN'
    saveRDS(fit, file.path(output, paste0('fit-', name, '.rds')), version = 3)
  } else {
    case$technical_status <- if (expect_error) 'BESTANDEN' else 'NICHT_BESTANDEN'
  }
  cases[[name]] <<- case
  cat(name, case$technical_status, '\n')
  invisible(case)
}

fit_case('ordinal_unweighted')
fit_case('ordinal_weighted', list(sampling_weights = 'w'))
fit_case('ordinal_cluster', list(cluster = 'synthetic_cluster'))
fit_case('ordinal_weighted_cluster', list(sampling_weights = 'w', cluster = 'synthetic_cluster'))
fit_case('ordinal_uniform_weights', list(sampling_weights = 'w_uniform'))
fit_case('ordinal_weights_scaled', list(sampling_weights = 'w_scaled', cluster = 'synthetic_cluster'))
fit_case('ordinal_cluster_permuted', list(sampling_weights = 'w', cluster = 'cluster_permuted'))

no_strata <- dat[, setdiff(names(dat), c('synthetic_stratum', 'stratum_permuted')), drop = FALSE]
changed_strata <- dat
changed_strata$synthetic_stratum <- dat$stratum_permuted
fit_case('ordinal_stratum_removed', list(sampling_weights = 'w', cluster = 'synthetic_cluster'), data = no_strata)
fit_case('ordinal_stratum_changed', list(sampling_weights = 'w', cluster = 'synthetic_cluster'), data = changed_strata)
for (arg in c('strata', 'stratum', 'stratification')) {
  extra <- list(sampling_weights = 'w', cluster = 'synthetic_cluster')
  extra[[arg]] <- 'synthetic_stratum'
  fit_case(paste0('api_', arg), extra, expect_error = TRUE)
}
negative_weight <- dat
negative_weight$w[1L] <- -0.1
fit_case('api_negative_weight', list(sampling_weights = 'w', cluster = 'synthetic_cluster'), negative_weight, TRUE)
na_weight <- dat
na_weight$w[1L] <- NA_real_
fit_case('api_na_weight', list(sampling_weights = 'w', cluster = 'synthetic_cluster'), na_weight, TRUE)
one_cluster <- dat
one_cluster$synthetic_cluster <- 'C_ONLY'
fit_case('api_one_cluster', list(sampling_weights = 'w', cluster = 'synthetic_cluster'), one_cluster, TRUE)
fit_case('api_absent_weight', list(sampling_weights = 'absent_weight', cluster = 'synthetic_cluster'), expect_error = TRUE)
fit_case('api_ordinal_missing_ml', list(sampling_weights = 'w', cluster = 'synthetic_cluster', missing = 'ml'), expect_error = TRUE)

maxdiff <- function(a, b) {
  if (is.null(a) || is.null(b)) return(NULL)
  if (!identical(length(a), length(b))) return(NULL)
  max(abs(as.numeric(a) - as.numeric(b)))
}
contrast <- function(first, second) {
  if (is.null(fits[[first]]) || is.null(fits[[second]])) return(list(status = 'NICHT_GEPRÜFT'))
  a <- fits[[first]]
  b <- fits[[second]]
  list(first = first, second = second,
    max_abs_coefficients = maxdiff(coef(a), coef(b)),
    max_abs_sample_statistics = maxdiff(lavInspect(a, 'wls.obs'), lavInspect(b, 'wls.obs')),
    max_abs_gamma = maxdiff(lavInspect(a, 'gamma'), lavInspect(b, 'gamma')),
    max_abs_vcov = maxdiff(lavInspect(a, 'vcov'), lavInspect(b, 'vcov')))
}
contrasts <- list(
  uniform_vs_unweighted = contrast('ordinal_uniform_weights', 'ordinal_unweighted'),
  weighted_vs_unweighted = contrast('ordinal_weighted', 'ordinal_unweighted'),
  weighted_cluster_vs_no_cluster = contrast('ordinal_weighted_cluster', 'ordinal_weighted'),
  weight_scale = contrast('ordinal_weights_scaled', 'ordinal_weighted_cluster'),
  cluster_permutation = contrast('ordinal_cluster_permuted', 'ordinal_weighted_cluster'),
  stratum_removed = contrast('ordinal_stratum_removed', 'ordinal_weighted_cluster'),
  stratum_changed = contrast('ordinal_stratum_changed', 'ordinal_weighted_cluster'))

# An independent marginal probability / delta / Taylor calculation.
# It checks only y1's first threshold, not the entire SEM sandwich or survey theory.
probability <- sum(dat$w * (dat$y1 <= 1L)) / sum(dat$w)
threshold <- qnorm(probability)
u <- dat$w * ((dat$y1 <= 1L) - probability) / (sum(dat$w) * dnorm(threshold))
cluster_u <- as.numeric(rowsum(u, cluster_number, reorder = FALSE))
cluster_strata <- rep(seq_len(n_strata), each = clusters_per_stratum)
taylor_stratified <- sum(vapply(split(cluster_u, cluster_strata), function(U) {
  length(U)/(length(U)-1) * sum((U - mean(U))^2)
}, numeric(1L)))
oracle <- list(target = 'marginal qnorm(weighted Pr(y1<=1))', weighted_probability = probability,
  threshold_delta = threshold, iid_meat_variance_without_finite_correction = sum(u^2),
  cluster_meat_variance_without_finite_correction = sum(cluster_u^2),
  unstratified_cluster_Taylor = n_clusters/(n_clusters-1) * sum((cluster_u-mean(cluster_u))^2),
  stratified_cluster_Taylor = taylor_stratified,
  strata_Taylor_df = n_clusters-n_strata,
  interpretation = 'One marginal threshold comparison only. No SEM coverage or ESS design validation.')
if (!is.null(fits$ordinal_weighted_cluster)) {
  sample_statistics <- lavInspect(fits$ordinal_weighted_cluster, 'wls.obs')
  first <- match('y1|t1', names(sample_statistics))
  stopifnot(!is.na(first))
  oracle$lavaan_threshold <- as.numeric(sample_statistics[first])
  oracle$lavaan_gamma_over_n <- as.numeric(lavInspect(fits$ordinal_weighted_cluster, 'gamma')[first, first] / n)
  oracle$abs_difference_threshold <- abs(oracle$lavaan_threshold - threshold)
  oracle$abs_difference_cluster_meat <- abs(oracle$lavaan_gamma_over_n - sum(cluster_u^2))
  oracle$abs_difference_unstratified_Taylor <- abs(oracle$lavaan_gamma_over_n - oracle$unstratified_cluster_Taylor)
  oracle$abs_difference_stratified_Taylor <- abs(oracle$lavaan_gamma_over_n - taylor_stratified)
}
if (!is.null(fits$ordinal_weighted)) {
  oracle$lavaan_iid_gamma_over_n <- as.numeric(lavInspect(fits$ordinal_weighted, 'gamma')[1L,1L]/n)
  oracle$abs_difference_iid_meat <- abs(oracle$lavaan_iid_gamma_over_n - sum(u^2))
}

optional <- list()
if (requireNamespace('semTools', quietly = TRUE) && !is.null(fits$ordinal_weighted_cluster)) {
  optional$semTools_version <- as.character(packageVersion('semTools'))
  W <- 'observed_mean <~ 0.0625*y1 + 0.0625*y2 + 0.0625*y3 + 0.0625*y4'
  rel <- capture(function() semTools::compRelSEM(fits$ordinal_weighted_cluster,
                   ord.scale = TRUE, W = W, obs.var = TRUE))
  optional$observed_scale_reliability <- list(call = 'compRelSEM(fit, ord.scale=TRUE, W=explicit 1/(4*4) weights, obs.var=TRUE)',
    weights_syntax = W, value = rel$value, error = rel$error, warnings = rel$warnings,
    status = if (is.null(rel$error)) 'API_AUSGEFÜHRT' else 'API_FEHLER',
    boundary = 'No reliability interval, no independent formula verification, no personal uncertainty or ESS approval.')
  syntax <- capture(function() semTools::measEq.syntax(configural.model = model,
    data = dat, ordered = items, parameterization = 'theta', ID.fac = 'std.lv',
    ID.cat = 'Wu.Estabrook.2016', group = 'synthetic_stratum', group.equal = 'thresholds'))
  optional$threshold_invariance_syntax <- list(error = syntax$error, warnings = syntax$warnings,
    status = if (is.null(syntax$error)) 'SYNTAX_ERZEUGT_NICHT_GEFITTET' else 'API_FEHLER',
    boundary = 'group names are invented; group argument is not survey stratification. No invariance test fitted.')
  if (is.null(syntax$error)) {
    syntax_path <- file.path(output, 'semTools-threshold-invariance-syntax.txt')
    writeLines(as.character(syntax$value), syntax_path)
    optional$threshold_invariance_syntax$syntax_file <- 'outputs/loop/software-author/semTools-threshold-invariance-syntax.txt'
    optional$threshold_invariance_syntax$syntax_sha256 <- sha256(syntax_path)
  }
} else {
  optional$status <- 'NICHT_GEPRÜFT'
  optional$reason <- 'semTools unavailable or weighted clustered CFA failed'
}

packages <- c('lavaan','MASS','mnormt','pbivnorm','numDeriv','quadprog','jsonlite','semTools')
versions <- setNames(lapply(packages, function(p) {
  if (requireNamespace(p, quietly = TRUE)) as.character(packageVersion(p)) else NULL
}), packages)
free_parameters <- if (!is.null(fits$ordinal_weighted_cluster)) nrow(parameterTable(fits$ordinal_weighted_cluster)[parameterTable(fits$ordinal_weighted_cluster)$free>0L,]) else NULL
primary <- cases$ordinal_weighted_cluster
primary_robust <- !is.null(primary$tests$scaled.shifted) && is.finite(primary$tests$scaled.shifted$stat)
checks <- list(
  weighted_ordinal_cluster_numerical = identical(primary$technical_status, 'BESTANDEN') && primary_robust,
  internal_cluster_count_matches_input = identical(as.integer(primary$nclusters_internal_Lp), as.integer(n_clusters)) && identical(as.integer(primary$nclusters_input), as.integer(n_clusters)),
  uniform_weight_equivalence = !is.null(contrasts$uniform_vs_unweighted$max_abs_gamma) && contrasts$uniform_vs_unweighted$max_abs_gamma < 1e-8,
  scaling_invariance = !is.null(contrasts$weight_scale$max_abs_gamma) && contrasts$weight_scale$max_abs_gamma < 1e-8,
  cluster_changes_gamma = !is.null(contrasts$cluster_permutation$max_abs_gamma) && contrasts$cluster_permutation$max_abs_gamma > 1e-8,
  strata_unused_without_api = !is.null(contrasts$stratum_removed$max_abs_gamma) && contrasts$stratum_removed$max_abs_gamma < 1e-12 && contrasts$stratum_changed$max_abs_gamma < 1e-12,
  stratum_named_api_rejected = all(vapply(c('api_strata','api_stratum','api_stratification'),function(k)!is.null(cases[[k]]$error),logical(1L))),
  all_planned_negative_cases_rejected = all(vapply(names(cases)[startsWith(names(cases),'api_')],function(k)!is.null(cases[[k]]$error),logical(1L))),
  first_threshold_matches_weighted_probability = !is.null(oracle$abs_difference_threshold) && oracle$abs_difference_threshold < 1e-10,
  first_threshold_gamma_matches_unstratified_Taylor = !is.null(oracle$abs_difference_unstratified_Taylor) && oracle$abs_difference_unstratified_Taylor < 1e-10)
report <- list(schemaVersion = 1L, package = 'SOFTWARE-001', executed = TRUE,
  type = 'synthetic_software_capability_smoke', dateUtc = '2026-10-03',
  author = '/root/software001_author', authorIsIndependentReviewer = FALSE,
  script = 'pipeline/synthetic/software-001.R', scriptSha256 = sha256(file.path(project,'pipeline/synthetic/software-001.R')),
  input = list(syntheticOnly = TRUE, noESSDataRead = TRUE, seed = seed, RNGkind = RNGkind(),
    file = 'outputs/loop/software-author/synthetic-input.csv', sha256 = sha256(input_path),
    n = n, strata = n_strata, independentClusters = n_clusters, casesPerCluster = cases_per_cluster,
    independentWeights = 'Uniform(0.5,1.5)', clusterLatentVariance = 0.25,
    individualLatentVariance = 0.75, populationResponseLoadings = loadings,
    fixedResponseThresholds = thresholds, ordinalCategories = 1:5,
    items = items, categoryCounts = lapply(dat[items], function(y) as.integer(table(factor(y,levels=1:5)))),
    model = model, freeParameters = free_parameters),
  environment = list(R = R.version.string, platform = R.version$platform,
    packages = versions, libraryPaths = .libPaths(), tmpdir = tempdir(),
    sessionInfo = capture.output(sessionInfo())),
  setup = list(status = 'NICHT_BESTANDEN',
    reason = 'Conda create unexpectedly touched an empty ~/.conda/environments.txt despite register_envs=false; parent .conda birth time falls in the create interval.',
    evidence = 'outputs/loop/software-author/outside-write-incident.json',
    runtimeBoundary = 'Final Rscript runs directly with --vanilla and per-child Landlock write rules; no further Conda calls.'),
  cases = cases, contrasts = contrasts, firstThresholdOracle = oracle,
  optionalSemTools = optional, technicalChecks = checks,
  technicalPackageStatus = if (all(unlist(checks))) 'BESTANDEN_IM_BENANNTEN_SYNTHETISCHEN_SMOKE' else 'NICHT_BESTANDEN',
  scientificAcceptance = 'NICHT_GEPRÜFT',
  ESS_full_design_support = 'NICHT_BELEGT',
  untested = c('ESS data and models','full stratum/PSU SEM sandwich and its theory',
    'PPS or finite-population correction','survey calibration/nonresponse weight uncertainty',
    'ordinal EFA and rotation stability','fitted invariance chain and robust nested tests',
    'reliability formula original-source review and design intervals',
    'mixed continuous/discrete composite reliability','personal measurement uncertainty',
    'sparse-category/high-weight numerical stress','interval coverage or model-selection calibration'),
  scope = 'Successful API/numerical execution on the named invented scenario is not a scientific gate or approved estimator for ESS.')
write_json(report, public_output, auto_unbox = TRUE, pretty = TRUE, digits = NA, na = 'null', null = 'null')
cat('report', public_output, '\n')
cat('technical package:',report$technicalPackageStatus,'scientific:',report$scientificAcceptance,'\n')
