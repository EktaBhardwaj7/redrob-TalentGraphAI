# score_breakdown.py
from dataclasses import dataclass
from .feature_result import FeatureResult


@dataclass(frozen=True)
class ScoreBreakdown:
    feature_results: dict[str, FeatureResult]
    tier_score: float
    fine_score: float
    penalties: float
    final_score: float