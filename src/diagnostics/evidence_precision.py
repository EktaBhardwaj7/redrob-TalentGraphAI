"""Evidence precision placeholders for manual audits."""


def evidence_precision_sample(states, limit: int = 20) -> list[dict[str, object]]:
    rows = []
    for state in states[:limit]:
        rows.append(
            {
                "candidate_id": state.candidate_id,
                "evidence": sorted(state.matched_evidence),
            }
        )
    return rows


__all__ = ["evidence_precision_sample"]
