#!/usr/bin/env python3
"""S1: ergebnisblinde Strukturprüfung veröffentlichter Eurobarometer-Tabellen.

Auftrag: reports/claude/auftraege/S1-strukturpruefung-eurobarometer.md

Das Skript gibt aus Volume-Dateien (xlsx, auch innerhalb von zip) nur Struktur aus:
Blattnamen, Tabellenköpfe, Spaltenköpfe, Zeilenbeschriftungen, Beschriftungen von
Basiszeilen und Fußnoten. Jeder Zellinhalt, der eine Zahl ist, wird durch "#"
ersetzt. Ausnahme: Zeilen, deren Beschriftung eine Basis oder Fallzahl bezeichnet
und deren Werte wie Fallzahlen aussehen (keine Bruchzahl zwischen 0 und 100).
Zahlen in Textzellen mit Prozentzeichen oder Vorzeichen werden ebenfalls maskiert.

Aufruf (isolierte Umgebung mit openpyxl):
  outputs/claude/venv-readstat/bin/python reports/claude/kontrollrechnung/s1_struktur.py <befehl> ...

Befehle:
  sheets  DATEI[::ZIPMITGLIED]                     Blattnamen und Größe
  dump    DATEI[::ZIPMITGLIED] BLATT [MAXZEILEN]   maskierte Zeilen eines Blatts
  inv     DATEI[::ZIPMITGLIED] [MUSTER]            Inventar je Blatt (Titel, Köpfe,
                                                   Zeilenbeschriftungen, Basiszeilen,
                                                   Fußnoten); MUSTER filtert Blätter
  json    DATEI[::ZIPMITGLIED] [MUSTER]            wie inv, als JSON
  pdfmeth PDF                                      nur Methodenseiten (Technische
                                                   Spezifikation) mit maskierten Prozentwerten

Das Skript schreibt nichts außer auf die Standardausgabe.
"""
from __future__ import annotations

import datetime as _dt
import io
import json
import re
import subprocess
import sys
import zipfile

MASK = "#"

_NUM_FULL = re.compile(r"^\s*[-+−]?\s*(\d[\d\s.,']*)?\d\s*%?\s*$|^\s*[-+−]?\s*[.,]\d+\s*%?\s*$")
_NUM_PCT = re.compile(r"[-+−]?\d+(?:[.,]\d+)?\s*%")
_NUM_SIGNED = re.compile(r"(?<![\w.])[+−]\d+(?:[.,]\d+)?(?![\w.])")
_NUM_DECIMAL = re.compile(r"(?<![\w.])\d+[.,]\d+(?![\w.])")

_BASE_EXCLUDE = re.compile(
    r"mean|average|moyenne|m[ée]diane?|median|index|indice|score|%|percent|pourcent|share|part\b|ratio|"
    r"total\s*['\"‘’“”]|difference|diff\.|change|[ée]volution|trend",
    re.I,
)
_BASE_INCLUDE = re.compile(
    r"\bbases?\b|\bbasis\b|\bunweighted\b|\bweighted\b|\bpond[ée]r|\bsample size\b|"
    r"\bnumber of (interviews|respondents|cases)\b|\bn\s*=|^\s*n\s*$|\bnombre d|\beffectifs?\b|\bfallzahl",
    re.I,
)


def is_number_value(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def mask_text(s: str) -> str:
    """Maskiert Zahlen in Textzellen, die Ergebnisse sein könnten."""
    if _NUM_FULL.match(s):
        return MASK
    s = _NUM_PCT.sub(MASK + "%", s)
    s = _NUM_SIGNED.sub(MASK, s)
    s = _NUM_DECIMAL.sub(MASK, s)
    return s


def cell_text(v) -> str:
    if v is None:
        return ""
    if isinstance(v, (_dt.datetime, _dt.date)):
        return v.isoformat()[:10]
    if is_number_value(v):
        return MASK
    return mask_text(str(v)).replace("\n", " ").strip()


def is_base_label(label: str) -> bool:
    if not label:
        return False
    if _BASE_EXCLUDE.search(label):
        return False
    return bool(_BASE_INCLUDE.search(label))


def base_values_plausible(values) -> bool:
    """Fallzahlen sind >= 1; Bruchzahlen bis 100 könnten Anteile sein."""
    nums = [v for v in values if is_number_value(v)]
    if not nums:
        return False
    for v in nums:
        if v < 1:
            return False
        if float(v) != int(v) and v <= 100:
            return False
    return True


def fmt_base(v) -> str:
    if is_number_value(v):
        if float(v) == int(v):
            return str(int(v))
        return f"{v:.1f}"
    return cell_text(v)


def open_workbook(spec: str):
    import openpyxl  # nur in der isolierten Umgebung

    if "::" in spec:
        zpath, member = spec.split("::", 1)
        z = zipfile.ZipFile(zpath)
        names = [n for n in z.namelist() if n.endswith(member) or member in n]
        if len(names) != 1:
            raise SystemExit(f"Zipmitglied nicht eindeutig: {member} -> {names}")
        data = z.read(names[0])
        return openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True), names[0]
    return openpyxl.load_workbook(spec, read_only=True, data_only=True), spec


def sheet_rows(ws):
    for r in ws.iter_rows(values_only=True):
        yield list(r)


def row_label(row) -> tuple[int, str]:
    """Erste nichtleere Textzelle (Index, Text) einer Zeile."""
    for i, v in enumerate(row):
        if isinstance(v, str) and v.strip():
            return i, v.strip()
    return -1, ""


def masked_row(row):
    label_idx, label = row_label(row)
    base = is_base_label(label) and base_values_plausible(row[label_idx + 1 :] if label_idx >= 0 else [])
    out = []
    for i, v in enumerate(row):
        if base and is_number_value(v):
            out.append(fmt_base(v))
        else:
            out.append(cell_text(v))
    return out, base, label


def cmd_sheets(spec):
    wb, name = open_workbook(spec)
    print(f"Datei: {name}")
    for ws in wb.worksheets:
        print(f"  {ws.title!r}  max_row={ws.max_row} max_col={ws.max_column}")


def cmd_dump(spec, sheet, maxrows=80):
    wb, name = open_workbook(spec)
    ws = wb[sheet]
    print(f"Datei: {name} | Blatt: {sheet}")
    for n, row in enumerate(sheet_rows(ws), start=1):
        if n > maxrows:
            print("  ...")
            break
        cells, base, _ = masked_row(row)
        while cells and cells[-1] == "":
            cells.pop()
        if not cells:
            continue
        tag = "BASIS " if base else ""
        print(f"  r{n} {tag}| " + " | ".join(cells))


def analyse_sheet(ws, de_codes=("DE",)):
    """Inventar eines Blatts. Gibt nur Beschriftungen und Basiswerte zurück."""
    rows = list(sheet_rows(ws))
    header_idx = None
    header = []
    # Kopfzeile: Zeile mit mindestens drei kurzen Textzellen und keiner Zahl, vor der ersten Zeile mit Zahlen
    first_num_row = None
    for i, row in enumerate(rows):
        if any(is_number_value(v) for v in row):
            first_num_row = i
            break
    if first_num_row is not None:
        for j in range(first_num_row - 1, -1, -1):
            texts = [v for v in rows[j] if isinstance(v, str) and v.strip()]
            if len(texts) >= 2:
                header_idx = j
                header = [cell_text(v) for v in rows[j]]
                break
    title_lines = []
    stop = header_idx if header_idx is not None else (first_num_row or len(rows))
    for row in rows[:stop]:
        t = [cell_text(v) for v in row if v is not None and str(v).strip()]
        if t:
            title_lines.append(" | ".join(t))
    data_rows = []
    footnotes = []
    last_num = max((i for i, r in enumerate(rows) if any(is_number_value(v) for v in r)), default=-1)
    for i, row in enumerate(rows[(header_idx + 1) if header_idx is not None else 0 :], start=(header_idx + 1) if header_idx is not None else 0):
        has_num = any(is_number_value(v) for v in row)
        li, label = row_label(row)
        if i > last_num:
            if label:
                footnotes.append(cell_text(label))
            continue
        if not label and not has_num:
            continue
        cells, base, _ = masked_row(row)
        entry = {"zeile": i + 1, "beschriftung": cell_text(label), "zahlenzellen": sum(1 for v in row if is_number_value(v))}
        if base:
            entry["basis"] = True
            entry["werte"] = {}
            for ci, v in enumerate(row):
                if is_number_value(v):
                    col = header[ci] if ci < len(header) and header[ci] else f"c{ci+1}"
                    entry["werte"][col] = fmt_base(v)
        elif is_base_label(label):
            entry["basis"] = "Beschriftung wie Basis, Werte nicht plausibel als Fallzahl; maskiert"
        data_rows.append(entry)
    return {
        "blatt": ws.title,
        "titel": title_lines,
        "kopfzeile": header,
        "zeilen": data_rows,
        "fussnoten": footnotes,
    }


def cmd_inv(spec, pattern=None, as_json=False):
    wb, name = open_workbook(spec)
    rx = re.compile(pattern, re.I) if pattern else None
    out = {"datei": name, "blaetter": []}
    for ws in wb.worksheets:
        if rx and not rx.search(ws.title):
            continue
        out["blaetter"].append(analyse_sheet(ws))
    if as_json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return
    print(f"Datei: {name}")
    for s in out["blaetter"]:
        print(f"== Blatt {s['blatt']!r}")
        for t in s["titel"]:
            print(f"   T: {t}")
        print(f"   K: {' | '.join(h for h in s['kopfzeile'])}")
        for z in s["zeilen"]:
            b = ""
            if z.get("basis") is True:
                b = "  BASIS " + json.dumps(z["werte"], ensure_ascii=False)
            elif z.get("basis"):
                b = "  (" + z["basis"] + ")"
            print(f"   r{z['zeile']}: {z['beschriftung']}  [{z['zahlenzellen']}x{MASK}]{b}")
        for f in s["fussnoten"]:
            print(f"   F: {f}")


_METH_START = re.compile(r"TECHNICAL SPECIFICATIONS|TECHNISCHE SPEZIFIKATION|SP[ÉE]CIFICATIONS TECHNIQUES|METHODOLOGY|METHODIK", re.I)


def cmd_pdfmeth(pdf):
    """Gibt nur Seiten mit Technischer Spezifikation aus, Prozentwerte maskiert."""
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", info)
    pages = int(m.group(1)) if m else 0
    hits = []
    for p in range(1, pages + 1):
        txt = subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), pdf, "-"], capture_output=True, text=True).stdout
        head = "\n".join(txt.splitlines()[:12])
        if _METH_START.search(head):
            hits.append((p, txt))
    print(f"PDF: {pdf} | Seiten: {pages} | Methodenseiten: {[p for p, _ in hits]}")
    for p, txt in hits:
        print(f"===== Seite {p}")
        for line in txt.splitlines():
            line = _NUM_PCT.sub(MASK + "%", line)
            line = _NUM_SIGNED.sub(MASK, line)
            if line.strip():
                print(line.rstrip())


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, spec = argv[1], argv[2]
    if cmd == "sheets":
        cmd_sheets(spec)
    elif cmd == "dump":
        cmd_dump(spec, argv[3], int(argv[4]) if len(argv) > 4 else 80)
    elif cmd == "inv":
        cmd_inv(spec, argv[3] if len(argv) > 3 else None)
    elif cmd == "json":
        cmd_inv(spec, argv[3] if len(argv) > 3 else None, as_json=True)
    elif cmd == "pdfmeth":
        cmd_pdfmeth(spec)
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
