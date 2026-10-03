#!/usr/bin/env python3
"""Pinned R stages. Synthetic runs are public probes; A runs require receipts.

Landlock limits the twelve listed child write rights. This wrapper does not
isolate reads, network, devices, the supervisor, or other agents on the shared FS.
No shell commands, arbitrary R entry points, installers, or gate bypass flags.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PROJECT = Path(__file__).resolve().parents[1]
SOFTWARE = "outputs/loop/software-env"
PREFIX = SOFTWARE + "/envs/r-smoke"
RSCRIPT = PREFIX + "/bin/Rscript"
RSCRIPT_SHA = "152d8b4f60d5c76403402d072825252c0ff96f6035e01d2562eecd864ad7a0ec"
# Complete existing prefix, including dependencies and symlink targets.
PREFIX_SHA = "3bc6b04077406586ef84c901beff6d93d04db3ea74160ad1ae45f4e6eba3b2e4"
RIGHTS = "write-file,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate"
LIMITS = "Listed child write rights only; no complete read/network/device/supervisor/agent isolation"
SYNTHETIC_ROOT = "outputs/loop/r-runtime"
PRIVATE_ROOT = "data/local/empirical-v1"
PRIVATE_RECEIPT = PRIVATE_ROOT + "/runtime-input-receipt.json"
PRIVATE_INPUT = PRIVATE_ROOT + "/A.csv"
ASSIGNMENT = PRIVATE_ROOT + "/assignment.json"
GATE_PATH = "reports/loop/gates/pre-empirical.json"
CODE_SUPPORT = (
    "pipeline/r_runtime.py", "pipeline/ordinal/reproduce-support.R",
    "pipeline/ordinal/test-support.R", "pipeline/ordinal/support.R", "pipeline/ordinal/adapter_v2.R",
)
CODE_DEVELOPMENT = (
    "pipeline/r_runtime.py", "pipeline/empirical_access.py", "pipeline/ordinal/develop.R",
    "pipeline/ordinal/develop-config.R", "pipeline/ordinal/support.R", "pipeline/ordinal/adapter_v2.R",
)
SUPPORT_PINS = {
    "pipeline/ordinal/test-support.R": "2083f0fff96f67477bb211b11aa50d1315987cb3a7b0e12bc73588adfcea96bd",
    "pipeline/ordinal/support.R": "b1b986e05424e11208f9184c5159f3d628cc032b48a36c028aa6ef222c81ae22",
    "pipeline/ordinal/adapter_v2.R": "8786b8c1d60eadd2bd3faf88eb175e9df2e7afc952b7dbc26cb58ce15d7d038b",
}
CUSTOM_PACKAGE_PINS = {
    "lavaan": "db9e4883c1b8ed2abc2d09602225018b236bd54d79b959ca3f899e8078e7c24c",
    "semTools": "e22b63d1396c967151b9e3baba56a98982bca1776a381dd1f600948317eca3df",
}
PACKAGE_VERSIONS = {
    "MASS": "7.3.66", "base": "4.5.3", "grDevices": "4.5.3", "graphics": "4.5.3",
    "jsonlite": "2.0.0", "lavaan": "0.7.2", "methods": "4.5.3", "mnormt": "2.1.2",
    "numDeriv": "2016.8.1.1", "pbivnorm": "0.6.0", "quadprog": "1.5.8", "semTools": "0.5.9",
    "stats": "4.5.3", "stats4": "4.5.3", "utils": "4.5.3",
}


class RuntimeErrorCode(Exception):
    """Fixed codes, never input values or arbitrary library messages."""


def require(condition, code):
    if not condition:
        raise RuntimeErrorCode(code)


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def digest(path):
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def regular_path(root, relative, *, private=False):
    """Check every component without following a symlink or finding input files."""
    path = root / relative
    require(path.is_absolute() and ".." not in path.parts and path.is_relative_to(root), "PATH")
    current = Path(path.anchor)
    for component in path.parts[1:]:
        current /= component
        require(not current.is_symlink(), "SYMLINK")
        require(current.exists(), "MISSING_PATH")
    require(path.is_file(), "REGULAR_FILE")
    if private:
        for parent in (root / "data/local", root / PRIVATE_ROOT):
            require(parent.is_dir() and parent.stat().st_mode & 0o077 == 0, "PRIVATE_PARENT_MODE")
        require(path.stat().st_mode & 0o777 == 0o600, "PRIVATE_FILE_MODE")
    return path


def tree_digest(root, *, prefix=False):
    """Sorted relative path + NUL + file SHA bytes; prefix adds F/L type tags."""
    h = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix().encode()
        if path.is_symlink():
            require(prefix and path.resolve().is_relative_to(root.resolve()), "RUNTIME_SYMLINK")
            h.update(b"L" + relative + b"\0" + str(path.readlink()).encode() + b"\0")
        elif path.is_file():
            h.update((b"F" if prefix else b"") + relative + b"\0" + bytes.fromhex(digest(path)))
    return h.hexdigest()


def validate_runtime(root):
    rscript = regular_path(root, RSCRIPT)
    require(digest(rscript) == RSCRIPT_SHA, "RSCRIPT_PIN")
    prefix = root / PREFIX
    require(tree_digest(prefix, prefix=True) == PREFIX_SHA, "RUNTIME_PREFIX_PIN")
    packages = {}
    for name, expected in CUSTOM_PACKAGE_PINS.items():
        package = root / SOFTWARE / "r-library" / name
        regular_path(root, str(package.relative_to(root) / "DESCRIPTION"))
        packages[name] = tree_digest(package)
        require(packages[name] == expected, "R_PACKAGE_PIN")
    return {"rscriptSha256": RSCRIPT_SHA, "prefixTreeSha256": PREFIX_SHA,
            "customPackageTreeSha256": packages, "expectedPackageVersions": PACKAGE_VERSIONS}


def code_hashes(root, paths):
    return {relative: digest(regular_path(root, relative)) for relative in paths}


def preflight_private(root=PROJECT):
    """Gate + remote tags + code pins precede all private receipt/input reads.

    Coordinator receipts are mutable on a shared FS, not cryptographic trust.
    Input rehashes reduce accidental drift; they do not close a concurrent race.
    """
    sys.dont_write_bytecode = True  # Parent imports must not create public cache output.
    from pipeline import empirical_access as access

    # Inspect only public gate paths before the existing gate follows artifact paths.
    # A public alias/symlink must not let gate() read private inputs prematurely.
    gate_file = regular_path(root, GATE_PATH)
    preview = json.loads(gate_file.read_text())
    for entry in [*preview.get("artifacts", []), *preview.get("reviews", [])]:
        relative = entry.get("path")
        require(isinstance(relative, str) and not Path(relative).is_absolute() and
                ".." not in Path(relative).parts and
                not relative.startswith(("data/raw/", "data/local/")), "GATE_PUBLIC_PATH")
        regular_path(root, relative)
    receipt = access.gate(root)  # Actual reviewed artifacts, Python version, local + remote tags.
    spec = receipt.get("runtime", {})
    require(spec.get("schema") == "r-runtime-v1", "GATE_RUNTIME_SCHEMA")
    require(spec.get("sourceSha256") == access.SHA, "SOURCE_PIN")
    require(spec.get("privateReceiptPath") == PRIVATE_RECEIPT, "RECEIPT_PATH")
    reviewed = spec.get("reviewedCodeHashes", {})
    require(isinstance(reviewed, dict) and set(CODE_DEVELOPMENT).issubset(reviewed), "REVIEWED_CODE_SET")
    # All receipt-listed code pins are checked before the first private read.
    for relative, expected in reviewed.items():
        require(isinstance(relative, str) and relative.startswith(("pipeline/", "data/")) and
                not relative.startswith(("data/raw/", "data/local/")), "REVIEWED_CODE_PATH")
        require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected), "REVIEWED_CODE_HASH")
        require(digest(regular_path(root, relative)) == expected, "REVIEWED_CODE_PIN")
    public_gate_sha = digest(regular_path(root, GATE_PATH))
    private_receipt_path = regular_path(root, PRIVATE_RECEIPT, private=True)
    private_receipt = json.loads(private_receipt_path.read_text())
    require(private_receipt.get("schema") == "r-runtime-input-v1", "PRIVATE_RECEIPT_SCHEMA")
    require(private_receipt.get("sourceSha256") == access.SHA and
            private_receipt.get("gateSha256") == public_gate_sha and
            private_receipt.get("empiricalAccessSha256") == reviewed["pipeline/empirical_access.py"],
            "PRIVATE_RECEIPT_BINDING")
    observed = {}
    for key, relative in (("assignment", ASSIGNMENT), ("developmentInput", PRIVATE_INPUT)):
        binding = private_receipt.get(key, {})
        require(binding.get("path") == relative and
                isinstance(binding.get("sha256"), str) and
                re.fullmatch(r"[0-9a-f]{64}", binding["sha256"]), "PRIVATE_INPUT_BINDING")
        path = regular_path(root, relative, private=True)
        observed[key] = digest(path)
        require(observed[key] == binding["sha256"], "PRIVATE_INPUT_PIN")
        if key == "assignment":
            split = json.loads(path.read_text())
            require(split.get("inputSha256") == access.SHA and split.get("seed") == 2026100301,
                    "ASSIGNMENT_SOURCE_PIN")
    return {"gateSha256": public_gate_sha, "reviewedCodeHashes": reviewed,
            "privateReceiptSha256": digest(private_receipt_path), "sourceSha256": access.SHA,
            "assignmentSha256": observed["assignment"], "aSha256": observed["developmentInput"]}


def make_output(root, label, private):
    require(bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", label)), "LABEL")
    relative = PRIVATE_ROOT + "/runtime-runs" if private else SYNTHETIC_ROOT
    parent = root / relative
    current = Path(root.anchor)
    for component in parent.parts[1:]:
        current /= component
        require(not current.is_symlink(), "OUTPUT_SYMLINK")
        if current.exists():
            require(current.is_dir(), "OUTPUT_PARENT")
        else:
            current.mkdir(mode=0o700)
        if private and current.is_relative_to(root / "data/local"):
            require(current.stat().st_mode & 0o077 == 0, "PRIVATE_PARENT_MODE")
    own = parent / label
    require(not own.exists() and not own.is_symlink(), "DO_NOT_OVERWRITE")
    own.mkdir(mode=0o700)
    require(own.stat().st_mode & 0o777 == 0o700, "OUTPUT_MODE")
    return own


def exclusive_text(path, payload):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "w") as stream:
        stream.write(payload)


def save_json(path, value):
    exclusive_text(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def source_snapshots(root, own, hashes):
    snapshots = {}
    for relative, expected in hashes.items():
        source = regular_path(root, relative)
        payload = source.read_text()
        require(hashlib.sha256(payload.encode()).hexdigest() == expected, "CODE_SNAPSHOT_DRIFT")
        target = own / "source-snapshot" / relative
        target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        exclusive_text(target, payload)
        snapshots[relative] = str(target.relative_to(own))
    return snapshots


def scoped_environment(root, own):
    env = dict(os.environ)
    home = env.get("HOME")
    require(bool(home), "HOME_REQUIRED")
    for key in list(env):
        if key.startswith(("CONDA_", "MAMBA_", "R_", "R_LIBS", "R_ENVIRON", "R_PROFILE")) or key in (
            "CONDARC", "MAMBARC", "PYTHONPATH", "PYTHONHOME", "LD_PRELOAD", "LD_LIBRARY_PATH", "ENV", "BASH_ENV"
        ):
            del env[key]
    env.update(HOME=home, PATH=str(root / PREFIX / "bin") + ":/usr/bin:/bin",
               TZ="UTC", LC_ALL="C.UTF-8", LANG="C.UTF-8", OPENBLAS_NUM_THREADS="1", OMP_NUM_THREADS="1",
               MKL_NUM_THREADS="1", BLIS_NUM_THREADS="1", VECLIB_MAXIMUM_THREADS="1",
               R_LIBS_USER=str(root / SOFTWARE / "r-library"), R_LIBS_SITE=str(root / SOFTWARE / "r-library"),
               R_HISTFILE=str(own / "no-Rhistory"), R_PROFILE_USER=str(own / "profile-sentinel.R"),
               R_ENVIRON_USER=str(own / "Renviron-sentinel"), ESS_RUNTIME_OUTPUT=str(own))
    for key, relative in {
        "TMPDIR": "tmp", "TEMP": "tmp", "TMP": "tmp", "XDG_CACHE_HOME": "cache",
        "XDG_DATA_HOME": "data", "XDG_CONFIG_HOME": "config", "R_USER_CACHE_DIR": "cache/R",
    }.items():
        path = own / relative
        path.mkdir(mode=0o700, parents=True, exist_ok=True)
        env[key] = str(path)
    require(env["HOME"] == os.environ["HOME"], "HOME_CHANGED")
    return env


def child_command(root, own, entry, arguments):
    return ["/usr/bin/setpriv", "--no-new-privs", "--landlock-access", "fs:" + RIGHTS,
            "--landlock-rule", "path-beneath:" + RIGHTS + ":" + str(own),
            "--landlock-rule", "path-beneath:write-file:/dev/null",
            str(root / RSCRIPT), "--vanilla", str(entry), *arguments]


def runtime_probe(root, own):
    versions = json.dumps(PACKAGE_VERSIONS)
    expected_paths = {name: str(root / (SOFTWARE + "/r-library" if name in CUSTOM_PACKAGE_PINS
                                      else PREFIX + "/lib/R/library") / name) for name in PACKAGE_VERSIONS}
    return """args <- commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==3L, identical(Sys.getenv('HOME'),args[[3]]),
          identical(as.character(getRversion()),'4.5.3'))
expected <- jsonlite::fromJSON(%s)
paths <- jsonlite::fromJSON(%s)
versions <- setNames(lapply(names(expected),function(x)as.character(packageVersion(x))),names(expected))
actual_paths <- setNames(lapply(names(expected),function(x)normalizePath(find.package(x))),names(expected))
stopifnot(all(vapply(names(expected),function(x)identical(versions[[x]],expected[[x]]),logical(1))),
          all(vapply(names(paths),function(x)identical(actual_paths[[x]],paths[[x]]),logical(1))))
outside <- file.path(dirname(args[[2]]),paste0(basename(args[[2]]),'-outside-write-probe'))
stopifnot(!file.exists(outside))
write_denied <- !isTRUE(suppressWarnings(file.create(outside)))
stopifnot(write_denied,!file.exists(outside))
jsonlite::write_json(list(R=as.character(getRversion()),packages=versions,package_paths=actual_paths,
  outside_write_denied=write_denied,
  libraries=.libPaths(),HOME=Sys.getenv('HOME'),timezone=Sys.getenv('TZ'),locale=Sys.getenv('LC_ALL')),
  file.path(args[[2]],'runtime.json'),auto_unbox=TRUE,pretty=TRUE)
cat('R_RUNTIME_VERSION_PINS_PASSED\\n')
""" % (json.dumps(versions), json.dumps(json.dumps(expected_paths)))


def development_entry(synthetic):
    setup = """initialized <- ed_initialize(project)
cfg <- initialized$config
RNGkind('Mersenne-Twister','Inversion','Rejection');set.seed(2026100325L)
g <- 192L;n <- g*40L;psu <- rep(seq_len(g),each=40L)
stratum <- rep(rep(1:4,each=g/4L),each=40L)
phi <- matrix(.1,3L,3L);diag(phi)<-1
eta <- MASS::mvrnorm(n,rep(0,3),phi)+MASS::mvrnorm(g,rep(0,3),.12*phi)[psu,]
frame <- data.frame(stratum=stratum,psu=psu,weight=runif(n,.5,1.5))
for(j in seq_along(cfg$items)) {
  k <- length(cfg$manifest[[cfg$items[j]]]);lambda <- .82
  z <- lambda*eta[,ceiling(j/3)]+rnorm(n,sd=sqrt(1-lambda^2))
  frame[[cfg$items[j]]] <- as.integer(cut(z,c(-Inf,qnorm(seq_len(k-1L)/k),Inf),labels=FALSE))-1L
}
input <- file.path(own,'invented-frame.csv')
frame[psu%%48L==1L,cfg$items] <- NA
utils::write.csv(frame,input,row.names=FALSE,na='NA');Sys.chmod(input,'0600')
""" if synthetic else "input <- args[[4]]\n"
    return """args <- commandArgs(trailingOnly=TRUE)
stopifnot(length(args)==%dL,identical(Sys.getenv('HOME'),args[[3]]))
project <- normalizePath(args[[1]],mustWork=TRUE);own <- normalizePath(args[[2]],mustWork=TRUE)
stopifnot(identical(own,Sys.getenv('ESS_RUNTIME_OUTPUT')))
source(file.path(project,'pipeline/ordinal/develop.R'))
%s
code <- ed_main(project_root=project,input_A_csv=input,private_output_dir=own,
  authorization=list(decision='ACCEPTED_BOUNDED',arm='A',wrapper_verified=TRUE,syntheticFake=%s),retain_fits=TRUE)
quit(status=code)
""" % (3 if synthetic else 4, setup, "TRUE" if synthetic else "FALSE")


def execute(command, env, own, log_name, timeout):
    fd = os.open(own / log_name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "w") as log:
        try:
            result = subprocess.run(command, env=env, cwd=own, input="", text=True,
                                    stdout=log, stderr=subprocess.STDOUT, close_fds=True, timeout=timeout)
            return result.returncode
        except subprocess.TimeoutExpired:
            return 124


def file_inventory(own):
    inventory = {}
    for path in sorted(own.rglob("*")):
        require(not path.is_symlink(), "OUTPUT_SYMLINK")
        if path.is_file():
            require(path.stat().st_mode & 0o777 == 0o600, "OUTPUT_FILE_MODE")
            inventory[str(path.relative_to(own))] = {"sha256": digest(path), "bytes": path.stat().st_size}
    return inventory


def run(stage, label, root=PROJECT):
    private = stage == "development-a"
    require(stage in ("support", "development", "development-a"), "STAGE")
    require(bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}", label)), "LABEL")
    os.umask(0o077)
    authorization = preflight_private(root) if private else None
    paths = CODE_SUPPORT if stage == "support" else CODE_DEVELOPMENT
    hashes = code_hashes(root, paths)
    if stage == "support":
        require(all(hashes[path] == expected for path, expected in SUPPORT_PINS.items()), "SUPPORT_CODE_PIN")
    runtime_pins = validate_runtime(root)
    own = make_output(root, label, private)
    snapshots = source_snapshots(root, own, hashes)
    env = scoped_environment(root, own)
    probe = own / "runtime-probe.R"
    exclusive_text(probe, runtime_probe(root, own))
    probe_command = child_command(root, own, probe, [str(root), str(own), env["HOME"]])
    if stage == "support":
        internal_label = "test-fixed-v2-" + label
        entry = root / "pipeline/ordinal/reproduce-support.R"
        arguments = [str(root), str(own), env["HOME"], internal_label]
    else:
        entry = own / "development-entry.R"
        exclusive_text(entry, development_entry(not private))
        arguments = [str(root), str(own), env["HOME"]]
        if private:
            arguments.append(str(root / PRIVATE_INPUT))
    command = child_command(root, own, entry, arguments)
    record = {"schema": "r-runtime-run-v1", "stage": stage, "label": label, "startedAtUtc": utc(),
              "scope": "private A development" if private else "invented synthetic responses only",
              "command": command, "runtimeProbeCommand": probe_command, "cwd": str(own),
              "codeHashes": hashes, "sourceSnapshots": snapshots, "pythonVersion": sys.version.split()[0],
              "runtimePins": runtime_pins, "privateAuthorization": authorization,
              "childHandledWriteRights": RIGHTS.split(","), "childAllowRules": [str(own), "/dev/null:write-file"],
              "limits": LIMITS, "receiptTrustLimit": "Coordinator receipts are mutable on shared FS; concurrent races are not excluded",
              "homeUnchanged": env["HOME"] == os.environ["HOME"], "noCondaCall": True,
              "environment": {k: env[k] for k in ("HOME", "PATH", "TZ", "LC_ALL", "OPENBLAS_NUM_THREADS",
                  "OMP_NUM_THREADS", "R_LIBS_USER", "R_LIBS_SITE", "TMPDIR", "XDG_CACHE_HOME", "XDG_DATA_HOME",
                  "XDG_CONFIG_HOME", "R_USER_CACHE_DIR", "R_HISTFILE", "R_PROFILE_USER", "R_ENVIRON_USER")}}
    save_json(own / "start.json", record)
    try:
        record["runtimeProbeExitCode"] = execute(probe_command, env, own, "runtime-probe.log", 60)
        if record["runtimeProbeExitCode"] != 0:
            record["exitCode"] = record["runtimeProbeExitCode"]
        else:
            # Recheck private source/code receipts immediately before R can read A.
            if private:
                require(preflight_private(root) == authorization, "PRIVATE_PREFLIGHT_DRIFT")
            record["exitCode"] = execute(command, env, own, "stage.log", 600)
        record["runtimePinsAfter"] = validate_runtime(root)
        require(code_hashes(root, paths) == hashes, "CODE_DRIFT")
        if private:
            require(preflight_private(root) == authorization, "PRIVATE_INPUT_DRIFT")
    except RuntimeErrorCode as error:
        record["exitCode"] = 2
        record["failureCode"] = "R_RUNTIME_" + str(error)
    except Exception:
        record["exitCode"] = 2
        record["failureCode"] = "R_RUNTIME_STAGE_OR_RECEIPT_ERROR"
    record["endedAtUtc"] = utc()
    try:
        record["filesBeforeFinalReceipt"] = file_inventory(own)
    except Exception:
        record["exitCode"] = 2
        record["failureCode"] = "R_RUNTIME_OUTPUT_METADATA_ERROR"
    save_json(own / "receipt.json", record)
    print("R_RUNTIME_PRIVATE_COMPLETED" if private else f"{label} exitCode {record['exitCode']}")
    return record["exitCode"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    synthetic = sub.add_parser("synthetic", help="Invented input only, fresh 0700 outputs/loop run folder")
    synthetic.add_argument("--stage", choices=("support", "development"), default="support")
    synthetic.add_argument("--label", required=True)
    private = sub.add_parser("development-a", help="Fixed A.csv only; real gate, tags, code/input receipts required")
    private.add_argument("--label", required=True)
    args = parser.parse_args()
    try:
        stage = args.stage if args.command == "synthetic" else "development-a"
        return run(stage, args.label)
    except RuntimeErrorCode as error:
        print("R_RUNTIME_" + str(error), file=sys.stderr)
        return 2
    except Exception:
        print("R_RUNTIME_INPUT_OR_GATE_ERROR", file=sys.stderr)
        return 2


if __name__ == "__main__":
    # Support direct execution without relying on an ignored author launcher.
    sys.path.insert(0, str(PROJECT))
    sys.exit(main())
