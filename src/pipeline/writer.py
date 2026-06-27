# writer.py
import csv
from pathlib import Path
from typing import List
from src.models.candidate_state import CandidateState


def write_submission(states: List[CandidateState], path: str) -> None:
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["candidate_id", "rank", "score", "reasoning"])
        for i, state in enumerate(states, start=1):
            writer.writerow([
                state.candidate_id,
                i,
                f"{state.final_score:.4f}" if state.final_score is not None else "0.0000",
                state.reasoning or "",
            ])
