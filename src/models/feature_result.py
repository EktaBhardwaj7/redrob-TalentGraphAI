# feature_result.py
from dataclasses import dataclass, field
from .evidence_item import EvidenceItem


@dataclass(frozen=True)
class FeatureResult:
    name: str
    raw_score: float
    normalized_score: float
    confidence: float = 1.0
    evidence: list[EvidenceItem] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


__all__ = ["FeatureResult"]