# Fixed entry only: unmodified public mathematics test or private stdin snapshot.
args<-commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==5L,identical(Sys.getenv('HOME'),args[[3]]))
project<-normalizePath(args[[1]],mustWork=TRUE);own<-normalizePath(args[[2]],mustWork=TRUE)
stopifnot(identical(own,Sys.getenv('ESS_RUNTIME_OUTPUT')),
  bitwAnd(as.integer(file.info(own)$mode),511L)==448L,args[[5]]%in%c('synthetic','FULL'))
source(file.path(project,'pipeline/ordinal/norms.R'))
ern_payload_main<-function(payload,output,init)tryCatch({
  a<-payload$authorization
  if(!is.list(a)||!identical(a$schema,'r-norm-runtime-auth-v1')||
    !identical(a$decision,'ACCEPTED_BOUNDED')||!identical(a$arm,'FULL')||!isTRUE(a$wrapper_verified)||
    !is.character(a$normGateSha256)||!grepl('^[0-9a-f]{64}$',a$normGateSha256)||
    !ec_equal(a$codeHashes[names(init$pins)],init$pins))en_stop('RUNTIME_AUTHORIZATION')
  if(!dir.exists(output)||bitwAnd(as.integer(file.info(output)$mode),511L)!=448L)en_stop('PRIVATE_OUTPUT_MODE')
  destination<-file.path(output,'norms-aggregate.private.json')
  if(file.exists(destination))en_stop('DO_NOT_OVERWRITE')
  frame<-as.data.frame(payload$frame,optional=TRUE,stringsAsFactors=FALSE)
  result<-en_quiet(en_public(en_analyse(frame,payload$full_aggregate,payload$pspwght)))
  en_quiet(jsonlite::write_json(result,destination,auto_unbox=TRUE,pretty=TRUE,digits=16,na='null'))
  if(!en_quiet(Sys.chmod(destination,'0600')))en_stop('PRIVATE_FILE_MODE')
  cat('ESS_NORMS_FULL_EXECUTED_PRIVATE_OUTPUT\n');0L
},error=function(e){cat(en_code(e),'\n',sep='');1L})
if(args[[5]]=='synthetic') {
  # Only a fixture FUNCTION is saved. All invented cases stay in memory.
  fixture<-"ed_synthetic_frame<-function(cfg,kind,seed,weak_factor=1L) {
    stopifnot(kind%in%c('M2','M3','weak'));set.seed(seed)
    g<-192L;size<-40L;n<-g*size;psu<-rep(seq_len(g),each=size)
    dimensions<-if(kind=='M2')2L else 3L
    eta<-matrix(rnorm(n*dimensions),n,dimensions);eta<-sqrt(.9)*eta+sqrt(.1)*rnorm(n)
    clusters<-matrix(rnorm(g*dimensions),g,dimensions)
    eta<-sqrt(.96)*eta+sqrt(.04)*clusters[psu,,drop=FALSE]
    factor<-if(kind=='M2')c(rep(1L,3L),rep(2L,6L))else rep(1:3,each=3L)
    loads<-rep(.82,9L);if(kind=='weak')loads[((weak_factor-1L)*3L+1L):(weak_factor*3L)]<-.25
    x<-matrix(rnorm(n*9L),n,9L)
    x<-sweep(x,2L,sqrt(1-loads^2),'*')+sweep(eta[,factor],2L,loads,'*')
    frame<-data.frame(stratum=rep(rep(1:4,each=g/4),each=size),psu=psu,weight=runif(n,.8,1.2))
    for(j in seq_len(9L)) {
      breaks<-qnorm(seq(1/cfg$categories[j],1-1/cfg$categories[j],length.out=cfg$categories[j]-1L))
      frame[[cfg$items[j]]]<-as.integer(findInterval(x[,j],breaks))
      frame[[cfg$items[j]]][psu<=4L]<-NA_integer_
    };frame
  }"
  path<-file.path(own,'fixture.R');stopifnot(!file.exists(path))
  writeLines(fixture,path);stopifnot(Sys.chmod(path,'0600'))
  source(file.path(project,'pipeline/ordinal/test-norms.R'))
  # Exercise exactly the same decoded-memory path, without any private input.
  runtime_start<-jsonlite::fromJSON(file.path(own,'start.json'),simplifyVector=TRUE)
  payload<-list(authorization=list(schema='r-norm-runtime-auth-v1',decision='ACCEPTED_BOUNDED',
    arm='FULL',wrapper_verified=TRUE,normGateSha256=paste(rep('a',64),collapse=''),codeHashes=runtime_start$codeHashes),
    frame=as.list(frame_actual),pspwght=2*frame_actual$weight,full_aggregate=full_actual)
  payload<-jsonlite::fromJSON(jsonlite::toJSON(payload,auto_unbox=TRUE,digits=16,na='null'),simplifyVector=TRUE)
  transport_checks<-list();probeout<-file.path(own,'memory-transport-probe');dir.create(probeout,mode='0700')
  status<-capture.output(code<-ern_payload_main(payload,probeout,init))
  transport_checks$actual_memory_snapshot_path<-code==0L&&identical(status,'ESS_NORMS_FULL_EXECUTED_PRIVATE_OUTPUT')
  output<-file.path(probeout,'norms-aggregate.private.json')
  transport_checks$aggregate_only600_no_RDS<-identical(list.files(probeout),'norms-aggregate.private.json')&&
    bitwAnd(as.integer(file.info(output)$mode),511L)==384L
  decoded<-jsonlite::fromJSON(output,simplifyVector=TRUE)
  transport_checks$same_actual_norm_counts<-ec_equal(decoded$counts,actual$counts)
  status<-capture.output(code<-ern_payload_main(payload,probeout,init))
  transport_checks$overwrite_rejected<-code==1L&&identical(status,'ESS_NORMS_DO_NOT_OVERWRITE')
  payload$authorization$decision<-'REJECTED'
  status<-capture.output(code<-ern_payload_main(payload,probeout,init))
  transport_checks$bad_authorization_fixed_code<-code==1L&&identical(status,'ESS_NORMS_RUNTIME_AUTHORIZATION')
  jsonlite::write_json(list(scope='invented decoded-memory transport only',checks=transport_checks,
    passed=sum(unlist(transport_checks)),total=length(transport_checks)),file.path(own,'transport-checks.json'),auto_unbox=TRUE,pretty=TRUE)
  stopifnot(Sys.chmod(file.path(own,'transport-checks.json'),'0600'))
  cat('NORM_SYNTHETIC_TRANSPORT_CHECKS ',sum(unlist(transport_checks)),'/',length(transport_checks),'\n',sep='')
  quit(status=if(all(unlist(transport_checks)))0L else 1L)
} else {
  code<-tryCatch({
    init<-en_initialize(project)
    payload<-en_quiet(jsonlite::fromJSON(paste(readLines(file('stdin'),warn=FALSE),collapse='\n'),simplifyVector=TRUE))
    ern_payload_main(payload,own,init)
  },error=function(e){cat(en_code(e),'\n',sep='');1L})
  quit(status=code)
}
