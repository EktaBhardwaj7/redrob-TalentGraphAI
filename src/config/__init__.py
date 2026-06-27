# config/__init__.py
from .loader import load_config, RankingConfig
from .ontology import (
    EVIDENCE_MAP,
    REQUIRED_CAPS,
    PREFERRED_CAPS,
    ALL_CAPS,
    EvidenceRule,
    DIRECT,
    RELATED,
    IMPLICIT,
)
from .scoring_v1 import (
    VERSION,
    FEATURE_ORDER,
    TIER_WEIGHTS,
    FINE_WEIGHTS,
    FEATURE_WEIGHTS,
    PENALTIES,
    EXPERIENCE_TARGET,
    ExperienceTarget,
    SCORING_CONFIG,
)
from .thresholds import TIER_THRESHOLDS
from .runtime import BATCH_SIZE, MAX_WORKERS, ENABLE_CACHE, OUTPUT_DIR
from .keywords import (
    REQUIRED_KEYWORDS,
    PREFERRED_KEYWORDS,
    PRODUCTION_CORE,
    PRODUCTION_SUPPORT,
)

__all__ = [
    "load_config",
    "RankingConfig",
    "EVIDENCE_MAP",
    "REQUIRED_CAPS",
    "PREFERRED_CAPS",
    "ALL_CAPS",
    "EvidenceRule",
    "DIRECT",
    "RELATED",
    "IMPLICIT",
    "VERSION",
    "FEATURE_ORDER",
    "TIER_WEIGHTS",
    "FINE_WEIGHTS",
    "FEATURE_WEIGHTS",
    "PENALTIES",
    "EXPERIENCE_TARGET",
    "ExperienceTarget",
    "SCORING_CONFIG",
    "TIER_THRESHOLDS",
    "BATCH_SIZE",
    "MAX_WORKERS",
    "ENABLE_CACHE",
    "OUTPUT_DIR",
    "REQUIRED_KEYWORDS",
    "PREFERRED_KEYWORDS",
    "PRODUCTION_CORE",
    "PRODUCTION_SUPPORT",
]