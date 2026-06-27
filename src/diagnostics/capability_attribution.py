"""Capability attribution diagnostics."""


def capability_attribution(states) -> dict[str, int]:
    counts: dict[str, int] = {}
    for state in states:
        for evidence in state.matched_evidence.values():
            for capability in evidence.metadata.get("capabilities", []):
                counts[capability] = counts.get(capability, 0) + 1
    return dict(sorted(counts.items()))


__all__ = ["capability_attribution"]
