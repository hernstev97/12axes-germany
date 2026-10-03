#!/usr/bin/env python3
"""Reproduce the historical public C-v2 annotation without private ESS data."""
import argparse
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = "70ad20618e3b2084cbbb300f50b387d465a47cb97aa3b06be30ec5b59fc5ef5e"
PUBLIC_INPUTS = {
    "data/inventar.entwurf.csv": "8c73adb8b361db2992f5fe9e321e0c5b978afdc41ba22c1cbb471f92e60057c1",
    "data/inventar.provenienz.json": "533a12c517ac49f869aea1fbc09dc86e3c1dfe7ef9bc7b05018b5a49ba753aa6",
}
PUBLIC_PDFS = [
    ("ESS11_questionnaires_DE.pdf", "https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf", "be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75"),
    ("ESS11_showcards_DE.pdf", "https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf", "786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca"),
    ("ESS11_appendix_a7_e04_1.pdf", "https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf", "b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35"),
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plain_path(path):
    if not path.is_relative_to(ROOT):
        raise ValueError("Path outside this checkout")
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError("Symlink path is not accepted")
        if part == ROOT:
            break
    return path


def fresh_output(name):
    relative = Path(name)
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("Expected a relative output path without parent components")
    if relative.parts[:2] != ("outputs", "public-reproduction") or len(relative.parts) < 3:
        raise ValueError("Output must be a new child of outputs/public-reproduction")
    target = plain_path(ROOT / relative)
    if target.exists():
        raise ValueError("Existing output directory will not be overwritten")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    output = fresh_output(args.output_dir)
    inputs = {}
    for name, expected in PUBLIC_INPUTS.items():
        path = plain_path(ROOT / name)
        actual = digest(path)
        if actual != expected:
            raise ValueError("Public inventory input pin mismatch: " + name)
        inputs[name] = actual
    output.mkdir(parents=True, exist_ok=False)
    sources = output / "sources"
    sources.mkdir()
    record = {
        "startedAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "scope": "Reproduction of historical public document annotation, no ESS answers",
        "historicalAnnotationMetadataRetained": True,
        "expectedAnnotationSha256": EXPECTED,
        "publicInputs": inputs,
        "sourceDownloads": [],
        "status": "RUNNING",
        "scienceAcceptance": "NICHT_GEPRÜFT",
    }
    record_path = output / "reproduction.json"
    try:
        for filename, url, expected in PUBLIC_PDFS:
            started = datetime.datetime.now(datetime.timezone.utc).isoformat()
            with urllib.request.urlopen(url, timeout=30) as response:
                data = response.read()
                status = response.status
                final_url = response.url
            path = sources / filename
            path.write_bytes(data)
            actual = digest(path)
            record["sourceDownloads"].append({
                "url": url, "finalUrl": final_url, "startedAtUtc": started,
                "endedAtUtc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "httpStatus": status, "path": path.relative_to(ROOT).as_posix(),
                "sha256": actual, "expectedSha256": expected, "bytes": len(data),
            })
            if actual != expected:
                raise ValueError("Public PDF pin mismatch: " + filename)
        folder = ROOT / "pipeline/annotations"
        sys.dont_write_bytecode = True
        sys.path.insert(0, str(folder))
        spec = importlib.util.spec_from_file_location("historical_c_builder_v2", folder / "c_builder_v2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.OWN = output
        module.CACHE = sources
        module.TARGET = output / "annotation.json"
        sys.argv = [str(folder / "c_builder_v2.py"), "--out", str(module.TARGET), "--work", str(output / "build-inputs")]
        module.main()
        actual = digest(module.TARGET)
        record["annotationSha256"] = actual
        if actual != EXPECTED:
            raise ValueError("Generated annotation differs from historical C-v2 bytes")
        for name, expected in PUBLIC_INPUTS.items():
            if digest(plain_path(ROOT / name)) != expected:
                raise ValueError("Public inventory input changed during reproduction: " + name)
        version = subprocess.run(["pdftotext", "-v"], text=True, capture_output=True)
        record["runtime"] = {"python": sys.version, "pdftotextVersion": version.stdout + version.stderr, "versionExit": version.returncode}
        record["status"] = "BESTANDEN"
    except BaseException as error:
        record["status"] = "NICHT_BESTANDEN"
        record["errorType"] = type(error).__name__
        record["error"] = str(error)
        raise
    finally:
        record["endedAtUtc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
        record_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": record["status"], "sha256": record["annotationSha256"], "record": record_path.relative_to(ROOT).as_posix()}))


if __name__ == "__main__":
    main()
