"""Minimal search API skeleton.

No chatbot. Keyword search + date filter over minutes_raw / minutes_structured.
Run with: uvicorn search.app:app --reload
"""

from fastapi import FastAPI

app = FastAPI(title="Elizabethtown Minutes Search", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "search"}


@app.get("/search")
def search(q: str = "", date_from: str | None = None, date_to: str | None = None):
    # TODO: query MongoDB minutes_raw / minutes_structured
    return {"query": q, "date_from": date_from, "date_to": date_to, "results": []}
