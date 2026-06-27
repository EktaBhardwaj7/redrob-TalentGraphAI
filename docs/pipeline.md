# Pipeline

1. Load configuration and job description.
2. Stream JSONL or JSONL.GZ candidates.
3. Normalize each candidate into `CandidateState`.
4. Build an evidence index from the ontology.
5. Run feature extractors in registry order.
6. Compute tier and fine scores.
7. Retain the top 100 candidates.
8. Sort deterministically and generate evidence-backed reasoning.
9. Write and validate the submission CSV.
