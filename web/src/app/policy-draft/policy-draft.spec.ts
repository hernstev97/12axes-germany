import { type ComponentFixture, TestBed } from '@angular/core/testing';
import { PolicyDraft } from './policy-draft';
import { REVIEWED_HISTORICAL_REFERENCES } from './reviewed-historical-references';

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

  it.each([
    ['Zur nächsten Frage', 'Frage 3 von 43'],
    ['Zur vorherigen Frage', 'Frage 1 von 43'],
    ['Diese Frage überspringen', 'Frage 3 von 43'],
  ])('Fokus und Scrollen folgen dem gerenderten Fragenwechsel durch %s', async (action, title) => {
    await click('Zur nächsten Frage');
    headingInteractions = [];
    await click(action);
    const heading = element.querySelector<HTMLElement>('#draft-question-title')!;
    expect(heading.textContent).toContain(title);
    expectFocusedAndScrolled(heading);
  });

  it.each([
    ['Zu den Fragen', 'Zur Fragenübersicht', 'Fragenübersicht'],
    ['Zu den Fragen', 'Zum Ergebnisentwurf', 'Ergebnisentwurf'],
    ['Zur Fragenübersicht', 'Zu den Fragen', 'Fragenentwurf'],
    ['Zur Fragenübersicht', 'Zum Ergebnisentwurf', 'Ergebnisentwurf'],
    ['Zum Ergebnisentwurf', 'Zu den Fragen', 'Fragenentwurf'],
    ['Zum Ergebnisentwurf', 'Zur Fragenübersicht', 'Fragenübersicht'],
  ])(
    'Fokus und Scrollen folgen der gerenderten Ansichtsüberschrift von %s durch %s',
    async (fromAction, action, title) => {
      await click(fromAction);
      headingInteractions = [];
      await click(action);
      const heading = element.querySelector<HTMLElement>('h1')!;
      expect(heading.textContent).toContain(title);
      expectFocusedAndScrolled(heading);
    },
  );

  it('Fokus und Scrollen führen von der letzten Übersichtsfrage zur gerenderten Frage 43', async () => {
    await click('Zur Fragenübersicht');
    headingInteractions = [];
    element.querySelector<HTMLButtonElement>('.overview-list li:last-child button')!.click();
    await fixture.whenStable();
    const heading = element.querySelector<HTMLElement>('#draft-question-title')!;
    expect(heading.textContent).toContain('Frage 43 von 43');
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
    expect(heading.textContent).toContain('Frage 43 von 43');
    expect(element.textContent).toContain('Originalfrage E35');
    expectFocusedAndScrolled(heading);
  });

  it.each(['Zum Ergebnisentwurf', 'Diese Frage überspringen'])(
    'Fokus und Scrollen führen nach Frage 43 durch %s zur Ergebnisüberschrift',
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
    await click('Zur nächsten Frage');
    expect(element.querySelector('#draft-question-title')?.textContent).toContain('Frage 2');
    expect(document.activeElement?.id).toBe('draft-question-title');
    await choose('5');
    await click('Zur vorherigen Frage');
    expect(element.querySelector<HTMLInputElement>('input[value="2"]')?.checked).toBe(true);
    await choose('1');
    await click('Zur nächsten Frage');
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
    await click('Zur nächsten Frage');
    const reason = element.querySelector<HTMLSelectElement>('#draft-skip-reason')!;
    reason.value = 'dont-know';
    reason.dispatchEvent(new Event('change'));
    await click('Diese Frage überspringen');
    await click('Zum Ergebnisentwurf');
    const first = element.querySelector<HTMLElement>('[data-question-id="ESS9e03_3:sofrdst"]')!;
    const second = element.querySelector<HTMLElement>('[data-question-id="ESS9e03_3:sofrwrk"]')!;
    expect(first.textContent).toContain('Unberührt');
    expect(second.textContent).toContain('Grund dieser Entwurfssitzung: Weiß nicht');
    expect(second.textContent).toContain('keinem Missing-Code');
    expect(second.textContent).not.toContain('Gewählte Originalkategorie');
    expect(element.querySelectorAll('.result-item')).toHaveLength(43);
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
    expect(element.querySelector('fieldset')?.getAttribute('aria-describedby')).toContain(
      'draft-original-context',
    );
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
    expect(element.querySelectorAll('section h2')).toHaveLength(9);
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
    await click('Zur nächsten Frage');
    await click('Diese Frage überspringen');
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
});
