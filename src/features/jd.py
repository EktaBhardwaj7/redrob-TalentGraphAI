# jd.py
import re
from typing import Any, Dict

from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class JDFeature(Feature):
    name = "jd_coverage"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        required_caps = context.required_capabilities
        cap_scores = {cap: 0.0 for cap in required_caps}
        cap_evidences = {cap: [] for cap in required_caps}
        matched_evidence = []

        # Use pre-built evidence index from state
        for phrase, rule in context.evidence_map.items():
            if phrase in state.matched_evidence:
                matched_evidence.append((rule.weight, phrase, rule.capabilities))
                for cap in rule.capabilities:
                    if rule.weight > cap_scores[cap]:
                        cap_scores[cap] = rule.weight
                    cap_evidences[cap].append((phrase, rule.weight))

        coverage = sum(cap_scores.values()) / len(required_caps) if required_caps else 0.0
        total_weight = sum(w for w, _, _ in matched_evidence)
        confidence = min(1.0, total_weight / len(required_caps)) if required_caps else 0.0
        raw_score = 0.8 * coverage + 0.2 * confidence
        raw_score = max(0.0, min(1.0, raw_score))

        evidence_list = []
        matched_phrases = {phrase for values in cap_evidences.values() for phrase, _ in values}
        for phrase, rule in context.evidence_map.items():
            if phrase in matched_phrases:
                evidence_list.append(
                    EvidenceItem(
                        source="jd",
                        value=phrase,
                        confidence=rule.weight,
                        metadata={"capabilities": list(rule.capabilities)}
                    )
                )

        return FeatureResult(
            name=self.name,
            raw_score=raw_score,
            normalized_score=raw_score,
            confidence=confidence,
            evidence=evidence_list,
        )
