# hireability.py
from src.models.feature_result import FeatureResult
from src.models.evidence_item import EvidenceItem
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from .base import Feature
from .registry import register_feature


@register_feature
class HireabilityFeature(Feature):
    name = "hireability"

    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        signals = state.raw.get("redrob_signals", {})
        response_rate = signals.get("recruiter_response_rate", 0)
        interview_rate = signals.get("interview_completion_rate", 0)
        open_to_work = 1.0 if signals.get("open_to_work_flag") else 0.0
        notice_days = signals.get("notice_period_days", 90)

        if notice_days <= 30:
            notice_score = 1.0
        elif notice_days <= 60:
            notice_score = 0.5
        elif notice_days <= 90:
            notice_score = 0.2
        else:
            notice_score = 0.0

        raw_score = 0.4 * response_rate + 0.3 * interview_rate + 0.2 * open_to_work + 0.1 * notice_score
        score = max(0.0, min(1.0, raw_score))

        evidence = [
            EvidenceItem(
                source="redrob_signals",
                value=f"response_rate={response_rate:.2f}",
                confidence=response_rate,
            ),
            EvidenceItem(
                source="redrob_signals",
                value=f"notice_period={notice_days}d",
                confidence=notice_score,
            ),
        ]
        if open_to_work:
            evidence.append(EvidenceItem(
                source="redrob_signals",
                value="open_to_work",
                confidence=1.0,
            ))

        return FeatureResult(
            name=self.name,
            raw_score=raw_score,
            normalized_score=score,
            evidence=evidence,
        )