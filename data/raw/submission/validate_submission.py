#!/usr/bin/env python3
"""Wrapper that correctly finds the project root and calls the internal validator."""

import sys
import os
from pathlib import Path

# Find the project root (where this script is located under data/raw/submission/)
# We go up 3 levels: data/raw/submission -> data/raw -> data -> project root
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent.parent  # go up 3 levels
sys.path.insert(0, str(project_root))

from src.pipeline.submission_validator import validate_submission

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_submission.py <csv_path>")
        sys.exit(1)

    csv_path = sys.argv[1]
    valid, errors = validate_submission(csv_path, expected_rows=100)

    if not valid:
        print("Validation failed:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    print("Submission is valid.")
    sys.exit(0)
