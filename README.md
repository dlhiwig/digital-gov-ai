# Digital Gov AI

Open-source collection and tooling for **artificial intelligence in digital government**.

This repository gathers publicly available information, datasets, tools, and projects related to how governments use AI for service delivery, transparency, policy, and citizen engagement. The goal is to make that knowledge easier to find, reuse, and build on.

## What this repo is

- A curated index of open-source projects, datasets, and APIs in the civic-tech / digital-government space
- A living roadmap of ideas and work we want to tackle
- A place to collect and organize open information (scrapers, summaries, metadata) without reinventing the wheel

## Repository structure

```
.
├── README.md              # You are here
├── ROADMAP.md             # Things we want to work on / could work on
├── resources/             # Curated lists of existing open-source projects & data
│   ├── projects.md
│   ├── datasets.md
│   └── apis.md
├── data/                  # Collected open information (raw + processed)
│   ├── raw/
│   └── processed/
├── scripts/               # Collection, cleaning, and analysis scripts
└── docs/                  # Longer notes, methodology, and write-ups
```

## Naming & conventions

- Repo and folders use **kebab-case** (lowercase, hyphens).
- Keep data sources documented with a short README in each subfolder.
- Prefer linking to upstream open data over vendoring large files.

## Getting started

1. Browse `ROADMAP.md` for current priorities.
2. Check `resources/` for existing projects to build on or avoid duplicating.
3. Drop collected data under `data/` and scripts under `scripts/`.

## License

TBD — likely MIT or CC-BY for the curated content. Data retains its original licenses.

## Contributing

PRs welcome. Open an issue first for larger changes so we can keep the roadmap coherent.
