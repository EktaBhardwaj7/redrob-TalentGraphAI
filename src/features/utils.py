"""Shared helpers for feature implementations."""

from __future__ import annotations


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def ratio(count: int, target: float) -> float:
    if target <= 0:
        return 0.0
    return clamp01(count / target)


__all__ = ["clamp01", "ratio"]
