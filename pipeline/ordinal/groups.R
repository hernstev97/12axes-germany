# Fixed identity joint ordinal groups, author candidate. No file reads/exports.
# Source adapter_v2.R and support.R first. Scientific selection/gates are external.
og_stop <- function(code) stop(paste0('ORDINAL_GROUPS_',code),call.=FALSE)
og_runtime <- function() {
  oa_runtime()
  if(!requireNamespace('semTools',quietly=TRUE) || as.character(packageVersion('semTools'))!='0.5.9')
    og_stop('SEMTOOLS_VERSION')
}
og_psd <- function(x,code,tolerance=1e-9) {
  if(!is.matrix(x)||nrow(x)!=ncol(x)||any(!is.finite(x))||max(abs(x-t(x)))>tolerance)
    og_stop(code)
  e <- eigen(os_sym(x),symmetric=TRUE)
  if(min(e$values)< -tolerance*max(1,max(abs(e$values)))) og_stop(code)
  e
}
og_block <- function(xs) {
  out <- matrix(0,sum(vapply(xs,nrow,integer(1))),sum(vapply(xs,ncol,integer(1))))
  i <- j <- 0L
  for(x in xs) { out[i+seq_len(nrow(x)),j+seq_len(ncol(x))] <- x;i<-i+nrow(x);j<-j+ncol(x) }
  out
}
og_build <- function(items,manifest,weight,psu,stratum,domain,group,levels) {
  og_runtime()
  if(!is.character(levels)||length(levels)<2L||anyNA(levels)||anyDuplicated(levels)||
     !is.atomic(group)||length(group)!=nrow(items)) og_stop('GROUP_CONTRACT')
  # Invalid/unassigned groups leave the national/full frame, not the PSU frame.
  group <- as.character(group)
  if(any(!is.na(group)&!group %in% levels)) og_stop('GROUP_OUTSIDE_MANIFEST')
  aa <- lapply(levels,function(g)oa_fixed_metric(oa_build(items,manifest,weight,psu,stratum,
    domain & !is.na(group) & group==g)))
  og_joint(aa)
}
og_joint <- function(adapters) {
  if(!is.list(adapters)||length(adapters)<2L||!all(vapply(adapters,inherits,logical(1),'oa_adapter')))
    og_stop('ADAPTER_LIST')
  a <- adapters[[1L]];prep <- a$private$prepared;labels<-names(a$moments)
  if(any(lengths(prep$manifest)<4L))og_stop('CATEGORY_FAMILY_UNSUPPORTED')
  for(b in adapters) {
    bp <- b$private$prepared
    if(!identical(bp$design,prep$design)||!identical(bp$weight,prep$weight)||
       !identical(bp$coded,prep$coded)||!identical(bp$manifest,prep$manifest)||
       !identical(names(b$moments),labels)) og_stop('ORIGINAL_FRAME_BINDING')
    if(max(abs(b$wls_v-diag(length(labels))))>1e-10) og_stop('FIXED_IDENTITY_REQUIRED')
  }
  masks <- do.call(cbind,lapply(adapters,function(b)b$private$prepared$mask))
  if(any(rowSums(masks)>1L)) og_stop('OVERLAPPING_GROUP_DOMAINS')
  u <- do.call(cbind,lapply(adapters,function(b)b$private$m$contributions))
  joint_labels <- unlist(lapply(seq_along(adapters),function(g)paste0('g',g,'::',labels)),use.names=FALSE)
  colnames(u)<-joint_labels;v<-oa_taylor(u,prep$design);og_psd(v,'JOINT_MOMENT_COVARIANCE')
  s <- setNames(unlist(lapply(adapters,function(b)unname(b$moments)),use.names=FALSE),joint_labels)
  for(g in seq_along(adapters)) {
    ii <- (g-1L)*length(labels)+seq_along(labels)
    if(max(abs(v[ii,ii]-adapters[[g]]$covariance))>1e-9) og_stop('JOINT_BLOCK_BINDING')
  }
  structure(list(private=list(adapters=adapters,contributions=u,design=prep$design),moments=s,
    covariance=v,manifest=prep$manifest,ng=vapply(adapters,function(b)b$aggregate$n_complete,integer(1)),
    aggregate=list(groups=length(adapters),moments=length(s),design_df=prep$design$df,
      original_psus=length(prep$design$psu_stratum),strata=length(prep$design$psus_by_stratum),
      zero_domain_psus=sum(vapply(seq_along(prep$design$psu_stratum),function(p)
        !any(rowSums(masks)[prep$design$psu==p]>0),logical(1))),
      point_metric='fixed identity on full group threshold/polychoric moment stack',
      within_group_constraint='adapter requires SPD moment covariance and >=87 design df')),class='og_joint')
}
og_model <- function(joint,key) {
  if(!key %in% c('M3','M2')) og_stop('MODEL_UNSUPPORTED')
  items<-names(joint$manifest)
  sets<-if(key=='M3')list(H=items[1:3],I=items[4:6],E=items[7:9]) else list(H=items[1:3],migration=items[4:9])
  list(key=key,sets=sets,syntax=paste(vapply(names(sets),function(f)
    paste0(f,' =~ ',paste(sets[[f]],collapse=' + ')),character(1)),collapse='\n'))
}
og_arguments <- function(joint,model) {
  aa<-joint$private$adapters;items<-names(joint$manifest);total<-sum(joint$ng)
  th<-lapply(aa,function(a) {
    x<-a$thresholds;names(x)<-names(a$moments)[seq_along(x)]
    attr(x,'th.idx')<-setNames(a$threshold_index,names(x));x
  })
  attr(th,'th.idx')<-lapply(th,function(x)attr(x,'th.idx'))
  # Pinned categorical DWLS applies (n_g-1)/N in objective and gradient.
  # Scaling each import by N/(n_g-1) yields exactly Wjoint=I.
  list(model=model,sample_cov=lapply(aa,function(a)a$correlation),sample_th=th,
    sample_mean=lapply(aa,function(a)setNames(rep(0,9),items)),sample_nobs=as.list(joint$ng),
    ordered=items,estimator='DWLS',parameterization='theta',std_lv=TRUE,
    nacov=lapply(aa,function(a)a$gamma),wls_v=lapply(seq_along(aa),function(g)
      aa[[g]]$wls_v*total/(joint$ng[g]-1L)),se='none',test='none',
    ceq_simple=FALSE,control=list(iter.max=20000L))
}
og_tangent <- function(pt,p) {
  equal<-pt[pt$op=='==',,drop=FALSE];h<-matrix(0,nrow(equal),p)
  for(i in seq_len(nrow(equal))) {
    find<-function(label) {
      ii<-which(pt$plabel==label | nzchar(pt$label)&pt$label==label)
      if(length(ii)!=1L||pt$free[ii]<=0L) og_stop('NONLINEAR_OR_FIXED_CONSTRAINT_UNSUPPORTED')
      pt$free[ii]
    }
    h[i,find(equal$lhs[i])]<-1;h[i,find(equal$rhs[i])]<- -1
  }
  if(nrow(h)) {
    q<-qr(t(h),tol=1e-9);r<-q$rank
    if(r>=p) og_stop('EMPTY_TANGENT')
    z<-qr.Q(q,complete=TRUE)[,seq.int(r+1L,p),drop=FALSE]
  } else {r<-0L;z<-diag(p)}
  list(h=h,z=z,constraint_rank=r)
}
og_context <- function(fit,joint) {
  f<-fit;m<-f@Model;pt<-lavaan::parTable(f)
  if(m@multilevel||m@conditional.x||m@representation!='LISREL'||m@parameterization!='theta'||
     any(pt$op %in% c('<','>','~',':='))||any(pt$op=='~*~'&pt$free>0L)) og_stop('MODEL_CONTRACT')
  x<-os_fun('lav_model_get_parameters')(m)
  cc<-os_fun('lav_inspect_coef')(f,type='free',add_labels=TRUE)
  if(length(x)!=m@nx.free||length(cc)!=length(x)||max(abs(x-cc))>1e-9) og_stop('FREE_ORDER')
  dl<-lavaan::lavInspect(f,'delta')
  if(!is.list(dl)||length(dl)!=length(joint$ng)) og_stop('DELTA_GROUPS')
  obs<-lavaan::lavInspect(f,'wls.obs');w<-lavaan::lavInspect(f,'wls.v')
  for(g in seq_along(dl)) {
    a<-joint$private$adapters[[g]]
    if(!identical(names(obs[[g]]),names(a$moments))||max(abs(obs[[g]]-a$moments))>1e-7||
       !identical(rownames(dl[[g]]),names(a$moments))||ncol(dl[[g]])!=length(x)||
       !identical(colnames(dl[[g]]),names(cc))||
       max(abs(w[[g]]-a$wls_v*sum(joint$ng)/(joint$ng[g]-1L)))>1e-7)
      og_stop('IMPORT_ORDER_OR_METRIC')
  }
  tangent<-og_tangent(pt,length(x))
  if(nrow(tangent$h)&&max(abs(tangent$h%*%x))>1e-7) og_stop('INITIAL_CONSTRAINT')
  names(x)<-paste0('p',seq_along(x),'::',names(cc))
  list(fit=f,model=m,x=x,native_parameter_labels=names(cc),parameter_labels=names(x),pt=pt,
    moment_labels=names(joint$moments),items=names(joint$manifest),
    factors=og_model(joint,'M3')$sets,tangent=tangent,joint=joint)
}
og_at <- function(context,x) {
  if(length(x)!=length(context$x)||any(!is.finite(x))) og_stop('PARAMETER_VECTOR')
  m<-os_fun('lav_model_set_parameters')(context$model,unname(x))
  gl<-lapply(seq_len(m@nblocks),function(g)m@GLIST[cumsum(c(0L,m@nmat))[g]+seq_len(m@nmat[g])])
  for(g in gl) {
    if(!all(c('lambda','theta','psi','tau')%in%names(g))||
       any(g$theta[lower.tri(g$theta)]!=0)||any(diag(g$theta)<=0)||
       !is.null(g$beta)&&any(g$beta!=0)) og_stop('LOCAL_INDEPENDENCE_OR_VARIANCE')
    os_check_spd(g$psi,'GROUP_LATENT_COVARIANCE')
    os_check_spd(g$lambda%*%g$psi%*%t(g$lambda)+g$theta,'GROUP_RESPONSE_COVARIANCE')
  }
  moments<-unlist(os_fun('lav_model_wls_est')(m),use.names=FALSE)
  if(length(moments)!=length(context$moment_labels)||any(!is.finite(moments))) og_stop('IMPLIED_ORDER')
  names(moments)<-context$moment_labels
  d<-do.call(rbind,os_fun('lav_model_delta')(m))
  if(nrow(d)!=length(moments)||ncol(d)!=length(x)||any(!is.finite(d))) og_stop('DELTA_ORDER')
  dimnames(d)<-list(context$moment_labels,context$parameter_labels)
  list(model=m,glist=gl,moments=moments,delta=d)
}
og_score <- function(context,x,moments=context$joint$moments) {
  a<-og_at(context,x)
  setNames(as.numeric(crossprod(a$delta,moments-a$moments)),context$parameter_labels)
}
og_refit <- function(context,moments=context$joint$moments,start=context$x) {
  z<-context$tangent$z;base<-start
  if(length(start)!=length(context$x)||!identical(names(start),context$parameter_labels)||any(!is.finite(start))||
     nrow(context$tangent$h)&&max(abs(context$tangent$h%*%start))>1e-7)
    og_stop('REFIT_START_CONSTRAINT')
  if(length(moments)!=length(context$moment_labels)||!identical(names(moments),context$moment_labels))
    og_stop('REFIT_MOMENT_ORDER')
  fun<-function(t) {
    value<-tryCatch(og_at(context,base+as.numeric(z%*%t)),error=function(e)NULL)
    if(is.null(value)) return(1e30)
    sum((moments-value$moments)^2)/2
  }
  gradient<-function(t) as.numeric(-crossprod(z,og_score(context,base+as.numeric(z%*%t),moments)))
  fit<-stats::optim(rep(0,ncol(z)),fun,gradient,method='BFGS',
    control=list(reltol=1e-13,maxit=20000L))
  tangent <- fit$par
  # BFGS's objective stopping can leave too much score error for a derivative
  # oracle. Polish the same objective with its observed local Newton equation.
  for(iteration in seq_len(8L)) {
    scorefun <- function(t)setNames(as.numeric(crossprod(z,
      og_score(context,base+as.numeric(z%*%t),moments))),paste0('t',seq_len(ncol(z))))
    scorevec <- scorefun(tangent)
    if(max(abs(scorevec))<=5e-11) break
    names(tangent)<-names(scorevec)
    bread <- -os_numeric_jacobian(scorefun,tangent,1e-5)
    os_check_spd(bread,'GROUP_REFIT_POLISH_BREAD')
    shift <- as.numeric(solve(bread,scorevec));before<-fun(tangent);accepted<-FALSE
    for(fraction in 2^-(0:12)) {
      trial<-tangent+fraction*shift;after<-fun(trial)
      if(after<=before+1e-16) {tangent<-trial;accepted<-TRUE;break}
    }
    if(!accepted) og_stop('REFIT_POLISH_LINE_SEARCH')
  }
  x<-base+as.numeric(z%*%tangent);names(x)<-context$parameter_labels
  a<-og_at(context,x);score<-max(abs(crossprod(z,og_score(context,x,moments))))
  if(fit$convergence!=0L||score>2e-9) og_stop('CANONICAL_OPTIMIZATION')
  list(x=x,objective=fun(tangent),score_max=score,iterations=unname(fit$counts),at=a)
}
og_fit <- function(joint,model_key='M3',stage='strict') {
  og_runtime()
  stages<-list(configural=character(),thresholds='thresholds',loadings=c('thresholds','loadings'),
    intercepts=c('thresholds','loadings','intercepts'),strict=c('thresholds','loadings','intercepts','residuals'))
  if(!inherits(joint,'og_joint')||!stage%in%names(stages)) og_stop('FIT_CONTRACT')
  model<-og_model(joint,model_key)
  initial<-oa_quiet(do.call(lavaan::cfa,og_arguments(joint,model$syntax)))
  syntax<-oa_quiet(semTools::measEq.syntax(configural.model=initial,
    parameterization='theta',meanstructure=TRUE,ID.fac='std.lv',ID.cat='Wu.Estabrook.2016',group.equal=stages[[stage]]))
  args<-og_arguments(joint,as.character(syntax));args$std_lv<-FALSE;args$auto_fix_first<-FALSE
  native<-oa_quiet(do.call(lavaan::cfa,args))
  context<-og_context(native,joint);canonical<-og_refit(context)
  context$x<-canonical$x;context$model<-canonical$at$model
  z<-context$tangent$z;d<-canonical$at$delta;a<-d%*%z
  if(qr(a,tol=1e-9)$rank!=ncol(z)) og_stop('UNIDENTIFIED_TANGENT')
  structure(list(private=list(context=context,joint=joint,canonical=canonical),syntax=as.character(syntax),
    aggregate=list(stage=stage,model=model_key,tangent_dimension=ncol(z),constraints=context$tangent$constraint_rank,
      moments=length(joint$moments),moment_df=length(joint$moments)-ncol(z),
      canonical_score_max=canonical$score_max,point_metric='fixed full joint identity; exact tangent optimization',
      initial_native_converged=isTRUE(lavaan::lavInspect(native,'converged')))),class='og_fit')
}
og_sandwich <- function(fit,step=1e-5) {
  if(!inherits(fit,'og_fit')) og_stop('FIT_CLASS')
  context<-fit$private$context;joint<-fit$private$joint;x<-context$x;z<-context$tangent$z
  at<-og_at(context,x);d<-at$delta;a<-d%*%z
  # Differentiate the full tangent score at the fitted point, including residual curvature.
  tangent_score<-function(t)setNames(as.numeric(crossprod(z,og_score(context,x+as.numeric(z%*%t)))),
    paste0('t',seq_len(ncol(z))))
  zeros<-setNames(rep(0,ncol(z)),paste0('t',seq_len(ncol(z))))
  j<-os_numeric_jacobian(tangent_score,zeros,step);bread<- -j
  os_check_spd(bread,'GROUP_OBSERVED_BREAD')
  expected<-crossprod(a);os_check_spd(expected,'GROUP_EXPECTED_BREAD')
  kt<-solve(bread,t(a));k<-z%*%kt;dimnames(k)<-list(context$parameter_labels,context$moment_labels)
  vb<-os_sym(k%*%joint$covariance%*%t(k));og_psd(vb,'PARAMETER_COVARIANCE')
  residual_transform<-diag(length(joint$moments))-d%*%k
  # Null-correct tangent projection for asymptotic global quadratic fit.
  null_projection<-diag(length(joint$moments))-a%*%solve(expected,t(a))
  structure(list(private=list(context=context,joint=joint,delta=d,z=z,k=k,bread=bread,
    expected_bread=expected,parameter_covariance=vb,residual_transform=residual_transform,
    null_projection=null_projection),aggregate=c(fit$aggregate,list(design_df=joint$aggregate$design_df,
      observed_expected_bread_max_difference=max(abs(bread-expected)),jacobian_step=step,
      covariance_method='Kstack full original-frame joint moment covariance Kstack transpose'))),class='og_sandwich')
}
# Pure eigen quadratic-tail oracle, no global RNG state left changed.
og_spectral_mc <- function(eigenvalues,q,draws=200000L,seed=2026100342L,batch=2000L,level=.95) {
  if(any(!is.finite(eigenvalues))||any(eigenvalues<0)||!is.finite(q)||q<0||
     draws<1L||draws>200000L||batch<1L||level<=0||level>=1) og_stop('SPECTRAL_CONTRACT')
  old_kind<-RNGkind()
  old<-if(exists('.Random.seed',.GlobalEnv,inherits=FALSE))get('.Random.seed',.GlobalEnv) else NULL
  on.exit({
    do.call(RNGkind,as.list(old_kind))
    if(is.null(old)) {if(exists('.Random.seed',.GlobalEnv,inherits=FALSE))rm('.Random.seed',envir=.GlobalEnv)} else
      assign('.Random.seed',old,envir=.GlobalEnv)
  })
  RNGkind('Mersenne-Twister','Inversion','Rejection');set.seed(seed);hit<-0L;done<-0L;ev<-eigenvalues[eigenvalues>0]
  while(done<draws) {
    n<-min(batch,draws-done)
    values<-if(length(ev))as.numeric(matrix(rnorm(n*length(ev)),n,length(ev))^2%*%ev) else rep(0,n)
    hit<-hit+sum(values>=q);done<-done+n
  }
  alpha<-1-level
  interval<-c(if(hit==0L)0 else qbeta(alpha/2,hit,draws-hit+1),
    if(hit==draws)1 else qbeta(1-alpha/2,hit+1,draws-hit))
  list(p_mc=hit/draws,mc_interval=interval,hits=hit,draws=draws,seed=seed,batch=batch,
    method='fixed-seed Monte Carlo tail of asymptotic weighted chi-square quadratic; exact binomial MC interval',
    limitation='binomial interval measures Monte Carlo error only; not finite-sample model calibration')
}
og_global_fit <- function(sandwich,draws=200000L,seed=2026100342L) {
  p<-sandwich$private;r<-p$joint$moments-og_at(p$context,p$context$x)$moments
  q<-sum(r^2);ve<-og_psd(p$joint$covariance,'JOINT_MOMENT_COVARIANCE')
  root<-ve$vectors%*%diag(sqrt(pmax(0,ve$values)))%*%t(ve$vectors)
  u<-crossprod(p$null_projection);spectrum<-og_psd(os_sym(root%*%u%*%root),'GLOBAL_SPECTRUM')$values
  spectrum[spectrum<0]<-0
  c(list(quadratic=q,eigenvalues=spectrum,rank=sum(spectrum>1e-10),
    interpretation='asymptotic global fit under this stage model null, fixed I and full shared-PSU covariance'),
    og_spectral_mc(spectrum,q,draws,seed))
}
# Only estimable linear restrictions in the existing identified parameterization.
# Pure ID restrictions H beta=0 and zero/singular contrast covariance are rejected.
og_wald <- function(sandwich,C,target=rep(0,nrow(C))) {
  p<-sandwich$private
  if(!is.matrix(C)||nrow(C)<1L||ncol(C)!=length(p$context$x)||any(!is.finite(C))||
     length(target)!=nrow(C)||any(!is.finite(target))) og_stop('WALD_CONTRACT')
  if(sum(svd(C%*%p$z,nu=0,nv=0)$d>1e-9)!=nrow(C)) og_stop('WALD_NOT_TESTABLE')
  v<-os_sym(C%*%p$parameter_covariance%*%t(C));os_check_spd(v,'WALD_NOT_ESTIMABLE')
  diff<-as.numeric(C%*%p$context$x-target);q<-as.numeric(crossprod(diff,solve(v,diff)))
  list(quadratic=q,df=nrow(C),p_asymptotic=pchisq(q,nrow(C),lower.tail=FALSE),
    method='joint design Wald for explicitly supplied estimable linear contrasts; no native lavaan test')
}
og_curve <- function(configural_context,strict_context,manifest,model_key='M3',grid=c(-2,-1,0,1,2),
    xc=configural_context$x,xs=strict_context$x,scores=NULL) {
  if(!identical(grid,c(-2,-1,0,1,2))) og_stop('GRID_NOT_PREDEFINED')
  score_spec<-os_score_spec(manifest,names(manifest),scores)
  cp<-configural_context$pt;sp<-strict_context$pt
  fill<-function(pt,x) {v<-pt$est;ii<-pt$free>0;v[ii]<-x[pt$free[ii]];v}
  cv<-fill(cp,xc);sv<-fill(sp,xs);gcount<-length(configural_context$joint$ng)
  sets<-og_model(configural_context$joint,model_key)$sets
  namesc<-paste0('C::',configural_context$parameter_labels);namess<-paste0('S::',strict_context$parameter_labels)
  curves<-numeric();jac<-matrix(0,0,length(xc)+length(xs));all_labels<-c(namesc,namess)
  take<-function(pt,group,op,lhs=NULL,rhs=NULL) {
    ii<-which(pt$group==group&pt$op==op)
    if(!is.null(lhs))ii<-ii[pt$lhs[ii]==lhs];if(!is.null(rhs))ii<-ii[pt$rhs[ii]==rhs];ii
  }
  for(g in seq_len(gcount))for(f in names(sets))for(x in grid) {
    row<-numeric(length(all_labels));value<-0
    muidx<-take(sp,g,'~1',f);varidx<-take(sp,g,'~~',f,f)
    if(length(muidx)!=1L||length(varidx)!=1L||sv[varidx]<=0) og_stop('LINK_PARAMETER_ORDER')
    mu<-sv[muidx];psi<-sv[varidx];z<-(x-mu)/sqrt(psi)
    add<-function(index,derivative,pt,offset) for(i in seq_along(index)) {
      free<-pt$free[index[i]];if(free>0) row[offset+free]<<-row[offset+free]+derivative[i]
    }
    dz_total<-0
    for(item in sets[[f]]) {
      li<-take(cp,g,'=~',f,item);ni<-take(cp,g,'~1',item);vi<-take(cp,g,'~~',item,item);ti<-take(cp,g,'|',item)
      if(length(li)!=1L||length(ni)!=1L||length(vi)!=1L||length(ti)!=length(manifest[[item]])-1L||cv[vi]<=0)
        og_stop('CURVE_PARAMETER_ORDER')
      sd<-sqrt(cv[vi]);u<-(cv[ni]+cv[li]*z-cv[ti])/sd;density<-dnorm(u)
      divisor<-length(sets[[f]]);increments<-diff(score_spec$scores[[item]])
      weighted_density<-density*increments
      value<-value+(score_spec$scores[[item]][1L]+sum(increments*pnorm(u)))/divisor
      dz<-sum(weighted_density)*cv[li]/(divisor*sd);dz_total<-dz_total+dz
      add(li,sum(weighted_density)*z/(divisor*sd),cp,0L);add(ni,sum(weighted_density)/(divisor*sd),cp,0L)
      add(ti,-weighted_density/(divisor*sd),cp,0L);add(vi,-sum(weighted_density*u)/(2*cv[vi]*divisor),cp,0L)
    }
    add(muidx,-dz_total/sqrt(psi),sp,length(xc));add(varidx,-dz_total*z/(2*psi),sp,length(xc))
    label<-paste0('g',g,'::',f,'::',x);curves[label]<-value;jac<-rbind(jac,row)
  }
  dimnames(jac)<-list(names(curves),all_labels)
  list(values=curves,gradient=jac)
}
og_equivalence <- function(configural,strict,model_key='M3',margin=.05,alpha=.05,scores=NULL) {
  if(configural$aggregate$stage!='configural'||strict$aggregate$stage!='strict'||
     configural$aggregate$model!=model_key||strict$aggregate$model!=model_key||
     !identical(configural$private$joint$moments,strict$private$joint$moments)||
     !identical(configural$private$joint$covariance,strict$private$joint$covariance)||margin!=.05||alpha!=.05)
    og_stop('TWO_FIT_BINDING')
  pc<-configural$private;ps<-strict$private;joint<-pc$joint
  curve<-og_curve(pc$context,ps$context,joint$manifest,model_key,scores=scores)
  sets<-og_model(joint,model_key)$sets;grid<-c(-2,-1,0,1,2);pairs<-combn(seq_along(joint$ng),2L)
  l<-ncol(pairs)*length(sets)*length(grid);c<-matrix(0,l,length(curve$values));labels<-character(l);i<-0L
  for(pair in seq_len(ncol(pairs)))for(f in names(sets))for(x in grid) {
    i<-i+1L;g1<-pairs[1L,pair];g2<-pairs[2L,pair]
    c[i,match(paste0('g',g2,'::',f,'::',x),names(curve$values))]<-1
    c[i,match(paste0('g',g1,'::',f,'::',x),names(curve$values))]<- -1
    labels[i]<-paste0('g',g2,'-g',g1,'::',f,'::',x)
  }
  kstack<-rbind(pc$k,ps$k);vstack<-os_sym(kstack%*%joint$covariance%*%t(kstack))
  j<-c%*%curve$gradient;dif<-as.numeric(c%*%curve$values);names(dif)<-labels
  v<-os_sym(j%*%vstack%*%t(j));og_psd(v,'CURVE_CONTRAST_COVARIANCE')
  if(any(diag(v)<=0)) og_stop('CURVE_CONTRAST_NOT_ESTIMABLE')
  se<-sqrt(diag(v));critical<-qt(1-alpha/(2*l),joint$aggregate$design_df)
  upper<-abs(dif)+critical*se
  list(contrasts=dif,design_se=se,gradient=j,covariance=v,stacked_covariance=vstack,kstack=kstack,
    curves=curve$values,family_size=l,grid=grid,margin=margin,alpha=alpha,critical=critical,
    upper_bounds=upper,simultaneous_upper_bound=max(upper),within_own_budget=max(upper)<margin,
    interpretation='free configural curves linked using strict group means/variances; conditional grid equivalence only',
    limits=c('own .05 product margin; first-order Delta and design-t Bonferroni family need calibration',
      'strict all-item link assumption; common affine DIF is observationally unidentified',
      'no answer-selected anchors or partial-invariance rescue; no exact finite-sample claim'))
}
print.og_joint <- function(x,...) {cat('Joint ordinal adapter: ',x$aggregate$groups,' groups; ',x$aggregate$moments,' moments.\n',sep='');invisible(x)}
print.og_fit <- function(x,...) {cat('Joint ordinal fit: ',x$aggregate$model,' ',x$aggregate$stage,'; ',x$aggregate$tangent_dimension,' tangent parameters.\n',sep='');invisible(x)}
print.og_sandwich <- function(x,...) {cat('Joint ordinal sandwich: ',x$aggregate$stage,'; full original-frame covariance.\n',sep='');invisible(x)}
# Transform the immediately restrictive Wu representation into the preceding
# freer one at the restrictive null point. All selected models have simple
# loadings, local independence and >=4 categories per item.
og_map_null <- function(restricted,free) {
  rp<-restricted$private;fp<-free$private;rctx<-rp$context;fctx<-fp$context
  order<-c('configural','thresholds','loadings','intercepts','strict')
  ri<-match(restricted$aggregate$stage,order);fi<-match(free$aggregate$stage,order)
  if(is.na(ri)||is.na(fi)||ri!=fi+1L||restricted$aggregate$model!=free$aggregate$model||
     !identical(rp$joint$moments,fp$joint$moments)||
     !identical(rp$joint$covariance,fp$joint$covariance)) og_stop('NESTED_STAGE_BINDING')
  rt<-rctx$pt;ft<-fctx$pt;rv<-rt$est;ii<-rt$free>0;rv[ii]<-rctx$x[rt$free[ii]]
  original<-function(g,op,lhs,rhs) {
    at<-which(rt$group==g&rt$op==op&rt$lhs==lhs&rt$rhs==rhs)
    if(length(at)!=1L) og_stop('NULL_MAPPING_PARAMETER_ORDER')
    rv[at]
  }
  factor_for<-function(item) {
    at<-which(rt$op=='=~'&rt$rhs==item&rt$group==1L)
    if(length(at)!=1L) og_stop('NULL_MAPPING_CROSSLOADING_UNSUPPORTED')
    rt$lhs[at]
  }
  items<-names(fp$joint$manifest);factors<-names(og_model(fp$joint,free$aggregate$model)$sets)
  # Each free column has one table position. Fixed rows are verified too.
  fv<-ft$est
  for(i in which(ft$group>0L & ft$op %in% c('=~','|','~1','~~','~*~'))) {
    g<-ft$group[i];op<-ft$op[i];lhs<-ft$lhs[i];rhs<-ft$rhs[i]
    value<-original(g,op,lhs,rhs)
    if(fi==1L) {
      if(op=='=~')value<-value*sqrt(original(g,'~~',lhs,lhs))/sqrt(original(g,'~~',rhs,rhs))
      if(op=='|') {
        f<-factor_for(lhs);lambda<-original(g,'=~',f,lhs)
        value<-(value-original(g,'~1',lhs,'')-lambda*original(g,'~1',f,''))/
          sqrt(original(g,'~~',lhs,lhs))
      }
      if(op=='~1')value<-0
      if(op=='~~'&&lhs==rhs)value<-1
      if(op=='~~'&&lhs!=rhs&&lhs%in%factors&&rhs%in%factors)
        value<-value/sqrt(original(g,'~~',lhs,lhs)*original(g,'~~',rhs,rhs))
    } else if(fi==2L) {
      if(op=='=~')value<-value*sqrt(original(g,'~~',lhs,lhs))
      if(op=='~1'&&lhs%in%factors)value<-0
      if(op=='~1'&&lhs%in%items) {
        f<-factor_for(lhs);value<-value+original(g,'=~',f,lhs)*original(g,'~1',f,'')
      }
      if(op=='~~'&&lhs%in%factors&&rhs%in%factors)
        value<-value/sqrt(original(g,'~~',lhs,lhs)*original(g,'~~',rhs,rhs))
    } else if(fi==3L) {
      if(op=='~1'&&lhs%in%factors)value<-0
      if(op=='~1'&&lhs%in%items) {
        f<-factor_for(lhs);value<-value+original(g,'=~',f,lhs)*original(g,'~1',f,'')
      }
    }
    # Delta is a derived THETA response scaling, not an independent parameter.
    if(op=='~*~')next
    if(ft$free[i]==0L&&abs(fv[i]-value)>1e-7)og_stop('NULL_MAPPING_FIXED_PARAMETER')
    fv[i]<-value
  }
  x<-fctx$x
  for(i in which(ft$free>0L))x[ft$free[i]]<-fv[i]
  if(nrow(fctx$tangent$h)&&max(abs(fctx$tangent$h%*%x))>1e-7)og_stop('NULL_MAPPING_EQUALITY')
  ra<-og_at(rctx,rctx$x);fa<-og_at(fctx,x)
  error<-max(abs(ra$moments-fa$moments))
  if(error>1e-7)og_stop('NULL_MAPPING_MOMENT_MISMATCH')
  list(x=x,restricted=ra,free=fa,moment_error=error)
}
og_nested <- function(restricted,free,draws=200000L,seed=2026100347L) {
  mapped<-og_map_null(restricted,free);rp<-restricted$private;fp<-free$private
  ar<-mapped$restricted$delta%*%rp$z;af<-mapped$free$delta%*%fp$z
  br<-crossprod(ar);bf<-crossprod(af)
  os_check_spd(br,'NESTED_RESTRICTIVE_BREAD');os_check_spd(bf,'NESTED_FREE_BREAD')
  pr<-diag(nrow(ar))-ar%*%solve(br,t(ar));pf<-diag(nrow(af))-af%*%solve(bf,t(af))
  nesting_error<-max(abs(pf%*%ar))
  if(nesting_error>1e-7)og_stop('NULL_TANGENTS_NOT_NESTED')
  u<-os_sym(crossprod(pr)-crossprod(pf));og_psd(u,'NESTED_DIFFERENCE_NOT_PSD')
  qr<-sum((rp$joint$moments-mapped$restricted$moments)^2)
  qf<-sum((fp$joint$moments-og_at(fp$context,fp$context$x)$moments)^2)
  q<-qr-qf
  if(q< -1e-9)og_stop('NESTED_OBJECTIVE_ORDER')
  q<-max(0,q)
  ve<-og_psd(rp$joint$covariance,'JOINT_MOMENT_COVARIANCE')
  root<-ve$vectors%*%diag(sqrt(pmax(0,ve$values)))%*%t(ve$vectors)
  ev<-og_psd(os_sym(root%*%u%*%root),'NESTED_SPECTRUM')$values;ev[ev<0]<-0
  c(list(quadratic_difference=q,eigenvalues=ev,rank=sum(ev>1e-10),
    null_moment_mapping_error=mapped$moment_error,null_tangent_nesting_error=nesting_error,
    restrictive_stage=restricted$aggregate$stage,free_stage=free$aggregate$stage,
    method='successive joint fixed-I objective difference; both tangent projectors evaluated at one restrictive null point'),
    og_spectral_mc(ev,q,draws,seed))
}
og_mc_decision <- function(test,threshold) {
  ci<-test$mc_interval
  if(length(ci)!=2L||threshold<=0||threshold>=1)og_stop('MC_DECISION_CONTRACT')
  if(ci[2]<threshold)'REJECT' else if(ci[1]>threshold)'NOT_REJECTED' else 'OPEN_MC_INTERVAL_CROSSES_THRESHOLD'
}
# Five global and four substantive successive restrictions form a declared
# nine-test family per grouping variable. No implicit group dropping or rescue.
og_sequence <- function(joint,model_key='M3',alpha=.05,seed_base=2026100341L,draws=200000L,scores=NULL) {
  if(alpha!=.05||seed_base!=2026100341L||draws!=200000L)og_stop('SEQUENCE_BUDGET_CONTRACT')
  stages<-c('configural','thresholds','loadings','intercepts','strict');fits<-sws<-list();tests<-list()
  for(i in seq_along(stages)) {
    s<-stages[i];fits[[s]]<-og_fit(joint,model_key,s);sws[[s]]<-og_sandwich(fits[[s]])
    t<-og_global_fit(sws[[s]],draws,seed_base+i);t$stage_index<-i;t$family_test_index<-i
    tests[[paste0('global_',s)]]<-t
  }
  for(i in 2:5) {
    t<-og_nested(sws[[stages[i]]],sws[[stages[i-1L]]],draws,seed_base+i+4L)
    t$stage_index<-i;t$family_test_index<-i+4L;tests[[paste0('restriction_',stages[i])]]<-t
  }
  threshold<-alpha/length(tests)
  decisions<-vapply(tests,og_mc_decision,character(1),threshold=threshold)
  eq<-og_equivalence(sws$configural,sws$strict,model_key,scores=scores)
  list(private=list(fits=fits,sandwiches=sws),tests=tests,decisions=decisions,
    family_size=length(tests),alpha=alpha,bonferroni_threshold=threshold,seed_base=seed_base,
    equivalence=eq,software_conditionally_clear=all(decisions=='NOT_REJECTED')&&eq$within_own_budget,
    limitation='software calculation and asymptotic criteria only; not empirical, finite-ESS calibration or scientific approval')
}
