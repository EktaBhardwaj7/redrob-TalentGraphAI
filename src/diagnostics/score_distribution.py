# src/diagnostics/score_distribution.py

from __future__ import annotations
import json
from collections import Counter
from statistics import mean, median, stdev
from pathlib import Path
from typing import Any

def generate_full_report(states: list, context: Any, output_path: str) -> None:
    """
    Generate a diagnostic report of the ranking results and write to a JSON file.
    
    Args:
        states: List of CandidateState objects after ranking (already sorted).
        context: RankingContext (used for ontology info, optional).
        output_path: Path to write the JSON report.
    """
    if not states:
        # Write empty report
        report = {"error": "No candidates ranked"}
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        return

    scores = [s.final_score or 0.0 for s in states]
    tiers = [s.tier for s in states if s.tier]
    tier_counts = Counter(tiers)

    # Feature averages
    feature_names = set()
    for s in states:
        feature_names.update(s.features.keys())
    feature_averages = {}
    for name in sorted(feature_names):
        vals = [s.features[name].normalized_score for s in states if name in s.features]
        if vals:
            feature_averages[name] = {
                "mean": mean(vals),
                "median": median(vals),
                "min": min(vals),
                "max": max(vals),
            }

    # Score distribution with percentiles
    sorted_scores = sorted(scores)
    n = len(sorted_scores)

    def percentile(p: float) -> float:
        if n == 0:
            return 0.0
        idx = (p / 100) * (n - 1)
        floor = int(idx)
        ceil = min(floor + 1, n - 1)
        if floor == ceil:
            return float(sorted_scores[floor])
        # Linear interpolation
        return sorted_scores[floor] + (idx - floor) * (sorted_scores[ceil] - sorted_scores[floor])

    dist = {
        "count": n,
        "min": min(scores),
        "max": max(scores),
        "mean": mean(scores),
        "median": median(scores),
        "std": stdev(scores) if n > 1 else 0.0,
        "p25": percentile(25),
        "p75": percentile(75),
    }

    # Top 10 and bottom 10 candidates
    top10 = [(s.candidate_id, s.final_score) for s in states[:10]]
    bottom10 = [(s.candidate_id, s.final_score) for s in states[-10:]]

    # Check if honeypot feature exists
    honeypot_applied = any("honeypot" in s.features for s in states)

    report = {
        "score_distribution": dist,
        "tier_distribution": dict(tier_counts),
        "feature_averages": feature_averages,
        "top_10": top10,
        "bottom_10": bottom10,
        "honeypot_penalty_applied": honeypot_applied,
        "total_candidates_ranked": len(states),
        "ontology_required_capabilities": list(context.required_capabilities) if hasattr(context, "required_capabilities") else [],
        "ontology_preferred_capabilities": list(context.preferred_capabilities) if hasattr(context, "preferred_capabilities") else [],
    }

    # Ensure output directory exists
    out_path = Path(output_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)