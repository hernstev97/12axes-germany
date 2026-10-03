#!/usr/bin/env python3
"""Öffentliche Paketintegrität und Protokollkontrolle, keine Analysepipeline.

Symlinks werden in Eingaben und Archivpfaden vollständig abgewiesen. Dies ist
keine Sandbox gegen gleichzeitig schreibende Benutzer oder fremde Hardlinks.
Eine formale Evidenzbindung beurteilt nicht die wissenschaftliche Tragfähigkeit.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
CHECK_STATUSES = {"BESTANDEN", "NICHT_BESTANDEN", "NICHT_GEPRÜFT", "BLOCKIERT",
                  "IN_DIESER_PHASE_NICHT_ERFORDERLICH"}
LOOP_STATUSES = {"RUNNING", "BLOCKED", "READY_FOR_APPROVAL", "WAITING_FOR_HUMAN_TEST", "DONE"}
SHA256 = re.compile(r"[0-9a-f]{64}\Z")
# Vertragskennungen für vollständige Phasen, keine frei benannten Teilprüfungen.
# Ihr Vorhandensein belegt formal den beanspruchten Umfang, nicht dessen Wahrheit.
COMPLETION_SCOPES = {phase: "LIFE-93/" + phase + "/complete-v1"
                     for phase in ["setup", "release"] + ["phase-" + str(i) for i in range(10)]}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def relative_name(name):
    if not isinstance(name, str) or not name or "\x00" in name:
        raise ValueError("Ungültiger Projektpfad")
    relative = Path(name)
    if relative.is_absolute() or ".." in relative.parts or not relative.parts:
        raise ValueError("Eingabe muss ein relativer Projektpfad sein")
    return relative


def plain_path(root, path):
    """Lexikalische und reale Grenze kontrollieren, bevor Bytes gelesen werden."""
    root = root.resolve()
    try:
        relative = path.relative_to(root)
    except ValueError as exc:
        raise ValueError("Pfad verlässt die Projektgrenze") from exc
    if ".." in relative.parts:
        raise ValueError("Pfad verlässt die Projektgrenze")
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError("Symlinks sind in öffentlichen Paketpfaden verboten")
    if not path.resolve().is_relative_to(root):
        raise ValueError("Pfad verlässt die reale Projektgrenze")
    return path


def public_input(root, name):
    root = root.resolve()
    relative = relative_name(name)
    normalized = relative.as_posix()
    forbidden = ("data/raw", "data/local", "outputs", ".git", "node_modules", ".agents")
    if any(normalized == prefix or normalized.startswith(prefix + "/") for prefix in forbidden):
        raise ValueError("Nichtöffentliche oder verwaltete Eingabe verboten: " + name)
    if any(part.startswith(".env") for part in relative.parts):
        raise ValueError("Umgebungsdateien sind keine öffentlichen Eingaben")
    path = plain_path(root, root / relative)
    if not path.is_file():
        raise ValueError("Eingabe fehlt: " + name)
    return path


def package_path(root, path):
    root = root.resolve()
    path = plain_path(root, path)
    base = root / "reports/loop/packages"
    plain_path(root, base)
    if path == base or not path.is_relative_to(base):
        raise ValueError("Prüfpaket muss unter reports/loop/packages liegen")
    return path


def freeze(root, output, names, metadata):
    root = root.resolve()
    # Alle Pfade vor Erstellung prüfen. Bestehende Fassungen nie überschreiben.
    inputs = [(relative_name(name).as_posix(), public_input(root, name)) for name in names]
    if not inputs or len({name for name, _ in inputs}) != len(inputs):
        raise ValueError("Leere oder doppelte normalisierte Paketpfade")
    output = package_path(root, output)
    if output.exists():
        raise ValueError("Prüfpaket existiert bereits")
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


def verify(package, root=ROOT):
    package = package_path(root, package)
    manifest_path = plain_path(root, package / "manifest.json")
    manifest = json.loads(manifest_path.read_text())
    files = manifest.get("files")
    if not isinstance(files, dict) or not files:
        raise ValueError("Leeres oder ungültiges Prüfmanifest")
    archive = plain_path(root, package / "files")
    checks = []
    names = set()
    for name, entry in files.items():
        normalized = relative_name(name).as_posix()
        if normalized in names:
            raise ValueError("Doppelte normalisierte Manifestpfade")
        names.add(normalized)
        path = public_input(archive, name)
        expected = entry.get("sha256", "")
        size = entry.get("bytes")
        passed = (isinstance(expected, str) and SHA256.fullmatch(expected) is not None
                  and isinstance(size, int) and not isinstance(size, bool) and size >= 0
                  and digest(path) == expected and path.stat().st_size == size)
        checks.append({"file": name, "passed": passed})
    return {"manifestSha256": digest(manifest_path), "checks": checks,
            "allPassed": all(c["passed"] for c in checks),
            "scope": "Datei-/Hashintegrität, keine inhaltliche Abnahme"}


def completion_binding(root, phase, entry):
    """Konkrete öffentliche Fassung mit einem formalen Abnahmeprotokoll verbinden."""
    expected_scope = COMPLETION_SCOPES.get(phase)
    if expected_scope is None or entry.get("scope") != expected_scope:
        raise ValueError("Abschlussumfang entspricht nicht dem vollständigen Phasenvertrag")
    for key in ("manifestSha256", "reportSha256"):
        value = entry.get(key)
        if not isinstance(value, str) or not SHA256.fullmatch(value):
            raise ValueError("Ungültiger Evidenzhash: " + key)
    manifest = public_input(root, entry.get("manifest"))
    if manifest.name != "manifest.json":
        raise ValueError("Abschluss braucht ein Paketmanifest")
    if digest(manifest) != entry["manifestSha256"]:
        raise ValueError("Abschlussmanifest hat abweichenden Hash")
    if not verify(manifest.parent, root)["allPassed"]:
        raise ValueError("Abschlussarchiv hat abweichende Dateien")
    report = public_input(root, entry.get("report"))
    if digest(report) != entry["reportSha256"]:
        raise ValueError("Abnahmebericht hat abweichenden Hash")
    protocol = json.loads(report.read_text())
    if (protocol.get("phase") != phase or protocol.get("status") != "BESTANDEN"
            or protocol.get("manifestSha256") != entry["manifestSha256"]
            or protocol.get("scope") != expected_scope
            or not isinstance(protocol.get("checks"), list) or not protocol["checks"]
            or any(c.get("status") != "BESTANDEN" or not c.get("evidence")
                   for c in protocol["checks"])):
        raise ValueError("Abnahmeprotokoll passt nicht zum benannten Abschlussumfang")


def validate_state(state, root=ROOT):
    errors = []
    done = state.get("status") == "DONE"
    if state.get("status") not in LOOP_STATUSES:
        errors.append("Ungültiger Loopstatus")
    for name, value in state.get("checks", {}).items():
        if value not in CHECK_STATUSES:
            errors.append("Ungültiger Prüfstatus: " + name)
        if done and value != "BESTANDEN":
            errors.append("DONE trotz nicht bestandenem aktuellem Check: " + name)
    for dependency in state.get("dependencies", []):
        if dependency.get("status") not in CHECK_STATUSES:
            errors.append("Ungültiger Abhängigkeitsstatus: " + dependency.get("id", "?"))
        if done and dependency.get("status") != "BESTANDEN":
            errors.append("DONE trotz unerfüllter Pflichtvoraussetzung: " + dependency.get("id", "?"))
    for package in state.get("workPackages", []):
        if package.get("status") not in LOOP_STATUSES:
            errors.append("Ungültiger Arbeitspaketstatus: " + package.get("id", "?"))
        if done and package.get("status") != "DONE":
            errors.append("DONE trotz offenem Arbeitspaket: " + package.get("id", "?"))
    if done:
        if state.get("activeAgents"):
            errors.append("DONE trotz aktiven Agents")
        required = {"setup", "release"} | {"phase-" + str(i) for i in range(10)}
        evidence = state.get("completionEvidence", {})
        for phase in sorted(required):
            entry = evidence.get(phase, {})
            try:
                if entry.get("status") != "BESTANDEN":
                    raise ValueError("Keine bestandene Abnahme")
                completion_binding(root, phase, entry)
            except (ValueError, OSError, TypeError, KeyError, AttributeError) as exc:
                errors.append("Ungültiger formaler Abschluss " + phase + ": " + str(exc))
        if state.get("blockingFindingIds"):
            errors.append("DONE trotz blockierender Findings")
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
        freeze(ROOT, ROOT / relative_name(args.output), spec["paths"], spec["metadata"])
        print(json.dumps({"files": len(spec["paths"]), "output": args.output}))
        return 0
    if args.command == "verify":
        result = verify(ROOT / relative_name(args.package))
        print(json.dumps(result, ensure_ascii=False))
        return 0 if result["allPassed"] else 1
    state = json.loads(public_input(ROOT, "reports/loop/state.json").read_text())
    errors = validate_state(state)
    result = {"status": state.get("status"), "stateErrors": errors,
              "blockingFindingIds": state.get("blockingFindingIds", []),
              "dependencies": state.get("dependencies", []),
              "scope": "Formale Protokoll-/Evidenzbindung, keine Bestätigung wissenschaftlicher Voraussetzungen"}
    if args.command == "all":
        result["scientificReproduction"] = "BLOCKIERT"
        result["reason"] = "Analyseplan, Erstbewertungen, öffentliche Tags und empirische Pipeline fehlen."
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if args.command == "all" else (1 if errors else 0)


if __name__ == "__main__":
    raise SystemExit(main())
