# What a lead engineer / AI director would do next

Beyond the seed document and working skeleton, here's the prioritized list.

## Immediate (this week)

1. **Run the fetcher live** against the Documents tree — the seed came from the CDN because the city host refused the connection from this environment. Verify the crawler handles the `?t=` timestamp params and DOCX.PDF variants.
2. **Deep-crawl 2024–2025** — the public page only lists two 2025 meetings; older minutes likely sit in `wp-content/uploads/` or other folders. Log every gap for the clerk request.
3. **Email/visit Jessica Graham** (City Clerk) to confirm 2025 coverage and request missing PDFs. This is the human wedge that unblocks the data.
4. **Stand up Mongo locally** via `docker compose up db` and run `python -m store` on the seed to prove the write path.
5. **Smoke-test the search API** — `python -m search`, hit `/search?q=ordinance`, confirm the seed doc returns.

## Short-term (next 2–4 weeks)

6. **Swap regex extraction for an LLM pass** — send each minute's text to a local model (or API) with a strict JSON schema for attendees, motions, votes, amounts, decisions. Keep regex as a fallback + confidence check.
7. **Add a review queue** — low-confidence extractions get flagged for manual confirmation before they hit the structured collection. Trust is the product.
8. **Normalize names** — "Council Member Tyler" ↔ "Mika Tyler"; build a small alias table for the six council members + mayor + clerk + staff who recur.
9. **Link ordinances to minutes** — Ordinance #14-2026 was read at this meeting; later phases should resolve each ordinance number to the minute it was introduced and the minute it passed on second reading.
10. **Add tests** — fixture PDFs + golden extracted JSON so refactors don't silently break extraction.
11. **Add a GitHub Action** — weekly cron that runs the fetcher, diffs the manifest, and opens a PR when new minutes appear. Keeps the index fresh without babysitting.
12. **Write the one-page AI policy** (risk tiers, no high-risk automated decisions, human-in-the-loop) and socialize it with Thomas Hill. Legitimacy before scale.

## Medium-term (before demo to city)

13. **Host a cheap VPS demo** — `docker compose up` on a $5–10/mo box, share the URL with Hill and the clerk. "Here's a searchable index of your last two years of minutes, zero cost to you."
14. **Add agenda PDFs too** — agendas are posted earlier than minutes; indexing both lets residents see what's coming, not just what happened.
15. **Capture audio at one in-person meeting** — parallel ingestion path; even one transcribed meeting is a strong Phase 5 teaser.
16. **Build the attribution + license footer** into the search UI so every result cites the city source. Non-negotiable for public trust.
17. **Prepare the handoff doc** — how Hill's team takes over the pipeline, the schema, the cron, the review queue. Frame it as "we built it, you own it."

## Explicitly not yet

- No chatbot / Q&A (Phase 5, after data is trustworthy).
- No write-back to city systems.
- No scraping behind logins (permit portal) until a data-sharing agreement exists.
- No production SLA or on-call rotation.
