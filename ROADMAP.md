# Roadmap — Digital Gov AI

Living list of things we **want to work on** and **could work on**. Check items off as they land; add new ones as ideas come up.

## Near-term (next few weeks)

- [x] Add MIT license
- [x] Compile list of similar repositories (see `resources/related-repos.md`)
- [ ] Finalize contribution guidelines
- [ ] Expand `resources/projects.md` with 20–30 high-quality open-source civic/digital-gov AI projects
- [ ] Add a first dataset: U.S. federal AI use-case inventory (OMB) normalized snapshot
- [x] Write a short methodology note on how we collect and attribute open information
- [ ] Set up a simple issue template for "new resource" and "new dataset" suggestions

## Active project — Elizabethtown, KY pilot

First concrete implementation: an AI-ready civic data pipeline for the City of Elizabethtown (Hardin County, KY). Full plan with phases and sub-phases: **[docs/elizabethtown-plan.md](docs/elizabethtown-plan.md)**.

- [ ] **Phase 0 — Foundation:** source inventory, storage decision, Docker skeleton, one sample doc through the pipeline.
- [ ] **Phase 1 — Vertical slice:** searchable index of the last ~2 years of city council minutes (OCR + extraction + query).
- [ ] Phase 2+: ordinances, permits, GIS layers, meeting audio (sketched in the plan).

## Could work on (backlog / ideas)

### Data collection & curation
- [ ] Scrape or mirror high-value open government datasets (data.gov, state/local open data portals)
- [ ] Build a lightweight catalog of AI-related government policies and algorithm registers (e.g. Amsterdam, Helsinki, Eurocities schema)
- [ ] Collect public AI procurement / vendor disclosures from government sources
- [ ] Track open-source AI tools adopted by municipalities (Boston MCP skills, Jigsaw Sensemaking, etc.)
- [ ] Curate a list of FOIA / open-records AI tooling (e.g. CivicSunshine)

### Analysis & tooling
- [ ] Small scripts to normalize and dedupe collected datasets
- [ ] A simple search or filter over the curated resources (static site or GitHub Pages)
- [ ] Summarization pipeline for long policy documents using open models
- [ ] Prototype an MCP server or agent skills layer over a small set of civic data sources
- [ ] Dashboard of "AI in government" adoption signals by jurisdiction

### Community & documentation
- [ ] Write-up: landscape of open-source digital government AI (who is doing what)
- [ ] Case studies: 2–3 real deployments (e.g. participatory budgeting platforms, citizen engagement tools)
- [ ] Glossary of terms (digital government, civic tech, algorithm register, etc.)
- [ ] Monthly digest of new open-source releases in this space

### Stretch / later
- [ ] Federated or multi-jurisdiction comparison of AI governance frameworks
- [ ] Evaluation harness for civic-facing LLM outputs (accuracy, bias, source attribution)
- [ ] Partnerships or mirrors with existing awesome lists (awesome-civic-tech, Civic Tech Field Guide)

## Done

- [x] Create repository and initial structure
- [x] Seed README, ROADMAP, and starter resource lists
- [x] Add MIT license
- [x] Compile list of similar repositories
- [x] Write methodology note
- [x] Lock Elizabethtown, KY as the first implementation target and draft Phase 0 / Phase 1 plan
