options(warn=1,digits=16)
args <- commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==4L)
project <- normalizePath(args[[1]],mustWork=TRUE); own <- normalizePath(args[[2]],mustWork=TRUE)
stopifnot(identical(own,file.path(project,'outputs/loop/resume-ordinal-support')),
          identical(Sys.getenv('HOME'),args[[3]]))
source(file.path(project,'pipeline/ordinal/adapter.R'))
source(file.path(project,'pipeline/ordinal/support.R'))
checks <- list(); warnings_seen <- character(); diagnostic <- list()
check <- function(id,observed,passed,rule) {
  checks[[id]] <<- list(observed=observed,status=if(isTRUE(passed))'BESTANDEN'else'NICHT_BESTANDEN',rule=rule)
  cat(id,checks[[id]]$status,'\n')
}
md <- function(a,b) if(length(a)!=length(b)||any(!is.finite(c(a,b))))Inf else max(abs(a-b))
expect_stop <- function(id,expr,code) {
  got <- tryCatch({force(expr);'NO_STOP'},error=function(e)conditionMessage(e))
  check(id,got,identical(got,paste0('ORDINAL_SUPPORT_',code)),'fixed expected stop code')
}
models <- list(M3='f1 =~ q1 + q2 + q3\nf2 =~ q4 + q5 + q6\nf3 =~ q7 + q8 + q9',
  M2='f1 =~ q1 + q2 + q3\nf2 =~ q4 + q5 + q6 + q7 + q8 + q9',
  M1='f1 =~ q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9')
perturbed_adapter <- function(adapter,moments) {
  out <- adapter; out$moments <- moments
  out$thresholds <- unname(moments[seq_along(adapter$thresholds)])
  out$correlation[lower.tri(out$correlation)] <- moments[-seq_along(out$thresholds)]
  out$correlation[upper.tri(out$correlation)] <- t(out$correlation)[upper.tri(out$correlation)]
  out
}
oracle_refit <- function(adapter,model) {
  # Only the synthetic full-refit oracle gets tighter optimizer controls.
  # Summary inputs and pinned version remain identical to oa_fit.
  th <- adapter$thresholds;names(th)<-names(adapter$moments)[seq_along(th)]
  attr(th,'th.idx')<-setNames(adapter$threshold_index,names(th))
  fit <- oa_quiet(lavaan::cfa(model=model,sample_cov=adapter$correlation,sample_th=th,
    sample_mean=setNames(rep(0,9L),colnames(adapter$correlation)),
    sample_nobs=adapter$aggregate$n_complete,ordered=colnames(adapter$correlation),
    estimator='WLSMV',parameterization='theta',std_lv=TRUE,nacov=adapter$gamma,wls_v=adapter$wls_v,
    optim_method='BFGS',control=list(reltol=1e-13,maxit=20000L)))
  structure(list(private=fit,aggregate=list(df=unname(lavaan::fitMeasures(fit,'df')),
    converged=TRUE,postcheck=TRUE,efa_factors=NULL)),class='oa_fit')
}
conditional_integral <- function(context,spec) {
  a <- os_at(context,context$x); idx <- match(spec$items,rownames(a$glist$lambda))
  active <- which(colSums(abs(a$glist$lambda[idx,,drop=FALSE]))>0)
  stopifnot(length(active)==1L)
  lambda <- a$glist$lambda[idx,active]*sqrt(a$glist$psi[active,active])
  sd <- sqrt(diag(a$glist$theta)[idx]); tau <- lapply(idx,function(i)
    a$glist$tau[context$model@th.idx[[1]]==i,1])
  cond <- function(eta) {
    prob <- lapply(seq_along(idx),function(j)diff(c(0,pnorm((tau[[j]]-lambda[j]*eta)/sd[j]),1)))
    means <- vapply(seq_along(idx),function(j)sum(prob[[j]]*spec$scores[[j]]),numeric(1))
    vars <- vapply(seq_along(idx),function(j)sum(prob[[j]]*spec$scores[[j]]^2)-means[j]^2,numeric(1))
    c(mean=mean(means),variance=sum(vars)/length(idx)^2)
  }
  integral <- function(fun)integrate(Vectorize(function(x)fun(cond(x))*dnorm(x)),
    -Inf,Inf,rel.tol=1e-10,abs.tol=1e-11,subdivisions=1000L)$value
  mu <- integral(function(v)v[1]); true <- integral(function(v)v[1]^2)-mu^2
  error <- integral(function(v)v[2])
  c(mean=mu,true_variance=true,error_variance=error,reliability=true/(true+error))
}
run <- function() {
  oa_runtime(); stopifnot(as.character(packageVersion('semTools'))=='0.5.9')
  RNGkind('Mersenne-Twister','Inversion','Rejection');set.seed(2026100321L)
  g <- 192L; n <- g*20L; psu <- rep(seq_len(g),each=20L)
  stratum <- rep(rep(1:4,each=g/4),each=20L)
  phi <- matrix(c(1,.3,.2,.3,1,.25,.2,.25,1),3,3)
  eta <- MASS::mvrnorm(n,rep(0,3),phi)+MASS::mvrnorm(g,rep(0,3),.12*phi)[psu,]
  categories <- rep(c(5L,4L,11L),3L)
  manifest <- setNames(lapply(categories,function(k)0:(k-1L)),paste0('q',1:9))
  dat <- as.data.frame(setNames(lapply(1:9,function(j) {
    lambda <- c(.7,.6,.55)[(j-1L)%%3L+1L]
    z <- lambda*eta[,ceiling(j/3)]+rnorm(n,sd=sqrt(1-lambda^2))
    as.integer(cut(z,c(-Inf,qnorm((1:(categories[j]-1))/categories[j]),Inf),labels=FALSE))-1L
  }),names(manifest)))
  weight <- runif(n,.5,1.5); domain <- !psu %in% c(1L,49L,97L,145L)
  adapter <- oa_build(dat,manifest,weight,psu,stratum,domain)
  metric <- 'diagnostic sample-estimated DWLS diagonal held fixed'
  if(startsWith(args[[4]],'test-fixed')) {
    original <- adapter$wls_v
    fixed <- oa_fixed_metric(adapter)
    check('fixed_identity_copy_contract',list(diagonal_range=range(diag(fixed$wls_v))),
      identical(adapter$wls_v,original)&&identical(dimnames(fixed$wls_v),dimnames(original))&&
      all(diag(fixed$wls_v)==1)&&all(fixed$wls_v[row(fixed$wls_v)!=col(fixed$wls_v)]==0),
      'fixed identity external moment metric; original adapter/labels unchanged; no estimated metric uncertainty')
    adapter <- fixed;metric <- adapter$aggregate$point_metric
  }
  check('87_moments_null_domain_psus',list(moments=length(adapter$moments),null_psus=adapter$aggregate$zero_psus),
    length(adapter$moments)==87L&&adapter$aggregate$zero_psus==4L,'87 labeled moments; all original domain-null PSUs preserved')
  outputs <- list()
  for(name in names(models)) {
    fit <- oa_fit(adapter,models[[name]])
    sw <- os_sandwich(adapter,fit); p <- sw$private; context <- p$context
    dnum <- os_numeric_jacobian(function(x)os_at(context,x)$moments,context$x)
    check(paste0(name,'_delta_free_parameter_derivative'),md(dnum,p$delta),md(dnum,p$delta)<=2e-5,
      'native Delta with exact moment/free-parameter labels vs central free-parameter perturbation <=2e-5')
    expected_sw <- os_sandwich(adapter,fit,bread_method='expected')
    native <- lavaan::lavInspect(fit$private,'vcov')
    ncomplete <- adapter$aggregate$n_complete
    # Pinned lav_model_vcov.R divides non-ML WLS by N-ngroups, independently
    # of gamma.vcov.mplus. Single-group finite factor is therefore N/(N-1).
    finite_factor <- ncomplete/(ncomplete-1)
    diff <- md(native/finite_factor,expected_sw$private$parameter_covariance)
    check(paste0(name,'_native_synthetic_sandwich_oracle'),list(max_difference=diff,finite_factor=finite_factor,
      ncomplete=ncomplete,gamma_vcov_mplus=fit$private@Options$gamma.vcov.mplus),diff<=1e-7,
      'native lavaan expected-information sandwich is oracle only for separate expected projection; pinned non-ML denominator N-ngroups gives N/(N-1)')
    jacstep <- os_sandwich(adapter,fit,step=2e-5)
    check(paste0(name,'_observed_jacobian_steps'),md(p$jacobian,jacstep$private$jacobian),
      md(p$jacobian,jacstep$private$jacobian)<=2e-5,'full estimating-equation Jacobian includes residual Delta derivative; two central steps <=2e-5')
    std <- os_standardized(sw)
    stdstep <- os_standardized(sw,step=2e-5)
    check(paste0(name,'_standardized_gradient_steps'),md(std$gradient,stdstep$gradient),
      md(std$gradient,stdstep$gradient)<=2e-5,'free-parameter derivatives of actual standardized transform at two steps')
    rms <- os_residual_rms(sw)
    check(paste0(name,'_residual_rms_ci'),rms[c('estimate','design_se','lower','upper','status')],
      rms$status=='NORMAL_DELTA_APPROXIMATION'&&is.finite(rms$design_se)&&rms$design_se>0&&
      abs(rms$upper-rms$estimate-qnorm(.975)*rms$design_se)<1e-12,'normal/delta RMS interval through (I-DK) Cov(m) (I-DK)t')
    sets <- if(name=='M3')list(block1=paste0('q',1:3),block2=paste0('q',4:6),block3=paste0('q',7:9))else
      if(name=='M2')list(block1=paste0('q',1:3),block6=paste0('q',4:9))else list(all9=paste0('q',1:9))
    score_outputs <- list()
    for(score_name in names(sets)) {
      items <- sets[[score_name]]; spec <- os_score_spec(manifest,items)
      score <- os_score(sw,manifest,items); raw <- os_raw_score(adapter,manifest,items)
      second <- os_score(sw,manifest,items,step=2e-5)
      comp <- os_score_components(context,context$x,spec)
      syntax <- paste0('score <~ ',paste(paste0(1/(length(items)*(categories[match(items,names(manifest))]-1)),
                            '*',items),collapse=' + '))
      oracle <- oa_quiet(semTools::compRelSEM(fit$private,W=syntax,ord.scale=TRUE,obs.var=FALSE,simplify=-1L))
      oracle <- as.numeric(unlist(oracle,use.names=FALSE))
      stopifnot(length(oracle)==1L)
      integ <- conditional_integral(context,spec)
      check(paste0(name,'_',score_name,'_observed_reliability'),list(value=comp$reliability,semTools=oracle,
        conditional_integral=unname(integ['reliability']),true_variance=comp$true_variance,
        error_variance=comp$error_variance),abs(comp$reliability-oracle)<=2e-6&&
        abs(comp$reliability-integ['reliability'])<=2e-6,
        'mixed category normalized observed score vs actual semTools W oracle and independent conditional integration <=2e-6')
      check(paste0(name,'_',score_name,'_score_gradient'),md(score$gradient,second$gradient),
        md(score$gradient,second$gradient)<=2e-5,'central free-parameter derivative comparison across 1e-5/2e-5 steps')
      r <- score$results$reliability
      check(paste0(name,'_',score_name,'_score_ci'),r,r$design_se>0&&
        abs(r$lower-r$estimate+qnorm(.975)*r$design_se)<1e-12,'normal CI from gradient Vbeta gradientt, not individual measurement uncertainty')
      # Independent direct weighted population-moment identity for observed covariance.
      xx <- sapply(items,function(item)dat[domain,item]/max(manifest[[item]]))
      ww <- weight[domain]/sum(weight[domain]); s <- rowMeans(xx)
      mu <- colSums(xx*ww); mus <- sum(s*ww); v <- sum(ww*s^2)-mus^2
      cs <- colSums(xx*s*ww)-mu*mus
      check(paste0(name,'_',score_name,'_raw_dominance'),list(sum=sum(raw$dominance),
        max_difference=md(cs/(length(items)*v),raw$dominance)),
        md(cs/(length(items)*v),raw$dominance)<=1e-10&&abs(sum(raw$dominance)-1)<=1e-10&&
        md(rowSums(raw$item_covariance)/length(items),raw$covariance_with_score)<=1e-10,
        'raw weighted second moments vs centered covariance; exact Cov(xj,S)/(k Var(S)) and sum1')
      score_outputs[[score_name]] <- list(model=score,raw=raw)
    }
    outputs[[name]] <- list(fit=fit$aggregate,sandwich=sw$aggregate,standardized=std,
                            residual_rms=rms,scores=score_outputs)
    if(name=='M3') {
      direction <- sin(seq_along(adapter$moments)/7); direction[1:51] <- direction[1:51]*.3
      step <- .00025
      plus <- oracle_refit(perturbed_adapter(adapter,adapter$moments+step*direction),models[[name]])
      minus <- oracle_refit(perturbed_adapter(adapter,adapter$moments-step*direction),models[[name]])
      actual <- (os_context(plus)$x-os_context(minus)$x)/(2*step)
      predicted <- as.numeric(p$k %*% direction)
      err <- md(actual,predicted)
      check('actual_misfit_refit_parameter_influence',list(error=err,step=step,
        expected_projection_error=md(actual,as.numeric(expected_sw$private$k%*%direction))),err<=2e-5,
        'full actual +/- summary-moment refits vs observed estimating-Jacobian K at actual misfit point <=2e-5')
      ar <- ((adapter$moments+step*direction)-lavaan::lavInspect(plus$private,'wls.est')-
             ((adapter$moments-step*direction)-lavaan::lavInspect(minus$private,'wls.est')))/(2*step)
      err <- md(ar,as.numeric(p$residual_transform%*%direction))
      check('actual_misfit_refit_residual_influence',err,err<=2e-5,
        'actual fitted residual refits vs I-DK using observed Jacobian <=2e-5')
      rmsactual <- (sqrt(mean((adapter$moments[-(1:51)]+step*direction[-(1:51)]-
        lavaan::lavInspect(plus$private,'wls.est')[-(1:51)])^2))-
        sqrt(mean((adapter$moments[-(1:51)]-step*direction[-(1:51)]-
        lavaan::lavInspect(minus$private,'wls.est')[-(1:51)])^2)))/(2*step)
      rmsprojected <- as.numeric(crossprod(rms$gradient,p$residual_transform%*%direction))
      check('actual_misfit_refit_rms_derivative',list(error=abs(rmsactual-rmsprojected),step=step),
        abs(rmsactual-rmsprojected)<=2e-5,'actual RMS refit derivative vs full observed delta chain <=2e-5')
      # On a model-exact moment point the expected projection has an actual refit oracle.
      exact_m <- os_at(context,context$x)$moments
      exact_adapter <- perturbed_adapter(adapter,exact_m)
      exact_fit <- oa_fit(exact_adapter,models[[name]])
      exact_sw <- os_sandwich(exact_adapter,exact_fit)
      near <- os_residual_rms(exact_sw,zero_tolerance=1e-7)
      check('near_zero_rms_explicit_undefined',near,near$status=='DELTA_UNDEFINED_NEAR_ZERO'&&is.na(near$design_se),
        'undefined nearzero norm derivative never becomes zero certainty')
      direction <- sin(seq_along(exact_m)/7); direction[1:51] <- direction[1:51]*.3
      step <- 2e-5
      plus <- oa_fit(perturbed_adapter(adapter,exact_m+step*direction),models[[name]])
      minus <- oa_fit(perturbed_adapter(adapter,exact_m-step*direction),models[[name]])
      actual <- (os_context(plus)$x-os_context(minus)$x)/(2*step)
      predicted <- as.numeric(exact_sw$private$k %*% direction)
      err <- md(actual,predicted)
      check('model_exact_refit_parameter_projection',err,err<=2e-5,
        'actual +/- summary-moment refits at model-exact point vs expected DWLS K direction <=2e-5')
      ar <- ((exact_m+step*direction)-lavaan::lavInspect(plus$private,'wls.est')-
             ((exact_m-step*direction)-lavaan::lavInspect(minus$private,'wls.est')))/(2*step)
      err <- md(ar,as.numeric(exact_sw$private$residual_transform%*%direction))
      check('model_exact_refit_residual_projection',err,err<=2e-5,
        'actual fitted-model residual derivative vs (I-DK) at model-exact point <=2e-5')
    }
  }
  efa <- list()
  for(factors in 1:3) {
    fit <- oa_fit(adapter,NULL,efa_factors=factors)
    efa[[as.character(factors)]] <- fit$aggregate
    check(paste0('actual_external_efa',factors),fit$aggregate,fit$aggregate$df==c(27,19,12)[factors],
      'genuine external-summary EFA with imported own Gamma/WLS; no rotated SE claim')
    expect_stop(paste0('reject_rotated_efa_se',factors),os_sandwich(adapter,fit),'ROTATED_EFA_SE_UNSUPPORTED')
  }
  # The existing adapter is preserved. These are diagnoses, not test-success claims.
  for(rho in c(.85,.95)) {
    for(k in c(5L,11L)) {
      thresholds <- qnorm(seq_len(k-1L)/k)
      key <- paste0('rho',rho,'_k',k)
      got <- tryCatch({r<-oa_rect(thresholds,thresholds,rho);list(status='EXECUTED',minimum=min(r$p))},
                      error=function(e)list(status='STOPPED',code=conditionMessage(e)))
      diagnostic[[key]] <<- got
    }
  }
  expect_stop('inadmissible_parameter_stops',{
    context <- os_context(oa_fit(adapter,models$M3)); x <- context$x
    x[which(grepl('~~',names(x),fixed=TRUE))[1]] <- 2; os_at(context,x)
  },'LATENT_COVARIANCE')
  list(configuration=list(seed=2026100321L,n=n,psus=g,strata=4L,categories=categories,metric=metric,
    mask='four whole domain-null PSUs, all-nine complete synthetic items'),
    outputs=outputs,efa=efa,adapter_diagnostics=diagnostic,
    limits=c('All invented synthetic responses; no ESS empirical run or scientific acceptance',
      'normal/delta model-conditional approximations with fixed weights and DWLS metric; no coverage study',
      'Gamma uses exact observed-score Jacobian adapter; native oracle is never its assumed OPG replacement',
      'real observed category covariances and model-implied observed score covariance reported separately'))
}
fatal <- NULL; fatal_calls <- NULL
result <- tryCatch(withCallingHandlers(run(),warning=function(w){
  warnings_seen <<- c(warnings_seen,conditionMessage(w));invokeRestart('muffleWarning')},
  error=function(e){fatal_calls <<- vapply(sys.calls(),function(x)deparse(x[[1]])[1L],character(1))}),
  error=function(e){fatal <<- conditionMessage(e);list()})
result$checks <- checks;result$warnings <- warnings_seen;result$fatal <- fatal
result$fatal_calls <- fatal_calls
result$diagnostic_if_early_stop <- diagnostic
result$runtime <- list(R=R.version.string,lavaan=as.character(packageVersion('lavaan')),
  pbivnorm=as.character(packageVersion('pbivnorm')),semTools=as.character(packageVersion('semTools')),
  jsonlite=as.character(packageVersion('jsonlite')),HOME=Sys.getenv('HOME'),libraries=.libPaths(),temp=tempdir())
result$status <- if(is.null(fatal)&&length(checks)>0&&all(vapply(checks,function(x)x$status=='BESTANDEN',logical(1)))&&
  length(warnings_seen)==0L)'SYNTHETIC_SUPPORT_CHECKS_PASSED'else'SYNTHETIC_SUPPORT_CHECKS_FAILED'
jsonlite::write_json(result,file.path(own,paste0(args[[4]],'-result.json')),auto_unbox=TRUE,pretty=TRUE,digits=16,na='null')
cat(result$status,'\n')
quit(status=if(result$status=='SYNTHETIC_SUPPORT_CHECKS_PASSED')0L else 1L)
