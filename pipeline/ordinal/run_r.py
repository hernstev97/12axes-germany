#!/usr/bin/env python3
"""Run only the ordinal-support synthetic probes in the pinned local R runtime.

The listed child filesystem write rights are limited by Landlock. Read,
network, device, and supervisor isolation are not claimed.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[2]
OWN = PROJECT / "outputs/loop/resume-ordinal-support"
BASE = PROJECT / "outputs/loop/software-env"
MANIFEST = PROJECT / "reports/loop/packages/SOFTWARE-001/v1/manifest.json"
MANIFEST_HASH = "126ab5309ec15a42ebd7b07d63e7c47eb8397d2d9d57b0a1c78675d4ca660a0e"
RSCRIPT_HASH = "152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec"
RIGHTS = "write-file,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate"


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def own_path(path):
    if not path.resolve().is_relative_to(OWN.resolve()) or path.is_symlink():
        raise RuntimeError("Output path escaped synthetic directory")
    return path


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in (
        "inspect-001", "inspect-002", "inspect-003", "test-001", "test-002", "test-003", "test-004",
        "test-005", "test-006", "test-007", "test-008", "test-adapter-v2-001",
        "test-strong-v2-001", "test-strong-v2-002", "test-fixed-001", "test-fixed-002", "test-009",
        "test-fixed-v2-001"
    ):
        raise RuntimeError("Only fixed synthetic labels are supported")
    label = sys.argv[1]
    if OWN.is_symlink() or not OWN.is_dir() or OWN.resolve() != OWN:
        raise RuntimeError("Synthetic output directory must be a real project directory")
    if digest(MANIFEST) != MANIFEST_HASH:
        raise RuntimeError("Frozen software manifest mismatch")
    manifest = json.loads(MANIFEST.read_text())
    source_hashes = {entry["path"]: entry["sha256"] for entry in manifest["sourceInputs"]}
    bindings = {}
    for relative in (
        "outputs/loop/software-author/run-r-direct.py",
        "outputs/loop/software-author/scoped-env.json",
    ):
        actual = digest(PROJECT / relative)
        if actual != source_hashes[relative]:
            raise RuntimeError("Frozen launcher or environment mismatch")
        bindings[relative] = actual
    scoped = json.loads((PROJECT / "outputs/loop/software-author/scoped-env.json").read_text())
    rscript = BASE / "envs/r-smoke/bin/Rscript"
    if not rscript.is_file() or not rscript.resolve().is_relative_to(BASE.resolve()) or digest(rscript) != RSCRIPT_HASH:
        raise RuntimeError("Pinned direct Rscript mismatch")
    if label.startswith("inspect"):
        probe = own_path(OWN / "inspect.R")
    elif label.startswith("test-adapter-v2"):
        probe = own_path(OWN / "test-adapter-v2.R")
    elif label.startswith("test-strong-v2"):
        probe = own_path(OWN / "test-strong-v2.R")
    else:
        probe = PROJECT / "pipeline/ordinal/test-support.R"
    plan = own_path(OWN / "plan-before-run.md")
    if not probe.is_file() or not plan.is_file():
        raise RuntimeError("Probe and prior plan required")
    env = dict(os.environ)
    for key in list(env):
        if key.startswith(("CONDA_", "MAMBA_", "R_LIBS", "R_ENVIRON", "R_PROFILE")) or key in (
            "CONDARC", "MAMBARC", "R_HOME", "R_USER", "PYTHONPATH", "PYTHONHOME"
        ):
            del env[key]
    for key in ("LC_ALL", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "TZ", "R_LIBS_USER", "R_LIBS_SITE"):
        env[key] = scoped[key]
    for key in ("R_LIBS_USER", "R_LIBS_SITE"):
        if not Path(env[key]).resolve().is_relative_to(BASE.resolve()):
            raise RuntimeError("Pinned R library path escaped software prefix")
    for key, relative in {
        "TMPDIR": "tmp", "TEMP": "tmp", "TMP": "tmp",
        "XDG_CACHE_HOME": "cache", "XDG_DATA_HOME": "data", "XDG_CONFIG_HOME": "config",
        "R_USER_CACHE_DIR": "cache/R",
    }.items():
        path = own_path(OWN / relative)
        path.mkdir(parents=True, exist_ok=True)
        env[key] = str(path)
    home_before = os.environ.get("HOME")
    if not home_before or env.get("HOME") != home_before:
        raise RuntimeError("HOME must remain unchanged")
    env.update(R_HISTFILE=str(own_path(OWN / "no-Rhistory")),
               R_PROFILE_USER=str(own_path(OWN / "profile-sentinel.R")),
               R_ENVIRON_USER=str(own_path(OWN / "Renviron-sentinel")),
               PATH=str(BASE / "envs/r-smoke/bin") + os.pathsep + "/usr/bin:/bin")
    command = ["/usr/bin/setpriv", "--no-new-privs", "--landlock-access", "fs:" + RIGHTS,
               "--landlock-rule", "path-beneath:" + RIGHTS + ":" + str(OWN),
               "--landlock-rule", "path-beneath:write-file:/dev/null",
               str(rscript), "--vanilla", str(probe), str(PROJECT), str(OWN), home_before, label]
    command_path = own_path(OWN / (label + "-command.json"))
    log_path = own_path(OWN / (label + ".log"))
    if command_path.exists() or log_path.exists():
        raise RuntimeError("Prior run must not be overwritten")
    code_paths = [probe, Path(__file__), PROJECT / "pipeline/ordinal/adapter.R"]
    support = PROJECT / "pipeline/ordinal/support.R"
    if support.is_file():
        code_paths.append(support)
    if label.startswith(("test-adapter-v2", "test-strong-v2", "test-fixed-v2")):
        code_paths.append(PROJECT / "pipeline/ordinal/adapter_v2.R")
    record = dict(label=label, command=command, cwd=str(OWN), startedAtUtc=utc(),
                  childHandledWriteRights=RIGHTS.split(","),
                  childAllowRules=[str(OWN), "/dev/null:write-file"],
                  limits="Listed child write rights only; no full read/network/device/supervisor isolation",
                  homeUnchanged=env["HOME"] == home_before, noCondaCall=True,
                  originalInputBindings=bindings, manifestSha256=digest(MANIFEST),
                  planSha256=digest(plan), rscriptSha256=digest(rscript),
                  codeHashes={str(path.relative_to(PROJECT)): digest(path) for path in code_paths},
                  scopedEnvironment={key: env[key] for key in (
                      "HOME", "PATH", "LC_ALL", "TZ", "OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS",
                      "TMPDIR", "TEMP", "TMP", "XDG_CACHE_HOME", "XDG_DATA_HOME", "XDG_CONFIG_HOME",
                      "R_USER_CACHE_DIR", "R_HISTFILE", "R_PROFILE_USER", "R_ENVIRON_USER",
                      "R_LIBS_USER", "R_LIBS_SITE")})
    command_path.write_text(json.dumps(record, indent=2) + "\n")
    try:
        with log_path.open("x") as log:
            result = subprocess.run(command, env=env, cwd=OWN, input="", text=True,
                                    stdout=log, stderr=subprocess.STDOUT, close_fds=True, timeout=600)
        record["exitCode"] = result.returncode
    except subprocess.TimeoutExpired:
        record["exitCode"] = 124
        record["failure"] = "Probe timed out and child was killed"
    finally:
        record["endedAtUtc"] = utc()
        record["rscriptSha256After"] = digest(rscript)
        record["manifestSha256After"] = digest(MANIFEST)
        command_path.write_text(json.dumps(record, indent=2) + "\n")
    print(label, "exitCode", record["exitCode"])
    return record["exitCode"]


if __name__ == "__main__":
    sys.exit(main())
