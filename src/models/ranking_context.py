# ranking_context.py
from dataclasses import dataclass, field
from typing import Pattern
import re


@dataclass(frozen=True)
class RankingContext:
    jd_text: str
    required_capabilities: list[str]
    preferred_capabilities: list[str]
    evidence_map: dict
    feature_order: list[str]
    feature_weights: dict[str, float]
    tier_thresholds: dict[str, float]
    experience_target: object
    capability_weights: dict[str, float] = field(default_factory=dict)
    compiled_patterns: dict[str, Pattern] = field(default_factory=dict)
    compiled_skill_patterns: dict[str, Pattern] = field(default_factory=dict)
    compiled_required_patterns: dict[str, Pattern] = field(default_factory=dict)
    compiled_preferred_patterns: dict[str, Pattern] = field(default_factory=dict)

    def __post_init__(self):
        patterns = dict(self.compiled_patterns)
        if not patterns:
            for phrase in self.evidence_map.keys():
                patterns[phrase] = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        object.__setattr__(self, "compiled_patterns", patterns)
        object.__setattr__(self, "compiled_skill_patterns", patterns)

        req_patterns = {}
        for phrase in self.required_capabilities:
            req_patterns[phrase] = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        object.__setattr__(self, "compiled_required_patterns", req_patterns)

        pref_patterns = {}
        for phrase in self.preferred_capabilities:
            pref_patterns[phrase] = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        object.__setattr__(self, "compiled_preferred_patterns", pref_patterns)

        if not self.capability_weights:
            weights = {cap: 1.0 for cap in self.required_capabilities}
            weights.update({cap: 0.5 for cap in self.preferred_capabilities})
            object.__setattr__(self, "capability_weights", weights)


__all__ = ["RankingContext"]
