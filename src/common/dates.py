# dates.py
from datetime import date, datetime
from typing import Optional
from dateutil import parser

_PRESENT_WORDS = {
    "present",
    "current",
    "now",
    "ongoing",
    "today",
}


def parse_date(value: str | None) -> Optional[date]:
    if not value:
        return None
    value = value.strip().lower()
    if value in _PRESENT_WORDS:
        return date.today()
    try:
        return parser.parse(value, fuzzy=True, default=datetime(1900, 1, 1)).date()
    except (ValueError, TypeError):
        return None


def months_between(start: date | None, end: date | None) -> int:
    if not start or not end:
        return 0
    months = (end.year - start.year) * 12
    months += end.month - start.month
    return max(months, 0)


def years_between(start: date | None, end: date | None) -> float:
    return round(months_between(start, end) / 12, 2)


def is_present(value: str | None) -> bool:
    if not value:
        return False
    return value.strip().lower() in _PRESENT_WORDS


__all__ = [
    "parse_date",
    "months_between",
    "years_between",
    "is_present",
]