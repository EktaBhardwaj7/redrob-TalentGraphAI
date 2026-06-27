# engine.py
import heapq
import logging
from typing import List, Iterator, Dict, Any

from src.models.candidate_state import CandidateState
from src.models.ranking_context import RankingContext
from src.validation import normalize_and_validate
from src.features import create_features
from src.pipeline.ranking import compute_final_state
from src.pipeline.tiering import assign_tier
from src.pipeline.reasoning import generate_reasoning
from src.pipeline.sorting import sort_candidates

logger = logging.getLogger(__name__)


class RankingEngine:
    def __init__(self, context: RankingContext):
        self.context = context
        self.features = create_features(context.feature_order)

    def rank(self, candidates: Iterator[Dict[str, Any]]) -> List[CandidateState]:
        # Min-heap for top 100 (stores positive score; pops smallest)
        heap = []

        for raw in candidates:
            state = self._process_candidate(raw)
            if state is None:
                continue

            # Push positive score; heap pops the smallest (lowest score)
            heapq.heappush(heap, (state.final_score or 0.0, state.candidate_id, state))
            if len(heap) > 100:
                heapq.heappop(heap)

        states = [item[2] for item in heap]
        states = sort_candidates(states)

        # Generate reasoning for final output
        for state in states:
            state.reasoning = generate_reasoning(state)

        return states[:100]

    def _process_candidate(self, raw: Dict[str, Any]) -> CandidateState | None:
        cid = raw.get("candidate_id", "unknown")
        state = CandidateState(candidate_id=cid, raw=raw)

        # Normalize and validate
        validation_result = normalize_and_validate(raw, state)
        state.warnings.extend(validation_result.warnings)
        state.warnings.extend(validation_result.errors)

        if not validation_result.is_valid:
            logger.warning(f"Candidate {cid} failed validation: {validation_result.errors}")

        # Build evidence index once (scan text against ontology)
        state.build_evidence_index(self.context)

        # Compute features
        for feature in self.features:
            try:
                res = feature.compute(state, self.context)
                state.features[res.name] = res
                state.warnings.extend(res.warnings)
            except Exception as e:
                logger.warning(f"Feature {feature.name} failed for {cid}: {e}")
                from src.models.feature_result import FeatureResult
                state.features[feature.name] = FeatureResult(
                    name=feature.name,
                    raw_score=0.0,
                    normalized_score=0.0,
                    warnings=[str(e)],
                )

        # Compute final scores
        breakdown = compute_final_state(state, self.context)
        state.score_breakdown = breakdown
        state.final_score = breakdown.final_score
        state.tier = assign_tier(state, self.context)

        return state

    def run_diagnostics(self, candidates: Iterator[Dict[str, Any]]) -> dict:
        """Run diagnostics on the engine."""
        # Placeholder – to be implemented
        return {"status": "not implemented"}
