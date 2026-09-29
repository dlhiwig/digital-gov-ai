# Elizabethtown, KY — Civic Data Pipeline

**Target:** City of Elizabethtown, Hardin County, Kentucky (county seat, ~31k people).
**Goal:** Build an open, searchable, AI-ready index of local government records — starting with council minutes — proving the model on a small government that hasn't done the heavy lifting yet.

This is the first concrete implementation project under the Digital Gov AI umbrella. The general repo stays a curated index; this plan lives here as the working blueprint for the Elizabethtown pilot.

---

## Why Elizabethtown

- County seat and largest city in Hardin County — the natural local target.
- Already has a thin but real digital footprint: online permit portal, ArcGIS zoning maps, published ordinances, public-works site.
- No true open-data API exists — the gap this project fills.
- Local access: I live in Elizabethtown, can attend council meetings, and can work directly with the county clerk for source documents.
- Small enough to be tractable; real enough to matter.

**Out of scope for now:** Louisville (different metro, would make the project generic), Radcliff (thinner web presence), Brandenburg (Meade County, not Hardin).

---

## Architecture (three layers)

1. **Ingestion** — pull from the city site (ordinances, agendas, minutes) and from my own scans/photos of physical documents. Second path: meeting audio capture.
2. **Processing** — OCR (advanced AI OCR) + extraction of structured fields: dates, attendees, motions, votes, dollar amounts, decisions.
3. **Storage** — document store (Mongo or Azure/AWS) for raw text + structured layer for extracted fields, so both free-text and field queries work. Dockerized end to end so it runs identically locally and on a cheap VPS.

---

## Phase 0 — Foundation

*Scope the problem, lock the target, set up the skeleton. No heavy processing yet.*

### 0.1 Target & access
- [x] Confirm Elizabethtown as the pilot target.
- [x] Inventory the city's public document sources (ordinances page, agendas/minutes, permit portal, GIS). See `docs/elizabethtown-source-inventory.md`.
- [ ] Identify the county clerk / city clerk contact path for physical or higher-fidelity copies.
- [ ] Decide storage backend: Mongo vs Azure Cosmos vs AWS DocumentDB (lean Mongo for the pilot).

### 0.2 Repo & environment
- [ ] Create a dedicated working area in this repo (e.g. `elizabethtown/` or a sibling repo) with `data/raw`, `data/processed`, `scripts`, `docs`.
- [ ] Dockerize a minimal pipeline skeleton (fetcher + OCR stub + store stub).
- [ ] Add a `.env.example` and a short `CONTRIBUTING` note for the pilot.
- [ ] Pick the OCR engine (Tesseract baseline, with an AI-OCR upgrade path).

### 0.3 Success criteria
- Skeleton runs in Docker locally.
- One sample document (a single PDF of minutes) flows through fetch → OCR → store.
- A written source inventory committed to the repo.

---

## Phase 1 — First Vertical Slice

*Prove the full pipeline on one document type before scaling.*

### 1.1 Ingestion
- [ ] Scrape or download the last ~2 years of Elizabethtown City Council minutes (PDFs/HTML).
- [ ] Build a fetcher that respects rate limits and records source URL + retrieval date (per `docs/methodology.md`).
- [ ] Capture meeting audio at in-person sessions as a parallel ingestion path.

### 1.2 Processing
- [ ] Run OCR on scanned/image-based minutes; keep text layer for born-digital PDFs.
- [ ] Extract structured fields: meeting date, attendees, agenda items, motions, votes, dollar amounts, decisions.
- [ ] Normalize names and dates; dedupe across documents.

### 1.3 Storage & query
- [ ] Store raw text in the document DB; extracted fields in a structured collection.
- [ ] Expose a minimal search endpoint (full-text over minutes + filter by date/topic).
- [ ] Docker Compose brings up fetcher, processor, DB, and a tiny search UI.

### 1.4 Success criteria (Phase 1 milestone)
- **Searchable index of the last two years of council minutes**, queryable by keyword, date, and extracted fields.
- Pipeline fully containerized and reproducible.
- Everything documented so a second person could refresh the data.

---

## Later phases (sketch)

- **Phase 2:** Ordinances + zoning text; link decisions back to the minutes that produced them.
- **Phase 3:** Permits and public-works requests (the existing portals).
- **Phase 4:** GIS layers (parcels, zoning, floodplain) joined to the document index.
- **Phase 5:** Audio transcription of meetings; meeting summarization; a public-facing Q&A layer.

Each phase gets its own sub-phases when we reach it. Don't build ahead of the slice.

---

## Conventions

- Follow the repo's kebab-case naming and attribution rules (`docs/methodology.md`).
- Prefer linking to canonical city sources; mirror only when it adds stability or analysis value.
- Keep raw and processed data separated; never commit secrets.
- Update this file as phases complete — it's the living plan, not a one-time doc.
