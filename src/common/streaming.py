# streaming.py
import gzip
import json
import logging
from pathlib import Path
from typing import Iterator, Any

logger = logging.getLogger(__name__)


def stream_candidates(file_path: str | Path) -> Iterator[dict[str, Any]]:
    """Stream candidates from a JSONL or JSONL.GZ file, skipping malformed lines."""
    path = Path(file_path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                logger.warning(f"Skipping malformed JSON at line {line_num}: {e}")


__all__ = ["stream_candidates"]