#!/usr/bin/env bash
set -euo pipefail

python data/raw/submission/validate_submission.py "${1:-data/output/submission.csv}"
