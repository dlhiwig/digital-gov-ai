# Fetcher

Crawls the Elizabethtown city Documents tree for council agendas and minutes.

## Target

- Base: `https://www.elizabethtownky.org`
- Tree: `/Documents/Government/Agenda and Minutes/[Year]/...`
- Entry page: https://www.elizabethtownky.org/government/city_clerk/meeting_minutes_/
- Formats: PDF, DOCX, DOCX.PDF (may carry `?t=` timestamp query params)

## Responsibilities

1. Walk the Documents folder (respect `robots.txt` and rate limits).
2. Download each document; compute SHA-256.
3. Write a **manifest** (CSV/JSON) with: `filename, source_url, retrieved_at, sha256, meeting_date, type`.
4. Handle gaps: log missing years for the clerk request; do not fail the whole run.
5. Store raw files under `data/raw/elizabethtown/minutes/` or external storage (link from manifest).

## Output contract

The manifest is the handoff to `processor/`. Every downstream step keys off the manifest, not the raw URLs.

## Status

- [ ] Skeleton
- [ ] Crawler for 2026 entries (visible on page)
- [ ] Deep crawl for 2024–2025
- [ ] Manifest writer
