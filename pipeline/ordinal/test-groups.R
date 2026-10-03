# Original synthetic data only. Aggregate test outcomes, no row/ID dump.
options(warn=1,digits=16)
args<-commandArgs(TRUE);stopifnot(length(args)==4L)
project<-normalizePath(args[1],mustWork=TRUE);own<-normalizePath(args[2],mustWork=TRUE);label<-args[4]
stopifnot(own==file.path(project,'outputs/loop/resume-joint-groups'),Sys.getenv('HOME')==args[3])
source(file.path(project,'pipeline/ordinal/adapter_v2.R'));source(file.path(project,'pipeline/ordinal/support.R'));source(file.path(project,'pipeline/ordinal/groups.R'))
library(jsonlite)
os_original_spd <- os_check_spd
os_check_spd <- function(x,code) {
  tryCatch(os_original_spd(x,code),error=function(e) {
    stop(paste0(conditionMessage(e),'; synthetic minEigen=',format(min(eigen(os_sym(x),symmetric=TRUE,only.values=TRUE)$values),digits=16),
      '; maxAsymmetry=',format(max(abs(x-t(x))),digits=16)),call.=FALSE)
  })
}
checks<-list();warnings_seen<-character()
check<-function(id,observed,pass,rule) {
  checks[[id]]<<-list(observed=observed,status=if(isTRUE(pass))'BESTANDEN' else 'NICHT_BESTANDEN',rule=rule)
  cat(id,checks[[id]]$status,'\n')
}
md<-function(a,b)if(length(a)!=length(b))Inf else max(abs(a-b))
run<-function() {
  og_runtime();RNGkind('Mersenne-Twister','Inversion','Rejection');set.seed(2026100341L)
  np<-192L;n<-np*20L;psu<-rep(seq_len(np),each=20L);stratum<-rep(rep(1:4,each=48L),each=20L)
  group<-rep(c(rep('G1',6L),rep('G2',14L)),np);focal<-group=='G2'
  phi<-matrix(c(1,.3,.2,.3,1,.25,.2,.25,1),3,3)
  eta<-MASS::mvrnorm(n,rep(0,3),.85*phi)+MASS::mvrnorm(np,rep(0,3),.15*phi)[psu,]
  eta[focal,]<-sweep(eta[focal,,drop=FALSE],2,c(.2,-.15,.25),'+')
  cats<-rep(c(5L,4L,11L),3L);manifest<-setNames(lapply(cats,function(k)0:(k-1L)),paste0('q',1:9))
  lambda<-rep(c(.7,.65,.6),3);eps<-matrix(rnorm(n*9L),n,9)
  make<-function(dif=FALSE,shift=.65,multiplier=1.25)as.data.frame(setNames(lapply(1:9,function(j) {
    slope<-rep(lambda[j],n);intercept<-rep(0,n)
    if(dif&&j==2L){slope[focal]<-multiplier*lambda[j];intercept[focal]<-shift}
    response<-slope*eta[,ceiling(j/3)]+sqrt(1-lambda[j]^2)*eps[,j]+intercept
    as.integer(cut(response,c(-Inf,qnorm(seq_len(cats[j]-1L)/cats[j]),Inf),labels=FALSE))-1L
  }),names(manifest)))
  weight<-runif(n,.5,1.5);domain<-!psu%in%c(1L,49L,97L,145L)
  joint<-og_build(make(),manifest,weight,psu,stratum,domain,group,c('G1','G2'))
  check('joint_frame_identity_and_unequal_groups',list(groups=joint$ng,psus=joint$aggregate$original_psus,
    strata=joint$aggregate$strata,df=joint$aggregate$design_df,zero_psus=joint$aggregate$zero_domain_psus,
    crossblock_max=max(abs(joint$covariance[1:87,88:174])),rank=qr(joint$covariance)$rank),
    joint$ng[1]!=joint$ng[2]&&joint$aggregate$zero_domain_psus==4L&&
      joint$aggregate$original_psus==192L&&max(abs(joint$covariance[1:87,88:174]))>1e-7,
    'shared original PSU frame including four null-domain PSUs; unequal complete group n and nonzero crossblocks')
  # Independently compute PSU totals/centered full covariance from the own IF.
  u<-joint$private$contributions;manual<-matrix(0,ncol(u),ncol(u))
  totals<-rowsum(u,psu,reorder=FALSE);hs<-stratum[match(as.numeric(rownames(totals)),psu)]
  for(h in 1:4){b<-totals[hs==h,,drop=FALSE];manual<-manual+48/47*crossprod(sweep(b,2,colMeans(b)))}
  check('joint_full_psu_hand_covariance',md(manual,joint$covariance),md(manual,joint$covariance)<1e-10,
    'independent original PSU totals/stratum centering reproduces all within/crossblocks')
  sequence<-og_sequence(joint);fits<-sequence$private$fits;sws<-sequence$private$sandwiches;summaries<-list()
  check('full_nine_test_family_and_mc_open_rule',list(size=sequence$family_size,threshold=sequence$bonferroni_threshold,decisions=sequence$decisions),
    sequence$family_size==9L&&sequence$bonferroni_threshold==.05/9&&
      og_mc_decision(list(mc_interval=c(.004,.006)),.05/9)=='OPEN_MC_INTERVAL_CROSSES_THRESHOLD',
    'five global plus four successive substantive tests per grouping variable, complete Bonferroni family; CI crossing OPEN without rerun')
  for(stage in c('configural','thresholds','loadings','intercepts','strict')) {
    fit<-fits[[stage]];sw<-sws[[stage]]
    p<-sw$private;context<-p$context;x<-context$x;at<-og_at(context,x)
    numerical<-os_numeric_jacobian(function(v)og_at(context,v)$moments,x)
    check(paste0(stage,'_actual_parameter_moment_derivative'),md(numerical,p$delta),md(numerical,p$delta)<=2e-5,
      'exact native free order/model setter transformed THETA moments vs independent central perturbation <=2e-5')
    # Verify actual weighted native objective at canonical point and off-point.
    nativeObjective<-function(v) {
      a<-og_at(context,v);f<-context$fit
      as.numeric(os_fun('lav_model_objective')(a$model,lavsamplestats=f@SampleStats,
        lavdata=f@Data,lavcache=f@Cache))
    }
    trueObjective<-function(v)sum((joint$moments-og_at(context,v)$moments)^2)/2
    perturbed<-x+sin(seq_along(x))*.015
    objective_error<-max(abs(c(nativeObjective(x)-trueObjective(x),nativeObjective(perturbed)-trueObjective(perturbed))))
    derivative<-os_numeric_jacobian(function(v)c(objective=nativeObjective(v)),perturbed)
    analytic<--og_score(context,perturbed)
    check(paste0(stage,'_native_joint_identity_objective_gradient'),list(objective_error=objective_error,
      freegradient_error=md(derivative,analytic)),objective_error<1e-7&&md(derivative,analytic)<=2e-5,
      'N/(n_g-1) external blocks cancel actual objective weighting at unequal n; actual objective freegradient <=2e-5')
    step2<-og_sandwich(fit,step=2e-5)
    check(paste0(stage,'_observed_jacobian_steps'),md(p$bread,step2$private$bread),
      md(p$bread,step2$private$bread)<=2e-5,'full tangent observed score derivative at 1e-5 and 2e-5 <=2e-5')
    global<-sequence$tests[[paste0('global_',stage)]]
    check(paste0(stage,'_global_spectral_fit'),global[c('quadratic','p_mc','mc_interval','rank','draws')],
      global$draws==200000L&&global$p_mc>=global$mc_interval[1]&&global$p_mc<=global$mc_interval[2]&&
        all(global$eigenvalues>=0),'own full-Vm spectral asymptotic null law; fixed 200000 draw tail with binomial MC interval')
    summaries[[stage]]<-c(sw$aggregate,global[c('quadratic','p_mc','mc_interval','rank')])
  }
  check('wu_estabrook_stage_identification',vapply(sws,function(s)s$aggregate$tangent_dimension,integer(1)),
    identical(unname(vapply(sws,function(s)s$aggregate$tangent_dimension,integer(1))),c(126L,93L,87L,81L,72L)),
    'M3 configural -> thresholds -> loadings -> intercepts -> residuals tangent dimensions 126/93/87/81/72')
  nested_outputs <- list();stage_names<-names(sws)
  for(i in 2:5) {
    nt<-sequence$tests[[paste0('restriction_',stage_names[i])]]
    check(paste0('successive_null_aligned_',stage_names[i]),
      nt[c('quadratic_difference','p_mc','mc_interval','rank','null_moment_mapping_error','null_tangent_nesting_error')],
      nt$null_moment_mapping_error<1e-7&&nt$null_tangent_nesting_error<1e-7&&all(nt$eigenvalues>=0),
      'both tangent spaces at one transformed restrictive null point; identical moments, nested tangent and PSD difference')
    nested_outputs[[stage_names[i]]]<-nt[c('p_mc','mc_interval','rank')]
  }
  eq<-og_equivalence(sws$configural,sws$strict)
  pc<-sws$configural$private;ps<-sws$strict$private;nc<-length(pc$context$x)
  stacked<-c(pc$context$x,ps$context$x);names(stacked)<-colnames(eq$gradient)
  curvecontrast<-function(xc,xs) {
    curve<-og_curve(pc$context,ps$context,manifest,'M3',xc=xc,xs=xs)$values
    # Complete pair family is g2-g1, H/I/E and five fixed points.
    setNames(curve[16:30]-curve[1:15],names(eq$contrasts))
  }
  curvefun<-function(x)curvecontrast(x[seq_len(nc)],x[-seq_len(nc)])
  jnum<-os_numeric_jacobian(curvefun,stacked)
  check('twofit_curve_and_link_analytic_gradient',md(eq$gradient,jnum),md(eq$gradient,jnum)<=2e-5,
    'all free item parameters plus strict mu/psi link derivatives vs actual parameter perturbation <=2e-5')
  split<-nrow(pc$k);crossfit<-eq$stacked_covariance[1:split,-seq_len(split),drop=FALSE]
  check('twofit_shared_moment_crosscovariance',list(max_crossfit=max(abs(crossfit)),family=eq$family_size,
    max_delta=max(abs(eq$contrasts)),upper=eq$simultaneous_upper_bound,within_own_budget=eq$within_own_budget),
    max(abs(crossfit))>1e-7&&eq$family_size==15L&&all(eq$design_se>0),
    'same full Vm stacked K preserves crossfit covariance; complete predefined 15-contrast .05 Bonferroni family')
  # Actual perturbed summary refits of both estimators, not only beta setter.
  direction<-sin(seq_along(joint$moments)*.71);direction<-direction/max(abs(direction))
  step<-.00025;plus<-joint$moments+step*direction;minus<-joint$moments-step*direction
  rcplus<-og_refit(pc$context,plus);rcminus<-og_refit(pc$context,minus)
  rsplus<-og_refit(ps$context,plus);rsminus<-og_refit(ps$context,minus)
  parameter_derivative<-c((rcplus$x-rcminus$x)/(2*step),(rsplus$x-rsminus$x)/(2*step))
  predicted<-as.numeric(eq$kstack%*%direction)
  check('true_twofit_summary_parameter_refits',md(parameter_derivative,predicted),
    md(parameter_derivative,predicted)<=2e-5,'actual BFGS +/-0.00025 moment refits vs observed Kstack <=2e-5')
  actual_curve<-(curvecontrast(rcplus$x,rsplus$x)-curvecontrast(rcminus$x,rsminus$x))/(2*step)
  predicted_curve<-as.numeric(eq$gradient%*%eq$kstack%*%direction)
  check('true_twofit_summary_function_refits',md(actual_curve,predicted_curve),md(actual_curve,predicted_curve)<=2e-5,
    'actual twofit free curves plus strict links refitted jointly vs J Kstack direction <=2e-5')
  # Linear testable restriction, unlike identification equalities.
  pt<-pc$context$pt;ii<-which(pt$op=='=~'&pt$rhs=='q1'&pt$free>0)
  C<-matrix(0,1,length(pc$context$x));C[1,pt$free[ii]]<-c(1,-1)
  wald<-og_wald(sws$configural,C)
  check('wald_testable_restriction',wald,is.finite(wald$quadratic)&&wald$df==1L,
    'simple difference in two identified configural loading coordinates; does not certify latent invariance')
  pureid<-tryCatch({og_wald(sws$strict,sws$strict$private$context$tangent$h[1,,drop=FALSE]);FALSE},
    error=function(e)grepl('WALD_NOT_TESTABLE',conditionMessage(e)))
  check('wald_identification_constraint_rejected',pureid,pureid,'pure equality tangent null is not a material test')
  # Deliberately rank-deficient PSD covariance counterexample; bread unchanged.
  low<-joint;ve<-eigen(joint$covariance,symmetric=TRUE);ve$values[seq.int(161L,174L)]<-0
  low$covariance<-os_sym(ve$vectors%*%diag(ve$values)%*%t(ve$vectors));lowfit<-fits$strict
  lowfit$private$joint<-low;lowfit$private$context$joint<-low;lowsw<-og_sandwich(lowfit);lf<-og_global_fit(lowsw)
  check('rankdeficient_joint_psd_supported',list(rank=qr(low$covariance)$rank,p=lf$p_mc),
    qr(low$covariance)$rank<174L&&is.finite(lf$p_mc),
    'explicit synthetic PSD rank truncation only; invert identified bread, never full Vm')
  # Exact ordinary chi-square special case and independent Gaussian form.
  oracle<-og_spectral_mc(rep(1,4),qchisq(.95,4),seed=2026100343L)
  check('spectral_chisquare_normal_oracle',oracle[c('p_mc','mc_interval')],
    oracle$mc_interval[1]<=.05&&oracle$mc_interval[2]>=.05,
    'four unit eigenvalues reduce to known chi-square4 tail=.05, within predeclared binomial interval')
  # Nontrivial full Gaussian quadratic versus its eigen representation.
  Vknown<-matrix(c(1,.35,.15,.35,.8,.2,.15,.2,.6),3,3)
  Uknown<-crossprod(matrix(c(1,.2,-.1,.3,.7,.25),2,3))
  ve<-eigen(Vknown,symmetric=TRUE);root<-ve$vectors%*%diag(sqrt(ve$values))%*%t(ve$vectors)
  eigenknown<-eigen(os_sym(root%*%Uknown%*%root),symmetric=TRUE,only.values=TRUE)$values
  eigenknown[eigenknown<0]<-0
  spectral<-og_spectral_mc(eigenknown,1.5,seed=2026100350L)
  set.seed(2026100351L);normal<-matrix(rnorm(200000L*3L),200000L,3L)%*%chol(Vknown)
  direct<-rowSums((normal%*%Uknown)*normal);direct_p<-mean(direct>=1.5)
  tail_error<-abs(direct_p-spectral$p_mc)
  allowed<-5*sqrt(direct_p*(1-direct_p)/200000+spectral$p_mc*(1-spectral$p_mc)/200000)
  check('nontrivial_full_normal_eigen_quadratic_oracle',list(direct_p=direct_p,eigen_p=spectral$p_mc,
    tail_difference=tail_error,predefined_5MCSE_bound=allowed),tail_error<allowed,
    'independent 200000 direct correlated-normal quadratic draws vs weighted chi-square eigen law within five Monte Carlo SE; algebra diagnostic only')
  reverse_scores<-lapply(manifest,function(v)1-(v-min(v))/(max(v)-min(v)))
  reversed<-og_equivalence(sws$configural,sws$strict,scores=reverse_scores)
  check('explicit_fixed_reversed_polarity_scores',list(contrast_error=md(reversed$contrasts,-eq$contrasts),
    covariance_error=md(reversed$covariance,eq$covariance)),
    md(reversed$contrasts,-eq$contrasts)<1e-10&&md(reversed$covariance,eq$covariance)<1e-10,
    'all fixed score codings reversed: curve contrasts negate, full twofit covariance unchanged')
  original_kind<-RNGkind();original_seed<-.Random.seed
  firstmc<-og_spectral_mc(c(1,.5),1,draws=100L,seed=41L)
  RNGkind("L'Ecuyer-CMRG");set.seed(91L);before_kind<-RNGkind();before_seed<-.Random.seed
  secondmc<-og_spectral_mc(c(1,.5),1,draws=100L,seed=41L)
  restored<-identical(before_kind,RNGkind())&&identical(before_seed,.Random.seed)
  do.call(RNGkind,as.list(original_kind));assign('.Random.seed',original_seed,.GlobalEnv)
  check('spectral_fixed_rng_and_caller_restored',list(equal_tail=firstmc$p_mc==secondmc$p_mc,restored=restored),
    firstmc$p_mc==secondmc$p_mc&&restored,'fixed Mersenne-Twister/Inversion/Rejection inside MC; caller RNG kind and exact state restored')
  # Known common affine DIF versus different latent location/scale: identical y*.
  set.seed(2026100344L);latent<-rnorm(100);a<-.4;b<-1.3;lam<-.7;residual<-rnorm(100)
  y_dif<-lam*a+lam*b*latent+residual;y_latent<-lam*(a+b*latent)+residual
  check('common_affine_dif_observational_nonidentifiability',md(y_dif,y_latent),md(y_dif,y_latent)<1e-12,
    'common item intercept/loading affine change equals latent mu/variance change exactly; not detectable by invariance fit')
  # M2 H trio / migration six fully executed too, using same moments.
  m2sequence<-og_sequence(joint,'M2');m2c<-m2sequence$private$sandwiches$configural
  m2s<-m2sequence$private$sandwiches$strict;m2eq<-m2sequence$equivalence
  check('m2_trio_migration6_supported',list(dimensions=c(m2c$aggregate$tangent_dimension,m2s$aggregate$tangent_dimension),
    family=m2eq$family_size,upper=m2eq$simultaneous_upper_bound,all_stages=m2sequence$decisions),m2eq$family_size==10L&&all(is.finite(m2eq$design_se)),
    'M2 H3/migration6 configural plus strict fit and full twofit covariance; no model acceptance')
  # Known DIF generator, same original random draws/design, no seed hunting.
  strong_dif <- tryCatch({
    difjoint<-og_build(make(TRUE),manifest,weight,psu,stratum,domain,group,c('G1','G2'))
    dc<-og_sandwich(og_fit(difjoint,'M3','configural'));ds<-og_sandwich(og_fit(difjoint,'M3','strict'))
    deq<-og_equivalence(dc,ds);dg<-og_global_fit(ds,seed=2026100346L)
    list(status='CALCULATED_SYNTHETIC_ONLY',fit=dg[c('p_mc','mc_interval')],upper=deq$simultaneous_upper_bound,
      within_own_budget=deq$within_own_budget)
  },error=function(e)list(status='BLOCKED_REQUIRED_POSITIVE_BREAD_OR_IDENTIFICATION',error=conditionMessage(e)))
  write_json(strong_dif,file.path(own,paste0(label,'-strong-dif.json')),auto_unbox=TRUE,pretty=TRUE,digits=16)
  check('strong_dif_fail_closed_limit',strong_dif,
    strong_dif$status=='BLOCKED_REQUIRED_POSITIVE_BREAD_OR_IDENTIFICATION'||!strong_dif$within_own_budget,
    'strong .65 intercept/25% loading DIF scenario retained; inadmissible/negative-or-zero bread blocks its latent comparison, no rescue or power claim')
  # Additional newly declared diagnostic, preserving the failed strong scenario.
  moderatejoint<-og_build(make(TRUE,shift=.35,multiplier=1.15),manifest,weight,psu,stratum,domain,group,c('G1','G2'))
  mc<-og_sandwich(og_fit(moderatejoint,'M3','configural'));ms<-og_sandwich(og_fit(moderatejoint,'M3','strict'))
  meq<-og_equivalence(mc,ms);mg<-og_global_fit(ms,seed=2026100346L)
  check('additional_known_threshold_loading_dif_not_certified',list(p_mc=mg$p_mc,mc_interval=mg$mc_interval,
    max_delta=max(abs(meq$contrasts)),upper=meq$simultaneous_upper_bound,budget_pass=meq$within_own_budget),
    (!meq$within_own_budget||og_mc_decision(mg,.05/9)=='REJECT'),
    'additional fixed .35 intercept/15% loading DIF: combined fit AND positive-score gate blocks, either violation suffices; score margin may pass; no power claim')
  list(configuration=list(seed=2026100341L,n_synthetic=n,PSUs=np,strata=4,categories=cats,
      full_frame_null_psus=4,unequal_group_complete_n=joint$ng,fixed_metric='joint I'),
    stages=summaries,nested_restrictions=nested_outputs,strong_dif=strong_dif,equivalence=eq[c('family_size','grid','margin','alpha','critical','simultaneous_upper_bound','within_own_budget')],
    limitations=c('isolated synthetic scenarios only; no empirical or coverage/power calibration',
      'all-item strict affine link assumption; undetectable common affine DIF',
      'no native block diagonal inference or subtraction of fitted projectors','nine-test family per grouping variable; MC interval crossing remains OPEN without rerun'))
}
result<-tryCatch(withCallingHandlers(run(),warning=function(w){warnings_seen<<-c(warnings_seen,conditionMessage(w));invokeRestart('muffleWarning')}),
  error=function(e)list(error=conditionMessage(e),error_call=paste(deparse(conditionCall(e)),collapse=" "),calls=vapply(sys.calls(),function(c)paste(deparse(c),collapse=' '),character(1))))
result$runtime<-list(R=R.version.string,lavaan=as.character(packageVersion('lavaan')),semTools=as.character(packageVersion('semTools')))
result$checks<-checks;result$warnings<-warnings_seen
result$status<-if(is.null(result$error)&&length(checks)>0L&&all(vapply(checks,function(x)x$status=='BESTANDEN',logical(1))))
  'SYNTHETIC_CHECKS_PASSED' else 'SYNTHETIC_CHECKS_FAILED'
write_json(result,file.path(own,paste0(label,'-result.json')),auto_unbox=TRUE,pretty=TRUE,digits=16)
cat(result$status,'\n');if(result$status!='SYNTHETIC_CHECKS_PASSED')quit(status=1)
