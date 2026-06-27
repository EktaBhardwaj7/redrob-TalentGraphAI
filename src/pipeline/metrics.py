"""Lightweight ranking and runtime metrics."""

from __future__ import annotations

from statistics import mean

from src.models.candidate_state import CandidateState


def throughput(count: int, elapsed_seconds: float) -> float:
    return count / elapsed_seconds if elapsed_seconds > 0 else 0.0


def average_score(states: list[CandidateState]) -> float:
    scores = [state.final_score or 0.0 for state in states]
    return mean(scores) if scores else 0.0


__all__ = ["average_score", "throughput"]
