# Aggregate norms and fixed supplemental variants; no file reads in en_analyse.
en_stop<-function(code,diagnostics=NULL)stop(structure(list(message=paste0('ESS_NORMS_',code),
  call=NULL,diagnostics=diagnostics),class=c('en_error','error','condition')))
en_code<-function(e) {
  code<-conditionMessage(e)
  if(grepl('^(ESS_NORMS|ESS_CONFIRMATORY|ESS_DEVELOPMENT|ORDINAL_ADAPTER|ORDINAL_SUPPORT)_[A-Z0-9_]+$',code))code else 'ESS_NORMS_LIBRARY_ERROR'
}
en_quiet<-function(expr) {
  warned<-FALSE
  discarded<-capture.output(value<-tryCatch(withCallingHandlers(expr,
    warning=function(w){warned<<-TRUE;invokeRestart('muffleWarning')},message=function(m)invokeRestart('muffleMessage')),
    error=function(e)stop(e)))
  if(warned)en_stop('LIBRARY_WARNING')
  value
}
en_dependencies<-function()list(
  'pipeline/ordinal/develop.R'='d1b725b05ba43d9a3edbe4964e05ae0d5365ef951944fe1c83284967ff800e74',
  'pipeline/ordinal/develop-config.R'='44a74f0e59645d047f2bdc4508cc0058d0dd80ffb4a67a8963ee9e84f0f429b0',
  'pipeline/ordinal/adapter_v2.R'='8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b',
  'pipeline/ordinal/support.R'='b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22',
  'pipeline/ordinal/confirm.R'='e7c8d04d8010c456c5db6d9902353a37786737b201cf9a160d082f40a84bddad')
en_initialize<-function(project_root) {
  project<-normalizePath(project_root,mustWork=TRUE);namespace<-environment(en_initialize)
  for(path in names(en_dependencies())) {
    value<-en_quiet(system2('/usr/bin/sha256sum',shQuote(file.path(project,path)),stdout=TRUE,stderr=FALSE))
    if(length(value)!=1L||!is.null(attr(value,'status'))||substr(value,1L,64L)!=en_dependencies()[[path]])en_stop('DEPENDENCY_PIN')
  }
  source(file.path(project,'pipeline/ordinal/confirm.R'),local=namespace)
  initialized<-ec_initialize(project)
  initialized$pins<-c(initialized$pins,list('pipeline/ordinal/norms.R'=ec_sha256(file.path(project,'pipeline/ordinal/norms.R'))))
  initialized
}
en_full_contract<-function(full) {
  cfg<-ed_default_config()
  if(!is.list(full)||!identical(full$schema,'life93-fixed-model-confirmation-aggregate-1')||
      !identical(full$arm,'FULL')||!identical(full$model$status,'EXECUTED')||!isTRUE(full$model$eligible)||
      !isTRUE(full$confirmation$global_model_passed)||
      !identical(full$confirmation$status,'CRITERIA_PASSED_PENDING_RESULT_REVIEW'))en_stop('FULL_CONTRACT')
  ec_validate_freeze(full$freeze,cfg,full$source_code_pins)
  if(!ec_equal(full$source_code_pins,en_dependencies()))en_stop('FULL_CODE_PINS')
  if(!identical(full$model_name,full$freeze$model))en_stop('FULL_MODEL')
  scores<-full$confirmation$retained_scores
  ec_validate_scores(scores,full$freeze$scores,cfg$criteria$minimum_scores)
  points<-full$model$standardized_points
  if(!identical(points$items,cfg$items)||!identical(points$factors,names(full$freeze$groups)))en_stop('MODEL_AXES')
  list(cfg=cfg,scores=scores,groups=full$freeze$groups[scores])
}
en_gcd<-function(a,b){while(b!=0){next_b<-a%%b;a<-b;b<-next_b};a}
en_rational<-function(categories,denominators) {
  if(!is.matrix(categories)||ncol(categories)!=length(denominators)||nrow(categories)==0L||
      any(!is.finite(categories))||any(categories!=floor(categories))||any(denominators<1)||
      any(denominators!=floor(denominators)))en_stop('RATIONAL_INPUT')
  lcm<-1
  for(d in denominators)lcm<-lcm/en_gcd(lcm,d)*d
  denominator<-ncol(categories)*lcm
  if(!is.finite(denominator)||denominator>2^52)en_stop('RATIONAL_RANGE')
  numerator<-rowSums(sweep(categories,2L,lcm/denominators,'*'))
  if(any(numerator<0|numerator>denominator)||any(numerator!=floor(numerator)))en_stop('RATIONAL_RANGE')
  list(values=numerator/denominator,numerator=numerator,denominator=denominator,lcm=lcm)
}
en_norm<-function(values,weight,rational=NULL,missing_share=0) {
  if(!is.numeric(missing_share)||length(missing_share)!=1L||!is.finite(missing_share)||
      missing_share<0||missing_share>1)en_stop('MISSING_SHARE')
  if(!is.numeric(values)||!length(values)||any(!is.finite(values))||any(values<0|values>1))en_stop('SCORE_DOMAIN')
  if(!is.numeric(weight)||length(weight)!=length(values)||any(!is.finite(weight))||any(weight<=0)||
      !is.finite(sum(weight)))en_stop('REFERENCE_WEIGHT')
  keys<-if(is.null(rational))values else rational$numerator
  grid_key<-sort(unique(keys));bin<-match(keys,grid_key)
  masses<-rowsum(matrix(weight,ncol=1L),bin,reorder=FALSE)
  mass<-numeric(length(grid_key));mass[as.integer(rownames(masses))]<-masses[,1L]
  count<-tabulate(bin,nbins=length(grid_key));total<-sum(mass)
  if(total<=0||!is.finite(total)||any(mass<=0))en_stop('REFERENCE_WEIGHT')
  midrank<-(cumsum(mass)-mass/2)/total
  grid<-if(is.null(rational))grid_key else grid_key/rational$denominator
  public<-list(score_grid=grid,weight_mass=mass,counts=count,reference_weight=total,
    midrank_cdf=midrank,midrank_percentile=100*midrank,
    ties=if(is.null(rational))'Exact equality of computed double values; no epsilon merging'else
      'Exact integer numerator on one LCM denominator',
    integer_numerator=if(is.null(rational))NULL else grid_key,
    integer_denominator=if(is.null(rational))NULL else rational$denominator,
    worst_cdf_lower=(1-missing_share)*midrank,
    worst_cdf_upper=(1-missing_share)*midrank+missing_share,
    worst_cdf_width=missing_share,population_transfer_missing_budget_passed=missing_share<=.05)
  list(public=public,positions=midrank[bin])
}
en_compare<-function(main,variant,original_weight,main_norm,variant_norm,main_rational=NULL,variant_rational=NULL) {
  if(length(main)!=length(variant)||length(original_weight)!=length(main)||any(!is.finite(variant)))en_stop('COMPARISON_DOMAIN')
  delta<-abs(variant-main);exceeds<-delta>.05
  if(!is.null(main_rational)&&!is.null(variant_rational)) {
    product<-main_rational$denominator*variant_rational$denominator
    cross<-abs(variant_rational$numerator*main_rational$denominator-main_rational$numerator*variant_rational$denominator)
    if(product*20>2^52)en_stop('RATIONAL_COMPARISON_RANGE')
    exceeds<-cross*20>product;delta<-cross/product
  }
  norm_delta<-abs(variant_norm$positions-main_norm$positions)
  total<-sum(original_weight);raw_mass<-sum(original_weight[exceeds])/total
  percentile_mass<-sum(original_weight[norm_delta>.05])/total
  dependent<-raw_mass>=.05||percentile_mass>=.05
  list(status=if(dependent)'CONTRACT_DEPENDENCE_BUDGET_EXCEEDED'else'WITHIN_SPECIFIED_BUDGETS',
    raw_max_absolute_difference=max(delta),percentile_max_absolute_difference=100*max(norm_delta),
    original_weight_mass_raw_over_05=raw_mass,original_weight_mass_percentile_over_5=percentile_mass,
    original_reference_weight=total,raw_difference_exclusive=.05,percentile_difference_exclusive=5,
    affected_original_weight_mass_inclusive=.05)
}
en_variant<-function(fun,main,weight,main_norm,main_rational) {
  tryCatch({v<-en_quiet(fun());missing<-if(is.null(v$missing_share))main_norm$public$worst_cdf_width else v$missing_share
    n<-en_norm(v$values,v$reference_weight,v$rational,missing)
    list(status='EXECUTED',norm=n$public,comparison=en_compare(main,v$values,weight,main_norm,n,main_rational,v$rational),
      diagnostics=v$diagnostics,definition=v$definition)},error=function(e)
    list(status='UNSUPPORTED',code=en_code(e),diagnostics=if(inherits(e,'en_error'))e$diagnostics else NULL))
}
en_gh<-function(n) {
  if(length(n)!=1L||!n%in%c(81L,161L,321L))en_stop('QUADRATURE_NODES')
  jacobi<-matrix(0,n,n);j<-seq_len(n-1L)
  jacobi[cbind(j,j+1L)]<-jacobi[cbind(j+1L,j)]<-sqrt(j)
  nodes<-sort(eigen(jacobi,symmetric=TRUE,only.values=TRUE)$values)
  # Equivalent Christoffel weights avoid tiny first-eigenvector components.
  previous<-rep(1,n);current<-nodes
  for(k in 2:(n-1L)){next_p<-(nodes*current-sqrt(k-1)*previous)/sqrt(k);previous<-current;current<-next_p}
  log_weight<- -log(n)-2*log(abs(current));weight<-exp(log_weight)
  if(any(!is.finite(nodes))||any(!is.finite(log_weight))||abs(sum(weight)-1)>1e-10)en_stop('QUADRATURE_WEIGHT')
  list(nodes=nodes,log_weight=log_weight,n=n)
}
en_log_interval<-function(a,b) {
  if(length(a)!=length(b)||anyNA(a)||anyNA(b)||any(a>=b))en_stop('NORMAL_RECTANGLE')
  out<-numeric(length(a));whole<-a== -Inf&b==Inf;out[whole]<-0
  left<-a== -Inf&!whole;out[left]<-pnorm(b[left],log.p=TRUE)
  right<-b==Inf&!whole;out[right]<-pnorm(a[right],lower.tail=FALSE,log.p=TRUE)
  internal<-!(whole|left|right);upper_tail<-internal&a>=0
  lower_tail<-internal&!upper_tail
  difference<-function(high,low)high+log(-expm1(low-high))
  out[lower_tail]<-difference(pnorm(b[lower_tail],log.p=TRUE),pnorm(a[lower_tail],log.p=TRUE))
  out[upper_tail]<-difference(pnorm(a[upper_tail],lower.tail=FALSE,log.p=TRUE),pnorm(b[upper_tail],lower.tail=FALSE,log.p=TRUE))
  if(any(!is.finite(out))||any(out>0))en_stop('NORMAL_RECTANGLE')
  out
}
en_item_model<-function(full,ids,factor) {
  p<-full$model$standardized_points
  loadings<-p$loadings
  if(!is.matrix(loadings))loadings<-do.call(rbind,lapply(loadings,unlist))
  if(!is.numeric(loadings)||!identical(dim(loadings),c(length(p$items),length(p$factors))))en_stop('LOADING_MATRIX')
  lambda<-as.numeric(loadings[match(ids,p$items),match(factor,p$factors)])
  if(any(!is.finite(lambda))||any(lambda<=0|lambda>=1))en_stop('ITEM_LOADING')
  labels<-p$threshold_labels;thresholds<-unlist(p$thresholds,use.names=FALSE)
  if(!is.character(labels)||length(labels)!=length(thresholds)||anyDuplicated(labels)||any(!is.finite(thresholds)))en_stop('MODEL_THRESHOLDS')
  cfg<-ed_default_config()
  expected<-oa_labels(cfg$manifest)[grepl('|',oa_labels(cfg$manifest),fixed=TRUE)]
  if(!identical(labels,expected))en_stop('MODEL_THRESHOLD_LABELS')
  tt<-lapply(ids,function(id)thresholds[startsWith(labels,paste0(id,'|'))])
  if(any(lengths(tt)!=vapply(cfg$manifest[ids],length,integer(1))-1L)||
      any(vapply(tt,function(x)is.unsorted(x,strictly=TRUE),logical(1))))en_stop('MODEL_THRESHOLDS')
  list(lambda=lambda,thresholds=tt,items=ids)
}
en_curve<-function(eta,model) {
  out<-numeric(length(eta))
  for(j in seq_along(model$lambda))out<-out+rowSums(pnorm(outer(eta*model$lambda[j],model$thresholds[[j]],'-')/
    sqrt(1-model$lambda[j]^2)))/length(model$thresholds[[j]])
  out/length(model$lambda)
}
en_posterior<-function(patterns,model,quadrature) {
  log_prob<-matrix(0,nrow(patterns),length(quadrature$nodes))
  for(j in seq_along(model$lambda)) {
    bounds<-c(-Inf,model$thresholds[[j]],Inf);category<-patterns[,j]
    sd<-sqrt(1-model$lambda[j]^2);shift<-model$lambda[j]*quadrature$nodes
    a<-outer(bounds[category+1L],shift,'-')/sd;b<-outer(bounds[category+2L],shift,'-')/sd
    log_prob<-log_prob+matrix(en_log_interval(as.vector(a),as.vector(b)),nrow(patterns))
  }
  log_prob<-sweep(log_prob,2L,quadrature$log_weight,'+')
  largest<-apply(log_prob,1L,max)
  if(any(!is.finite(largest)))en_stop('POSTERIOR_UNDEFINED')
  centered<-exp(log_prob-largest);denominator<-rowSums(centered)
  eta<-as.numeric(centered%*%quadrature$nodes)/denominator
  if(any(!is.finite(eta))||any(denominator<=0))en_stop('POSTERIOR_UNDEFINED')
  list(eta=eta,curve=en_curve(eta,model))
}
en_latent<-function(categories,model,weight) {
  key<-do.call(paste,c(as.data.frame(categories),sep=':'));first<-!duplicated(key)
  patterns<-categories[first,,drop=FALSE];mapping<-match(key,key[first])
  calculations<-lapply(c(81L,161L,321L),function(n)en_posterior(patterns,model,en_gh(n)))
  differences<-c('81_161'=max(abs(calculations[[1]]$curve-calculations[[2]]$curve)),
    '161_321'=max(abs(calculations[[2]]$curve-calculations[[3]]$curve)))
  diagnostics<-list(quadrature_nodes=c(81L,161L,321L),max_curve_difference=as.list(differences),
    required_161_321_max=1e-6,pattern_count=nrow(patterns),parameter_uncertainty='not included; no personal CI')
  if(differences['161_321']>1e-6)en_stop('EAP_STABILITY',diagnostics)
  list(values=calculations[[3]]$curve[mapping],reference_weight=weight,rational=NULL,diagnostics=diagnostics,
    definition='Marginal N(0,1) factor EAP using only this fixed score; original expected 0-1 curve at EAP')
}
en_analyse<-function(frame,full_aggregate,pspwght) {
  contract<-en_full_contract(full_aggregate);cfg<-contract$cfg;groups<-contract$groups;scores<-contract$scores
  ed_validate_frame(frame,cfg);n<-nrow(frame)
  design<-oa_design(frame$weight,frame$psu,frame$stratum,n,min_df=1L)
  keep<-complete.cases(frame[cfg$items]);complete_weight<-sum(frame$weight[keep]);total_weight<-sum(frame$weight)
  if(!is.finite(total_weight)||total_weight<=0)en_stop('WEIGHT_TOTAL')
  missing_share<-sum(frame$weight[!keep])/total_weight
  counts<-list(n_original=n,n_complete=sum(keep),n_missing=sum(!keep),original_psus=length(design$psu_stratum),
    original_strata=length(design$psus_by_stratum),original_design_df=design$df,
    zero_complete_psus=sum(vapply(seq_along(design$psu_stratum),function(p)!any(keep[design$psu==p]),logical(1))),
    original_weight=total_weight,complete_weight=complete_weight,complete_weight_share=complete_weight/total_weight,
    missing_weight_share=missing_share,missing_worst_cdf_width=missing_share)
  out<-list();means<-matrix(0,n,length(scores),dimnames=list(NULL,scores));mean_estimate<-numeric(length(scores))
  if(!any(keep)) {
    unavailable<-list(status='UNSUPPORTED',code='ESS_NORMS_EMPTY_COMPLETE')
    for(factor in scores)out[[factor]]<-list(items=groups[[factor]],status='UNSUPPORTED',code='ESS_NORMS_EMPTY_COMPLETE',
      primary=unavailable,raw_mean=unavailable,variants=list(unweighted=unavailable,pspwght=unavailable,
        weighted_z=unavailable,latent=unavailable,leave_one_out=setNames(rep(list(unavailable),length(groups[[factor]])),groups[[factor]])))
    covariance<-NULL
  } else {
    w<-frame$weight[keep];coded<-as.matrix(frame[keep,cfg$items,drop=FALSE]);denominators<-setNames(vapply(cfg$manifest,length,integer(1))-1L,cfg$items)
    for(factor in scores) {
      ids<-groups[[factor]];cats<-coded[,ids,drop=FALSE];x<-sweep(cats,2L,denominators[ids],'/')
      rational<-en_rational(cats,denominators[ids]);s<-rational$values;primary<-en_norm(s,w,rational,missing_share)
      mu<-sum(w*s)/sum(w);mean_estimate[match(factor,scores)]<-mu
      means[keep,factor]<-w/sum(w)*(s-mu)
      variants<-list()
      variants$unweighted<-en_variant(function()list(values=s,reference_weight=rep(1,length(s)),rational=rational,missing_share=sum(!keep)/n,
        definition='Same rational main score; unit reference weights'),s,w,primary,rational)
      variants$pspwght<-en_variant(function() {
        if(!is.numeric(pspwght)||length(pspwght)!=n||any(!is.finite(pspwght))||any(pspwght<=0))en_stop('PSPWGHT')
        if(!is.finite(sum(pspwght)))en_stop('PSPWGHT_TOTAL')
        ratio<-pspwght/frame$weight;scale<-median(ratio)
        if(any(!is.finite(ratio))||!is.finite(scale)||scale<=0)en_stop('PSPWGHT_SCALE')
        list(values=s,reference_weight=pspwght[keep],rational=rational,missing_share=sum(pspwght[!keep])/sum(pspwght),
          diagnostics=list(estimated_common_scale=scale,ratio_min=min(ratio),ratio_max=max(ratio),
            exact_multiplication_match=all(pspwght==frame$weight*scale),
            max_relative_rounding_difference=max(abs(ratio/scale-1)),
            max_absolute_rounding_residual=max(abs(pspwght-frame$weight*scale)),
            scope='Observed scalar/rounding diagnostics on original frame; no assumed ESS metadata equality'),
          definition='Same rational main score; original pspwght reference weights')
      },s,w,primary,rational)
      variants$weighted_z<-en_variant(function() {
        normalized<-w/sum(w);center<-colSums(x*normalized)
        sd<-sqrt(colSums(sweep(x,2L,center,'-')^2*normalized))
        if(any(!is.finite(sd))||any(sd<=0))en_stop('Z_SD')
        values<-as.numeric(x%*%(1/sd))/sum(1/sd)
        list(values=values,reference_weight=w,rational=NULL,diagnostics=list(item_population_sd=setNames(as.list(sd),ids)),
          definition='Weighted population item z mean rescaled by theoretical endpoints: sum(x/sd)/sum(1/sd)')
      },s,w,primary,rational)
      variants$latent<-en_variant(function()en_latent(cats,en_item_model(full_aggregate,ids,factor),w),s,w,primary,rational)
      variants$leave_one_out<-setNames(lapply(ids,function(omitted)en_variant(function() {
        left<-ids[ids!=omitted];r<-en_rational(coded[,left,drop=FALSE],denominators[left])
        list(values=r$values,reference_weight=w,rational=r,diagnostics=list(omitted_item=omitted,remaining_items=left),
          definition='One fixed omitted item; own equally weighted rational score and own norm on same nine-complete domain')
      },s,w,primary,rational)),ids)
      out[[factor]]<-list(status='EXECUTED',items=ids,primary=primary$public,variants=variants,
        rotation='No alternate score formula; structural rotation diagnostics remain in FULL confirmation')
    }
    covariance<-oa_taylor(means,design)
    for(i in seq_along(scores)) {
      variance<-covariance[i,i]
      if(!is.finite(variance)||variance<0)en_stop('MEAN_VARIANCE')
      se<-sqrt(variance);critical<-qt(.975,design$df)
      out[[scores[i]]]$raw_mean<-list(estimate=mean_estimate[i],design_se=se,lower=mean_estimate[i]-critical*se,
        upper=mean_estimate[i]+critical*se,critical=critical,df=design$df,
        method='Original-frame WR ultimate-PSU ratio mean; two-sided95 t; fixed coding/weights; no personal CI')
    }
  }
  structure(list(schema='life93-full-norms-aggregate-1',scope='Fixed FULL reference and supplemental variants; publication review still required',
    model_name=full_aggregate$model_name,retained_scores=scores,source_code_pins=full_aggregate$source_code_pins,
    counts=counts,raw_mean_covariance=covariance,scores=out,
    limits=c('All variants use the same nine-complete domain and original full PSU frame',
      'Main rational ties; floating variants tie only exact computed doubles; no epsilon coalescence',
      'Variant comparison masses always use original weights, even for alternate reference weights',
      'No favorable variant selection, case vectors, identifiers, IF or RDS export',
      'Conditional fixed-model/weight diagnostics; no model/parameter/calibration uncertainty or personal intervals',
      'Original weight/data provenance and actual FULL authority require the future root wrapper')),class='en_analysis')
}
en_public<-function(result) {
  if(!inherits(result,'en_analysis'))en_stop('RESULT_CLASS')
  unclass(result)[c('schema','scope','model_name','retained_scores','source_code_pins','counts',
    'raw_mean_covariance','scores','limits')]
}
