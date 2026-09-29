"""Store entry point: python -m store

Loads processed JSON into MongoDB collections: minutes_raw + minutes_structured.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("MONGO_DB", "elizabethtown")
PROCESSED = Path("data/processed/elizabethtown/extracted.json")


def main() -> None:
    if not PROCESSED.exists():
        print(f"no processed data at {PROCESSED}; run processor first")
        return
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    records = json.loads(PROCESSED.read_text())
    raw = db["minutes_raw"]
    structured = db["minutes_structured"]
    for rec in records:
        raw.update_one({"doc_id": rec["doc_id"]}, {"$set": rec}, upsert=True)
        structured.update_one({"doc_id": rec["doc_id"]}, {"$set": {k: rec[k] for k in rec if k != "raw_text"}}, upsert=True)
    print(f"upserted {len(records)} docs into {DB_NAME}")


if __name__ == "__main__":
    main()
