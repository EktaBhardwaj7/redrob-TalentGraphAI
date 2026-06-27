"""Export ranking states to serializable dictionaries."""

from __future__ import annotations

from src.models.candidate_state import CandidateState


def export_states(states: list[CandidateState]) -> list[dict[str, object]]:
    rows = []
    for rank, state in enumerate(states, start=1):
        rows.append(
            {
                "candidate_id": state.candidate_id,
                "rank": rank,
                "score": round(state.final_score or 0.0, 6),
                "tier": state.tier or "D",
                "reasoning": state.reasoning or "",
            }
        )
    return rows


__all__ = ["export_states"]
