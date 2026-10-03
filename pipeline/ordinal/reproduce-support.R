# Reproduce the hash-pinned committed support test in a fresh runtime output.
# Only its historical output-directory guard is adapted. Scientific expressions,
# constants, tolerances and test order remain unchanged. The wrapper supplies a
# test-fixed-v2- prefix for free labels, selecting adapter_v2 and fixed W=I.
args <- commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==4L,startsWith(args[[4]],'test-fixed-v2-'))
project <- normalizePath(args[[1]],mustWork=TRUE)
own <- normalizePath(args[[2]],mustWork=TRUE)
stopifnot(identical(own,Sys.getenv('ESS_RUNTIME_OUTPUT')),
          startsWith(own,paste0(file.path(project,'outputs/loop/r-runtime'),'/')),
          identical(Sys.getenv('HOME'),args[[3]]))
original <- readLines(file.path(project,'pipeline/ordinal/test-support.R'),warn=FALSE)
guard <- "identical(own,file.path(project,'outputs/loop/resume-ordinal-support'))"
replacement <- "identical(own,Sys.getenv('ESS_RUNTIME_OUTPUT'))"
stopifnot(sum(grepl(guard,original,fixed=TRUE))==1L)
adapted <- sub(guard,replacement,original,fixed=TRUE)
eval(parse(text=adapted),envir=globalenv())
