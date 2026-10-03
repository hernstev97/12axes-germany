import type { PolicyQuestion } from '../research/policy-profile';
import type { PublicCategory, PublicItem, PublicStudy } from './catalogue-types';
import { ITEM_MEANINGS } from './item-meanings';
import { PUBLIC_CATALOGUE } from './public-catalogue';

export const POLICY_RUBRICS = Object.freeze([
  { id: 'economy_distribution', title: 'Wirtschaft und Verteilung' },
  { id: 'welfare', title: 'Sozialstaat' },
  { id: 'democracy_authority', title: 'Demokratie und politische Autorität' },
  { id: 'rights_security', title: 'Bürgerrechte und Sicherheit' },
  { id: 'europe', title: 'Europäische Integration' },
  { id: 'climate_energy', title: 'Klima und Energie' },
  { id: 'migration', title: 'Migration' },
  { id: 'equality_family', title: 'Gleichstellungs- und Familienpolitik' },
]);

const democracy = PUBLIC_CATALOGUE.groups.find((group) => group.id === 'democracy_norms')!;
const democracyIds = new Set(democracy.itemIds);
const numberedTypes = new Set([
  'ordered_responsibility',
  'ordered_importance',
  'ordered_obligation',
  'ordered_direction',
]);

export interface PolicyDraftItem extends PublicItem {
  readonly study: PublicStudy;
  readonly title: string;
  readonly meaning: string;
  readonly rubricTitle: string;
  readonly origin: string;
  readonly fieldworkLabel: string;
  readonly modesLabel: string;
  readonly displayWording: readonly string[];
  readonly developmentNote: string;
  readonly question: PolicyQuestion;
}

function date(value: string): string {
  return new Intl.DateTimeFormat('de-DE', { dateStyle: 'long', timeZone: 'UTC' }).format(
    new Date(value),
  );
}

export function categoryLabel(item: PublicItem, category: PublicCategory): string {
  return numberedTypes.has(item.responseType) && !/^\d+$/.test(category.labelDe)
    ? `${category.printedCodeDe}: ${category.labelDe}`
    : category.labelDe;
}

function developmentNote(item: PublicItem): string {
  if (democracyIds.has(item.id)) {
    return 'Entwicklungsfassung: B1–B12 bleiben in der Originalreihenfolge zusammen. Die vollständige Einleitung nennt nachfolgende Fragen zur Funktionsweise der Demokratie; B13–B24 fehlen in diesem Entwurf. Einzelansicht und Gesamtfragebogenkontext sind neu. B12 erscheint im Ergebnis unter europäischer Integration.';
  }
  if (item.variable === 'scchpldm') {
    return 'Entwicklungsfassung B25: Die gebundene Papierfassung führt ursprünglich je nach Alternative zu B26 oder B28. Dieser Entwurf geht unabhängig von der Auswahl zur nächsten gewählten Frage und lässt B26–B29 aus. Eine ursprüngliche operative Weiterleitung oder CAWI-Äquivalenz ist damit nicht belegt.';
  }
  if (item.variable === 'hrshsnta') {
    return 'Originalkontext 2010/2011: „heute“ bezeichnet die damalige Strafpraxis. Einzelansicht und Durchführung auf dieser Website sind eine neue Entwicklungsfassung.';
  }
  return 'Entwicklungsfassung: Die gebundene nationale Papier- oder Interviewfassung bleibt als Originalkontext sichtbar. Radioauswahl, Überspringen und neue Zusammenstellung sind noch nicht als gleichwertige Durchführung geprüft.';
}

function adapt(item: PublicItem): PolicyDraftItem {
  const study = PUBLIC_CATALOGUE.studies.find((entry) => entry.id === item.studyId)!;
  const name = study.id === 'ESS10SCe03_2' ? 'ESS10 Self-completion' : study.id.split('e')[0];
  const origin = `${name}, Datenausgabe ${study.edition}, Originalfrage ${item.originalQuestionId}`;
  const fieldworkLabel = study.fieldwork
    .map((period) => `${date(period.start)} bis ${date(period.end)}`)
    .join('; ');
  const modesLabel = [...new Set(study.fieldwork.flatMap((period) => period.modesDeclaredEn))]
    .map((mode) => {
      if (mode.includes('CAPI/CAMI'))
        return 'Persönliches computergestütztes Interview (CAPI/CAMI)';
      if (mode.includes('Paper')) return 'Selbstbeantwortung auf Papier';
      if (mode.includes('CAWI')) return 'Webselbstbeantwortung (CAWI)';
      return mode;
    })
    .join('; ');
  const stem = item.responseStemDe;
  const displayWording = stem
    ? item.groupId === 'migration_admission'
      ? [item.wordingDe, stem]
      : [stem, item.wordingDe]
    : [item.wordingDe];
  const [title, meaning] = ITEM_MEANINGS[item.variable]!;
  return Object.freeze({
    ...item,
    study,
    title,
    meaning,
    origin,
    fieldworkLabel,
    modesLabel,
    rubricTitle: POLICY_RUBRICS.find((rubric) => rubric.id === item.primaryTheme)!.title,
    displayWording: Object.freeze(displayWording),
    developmentNote: developmentNote(item),
    question: Object.freeze({
      id: item.id,
      primaryTheme: item.primaryTheme,
      // The public source explicitly binds these API/export codes to printed codes.
      categories: Object.freeze(item.categories.map((category) => category.code)),
      source: Object.freeze({
        studyId: item.studyId,
        originalQuestionId: item.originalQuestionId,
        sourceId: item.sourceRefs[0]!.sourceId,
        time: fieldworkLabel,
        population: study.populationDeclaredEn,
        mode: modesLabel,
      }),
    }),
  });
}

const originalById = new Map(PUBLIC_CATALOGUE.items.map((item) => [item.id, item]));
const ordered: PublicItem[] = [];
let blockAdded = false;
for (const item of PUBLIC_CATALOGUE.items) {
  if (!democracyIds.has(item.id)) ordered.push(item);
  else if (!blockAdded) {
    ordered.push(...democracy.itemIds.map((id) => originalById.get(id)!));
    blockAdded = true;
  }
}

export const POLICY_DRAFT_ITEMS = Object.freeze(ordered.map(adapt));
export const POLICY_DRAFT_QUESTIONS = Object.freeze(
  POLICY_DRAFT_ITEMS.map((item) => item.question),
);
