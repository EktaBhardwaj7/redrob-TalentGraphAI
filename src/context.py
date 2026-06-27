import re
from typing import Optional

from src.models.ranking_context import RankingContext
from src.config.loader import RankingConfig, load_config


def build_context(jd_text: str | RankingConfig = "", config: Optional[RankingConfig] = None) -> RankingContext:
    """Build an immutable ranking context.

    Accepts both ``build_context(config)`` and ``build_context(jd_text, config)``
    so older scripts and the final CLI layout can share the same entrypoint.
    """
    if isinstance(jd_text, RankingConfig):
        config = jd_text
        jd_text = ""
    if config is None:
        config = load_config("v1")

    compiled = {}
    for phrase in config.evidence_map.keys():
        compiled[phrase] = re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)

    return RankingContext(
        jd_text=str(jd_text or ""),
        required_capabilities=config.required_caps,
        preferred_capabilities=config.preferred_caps,
        evidence_map=config.evidence_map,
        feature_order=config.feature_order,
        feature_weights=config.feature_weights,
        tier_thresholds=config.tier_thresholds,
        experience_target=config.experience_target,
        compiled_patterns=compiled,
        capability_weights={cap: 1.0 for cap in config.required_caps}
        | {cap: 0.5 for cap in config.preferred_caps},
    )
