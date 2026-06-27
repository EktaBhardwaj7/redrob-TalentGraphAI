"""Ontology stress-test helpers."""


def ontology_stress(context) -> dict[str, int]:
    capability_counts: dict[str, int] = {}
    for rule in context.evidence_map.values():
        for capability in rule.capabilities:
            capability_counts[capability] = capability_counts.get(capability, 0) + 1
    return dict(sorted(capability_counts.items()))


__all__ = ["ontology_stress"]
