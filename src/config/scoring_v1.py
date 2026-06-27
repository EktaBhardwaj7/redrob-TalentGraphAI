# scoring_v1.py
from dataclasses import dataclass

VERSION = "v1"

# Explicit order for feature execution (must match registered feature names)
FEATURE_ORDER = [
    "jd_coverage",
    "production",
    "experience_fit",
    "consistency",
    "market_validation",
    "hireability",
    "preferred_match",
    "penalties",
]

# Weights for tier assignment (primary ranking)
TIER_WEIGHTS = {
    "jd_coverage": 0.40,
    "production": 0.20,
    "experience_fit": 0.08,
    "consistency": 0.07,
}

# Weights for fine-grained ordering within tier
FINE_WEIGHTS = {
    "market_validation": 0.10,
    "hireability": 0.05,
    "preferred_match": 0.05,
}

FEATURE_WEIGHTS = {**TIER_WEIGHTS, **FINE_WEIGHTS}
FEATURE_WEIGHTS["penalties"] = 0.05

PENALTIES = {
    "disqualifier": -0.20,
}


@dataclass(frozen=True)
class ExperienceTarget:
    minimum: float
    ideal: float
    maximum: float


EXPERIENCE_TARGET = ExperienceTarget(minimum=3.0, ideal=7.0, maximum=12.0)

SCORING_CONFIG = {
    "tier": TIER_WEIGHTS,
    "fine": FINE_WEIGHTS,
    "penalties": PENALTIES,
    "order": FEATURE_ORDER,
}
