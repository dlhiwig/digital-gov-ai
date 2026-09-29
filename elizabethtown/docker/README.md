# Docker

Containerized pipeline so it runs identically locally and on a cheap VPS.

## Proposed services (docker-compose)

| Service | Image | Role |
|---------|-------|------|
| `fetcher` | custom (Python) | Crawl + download minutes |
| `processor` | custom (Python + Tesseract) | OCR + extraction |
| `db` | `mongo:7` | Raw text + structured fields |
| `search` | custom (FastAPI/Flask) | Search endpoint + tiny UI |

## Files

- `Dockerfile.fetcher`, `Dockerfile.processor`, `Dockerfile.search`
- `docker-compose.yml` — brings up all four services
- `.env.example` — DB URL, OCR config, rate limits (copy to `.env`, never commit)

## Status

- [ ] Dockerfiles
- [ ] docker-compose.yml
- [ ] .env.example
- [ ] `docker compose up` runs end-to-end with one sample doc
