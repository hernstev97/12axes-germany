import { ITEM_RULES, type Direction, type ItemRule } from './profile-rules';
import {
  BLOCK_RULES,
  CROSS_REFERENCE_RULES,
  type BlockRule,
  type CrossReferenceRule,
} from './profile-structure';

/**
 * Descriptive answer profile (Profilregeln v1). A pure function of the answer
 * codes and the fixed rule tables: the same answers give the same text in any
 * answer order. No value, score, rank, axis or label of the person is computed.
 */

export interface ProfileCategory {
  readonly code: string;
  readonly labelDe: string;
}

export interface ProfileItem {
  readonly id: string;
  readonly primaryTheme: string;
  readonly categories: readonly ProfileCategory[];
}

export interface ProfileArea {
  readonly id: string;
  readonly title: string;
}

export type ProfileAnswer =
  | { readonly status: 'untouched' }
  | { readonly status: 'skipped' }
  | { readonly status: 'answered'; readonly code: string };

export interface ItemStatement {
  readonly itemId: string;
  readonly title: string;
  readonly text: string;
  /** Short form for lists: chosen label or value. */
  readonly answer: string;
  readonly context: string;
  readonly direction: Direction | null;
  readonly code: string;
}

export interface BlockStatement {
  readonly blockId: string;
  readonly title: string;
  readonly sentences: readonly string[];
  readonly note: string;
  readonly basis: string;
  readonly itemIds: readonly string[];
  readonly unansweredItemIds: readonly string[];
}

export interface CrossReferenceStatement {
  readonly id: string;
  readonly title: string;
  readonly answers: readonly {
    readonly itemId: string;
    readonly title: string;
    readonly answer: string;
  }[];
  readonly unansweredItemIds: readonly string[];
  readonly context: string;
}

export interface AreaProfile {
  readonly areaId: string;
  readonly title: string;
  readonly answered: number;
  readonly total: number;
  readonly statements: readonly ItemStatement[];
  readonly blocks: readonly BlockStatement[];
}

export interface AnswerProfile {
  readonly answered: number;
  readonly total: number;
  readonly areas: readonly AreaProfile[];
  readonly crossReferences: readonly CrossReferenceStatement[];
  readonly withoutAnswer: readonly {
    readonly itemId: string;
    readonly status: 'skipped' | 'untouched';
  }[];
  readonly usesMiddleCategory: boolean;
}

export class ProfileInputError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ProfileInputError';
  }
}

function fail(message: string): never {
  throw new ProfileInputError(message);
}

function ruleFor(itemId: string): ItemRule {
  return ITEM_RULES[itemId] ?? fail(`no profile rule for ${itemId}`);
}

function quoted(text: string): string {
  return `„${text}“`;
}

/** Ends a sentence without doubling punctuation that is already inside a quote. */
function sentence(text: string): string {
  return /[.?!]“?$/.test(text) ? text : `${text}.`;
}

function anchors(item: ProfileItem): { readonly low: string; readonly high: string } {
  const low = item.categories.find((category) => category.code === '0');
  const high = item.categories.find((category) => category.code === '10');
  if (!low || !high) fail(`${item.id} has no 0–10 anchors`);
  return { low: low.labelDe, high: high.labelDe };
}

function direction(rule: ItemRule, itemId: string, code: string): Direction {
  const value = rule.directions?.[code];
  return value ?? fail(`no direction for ${itemId} code ${code}`);
}

function statementFor(item: ProfileItem, code: string): ItemStatement {
  const rule = ruleFor(item.id);
  const category = item.categories.find((entry) => entry.code === code);
  if (!category) fail(`unknown category ${code} for ${item.id}`);
  const chosen = `(gewählt: ${quoted(category.labelDe)})`;
  const form = rule.statement;
  let text: string;
  let answer = quoted(category.labelDe);
  let dir: Direction | null = null;
  switch (form.form) {
    case 'agreement': {
      dir = direction(rule, item.id, code);
      const lead = {
        positive: 'Zustimmung zur Aussage',
        middle: 'Weder Zustimmung noch Ablehnung zur Aussage',
        negative: 'Ablehnung der Aussage',
      }[dir];
      text = `${lead} ${quoted(form.statement)} ${chosen}.`;
      break;
    }
    case 'support-clause': {
      dir = direction(rule, item.id, code);
      const lead = {
        positive: 'Dafür',
        middle: 'Weder dafür noch dagegen',
        negative: 'Dagegen',
      }[dir];
      text = `${lead}, ${form.clause} ${chosen}.`;
      break;
    }
    case 'support-noun': {
      dir = direction(rule, item.id, code);
      const lead = { positive: 'Für', middle: 'Weder für noch gegen', negative: 'Gegen' }[dir];
      text = `${lead} ${form.nounPhrase} ${chosen}.`;
      break;
    }
    case 'scale': {
      if (!/^(?:[0-9]|10)$/.test(code)) fail(`${item.id} is not a 0–10 scale`);
      const { low, high } = anchors(item);
      text = `${form.subject}: ${code} (0 = ${quoted(low)}, 10 = ${quoted(high)}).`;
      answer = `${code} von 10`;
      break;
    }
    case 'bipolar': {
      if (!/^(?:[0-9]|10)$/.test(code)) fail(`${item.id} is not a 0–10 scale`);
      const { low, high } = anchors(item);
      const value = Number(code);
      if (value === 0) text = `${form.subject}: 0 (${quoted(low)}).`;
      else if (value === 10) text = `${form.subject}: 10 (${quoted(high)}).`;
      else if (value < 5) text = `${form.subject}: ${code}, näher an ${quoted(low)}.`;
      else if (value > 5) text = `${form.subject}: ${code}, näher an ${quoted(high)}.`;
      else text = `${form.subject}: 5, gleicher Abstand zu ${quoted(low)} und ${quoted(high)}.`;
      answer = `${code} von 10`;
      break;
    }
    case 'label': {
      text = sentence(`${form.subject}: ${quoted(category.labelDe)}`);
      break;
    }
  }
  return Object.freeze({
    itemId: item.id,
    title: rule.title,
    text,
    answer,
    context: rule.context,
    direction: dir,
    code,
  });
}

function joinTitles(statements: readonly ItemStatement[]): string {
  const titles = statements.map((statement) => statement.title);
  if (titles.length <= 1) return titles.join('');
  return `${titles.slice(0, -1).join(', ')} und ${titles.at(-1)}`;
}

function directionSentences(statements: readonly ItemStatement[], support: boolean): string[] {
  const labels: Record<Direction, string> = support
    ? { positive: 'Dafür', middle: 'Weder dafür noch dagegen', negative: 'Dagegen' }
    : { positive: 'Zustimmung', middle: 'Weder Zustimmung noch Ablehnung', negative: 'Ablehnung' };
  const order: readonly Direction[] = ['positive', 'middle', 'negative'];
  const present = order.filter((dir) => statements.some((entry) => entry.direction === dir));
  if (present.length === 1) {
    return [`Alle beantworteten Fragen dieses Blocks: ${labels[present[0]!]}.`];
  }
  return present.map(
    (dir) =>
      `${labels[dir]}: ${joinTitles(statements.filter((entry) => entry.direction === dir))}.`,
  );
}

function scaleSentences(statements: readonly ItemStatement[]): string[] {
  const values = statements.map((statement) => Number(statement.code));
  const max = Math.max(...values);
  const min = Math.min(...values);
  if (max === min) {
    return [`Alle beantworteten Fragen dieses Blocks erhielten denselben Wert: ${max}.`];
  }
  const listed = statements.map((statement) => `${statement.title} ${statement.code}`).join(', ');
  const highest = statements.filter((statement) => Number(statement.code) === max);
  const lowest = statements.filter((statement) => Number(statement.code) === min);
  return [
    `Die Werte unterscheiden sich: ${listed}.`,
    `Höchster Wert (${max}): ${joinTitles(highest)}.`,
    `Niedrigster Wert (${min}): ${joinTitles(lowest)}.`,
  ];
}

/** Ordered labels where a lower code means more admitted immigration (ESS A54–A56). */
function orderedLabelSentences(statements: readonly ItemStatement[]): string[] {
  const codes = new Set(statements.map((statement) => statement.code));
  if (codes.size === 1) {
    return [`Für alle beantworteten Gruppen dieselbe Antwort: ${statements[0]!.answer}.`];
  }
  const sentences = [
    `Die Antworten unterscheiden sich nach Gruppe: ${statements
      .map((statement) => `${statement.title} ${statement.answer}`)
      .join(', ')}.`,
  ];
  for (let i = 0; i < statements.length; i++) {
    for (let j = i + 1; j < statements.length; j++) {
      const a = statements[i]!;
      const b = statements[j]!;
      if (a.code === b.code) continue;
      const [more, less] = Number(a.code) < Number(b.code) ? [a, b] : [b, a];
      sentences.push(`Für ${more.title} wurde mehr Zuwanderung erlaubt als für ${less.title}.`);
    }
  }
  return sentences;
}

function blockStatement(
  block: BlockRule,
  statements: ReadonlyMap<string, ItemStatement>,
): BlockStatement | null {
  const answered = block.itemIds
    .map((id) => statements.get(id))
    .filter((statement): statement is ItemStatement => statement !== undefined);
  if (answered.length < 2) return null;
  const support = answered.some((statement) => {
    const form = ruleFor(statement.itemId).statement.form;
    return form === 'support-clause' || form === 'support-noun';
  });
  const sentences =
    block.pattern === 'directions'
      ? directionSentences(answered, support)
      : block.pattern === 'scale-values'
        ? scaleSentences(answered)
        : orderedLabelSentences(answered);
  return Object.freeze({
    blockId: block.id,
    title: block.title,
    sentences: Object.freeze(sentences),
    note: block.note,
    basis: block.basis,
    itemIds: Object.freeze(answered.map((statement) => statement.itemId)),
    unansweredItemIds: Object.freeze(block.itemIds.filter((id) => !statements.has(id))),
  });
}

function crossReference(
  rule: CrossReferenceRule,
  statements: ReadonlyMap<string, ItemStatement>,
): CrossReferenceStatement | null {
  const answered = rule.itemIds
    .map((id) => statements.get(id))
    .filter((statement): statement is ItemStatement => statement !== undefined);
  if (answered.length < 2) return null;
  return Object.freeze({
    id: rule.id,
    title: rule.title,
    answers: Object.freeze(
      answered.map((statement) =>
        Object.freeze({
          itemId: statement.itemId,
          title: statement.title,
          answer: statement.answer,
        }),
      ),
    ),
    unansweredItemIds: Object.freeze(rule.itemIds.filter((id) => !statements.has(id))),
    context: rule.context,
  });
}

export function buildAnswerProfile(
  items: readonly ProfileItem[],
  areas: readonly ProfileArea[],
  answers: ReadonlyMap<string, ProfileAnswer>,
): AnswerProfile {
  const statements = new Map<string, ItemStatement>();
  const withoutAnswer: { itemId: string; status: 'skipped' | 'untouched' }[] = [];
  for (const item of items) {
    const answer = answers.get(item.id) ?? fail(`missing answer state for ${item.id}`);
    if (answer.status === 'answered') statements.set(item.id, statementFor(item, answer.code));
    else withoutAnswer.push(Object.freeze({ itemId: item.id, status: answer.status }));
  }
  const areaProfiles = areas.map((area) => {
    const areaItems = items.filter((item) => item.primaryTheme === area.id);
    const areaIds = new Set(areaItems.map((item) => item.id));
    const blocks = BLOCK_RULES.filter((block) => block.itemIds.every((id) => areaIds.has(id)))
      .map((block) => blockStatement(block, statements))
      .filter((block): block is BlockStatement => block !== null);
    const areaStatements = areaItems
      .map((item) => statements.get(item.id))
      .filter((statement): statement is ItemStatement => statement !== undefined);
    return Object.freeze({
      areaId: area.id,
      title: area.title,
      answered: areaStatements.length,
      total: areaItems.length,
      statements: Object.freeze(areaStatements),
      blocks: Object.freeze(blocks),
    });
  });
  const crossReferences = CROSS_REFERENCE_RULES.map((rule) =>
    crossReference(rule, statements),
  ).filter((entry): entry is CrossReferenceStatement => entry !== null);
  return Object.freeze({
    answered: statements.size,
    total: items.length,
    areas: Object.freeze(areaProfiles),
    crossReferences: Object.freeze(crossReferences),
    withoutAnswer: Object.freeze(withoutAnswer),
    usesMiddleCategory: [...statements.values()].some(
      (statement) => statement.direction === 'middle',
    ),
  });
}

/** Item ids covered by the rule tables; used by tests to keep catalogue and rules aligned. */
export function ruleItemIds(): readonly string[] {
  return Object.keys(ITEM_RULES);
}
