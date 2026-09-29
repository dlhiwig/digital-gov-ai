# Search

Minimal search over the minutes index. **No chatbot in v1.**

## Capabilities (v1)

- Full-text keyword search over `minutes_raw.raw_text`.
- Filters: date range, meeting type, attendee, topic, dollar amount present.
- Tiny UI: single search box + date filter (static page or simple FastAPI/Flask template).
- Results show: meeting date, type, matched snippet, link to source PDF.

## Out of scope (v1)

- LLM Q&A / summarization (Phase 5).
- Faceted navigation beyond basic filters.
- Public auth or rate limiting (add when hosted).

## Status

- [ ] Search endpoint
- [ ] Tiny UI
- [ ] Dockerized alongside DB
