#!/usr/bin/env python3
"""Datei-/Protokollprüfungen für das KI-Audit; keine ESS-Antwortanalyse."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess

root = Path(__file__).resolve().parents[2]
audit = root / "reports/audit-recherche"

def digest(path):
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

parser = argparse.ArgumentParser()
parser.add_argument("--phase", choices=["eingang", "vor-juror", "abschluss"], required=True)
parser.add_argument("--output", required=True, help="JSON-Prüfbeleg, relativ zum Repository")
args = parser.parse_args()
checks = []
manifest = json.loads((audit / "ausgangsmanifest.json").read_text())
for relative, expected in manifest["files"].items():
    checks.append({"name": "unveränderte Ausgangsfassung", "file": relative,
                   "passed": digest(audit / "ausgangsfassung" / relative) == expected["sha256"]})
for relative, expected in manifest["auditInputFiles"].items():
    checks.append({"name": "unveränderter Issue-/Erstauftrag", "file": relative,
                   "passed": digest(audit / relative) == expected})

raw_relative = "data/raw/ess11-ed4.2/ESS11e04_2.csv"
raw = root / raw_relative
checks.append({"name": "Rohdatei unverändert", "file": raw_relative,
               "passed": raw.exists() and digest(raw) == "4b0bfa73fa86bcf9f868b0a6145f96504a40d7e3f2deeb3e822555993ab32dc8"})
checks.append({"name": "Rohdatei von Git ausgeschlossen",
               "passed": subprocess.run(["git", "check-ignore", "--quiet", raw_relative],
                                        cwd=root).returncode == 0})
tracked = subprocess.check_output(["git", "ls-files", "data/raw", "data/local"],
                                  cwd=root, text=True).splitlines()
checks.append({"name": "Keine Roh-/Zwischendaten getrackt",
               "passed": tracked == ["data/raw/.gitkeep"], "trackedPaths": tracked})

if args.phase in {"vor-juror", "abschluss"}:
    corrected = json.loads((audit / "korrekturmanifest.json").read_text())
    for relative, expected in corrected["files"].items():
        checks.append({"name": "Korrigierter Forschungsstand", "file": relative,
                       "passed": digest(root / relative) == expected["sha256"]})
    for relative, expected in corrected["reviewerReports"].items():
        checks.append({"name": "Unveränderter unabhängiger Erstbericht", "file": relative,
                       "passed": digest(root / relative) == expected})
    decisions = json.loads((audit / "finding-entscheidungen.json").read_text())
    all_ids = [finding["id"] for finding in decisions["findings"]]
    checks.append({"name": "Eindeutige Finding-IDs", "passed": len(all_ids) == len(set(all_ids))})
    allowed = {"angenommen", "teilweise angenommen", "verworfen"}
    for finding in decisions["findings"]:
        checks.append({"name": "Dokumentierte Autorentscheidung", "finding": finding["id"],
                       "passed": finding.get("decision") in allowed
                                 and bool(finding.get("reason"))
                                 and bool(finding.get("evidence"))
                                 and bool(finding.get("verification"))})
    for reviewer in range(1, 6):
        report_files = list(audit.glob("reviewer-" + str(reviewer) + "-*.md"))
        checks.append({"name": "Erstbericht vorhanden", "reviewer": reviewer,
                       "passed": len(report_files) == 1})
    if args.phase == "abschluss":
        checks.append({"name": "Jurorbericht vorhanden",
                       "passed": (audit / "juror-6.md").exists()})

result = {"kind": "audit-integrity-check", "phase": args.phase,
          "performedAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "scriptSha256": digest(Path(__file__).resolve()),
          "checks": checks, "allChecksPassed": all(check["passed"] for check in checks),
          "scope": "Dateihashes, Protokollvollständigkeit und Git-Ausschluss; keine inhaltliche Prüfung, Validitäts- oder Neutralitätsbestätigung."}
output = root / args.output
if not output.is_relative_to(audit):
    raise SystemExit("Prüfbeleg muss unter reports/audit-recherche liegen")
output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"phase": args.phase, "checks": len(checks),
                  "allChecksPassed": result["allChecksPassed"],
                  "output": str(output.relative_to(root))}))
raise SystemExit(0 if result["allChecksPassed"] else 1)

