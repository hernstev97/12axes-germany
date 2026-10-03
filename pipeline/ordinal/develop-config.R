# Author copy of the A-development criteria before any real response access.
# These are project budgets, not literature validity standards or gate approval.
ed_default_config <- function() {
  ids <- c('B34','B35','B36','B40','B41','B42','B43','B44','B45')
  counts <- c(5L,5L,5L,4L,4L,4L,11L,11L,11L)
  manifest <- setNames(lapply(counts,function(k)0:(k-1L)),ids)
  list(schema='life93-A-development-1',status='AUTHOR_DRAFT_NO_EMPIRICAL_GATE',
    input_columns=c('stratum','psu','weight',ids),items=ids,categories=counts,manifest=manifest,
    models=list(M1=list(ALL=ids),M2=list(H=ids[1:3],ZF=ids[4:9]),
                M3=list(H=ids[1:3],Z=ids[4:6],F=ids[7:9])),
    labels=list(H='Freiheit, familiäre Scham und Adoption homosexueller Menschen',
      Z='Zulassung von Zuwanderung für die drei erfragten Gruppen',
      F='Wahrgenommene wirtschaftliche, kulturelle und allgemeine Folgen von Zuwanderung',
      ZF='Zulassung und wahrgenommene Folgen von Zuwanderung'),
    metric='fixed identity ULS on survey-weighted ordinal moments',
    efa=list(factors=1:3,rotation='geomin',rstarts=30L,epsilon=.001,
      seed=2026100313L,repeat_seed=2026100314L,sensitivity='oblimin',
      alignment_max_difference=1e-4,numerical_tie_tolerance=1e-8),
    criteria=list(alpha=.05,rms_one_sided_upper_max=.10,loading_lower_exclusive=0,
      reliability_lower_exclusive=.50,dominance_upper_max=.50,correlation_lower_exclusive=-1,
      correlation_upper_exclusive=1,
      minimum_scores=2L,selection_order=c('M2','M3'),
      rms_interval='one-sided95 normal delta',other_intervals='two-sided95 normal delta',
      loading_family='Bonferroni within each fixed score',
      dominance_family='Bonferroni within each fixed score, checked separately for raw and model covariance',
      correlation_family='Bonferroni all pairs of the complete candidate model, before score outcomes',
      near_zero_rms='INCONCLUSIVE; no conservative alternative implemented'),
    runtime=list(R='4.5.3',lavaan='0.7.2',pbivnorm='0.6.0',jsonlite='2.0.0'),
    source_pins=list('pipeline/ordinal/adapter_v2.R'='8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b',
                    'pipeline/ordinal/support.R'='b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22'),
    limits=c('fixed original item set and oriented category coding; no outcome-based item drops or residual repairs',
      'normal/delta inference conditional on the chosen model, fixed coding and weights',
      'WR ultimate-PSU approximation; no calibration/FPC/PPS-WOR or personal uncertainty',
      'conservative full-moment SPD/design-df contract inherited from the pinned adapter',
      'selection in A is exploratory development; B remains held back; no immediate publication permission'))
}
