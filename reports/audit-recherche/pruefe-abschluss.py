#!/usr/bin/env python3
"""Zusätzliche Integritätskontrolle nach dem Juror; keine fachliche Freigabe."""
from pathlib import Path
import datetime
import hashlib
import json

root = Path(__file__).resolve().parents[2]
audit = root / "reports/audit-recherche"
checks = []

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

fixed = {
    "ausgangsmanifest.json": "dab36982ce6aac113acc2f807611e8630b546ee451684d683a096e0b4fd23cd8",
    "korrekturmanifest.json": "c6fef40eff714e5e15bdf045c6e46f92b2e14bddda14a24148e56349c2439406",
    "finding-entscheidungen.json": "e4703993a389d19144b60623c92ac4690b008774b37f57fec124fa16656b63fc",
    "juror-6.md": "6beed214a6c22551317ed3e2aefcac92d33d7930d5545c4dd0649a3f1754ccd8",
    "04-korrekturpruefung.json": "7b1acf077d19f5ba2a540c100004a2b12c0dcf3b7e078f110c422838f2c4b29c",
    "technische-pruefung.json": "0a3447cb9f37c283a9f2cebb1902b2dce684167f961888686614631674bbd4db",
}
for name, expected in fixed.items():
    checks.append({"name": "Geschützter Bezug unverändert", "file": name,
                   "passed": sha(audit / name) == expected})
for manifest_name, directory in [("ausgangsmanifest.json", "ausgangsfassung"),
                                  ("korrekturmanifest.json", "korrekturfassung")]:
    manifest = json.loads((audit / manifest_name).read_text())
    for name, expected in manifest["files"].items():
        path = audit / directory / name
        checks.append({"name": "Archivhash und Bytezahl", "file": directory + "/" + name,
                       "passed": sha(path) == expected["sha256"]
                                 and path.stat().st_size == expected["bytes"]})
registry = json.loads((audit / "agent-protokoll.json").read_text())
calls = registry["spawnCalls"]
checks.append({"name": "Sechs dokumentierte abgeschlossene Subagents",
               "passed": len(calls) == 6 and all(c["observedStatus"] == "completed" for c in calls)})
for call in calls:
    checks.append({"name": "Abgeschlossener Bericht unverändert", "agent": call["returnedTaskName"],
                   "passed": sha(root / call["reportPath"]) == call["reportSha256"]})
for entry in json.loads((audit / "juror-belegregister.json").read_text())["files"]:
    path = root / entry["preservedCopy"]
    checks.append({"name": "Unveränderte Kopie eines Jurorbelegs", "file": entry["preservedCopy"],
                   "passed": sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]})
for name in ["technische-pruefung.json", "technische-pruefung-final.json", "technische-pruefung-abschluss.json"]:
    run = json.loads((audit / name).read_text())
    checks.append({"name": "Tatsächlicher erfolgreicher Lauf und Loghash", "file": name,
                   "passed": run["exitCode"] == 0 and sha(root / run["logPath"]) == run["logSha256"]})
    manifest = root / run["inputManifest"]
    checks.append({"name": "Eingabemanifest zum technischen Lauf", "file": name,
                   "passed": sha(manifest) == run["inputManifestSha256"]})
final_inputs = json.loads((audit / "technischer-pruefstand-abschluss.json").read_text())
for name, expected in final_inputs["files"].items():
    checks.append({"name": "Aktiver öffentlicher Prüfstand unverändert", "file": name,
                   "passed": sha(root / name) == expected})
result = {"kind": "additional-final-audit-integrity-check",
          "performedAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "command": ["python", "reports/audit-recherche/pruefe-abschluss.py"],
          "scriptSha256": sha(Path(__file__).resolve()), "checks": checks,
          "allChecksPassed": all(c["passed"] for c in checks),
          "scope": "Geschützte Archive, Berichte, tatsächliche technische Läufe und öffentlicher Prüfstand; keine wissenschaftliche Prüfung."}
(audit / "08-abschluss-hashes.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"checks": len(checks), "allChecksPassed": result["allChecksPassed"]}))
raise SystemExit(0 if result["allChecksPassed"] else 1)
