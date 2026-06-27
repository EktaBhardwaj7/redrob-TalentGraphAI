"""Ontology coverage report helpers."""


def ontology_report(context, states=None) -> dict[str, object]:
    matched = set()
    for state in states or []:
        matched.update(state.matched_evidence)
    return {
        "evidence_rule_count": len(context.evidence_map),
        "required_capabilities": list(context.required_capabilities),
        "preferred_capabilities": list(context.preferred_capabilities),
        "matched_evidence_count": len(matched),
    }


__all__ = ["ontology_report"]
