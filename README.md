# TalentGraph AI

TalentGraph AI is a deterministic, CPU-only candidate ranking engine for the
Redrob Intelligent Candidate Discovery & Ranking Challenge.

The pipeline streams candidate profiles, extracts capability-based evidence,
scores each candidate with recruiter-inspired features, keeps only the top 100
profiles in memory, and writes a submission CSV with evidence-backed reasoning.

## Quick Start

```bash
python rank.py --candidates data/raw/candidates/candidates.jsonl --jd data/processed/parsed_jd.json --out data/output/submission.csv
```

For a quick smoke run:

```bash
python rank.py --candidates data/raw/candidates/candidates.jsonl --out data/output/submission.csv --limit 100
python data/raw/submission/validate_submission.py data/output/submission.csv
```

## Deployment / Reproducibility

This repository is Binder-ready. After pushing it to GitHub, open it with:

```text
https://mybinder.org/v2/gh/EktaBhardwaj7/redrob-TalentGraphAI/HEAD?urlpath=lab
```

Then run the same ranking command from the Binder terminal. See `DEPLOYMENT.md`
for the full reproducibility guide and submission checklist.

## Architecture

- `src/common/`: text, dates, streaming, regex, math, logging, and I/O helpers.
- `src/config/`: ontology, scoring weights, thresholds, runtime defaults, and keywords.
- `src/models/`: evidence, feature, candidate, ranking, validation, and score dataclasses.
- `src/preprocess/`: normalization aliases, JD parsing, compiled patterns, evidence and lookup indexes.
- `src/features/`: independent feature extractors for JD coverage, production, experience, market validation, hireability, preferred match, consistency, and penalties.
- `src/pipeline/`: scoring, tiering, sorting, reasoning, exporting, writing, validation, and metrics.
- `src/diagnostics/`: lightweight diagnostics hooks for reports and future analysis.

## Design Principles

- No network calls at runtime.
- Deterministic sorting with `candidate_id` as the final tie-breaker.
- Evidence-first reasoning generated only from extracted profile signals.
- Streaming input and top-k retention for 100,000+ candidates under CPU/memory limits.
