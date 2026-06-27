"""Feature-level aggregate statistics."""

from __future__ import annotations

from statistics import mean


def feature_statistics(states) -> dict[str, dict[str, float]]:
    buckets: dict[str, list[float]] = {}
    for state in states:
        for name, result in state.features.items():
            buckets.setdefault(name, []).append(result.normalized_score)
    return {
        name: {
            "count": float(len(scores)),
            "mean": mean(scores) if scores else 0.0,
            "min": min(scores) if scores else 0.0,
            "max": max(scores) if scores else 0.0,
        }
        for name, scores in sorted(buckets.items())
    }


__all__ = ["feature_statistics"]
