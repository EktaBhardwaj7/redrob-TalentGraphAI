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
    "jd_coverage": 0.30,
    "production": 0.25,
    "experience_fit": 0.08,
    "consistency": 0.07,
}

FINE_WEIGHTS = {
    "market_validation": 0.10,
    "hireability": 0.10,
    "preferred_match": 0.05,
}

FEATURE_WEIGHTS = {**TIER_WEIGHTS, **FINE_WEIGHTS}
FEATURE_WEIGHTS["penalties"] = 0.05
FEATURE_WEIGHTS["honeypot"] = 0.0

# Ensure sum = 1.0
assert abs(sum(FEATURE_WEIGHTS.values()) - 1.0) < 1e-6

PENALTIES = {"disqualifier": -0.20}

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