# src/features/honeypot.py
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature

@register_feature
class HoneypotFeature(Feature):
    name = "honeypot"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        warnings = []
        penalty = 0.0
        raw = state.raw

        # 1. Check career total vs years_of_experience
        exp_years = raw.get("profile", {}).get("years_of_experience", 0)
        total_months = 0
        career = raw.get("career_history", [])
        for entry in career:
            dur = entry.get("duration_months", 0)
            total_months += dur
        if exp_years > 0 and total_months > 0:
            ratio = total_months / (exp_years * 12)
            if ratio < 0.8 or ratio > 1.2:
                warnings.append(f"Experience mismatch: {exp_years} years vs. {total_months//12} months career")
                penalty += 0.15

        # 2. Check expert skills with low duration
        expert_short = 0
        for skill in raw.get("skills", []):
            if skill.get("proficiency") == "expert" and skill.get("duration_months", 0) < 12:
                expert_short += 1
        if expert_short >= 3:
            warnings.append(f"{expert_short} expert skills with < 12 months")
            penalty += 0.15

        # 3. Timeline inversions already in warnings
        if any("Timeline inversion" in w for w in state.warnings):
            warnings.append("Timeline inversion detected")
            penalty += 0.20

        # 4. Many skills, low endorsements
        skills = raw.get("skills", [])
        if len(skills) > 20:
            endorsements = sum(s.get("endorsements", 0) for s in skills)
            if endorsements / len(skills) < 1:
                warnings.append("Many skills but low endorsements")
                penalty += 0.10

        final_penalty = -min(0.30, penalty)
        evidence = [EvidenceItem(
            source="honeypot",
            value="; ".join(warnings) if warnings else "clean",
            confidence=1.0,
            metadata={"warnings": warnings}
        )]
        return FeatureResult(
            name=self.name,
            raw_score=final_penalty,
            normalized_score=final_penalty,
            evidence=evidence,
            warnings=warnings,
        )
