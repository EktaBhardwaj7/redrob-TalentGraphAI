import pytest
from src.config.loader import load_config
from src.context import build_context
from src.features.honeypot import HoneypotFeature
from src.models.candidate_state import CandidateState

def test_honeypot_detects_mismatch():
    config = load_config("v1")
    context = build_context("", config)
    candidate = {
        "candidate_id": "CAND_0000001",
        "profile": {"years_of_experience": 8},
        "career_history": [
            {"duration_months": 12, "company": "X", "start_date": "2020-01", "end_date": "2021-01"},
            {"duration_months": 12, "company": "Y", "start_date": "2021-02", "end_date": "2022-02"},
        ],
        "skills": [
            {"name": "Python", "proficiency": "expert", "duration_months": 6},
            {"name": "SQL", "proficiency": "expert", "duration_months": 4},
            {"name": "Java", "proficiency": "expert", "duration_months": 3},
        ]
    }
    state = CandidateState(candidate_id="CAND_0000001", raw=candidate)
    state.text = "some text"  # minimal
    feature = HoneypotFeature()
    result = feature.compute(state, context)
    # Should have warnings and a negative score
    assert result.warnings
    assert result.normalized_score < 0