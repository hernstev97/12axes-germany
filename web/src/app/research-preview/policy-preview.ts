import { ChangeDetectionStrategy, Component } from '@angular/core';
import { PolicyDraft } from '../policy-draft/policy-draft';
import { REVIEWED_HISTORICAL_REFERENCES } from '../policy-draft/reviewed-historical-references';
import { REVIEWED_HISTORICAL_GROUPS } from '../policy-draft/reviewed-historical-groups';

/** Local review harness. Public builds use an empty research route list. */
@Component({
  standalone: true,
  imports: [PolicyDraft],
  template: '<app-policy-draft [historicalReferences]="references" [historicalGroups]="groups" />',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicyPreview {
  protected readonly references = REVIEWED_HISTORICAL_REFERENCES;
  protected readonly groups = REVIEWED_HISTORICAL_GROUPS;
}
