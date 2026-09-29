"""Fetcher entry point: python -m fetcher

Walks the Elizabethtown Documents tree for council agendas/minutes,
downloads each document, computes a content hash, and writes a manifest.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse

import requests
from bs4 import BeautifulSoup

BASE = os.environ.get("FETCH_BASE_URL", "https://www.elizabethtownky.org")
INDEX_URL = f"{BASE}/government/city_clerk/meeting_minutes_/"
UA = os.environ.get(
    "FETCH_USER_AGENT",
    "DigitalGovAI-Research/0.1 (research; contact: research@example.com)",
)
RATE = float(os.environ.get("FETCH_RATE_LIMIT_RPS", "1"))
OUT_DIR = Path(os.environ.get("FETCH_OUT_DIR", "data/raw/elizabethtown/minutes"))
MANIFEST = Path(os.environ.get("FETCH_MANIFEST", "data/raw/elizabethtown/manifest.json"))


@dataclass
class DocRecord:
    filename: str
    source_url: str
    retrieved_at: str
    content_sha256: str
    meeting_date: Optional[str]
    meeting_type: Optional[str]
    doc_kind: str  # agenda | minutes | notice | cancellation
    format: str
    bytes: int
    attribution: str = "City of Elizabethtown, KY — public record, elizabethtownky.org"
    license: str = "public record / open for reuse with attribution"
    local_path: Optional[str] = None
    notes: str = ""


def _session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "application/pdf,*/*"})
    return s


def _guess_kind(name: str) -> str:
    n = name.lower()
    if "minutes" in n:
        return "minutes"
    if "notice" in n and "cancel" in n:
        return "cancellation"
    if "notice" in n:
        return "notice"
    if "agenda" in n:
        return "agenda"
    return "other"


def _guess_type(name: str) -> Optional[str]:
    n = name.lower()
    if "regular" in n:
        return "regular"
    if "special" in n:
        return "special"
    if "work" in n:
        return "work_session"
    if "joint" in n:
        return "joint"
    return None


def _guess_date(name: str) -> Optional[str]:
    m = re.search(r"(20\d{2})-(\d{2})-(\d{2})", name)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    m = re.search(r"(\d{2})-(\d{2})-(\d{4})", name)
    if m:
        return f"{m.group(3)}-{m.group(1)}-{m.group(2)}"
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", name)
    if m:
        y = m.group(3)
        y = f"20{y}" if len(y) == 2 else y
        return f"{y}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
    return None


def _clean_url(href: str) -> str:
    # strip duplicate timestamp params some CMS links carry
    return href.split("&t=")[0] if "&t=" in href else href


def crawl(session: requests.Session) -> list[DocRecord]:
    r = session.get(INDEX_URL, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")
    records: list[DocRecord] = []
    seen: set[str] = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "Documents/Government/Agenda and Minutes" not in href:
            continue
        url = _clean_url(href)
        if not url.startswith("http"):
            url = BASE + url if url.startswith("/") else BASE + "/" + url
        if url in seen:
            continue
        seen.add(url)
        name = unquote(urlparse(url).path.split("/")[-1])
        rec = DocRecord(
            filename=name,
            source_url=url,
            retrieved_at=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            content_sha256="",
            meeting_date=_guess_date(name),
            meeting_type=_guess_type(name),
            doc_kind=_guess_kind(name),
            format=Path(name).suffix.lstrip(".").lower() or "unknown",
            bytes=0,
        )
        records.append(rec)
    return records


def download(session: requests.Session, rec: DocRecord) -> DocRecord:
    r = session.get(rec.source_url, timeout=60)
    r.raise_for_status()
    data = r.content
    rec.bytes = len(data)
    rec.content_sha256 = hashlib.sha256(data).hexdigest()
    rec.local_path = str(OUT_DIR / rec.filename)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / rec.filename).write_bytes(data)
    return rec


def write_manifest(records: list[DocRecord]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(r) for r in records]
    MANIFEST.write_text(json.dumps(payload, indent=2))
    print(f"wrote {len(records)} records -> {MANIFEST}")


def main() -> None:
    session = _session()
    print(f"crawling {INDEX_URL}")
    records = crawl(session)
    print(f"found {len(records)} document links")
    for rec in records:
        try:
            download(session, rec)
            print(f"  ok  {rec.filename} ({rec.bytes} bytes)")
        except Exception as e:  # noqa: BLE001
            rec.notes = f"download failed: {e}"
            print(f"  ERR {rec.filename}: {e}")
    write_manifest(records)


if __name__ == "__main__":
    main()
