# candidate_state.py
from dataclasses import dataclass, field
from typing import Any, Optional
from .feature_result import FeatureResult
from .score_breakdown import ScoreBreakdown
from .evidence_item import EvidenceItem


@dataclass
class CandidateState:
    candidate_id: str
    raw: dict[str, Any]
    # Normalized data reused across features
    text: str = ""
    skills: list[str] = field(default_factory=list)
    titles: list[str] = field(default_factory=list)
    dates: list[tuple[str, str]] = field(default_factory=list)
    # Evidence cache
    matched_evidence: dict[str, EvidenceItem] = field(default_factory=dict)
    features: dict[str, FeatureResult] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    score_breakdown: Optional[ScoreBreakdown] = None
    tier: Optional[str] = None
    final_score: Optional[float] = None
    reasoning: Optional[str] = None

    def build_evidence_index(self, context) -> None:
        """Scan candidate text once and cache matched evidence."""
        if self.matched_evidence:
            return
        text = self.text
        for phrase, rule in context.evidence_map.items():
            if context.compiled_patterns[phrase].search(text):
                self.matched_evidence[phrase] = EvidenceItem(
                    source="profile",
                    value=phrase,
                    confidence=rule.weight,
                    metadata={"capabilities": list(rule.capabilities)}
                )