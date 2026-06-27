# evidence_item.py
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class EvidenceItem:
    source: str
    value: str
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)


__all__ = ["EvidenceItem"]