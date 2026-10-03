import { type ComponentFixture, TestBed } from '@angular/core/testing';
import { PolicyDraft } from './policy-draft';

describe('Unrouteter Angular-Fragen- und Ergebnisentwurf', () => {
  let fixture: ComponentFixture<PolicyDraft>;
  let element: HTMLElement;

  beforeEach(async () => {
    await TestBed.configureTestingModule({ imports: [PolicyDraft] }).compileComponents();
    fixture = TestBed.createComponent(PolicyDraft);
    await fixture.whenStable();
    element = fixture.nativeElement as HTMLElement;
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
});
