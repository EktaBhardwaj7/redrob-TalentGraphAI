# ontology.py
from dataclasses import dataclass
from typing import FrozenSet

DIRECT = 1.0
RELATED = 0.6
IMPLICIT = 0.3


@dataclass(frozen=True)
class EvidenceRule:
    weight: float
    capabilities: FrozenSet[str]
    source: str = ""
    priority: int = 0


EVIDENCE_MAP = {
    # direct
    "faiss": EvidenceRule(DIRECT, frozenset({"retrieval", "vector_db"})),
    "qdrant": EvidenceRule(DIRECT, frozenset({"retrieval", "vector_db"})),
    "milvus": EvidenceRule(DIRECT, frozenset({"retrieval", "vector_db"})),
    "weaviate": EvidenceRule(DIRECT, frozenset({"retrieval", "vector_db"})),
    "pinecone": EvidenceRule(DIRECT, frozenset({"retrieval", "vector_db"})),
    "chroma": EvidenceRule(DIRECT, frozenset({"retrieval", "vector_db"})),
    "rag": EvidenceRule(DIRECT, frozenset({"retrieval"})),
    "learning to rank": EvidenceRule(DIRECT, frozenset({"ranking"})),
    "ltr": EvidenceRule(DIRECT, frozenset({"ranking"})),
    "reranking": EvidenceRule(DIRECT, frozenset({"ranking"})),
    "ab testing": EvidenceRule(DIRECT, frozenset({"evaluation"})),
    "a/b test": EvidenceRule(DIRECT, frozenset({"evaluation"})),
    "production ml": EvidenceRule(DIRECT, frozenset({"production_ml"})),
    "model serving": EvidenceRule(DIRECT, frozenset({"production_ml"})),
    "inference pipeline": EvidenceRule(DIRECT, frozenset({"production_ml"})),
    # related
    "semantic search": EvidenceRule(RELATED, frozenset({"retrieval"})),
    "vector search": EvidenceRule(RELATED, frozenset({"retrieval"})),
    "hybrid search": EvidenceRule(RELATED, frozenset({"retrieval"})),
    "ndcg": EvidenceRule(RELATED, frozenset({"ranking", "evaluation"})),
    "mrr": EvidenceRule(RELATED, frozenset({"ranking", "evaluation"})),
    "mean average precision": EvidenceRule(RELATED, frozenset({"ranking", "evaluation"})),
    "offline evaluation": EvidenceRule(RELATED, frozenset({"evaluation"})),
    "online experiment": EvidenceRule(RELATED, frozenset({"evaluation"})),
    "deployed model": EvidenceRule(RELATED, frozenset({"production_ml"})),
    # implicit
    "information retrieval": EvidenceRule(IMPLICIT, frozenset({"retrieval"})),
    "search infrastructure": EvidenceRule(IMPLICIT, frozenset({"retrieval"})),
    "relevance optimization": EvidenceRule(IMPLICIT, frozenset({"ranking"})),
    "search quality": EvidenceRule(IMPLICIT, frozenset({"ranking"})),
    "benchmarking": EvidenceRule(IMPLICIT, frozenset({"evaluation"})),
    "ml infrastructure": EvidenceRule(IMPLICIT, frozenset({"production_ml"})),
}

EVIDENCE_MAP.update({
    "hybrid retrieval": EvidenceRule(RELATED, frozenset({"retrieval"})),
    "reranking": EvidenceRule(DIRECT, frozenset({"ranking"})),
    "offline evaluation": EvidenceRule(RELATED, frozenset({"evaluation"})),
    "embedding drift": EvidenceRule(RELATED, frozenset({"retrieval", "production_ml"})),
    "index refresh": EvidenceRule(RELATED, frozenset({"retrieval", "production_ml"})),
    "online a/b": EvidenceRule(DIRECT, frozenset({"evaluation"})),
    "eval framework": EvidenceRule(RELATED, frozenset({"evaluation"})),
    "ml pipeline": EvidenceRule(RELATED, frozenset({"production_ml"})),
    "feature store": EvidenceRule(RELATED, frozenset({"production_ml"})),
    "kubernetes": EvidenceRule(RELATED, frozenset({"production_ml"})),
    "docker": EvidenceRule(RELATED, frozenset({"production_ml"})),
    "spark": EvidenceRule(RELATED, frozenset({"production_ml", "inference_optimization"})),
})

REQUIRED_CAPS = ["retrieval", "ranking", "evaluation", "vector_db", "production_ml"]
PREFERRED_CAPS = ["llm_finetuning", "learning_to_rank", "hrtech", "inference_optimization"]
ALL_CAPS = frozenset(REQUIRED_CAPS + PREFERRED_CAPS)