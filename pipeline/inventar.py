#!/usr/bin/env python3
"""ESS11-DE documentation inventory. Never reads respondent data.

Run from the repository root: python3 pipeline/inventar.py build
Then: python3 pipeline/inventar.py check
Inputs are pinned public PDFs under outputs/loop/inventory/. Fetch downloads
only the named official documentation URLs. Source PDF files stay outside Git.

This is an author draft, not an independent item judgement or a model input.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / "outputs/loop/inventory"
CSV = ROOT / "data/inventar.entwurf.csv"
PROVENANCE = ROOT / "data/inventar.provenienz.json"
DOC_CITATION = "European Social Survey European Research Infrastructure (ESS ERIC) (2025). ESS round 11 - 2023. Social inequalities in health, Gender in contemporary Europe. Sikt - Norwegian Agency for Shared Services in Education and Research. https://doi.org/10.21338/ess11-2023. Deutsche Fragebogen-/Listenheftdokumentation und Codebook 4.1, Fundstellen je Zeile; CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/. Extraktion, Strukturierung und Entwurfsannotationen durch dieses Projekt; keine ESS-Billigung."
NS = {"x": "http://www.w3.org/1999/xhtml"}
SOURCES = {
    "ESS11-DE-QUESTIONNAIRE": {
        "file": "ESS11_questionnaires_DE.pdf",
        "url": "https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_questionnaires_DE.pdf",
        "sha256": "be6fbca3efbe18a062a6ae96d242a7f79e02b511bd5fcf03d448943bb3a5ae75",
        "pages": 100,
    },
    "ESS11-DE-SHOWCARDS": {
        "file": "ESS11_showcards_DE.pdf",
        "url": "https://stessrelpubprodwe.blob.core.windows.net/data/round11/fieldwork/germany/ESS11_showcards_DE.pdf",
        "sha256": "786d1a3df9d9a9002b83be15ae57462fd3e56042befd510278fcbac45af4b3ca",
        "pages": 100,
    },
    "ESS11-CODEBOOK": {
        "file": "ESS11_appendix_a7_e04_1.pdf",
        "url": "https://stessrelpubprodwe.blob.core.windows.net/data/round11/survey/ESS11_appendix_a7_e04_1.pdf",
        "sha256": "b41e285845f0df030c7a588a14643e2414ab2b588781fbd1c1fb2ac0daddbe35",
        "pages": 552,
        "edition": "4.1",
    },
}
QID = re.compile(r"~?([A-FHIJKR]\d+[a-zMW]?)[.]?$")
# These are words in filters, not question labels. All five were read in layout.
FILTER_REFERENCES = {(21, "C11"), (58, "F4"), (65, "F19"), (66, "F19"), (97, "K1")}
PORTRAIT_VARIABLES = [
    "ipcrtiva", "impricha", "ipeqopta", "ipshabta", "impsafea",
    "impdiffa", "ipfrulea", "ipudrsta", "ipmodsta", "ipgdtima",
    "impfreea", "iphlppla", "ipsucesa", "ipstrgva", "ipadvnta",
    "ipbhprpa", "iprspota", "iplylfra", "impenva", "imptrada", "impfuna",
]
# A location-only map would be wrong for these adaptations. Open mappings are
# intentionally kept open. The reported German schooling mapping is not guessed.
SPECIAL_LOCATIONS = {
    "B14a": ["prtvgde1"], "B14b": ["prtvgde2"],
    "B24": ["prtclgde"], "C12": ["rlgdnade"], "C14": ["rlgdeade"],
    "E8M": ["impbemw"], "E8W": ["impbemw"],
    "E9M": ["trmedmw"], "E9W": ["trmedmw"],
    "E10M": ["trwrkmw"], "E10W": ["trwrkmw"],
    "E11M": ["trplcmw"], "E11W": ["trplcmw"],
    **dict(zip([f"B{i}" for i in range(6, 13)], [[v] for v in ["trstprl", "trstlgl", "trstplc", "trstplt", "trstprt", "trstep", "trstun"]])),
    **dict(zip([f"B{i}" for i in range(33, 37)], [[v] for v in ["gincdif", "freehms", "hmsfmlsh", "hmsacld"]])),
    "B38": ["lrnobed"], "B39": ["loylead"],
    "D10a": ["alcbnge"], "D10b": ["alcbnge"],
    **dict(zip([f"D{i}" for i in range(20, 28)], [[v] for v in ["fltdpr", "flteeff", "slprl", "wrhpp", "fltlnl", "enjlf", "fltsd", "cldgng"]])),
    "F27": ["wkdcorga"], "F28": ["iorgact"],
    # testji9 has a conflicting C36 Location. Do not append it to C36 merely
    # because the published metadata repeats that Location.
    "C36": ["testjc36"],
    **dict(zip([f"B{i}" for i in range(15, 23)], [[v] for v in ["contplt", "donprty", "badge", "sgnptit", "pbldmna", "bctprd", "pstplonl", "volunfp"]])),
    "F33": ["isco08"], "F34": ["isco08"], "F34a": ["isco08"],
    "F47": ["isco08p"], "F48": ["isco08p"], "F49": ["isco08p"],
}
TABLE_COLUMNS = {
    **{f"B{i}": (65, 160, 0) for i in range(6, 13)},
    **{f"B{i}": (70, 335, 0) for i in range(15, 23)},
    **{f"B{i}": (70, 168, 0) for i in (33, 34, 35, 36, 38, 39)},
    **{f"D{i}": (70, 220, -13) for i in range(20, 28)},
    "F27": (55, 160, 0), "F28": (55, 160, 0),
}
FIELDS = [
    "inventar_id", "frage_id", "modul", "ess_variablen", "zuordnung_status",
    "zuordnung_beleg", "wortlaut_de", "wortlaut_status", "antwortkategorien_de",
    "kategorien_status", "missingcodes_fragebogen", "missingcodes_status",
    "filter_einleitung_de", "kontext_status", "liste", "listenheft_beleg",
    "pdf_seiten", "gedruckte_seiten", "quelle_id", "quelle_sha256",
    "wortlaut_fundstelle_json", "originalblock_de", "originalblock_sha256",
    "antwortgegenstand", "antworttyp", "eignungsstatus", "ausschlussgrund_entwurf",
    "polung", "offene_punkte", "lizenz", "attribution",
    "kategorien_beleg_json",
    "kontext_beleg_json",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def words_text(words: list[dict]) -> str:
    """Keep line breaks and visible hyphens. Only PDF geometry defines ordering."""
    lines: list[list[dict]] = []
    for word in sorted(words, key=lambda w: (w["y0"], w["x0"])):
        if not lines or abs(word["y0"] - lines[-1][0]["y0"]) > 2:
            lines.append([word])
        else:
            lines[-1].append(word)
    return "\n".join(" ".join(w["text"] for w in sorted(line, key=lambda w: w["x0"])) for line in lines)


def page_words(page: ET.Element) -> list[dict]:
    return [{"text": w.text or "", "x0": float(w.get("xMin")), "x1": float(w.get("xMax")),
             "y0": float(w.get("yMin")), "y1": float(w.get("yMax"))}
            for w in page.findall(".//x:word", NS)]


def crop(words: list[dict], x0: float, x1: float, y0: float, y1: float) -> list[dict]:
    return [w for w in words if x0 <= w["x0"] < x1 and y0 <= w["y0"] < y1]


def run_extract() -> tuple[list[ET.Element], list[str], list[str]]:
    for src in SOURCES.values():
        path = CACHE / src["file"]
        if not path.exists() or digest(path) != src["sha256"]:
            raise RuntimeError(f"Missing or changed pinned documentation: {path}")
    subprocess.run(["pdftotext", "-bbox-layout", str(CACHE / SOURCES["ESS11-DE-QUESTIONNAIRE"]["file"]), str(CACHE / "questionnaire.bbox.html")], check=True)
    for sid, stem in [("ESS11-CODEBOOK", "codebook"), ("ESS11-DE-SHOWCARDS", "showcards")]:
        subprocess.run(["pdftotext", "-layout", str(CACHE / SOURCES[sid]["file"]), str(CACHE / f"{stem}.layout.txt")], check=True)
    pages = ET.parse(CACHE / "questionnaire.bbox.html").findall(".//x:page", NS)
    if len(pages) != 100:
        raise RuntimeError("Questionnaire page count changed")
    return pages, (CACHE / "codebook.layout.txt").read_text().split("\f"), (CACHE / "showcards.layout.txt").read_text().split("\f")


def codebook_blocks(pages: list[str]) -> dict[str, list[dict]]:
    variables: dict[str, list[dict]] = collections.defaultdict(list)
    current = None
    for p, page in enumerate(pages, 1):
        for line in page.splitlines():
            m = re.match(r"^\s*([a-z][a-z0-9_]*) - (.+)$", line)
            if m:
                current = {"variable": m[1], "label": m[2], "pages": [p], "lines": []}
                variables[m[1]].append(current)
            if current:
                current["lines"].append(line)
                if p not in current["pages"]:
                    current["pages"].append(p)
    for blocks in variables.values():
        for block in blocks:
            block["text"] = "\n".join(block.pop("lines"))
            block["locations"] = re.findall(r"^\s*Location\s+(.+)", block["text"], re.M)
    return variables


def mapping(qid: str, variables: dict[str, list[dict]]) -> tuple[str, str, str, list[str]]:
    if qid in {"F15", "F44", "F52", "F55"}:
        return "OFFEN: generische und deutsche Bildungskodierung getrennt abzugleichen", "OFFEN_DE_BILDUNGSADAPTATION", "ESS11-CODEBOOK: Länderadaptation F15DE1/F15DE2, F44DE1/F44DE2, F52DE1/F52DE2, F55DE1/F55DE2; Originalfragebogen trennt Schul-/Ausbildungsabschluss", ["Keine Gleichsetzung des deutschen Originalitems mit harmonisierter Bildungsvariable"]
    if qid == "I9":
        return "OFFEN: testji9 als dokumentierter Kandidat", "OFFEN_WIDERSPRUCH_CODEBOOK", "ESS11-CODEBOOK testji9 nennt Location C36; deutscher Fragebogen I9, S.96", ["I9-Location im Codebook widerspricht Original; keine stille Korrektur"]
    if "." in qid and qid.startswith("H"):
        names = [PORTRAIT_VARIABLES[ord(qid[-1]) - ord("A")]]
        status = "ENTWURF_INHALTSABGLEICH_Ha-u"
    elif qid in SPECIAL_LOCATIONS:
        names = SPECIAL_LOCATIONS[qid]
        status = "ENTWURF_DE_ADAPTATION"
    else:
        names = [name for name, blocks in variables.items() if any(qid in b["locations"] for b in blocks)]
        status = "ENTWURF_LOCATION_ABGLEICH"
    names = list(dict.fromkeys(names))
    if not names:
        return "OFFEN", "OFFEN_KEINE_EINDEUTIGE_LOCATION", "", ["ESS-Variablenzuordnung nicht aus einer ähnlichen Nummer abgeleitet"]
    evidence = []
    for name in names:
        if name not in variables:
            raise RuntimeError(f"Declared metadata variable missing: {name}")
        block = variables[name][0]
        evidence.append({"quelle": "ESS11-CODEBOOK", "variable": name, "pdf_seiten": block["pages"],
                         "gedruckte_seiten": [p - 1 for p in block["pages"]], "locations": block["locations"], "label": block["label"]})
    notes = ["Codebook 4.1; kein Abgleich mit Antwortdatei 4.2, keine Datenkodierung als freigegeben"]
    if qid in {"B14a", "B14b", "B24"}:
        notes.append("Deutsche Interviewcodes und Nachkodierungen der Variablen nicht gleichgesetzt")
    if qid.startswith("H"):
        notes.append("Ha-u ist Sammel-Location; deutscher Portraitinhalt und englischer Variablentext abgeglichen; unabhängige Prüfung offen")
    return "|".join(names), status, json_text(evidence), notes


def judgement(qid: str) -> tuple[str, str, str]:
    """Draft scope notes only. No acceptance, polarity or score is generated."""
    if qid in {"B10", "B14a", "B14b", "B16", "B23", "B24", "B25"}:
        return "ENTWURF_AUSSCHLUSS_NACH_ISSUE", "Parteibezug im Wortlaut oder übernommenen Filter; Phase 1 schließt Parteibezug aus", "Parteibezogene Auskunft"
    if qid == "B29":
        return "ENTWURF_AUSSCHLUSS_NACH_ISSUE", "Bewertung der Leistungen der amtierenden Bundesregierung; Phase 1", "Regierungsbewertung"
    if qid == "B26":
        return "ENTWURF_PRUEFVARIABLE_AUSSEN", "Links-Rechts-Selbsteinstufung bleibt nach Phase 1 als Prüfvariable außerhalb der Modellitems", "Politische Selbsteinstufung"
    if qid in {"B13", "A1", "A2", "A3", *[f"B{i}" for i in range(15, 23)], "C2", "C4", "C16", "C17", "K4", "F58"} or qid in {f"D{i}" for i in range(2, 20)} or qid in {"D10a", "D10b"}:
        return "ENTWURF_AUSSCHLUSS_NACH_ISSUE", "Selbstbericht über eigenes Verhalten, keine Einstellung zu Streitfrage/Wert; Abgrenzung am Original erneut prüfen", "Eigenes Verhalten"
    if qid.startswith("J") or qid in {"C33", "D9", "H1", "H2"}:
        return "ENTWURF_KONTEXT_ODER_VERWALTUNG", "Interview-/Randomisierungs-/Einleitungseintrag, kein selbstständiges Einstellungsitem", "Interviewverwaltung/Einleitung"
    if qid in {f"D{i}" for i in range(20, 34)}:
        return "ENTWURF_AUSSERHALB_AUFNAHME", "Eigener Gesundheitszustand, Befinden oder persönliche Erfahrung; keine politische Streitfrage oder Wertorientierung im Wortlaut", "Persönlicher Zustand/Erfahrung"
    if qid.startswith("F") and qid not in {"F14a", "F27", "F28", "F42"}:
        return "ENTWURF_AUSSERHALB_AUFNAHME", "Soziodemografischer oder beruflicher Selbstbericht; keine politische/gesellschaftliche Streitfrage oder Wertorientierung im Wortlaut", "Soziodemografie/Beruf"
    if qid in {"C3", "C5", "C7", "C8", "C11", "C12", "C13", "C14", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29", "E1", "K1", "K2", "K3"}:
        return "ENTWURF_AUSSERHALB_AUFNAHME", "Persönliche Zugehörigkeit, Zustand oder Erfahrung; Aufnahme als Streitfrage/Wert aus Wortlaut nicht begründet", "Persönliche Zugehörigkeit/Zustand/Erfahrung"
    if qid.startswith("H"):
        return "ENTWURF_OFFEN", "", "Persönliche Wertorientierung als Portraitähnlichkeit"
    if qid in {"B2", "B4", "B31", "B32", "C30", *[f"C{i}" for i in range(34, 43)], *[f"I{i}" for i in range(1, 10)], "E12", "E13", "E14", "E23", "E24", "E25", "E26", "F14a", "F27", "F28"}:
        return "ENTWURF_OFFEN", "", "Wahrgenommener Zustand/Folge oder Wahrscheinlichkeit"
    if qid in {*[f"B{i}" for i in range(6, 13)]}:
        return "ENTWURF_OFFEN", "", "Institutionenvertrauen"
    if qid in {"B33", "B36", "B37", "B38", "B39", "B40", "B41", "B42", "E19", "E20", "E21", "E22", "E27", "E28"}:
        return "ENTWURF_OFFEN", "", "Gewünschte Maßnahme oder normative Aussage"
    if qid in {"B43", "B44", "B45", "E15", "E16", "E17", "E18", "B27", "B28", "B30", "F42"}:
        return "ENTWURF_OFFEN", "", "Bewertung eines Zustands/einer Folge"
    return "ENTWURF_OFFEN", "", "Anderer Typ: persönliche Haltung/Selbstwahrnehmung; Grenzfallprüfung offen"


def context_for(qid: str, p: int, words: list[dict], y: float) -> str:
    # Retain the page prefix even when it also contains earlier question material.
    # It is explicitly labelled context, never appended silently to the wording.
    prefix = words_text(crop(words, 0, 1000, 0, y))
    if qid.startswith("H"):
        return "FRAGEN WENN BEFRAGTER MÄNNLICH IST (WENN E1 = 1)" if qid.startswith("H1") else "FRAGEN WENN BEFRAGTE WEIBLICH IST (WENN E1 = 2)"
    return prefix


def shared_context(qid: str, pages: list[ET.Element]) -> tuple[str, list[dict]]:
    """Explicit inherited source passages; no questionnaire filter is invented."""
    regions = []
    if qid in {f"B{i}" for i in range(6, 13)}:
        regions = [(7, 50, 113)]
    elif qid in {f"B{i}" for i in range(15, 19)}:
        regions = [(9, 50, 125)]
    elif qid in {f"B{i}" for i in range(19, 23)}:
        regions = [(9, 379, 432)]
    elif qid in {f"B{i}" for i in range(33, 37)}:
        regions = [(13, 50, 78)]
    elif qid in {"B38", "B39"}:
        regions = [(14, 239, 268)]
    elif qid in {f"D{i}" for i in range(20, 28)}:
        regions = [(39, 537, 603)]
    elif qid in {"F27", "F28"}:
        regions = [(67, 50, 145)]
    elif qid in {"C31", "C32"}:
        regions = [(26, 358, 372)]
    elif qid in {f"C{i}" for i in range(34, 43)}:
        group_page = 27 if int(qid[1:]) <= 36 else 29 if int(qid[1:]) <= 39 else 30
        group_end = min(w["y0"] for w in page_words(pages[group_page - 1]) if w["text"] in {"C34", "C37", "C40"} and w["x0"] < 65)
        regions = [(26, 358, 372), (27, 50, 88), (group_page, 224 if group_page == 27 else 0, group_end)]
    elif re.fullmatch(r"I[1-9]", qid):
        start = 93 if int(qid[1:]) <= 3 else 94 if int(qid[1:]) <= 6 else 95
        first_id = "I1" if start == 93 else "I4" if start == 94 else "I7"
        end = min(w["y0"] for w in page_words(pages[start - 1]) if w["text"] == first_id and w["x0"] < 65)
        regions = [(start, 0, end)]
    if not regions:
        return "", []
    evidence = [{"quelle": "ESS11-DE-QUESTIONNAIRE", "pdf_seite": p, "x0": 0, "x1": 1000, "y0": low, "y1": high} for p, low, high in regions]
    return "\n[ORIGINALKONTEXT-FUNDSTELLE]\n".join(words_text(crop(page_words(pages[p - 1]), 0, 1000, low, high)) for p, low, high in regions), evidence


def primary_wording(page: ET.Element, label: dict, next_y: float, qid: str) -> tuple[str, list[dict], float, str]:
    words = page_words(page)
    if qid in {"F2", "F3", "F4"}:
        # Printed repeat-table headings are not respondent sentences. Keep their
        # caption as wording and the full household matrix in the answer block.
        first_line = crop(words, label["x1"] + 1, 250, label["y0"] - 0.1, label["y0"] + 12.5)
        text = words_text(first_line)
        if text in {"Geschlecht", "Geburtsjahr", "Beziehung"}:
            return text, [{"x0": label["x1"] + 1, "x1": 250, "y0": label["y0"] - 0.1, "y1": label["y0"] + 12.5}], label["y1"], "ENTWURF_TABELLENUEBERSCHRIFT"
    if qid in TABLE_COLUMNS:
        x0, x1, delta = TABLE_COLUMNS[qid]
        cellblocks = [block for block in page.findall(".//x:block", NS) if x0 <= float(block.get("xMin")) < x1 and float(block.get("xMax")) < x1 and float(block.get("yMin")) <= label["y0"] + 1 and float(block.get("yMax")) >= label["y0"]]
        stop = min(next_y + delta, max([float(b.get("yMax")) for b in cellblocks], default=next_y + delta) + 1)
        selected = crop(words, x0, x1, label["y0"] + delta, stop)
        return words_text(selected), [{"x0": x0, "x1": x1, "y0": label["y0"] + delta, "y1": stop}], max([w["y1"] for w in selected], default=label["y1"]), "ENTWURF_TABELLENZELLE"
    blocks = []
    for block in page.findall(".//x:block", NS):
        bw = page_words(block)
        selected = [w for w in bw if w["y0"] >= label["y0"] - 1 and w["y0"] < next_y and not (w["text"] == label["text"] and abs(w["y0"] - label["y0"]) < 1)]
        if selected:
            blocks.append((block, selected))
    first = [(b, ws) for b, ws in blocks if abs(min(w["y0"] for w in ws) - label["y0"]) < 3 and max(w["x1"] for w in ws) > label["x1"] + 35 and not all(re.fullmatch(r"\d+", w["text"]) for w in ws)]
    if not first:
        return "", [], label["y1"], "OFFEN_KEIN_SICHERER_TEXTBLOCK"
    first.sort(key=lambda b: min(w["x0"] for w in b[1]))
    selected = first[0][1]
    end_y = max(w["y1"] for w in selected)
    for block, ws in sorted(blocks, key=lambda b: float(b[0].get("yMin"))):
        if min(w["y0"] for w in ws) <= end_y:
            continue
        text = words_text(ws)
        xmin = min(w["x0"] for w in ws)
        body_xmin = min(w["x0"] for w in selected)
        if text.startswith("Was auf Liste") and qid in {"F15", "F44", "F52", "F55"}:
            selected.extend(ws)
            end_y = max(w["y1"] for w in ws)
            continue
        if min(w["y0"] for w in ws) - end_y > 28 or xmin > 125 or xmin < 60 or abs(xmin - body_xmin) > 5 or re.search(r"\b(?:AN ALLE|FRAGEN WENN|FRAGEN, WENN|WEITER MIT|ZEIT EINTRAGEN|BITTE ANZAHL|LISTE \d+ Ich lese)\b", text):
            break
        if "INTERVIEWER" in text:
            end_y = max(w["y1"] for w in ws)
            continue
        if any(re.fullmatch(r"\d+", w["text"]) for w in ws) and (re.search(r"\d+\s*$", text) or not (re.match(r"^(?:WEITER )?LISTE\s+\d", text, re.I) or "?" in text)):
            break
        selected.extend(ws)
        end_y = max(w["y1"] for w in ws)
    bounds = [{"x0": w["x0"], "x1": w["x1"], "y0": w["y0"], "y1": w["y1"], "text": w["text"]} for w in selected]
    return words_text(selected), bounds, end_y, "ENTWURF_TEXTBLOCK_AUTOMATISCH"


def table_answers(qid: str) -> tuple[str, str]:
    if re.fullmatch(r"B(?:[6-9]|1[012])", qid):
        return "00=Vertraue überhaupt nicht; 01; 02; 03; 04; 05; 06; 07; 08; 09; 10=Vertraue voll und ganz", "77=(Antwort verweigert); 88=(Weiß nicht)"
    if qid in {f"B{i}" for i in range(15, 23)}:
        return "1=Ja; 2=Nein", "7=(Antwort verweigert); 8=(Weiß nicht)"
    if qid in {f"B{i}" for i in [33, 34, 35, 36, 38, 39]}:
        return "1=Stimme stark zu; 2=Stimme zu; 3=Weder noch; 4=Lehne ab; 5=Lehne stark ab", "7=(Antwort verweigert); 8=(Weiß nicht)"
    if qid in {f"D{i}" for i in range(20, 28)}:
        return "1=Nie oder fast nie; 2=Manch mal; 3=Meistens; 4=Immer oder fast immer", "7=(Antwort verweigert); 8=(Weiß nicht)"
    if qid in {"F27", "F28"}:
        return "00=Kann/Konnte ich nicht beeinflussen; 01; 02; 03; 04; 05; 06; 07; 08; 09; 10=Kann/Konnte ich völlig eigenständig bestimmen", "77=(Antwort verweigert); 88=(Weiß nicht)"
    return "", ""


def documented_missing(answer_block: str, qid: str) -> tuple[str, str]:
    """Record visible questionnaire codes only, never infer ESS dataset missing."""
    compact = re.sub(r"\s+", " ", answer_block)
    numbers = set(re.findall(r"(?<!\w)\d+(?!\w)", answer_block))
    pairs = [("7" * n, "8" * n) for n in (6, 4, 3, 2, 1)]
    chosen = next(((r, d) for r, d in pairs if r in numbers and d in numbers), None)
    if qid == "C31":
        chosen = ("77", "88")  # original 88 printed over two source lines; visual check
    if not chosen:
        return "OFFEN: keine sicher zusammengehörigen Codepaare im Originalantwortblock", "OFFEN"
    entries = []
    if "Antwort" in compact and "verweigert)" in compact:
        entries.append(chosen[0] + "=(Antwort verweigert)")
    if "Weiß" in compact and "nicht)" in compact:
        entries.append(chosen[1] + "=(Weiß nicht)")
    if not entries:
        return "OFFEN: Labels nicht geschlossen extrahiert; Originalantwortblock prüfen", "OFFEN"
    return "; ".join(entries), "ENTWURF_ORIGINALBLOCK_CODEPAAR_ZUORDNUNG_NACHPRUEFEN"


def vertical_categories(words: list[dict], low: float, high: float) -> tuple[str, list[dict]]:
    """Extract a single vertical code column; preserve ambiguous layouts raw."""
    active = crop(words, 0, 1000, low, high)
    numbers = [w for w in active if w["x0"] > 180 and re.fullmatch(r"\d+", w["text"])]
    columns = collections.Counter(round(w["x0"] / 10) for w in numbers)
    if not columns or columns.most_common(1)[0][1] < 3:
        return "", []
    col = columns.most_common(1)[0][0] * 10
    codes = sorted([w for w in numbers if abs(w["x0"] - col) <= 8], key=lambda w: w["y0"])
    if any(abs(a["y0"] - b["y0"]) < 3 for a, b in zip(codes, codes[1:])):
        return "", []
    pairs, evidence = [], []
    for code in codes:
        # Repeated household matrices and horizontal scales are not coerced.
        if any(abs(other["y0"] - code["y0"]) < 2 and abs(other["x0"] - code["x0"]) > 10 for other in numbers):
            return "", []
        next_y = min([other["y0"] for other in codes if other["y0"] > code["y0"]], default=high)
        bottom = next_y - 1 if next_y != high else min(code["y0"] + 13, high)
        top = code["y0"] - 1
        label_words = crop(active, 0, code["x0"] - 1, top, bottom)
        # All missing captions and ordinary categories remain verbatim. A code
        # with no caption (interior scale point) is a valid documented blank.
        text = words_text(label_words)
        pairs.append({"code_fragebogen": code["text"], "label_original_de": text})
        evidence.append({"code": code, "label_tokens": label_words})
    return json_text(pairs), evidence


def make_rows(pages: list[ET.Element], variables: dict[str, list[dict]], cards: list[str]) -> tuple[list[dict], list[dict]]:
    labels = []
    for p, page in enumerate(pages, 1):
        for word in page_words(page):
            match = QID.fullmatch(word["text"])
            if match and word["x0"] < 65 and p >= 3:
                qid = match[1]
                if (p, qid) in FILTER_REFERENCES and not any(x["qid"] == qid and x["p"] == p for x in labels):
                    # K1 occurs twice on page 97: retain first, drop filter reference.
                    if qid != "K1":
                        continue
                if (p, qid) == (97, "K1") and any(x["qid"] == "K1" and x["p"] == 97 for x in labels):
                    continue
                labels.append({"qid": qid, "p": p, "word": word})
    labels.sort(key=lambda l: (l["p"], l["word"]["y0"]))
    rows = []
    seen = collections.Counter()
    for i, label in enumerate(labels):
        qid, p, word = label["qid"], label["p"], label["word"]
        nxt = labels[i + 1] if i + 1 < len(labels) else {"p": 101, "word": {"y0": 0}}
        next_y = nxt["word"]["y0"] if nxt["p"] == p else 800
        segment_pages = list(range(p, min(nxt["p"], 101))) if nxt["p"] != p else [p]
        source_segments = []
        for sp in segment_pages:
            ws = page_words(pages[sp - 1])
            low = word["y0"] if sp == p else 0
            source_segments.append(words_text(crop(ws, 0, 1000, low, 800)))
        if nxt["p"] > p and nxt["p"] <= 100 and nxt["word"]["y0"] > 70:
            sp = nxt["p"]
            source_segments.append(words_text(crop(page_words(pages[sp - 1]), 0, 1000, 0, nxt["word"]["y0"])))
            segment_pages.append(sp)
        original = "\n[SEITENWECHSEL]\n".join(source_segments)
        wording, bounds, body_end, wstatus = primary_wording(pages[p - 1], word, next_y, qid)
        answers, missing = table_answers(qid)
        if answers:
            cstatus = "ENTWURF_TABELLENKOPF_UND_ZEILE"
            mstatus = "ENTWURF_FRAGEBOGEN_CODES"
        else:
            answers = words_text(crop(page_words(pages[p - 1]), 0, 1000, body_end + 0.1, next_y))
            if len(segment_pages) > 1:
                answers += "\n" + "\n".join(source_segments[1:])
            cstatus = "OFFEN_ORIGINALANTWORTBLOCK_NOCH_NICHT_ZELLENWEISE"
            missing, mstatus = documented_missing(answers, qid)
            parsed, category_tokens = vertical_categories(page_words(pages[p - 1]), body_end + 0.1, next_y)
            if parsed:
                answers = parsed
                cstatus = "ENTWURF_VERTIKALE_CODES_LABELZEILEN_NACHPRUEFEN"
        names, mapstatus, mapevidence, notes = mapping(qid, variables)
        status, reason, kind = judgement(qid)
        seen[qid] += 1
        rid = qid if seen[qid] == 1 else f"{qid}@{p}.{seen[qid]}"
        inherited_lists = {**{f"B{i}": "9" for i in range(6, 13)}, **{f"B{i}": "13" for i in range(33, 37)}, "B38": "15", "B39": "15", **{f"D{i}": "45" for i in range(20, 28)}, "F27": "75", "F28": "75"}
        lists = sorted(set(re.findall(r"(?:LISTE|Liste)\s+(\d+[a-z]?)", wording) + ([inherited_lists[qid]] if qid in inherited_lists else [])))
        card_evidence = []
        for number in lists:
            found = [cp for cp, text in enumerate(cards, 1) if re.search(rf"\bLISTE\s+{re.escape(number)}\b(?!\d)", text, re.I)]
            card_evidence.append({"liste": number, "quelle": "ESS11-DE-SHOWCARDS", "pdf_seiten": found, "status": "ENTWURF_NUMMERNABGLEICH_KARTENINHALT_OFFEN"})
        notes.extend(["Keine getrennte Codex-/Claude-Itemerstbewertung; keine Polung", "Wortlaut behält sichtbare Trennstriche, Schreibweisen und Zeilenumbrüche des PDFs"])
        if not answers.strip():
            notes.append("Antwortfeld ohne rekonstruierte Kategorien; am Original prüfen")
        if qid == "C31":
            notes.append("Weiß-nicht-Code 88 ist im PDF räumlich als 8/8 aufgeteilt; visuell geprüft, nicht als Antwortkategorie 8 behandelt")
        rows.append(dict(zip(FIELDS, [rid, qid, qid[0], names, mapstatus, mapevidence, wording, wstatus, answers, cstatus, missing, mstatus,
            context_for(qid, p, page_words(pages[p - 1]), word["y0"]), "OFFEN_SEITENKONTEXT_VOLLSTAENDIG_GEROUTETER_FILTERABGLEICH_AUSSTEHEND", "|".join(lists), json_text(card_evidence),
            "|".join(map(str, segment_pages)), "|".join(map(str, segment_pages)), "ESS11-DE-QUESTIONNAIRE", SOURCES["ESS11-DE-QUESTIONNAIRE"]["sha256"],
            json_text({"pdf_seite": p, "regions_or_tokens": bounds}), original, hashlib.sha256(original.encode()).hexdigest(),
            wording.replace("\n", " "), kind, status, reason, "OFFEN_NICHT_BESTIMMT", " | ".join(notes), "CC BY-SA 4.0", DOC_CITATION])))
        rows[-1]["kategorien_beleg_json"] = json_text({"quelle": "ESS11-DE-QUESTIONNAIRE", "kopf_pdf_seite": 39 if qid in {f"D{i}" for i in range(23, 28)} else p, "codes_pdf_seite": p, "status": cstatus, "vertical_code_label_tokens": category_tokens if cstatus.startswith("ENTWURF_VERTIKALE") else []})
        contextual, context_evidence = shared_context(qid, pages)
        if contextual:
            rows[-1]["filter_einleitung_de"] = contextual
            rows[-1]["kontext_status"] = "ENTWURF_UEBERNOMMENER_ORIGINALKONTEXT_ROUTING_NACHPRUEFEN"
        rows[-1]["kontext_beleg_json"] = json_text(context_evidence if context_evidence else [{"quelle": "ESS11-DE-QUESTIONNAIRE", "pdf_seite": p, "x0": 0, "x1": 1000, "y0": 0, "y1": word["y0"], "status": "raw page prefix; inherited routing remains open"}])
    # Every portrait is a separate response object, with both German variants.
    for p in range(85, 93):
        parent = "H1" if p <= 88 else "H2"
        ws = page_words(pages[p - 1])
        letters = sorted([w for w in ws if re.fullmatch(r"[A-U]", w["text"]) and w["x0"] < 45], key=lambda w: w["y0"])
        for i, letter in enumerate(letters):
            qid = f"{parent}.{letter['text']}"
            y1 = letters[i + 1]["y0"] if i + 1 < len(letters) else 800
            textwords = crop(ws, 50, 145, letter["y0"] - 1, y1 - 1)
            wording = words_text(textwords)
            names, mapstatus, evidence, notes = mapping(qid, variables)
            intro = next(r for r in rows if r["frage_id"] == parent)
            row = {k: "" for k in FIELDS}
            row.update({"inventar_id": qid, "frage_id": qid, "modul": "H", "ess_variablen": names, "zuordnung_status": mapstatus,
                "zuordnung_beleg": evidence, "wortlaut_de": wording, "wortlaut_status": "ENTWURF_TABELLENZELLE",
                "antwortkategorien_de": "1=Ist mir sehr ähnlich; 2=Ist mir ähnlich; 3=Ist mir etwas ähnlich; 4=Ist mir nur ein kleines bisschen ähnlich; 5=Ist mir nicht ähnlich; 6=Ist mir überhaupt nicht ähnlich",
                "kategorien_status": "ENTWURF_TABELLENKOPF_UND_ZEILE", "missingcodes_fragebogen": "77=(Antwort verweigert); 88=(Weiß nicht)", "missingcodes_status": "ENTWURF_FRAGEBOGEN_CODES",
                "filter_einleitung_de": intro["filter_einleitung_de"] + "\n" + intro["wortlaut_de"] + ("\nINTERVIEWER: BITTE VORLESEN" if parent == "H2" else ""), "kontext_status": "ENTWURF_ORIGINALFILTER_UND_H_EINLEITUNG", "liste": "89", "listenheft_beleg": intro["listenheft_beleg"],
                "pdf_seiten": str(p), "gedruckte_seiten": str(p), "quelle_id": "ESS11-DE-QUESTIONNAIRE", "quelle_sha256": SOURCES["ESS11-DE-QUESTIONNAIRE"]["sha256"],
                "wortlaut_fundstelle_json": json_text({"pdf_seite": p, "regions_or_tokens": [{"x0": 50, "x1": 145, "y0": letter["y0"] - 1, "y1": y1 - 1}]}),
                "originalblock_de": wording, "originalblock_sha256": hashlib.sha256(wording.encode()).hexdigest(), "antwortgegenstand": wording.replace("\n", " "),
                "antworttyp": "Persönliche Wertorientierung als Portraitähnlichkeit", "eignungsstatus": "ENTWURF_OFFEN", "polung": "OFFEN_NICHT_BESTIMMT", "offene_punkte": " | ".join(notes), "lizenz": intro["lizenz"], "attribution": intro["attribution"]})
            row["kategorien_beleg_json"] = json_text({"quelle": "ESS11-DE-QUESTIONNAIRE", "kopf_pdf_seite": 85 if parent == "H1" else 89, "codes_pdf_seite": p, "status": row["kategorien_status"]})
            row["kontext_beleg_json"] = json_text({"quelle": "ESS11-DE-QUESTIONNAIRE", "pdf_seite": 85 if parent == "H1" else 89, "frage": parent, "status": "original gender filter and introduction including READ OUT; independent source check pending"})
            rows.append(row)
    rows.sort(key=lambda r: (int(r["pdf_seiten"].split("|")[0]), r["frage_id"][0], float(json.loads(r["wortlaut_fundstelle_json"])["regions_or_tokens"][0].get("y0", 0)) if json.loads(r["wortlaut_fundstelle_json"])["regions_or_tokens"] else 0))
    return rows, [{"frage_id": l["qid"], "pdf_seite": l["p"], "y": l["word"]["y0"]} for l in labels]


def validate(rows: list[dict], pages: list[ET.Element]) -> dict:
    errors, pending = [], []
    for row in rows:
        if row["polung"] != "OFFEN_NICHT_BESTIMMT" or not row["eignungsstatus"].startswith("ENTWURF"):
            errors.append(f"Unexpected final decision: {row['inventar_id']}")
        if not row["wortlaut_de"]:
            pending.append({"id": row["inventar_id"], "reason": "Wortlauttextblock offen"})
            continue
        loc = json.loads(row["wortlaut_fundstelle_json"])
        page = pages[loc["pdf_seite"] - 1]
        words = page_words(page)
        regions = loc["regions_or_tokens"]
        if regions and "text" in regions[0]:
            selected = regions
            # Check every token and its coordinates against the pinned PDF.
            tokens = {(w["text"], w["x0"], w["y0"]) for w in words}
            if any((w["text"], w["x0"], w["y0"]) not in tokens for w in selected):
                errors.append(f"Token not found in pinned PDF: {row['inventar_id']}")
        else:
            selected = []
            for region in regions:
                selected.extend(crop(words, region["x0"], region["x1"], region["y0"], region["y1"]))
        if words_text(selected) != row["wortlaut_de"]:
            errors.append(f"Exact extraction mismatch: {row['inventar_id']}")
        if row["kategorien_status"] == "ENTWURF_TABELLENKOPF_UND_ZEILE":
            category_evidence = json.loads(row["kategorien_beleg_json"])
            caption_words = page_words(pages[category_evidence["kopf_pdf_seite"] - 1])
            source_tokens = set(re.findall(r"[\w/]+", " ".join(w["text"] for w in caption_words + words)))
            for entry in row["antwortkategorien_de"].split("; "):
                for token in re.findall(r"[\w/]+", entry):
                    if token not in source_tokens:
                        errors.append(f"Caption/code token absent on source page: {row['inventar_id']} {token}")
        elif row["kategorien_status"].startswith("ENTWURF_VERTIKALE"):
            evidence = json.loads(row["kategorien_beleg_json"])["vertical_code_label_tokens"]
            source_token_set = {(w["text"], w["x0"], w["y0"]) for w in words}
            pairs = []
            for cell in evidence:
                for token in [cell["code"], *cell["label_tokens"]]:
                    if (token["text"], token["x0"], token["y0"]) not in source_token_set:
                        errors.append(f"Category token absent in pinned PDF: {row['inventar_id']}")
                pairs.append({"code_fragebogen": cell["code"]["text"], "label_original_de": words_text(cell["label_tokens"])})
            if json_text(pairs) != row["antwortkategorien_de"]:
                errors.append(f"Category extraction mismatch: {row['inventar_id']}")
        if row["kontext_status"].startswith("ENTWURF_UEBERNOMMENER"):
            context_evidence = json.loads(row["kontext_beleg_json"])
            passages = [words_text(crop(page_words(pages[r["pdf_seite"] - 1]), r["x0"], r["x1"], r["y0"], r["y1"])) for r in context_evidence]
            if "\n[ORIGINALKONTEXT-FUNDSTELLE]\n".join(passages) != row["filter_einleitung_de"]:
                errors.append(f"Inherited original context mismatch: {row['inventar_id']}")
        if row["kategorien_status"].startswith("OFFEN") or row["kontext_status"].startswith("OFFEN") or row["zuordnung_status"].startswith("OFFEN"):
            pending.append({"id": row["inventar_id"], "reason": " | ".join([row["kategorien_status"], row["kontext_status"], row["zuordnung_status"]])})
    expected_h = {f"H{sex}.{chr(letter)}" for sex in (1, 2) for letter in range(ord("A"), ord("U") + 1)}
    actual_h = {r["frage_id"] for r in rows if r["frage_id"].startswith(("H1.", "H2."))}
    if expected_h != actual_h:
        errors.append(f"Portrait coverage mismatch {sorted(expected_h ^ actual_h)}")
    by_id = {r["inventar_id"]: r for r in rows}
    source_assertions = {
        "B18": ("beteiligt?", "weiterhin"),
        "B14a": ("Erststimme gegeben?", None),
        "C43": ("stimmen?", "(Würde nicht wählen)"),
        "E9M": ("ein Mann sind?", None),
        "E9W": ("eine Frau sind?", None),
        "E20": ("um ihr Kind zu betreuen?", None),
        "F15": ("höchster allgemeinbildender Schulabschluss?", None),
        "F44": ("Ehemanns/Ehefrau/Partners/Partnerin?", None),
        "F52": ("allgemeinbildende Schulabschluss Ihres Vaters?", None),
        "F55": ("allgemeinbildende Schulabschluss Ihrer Mutter?", None),
    }
    for rid, (present, absent) in source_assertions.items():
        wording = re.sub(r"\s+", " ", by_id[rid]["wortlaut_de"])
        if present not in wording or (absent and absent in wording):
            errors.append(f"Read-source regression assertion failed: {rid}")
    if dict(collections.Counter(r["modul"] for r in rows)) != {"A": 6, "B": 46, "C": 43, "D": 34, "E": 32, "F": 69, "H": 44, "I": 9, "K": 4, "J": 9}:
        errors.append("Pinned German form module counts changed")
    return {"status": "BESTANDEN" if not errors else "NICHT_BESTANDEN", "scope": "Pinned source hashes, exact emitted wording tokens/regions, row identity and 42 German portraits; not semantic or category/filter completeness", "rows": len(rows), "errors": errors, "pending_rows": pending, "final_item_decisions": 0}


def build() -> None:
    pages, codepages, cards = run_extract()
    variables = codebook_blocks(codepages)
    rows, labels = make_rows(pages, variables, cards)
    validation = validate(rows, pages)
    CSV.parent.mkdir(exist_ok=True)
    with CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    provenance = {
        "artifact": "ESS11 Germany original questionnaire inventory, AUTHOR DRAFT",
        "status": "ENTWURF_TEILWEISE_STRUKTURIERT_KEINE_PHASE1_ABNAHME",
        "createdOn": "2026-10-03", "round": 11, "questionnaireYear": 2023,
        "targetDataCandidateEdition": "4.2; no response file read", "metadataEdition": "Codebook 4.1",
        "sources": SOURCES,
        "license": {"documentation": "CC BY-SA 4.0", "url": "https://creativecommons.org/licenses/by-sa/4.0/", "evidence": "ESS disclaimer Conditions of use, https://www.europeansocialsurvey.org/contact/disclaimer", "liveEvidenceFile": "outputs/loop/inventory/ess-disclaimer.html", "liveEvidenceSha256": digest(CACHE / "ess-disclaimer.html") if (CACHE / "ess-disclaimer.html").exists() else None, "attribution": DOC_CITATION, "changes": "PDF text extraction, inventory structure and author draft annotations; no rewritten question, no ESS endorsement", "publicationGate": "Specific inventory reuse subject to repository review; this author records the public documentation licence, not legal approval"},
        "build": {"command": "python3 pipeline/inventar.py build", "verify": "python3 pipeline/inventar.py check", "python": sys.version, "poppler": subprocess.run(["pdftotext", "-v"], capture_output=True, text=True).stderr.strip(), "builderSha256": digest(Path(__file__)), "csvSha256": digest(CSV), "normalization": "Geometry orders words into source lines. Line breaks, displayed hyphens, spelling and punctuation retained. Table response captions serialized; no polarity or item rewriting."},
        "accessBoundary": {"rawDataRead": False, "respondentRows": False, "portalAnalysis": False, "partyDistributions": False, "reviewerRole": False, "otherModelFamily": False},
        "coverage": {"labelOccurrences": len(labels), "rows": len(rows), "uniqueQuestionLabels": len({l["frage_id"] for l in labels}), "portraits": 42, "moduleCounts": dict(collections.Counter(r["modul"] for r in rows)), "categoryStatusCounts": dict(collections.Counter(r["kategorien_status"] for r in rows)), "missingStatusCounts": dict(collections.Counter(r["missingcodes_status"] for r in rows)), "capturedLabels": labels, "filteredReferences": sorted([list(x) for x in FILTER_REFERENCES]), "originalQuestionnairePages": 100, "claimsFullStructuredInventory": False, "pendingByCriterion": {key: [r["inventar_id"] for r in rows if r[key].startswith("OFFEN")] for key in ["zuordnung_status", "kategorien_status", "missingcodes_status", "kontext_status"]}, "routingAndIndependentSemanticReview": "not complete; no first ratings or polarity, every row remains a draft"},
        "checks": validation,
        "open": ["Category cells and missing-code transfer to ESS data remain partly unparsed", "Filtered routing and inherited shared introductions need complete row-by-row review", "German-specific schooling, household repeat tables and open codebook mappings need official adaptation reconciliation", "I9 source Location disagreement, codebook edition 4.1 versus candidate data edition 4.2", "No C44 German item and no numbered R item found in German PDF despite overview; numbering gaps not invented", "No independent item judgements, Claude first ratings, polarity or research phase acceptance"],
        "authorToolModel": {"runtimeReportedFamily": "GPT-6.1-Sol as documented by coordinator", "internalRevision": "not exposed", "tools": ["exec_command", "Poppler pdftotext/pdftoppm", "Python standard library", "view_image", "web.run source access"]},
    }
    PROVENANCE.write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    (CACHE / "check-build.json").write_text(json.dumps(validation, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"rows": len(rows), "wordingErrors": validation["errors"], "pendingRows": len(validation["pending_rows"]), "csvSha256": digest(CSV)}, ensure_ascii=False))
    if validation["errors"]:
        raise SystemExit(1)


def check() -> None:
    provenance = json.loads(PROVENANCE.read_text())
    if digest(CSV) != provenance["build"]["csvSha256"] or digest(Path(__file__)) != provenance["build"]["builderSha256"]:
        raise SystemExit("Inventory/builder no longer matches provenance; rebuild required")
    pages, _, _ = run_extract()
    with CSV.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    result = validate(rows, pages)
    (CACHE / "check-current.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "rows": result["rows"], "errors": result["errors"], "pendingRows": len(result["pending_rows"])}, ensure_ascii=False))
    if result["errors"]:
        raise SystemExit(1)


def fetch() -> None:
    CACHE.mkdir(parents=True, exist_ok=True)
    for source in SOURCES.values():
        path = CACHE / source["file"]
        if path.exists() and digest(path) == source["sha256"]:
            continue
        with urllib.request.urlopen(source["url"], timeout=60) as response:
            content = response.read()
        if hashlib.sha256(content).hexdigest() != source["sha256"]:
            raise SystemExit(f"Official source changed; refusing silent update: {source['url']}")
        path.write_bytes(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["fetch", "build", "check"])
    args = parser.parse_args()
    {"fetch": fetch, "build": build, "check": check}[args.operation]()
