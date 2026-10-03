import { designCatalogue as catalogue } from './catalogue.js';

const themes = [
  ['economy_distribution', 'Wirtschaft und Verteilung'],
  ['welfare', 'Sozialstaat'],
  ['democracy_authority', 'Demokratie und politische Autorität'],
  ['rights_security', 'Bürgerrechte und Sicherheit'],
  ['europe', 'Europäische Integration'],
  ['climate_energy', 'Klima und Energie'],
  ['migration', 'Migration'],
  ['equality_family', 'Gleichstellungs- und Familienpolitik'],
];
const meanings = {
  sofrdst: [
    'Gleichmäßige Verteilung',
    'Die Auswahl beschreibt die Zustimmung zur gleichmäßigen Verteilung von Einkommen und Vermögen als Gerechtigkeitsprinzip.',
  ],
  sofrwrk: [
    'Verdienst durch harte Arbeit',
    'Die Auswahl beschreibt Zustimmung oder Ablehnung der Aussage, dass eine Gesellschaft gerecht ist, wenn hart arbeitende Menschen mehr verdienen als andere.',
  ],
  sofrpr: [
    'Fürsorge ohne Gegenleistung',
    'Die Auswahl beschreibt Zustimmung oder Ablehnung der Aussage, dass eine Gesellschaft gerecht ist, wenn sie sich um Arme und Bedürftige kümmert, unabhängig davon, was diese der Gesellschaft zurückgeben.',
  ],
  sofrprv: [
    'Privilegien durch Familienstatus',
    'Die Auswahl beschreibt Zustimmung oder Ablehnung der Aussage, dass eine Gesellschaft gerecht ist, wenn Menschen aus Familien mit hoher gesellschaftlicher Stellung Privilegien in ihrem Leben genießen.',
  ],
  gincdif: [
    'Einkommensunterschiede verringern',
    'Die Auswahl beschreibt die Zustimmung zu staatlichen Maßnahmen gegen Einkommensunterschiede. Eine bestimmte Steuer- oder Eigentumsordnung folgt daraus nicht.',
  ],
  gvslvol: [
    'Lebensstandard im Alter',
    'Die Auswahl nennt das gewünschte Ausmaß staatlicher Verantwortung für einen angemessenen Lebensstandard im Alter.',
  ],
  gvslvue: [
    'Lebensstandard bei Arbeitslosigkeit',
    'Die Auswahl nennt das gewünschte Ausmaß staatlicher Verantwortung für einen angemessenen Lebensstandard von Arbeitslosen.',
  ],
  gvcldcr: [
    'Kinderbetreuung für berufstätige Eltern',
    'Die Auswahl nennt das gewünschte Ausmaß staatlicher Verantwortung für ausreichende Kinderbetreuung. Diese Frage zählt primär zum Sozialstaat.',
  ],
  bnlwinc: [
    'Sozialleistungen nur für niedrigste Einkommen',
    'Die Auswahl bezieht sich auf die Beschränkung staatlicher Sozialleistungen auf die niedrigsten Einkommen mit der genannten Folge für mittlere und hohe Einkommen.',
  ],
  eduunmp: [
    'Mehr Aus- und Weiterbildung, weniger Arbeitslosenunterstützung',
    'Die Auswahl betrifft mehr Aus- und Weiterbildung bei weniger Arbeitslosenunterstützung unter einer festen Geldsumme.',
  ],
  fairelc: [
    'Freie und faire Wahlen',
    'Die Auswahl nennt die Wichtigkeit freier und fairer Parlamentswahlen für Demokratie im Allgemeinen. Sie bewertet keine tatsächliche Wahl.',
  ],
  dfprtal: [
    'Inhaltliche Unterschiede zwischen Parteien',
    'Die Auswahl nennt die Wichtigkeit klarer inhaltlicher Unterschiede zwischen politischen Parteien für Demokratie im Allgemeinen.',
  ],
  medcrgv: [
    'Kritikrecht der Medien',
    'Die Auswahl nennt die Wichtigkeit des Rechts der Medien, die Regierung zu kritisieren.',
  ],
  rghmgpr: [
    'Schutz von Minderheitenrechten',
    'Die Auswahl nennt die Wichtigkeit geschützter Minderheitenrechte für Demokratie im Allgemeinen.',
  ],
  votedir: [
    'Volksabstimmungen bei wichtigen Sachfragen',
    'Die Auswahl nennt die Wichtigkeit des letzten Wortes der Bürger durch direkte Volksabstimmungen bei wichtigen Sachfragen.',
  ],
  cttresa: [
    'Gleichbehandlung durch Gerichte',
    'Die Auswahl nennt die Wichtigkeit gleicher Behandlung aller Menschen durch Gerichte.',
  ],
  gptpelc: [
    'Wahlfolgen schlechter Regierungsarbeit',
    'Die Auswahl nennt die Wichtigkeit, Regierungsparteien für schlechte Arbeit bei Wahlen abzustrafen.',
  ],
  gvctzpv: [
    'Schutz aller Bürger vor Armut',
    'Die Auswahl nennt die Wichtigkeit staatlichen Schutzes aller Bürger vor Armut als Demokratieprinzip.',
  ],
  grdfinc: [
    'Verringerung von Einkommensunterschieden als Demokratieprinzip',
    'Die Auswahl nennt die Wichtigkeit staatlicher Maßnahmen zur Verringerung von Einkommensunterschieden für Demokratie im Allgemeinen. Sie ist eine andere Frage als die Zustimmung zu einer Maßnahme.',
  ],
  viepol: [
    'Vorrang gewöhnlicher Menschen vor Eliten',
    'Die Auswahl nennt die Wichtigkeit des Vorrangs der Ansichten gewöhnlicher Menschen gegenüber politischen Eliten im genannten Demokratiekontext.',
  ],
  wpestop: [
    'Durchsetzung des Volkswillens',
    'Die Auswahl nennt die Wichtigkeit, dass sich der Wille des Volkes immer durchsetzt. Daraus folgt keine allgemeine Eigenschaft der Person.',
  ],
  scchpldm: [
    'Mehrheit folgen oder Pläne beibehalten',
    'Die Auswahl nennt eine der beiden Regierungsreaktionen im beschriebenen Konflikt mit der großen Bevölkerungsmehrheit. Die ursprünglichen Anschlussfragen fehlen im Entwurf.',
  ],
  bplcdc: [
    'Polizeientscheidungen trotz Widerspruch',
    'Die Auswahl nennt das empfundene Pflichtausmaß, Polizeientscheidungen trotz eigenen Widerspruchs zu akzeptieren.',
  ],
  dpcstrb: [
    'Polizeianweisungen trotz missbilligter Behandlung',
    'Die Auswahl nennt das empfundene Pflichtausmaß, Polizeianweisungen trotz missbilligter Behandlung zu befolgen.',
  ],
  hrshsnta: [
    'Härtere Strafen als im damaligen Kontext',
    'Die Auswahl bezieht sich auf wesentlich härtere Strafen als im historischen Originalkontext 2010/2011. Das Wort „heute“ bezeichnet dort keinen Vergleich mit 2026.',
  ],
  dbctvrd: [
    'Abschließende Gerichtsurteile akzeptieren',
    'Die Auswahl beschreibt die Zustimmung zur Pflicht, ein abschließendes Gerichtsurteil zu akzeptieren.',
  ],
  lwstrob: [
    'Gesetze strikt befolgen',
    'Die Auswahl beschreibt die Zustimmung zur strikten Befolgung aller Gesetze.',
  ],
  rgbrklw: [
    'Gesetzesbruch für das Richtige',
    'Die Auswahl beschreibt die Zustimmung zum genannten Ausnahmefall, ein Gesetz zu brechen, um das Richtige zu tun.',
  ],
  vteurmmb: [
    'Hypothetisches EU-Mitgliedschaftsreferendum',
    'Die Auswahl nennt eine Antwort im hypothetischen Mitgliedschaftsreferendum. Leerer oder ungültiger Stimmzettel, Nichtwahl und fehlende Stimmberechtigung bleiben eigene Originalkategorien.',
  ],
  keydec: [
    'Nationale statt EU-Entscheidungen',
    'Die Auswahl nennt die Wichtigkeit nationaler statt EU-Entscheidungen als Demokratieprinzip. B12 bleibt im Fragenablauf Teil von B1–B12 und wird hier primär der EU zugeordnet.',
  ],
  euftf: [
    'Umfang europäischer Einigung',
    'Die Auswahl nennt eine Originalkategorie zwischen bereits zu weit gegangener und weitergehender europäischer Einigung. Sie wird nicht mit der Mitgliedschaftsfrage verrechnet.',
  ],
  inctxff: [
    'Abgaben auf fossile Brennstoffe',
    'Die Auswahl beschreibt die Unterstützung der genannten Abgabenerhöhung auf Öl, Gas und Kohle.',
  ],
  sbsrnen: [
    'Öffentliche Förderung erneuerbarer Energie',
    'Die Auswahl beschreibt die Unterstützung öffentlicher Gelder für Wind- oder Sonnenenergie.',
  ],
  banhhap: [
    'Verkaufsverbot ineffizienter Haushaltsgeräte',
    'Die Auswahl beschreibt die Unterstützung des genannten gesetzlichen Verkaufsverbots.',
  ],
  imsmetn: [
    'Zulassung der im Original genannten gleichen Gruppe',
    'Die Auswahl nennt den gewünschten Zulassungsumfang für die im Original bezeichnete Volksgruppe oder ethnische Gruppe. Der Gruppenbegriff bleibt als historische Originalformulierung sichtbar.',
  ],
  imdfetn: [
    'Zulassung der im Original genannten anderen Gruppe',
    'Die Auswahl nennt den gewünschten Zulassungsumfang für die im Original bezeichnete andere Volksgruppe oder ethnische Gruppe. Sie belegt keine tatsächlichen Zuwanderungsfolgen.',
  ],
  impcntr: [
    'Zulassung aus ärmeren Ländern außerhalb Europas',
    'Die Auswahl nennt den gewünschten Zulassungsumfang für die ausdrücklich genannte Herkunftsgruppe.',
  ],
  imsclbn: [
    'Bedingungen gleicher Sozialleistungsrechte',
    'Die Auswahl nennt eine konkrete Bedingung für gleiche Sozialleistungsrechte. Aufenthaltsdauer, Arbeit, Steuern und Staatsbürgerschaft werden nicht in einen gemeinsamen Zeitwert umgerechnet.',
  ],
  eqparep: [
    'Gleiche Sitzverteilung im Bundestag',
    'Die Auswahl beschreibt die Unterstützung des genannten Gesetzes zur gleichen Sitzverteilung zwischen Frauen und Männern.',
  ],
  eqparlv: [
    'Gleich lange bezahlte Elternzeit',
    'Die Auswahl beschreibt die Unterstützung verpflichtender gleich langer bezahlter Elternzeit im vollständigen Doppelverdiener- und Neugeborenenszenario.',
  ],
  freinsw: [
    'Kündigung bei frauenbeleidigenden Bemerkungen',
    'Die Auswahl beschreibt die Unterstützung der Kündigung von Mitarbeitenden im genannten Fall.',
  ],
  fineqpy: [
    'Geldstrafe bei ungleicher Bezahlung',
    'Die Auswahl beschreibt die Unterstützung einer Unternehmensgeldstrafe, wenn Männer für gleiche Arbeit besser bezahlt werden als Frauen.',
  ],
  wrkprbf: [
    'Familienleistungen trotz höherer Steuern',
    'Die Auswahl beschreibt die Unterstützung zusätzlicher Leistungen für die Vereinbarkeit von Arbeit und Familie unter der ausdrücklich genannten Steuerfolge.',
  ],
};

const byId = new Map(catalogue.items.map((item) => [item.id, item]));
const studies = new Map(catalogue.studies.map((study) => [study.id, study]));
const sources = new Map(catalogue.sources.map((source) => [source.id, source]));
const licenses = new Map(catalogue.attribution.licenses.map((license) => [license.id, license]));
const democracy = catalogue.groups.find((group) => group.id === 'democracy_norms');
const democracyIds = new Set(democracy.itemIds);
const items = [];
let blockAdded = false;
for (const item of catalogue.items) {
  if (!democracyIds.has(item.id)) {
    items.push(item);
  } else if (!blockAdded) {
    items.push(...democracy.itemIds.map((id) => byId.get(id)));
    blockAdded = true;
  }
}

// Only this in-memory map holds session choices. It is not encoded in URLs or exported.
const answers = new Map(items.map((item) => [item.id, { status: 'untouched' }]));
const stateLabels = { untouched: 'Unberührt', answered: 'Beantwortet', skipped: 'Übersprungen' };
const skipLabels = {
  unspecified: 'Keine Angabe',
  'dont-know': 'Weiß nicht',
  decline: 'Keine Antwort geben',
};
const numberedTypes = new Set([
  'ordered_responsibility',
  'ordered_importance',
  'ordered_obligation',
  'ordered_direction',
]);
let index = 0;
let activeView = 'questions';

const element = (id) => document.getElementById(id);
function node(tag, text, className) {
  const result = document.createElement(tag);
  if (text !== undefined) result.textContent = text;
  if (className) result.className = className;
  return result;
}
function link(text, url) {
  const result = node('a', text);
  if (new URL(url, window.location.href).protocol !== 'https:') {
    throw new Error('Only bound HTTPS source links are allowed.');
  }
  result.href = url;
  result.target = '_blank';
  result.rel = 'noopener noreferrer';
  return result;
}
function fact(list, term, value) {
  const row = node('div');
  row.append(node('dt', term));
  const description = node('dd');
  description.append(typeof value === 'string' ? document.createTextNode(value) : value);
  row.append(description);
  list.append(row);
}
function studyName(study) {
  return study.id === 'ESS10SCe03_2' ? 'ESS10 Self-completion' : study.id.split('e')[0];
}
function origin(item) {
  const study = studies.get(item.studyId);
  return `${studyName(study)}, Datenausgabe ${study.edition}, Originalfrage ${item.originalQuestionId}`;
}
function categoryLabel(item, category) {
  if (!numberedTypes.has(item.responseType) || /^\d+$/.test(category.labelDe)) {
    return category.labelDe;
  }
  return `${category.printedCodeDe}: ${category.labelDe}`;
}
function date(value) {
  return new Intl.DateTimeFormat('de-DE', { dateStyle: 'long', timeZone: 'UTC' }).format(
    new Date(value),
  );
}
function fieldwork(study) {
  return study.fieldwork
    .map((period) => `${date(period.start)} bis ${date(period.end)}`)
    .join('; ');
}
function modes(study) {
  return [...new Set(study.fieldwork.flatMap((period) => period.modesDeclaredEn))]
    .map((mode) => {
      if (mode.includes('CAPI/CAMI'))
        return 'Persönliches computergestütztes Interview (CAPI/CAMI)';
      if (mode.includes('Paper')) return 'Selbstbeantwortung auf Papier';
      if (mode.includes('CAWI')) return 'Webselbstbeantwortung (CAWI)';
      return mode;
    })
    .join('; ');
}
function introductions(item) {
  return democracyIds.has(item.id) ? [democracy.introductionDe] : item.introductionsDe || [];
}
function appendOriginalContext(parent, item) {
  parent.append(node('h3', 'Originalkontext'));
  for (const intro of introductions(item)) parent.append(node('p', intro));
  if (item.situationDe) parent.append(node('p', item.situationDe));
  if (!introductions(item).length && !item.situationDe) {
    parent.append(
      node('p', 'Für diese Einzelangabe enthält der Katalog keine zusätzliche Einleitung.', 'meta'),
    );
  }
}
function appendWording(parent, item, tag = 'span') {
  const wording = node(tag, item.wordingDe);
  const stem = item.responseStemDe ? node(tag, item.responseStemDe) : null;
  if (stem && item.groupId !== 'migration_admission') parent.append(stem);
  parent.append(wording);
  if (stem && item.groupId === 'migration_admission') parent.append(stem);
}
function developmentNote(item) {
  if (democracyIds.has(item.id)) {
    return 'Entwicklungsfassung: B1–B12 bleiben in der Originalreihenfolge zusammen. Die vollständige Einleitung nennt nachfolgende Fragen zur Funktionsweise der Demokratie; B13–B24 wird hier bewusst ausgelassen. Einzelansicht und Gesamtfragebogenkontext sind neu. B12 erscheint im Ergebnis unter europäischer Integration.';
  }
  if (item.variable === 'scchpldm') {
    return 'Entwicklungsfassung B25: Die gebundene Papierfassung führt ursprünglich je nach Alternative zu B26 oder B28. Dieser Entwurf geht unabhängig von der Auswahl zur nächsten gewählten Frage weiter und lässt B26–B29 aus. Eine ursprüngliche operative Weiterleitung oder CAWI-Äquivalenz wird damit nicht behauptet.';
  }
  if (item.variable === 'hrshsnta') {
    return 'Originalkontext 2010/2011: „heute“ bezeichnet in dieser Frage die damalige Strafpraxis. Einzelansicht und Durchführung auf dieser Website sind eine neue Entwicklungsfassung.';
  }
  return 'Entwicklungsfassung: Die gebundene nationale Papier- oder Interviewfassung erscheint als Originalkontext. Radioauswahl, Überspringen und die neue Zusammenstellung sind keine geprüfte gleichwertige Durchführung.';
}
function sourceDetails(item, withOriginal = false) {
  const study = studies.get(item.studyId);
  const details = node('details');
  details.append(
    node(
      'summary',
      withOriginal
        ? 'Originalkontext, Kategorien, Version und Quellen'
        : 'Version, Originalanweisung und Quellen',
    ),
  );
  if (withOriginal) {
    appendOriginalContext(details, item);
    appendWording(details, item, 'p');
    const list = node('ul');
    for (const category of item.categories) list.append(node('li', categoryLabel(item, category)));
    details.append(list);
    details.append(node('p', developmentNote(item), 'context-note'));
  }
  if (item.instructionDe) {
    details.append(node('h3', 'Angabe zur Originalanweisung aus dem Katalog'));
    details.append(node('p', item.instructionDe));
    details.append(
      node(
        'p',
        'Listen- und Interviewanweisungen sind Originalkontext. Die Bedienung dieses Entwurfs führt sie nicht als ursprüngliches Feldinstrument aus.',
        'meta',
      ),
    );
  }
  const facts = node('dl', undefined, 'facts');
  fact(
    facts,
    'Urheber und Archiv',
    `${catalogue.attribution.creator}; ${catalogue.attribution.archive}`,
  );
  fact(facts, 'Quelle und Ausgabe', origin(item));
  fact(facts, 'Erhebungszeit Deutschland', fieldwork(study));
  fact(facts, 'Originale Erhebungsmodi', modes(study));
  fact(facts, 'Im Katalog gebundene Originalform', item.boundOriginalForm);
  fact(
    facts,
    'Deklarierte Zielpopulation',
    'Menschen ab 15 Jahren in Privathaushalten, unabhängig von Nationalität, Staatsangehörigkeit, Sprache oder rechtlichem Status. Dies ist die deklarierte Zielpopulation, kein Nachweis der erreichten deutschen Abdeckung.',
  );
  fact(facts, 'Originale Populationsangabe', study.populationDeclaredEn);
  if (study.id === 'ESS8e02_3') {
    fact(
      facts,
      'Dokumentierte Stichprobengrenze',
      'Die ESS8-Stichprobendokumentation berichtet, dass in München keine Befragten erfasst wurden. Gewichtung ersetzt diese nicht erhobenen Antworten nicht.',
    );
  }
  const sampling = node('details');
  sampling.append(node('summary', 'Originale Stichprobendokumentation'));
  for (const text of study.samplingProceduresDeclaredEn) sampling.append(node('p', text));
  details.append(sampling);
  fact(
    facts,
    'Historische Grenze',
    'Keine aktuelle Bevölkerungsnorm für 2026. Neue Zusammenstellung, Modus und Publikum sind nicht empirisch gleichgesetzt.',
  );
  fact(facts, 'Datenausgabe', link(`${studyName(study)} ${study.edition}, DOI`, study.dataDoiUrl));
  fact(
    facts,
    'Dokumentationszitation',
    link('Offizielle Dokumentations-DOI', study.documentationDoiUrl),
  );
  const docLicense = licenses.get(study.documentationLicenseId);
  const dataLicense = licenses.get(study.dataLicenseId);
  fact(facts, 'Originaldokumentation', link(docLicense.name, docLicense.url));
  fact(
    facts,
    'Daten separat lizenziert',
    link(`${dataLicense.name}, keine Antwortdaten eingebunden`, dataLicense.url),
  );
  details.append(facts);
  const sourceList = node('ul');
  for (const ref of item.sourceRefs) {
    const source = sources.get(ref.sourceId);
    const entry = node('li');
    const pages = ref.pdfPages.join(', ');
    const text = `${ref.listLabelDe || (ref.sourceId.includes('showcards') ? 'Originale Antwortlisten' : 'Deutsches Originalinstrument')}, PDF-Seiten ${pages}${ref.originalForm ? `, ${ref.originalForm}` : ''}`;
    entry.append(link(text, `${source.publicUrl}#page=${ref.pdfPages[0]}`));
    sourceList.append(entry);
  }
  details.append(sourceList);
  if (study.versionNotes.length) {
    details.append(node('h3', 'Versionshinweise des Katalogs'));
    for (const note of study.versionNotes) details.append(node('p', note));
  }
  const citation = node('details');
  citation.append(node('summary', 'Originale Zitationsvorgabe der Quelle'));
  const text = node('p', study.citationRequirementDeclaredEn);
  text.className = 'citation';
  citation.append(text);
  if (study.id === 'ESS10SCe03_2') {
    citation.append(
      node(
        'p',
        'Die Katalogbindung nennt Ausgabe 3.2. Die überlieferte Zitationsvorgabe nennt teilweise noch 3.1; dieser Widerspruch wird nicht stillschweigend berichtigt.',
        'context-note',
      ),
    );
  }
  details.append(citation);
  return details;
}
function updateStatus() {
  element('answer-status').textContent = stateLabels[answers.get(items[index].id).status];
}
function renderOverview() {
  const list = element('overview-list');
  const rows = items.map((item, itemIndex) => {
    const row = node('li');
    const open = node('a', `Frage ${itemIndex + 1}: ${origin(item)}`);
    open.href = '#fragen';
    open.addEventListener('click', (event) => {
      event.preventDefault();
      index = itemIndex;
      showQuestions(true);
    });
    row.append(
      open,
      node('p', item.wordingDe),
      node('p', stateLabels[answers.get(item.id).status], 'state'),
    );
    return row;
  });
  list.replaceChildren(...rows);
}
function renderQuestion(focus = false) {
  const item = items[index];
  const answer = answers.get(item.id);
  element('question-number').textContent = `Frage ${index + 1} von ${items.length}`;
  element('question-number').tabIndex = -1;
  element('question-theme').textContent = themes.find(([id]) => id === item.primaryTheme)[1];
  element('question-origin').textContent = origin(item);
  updateStatus();
  const context = element('original-context');
  context.replaceChildren();
  appendOriginalContext(context, item);
  element('development-note').textContent = developmentNote(item);
  const legend = element('question-wording');
  legend.replaceChildren();
  appendWording(legend, item);
  const choices = item.categories.map((category, categoryIndex) => {
    const label = node('label', undefined, 'answer-option');
    const radio = node('input');
    radio.type = 'radio';
    radio.name = 'original-answer';
    radio.value = String(categoryIndex);
    radio.checked = answer.status === 'answered' && answer.categoryIndex === categoryIndex;
    radio.addEventListener('change', () => {
      if (!radio.checked) return;
      answers.set(item.id, { status: 'answered', categoryIndex });
      element('skip-reason').value = 'unspecified';
      updateStatus();
      renderOverview();
    });
    label.append(radio, node('span', categoryLabel(item, category)));
    return label;
  });
  element('answer-options').replaceChildren(...choices);
  element('skip-reason').value = answer.status === 'skipped' ? answer.reason : 'unspecified';
  element('previous').disabled = index === 0;
  element('next').textContent =
    index === items.length - 1 ? 'Zum Ergebnisentwurf' : 'Zur nächsten Frage';
  element('question-sources').replaceChildren(sourceDetails(item));
  renderOverview();
  if (focus) element('question-number').focus();
}
function setView(view) {
  activeView = view;
  element('question-view').hidden = view !== 'questions';
  element('result-view').hidden = view !== 'results';
  element('page-title').textContent = view === 'questions' ? 'Fragenentwurf' : 'Ergebnisentwurf';
  element('view-lead').textContent =
    view === 'questions'
      ? '43 Originalangaben aus fünf historischen ESS-Studien bilden den Fragenentwurf. Die neue Zusammenstellung und ihre Durchführung sind noch nicht freigegeben.'
      : 'Die eigene Auswahl erscheint als getrennte Einzelangabe unter acht Themenrubriken. Unberührte und übersprungene Fragen bleiben sichtbar; historische Vergleiche sind noch nicht freigegeben.';
  for (const [id, current] of [
    ['questions-view', view === 'questions'],
    ['results-view', view === 'results'],
  ]) {
    if (current) element(id).setAttribute('aria-current', 'page');
    else element(id).removeAttribute('aria-current');
  }
}
function showQuestions(focus = false) {
  const changedView = activeView !== 'questions';
  setView('questions');
  renderQuestion(focus && !changedView);
  if (focus && changedView) element('page-title').focus();
}
function resultItem(item) {
  const answer = answers.get(item.id);
  const [title, interpretation] = meanings[item.variable];
  const article = node('article', undefined, 'result-item');
  article.append(
    node('h3', title),
    node('p', origin(item), 'meta'),
    node('p', stateLabels[answer.status], 'state'),
  );
  if (answer.status === 'answered') {
    article.append(
      node(
        'p',
        `Gewählte Originalkategorie: ${categoryLabel(item, item.categories[answer.categoryIndex])}`,
      ),
    );
    article.append(node('p', interpretation));
  } else if (answer.status === 'skipped') {
    article.append(
      node('p', `Bewusst übersprungen. Grund der Entwurfssitzung: ${skipLabels[answer.reason]}.`),
    );
    article.append(
      node(
        'p',
        'Keine politische Aussage abgeleitet. Der Grund wird keinem Missing-Code der Originalstudie gleichgesetzt.',
      ),
    );
  } else {
    article.append(
      node(
        'p',
        'Keine Auswahl und kein bewusstes Überspringen. Für diese Einzelangabe liegt keine eigene Antwort vor.',
      ),
    );
  }
  article.append(node('p', 'Historische Referenz noch nicht freigegeben', 'context-note'));
  article.append(sourceDetails(item, true));
  const edit = node('a', 'Zu dieser Originalfrage');
  edit.href = '#fragen';
  edit.className = 'text-link';
  edit.addEventListener('click', (event) => {
    event.preventDefault();
    index = items.indexOf(item);
    showQuestions(true);
  });
  article.append(edit);
  return article;
}
function showResults() {
  setView('results');
  const sections = themes.map(([id, title]) => {
    const section = node('section', undefined, 'section page-width');
    const grid = node('div', undefined, 'grid');
    const heading = node('h2', title, 'section-title area-title');
    heading.id = `result-${id}`;
    section.setAttribute('aria-labelledby', heading.id);
    const body = node('div', undefined, 'prose area-body');
    body.append(
      node(
        'p',
        'Die Rubrik ordnet konkrete Originalangaben. Sie ist keine bestätigte Dimension und erhält keinen gemeinsamen Score.',
        'meta',
      ),
    );
    for (const item of items.filter((item) => item.primaryTheme === id))
      body.append(resultItem(item));
    grid.append(heading, body);
    section.append(grid);
    return section;
  });
  element('result-view').replaceChildren(...sections);
  element('page-title').focus();
}
function advance() {
  if (index === items.length - 1) showResults();
  else {
    index += 1;
    renderQuestion(true);
  }
}

element('previous').addEventListener('click', () => {
  if (index === 0) return;
  index -= 1;
  renderQuestion(true);
});
element('next').addEventListener('click', advance);
element('skip').addEventListener('click', () => {
  answers.set(items[index].id, { status: 'skipped', reason: element('skip-reason').value });
  advance();
});
element('questions-view').addEventListener('click', (event) => {
  event.preventDefault();
  showQuestions(true);
});
element('results-view').addEventListener('click', (event) => {
  event.preventDefault();
  showResults();
});
document.querySelector('.skip-link').addEventListener('click', (event) => {
  event.preventDefault();
  element('main-content').focus();
});
showQuestions();
