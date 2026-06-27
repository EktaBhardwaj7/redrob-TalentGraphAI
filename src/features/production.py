# production.py
import re
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature

# These should come from config eventually
CORE_PROD = {"production", "shipped", "deployed", "model serving"}
SUPPORT_PROD = {"latency", "throughput", "online experiment", "inference optimization"}


@register_feature
class ProductionFeature(Feature):
    name = "production"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        text = state.text

        core_matches = [kw for kw in CORE_PROD if re.search(r"\b" + re.escape(kw) + r"\b", text, re.IGNORECASE)]
        support_matches = [kw for kw in SUPPORT_PROD if re.search(r"\b" + re.escape(kw) + r"\b", text, re.IGNORECASE)]

        core_score = min(1.0, len(core_matches) / 2.0)
        support_score = min(1.0, len(support_matches) / 3.0)
        raw_score = 0.7 * core_score + 0.3 * support_score

        evidence = []
        for kw in core_matches:
            evidence.append(EvidenceItem(
                source="production",
                value=kw,
                confidence=1.0,
                metadata={"tier": "core"}
            ))
        for kw in support_matches:
            evidence.append(EvidenceItem(
                source="production",
                value=kw,
                confidence=0.5,
                metadata={"tier": "support"}
            ))

        return FeatureResult(
            name=self.name,
            raw_score=raw_score,
            normalized_score=raw_score,
            evidence=evidence,
        )