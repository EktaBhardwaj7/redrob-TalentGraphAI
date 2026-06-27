"""Score distribution summaries."""

from __future__ import annotations

from statistics import mean, median


def score_distribution(states) -> dict[str, float]:
    scores = [state.final_score or 0.0 for state in states]
    if not scores:
        return {"count": 0.0, "min": 0.0, "max": 0.0, "mean": 0.0, "median": 0.0}
    return {
        "count": float(len(scores)),
        "min": min(scores),
        "max": max(scores),
        "mean": mean(scores),
        "median": median(scores),
    }


__all__ = ["score_distribution"]
