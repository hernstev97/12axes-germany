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


_SIG_LETTERS = re.compile(r"^\s*(\(\s*[A-Z]{1,3}\s*\)\s*)+$")


def mask_text(s: str) -> str:
    """Maskiert Zahlen in Textzellen, die Ergebnisse sein könnten.

    Signifikanzbuchstaben wie "(AD) (AF)" (Flash-Tabellen) sind Ergebnisse von
    Spaltenvergleichen und werden ebenfalls maskiert.
    """
    if _NUM_FULL.match(s) or _SIG_LETTERS.match(s):
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


def cmd_content(spec):
    """Inhaltsblatt: Blattkennung und englischer Fragetext (Zahlen maskiert)."""
    wb, name = open_workbook(spec)
    ws = wb[wb.sheetnames[0]]
    print(f"Datei: {name} | Blatt: {ws.title}")
    for n, row in enumerate(sheet_rows(ws), start=1):
        cells = [cell_text(v) for v in row]
        texts = [c for c in cells if c]
        if not texts:
            continue
        print(f"  r{n} | {cells[0]} | {texts[-1]}")


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


# ---------------------------------------------------------------------------
# S1-Formular: je Erhebung und je Frage ein Eintrag ohne Ergebniswerte
# ---------------------------------------------------------------------------

FILES = "outputs/claude/s1/files"

LIZENZ_COM_REUSE = (
    "COM_REUSE – „European Commission reuse notice“ (Beschluss 2011/833/EU), Lizenzfeld der Distribution "
    "auf data.europa.eu; Bedingungen nach Art. 6 Abs. 2: Quelle nennen, ursprüngliche Bedeutung nicht "
    "verzerren, Haftungsausschluss der Kommission"
)

GEWICHT_EB = (
    "Tabelle: „VOL A weighted“ bzw. „VOL C weighted“, ohne Namen der Gewichtungsvariable. Technische "
    "Spezifikation: „Weights are used to match the responding sample to the universe on gender by age, "
    "region and degree of urbanisation“; für EU-Werte zusätzliche Anpassung nach Anteil an der EU-Bevölkerung 15+. "
    "Wie die getrennt gezogenen Teilstichproben West (DEW) und Ost (DEE) für die Spalte DE zusammengeführt "
    "werden, nennen weder Tabelle noch Spezifikation."
)

SURVEYS = {
    "std105": {
        "erhebung": "Standard-Eurobarometer 105 (Frühjahr 2026)",
        "welle": "Eurobarometer 105.2 (data.europa.eu s3613_105_2_std105_eng, Distributionen vom 2026-05-08)",
        "A": ("std105_volume_A.xlsx", "Standard Eurobarometer 105 spring 2026_volume A.xlsx"),
        "C": ("std105_volumes_C_EU27.zip", "Standard Eurobarometer 105 spring 2026_volumes C_EU27.zip", "volume C_DE.xlsx"),
        "feldzeit": "12.03.2026–01.04.2026 (Technische Spezifikation TS2 im Bericht „Public opinion in the EU“, deliverableId 108404, PDF-S. 270; Volume C DE: „12/3 - 1/4/2026“)",
        "modus": "persönliches Interview (face-to-face, CAPI); Videointerviews (CAVI) laut TS3 nur in CY, DK, MT, FI, SE; Institut Mantle Germany (Verian); 1.515 Interviews in DE (TS2)",
        "gewicht": GEWICHT_EB,
        "ts": "Bericht STD105 „Public opinion in the EU“ (deliverableId 108404), PDF-S. 269–273",
        "fragebogen": None,
        "vc_vorhanden": True,
    },
    "std104": {
        "erhebung": "Standard-Eurobarometer 104 (Herbst 2025)",
        "welle": "Eurobarometer 104.1 (data.europa.eu s3378_104_1_std104_eng, Distributionen vom 2026-02-11)",
        "A": ("std104_volume_A.xlsx", "Standard Eurobarometer 104_Autumn 2025_volume A.xlsx"),
        "C": ("std104_volumes_C_AT-HR.zip", "Standard Eurobarometer 104_Autumn 2025_volumes C_AT-HR (1).zip", "Volume C_DE.xlsx"),
        "feldzeit": "09.10.2025–29.10.2025 (Technische Spezifikation im Bericht „First results“, deliverableId 101601, PDF-S. 61)",
        "modus": "persönliches Interview (face-to-face, CAPI); CAVI laut Spezifikation nur in CY, DK, MT, NL, FI, SE; Institut Mantle Germany (Verian); 1.516 Interviews in DE",
        "gewicht": GEWICHT_EB,
        "ts": "Bericht STD104 „First results“ (deliverableId 101601), PDF-S. 60–63; in den übrigen fünf geprüften STD104-Berichten keine Technische Spezifikation gefunden",
        "fragebogen": None,
        "vc_vorhanden": True,
    },
    "sp559": {
        "erhebung": "Spezial-Eurobarometer 559 „Investing in fairness“",
        "welle": "Eurobarometer 103.1 (data.europa.eu s3223_103_1_sp559_eng, Distributionen vom 2026-03-05)",
        "A": ("sp559_volume_A.xlsx", "Investing in fairness_SP559_volume_A.xlsx"),
        "C": ("sp559_volume_C.zip", "Investing in fairness_SP559_volume_C.zip", "SP559_volume_C_DE.xlsx"),
        "feldzeit": "10.01.2025–28.01.2025 (Technische Spezifikation TS2 im Bericht, deliverableId 98737, PDF-S. 104; dort im Format Monat-Tag-Jahr „01-10-2025 – 01-28-2025“)",
        "modus": "persönliches Interview (face-to-face, CAPI); CAVI laut TS3 nur in CZ, DK, MT, NL, FI, SE; Institut Mantle Germany (Verian); 1.504 Interviews in DE",
        "gewicht": GEWICHT_EB,
        "ts": "Bericht SP559 (deliverableId 98737), PDF-S. 103–107; englischer Fragebogen PDF-S. 108–118",
        "fragebogen": "englischer Fragebogen im Bericht (PDF-S. 108–118), Nummerierung Q1 ff. statt QB1 ff.; deutscher Fragebogen nicht geprüft",
        "vc_vorhanden": True,
    },
    "sp564": {
        "erhebung": "Spezial-Eurobarometer 564 „Attitudes towards EU enlargement“",
        "welle": "Eurobarometer 103.2 (data.europa.eu s3413_103_2_sp564_eng, Distributionen vom 2025-09-02)",
        "A": ("sp564_volume_A.xlsx", "Attitudes towards EU enlargement_SP564_volume_A.xlsx"),
        "C": ("sp564_volume_C.zip", "Attitudes towards EU enlargement_SP564_volume_C.zip", "vol_C_DE.xlsx"),
        "feldzeit": "19.02.2025–10.03.2025 (Technische Spezifikation TS3 im Bericht, deliverableId 100304, PDF-S. 89)",
        "modus": "persönliches Interview (face-to-face, CAPI); CAVI laut TS4 nur in DK, MT, NL, FI, SE; Institut Mantle Germany (Verian); 1.510 Interviews in DE",
        "gewicht": GEWICHT_EB,
        "ts": "Bericht SP564 (deliverableId 100304), PDF-S. 87–92; englischer Fragebogen PDF-S. 93–98",
        "fragebogen": "englischer Fragebogen im Bericht (PDF-S. 93–98): Q3 und Q5 „ASK ALL“, Codes 1–4 und 999, kein Verweigerungscode",
        "vc_vorhanden": True,
    },
    "sp565": {
        "erhebung": "Spezial-Eurobarometer 565 „Climate change“",
        "welle": "Eurobarometer 103.2 (data.europa.eu s3472_103_2_sp565_eng, Distributionen vom 2026-03-05)",
        "A": ("sp565_volume_A.xlsx", "Climate change_SP565_volume A.xlsx"),
        "C": ("sp565_volumes_C.zip", "Climate_Change_SP565_volume_C.zip", "SP565_volume_C_DE.xlsx"),
        "feldzeit": "19.02.2025–10.03.2025 (Technische Spezifikation TS2 im Bericht, deliverableId 98729, PDF-S. 96)",
        "modus": "persönliches Interview (face-to-face, CAPI); CAVI laut TS3 nur in DK, MT, NL, FI, SE; Institut Mantle Germany (Verian); 1.510 Interviews in DE",
        "gewicht": GEWICHT_EB,
        "ts": "Bericht SP565 (deliverableId 98729), PDF-S. 95–99; englischer Fragebogen PDF-S. 100–104",
        "fragebogen": "englischer Fragebogen im Bericht (PDF-S. 100–104): Q10 und Q11 mit Codes 1–4 bzw. 1–4 und 999, kein Verweigerungscode",
        "vc_vorhanden": True,
    },
    "sp572": {
        "erhebung": "Spezial-Eurobarometer 572 „The Digital Decade 2026“",
        "welle": "Eurobarometer 105.1 (data.europa.eu s3682_105_1_sp572_eng, Distributionen vom 2026-06-17)",
        "A": ("sp572_volume_A.xlsx", "Digital decade_SP572_volume_A.xlsx"),
        "C": ("sp572_volume_C.zip", "Digital decade_SP572_Volume_C.zip", "SP572_volume_C_DE.xlsx"),
        "feldzeit": "05.02.2026–24.02.2026 (Technische Spezifikation TS74 im Bericht, deliverableId 106581, PDF-S. 74)",
        "modus": "persönliches Interview (face-to-face, CAPI); CAVI laut TS75 nur in CY, DK, MT, NL, FI, SE; Institut Mantle Germany (Verian); 1.513 Interviews in DE",
        "gewicht": GEWICHT_EB,
        "ts": "Bericht SP572 (deliverableId 106581), PDF-S. 73–77; die Kopfzeilen dieser Seiten nennen irrtümlich „Special Eurobarometer 569“; englischer Fragebogen PDF-S. 78–81",
        "fragebogen": "englischer Fragebogen im Bericht (PDF-S. 78–81): Q5 und Q12 mit „Don't know“, kein Verweigerungscode",
        "vc_vorhanden": True,
    },
    "fl561": {
        "erhebung": "Flash-Eurobarometer 561 „Public opinion on urban challenges and investment in cities“",
        "welle": "Flash 561 (data.europa.eu s3368_fl561_eng, Distributionen vom 2025-06-18)",
        "A": ("fl561_volume_A.xlsx", "fl_561_volume_A.xlsx"),
        "C": None,
        "feldzeit": "26.03.2025–02.04.2025 (Technische Spezifikation im Bericht, deliverableId 98987, PDF-S. 83)",
        "modus": "online (CAWI) über Online-Access-Panels von Ipsos und Partnern, teils Anwerbung über soziale Netzwerke; Quoten nach Alter, Geschlecht und DEGURBA (keine Zufallsstichprobe); DE: 513 Interviews in Städten, 520 in Kleinstädten und Vororten, 401 in ländlichen Gebieten",
        "gewicht": "Tabelle: „VOLUME A (Weighted)“. Technische Notiz (Datenanhang S. 3): „Survey data are weighted to marginal age by gender distributions using rim weighting“; EU27 nach Bevölkerung 15+ je Land und DEGURBA. Wie die drei DEGURBA-Teilstichproben für die Spalte DE gewichtet werden, ist nicht ausdrücklich genannt.",
        "ts": "Bericht FL561 (deliverableId 98987), PDF-S. 83; Datenanhang (deliverableId 98958), PDF-S. 3",
        "fragebogen": None,
        "vc_vorhanden": False,
    },
}

# (Blatt, Trendkennung laut R6/R10, Zuordnung, Beleg)
R6 = "R6 Abschnitt 6 nennt dieselbe Fragenummer in derselben Welle (deutscher GESIS-Fragebogen {q})"
QUESTIONS = {
    "std105": (
        [(f"QB2_{i}", "SE037", "eindeutig", R6.format(q="ZA9144 S. 12, QB2")) for i in range(1, 13)]
        + [("QB6_2", "SE040 Item 2", "unklar", "R6 nennt die Fragenummer in 105.2 nicht; englischer Text gleicht STD104 QB4_2")]
        + [("QB12_2", "ST0939 Item 2", "eindeutig", R6.format(q="ZA9144 S. 17, QB12"))]
        + [(f"QD2_{i}", "ST0350", "unklar", "R6 nennt die Fragenummer in 105.2 nicht; englischer Text gleicht STD104 QD2") for i in range(1, 6)]
        + [(f"QD3_{i}", "ST0359", "unklar", "R6 nennt die Fragenummer in 105.2 nicht; englischer Itemtext gleicht STD104 QD3") for i in (3, 4, 5)]
        + [("QE1", "SE050", "unklar", "R6 belegt SE050 nur für 104.1 (QF1); englischer Text und Antwortvorgaben gleichen STD104 QF1")]
    ),
    "std104": (
        [(f"QB1_{i}", "SE037", "eindeutig", R6.format(q="ZA9130 S. 10, QB1")) for i in range(1, 12)]
        + [("QB2_5", "SE035 Item 5", "eindeutig", R6.format(q="ZA9130 S. 11, QB2"))]
        + [("QB4_2", "SE040 Item 2", "eindeutig", R6.format(q="ZA9130 S. 12, QB4"))]
        + [(f"QD2_{i}", "ST0350", "eindeutig", R6.format(q="ZA9130 S. 18, QD2")) for i in range(1, 6)]
        + [(f"QD3_{i}", "ST0359", "eindeutig", R6.format(q="ZA9130 S. 19, QD3")) for i in (3, 4, 5, 6, 7)]
        + [("QF1", "SE050", "eindeutig", R6.format(q="ZA9130 S. 23, QF1"))]
    ),
    "sp564": (
        [("QC3", "", "eindeutig", R6.format(q="ZA9127 S. 48, QC3"))]
        + [(f"QC5_{i}", "", "eindeutig", R6.format(q="ZA9127 S. 49, QC5")) for i in range(1, 11)]
    ),
    "sp565": [("QD10", "", "eindeutig", R6.format(q="ZA9127 S. 75, QD10")), ("QD11_2", "", "eindeutig", R6.format(q="ZA9127 S. 75, QD11 Item 2"))],
    "sp572": [("QB5_6", "", "eindeutig", R6.format(q="ZA9143 S. 18, QB5 Item 6")), ("QB12", "", "eindeutig", R6.format(q="ZA9143 S. 21, QB12"))],
    "sp559": "^QB\\d",
    "fl561": "^Q\\d",
}

_DK = re.compile(r"don.?t know|ne sait pas|\bDK\b", re.I)
_REF = re.compile(r"refus|verweiger", re.I)
_COMBINED = re.compile(r"^\s*total\s*['\"‘’“”]", re.I)
_DE_HEAD = {"DE"}
_DE_WE = {"DEW", "DEE", "D-W", "D-E", "DE-W", "DE-E"}


def sha256_file(path):
    import hashlib

    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_zip_member(zpath, member):
    import hashlib

    z = zipfile.ZipFile(zpath)
    names = [n for n in z.namelist() if n.endswith(member)]
    return names[0], hashlib.sha256(z.read(names[0])).hexdigest()


def is_frac_row(nums):
    return bool(nums) and all(0 <= v <= 1 for v in nums) and not all(float(v) == int(v) for v in nums)


def parse_sheet(ws):
    """Liest ein Volume-Blatt. Gibt nur Beschriftungen, Formate und erlaubte Basiswerte zurück."""
    cells = [list(r) for r in ws.iter_rows()]
    vals = [[c.value for c in r] for r in cells]
    # Kopfzeile: erste Zeile mit einer Zelle "DE" vor der ersten Zahlenzeile
    first_num = next((i for i, r in enumerate(vals) if any(is_number_value(v) for v in r)), len(vals))
    head_i, de_col, has_we = None, None, False
    for i in range(first_num):
        texts = [str(v).strip() if isinstance(v, str) else None for v in vals[i]]
        if "DE" in texts:
            head_i, de_col = i, texts.index("DE")
            has_we = any(t in _DE_WE for t in texts if t)
            break
    titles = []
    for r in vals[: head_i if head_i is not None else first_num]:
        t = [cell_text(v) for v in r if v is not None and str(v).strip()]
        if t:
            titles.append(t)
    base_desc = ""
    for t in titles:
        for x in t:
            if x.lower().startswith("base"):
                base_desc = x  # letzte (englische) Fassung gewinnt
    group_row = []
    if head_i is not None and head_i > 0:
        gr = [cell_text(v) for v in vals[head_i - 1] if isinstance(v, str) and v.strip()]
        if len(gr) >= 3:
            group_row = gr
    # Datenzeilen
    data = []
    last_num = max((i for i, r in enumerate(vals) if any(is_number_value(v) for v in r)), default=-1)
    for i in range((head_i or 0) + 1, last_num + 1):
        r = vals[i]
        nums = [v for v in r if is_number_value(v)]
        if not nums:
            continue
        li, lab = row_label(r)
        fmt = None
        if de_col is not None and de_col < len(cells[i]) and is_number_value(cells[i][de_col].value):
            fmt = cells[i][de_col].number_format
        data.append({"i": i, "label": lab, "frac": is_frac_row(nums), "nums": nums, "fmt": fmt,
                     "de": r[de_col] if de_col is not None and de_col < len(r) else None})
    foot = []
    for r in vals[last_num + 1 :]:
        t = [cell_text(v) for v in r if isinstance(v, str) and v.strip()]
        t = [x for x in t if x and not x.startswith("<<") and x != MASK]
        if t:
            foot.append(" | ".join(t))
    return {"titles": titles, "base_desc": base_desc, "de_col": de_col, "has_we": has_we,
            "group_row": group_row, "data": data, "foot": foot,
            "header": [cell_text(v) for v in vals[head_i]] if head_i is not None else []}


def classify_rows(p, flash=False):
    """Trennt Basiszeilen und Kategoriezeilen (nur Beschriftungen)."""
    w_base = u_base = None
    cats, combined = [], []
    rows = p["data"]
    rest = []
    pair_anomalies = 0
    for k, d in enumerate(rows):
        lab = (d["label"] or "").strip()
        low = lab.lower()
        if low in ("total",) and k == 0 and not d["frac"]:
            w_base = d["de"]
            continue
        if low in ("weighted base", "base: weighted total"):
            w_base = d["de"]
            continue
        if low in ("unweighted base", "base: total", "base: unweighted total"):
            u_base = d["de"]
            continue
        rest.append(d)
    if flash:
        labels = [d["label"].strip() for d in rest if d["label"] and d["label"].strip()]
        fmt_rows = [d for d in rest if not (d["label"] and d["label"].strip())]
    else:
        # Paare: französische Zeile (gewichtete Anzahl), englische Zeile (Anteil)
        labels, fmt_rows = [], []
        for j in range(0, len(rest) - 1, 2):
            fr, en = rest[j], rest[j + 1]
            labels.append(f"{cell_text(en['label'])} / {cell_text(fr['label'])}")
            fmt_rows.append(en)
            if fr["frac"] or not (en["frac"] or all(float(v) in (0.0, 1.0) for v in en["nums"])):
                pair_anomalies += 1
        if len(rest) % 2:
            labels.append("UNGERADE ZEILENZAHL – Paarung prüfen")
    for lab in labels:
        (combined if _COMBINED.match(lab) else cats).append(cell_text(lab))
    fmts = sorted({d["fmt"].replace("\\", "") for d in fmt_rows if d["fmt"]})
    fracs = [v for d in fmt_rows for v in d["nums"] if is_number_value(v) and 0 <= v <= 1]
    finer = any(abs(v * 100 - round(v * 100)) > 1e-9 for v in fracs)
    if pair_anomalies:
        cats.append(f"PAARUNG FR/EN AUFFÄLLIG ({pair_anomalies}x) – prüfen")
    return w_base, u_base, cats, combined, fmts, finer


def base_value(v, base_desc):
    if v is None:
        return "fehlt"
    d = base_desc.lower()
    if re.search(r"base:\s*(all respondents|all|ensemble)\s*$", d):
        return int(v) if float(v) == int(v) else round(float(v), 1)
    return "vorhanden, nicht ausgegeben (Filterbasis würde den Anteil der Filtergruppe offenlegen)"


_META = ("base", "vol ", "volume", "eurobarometer", "terrain", "home", "flash eurobarometer")


def question_text(p):
    """Fragetext aus den Titelzeilen: zwei Zellen = französisch | englisch, eine Zelle = englisch."""
    en, fr = [], []
    for row in p["titles"]:
        cand = [x for x in row if not x.lower().startswith(_META)
                and x != "Public opinion on urban challenges and investment in cities" and "Fieldwork" not in x]
        if len(cand) == 2:
            fr.append(cand[0])
            en.append(cand[1])
        elif len(cand) == 1:
            en.append(cand[0])
    return {"englisch": " ".join(en).strip(), "franzoesisch": " ".join(fr).strip() or None}


def build_entries():
    entries = []
    for key, cfg in SURVEYS.items():
        import openpyxl

        a_path = f"{FILES}/{cfg['A'][0]}"
        wb_a = openpyxl.load_workbook(a_path, read_only=True, data_only=True)
        sha_a = sha256_file(a_path)
        wb_c, sha_c, c_member, sha_cm = None, None, None, None
        if cfg["C"]:
            c_path = f"{FILES}/{cfg['C'][0]}"
            sha_c = sha256_file(c_path)
            c_member, sha_cm = sha256_zip_member(c_path, cfg["C"][2])
            wb_c, _ = open_workbook(f"{c_path}::{cfg['C'][2]}")
        qs = QUESTIONS[key]
        if isinstance(qs, str):
            rx = re.compile(qs)
            qs = [(n, "", "unklar", "keine Fragenummer in R6; deutscher Fragebogen nicht geprüft (GESIS-Sperre)")
                  for n in wb_a.sheetnames if rx.match(n)]
        flash = key.startswith("fl")
        for code, trend, zuord, beleg in qs:
            p = parse_sheet(wb_a[code])
            w_base, u_base, cats, combined, fmts, finer = classify_rows(p, flash=flash)
            vc_groups, vc_w = [], None
            if wb_c is not None and code in wb_c.sheetnames:
                pc = parse_sheet(wb_c[code])
                vc_groups = [g.split(" - ", 1)[1].strip() if " - " in g else g for g in pc["group_row"]]
                vc_groups = [("Germany (Gliederung nach Bundesländern, NUTS 1)" if g == "Germany" else g) for g in vc_groups]
                vc_w, _, _, _, _, _ = classify_rows(pc)
            dk = any(_DK.search(c) for c in cats)
            ref = any(_REF.search(c) for c in cats)
            de = p["de_col"] is not None
            base_all = bool(re.search(r"base:\s*(all respondents|all|ensemble)\s*$", p["base_desc"].lower()))
            offen = []
            if p["has_we"]:
                offen.append("Volume A enthält neben DE auch die Spalten DEW (West) und DEE (Ost).")
            offen.append(f"Zuordnung: {beleg}.")
            if not flash:
                offen.append("Ungewichtete Basis je Frage fehlt in Volume A und C. Bekannt ist nur die Interviewzahl für DE aus der Technischen Spezifikation; ob sie bei „Base: All respondents“ der ungewichteten Basis entspricht, steht in keiner Tabelle.")
            if not ref:
                offen.append("Keine Verweigerungszeile; ob der deutsche Fragebogen dafür einen Code vorsieht, ist ohne GESIS-Fragebogen nicht prüfbar" + (" (englischer Fragebogen im Bericht: kein Verweigerungscode)." if key in ("sp564", "sp565", "sp572") else "."))
            if vc_w is not None and w_base is not None and base_all and float(vc_w) != float(w_base):
                offen.append(f"Gewichtete Basis DE in Volume C ({int(vc_w)}) weicht von Volume A ab.")
            if not base_all:
                offen.append(f"Gefilterte Frage („{p['base_desc']}“): Basiswerte nicht ausgegeben.")
            if p["foot"]:
                offen.append("Fußnoten/Textzeilen unter der Tabelle: " + " ‖ ".join(p["foot"]))
            if flash:
                offen.append("Tabellenzellen enthalten Signifikanzbuchstaben aus paarweisen Ländervergleichen (Blatt „Note“); sie sind Ergebnisse und wurden maskiert.")
            rund = ("Anteile in ganzen Prozentpunkten gespeichert (Zahlenformat " + ", ".join(fmts) + ")") if fmts and not finer else (
                ("Anteile feiner als ganze Prozentpunkte gespeichert, Anzeigeformat " + ", ".join(fmts)) if fmts else "Format der Anteilszellen nicht bestimmbar")
            if not flash:
                rund += "; gewichtete Anzahlen ganzzahlig. Umgang mit fehlenden Werten in Tabelle und Spezifikation nicht beschrieben."
            else:
                rund = ("Anteile als ganze Zahlen mit Zahlenformat „0\\%“ (wörtliches Prozentzeichen) gespeichert, also auf ganze "
                        "Prozentpunkte gerundet; gewichtete Anzahlen ganzzahlig. Umgang mit fehlenden Werten nicht beschrieben.")
            filt = f"Tabelle: „{p['base_desc']}“" if p["base_desc"] else "Tabelle: keine Basisangabe"
            filt += "; kein Hinweis auf Split-Ballot in Tabelle oder Spezifikation"
            if cfg.get("fragebogen"):
                filt += "; " + cfg["fragebogen"]
            cond = {
                "1": "erfüllt" if de else "nicht erfüllt",
                "2": "erfüllt" if (dk and len(cats) >= 2) else "nicht erfüllt",
                "3": "erfüllt" if (w_base is not None and u_base is not None) else "nicht erfüllt",
                "4": "nicht erfüllt",
                "5": "erfüllt" if zuord == "eindeutig" else "ungeprüft",
                "6": "erfüllt",
                "7": "nicht erfüllt",
                "8": "erfüllt",
                "9": "erfüllt" if vc_groups else "nicht erfüllt",
            }
            datei = f"Volume A: {cfg['A'][1]}"
            if cfg["C"]:
                datei += f"; Volume C: {cfg['C'][1]} → {c_member.split('/')[-1]}"
            else:
                datei += "; Volume C für DE nicht veröffentlicht (nur fl_561_volume_C_BE.xlsx)"
            entries.append({
                "erhebung": cfg["erhebung"],
                "welle": cfg["welle"],
                "datei": datei,
                "sha256": {"volumeA": sha_a, **({"volumeC_zip": sha_c, "volumeC_DE": sha_cm} if cfg["C"] else {})},
                "lizenz": LIZENZ_COM_REUSE,
                "frageKennung": code + (f" ({trend})" if trend else ""),
                "frageTextInTabelle": question_text(p),
                "spalteDeutschlandGesamt": "ja" if de else "nein",
                "kategorienEinzeln": cats,
                "weissNichtGetrennt": "ja" if dk else "nein",
                "verweigertGetrennt": "ja" if ref else "nicht vorhanden",
                "zusammengefassteKategorien": combined,
                "basisUngewichtetDeutschland": base_value(u_base, p["base_desc"]),
                "basisGewichtetDeutschland": base_value(w_base, p["base_desc"]),
                "filterOderSplit": filt,
                "gewichtungDeutschland": cfg["gewicht"],
                "feldzeitDeutschland": cfg["feldzeit"],
                "modusDeutschland": cfg["modus"],
                "rundung": rund,
                "gliederungsmerkmaleVolumeC": vc_groups,
                "zuordnungZumFragebogen": zuord,
                "bedingungenR10Abschnitt5_3": cond,
                "offen": offen,
            })
    return entries


def cmd_s1(out_path=None):
    entries = build_entries()
    doc = {
        "auftrag": "reports/claude/auftraege/S1-strukturpruefung-eurobarometer.md",
        "erzeugtMit": "reports/claude/kontrollrechnung/s1_struktur.py s1",
        "hinweis": "Enthält keine Anteile, Mittelwerte oder Rangfolgen. Zahlen nur als gewichtete Basis für Deutschland bei Fragen an alle Befragten.",
        "eintraege": entries,
    }
    text = json.dumps(doc, ensure_ascii=False, indent=1)
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    # Kurzübersicht ohne Werte außer erlaubten Basen
    for e in entries:
        c = e["bedingungenR10Abschnitt5_3"]
        print(f"{e['erhebung'][:28]:28} {e['frageKennung']:22} DE={e['spalteDeutschlandGesamt']} DK={e['weissNichtGetrennt']} "
              f"kat={len(e['kategorienEinzeln'])} komb={len(e['zusammengefassteKategorien'])} uB={str(e['basisUngewichtetDeutschland'])[:12]} "
              f"wB={str(e['basisGewichtetDeutschland'])[:12]} VC={len(e['gliederungsmerkmaleVolumeC'])} "
              f"bed={''.join(v[0] for v in c.values())}")


def main(argv):
    if len(argv) >= 2 and argv[1] == "s1":
        cmd_s1(argv[2] if len(argv) > 2 else None)
        return 0
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd, spec = argv[1], argv[2]
    if cmd == "sheets":
        cmd_sheets(spec)
    elif cmd == "content":
        cmd_content(spec)
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
