import { PolicyProfileInputError, PolicyProfileSession } from '../research/policy-profile';
import { POLICY_DRAFT_ITEMS, POLICY_DRAFT_QUESTIONS, POLICY_RUBRICS } from './policy-catalogue';
import { PUBLIC_CATALOGUE } from './public-catalogue';
import { PUBLIC_CATALOGUE_V22 } from './public-catalogue-v22';

describe('Öffentliche Originalbindung des Angular-Entwurfs', () => {
  it('bietet die im Interview nicht vorgelesene Antwort zu Energiequellen nicht an', () => {
    for (const item of POLICY_DRAFT_ITEMS.filter(
      (entry) => entry.groupId === 'electricity_sources',
    )) {
      expect(item.categories.map((category) => category.code)).toContain('55');
      expect(item.offeredCategories.map((category) => category.code)).not.toContain('55');
      expect(item.question.categories).not.toContain('55');
    }
  });

  it('enthält die gepinnten 43 v2-Fragen und 18 v2.2-Fragen mit 428 ausdrücklich gebundenen Optionen', () => {
    expect(PUBLIC_CATALOGUE.catalogueSha256).toBe(
      '5fe6b93513151e07399840a3a9c1b6222be0fe90b6b98b0997e31dfde89422e4',
    );
    expect(PUBLIC_CATALOGUE_V22.items).toHaveLength(18);
    expect(POLICY_DRAFT_ITEMS).toHaveLength(61);
    expect(POLICY_DRAFT_ITEMS.filter((item) => item.addedInV22)).toHaveLength(18);
    expect(POLICY_DRAFT_ITEMS.reduce((count, item) => count + item.categories.length, 0)).toBe(428);
    expect(new Set(POLICY_DRAFT_ITEMS.map((item) => item.id)).size).toBe(61);
    for (const item of POLICY_DRAFT_ITEMS) {
      expect(item.categories.map((category) => category.code)).toEqual(item.apiValidCodeOrder);
      expect(
        item.categories.every(
          (category) => !category.isMissingApi && category.labelSourceRef.length > 0,
        ),
      ).toBe(true);
      expect(item.codeBinding.sourceFieldId.length).toBeGreaterThan(0);
    }
  });

  it('hält B1–B12 in Originalfolge zusammen und ordnet B12 erst im Ergebnis primär der EU zu', () => {
    const first = POLICY_DRAFT_ITEMS.findIndex((item) => item.originalQuestionId === 'B1');
    const block = POLICY_DRAFT_ITEMS.slice(first, first + 12);
    expect(block.map((item) => item.originalQuestionId)).toEqual([
      'B1',
      'B2',
      'B3',
      'B4',
      'B5',
      'B6',
      'B7',
      'B8',
      'B9',
      'B10',
      'B11',
      'B12',
    ]);
    expect(block.at(-1)!.primaryTheme).toBe('europe');
    expect(block[0]!.introductionsDe[0]).toContain('Nachher werden wir Sie fragen');
    expect(block.at(-1)!.developmentNote).toContain('B13–B24 fehlen');
    const next = POLICY_DRAFT_ITEMS[first + 12]!;
    expect(next.originalQuestionId).toBe('B25');
    expect(next.developmentNote).toContain('B26 oder B28');
    expect(next.developmentNote).toContain('B26–B29 aus');
    expect(POLICY_RUBRICS).toHaveLength(8);
  });

  it('bindet Druckcodes an Exportcodes und weist echte Missing-Codes als Antwort zurück', () => {
    const item = POLICY_DRAFT_ITEMS.find((entry) => entry.variable === 'euftf')!;
    expect(item.categories[0]).toMatchObject({ printedCodeDe: '00', code: '0' });
    expect(item.categories[1]).toMatchObject({ printedCodeDe: '01', code: '1' });
    const session = new PolicyProfileSession(POLICY_DRAFT_QUESTIONS);
    session.answer(item.id, '9');
    expect(session.getAnswer(item.id)).toEqual({ status: 'answered', code: '9' });
    expect(() => session.answer(item.id, '09')).toThrow(PolicyProfileInputError);
    expect(() => session.answer(item.id, '88')).toThrow(PolicyProfileInputError);
    expect(session.getAnswer(item.id)).toEqual({ status: 'answered', code: '9' });
  });

  it('behält die nominalen EU-Kategorien und das vollständige Elternzeitszenario', () => {
    const referendum = POLICY_DRAFT_ITEMS.find((item) => item.variable === 'vteurmmb')!;
    expect(referendum.categories.slice(2).map((category) => category.semanticRole)).toEqual([
      'blank_ballot',
      'invalid_ballot',
      'non_voting',
      'ineligibility',
    ]);
    const parentalLeave = POLICY_DRAFT_ITEMS.find((item) => item.variable === 'eqparlv')!;
    expect(parentalLeave.situationDe).toContain(
      'beide Vollzeit arbeiten und ungefähr gleich viel verdienen',
    );
    expect(parentalLeave.situationDe).toContain('neugeborenes Kind');
    expect(parentalLeave.situationDe).toContain('Beide haben Anspruch auf bezahlte Elternzeit');
  });
});
