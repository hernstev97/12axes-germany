#!/usr/bin/env python3
"""Prüft Auditartefakte und wiederholt synthetische Gegenrechnungen, keine ESS-Analyse."""
from pathlib import Path
import ast
import datetime
import hashlib
import importlib.metadata
import json
import re
import subprocess
import urllib.request

import jsonschema
import yaml

root = Path(__file__).resolve().parents[2]
audit = root / "reports/audit-recherche"
local = root / "outputs/audit-recherche"
local.mkdir(parents=True, exist_ok=True)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
checks = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def add(name, passed, scope):
    checks.append({"name": name, "passed": bool(passed), "scope": scope})

registry = json.loads((audit / "agent-protokoll.json").read_text())
review_ids = set()
for call in registry["spawnCalls"]:
    if not call["task_name"].startswith("reviewer_"):
        continue
    path = root / call["reportPath"]
    add("Unveränderter Erstbericht " + call["task_name"],
        sha(path) == call["reportSha256"], "Dateiintegrität")
    review_ids.update(re.findall(r"^### (R[1-5]-F\d{2})", path.read_text(), re.M))

dispositions = json.loads((audit / "finding-entscheidungen.json").read_text())
listed = [f["id"] for f in dispositions["findings"]]
add("Alle Erstfindings einzeln entschieden",
    review_ids == {i for i in listed if i.startswith("R")} and len(listed) == len(set(listed)),
    "Protokollvollständigkeit, keine inhaltliche Richtigkeitsprüfung")

data = (root / "docs/datenlage.md").read_text()
rules = (root / "docs/pruefregeln.md").read_text()
plan = (root / "docs/analyseplan.md").read_text()
contracts = (root / "docs/analyseanforderungen.md").read_text()
add("Versionswarnung präzisiert", "Alte Ausgaben sind daher" not in data
    and "keine pauschale Untauglichkeit von 4.0 oder 4.1" in data,
    "Formaler Textabgleich nach Originallektüre")
add("Parteibezug konsistent", "parteibenannte" not in rules
    and "Fragen mit Parteibezug" in rules and "Einleitung/Filter" in rules,
    "Formaler Regelabgleich; noch keine Item-Erstbewertung")
add("Persönliche Statistik-Abnahme nicht neu eingeführt",
    "keine persönliche Statistik-Abnahme" in plan,
    "Abgrenzung gegen Phase 0, keine Erfüllung späterer Voraussetzungen")
add("Spätere Anforderungen als offen gekennzeichnet",
    "Keine der dort geforderten empirischen Prüfungen ist bereits durchgeführt" in plan
    and "Noch keine" in contracts,
    "Statuswortlaut, keine empirische Prüfung")
add("Keine finale Auswahl- und Analyseartefakte",
    all(not (root / p).exists() for p in
        ["data/inventar.csv", "docs/themenabdeckung.md", "docs/erwartungsmodell.md", "model/v1.json"]),
    "Tatsächlich noch fehlende Artefakte")
add("Keine Präregistrierungs-/Modell-Tags",
    not subprocess.check_output(["git", "tag", "--list", "*-v1"], cwd=root, text=True).strip(),
    "Lokale Tagliste, keine allgemeine Chronologiegarantie")

catalog = json.loads((root / "docs/quellen.json").read_text())
sources = [s["id"] for s in catalog["sources"]]
add("Quellen-IDs eindeutig", len(sources) == len(set(sources)), "Registerstruktur")
claims = set(re.findall(r"\bB-[A-Z]+-\d{3}\b", (root / "docs/belegregister.md").read_text()))
add("Neue tragende Quellenbefunde registriert",
    {"B-CONT-001", "B-CONT-002", "B-METH-005", "B-METH-006"}.issubset(claims),
    "Belegstruktur, keine Quellenvalidierung")

evidence = json.loads((audit / "quellenbelege.json").read_text())
for entry in evidence["evidence"]:
    add("Lokaler datierter Quellenbeleg " + entry["sourceId"],
        sha(root / entry["localFullCapture"]) == entry["localFullCaptureSha256"],
        "Hash des tatsächlichen aktuellen Abrufs, kein historischer Rückbeweis")
version = json.loads((root / evidence["evidence"][0]["localFullCapture"]).read_text())["section"]
blocks = {v: version.split("ESS11 edition " + v + " ")[1].split("ESS11 edition ")[0]
          for v in ["4.2", "4.1", "4.0"]}
add("Gesicherte Versionsstelle trägt die engere Warnung",
    "Germany: Error in stratum variable corrected." in blocks["4.0"]
    and "Germany" not in blocks["4.1"] and "Germany" not in blocks["4.2"],
    "Versionshinweisinhaltsprüfung; fehlender Eintrag beweist keine Dateigleichheit")

schema_url = "https://coderabbit.ai/integrations/schema.v2.json"
with urllib.request.urlopen(schema_url, timeout=30) as response:
    schema_bytes = response.read()
schema_path = local / "coderabbit-schema-v2.json"
schema_path.write_bytes(schema_bytes)
schema = json.loads(schema_bytes)
config_path = root / ".coderabbit.yaml"
validator = jsonschema.validators.validator_for(schema)
validator.check_schema(schema)
validator(schema).validate(yaml.safe_load(config_path.read_text()))
add("CodeRabbit-Konfiguration gegen aktuelles Originalschema", True,
    "Technische Schema-Gültigkeit, kein CodeRabbit-Lauf oder Methodenreview")

synthetic = audit / "synthetische-gegenbeispiele.py"
result = subprocess.run(["python", str(synthetic)], cwd=root, text=True,
                        capture_output=True, check=True)
(audit / "synthetische-gegenbeispiele.log").write_text(result.stdout)
lines = result.stdout.splitlines()
missing = ast.literal_eval(lines[0].split(":", 1)[1].strip())
dominance = ast.literal_eval(lines[1].split(":", 1)[1].strip())
covariance = ast.literal_eval(lines[2].split(":", 1)[1].strip())
mirror = ast.literal_eval(lines[3].split(":", 1)[1].strip())
add("Teilantwort-Gegenrechnung wiederholt",
    missing["teil_score_vollnorm"] == 0.25 and missing["teil_score_maskennorm"] == 0.75,
    "Erfundene Werte; keine Normmethode oder ESS-Prüfung validiert")
add("Dominanz-Gegenrechnung wiederholt",
    dominance["voll_scores"] == [0.25, 0.5, 0.75]
    and dominance["ohne_variables_item"] == [0.5, 0.5, 0.5],
    "Erfundene Werte; kein tatsächliches dominantes ESS-Item festgestellt")
add("Kovarianz-Gegenrechnung wiederholt",
    abs(covariance["0.9"] - 0.0447213595499958) < 1e-12
    and abs(covariance["-0.9"] - 0.1949358868961793) < 1e-12,
    "Erfundene Kovarianzen; kein Rangverfahren validiert")
add("Algebraische Spiegelung mit festen Missing-Masken",
    mirror["max_fehlbetrag"] < 1e-12,
    "Drei synthetische Fälle; keine politische Gegenhaltung oder Perzentilsymmetrie bewiesen")

# Lokale Ziele nur in der aktiven Forschungsdokumentation, keine externen URL-Checks.
missing_links = []
for path in (root / "docs").rglob("*.md"):
    for target in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", path.read_text()):
        target = target.strip().strip("<>").split("#", 1)[0]
        if not target or re.match(r"^[a-z]+:", target):
            continue
        if not (path.parent / target).exists():
            missing_links.append({"file": str(path.relative_to(root)), "target": target})
add("Lokale Markdown-Ziele", not missing_links, "Dateiexistenz, keine externe Linkprüfung")

output = {"kind": "performed-correction-checks", "startedAtUtc": started,
          "endedAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "scriptSha256": sha(Path(__file__).resolve()),
          "versions": {"python": subprocess.check_output(["python", "--version"], text=True).strip(),
                       "jsonschema": importlib.metadata.version("jsonschema"),
                       "PyYAML": importlib.metadata.version("PyYAML")},
          "schema": {"url": schema_url, "localPath": str(schema_path.relative_to(root)),
                     "sha256": sha(schema_path), "configurationSha256": sha(config_path)},
          "sourceCount": len(sources), "claimCount": len(claims),
          "reviewerFindingCount": len(review_ids), "decisionCount": len(listed),
          "synthetic": {"scriptSha256": sha(synthetic),
                        "logSha256": sha(audit / "synthetische-gegenbeispiele.log")},
          "checks": checks, "missingLinks": missing_links,
          "allChecksPassed": all(c["passed"] for c in checks),
          "notPerformed": ["vollständiges Inventar/Themen-/Erwartungsmodell",
                           "ESS-Import, Split, EFA/CFA, Invarianz und Reliabilität",
                           "persönliche Messintervalle, Norm-/Rangvalidierung",
                           "andere Modellfamilie, konkrete Item-Erstbewertungen",
                           "CodeRabbit-Lauf, menschliche Verständlichkeit"]}
(audit / "04-korrekturpruefung.json").write_text(
    json.dumps(output, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"checks": len(checks), "allChecksPassed": output["allChecksPassed"],
                  "reviewerFindings": len(review_ids), "sources": len(sources),
                  "claims": len(claims), "missingLinks": missing_links}))
raise SystemExit(0 if output["allChecksPassed"] else 1)

