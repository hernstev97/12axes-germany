/**
 * Blocks and cross-references of the descriptive answer profile (Profilregeln v1).
 * A block is an original question block with one answer format. A cross-reference
 * is a project compilation across blocks or studies. Neither yields a value.
 */

export type BlockPattern = 'directions' | 'scale-values' | 'ordered-labels' | 'grouped-labels';

export interface BlockRule {
  readonly id: string;
  readonly title: string;
  readonly itemIds: readonly string[];
  readonly pattern: BlockPattern;
  /** Fixed explanatory sentence shown with the block pattern. */
  readonly note: string;
  /** Why these questions are read together, with source locations. */
  readonly basis: string;
}

export interface CrossReferenceRule {
  readonly id: string;
  readonly title: string;
  readonly itemIds: readonly string[];
  /** Explains how the questions differ. Never evaluates the combination. */
  readonly context: string;
}

export const BLOCK_RULES: readonly BlockRule[] = Object.freeze([
  {
    id: 'justice_principles',
    title: 'Vier Gerechtigkeitsprinzipien',
    itemIds: ['ESS9e03_3:sofrdst', 'ESS9e03_3:sofrwrk', 'ESS9e03_3:sofrpr', 'ESS9e03_3:sofrprv'],
    pattern: 'directions',
    note: 'Die Forschung behandelt Gleichheit, Leistung, Bedarf und Anrecht als getrennte Gerechtigkeitsprinzipien. Zustimmung zu mehreren Prinzipien zugleich ist häufig und kein Widerspruch.',
    basis:
      'Originalblock ESS9 G26–G29 mit gleicher Einleitung und Antwortliste. ESS9-Modulvorlage „Justice and Fairness“, S. 4 und 33–36. Adriaans und Fourré 2022, S. 2–3.',
  },
  {
    id: 'state_responsibility',
    title: 'Staatliche Verantwortung für drei Lebenslagen',
    itemIds: ['ESS8e02_3:gvslvol', 'ESS8e02_3:gvslvue', 'ESS8e02_3:gvcldcr'],
    pattern: 'scale-values',
    note: 'Das ESS-Modul unterscheidet diese Lebenslagen bewusst. Unterschiedliche Werte beschreiben eine Unterscheidung zwischen Gruppen, keinen Widerspruch.',
    basis:
      'Originalblock ESS8 E6–E8 mit gleicher Einleitung und Skala. ESS8-Modulvorlage „Welfare Attitudes“, S. 3–4 und 8–9.',
  },
  {
    id: 'democracy_norms',
    title: 'Merkmale der Demokratie im Allgemeinen',
    itemIds: [
      'ESS10SCe03_2:fairelc',
      'ESS10SCe03_2:dfprtal',
      'ESS10SCe03_2:medcrgv',
      'ESS10SCe03_2:rghmgpr',
      'ESS10SCe03_2:votedir',
      'ESS10SCe03_2:cttresa',
      'ESS10SCe03_2:gptpelc',
      'ESS10SCe03_2:gvctzpv',
      'ESS10SCe03_2:grdfinc',
      'ESS10SCe03_2:viepol',
      'ESS10SCe03_2:wpestop',
    ],
    pattern: 'scale-values',
    note: 'Die Werte beschreiben, wie wichtig einzelne Merkmale für Demokratie im Allgemeinen sind. Sie bewerten nicht die Demokratie in Deutschland und ergeben keinen Gesamtwert.',
    basis:
      'Originalblock ESS10 B1–B11 mit gleicher Einleitung und Skala. B12 steht unter europäischer Integration. ESS10-Antrag „Understandings and Evaluations of Democracy“, S. 9–12.',
  },
  {
    id: 'police_obligation',
    title: 'Pflichten gegenüber der Polizei',
    itemIds: ['ESS5e03_6:bplcdc', 'ESS5e03_6:dpcstrb'],
    pattern: 'scale-values',
    note: 'Die beiden Fragen unterscheiden sich im Anlass: fehlendes Einverständnis mit einer Entscheidung und eine als nicht gut empfundene Behandlung.',
    basis:
      'Originalblock ESS5 D18–D20 mit gleicher Einleitung und Skala. D19 ist nicht im Entwurf. ESS5-Modulvorlage „Trust in Justice“, S. 20–23.',
  },
  {
    id: 'law_obligation',
    title: 'Gesetze und Gerichtsurteile',
    itemIds: ['ESS5e03_6:dbctvrd', 'ESS5e03_6:lwstrob', 'ESS5e03_6:rgbrklw'],
    pattern: 'directions',
    note: 'Die drei Aussagen unterscheiden sich in ihrer Reichweite: eine Pflicht gegenüber abschließenden Gerichtsurteilen, eine allgemeine Regel und ein Ausnahmefall („manchmal“).',
    basis:
      'Originalblock ESS5 D34–D36 mit gleicher Einleitung und Antwortliste. D33 gehört zu einem anderen Konzept. ESS5-Modulvorlage „Trust in Justice“, S. 25–26 und 31–32.',
  },
  {
    id: 'climate_measures',
    title: 'Drei Maßnahmen gegen den Klimawandel',
    itemIds: ['ESS8e02_3:inctxff', 'ESS8e02_3:sbsrnen', 'ESS8e02_3:banhhap'],
    pattern: 'directions',
    note: 'Abgabe, Förderung und Verkaufsverbot sind verschiedene Arten von Maßnahmen. Die Antworten beschreiben jeweils nur die genannte Maßnahme.',
    basis:
      'Originalblock ESS8 D30–D32 mit gleicher Einleitung und Antwortliste. ESS Topline Results 9, S. 13–14.',
  },
  {
    id: 'migration_admission',
    title: 'Zuwanderung nach Herkunftsgruppen',
    itemIds: ['ESS10SCe03_2:imsmetn', 'ESS10SCe03_2:imdfetn', 'ESS10SCe03_2:impcntr'],
    pattern: 'ordered-labels',
    note: 'Die drei Fragen unterscheiden Herkunftsgruppen. Unterschiedliche Antworten beschreiben eine Unterscheidung nach Gruppe. Gründe erfragt der Fragebogen nicht. „Volksgruppe oder ethnische Gruppe“ ist die deutsche ESS-Übersetzung von „race or ethnic group“ aus dem Jahr 2021. Das Projekt übernimmt den Begriff unverändert, damit die Antworten vergleichbar bleiben.',
    basis: 'Originalblock ESS10 A54–A56 mit gleicher Antwortliste. ESS Topline Results 7, S. 5.',
  },
  {
    id: 'gender_policy_measures',
    title: 'Mittel der Gleichstellungspolitik',
    itemIds: [
      'ESS11e04_2:eqparep',
      'ESS11e04_2:eqparlv',
      'ESS11e04_2:freinsw',
      'ESS11e04_2:fineqpy',
    ],
    pattern: 'directions',
    note: 'Die Fragen betreffen bestimmte gesetzliche oder betriebliche Mittel. Eine Antwort zu einem Mittel sagt nicht, wie das Ziel der Gleichstellung bewertet wird.',
    basis:
      'Originalblock ESS11 E19–E22 mit gleicher Antwortliste. ESS11-Modulvorlage „Gender in Contemporary Europe“, S. 11–12 und 36–38.',
  },
  {
    id: 'electricity_sources',
    title: 'Strom aus sieben Energiequellen',
    itemIds: [
      'ESS8e02_3:elgcoal',
      'ESS8e02_3:elgngas',
      'ESS8e02_3:elghydr',
      'ESS8e02_3:elgnuc',
      'ESS8e02_3:elgsun',
      'ESS8e02_3:elgwind',
      'ESS8e02_3:elgbio',
    ],
    pattern: 'grouped-labels',
    note: 'Die Fragen erfassen die gewünschte Menge je Energiequelle. Sie nennen keine Kosten, keine Fristen und keinen Gesamtumfang der Stromerzeugung.',
    basis:
      'Originalblock ESS8 D4–D10 mit gleicher Einleitung und Liste 35. ESS8-Modulvorlage „Climate Change and Energy“.',
  },
  {
    id: 'asylum',
    title: 'Asyl',
    itemIds: ['ESS8e02_3:gvrfgap', 'ESS8e02_3:rfgbfml'],
    pattern: 'directions',
    note: 'Die beiden Fragen betreffen die Prüfung von Asylanträgen und den Familiennachzug nach einer Anerkennung. Die Frage C43 dazwischen erfasst eine Wahrnehmung und ist nicht enthalten.',
    basis: 'Originalblock ESS8 C42–C44 mit gleicher Einleitung und Liste 31.',
  },
  {
    id: 'same_sex_couples',
    title: 'Schwule und Lesben',
    itemIds: ['ESS10SCe03_2:freehms', 'ESS10SCe03_2:hmsacld'],
    pattern: 'directions',
    note: 'Die eine Frage nennt ein allgemeines Prinzip, die andere ein bestimmtes Recht. Die Frage A48 dazwischen erfasst ein persönliches Gefühl und ist nicht enthalten.',
    basis: 'Originalblock ESS10 A46–A49 mit gleicher Einleitung und Antwortliste.',
  },
]);

export const CROSS_REFERENCE_RULES: readonly CrossReferenceRule[] = Object.freeze([
  {
    id: 'income_differences',
    title: 'Einkommensunterschiede',
    itemIds: ['ESS9e03_3:sofrdst', 'ESS11e04_2:gincdif', 'ESS10SCe03_2:grdfinc'],
    context:
      'Alle drei Fragen betreffen Einkommensunterschiede. Sie fragen nach Verschiedenem: einem Merkmal einer gerechten Gesellschaft (ESS9), einem Auftrag an den Staat (ESS11) und der Wichtigkeit für Demokratie im Allgemeinen (ESS10).',
  },
  {
    id: 'social_protection',
    title: 'Soziale Absicherung',
    itemIds: [
      'ESS9e03_3:sofrpr',
      'ESS10SCe03_2:gvctzpv',
      'ESS8e02_3:gvslvol',
      'ESS8e02_3:gvslvue',
      'ESS8e02_3:basinc',
    ],
    context:
      'Die Fragen betreffen soziale Absicherung, aber verschiedene Gegenstände: die Sorge für Arme und Bedürftige als Merkmal einer gerechten Gesellschaft (ESS9), den Schutz aller vor Armut als Merkmal der Demokratie (ESS10), staatliche Verantwortung für den Lebensstandard im Alter und bei Arbeitslosigkeit ohne Bedürftigkeitsprüfung (ESS8) und ein Grundeinkommen für alle, das viele bestehende Leistungen ersetzen würde (ESS8).',
  },
  {
    id: 'majority_will',
    title: 'Gewicht der Bevölkerungsmehrheit',
    itemIds: [
      'ESS10SCe03_2:votedir',
      'ESS10SCe03_2:viepol',
      'ESS10SCe03_2:wpestop',
      'ESS10SCe03_2:scchpldm',
    ],
    context:
      'Drei Fragen erfassen die Wichtigkeit eines Merkmals auf einer Skala von 0 bis 10. Die vierte verlangt eine Wahl zwischen zwei Reaktionen der Regierung. Die beiden Formate lassen sich nicht verrechnen.',
  },
  {
    id: 'law_and_authorities',
    title: 'Recht, Gerichte und Polizei',
    itemIds: [
      'ESS10SCe03_2:cttresa',
      'ESS5e03_6:dbctvrd',
      'ESS5e03_6:lwstrob',
      'ESS5e03_6:rgbrklw',
      'ESS5e03_6:bplcdc',
      'ESS5e03_6:dpcstrb',
    ],
    context:
      'Die Fragen betreffen die Bindung an Recht und Behörden. Sie erfassen die Wichtigkeit gleicher Behandlung durch Gerichte für Demokratie im Allgemeinen (ESS10), Zustimmung zu allgemeinen Aussagen über Gesetze und Urteile (ESS5) und die eigene Pflicht gegenüber der Polizei (ESS5).',
  },
  {
    id: 'leadership_and_law',
    title: 'Politische Führung und Recht',
    itemIds: [
      'ESS10SCe03_2:accalaw',
      'ESS10SCe03_2:loylead',
      'ESS10SCe03_2:cttresa',
      'ESS5e03_6:prtyban',
    ],
    context:
      'Die Fragen betreffen die Bindung politischer Macht. Sie erfassen die Akzeptanz einer Führungsperson über dem Gesetz auf einer Skala von 0 bis 10 (ESS10), Zustimmung zu einer Aussage über Loyalität (ESS10), die Wichtigkeit gleicher Behandlung durch Gerichte für Demokratie im Allgemeinen (ESS10) und Zustimmung zum Verbot demokratiefeindlicher Parteien (ESS5, 2010/11).',
  },
  {
    id: 'work_and_family',
    title: 'Erwerbsarbeit und Kinderbetreuung',
    itemIds: ['ESS8e02_3:gvcldcr', 'ESS8e02_3:wrkprbf', 'ESS11e04_2:eqparlv'],
    context:
      'Die Fragen betreffen Kinderbetreuung und Erwerbsarbeit von Eltern. Sie erfassen staatliche Verantwortung (ESS8), zusätzliche Leistungen trotz deutlich höherer Steuern (ESS8) und eine gesetzliche Pflicht zu gleich langer Elternzeit (ESS11).',
  },
  {
    id: 'european_union',
    title: 'Europäische Union',
    itemIds: [
      'ESS10SCe03_2:vteurmmb',
      'ESS10SCe03_2:keydec',
      'ESS11e04_2:euftf',
      'ESS8e02_3:eusclbf',
    ],
    context:
      'Die Fragen stellen verschiedene Aufgaben: eine hypothetische Abstimmung über die Mitgliedschaft (ESS10), die Wichtigkeit nationaler Entscheidungen für Demokratie im Allgemeinen (ESS10), die Richtung der Einigung (ESS11) und ein bestimmtes gemeinsames Sozialleistungsprogramm (ESS8).',
  },
]);

/** Shown once when any answer uses the middle category of an agreement or support list. */
export const MIDDLE_NOTE =
  '„Weder noch“ und „Weder dafür noch dagegen“ können Unentschiedenheit, eine fehlende Meinung oder die Zurückweisung einer Annahme der Frage ausdrücken. Welcher Grund vorliegt, erfasst die Frage nicht.';

/** Shown with every cross-reference. */
export const CROSS_REFERENCE_NOTE =
  'Zusammenstellung durch das Projekt. Die Antworten stehen nebeneinander und werden nicht verrechnet. Eine gemeinsame Struktur dieser Fragen ist nicht geprüft.';
