# market.py
import math
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class MarketFeature(Feature):
    name = "market_validation"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        signals = state.raw.get("redrob_signals", {})
        views = signals.get("profile_views_received_30d", 0)
        searches = signals.get("search_appearance_30d", 0)
        saves = signals.get("saved_by_recruiters_30d", 0)

        views_cap = 500
        searches_cap = 500
        saves_cap = 50

        views_norm = math.log1p(views) / math.log1p(views_cap)
        searches_norm = math.log1p(searches) / math.log1p(searches_cap)
        saves_norm = math.log1p(saves) / math.log1p(saves_cap)

        raw_score = 0.4 * views_norm + 0.3 * searches_norm + 0.3 * saves_norm
        score = max(0.0, min(1.0, raw_score))

        evidence = []
        if views > 0:
            evidence.append(EvidenceItem(
                source="redrob_signals",
                value=f"views={views}",
                confidence=min(1.0, views / views_cap),
                metadata={"type": "views"}
            ))
        if saves > 0:
            evidence.append(EvidenceItem(
                source="redrob_signals",
                value=f"saves={saves}",
                confidence=min(1.0, saves / saves_cap),
                metadata={"type": "saves"}
            ))

        return FeatureResult(
            name=self.name,
            raw_score=raw_score,
            normalized_score=score,
            evidence=evidence,
        )