"""Small synonym index for capability-oriented matching."""

DEFAULT_SYNONYMS = {
    "retrieval": {"search", "semantic search", "vector search", "information retrieval"},
    "ranking": {"reranking", "learning to rank", "ltr", "relevance"},
    "evaluation": {"ndcg", "mrr", "map", "ab testing", "offline evaluation"},
    "vector_db": {"faiss", "qdrant", "milvus", "pinecone", "weaviate", "chroma"},
    "production_ml": {"model serving", "inference", "deployed model", "production ml"},
}


def build_synonym_index(extra: dict[str, set[str]] | None = None) -> dict[str, set[str]]:
    index = {key: set(values) for key, values in DEFAULT_SYNONYMS.items()}
    for key, values in (extra or {}).items():
        index.setdefault(key, set()).update(values)
    return index


__all__ = ["DEFAULT_SYNONYMS", "build_synonym_index"]
