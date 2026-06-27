from src.config.loader import load_config
from src.context import build_context
from src.engine import RankingEngine


def test_engine_ranks_sample_candidates():
    context = build_context("machine learning retrieval ranking production", load_config("v1"))
    engine = RankingEngine(context)
    candidates = [
        {
            "candidate_id": "CAND_0000001",
            "profile": {
                "summary": "Built FAISS semantic search and production ML inference.",
                "years_of_experience": 6,
                "current_title": "Machine Learning Engineer",
            },
            "skills": [{"name": "FAISS"}, {"name": "Python"}],
            "career_history": [
                {
                    "title": "Machine Learning Engineer",
                    "description": "Deployed vector search and model serving.",
                    "duration_months": 24,
                }
            ],
        },
        {
            "candidate_id": "CAND_0000002",
            "profile": {
                "summary": "Marketing operations and customer support.",
                "years_of_experience": 3,
                "current_title": "Operations Manager",
            },
            "skills": [{"name": "Excel"}],
            "career_history": [
                {
                    "title": "Operations Manager",
                    "description": "Managed support operations.",
                    "duration_months": 24,
                }
            ],
        },
    ]

    ranked = engine.rank(iter(candidates))

    assert len(ranked) == 2
    assert ranked[0].candidate_id == "CAND_0000001"
    assert ranked[0].reasoning
