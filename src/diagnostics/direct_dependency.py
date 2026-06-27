"""Direct dependency diagnostics."""


def direct_dependency_report(context) -> dict[str, list[str]]:
    direct = {}
    for phrase, rule in context.evidence_map.items():
        if getattr(rule, "weight", 0.0) >= 1.0:
            for capability in rule.capabilities:
                direct.setdefault(capability, []).append(phrase)
    return {capability: sorted(phrases) for capability, phrases in sorted(direct.items())}


__all__ = ["direct_dependency_report"]
