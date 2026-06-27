# base.py
from abc import ABC, abstractmethod
from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from src.models.feature_result import FeatureResult


class Feature(ABC):
    name: str = "feature"

    @abstractmethod
    def compute(self, state: CandidateState, context: RankingContext) -> FeatureResult:
        pass