import type { PolicyQuestion } from '../research/policy-profile';
import type { PublicCategory, PublicItem, PublicStudy } from './catalogue-types';
import { ITEM_RULES } from './profile/profile-rules';
import { PUBLIC_CATALOGUE } from './public-catalogue';
import { PUBLIC_CATALOGUE_V22 } from './public-catalogue-v22';

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
  readonly rubricTitle: string;
  /** True for the 19 questions added by Analyseplan v2.2. */
  readonly addedInV22: boolean;
  /** Categories shown as answer options; excludes categories not read out originally. */
  readonly offeredCategories: readonly PublicCategory[];
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
    ? `${category.printedCodeDe ?? category.code}: ${category.labelDe}`
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
    return 'Originalkontext 2010/2011: Für die damals Befragten bezeichnete „heute“ die Strafpraxis der Feldzeit. Wer jetzt antwortet, bezieht „heute“ auf die Gegenwart. Einzelansicht und Durchführung auf dieser Website sind eine neue Entwicklungsfassung.';
  }
  if (item.contextNotes?.length) {
    return `Entwicklungsfassung: ${item.contextNotes.join(' ')} Radioauswahl, Überspringen und neue Zusammenstellung sind noch nicht als gleichwertige Durchführung geprüft.`;
  }
  return 'Entwicklungsfassung: Die gebundene nationale Papier- oder Interviewfassung bleibt als Originalkontext sichtbar. Radioauswahl, Überspringen und neue Zusammenstellung sind noch nicht als gleichwertige Durchführung geprüft.';
}

function adapt(item: PublicItem, addedInV22: boolean): PolicyDraftItem {
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
  const title = ITEM_RULES[item.id]!.title;
  const offeredCategories = Object.freeze(
    item.categories.filter((category) => category.offeredOnWebsite !== false),
  );
  return Object.freeze({
    ...item,
    study,
    title,
    addedInV22,
    offeredCategories,
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
      categories: Object.freeze(offeredCategories.map((category) => category.code)),
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

/** Analyseplan v2.2: each new question follows the last v2 question of its block or area. */
const V22_AFTER: Readonly<Record<string, readonly string[]>> = {
  'ESS8e02_3:eduunmp': ['ESS8e02_3:basinc'],
  'ESS10SCe03_2:scchpldm': ['ESS10SCe03_2:accalaw', 'ESS10SCe03_2:loylead', 'ESS5e03_6:prtyban'],
  'ESS5e03_6:rgbrklw': ['ESS10SCe03_2:panpriph', 'ESS10SCe03_2:panmonpb'],
  'ESS11e04_2:euftf': ['ESS8e02_3:eusclbf'],
  'ESS8e02_3:banhhap': [
    'ESS8e02_3:elgcoal',
    'ESS8e02_3:elgngas',
    'ESS8e02_3:elghydr',
    'ESS8e02_3:elgnuc',
    'ESS8e02_3:elgsun',
    'ESS8e02_3:elgwind',
    'ESS8e02_3:elgbio',
  ],
  'ESS8e02_3:imsclbn': ['ESS8e02_3:gvrfgap', 'ESS8e02_3:rfgbfml'],
  'ESS8e02_3:wrkprbf': ['ESS8e02_3:mnrgtjb', 'ESS10SCe03_2:freehms', 'ESS10SCe03_2:hmsacld'],
};
const v22ById = new Map(PUBLIC_CATALOGUE_V22.items.map((item) => [item.id, item]));
const merged: PolicyDraftItem[] = [];
for (const item of ordered) {
  merged.push(adapt(item, false));
  for (const id of V22_AFTER[item.id] ?? []) merged.push(adapt(v22ById.get(id)!, true));
}

export const POLICY_DRAFT_ITEMS = Object.freeze(merged);
export const POLICY_DRAFT_QUESTIONS = Object.freeze(
  POLICY_DRAFT_ITEMS.map((item) => item.question),
);
