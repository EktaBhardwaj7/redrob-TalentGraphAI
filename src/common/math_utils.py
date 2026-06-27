# math_utils.py
import math
from typing import Iterable


def clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(minimum, min(value, maximum))


def normalize(value: float, minimum: float, maximum: float) -> float:
    if maximum <= minimum:
        return 0.0
    return clamp((value - minimum) / (maximum - minimum))


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Return numerator/denominator, or default if denominator is zero."""
    if denominator == 0:
        return default
    return numerator / denominator


def weighted_average(scores: Iterable[tuple[float, float]]) -> float:
    total_score = 0.0
    total_weight = 0.0
    for score, weight in scores:
        total_score += score * weight
        total_weight += weight
    return safe_divide(total_score, total_weight)


def bell_curve(value: float, center: float, spread: float) -> float:
    if spread <= 0:
        return 0.0
    exponent = -((value - center) ** 2) / (2 * spread**2)
    return math.exp(exponent)


def log_normalize(value: float, maximum: float) -> float:
    if value <= 0 or maximum <= 0:
        return 0.0
    return math.log1p(value) / math.log1p(maximum)


def cosine_similarity(vector_a: list[float], vector_b: list[float]) -> float:
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same length.")
    dot = sum(a * b for a, b in zip(vector_a, vector_b))
    norm_a = math.sqrt(sum(a * a for a in vector_a))
    norm_b = math.sqrt(sum(b * b for b in vector_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


__all__ = [
    "clamp",
    "normalize",
    "safe_divide",
    "weighted_average",
    "bell_curve",
    "log_normalize",
    "cosine_similarity",
]