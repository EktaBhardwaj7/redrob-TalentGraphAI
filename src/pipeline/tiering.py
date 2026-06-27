# tiering.py
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext


def assign_tier(state: CandidateState, context: RankingContext) -> str:
    score = state.final_score
    if score is None:
        return "D"

    thresholds = context.tier_thresholds
    for tier, cutoff in sorted(thresholds.items(), key=lambda x: x[1], reverse=True):
        if score >= cutoff:
            return tier
    return "D"