# consistency.py
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class ConsistencyFeature(Feature):
    name = "consistency"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        warnings = []
        score = 1.0

        if not state.skills:
            warnings.append("No skills listed")
            score -= 0.1

        if not state.titles:
            warnings.append("No career history")
            score -= 0.1

        # Short tenures
        history = state.raw.get("career_history", [])
        short_tenures = sum(1 for e in history if e.get("duration_months", 0) < 6)
        if history and short_tenures > len(history) / 2:
            warnings.append("Many short tenures")
            score -= 0.1

        # Title-skill mismatch
        title = state.raw.get("profile", {}).get("current_title", "").lower()
        has_ml_skill = any(
            skill in ["machine learning", "ml", "deep learning", "nlp", "pytorch", "tensorflow"]
            for skill in state.skills
        )
        if has_ml_skill and "engineer" not in title and "scientist" not in title:
            warnings.append("ML skills but non-technical title")
            score -= 0.05

        exp_years = state.raw.get("profile", {}).get("years_of_experience", 0)
        if exp_years > 40:
            warnings.append("Suspiciously high experience")
            score -= 0.1

        score = max(0.0, min(1.0, score))

        evidence = [
            EvidenceItem(
                source="consistency",
                value="; ".join(warnings) if warnings else "consistent",
                confidence=score,
                metadata={"warnings": warnings}
            )
        ]

        return FeatureResult(
            name=self.name,
            raw_score=score,
            normalized_score=score,
            evidence=evidence,
            warnings=warnings,
        )
