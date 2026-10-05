import { type ComponentFixture, TestBed } from '@angular/core/testing';
import { PolicyDraft } from './policy-draft';
import { REVIEWED_HISTORICAL_REFERENCES } from './reviewed-historical-references';
import { REVIEWED_HISTORICAL_GROUPS } from './reviewed-historical-groups';
import { POLICY_DRAFT_ITEMS } from './policy-catalogue';
import { AUTO_ADVANCE_DELAY_MS } from './policy-question';
import type { ReferencesV22 } from './reference-v22';

// Synthetic v2.2 aggregates for display logic only. Not survey results.
const SYNTHETIC_V22: ReferencesV22 = {
  sources: {},
  studies: [
    {
      study: 'ESS9e03_3',
      designAvailable: true,
      questions: [
        {
          id: 'ESS9e03_3:sofrdst',
          status: 'reviewed_historical_reference',
          reference: {
            validCount: 500,
            totalCount: 510,
            missingCount: 10,
            notAskedCount: 0,
            categories: ['1', '2', '3', '4', '5'].map((code) => ({
              code,
              proportion: code === '1' ? 0 : 0.25,
              lower: code === '1' ? null : 0.15,
              upper: code === '1' ? null : 0.25,
            })),
            interval: { degreesOfFreedom: 89, strata: 89, psus: 178 },
          },
        },
      ],
      groups: [
        {
          groupId: 'ESS9e03_3:second_vote:1',
          pairs: [
            {
              questionId: 'ESS9e03_3:sofrdst',
              status: 'reviewed_historical_reference',
              reference: {
                validCount: 300,
                totalCount: 305,
                missingCount: 5,
                notAskedCount: 0,
                categories: ['1', '2', '3', '4', '5'].map((code) => ({
                  code,
                  proportion: 0.2,
                  lower: 0.12,
                  upper: 0.3,
                })),
                interval: { degreesOfFreedom: 89, strata: 89, psus: 178 },
              },
            },
          ],
        },
      ],
    },
    {
      study: 'ESS8e02_3',
      designAvailable: false,
      questions: [
        {
          id: 'ESS8e02_3:elgcoal',
          status: 'reviewed_historical_reference',
          reference: {
            validCount: 400,
            totalCount: 420,
            missingCount: 20,
            notAskedCount: 0,
            categories: ['1', '2', '3', '4', '5', '55'].map((code) => ({
              code,
              proportion: code === '55' ? 0 : 0.2,
              lower: null,
              upper: null,
            })),
            interval: null,
          },
        },
        { id: 'ESS8e02_3:elgngas', status: 'no_valid_answers', reference: null },
      ],
      groups: [
        {
          groupId: 'ESS8e02_3:second_vote:1',
          pairs: [
            {
              questionId: 'ESS8e02_3:elgcoal',
              status: 'reviewed_historical_reference',
              reference: {
                validCount: 150,
                totalCount: 160,
                missingCount: 10,
                notAskedCount: 0,
                categories: ['1', '2', '3', '4', '5', '55'].map((code) => ({
                  code,
                  proportion: code === '55' ? 0 : 0.2,
                  lower: null,
                  upper: null,
                })),
                interval: null,
              },
            },
          ],
        },
      ],
    },
  ],
};

const TOTAL = POLICY_DRAFT_ITEMS.length;
const E35_INDEX = POLICY_DRAFT_ITEMS.findIndex((item) => item.id === 'ESS8e02_3:wrkprbf') + 1;

describe('Unrouteter Angular-Fragen- und Ergebnisentwurf', () => {
  let fixture: ComponentFixture<PolicyDraft>;
  let element: HTMLElement;
  let restoreFocus: () => void;
  let originalScrollDescriptor: PropertyDescriptor | undefined;
  let headingInteractions: (
    | { kind: 'focus'; target: HTMLElement; options: FocusOptions | undefined }
    | {
        kind: 'scroll';
        target: HTMLElement;
        options: boolean | ScrollIntoViewOptions | undefined;
        focusedAtCall: Element | null;
      }
  )[];

  beforeEach(async () => {
    headingInteractions = [];
    const nativeFocus = HTMLElement.prototype.focus;
    const focusSpy = vi.spyOn(HTMLElement.prototype, 'focus').mockImplementation(function (
      this: HTMLElement,
      options?: FocusOptions,
    ) {
      headingInteractions.push({ kind: 'focus', target: this, options });
      nativeFocus.call(this, options);
    });
    restoreFocus = () => focusSpy.mockRestore();
    originalScrollDescriptor = Object.getOwnPropertyDescriptor(
      HTMLElement.prototype,
      'scrollIntoView',
    );
    // jsdom has no layout or scrollIntoView implementation. This testdouble
    // records the requested target/options and actual focus at the call only.
    Object.defineProperty(HTMLElement.prototype, 'scrollIntoView', {
      configurable: true,
      writable: true,
      value(this: HTMLElement, options?: boolean | ScrollIntoViewOptions) {
        headingInteractions.push({
          kind: 'scroll',
          target: this,
          options,
          focusedAtCall: document.activeElement,
        });
      },
    });
    await TestBed.configureTestingModule({ imports: [PolicyDraft] }).compileComponents();
    fixture = TestBed.createComponent(PolicyDraft);
    await fixture.whenStable();
    element = fixture.nativeElement as HTMLElement;
    // Start screen, then the introduction of questions 1 to 4, then question 1.
    await click('Zu den Fragen');
    // These tests check single steps. The automatic change has its own block below.
    await setAutoAdvance(false);
    await click('Zu Frage 1');
  });

  afterEach(() => {
    restoreFocus();
    if (originalScrollDescriptor) {
      Object.defineProperty(HTMLElement.prototype, 'scrollIntoView', originalScrollDescriptor);
    } else {
      Reflect.deleteProperty(HTMLElement.prototype, 'scrollIntoView');
    }
  });

  async function click(text: string): Promise<void> {
    const button = [...element.querySelectorAll('button')].find(
      (candidate) => candidate.textContent?.trim() === text,
    );
    if (!button) throw Error(`Missing native button: ${text}`);
    button.click();
    await fixture.whenStable();
  }

  async function choose(code: string): Promise<void> {
    const radio = element.querySelector<HTMLInputElement>(`input[type="radio"][value="${code}"]`)!;
    radio.click();
    await fixture.whenStable();
  }

  async function setAutoAdvance(on: boolean): Promise<void> {
    const toggle = element.querySelector<HTMLInputElement>('#draft-auto-advance')!;
    if (toggle.checked !== on) toggle.click();
    await fixture.whenStable();
  }

  async function selectComparison(id: string, value: string): Promise<void> {
    const select = element.querySelector<HTMLSelectElement>(`#${id}`)!;
    select.value = value;
    select.dispatchEvent(new Event('change'));
    await fixture.whenStable();
  }

  function expectFocusedAndScrolled(target: HTMLElement): void {
    expect(document.activeElement).toBe(target);
    expect(headingInteractions).toEqual([
      { kind: 'focus', target, options: { preventScroll: true } },
      {
        kind: 'scroll',
        target,
        options: { block: 'start', inline: 'nearest', behavior: 'instant' },
        focusedAtCall: target,
      },
    ]);
  }

  async function openLastQuestion(): Promise<void> {
    await click('Zur Fragenübersicht');
    element.querySelector<HTMLButtonElement>('.overview-list li:last-child button')!.click();
    await fixture.whenStable();
  }

  it('zeigt v2.2-Bereiche, neue Referenzen, fehlende gültige Antworten und neue Gruppenpaare', async () => {
    fixture.componentRef.setInput('historicalReferences', REVIEWED_HISTORICAL_REFERENCES);
    fixture.componentRef.setInput('historicalGroups', REVIEWED_HISTORICAL_GROUPS);
    fixture.componentRef.setInput('referencesV22', SYNTHETIC_V22);
    await click('Zum Ergebnisentwurf');
    const withInterval = element.querySelector<HTMLElement>(
      '[data-question-id="ESS9e03_3:sofrdst"]',
    )!;
    expect(withInterval.querySelectorAll('.interval').length).toBe(4);
    expect(withInterval.querySelectorAll('.interval-none')).toHaveLength(1);
    expect(withInterval.querySelector('.interval-missing')).toBeNull();
    expect(withInterval.querySelector('.interval')?.textContent).toMatch(/15,0\s%\sbis 25,0\s%/);
    expect(withInterval.querySelector('.interval-note')).toBeNull();
    const explanation = element.querySelectorAll('.interval-note');
    expect(explanation).toHaveLength(1);
    expect(explanation[0]!.textContent).toContain('keine Unsicherheit der');
    expect(explanation[0]!.textContent).toContain('Messfehler einzelner Antworten');
    const added = element.querySelector<HTMLElement>('[data-question-id="ESS8e02_3:elgcoal"]')!;
    expect(added.querySelector('.historical-reference')).not.toBeNull();
    expect(added.querySelector('.interval')).toBeNull();
    expect(added.querySelector('.interval-missing')?.textContent).toContain('Stichprobendesign');
    const empty = element.querySelector<HTMLElement>('[data-question-id="ESS8e02_3:elgngas"]')!;
    expect(empty.querySelector('.reference-no-valid')).not.toBeNull();
    expect(empty.querySelector('.historical-reference')).toBeNull();
    await selectComparison('draft-group-study', 'ESS8e02_3');
    await selectComparison('draft-vote-group', 'ESS8e02_3:second_vote:1');
    const pair = element.querySelector<HTMLElement>(
      '[data-question-id="ESS8e02_3:elgcoal"] .group-reference',
    );
    expect(pair).not.toBeNull();
    expect(pair!.querySelectorAll('[data-category-code]')).toHaveLength(6);
    expect(pair!.querySelector('.interval-note')).toBeNull();
    expect(pair!.querySelector('.interval')).toBeNull();
    expect(pair!.querySelector('.interval-missing')?.textContent).toContain(
      'keine Unsicherheit von null',
    );
    expect(element.querySelectorAll('.interval-note')).toHaveLength(1);
    await selectComparison('draft-group-study', 'ESS9e03_3');
    await selectComparison('draft-vote-group', 'ESS9e03_3:second_vote:1');
    const ess9Pair = element.querySelector<HTMLElement>(
      '[data-question-id="ESS9e03_3:sofrdst"] .group-reference',
    )!;
    expect(ess9Pair.querySelectorAll('.interval').length).toBe(5);
    expect(ess9Pair.querySelector('.interval-note')).toBeNull();
    expect(element.querySelector('.interval-note')?.textContent).toContain(
      'kein Test auf Unterschiede zwischen Gruppen',
    );
  }, 20_000);
  it('T30: zeigt bei zurückgehaltener Referenz keine Zahlen, behält aber die eigene Aussage', async () => {
    fixture.componentRef.setInput('historicalReferences', REVIEWED_HISTORICAL_REFERENCES);
    await click('Zur Fragenübersicht');
    const target = POLICY_DRAFT_ITEMS.findIndex((item) => item.id === 'ESS10SCe03_2:cttresa');
    element.querySelectorAll<HTMLButtonElement>('.overview-list li button')[target]!.click();
    await fixture.whenStable();
    await choose('9');
    await click('Zum Ergebnisentwurf');
    const article = element.querySelector<HTMLElement>(
      '[data-question-id="ESS10SCe03_2:cttresa"]',
    )!;
    expect(article.querySelector('.profile-statement')?.textContent).toContain(': 9 (0 = ');
    expect(article.querySelector('.reference-withheld')).not.toBeNull();
    expect(article.querySelector('.same-category')).toBeNull();
    expect(article.querySelector('.historical-reference')).toBeNull();
    expect(article.textContent).not.toMatch(/\d+(?:,\d+)? %/);
  });
  it('zeigt das erklärende Profil mit Blockmuster, Querbezug, markierter eigener Antwort und Lücken', async () => {
    fixture.componentRef.setInput('historicalReferences', REVIEWED_HISTORICAL_REFERENCES);
    await choose('1');
    await click('Nächste Frage');
    await choose('5');
    await click('Zum Ergebnisentwurf');
    const block = element.querySelector<HTMLElement>('[data-block-id="justice_principles"]')!;
    expect(block.textContent).toContain('Zustimmung: Gleichheit.');
    expect(block.textContent).toContain('Ablehnung: Leistung.');
    expect(block.textContent).toContain('kein Widerspruch');
    const first = element.querySelector<HTMLElement>('[data-question-id="ESS9e03_3:sofrdst"]')!;
    expect(first.querySelector('.profile-statement')?.textContent).toContain(
      'Zustimmung zur Aussage „Eine Gesellschaft ist gerecht',
    );
    expect(first.querySelectorAll('.own-answer-label')).toHaveLength(1);
    const missing = first.querySelector('.interval-missing')?.textContent ?? '';
    expect(missing).toContain('keine Unsicherheit von null');
    expect(missing).not.toContain('Stichprobendesign');
    expect(first.querySelector('.same-category')?.textContent).toContain('Dieselbe Kategorie');
    expect(element.querySelector('#draft-cross-title')).not.toBeNull();
    expect(element.querySelectorAll('.profile-cross')).toHaveLength(0);
    const uncovered = element.querySelector<HTMLElement>('.uncovered-areas')!;
    expect(uncovered.textContent).toContain('Außen-, Verteidigungs- und Friedenspolitik');
    expect(uncovered.textContent).toContain('Gesundheit und Pflege');
    expect(element.querySelector('.area-scope')?.textContent).toContain('Nicht erfasst');
    expect(element.textContent).not.toMatch(
      /(?<!\p{L})(?:links|rechts|konservativ|liberal|populistisch)(?!\p{L})/iu,
    );
  });
  it('hält native Radios bei Eingaben schneller als ein Renderzyklus am Sitzungszustand', async () => {
    const radios = () => [...element.querySelectorAll<HTMLInputElement>('input[type="radio"]')];
    await choose('1');
    // Select again and reset before Angular renders: the session ends untouched.
    radios()[1]!.click();
    const reset = [...element.querySelectorAll('button')].find(
      (button) => button.textContent?.trim() === 'Auswahl zurücksetzen',
    )!;
    reset.click();
    await fixture.whenStable();
    expect(radios().some((radio) => radio.checked)).toBe(false);
    // Select and move on before Angular renders: the next question starts unchecked.
    radios()[1]!.click();
    await click('Nächste Frage');
    expect(radios().some((radio) => radio.checked)).toBe(false);
  });
  it('Zurücksetzen führt den Fokus vom danach entfernten Button zur Frage', async () => {
    await choose('1');
    const reset = [...element.querySelectorAll('button')].find(
      (button) => button.textContent?.trim() === 'Auswahl zurücksetzen',
    )!;
    reset.focus();
    headingInteractions = [];
    await click('Auswahl zurücksetzen');
    expect(reset.isConnected).toBe(false);
    expect(element.querySelector('input[type="radio"]:checked')).toBeNull();
    expectFocusedAndScrolled(element.querySelector<HTMLElement>('#draft-question-title')!);
  });

  it.each([
    ['Nächste Frage', `Frage 3 von ${TOTAL}`],
    ['Vorherige Frage', `Frage 1 von ${TOTAL}`],
    ['Frage überspringen', `Frage 3 von ${TOTAL}`],
  ])('Fokus und Scrollen folgen dem gerenderten Fragenwechsel durch %s', async (action, title) => {
    await click('Nächste Frage');
    headingInteractions = [];
    await click(action);
    const heading = element.querySelector<HTMLElement>('#draft-question-title')!;
    expect(heading.textContent).toContain(title);
    expectFocusedAndScrolled(heading);
  });

  it.each([
    ['den Fragen', null, 'Zur Fragenübersicht', 'Fragenübersicht'],
    ['den Fragen', null, 'Zum Ergebnisentwurf', 'Ergebnisentwurf'],
    ['der Übersicht', 'Zur Fragenübersicht', 'Zum Ergebnisentwurf', 'Ergebnisentwurf'],
    ['dem Ergebnis', 'Zum Ergebnisentwurf', 'Zur Fragenübersicht', 'Fragenübersicht'],
  ])(
    'Fokus und Scrollen folgen der gerenderten Ansichtsüberschrift von %s durch %s',
    async (_from, fromAction, action, title) => {
      if (fromAction) await click(fromAction);
      headingInteractions = [];
      await click(action);
      const heading = element.querySelector<HTMLElement>('h1')!;
      expect(heading.textContent).toContain(title);
      expectFocusedAndScrolled(heading);
    },
  );

  it.each(['Zur Fragenübersicht', 'Zum Ergebnisentwurf'])(
    'Fokus und Scrollen führen von %s zurück zur gerenderten Frage',
    async (fromAction) => {
      await click(fromAction);
      headingInteractions = [];
      await click('Zu den Fragen');
      const heading = element.querySelector<HTMLElement>('#draft-question-title')!;
      expect(heading.textContent).toContain(`Frage 1 von ${TOTAL}`);
      expectFocusedAndScrolled(heading);
      expect(element.querySelector('h1')?.textContent).toContain('Fragenentwurf');
    },
  );

  it('Fokus und Scrollen führen von der letzten Übersichtsfrage zur gerenderten letzten Frage', async () => {
    await click('Zur Fragenübersicht');
    headingInteractions = [];
    element.querySelector<HTMLButtonElement>('.overview-list li:last-child button')!.click();
    await fixture.whenStable();
    const heading = element.querySelector<HTMLElement>('#draft-question-title')!;
    expect(heading.textContent).toContain(`Frage ${TOTAL} von ${TOTAL}`);
    expectFocusedAndScrolled(heading);
  });

  it('Fokus und Scrollen führen beim nativen Bearbeiten des letzten Ergebnisses zur gerenderten E35-Frage', async () => {
    await click('Zum Ergebnisentwurf');
    headingInteractions = [];
    element
      .querySelector<HTMLButtonElement>('[data-question-id="ESS8e02_3:wrkprbf"] button')!
      .click();
    await fixture.whenStable();
    const heading = element.querySelector<HTMLElement>('#draft-question-title')!;
    expect(heading.textContent).toContain(`Frage ${E35_INDEX} von ${TOTAL}`);
    expect(element.textContent).toContain('Originalfrage E35');
    expectFocusedAndScrolled(heading);
  });

  it.each(['Zum Ergebnisentwurf', 'Frage überspringen'])(
    'Fokus und Scrollen führen nach der letzten Frage durch %s zur Ergebnisüberschrift',
    async (action) => {
      await openLastQuestion();
      headingInteractions = [];
      const controls = action === 'Zum Ergebnisentwurf' ? '.question-controls' : '.skip-controls';
      const button = [...element.querySelectorAll<HTMLButtonElement>(`${controls} button`)].find(
        (candidate) => candidate.textContent?.trim() === action,
      )!;
      button.click();
      await fixture.whenStable();
      const heading = element.querySelector<HTMLElement>('h1')!;
      expect(heading.textContent).toContain('Ergebnisentwurf');
      expectFocusedAndScrolled(heading);
    },
  );

  it('Fokus und Scrollen werden bei einer bloßen Auswahl nicht neu angefordert', async () => {
    headingInteractions = [];
    await choose('2');
    expect(headingInteractions).toEqual([]);
    expect(element.querySelector<HTMLInputElement>('input[value="2"]')?.checked).toBe(true);
  });

  it('behält Originalauswahl beim Zurückgehen und bearbeitet sie ohne andere Antworten zu ändern', async () => {
    await choose('2');
    await click('Nächste Frage');
    expect(element.querySelector('#draft-question-title')?.textContent).toContain('Frage 2');
    expect(document.activeElement?.id).toBe('draft-question-title');
    await choose('5');
    await click('Vorherige Frage');
    expect(element.querySelector<HTMLInputElement>('input[value="2"]')?.checked).toBe(true);
    await choose('1');
    await click('Nächste Frage');
    expect(element.querySelector<HTMLInputElement>('input[value="5"]')?.checked).toBe(true);
    await click('Zum Ergebnisentwurf');
    expect(element.querySelector('[data-question-id="ESS9e03_3:sofrdst"]')?.textContent).toContain(
      'Gewählte Originalkategorie: Stimme stark zu',
    );
    expect(element.querySelector('[data-question-id="ESS9e03_3:sofrwrk"]')?.textContent).toContain(
      'Gewählte Originalkategorie: Lehne stark ab',
    );
    expect(element.querySelectorAll('h1')).toHaveLength(1);
  });

  it('trennt unberührt und bewusst übersprungen, ermöglicht Teilresultat und Bearbeitung', async () => {
    await click('Nächste Frage');
    const reason = element.querySelector<HTMLSelectElement>('#draft-skip-reason')!;
    reason.value = 'dont-know';
    reason.dispatchEvent(new Event('change'));
    await click('Frage überspringen');
    await click('Zum Ergebnisentwurf');
    const first = element.querySelector<HTMLElement>('[data-question-id="ESS9e03_3:sofrdst"]')!;
    const second = element.querySelector<HTMLElement>('[data-question-id="ESS9e03_3:sofrwrk"]')!;
    expect(first.textContent).toContain('Unberührt');
    expect(second.textContent).toContain('Grund dieser Entwurfssitzung: Weiß nicht');
    expect(second.textContent).toContain('keinem Missing-Code');
    expect(second.textContent).not.toContain('Gewählte Originalkategorie');
    expect(element.querySelectorAll('.result-item')).toHaveLength(TOTAL);
    second.querySelector('button')!.click();
    await fixture.whenStable();
    expect(element.querySelector('#draft-question-title')?.textContent).toContain('Frage 2');
    await choose('3');
    await click('Zum Ergebnisentwurf');
    expect(element.querySelector('[data-question-id="ESS9e03_3:sofrwrk"]')?.textContent).toContain(
      'Gewählte Originalkategorie: Weder noch',
    );
    expect(
      element.querySelector('[data-question-id="ESS9e03_3:sofrwrk"]')?.textContent,
    ).not.toContain('Grund dieser Entwurfssitzung');
  });

  it('bietet die native Radio-Gruppe und zeigt ohne Referenzeingabe keine historischen Zahlen', async () => {
    expect(element.querySelector('fieldset legend')?.textContent).toContain(
      'Einkommen und Vermögen',
    );
    expect(element.querySelector('fieldset')?.getAttribute('aria-describedby')).toBe(
      'draft-development-note',
    );
    expect(element.textContent).not.toContain('Nun einige Fragen zur Gesellschaft');
    expect(
      element.querySelectorAll('input[type="radio"][name="draft-original-answer"]'),
    ).toHaveLength(5);
    await click('Zum Ergebnisentwurf');
    expect(element.querySelectorAll('.historical-reference')).toHaveLength(0);
    expect(element.textContent).toContain(
      'Historische Vergleichswerte sind in dieser Fassung noch nicht eingebunden',
    );
    expect(element.textContent).toContain(
      'Texte und Ergebnisdarstellung wurden noch nicht mit Menschen',
    );
    expect(element.querySelectorAll('section h2')).toHaveLength(11);
  });

  it('zeigt Druckcodes und bewahrt den zugeordneten Exportcode bei der Auswahl', async () => {
    await click('Zur Fragenübersicht');
    const question = [...element.querySelectorAll('button')].find((button) =>
      button.textContent?.includes('Originalfrage B37'),
    )!;
    question.click();
    await fixture.whenStable();
    expect(element.querySelector('input[value="0"]')?.parentElement?.textContent).toContain(
      '00: Einigung ist schon zu weit gegangen',
    );
    await choose('0');
    await click('Zum Ergebnisentwurf');
    expect(element.querySelector('[data-question-id="ESS11e04_2:euftf"]')?.textContent).toContain(
      'Gewählte Originalkategorie: 00: Einigung ist schon zu weit gegangen',
    );
  });

  it('überträgt, speichert und codiert beim lokalen Durchgang keine Antworten in URLs', async () => {
    const storage = vi.spyOn(Storage.prototype, 'setItem');
    const fetch = vi.spyOn(globalThis, 'fetch');
    const locationBefore = window.location.href;
    await choose('4');
    await click('Nächste Frage');
    await click('Frage überspringen');
    await click('Zum Ergebnisentwurf');
    expect(storage).not.toHaveBeenCalled();
    expect(fetch).not.toHaveBeenCalled();
    expect(window.location.href).toBe(locationBefore);
    storage.mockRestore();
    fetch.mockRestore();
  });

  it('unterdrückt eine falsch gebundene Referenzeingabe vollständig', async () => {
    fixture.componentRef.setInput('historicalReferences', {
      catalogueSha256: 'wrong-source',
      references: [],
    });
    await click('Zum Ergebnisentwurf');
    expect(element.querySelectorAll('.historical-reference')).toHaveLength(0);
    expect(element.querySelector('[role="status"]')?.textContent).toContain(
      'passt nicht zu den gebundenen Originalquellen',
    );
  });

  it('zeigt die 42 echten Einzelreferenzen mit getrennten Fallzahlen und hält cttresa ohne Zahlen', async () => {
    fixture.componentRef.setInput('historicalReferences', REVIEWED_HISTORICAL_REFERENCES);
    await click('Zum Ergebnisentwurf');
    expect(element.querySelectorAll('.historical-reference')).toHaveLength(42);
    const withheld = element.querySelector<HTMLElement>(
      '[data-question-id="ESS10SCe03_2:cttresa"]',
    )!;
    expect(withheld.querySelector('.historical-reference')).toBeNull();
    expect(withheld.querySelector('.reference-counts')).toBeNull();
    expect(withheld.querySelector('.reference-withheld')?.textContent).toContain(
      'bleibt wegen unzureichender',
    );
    const actual = REVIEWED_HISTORICAL_REFERENCES.references.find(
      (reference) => reference.questionId === 'ESS11e04_2:euftf',
    )!;
    const displayed = element.querySelector<HTMLElement>(
      '[data-question-id="ESS11e04_2:euftf"] .historical-reference',
    )!;
    expect(displayed.textContent).toContain('9. Mai 2023 bis 21. Dezember 2023');
    expect(displayed.textContent).toContain('pspwght');
    const counts = [...displayed.querySelectorAll('.reference-counts dd')].map((count) =>
      count.textContent?.trim(),
    );
    expect(counts).toEqual(
      [
        actual.validUnweightedN,
        actual.totalUnweightedN,
        actual.missingUnweightedN,
        actual.notAskedUnweightedN,
      ].map(String),
    );
    fixture.componentRef.setInput('historicalReferences', null);
    await fixture.whenStable();
    expect(element.querySelectorAll('.historical-reference')).toHaveLength(0);
    expect(element.querySelectorAll('.reference-withheld')).toHaveLength(0);
  });

  it('beginnt optional ohne Vergleichsgruppe und erhält alle ursprünglichen Parteien und Other in ihrer Reihenfolge', async () => {
    await click('Zum Ergebnisentwurf');
    expect(element.querySelector('#draft-group-study')).toBeNull();
    fixture.componentRef.setInput('historicalGroups', REVIEWED_HISTORICAL_GROUPS);
    await fixture.whenStable();
    const studySelect = element.querySelector<HTMLSelectElement>('#draft-group-study')!;
    const groupSelect = element.querySelector<HTMLSelectElement>('#draft-vote-group')!;
    expect(studySelect.value).toBe('');
    expect(groupSelect.value).toBe('');
    expect(groupSelect.disabled).toBe(true);
    expect(element.querySelectorAll('.group-reference')).toHaveLength(0);
    for (const study of REVIEWED_HISTORICAL_GROUPS.studies) {
      await selectComparison('draft-group-study', study.id);
      const options = [...groupSelect.options].slice(1);
      expect(options.map((option) => option.value)).toEqual(study.groups.map((group) => group.id));
      expect(options.map((option) => option.textContent?.trim())).toEqual(
        study.groups.map((group) =>
          group.heterogeneousUnlabelledOther ? 'Andere Partei (heterogener Rest)' : group.label,
        ),
      );
    }
    expect([...groupSelect.options].map((option) => option.textContent?.trim())).toContain('NPD');
    expect(groupSelect.options[groupSelect.options.length - 1]!.textContent?.trim()).toBe(
      'Andere Partei (heterogener Rest)',
    );
    expect(element.querySelectorAll('h1')).toHaveLength(1);
    expect(element.querySelectorAll('section h2')).toHaveLength(11);
  });

  it('zeigt nur echte gleichstudienbezogene Gruppenanteile und den gültigen Fragenenner neben getrennten Missing-Fällen', async () => {
    fixture.componentRef.setInput('historicalGroups', REVIEWED_HISTORICAL_GROUPS);
    await click('Zum Ergebnisentwurf');
    await selectComparison('draft-group-study', 'ESS9e03_3');
    await selectComparison('draft-vote-group', 'ESS9e03_3:second_vote:1');
    const actual = REVIEWED_HISTORICAL_GROUPS.studies[2]!.groups[0]!.questions[0]!.reference!;
    const approved = element.querySelector<HTMLElement>(
      '[data-question-id="ESS9e03_3:sofrdst"] .group-reference',
    )!;
    expect(approved.textContent).toContain('September 2017');
    expect(approved.textContent).toContain('29.08.2018 bis 04.03.2019');
    expect(approved.textContent).toContain('pspwght');
    expect(
      [...approved.querySelectorAll('[data-category-code]')].map((row) =>
        row.getAttribute('data-category-code'),
      ),
    ).toEqual(actual.categories.map((category) => category.code));
    const percent = new Intl.NumberFormat('de-DE', {
      style: 'percent',
      minimumFractionDigits: 1,
      maximumFractionDigits: 1,
    });
    expect(
      [...approved.querySelectorAll('.group-proportions dd')].map((row) => row.textContent?.trim()),
    ).toEqual(actual.categories.map((category) => percent.format(category.proportion)));
    expect(
      [...approved.querySelectorAll('.group-counts dd')].map((row) => row.textContent?.trim()),
    ).toEqual(
      [actual.validCount, actual.totalCount, actual.missingCount, actual.notAskedCount].map(String),
    );
    const withheld = element.querySelector<HTMLElement>('[data-question-id="ESS9e03_3:sofrwrk"]')!;
    expect(withheld.querySelector('.group-reference')).toBeNull();
    expect(withheld.querySelector('.group-unavailable')?.textContent).toContain(
      'weder null Prozent noch eine mittlere Position',
    );
    expect(
      element.querySelector('[data-question-id="ESS8e02_3:wrkprbf"] .group-other-study')
        ?.textContent,
    ).toContain('anderen Studie');
  });

  it('setzt beim Studienwechsel die Gruppe zurück und zeigt für Other keine Basis oder Prozentzahl', async () => {
    fixture.componentRef.setInput('historicalGroups', REVIEWED_HISTORICAL_GROUPS);
    await click('Zum Ergebnisentwurf');
    await selectComparison('draft-group-study', 'ESS9e03_3');
    await selectComparison('draft-vote-group', 'ESS9e03_3:second_vote:1');
    expect(element.querySelectorAll('.group-reference')).toHaveLength(2);
    await selectComparison('draft-group-study', 'ESS8e02_3');
    expect(element.querySelector<HTMLSelectElement>('#draft-vote-group')!.value).toBe('');
    expect(element.querySelectorAll('.group-reference')).toHaveLength(0);
    await selectComparison('draft-vote-group', 'ESS8e02_3:second_vote:9');
    expect(element.querySelectorAll('.group-reference')).toHaveLength(0);
    expect(element.querySelectorAll('.group-counts')).toHaveLength(0);
    expect(element.querySelectorAll('.group-proportions')).toHaveLength(0);
    expect(element.querySelectorAll('.group-unavailable')).toHaveLength(
      POLICY_DRAFT_ITEMS.filter((item) => item.studyId === 'ESS8e02_3').length,
    );
    expect(element.querySelector('.group-other-limit')?.textContent).toContain(
      'heterogene, unbenannte Rest',
    );
    expect(element.querySelector('.group-other-limit')?.textContent).toContain('„Other“');
    expect(element.querySelector('.group-coverage')?.textContent).toMatch(
      /Anteile zu 0 von \d+ Fragen dieser Studie/,
    );
    expect(element.querySelector('.group-coverage-limit')?.textContent).toContain('In München');
    expect(element.querySelector('.group-sources')?.textContent).toContain('schwächer als');
    expect(
      element.querySelector('.group-sources a[href="https://doi.org/10.21338/ess8e02_3"]'),
    ).not.toBeNull();
    expect(
      element.querySelector(
        '.group-sources a[href="https://creativecommons.org/licenses/by-nc-sa/4.0/"]',
      ),
    ).not.toBeNull();
  });

  it('unterdrückt ein eingeschleustes Gruppenobjekt und erhält die 42 unabhängigen Einzelreferenzen', async () => {
    fixture.componentRef.setInput('historicalReferences', REVIEWED_HISTORICAL_REFERENCES);
    fixture.componentRef.setInput('historicalGroups', structuredClone(REVIEWED_HISTORICAL_GROUPS));
    await click('Zum Ergebnisentwurf');
    expect(element.querySelector('.group-rejected')?.textContent).toContain(
      'nicht der gebundene öffentliche Adapter',
    );
    expect(element.querySelector('#draft-group-study')).toBeNull();
    expect(element.querySelectorAll('.group-reference')).toHaveLength(0);
    expect(element.querySelectorAll('.historical-reference')).toHaveLength(42);
  });

  it('hält Gruppenwahl und Antworten in RAM unabhängig, auch beim Bearbeiten und Zurückgehen ohne URL, Speicher oder Netzwerk', async () => {
    const storage = vi.spyOn(Storage.prototype, 'setItem');
    const fetch = vi.spyOn(globalThis, 'fetch');
    const locationBefore = window.location.href;
    try {
      fixture.componentRef.setInput('historicalGroups', REVIEWED_HISTORICAL_GROUPS);
      await choose('4');
      await click('Nächste Frage');
      await click('Frage überspringen');
      await click('Zum Ergebnisentwurf');
      await selectComparison('draft-group-study', 'ESS9e03_3');
      await selectComparison('draft-vote-group', 'ESS9e03_3:second_vote:5');
      const groupSelect = element.querySelector<HTMLSelectElement>('#draft-vote-group')!;
      groupSelect.focus();
      headingInteractions = [];
      await selectComparison('draft-vote-group', 'ESS9e03_3:second_vote:6');
      expect(document.activeElement).toBe(groupSelect);
      expect(headingInteractions).toEqual([]);
      element
        .querySelector<HTMLButtonElement>('[data-question-id="ESS9e03_3:sofrdst"] button')!
        .click();
      await fixture.whenStable();
      expect(element.querySelector<HTMLInputElement>('input[value="4"]')!.checked).toBe(true);
      await click('Nächste Frage');
      expect(element.textContent).toContain('Übersprungen');
      await click('Zum Ergebnisentwurf');
      expect(element.querySelector<HTMLSelectElement>('#draft-vote-group')!.value).toBe(
        'ESS9e03_3:second_vote:6',
      );
      expect(
        element.querySelector('[data-question-id="ESS9e03_3:sofrdst"]')?.textContent,
      ).toContain('Gewählte Originalkategorie: Lehne ab');
      expect(storage).not.toHaveBeenCalled();
      expect(fetch).not.toHaveBeenCalled();
      expect(window.location.href).toBe(locationBefore);
      fixture.destroy();
      fixture = TestBed.createComponent(PolicyDraft);
      await fixture.whenStable();
      element = fixture.nativeElement as HTMLElement;
      fixture.componentRef.setInput('historicalGroups', REVIEWED_HISTORICAL_GROUPS);
      await click('Zum Ergebnisentwurf');
      expect(element.querySelector<HTMLSelectElement>('#draft-group-study')!.value).toBe('');
      expect(element.textContent).toContain('0 beantwortet');
    } finally {
      storage.mockRestore();
      fetch.mockRestore();
    }
  }, 20_000);

  describe('automatischer Wechsel nach einer Antwort', () => {
    const heading = () => element.querySelector<HTMLElement>('#draft-question-title')!;
    const radio = (code: string) =>
      element.querySelector<HTMLInputElement>(`input[type="radio"][value="${code}"]`)!;

    async function afterDelay(): Promise<void> {
      await new Promise((resolve) => setTimeout(resolve, AUTO_ADVANCE_DELAY_MS + 50));
      await fixture.whenStable();
    }

    beforeEach(async () => {
      await setAutoAdvance(true);
      headingInteractions = [];
    });

    it('ist zu Beginn eingeschaltet und als Schalter vor den Antworten beschriftet', async () => {
      const fresh = TestBed.createComponent(PolicyDraft);
      await fresh.whenStable();
      const freshElement = fresh.nativeElement as HTMLElement;
      for (const text of ['Zu den Fragen', 'Zu Frage 1']) {
        [...freshElement.querySelectorAll('button')]
          .find((button) => button.textContent?.trim() === text)!
          .click();
        await fresh.whenStable();
      }
      const toggle = freshElement.querySelector<HTMLInputElement>('#draft-auto-advance')!;
      expect(toggle.checked).toBe(true);
      expect(toggle.getAttribute('role')).toBe('switch');
      expect(toggle.closest('label')?.textContent?.trim()).toBe(
        'Nach einer Antwort automatisch zur nächsten Frage',
      );
      const firstRadio = freshElement.querySelector('input[type="radio"]')!;
      expect(toggle.compareDocumentPosition(firstRadio) & Node.DOCUMENT_POSITION_FOLLOWING).toBe(
        Node.DOCUMENT_POSITION_FOLLOWING,
      );
      fresh.destroy();
    });

    it('wechselt nach einer Auswahl mit kurzer Pause zur nächsten Frage und behält die Antwort', async () => {
      await choose('2');
      expect(heading().textContent).toContain(`Frage 1 von ${TOTAL}`);
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 2 von ${TOTAL}`);
      expectFocusedAndScrolled(heading());
      await click('Vorherige Frage');
      expect(radio('2').checked).toBe(true);
    });

    it('wechselt auch beim erneuten Bestätigen einer schon gewählten Antwort', async () => {
      await choose('2');
      await afterDelay();
      await click('Vorherige Frage');
      radio('2').click();
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 2 von ${TOTAL}`);
    });

    it('wählt mit Pfeiltasten ohne Wechsel', async () => {
      const fieldset = element.querySelector('#draft-answer-fieldset')!;
      fieldset.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true }));
      radio('3').click();
      fieldset.dispatchEvent(new KeyboardEvent('keyup', { key: 'ArrowDown', bubbles: true }));
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 1 von ${TOTAL}`);
      expect(radio('3').checked).toBe(true);
      expect(headingInteractions).toEqual([]);
    });

    it('bestätigt eine mit Pfeiltasten gewählte Antwort mit Leertaste oder Eingabetaste', async () => {
      for (const key of [' ', 'Enter']) {
        const fieldset = element.querySelector('#draft-answer-fieldset')!;
        fieldset.dispatchEvent(new KeyboardEvent('keydown', { key: 'ArrowDown', bubbles: true }));
        radio('2').click();
        fieldset.dispatchEvent(new KeyboardEvent('keyup', { key: 'ArrowDown', bubbles: true }));
        await fixture.whenStable();
        radio('2').dispatchEvent(new KeyboardEvent('keyup', { key, bubbles: true }));
        await afterDelay();
        expect(heading().textContent).toContain(`Frage 2 von ${TOTAL}`);
        await click('Vorherige Frage');
      }
    });

    it('bleibt ausgeschaltet stehen und bricht einen laufenden Wechsel ab', async () => {
      await choose('2');
      await setAutoAdvance(false);
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 1 von ${TOTAL}`);
      await choose('3');
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 1 von ${TOTAL}`);
    });

    it('wechselt nicht, wenn die Auswahl vor Ablauf der Pause zurückgesetzt wird', async () => {
      await choose('2');
      await click('Auswahl zurücksetzen');
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 1 von ${TOTAL}`);
      expect(element.querySelector('input[type="radio"]:checked')).toBeNull();
    });

    it('springt nach einem schnellen Klick auf die nächste Frage nicht doppelt', async () => {
      await choose('2');
      await click('Nächste Frage');
      await afterDelay();
      expect(heading().textContent).toContain(`Frage 2 von ${TOTAL}`);
    });

    it('wechselt nach der letzten Frage nicht von selbst zum Ergebnisentwurf', async () => {
      await openLastQuestion();
      element.querySelector<HTMLInputElement>('input[type="radio"]')!.click();
      await afterDelay();
      expect(heading().textContent).toContain(`Frage ${TOTAL} von ${TOTAL}`);
      expect(element.querySelector('h1')?.textContent).toContain('Fragenentwurf');
    });

    it('führt nach der letzten Frage eines Blocks zur Einleitung des nächsten', async () => {
      for (const code of ['1', '2', '3', '4']) {
        await choose(code);
        await afterDelay();
      }
      expect(heading().textContent?.trim()).toBe('Einleitung zu Frage 5');
      expect(element.querySelector('input[type="radio"]')).toBeNull();
    });
  });

  describe('Start und Einleitungen', () => {
    const heading = () => element.querySelector<HTMLElement>('#draft-question-title')!;

    it('beginnt mit einem eigenen Startbildschirm ohne Fragen', async () => {
      const fresh = TestBed.createComponent(PolicyDraft);
      await fresh.whenStable();
      const freshElement = fresh.nativeElement as HTMLElement;
      expect(freshElement.querySelector('h1')?.textContent?.trim()).toBe('Fragenentwurf');
      expect(freshElement.textContent).toContain('Originalfragen aus fünf historischen');
      expect(freshElement.textContent).toContain('speichert und überträgt keine Antworten');
      expect(freshElement.querySelector('input[type="radio"]')).toBeNull();
      expect(freshElement.querySelector('#draft-question-title')).toBeNull();
      const start = [...freshElement.querySelectorAll('button')].filter(
        (button) => button.textContent?.trim() === 'Zu den Fragen',
      );
      expect(start).toHaveLength(1);
      expect(start[0]!.classList).toContain('primary');
      fresh.destroy();
    });

    it('zeigt die Originaleinleitung vor dem ersten Block auf einem eigenen Bildschirm', async () => {
      const fresh = TestBed.createComponent(PolicyDraft);
      await fresh.whenStable();
      const freshElement = fresh.nativeElement as HTMLElement;
      [...freshElement.querySelectorAll('button')]
        .find((button) => button.textContent?.trim() === 'Zu den Fragen')!
        .click();
      await fresh.whenStable();
      const introHeading = freshElement.querySelector<HTMLElement>('#draft-question-title')!;
      expect(introHeading.textContent?.trim()).toBe('Einleitung zu Frage 1 bis 4');
      expect(document.activeElement).toBe(introHeading);
      expect(freshElement.textContent).toContain('Nun einige Fragen zur Gesellschaft');
      expect(freshElement.querySelector('input[type="radio"]')).toBeNull();
      expect(freshElement.querySelectorAll('h1')).toHaveLength(1);
      fresh.destroy();
    });

    it('zeigt eine Einleitung beim Vorwärtsgehen einmal und dann die Frage direkt', async () => {
      for (let question = 1; question < 4; question++) await click('Nächste Frage');
      expect(heading().textContent).toContain(`Frage 4 von ${TOTAL}`);
      headingInteractions = [];
      await click('Nächste Frage');
      expect(heading().textContent?.trim()).toBe('Einleitung zu Frage 5');
      expectFocusedAndScrolled(heading());
      await click('Vorherige Frage');
      expect(heading().textContent).toContain(`Frage 4 von ${TOTAL}`);
      await click('Nächste Frage');
      expect(heading().textContent).toContain(`Frage 5 von ${TOTAL}`);
    });

    it('öffnet die Einleitung zur aktuellen Frage und kehrt zu ihr zurück', async () => {
      await click('Nächste Frage');
      await click('Einleitung zu dieser Frage anzeigen');
      expect(heading().textContent?.trim()).toBe('Einleitung zu Frage 1 bis 4');
      expect(element.textContent).toContain('Nun einige Fragen zur Gesellschaft');
      headingInteractions = [];
      await click('Zu Frage 2');
      expect(heading().textContent).toContain(`Frage 2 von ${TOTAL}`);
      expectFocusedAndScrolled(heading());
    });

    it('springt aus der Übersicht direkt zur Frage, auch am Anfang eines Blocks', async () => {
      await click('Zur Fragenübersicht');
      element.querySelectorAll<HTMLButtonElement>('.overview-list li button')[4]!.click();
      await fixture.whenStable();
      expect(heading().textContent).toContain(`Frage 5 von ${TOTAL}`);
      expect(element.querySelector('input[type="radio"]')).not.toBeNull();
    });

    it('zeigt Auswahl zurücksetzen nur, wenn es etwas zurückzusetzen gibt', async () => {
      const reset = () =>
        [...element.querySelectorAll('button')].filter(
          (button) => button.textContent?.trim() === 'Auswahl zurücksetzen',
        );
      expect(reset()).toHaveLength(0);
      await choose('2');
      expect(reset()).toHaveLength(1);
      await click('Frage überspringen');
      await click('Vorherige Frage');
      expect(element.querySelector('.card-head')?.textContent).toContain('Übersprungen');
      expect(reset()).toHaveLength(1);
    });
  });
});
