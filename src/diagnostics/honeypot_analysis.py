"""Honeypot and keyword-stuffing diagnostics."""


def honeypot_analysis(states) -> dict[str, int]:
    suspicious = 0
    for state in states:
        if len(state.matched_evidence) >= 12 and (state.final_score or 0.0) < 0.5:
            suspicious += 1
    return {"suspicious_candidates": suspicious}


__all__ = ["honeypot_analysis"]
