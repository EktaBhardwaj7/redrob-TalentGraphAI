#!/usr/bin/env python3
"""Run a small deterministic benchmark for the ranking engine."""

from __future__ import annotations

import argparse
import time
from pathlib import Path

from src.common.streaming import stream_candidates
from src.config.loader import load_config
from src.context import build_context
from src.engine import RankingEngine
from src.pipeline.metrics import throughput


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark TalentGraph AI ranking throughput.")
    parser.add_argument("--candidates", default="data/raw/candidates/candidates.jsonl")
    parser.add_argument("--jd", default="data/processed/parsed_jd.json")
    parser.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()

    jd_text = Path(args.jd).read_text(encoding="utf-8") if Path(args.jd).exists() else ""
    engine = RankingEngine(build_context(jd_text, load_config("v1")))

    start = time.perf_counter()
    count = 0
    def limited():
        nonlocal count
        for candidate in stream_candidates(args.candidates):
            if count >= args.limit:
                break
            count += 1
            yield candidate

    results = engine.rank(limited())
    elapsed = time.perf_counter() - start
    print(f"processed={count} retained={len(results)} elapsed_seconds={elapsed:.3f} throughput_per_second={throughput(count, elapsed):.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
