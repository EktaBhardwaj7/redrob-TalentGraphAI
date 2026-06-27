"""Evidence exclusivity diagnostics."""


def multi_capability_evidence(context) -> dict[str, list[str]]:
    return {
        phrase: sorted(rule.capabilities)
        for phrase, rule in context.evidence_map.items()
        if len(rule.capabilities) > 1
    }


__all__ = ["multi_capability_evidence"]
