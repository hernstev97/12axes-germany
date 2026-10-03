# Author numerical diagnostics for a fixed single-group ordinal CFA.
# No file reads/exports, data selection, cutoffs, or scientific gate.
os_stop <- function(code) stop(paste0('ORDINAL_SUPPORT_',code),call.=FALSE)
os_fun <- function(name) getFromNamespace(name,'lavaan')
os_sym <- function(x) (x+t(x))/2
os_fixed_metric <- function(adapter) {
  if(!inherits(adapter,'oa_adapter')) os_stop('ADAPTER_CLASS')
  labels <- names(adapter$moments)
  if(is.null(labels) || anyDuplicated(labels) ||
     !identical(dimnames(adapter$wls_v),list(labels,labels)) ||
     !identical(dimnames(adapter$covariance),list(labels,labels))) os_stop('MOMENT_BINDING')
  out <- adapter
  out$wls_v <- diag(length(labels))
  dimnames(out$wls_v) <- list(labels,labels)
  out$aggregate$point_metric <- 'fixed identity on ordered thresholds and polychoric correlations'
  out$aggregate$point_estimator <- 'unweighted least-squares external moment fit; nominal lavaan DWLS engine only'
  out
}
# Explicit alias requested by the coordinator; returns a copy, never changes
# adapter.R or the supplied adapter object.
oa_fixed_metric <- os_fixed_metric
os_check_spd <- function(x,code) {
  if(!is.matrix(x) || nrow(x)!=ncol(x) || any(!is.finite(x)) ||
     max(abs(x-t(x)))>1e-8 || min(eigen(os_sym(x),symmetric=TRUE,only.values=TRUE)$values)<=0)
    os_stop(code)
  invisible(TRUE)
}
os_context <- function(fit) {
  oa_runtime()
  if(!inherits(fit,'oa_fit') || !inherits(fit$private,'lavaan')) os_stop('FIT_CLASS')
  if(!is.null(fit$aggregate$efa_factors)) os_stop('ROTATED_EFA_SE_UNSUPPORTED')
  f <- fit$private; m <- f@Model; pt <- lavaan::parTable(f)
  if(lavaan::lavInspect(f,'ngroups')!=1L || m@multilevel || m@conditional.x ||
     m@representation!='LISREL' || m@parameterization!='theta' ||
     any(pt$op %in% c('==','<','>','~',':=')) || any(pt$op=='~*~' & pt$free>0L) ||
     anyDuplicated(pt$free[pt$free>0L]) ||
     !isTRUE(lavaan::lavInspect(f,'converged')) || !isTRUE(lavaan::lavInspect(f,'post.check')))
    os_stop('MODEL_CONTRACT')
  x <- os_fun('lav_model_get_parameters')(m)
  # Call the pinned namespace implementation. stats::coef without attaching
  # lavaan can take its default $coefficients route on the S4 object.
  coefficients <- os_fun('lav_inspect_coef')(f,type='free',add_labels=TRUE)
  labels <- names(coefficients)
  if(length(x)!=length(labels) || anyDuplicated(labels) || length(x)!=m@nx.free ||
     max(abs(x-coefficients))>1e-10)
    os_stop('FREE_PARAMETER_ORDER')
  names(x) <- labels
  g <- m@GLIST
  if(!all(c('lambda','theta','psi','tau') %in% names(g)) ||
     any(g$theta[lower.tri(g$theta)]!=0) ||
     !is.null(g$beta) && any(g$beta!=0) ||
     !is.null(g$nu) && any(g$nu!=0) || !is.null(g$alpha) && any(g$alpha!=0))
    os_stop('CFA_LOCAL_INDEPENDENCE')
  list(fit=f,model=m,x=x,parameter_labels=labels,
       moment_labels=names(lavaan::lavInspect(f,'wls.obs')),
       ov_names=lavaan::lavNames(f,'ov'),lv_names=lavaan::lavNames(f,'lv'))
}
os_at <- function(context,x) {
  if(length(x)!=length(context$x) || any(!is.finite(x))) os_stop('PARAMETER_VECTOR')
  m <- os_fun('lav_model_set_parameters')(context$model,as.numeric(x))
  g <- m@GLIST
  dimnames(g$lambda) <- list(context$ov_names,context$lv_names)
  dimnames(g$theta) <- list(context$ov_names,context$ov_names)
  dimnames(g$psi) <- list(context$lv_names,context$lv_names)
  phi <- g$psi; theta <- g$theta
  os_check_spd(phi,'LATENT_COVARIANCE')
  if(any(diag(theta)<=0) || any(theta[lower.tri(theta)]!=0)) os_stop('RESIDUAL_VARIANCE')
  common <- g$lambda %*% phi %*% t(g$lambda)
  total <- common+theta
  os_check_spd(total,'RESPONSE_COVARIANCE')
  implied <- os_fun('lav_model_implied')(m)
  moments <- os_fun('lav_model_wls_est')(m,lavimplied=implied)[[1L]]
  if(length(moments)!=length(context$moment_labels) || any(!is.finite(moments)))
    os_stop('IMPLIED_MOMENT_ORDER')
  names(moments) <- context$moment_labels
  list(model=m,glist=g,common=common,total=total,sd=sqrt(diag(total)),
       implied=implied,moments=moments)
}
os_numeric_jacobian <- function(fun,x,relative_step=1e-5) {
  if(!is.numeric(relative_step) || length(relative_step)!=1L || !is.finite(relative_step) || relative_step<=0)
    os_stop('DERIVATIVE_STEP')
  center <- fun(x)
  if(!is.numeric(center) || any(!is.finite(center))) os_stop('FUNCTION_VALUE')
  ans <- matrix(0,length(center),length(x),dimnames=list(names(center),names(x)))
  for(j in seq_along(x)) {
    step <- relative_step*max(1,abs(x[j])); a <- b <- x
    a[j] <- a[j]+step; b[j] <- b[j]-step
    plus <- fun(a); minus <- fun(b)
    if(!identical(names(plus),names(center)) || !identical(names(minus),names(center)) ||
       any(!is.finite(c(plus,minus)))) os_stop('DERIVATIVE_DOMAIN')
    ans[,j] <- (plus-minus)/(2*step)
  }
  ans
}
os_interval <- function(value,variance,level=.95) {
  if(!is.numeric(level) || length(level)!=1L || !is.finite(level) || level<=0 || level>=1)
    os_stop('CI_LEVEL')
  if(!is.finite(value) || !is.finite(variance) || variance<0) os_stop('DELTA_VARIANCE')
  se <- sqrt(variance); critical <- qnorm((1+level)/2)
  list(estimate=unname(value),design_se=se,lower=value-critical*se,upper=value+critical*se,
       level=level,method='normal first-order delta; raw interval without truncation')
}
os_sandwich <- function(adapter,fit,bread_method='observed',step=1e-5) {
  if(!inherits(adapter,'oa_adapter')) os_stop('ADAPTER_CLASS')
  context <- os_context(fit); f <- context$fit
  labels <- names(adapter$moments)
  if(!identical(labels,context$moment_labels) ||
     max(abs(lavaan::lavInspect(f,'wls.obs')-adapter$moments))>1e-7 ||
     !identical(dimnames(adapter$covariance),list(labels,labels)) ||
     !identical(dimnames(adapter$wls_v),list(labels,labels)) ||
     max(abs(adapter$gamma-adapter$aggregate$n_complete*adapter$covariance))>1e-7)
    os_stop('MOMENT_BINDING')
  for(pair in list(list('gamma',adapter$gamma),list('wls.v',adapter$wls_v))) {
    actual <- lavaan::lavInspect(f,pair[[1]])
    if(!identical(dimnames(actual),dimnames(pair[[2]])) || max(abs(actual-pair[[2]]))>1e-7)
      os_stop('IMPORT_BINDING')
  }
  d <- lavaan::lavInspect(f,'delta')
  if(!is.matrix(d) || nrow(d)!=length(labels) || ncol(d)!=length(context$x) ||
     !identical(rownames(d),labels) || !identical(colnames(d),context$parameter_labels))
    os_stop('DELTA_LABELS')
  w <- adapter$wls_v; v <- adapter$covariance
  if(any(w[row(w)!=col(w)]!=0) || any(diag(w)<=0)) os_stop('DWLS_METRIC')
  os_check_spd(v,'MOMENT_COVARIANCE')
  if(!bread_method %in% c('observed','expected')) os_stop('BREAD_METHOD')
  expected_bread <- crossprod(d,w %*% d)
  os_check_spd(expected_bread,'UNIDENTIFIED_MODEL')
  if(qr(d,tol=1e-9)$rank!=ncol(d)) os_stop('UNIDENTIFIED_MODEL')
  # Differentiate the actual DWLS estimating equation at its fitted point.
  # J includes the residual-dependent derivative of Delta, with W held fixed.
  score <- function(x) {
    a <- os_at(context,x)
    dx <- os_fun('lav_model_delta')(a$model)[[1L]]
    if(!identical(dim(dx),dim(d)) || any(!is.finite(dx))) os_stop('LOCAL_DELTA')
    setNames(as.numeric(crossprod(dx,w %*% (adapter$moments-a$moments))),context$parameter_labels)
  }
  jacobian <- os_numeric_jacobian(score,context$x,step)
  bread <- if(bread_method=='observed') -jacobian else expected_bread
  os_check_spd(bread,'ESTIMATING_JACOBIAN')
  k <- solve(bread,crossprod(d,w))
  dimnames(k) <- list(context$parameter_labels,labels)
  vb <- os_sym(k %*% v %*% t(k))
  os_check_spd(vb,'PARAMETER_COVARIANCE')
  transform <- diag(length(labels))-d %*% k
  dimnames(transform) <- list(labels,labels)
  residual_covariance <- os_sym(transform %*% v %*% t(transform))
  names(context$x) <- context$parameter_labels
  structure(list(private=list(context=context,delta=d,k=k,bread=bread,jacobian=jacobian,
      expected_bread=expected_bread,parameter_covariance=vb,
      residual_transform=transform,residual_covariance=residual_covariance,
      adapter=adapter),aggregate=list(moment_count=length(labels),free_parameters=length(context$x),
      delta_rank=qr(d,tol=1e-9)$rank,design_df=adapter$aggregate$design_df,
      bread_method=bread_method,jacobian_step=step,
      point_metric=if(is.null(adapter$aggregate$point_metric))
        'sample-estimated native iid DWLS diagonal treated as fixed in this diagnostic' else adapter$aggregate$point_metric,
      estimating_score_max=max(abs(score(context$x))),
      observed_expected_bread_max_difference=max(abs(-jacobian-expected_bread)),
      estimator=if(bread_method=='observed')
        'psi=D(theta)t W [s-m(theta)]; J=dpsi/dtheta; K=-J^-1 DtW; Vbeta=K Cov(m) Kt' else
        'model-correctness-conditional expected projection K=(DtWD)^-1 DtW; Vbeta=K Cov(m) Kt',
      limits=c('single-group identified unconstrained CFA only; local normal/delta approximation',
        if(bread_method=='observed') 'point metric held fixed; observed Jacobian includes fitted residual curvature' else
          'expected projection is conditional on model correctness; residual curvature omitted',
        'WR ultimate-PSU approximation; no FPC/PPS-WOR or calibration/nonresponse-weight uncertainty',
        'no model-selection, rotation, small-PSU coverage or personal measurement uncertainty'))),
    class='os_sandwich')
}
os_delta <- function(sandwich,fun,level=.95,step=1e-5) {
  if(!inherits(sandwich,'os_sandwich')) os_stop('SANDWICH_CLASS')
  p <- sandwich$private; x <- p$context$x
  estimate <- fun(x); gradient <- os_numeric_jacobian(fun,x,step)
  covariance <- os_sym(gradient %*% p$parameter_covariance %*% t(gradient))
  results <- lapply(seq_along(estimate),function(i)os_interval(estimate[i],covariance[i,i],level))
  names(results) <- names(estimate)
  list(results=results,gradient=gradient,covariance=covariance,relative_step=step)
}
os_standardized <- function(sandwich,level=.95,step=1e-5) {
  context <- sandwich$private$context
  base <- os_at(context,context$x); index <- which(base$glist$lambda!=0,arr.ind=TRUE)
  pairs <- which(lower.tri(base$glist$psi),arr.ind=TRUE)
  labels <- c(apply(index,1L,function(a)paste0(colnames(base$glist$lambda)[a[2]],'=~',
      rownames(base$glist$lambda)[a[1]])),apply(pairs,1L,function(a)
      paste0(colnames(base$glist$psi)[a[2]],'~~',colnames(base$glist$psi)[a[1]])))
  fun <- function(x) {
    a <- os_at(context,x); g <- a$glist
    loading <- sweep(sweep(g$lambda,2L,sqrt(diag(g$psi)),'*'),1L,a$sd,'/')
    phi <- stats::cov2cor(g$psi)
    setNames(c(loading[index],phi[pairs]),labels)
  }
  os_delta(sandwich,fun,level,step)
}
# Covariance of cumulative indicators under a standard bivariate normal.
# Exact degenerate correlations are used only for marginal observed variances.
os_cdf_cov <- function(a,b,rho) {
  if(length(rho)!=1L || !is.finite(rho) || abs(rho)>1 || any(!is.finite(c(a,b))))
    os_stop('NORMAL_DOMAIN')
  aa <- rep(a,times=length(b)); bb <- rep(b,each=length(a))
  joint <- if(rho==1) pnorm(pmin(aa,bb)) else if(rho== -1)
    pmax(pnorm(aa)-pnorm(-bb),0) else pbivnorm::pbivnorm(aa,bb,rho)
  matrix(joint-pnorm(aa)*pnorm(bb),length(a),length(b))
}
os_score_spec <- function(manifest,items,scores=NULL) {
  manifest <- oa_manifest(manifest)
  if(!is.character(items) || length(items)<2L || anyDuplicated(items) || any(!items %in% names(manifest)))
    os_stop('SCORE_ITEMS')
  if(is.null(scores)) scores <- lapply(manifest[items],function(v)(v-min(v))/(max(v)-min(v)))
  if(!is.list(scores) || !identical(names(scores),items)) os_stop('SCORE_CODING')
  for(j in seq_along(items)) if(!is.numeric(scores[[j]]) || length(scores[[j]])!=length(manifest[[items[j]]]) ||
      any(!is.finite(scores[[j]])) || any(scores[[j]]<0|scores[[j]]>1) ||
      !all(diff(scores[[j]])>0) && !all(diff(scores[[j]])<0)) os_stop('SCORE_CODING')
  list(items=items,scores=scores,manifest=manifest)
}
os_score_components <- function(context,x,spec) {
  a <- os_at(context,x); vars <- rownames(a$glist$lambda)
  index <- match(spec$items,vars)
  if(anyNA(index)) os_stop('SCORE_MODEL_ITEMS')
  common <- a$common[index,index,drop=FALSE]/outer(a$sd[index],a$sd[index])
  total <- stats::cov2cor(a$total[index,index,drop=FALSE])
  all_th <- a$moments[grepl('|',names(a$moments),fixed=TRUE)]
  thresholds <- lapply(spec$items,function(item)unname(all_th[startsWith(names(all_th),paste0(item,'|'))]))
  if(any(lengths(thresholds)!=lengths(spec$scores)-1L) ||
     any(vapply(thresholds,function(t)is.unsorted(t,strictly=TRUE),logical(1)))) os_stop('SCORE_THRESHOLDS')
  k <- length(index); observed <- true <- matrix(0,k,k,dimnames=list(spec$items,spec$items))
  means <- numeric(k)
  for(i in seq_len(k)) {
    increments <- diff(spec$scores[[i]])
    means[i] <- spec$scores[[i]][1]+sum(increments*pnorm(thresholds[[i]],lower.tail=FALSE))
    for(j in seq_len(i)) {
      wi <- increments; wj <- diff(spec$scores[[j]])
      observed[i,j] <- observed[j,i] <- sum(outer(wi,wj)*os_cdf_cov(thresholds[[i]],thresholds[[j]],total[i,j]))
      true[i,j] <- true[j,i] <- sum(outer(wi,wj)*os_cdf_cov(thresholds[[i]],thresholds[[j]],common[i,j]))
    }
  }
  v <- sum(observed)/k^2; t <- sum(true)/k^2
  if(!is.finite(v) || v<=0 || !is.finite(t) || t<0 || t>v) os_stop('SCORE_VARIANCE')
  # Cov(x_j,S)/(k Var(S)); sum equals one, contributions need not be equal.
  dominance <- rowSums(observed)/(k^2*v)
  list(mean=mean(means),observed_variance=v,true_variance=t,error_variance=v-t,
       reliability=t/v,item_covariance=observed,true_covariance=true,
       covariance_with_score=rowSums(observed)/k,dominance=dominance,
       thresholds=thresholds,standard_common=common,standard_total=total)
}
os_score <- function(sandwich,manifest,items,scores=NULL,level=.95,step=1e-5) {
  spec <- os_score_spec(manifest,items,scores); context <- sandwich$private$context
  fun <- function(x) {
    a <- os_score_components(context,x,spec)
    c(reliability=a$reliability,mean=a$mean,observed_variance=a$observed_variance,
      true_variance=a$true_variance,error_variance=a$error_variance,
      setNames(a$dominance,paste0('dominance:',items)))
  }
  out <- os_delta(sandwich,fun,level,step)
  a <- os_score_components(context,context$x,spec)
  out$components <- a[c('item_covariance','true_covariance','covariance_with_score','dominance')]
  out$definition <- 'S=mean(normalized observed category values); reliability=Var(E[S|all eta])/Var(S)'
  out$limits <- c('Gaussian CFA, fixed coding/polarity, local independence and all modeled common factors',
    'model-implied observed-score denominator; no latent-response omega substitution',
    'equal score weights alone do not establish absence of item dominance',
    'normal delta CI conditional on selected model; no coverage or personal interval claim')
  out
}
os_raw_score <- function(adapter,manifest,items,scores=NULL,level=.95) {
  if(!inherits(adapter,'oa_adapter')) os_stop('ADAPTER_CLASS')
  spec <- os_score_spec(manifest,items,scores)
  prep <- adapter$private$prepared
  if(!identical(spec$manifest,prep$manifest)) os_stop('MANIFEST_BINDING')
  keep <- prep$mask; k <- length(items); n <- length(keep)
  xx <- matrix(0,sum(keep),k,dimnames=list(NULL,items))
  for(j in seq_len(k)) xx[,j] <- spec$scores[[j]][prep$coded[keep,items[j]]]
  w <- prep$weight[keep]/sum(prep$weight[keep]); s <- rowMeans(xx)
  mu <- colSums(xx*w); mus <- sum(s*w)
  xc <- sweep(xx,2L,mu); sc <- s-mus
  covariance <- crossprod(xc,xc*w)
  variance <- sum(w*sc^2); cs <- colSums(xc*sc*w)
  if(!is.finite(variance) || variance<=0) os_stop('RAW_SCORE_VARIANCE')
  dominance <- cs/(k*variance)
  values <- c(mean=mus,variance=variance,setNames(cs,paste0('covariance:',items)),
              setNames(dominance,paste0('dominance:',items)))
  local <- cbind(mean=w*sc,variance=w*(sc^2-variance),
    sweep(xc*sc,2L,cs)*w,
    (sweep(xc*sc,2L,cs)-outer(sc^2-variance,cs/variance))*w/(k*variance))
  contributions <- matrix(0,n,length(values),dimnames=list(NULL,names(values)))
  contributions[keep,] <- local
  v <- oa_taylor(contributions,prep$design)
  results <- lapply(seq_along(values),function(j)os_interval(values[j],v[j,j],level))
  names(results) <- names(values)
  list(results=results,item_covariance=covariance,covariance_with_score=cs,dominance=dominance,
       definition='Exact weighted observed category covariance; Cov(xj,S)/(k Var(S))',
       mask='same all-nine complete domain as adapter; separate score/norm masks require separate design computation',
       limits=c('centered ratio-moment Taylor IF; full original PSU/stratum set including null-domain PSUs',
         'fixed category coding/polarity and fixed weights; WR ultimate-PSU normal CI',
         'equal weights do not imply equal covariance contributions; no latent reliability claim'))
}
os_residual_rms <- function(sandwich,level=.95,zero_tolerance=1e-8) {
  p <- sandwich$private; labels <- names(p$adapter$moments)
  if(!is.numeric(zero_tolerance) || length(zero_tolerance)!=1L || !is.finite(zero_tolerance) || zero_tolerance<=0)
    os_stop('ZERO_TOLERANCE')
  fitted <- os_at(p$context,p$context$x)$moments
  index <- which(grepl('~~',labels,fixed=TRUE))
  residual <- p$adapter$moments[index]-fitted[index]
  value <- sqrt(mean(residual^2))
  if(value<=zero_tolerance) return(list(estimate=value,status='DELTA_UNDEFINED_NEAR_ZERO',
    design_se=NA_real_,lower=NA_real_,upper=NA_real_,zero_tolerance=zero_tolerance,
    reason='Euclidean norm is nondifferentiable at zero; no false zero-uncertainty claim'))
  gradient <- numeric(length(labels)); names(gradient) <- labels
  gradient[index] <- residual/(length(index)*value)
  variance <- as.numeric(crossprod(gradient,p$residual_covariance %*% gradient))
  out <- os_interval(value,variance,level)
  out$status <- 'NORMAL_DELTA_APPROXIMATION'
  out$gradient <- gradient
  out$definition <- 'RMS of 36 fitted-model residual polychoric correlations; residual IF=(I-DK) IF(m)'
  out$limits <- c('first-order fitted-model projection, fixed DWLS metric',
    'nearzero RMS delta interval undefined; no model-fit or coverage guarantee')
  out
}
print.os_sandwich <- function(x,...) {
  cat('Ordinal CFA sandwich: ',x$aggregate$moment_count,' moments; ',x$aggregate$free_parameters,
      ' free parameters.\n',sep=''); invisible(x)
}
