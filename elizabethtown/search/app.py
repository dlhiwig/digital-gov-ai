"""Minimal search API: keyword + date filter over minutes. No chatbot in v1."""
from __future__ import annotations

import os
from typing import Optional

from fastapi import FastAPI, Query
from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("MONGO_DB", "elizabethtown")

app = FastAPI(title="Elizabethtown Minutes Search", version="0.1.0")
_client = None


def db():
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URL)
    return _client[DB_NAME]


@app.get("/health")
def health():
    return {"status": "ok", "service": "search"}


@app.get("/search")
def search(
    q: str = "",
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    meeting_type: Optional[str] = None,
    limit: int = Query(20, le=100),
):
    filt: dict = {}
    if q:
        filt["$text"] = {"$search": q}
    if date_from or date_to:
        dr = {}
        if date_from:
            dr["$gte"] = date_from
        if date_to:
            dr["$lte"] = date_to
        filt["meeting_date"] = dr
    if meeting_type:
        filt["meeting_type"] = meeting_type
    cur = db()["minutes_structured"].find(filt, {"raw_text": 0}).limit(limit)
    return {"query": q, "count": cur.count() if hasattr(cur, "count") else None, "results": list(cur)}


@app.get("/")
def index():
    return {
        "service": "Elizabethtown Minutes Search",
        "endpoints": ["/health", "/search?q=...&date_from=...&date_to=..."],
        "note": "No chatbot in v1 — search + filters only.",
    }
