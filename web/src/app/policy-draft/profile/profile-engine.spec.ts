import { POLICY_DRAFT_ITEMS, POLICY_RUBRICS } from '../policy-catalogue';
import {
  buildAnswerProfile,
  ProfileInputError,
  ruleItemIds,
  type AnswerProfile,
  type ProfileAnswer,
} from './profile-engine';
import { BLOCK_RULES, CROSS_REFERENCE_RULES } from './profile-structure';

// Synthetic technical answer combinations (Profilregeln v1, T01–T30).
// They test computation and wording limits. They are not empirical persons.

const ITEMS = POLICY_DRAFT_ITEMS.map((item) => ({
  id: item.id,
  primaryTheme: item.primaryTheme,
  categories: item.categories.map((category) => ({
    code: category.code,
    labelDe: category.labelDe,
  })),
}));

const FORBIDDEN_WORDS = [
  'links',
  'rechts',
  'liberal',
  'konservativ',
  'progressiv',
  'libertär',
  'autoritär',
  'populistisch',
  'etatistisch',
  'marktliberal',
  'euroskeptisch',
  'nationalistisch',
  'feministisch',
  'solidarisch',
  'streng',
  'tolerant',
  'rechtstreu',
  'punitiv',
  'neutral',
  'gemäßigt',
  'ambivalent',
  'unentschlossen',
  'inkonsistent',
  'widersprüchlich',
  'typisch',
  'ungewöhnlich',
  'Mehrheitsmeinung',
];
const FORBIDDEN = new RegExp(`(?<!\\p{L})(?:${FORBIDDEN_WORDS.join('|')})(?!\\p{L})`, 'iu');

/** Own wording only: quoted original text is excluded from address checks. */
function ownWording(text: string): string {
  return text.replace(/„[^“]*“/g, '');
}

function id(variable: string): string {
  const item = POLICY_DRAFT_ITEMS.find((entry) => entry.variable === variable);
  if (!item) throw new Error(`unknown variable ${variable}`);
  return item.id;
}

function answers(
  codes: Readonly<Record<string, string>> = {},
  skipped: readonly string[] = [],
): Map<string, ProfileAnswer> {
  const map = new Map<string, ProfileAnswer>();
  for (const item of ITEMS) map.set(item.id, { status: 'untouched' });
  for (const variable of skipped) map.set(id(variable), { status: 'skipped' });
  for (const [variable, code] of Object.entries(codes)) {
    map.set(id(variable), { status: 'answered', code });
  }
  return map;
}

function profile(codes: Readonly<Record<string, string>> = {}, skipped: readonly string[] = []) {
  return buildAnswerProfile(ITEMS, POLICY_RUBRICS, answers(codes, skipped));
}

function allText(result: AnswerProfile): string {
  return [
    ...result.areas.flatMap((area) => [
      ...area.statements.flatMap((statement) => [statement.text, statement.context]),
      ...area.blocks.flatMap((block) => [...block.sentences, block.note]),
    ]),
    ...result.crossReferences.flatMap((entry) => [
      entry.context,
      ...entry.answers.map((answer) => answer.answer),
    ]),
  ].join('\n');
}

function statement(result: AnswerProfile, variable: string) {
  return result.areas
    .flatMap((area) => area.statements)
    .find((entry) => entry.itemId === id(variable));
}

function block(result: AnswerProfile, blockId: string) {
  return result.areas.flatMap((area) => area.blocks).find((entry) => entry.blockId === blockId);
}

describe('descriptive answer profile', () => {
  it('has exactly one rule for every catalogue question and valid block members', () => {
    expect([...ruleItemIds()].sort()).toEqual(ITEMS.map((item) => item.id).sort());
    const ids = new Set(ITEMS.map((item) => item.id));
    for (const rule of [...BLOCK_RULES, ...CROSS_REFERENCE_RULES]) {
      for (const itemId of rule.itemIds) expect(ids.has(itemId)).toBe(true);
    }
  });

  it('T01/T03: without substantive answers it states nothing about the person', () => {
    const untouched = profile();
    const skipped = profile(
      {},
      POLICY_DRAFT_ITEMS.map((item) => item.variable),
    );
    for (const result of [untouched, skipped]) {
      expect(result.answered).toBe(0);
      expect(result.areas.every((area) => area.statements.length === 0)).toBe(true);
      expect(result.areas.every((area) => area.blocks.length === 0)).toBe(true);
      expect(result.crossReferences).toEqual([]);
      expect(result.withoutAnswer.length).toBe(ITEMS.length);
    }
    expect(skipped.withoutAnswer.every((entry) => entry.status === 'skipped')).toBe(true);
  });

  it('T02: middle categories are reported literally and the middle note is flagged once', () => {
    const codes: Record<string, string> = {};
    for (const item of POLICY_DRAFT_ITEMS) {
      if (item.categories.length === 5 && item.responseType !== 'nominal')
        codes[item.variable] = '3';
      if (item.categories.length === 11) codes[item.variable] = '5';
    }
    const result = profile(codes);
    expect(result.usesMiddleCategory).toBe(true);
    expect(statement(result, 'sofrdst')!.text).toMatch(
      /^Weder Zustimmung noch Ablehnung zur Aussage/,
    );
    expect(statement(result, 'inctxff')!.text).toMatch(/^Weder für noch gegen /);
    expect(statement(result, 'gvslvol')!.text).toContain(': 5 (0 = ');
    expect(statement(result, 'euftf')!.text).toContain('gleicher Abstand');
    expect(allText(result)).not.toMatch(FORBIDDEN);
  });

  it('T04: code 1 means opposite directions in different answer lists', () => {
    const result = profile({ bnlwinc: '1', inctxff: '1', imsmetn: '1', sofrdst: '1' });
    expect(statement(result, 'bnlwinc')!.text).toMatch(/^Dagegen, dass nur noch/);
    expect(statement(result, 'bnlwinc')!.direction).toBe('negative');
    expect(statement(result, 'inctxff')!.text).toMatch(/^Für die Erhöhung/);
    expect(statement(result, 'inctxff')!.direction).toBe('positive');
    expect(statement(result, 'imsmetn')!.text).toContain(
      '„Vielen erlauben, herzukommen und hier zu leben“',
    );
    expect(statement(result, 'sofrdst')!.text).toMatch(/^Zustimmung zur Aussage/);
  });

  it('T05/T06: endpoints use the original anchors without counting extremes', () => {
    const low = profile({ gvslvol: '0', euftf: '0' });
    expect(statement(low, 'gvslvol')!.text).toContain(
      '0 (0 = „Der Staat sollte dafür überhaupt nicht verantwortlich sein“',
    );
    expect(statement(low, 'euftf')!.text).toBe(
      'Europäische Einigung: 0 („Einigung ist schon zu weit gegangen“).',
    );
    const codes: Record<string, string> = {};
    for (const variable of ['fairelc', 'dfprtal', 'medcrgv', 'rghmgpr', 'votedir']) {
      codes[variable] = '10';
    }
    const high = profile(codes);
    expect(block(high, 'democracy_norms')!.sentences).toEqual([
      'Alle beantworteten Fragen dieses Blocks erhielten denselben Wert: 10.',
    ]);
  });

  it('T07/T08: several justice principles are listed without a dominant type', () => {
    const result = profile({ sofrdst: '1', sofrwrk: '1', sofrpr: '5', sofrprv: '5' });
    expect(block(result, 'justice_principles')!.sentences).toEqual([
      'Zustimmung: Gleichheit und Leistung.',
      'Ablehnung: Bedarf und Anrecht durch Herkunft.',
    ]);
    expect(block(result, 'justice_principles')!.note).toContain('kein Widerspruch');
    const two = profile({ sofrdst: '1', sofrprv: '1' });
    expect(block(two, 'justice_principles')!.sentences).toEqual([
      'Alle beantworteten Fragen dieses Blocks: Zustimmung.',
    ]);
    expect(block(two, 'justice_principles')!.unansweredItemIds.length).toBe(2);
  });

  it('T09/T10: scale blocks report equal or different values without an average', () => {
    const different = profile({ gvslvol: '10', gvslvue: '0', gvcldcr: '5' });
    expect(block(different, 'state_responsibility')!.sentences).toEqual([
      'Die Werte unterscheiden sich: Lebensstandard im Alter 10, Lebensstandard bei Arbeitslosigkeit 0, Kinderbetreuung für berufstätige Eltern 5.',
      'Höchster Wert (10): Lebensstandard im Alter.',
      'Niedrigster Wert (0): Lebensstandard bei Arbeitslosigkeit.',
    ]);
    const equal = profile({ gvslvol: '7', gvslvue: '7', gvcldcr: '7' });
    expect(block(equal, 'state_responsibility')!.sentences).toEqual([
      'Alle beantworteten Fragen dieses Blocks erhielten denselben Wert: 7.',
    ]);
    expect(allText(equal)).not.toMatch(/eher hoch|Mittelwert|Durchschnitt/);
  });

  it('T11: the welfare reform questions get no block statement', () => {
    const result = profile({ bnlwinc: '4', eduunmp: '1', wrkprbf: '4' });
    const ids = result.areas.flatMap((area) => area.blocks.flatMap((entry) => entry.itemIds));
    expect(ids).not.toContain(id('bnlwinc'));
    expect(statement(result, 'eduunmp')!.context).toContain('feste Geldsumme');
  });

  it('T12/T25: cross-references need two answers and never compute a direction', () => {
    const result = profile({ sofrdst: '1', gincdif: '5', grdfinc: '8' });
    const entry = result.crossReferences.find((cross) => cross.id === 'income_differences')!;
    expect(entry.answers.map((answer) => answer.answer)).toEqual([
      '„Stimme stark zu“',
      '„Lehne stark ab“',
      '8 von 10',
    ]);
    expect(allText(result)).not.toMatch(FORBIDDEN);
    const single = profile({ sofrdst: '1' });
    expect(single.crossReferences).toEqual([]);
  });

  it('T13: the democracy block names highest and lowest values, including ties', () => {
    const result = profile({
      votedir: '10',
      viepol: '10',
      wpestop: '10',
      rghmgpr: '2',
      cttresa: '2',
    });
    const sentences = block(result, 'democracy_norms')!.sentences;
    expect(sentences[1]).toBe(
      'Höchster Wert (10): Letztes Wort durch Volksabstimmungen, Vorrang der Ansichten gewöhnlicher Menschen und Durchsetzung des Volkswillens.',
    );
    expect(sentences[2]).toBe(
      'Niedrigster Wert (2): Schutz der Rechte von Minderheiten und Gleichbehandlung durch Gerichte.',
    );
    expect(allText(result)).not.toMatch(FORBIDDEN);
  });

  it('T15/T16: police and law answers keep their occasion and time reference', () => {
    const result = profile({
      bplcdc: '10',
      dpcstrb: '0',
      hrshsnta: '1',
      lwstrob: '1',
      rgbrklw: '1',
    });
    expect(block(result, 'police_obligation')!.note).toContain('Anlass');
    expect(statement(result, 'hrshsnta')!.context).toContain('2010/11');
    expect(block(result, 'law_obligation')!.itemIds).not.toContain(id('hrshsnta'));
    expect(block(result, 'law_obligation')!.note).toContain('Ausnahmefall');
    expect(allText(result)).not.toMatch(FORBIDDEN);
  });

  it('T17/T18: EU non-position answers are their own answers', () => {
    const result = profile({ vteurmmb: '55', keydec: '10', euftf: '10' });
    expect(statement(result, 'vteurmmb')!.text).toContain('„Würde nicht wählen“');
    expect(statement(result, 'vteurmmb')!.direction).toBeNull();
    const ineligible = profile({ vteurmmb: '65' });
    expect(statement(ineligible, 'vteurmmb')!.text).toContain('„Nicht stimmberechtigt“');
  });

  it('T19/T20: admission answers compare groups only by the chosen labels', () => {
    const result = profile({ imsmetn: '1', imdfetn: '4', impcntr: '4' });
    expect(block(result, 'migration_admission')!.sentences).toContain(
      'Für Menschen derselben Volksgruppe wie die Mehrheit wurde mehr Zuwanderung erlaubt als für Menschen einer anderen Volksgruppe als die Mehrheit.',
    );
    const same = profile({ imsmetn: '2', imdfetn: '2', impcntr: '2' });
    expect(block(same, 'migration_admission')!.sentences).toEqual([
      'Für alle beantworteten Gruppen dieselbe Antwort: „Einigen erlauben“.',
    ]);
  });

  it('T21/T22/T23: single measures stay single statements with their means', () => {
    const result = profile({
      imsclbn: '5',
      inctxff: '5',
      sbsrnen: '1',
      banhhap: '3',
      eqparep: '1',
      fineqpy: '5',
    });
    expect(statement(result, 'imsclbn')!.text).toBe(
      'Zeitpunkt gleicher Rechte auf Sozialleistungen für Menschen, die aus anderen Ländern nach Deutschland kommen, um hier zu leben: „Sie sollten niemals die gleichen Rechte bekommen.“',
    );
    expect(block(result, 'climate_measures')!.sentences).toEqual([
      'Dafür: Förderung erneuerbarer Energien.',
      'Weder dafür noch dagegen: Verkaufsverbot für ineffiziente Haushaltsgeräte.',
      'Dagegen: Höhere Abgaben auf fossile Brennstoffe.',
    ]);
    expect(block(result, 'gender_policy_measures')!.note).toContain('Ziel der Gleichstellung');
    expect(allText(result)).not.toMatch(FORBIDDEN);
  });

  it('T24: one answered area gives statements only for that area', () => {
    const result = profile({ inctxff: '2', sbsrnen: '2' });
    const answeredAreas = result.areas.filter((area) => area.answered > 0);
    expect(answeredAreas.map((area) => area.areaId)).toEqual(['climate_energy']);
    expect(result.crossReferences).toEqual([]);
  });

  it('T26: invalid codes are rejected instead of recoded', () => {
    expect(() => profile({ sofrdst: '6' })).toThrow(ProfileInputError);
    expect(() => profile({ gvslvol: '11' })).toThrow(ProfileInputError);
    expect(() => profile({ imsmetn: '9' })).toThrow(ProfileInputError);
    expect(() => profile({ scchpldm: '3' })).toThrow(ProfileInputError);
  });

  it('T27: the same answers in a different order give the same profile', () => {
    const first = answers({ sofrdst: '2', gvslvol: '8', euftf: '3', imsmetn: '2' });
    const reordered = new Map([...first.entries()].reverse());
    expect(buildAnswerProfile(ITEMS, POLICY_RUBRICS, reordered)).toEqual(
      buildAnswerProfile(ITEMS, POLICY_RUBRICS, first),
    );
  });

  it('T28/T29: a single directed answer is not turned into an area direction', () => {
    const result = profile({ inctxff: '3', sbsrnen: '1' });
    expect(block(result, 'climate_measures')!.sentences).toEqual([
      'Dafür: Förderung erneuerbarer Energien.',
      'Weder dafür noch dagegen: Höhere Abgaben auf fossile Brennstoffe.',
    ]);
    const strong: Record<string, string> = {};
    for (const variable of ['sofrdst', 'sofrwrk', 'gincdif', 'lwstrob']) strong[variable] = '1';
    expect(allText(profile(strong))).not.toMatch(/Tendenz|Antwortstil/);
  });

  it('T14: a cross-reference across answer formats lists answers without computing', () => {
    const result = profile({ scchpldm: '1', wpestop: '0' });
    const entry = result.crossReferences.find((cross) => cross.id === 'majority_will')!;
    expect(entry.answers.map((answer) => answer.answer)).toEqual([
      '0 von 10',
      '„Die Regierung sollte ihre Pläne ändern und darauf reagieren, was die große Mehrheit der Bevölkerung denkt.“',
    ]);
    expect(entry.context).toContain('nicht verrechnen');
  });

  it('v2.2 blocks: energy sources are grouped by chosen amount in list order', () => {
    const result = profile({ elgcoal: '5', elgnuc: '5', elgsun: '1', elgwind: '1', elgngas: '3' });
    expect(block(result, 'electricity_sources')!.sentences).toEqual([
      '„Eine sehr große Menge“: Sonnenenergie und Windkraft.',
      '„Eine mittelgroße Menge“: Erdgas.',
      '„Überhaupt nichts“: Kohle und Atom- bzw. Kernkraft.',
    ]);
    expect(statement(result, 'elgnuc')!.context).toContain('April 2023');
    const same = profile({ elgcoal: '3', elgbio: '3' });
    expect(block(same, 'electricity_sources')!.sentences).toEqual([
      'Alle beantworteten Fragen dieses Blocks: „Eine mittelgroße Menge“.',
    ]);
  });

  it('v2.2 blocks: asylum and same-sex couples list directions without labels', () => {
    const result = profile({ gvrfgap: '1', rfgbfml: '4', freehms: '2', hmsacld: '3' });
    expect(block(result, 'asylum')!.sentences).toEqual([
      'Zustimmung: Großzügige Prüfung von Asylanträgen.',
      'Ablehnung: Familiennachzug anerkannter Asylsuchender.',
    ]);
    expect(block(result, 'same_sex_couples')!.sentences).toEqual([
      'Zustimmung: Freie Lebensführung von Schwulen und Lesben.',
      'Weder Zustimmung noch Ablehnung: Gleiches Adoptionsrecht gleichgeschlechtlicher Paare.',
    ]);
    expect(allText(result)).not.toMatch(FORBIDDEN);
  });

  it('v2.2 cross-reference: social protection leaves a means test unspecified', () => {
    const result = profile({ sofrpr: '1', basinc: '4' });
    const entry = result.crossReferences.find((cross) => cross.id === 'social_protection')!;
    expect(entry.answers).toHaveLength(2);
    expect(entry.context).toContain('Ob eine Bedürftigkeit geprüft wird, legen');
    expect(entry.context).not.toContain('ohne Bedürftigkeitsprüfung');
    expect(statement(result, 'basinc')!.text).toBe(
      'Für ein solches Grundeinkommen in Deutschland (gewählt: „Sehr dafür“).',
    );
  });

  it('every offered category of every question yields a sentence without forbidden labels', () => {
    for (const item of POLICY_DRAFT_ITEMS) {
      for (const category of item.offeredCategories) {
        const result = profile({ [item.variable]: category.code });
        const text = statement(result, item.variable)!.text;
        expect(text.length).toBeGreaterThan(10);
        expect(text).not.toMatch(FORBIDDEN);
        expect(ownWording(text)).not.toMatch(/(?<!\p{L})(?:Sie|du|dein\p{L}*|Ihr\p{L}*)(?!\p{L})/u);
      }
    }
  });
});
