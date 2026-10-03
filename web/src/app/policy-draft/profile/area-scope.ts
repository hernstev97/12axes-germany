/**
 * Reach of each area, taken from docs/abdeckung-v2.2.md. An area orders questions
 * for reading. It is not a measurement dimension and receives no value.
 */
export interface AreaScope {
  readonly id: string;
  readonly title: string;
  readonly covered: string;
  readonly notCovered: string;
}

/** Areas with questions in the profile (primary themes). */
export const AREA_SCOPES: readonly AreaScope[] = Object.freeze([
  {
    id: 'economy_distribution',
    title: 'Wirtschaft und Verteilung',
    covered:
      'Vier Gerechtigkeitsprinzipien (ESS9, 2018/19) und staatliche Maßnahmen gegen Einkommensunterschiede (ESS11, 2023).',
    notCovered:
      'Steuern, Schuldenbremse, Marktordnung und Regulierung, Industrie- und Handelspolitik, Mindestlohn, Arbeitszeit.',
  },
  {
    id: 'welfare',
    title: 'Sozialstaat',
    covered:
      'Staatliche Verantwortung für Alter, Arbeitslosigkeit und Kinderbetreuung, Zielgruppen und Umschichtung von Leistungen, Grundeinkommen (ESS8, 2016/17).',
    notCovered: 'Bürgergeld, Sanktionen und Leistungshöhe, Finanzierung, Rente im Einzelnen.',
  },
  {
    id: 'democracy_authority',
    title: 'Demokratie und politische Autorität',
    covered:
      'Wichtigkeit von elf Demokratiemerkmalen, Regierung und Mehrheitsmeinung, starke Führungsperson über dem Gesetz, Loyalität gegenüber der politischen Führung (ESS10, 2021/22). Verbot demokratiefeindlicher Parteien (ESS5, 2010/11).',
    notCovered:
      'Konkrete Reformen wie Wahlalter oder Volksentscheide auf Bundesebene, Gerichtskontrolle im Konfliktfall, Föderalismus.',
  },
  {
    id: 'rights_security',
    title: 'Bürgerrechte und Sicherheit',
    covered:
      'Pflichten gegenüber Polizei und Gesetz, härtere Strafen (ESS5, 2010/11). Pandemieabwägungen zwischen Gesundheit und Wirtschaft sowie zwischen Überwachung und Privatsphäre (ESS10, 2021/22).',
    notCovered:
      'Überwachung und Datenspeicherung außerhalb der Pandemie, Gesichtserkennung, Versammlungsrecht, Strafmündigkeit.',
  },
  {
    id: 'europe',
    title: 'Europäische Integration',
    covered:
      'Hypothetische Abstimmung über die Mitgliedschaft und nationale statt EU-Entscheidungen (ESS10), Richtung der Einigung (ESS11, 2023), EU-weites Sozialleistungsprogramm (ESS8, 2016/17).',
    notCovered:
      'Gemeinsame Politikfelder wie Verteidigung und Migration, Euro, Erweiterung, Finanzsolidarität.',
  },
  {
    id: 'climate_energy',
    title: 'Klima und Energie',
    covered:
      'Abgaben, Förderung und Verkaufsverbot gegen den Klimawandel sowie der gewünschte Anteil von sieben Energiequellen am Strom (ESS8, 2016/17).',
    notCovered: 'Gebäude und Heizung, Verkehr und Tempolimit, Klimaziele, Landwirtschaft.',
  },
  {
    id: 'migration',
    title: 'Migration',
    covered:
      'Zuwanderung nach Herkunftsgruppen (ESS10), gleiche Rechte auf Sozialleistungen, Prüfung von Asylanträgen und Familiennachzug (ESS8, 2016/17).',
    notCovered:
      'Grenzkontrollen und Zurückweisung, Rückführung, Integrationsanforderungen, Staatsangehörigkeit.',
  },
  {
    id: 'equality_family',
    title: 'Gleichstellungs- und Familienpolitik',
    covered:
      'Vier gesetzliche oder betriebliche Gleichstellungsmittel (ESS11, 2023), Leistungen für erwerbstätige Eltern (ESS8), freie Lebensführung von Schwulen und Lesben und gleiches Adoptionsrecht (ESS10, 2021/22).',
    notCovered:
      'Schwangerschaftsabbruch, Frauenquote in der Wirtschaft, geschlechtergerechte Sprache, Rechte von trans Personen.',
  },
]);

/** Areas without questions of their own; shown so the gaps stay visible. */
export const UNCOVERED_AREAS: readonly AreaScope[] = Object.freeze([
  {
    id: 'labour_pensions',
    title: 'Arbeit und Rente',
    covered: 'Nur indirekt über die staatliche Verantwortung im Alter und bei Arbeitslosigkeit.',
    notCovered:
      'Rentenniveau, Renteneintrittsalter, Rentenfinanzierung, Mindestlohn, Arbeitszeit, Tarifbindung und Streikrecht.',
  },
  {
    id: 'health_care',
    title: 'Gesundheit und Pflege',
    covered: 'Keine Frage.',
    notCovered:
      'Finanzierung der Krankenversicherung, Pflegeversicherung und Eigenanteile, Pflegekräfte, Krankenhausreform.',
  },
  {
    id: 'housing',
    title: 'Wohnen',
    covered: 'Keine Frage.',
    notCovered:
      'Mietregulierung, sozialer Wohnungsbau, Vergesellschaftung, Eigentumsförderung, Grundsteuer.',
  },
  {
    id: 'foreign_defence',
    title: 'Außen-, Verteidigungs- und Friedenspolitik',
    covered: 'Keine Frage.',
    notCovered:
      'Unterstützung der Ukraine, Verteidigungsausgaben, Wehrpflicht und Wehrdienst, Rüstungsexporte, NATO, Handelspolitik.',
  },
  {
    id: 'education_research',
    title: 'Bildung und Forschung',
    covered: 'Keine Frage.',
    notCovered:
      'Zuständigkeit von Bund und Ländern, BAföG, Studiengebühren, Kita- und Sprachtestpflicht, Schulstruktur, Forschungsausgaben.',
  },
  {
    id: 'media_digital',
    title: 'Medien und Digitalpolitik',
    covered: 'Nur das Recht der Medien auf Kritik an der Regierung als Demokratiemerkmal.',
    notCovered:
      'Rundfunkbeitrag, Plattformregulierung, Hassrede und Desinformation, IP-Adressen-Speicherung, Gesichtserkennung, KI-Regulierung.',
  },
]);
