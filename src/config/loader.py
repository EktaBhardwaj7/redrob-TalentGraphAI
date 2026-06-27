# loader.py
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, FrozenSet

from .ontology import EVIDENCE_MAP, REQUIRED_CAPS, PREFERRED_CAPS, ALL_CAPS
from .scoring_v1 import (
    VERSION,
    FEATURE_WEIGHTS,
    FEATURE_ORDER,
    PENALTIES,
    EXPERIENCE_TARGET,
    ExperienceTarget,
)
from .thresholds import TIER_THRESHOLDS
from .runtime import BATCH_SIZE, MAX_WORKERS, ENABLE_CACHE, OUTPUT_DIR
from .keywords import REQUIRED_KEYWORDS, PREFERRED_KEYWORDS


@dataclass(frozen=True)
class RankingConfig:
    version: str
    evidence_map: Dict[str, Any]
    required_caps: list[str]
    preferred_caps: list[str]
    all_caps: FrozenSet[str]
    feature_order: list[str]
    feature_weights: dict[str, float]
    penalties: dict[str, float]
    tier_thresholds: dict[str, float]
    experience_target: ExperienceTarget
    batch_size: int
    max_workers: int
    enable_cache: bool
    output_dir: Path
    required_keywords: list[str]
    preferred_keywords: list[str]


def load_config(version: str = "v1") -> RankingConfig:
    if version != "v1":
        raise ValueError(f"Unknown config version: {version}")

    # Validate feature weights sum to 1.0
    total = sum(FEATURE_WEIGHTS.values())
    if abs(total - 1.0) > 1e-6:
        raise ValueError(f"Feature weights must sum to 1.0 (got {total:.3f})")

    # Validate tier thresholds are descending
    sorted_thresholds = sorted(TIER_THRESHOLDS.values(), reverse=True)
    if list(TIER_THRESHOLDS.values()) != sorted_thresholds:
        raise ValueError("Tier thresholds must be descending")

    # Validate feature weight/order alignment
    weight_names = set(FEATURE_WEIGHTS.keys())
    order_names = set(FEATURE_ORDER)
    if weight_names != order_names:
        missing_in_order = weight_names - order_names
        missing_in_weights = order_names - weight_names
        errors = []
        if missing_in_order:
            errors.append(f"Features with weights but no order: {missing_in_order}")
        if missing_in_weights:
            errors.append(f"Features in order but no weight: {missing_in_weights}")
        raise ValueError("Feature weight/order mismatch: " + "; ".join(errors))

    # Validate all capabilities used in evidence are declared
    used_caps = set()
    for rule in EVIDENCE_MAP.values():
        used_caps.update(rule.capabilities)
    undeclared = used_caps - set(ALL_CAPS)
    if undeclared:
        raise ValueError(f"Undeclared capabilities in ontology: {undeclared}")

    return RankingConfig(
        version=VERSION,
        evidence_map=EVIDENCE_MAP,
        required_caps=REQUIRED_CAPS,
        preferred_caps=PREFERRED_CAPS,
        all_caps=ALL_CAPS,
        feature_order=FEATURE_ORDER,
        feature_weights=FEATURE_WEIGHTS,
        penalties=PENALTIES,
        tier_thresholds=TIER_THRESHOLDS,
        experience_target=EXPERIENCE_TARGET,
        batch_size=BATCH_SIZE,
        max_workers=MAX_WORKERS,
        enable_cache=ENABLE_CACHE,
        output_dir=OUTPUT_DIR,
        required_keywords=REQUIRED_KEYWORDS,
        preferred_keywords=PREFERRED_KEYWORDS,
    )