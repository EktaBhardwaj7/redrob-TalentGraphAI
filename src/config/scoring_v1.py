from dataclasses import dataclass

VERSION = "v1"

FEATURE_ORDER = [
    "jd_coverage",
    "production",
    "experience_fit",
    "consistency",
    "market_validation",
    "hireability",
    "preferred_match",
    "penalties",
    "honeypot",
]

TIER_WEIGHTS = {
    "jd_coverage": 0.40,
    "production": 0.20,
    "experience_fit": 0.08,
    "consistency": 0.07,
}

FINE_WEIGHTS = {
    "market_validation": 0.10,
    "hireability": 0.05,
    "preferred_match": 0.05,
}

FEATURE_WEIGHTS = {**TIER_WEIGHTS, **FINE_WEIGHTS}
FEATURE_WEIGHTS["penalties"] = 0.05
FEATURE_WEIGHTS["honeypot"] = 0.0   # dummy weight, used separately for penalty

assert abs(sum(FEATURE_WEIGHTS.values()) - 1.0) < 1e-6, "Weights must sum to 1.0"

PENALTIES = {"disqualifier": -0.20}

@dataclass(frozen=True)
class ExperienceTarget:
    minimum: float
    ideal: float
    maximum: float

EXPERIENCE_TARGET = ExperienceTarget(minimum=4.0, ideal=7.0, maximum=9.0)

SCORING_CONFIG = {
    "tier": TIER_WEIGHTS,
    "fine": FINE_WEIGHTS,
    "penalties": PENALTIES,
    "order": FEATURE_ORDER,
}
