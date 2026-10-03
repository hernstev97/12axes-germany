// Formale synthetische Gegenfälle, kein realer Review oder Quellennachweis.
import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';
import Ajv2020 from 'ajv/dist/2020.js';

const schema = JSON.parse(
  readFileSync(
    new URL('../.claude/skills/life93-review/references/urteil-schema.json', import.meta.url),
  ),
);
const validate = new Ajv2020({ strict: true, allErrors: true }).compile(schema);
const hash = 'a'.repeat(64); // ausdrücklich erfundene Formalfixture
const base = {
  schemaVersion: 1,
  mode: 'SYNTHETISCHE_SKILLPRUEFUNG',
  task: 'Prüfe nur diese synthetische Struktur',
  scope: 'Formale Schema-Gegenfälle',
  manifestSha256: hash,
  status: 'BESTANDEN',
  execution: {
    provider: 'Codex',
    model: null,
    modelEvidence: 'Modellversion unbekannt; diese Fixture behauptet keinen Modelllauf',
    internalRevision: null,
    internalInstructions: null,
    tools: ['Ajv 8.20.0'],
    prompt: 'Synthetischer Strukturtest, keine wissenschaftliche Prüfung',
    inputHashes: { synthetic: hash },
  },
  checks: [
    {
      id: 'SYN-1',
      scope: 'Formalfixture',
      status: 'BESTANDEN',
      requiredInScope: true,
      evidence: ['Synthetischer Beleg'],
    },
  ],
  findings: [],
  limits: ['Hashstrings werden hier nicht gegen echte Dateien geprüft'],
};
const finding = {
  id: 'SYN-F01',
  claim: 'Erfundene Behauptung',
  problem: 'Erfundener Gegenfall',
  evidence: ['Synthetische Fundstelle'],
  impact: 'Nur Formatprüfung',
  severity: 'erheblich',
  severityReason: 'Erfundene blockierende Folge',
  correction: 'Synthetische Reparatur',
  recheck: 'Erfundener Gegenfall',
  certainty: 'BELEGT',
  blocksScope: true,
  state: 'OFFEN',
};
const cases = [];
function check(name, expected, mutate = () => {}) {
  const value = structuredClone(base);
  mutate(value);
  const observed = validate(value);
  assert.equal(observed, expected, `${name}: ${JSON.stringify(validate.errors)}`);
  cases.push({ name, expected, observed });
}
check('gültiger begrenzter Erfolg mit unbekannter Modellversion', true);
check('fehlendes Manifest bei Erfolg', false, (v) => {
  v.manifestSha256 = null;
});
check('keine Checks bei Erfolg', false, (v) => {
  v.checks = [];
});
check('keine Eingabehashes bei Erfolg', false, (v) => {
  v.execution.inputHashes = {};
});
check('leerer Prompt', false, (v) => {
  v.execution.prompt = '';
});
check('leerer Modellbeleg', false, (v) => {
  v.execution.modelEvidence = ' ';
});
check('erforderlicher negativer Check', false, (v) => {
  v.checks[0].status = 'NICHT_BESTANDEN';
});
check('erforderlicher ungeprüfter Check', false, (v) => {
  v.checks[0].status = 'NICHT_GEPRÜFT';
});
check('kein erforderlicher Check', false, (v) => {
  v.checks[0].requiredInScope = false;
});
check('bestandener Check ohne Beleg', false, (v) => {
  v.checks[0].evidence = [];
});
check('bestandener Check mit leerem Beleg', false, (v) => {
  v.checks[0].evidence = [''];
});
check('offenes blockierendes Finding bei Erfolg', false, (v) => {
  v.findings = [finding];
});
check('leerer Findingtext', false, (v) => {
  v.status = 'NICHT_BESTANDEN';
  v.findings = [{ ...finding, problem: '' }];
});
check('korrigiertes Finding blockiert widersprüchlich', false, (v) => {
  v.findings = [{ ...finding, state: 'KORRIGIERT' }];
});
check('ehrlich blockiert ohne Manifest oder Hashes', true, (v) => {
  v.status = 'BLOCKIERT';
  v.manifestSha256 = null;
  v.execution.inputHashes = {};
  v.checks[0].status = 'BLOCKIERT';
  v.checks[0].evidence = [];
});
check('negatives Urteil mit blockierendem Finding', true, (v) => {
  v.status = 'NICHT_BESTANDEN';
  v.findings = [finding];
});
check('späterer außerhalb Scope ungeprüfter Check', true, (v) => {
  v.checks.push({
    id: 'SYN-FUTURE',
    scope: 'Spätere Empirie',
    status: 'IN_DIESER_PHASE_NICHT_ERFORDERLICH',
    requiredInScope: false,
    evidence: [],
  });
});
check('späteres Finding außerhalb Scope', true, (v) => {
  v.findings = [{ ...finding, blocksScope: false, state: 'AUSSERHALB_SCOPE' }];
});
console.log(
  JSON.stringify(
    {
      status: 'BESTANDEN',
      scope:
        '18 synthetische Schemafälle; keine Quellen-, Hash-, Claude- oder wissenschaftliche Abnahme',
      cases,
    },
    null,
    2,
  ),
);
