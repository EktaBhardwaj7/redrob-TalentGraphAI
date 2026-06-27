"""Capability necessity diagnostics."""


def missing_required_capabilities(context, state) -> list[str]:
    seen = set()
    for evidence in state.matched_evidence.values():
        seen.update(evidence.metadata.get("capabilities", []))
    return [capability for capability in context.required_capabilities if capability not in seen]


__all__ = ["missing_required_capabilities"]
