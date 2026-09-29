# Elizabethtown, KY — Civic Data Pipeline

Working area for the **Elizabethtown minutes index** pilot (Phase 1 vertical slice).

Full plan: [`docs/elizabethtown-plan.md`](../docs/elizabethtown-plan.md)  
Detailed build plan: [`docs/elizabethtown-minutes-index.md`](../docs/elizabethtown-minutes-index.md)  
Source inventory: [`docs/elizabethtown-source-inventory.md`](../docs/elizabethtown-source-inventory.md)

## Layout (proposed)

```
elizabethtown/
├── fetcher/      # crawler for /Documents/Government/Agenda and Minutes/
├── processor/    # OCR (Tesseract) + field extraction
├── store/        # MongoDB schema + client
├── search/       # minimal search endpoint + tiny UI
├── docker/       # Dockerfiles + docker-compose.yml
└── README.md     # this file
```

## Principles

- **Search first, answers second.** No chatbot in v1.
- Respect rate limits; record source URL + retrieval date + content hash per document.
- Never commit secrets (use `.env.example`).
- Large binaries out of git (Git LFS or external storage); repo holds manifests + scripts.
- Dockerized end to end so it runs identically locally and on a cheap VPS.

## Status

- [x] Plan + phasing committed
- [ ] Fetcher implemented
- [ ] One sample PDF through fetch → OCR → store
- [ ] Searchable index of last ~2 years of minutes
