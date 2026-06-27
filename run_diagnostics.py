#!/usr/bin/env python3
"""Generate a compact diagnostics report for a candidate ranking run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.common.streaming import stream_candidates
from src.config.loader import load_config
from src.context import build_context
from src.engine import RankingEngine
from src.diagnostics.feature_statistics import feature_statistics
from src.diagnostics.score_distribution import score_distribution


def main() -> int:
    parser = argparse.ArgumentParser(description="Run TalentGraph AI diagnostics.")
    parser.add_argument("--candidates", default="data/raw/candidates/candidates.jsonl")
    parser.add_argument("--jd", default="data/processed/parsed_jd.json")
    parser.add_argument("--out", default="data/output/diagnostics/report.json")
    parser.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()

    jd_text = Path(args.jd).read_text(encoding="utf-8") if Path(args.jd).exists() else ""
    engine = RankingEngine(build_context(jd_text, load_config("v1")))

    candidates = stream_candidates(args.candidates)
    if args.limit:
        import itertools

        candidates = itertools.islice(candidates, args.limit)

    states = engine.rank(candidates)
    report = {
        "count": len(states),
        "score_distribution": score_distribution(states),
        "feature_statistics": feature_statistics(states),
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
