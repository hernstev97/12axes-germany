import { Artwork } from './artwork';

// Herkunft, Rechtehinweise, Prüfsummen und Verarbeitung: docs/assets.md.
const WIDTHS = [480, 800, 1200] as const;

const KREIDEFELSEN: Artwork = {
  id: 'friedrich-kreidefelsen',
  artist: 'Caspar David Friedrich',
  title: 'Kreidefelsen auf Rügen',
  date: '1818',
  collection: 'Kunst Museum Winterthur, Reinhart am Stadtgarten',
  alt: 'Blick unter Bäumen hindurch über weiße, zackige Kreidefelsen aufs Meer mit zwei Segelbooten. Vorn eine Frau in Rot, ein kriechender und ein stehender Mann.',
  width: 4237,
  height: 5465,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Kreidefelsen_auf_R%C3%BCgen_(1818).jpg',
  tone: '#7d6e59',
};

const RIESENGEBIRGE: Artwork = {
  id: 'friedrich-riesengebirge',
  artist: 'Caspar David Friedrich',
  title: 'Riesengebirgslandschaft mit aufsteigendem Nebel',
  date: 'um 1819/20',
  collection: 'Neue Pinakothek, München',
  alt: 'Gestaffelte Bergrücken im Dunst unter hellem Himmel, aus den Tälern steigt Nebel. Vorn ein dunkler Hang mit Felsen und zwei kahlen Bäumen.',
  width: 3000,
  height: 2334,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Riesengebirge_Landscape_with_Rising_Fog_-_WGA8257.jpg',
  tone: '#918478',
};

const MOENCH: Artwork = {
  id: 'friedrich-moench',
  artist: 'Caspar David Friedrich',
  title: 'Mönch am Meer',
  date: '1808–1810',
  collection: 'Alte Nationalgalerie, Berlin',
  alt: 'Weiter, grau-blauer Wolkenhimmel über einem fast schwarzen Meer. Vorn ein heller Sandstreifen mit einer kleinen, dunkel gekleideten Gestalt.',
  width: 3531,
  height: 2270,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Friedrich,_Caspar_David_-_M%C3%B6nch_am_Meer_-_Alte_Nationalgalerie_in_Berlin.jpg',
  tone: '#758091',
};

const SCHRECKENSTEIN: Artwork = {
  id: 'richter-schreckenstein',
  artist: 'Ludwig Richter',
  title: 'Die Überfahrt am Schreckenstein',
  date: '1837',
  collection: 'Albertinum, Dresden',
  alt: 'Ein Fährmann rudert ein Boot mit Reisenden und einem Harfner im Abendlicht über einen Fluss. Links eine Burgruine auf steilem Fels.',
  width: 3130,
  height: 2341,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Ludwig_Richter_-_Crossing_at_Schreckenstein_-_Google_Art_Project.jpg',
  tone: '#9f865e',
};

const DRESDEN: Artwork = {
  id: 'carus-dresden',
  artist: 'Carl Gustav Carus',
  title: 'Blick auf Dresden bei Sonnenuntergang',
  date: 'um 1822',
  collection: 'Kunstsammlungen Chemnitz',
  alt: 'Orangeroter Abendhimmel über einer dunklen Anhöhe mit Weg. Oben sitzen zwei Personen vor einer fernen Stadtsilhouette mit Türmen und Kuppel.',
  width: 5074,
  height: 3651,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Carl_Gustav_Carus_-_Blick_auf_Dresden_bei_Sonnenuntergang.jpg',
  tone: '#593f2c',
};

const MORGENSTUNDE: Artwork = {
  id: 'schwind-morgenstunde',
  artist: 'Moritz von Schwind',
  title: 'Die Morgenstunde',
  date: 'um 1860',
  collection: 'Sammlung Schack, München',
  alt: 'Eine junge Frau in weißem Kleid steht, von hinten gesehen, am offenen Fenster mit Blick auf Berge. Im sonnigen Zimmer eine Kommode und ein Himmelbett.',
  width: 5618,
  height: 4646,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Moritz_von_Schwind_-_Die_Morgenstunde_-_Sammlung_Schack_-_11559.jpg',
  tone: '#60554c',
};

const GREIFSWALD: Artwork = {
  id: 'friedrich-greifswald',
  artist: 'Caspar David Friedrich',
  title: 'Wiesen bei Greifswald',
  date: '1821/22',
  collection: 'Hamburger Kunsthalle',
  alt: 'Weite grüne Wiesen mit grasenden und galoppierenden Pferden. Am Horizont eine Stadtsilhouette mit Kirchtürmen und Windmühlen unter hellem Himmel.',
  width: 2362,
  height: 1679,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Wiesen_bei_Greifswald_(1821-1822)_-_Caspar_David_Friedrich_(Hamburger_Kunsthalle).jpg',
  tone: '#a29e83',
};

const FRAU_AM_FENSTER: Artwork = {
  id: 'friedrich-fenster',
  artist: 'Caspar David Friedrich',
  title: 'Frau am Fenster',
  date: '1822',
  collection: 'Alte Nationalgalerie, Berlin',
  alt: 'Eine Frau in langem, grünlichem Kleid steht, von hinten gesehen, am offenen Fenster eines dunklen Raums. Draußen Bäume, ein Schiffsmast und heller Himmel.',
  width: 2831,
  height: 4000,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Caspar_David_Friedrich_-_Frau_am_Fenster_(1822).jpg',
  tone: '#58493d',
};

const DAECHER: Artwork = {
  id: 'blechen-daecher',
  artist: 'Carl Blechen',
  title: 'Blick auf Dächer und Gärten',
  date: 'um 1835',
  collection: 'Alte Nationalgalerie, Berlin',
  alt: 'Erhöhter Blick: rechts ein steiles, hell schimmerndes Dach, links ein Schuppen am Hof. Dahinter Holzzäune, Gärten, Bäume und Häuser unter grauweißem Himmel.',
  width: 2199,
  height: 1671,
  widths: WIDTHS,
  source:
    'https://commons.wikimedia.org/wiki/File:Carl_Blechen_-_Blick_auf_D%C3%A4cher_und_G%C3%A4rten_-_Google_Art_Project.jpg',
  tone: '#615953',
};

/** Wechselnde Auswahl auf der Startseite. */
export const HOME_GALLERY: readonly Artwork[] = [
  KREIDEFELSEN,
  RIESENGEBIRGE,
  MOENCH,
  SCHRECKENSTEIN,
  DRESDEN,
  MORGENSTUNDE,
];

/** Fläche „Grundlage“ auf der Startseite. */
export const BASIS_ARTWORK = GREIFSWALD;
export const PROJECT_ARTWORK = FRAU_AM_FENSTER;
export const NOT_FOUND_ARTWORK = DAECHER;

/** Alle ausgelieferten Werke in der Reihenfolge der Bildnachweise. */
export const ALL_ARTWORKS: readonly Artwork[] = [
  ...HOME_GALLERY,
  BASIS_ARTWORK,
  PROJECT_ARTWORK,
  NOT_FOUND_ARTWORK,
];
