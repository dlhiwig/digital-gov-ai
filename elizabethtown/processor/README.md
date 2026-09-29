# Processor

OCR + structured field extraction for council minutes.

## Pipeline

1. **OCR** — Tesseract baseline for scanned/image PDFs; keep text layer for born-digital PDFs.
2. **Extract** structured fields:
   - meeting date, type (regular / special / work session)
   - attendees (mayor, council, staff)
   - agenda items / topics
   - motions, votes (for/against/abstain), outcomes
   - dollar amounts
   - decisions / actions taken
3. **Normalize** names and dates; dedupe across documents.
4. **Write** raw OCR text → `minutes_raw`; extracted fields → `minutes_structured`.
5. **Flag** low-confidence fields for manual review.

## Output contract

Structured collection is queryable by date, topic, attendee, and amount. Raw text supports full-text search.

## Status

- [ ] OCR stub (Tesseract)
- [ ] Extraction stub (regex / LLM-assisted, TBD)
- [ ] Normalization + dedupe
- [ ] Confidence logging
