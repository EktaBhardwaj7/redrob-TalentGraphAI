# validation_result.py
from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValidationResult:
    is_valid: bool
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


__all__ = ["ValidationResult"]