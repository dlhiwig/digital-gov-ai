# Store

MongoDB schema and client for the minutes index.

## Collections (proposed)

### `minutes_raw`
- `doc_id`, `filename`, `source_url`, `retrieved_at`, `sha256`
- `meeting_date`, `meeting_type`
- `raw_text` (full OCR text)
- `ocr_engine`, `ocr_confidence`

### `minutes_structured`
- `doc_id` (FK → minutes_raw)
- `attendees[]`, `agenda_items[]`, `motions[]`, `votes[]`
- `dollar_amounts[]`, `decisions[]`
- `extracted_at`, `extraction_confidence`

## Principles

- Lean Mongo for the pilot; schema is portable to Cosmos/DocumentDB later.
- Separate raw text from structured fields so both free-text and field queries work.
- No secrets in repo — connection string via `.env`.

## Status

- [ ] Schema definition
- [ ] Client module
- [ ] Seed with one sample document
