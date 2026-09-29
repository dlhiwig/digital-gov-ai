# Methodology

How we collect and attribute open information in this repo.

## Principles

1. **Open first** — prefer publicly available, openly licensed sources.
2. **Attribute everything** — record source URL, retrieval date, and license for every dataset or document.
3. **Don't duplicate unnecessarily** — link to canonical sources; mirror only when it adds value (normalization, stability, analysis).
4. **Reproducible** — scripts should be runnable and documented so others can refresh the data.
5. **Respect terms** — honor robots.txt, rate limits, and API terms of service.

## Workflow

1. Identify a source (dataset, API, project, policy document).
2. Document it under `resources/`.
3. If collecting, write a script under `scripts/` and store raw output in `data/raw/`.
4. Process into `data/processed/` with a short note on transformations.
5. Update `ROADMAP.md` if the work suggests new tasks.

## Attribution template

```
Source: <URL>
Retrieved: <YYYY-MM-DD>
License: <SPDX or description>
Notes: <any caveats>
```
