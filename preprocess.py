#!/usr/bin/env python3
"""Precompute lightweight artifacts used by the TalentGraph ranking pipeline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.context import build_context
from src.config.loader import load_config
from src.preprocess.compile_patterns import compile_patterns
from src.preprocess.parse_jd import parse_jd


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare TalentGraph AI preprocessing artifacts.")
    parser.add_argument("--jd", default="data/raw/jd/job_description.docx", help="Job description path")
    parser.add_argument("--out", default="data/processed/parsed_jd.json", help="Parsed JD output path")
    parser.add_argument("--config", default="v1", help="Configuration version")
    args = parser.parse_args()

    config = load_config(args.config)
    jd = parse_jd(args.jd)
    context = build_context(jd.get("text", ""), config)
    patterns = compile_patterns(context.evidence_map)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        json.dumps(
            {
                "source": args.jd,
                "capabilities": sorted(context.capability_weights),
                "evidence_patterns": len(patterns),
                **jd,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
