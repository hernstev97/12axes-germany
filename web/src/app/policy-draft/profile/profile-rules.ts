/**
 * Rule tables for the descriptive answer profile (Profilregeln v1).
 * Texts are project wording. Quoted parts and dass-clauses follow the German
 * ESS originals; deviations are listed in docs/profilregeln-v1.md.
 * Direction comes from these explicit tables, never from code numbers alone.
 */

export type Direction = 'positive' | 'middle' | 'negative';

/** How a chosen category becomes a sentence. */
export type StatementForm =
  /** Five-point agreement: the original statement is quoted. */
  | { readonly form: 'agreement'; readonly statement: string }
  /** Support for a measure: "Dafür, dass …" with an original dass-clause. */
  | { readonly form: 'support-clause'; readonly clause: string }
  /** Support for a measure: "Für …" with a noun phrase. */
  | { readonly form: 'support-noun'; readonly nounPhrase: string }
  /** 0–10 scale without a substantive middle: value and anchors only. */
  | { readonly form: 'scale'; readonly subject: string }
  /** 0–10 scale between two opposite statements. */
  | { readonly form: 'bipolar'; readonly subject: string }
  /** Ordered or nominal categories: the original label is quoted. */
  | { readonly form: 'label'; readonly subject: string };

export interface ItemRule {
  /** Short title for lists and evidence lines. */
  readonly title: string;
  readonly statement: StatementForm;
  /** Fixed context marker from the wording; shown with every statement. */
  readonly context: string;
  /** Explicit direction for agreement and support forms. */
  readonly directions?: Readonly<Record<string, Direction>>;
}

const AGREE: Readonly<Record<string, Direction>> = Object.freeze({
  '1': 'positive',
  '2': 'positive',
  '3': 'middle',
  '4': 'negative',
  '5': 'negative',
});
/** 1 = Sehr dafür … 5 = Sehr dagegen (ESS8 D30–D32, ESS11 E19–E22). */
const FOR_FIRST: Readonly<Record<string, Direction>> = AGREE;
/** 1 = Sehr dagegen … 4 = Sehr dafür, no middle category (ESS8 E33–E35). */
const AGAINST_FIRST: Readonly<Record<string, Direction>> = Object.freeze({
  '1': 'negative',
  '2': 'negative',
  '3': 'positive',
  '4': 'positive',
});

const DEMOCRACY_CONTEXT =
  'Wichtigkeit für die Demokratie im Allgemeinen. Die Frage bewertet nicht die Demokratie in Deutschland.';
const CLIMATE_CONTEXT = 'Maßnahme in Deutschland zur Reduzierung des Klimawandels.';
const RESPONSIBILITY_CONTEXT =
  'Ausmaß staatlicher Verantwortung. Die Frage nennt keine Ausgabenhöhe und keine bestimmte Leistung.';
const JUSTICE_CONTEXT =
  'Merkmal einer gerechten Gesellschaft. Die Frage nennt keinen Auftrag an den Staat.';
const ADMISSION_CONTEXT =
  'Wie vielen Menschen dieser Gruppe Deutschland erlauben sollte, hier zu leben. Die Frage nennt keine Gründe und keine Bedingungen.';

const ELECTRICITY_CONTEXT =
  'Gewünschte Menge des in Deutschland verbrauchten Stroms aus dieser Energiequelle. Erhoben 2016/17.';
const ESS10_PANDEMIC_CONTEXT =
  'Erhoben 2021/22. Die Frage gilt ausdrücklich für die Bekämpfung einer Pandemie.';

export const ITEM_RULES: Readonly<Record<string, ItemRule>> = Object.freeze({
  'ESS9e03_3:sofrdst': {
    title: 'Gleichheit',
    statement: {
      form: 'agreement',
      statement:
        'Eine Gesellschaft ist gerecht, wenn Einkommen und Vermögen gleichmäßig auf alle Menschen verteilt sind.',
    },
    context: JUSTICE_CONTEXT,
    directions: AGREE,
  },
  'ESS9e03_3:sofrwrk': {
    title: 'Leistung',
    statement: {
      form: 'agreement',
      statement:
        'Eine Gesellschaft ist gerecht, wenn hart arbeitende Menschen mehr verdienen als andere.',
    },
    context: JUSTICE_CONTEXT,
    directions: AGREE,
  },
  'ESS9e03_3:sofrpr': {
    title: 'Bedarf',
    statement: {
      form: 'agreement',
      statement:
        'Eine Gesellschaft ist gerecht, wenn sie sich um Arme und Bedürftige kümmert, unabhängig davon, was diese der Gesellschaft zurückgeben.',
    },
    context: JUSTICE_CONTEXT,
    directions: AGREE,
  },
  'ESS9e03_3:sofrprv': {
    title: 'Anrecht durch Herkunft',
    statement: {
      form: 'agreement',
      statement:
        'Eine Gesellschaft ist gerecht, wenn Menschen aus Familien mit hoher gesellschaftlicher Stellung Privilegien in ihrem Leben genießen.',
    },
    context: JUSTICE_CONTEXT,
    directions: AGREE,
  },
  'ESS11e04_2:gincdif': {
    title: 'Staatliche Maßnahmen gegen Einkommensunterschiede',
    statement: {
      form: 'agreement',
      statement: 'Der Staat sollte Maßnahmen ergreifen, um Einkommensunterschiede zu verringern.',
    },
    context: 'Auftrag an den Staat. Die Frage nennt keine bestimmte Maßnahme und keine Kosten.',
    directions: AGREE,
  },
  'ESS8e02_3:gvslvol': {
    title: 'Lebensstandard im Alter',
    statement: {
      form: 'scale',
      subject: 'Staatliche Verantwortung für einen angemessenen Lebensstandard im Alter',
    },
    context: RESPONSIBILITY_CONTEXT,
  },
  'ESS8e02_3:gvslvue': {
    title: 'Lebensstandard bei Arbeitslosigkeit',
    statement: {
      form: 'scale',
      subject: 'Staatliche Verantwortung für einen angemessenen Lebensstandard für Arbeitslose',
    },
    context: RESPONSIBILITY_CONTEXT,
  },
  'ESS8e02_3:gvcldcr': {
    title: 'Kinderbetreuung für berufstätige Eltern',
    statement: {
      form: 'scale',
      subject:
        'Staatliche Verantwortung für ausreichende Kinderbetreuungsmöglichkeiten für berufstätige Eltern',
    },
    context: RESPONSIBILITY_CONTEXT,
  },
  'ESS8e02_3:bnlwinc': {
    title: 'Sozialleistungen nur für die niedrigsten Einkommen',
    statement: {
      form: 'support-clause',
      clause:
        'dass nur noch die Personen mit den niedrigsten Einkommen staatliche Sozialleistungen erhalten würden, während Personen mit einem mittleren oder hohen Einkommen auf sich selbst gestellt wären',
    },
    context:
      'Die Frage nennt die Folge für mittlere und hohe Einkommen. Eine mittlere Antwort war nicht vorgesehen.',
    directions: AGAINST_FIRST,
  },
  'ESS8e02_3:eduunmp': {
    title: 'Mehr Weiterbildung, weniger Arbeitslosenunterstützung',
    statement: {
      form: 'support-clause',
      clause:
        'dass der Staat mehr für die Aus- und Weiterbildung von Arbeitslosen ausgibt, aber dafür weniger Arbeitslosenunterstützung zahlt',
    },
    context:
      'Die Frage setzt eine feste Geldsumme zur Bewältigung der Arbeitslosigkeit voraus. Eine mittlere Antwort war nicht vorgesehen.',
    directions: AGAINST_FIRST,
  },
  'ESS8e02_3:wrkprbf': {
    title: 'Leistungen für erwerbstätige Eltern trotz höherer Steuern',
    statement: {
      form: 'support-clause',
      clause:
        'dass Staat und Regierung zusätzliche Sozialleistungen einführen, die es erwerbstätigen Eltern erleichtern, Arbeit und Familie zu vereinbaren, auch wenn das deutlich höhere Steuern für alle bedeuten würde',
    },
    context:
      'Die Frage verbindet die Leistung mit deutlich höheren Steuern für alle. Eine mittlere Antwort war nicht vorgesehen.',
    directions: AGAINST_FIRST,
  },
  'ESS10SCe03_2:fairelc': {
    title: 'Freie und faire Wahlen',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass Wahlen zum nationalen Parlament frei und fair sind“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:dfprtal': {
    title: 'Klare Unterschiede zwischen Parteien',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass sich die verschiedenen politischen Parteien inhaltlich klar voneinander unterscheiden“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:medcrgv': {
    title: 'Recht der Medien auf Kritik an der Regierung',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Medien das Recht haben, Kritik an der Regierung zu üben“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:rghmgpr': {
    title: 'Schutz der Rechte von Minderheiten',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Rechte von Minderheiten geschützt werden“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:votedir': {
    title: 'Letztes Wort durch Volksabstimmungen',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Bürger bei den wichtigsten politischen Sachfragen durch direkte Volksabstimmungen das letzte Wort haben“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:cttresa': {
    title: 'Gleichbehandlung durch Gerichte',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Gerichte alle Menschen gleich behandeln“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:gptpelc': {
    title: 'Abwahl von Regierungsparteien nach schlechter Arbeit',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass Regierungsparteien bei Wahlen abgestraft werden, wenn sie schlechte Arbeit geleistet haben“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:gvctzpv': {
    title: 'Schutz vor Armut durch die Regierung',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Regierung alle Bürger vor Armut schützt“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:grdfinc': {
    title: 'Maßnahmen der Regierung gegen Einkommensunterschiede',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Regierung Maßnahmen ergreift, um Einkommensunterschiede zu verringern“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:viepol': {
    title: 'Vorrang der Ansichten gewöhnlicher Menschen',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die Ansichten gewöhnlicher Menschen Vorrang vor den Ansichten der politischen Elite haben“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:wpestop': {
    title: 'Durchsetzung des Volkswillens',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass sich der Wille des Volkes immer durchsetzt“',
    },
    context: DEMOCRACY_CONTEXT,
  },
  'ESS10SCe03_2:keydec': {
    title: 'Wichtigste Entscheidungen durch nationale Regierungen',
    statement: {
      form: 'scale',
      subject:
        'Wichtigkeit für die Demokratie im Allgemeinen, „dass die wichtigsten Entscheidungen von den nationalen Regierungen getroffen werden und nicht von der Europäischen Union“',
    },
    context: `${DEMOCRACY_CONTEXT} Die Frage gehört zum Demokratieblock und steht im Profil unter europäischer Integration.`,
  },
  'ESS10SCe03_2:scchpldm': {
    title: 'Regierung und Mehrheitsmeinung',
    statement: {
      form: 'label',
      subject:
        'Am besten für die Demokratie im Allgemeinen, wenn die Regierung anderer Meinung ist als die große Mehrheit der Bevölkerung',
    },
    context:
      'Wahl zwischen zwei Aussagen. Die Folgefragen des Originalfragebogens (B26–B29) fehlen in diesem Entwurf.',
  },
  'ESS5e03_6:bplcdc': {
    title: 'Pflicht, Entscheidungen der Polizei zu akzeptieren',
    statement: {
      form: 'scale',
      subject:
        'Eigene Pflicht, die Entscheidungen der Polizei zu akzeptieren, auch wenn man damit nicht einverstanden ist',
    },
    context:
      'Eigene Pflicht gegenüber der Polizei in Deutschland, auch bei fehlendem Einverständnis.',
  },
  'ESS5e03_6:dpcstrb': {
    title: 'Pflicht, Anweisungen der Polizei zu folgen',
    statement: {
      form: 'scale',
      subject:
        'Eigene Pflicht, zu tun, was die Polizei sagt, auch wenn man die Art der Behandlung durch die Polizei nicht gut findet',
    },
    context:
      'Eigene Pflicht gegenüber der Polizei in Deutschland, auch bei missbilligter Behandlung.',
  },
  'ESS5e03_6:hrshsnta': {
    title: 'Härtere Strafen',
    statement: {
      form: 'agreement',
      statement:
        'Menschen, die das Gesetz brechen, sollten viel härter bestraft werden, als sie heute bestraft werden.',
    },
    context:
      '„Heute“ bezieht sich bei der eigenen Antwort auf die Gegenwart. Bei den ESS-Befragten bezog es sich auf die Strafpraxis zur Feldzeit 2010/11.',
    directions: AGREE,
  },
  'ESS5e03_6:dbctvrd': {
    title: 'Pflicht, Gerichtsurteile zu akzeptieren',
    statement: {
      form: 'agreement',
      statement: 'Alle haben die Pflicht, ein abschließendes Gerichtsurteil zu akzeptieren.',
    },
    context: 'Allgemeine Pflicht gegenüber abschließenden Gerichtsurteilen.',
    directions: AGREE,
  },
  'ESS5e03_6:lwstrob': {
    title: 'Strikte Befolgung aller Gesetze',
    statement: { form: 'agreement', statement: 'Alle Gesetze müssen strikt befolgt werden.' },
    context: 'Allgemeine Regel ohne Ausnahme.',
    directions: AGREE,
  },
  'ESS5e03_6:rgbrklw': {
    title: 'Gesetzesbruch, um das Richtige zu tun',
    statement: {
      form: 'agreement',
      statement: 'Manchmal muss man das Gesetz brechen, um das Richtige zu tun.',
    },
    context: 'Ausnahmefall („manchmal“).',
    directions: AGREE,
  },
  'ESS10SCe03_2:vteurmmb': {
    title: 'Volksabstimmung über die EU-Mitgliedschaft',
    statement: {
      form: 'label',
      subject:
        'Hypothetische Volksabstimmung über die Mitgliedschaft Deutschlands in der Europäischen Union',
    },
    context:
      'Hypothetische Abstimmung „morgen“. Leere oder ungültige Stimmzettel, Nichtwahl und fehlendes Stimmrecht sind eigene Antworten.',
  },
  'ESS11e04_2:euftf': {
    title: 'Richtung der europäischen Einigung',
    statement: { form: 'bipolar', subject: 'Europäische Einigung' },
    context:
      'Skala zwischen zwei Aussagen. „Schon jetzt“ bezieht sich auf den Zeitpunkt der Antwort.',
  },
  'ESS8e02_3:inctxff': {
    title: 'Höhere Abgaben auf fossile Brennstoffe',
    statement: {
      form: 'support-noun',
      nounPhrase: 'die Erhöhung der Abgaben auf fossile Brennstoffe wie Öl, Gas und Kohle',
    },
    context: CLIMATE_CONTEXT,
    directions: FOR_FIRST,
  },
  'ESS8e02_3:sbsrnen': {
    title: 'Förderung erneuerbarer Energien',
    statement: {
      form: 'support-noun',
      nounPhrase:
        'die Verwendung öffentlicher Gelder zur Förderung erneuerbarer Energiequellen wie Wind- oder Sonnenenergie',
    },
    context: CLIMATE_CONTEXT,
    directions: FOR_FIRST,
  },
  'ESS8e02_3:banhhap': {
    title: 'Verkaufsverbot für ineffiziente Haushaltsgeräte',
    statement: {
      form: 'support-noun',
      nounPhrase:
        'ein gesetzliches Verbot für den Verkauf von Haushaltgeräten mit der schlechtesten Energieeffizienz',
    },
    context: CLIMATE_CONTEXT,
    directions: FOR_FIRST,
  },
  'ESS10SCe03_2:imsmetn': {
    title: 'Menschen derselben Volksgruppe wie die Mehrheit',
    statement: {
      form: 'label',
      subject:
        'Zuwanderung von Menschen derselben „Volksgruppe oder ethnischen Gruppe“ wie die Mehrheit der Deutschen',
    },
    context: ADMISSION_CONTEXT,
  },
  'ESS10SCe03_2:imdfetn': {
    title: 'Menschen einer anderen Volksgruppe als die Mehrheit',
    statement: {
      form: 'label',
      subject:
        'Zuwanderung von Menschen einer anderen „Volksgruppe oder ethnischen Gruppe“ als die Mehrheit der Deutschen',
    },
    context: ADMISSION_CONTEXT,
  },
  'ESS10SCe03_2:impcntr': {
    title: 'Menschen aus ärmeren Ländern außerhalb Europas',
    statement: {
      form: 'label',
      subject: 'Zuwanderung von Menschen aus den ärmeren Ländern außerhalb Europas',
    },
    context: ADMISSION_CONTEXT,
  },
  'ESS8e02_3:imsclbn': {
    title: 'Gleiche Rechte auf Sozialleistungen für Zugewanderte',
    statement: {
      form: 'label',
      subject:
        'Zeitpunkt gleicher Rechte auf Sozialleistungen für Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben',
    },
    context:
      'Bedingung für gleiche Rechte auf Sozialleistungen. Die Antwortmöglichkeiten nennen Zeitpunkte und Bedingungen.',
  },
  'ESS11e04_2:eqparep': {
    title: 'Gesetz zur gleichen Sitzverteilung im Bundestag',
    statement: {
      form: 'support-noun',
      nounPhrase:
        'ein Gesetz, welches eine gleiche Verteilung der Sitze im Bundestag zwischen Frauen und Männern vorschreibt',
    },
    context: 'Gesetzliche Vorgabe als Mittel.',
    directions: FOR_FIRST,
  },
  'ESS11e04_2:eqparlv': {
    title: 'Gesetzlich gleich lange Elternzeit',
    statement: {
      form: 'support-noun',
      nounPhrase:
        'ein Gesetz, welches beiden Elternteilen vorschreibt, gleich lange bezahlte Elternzeit zu nehmen, um ihr Kind zu betreuen',
    },
    context:
      'Gesetzliche Pflicht für beide Eltern. Die Frage beschreibt ein Paar, bei dem beide Vollzeit arbeiten und ungefähr gleich viel verdienen.',
    directions: FOR_FIRST,
  },
  'ESS11e04_2:freinsw': {
    title: 'Kündigung nach beleidigenden Bemerkungen gegenüber Frauen',
    statement: {
      form: 'support-clause',
      clause:
        'dass Mitarbeitenden gekündigt wird, die bei der Arbeit Frauen gegenüber beleidigende Bemerkungen machen',
    },
    context: 'Kündigung als Folge.',
    directions: FOR_FIRST,
  },
  'ESS11e04_2:fineqpy': {
    title: 'Geldstrafe bei ungleicher Bezahlung',
    statement: {
      form: 'support-clause',
      clause:
        'dass Unternehmen eine Geldstrafe zahlen müssen, wenn sie Männer für die gleiche Arbeit besser bezahlen als Frauen',
    },
    context: 'Geldstrafe für Unternehmen als Mittel.',
    directions: FOR_FIRST,
  },
  'ESS8e02_3:elgcoal': {
    title: 'Kohle',
    statement: { form: 'label', subject: 'Strom aus Kohle' },
    context: ELECTRICITY_CONTEXT,
  },
  'ESS8e02_3:elgngas': {
    title: 'Erdgas',
    statement: { form: 'label', subject: 'Strom aus Erdgas' },
    context: ELECTRICITY_CONTEXT,
  },
  'ESS8e02_3:elghydr': {
    title: 'Wasserkraft',
    statement: { form: 'label', subject: 'Strom aus Wasserkraft' },
    context: ELECTRICITY_CONTEXT,
  },
  'ESS8e02_3:elgnuc': {
    title: 'Atom- bzw. Kernkraft',
    statement: { form: 'label', subject: 'Strom aus Atom- bzw. Kernkraft' },
    context: `${ELECTRICITY_CONTEXT} Der Leistungsbetrieb der Kernkraftwerke in Deutschland endete im April 2023 (§ 7 Abs. 1e Atomgesetz).`,
  },
  'ESS8e02_3:elgsun': {
    title: 'Sonnenenergie',
    statement: { form: 'label', subject: 'Strom aus Sonnenenergie' },
    context: ELECTRICITY_CONTEXT,
  },
  'ESS8e02_3:elgwind': {
    title: 'Windkraft',
    statement: { form: 'label', subject: 'Strom aus Windkraft' },
    context: ELECTRICITY_CONTEXT,
  },
  'ESS8e02_3:elgbio': {
    title: 'Biomasse',
    statement: { form: 'label', subject: 'Strom aus Biomasse wie Holz, Pflanzen oder Tiermist' },
    context: ELECTRICITY_CONTEXT,
  },
  'ESS8e02_3:gvrfgap': {
    title: 'Großzügige Prüfung von Asylanträgen',
    statement: {
      form: 'agreement',
      statement: 'Bei der Prüfung von Asylanträgen sollte der Staat großzügig sein.',
    },
    context:
      'Asylanträge von Menschen, die Angst vor Verfolgung in ihrem Land haben. Erhoben 2016/17.',
    directions: AGREE,
  },
  'ESS8e02_3:rfgbfml': {
    title: 'Familiennachzug anerkannter Asylsuchender',
    statement: {
      form: 'agreement',
      statement:
        'Asylbewerber, deren Anträge bewilligt wurden, sollten das Recht haben, ihre engen Familienangehörigen nach Deutschland zu holen.',
    },
    context: 'Erhoben 2016/17. Die Frage unterscheidet nicht nach Schutzstatus.',
    directions: AGREE,
  },
  'ESS8e02_3:basinc': {
    title: 'Grundeinkommen',
    statement: {
      form: 'support-noun',
      nounPhrase: 'ein solches Grundeinkommen in Deutschland',
    },
    context:
      'Grundeinkommen mit allen sechs Merkmalen der Originalliste, darunter der Ersatz vieler bestehender Sozialleistungen und die Finanzierung über Steuern. Eine mittlere Antwort war nicht vorgesehen.',
    directions: AGAINST_FIRST,
  },
  'ESS8e02_3:eusclbf': {
    title: 'EU-weites Sozialleistungsprogramm',
    statement: {
      form: 'support-noun',
      nounPhrase: 'ein solches EU-weites Sozialleistungsprogramm',
    },
    context:
      'Programm mit allen drei Merkmalen der Originalliste, darunter höhere Beiträge reicherer EU-Länder. Eine mittlere Antwort war nicht vorgesehen.',
    directions: AGAINST_FIRST,
  },
  'ESS10SCe03_2:panpriph': {
    title: 'Pandemie: Gesundheit oder Wirtschaft',
    statement: {
      form: 'bipolar',
      subject: 'Bei der Bekämpfung einer Pandemie vorrangig zu berücksichtigen',
    },
    context: ESS10_PANDEMIC_CONTEXT,
  },
  'ESS10SCe03_2:panmonpb': {
    title: 'Pandemie: Überwachung oder Privatsphäre',
    statement: {
      form: 'bipolar',
      subject: 'Bei der Bekämpfung einer Pandemie wichtiger',
    },
    context: ESS10_PANDEMIC_CONTEXT,
  },
  'ESS8e02_3:mnrgtjb': {
    title: 'Vorrang von Männern bei knappen Arbeitsplätzen',
    statement: {
      form: 'agreement',
      statement:
        'Wenn Arbeitsplätze knapp sind, sollten Männer eher einen Anspruch auf einen Arbeitsplatz haben als Frauen.',
    },
    context: 'Allgemeine Aussage über Ansprüche auf Arbeitsplätze. Erhoben 2016/17.',
    directions: AGREE,
  },
  'ESS10SCe03_2:freehms': {
    title: 'Freie Lebensführung von Schwulen und Lesben',
    statement: {
      form: 'agreement',
      statement: 'Schwule und Lesben sollten ihr Leben so führen dürfen, wie sie es wollen.',
    },
    context: 'Allgemeines Prinzip. Erhoben 2021/22.',
    directions: AGREE,
  },
  'ESS10SCe03_2:hmsacld': {
    title: 'Gleiches Adoptionsrecht gleichgeschlechtlicher Paare',
    statement: {
      form: 'agreement',
      statement:
        'Schwule und lesbische Paare sollten die gleichen Rechte haben, Kinder zu adoptieren, wie Paare, die aus Mann und Frau bestehen.',
    },
    context: 'Erhoben 2021/22, nach der Eheöffnung für gleichgeschlechtliche Paare im Jahr 2017.',
    directions: AGREE,
  },
  'ESS10SCe03_2:accalaw': {
    title: 'Starke Führungsperson über dem Gesetz',
    statement: {
      form: 'scale',
      subject: 'Akzeptanz einer starken Führungsperson für Deutschland, die über dem Gesetz steht',
    },
    context: 'Wie akzeptabel diese Vorstellung wäre. Erhoben 2021/22.',
  },
  'ESS10SCe03_2:loylead': {
    title: 'Loyalität gegenüber der politischen Führung',
    statement: {
      form: 'agreement',
      statement:
        'Was Deutschland am meisten braucht, ist Loyalität gegenüber der politischen Führung.',
    },
    context: 'Allgemeine Aussage über Deutschland. Erhoben 2021/22.',
    directions: AGREE,
  },
  'ESS5e03_6:prtyban': {
    title: 'Verbot demokratiefeindlicher Parteien',
    statement: {
      form: 'agreement',
      statement:
        'Politische Parteien, die die Demokratie abschaffen wollen, sollten verboten werden',
    },
    context: 'Allgemeine Aussage, keine bestimmte Partei. Erhoben 2010/11.',
    directions: AGREE,
  },
});
