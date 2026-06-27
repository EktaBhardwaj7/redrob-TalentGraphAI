# experience.py
import math
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class ExperienceFeature(Feature):
    name = "experience_fit"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        years = state.raw.get("profile", {}).get("years_of_experience", 0)
        target = context.experience_target
        min_y, ideal, max_y = target.minimum, target.ideal, target.maximum

        if years <= 0:
            score = 0.0
        elif years < min_y:
            score = (years - 0) / (min_y - 0) if min_y > 0 else 0.0
        elif years <= max_y:
            spread = (max_y - min_y) / 3
            score = math.exp(-((years - ideal) ** 2) / (2 * spread ** 2))
        else:
            score = max(0.0, 1.0 - (years - max_y) / max_y)

        score = max(0.0, min(1.0, score))

        evidence = [
            EvidenceItem(
                source="profile",
                value=f"{years:.1f} years",
                confidence=1.0,
                metadata={"target": f"{ideal}"}
            )
        ]

        return FeatureResult(
            name=self.name,
            raw_score=score,
            normalized_score=score,
            evidence=evidence,
        )