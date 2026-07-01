# ranking.py
from typing import Dict, Any
from src.models.candidate_state import CandidateState
from src.models.score_breakdown import ScoreBreakdown
from src.models.ranking_context import RankingContext


def compute_tier_score(state: CandidateState, context: RankingContext) -> float:
    """Score used for tier assignment (primary)."""
    weights = context.feature_weights
    tier_features = ["jd_coverage", "production", "experience_fit", "consistency"]
    total_weighted = 0.0
    total_weight = 0.0

    for name in tier_features:
        result = state.features.get(name)
        if result is None:
            continue
        weight = weights.get(name, 0.0)
        if weight > 0:
            total_weighted += result.normalized_score * weight
            total_weight += weight

    return total_weighted / total_weight if total_weight > 0 else 0.0


def compute_fine_score(state: CandidateState, context: RankingContext) -> float:
    """Score used to order candidates within the same tier."""
    weights = context.feature_weights
    fine_features = ["market_validation", "hireability", "preferred_match"]
    total_weighted = 0.0
    total_weight = 0.0

    for name in fine_features:
        result = state.features.get(name)
        if result is None:
            continue
        weight = weights.get(name, 0.0)
        if weight > 0:
            total_weighted += result.normalized_score * weight
            total_weight += weight

    return total_weighted / total_weight if total_weight > 0 else 0.0


def compute_final_state(state: CandidateState, context: RankingContext) -> ScoreBreakdown:
    tier_score = compute_tier_score(state, context)
    fine_score = compute_fine_score(state, context)

    # Get penalties from the dedicated feature
    penalty_feature = state.features.get("penalties")
    penalties = penalty_feature.normalized_score if penalty_feature else 0.0

    # Get honeypot penalty
    honeypot_feature = state.features.get("honeypot")
    honeypot_penalty = honeypot_feature.normalized_score if honeypot_feature else 0.0

    # Combine penalties (both are already negative)
    total_penalty = penalties + honeypot_penalty

    final_score = max(0.0, min(1.0, tier_score + total_penalty))
    return ScoreBreakdown(
        feature_results=state.features,
        tier_score=tier_score,
        fine_score=fine_score,
        penalties=total_penalty,           # store combined penalty
        final_score=final_score,
    )