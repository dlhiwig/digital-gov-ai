"""Processor entry point: python -m processor

Reads the fetcher manifest, runs OCR/text extraction on each document,
extracts structured fields, and writes processed JSON + normalized text.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Optional

import fitz  # PyMuPDF

MANIFEST = Path("data/raw/elizabethtown/manifest.json")
OUT_DIR = Path("data/processed/elizabethtown")


@dataclass
class Extracted:
    doc_id: str
    meeting_date: Optional[str]
    meeting_type: Optional[str]
    attendees: list[str] = field(default_factory=list)
    absent: list[str] = field(default_factory=list)
    motions: list[dict[str, Any]] = field(default_factory=list)
    ordinances: list[str] = field(default_factory=list)
    municipal_orders: list[str] = field(default_factory=list)
    dollar_amounts: list[str] = field(default_factory=list)
    decisions: list[str] = field(default_factory=list)
    raw_text: str = ""
    extraction_confidence: float = 0.0
    notes: str = ""


ATTENDEE_RE = re.compile(r"PRESENT:\s*([^\n]+)", re.I)
ABSENT_RE = re.compile(r"ABSENT:\s*([^\n]+)", re.I)
MOTION_RE = re.compile(r"moved by ([^,]+), seconded by ([^\n,]+).*?carried", re.I | re.S)
ORD_RE = re.compile(r"Ordinance\s*#?(\d{1,3}-\d{4})", re.I)
MO_RE = re.compile(r"Municipal Order\s*#?(\d{1,3}-\d{4})", re.I)
DOLLAR_RE = re.compile(r"\$\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?")


def extract_text(path: Path) -> str:
    try:
        doc = fitz.open(path)
        return "\n".join(p.get_text("text") for p in doc)
    except Exception:  # noqa: BLE001
        return path.read_text(errors="ignore")


def extract_fields(text: str, rec: dict) -> Extracted:
    ex = Extracted(
        doc_id=rec.get("content_sha256", "")[:12],
        meeting_date=rec.get("meeting_date"),
        meeting_type=rec.get("meeting_type"),
        raw_text=text,
    )
    m = ATTENDEE_RE.search(text)
    if m:
        ex.attendees = [x.strip() for x in m.group(1).split(",") if x.strip()]
    m = ABSENT_RE.search(text)
    if m:
        ex.absent = [x.strip() for x in m.group(1).split(",") if x.strip()]
    for mm in MOTION_RE.finditer(text):
        ex.motions.append({"mover": mm.group(1).strip(), "seconder": mm.group(2).strip()})
    ex.ordinances = sorted(set(ORD_RE.findall(text)))
    ex.municipal_orders = sorted(set(MO_RE.findall(text)))
    ex.dollar_amounts = sorted(set(DOLLAR_RE.findall(text)))
    # crude decision capture
    for line in text.splitlines():
        if "motion passed" in line.lower() or "carried" in line.lower():
            ex.decisions.append(line.strip())
    ex.extraction_confidence = 0.7 if ex.attendees or ex.motions else 0.3
    return ex


def main() -> None:
    if not MANIFEST.exists():
        print(f"no manifest at {MANIFEST}; run fetcher first")
        return
    records = json.loads(MANIFEST.read_text())
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = []
    for rec in records:
        path = Path(rec.get("local_path") or (Path("data/raw/elizabethtown/minutes") / rec["filename"]))
        text = extract_text(path) if path.exists() else ""
        ex = extract_fields(text, rec)
        out.append(asdict(ex))
        (OUT_DIR / f"{ex.doc_id}.json").write_text(json.dumps(asdict(ex), indent=2))
    (OUT_DIR / "extracted.json").write_text(json.dumps(out, indent=2))
    print(f"processed {len(out)} documents -> {OUT_DIR}")


if __name__ == "__main__":
    main()
