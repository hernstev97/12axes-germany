# Author v2 candidate. Occupied-cell score and valid interior bracket only.
# Original adapter.R preserved; no file reads/exports or empirical approval.
# Private in-memory inputs never appear in condition messages or default print.
oa_stop <- function(code) stop(paste0('ORDINAL_ADAPTER_', code), call.=FALSE)
oa_runtime <- function() {
  if (!identical(as.character(getRversion()), '4.5.3') ||
      !requireNamespace('lavaan',quietly=TRUE) ||
      !identical(as.character(packageVersion('lavaan')), '0.7.2') ||
      !requireNamespace('pbivnorm',quietly=TRUE) ||
      !identical(as.character(packageVersion('pbivnorm')), '0.6.0')) oa_stop('VERSION')
  invisible(TRUE)
}
oa_quiet <- function(expr) {
  # Fixed error code; library messages can contain private input values.
  had_warning <- FALSE
  discarded <- capture.output(value <- tryCatch(withCallingHandlers(expr,
    warning=function(w) { had_warning <<- TRUE; invokeRestart('muffleWarning') },
    message=function(m) invokeRestart('muffleMessage')),
    error=function(e) oa_stop('LIBRARY_ERROR')))
  if(had_warning) oa_stop('LIBRARY_WARNING')
  value
}
oa_manifest <- function(manifest) {
  if(!is.list(manifest) || length(manifest)!=9L || is.null(names(manifest)) ||
     anyDuplicated(names(manifest)) || any(!grepl('^[A-Za-z][A-Za-z0-9_]*$',names(manifest))))
    oa_stop('NINE_ITEM_MANIFEST')
  for(v in manifest) if(!is.numeric(v) || length(v)<2L || any(!is.finite(v)) ||
      any(v!=floor(v)) || anyDuplicated(v) || is.unsorted(v, strictly=TRUE)) oa_stop('CATEGORY_MANIFEST')
  manifest
}
oa_labels <- function(manifest) {
  thresholds <- unlist(lapply(seq_along(manifest),function(j)
    paste0(names(manifest)[j],'|t',seq_len(length(manifest[[j]])-1L))),use.names=FALSE)
  pairs <- which(lower.tri(matrix(0,9L,9L)),arr.ind=TRUE)
  correlations <- apply(pairs,1L,function(x) paste0(names(manifest)[x[2]],'~~',names(manifest)[x[1]]))
  c(thresholds,correlations)
}
oa_design <- function(weight,psu,stratum,n,min_df=1L) {
  if(!is.numeric(weight) || length(weight)!=n || any(!is.finite(weight)) || any(weight<=0))
    oa_stop('WEIGHT')
  if(length(psu)!=n || length(stratum)!=n || !is.atomic(psu) || !is.atomic(stratum) ||
     anyNA(psu) || anyNA(stratum)) oa_stop('DESIGN_MISSING')
  if(is.numeric(psu) && any(!is.finite(psu)) || is.numeric(stratum) && any(!is.finite(stratum)))
    oa_stop('DESIGN_NONFINITE')
  if(any(!nzchar(as.character(psu))) || any(!nzchar(as.character(stratum)))) oa_stop('DESIGN_EMPTY')
  # No automatic renesting. A repeated PSU token across strata is rejected.
  p <- match(psu,unique(psu)); h <- match(stratum,unique(stratum))
  ph <- vapply(seq_len(max(p)),function(k) {
    hs <- unique(h[p==k]); if(length(hs)!=1L) oa_stop('PSU_NESTING'); hs
  },integer(1))
  g <- tabulate(ph,nbins=max(h))
  if(any(g<2L)) oa_stop('SINGLETON_STRATUM')
  df <- length(ph)-length(g)
  if(!is.numeric(min_df) || length(min_df)!=1L || !is.finite(min_df) || min_df<1L || df<min_df)
    oa_stop('DESIGN_DF')
  list(psu=p,stratum=h,psu_stratum=ph,psus_by_stratum=g,df=df)
}
oa_taylor <- function(contributions,design) {
  if(!is.matrix(contributions) || nrow(contributions)!=length(design$psu) ||
     any(!is.finite(contributions))) oa_stop('CONTRIBUTION')
  totals <- matrix(0,length(design$psu_stratum),ncol(contributions))
  for(p in seq_len(nrow(totals))) totals[p,] <- colSums(contributions[design$psu==p,,drop=FALSE])
  out <- matrix(0,ncol(contributions),ncol(contributions))
  for(h in seq_along(design$psus_by_stratum)) {
    block <- totals[design$psu_stratum==h,,drop=FALSE]
    g <- nrow(block)
    if(g<2L) oa_stop('SINGLETON_STRATUM')
    centered <- sweep(block,2L,colMeans(block))
    out <- out + g/(g-1)*crossprod(centered)
  }
  dimnames(out) <- list(colnames(contributions),colnames(contributions))
  out
}
oa_prepare <- function(items,manifest,weight,psu,stratum,domain) {
  oa_runtime(); manifest <- oa_manifest(manifest)
  if(!is.data.frame(items) || !identical(names(items),names(manifest))) oa_stop('ITEM_FRAME')
  n <- nrow(items)
  if(!is.logical(domain) || length(domain)!=n || anyNA(domain)) oa_stop('DOMAIN')
  design <- oa_design(weight,psu,stratum,n,min_df=length(oa_labels(manifest)))
  coded <- matrix(NA_integer_,n,9L,dimnames=list(NULL,names(manifest)))
  for(j in seq_len(9L)) {
    x <- items[[j]]
    if(!is.numeric(x) || any(!is.na(x) & !is.finite(x))) oa_stop('ITEM_TYPE')
    if(any(!is.na(x) & !x %in% manifest[[j]])) oa_stop('CATEGORY_OUTSIDE_MANIFEST')
    coded[,j] <- match(x,manifest[[j]])
  }
  mask <- domain & complete.cases(coded)
  if(sum(mask)<=length(oa_labels(manifest))+1L) oa_stop('COMPLETE_N')
  for(j in seq_len(9L)) if(any(tabulate(coded[mask,j],nbins=length(manifest[[j]]))==0L))
    oa_stop('EMPTY_CATEGORY')
  if(!is.finite(sum(weight[mask])) || sum(weight[mask])<=0) oa_stop('WEIGHT_SUM')
  list(coded=coded,manifest=manifest,weight=weight,mask=mask,design=design)
}
# Analytic bivariate normal CDF with exact infinite-boundary cases.
oa_bvn <- function(a,b,rho) {
  a <- rep(a,length.out=max(length(a),length(b))); b <- rep(b,length.out=length(a))
  out <- numeric(length(a)); neg <- a==-Inf | b==-Inf
  both <- a==Inf & b==Inf; out[both] <- 1
  onlya <- a==Inf & is.finite(b); out[onlya] <- pnorm(b[onlya])
  onlyb <- b==Inf & is.finite(a); out[onlyb] <- pnorm(a[onlyb])
  finite <- is.finite(a)&is.finite(b)
  if(any(finite)) out[finite] <- pbivnorm::pbivnorm(a[finite],b[finite],rho)
  out[neg] <- 0; out
}
oa_bvn_density <- function(a,b,rho) {
  out <- numeric(length(a)); keep <- is.finite(a)&is.finite(b)
  out[keep] <- exp(-(a[keep]^2-2*rho*a[keep]*b[keep]+b[keep]^2)/(2*(1-rho^2))) /
    (2*pi*sqrt(1-rho^2)); out
}
oa_rect <- function(t1,t2,rho,active=NULL) {
  a <- c(-Inf,t1,Inf); b <- c(-Inf,t2,Inf)
  index <- expand.grid(i=seq_len(length(a)-1L),j=seq_len(length(b)-1L))
  al <- a[index$i]; au <- a[index$i+1L]; bl <- b[index$j]; bu <- b[index$j+1L]
  p <- oa_bvn(au,bu,rho)-oa_bvn(al,bu,rho)-oa_bvn(au,bl,rho)+oa_bvn(al,bl,rho)
  d <- oa_bvn_density(au,bu,rho)-oa_bvn_density(al,bu,rho)-
    oa_bvn_density(au,bl,rho)+oa_bvn_density(al,bl,rho)
  if(is.null(active)) active <- rep(TRUE,length(p))
  if(!is.logical(active) || length(active)!=length(p) || anyNA(active)) oa_stop('RECTANGLE_ACTIVE')
  # Unobserved cells have exactly zero log-likelihood score contribution.
  # Never clip, renormalize, or replace a positive-count cell probability.
  # CDF subtraction can lose tiny unobserved rectangles; bounded cancellation
  # is tolerated there only, while occupied cells retain the original floor.
  if(any(!is.finite(p)) || any(!is.finite(d)) || any(p < -1e-12) ||
     any(p[active]<=1e-12) || abs(sum(p)-1)>1e-9) oa_stop('RECTANGLE_PROBABILITY')
  score <- numeric(length(p));score[active]<-d[active]/p[active]
  list(p=p,score=score)
}
oa_pair <- function(x1,x2,w,t1,t2) {
  k1 <- length(t1)+1L; k2 <- length(t2)+1L
  cell <- x1 + (x2-1L)*k1
  counts <- vapply(seq_len(k1*k2),function(k) sum(w[cell==k]),numeric(1))
  sw <- sum(w)
  score <- function(rho) sum(counts*oa_rect(t1,t2,rho,counts>0)$score)/sw
  # Require an interior score root; no boundary correlations are rescued.
  bounds <- NULL
  # Evaluate the same bounded interior grid individually. A numerically invalid
  # opposite-sign endpoint must not discard a valid bracket at strong rho.
  grid <- sort(c(0,c(.25,.5,.7,.8,.9,.95,.98),-c(.25,.5,.7,.8,.9,.95,.98)))
  vals <- vapply(grid,function(rho)tryCatch(score(rho),error=function(e)NA_real_),numeric(1))
  valid <- which(is.finite(vals))
  if(length(valid)>1L) for(a in seq_len(length(valid)-1L)) {
    left <- valid[a];right<-valid[a+1L]
    if(vals[left]>0 && vals[right]<0) { bounds<-grid[c(left,right)];break }
  }
  if(is.null(bounds)) oa_stop('CORRELATION_BOUNDARY')
  rho <- uniroot(score,bounds,tol=1e-12)$root
  if(abs(score(rho))>1e-9) oa_stop('CORRELATION_SCORE')
  list(rho=rho,cell=cell,counts=counts,sw=sw)
}
oa_moments <- function(prepared,with_if=TRUE) {
  z <- prepared$coded[prepared$mask,,drop=FALSE]; raww <- prepared$weight[prepared$mask]
  n <- nrow(z); w <- raww*n/sum(raww); sw <- sum(w)
  manifest <- prepared$manifest; labels <- oa_labels(manifest)
  th <- list(); th_if <- list(); at <- list(); start <- 0L
  for(j in seq_len(9L)) {
    cuts <- seq_len(length(manifest[[j]])-1L)
    indicators <- outer(z[,j],cuts,'<=')
    probs <- as.numeric(crossprod(w,indicators)/sw)
    th[[j]] <- qnorm(probs)
    if(any(!is.finite(th[[j]])) || any(diff(th[[j]])<=0)) oa_stop('THRESHOLD')
    th_if[[j]] <- sweep(sweep(indicators,2L,probs),2L,dnorm(th[[j]]),'/')*(w/sw)
    at[[j]] <- start+seq_along(cuts); start <- start+length(cuts)
  }
  thvec <- unlist(th,use.names=FALSE); p <- length(labels)
  local_if <- matrix(0,n,p); local_if[,seq_along(thvec)] <- do.call(cbind,th_if)
  cor <- diag(9L); dimnames(cor) <- list(names(manifest),names(manifest))
  pair_index <- which(lower.tri(cor),arr.ind=TRUE)
  jacobian_info <- numeric(36L)
  for(k in seq_len(36L)) {
    j <- pair_index[k,2]; i <- pair_index[k,1]
    pair <- oa_pair(z[,j],z[,i],w,th[[j]],th[[i]])
    rho <- pair$rho; cor[i,j] <- cor[j,i] <- rho
    if(with_if) {
      r <- oa_rect(th[[j]],th[[i]],rho,pair$counts>0)
      eq <- function(a,b,c) sum(pair$counts*oa_rect(a,b,c,pair$counts>0)$score)/pair$sw
      step <- 1e-5
      jr <- (eq(th[[j]],th[[i]],rho+step)-eq(th[[j]],th[[i]],rho-step))/(2*step)
      if(!is.finite(jr) || jr>=-1e-8) oa_stop('CORRELATION_JACOBIAN')
      gradient <- numeric(length(th[[j]])+length(th[[i]]))
      pos <- 0L
      for(item in c(j,i)) for(cut in seq_along(th[[item]])) {
        pos <- pos+1L; plus <- minus <- th
        plus[[item]][cut] <- plus[[item]][cut]+step
        minus[[item]][cut] <- minus[[item]][cut]-step
        gradient[pos] <- (eq(plus[[j]],plus[[i]],rho)-eq(minus[[j]],minus[[i]],rho))/(2*step)
      }
      scores <- r$score[pair$cell]
      centered <- scores-sum(w*scores)/sw
      local_if[,length(thvec)+k] <- -(w/sw*centered +
        as.numeric(local_if[,c(at[[j]],at[[i]]),drop=FALSE] %*% gradient))/jr
      jacobian_info[k] <- -jr
    }
  }
  moments <- setNames(c(thvec,cor[lower.tri(cor)]),labels)
  full_if <- matrix(0,length(prepared$mask),p,dimnames=list(NULL,labels))
  full_if[prepared$mask,] <- local_if
  list(moments=moments,thresholds=thvec,threshold_index=rep(seq_len(9L),lengths(th)),
       correlation=cor,contributions=full_if,n_complete=n,
       jacobian_min=min(jacobian_info),normalized_weights=w)
}
oa_build <- function(items,manifest,weight,psu,stratum,domain) {
  prepared <- oa_prepare(items,manifest,weight,psu,stratum,domain)
  m <- oa_quiet(oa_moments(prepared))
  cov <- oa_taylor(m$contributions,prepared$design)
  gamma <- m$n_complete*cov
  # Point-estimation metric fixed to the previous lavaan design-weight OPG path.
  native <- oa_quiet(getFromNamespace('muthen1984','lavaan')(
    data_1=prepared$coded[prepared$mask,,drop=FALSE],ov_names=names(manifest),
    ov_types=rep('ordered',9L),ov_levels=lengths(manifest),wt=m$normalized_weights,
    sampling_weights_type='design'))
  native_moments <- c(unlist(native$TH,use.names=FALSE),native$COR[lower.tri(native$COR)])
  if(max(abs(native_moments-m$moments))>1e-6) oa_stop('POINT_MOMENT_BINDING')
  iid_diag <- m$n_complete*diag(native$WLS.W)
  if(any(!is.finite(iid_diag)) || any(iid_diag<=0)) oa_stop('DWLS_DIAGONAL')
  labels <- names(m$moments); wls <- diag(1/iid_diag)
  dimnames(wls) <- list(labels,labels)
  if(any(!is.finite(gamma)) || max(abs(gamma-t(gamma)))>1e-9 ||
     qr(gamma,tol=1e-9)$rank!=length(labels) || min(eigen(gamma,symmetric=TRUE,only.values=TRUE)$values)<=1e-10)
    oa_stop('GAMMA_RANK')
  structure(list(private=list(prepared=prepared,m=m),moments=m$moments,
    correlation=m$correlation,thresholds=m$thresholds,threshold_index=m$threshold_index,
    gamma=gamma,wls_v=wls,covariance=cov,
    aggregate=list(n_design=nrow(items),n_complete=m$n_complete,n_excluded=sum(!prepared$mask),
      psus=length(prepared$design$psu_stratum),strata=length(prepared$design$psus_by_stratum),
      design_df=prepared$design$df,moments=length(labels),
      zero_psus=sum(vapply(seq_along(prepared$design$psu_stratum),function(p)
        !any(prepared$mask[prepared$design$psu==p]),logical(1))),
      native_point_max_difference=max(abs(native_moments-m$moments)))),class='oa_adapter')
}
print.oa_adapter <- function(x,...) {
  cat('Ordinal adapter: ',x$aggregate$n_complete,' complete cases; ',x$aggregate$moments,
      ' moments; ',x$aggregate$design_df,' design df.\n',sep=''); invisible(x)
}
oa_fit <- function(adapter,model,efa_factors=NULL,rotation_seed=2026100313L) {
  oa_runtime()
  if(!inherits(adapter,'oa_adapter')) oa_stop('ADAPTER_CLASS')
  if(!is.null(efa_factors)) {
    if(length(efa_factors)!=1L || !efa_factors %in% 1:3) oa_stop('EFA_FACTOR_COUNT')
    model <- paste0(paste(paste0('efa("minimal")*e',seq_len(efa_factors)),collapse=' + '),
      ' =~ ',paste(colnames(adapter$correlation),collapse=' + '))
  }
  if(!is.character(model) || length(model)!=1L || !nzchar(model)) oa_stop('MODEL')
  th <- adapter$thresholds
  names(th) <- names(adapter$moments)[seq_along(th)]
  attr(th,'th.idx') <- setNames(adapter$threshold_index,names(th))
  args <- list(model=model,sample_cov=adapter$correlation,sample_th=th,
    sample_mean=setNames(rep(0,9L),colnames(adapter$correlation)),
    sample_nobs=adapter$aggregate$n_complete,ordered=colnames(adapter$correlation),
    estimator='WLSMV',parameterization='theta',std_lv=TRUE,
    nacov=adapter$gamma,wls_v=adapter$wls_v)
  if(!is.null(efa_factors)) {
    set.seed(rotation_seed)
    args$rotation <- 'geomin'; args$rotation_args <- list(rstarts=30L,geomin_epsilon=.001)
  }
  fit <- oa_quiet(do.call(lavaan::cfa,args))
  if(!isTRUE(lavaan::lavInspect(fit,'converged')) || !isTRUE(lavaan::lavInspect(fit,'post.check')))
    oa_stop('MODEL_CONVERGENCE')
  if(lavaan::fitMeasures(fit,'df')<=0) oa_stop('MODEL_DF')
  v <- lavaan::lavInspect(fit,'vcov')
  if(any(!is.finite(v)) || any(diag(v)<=0)) oa_stop('PARAMETER_COVARIANCE')
  obs <- lavaan::lavInspect(fit,'wls.obs')
  if(!identical(names(obs),names(adapter$moments)) || max(abs(obs-adapter$moments))>1e-7)
    oa_stop('IMPORTED_MOMENTS')
  for(entry in list(list('gamma',adapter$gamma),list('wls.v',adapter$wls_v))) {
    actual <- lavaan::lavInspect(fit,entry[[1]])
    if(!identical(dimnames(actual),dimnames(entry[[2]])) || max(abs(actual-entry[[2]]))>1e-7)
      oa_stop('IMPORTED_MATRIX')
  }
  structure(list(private=fit,aggregate=list(df=unname(lavaan::fitMeasures(fit,'df')),
    converged=TRUE,postcheck=TRUE,efa_factors=efa_factors)),class='oa_fit')
}
print.oa_fit <- function(x,...) { cat('Ordinal external fit: df=',x$aggregate$df,'; checked import.\n',sep=''); invisible(x) }
oa_public <- function(adapter) {
  if(!inherits(adapter,'oa_adapter')) oa_stop('ADAPTER_CLASS')
  # Fixed whitelist. No mask, weights, contributions, category counts or IDs.
  adapter$aggregate
}
