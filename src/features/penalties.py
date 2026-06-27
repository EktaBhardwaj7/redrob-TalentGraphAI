# penalties.py
import re
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class PenaltiesFeature(Feature):
    name = "penalties"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        accumulated = 0.0
        warnings = []

        consulting_companies = {"tcs", "infosys", "wipro", "accenture", "cognizant", "capgemini"}
        history = state.raw.get("career_history", [])
        all_consulting = all(
            entry.get("company", "").lower() in consulting_companies
            for entry in history
        )
        if all_consulting and len(history) > 1:
            accumulated += 0.20
            warnings.append("Consulting-only career")

        # Check for retrieval evidence using the pre-built index
        has_retrieval = any(
            phrase in state.matched_evidence
            for phrase in ["faiss", "retrieval", "ranking", "ndcg", "mrr"]
        )
        if not has_retrieval:
            accumulated += 0.10
            warnings.append("No retrieval/ranking evidence")

        # Apply penalty as negative, capped at -0.20
        penalty = -min(0.20, accumulated)

        evidence = [
            EvidenceItem(
                source="penalties",
                value=f"{len(warnings)} warnings",
                confidence=1.0,
                metadata={"warnings": warnings}
            )
        ]

        return FeatureResult(
            name=self.name,
            raw_score=penalty,
            normalized_score=penalty,
            evidence=evidence,
            warnings=warnings,
        )