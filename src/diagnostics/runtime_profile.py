"""Runtime profiling helpers."""

from __future__ import annotations

from src.pipeline.metrics import throughput


def runtime_profile(count: int, elapsed_seconds: float) -> dict[str, float]:
    return {
        "count": float(count),
        "elapsed_seconds": elapsed_seconds,
        "throughput_per_second": throughput(count, elapsed_seconds),
    }


__all__ = ["runtime_profile"]
