export interface HistoricalGroupReference {
  readonly weight: 'pspwght';
  readonly validCount: number;
  readonly totalCount: number;
  readonly missingCount: number;
  readonly notAskedCount: number;
  readonly categories: readonly { readonly code: string; readonly proportion: number }[];
  readonly uncertainty: null;
}

export type HistoricalGroupQuestion =
  | {
      readonly id: string;
      readonly status: 'reviewed_historical_reference';
      readonly reference: HistoricalGroupReference;
    }
  | {
      readonly id: string;
      readonly status: 'withheld_base_or_cell_count';
      readonly reference: null;
    };

export interface HistoricalVoteGroup {
  readonly id: string;
  readonly party2Code: string;
  readonly printedCodeDe: string;
  readonly label: string;
  readonly labelEnExactApi: string;
  readonly heterogeneousUnlabelledOther: boolean;
  readonly questions: readonly HistoricalGroupQuestion[];
}

export interface HistoricalGroupStudy {
  readonly id: string;
  readonly edition: string;
  readonly election: { readonly monthDe: string; readonly year: number };
  readonly fieldwork: readonly {
    readonly start: string;
    readonly end: string;
    readonly modesDeclaredEn: readonly string[];
  }[];
  readonly dataDoiUrl: string;
  readonly documentationDoiUrl: string;
  readonly voteVariable: string;
  readonly party2Variable: string;
  readonly originalQuestionId: string;
  readonly originalQuestionPages: readonly number[];
  readonly aliasBinding:
    | 'WIP_ORDERED_FORM_AND_API_LABEL_ASSOCIATION'
    | 'OFFICIAL_ALIAS_EXPLICIT_TEXT_BOUND';
  readonly aliasSourcePage: number | null;
  readonly dataLicenseId: 'ess-data-cc-by-nc-sa-4.0';
  readonly documentationLicenseId: 'ess-documentation-cc-by-sa-4.0';
  readonly attribution: string;
  readonly documents: readonly {
    readonly id: string;
    readonly publicUrl: string;
    readonly originalBytesSha256: string;
  }[];
  readonly publicReferencePath: string;
  readonly publicReferenceUrl: string;
  readonly publicReadmeUrl: string;
  readonly publicReferenceSha256: string;
  readonly groups: readonly HistoricalVoteGroup[];
}

export interface HistoricalGroupInput {
  readonly schemaVersion: 1;
  readonly status: 'reviewed_historical_descriptive_group_reference';
  readonly catalogueSha256: string;
  readonly rootDecisionSha256: string;
  readonly sourceManifestSha256: string;
  readonly methodsManifestSha256: string;
  readonly sourceOpinionReusedUnchanged: true;
  readonly studies: readonly HistoricalGroupStudy[];
}

/** Freeze the generated public projection, including nested category arrays. */
export function freezeHistoricalGroups<T>(value: T): T {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const child of Object.values(value)) freezeHistoricalGroups(child);
    Object.freeze(value);
  }
  return value;
}
