/**
 * Display-only additions to the bound catalogues after the review V2
 * (reports/claude/agenten/V2-urteil.json). The catalogues and profile rules stay unchanged.
 * Every addition names its source. Texts were checked against the cached German
 * questionnaires and the cited legal text on 3 October 2026.
 */
export interface DisplayAddition {
  /** Original introductions shown before the bound ones. */
  readonly introductionsBefore?: readonly string[];
  /** Display stem instead of the bound response stem. */
  readonly responseStemDe?: string;
  /** Notes appended to the development note. */
  readonly notes: readonly string[];
}

// ESS8 German questionnaire, PDF page 41, before E33 (V2-F01).
const ESS8_E33_INTRODUCTION =
  'Als Reaktion auf veränderte wirtschaftliche und gesellschaftliche Rahmenbedingungen könnte es sein, dass Staat und Regierung in den nächsten zehn Jahren Änderungen bei den Sozialleistungen vornehmen.';
const ESS8_E33_NOTE =
  'Die Einleitung „Als Reaktion auf veränderte wirtschaftliche und gesellschaftliche Rahmenbedingungen …“ steht im deutschen ESS8-Fragebogen einmal vor E33 (PDF-Seite 41) und gilt für E33 bis E35. Die Einzelansicht zeigt sie bei jeder dieser drei Fragen.';
// ESS8 German questionnaire, introduction before E6 (V2-F12).
const ESS8_E6_STEM_NOTE =
  'Im Original steht „Sollte der Staat erstens dafür verantwortlich sein…“ einmal vor E6. Die Einzelansicht lässt „erstens“ bei E7 und E8 weg.';
// ESS10 PAPI A54–A56 (V2-F08, V2-F12).
const ESS10_A54_STEM_NOTE =
  'Die Frage „Wie vielen von ihnen sollte Deutschland erlauben, hier zu leben? Sollte Deutschland es…“ steht im Papierfragebogen nur bei A54. Die Einzelansicht wiederholt sie, weil jede Frage einzeln erscheint.';
const ESS10_ETHNIC_GROUP_NOTE =
  '„Volksgruppe oder ethnische Gruppe“ ist die deutsche ESS-Übersetzung von „race or ethnic group“ aus dem Jahr 2021. Das Projekt übernimmt den Begriff unverändert, damit die Antworten vergleichbar bleiben.';
// V2-F17: questions that depend on the situation at the time of fieldwork.
const STATUS_QUO_NOTE =
  'Die damaligen Befragten bezogen die Frage auf die Lage zur Feldzeit. Ob sich die Rechtslage seither geändert hat, hat das Projekt für diese Frage nicht geprüft.';

export const DISPLAY_ADDITIONS: Readonly<Record<string, DisplayAddition>> = {
  'ESS8e02_3:bnlwinc': {
    introductionsBefore: [ESS8_E33_INTRODUCTION],
    notes: [ESS8_E33_NOTE],
  },
  'ESS8e02_3:eduunmp': {
    introductionsBefore: [ESS8_E33_INTRODUCTION],
    notes: [ESS8_E33_NOTE],
  },
  'ESS8e02_3:wrkprbf': {
    introductionsBefore: [ESS8_E33_INTRODUCTION],
    notes: [ESS8_E33_NOTE],
  },
  'ESS8e02_3:gvslvol': { notes: [STATUS_QUO_NOTE] },
  'ESS8e02_3:gvslvue': {
    responseStemDe: 'Sollte der Staat dafür verantwortlich sein…',
    notes: [ESS8_E6_STEM_NOTE, STATUS_QUO_NOTE],
  },
  'ESS8e02_3:gvcldcr': {
    responseStemDe: 'Sollte der Staat dafür verantwortlich sein…',
    notes: [ESS8_E6_STEM_NOTE, STATUS_QUO_NOTE],
  },
  'ESS8e02_3:inctxff': { notes: [STATUS_QUO_NOTE] },
  'ESS8e02_3:sbsrnen': { notes: [STATUS_QUO_NOTE] },
  'ESS8e02_3:banhhap': { notes: [STATUS_QUO_NOTE] },
  'ESS8e02_3:imsclbn': { notes: [STATUS_QUO_NOTE] },
  'ESS11e04_2:eqparep': { notes: [STATUS_QUO_NOTE] },
  'ESS8e02_3:rfgbfml': {
    notes: [
      'Seit der Feldzeit geändert: Der Familiennachzug zu subsidiär Schutzberechtigten wird „bis zum Ablauf des 23. Juli 2027“ nicht gewährt (§ 104 Abs. 14 Aufenthaltsgesetz). Die Frage unterscheidet nicht nach Schutzstatus.',
    ],
  },
  'ESS10SCe03_2:imsmetn': { notes: [ESS10_ETHNIC_GROUP_NOTE] },
  'ESS10SCe03_2:imdfetn': { notes: [ESS10_A54_STEM_NOTE, ESS10_ETHNIC_GROUP_NOTE] },
  'ESS10SCe03_2:impcntr': { notes: [ESS10_A54_STEM_NOTE] },
};
