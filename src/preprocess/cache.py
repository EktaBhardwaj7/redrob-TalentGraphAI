"""Tiny pickle cache helpers for preprocessing artifacts."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any


def load_cache(path: str | Path, default: Any = None) -> Any:
    cache_path = Path(path)
    if not cache_path.exists():
        return default
    with cache_path.open("rb") as handle:
        return pickle.load(handle)


def save_cache(path: str | Path, value: Any) -> None:
    cache_path = Path(path)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("wb") as handle:
        pickle.dump(value, handle)


__all__ = ["load_cache", "save_cache"]
