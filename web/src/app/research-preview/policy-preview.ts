import { ChangeDetectionStrategy, Component } from '@angular/core';
import { PolicyDraft } from '../policy-draft/policy-draft';
import { REVIEWED_HISTORICAL_REFERENCES } from '../policy-draft/reviewed-historical-references';

/** Local review harness. Public builds use an empty research route list. */
@Component({
  standalone: true,
  imports: [PolicyDraft],
  template: '<app-policy-draft [historicalReferences]="references" />',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicyPreview {
  protected readonly references = REVIEWED_HISTORICAL_REFERENCES;
}
