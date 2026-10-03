import { ChangeDetectionStrategy, Component } from '@angular/core';
import { PolicyDraft } from '../policy-draft/policy-draft';
import { REVIEWED_HISTORICAL_REFERENCES } from '../policy-draft/reviewed-historical-references';
import { REVIEWED_HISTORICAL_GROUPS } from '../policy-draft/reviewed-historical-groups';
import { REVIEWED_REFERENCES_V22 } from '../policy-draft/reviewed-references-v22';

/** Local review harness. Public builds use an empty research route list. */
@Component({
  standalone: true,
  imports: [PolicyDraft],
  template: `<app-policy-draft
    [historicalReferences]="references"
    [historicalGroups]="groups"
    [referencesV22]="referencesV22"
  />`,
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicyPreview {
  protected readonly references = REVIEWED_HISTORICAL_REFERENCES;
  protected readonly groups = REVIEWED_HISTORICAL_GROUPS;
  protected readonly referencesV22 = REVIEWED_REFERENCES_V22;
}
