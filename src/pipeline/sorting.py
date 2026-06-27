"""Deterministic ranking sort helpers."""

from __future__ import annotations

from src.models.candidate_state import CandidateState

TIER_ORDER = {"A+": 5, "A": 4, "B": 3, "C": 2, "D": 1}


def submission_score(state: CandidateState) -> float:
    return round(state.final_score or 0.0, 4)


def sort_candidates(states: list[CandidateState]) -> list[CandidateState]:
    return sorted(
        states,
        key=lambda state: (
            -submission_score(state),
            state.candidate_id,
        ),
    )


__all__ = ["TIER_ORDER", "sort_candidates", "submission_score"]
