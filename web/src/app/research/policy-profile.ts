/**
 * WIP preparation for separate categorical answers. No questionnaire content,
 * reference estimates, scoring, persistence, or source-specific interpretation.
 */
export interface PolicyQuestionSource {
  readonly studyId: string;
  readonly originalQuestionId: string;
  readonly sourceId: string;
  readonly time: string;
  readonly population: string;
  readonly mode: string;
}

export interface PolicyQuestion {
  readonly id: string;
  readonly primaryTheme: string;
  readonly categories: readonly string[];
  readonly source: PolicyQuestionSource;
}

export type PolicyAnswer =
  | { readonly status: 'untouched' }
  | { readonly status: 'skipped' }
  | { readonly status: 'answered'; readonly code: string };

export interface PolicyResponse {
  readonly question: PolicyQuestion;
  readonly answer: PolicyAnswer;
}

export interface PolicySessionSnapshot {
  readonly currentQuestionId: string | null;
  readonly responses: readonly PolicyResponse[];
}

export interface PolicySingleAnswer {
  readonly questionId: string;
  readonly code: string;
  readonly source: PolicyQuestionSource;
  readonly reference: { readonly status: 'none' };
}

export interface PolicyThemeAnswers {
  readonly primaryTheme: string;
  readonly answers: readonly PolicySingleAnswer[];
}

export interface PolicyUnanswered {
  readonly questionId: string;
  readonly primaryTheme: string;
  readonly status: 'untouched' | 'skipped';
  readonly source: PolicyQuestionSource;
  readonly reference: { readonly status: 'none' };
}

export interface PolicyProfileResult {
  readonly themes: readonly PolicyThemeAnswers[];
  readonly unanswered: readonly PolicyUnanswered[];
}

export class PolicyProfileInputError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'PolicyProfileInputError';
  }
}

const UNTOUCHED: PolicyAnswer = Object.freeze({ status: 'untouched' });
const SKIPPED: PolicyAnswer = Object.freeze({ status: 'skipped' });
const NO_REFERENCE = Object.freeze({ status: 'none' as const });

function fail(message: string): never {
  throw new PolicyProfileInputError(message);
}

function record(value: unknown, keys: readonly string[], path: string): Record<string, unknown> {
  if (typeof value !== 'object' || value === null || Array.isArray(value)) {
    return fail(`${path} must be a plain object`);
  }
  const prototype: unknown = Object.getPrototypeOf(value);
  if (prototype !== Object.prototype && prototype !== null) {
    return fail(`${path} must be a plain object`);
  }
  const actualKeys = Reflect.ownKeys(value);
  if (actualKeys.length !== keys.length || actualKeys.some((key) => !keys.includes(String(key)))) {
    return fail(`${path} has missing or unexpected fields`);
  }
  for (const key of keys) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key);
    if (!descriptor || !('value' in descriptor)) {
      return fail(`${path}.${key} must be a data field`);
    }
  }
  return value as Record<string, unknown>;
}

function metadata(value: unknown, path: string): string {
  if (typeof value !== 'string' || value.length === 0 || value.trim() !== value) {
    return fail(`${path} must be a nonempty string without surrounding whitespace`);
  }
  return value;
}

function source(value: unknown, path: string): PolicyQuestionSource {
  const input = record(
    value,
    ['studyId', 'originalQuestionId', 'sourceId', 'time', 'population', 'mode'],
    path,
  );
  return Object.freeze({
    studyId: metadata(input['studyId'], `${path}.studyId`),
    originalQuestionId: metadata(input['originalQuestionId'], `${path}.originalQuestionId`),
    sourceId: metadata(input['sourceId'], `${path}.sourceId`),
    time: metadata(input['time'], `${path}.time`),
    population: metadata(input['population'], `${path}.population`),
    mode: metadata(input['mode'], `${path}.mode`),
  });
}

/**
 * Copy only dense own numeric data fields. Caller iterators and unrelated own
 * properties are ignored without being read. Element getters/setters and holes
 * are rejected. This does not isolate proxies or global prototype changes.
 */
function passiveArray(value: unknown, path: string): readonly unknown[] {
  if (!Array.isArray(value)) {
    return fail(`${path} must be an array`);
  }
  const lengthDescriptor = Object.getOwnPropertyDescriptor(value, 'length');
  if (
    !lengthDescriptor ||
    !('value' in lengthDescriptor) ||
    typeof lengthDescriptor.value !== 'number' ||
    !Number.isInteger(lengthDescriptor.value) ||
    lengthDescriptor.value < 0 ||
    lengthDescriptor.value > 4_294_967_295
  ) {
    return fail(`${path} must have an own array length data field`);
  }
  const entries: unknown[] = [];
  for (let index = 0; index < lengthDescriptor.value; index++) {
    const descriptor = Object.getOwnPropertyDescriptor(value, String(index));
    if (!descriptor || !('value' in descriptor)) {
      return fail(`${path}[${index}] must be an own data field`);
    }
    entries.push(descriptor.value);
  }
  return Object.freeze(entries);
}

function catalog(value: unknown): readonly PolicyQuestion[] {
  const questionInputs = passiveArray(value, 'questions');
  const ids = new Set<string>();
  const originalIds = new Map<string, Set<string>>();
  const questions: PolicyQuestion[] = [];
  for (let index = 0; index < questionInputs.length; index++) {
    const path = `questions[${index}]`;
    const input = record(
      questionInputs[index],
      ['id', 'primaryTheme', 'categories', 'source'],
      path,
    );
    const id = metadata(input['id'], `${path}.id`);
    if (ids.has(id)) {
      return fail(`duplicate question id: ${id}`);
    }
    ids.add(id);
    const primaryTheme = metadata(input['primaryTheme'], `${path}.primaryTheme`);
    const originalCategories = passiveArray(input['categories'], `${path}.categories`);
    if (originalCategories.length === 0) {
      return fail(`${path}.categories must be a nonempty array`);
    }
    const categories: string[] = [];
    const codes = new Set<string>();
    for (const code of originalCategories) {
      // Original strings stay exact; no recoding, trimming, case folding, or polarity.
      if (typeof code !== 'string' || code.trim().length === 0) {
        return fail(`${path}.categories must contain nonempty original strings`);
      }
      if (codes.has(code)) {
        return fail(`${path}.categories contains duplicate code: ${code}`);
      }
      codes.add(code);
      categories.push(code);
    }
    const questionSource = source(input['source'], `${path}.source`);
    const studyQuestions = originalIds.get(questionSource.studyId) ?? new Set<string>();
    if (studyQuestions.has(questionSource.originalQuestionId)) {
      return fail(`duplicate original question in study: ${questionSource.studyId}`);
    }
    studyQuestions.add(questionSource.originalQuestionId);
    originalIds.set(questionSource.studyId, studyQuestions);
    questions.push(
      Object.freeze({
        id,
        primaryTheme,
        categories: Object.freeze(categories),
        source: questionSource,
      }),
    );
  }
  return Object.freeze(questions);
}

/**
 * Local state only. Navigation never answers or skips a question. Snapshots and
 * results preserve catalog order and are detached, frozen data objects. A theme
 * groups individual reports; it is not a measurement dimension or shared scale.
 * Empty catalogs are permitted and have no current question.
 */
export class PolicyProfileSession {
  readonly #questions: readonly PolicyQuestion[];
  readonly #indices = new Map<string, number>();
  readonly #answers = new Map<string, PolicyAnswer>();
  #position = 0;

  constructor(questions: readonly PolicyQuestion[]) {
    this.#questions = catalog(questions);
    this.#questions.forEach((question, index) => {
      this.#indices.set(question.id, index);
      this.#answers.set(question.id, UNTOUCHED);
    });
  }

  get currentQuestion(): PolicyQuestion | null {
    return this.#questions[this.#position] ?? null;
  }

  #index(questionId: string): number {
    metadata(questionId, 'questionId');
    const index = this.#indices.get(questionId);
    if (index === undefined) {
      return fail(`unknown question: ${questionId}`);
    }
    return index;
  }

  answer(questionId: string, code: string): void {
    const question = this.#questions[this.#index(questionId)];
    if (typeof code !== 'string' || !question.categories.includes(code)) {
      return fail(`unknown category for question: ${questionId}`);
    }
    this.#answers.set(questionId, Object.freeze({ status: 'answered', code }));
  }

  skip(questionId: string): void {
    this.#index(questionId);
    this.#answers.set(questionId, SKIPPED);
  }

  resetAnswer(questionId: string): void {
    this.#index(questionId);
    this.#answers.set(questionId, UNTOUCHED);
  }

  getAnswer(questionId: string): PolicyAnswer {
    this.#index(questionId);
    return this.#answers.get(questionId)!;
  }

  goTo(questionId: string): void {
    const index = this.#index(questionId);
    this.#position = index;
  }

  next(): void {
    if (this.#position < this.#questions.length - 1) {
      this.#position++;
    }
  }

  previous(): void {
    if (this.#position > 0) {
      this.#position--;
    }
  }

  snapshot(): PolicySessionSnapshot {
    return Object.freeze({
      currentQuestionId: this.currentQuestion?.id ?? null,
      responses: Object.freeze(
        this.#questions.map((question) =>
          Object.freeze({ question, answer: this.#answers.get(question.id)! }),
        ),
      ),
    });
  }

  result(): PolicyProfileResult {
    const themes = new Map<string, PolicySingleAnswer[]>();
    const unanswered: PolicyUnanswered[] = [];
    for (const question of this.#questions) {
      const answer = this.#answers.get(question.id)!;
      if (answer.status === 'answered') {
        const answers = themes.get(question.primaryTheme) ?? [];
        answers.push(
          Object.freeze({
            questionId: question.id,
            code: answer.code,
            source: question.source,
            reference: NO_REFERENCE,
          }),
        );
        themes.set(question.primaryTheme, answers);
      } else {
        unanswered.push(
          Object.freeze({
            questionId: question.id,
            primaryTheme: question.primaryTheme,
            status: answer.status,
            source: question.source,
            reference: NO_REFERENCE,
          }),
        );
      }
    }
    return Object.freeze({
      themes: Object.freeze(
        Array.from(themes, ([primaryTheme, answers]) =>
          Object.freeze({ primaryTheme, answers: Object.freeze(answers) }),
        ),
      ),
      unanswered: Object.freeze(unanswered),
    });
  }
}
