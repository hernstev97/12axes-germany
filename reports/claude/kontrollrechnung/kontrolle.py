#!/usr/bin/env python3
"""Unabhängige Kontrollrechnung V1 für LIFE-93 v2 / v2.1.

Eigenständige, bewusst einfache Implementierung nach der Spezifikation
(docs/empirie-plan-v2.entwurf.md, data/analysevertrag.v2.entwurf.json,
data/gruppenvertrag.v2.1.entwurf.json, data/politikprofil-v2.fragen.entwurf.json).
Der vorhandene Rechencode unter pipeline/ und scripts/run-*.py wurde für diese
Implementierung nicht gelesen.

Datenschutz:
- Liest die fünf lokalen CSV-Dateien unter data/raw/ nur zeilenweise im Speicher.
- Gibt keine Zeilen, keine Personenkennungen, keine Einzelgewichte und keine
  Zellbesetzungen von 1 bis 4 aus (Hilfsfunktion `safe`).
- Fehlermeldungen enthalten nie Zellinhalte.
- Schreibt ausschließlich `vergleich.json` neben diese Datei. Berechnete Werte
  für zurückgehaltene Referenzen werden weder ausgegeben noch geschrieben.

Nur Python-Standardbibliothek. Aufruf aus dem Repository-Stamm:
    PYTHONDONTWRITEBYTECODE=1 python3 reports/claude/kontrollrechnung/kontrolle.py
"""

from __future__ import annotations

import csv
import datetime as _dt
import hashlib
import json
import math
import re
import statistics
import sys
import traceback
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT_JSON = HERE / "vergleich.json"

ANALYSIS_CONTRACT = ROOT / "data/analysevertrag.v2.entwurf.json"
GROUP_CONTRACT = ROOT / "data/gruppenvertrag.v2.1.entwurf.json"
CATALOGUE = ROOT / "data/politikprofil-v2.fragen.entwurf.json"
REF_DIR = ROOT / "data/reference-v2"
GROUP_REF_DIR = ROOT / "data/reference-groups-v21"

# Gruppenweg: veröffentlicht und laut Reproduktionsdokument nur ESS5/8/9.
GROUP_STUDIES = ("ESS5e03_6", "ESS8e02_3", "ESS9e03_3")

# Kanonischer Integertext mit optionalem nullwertigem Bruchteil (Vertrag).
CANON = re.compile(r"^(0|[1-9][0-9]*)(?:\.0+)?$")

MIN_VALID = 100        # publicationRules.minimumValidCount
MIN_CELL = 5           # publicationRules.minimumPositiveCellCount
TOL = 1e-12            # arithmeticTolerance / ratioDiagnostic.tolerance

ST_NONE = "no_valid_answers"
ST_WITHHELD = "withheld_base_or_cell_count"
ST_PREPARED = "prepared_pending_result_review"

csv.field_size_limit(sys.maxsize)


class SafeError(Exception):
    """Fehler mit garantiert inhaltsfreier Meldung."""


def safe(n: int):
    """Zählwerte 1–4 werden nie ausgegeben."""
    return n if n == 0 or n >= MIN_CELL else "1-4"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(raw: str):
    """Liefert ('blank', None) | ('code', kanonischer Code) | ('literal', None)."""
    if raw == "":
        return "blank", None
    m = CANON.match(raw)
    if m is None:
        return "literal", None
    return "code", m.group(1)


def parse_weight(raw: str):
    try:
        w = float(raw)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(w) or w <= 0:
        return None
    return w


def round_ok(raw: str, expected: str) -> bool:
    m = CANON.match(raw)
    return m is not None and m.group(1) == expected


def edition_ok(raw: str, expected: str) -> bool:
    try:
        return Decimal(raw) == Decimal(expected)
    except (InvalidOperation, TypeError):
        return False


# ---------------------------------------------------------------- Einlesen


def read_de(path: Path, wanted: list[str]):
    """Liest nur benötigte Spalten der DE-Zeilen. Gibt nur Aggregate zurück."""
    diag = {}
    with open(path, newline="", encoding="utf-8", errors="surrogateescape") as fh:
        reader = csv.reader(fh)
        header = next(reader)
        if header and header[0].startswith("﻿"):
            header[0] = header[0][1:]
        dup = [k for k, v in Counter(header).items() if v > 1]
        diag["headerColumns"] = len(header)
        diag["duplicateHeaderNames"] = len(dup)
        diag["duplicateWantedHeaders"] = sorted(set(dup) & set(wanted))
        present = [c for c in wanted if c in header]
        diag["missingWantedColumns"] = [c for c in wanted if c not in header]
        idx = {c: header.index(c) for c in present}
        ci = idx["cntry"]
        total = 0
        bad_len = 0
        near_de = 0
        rows = []
        for row in reader:
            total += 1
            if len(row) != len(header):
                bad_len += 1
                continue
            cv = row[ci]
            if cv != "DE":
                if cv.strip().upper() == "DE":
                    near_de += 1
                continue
            rows.append({c: row[i] for c, i in idx.items()})
    diag["dataRowsAllCountries"] = total
    diag["rowsWithWrongFieldCount"] = safe(bad_len)
    diag["nonCanonicalDEVariants"] = safe(near_de)
    diag["deRows"] = len(rows)
    return rows, diag, set(idx)


# ---------------------------------------------------------------- Tabellierung


def tabulate(rows, var, cats, missing, not_asked, weights):
    """Kategorienanteile einer Frage über die übergebenen Zeilen.

    weights: dict schema -> Liste der Gewichte parallel zu rows
             (Schema 'unweighted' ist implizit 1).
    """
    cat_set = set(cats)
    n_cat = Counter()
    w_cat = {s: defaultdict(list) for s in weights}
    miss_n = Counter()
    miss_w = defaultdict(list)
    not_asked_n = 0
    unknown_code = 0
    unknown_literal = 0
    for i, r in enumerate(rows):
        kind, code = classify(r[var])
        if kind == "blank":
            reason = missing.get("")
            if reason is None:
                unknown_literal += 1
                continue
            miss_n[reason] += 1
            miss_w[reason].append(weights["pspwght"][i])
            continue
        if kind == "literal":
            unknown_literal += 1
            continue
        if code in cat_set:
            n_cat[code] += 1
            for s, ws in weights.items():
                w_cat[s][code].append(ws[i])
        elif code in missing:
            reason = missing[code]
            miss_n[reason] += 1
            miss_w[reason].append(weights["pspwght"][i])
        elif code in not_asked:
            not_asked_n += 1
        else:
            unknown_code += 1
    valid = sum(n_cat.values())
    props = {}
    for s in list(weights) + ["unweighted"]:
        if s == "unweighted":
            sums = {c: float(n_cat[c]) for c in cats}
        else:
            sums = {c: math.fsum(w_cat[s][c]) for c in cats}
        denom = math.fsum(sums.values())
        props[s] = [sums[c] / denom for c in cats] if denom > 0 else None
    small_cell = any(1 <= n_cat[c] < MIN_CELL for c in cats)
    if valid == 0:
        status = ST_NONE
    elif valid < MIN_VALID or small_cell:
        status = ST_WITHHELD
    else:
        status = ST_PREPARED
    reasons_order = [missing[k] for k in missing]  # Vertragsreihenfolge
    return {
        "status": status,
        "reasonBase": valid < MIN_VALID,
        "reasonCell": small_cell,
        "validCount": valid,
        "missingCount": sum(miss_n.values()),
        "notAskedCount": not_asked_n,
        "unknownCode": unknown_code,
        "unknownLiteral": unknown_literal,
        "totalCount": len(rows),
        "codes": list(cats),
        "props": props,
        "missingReasons": [
            {"reason": r, "count": miss_n[r], "primaryWeightSum": math.fsum(miss_w[r])}
            for r in reasons_order
        ],
        "missingWeight": math.fsum(x for r in miss_w.values() for x in r),
    }


def max_abs(a, b):
    if a is None or b is None:
        return None
    return max(abs(x - y) for x, y in zip(a, b))


# ---------------------------------------------------------------- Vergleich


def cmp_marginal(own, pub_q, all_de_weight, an_ratio):
    """Vergleicht eigene Einzelrechnung mit veröffentlichter Frage."""
    res = {
        "statusVeroeffentlicht": pub_q["status"],
        "statusBerechnet": own["status"],
    }
    ref = pub_q["reference"]
    published = pub_q["status"] == "reviewed_historical_reference"
    # Status-Übereinstimmung: veröffentlichte Referenz setzt eigene
    # 100/5-Prüfung 'prepared' voraus; Zurückhaltung muss gleich lauten.
    res["statusKonsistent"] = (
        (published and own["status"] == ST_PREPARED)
        or (not published and own["status"] == pub_q["status"])
    )
    if ref is None:
        res["referenzLeer"] = True
        return res
    codes_pub = [c["code"] for c in ref["categories"]]
    res["kategorienGleich"] = codes_pub == own["codes"]
    pub_props = [c["proportion"] for c in ref["categories"]]
    res["maxAbsAbweichungAnteil"] = max_abs(own["props"]["pspwght"], pub_props)
    res["nennerGleich"] = (
        ref["validCount"] == own["validCount"]
        and ref["totalCount"] == own["totalCount"]
        and ref["missingCount"] == own["missingCount"]
        and ref["notAskedCount"] == own["notAskedCount"]
    )
    pub_mr = {m["reason"]: m for m in ref["missingReasons"]}
    own_mr = {m["reason"]: m for m in own["missingReasons"]}
    res["missingGruendeGleich"] = (
        set(pub_mr) == set(own_mr)
        and all(pub_mr[k]["count"] == own_mr[k]["count"] for k in own_mr)
    )
    res["maxAbsAbweichungMissingGewicht"] = max(
        [abs(pub_mr[k]["primaryWeightSum"] - own_mr[k]["primaryWeightSum"]) for k in own_mr if k in pub_mr]
        + [abs(ref["missingWeight"] - own["missingWeight"])]
    )
    res["absAbweichungAllDEWeight"] = abs(ref["allDEWeight"] - all_de_weight)
    own_unw = max_abs(own["props"]["pspwght"], own["props"]["unweighted"])
    own_dw = max_abs(own["props"]["pspwght"], own["props"]["dweight"])
    own_an = max_abs(own["props"]["pspwght"], own["props"]["anweight"])
    sens = ref["sensitivity"]
    res["maxAbsAbweichungSensitivitaet"] = max(
        abs(sens["maxAbsUnweighted"] - own_unw), abs(sens["maxAbsDweight"] - own_dw)
    )
    diag = ref["anweightEquivalenceDiagnostic"]
    res["maxAbsAbweichungAnweightDiagnose"] = max(
        abs(diag["maxAbsDifference"] - own_an),
        abs(diag["ratioMin"] - an_ratio[0]),
        abs(diag["ratioMax"] - an_ratio[1]),
    )
    res["ratioScopeVeroeffentlicht"] = diag.get("ratioScope")
    res["unsicherheitNull"] = ref.get("uncertainty") is None
    res["_eigeneSensitivitaet"] = {"unweighted": own_unw, "dweight": own_dw, "anweight": own_an}
    return res


def cmp_group(own, pub_q):
    res = {
        "statusVeroeffentlicht": pub_q["status"],
        "statusBerechnet": own["status"],
    }
    ref = pub_q["reference"]
    published = pub_q["status"] == "reviewed_historical_reference"
    res["statusKonsistent"] = (
        (published and own["status"] == ST_PREPARED)
        or (not published and own["status"] == pub_q["status"])
    )
    if ref is None:
        res["referenzLeer"] = True
        return res
    codes_pub = [c["code"] for c in ref["categories"]]
    res["kategorienGleich"] = codes_pub == own["codes"]
    pub_props = [c["proportion"] for c in ref["categories"]]
    res["maxAbsAbweichungAnteil"] = max_abs(own["props"]["pspwght"], pub_props)
    res["nennerGleich"] = (
        ref["validCount"] == own["validCount"]
        and ref["totalCount"] == own["totalCount"]
        and ref["missingCount"] == own["missingCount"]
        and ref["notAskedCount"] == own["notAskedCount"]
    )
    res["unsicherheitNull"] = ref.get("uncertainty") is None
    res["_eigeneSensitivitaet"] = {
        "unweighted": max_abs(own["props"]["pspwght"], own["props"]["unweighted"]),
        "dweight": max_abs(own["props"]["pspwght"], own["props"]["dweight"]),
    }
    return res


def ergebnis(res):
    if not res["statusKonsistent"]:
        return "abweichung_status"
    if res.get("referenzLeer"):
        return "uebereinstimmung_status_zurueckgehalten"
    d = res["maxAbsAbweichungAnteil"]
    if (
        res["kategorienGleich"]
        and res["nennerGleich"]
        and res.get("missingGruendeGleich", True)
        and d is not None
        and d <= TOL
        and res.get("maxAbsAbweichungSensitivitaet", 0.0) <= TOL
        and res.get("maxAbsAbweichungAnweightDiagnose", 0.0) <= TOL
    ):
        return "uebereinstimmung_bis_auf_gleitkomma"
    return "abweichung_wert"


# ---------------------------------------------------------------- Design


def design_counts(rows, have):
    out = {"psuSpalte": "psu" in have, "stratumSpalte": "stratum" in have, "probSpalte": "prob" in have}
    if not (out["psuSpalte"] and out["stratumSpalte"]):
        return out
    blank_psu = sum(1 for r in rows if r["psu"] == "")
    blank_str = sum(1 for r in rows if r["stratum"] == "")
    strata = defaultdict(set)
    psu_strata = defaultdict(set)
    for r in rows:
        if r["psu"] == "" or r["stratum"] == "":
            continue
        strata[r["stratum"]].add(r["psu"])
        psu_strata[r["psu"]].add(r["stratum"])
    per = [len(v) for v in strata.values()]
    out.update(
        {
            "leerePsu": safe(blank_psu),
            "leereStratum": safe(blank_str),
            "anzahlStrata": len(strata),
            "anzahlPsu": len(psu_strata),
            "strataMitNurEinerPsu": sum(1 for v in per if v == 1),
            "psuInMehrerenStrata": sum(1 for v in psu_strata.values() if len(v) > 1),
            "psuJeStratumMin": min(per) if per else None,
            "psuJeStratumMedian": statistics.median(per) if per else None,
            "psuJeStratumMax": max(per) if per else None,
        }
    )
    if "prob" in have:
        bad_prob = sum(1 for r in rows if parse_weight(r["prob"]) is None)
        out["ungueltigeProb"] = safe(bad_prob)
    return out


# ---------------------------------------------------------------- Hauptlauf


def main() -> int:
    contract = json.loads(ANALYSIS_CONTRACT.read_text(encoding="utf-8"))
    gcontract = json.loads(GROUP_CONTRACT.read_text(encoding="utf-8"))
    catalogue_sha = sha256_file(CATALOGUE)
    contract_sha = sha256_file(ANALYSIS_CONTRACT)
    print("== Spezifikation")
    print("Katalog-SHA256 passt zum Analysevertrag:", catalogue_sha == contract["catalog"]["sha256"])
    print("Analysevertrag-SHA256 passt zum Gruppenvertrag:",
          contract_sha == gcontract["references"]["analysisContract"]["sha256"])
    print("Gruppenvertrag-SHA256:", sha256_file(GROUP_CONTRACT))
    pr = contract["publicationRules"]
    assert pr["minimumValidCount"] == MIN_VALID and pr["minimumPositiveCellCount"] == MIN_CELL
    assert pr["primaryWeight"] == "pspwght"

    gstudies = {s["studyId"]: s for s in gcontract["studies"]}
    out_marg = []
    out_group = []
    summary = Counter()
    gsummary = Counter()

    for study in contract["studies"]:
        sid = study["study_id"]
        ad = study["adapter"]
        meta = study["metadata"]
        path = ROOT / study["input"]["path"]
        print(f"\n== {sid}")
        size = path.stat().st_size
        digest = sha256_file(path)
        print("Datei:", study["input"]["path"])
        print("SHA256:", digest, "| passt zum Vertrag:", digest == study["input"]["sha256"])
        print("Bytes:", size, "| passt zum Vertrag:", size == study["input"]["bytes"])

        gs = gstudies.get(sid) if sid in GROUP_STUDIES else None
        wanted = ["name", "essround", "edition", "proddate", "idno", "cntry",
                  "pspwght", "dweight", "anweight", "pweight", "psu", "stratum", "prob"]
        wanted += [q["variable"] for q in ad["questions"]]
        if gs is not None:
            wanted += [gs["columns"]["vote"], gs["columns"]["party2"]]
        rows, diag, have = read_de(path, wanted)
        print("Lese-Diagnose:", json.dumps(diag, ensure_ascii=False))

        # Metadaten in den Daten selbst
        names = Counter(r.get("name", "") for r in rows)
        rounds = Counter(r["essround"] for r in rows)
        eds = Counter(r["edition"] for r in rows)
        prod = Counter(r.get("proddate", "") for r in rows)
        rok = all(round_ok(k, meta["expected_round"]) for k in rounds)
        eok = all(edition_ok(k, meta["expected_edition"]) for k in eds)
        print("name-Werte (DE):", sorted(names), "| essround-Werte:", sorted(rounds),
              "| edition-Werte:", sorted(eds), "| proddate-Werte:", sorted(prod))
        print("Runde passt:", rok, "| Edition passt:", eok,
              "| name passt zur Studien-ID:", set(names) == {sid})
        dup_ids = sum(1 for v in Counter(r["idno"] for r in rows).values() if v > 1)
        print("Doppelte idno innerhalb DE (Anzahl Werte):", safe(dup_ids))

        # Gewichte
        W = {}
        bad = {}
        for wcol in ("pspwght", "dweight", "anweight", "pweight"):
            vals = [parse_weight(r[wcol]) for r in rows]
            bad[wcol] = sum(1 for v in vals if v is None)
            W[wcol] = vals
        print("Ungültige Gewichte (nicht positiv/endlich):", {k: safe(v) for k, v in bad.items()})
        if any(bad[k] for k in ("pspwght", "dweight", "anweight")):
            raise SafeError(f"{sid}: ungültige Gewichte")
        all_de_weight = math.fsum(W["pspwght"])
        ratios = [a / p for a, p in zip(W["anweight"], W["pspwght"])]
        r0 = ratios[0]
        const = all(abs(x - r0) <= TOL or abs(x - r0) <= TOL * abs(r0) for x in ratios)
        rmin, rmax = min(ratios), max(ratios)
        pw = Counter(r["pweight"] for r in rows)
        print("Summe pspwght (DE):", repr(all_de_weight), "| Mittel pspwght:", all_de_weight / len(rows),
              "| Summe dweight:", math.fsum(W["dweight"]), "| Mittel dweight:", math.fsum(W["dweight"]) / len(rows))
        print("anweight/pspwght konstant (abs. oder rel. Toleranz 1e-12):", const,
              "| relative Spannweite:", (rmax - rmin) / rmin)
        if const:
            print("   Verhältnis (landesweite Konstante):", repr(r0),
                  "| pweight-Werte in DE:", len(pw),
                  "| Verhältnis/pweight:", r0 / W["pweight"][0] if len(pw) == 1 else None)
        # Ursache einer Nichtkonstanz: Rundung der gespeicherten Werte?
        # Nur Aggregate: Dezimalstellen und maximaler Rest gegen pspwght*pweight.
        def decimals(s):
            return len(s.split(".", 1)[1]) if "." in s else 0
        dec_a = Counter(decimals(r["anweight"]) for r in rows)
        dec_p = Counter(decimals(r["pspwght"]) for r in rows)
        if len(pw) == 1:
            pwv = W["pweight"][0]
            resid = max(abs(a - p * pwv) for a, p in zip(W["anweight"], W["pspwght"]))
            rel = max(abs(a / (p * pwv) - 1.0) for a, p in zip(W["anweight"], W["pspwght"]))
            half_ulp = 0.5 * 10 ** (-max(dec_a))
            print("   pweight in DE eindeutig: True | max |anweight - pspwght*pweight|:", f"{resid:.3e}",
                  "| halbe letzte Dezimalstelle von anweight:", f"{half_ulp:.1e}",
                  "| allein durch Dezimalrundung von anweight erklärbar:", resid <= half_ulp * (1 + 1e-9),
                  "| max rel. Abweichung:", f"{rel:.3e}",
                  "| <= 2^-23 (eine float32-Einheit):", rel <= 2.0 ** -23)
        else:
            print("   pweight in DE nicht eindeutig (Anzahl Werte):", len(pw))
        print("   Dezimalstellen anweight (min/max):", min(dec_a), max(dec_a),
              "| pspwght (min/max):", min(dec_p), max(dec_p))

        # Design (Aufgabe 4)
        print("Design:", json.dumps(design_counts(rows, have), ensure_ascii=False))

        # Einzelreferenzen
        pub = json.loads((REF_DIR / f"{sid}.json").read_text(encoding="utf-8"))
        pubq = {q["id"]: q for q in pub["questions"]}
        weights = {"pspwght": W["pspwght"], "dweight": W["dweight"], "anweight": W["anweight"]}
        print("Einzelfragen:")
        for q in ad["questions"]:
            qid = q["question_id"]
            own = tabulate(rows, q["variable"], q["categoryCodes"], q["missingCodes"],
                           set(q["structurallyNotAskedCodes"]), weights)
            res = cmp_marginal(own, pubq[qid], all_de_weight, (rmin, rmax))
            res["ergebnis"] = ergebnis(res)
            summary[res["ergebnis"]] += 1
            blank_n = next(m["count"] for m in own["missingReasons"] if m["reason"] == "export_blank_unclassified")
            line = (f"  {qid}: berechnet={own['status']} veröffentlicht={pubq[qid]['status']} "
                    f"-> {res['ergebnis']} | unbekannte Codes={safe(own['unknownCode'])} "
                    f"unbekannte Literale={safe(own['unknownLiteral'])} leere Exportzellen={safe(blank_n)} "
                    f"nichtGestellt={safe(own['notAskedCount'])}")
            if not res.get("referenzLeer"):
                line += (f" | maxAbsAnteil={res['maxAbsAbweichungAnteil']:.3e}"
                         f" Nenner gleich={res['nennerGleich']} Missing gleich={res['missingGruendeGleich']}"
                         f" Kategorien gleich={res['kategorienGleich']}"
                         f" Sens-Abw={res['maxAbsAbweichungSensitivitaet']:.3e}"
                         f" Anweight-Abw={res['maxAbsAbweichungAnweightDiagnose']:.3e}"
                         f" AllDE-Abw={res['absAbweichungAllDEWeight']:.3e}"
                         f" MissingW-Abw={res['maxAbsAbweichungMissingGewicht']:.3e}"
                         f" eigeneSens(unw/dw/an)={res['_eigeneSensitivitaet']['unweighted']:.4f}/"
                         f"{res['_eigeneSensitivitaet']['dweight']:.4f}/{res['_eigeneSensitivitaet']['anweight']:.2e}")
            else:
                # Nur grobe Ursache, keine Zahl.
                line += f" | Ursache Basisregel={own['reasonBase']} Zellregel={own['reasonCell']}"
            print(line)
            entry = {
                "frageId": qid,
                "statusBerechnet": own["status"],
                "statusVeroeffentlicht": pubq[qid]["status"],
                "statusKonsistent": res["statusKonsistent"],
                "maxAbsAbweichungAnteil": res.get("maxAbsAbweichungAnteil"),
                "maxAbsAbweichungSensitivitaet": res.get("maxAbsAbweichungSensitivitaet"),
                "maxAbsAbweichungAnweightDiagnose": res.get("maxAbsAbweichungAnweightDiagnose"),
                "nennerbasisGleich": res.get("nennerGleich"),
                "missingGruendeGleich": res.get("missingGruendeGleich"),
                "ergebnis": res["ergebnis"],
            }
            out_marg.append(entry)

        # Plausibilität der veröffentlichten Datei selbst (nur Aggregate)
        sum_dev = 0.0
        out_of_range = 0
        small_missing_entries = 0
        for q in pub["questions"]:
            ref = q["reference"]
            if ref is None:
                continue
            props = [c["proportion"] for c in ref["categories"]]
            sum_dev = max(sum_dev, abs(math.fsum(props) - 1.0))
            out_of_range += sum(1 for p in props if not (0.0 <= p <= 1.0))
            small_missing_entries += sum(1 for m in ref["missingReasons"] if 1 <= m["count"] < MIN_CELL)
        print("Veröffentlichte Einzeldatei: max |Summe Anteile - 1| =", f"{sum_dev:.3e}",
              "| Anteile außerhalb [0,1]:", out_of_range,
              "| Missing-Grund-Einträge mit 1-4 Fällen (samt Gewichtssumme veröffentlicht):", small_missing_entries)

        if gs is None:
            continue

        # Gruppen
        vcol, pcol = gs["columns"]["vote"], gs["columns"]["party2"]
        pvalid = list(gs["nationalParty2Field"]["validCodes"])
        vstate = Counter()
        pstate = Counter()
        eligible_idx = defaultdict(list)
        inconsistent = 0
        unknown_vp = 0
        routing_mismatch = 0
        p_miss = {m["code"] for m in gs["nationalParty2Field"]["sourceMissingCodes"]}
        p_na = {m["code"] for m in gs["nationalParty2Field"]["structurallyNotAskedCodes"]}
        v_miss = {m["code"] for m in gs["voteField"]["sourceMissingCodes"]}
        for i, r in enumerate(rows):
            vk, vc = classify(r[vcol])
            pk, pc = classify(r[pcol])
            if vk == "blank":
                vs = "technical_export_blank"
            elif vk == "literal":
                vs = "unknown"
            elif vc == "1":
                vs = "yes"
            elif vc == "2":
                vs = "no"
            elif vc == "3":
                vs = "not_eligible"
            elif vc in v_miss:
                vs = "source_missing"
            else:
                vs = "unknown"
            if pk == "blank":
                ps = "technical_export_blank"
            elif pk == "literal":
                ps = "unknown"
            elif pc in pvalid:
                ps = "valid"
            elif pc in p_na:
                ps = "structurally_not_asked"
            elif pc in p_miss:
                ps = "source_missing"
            else:
                ps = "unknown"
            vstate[vs] += 1
            pstate[ps] += 1
            if (ps == "structurally_not_asked") != (vs != "yes"):
                routing_mismatch += 1
            if vs == "unknown" or ps == "unknown":
                unknown_vp += 1
            if ps == "valid":
                if vs == "yes":
                    eligible_idx[pc].append(i)
                else:
                    inconsistent += 1
        # Keine Zustandsverteilungen und keine Gesamtzahl berechtigter Fälle
        # ausgeben: Aus Summen ließen sich sonst maskierte Kleinstwerte oder
        # Größen nicht veröffentlichter Gruppen per Differenz erschließen.
        print("Gruppenweg: inkonsistent (vote≠1, gültige Partei):", safe(inconsistent),
              "| unbekannte vote/party2-Codes:", safe(unknown_vp),
              "| Fälle, in denen party2='nicht gestellt' nicht genau vote≠1 entspricht:", safe(routing_mismatch))
        all_idx = [i for v in eligible_idx.values() for i in v]
        g_ratios = [ratios[i] for i in all_idx]
        if g_ratios:
            g0 = g_ratios[0]
            gconst = all(abs(x - g0) <= TOL or abs(x - g0) <= TOL * abs(g0) for x in g_ratios)
            print("  anweight/pspwght konstant über berechtigte Gruppenfälle:", gconst)

        gpub = json.loads((GROUP_REF_DIR / f"{sid}.json").read_text(encoding="utf-8"))
        gpub_by = {g["id"]: g for g in gpub["groups"]}
        contract_groups = [g["groupId"] for g in gs["groupsInDeclaredApiOrder"]]
        print("  Gruppenbestand gleich Vertrag:", contract_groups == [g["id"] for g in gpub["groups"]])
        g_sum_dev = 0.0
        g_small_missing = 0
        g_small_notasked = 0
        for g in gpub["groups"]:
            for q in g["questions"]:
                ref = q["reference"]
                if ref is None:
                    continue
                g_sum_dev = max(g_sum_dev, abs(math.fsum(c["proportion"] for c in ref["categories"]) - 1.0))
                g_small_missing += 1 if 1 <= ref["missingCount"] < MIN_CELL else 0
                g_small_notasked += 1 if 1 <= ref["notAskedCount"] < MIN_CELL else 0
        print("  Veröffentlichte Gruppendatei: max |Summe Anteile - 1| =", f"{g_sum_dev:.3e}",
              "| Paare mit missingCount 1-4:", g_small_missing,
              "| Paare mit notAskedCount 1-4:", g_small_notasked)
        for g in gs["groupsInDeclaredApiOrder"]:
            gid = g["groupId"]
            code = g["party2Code"]
            idx = eligible_idx.get(code, [])
            grows = [rows[i] for i in idx]
            gw = {k: [weights[k][i] for i in idx] for k in weights}
            gq_pub = {q["id"]: q for q in gpub_by[gid]["questions"]}
            for q in ad["questions"]:
                qid = q["question_id"]
                own = tabulate(grows, q["variable"], q["categoryCodes"], q["missingCodes"],
                               set(q["structurallyNotAskedCodes"]), gw)
                res = cmp_group(own, gq_pub[qid])
                res["ergebnis"] = ergebnis(res)
                gsummary[res["ergebnis"]] += 1
                if res.get("referenzLeer"):
                    gsummary["grund_basis" if own["reasonBase"] else ("grund_zelle" if own["reasonCell"] else "grund_keiner_exportentscheid")] += 1
                else:
                    gsummary["veroeffentlicht"] += 1
                    print(f"  {gid} x {qid}: {res['ergebnis']} maxAbsAnteil={res['maxAbsAbweichungAnteil']:.3e}"
                          f" Nenner gleich={res['nennerGleich']} Kategorien gleich={res['kategorienGleich']}"
                          f" eigeneSens(unw/dw)={res['_eigeneSensitivitaet']['unweighted']:.4f}/"
                          f"{res['_eigeneSensitivitaet']['dweight']:.4f}")
                if not res["statusKonsistent"]:
                    print(f"  STATUSABWEICHUNG {gid} x {qid}: berechnet={own['status']} veröffentlicht={gq_pub[qid]['status']}")
                out_group.append({
                    "frageId": qid,
                    "gruppenId": gid,
                    # Gruppenvertrag benennt den vorbereiteten Status eigens.
                    "statusBerechnet": ("prepared_pending_group_result_review"
                                        if own["status"] == ST_PREPARED else own["status"]),
                    "statusVeroeffentlicht": gq_pub[qid]["status"],
                    "statusKonsistent": res["statusKonsistent"],
                    "maxAbsAbweichungAnteil": res.get("maxAbsAbweichungAnteil"),
                    "nennerbasisGleich": res.get("nennerGleich"),
                    "ergebnis": res["ergebnis"],
                })

    print("\n== Zusammenfassung Einzelfragen:", dict(summary))
    print("== Zusammenfassung Frage-Gruppen-Paare:", dict(gsummary))
    doc = {
        "beschreibung": (
            "Unabhängige Kontrollrechnung V1 (Claude). Vergleich eigener Rechnung mit "
            "data/reference-v2 und data/reference-groups-v21. Enthält nur IDs, Status und "
            "maximale absolute Abweichungen; keine Anteile, keine Zählwerte, keine "
            "zurückgehaltenen Werte."
        ),
        "erzeugtUtc": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "toleranz": TOL,
        "einzelfragen": out_marg,
        "frageGruppenPaare": out_group,
        "jeFrageMaxAbweichungUeberVeroeffentlichteGruppen": {
            qid: max(e["maxAbsAbweichungAnteil"] for e in out_group
                     if e["frageId"] == qid and e["maxAbsAbweichungAnteil"] is not None)
            for qid in dict.fromkeys(e["frageId"] for e in out_group)
            if any(e["frageId"] == qid and e["maxAbsAbweichungAnteil"] is not None for e in out_group)
        },
    }
    OUT_JSON.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("geschrieben:", OUT_JSON.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SafeError as exc:
        print("ABBRUCH:", exc)
        sys.exit(2)
    except Exception as exc:  # keine Exception-Meldung ausgeben (könnte Zellinhalte enthalten)
        tb = traceback.extract_tb(exc.__traceback__)
        where = f"{tb[-1].name}:{tb[-1].lineno}" if tb else "?"
        print(f"ABBRUCH: {type(exc).__name__} in {where} (Meldung unterdrückt)")
        sys.exit(3)
