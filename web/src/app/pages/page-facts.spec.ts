import { TestBed } from '@angular/core/testing';
import { Router } from '@angular/router';
import { App } from '../app';
import { appConfig } from '../app.config';
import { POLICY_DRAFT_ITEMS } from '../policy-draft/policy-catalogue';
import { REVIEWED_REFERENCES_V22 } from '../policy-draft/reviewed-references-v22';

// The public pages state counts by hand (Handbuch 7.2). This test binds them to the
// catalogue and the reviewed export, so a new export with other counts fails here.
const REVIEWED = 'reviewed_historical_reference';
const questions = POLICY_DRAFT_ITEMS.length;
const singles = REVIEWED_REFERENCES_V22.studies
  .flatMap((study) => study.questions)
  .filter((entry) => entry.status === REVIEWED).length;
const pairs = REVIEWED_REFERENCES_V22.studies
  .flatMap((study) => study.groups.flatMap((group) => group.pairs))
  .filter((entry) => entry.status === REVIEWED).length;
const added = POLICY_DRAFT_ITEMS.filter((item) => item.addedInV22).length;

async function pageText(url: string): Promise<string> {
  const fixture = TestBed.createComponent(App);
  await fixture.whenStable();
  await TestBed.inject(Router).navigateByUrl(url);
  await fixture.whenStable();
  return (fixture.nativeElement as HTMLElement).textContent!.replace(/\s+/g, ' ');
}

describe('Zahlen auf den öffentlichen Seiten', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
      providers: appConfig.providers,
    }).compileComponents();
  });

  it('entsprechen Katalog und geprüftem Export v2.2', async () => {
    expect([questions, added, singles, pairs]).toEqual([62, 19, 59, 96]);
    const home = await pageText('/');
    expect(home).toContain(`${questions} Originalfragen`);
    expect(home).toContain(`Für ${singles} der ${questions} Fragen`);
    expect(home).toContain(`${pairs} historische Wählergruppenreferenzen`);
    const project = await pageText('/projekt');
    expect(project).toContain(`${questions} Originalfragen`);
    expect(project).toContain(`Für ${singles} Fragen`);
    expect(project).toContain(`${pairs} historische Wählergruppenreferenzen`);
    const methodology = await pageText('/methodik');
    expect(methodology).toContain(`enthält ${questions} Fragen im deutschen Originalwortlaut`);
    expect(methodology).toContain(`${added} Fragen kamen mit dem`);
    expect(methodology).toContain(`Für ${singles} der ${questions} Fragen`);
  });
});
