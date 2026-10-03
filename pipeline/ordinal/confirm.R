# Fixed-model confirmation only. No discovery, competition, repairs or publication.
ec_stop<-function(code)stop(paste0('ESS_CONFIRMATORY_',code),call.=FALSE)
ec_error_code<-function(e) {
  code<-conditionMessage(e)
  if(grepl('^(ESS_CONFIRMATORY|ESS_DEVELOPMENT|ORDINAL_ADAPTER|ORDINAL_SUPPORT)_[A-Z0-9_]+$',code))code else
    'ESS_CONFIRMATORY_LIBRARY_ERROR'
}
ec_quiet<-function(expr) {
  warned<-FALSE
  discarded<-capture.output(value<-tryCatch(withCallingHandlers(expr,
    warning=function(w){warned<<-TRUE;invokeRestart('muffleWarning')},
    message=function(m)invokeRestart('muffleMessage')),
    error=function(e)stop(ec_error_code(e),call.=FALSE)))
  if(warned)ec_stop('LIBRARY_WARNING')
  value
}
ec_attempt<-function(fun)tryCatch(list(status='EXECUTED',value=ec_quiet(fun()),code=NULL),
  error=function(e)list(status='FAILED',value=NULL,code=ec_error_code(e)))
ec_sha256<-function(path) {
  if(!is.character(path)||length(path)!=1L||!file.exists(path))ec_stop('SOURCE_PATH')
  value<-ec_quiet(system2('/usr/bin/sha256sum',shQuote(path),stdout=TRUE,stderr=FALSE))
  if(length(value)!=1L||!is.null(attr(value,'status'))||!grepl('^[0-9a-f]{64}$',substr(value,1L,64L)))
    ec_stop('SOURCE_HASH')
  substr(value,1L,64L)
}
ec_dependency_pins<-function()list(
  'pipeline/ordinal/develop.R'='d1b725b05ba43d9a3edbe4964e05ae0d5365ef951944fe1c83284967ff800e74',
  'pipeline/ordinal/develop-config.R'='44a74f0e59645d047f2bdc4508cc0058d0dd80ffb4a67a8963ee9e84f0f429b0',
  'pipeline/ordinal/adapter_v2.R'='8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b',
  'pipeline/ordinal/support.R'='b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22')
ec_initialize<-function(project_root) {
  project<-normalizePath(project_root,mustWork=TRUE);namespace<-environment(ec_initialize)
  for(path in names(ec_dependency_pins()))
    if(ec_sha256(file.path(project,path))!=ec_dependency_pins()[[path]])ec_stop('DEPENDENCY_PIN')
  source(file.path(project,'pipeline/ordinal/develop.R'),local=namespace)
  initialized<-ed_initialize(project)
  initialized$pins<-c(initialized$source_pins,list('pipeline/ordinal/confirm.R'=
    ec_sha256(file.path(project,'pipeline/ordinal/confirm.R'))))
  initialized$source_pins<-NULL;initialized
}
# JSON integer/double and object-key order are representational, not a config change.
ec_equal<-function(x,y) {
  if(is.list(y)) {
    if(!is.list(x)||length(x)!=length(y))return(FALSE)
    if(is.null(names(y)))return(is.null(names(x))&&all(vapply(seq_along(y),function(i)ec_equal(x[[i]],y[[i]]),logical(1))))
    if(is.null(names(x))||anyDuplicated(names(x))||!setequal(names(x),names(y)))return(FALSE)
    return(all(vapply(names(y),function(name)ec_equal(x[[name]],y[[name]]),logical(1))))
  }
  if(is.numeric(y))return(is.numeric(x)&&identical(names(x),names(y))&&identical(as.numeric(x),as.numeric(y)))
  identical(x,y)
}
ec_validate_pins<-function(pins) {
  expected<-ec_dependency_pins();allowed<-c(names(expected),'pipeline/ordinal/confirm.R')
  if(!is.list(pins)||is.null(names(pins))||anyDuplicated(names(pins))||!setequal(names(pins),allowed)||
      !all(vapply(pins,function(x)is.character(x)&&length(x)==1L&&grepl('^[0-9a-f]{64}$',x),logical(1))))
    ec_stop('SOURCE_PIN_WHITELIST')
  if(!ec_equal(pins[names(expected)],expected))ec_stop('SOURCE_PIN')
  invisible(TRUE)
}
ec_validate_scores<-function(scores,allowed,minimum=2L) {
  if(!is.character(scores)||length(scores)<minimum||anyNA(scores)||anyDuplicated(scores)||
      !identical(scores,allowed[allowed%in%scores]))ec_stop('FROZEN_SCORES')
  invisible(TRUE)
}
ec_validate_freeze<-function(freeze,cfg,pins) {
  if(!ec_equal(cfg,ed_default_config()))ec_stop('CONFIG_NOT_FIXED')
  ec_validate_pins(pins)
  keys<-c('schema','model','scores','items','groups','config','source_code_pins','a_result')
  if(!is.list(freeze)||is.null(names(freeze))||anyDuplicated(names(freeze))||!setequal(names(freeze),keys)||
      !identical(freeze$schema,'life93-model-freeze-1'))ec_stop('FREEZE_SCHEMA')
  if(!is.character(freeze$model)||length(freeze$model)!=1L||!freeze$model%in%c('M2','M3'))ec_stop('FROZEN_MODEL')
  if(!identical(freeze$items,cfg$items)||!ec_equal(freeze$groups,cfg$models[[freeze$model]]))ec_stop('FROZEN_ITEMS_GROUPS')
  if(!ec_equal(freeze$config,cfg))ec_stop('FROZEN_CONFIG')
  if(!ec_equal(freeze$source_code_pins,ec_dependency_pins()))ec_stop('FROZEN_CODE_PINS')
  if(!is.list(freeze$a_result)||is.null(names(freeze$a_result))||anyDuplicated(names(freeze$a_result))||
      !setequal(names(freeze$a_result),c('path','sha256'))||
      !identical(freeze$a_result$path,'reports/phasen/01-a-entwicklung.json')||
      !is.character(freeze$a_result$sha256)||length(freeze$a_result$sha256)!=1L||
      !grepl('^[0-9a-f]{64}$',freeze$a_result$sha256))ec_stop('A_RESULT_REFERENCE')
  ec_validate_scores(freeze$scores,names(cfg$models[[freeze$model]]),cfg$criteria$minimum_scores)
  invisible(TRUE)
}
ec_selected_efa<-function(adapter,groups,cfg) {
  k<-length(groups)
  runs<-list(main=ec_attempt(function()ed_efa_fit(adapter,k,'geomin',cfg$efa$seed,cfg)),
    repeated=ec_attempt(function()ed_efa_fit(adapter,k,'geomin',cfg$efa$repeat_seed,cfg)),
    oblimin=ec_attempt(function()ed_efa_fit(adapter,k,'oblimin',cfg$efa$seed,cfg)))
  public<-lapply(runs,function(x)if(x$status=='EXECUTED')
    list(status=x$status,solution=ed_efa_solution(x$value))else list(status=x$status,code=x$code))
  entry<-list(factor_count=k,runs=public,rotation_se='NOT_IMPLEMENTED_NO_CLAIM',eligible=FALSE)
  if(all(vapply(runs,function(x)x$status=='EXECUTED',logical(1)))) {
    mapping<-ec_attempt(function() {
      alignment<-ed_align(public$main$solution,public$repeated$solution)
      mappings<-lapply(public,function(x)ed_expected_mapping(x$solution,groups,cfg$efa$numerical_tie_tolerance))
      list(repeat_alignment=alignment,expected_mapping=mappings,
        reproduced=alignment$max_difference<=cfg$efa$alignment_max_difference,
        expected_mapping_passed=all(vapply(mappings,function(x)x$passed,logical(1))))
    })
    if(mapping$status=='EXECUTED') {
      entry<-c(entry,mapping$value);entry$eligible<-isTRUE(entry$reproduced)&&isTRUE(entry$expected_mapping_passed)
    }else entry$mapping_failure<-mapping$code
  }
  entry
}
ec_model_evaluation<-function(adapter,groups,scores,efa,cfg) {
  fit<-oa_fit(adapter,ed_model_syntax(groups));sw<-os_sandwich(adapter,fit)
  std<-os_standardized(sw);rms<-os_residual_rms(sw)
  rms_bound<-if(rms$status=='NORMAL_DELTA_APPROXIMATION')ed_bound(rms,cfg$criteria$alpha,one_sided=TRUE)else
    list(status='INCONCLUSIVE',reason=rms$status,estimate=rms$estimate)
  score_results<-ed_score_criteria(sw,adapter,groups[scores],std,cfg)
  count<-length(groups);pairs<-which(lower.tri(matrix(0,count,count)),arr.ind=TRUE);correlations<-list()
  for(i in seq_len(nrow(pairs))) {
    pair<-pairs[i,];id<-paste0(names(groups)[pair[2]],'~~',names(groups)[pair[1]])
    interval<-ed_bound(std$results[[id]],cfg$criteria$alpha,nrow(pairs))
    interval$passed<-interval$lower>cfg$criteria$correlation_lower_exclusive&&
      interval$upper<cfg$criteria$correlation_upper_exclusive;correlations[[id]]<-interval
  }
  loading_points<-matrix(0,length(cfg$items),count,dimnames=list(cfg$items,names(groups)))
  correlation_points<-diag(count);dimnames(correlation_points)<-list(names(groups),names(groups))
  for(factor in names(groups))for(id in groups[[factor]])
    loading_points[id,factor]<-std$results[[paste0(factor,'=~',id)]]$estimate
  for(i in seq_len(nrow(pairs))) {
    pair<-pairs[i,];id<-paste0(names(groups)[pair[2]],'~~',names(groups)[pair[1]])
    correlation_points[pair[1],pair[2]]<-correlation_points[pair[2],pair[1]]<-std$results[[id]]$estimate
  }
  criteria<-c(efa=isTRUE(efa$eligible),
    rms=is.null(rms_bound$status)&&rms_bound$upper<=cfg$criteria$rms_one_sided_upper_max,
    all_candidate_factor_pairs=all(vapply(correlations,function(x)x$passed,logical(1))),
    minimum_dimensions=count>=cfg$criteria$minimum_scores)
  diagnostics<-ec_attempt(function()as.list(lavaan::fitMeasures(fit$private,
    c('chisq','df','pvalue','chisq.scaled','df.scaled','pvalue.scaled','cfi.scaled','tli.scaled','rmsea.scaled','srmr'))))
  context<-sw$private$context
  fitted_moments<-os_at(context,context$x)$moments
  threshold_index<-grepl('|',names(fitted_moments),fixed=TRUE)
  list(status='EXECUTED',fit=fit$aggregate,metric=cfg$metric,sandwich=sw$aggregate,
    standardized_parameters=std$results,standardized_points=list(items=cfg$items,factors=names(groups),
      loadings=loading_points,correlation=correlation_points,
      thresholds=unname(fitted_moments[threshold_index]),
      threshold_labels=names(fitted_moments)[threshold_index],
      threshold_observed_max_difference=max(abs(fitted_moments[threshold_index]-adapter$moments[threshold_index]))),
    rms=rms_bound,correlations=correlations,
    model_criteria=as.list(criteria),eligible=all(criteria),scores=score_results,
    diagnostics=if(diagnostics$status=='EXECUTED')list(status='EXECUTED',values=diagnostics$value)else
      list(status='UNAVAILABLE',code=diagnostics$code))
}
ec_decision<-function(model,frozen_scores,cfg) {
  global<-identical(model$status,'EXECUTED')&&isTRUE(model$eligible)
  passing<-if(identical(model$status,'EXECUTED'))frozen_scores[vapply(model$scores[frozen_scores],
    function(x)isTRUE(x$passed),logical(1))]else character()
  allowed<-global&&length(passing)>=cfg$criteria$minimum_scores
  list(status=if(allowed)'CRITERIA_PASSED_PENDING_RESULT_REVIEW'else'NO_PUBLIC_PROFILE',
    global_model_passed=global,score_criteria_passed=passing,
    retained_scores=if(allowed)passing else character(),suppressed_scores=if(allowed)
      frozen_scores[!frozen_scores%in%passing]else frozen_scores,
    evaluated_frozen_scores=frozen_scores,minimum_scores=cfg$criteria$minimum_scores,
    rule='Only previously frozen scores may remain; no competing model or new score can be selected')
}
ec_analyse<-function(frame,freeze,cfg,pins,arm='B',previously_retained_scores=NULL) {
  ec_validate_freeze(freeze,cfg,pins);cfg<-ed_default_config()
  if(!is.character(arm)||length(arm)!=1L||!arm%in%c('B','FULL'))ec_stop('ARM')
  scores<-freeze$scores
  if(arm=='FULL') {
    ec_validate_scores(previously_retained_scores,freeze$scores,cfg$criteria$minimum_scores)
    scores<-previously_retained_scores
  }else if(!is.null(previously_retained_scores))ec_stop('B_SCORE_OVERRIDE')
  ed_validate_frame(frame,cfg)
  adapter<-oa_fixed_metric(oa_build(frame[cfg$items],cfg$manifest,frame$weight,frame$psu,frame$stratum,
    rep(TRUE,nrow(frame))))
  efa<-ec_selected_efa(adapter,freeze$groups,cfg)
  attempt<-ec_attempt(function()ec_model_evaluation(adapter,freeze$groups,scores,efa,cfg))
  model<-if(attempt$status=='EXECUTED')attempt$value else list(status='FAILED',code=attempt$code,eligible=FALSE)
  complete<-complete.cases(frame[cfg$items])
  counts<-c(oa_public(adapter),list(item_missing_counts=setNames(lapply(cfg$items,function(id)sum(is.na(frame[[id]]))),cfg$items),
    weighted_missing_mass=sum(frame$weight[!complete])/sum(frame$weight),
    contributing_complete_psus=nrow(unique(frame[complete,c('stratum','psu'),drop=FALSE]))))
  aggregate<-list(schema='life93-fixed-model-confirmation-aggregate-1',arm=arm,
    scope=if(arm=='B')'B fixed-model confirmation; result/publication review still required'else
      'Full-DE fixed-model transfer after completed B; includes A/B and is not independent confirmation',
    freeze=freeze,config=cfg,source_code_pins=pins,counts=counts,
    point_moments=list(items=cfg$items,labels=names(adapter$moments),thresholds=adapter$thresholds,correlation=adapter$correlation),
    efa=efa,model_name=freeze$model,model=model,confirmation=ec_decision(model,scores,cfg),
    limits=c(cfg$limits[c(1:4)],'Frozen A model and score set; no B competition or parameter rescue',
      'Author config status is not evidence of either freeze authority or empirical/result approval'))
  structure(list(aggregate=aggregate),class='ec_analysis')
}
ec_public<-function(result) {
  if(!inherits(result,'ec_analysis'))ec_stop('RESULT_CLASS')
  result$aggregate[c('schema','arm','scope','freeze','config','source_code_pins','counts','point_moments',
    'efa','model_name','model','confirmation','limits')]
}
ec_authorized<-function(authorization) {
  if(!is.list(authorization)||!identical(authorization$decision,'ACCEPTED_BOUNDED')||
      !identical(authorization$wrapper_verified,TRUE)||!is.character(authorization$arm)||
      length(authorization$arm)!=1L||!authorization$arm%in%c('B','FULL'))ec_stop('GATE_REQUIRED')
  if(authorization$arm=='FULL'&&!identical(authorization$B_step_completed,TRUE))ec_stop('FULL_B_REQUIRED')
  if(!is.character(authorization$freeze_sha256)||length(authorization$freeze_sha256)!=1L||
      !grepl('^[0-9a-f]{64}$',authorization$freeze_sha256))ec_stop('FREEZE_BINDING_REQUIRED')
  invisible(TRUE)
}
ec_verify_A_reference<-function(project_root,freeze,authorization) {
  ec_authorized(authorization);project<-normalizePath(project_root,mustWork=TRUE)
  base<-project
  if(identical(authorization$syntheticFake,TRUE)) {
    relative<-authorization$synthetic_public_root
    if(!is.character(relative)||length(relative)!=1L||!grepl('^outputs/loop/[A-Za-z0-9_/-]+$',relative))
      ec_stop('SYNTHETIC_REFERENCE_ROOT')
    base<-normalizePath(file.path(project,relative),mustWork=TRUE)
    allowed<-paste0(normalizePath(file.path(project,'outputs/loop'),mustWork=TRUE),'/')
    if(!startsWith(paste0(base,'/'),allowed))ec_stop('SYNTHETIC_REFERENCE_ROOT')
  }
  reference<-file.path(base,freeze$a_result$path)
  if(!file.exists(reference)||ec_sha256(reference)!=freeze$a_result$sha256)ec_stop('A_RESULT_BINDING')
  invisible(TRUE)
}
ec_read_freeze<-function(path,cfg,pins,authorization,project_root) {
  ec_authorized(authorization)
  if(ec_sha256(path)!=authorization$freeze_sha256)ec_stop('FREEZE_BINDING')
  freeze<-ec_quiet(jsonlite::fromJSON(path,simplifyVector=TRUE))
  ec_validate_freeze(freeze,cfg,pins)
  ec_verify_A_reference(project_root,freeze,authorization);freeze
}
ec_read_frame<-function(path,cfg,authorization) {
  ec_authorized(authorization)
  raw<-ec_quiet(utils::read.csv(path,colClasses='character',check.names=FALSE,na.strings='NA'))
  if(!identical(names(raw),cfg$input_columns))ec_stop('FRAME_COLUMNS')
  for(name in names(raw)) {
    if(name%in%c('stratum','psu')&&any(is.na(raw[[name]])|!grepl('^-?[0-9]+$',raw[[name]])))ec_stop('DESIGN_TOKEN')
    raw[[name]]<-ec_quiet(as.numeric(raw[[name]]))
  }
  ed_validate_frame(raw,cfg);raw
}
ec_run_file<-function(project_root,input_csv,freeze_path,private_output_dir,authorization) {
  ec_authorized(authorization);initialized<-ec_initialize(project_root)
  output<-normalizePath(private_output_dir,mustWork=TRUE)
  if(!dir.exists(output)||bitwAnd(as.integer(file.info(output)$mode),511L)!=448L)ec_stop('PRIVATE_OUTPUT_MODE')
  paths<-file.path(output,c('confirmation-aggregate.private.json','confirmation-config.private.json'))
  if(any(file.exists(paths)))ec_stop('DO_NOT_OVERWRITE')
  freeze<-ec_read_freeze(freeze_path,initialized$config,initialized$pins,authorization,project_root)
  previous<-if(authorization$arm=='FULL')authorization$B_retained_scores else NULL
  if(authorization$arm=='FULL')ec_validate_scores(previous,freeze$scores,initialized$config$criteria$minimum_scores)
  frame<-ec_read_frame(input_csv,initialized$config,authorization)
  result<-ec_quiet(ec_analyse(frame,freeze,initialized$config,initialized$pins,
    authorization$arm,previous))
  ec_quiet(jsonlite::write_json(ec_public(result),paths[1],auto_unbox=TRUE,pretty=TRUE,digits=16,na='null'))
  ec_quiet(jsonlite::write_json(initialized$config,paths[2],auto_unbox=TRUE,pretty=TRUE,digits=16,na='null'))
  if(!all(ec_quiet(Sys.chmod(paths,'0600'))))ec_stop('PRIVATE_FILE_MODE')
  invisible(ec_public(result))
}
ec_main<-function(project_root,input_csv,freeze_path,private_output_dir,authorization) {
  tryCatch({ec_quiet(ec_run_file(project_root,input_csv,freeze_path,private_output_dir,authorization));
    cat('ESS_CONFIRMATORY_',authorization$arm,'_EXECUTED_PRIVATE_OUTPUT\n',sep='');0L},
    error=function(e){cat(ec_error_code(e),'\n',sep='');1L})
}
