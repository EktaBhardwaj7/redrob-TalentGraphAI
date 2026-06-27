# io.py
import json
from pathlib import Path
from typing import Any


def read_json(path: str | Path) -> dict[str, Any]:
    """Read a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(data: dict[str, Any], path: str | Path, indent: int = 2) -> None:
    """Write a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, sort_keys=True)


def read_text(path: str | Path) -> str:
    """Read a text file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(content: str, path: str | Path) -> None:
    """Write a text file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


__all__ = [
    "read_json",
    "write_json",
    "read_text",
    "write_text",
]