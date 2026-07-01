# src/pipeline/sorting.py
from __future__ import annotations
from src.models.candidate_state import CandidateState

def submission_score(state: CandidateState) -> float:
    return round(state.final_score or 0.0, 4)

def sort_candidates(states: list[CandidateState]) -> list[CandidateState]:
    return sorted(
        states,
        key=lambda s: (
            -submission_score(s),                 # primary: highest rounded score
            -(s.score_breakdown.fine_score or 0.0), # secondary: highest fine_score
            s.candidate_id,                       # tertiary: ascending ID (deterministic)
        ),
    )