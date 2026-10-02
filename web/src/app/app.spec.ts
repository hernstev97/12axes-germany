import { TestBed } from '@angular/core/testing';
import { provideRouter, Router } from '@angular/router';
import { App } from './app';
import { routes } from './app.routes';

describe('Seitennavigation', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
      providers: [provideRouter(routes)],
    }).compileComponents();
  });

  it('führt nach einem Seitenwechsel zum Hauptinhalt und aktualisiert den Titel', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    await TestBed.inject(Router).navigateByUrl('/');
    await fixture.whenStable();
    const projectLink = fixture.nativeElement.querySelector(
      'header a[href="/projekt"]',
    ) as HTMLAnchorElement;
    projectLink.focus();
    projectLink.click();
    await fixture.whenStable();
    expect(document.title).toBe('Projektstand · Politikprofil');
    expect(document.activeElement?.id).toBe('main-content');
    expect(fixture.nativeElement.querySelector('h1')?.textContent).toContain('Ein offener Blick');
    expect(projectLink.getAttribute('aria-current')).toBe('page');
  });

  it('bietet für unbekannte Adressen einen Weg zurück zur Startseite', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    await TestBed.inject(Router).navigateByUrl('/unbekannt');
    await fixture.whenStable();
    expect(document.title).toBe('Seite nicht gefunden · Politikprofil');
    const returnLink = fixture.nativeElement.querySelector('main a') as HTMLAnchorElement;
    returnLink.click();
    await fixture.whenStable();
    expect(TestBed.inject(Router).url).toBe('/');
    expect(document.title).toBe('Politikprofil · Deutschland');
  });
});
