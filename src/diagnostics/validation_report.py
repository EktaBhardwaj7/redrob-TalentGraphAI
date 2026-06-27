"""Validation report helpers."""


def validation_report(states) -> dict[str, object]:
    warnings = sum(len(state.warnings) for state in states)
    return {
        "count": len(states),
        "warning_count": warnings,
        "candidates_with_warnings": sum(1 for state in states if state.warnings),
    }


__all__ = ["validation_report"]
