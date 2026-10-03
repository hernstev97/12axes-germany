/** Ein lokal ausgeliefertes Gemälde. Nachweise stehen in docs/assets.md. */
export interface Artwork {
  /** Dateipräfix in public/art, z. B. „friedrich-kreidefelsen“. */
  readonly id: string;
  readonly artist: string;
  readonly title: string;
  readonly date: string;
  readonly collection: string;
  readonly alt: string;
  /** Abmessungen der Originaldatei in Pixeln. */
  readonly width: number;
  readonly height: number;
  /** Verfügbare WebP-Breiten. */
  readonly widths: readonly number[];
  /** Dateiseite auf Wikimedia Commons. */
  readonly source: string;
  /** Mittlere Bildfarbe als Platzhalter, solange die Datei lädt. */
  readonly tone: string;
}

export function artworkSrc(artwork: Artwork, width = 800): string {
  const available = artwork.widths.filter((candidate) => candidate <= width);
  return `art/${artwork.id}-${available.at(-1) ?? artwork.widths[0]}.webp`;
}

export function artworkSrcset(artwork: Artwork): string {
  return artwork.widths.map((width) => `art/${artwork.id}-${width}.webp ${width}w`).join(', ');
}
