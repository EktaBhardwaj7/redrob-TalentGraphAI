"""Simple ablation helpers for score sensitivity checks."""

from __future__ import annotations


def ablate_feature(states, feature_name: str) -> dict[str, float]:
    deltas = []
    for state in states:
        current = state.final_score or 0.0
        feature = state.features.get(feature_name)
        ablated = max(0.0, current - (feature.normalized_score if feature else 0.0))
        deltas.append(current - ablated)
    return {
        "feature": feature_name,
        "count": float(len(deltas)),
        "average_delta": sum(deltas) / len(deltas) if deltas else 0.0,
    }


__all__ = ["ablate_feature"]
