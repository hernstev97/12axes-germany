import {
  bindHistoricalReferences,
  HistoricalReferenceInputError,
  type HistoricalCategoryReference,
  type HistoricalReferenceInput,
  referenceState,
} from './historical-reference';
import { POLICY_DRAFT_ITEMS } from './policy-catalogue';
import { PUBLIC_CATALOGUE } from './public-catalogue';

// Entirely synthetic category shares for a technical adapter test. No release,
// scientific validity, or actual reference distribution is asserted by this fixture.
function syntheticInput(): HistoricalReferenceInput {
  const item = POLICY_DRAFT_ITEMS.find((entry) => entry.variable === 'euftf')!;
  const reference: HistoricalCategoryReference = {
    questionId: item.id,
    studyId: item.studyId,
    variable: item.variable,
    originalQuestionId: item.originalQuestionId,
    edition: item.study.edition,
    dataDoiUrl: item.study.dataDoiUrl,
    instrumentSourceIds: [...new Set(item.sourceRefs.map((source) => source.sourceId))],
    codeSourceId: item.codeBinding.sourceId,
    sourceFieldId: item.codeBinding.sourceFieldId,
    sourceFieldMetadataVersion: item.codeBinding.sourceFieldMetadataVersion,
    dataFileMetadataId: item.codeBinding.dataFileMetadataId,
    dataFileMetadataVersion: item.codeBinding.dataFileMetadataVersion,
    basis: 'historical-study-item',
    weight: 'pspwght',
    denominator: 'valid_item_responses',
    validUnweightedN: 101,
    // Reverse order deliberately, proving category identity rather than index matching.
    categoryShares: item.categories
      .map((category) => ({ code: category.code, share: category.code === '9' ? 1 : 0 }))
      .reverse(),
  };
  return { catalogueSha256: PUBLIC_CATALOGUE.catalogueSha256, references: [reference] };
}

describe('Historische Referenzeingabe ohne eingebundene Zahlen', () => {
  it('lässt fehlende Referenzen leer und erkennt Kategorien unabhängig von der Listenfolge', () => {
    expect(bindHistoricalReferences(null)).toEqual({ status: 'none' });
    const result = bindHistoricalReferences(syntheticInput());
    expect(result.status).toBe('bound');
    if (result.status !== 'bound') throw Error('Synthetic technical fixture did not bind');
    const reference = result.references.get('ESS11e04_2:euftf')!;
    expect(reference.categoryShares[9]).toEqual({ code: '9', share: 1 });
    expect(reference.categoryShares[0]).toEqual({ code: '0', share: 0 });
  });

  it.each([
    ['studyId', 'ESS10SCe03_2'],
    ['edition', '4.1'],
    ['variable', 'gincdif'],
    ['originalQuestionId', 'B33'],
    ['codeSourceId', 'unbound-public-source'],
    ['sourceFieldId', 'unbound-field'],
    ['dataFileMetadataVersion', -1],
    ['dataDoiUrl', 'https://doi.org/10.21338/ess10sce03_2'],
    ['instrumentSourceIds', ['ess10-de-questionnaire']],
    ['weight', 'dweight'],
    ['denominator', 'all_respondents'],
  ])('verwirft eine andere Quelle oder Auswertung bei %s', (key, value) => {
    const original = syntheticInput();
    const input = { ...original, references: [{ ...original.references[0], [key]: value }] };
    expect(() => bindHistoricalReferences(input as HistoricalReferenceInput)).toThrow(
      HistoricalReferenceInputError,
    );
    expect(referenceState(input as HistoricalReferenceInput)).toEqual({ status: 'rejected' });
  });

  it('verwirft Druckcodes, Missing-Codes, doppelte Kategorien und zusätzliche Scorefelder', () => {
    const input = syntheticInput();
    const reference = input.references[0]!;
    for (const code of ['00', '88', reference.categoryShares[1]!.code]) {
      const categoryShares = [
        { ...reference.categoryShares[0], code },
        ...reference.categoryShares.slice(1),
      ];
      expect(() =>
        bindHistoricalReferences({ ...input, references: [{ ...reference, categoryShares }] }),
      ).toThrow(HistoricalReferenceInputError);
    }
    expect(() =>
      bindHistoricalReferences({
        ...input,
        references: [{ ...reference, score: 0.5 }],
      } as unknown as HistoricalReferenceInput),
    ).toThrow(HistoricalReferenceInputError);
    expect(() =>
      bindHistoricalReferences({ ...input, catalogueSha256: 'unbound-catalogue' }),
    ).toThrow(HistoricalReferenceInputError);
    expect(() =>
      bindHistoricalReferences({ ...input, references: [reference, reference] }),
    ).toThrow(HistoricalReferenceInputError);
  });
});
