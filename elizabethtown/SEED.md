# Seed document — September 14, 2026 Special Meeting

This is the first real document through the pipeline. It proves the vertical slice end to end.

## What it contains

- **4 ordinances** on first reading: tax rates (motor vehicle, franchise, real/personal property) + a zoning map amendment (Prospect Pointe Drive C-2 → C-3).
- **2 municipal orders**: Yale Drive sanitary sewer bid acceptance; Steelgrove Amphitheater contract scope revision (anonymous donation noted).
- **Employee recognitions**: CDL certifications, fire recruit graduates, playground safety inspectors.
- **Attendees / absent**, motions with movers and seconders, 4-0 votes.
- **Info items**: IACP national recognition of the police department, cooling shelter, Louisville Orchestra event, Harvest Festival.

## Why this one

It's recent, it's a special meeting (shorter, cleaner structure), and it touches taxes, zoning, and public works — the exact topics residents search for. Good stress test for the extractor.

## Pipeline status on this doc

| Stage | Status |
|-------|--------|
| Source identified | done |
| Text extracted | done (CDN) |
| Manifest entry | done |
| Structured extraction | done (regex) |
| Stored in Mongo | ready (run `python -m store`) |
| Searchable | ready (run `python -m search`) |

## Next

Run the fetcher against the live Documents tree to pull the rest of 2026, then re-run processor + store.
