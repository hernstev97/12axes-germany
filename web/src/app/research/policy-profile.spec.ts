import {
  PolicyProfileInputError,
  PolicyProfileSession,
  type PolicyQuestion,
  type PolicyQuestionSource,
} from './policy-profile';

// Entirely synthetic identities/codes/metadata; no original items or reference shares.
function source(studyId: string, originalQuestionId: string): PolicyQuestionSource {
  return {
    studyId,
    originalQuestionId,
    sourceId: `${studyId}-synthetic-document-v1`,
    time: `${studyId}-synthetic-time`,
    population: `${studyId}-synthetic-population`,
    mode: `${studyId}-synthetic-mode`,
  };
}

function questions(): PolicyQuestion[] {
  return [
    {
      id: 'entry-a',
      primaryTheme: 'synthetic-theme-1',
      categories: ['a-code-1', 'a-code-2'],
      source: source('synthetic-study-a', 'original-code-1'),
    },
    {
      id: 'entry-b',
      primaryTheme: 'synthetic-theme-1',
      categories: ['b-code-1', 'b-code-2', 'b-code-3'],
      source: source('synthetic-study-b', 'original-code-1'),
    },
    {
      id: 'entry-c',
      primaryTheme: 'synthetic-theme-2',
      categories: ['c-code-1'],
      source: source('synthetic-study-a', 'original-code-2'),
    },
  ];
}

function constructInvalid(input: unknown): void {
  new PolicyProfileSession(input as readonly PolicyQuestion[]);
}

describe('PolicyProfileSession: synthetic preparation only', () => {
  it('preserves answers while navigating, then changes an earlier answer independently', () => {
    const session = new PolicyProfileSession(questions());
    expect(session.currentQuestion?.id).toBe('entry-a');
    session.answer('entry-a', 'a-code-2');
    session.next();
    session.answer('entry-b', 'b-code-3');
    session.next();
    expect(session.currentQuestion?.id).toBe('entry-c');
    session.previous();
    session.previous();
    expect(session.getAnswer('entry-b')).toEqual({ status: 'answered', code: 'b-code-3' });
    const beforeEdit = session.snapshot();
    session.answer('entry-a', 'a-code-1');
    session.goTo('entry-c');
    expect(session.snapshot().responses.map(({ answer }) => answer)).toEqual([
      { status: 'answered', code: 'a-code-1' },
      { status: 'answered', code: 'b-code-3' },
      { status: 'untouched' },
    ]);
    expect(beforeEdit.responses[0].answer).toEqual({ status: 'answered', code: 'a-code-2' });
  });

  it('distinguishes untouched, skipped, answered and explicit resetting without completion', () => {
    const session = new PolicyProfileSession(questions());
    session.next();
    expect(session.getAnswer('entry-a')).toEqual({ status: 'untouched' });
    session.skip('entry-b');
    expect(session.result()).toEqual({
      themes: [],
      unanswered: [
        {
          questionId: 'entry-a',
          primaryTheme: 'synthetic-theme-1',
          status: 'untouched',
          source: source('synthetic-study-a', 'original-code-1'),
          reference: { status: 'none' },
        },
        {
          questionId: 'entry-b',
          primaryTheme: 'synthetic-theme-1',
          status: 'skipped',
          source: source('synthetic-study-b', 'original-code-1'),
          reference: { status: 'none' },
        },
        {
          questionId: 'entry-c',
          primaryTheme: 'synthetic-theme-2',
          status: 'untouched',
          source: source('synthetic-study-a', 'original-code-2'),
          reference: { status: 'none' },
        },
      ],
    });
    session.answer('entry-b', 'b-code-2');
    session.skip('entry-b');
    expect(session.getAnswer('entry-b')).toEqual({ status: 'skipped' });
    session.resetAnswer('entry-b');
    expect(session.getAnswer('entry-b')).toEqual({ status: 'untouched' });
  });

  it('groups actual categorical answers while retaining each study, source and original identity', () => {
    const session = new PolicyProfileSession(questions());
    session.answer('entry-b', 'b-code-1');
    session.answer('entry-c', 'c-code-1');
    session.answer('entry-a', 'a-code-2');
    expect(session.result()).toEqual({
      themes: [
        {
          primaryTheme: 'synthetic-theme-1',
          answers: [
            {
              questionId: 'entry-a',
              code: 'a-code-2',
              source: source('synthetic-study-a', 'original-code-1'),
              reference: { status: 'none' },
            },
            {
              questionId: 'entry-b',
              code: 'b-code-1',
              source: source('synthetic-study-b', 'original-code-1'),
              reference: { status: 'none' },
            },
          ],
        },
        {
          primaryTheme: 'synthetic-theme-2',
          answers: [
            {
              questionId: 'entry-c',
              code: 'c-code-1',
              source: source('synthetic-study-a', 'original-code-2'),
              reference: { status: 'none' },
            },
          ],
        },
      ],
      unanswered: [],
    });
  });

  it('rejects unknown question/category operations before changing state', () => {
    const session = new PolicyProfileSession(questions());
    session.answer('entry-a', 'a-code-1');
    session.goTo('entry-b');
    const before = session.snapshot();
    const invalidOperations = [
      () => session.answer('unknown', 'a-code-1'),
      () => session.answer('entry-a', 'b-code-1'),
      () => session.answer('entry-b', 'b-code-1 '),
      () => session.answer('entry-b', 'B-CODE-1'),
      () => session.skip('unknown'),
      () => session.resetAnswer('unknown'),
      () => session.getAnswer('unknown'),
      () => session.goTo('unknown'),
    ];
    for (const operation of invalidOperations) {
      expect(operation).toThrow(PolicyProfileInputError);
      expect(session.snapshot()).toEqual(before);
    }
  });

  it('keeps empty catalogs and end boundaries inert without implicit responses', () => {
    const empty = new PolicyProfileSession([]);
    empty.next();
    empty.previous();
    expect(empty.currentQuestion).toBeNull();
    expect(empty.snapshot()).toEqual({ currentQuestionId: null, responses: [] });
    expect(empty.result()).toEqual({ themes: [], unanswered: [] });
    expect(() => empty.goTo('entry-a')).toThrow(PolicyProfileInputError);

    const session = new PolicyProfileSession(questions());
    session.previous();
    expect(session.currentQuestion?.id).toBe('entry-a');
    session.goTo('entry-c');
    session.next();
    expect(session.currentQuestion?.id).toBe('entry-c');
    expect(session.snapshot().responses.every(({ answer }) => answer.status === 'untouched')).toBe(
      true,
    );
  });

  it('does not merge repeated original codes or category codes from different studies', () => {
    const input = questions();
    input[1] = { ...input[1], categories: ['a-code-1', 'independent-code'] };
    const session = new PolicyProfileSession(input);
    session.answer('entry-a', 'a-code-1');
    expect(session.getAnswer('entry-b')).toEqual({ status: 'untouched' });
    session.answer('entry-b', 'independent-code');
    expect(
      session.result().themes[0].answers.map(({ source, code }) => [source.studyId, code]),
    ).toEqual([
      ['synthetic-study-a', 'a-code-1'],
      ['synthetic-study-b', 'independent-code'],
    ]);
    expect(() => session.answer('entry-a', 'independent-code')).toThrow(PolicyProfileInputError);
  });

  it('keeps separate in-memory sessions independent even with the same catalog', () => {
    const input = questions();
    const first = new PolicyProfileSession(input);
    const second = new PolicyProfileSession(input);
    first.answer('entry-a', 'a-code-2');
    first.skip('entry-b');
    first.goTo('entry-c');
    expect(second.snapshot().responses.map(({ answer }) => answer)).toEqual([
      { status: 'untouched' },
      { status: 'untouched' },
      { status: 'untouched' },
    ]);
    expect(second.currentQuestion?.id).toBe('entry-a');
    second.answer('entry-a', 'a-code-1');
    expect(first.getAnswer('entry-a')).toEqual({ status: 'answered', code: 'a-code-2' });
  });

  it('rejects duplicate global ids and duplicate original identities within one study', () => {
    const duplicateId = questions();
    duplicateId[1] = { ...duplicateId[1], id: 'entry-a' };
    expect(() => new PolicyProfileSession(duplicateId)).toThrow(/duplicate question id/);
    const duplicateOriginal = questions();
    duplicateOriginal[1] = { ...duplicateOriginal[1], source: duplicateOriginal[0].source };
    expect(() => new PolicyProfileSession(duplicateOriginal)).toThrow(
      /duplicate original question/,
    );
  });

  it('rejects duplicated, missing and nonstring category codes without manufacturing a middle', () => {
    const invalidCategories: unknown[] = [[], ['same', 'same'], [''], ['   '], ['valid', 2], null];
    for (const categories of invalidCategories) {
      const input = questions();
      const malformed = [{ ...input[0], categories }];
      expect(() => constructInvalid(malformed)).toThrow(PolicyProfileInputError);
    }
    const input = questions();
    input[0] = { ...input[0], categories: [' code-with-space ', '0', 'null'] };
    const session = new PolicyProfileSession(input);
    session.answer('entry-a', ' code-with-space ');
    expect(session.getAnswer('entry-a')).toEqual({ status: 'answered', code: ' code-with-space ' });
    expect(() => session.answer('entry-a', 'code-with-space')).toThrow(PolicyProfileInputError);
  });

  it('requires separate nonempty source fields and rejects unrecognized metadata', () => {
    for (const field of [
      'studyId',
      'originalQuestionId',
      'sourceId',
      'time',
      'population',
      'mode',
    ]) {
      for (const value of ['', ' ', ' padded ', null, 2026]) {
        const input = questions();
        const malformed = [{ ...input[0], source: { ...input[0].source, [field]: value } }];
        expect(() => constructInvalid(malformed)).toThrow(PolicyProfileInputError);
      }
      const input = questions();
      const incomplete = { ...input[0].source } as Record<string, unknown>;
      delete incomplete[field];
      expect(() => constructInvalid([{ ...input[0], source: incomplete }])).toThrow(
        PolicyProfileInputError,
      );
    }
    const input = questions();
    expect(() => constructInvalid([{ ...input[0], source: null }])).toThrow(
      PolicyProfileInputError,
    );
    expect(() =>
      constructInvalid([{ ...input[0], source: { ...input[0].source, reference: 0.5 } }]),
    ).toThrow(PolicyProfileInputError);
  });

  it('rejects malformed identity/theme/catalog records at construction', () => {
    const input = questions();
    const invalid: unknown[] = [
      null,
      {},
      [null],
      [{ ...input[0], id: '' }],
      [{ ...input[0], id: ' entry-a' }],
      [{ ...input[0], primaryTheme: '' }],
      [{ ...input[0], primaryTheme: false }],
      [{ ...input[0], score: 4 }],
      new Array(1),
    ];
    for (const value of invalid) {
      expect(() => constructInvalid(value)).toThrow(PolicyProfileInputError);
    }
  });

  it('copies input data and freezes exposed data so later mutation cannot rewrite answers or provenance', () => {
    const input = questions();
    const categoryArray = input[0].categories as string[];
    const inputSource = input[0].source as {
      -readonly [Key in keyof PolicyQuestionSource]: string;
    };
    const session = new PolicyProfileSession(input);
    const oldSnapshot = session.snapshot();
    categoryArray.push('injected');
    inputSource.studyId = 'changed-study';
    input[0] = { ...input[0], id: 'changed-id' };
    expect(session.currentQuestion?.id).toBe('entry-a');
    expect(() => session.answer('entry-a', 'injected')).toThrow(PolicyProfileInputError);
    session.answer('entry-a', 'a-code-1');
    const result = session.result();
    expect(result.themes[0].answers[0].source.studyId).toBe('synthetic-study-a');
    expect(oldSnapshot.responses[0].answer).toEqual({ status: 'untouched' });
    expect(Object.isFrozen(oldSnapshot.responses[0].question.categories)).toBe(true);
    expect(Object.isFrozen(result.themes[0].answers[0].source)).toBe(true);
    expect(Reflect.set(result.themes[0].answers[0], 'code', 'a-code-2')).toBe(false);
    expect(Reflect.set(result.themes[0].answers[0].source, 'studyId', 'changed')).toBe(false);
    expect(session.getAnswer('entry-a')).toEqual({ status: 'answered', code: 'a-code-1' });
  });

  it('rejects accessor metadata without evaluating a caller getter', () => {
    const input = questions();
    let reads = 0;
    const accessorSource = { ...input[0].source };
    Object.defineProperty(accessorSource, 'time', {
      enumerable: true,
      get: () => {
        reads++;
        return 'synthetic-time';
      },
    });
    expect(() => constructInvalid([{ ...input[0], source: accessorSource }])).toThrow(
      PolicyProfileInputError,
    );
    expect(reads).toBe(0);
  });
});

describe('PP-001: passive array boundary', () => {
  it('reads declared category data without calling a custom iterator or accepting its injected code', () => {
    const input = questions();
    const categories = ['a-code-1', 'a-code-2'];
    let iteratorCalls = 0;
    Object.defineProperty(categories, Symbol.iterator, {
      value: () => {
        iteratorCalls++;
        return ['injected-code'][Symbol.iterator]();
      },
    });
    input[0] = { ...input[0], categories };
    const session = new PolicyProfileSession(input);
    expect(session.currentQuestion?.categories).toEqual(['a-code-1', 'a-code-2']);
    const before = session.snapshot();
    expect(() => session.answer('entry-a', 'injected-code')).toThrow(PolicyProfileInputError);
    expect(session.snapshot()).toEqual(before);
    session.answer('entry-a', 'a-code-2');
    expect(session.getAnswer('entry-a')).toEqual({ status: 'answered', code: 'a-code-2' });
    expect(iteratorCalls).toBe(0);
  });

  it('rejects an invalid indexed category even when its custom iterator would yield a valid code', () => {
    const input = questions();
    const categories: unknown[] = [null];
    let iteratorCalls = 0;
    Object.defineProperty(categories, Symbol.iterator, {
      value: () => {
        iteratorCalls++;
        return ['a-code-1'][Symbol.iterator]();
      },
    });
    expect(() => constructInvalid([{ ...input[0], categories }])).toThrow(PolicyProfileInputError);
    expect(iteratorCalls).toBe(0);
  });

  it('rejects a category getter without reading it or allowing it to mutate the source', () => {
    const input = questions();
    const mutableSource = input[0].source as {
      -readonly [Key in keyof PolicyQuestionSource]: string;
    };
    const categories = ['a-code-1'];
    let getterCalls = 0;
    Object.defineProperty(categories, '0', {
      get: () => {
        getterCalls++;
        mutableSource.studyId = 'changed-by-getter';
        return 'a-code-1';
      },
    });
    expect(() => constructInvalid([{ ...input[0], categories }])).toThrow(PolicyProfileInputError);
    expect(getterCalls).toBe(0);
    expect(mutableSource.studyId).toBe('synthetic-study-a');
  });

  it('rejects an outer question getter before it can read or mutate any source', () => {
    const firstQuestion = questions()[0];
    const mutableSource = firstQuestion.source as {
      -readonly [Key in keyof PolicyQuestionSource]: string;
    };
    const input: PolicyQuestion[] = [firstQuestion];
    let getterCalls = 0;
    Object.defineProperty(input, '0', {
      get: () => {
        getterCalls++;
        mutableSource.studyId = 'changed-by-outer-getter';
        return firstQuestion;
      },
    });
    expect(() => new PolicyProfileSession(input)).toThrow(PolicyProfileInputError);
    expect(getterCalls).toBe(0);
    expect(mutableSource.studyId).toBe('synthetic-study-a');
  });

  it('rejects setter-only elements in either array without invoking them', () => {
    const firstQuestion = questions()[0];
    let setterCalls = 0;
    const categories = ['a-code-1'];
    const input: PolicyQuestion[] = [firstQuestion];
    const setter = () => {
      setterCalls++;
    };
    Object.defineProperty(categories, '0', { set: setter });
    Object.defineProperty(input, '0', { set: setter });
    expect(() => constructInvalid([{ ...firstQuestion, categories }])).toThrow(
      PolicyProfileInputError,
    );
    expect(() => new PolicyProfileSession(input)).toThrow(PolicyProfileInputError);
    expect(setterCalls).toBe(0);
  });

  it('does not read iterator accessors on category arrays or the outer questions array', () => {
    const input = questions();
    const categories = ['a-code-1', 'a-code-2'];
    let iteratorReads = 0;
    const iteratorGetter = () => {
      iteratorReads++;
      throw new Error('caller iterator accessor must not run');
    };
    Object.defineProperty(categories, Symbol.iterator, { get: iteratorGetter });
    input[0] = { ...input[0], categories };
    Object.defineProperty(input, Symbol.iterator, { get: iteratorGetter });
    const session = new PolicyProfileSession(input);
    expect(session.snapshot().responses.map(({ question }) => question.id)).toEqual([
      'entry-a',
      'entry-b',
      'entry-c',
    ]);
    session.answer('entry-a', 'a-code-1');
    expect(session.getAnswer('entry-a')).toEqual({ status: 'answered', code: 'a-code-1' });
    expect(iteratorReads).toBe(0);
  });

  it('rejects sparse category and question arrays rather than accepting an iterator substitute', () => {
    const firstQuestion = questions()[0];
    const sparseCategories = new Array(1);
    const sparseQuestions = new Array(1);
    let iteratorCalls = 0;
    Object.defineProperty(sparseCategories, Symbol.iterator, {
      value: () => {
        iteratorCalls++;
        return ['a-code-1'][Symbol.iterator]();
      },
    });
    Object.defineProperty(sparseQuestions, Symbol.iterator, {
      value: () => {
        iteratorCalls++;
        return [firstQuestion][Symbol.iterator]();
      },
    });
    expect(() => constructInvalid([{ ...firstQuestion, categories: sparseCategories }])).toThrow(
      PolicyProfileInputError,
    );
    expect(() => constructInvalid(sparseQuestions)).toThrow(PolicyProfileInputError);
    expect(iteratorCalls).toBe(0);
  });

  it('preserves frozen readonly passive arrays and independent sessions', () => {
    const input = Object.freeze(
      questions().map((question) =>
        Object.freeze({ ...question, categories: Object.freeze([...question.categories]) }),
      ),
    );
    const first = new PolicyProfileSession(input);
    const second = new PolicyProfileSession(input);
    first.answer('entry-a', 'a-code-2');
    first.next();
    first.skip('entry-b');
    first.previous();
    expect(first.getAnswer('entry-a')).toEqual({ status: 'answered', code: 'a-code-2' });
    expect(first.getAnswer('entry-b')).toEqual({ status: 'skipped' });
    expect(second.snapshot().responses.map(({ answer }) => answer)).toEqual([
      { status: 'untouched' },
      { status: 'untouched' },
      { status: 'untouched' },
    ]);
    expect(second.currentQuestion?.id).toBe('entry-a');
    expect(first.currentQuestion?.source.studyId).toBe('synthetic-study-a');
  });
});
