import { ChangeDetectionStrategy, Component, computed, input } from '@angular/core';
import { categoryLabel, type PolicyDraftItem } from './policy-catalogue';
import { PUBLIC_CATALOGUE } from './public-catalogue';

@Component({
  selector: 'app-policy-source-details',
  standalone: true,
  templateUrl: './policy-source-details.html',
  styleUrl: './policy-source-details.scss',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class PolicySourceDetails {
  readonly item = input.required<PolicyDraftItem>();
  readonly showOriginal = input(false);
  protected readonly catalogue = PUBLIC_CATALOGUE;
  protected readonly categoryLabel = categoryLabel;
  protected readonly sources = computed(() =>
    this.item().sourceRefs.map((ref) => ({
      ...ref,
      url: `${PUBLIC_CATALOGUE.sources.find((source) => source.id === ref.sourceId)!.publicUrl}#page=${ref.pdfPages[0]}`,
      label: `${ref.listLabelDe ?? (ref.sourceId.includes('showcards') ? 'Originale Antwortlisten' : 'Deutsches Originalinstrument')}, PDF-Seiten ${ref.pdfPages.join(', ')}${ref.originalForm ? `, ${ref.originalForm}` : ''}`,
    })),
  );
  protected readonly codeSource = computed(
    () =>
      PUBLIC_CATALOGUE.sources.find((source) => source.id === this.item().codeBinding.sourceId)!,
  );
}
