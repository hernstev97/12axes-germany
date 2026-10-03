import { TestBed } from '@angular/core/testing';
import { Router } from '@angular/router';
import { App } from './app';
import { appConfig } from './app.config';

describe('Seitennavigation', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
      providers: appConfig.providers,
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
    expect(document.title).toBe('Projektstand · 12 Axes Deutschland');
    expect(document.activeElement?.id).toBe('main-content');
    expect(fixture.nativeElement.querySelector('h1')?.textContent).toContain('Projektstand');
    expect(projectLink.getAttribute('aria-current')).toBe('page');
  });

  it('bietet für unbekannte Adressen einen Weg zurück zur Startseite', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    await TestBed.inject(Router).navigateByUrl('/unbekannt');
    await fixture.whenStable();
    expect(document.title).toBe('Seite nicht gefunden · 12 Axes Deutschland');
    const returnLink = fixture.nativeElement.querySelector('main a') as HTMLAnchorElement;
    returnLink.click();
    await fixture.whenStable();
    expect(TestBed.inject(Router).url).toBe('/');
    expect(document.title).toBe('12 Axes Deutschland');
  });

  it('öffnet die Methodik über den Projektstand und behält die Abschnittsadresse', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    await TestBed.inject(Router).navigateByUrl('/projekt');
    await fixture.whenStable();
    const methodologyLink = fixture.nativeElement.querySelector(
      'main a[href="/methodik"]',
    ) as HTMLAnchorElement;
    methodologyLink.click();
    await fixture.whenStable();
    expect(document.title).toBe('Methodik und Grenzen · 12 Axes Deutschland');
    expect(document.activeElement?.id).toBe('main-content');
    const contentsLink = fixture.nativeElement.querySelector(
      'main nav a[href="/methodik#fragekontext"]',
    ) as HTMLAnchorElement;
    contentsLink.click();
    await fixture.whenStable();
    expect(TestBed.inject(Router).url).toBe('/methodik#fragekontext');
    const homeLink = fixture.nativeElement.querySelector(
      'main .breadcrumb a[href="/"]',
    ) as HTMLAnchorElement;
    homeLink.click();
    await fixture.whenStable();
    expect(TestBed.inject(Router).url).toBe('/');
    expect(document.title).toBe('12 Axes Deutschland');
  });
});
