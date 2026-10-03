# Synthetic-only reproducible entry. No input discovery or real-data loader.
args<-commandArgs(TRUE);project<-args[1];own<-args[2];label<-args[4]
stopifnot(identical(Sys.getenv('HOME'),args[3]))
source(file.path(project,'pipeline/ordinal/norms.R'));init<-en_initialize(project)
cfg<-init$config;pins<-init$pins
checks<-list();check<-function(name,value) {
  checks[[name]]<<-isTRUE(value);cat(if(isTRUE(value))'PASS 'else'FAIL ',name,'\n',sep='')
}
near<-function(x,y,tolerance=1e-10)length(x)==length(y)&&all(is.finite(c(x,y)))&&max(abs(x-y))<=tolerance
code<-function(expr)tryCatch({force(expr);NA_character_},error=en_code)
mock_full<-function(model='M2',scores=names(cfg$models[[model]])) {
  groups<-cfg$models[[model]];lambda<-matrix(0,9,length(groups),dimnames=list(cfg$items,names(groups)))
  for(f in names(groups))lambda[groups[[f]],f]<-.65
  labels<-oa_labels(cfg$manifest);threshold_labels<-labels[grepl('|',labels,fixed=TRUE)]
  thresholds<-unlist(lapply(cfg$categories,function(k)qnorm(seq(1/k,1-1/k,length.out=k-1L))),use.names=FALSE)
  freeze<-list(schema='life93-model-freeze-1',model=model,scores=scores,items=cfg$items,groups=groups,config=cfg,
    source_code_pins=ec_dependency_pins(),a_result=list(path='reports/phasen/01-a-entwicklung.json',sha256=paste(rep('a',64),collapse='')))
  list(schema='life93-fixed-model-confirmation-aggregate-1',arm='FULL',freeze=freeze,model_name=model,
    source_code_pins=pins[names(en_dependencies())],confirmation=list(status='CRITERIA_PASSED_PENDING_RESULT_REVIEW',
      global_model_passed=TRUE,retained_scores=scores),model=list(status='EXECUTED',eligible=TRUE,
      standardized_points=list(items=cfg$items,factors=names(groups),loadings=lambda,thresholds=thresholds,threshold_labels=threshold_labels)))
}
cats<-matrix(c(1,1,1,0,0,0, 0,0,0,10,0,0),2,6,byrow=TRUE)
r<-en_rational(cats,c(3,3,3,10,10,10))
check('heterogeneous denominators exact tie',identical(r$numerator,c(30,30))&&r$denominator==180&&r$lcm==30&&r$values[1]==r$values[2])
frame<-data.frame(stratum=c(1,1,2,2,2),psu=1:5,weight=c(1,2,3,4,5))
H<-c(0,1,2,4,0)
for(id in cfg$items[1:3])frame[[id]]<-H
for(id in cfg$items[4:6])frame[[id]]<-c(0,1,0,3,0)
frame$B43<-c(0,0,10,10,0);frame$B44<-frame$B45<-c(0,0,0,10,0)
frame$B40[5]<-NA_real_
frame<-frame[cfg$input_columns]
full<-mock_full();a<-en_public(en_analyse(frame,full,2*frame$weight));p<-a$scores$ZF$primary
check('weighted midrank hand CDF',near(p$score_grid,c(0,1/6,1))&&near(p$weight_mass,c(1,5,4))&&
  identical(p$counts,c(1L,2L,1L))&&near(p$midrank_cdf,c(.05,.35,.8)))
check('nine complete mask excludes complete H-only row',a$counts$n_complete==4L&&sum(a$scores$H$primary$counts)==4L&&a$counts$zero_complete_psus==1L)
check('missing worstCDF exact algebra',near(p$worst_cdf_lower,c(.05,.35,.8)*2/3)&&
  near(p$worst_cdf_upper,c(.05,.35,.8)*2/3+1/3)&&near(p$worst_cdf_width,1/3)&&!p$population_transfer_missing_budget_passed)
check('alternate norm missing shares appropriate',near(a$scores$ZF$variants$unweighted$norm$worst_cdf_width,1/5)&&
  near(a$scores$ZF$variants$pspwght$norm$worst_cdf_width,1/3))
values<-cbind(H=c(0,.25,.5,1),ZF=c(0,1/6,1/6,1));w<-frame$weight[1:4]
mu<-colSums(values*w)/sum(w);totals<-rbind(sweep(values,2,mu,'-')*w/sum(w),c(0,0))
hand<-matrix(0,2,2)
for(idx in list(1:2,3:5)) {
  g<-length(idx);block<-totals[idx,,drop=FALSE]
  hand<-hand+g/(g-1)*(crossprod(block)-outer(colSums(block),colSums(block))/g)
}
check('null PSU original-frame hand mean covariance',near(a$raw_mean_covariance,hand)&&near(vapply(a$scores,function(x)x$raw_mean$estimate,numeric(1)),mu))
check('original PSUdf t interval',a$counts$original_design_df==3L&&a$scores$ZF$raw_mean$df==3L&&
  a$scores$ZF$raw_mean$critical==qt(.975,3L)&&near(a$scores$ZF$raw_mean$design_se,sqrt(hand[2,2])))
scaled<-frame;scaled$weight<-17*frame$weight
b<-en_public(en_analyse(scaled,full,34*frame$weight))
check('weight scale leaves covariance and CDF unchanged',near(a$raw_mean_covariance,b$raw_mean_covariance)&&
  near(a$scores$ZF$primary$midrank_cdf,b$scores$ZF$primary$midrank_cdf)&&
  near(b$scores$ZF$primary$weight_mass,17*p$weight_mass))
check('unweighted actual contract dependence',a$scores$ZF$variants$unweighted$comparison$status=='CONTRACT_DEPENDENCE_BUDGET_EXCEEDED'&&
  a$scores$ZF$variants$unweighted$comparison$original_weight_mass_percentile_over_5==1&&
  a$scores$ZF$variants$unweighted$comparison$raw_max_absolute_difference==0)
check('psp scalar actual within-budget branch',a$scores$ZF$variants$pspwght$comparison$status=='WITHIN_SPECIFIED_BUDGETS'&&
  a$scores$ZF$variants$pspwght$diagnostics$estimated_common_scale==2&&
  a$scores$ZF$variants$pspwght$diagnostics$exact_multiplication_match)
rounded<-2*frame$weight;rounded[1]<-rounded[1]+.0001
c<-en_public(en_analyse(frame,full,rounded))
check('psp rounding diagnosed without equality claim',!c$scores$ZF$variants$pspwght$diagnostics$exact_multiplication_match&&
  c$scores$ZF$variants$pspwght$diagnostics$max_relative_rounding_difference>0)
for(score in names(full$freeze$groups)) {
  loo<-a$scores[[score]]$variants$leave_one_out
  check(paste(score,'every LOO retained separately'),identical(names(loo),full$freeze$groups[[score]])&&
    all(vapply(loo,function(x)x$status=='EXECUTED'&&sum(x$norm$counts)==4L,logical(1))))
}
badpsp<-en_public(en_analyse(frame,full,rep(NA_real_,5)))
check('invalid psp bounded only its variant',badpsp$scores$ZF$variants$pspwght$status=='UNSUPPORTED'&&
  badpsp$scores$ZF$variants$pspwght$code=='ESS_NORMS_PSPWGHT'&&badpsp$scores$ZF$variants$unweighted$status=='EXECUTED')
overflow<-en_public(en_analyse(frame,full,rep(1e308,5)))
check('overflowed full psp total explicitly unsupported',overflow$scores$ZF$variants$pspwght$status=='UNSUPPORTED'&&
  overflow$scores$ZF$variants$pspwght$code=='ESS_NORMS_PSPWGHT_TOTAL'&&overflow$scores$ZF$variants$unweighted$status=='EXECUTED')
check('nonfinite missing bound explicitly rejected',code(en_norm(c(0,1),c(1,1),missing_share=NaN))=='ESS_NORMS_MISSING_SHARE')
check('six item EAP and every five item LOO remain supported',a$scores$ZF$variants$latent$status=='EXECUTED'&&
  a$scores$ZF$variants$latent$diagnostics$max_curve_difference$`161_321`<=1e-6&&
  all(vapply(a$scores$ZF$variants$leave_one_out,function(v)length(v$diagnostics$remaining_items)==5L,logical(1))))
constant<-frame;constant$B34<-0
z<-en_public(en_analyse(constant,full,2*frame$weight))
check('zero item SD bounded only z variant',z$scores$H$variants$weighted_z$status=='UNSUPPORTED'&&
  z$scores$H$variants$weighted_z$code=='ESS_NORMS_Z_SD'&&z$scores$H$status=='EXECUTED')
badlambda<-full;badlambda$model$standardized_points$loadings[1,1]<-1
d<-en_public(en_analyse(frame,badlambda,2*frame$weight))
check('invalid loading bounded only latent variant',d$scores$H$variants$latent$status=='UNSUPPORTED'&&
  d$scores$H$variants$latent$code=='ESS_NORMS_ITEM_LOADING'&&d$scores$H$variants$unweighted$status=='EXECUTED')
badthreshold<-full;badthreshold$model$standardized_points$threshold_labels[1]<-'B34|t99'
d<-en_public(en_analyse(frame,badthreshold,2*frame$weight))
check('invalid model threshold label bounded to latent variant',d$scores$H$variants$latent$status=='UNSUPPORTED'&&
  d$scores$H$variants$latent$code=='ESS_NORMS_MODEL_THRESHOLD_LABELS'&&d$scores$H$variants$unweighted$status=='EXECUTED')
empty<-frame;empty$B45<-NA_real_
e<-en_public(en_analyse(empty,full,2*frame$weight))
check('empty complete returns every variant unsupported',all(vapply(e$scores,function(x)x$status=='UNSUPPORTED'&&
  x$code=='ESS_NORMS_EMPTY_COMPLETE'&&length(x$variants$leave_one_out)==length(x$items),logical(1))))
wrong<-full;wrong$arm<-'B'
check('non FULL contract rejected',code(en_analyse(frame,wrong,frame$weight))=='ESS_NORMS_FULL_CONTRACT')
wrong<-full;wrong$confirmation$retained_scores<-'H'
check('fewer than two retained scores rejected',code(en_analyse(frame,wrong,frame$weight))=='ESS_CONFIRMATORY_FROZEN_SCORES')

for(n in c(81L,161L,321L)) {
  gh<-en_gh(n);weight<-exp(gh$log_weight)
  check(paste('GH',n,'normal moments independent constants'),near(c(sum(weight),sum(weight*gh$nodes),sum(weight*gh$nodes^2),
    sum(weight*gh$nodes^4),sum(weight*gh$nodes^6)),c(1,0,1,3,15),1e-10)&&all(is.finite(gh$log_weight)))
}
oracle<-function(pattern,model) {
  likelihood<-function(eta) {
    p<-rep(1,length(eta))
    for(j in seq_along(pattern)) {
      threshold<-c(-Inf,model$thresholds[[j]],Inf);sd<-sqrt(1-model$lambda[j]^2)
      lo<-(threshold[pattern[j]+1L]-model$lambda[j]*eta)/sd
      hi<-(threshold[pattern[j]+2L]-model$lambda[j]*eta)/sd
      prob<-if(is.infinite(threshold[pattern[j]+2L]))pnorm(lo,lower.tail=FALSE)else pnorm(hi)-pnorm(lo)
      p<-p*prob
    }
    p*dnorm(eta)
  }
  denom<-integrate(likelihood,-Inf,Inf,rel.tol=1e-10,abs.tol=1e-30,subdivisions=5000L)$value
  eta<-integrate(function(x)x*likelihood(x),-Inf,Inf,rel.tol=1e-10,abs.tol=1e-30,subdivisions=5000L)$value/denom
  curve<-mean(vapply(seq_along(pattern),function(j)mean(pnorm((model$lambda[j]*eta-model$thresholds[[j]])/
    sqrt(1-model$lambda[j]^2))),numeric(1)))
  list(eta=eta,curve=curve)
}
models<-list(moderate=list(lambda=rep(.7,3),thresholds=rep(list(c(-.5,0,.5)),3),items=c('a','b','c')),
  high=list(lambda=rep(.85,3),thresholds=rep(list(c(4,5,6)),3),items=c('a','b','c')))
oracle_results<-list()
for(name in names(models)) {
  pattern<-rep(3L,3L);o<-oracle(pattern,models[[name]]);q<-en_posterior(matrix(pattern,1L),models[[name]],en_gh(321L))
  v<-en_latent(matrix(pattern,1L),models[[name]],1)
  check(paste(name,'independent integrate posterior and curve'),near(q$eta,o$eta,2e-6)&&near(q$curve,o$curve,2e-6))
  check(paste(name,'161321 curve tolerance actual pass'),v$diagnostics$max_curve_difference$`161_321`<=1e-6)
  oracle_results[[name]]<-list(oracle=o,quadrature_eta=q$eta,quadrature_curve=q$curve,
    max_161_321_difference=v$diagnostics$max_curve_difference$`161_321`)
}
check('high posterior not lost by direct probability underflow',oracle_results$high$quadrature_eta>6)
sharp<-list(lambda=rep(.9999,3),thresholds=rep(list(c(.05,.15,.3)),3),items=c('a','b','c'))
failure<-tryCatch(en_latent(matrix(1L,1L,3L),sharp,1),error=function(e)e)
check('quadrature instability explicit no rescue',inherits(failure,'en_error')&&en_code(failure)=='ESS_NORMS_EAP_STABILITY'&&
  failure$diagnostics$max_curve_difference$`161_321`>1e-6)

# Actual immutable FULL fit supplies actual fitted threshold fields; no fit in norms.
source(file.path(own,'fixture.R'));frame_actual<-ed_synthetic_frame(cfg,'M3',2026100342L)
freeze_actual<-mock_full('M3')$freeze
full_actual<-ec_public(ec_analyse(frame_actual,freeze_actual,cfg,init$pins[names(en_dependencies())],
  arm='FULL',previously_retained_scores=c('H','Z','F')))
check('actual FULL prerequisite executed',full_actual$confirmation$status=='CRITERIA_PASSED_PENDING_RESULT_REVIEW')
original_fit<-oa_fit;oa_fit<-function(...)stop('NORMS_MUST_NOT_FIT',call.=FALSE)
actual<-en_public(en_analyse(frame_actual,full_actual,2*frame_actual$weight));oa_fit<-original_fit
check('actual FULL norm complete mask counts and nullPSUs',actual$counts$n_original==7680L&&actual$counts$n_complete==7520L&&
  actual$counts$zero_complete_psus==4L&&actual$counts$original_design_df==188L)
for(score in actual$retained_scores) {
  s<-actual$scores[[score]]
  check(paste('actual',score,'all specified variants reported'),identical(names(s$variants),c('unweighted','pspwght','weighted_z','latent','leave_one_out'))&&
    identical(names(s$variants$leave_one_out),cfg$models$M3[[score]]))
  check(paste('actual',score,'latent uses fitted thresholds stable'),s$variants$latent$status=='EXECUTED'&&
    s$variants$latent$diagnostics$max_curve_difference$`161_321`<=1e-6)
  check(paste('actual',score,'mean and t original df'),s$raw_mean$df==188L&&is.finite(s$raw_mean$design_se)&&s$raw_mean$critical==qt(.975,188L))
}
forbidden<-c('psu','stratum','weight','weights','cases','mask','positions','numerator_by_case','values','eta','posterior','contributions','private','X','IF')
scan<-function(x)if(is.list(x))!any(names(x)%in%forbidden)&&all(vapply(x,scan,logical(1)))else TRUE
check('public norm aggregate no case vectors keys IF RDS',scan(actual)&&identical(names(actual),
  c('schema','scope','model_name','retained_scores','source_code_pins','counts','raw_mean_covariance','scores','limits')))
jsonlite::write_json(actual,file.path(own,paste0(label,'-actual-norms-aggregate.json')),auto_unbox=TRUE,pretty=TRUE,digits=16,na='null')
jsonlite::write_json(a,file.path(own,paste0(label,'-hand-norms-aggregate.json')),auto_unbox=TRUE,pretty=TRUE,digits=16,na='null')
exports<-file.path(own,paste0(label,c('-actual-norms-aggregate.json','-hand-norms-aggregate.json')))
check('own synthetic exports0600 and directory0700',as.integer(file.info(own)$mode)==448L&&
  all(as.integer(file.info(exports)$mode)==384L))
jsonlite::write_json(list(scope='invented synthetic norms only',checks=checks,passed=sum(unlist(checks)),total=length(checks),
  independent_oracles=oracle_results,stability_failure=list(code=en_code(failure),diagnostics=failure$diagnostics),
  source_pins=init$pins),file.path(own,paste0(label,'-checks.json')),auto_unbox=TRUE,pretty=TRUE,digits=16)
cat('CHECKS ',sum(unlist(checks)),'/',length(checks),'\n',sep='')
if(!all(unlist(checks)))quit(status=1L)
