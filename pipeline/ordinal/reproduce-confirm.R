# Reproducible invented B/FULL probes. No original-data input or public copying.
args<-commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==3L,identical(Sys.getenv('HOME'),args[[3]]))
project<-normalizePath(args[[1]],mustWork=TRUE);own<-normalizePath(args[[2]],mustWork=TRUE)
stopifnot(identical(own,Sys.getenv('ESS_RUNTIME_OUTPUT')))
source(file.path(project,'pipeline/ordinal/confirm.R'))
init<-ec_initialize(project);cfg<-init$config;pins<-init$pins
RNGkind('Mersenne-Twister','Inversion','Rejection')
checks<-list();check<-function(name,value)checks[[name]]<<-isTRUE(value)
save_json<-function(value,name) {
  path<-file.path(own,name);stopifnot(!file.exists(path))
  jsonlite::write_json(value,path,auto_unbox=TRUE,pretty=TRUE,digits=16,na='null')
  stopifnot(Sys.chmod(path,'0600'))
}
error_code<-function(expr)tryCatch({force(expr);NA_character_},error=ec_error_code)
freeze_mock<-function(model,scores=names(cfg$models[[model]]))list(schema='life93-model-freeze-1',
  model=model,scores=scores,items=cfg$items,groups=cfg$models[[model]],config=cfg,
  source_code_pins=ec_dependency_pins(),a_result=list(path='reports/phasen/01-a-entwicklung.json',
  sha256=paste(rep('a',64),collapse='')))

# Same invented fixture and seeds as the bounded earlier confirmation probes.
synthetic_frame<-function(kind,seed) {
  stopifnot(kind%in%c('M2','M3','weakH'));set.seed(seed)
  g<-192L;size<-40L;n<-g*size;psu<-rep(seq_len(g),each=size)
  dimensions<-if(kind=='M2')2L else 3L
  eta<-matrix(rnorm(n*dimensions),n,dimensions)
  eta<-sqrt(.9)*eta+sqrt(.1)*rnorm(n)
  clusters<-matrix(rnorm(g*dimensions),g,dimensions)
  eta<-sqrt(.96)*eta+sqrt(.04)*clusters[psu,,drop=FALSE]
  factor<-if(kind=='M2')c(rep(1L,3L),rep(2L,6L))else rep(1:3,each=3L)
  loads<-rep(.82,9L);if(kind=='weakH')loads[1:3]<-.25
  x<-matrix(rnorm(n*9L),n,9L)
  x<-sweep(x,2L,sqrt(1-loads^2),'*')+sweep(eta[,factor],2L,loads,'*')
  frame<-data.frame(stratum=rep(rep(1:4,each=g/4),each=size),psu=psu,weight=runif(n,.8,1.2))
  for(j in seq_len(9L)) {
    breaks<-qnorm(seq(1/cfg$categories[j],1-1/cfg$categories[j],length.out=cfg$categories[j]-1L))
    frame[[cfg$items[j]]]<-as.integer(findInterval(x[,j],breaks))
    frame[[cfg$items[j]]][psu<=4L]<-NA_integer_
  }
  frame
}

f2<-freeze_mock('M2');f3<-freeze_mock('M3');fzf<-freeze_mock('M3',c('Z','F'))
check('actual frozen dependency pins',ec_equal(pins[names(ec_dependency_pins())],ec_dependency_pins()))
check('fixed RMS one-sided normal95',ed_bound(list(estimate=.02,design_se=.01),one_sided=TRUE)$critical==qnorm(.95))
check('fixed complete3 correlation family',ed_bound(list(estimate=.2,design_se=.01),family=3)$critical==qnorm(1-.05/6))
bad<-f3;bad$scores<-c('F','Z')
check('reordered frozen score set rejected',error_code(ec_validate_freeze(bad,cfg,pins))=='ESS_CONFIRMATORY_FROZEN_SCORES')
bad<-f3;bad$model<-'M1'
check('M1 freeze rejected',error_code(ec_validate_freeze(bad,cfg,pins))=='ESS_CONFIRMATORY_FROZEN_MODEL')

original_efa<-ed_efa_fit;original_fit<-oa_fit;efa_calls<-integer();cfa_calls<-character()
ed_efa_fit<-function(adapter,k,rotation,seed,cfg) {
  efa_calls<<-c(efa_calls,k);original_efa(adapter,k,rotation,seed,cfg)
}
oa_fit<-function(adapter,model,efa_factors=NULL,rotation_seed=2026100313L) {
  if(is.null(efa_factors))cfa_calls<<-c(cfa_calls,model)
  original_fit(adapter,model,efa_factors,rotation_seed)
}
scenarios<-list(M2=list(kind='M2',seed=2026100341L,freeze=f2,expected=c('H','ZF')),
  M3=list(kind='M3',seed=2026100342L,freeze=f3,expected=c('H','Z','F')),
  weakH_all=list(kind='weakH',seed=2026100326L,freeze=f3,expected=c('Z','F')),
  weakH_ZF=list(kind='weakH',seed=2026100326L,freeze=fzf,expected=c('Z','F')),
  strongH_ZF=list(kind='M3',seed=2026100342L,freeze=fzf,expected=c('Z','F')))
results<-list()
for(name in names(scenarios)) {
  spec<-scenarios[[name]];efa_calls<-integer();cfa_calls<-character()
  frame<-synthetic_frame(spec$kind,spec$seed)
  result<-ec_public(ec_quiet(ec_analyse(frame,spec$freeze,cfg,pins)))
  results[[name]]<-result;save_json(result,paste0(name,'-aggregate.synthetic.json'))
  check(paste(name,'exact chosen-k three EFA calls'),identical(efa_calls,rep(length(spec$freeze$groups),3L)))
  check(paste(name,'exactly one frozen CFA'),identical(cfa_calls,ed_model_syntax(spec$freeze$groups)))
  check(paste(name,'nine-item domain and original null PSUs'),result$counts$n_design==7680L&&
    result$counts$n_complete==7520L&&result$counts$psus==192L&&result$counts$strata==4L&&result$counts$zero_psus==4L)
  check(paste(name,'actual fixed criterion pass'),result$model$status=='EXECUTED'&&result$model$eligible&&
    result$confirmation$status=='CRITERIA_PASSED_PENDING_RESULT_REVIEW')
  check(paste(name,'actual retained subset'),identical(result$confirmation$retained_scores,spec$expected))
  check(paste(name,'no competitor or reselection'),is.null(result$models)&&is.null(result$selection)&&
    result$model_name==spec$freeze$model&&identical(names(result$model$scores),spec$freeze$scores))
  check(paste(name,'fitted threshold vector and labels51'),length(result$model$standardized_points$thresholds)==51L&&
    identical(result$model$standardized_points$threshold_labels,result$point_moments$labels[1:51]))
}
ed_efa_fit<-original_efa;oa_fit<-original_fit
check('weak H truly suppressed',!results$weakH_all$model$scores$H$passed&&
  results$weakH_all$model$scores$H$reliability$lower<=.5&&identical(results$weakH_all$confirmation$suppressed_scores,'H'))
check('strong H cannot restore unfrozen score',is.null(results$strongH_ZF$model$scores$H))

frame<-synthetic_frame('M3',2026100342L)
adapter<-oa_fixed_metric(oa_build(frame[cfg$items],cfg$manifest,frame$weight,frame$psu,frame$stratum,rep(TRUE,nrow(frame))))
fit<-oa_fit(adapter,ed_model_syntax(cfg$models$M3));context<-os_context(fit)
fitted<-os_at(context,context$x)$moments;index<-grepl('|',names(fitted),fixed=TRUE)
points<-results$M3$model$standardized_points
check('thresholds equal actual fitted model points',max(abs(points$thresholds-unname(fitted[index])))<1e-12&&
  identical(points$threshold_labels,names(fitted)[index]))
observed_difference<-max(abs(fitted[index]-adapter$moments[index]))
check('observed threshold difference is measured not assumed exact',is.finite(points$threshold_observed_max_difference)&&
  abs(points$threshold_observed_max_difference-observed_difference)<1e-12)
full<-ec_public(ec_quiet(ec_analyse(frame,f3,cfg,pins,arm='FULL',previously_retained_scores=c('Z','F'))))
save_json(full,'FULL-aggregate.synthetic.json')
check('FULL cannot restore B-suppressed H',identical(names(full$model$scores),c('Z','F'))&&
  identical(full$confirmation$retained_scores,c('Z','F'))&&grepl('not independent confirmation',full$scope,fixed=TRUE))
check('FULL requires at least2 B-retained scores',error_code(ec_analyse(frame,f3,cfg,pins,arm='FULL',
  previously_retained_scores='F'))=='ESS_CONFIRMATORY_FROZEN_SCORES')
check('B cannot override frozen scores',error_code(ec_analyse(frame,f3,cfg,pins,
  previously_retained_scores=c('Z','F')))=='ESS_CONFIRMATORY_B_SCORE_OVERRIDE')

# Actual file API is exercised only against the fresh invented own directory.
mockroot<-file.path(own,'synthetic-public-root');dir.create(file.path(mockroot,'reports/phasen'),recursive=TRUE,mode='0700')
reference<-file.path(mockroot,'reports/phasen/01-a-entwicklung.json')
jsonlite::write_json(list(scope='invented reference only; no real A'),reference,auto_unbox=TRUE)
stopifnot(Sys.chmod(reference,'0600'))
filefreeze<-f3;filefreeze$a_result$sha256<-ec_sha256(reference)
save_json(filefreeze,'freeze.synthetic.json');freezepath<-file.path(own,'freeze.synthetic.json')
input<-file.path(own,'invented-B.csv');write.csv(frame,input,row.names=FALSE,na='NA');stopifnot(Sys.chmod(input,'0600'))
auth<-list(decision='ACCEPTED_BOUNDED',arm='B',wrapper_verified=TRUE,freeze_sha256=ec_sha256(freezepath),
  syntheticFake=TRUE,synthetic_public_root=substring(mockroot,nchar(project)+2L))
out<-file.path(own,'synthetic-file-api-B');dir.create(out,mode='0700')
status<-capture.output(code<-ec_main(project,input,freezepath,out,auth))
check('file API fixed B success token',code==0L&&identical(status,'ESS_CONFIRMATORY_B_EXECUTED_PRIVATE_OUTPUT'))
check('file API only two600 JSON and no RDS',identical(sort(list.files(out)),
  c('confirmation-aggregate.private.json','confirmation-config.private.json'))&&
  all(bitwAnd(as.integer(file.info(list.files(out,full.names=TRUE))$mode),511L)==384L))
status<-capture.output(code<-ec_main(project,input,freezepath,out,auth))
check('file API refuses overwrite',code==1L&&identical(status,'ESS_CONFIRMATORY_DO_NOT_OVERWRITE'))
bad_auth<-auth;bad_auth$arm<-'FULL'
status<-capture.output(code<-ec_main(project,'/invented-never-opened',freezepath,out,bad_auth))
check('FULL completion required beforeinput',code==1L&&identical(status,'ESS_CONFIRMATORY_FULL_B_REQUIRED'))
full_auth<-auth;full_auth$arm<-'FULL';full_auth$B_step_completed<-TRUE;full_auth$B_retained_scores<-c('Z','F')
fullout<-file.path(own,'synthetic-file-api-FULL');dir.create(fullout,mode='0700')
status<-capture.output(code<-ec_main(project,input,freezepath,fullout,full_auth))
filefull<-jsonlite::fromJSON(file.path(fullout,'confirmation-aggregate.private.json'),simplifyVector=FALSE)
check('file API FULL success and no restored H',code==0L&&
  identical(status,'ESS_CONFIRMATORY_FULL_EXECUTED_PRIVATE_OUTPUT')&&identical(names(filefull$model$scores),c('Z','F')))
save_json(list(schema='life93-confirm-runtime-synthetic-checks-1',scope='invented synthetic responses only',
  checks=checks,passed=sum(unlist(checks)),total=length(checks),source_pins=pins,
  fitted_threshold_observed_max_difference=observed_difference),'checks.json')
cat('CONFIRM_SYNTHETIC_CHECKS ',sum(unlist(checks)),'/',length(checks),'\n',sep='')
quit(status=if(all(unlist(checks)))0L else 1L)
