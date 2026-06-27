"""Feature importance approximations from configured weights and observed scores."""

from __future__ import annotations

from statistics import mean


def feature_importance(states, weights: dict[str, float] | None = None) -> dict[str, float]:
    weights = weights or {}
    buckets: dict[str, list[float]] = {}
    for state in states:
        for name, result in state.features.items():
            buckets.setdefault(name, []).append(result.normalized_score)
    return {
        name: (mean(scores) if scores else 0.0) * weights.get(name, 1.0)
        for name, scores in sorted(buckets.items())
    }


__all__ = ["feature_importance"]
