"""Compile evidence phrases into reusable regular expressions."""

from __future__ import annotations

import re
from typing import Mapping, Pattern


def compile_patterns(evidence_map: Mapping[str, object]) -> dict[str, Pattern[str]]:
    return {
        phrase: re.compile(r"\b" + re.escape(phrase) + r"\b", re.IGNORECASE)
        for phrase in evidence_map
    }


__all__ = ["compile_patterns"]
