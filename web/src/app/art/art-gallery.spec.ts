import { TestBed } from '@angular/core/testing';
import { provideRouter } from '@angular/router';
import { ArtGallery } from './art-gallery';
import { HOME_GALLERY } from './artworks';

describe('Gemäldegalerie', () => {
  const artworks = HOME_GALLERY.slice(0, 4);

  function setReducedMotion(reduce: boolean): void {
    Object.defineProperty(window, 'matchMedia', {
      configurable: true,
      value: (query: string) => ({ matches: reduce && query.includes('reduce') }),
    });
  }

  async function render(options: { startIndex?: number } = {}) {
    await TestBed.configureTestingModule({
      imports: [ArtGallery],
      providers: [provideRouter([])],
    }).compileComponents();
    const fixture = TestBed.createComponent(ArtGallery);
    fixture.componentRef.setInput('artworks', artworks);
    fixture.componentRef.setInput('label', 'Gemälde');
    fixture.componentRef.setInput('startIndex', options.startIndex ?? 0);
    fixture.componentRef.setInput('intervalMs', 1000);
    await vi.advanceTimersByTimeAsync(20);
    const element = fixture.nativeElement as HTMLElement;
    const caption = () => element.querySelector('.caption.is-current cite')?.textContent;
    const button = (label: string) =>
      element.querySelector(`button[aria-label="${label}"]`) as HTMLButtonElement;
    const loadImages = async () => {
      element.querySelectorAll('img').forEach((img) => img.dispatchEvent(new Event('load')));
      await vi.advanceTimersByTimeAsync(20);
    };
    return { element, caption, button, loadImages };
  }

  beforeEach(() => {
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.restoreAllMocks();
    vi.useRealTimers();
    Reflect.deleteProperty(window, 'matchMedia');
  });

  it('blättert vor und zurück und zeigt nur das aktuelle Bild', async () => {
    const { element, caption, button } = await render({ startIndex: 3 });
    expect(caption()).toBe(artworks[3].title);

    button('Nächstes Bild').click();
    await vi.advanceTimersByTimeAsync(20);
    expect(caption()).toBe(artworks[0].title);

    button('Vorheriges Bild').click();
    await vi.advanceTimersByTimeAsync(20);
    expect(caption()).toBe(artworks[3].title);

    const visible = element.querySelectorAll('.slide:not([aria-hidden])');
    expect(visible.length).toBe(1);
    expect(visible[0].querySelector('img')?.getAttribute('alt')).toBe(artworks[3].alt);
  });

  it('wechselt ohne reduzierte Bewegung mehrfach hintereinander und lädt das nächste Bild vor', async () => {
    setReducedMotion(false);
    const { element, caption, loadImages } = await render();
    for (let step = 1; step <= 3; step++) {
      await loadImages();
      await loadImages();
      await vi.advanceTimersByTimeAsync(1000);
      expect(caption()).toBe(artworks[step].title);
    }
    expect(element.querySelectorAll('.slide img').length).toBe(4);
  });

  it('wechselt bei reduzierter Bewegung nicht von selbst', async () => {
    setReducedMotion(true);
    const { caption, button, loadImages } = await render();
    await loadImages();
    await vi.advanceTimersByTimeAsync(3000);
    expect(caption()).toBe(artworks[0].title);
    expect(button('Bildwechsel fortsetzen')).toBeTruthy();
  });

  it('lässt sich anhalten und fortsetzen', async () => {
    setReducedMotion(false);
    const { caption, button, loadImages } = await render();
    await loadImages();
    button('Bildwechsel anhalten').click();
    await vi.advanceTimersByTimeAsync(3000);
    expect(caption()).toBe(artworks[0].title);

    button('Bildwechsel fortsetzen').click();
    await vi.advanceTimersByTimeAsync(1100);
    expect(caption()).toBe(artworks[1].title);
  });

  it('beendet den Wechsel dauerhaft, sobald der Tastaturfokus in die Galerie kommt', async () => {
    setReducedMotion(false);
    // jsdom wertet :focus-visible nicht aus; im Browser trifft es bei Tastaturfokus zu.
    const matches = Element.prototype.matches;
    vi.spyOn(Element.prototype, 'matches').mockImplementation(function (this: Element, selector) {
      return selector === ':focus-visible'
        ? this === document.activeElement
        : matches.call(this, selector);
    });
    const { element, caption, button, loadImages } = await render();
    button('Nächstes Bild').focus();
    button('Nächstes Bild').blur();
    await loadImages();
    await vi.advanceTimersByTimeAsync(3000);
    expect(caption()).toBe(artworks[0].title);
    expect(button('Bildwechsel fortsetzen')).toBeTruthy();
    expect(element.querySelector('.captions')?.getAttribute('aria-live')).toBe('polite');
  });

  it('hält bei Fokus ohne Tastatur nicht dauerhaft an', async () => {
    setReducedMotion(false);
    const { caption, button, loadImages } = await render();
    // Ein Mausklick löst focusin aus, ohne dass das Element :focus-visible ist.
    button('Nächstes Bild').dispatchEvent(new FocusEvent('focusin', { bubbles: true }));
    await loadImages();
    await vi.advanceTimersByTimeAsync(1100);
    expect(caption()).toBe(artworks[1].title);
    expect(button('Bildwechsel anhalten')).toBeTruthy();
  });

  it('zeigt bei nur einem Bild keine Bedienelemente', async () => {
    await TestBed.configureTestingModule({
      imports: [ArtGallery],
      providers: [provideRouter([])],
    }).compileComponents();
    const fixture = TestBed.createComponent(ArtGallery);
    fixture.componentRef.setInput('artworks', artworks.slice(0, 1));
    fixture.componentRef.setInput('label', 'Gemälde');
    await vi.advanceTimersByTimeAsync(20);
    const element = fixture.nativeElement as HTMLElement;
    expect(element.querySelector('.controls')).toBeNull();
    expect(element.querySelector('.caption.is-current cite')?.textContent).toBe(artworks[0].title);
  });
});
