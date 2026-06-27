"""Reasoning templates used by the submission explanation layer."""

from __future__ import annotations

DEFAULT_REASON = "Candidate shows relevant evidence for the role."

TEMPLATES = {
    "jd_coverage": "Matched role capability evidence: {evidence}.",
    "production": "Production experience: {evidence}.",
    "experience_fit": "Profile: {evidence}.",
    "market_validation": "Market validation: {evidence}.",
    "hireability": "Hireability signal: {evidence}.",
    "preferred_match": "Preferred signal: {evidence}.",
    "consistency": "Profile consistency: {evidence}.",
}


def render_reason(feature_name: str, evidence: str) -> str:
    template = TEMPLATES.get(feature_name)
    if not template:
        return evidence or DEFAULT_REASON
    return template.format(evidence=evidence or "supporting evidence found")


__all__ = ["DEFAULT_REASON", "TEMPLATES", "render_reason"]
