# timing.py
import time
from contextlib import contextmanager
from typing import Any


class Timer:
    """Simple timer for benchmarking."""

    def __init__(self):
        self.start_time = None
        self.elapsed = 0.0

    def start(self) -> None:
        self.start_time = time.perf_counter()

    def stop(self) -> float:
        if self.start_time is None:
            return 0.0
        self.elapsed = time.perf_counter() - self.start_time
        self.start_time = None
        return self.elapsed

    def reset(self) -> None:
        self.elapsed = 0.0
        self.start_time = None


@contextmanager
def timed_section(name: str):
    """Context manager to time a block of code."""
    timer = Timer()
    timer.start()
    yield
    elapsed = timer.stop()
    print(f"{name}: {elapsed:.4f}s")


__all__ = [
    "Timer",
    "timed_section",
]