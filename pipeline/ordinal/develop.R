# Fixed A-development runner. No raw-data discovery or automatic publication.
ed_stop <- function(code) stop(paste0('ESS_DEVELOPMENT_',code),call.=FALSE)
ed_error_code <- function(e) {
  code <- conditionMessage(e)
  if(grepl('^(ESS_DEVELOPMENT|ORDINAL_ADAPTER|ORDINAL_SUPPORT)_[A-Z0-9_]+$',code)) code else
    'ESS_DEVELOPMENT_LIBRARY_ERROR'
}
ed_quiet <- function(expr) {
  warned <- FALSE
  discarded <- capture.output(value <- tryCatch(withCallingHandlers(expr,
    warning=function(w){warned<<-TRUE;invokeRestart('muffleWarning')},
    message=function(m)invokeRestart('muffleMessage')),
    error=function(e)stop(ed_error_code(e),call.=FALSE)))
  if(warned) ed_stop('LIBRARY_WARNING')
  value
}
ed_attempt <- function(fun) {
  tryCatch(list(status='EXECUTED',value=ed_quiet(fun()),code=NULL),
    error=function(e)list(status='FAILED',value=NULL,code=ed_error_code(e)))
}
ed_sha256 <- function(path) {
  if(length(path)!=1L || !is.character(path) || !file.exists(path)) ed_stop('SOURCE_PATH')
  value <- ed_quiet(system2('/usr/bin/sha256sum',shQuote(path),stdout=TRUE,stderr=FALSE))
  if(length(value)!=1L || !is.null(attr(value,'status'))) ed_stop('SOURCE_HASH')
  hash <- substr(value,1L,64L)
  if(!grepl('^[0-9a-f]{64}$',hash)) ed_stop('SOURCE_HASH')
  hash
}
ed_initialize <- function(project_root) {
  project <- normalizePath(project_root,mustWork=TRUE)
  namespace <- environment(ed_initialize)
  source(file.path(project,'pipeline/ordinal/develop-config.R'),local=namespace)
  cfg <- ed_default_config()
  for(path in names(cfg$source_pins)) {
    if(ed_sha256(file.path(project,path))!=cfg$source_pins[[path]]) ed_stop('SOURCE_PIN')
    source(file.path(project,path),local=namespace)
  }
  oa_runtime()
  if(!requireNamespace('jsonlite',quietly=TRUE) ||
     as.character(packageVersion('jsonlite'))!=cfg$runtime$jsonlite) ed_stop('JSON_VERSION')
  paths <- c('pipeline/ordinal/develop.R','pipeline/ordinal/develop-config.R',names(cfg$source_pins))
  pins <- setNames(lapply(paths,function(path)ed_sha256(file.path(project,path))),paths)
  list(config=cfg,source_pins=pins)
}
ed_validate_frame <- function(frame,cfg) {
  if(!is.data.frame(frame)||!identical(names(frame),cfg$input_columns)||nrow(frame)==0L)
    ed_stop('A_FRAME_COLUMNS')
  if(!is.numeric(frame$weight)||any(!is.finite(frame$weight))||any(frame$weight<=0)) ed_stop('A_WEIGHT')
  for(key in c('stratum','psu')) if(!is.numeric(frame[[key]])||any(!is.finite(frame[[key]]))||
      any(frame[[key]]!=floor(frame[[key]]))) ed_stop('A_DESIGN')
  for(id in cfg$items) if(!is.numeric(frame[[id]])||
    any(!is.na(frame[[id]])&(!is.finite(frame[[id]])|!frame[[id]]%in%cfg$manifest[[id]]))) ed_stop('A_CATEGORY')
  invisible(TRUE)
}
ed_model_syntax <- function(groups) paste(vapply(names(groups),function(name)
  paste0(name,' =~ ',paste(groups[[name]],collapse=' + ')),character(1)),collapse='\n')
ed_permutations <- function(v) {
  if(length(v)==1L)return(matrix(v,nrow=1L))
  do.call(rbind,lapply(seq_along(v),function(j)cbind(v[j],ed_permutations(v[-j]))))
}
ed_align <- function(reference,other) {
  l <- reference$loadings; z <- other$loadings; k <- ncol(l)
  if(!identical(rownames(l),rownames(z))||ncol(z)!=k) ed_stop('EFA_ALIGNMENT_SHAPE')
  permutations <- ed_permutations(seq_len(k));signs <- as.matrix(expand.grid(rep(list(c(-1,1)),k)))
  best <- NULL;best_error<-Inf
  for(p in seq_len(nrow(permutations)))for(s in seq_len(nrow(signs))) {
    perm<-permutations[p,];sgn<-signs[s,]
    aligned<-sweep(z[,perm,drop=FALSE],2L,sgn,'*')
    correlation<-other$correlation[perm,perm,drop=FALSE]*outer(sgn,sgn)
    error<-max(abs(aligned-l),abs(correlation-reference$correlation))
    if(error<best_error){best_error<-error;best<-list(loadings=aligned,correlation=correlation,
      permutation=as.integer(perm),sign=as.integer(sgn),max_difference=error)}
  }
  best
}
ed_expected_mapping <- function(solution,groups,tie_tolerance) {
  l<-solution$loadings;k<-ncol(l)
  if(length(groups)!=k||!identical(unlist(groups,use.names=FALSE),rownames(l))) ed_stop('EFA_MAPPING_SHAPE')
  permutations<-ed_permutations(seq_len(k));best<-NULL;best_count<- -1L;best_margin<- -Inf
  for(p in seq_len(nrow(permutations))) {
    perm<-permutations[p,];mapped<-l[,perm,drop=FALSE]
    sgn<-vapply(seq_len(k),function(j)if(sum(mapped[groups[[j]],j])>=0)1 else -1,numeric(1))
    mapped<-sweep(mapped,2L,sgn,'*');colnames(mapped)<-names(groups)
    target<-match(rownames(l),unlist(groups,use.names=FALSE))
    target<-rep(seq_len(k),lengths(groups))[target]
    largest<-logical(nrow(l));margin<-numeric(nrow(l))
    for(i in seq_len(nrow(l))) {
      competition<-if(k==1L)0 else max(abs(mapped[i,-target[i]]))
      margin[i]<-abs(mapped[i,target[i]])-competition
      largest[i]<-mapped[i,target[i]]>0 && margin[i]>tie_tolerance
    }
    count<-sum(largest);minimum<-min(margin)
    if(count>best_count||count==best_count&&minimum>best_margin) {
      correlation<-solution$correlation[perm,perm,drop=FALSE]*outer(sgn,sgn)
      dimnames(correlation)<-list(names(groups),names(groups))
      best<-list(passed=all(largest),items=rownames(mapped),factors=colnames(mapped),loadings=mapped,correlation=correlation,
        item_largest_positive=setNames(largest,rownames(l)),minimum_absolute_loading_gap=minimum,
        permutation=as.integer(perm),sign=as.integer(sgn))
      best_count<-count;best_margin<-minimum
    }
  }
  best
}
ed_efa_fit <- function(adapter,k,rotation,seed,cfg) {
  if(rotation=='geomin') return(oa_fit(adapter,NULL,efa_factors=k,rotation_seed=seed))
  model<-paste0(paste(paste0('efa("minimal")*e',seq_len(k)),collapse=' + '),
                ' =~ ',paste(cfg$items,collapse=' + '))
  th<-adapter$thresholds;names(th)<-names(adapter$moments)[seq_along(th)]
  attr(th,'th.idx')<-setNames(adapter$threshold_index,names(th))
  set.seed(seed)
  fit<-ed_quiet(lavaan::cfa(model=model,sample_cov=adapter$correlation,sample_th=th,
    sample_mean=setNames(rep(0,9L),cfg$items),sample_nobs=adapter$aggregate$n_complete,
    ordered=cfg$items,estimator='WLSMV',parameterization='theta',std_lv=TRUE,
    nacov=adapter$gamma,wls_v=adapter$wls_v,rotation=rotation,
    rotation_args=list(rstarts=cfg$efa$rstarts)))
  if(!isTRUE(lavaan::lavInspect(fit,'converged'))||!isTRUE(lavaan::lavInspect(fit,'post.check')))
    ed_stop('EFA_CONVERGENCE')
  if(lavaan::fitMeasures(fit,'df')<=0)ed_stop('EFA_DF')
  obs<-lavaan::lavInspect(fit,'wls.obs')
  if(!identical(names(obs),names(adapter$moments))||max(abs(obs-adapter$moments))>1e-7)
    ed_stop('EFA_MOMENT_IMPORT')
  for(pair in list(list('gamma',adapter$gamma),list('wls.v',adapter$wls_v))) {
    actual<-lavaan::lavInspect(fit,pair[[1]])
    if(!identical(dimnames(actual),dimnames(pair[[2]]))||max(abs(actual-pair[[2]]))>1e-7)
      ed_stop('EFA_MATRIX_IMPORT')
  }
  structure(list(private=fit,aggregate=list(df=unname(lavaan::fitMeasures(fit,'df')),
    converged=TRUE,postcheck=TRUE,efa_factors=k)),class='oa_fit')
}
ed_efa_solution <- function(fit) {
  loadings<-unclass(lavaan::lavInspect(fit$private,'std')$lambda)
  list(items=rownames(loadings),factors=colnames(loadings),loadings=loadings,
    correlation=unclass(lavaan::lavInspect(fit$private,'cor.lv')),df=fit$aggregate$df)
}
ed_efa_suite <- function(adapter,cfg) {
  public<-private<-list()
  for(k in cfg$efa$factors) {
    runs<-list(main=ed_attempt(function()ed_efa_fit(adapter,k,'geomin',cfg$efa$seed,cfg)),
      repeated=ed_attempt(function()ed_efa_fit(adapter,k,'geomin',cfg$efa$repeat_seed,cfg)),
      oblimin=ed_attempt(function()ed_efa_fit(adapter,k,'oblimin',cfg$efa$seed,cfg)))
    private[[as.character(k)]]<-lapply(runs,function(x)x$value)
    public_runs<-lapply(runs,function(x)if(x$status=='EXECUTED')
      list(status=x$status,solution=ed_efa_solution(x$value))else list(status=x$status,code=x$code))
    entry<-list(runs=public_runs,rotation_se='NOT_IMPLEMENTED_NO_CLAIM')
    if(all(vapply(runs,function(x)x$status=='EXECUTED',logical(1)))) {
      alignment<-ed_align(public_runs$main$solution,public_runs$repeated$solution)
      groups<-cfg$models[[paste0('M',k)]]
      mappings<-lapply(public_runs,function(x)ed_expected_mapping(x$solution,groups,cfg$efa$numerical_tie_tolerance))
      entry$repeat_alignment<-alignment
      entry$expected_mapping<-mappings
      entry$reproduced<-alignment$max_difference<=cfg$efa$alignment_max_difference
      entry$expected_mapping_passed<-all(vapply(mappings,function(x)x$passed,logical(1)))
      entry$eligible<-isTRUE(entry$reproduced)&&isTRUE(entry$expected_mapping_passed)
    } else entry$eligible<-FALSE
    public[[as.character(k)]]<-entry
  }
  list(aggregate=public,private=private)
}
ed_bound <- function(result,alpha=.05,family=1L,one_sided=FALSE) {
  if(!is.list(result)||!is.finite(result$estimate)||!is.finite(result$design_se)||result$design_se<0||family<1L)
    ed_stop('CRITERION_INTERVAL')
  critical<-qnorm(1-alpha/(if(one_sided)family else 2*family))
  list(estimate=result$estimate,design_se=result$design_se,lower=result$estimate-critical*result$design_se,
    upper=result$estimate+critical*result$design_se,critical=critical,
    family=as.integer(family),method=if(one_sided)'one-sided normal95 bound'else'two-sided normal95 Bonferroni interval')
}
ed_score_criteria <- function(sw,adapter,groups,std,cfg) {
  out<-list();alpha<-cfg$criteria$alpha
  for(factor in names(groups)) {
    ids<-groups[[factor]];k<-length(ids)
    score<-os_score(sw,cfg$manifest,ids);raw<-os_raw_score(adapter,cfg$manifest,ids)
    loadings<-setNames(lapply(ids,function(id)ed_bound(std$results[[paste0(factor,'=~',id)]],alpha,k)),ids)
    model_dom<-setNames(lapply(ids,function(id)ed_bound(score$results[[paste0('dominance:',id)]],alpha,k)),ids)
    raw_dom<-setNames(lapply(ids,function(id)ed_bound(raw$results[[paste0('dominance:',id)]],alpha,k)),ids)
    reliability<-ed_bound(score$results$reliability,alpha)
    checks<-c(loadings=all(vapply(loadings,function(x)x$lower>cfg$criteria$loading_lower_exclusive,logical(1))),
      reliability=reliability$lower>cfg$criteria$reliability_lower_exclusive,
      model_dominance=all(vapply(model_dom,function(x)x$upper<=cfg$criteria$dominance_upper_max,logical(1))),
      raw_dominance=all(vapply(raw_dom,function(x)x$upper<=cfg$criteria$dominance_upper_max,logical(1))))
    out[[factor]]<-list(items=ids,label=cfg$labels[[factor]],passed=all(checks),criteria=as.list(checks),
      failures=names(checks)[!checks],loadings=loadings,reliability=reliability,
      model_dominance=model_dom,raw_dominance=raw_dom,
      model_components=list(mean=score$results$mean,observed_variance=score$results$observed_variance,
        true_variance=score$results$true_variance,error_variance=score$results$error_variance,
        item_covariance=score$components$item_covariance,covariance_with_score=score$components$covariance_with_score),
      raw_components=list(mean=raw$results$mean,variance=raw$results$variance,
        item_covariance=raw$item_covariance,covariance_with_score=raw$covariance_with_score),
      limits=score$limits)
  }
  out
}
ed_model_evaluation <- function(adapter,groups,efa,cfg,diagnostic_only=FALSE) {
  fit<-oa_fit(adapter,ed_model_syntax(groups));sw<-os_sandwich(adapter,fit)
  std<-os_standardized(sw);rms<-os_residual_rms(sw)
  rms_bound<-if(rms$status=='NORMAL_DELTA_APPROXIMATION')ed_bound(rms,cfg$criteria$alpha,one_sided=TRUE)else
    list(status='INCONCLUSIVE',reason=rms$status,estimate=rms$estimate)
  scores<-ed_score_criteria(sw,adapter,groups,std,cfg)
  count<-length(groups);pairs<-which(lower.tri(matrix(0,count,count)),arr.ind=TRUE)
  correlations<-list()
  if(nrow(pairs)>0L)for(i in seq_len(nrow(pairs))) {
    pair<-pairs[i,];id<-paste0(names(groups)[pair[2]],'~~',names(groups)[pair[1]])
    interval<-ed_bound(std$results[[id]],cfg$criteria$alpha,nrow(pairs))
    interval$passed<-interval$upper<cfg$criteria$correlation_upper_exclusive
    correlations[[id]]<-interval
  }
  rms_pass<-is.null(rms_bound$status)&&rms_bound$upper<=cfg$criteria$rms_one_sided_upper_max
  correlation_pass<-all(vapply(correlations,function(x)x$passed,logical(1)))
  loading_points<-matrix(0,length(cfg$items),count,dimnames=list(cfg$items,names(groups)))
  correlation_points<-diag(count);dimnames(correlation_points)<-list(names(groups),names(groups))
  for(factor in names(groups))for(id in groups[[factor]])
    loading_points[id,factor]<-std$results[[paste0(factor,'=~',id)]]$estimate
  if(nrow(pairs)>0L)for(i in seq_len(nrow(pairs))) {
    pair<-pairs[i,];id<-paste0(names(groups)[pair[2]],'~~',names(groups)[pair[1]])
    correlation_points[pair[1],pair[2]]<-correlation_points[pair[2],pair[1]]<-std$results[[id]]$estimate
  }
  criteria<-c(efa=isTRUE(efa$eligible),rms=rms_pass,all_candidate_factor_pairs=correlation_pass,
    minimum_dimensions=count>=cfg$criteria$minimum_scores&&!diagnostic_only)
  diagnostics<-ed_attempt(function()as.list(lavaan::fitMeasures(fit$private,
    c('chisq','df','pvalue','chisq.scaled','df.scaled','pvalue.scaled','cfi.scaled','tli.scaled','rmsea.scaled','srmr'))))
  list(aggregate=list(status='EXECUTED',fit=fit$aggregate,metric=cfg$metric,sandwich=sw$aggregate,
    standardized_parameters=std$results,standardized_points=list(items=cfg$items,factors=names(groups),
      loadings=loading_points,correlation=correlation_points),rms=rms_bound,correlations=correlations,
    model_criteria=as.list(criteria),eligible=all(criteria),scores=scores,
    diagnostics=if(diagnostics$status=='EXECUTED')list(status='EXECUTED',values=diagnostics$value)else
      list(status='UNAVAILABLE',code=diagnostics$code)),private=fit$private)
}
ed_select <- function(models,cfg) {
  for(name in cfg$criteria$selection_order) {
    candidate<-models[[name]]
    if(is.null(candidate)||candidate$status!='EXECUTED'||!isTRUE(candidate$eligible))next
    scores<-names(candidate$scores)[vapply(candidate$scores,function(x)isTRUE(x$passed),logical(1))]
    if(length(scores)>=cfg$criteria$minimum_scores)return(list(status='CANDIDATE_SELECTED_FOR_FREEZE_REVIEW',
      model=name,scores=scores,rule='M2 first if at least two complete fixed scores pass, otherwise M3'))
  }
  list(status='NO_PROFILE_CANDIDATE',model=NULL,scores=character(),
    rule='No eligible model with at least two scores; M1 cannot satisfy minimum dimensions')
}
ed_analyse <- function(frame,config=ed_default_config(),source_pins=list()) {
  cfg<-config
  if(!identical(cfg,ed_default_config()))ed_stop('CONFIG_NOT_FIXED')
  allowed_pins<-c('pipeline/ordinal/develop.R','pipeline/ordinal/develop-config.R',names(cfg$source_pins))
  if(!is.list(source_pins)||!identical(names(source_pins),allowed_pins)||
      !all(vapply(source_pins,function(x)is.character(x)&&length(x)==1L&&
        grepl('^[0-9a-f]{64}$',x),logical(1))))ed_stop('SOURCE_PIN_WHITELIST')
  ed_validate_frame(frame,cfg)
  adapter<-oa_fixed_metric(oa_build(frame[cfg$items],cfg$manifest,frame$weight,frame$psu,frame$stratum,
                                  rep(TRUE,nrow(frame))))
  efa<-ed_efa_suite(adapter,cfg);models<-fits<-list()
  for(name in names(cfg$models)) {
    result<-ed_attempt(function()ed_model_evaluation(adapter,cfg$models[[name]],
      efa$aggregate[[as.character(length(cfg$models[[name]]))]],cfg,diagnostic_only=name=='M1'))
    if(result$status=='EXECUTED') {
      models[[name]]<-result$value$aggregate;fits[[name]]<-result$value$private
    } else models[[name]]<-list(status='FAILED',code=result$code,eligible=FALSE)
  }
  complete<-complete.cases(frame[cfg$items])
  counts<-c(oa_public(adapter),list(item_missing_counts=setNames(lapply(cfg$items,function(id)sum(is.na(frame[[id]]))),cfg$items),
    weighted_missing_mass=sum(frame$weight[!complete])/sum(frame$weight),
    contributing_complete_psus=nrow(unique(frame[complete,c('stratum','psu'),drop=FALSE]))))
  aggregate<-list(schema='life93-A-development-aggregate-1',scope='A exploratory development; no publication or scientific approval',
    config=cfg,source_code_pins=source_pins,counts=counts,
    point_moments=list(items=cfg$items,labels=names(adapter$moments),
      thresholds=setNames(adapter$thresholds,names(adapter$moments)[seq_along(adapter$thresholds)]),
      correlation=adapter$correlation),efa=efa$aggregate,models=models,
    selection=ed_select(models,cfg),limits=cfg$limits)
  structure(list(aggregate=aggregate,private=list(cfa_fits=fits,efa_fits=efa$private)),class='ed_analysis')
}
ed_public <- function(result) {
  if(!inherits(result,'ed_analysis'))ed_stop('RESULT_CLASS')
  result$aggregate[c('schema','scope','config','source_code_pins','counts','point_moments','efa','models','selection','limits')]
}
ed_authorized <- function(authorization) {
  if(!is.list(authorization)||!identical(authorization$decision,'ACCEPTED_BOUNDED')||
    !identical(authorization$arm,'A')||!identical(authorization$wrapper_verified,TRUE))ed_stop('A_GATE_REQUIRED')
  invisible(TRUE)
}
ed_read_A <- function(path,cfg,authorization) {
  ed_authorized(authorization)
  raw<-ed_quiet(utils::read.csv(path,colClasses='character',check.names=FALSE,na.strings='NA'))
  if(!identical(names(raw),cfg$input_columns))ed_stop('A_FRAME_COLUMNS')
  for(name in names(raw)) {
    if(name%in%c('stratum','psu')&&any(is.na(raw[[name]])|!grepl('^-?[0-9]+$',raw[[name]])))ed_stop('A_DESIGN_TOKEN')
    raw[[name]]<-ed_quiet(as.numeric(raw[[name]]))
  }
  ed_validate_frame(raw,cfg);raw
}
ed_run_file <- function(project_root,input_A_csv,private_output_dir,authorization,retain_fits=TRUE) {
  ed_authorized(authorization)
  initialized<-ed_initialize(project_root)
  output<-normalizePath(private_output_dir,mustWork=TRUE)
  if(!dir.exists(output)||bitwAnd(as.integer(file.info(output)$mode),511L)!=448L)ed_stop('PRIVATE_OUTPUT_MODE')
  paths<-file.path(output,c('development-aggregate.private.json','development-config.private.json'))
  reserved<-c(paths,if(isTRUE(retain_fits))file.path(output,paste0('cfa-',names(initialized$config$models),'.private.rds')))
  if(any(file.exists(reserved)))ed_stop('DO_NOT_OVERWRITE')
  frame<-ed_read_A(input_A_csv,initialized$config,authorization)
  result<-ed_quiet(ed_analyse(frame,initialized$config,initialized$source_pins))
  ed_quiet(jsonlite::write_json(ed_public(result),paths[1],auto_unbox=TRUE,pretty=TRUE,digits=16,na='null'))
  ed_quiet(jsonlite::write_json(initialized$config,paths[2],auto_unbox=TRUE,pretty=TRUE,digits=16,na='null'))
  if(!all(ed_quiet(Sys.chmod(paths,'0600'))))ed_stop('PRIVATE_FILE_MODE')
  if(isTRUE(retain_fits)) {
    for(name in names(result$private$cfa_fits)) {
      path<-file.path(output,paste0('cfa-',name,'.private.rds'))
      ed_quiet(saveRDS(result$private$cfa_fits[[name]],path))
      if(!isTRUE(ed_quiet(Sys.chmod(path,'0600'))))ed_stop('PRIVATE_FILE_MODE')
    }
  }
  cat('ESS_DEVELOPMENT_A_EXECUTED_PRIVATE_OUTPUT\n')
  invisible(ed_public(result))
}
ed_main <- function(project_root,input_A_csv,private_output_dir,authorization,retain_fits=TRUE) {
  tryCatch({ed_quiet(ed_run_file(project_root,input_A_csv,private_output_dir,authorization,retain_fits));
    cat('ESS_DEVELOPMENT_A_EXECUTED_PRIVATE_OUTPUT\n');0L},
    error=function(e){cat(ed_error_code(e),'\n',sep='');1L})
}
