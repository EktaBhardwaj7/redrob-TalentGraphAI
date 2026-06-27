#!/usr/bin/env python3
# rank.py
import argparse
import logging
from pathlib import Path

from src.engine import RankingEngine
from src.context import build_context
from src.config.loader import load_config
from src.common.streaming import stream_candidates
from src.preprocess.parse_jd import parse_jd
from src.pipeline.writer import write_submission
from src.pipeline.submission_validator import validate_submission

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True, help="Path to candidates.jsonl.gz")
    parser.add_argument("--jd", default="data/raw/jd/job_description.docx", help="Path to JD file")
    parser.add_argument("--out", default="data/output/submission.csv", help="Output CSV path")
    parser.add_argument("--config", default="v1", help="Config version")
    parser.add_argument("--limit", type=int, help="Limit candidates (for testing)")
    args = parser.parse_args()

    config = load_config(args.config)
    jd_text = parse_jd(args.jd).get("text", "")
    context = build_context(jd_text, config)

    engine = RankingEngine(context)
    candidates = stream_candidates(args.candidates)
    if args.limit:
        import itertools
        candidates = itertools.islice(candidates, args.limit)

    results = engine.rank(candidates)
    write_submission(results, args.out)
    logger.info(f"Written {len(results)} candidates to {args.out}")

    expected_rows = min(args.limit, 100) if args.limit else 100
    valid, errors = validate_submission(args.out, expected_rows=expected_rows)
    if not valid:
        logger.error("Submission validation failed:")
        for e in errors:
            logger.error(f"  {e}")
        return 1

    logger.info("Submission validated successfully.")
    return 0


if __name__ == "__main__":
    exit(main())
