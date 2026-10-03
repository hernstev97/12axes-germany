#!/usr/bin/env python3
"""Rohdatenfreie Paketintegrität und Statuskontrolle, keine Analysepipeline."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
CHECK_STATUSES = {"BESTANDEN", "NICHT_BESTANDEN", "NICHT_GEPRÜFT", "BLOCKIERT",
                  "IN_DIESER_PHASE_NICHT_ERFORDERLICH"}
LOOP_STATUSES = {"RUNNING", "BLOCKED", "READY_FOR_APPROVAL", "WAITING_FOR_HUMAN_TEST", "DONE"}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def public_input(root, name):
    relative = Path(name)
    normalized = relative.as_posix()
    forbidden = ("data/raw", "data/local", "outputs", ".git", "node_modules", ".agents")
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Eingabe muss ein relativer Projektpfad sein")
    if any(normalized == prefix or normalized.startswith(prefix + "/") for prefix in forbidden):
        raise ValueError("Nichtöffentliche oder verwaltete Eingabe verboten: " + name)
    if any(part.startswith(".env") for part in relative.parts):
        raise ValueError("Umgebungsdateien sind keine öffentlichen Eingaben")
    path = root / relative
    if not path.resolve().is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError("Eingabe fehlt oder verlässt das Projekt: " + name)
    return path

def freeze(root, output, names, metadata):
    # Alle Pfade vor Erstellung prüfen. Bestehende Fassungen nie überschreiben.
    inputs = [(name, public_input(root, name)) for name in names]
    if len(set(names)) != len(names):
        raise ValueError("Doppelte Paketpfade")
    if output.exists():
        raise ValueError("Prüfpaket existiert bereits")
    if not output.resolve().is_relative_to((root / "reports/loop/packages").resolve()):
        raise ValueError("Prüfpaket muss unter reports/loop/packages liegen")
    output.mkdir(parents=True)
    files = {}
    for name, source in inputs:
        target = output / "files" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        files[name] = {"sha256": digest(target), "bytes": target.stat().st_size}
    manifest = {**metadata, "frozenAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "files": files, "scope": "Dateifassung; keine Prüfung oder Freigabe aus Hashes ableiten"}
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest

def verify(package):
    manifest = json.loads((package / "manifest.json").read_text())
    checks = []
    for name, entry in manifest["files"].items():
        relative = Path(name)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("Ungültiger Manifestpfad")
        path = package / "files" / relative
        passed = (path.is_file() and path.resolve().is_relative_to((package / "files").resolve())
                  and digest(path) == entry["sha256"] and path.stat().st_size == entry["bytes"])
        checks.append({"file": name, "passed": passed})
    return {"manifestSha256": digest(package / "manifest.json"), "checks": checks,
            "allPassed": bool(checks) and all(c["passed"] for c in checks),
            "scope": "Datei-/Hashintegrität, keine inhaltliche Abnahme"}

def validate_state(state):
    errors = []
    if state.get("status") not in LOOP_STATUSES:
        errors.append("Ungültiger Loopstatus")
    for name, value in state.get("checks", {}).items():
        if value not in CHECK_STATUSES:
            errors.append("Ungültiger Prüfstatus: " + name)
    if state.get("status") == "DONE":
        required = {"setup", "release"} | {"phase-" + str(i) for i in range(10)}
        evidence = state.get("completionEvidence", {})
        for phase in sorted(required):
            entry = evidence.get(phase, {})
            if entry.get("status") != "BESTANDEN" or len(entry.get("manifestSha256", "")) != 64:
                errors.append("Fehlender manifestegebundener Abschluss: " + phase)
        if state.get("blockingFindingIds"):
            errors.append("DONE trotz blockierender Findings")
        if any(d.get("status") in {"BLOCKIERT", "NICHT_GEPRÜFT", "NICHT_BESTANDEN"}
               for d in state.get("dependencies", [])):
            errors.append("DONE trotz unerfüllter Pflichtvoraussetzung")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    f = sub.add_parser("freeze")
    f.add_argument("--output", required=True)
    f.add_argument("--inputs", required=True, help="JSON mit paths und metadata")
    v = sub.add_parser("verify")
    v.add_argument("package")
    sub.add_parser("status")
    sub.add_parser("all")
    args = parser.parse_args()
    if args.command == "freeze":
        spec = json.loads(public_input(ROOT, args.inputs).read_text())
        manifest = freeze(ROOT, ROOT / args.output, spec["paths"], spec["metadata"])
        print(json.dumps({"files": len(manifest["files"]), "output": args.output}))
        return 0
    if args.command == "verify":
        package = ROOT / args.package
        if not package.resolve().is_relative_to((ROOT / "reports/loop/packages").resolve()):
            raise ValueError("Nur Projektprüfpakete erlaubt")
        result = verify(package)
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result["allPassed"] else 1
    state = json.loads((ROOT / "reports/loop/state.json").read_text())
    errors = validate_state(state)
    result = {"status": state.get("status"), "stateErrors": errors,
              "blockingFindingIds": state.get("blockingFindingIds", []),
              "dependencies": state.get("dependencies", []),
              "scope": "Protokollkontrolle, keine Bestätigung wissenschaftlicher Voraussetzungen"}
    if args.command == "all":
        # Keine empirische Funktion vorhanden. Ein grüner Infrastrukturcheck
        # darf nicht das fehlende reproduzierbare wissenschaftliche Produkt ersetzen.
        result["scientificReproduction"] = "BLOCKIERT"
        result["reason"] = "Analyseplan, Erstbewertungen, öffentliche Tags und empirische Pipeline fehlen."
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if args.command == "all" else (1 if errors else 0)

if __name__ == "__main__":
    raise SystemExit(main())
