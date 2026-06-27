# regex.py
import re

EMAIL_RE = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    re.IGNORECASE,
)

PHONE_RE = re.compile(
    r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}"
)

URL_RE = re.compile(r"https?://[^\s]+", re.IGNORECASE)

LINKEDIN_RE = re.compile(
    r"https?://(?:www\.)?linkedin\.com/[^\s]+",
    re.IGNORECASE,
)

GITHUB_RE = re.compile(
    r"https?://(?:www\.)?github\.com/[A-Za-z0-9_.-]+/?",
    re.IGNORECASE,
)

YEARS_EXPERIENCE_RE = re.compile(
    r"(\d+(?:\.\d+)?)\s*(?:\+)?\s*(?:years?|yrs?)",
    re.IGNORECASE,
)

VERSION_RE = re.compile(r"\b\d+(?:\.\d+){1,3}\b")

WORD_RE = re.compile(r"\b\w+\b")
WHITESPACE_RE = re.compile(r"\s+")


def find_email(text: str) -> str | None:
    match = EMAIL_RE.search(text)
    return match.group(0) if match else None


def find_phone(text: str) -> str | None:
    match = PHONE_RE.search(text)
    return match.group(0) if match else None


def find_linkedin(text: str) -> str | None:
    match = LINKEDIN_RE.search(text)
    return match.group(0) if match else None


def find_github(text: str) -> str | None:
    match = GITHUB_RE.search(text)
    return match.group(0) if match else None


def find_urls(text: str) -> list[str]:
    return URL_RE.findall(text)


def extract_years(text: str) -> list[float]:
    return [float(x) for x in YEARS_EXPERIENCE_RE.findall(text)]


def has_email(text: str) -> bool:
    return EMAIL_RE.search(text) is not None


def has_phone(text: str) -> bool:
    return PHONE_RE.search(text) is not None


def has_github(text: str) -> bool:
    return GITHUB_RE.search(text) is not None


def has_linkedin(text: str) -> bool:
    return LINKEDIN_RE.search(text) is not None


__all__ = [
    "EMAIL_RE",
    "PHONE_RE",
    "URL_RE",
    "LINKEDIN_RE",
    "GITHUB_RE",
    "YEARS_EXPERIENCE_RE",
    "VERSION_RE",
    "WORD_RE",
    "WHITESPACE_RE",
    "find_email",
    "find_phone",
    "find_linkedin",
    "find_github",
    "find_urls",
    "extract_years",
    "has_email",
    "has_phone",
    "has_github",
    "has_linkedin",
]