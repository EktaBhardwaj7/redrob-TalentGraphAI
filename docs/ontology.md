# Ontology

The ontology maps phrases such as `faiss`, `semantic search`, and `ndcg` to
higher-level capabilities including retrieval, ranking, evaluation, vector
databases, and production ML.

Each rule carries a confidence weight:

- Direct evidence: `1.0`
- Related evidence: `0.6`
- Implicit evidence: `0.3`

This gives the ranker flexibility without rewarding keyword stuffing blindly.
