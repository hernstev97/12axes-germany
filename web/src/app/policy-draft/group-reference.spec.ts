import { groupComparison, groupReferenceState } from './group-reference';
import { REVIEWED_HISTORICAL_GROUPS } from './reviewed-historical-groups';

describe('Authentische optionale historische Gruppenreferenz', () => {
  it('akzeptiert ausschließlich den tief gefrorenen gebundenen Adapter, keine eingespielten Zahlen', () => {
    expect(groupReferenceState(null).status).toBe('none');
    expect(groupReferenceState(REVIEWED_HISTORICAL_GROUPS).status).toBe('bound');
    const clone = structuredClone(REVIEWED_HISTORICAL_GROUPS);
    expect(groupReferenceState(clone).status).toBe('rejected');
    const reference = clone.studies[0]!.groups[0]!.questions.find((q) => q.reference)!.reference!;
    Object.assign(reference.categories[0]!, { proportion: 1 });
    expect(groupReferenceState(clone).studies).toEqual([]);
    const original = REVIEWED_HISTORICAL_GROUPS.studies[0]!.groups[0]!.questions.find(
      (q) => q.reference,
    )!.reference!;
    expect(Object.isFrozen(REVIEWED_HISTORICAL_GROUPS)).toBe(true);
    expect(Object.isFrozen(original.categories)).toBe(true);
    expect(Object.isFrozen(original.categories[0])).toBe(true);
  });

  it('gibt Originalanteile unverändert zurück und trennt fehlende Basis von fremder Studie', () => {
    const state = groupReferenceState(REVIEWED_HISTORICAL_GROUPS);
    const study = REVIEWED_HISTORICAL_GROUPS.studies[2]!;
    const group = study.groups[0]!;
    const available = groupComparison(state, study.id, group.id, 'ESS9e03_3:sofrdst');
    expect(available.status).toBe('available');
    if (available.status !== 'available') throw Error('missing actual approved pair');
    expect(available.reference).toBe(group.questions[0]!.reference);
    expect(available.reference.categories.map((category) => category.code)).toEqual([
      '1',
      '2',
      '3',
      '4',
      '5',
    ]);
    expect(groupComparison(state, study.id, group.id, 'ESS9e03_3:sofrwrk')).toEqual({
      status: 'unavailable',
    });
    expect(groupComparison(state, study.id, group.id, 'ESS8e02_3:wrkprbf')).toEqual({
      status: 'other-study',
    });
    expect(
      groupComparison(state, study.id, 'ESS8e02_3:second_vote:1', 'ESS9e03_3:sofrdst'),
    ).toEqual({ status: 'none' });
    expect(groupComparison(state, '', '', 'ESS9e03_3:sofrdst')).toEqual({ status: 'none' });
  });
});
