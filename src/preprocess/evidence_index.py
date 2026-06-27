"""Build per-candidate evidence indexes."""

from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext


def build_evidence_index(state: CandidateState, context: RankingContext) -> dict:
    """Populate and return the candidate's matched evidence map."""
    state.build_evidence_index(context)
    return state.matched_evidence


__all__ = ["build_evidence_index"]
