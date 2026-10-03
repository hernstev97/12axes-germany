/** Public ESS instrument metadata only. No respondent rows or estimates. */
export interface PublicCategory {
  readonly code: string;
  readonly printedCodeDe: string;
  readonly labelDe: string;
  readonly labelEn: string;
  readonly isMissingApi: boolean;
  readonly semanticRole: string;
  readonly labelSourceRef: string;
}

export interface PublicCodeBinding {
  readonly sourceId: string;
  readonly sourceFieldId: string;
  readonly sourceFieldMetadataVersion: number;
  readonly dataFileMetadataId: string;
  readonly dataFileMetadataVersion: number;
}

export interface PublicItem {
  readonly id: string;
  readonly studyId: string;
  readonly variable: string;
  readonly primaryTheme: string;
  readonly originalQuestionId: string;
  readonly wordingDe: string;
  readonly introductionsDe: readonly string[];
  readonly responseStemDe: string | null;
  readonly situationDe: string | null;
  readonly instructionDe: string | null;
  readonly groupId: string;
  readonly originalOrderInGroup: number;
  readonly responseType: string;
  readonly sourceRefs: readonly {
    readonly sourceId: string;
    readonly pdfPages: readonly number[];
    readonly originalForm: string | null;
    readonly listLabelDe: string | null;
  }[];
  readonly categories: readonly PublicCategory[];
  readonly boundOriginalForm: string;
  readonly codeBinding: PublicCodeBinding;
  readonly apiValidCodeOrder: readonly string[];
  readonly missingCodes: readonly {
    readonly code: string;
    readonly reasonApi: string;
    readonly printedCodeDe: string | null;
    readonly labelDe: string | null;
    readonly isMissingApi: boolean;
  }[];
  readonly notAskedCodes: readonly string[];
}

export interface PublicStudy {
  readonly id: string;
  readonly edition: string;
  readonly dataDoiUrl: string;
  readonly documentationDoiUrl: string;
  readonly citationRequirementDeclaredEn: string;
  readonly country: string;
  readonly populationDeclaredEn: string;
  readonly populationCoverageLimit: string;
  readonly fieldwork: readonly {
    readonly start: string;
    readonly end: string;
    readonly modesDeclaredEn: readonly string[];
  }[];
  readonly versionNotes: readonly string[];
  readonly dataLicenseId: string;
  readonly documentationLicenseId: string;
  readonly samplingProceduresDeclaredEn: readonly string[];
}

export interface PublicCatalogue {
  readonly catalogueSha256: string;
  readonly attribution: {
    readonly creator: string;
    readonly archive: string;
    readonly licenses: readonly {
      readonly id: string;
      readonly name: string;
      readonly url: string;
      readonly appliesTo: string;
      readonly officialSourceRef: string;
    }[];
  };
  readonly studies: readonly PublicStudy[];
  readonly sources: readonly {
    readonly id: string;
    readonly kind: string;
    readonly publicUrl: string;
    readonly licenseId: string | null;
  }[];
  readonly groups: readonly {
    readonly id: string;
    readonly studyId: string;
    readonly originalQuestionRange: string;
    readonly introductionDe: string;
    readonly responseStemDe: string;
    readonly itemIds: readonly string[];
  }[];
  readonly items: readonly PublicItem[];
}

export function freezePublicMetadata<T>(value: T): T {
  if (value !== null && typeof value === 'object') {
    for (const child of Object.values(value)) freezePublicMetadata(child);
    Object.freeze(value);
  }
  return value;
}
