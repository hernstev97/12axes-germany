import { indexReferencesV22, intervalFor, pairKey, type ReferencesV22 } from './reference-v22';

// Synthetic aggregates for binding logic only. Not survey results.
const reference = {
  validCount: 200,
  totalCount: 210,
  missingCount: 10,
  notAskedCount: 0,
  categories: [
    { code: '1', proportion: 0.25, lower: 0.2, upper: 0.31 },
    { code: '2', proportion: 0.75, lower: null, upper: null },
  ],
  interval: { degreesOfFreedom: 90, strata: 89, psus: 179 },
};

const input: ReferencesV22 = {
  sources: {},
  studies: [
    {
      study: 'ESS9e03_3',
      designAvailable: true,
      questions: [
        { id: 'ESS9e03_3:a', status: 'reviewed_historical_reference', reference },
        // A withheld or empty entry never exposes numbers, even if a malformed input carries them.
        { id: 'ESS9e03_3:b', status: 'withheld_base_or_cell_count', reference },
        { id: 'ESS9e03_3:c', status: 'no_valid_answers', reference: null },
      ],
      groups: [
        {
          groupId: 'ESS9e03_3:second_vote:1',
          pairs: [{ questionId: 'ESS9e03_3:a', status: 'withheld_base_or_cell_count', reference }],
        },
      ],
    },
  ],
};

describe('reviewed v2.2 references', () => {
  it('T30: only reviewed entries carry numbers', () => {
    const index = indexReferencesV22(input);
    expect(index.single.get('ESS9e03_3:a')?.reference).not.toBeNull();
    expect(index.single.get('ESS9e03_3:b')).toEqual({
      status: 'withheld_base_or_cell_count',
      reference: null,
    });
    expect(index.single.get('ESS9e03_3:c')?.reference).toBeNull();
    expect(
      index.pairs.get(pairKey('ESS9e03_3:second_vote:1', 'ESS9e03_3:a'))?.reference,
    ).toBeNull();
  });

  it('returns an interval only where one was computed', () => {
    const index = indexReferencesV22(input);
    expect(intervalFor(index.single.get('ESS9e03_3:a'), '1')).toEqual({ lower: 0.2, upper: 0.31 });
    expect(intervalFor(index.single.get('ESS9e03_3:a'), '2')).toBeNull();
    expect(intervalFor(index.single.get('ESS9e03_3:b'), '1')).toBeNull();
    expect(indexReferencesV22(null).single.size).toBe(0);
  });
});
