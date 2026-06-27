# Architecture

TalentGraph AI is organized as a streaming ranking pipeline. Configuration is
loaded once, converted into an immutable `RankingContext`, then reused for every
candidate.

Core layers:

- `common`: low-level utilities.
- `config`: ontology, thresholds, runtime, and scoring weights.
- `models`: frozen or narrowly mutable state objects.
- `preprocess`: parsing, validation aliases, regex compilation, and indexes.
- `features`: independent scoring modules.
- `pipeline`: scoring, tiering, sorting, reasoning, writing, and validation.
- `diagnostics`: report helpers for auditability and future experiments.
