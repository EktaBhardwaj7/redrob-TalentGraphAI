# preferred.py
import re
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class PreferredFeature(Feature):
    name = "preferred_match"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        text = state.text
        preferred_caps = context.preferred_capabilities
        matched = []
        for cap in preferred_caps:
            for phrase, rule in context.evidence_map.items():
                if cap in rule.capabilities:
                    if phrase in state.matched_evidence:
                        matched.append((phrase, rule.weight))
                        break

        if not matched:
            score = 0.0
        else:
            score = min(1.0, len(matched) / len(preferred_caps))

        evidence = [
            EvidenceItem(
                source="jd",
                value=f"{len(matched)}/{len(preferred_caps)} preferred",
                confidence=score,
                metadata={"matched": [m[0] for m in matched]}
            )
        ]

        return FeatureResult(
            name=self.name,
            raw_score=score,
            normalized_score=score,
            evidence=evidence,
        )