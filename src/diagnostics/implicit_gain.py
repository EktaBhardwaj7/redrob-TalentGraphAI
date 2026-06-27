"""Implicit evidence diagnostics."""


def implicit_gain(context, states) -> dict[str, float]:
    implicit_phrases = {
        phrase for phrase, rule in context.evidence_map.items() if getattr(rule, "weight", 0.0) < 0.5
    }
    matched = sum(1 for state in states for phrase in state.matched_evidence if phrase in implicit_phrases)
    return {"implicit_matches": float(matched)}


__all__ = ["implicit_gain"]
