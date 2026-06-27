# submission_validator.py
import csv
from typing import Tuple, List


def validate_submission(path: str, expected_rows: int = 100) -> Tuple[bool, List[str]]:
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except Exception as e:
        return False, [f"File error: {e}"]

    if len(rows) != expected_rows:
        errors.append(f"Expected {expected_rows} rows, got {len(rows)}")

    ranks = set()
    ids = set()
    scores = []

    for i, row in enumerate(rows, start=1):
        if "candidate_id" not in row:
            errors.append(f"Row {i}: missing candidate_id")
        if "rank" not in row:
            errors.append(f"Row {i}: missing rank")
        else:
            try:
                rank = int(row["rank"])
                if rank < 1 or rank > expected_rows:
                    errors.append(f"Row {i}: rank {rank} out of range")
                if rank in ranks:
                    errors.append(f"Row {i}: duplicate rank {rank}")
                ranks.add(rank)
            except ValueError:
                errors.append(f"Row {i}: invalid rank '{row['rank']}'")

        if "score" not in row:
            errors.append(f"Row {i}: missing score")
        else:
            try:
                scores.append(float(row["score"]))
            except ValueError:
                errors.append(f"Row {i}: invalid score '{row['score']}'")

        cid = row.get("candidate_id", "")
        if cid in ids:
            errors.append(f"Row {i}: duplicate candidate_id {cid}")
        ids.add(cid)

        if not row.get("reasoning", "").strip():
            errors.append(f"Row {i}: empty reasoning")

    if scores and scores != sorted(scores, reverse=True):
        errors.append("Scores are not monotonically non-increasing")

    if ranks != set(range(1, expected_rows + 1)):
        errors.append(f"Ranks do not cover 1..{expected_rows} exactly")

    return len(errors) == 0, errors
