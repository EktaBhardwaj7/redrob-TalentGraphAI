"""Capability contribution diagnostics."""


def capability_contribution(states) -> dict[str, float]:
    totals: dict[str, float] = {}
    for state in states:
        for evidence in state.matched_evidence.values():
            for capability in evidence.metadata.get("capabilities", []):
                totals[capability] = totals.get(capability, 0.0) + evidence.confidence
    return dict(sorted(totals.items()))


__all__ = ["capability_contribution"]
