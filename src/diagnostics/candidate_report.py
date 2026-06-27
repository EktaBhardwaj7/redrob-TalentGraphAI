"""Candidate-level diagnostics."""


def candidate_report(state) -> dict[str, object]:
    return {
        "candidate_id": state.candidate_id,
        "tier": state.tier,
        "score": state.final_score,
        "feature_count": len(state.features),
        "evidence_count": len(state.matched_evidence),
        "warnings": list(state.warnings),
    }


__all__ = ["candidate_report"]
