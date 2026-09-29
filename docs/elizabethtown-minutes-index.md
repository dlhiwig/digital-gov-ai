# Elizabethtown Minutes Index — Phase 1 Build Plan

**Status:** Planning (Phase 0.2 / 1.0)  
**Last updated:** 2026-09-29  
**Depends on:** `docs/elizabethtown-plan.md`, `docs/elizabethtown-source-inventory.md`  
**Goal:** A searchable, AI-ready index of Elizabethtown City Council minutes — the first vertical slice.

This document is the detailed build plan for the Phase 1 milestone: **searchable index of the last ~2 years of council minutes**, queryable by keyword, date, and extracted fields. No chatbot in v1 — search and structured filters only. Answers come later, once the data is trustworthy.

---

## 1. Why this first

- Documents already exist as PDFs on the city site — no permission needed to start.
- Output is immediately useful to residents, journalists, and council members.
- Lowest-friction entry point to earn trust with the city's IT team (Thomas Hill) and clerk (Jessica Graham).
- Builds the exact data foundation later phases (ordinances, permits, GIS, audio) will reuse.
- Chatbots hallucinate; one wrong answer about a fee or zoning rule erases months of trust. Search first.

---

## 2. Where the information comes from

### 2.1 Primary — City website Documents tree

| Item | Detail |
|------|--------|
| Page | https://www.elizabethtownky.org/government/city_clerk/meeting_minutes_/ |
| Storage pattern | `/Documents/Government/Agenda and Minutes/[Year]/...` |
| Formats | PDF, DOCX, DOCX.PDF (timestamped `?t=` query params) |
| Cadence | Regular meetings 1st & 3rd Mondays; work sessions 2nd & 4th Mondays; 4:30 p.m.; Council Chambers, 212 W Dixie Ave |
| Coverage on page | 2026: Apr–Sep (partial, ~28 entries); 2025: only Jan 13 & Jan 21 listed; 2024 & prior: not listed |
| Sample | `.../Minutes 2026 Council/MINUTES 2026-09-14 SPECIAL MEETING.docx.pdf` |

**Gap:** The minutes page only surfaces recent 2026 entries plus two from January 2025. Older years need a deeper crawl of the Documents folder or a direct request to the clerk. FOIA/open-records request is planned separately (user-owned).

### 2.2 Secondary — YouTube video archive (audio path, Phase 5+)

| Item | Detail |
|------|--------|
| Playlist | "City Council Meetings \| Elizabethtown, KY" |
| URL | https://www.youtube.com/playlist?list=PLhVkHi5RhvS8JXv6XGDVsfvd639uHGhIp |
| Volume | ~448 videos, back to at least 2020 |
| Channel | City of Elizabethtown |
| Use | Transcription + summarization in Phase 5; not required for Phase 1 search index |

### 2.3 Tertiary — In-person capture

- Attend meetings (regular cadence above) and capture audio with a phone or recorder.
- Useful for meetings not yet posted, and as a quality check against the posted minutes.
- Store raw audio under `data/raw/elizabethtown/audio/` (Git LFS or external storage; link from repo).

### 2.4 Contacts for filling gaps

| Role | Name | Contact |
|------|------|---------|
| City Clerk | Jessica Graham | City Hall, 200 W Dixie Ave; 270-765-6121 |
| Mayor | Jeff Gregory | jeff.gregory@elizabethtownky.gov; 270-765-6121 |
| Public Relations | Amy Inman | amy.inman@elizabethtownky.gov; 270-317-2617 |
| IT Director | Thomas Hill | (via City Hall switchboard) |

---

## 3. What needs to be done

### 3.1 Phase 0.2 — Repo & environment (skeleton)

- [ ] Create working area: `elizabethtown/` at repo root (or keep under `data/` + `scripts/`; decide in implementation).
- [ ] Add `elizabethtown/fetcher/` — crawler for the Documents tree.
- [ ] Add `elizabethtown/processor/` — OCR + extraction stubs.
- [ ] Add `elizabethtown/store/` — DB schema + client stubs.
- [ ] Add `elizabethtown/search/` — minimal search UI stub.
- [ ] Dockerize: `Dockerfile` per stage + `docker-compose.yml` (fetcher, processor, db, search).
- [ ] Add `.env.example` (DB URL, OCR config, rate-limit settings). Never commit secrets.
- [ ] Pick OCR engine: **Tesseract** as baseline; AI-OCR upgrade path documented.
- [ ] Decide storage: lean **MongoDB** for the pilot (raw text + structured fields).
- [ ] Success: skeleton runs in Docker locally; one sample PDF flows fetch → OCR → store.

### 3.2 Phase 1.1 — Ingestion (fetcher)

- [ ] Build a fetcher that walks `/Documents/Government/Agenda and Minutes/` and downloads PDFs/DOCX.
- [ ] Respect rate limits; record **source URL + retrieval date + content hash** per document (per `docs/methodology.md`).
- [ ] Handle timestamped query params (`?t=...`) and DOCX.PDF variants.
- [ ] Deep-crawl for 2024–2025 coverage missing from the public page; log gaps for the clerk request.
- [ ] Store raw files under `data/raw/elizabethtown/minutes/` (or external storage + manifest in repo).
- [ ] Produce a manifest CSV/JSON: `filename, source_url, retrieved_at, sha256, meeting_date (parsed), type (regular/special/work session)`.

### 3.3 Phase 1.2 — Processing (OCR + extraction)

- [ ] OCR scanned/image-based minutes with Tesseract; keep the text layer for born-digital PDFs.
- [ ] Extract structured fields:
  - meeting date, type (regular / special / work session)
  - attendees (mayor, council members, staff)
  - agenda items / topics
  - motions, votes (for/against/abstain), outcomes
  - dollar amounts mentioned
  - decisions / actions taken
- [ ] Normalize names and dates; dedupe across documents.
- [ ] Write extracted fields to a structured collection; raw OCR text to the document store.
- [ ] Log extraction confidence; flag low-confidence fields for manual review.

### 3.4 Phase 1.3 — Storage & query

- [ ] **Raw text** in MongoDB `minutes_raw` (full OCR text + metadata).
- [ ] **Structured fields** in MongoDB `minutes_structured` (queryable by date, topic, attendee, amount).
- [ ] Minimal search endpoint: full-text over minutes + filters (date range, topic, attendee).
- [ ] Tiny search UI (static page or simple Flask/FastAPI template) — keyword search + date filter.
- [ ] `docker-compose up` brings up fetcher, processor, DB, and search UI together.

### 3.5 Phase 1.4 — Success criteria (milestone)

- [x] Plan committed to repo (this file).
- [ ] Searchable index of the last ~2 years of council minutes, queryable by keyword, date, and extracted fields.
- [ ] Pipeline fully containerized and reproducible.
- [ ] Everything documented so a second person could refresh the data.
- [ ] No secrets committed; attribution recorded per `docs/methodology.md`.

---

## 4. Data layout (proposed)

```
elizabethtown/
├── fetcher/          # crawler + manifest writer
├── processor/        # OCR + field extraction
├── store/            # Mongo schema + client
├── search/           # search endpoint + tiny UI
├── docker/           # Dockerfiles, compose
└── README.md

data/
├── raw/elizabethtown/minutes/     # downloaded PDFs (or external + manifest)
├── raw/elizabethtown/audio/      # in-person captures (Phase 5+)
└── processed/elizabethtown/      # extracted JSON, normalized text
```

Large binaries stay out of git (Git LFS or external storage); the repo holds manifests, schemas, and scripts.

---

## 5. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Public page only lists partial 2025/2026 | Deep crawl + clerk request for missing years |
| DOCX.PDF / timestamped URLs break fetchers | Normalize URLs; hash content, not URL |
| OCR errors on scanned minutes | Tesseract baseline + manual review queue for low confidence |
| Hallucinated answers damage trust | No LLM Q&A in v1 — search + structured filters only |
| City IT sees this as a threat | Frame as "takes work off your plate"; offer to hand over the pipeline |
| Storage choice wrong | Lean Mongo for pilot; schema is portable to Cosmos/DocumentDB later |

---

## 6. Out of scope for this slice

- Chatbot / Q&A over minutes (Phase 5).
- Ordinances, permits, GIS, audio transcription (later phases).
- Any write-back to city systems.
- Production hosting beyond a cheap VPS for the demo.

---

## 7. Next actions

1. Implement the fetcher against the Documents tree (start with 2026 entries visible on the page).
2. Run one sample PDF end-to-end through OCR + store.
3. Email/visit Jessica Graham to fill the 2025 gap and confirm coverage.
4. Demo the searchable index to Thomas Hill as the credibility wedge.
