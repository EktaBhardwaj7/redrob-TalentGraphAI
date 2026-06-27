# text.py
import re
import unicodedata
from typing import Iterable, Any

# Preserve programming-language punctuation: +, #, ., -, /
# We'll keep these in the text by not removing them.
# We remove other punctuation (e.g., commas, quotes, parentheses) but keep these.
# The regex below matches any character that is not a word character, not whitespace,
# and not one of the allowed punctuation characters.
# Allowed: letters, digits, underscore, plus, hash, dot, dash, slash.
# We'll use a character class: [^\w\s+#.\-/] – note the hyphen is escaped or placed at the end.
# Actually, we want to allow: alphanumeric, underscore, whitespace, +, #, ., -, /.
_PUNCT_RE = re.compile(r"[^\w\s+#.\-/]")
_MULTISPACE_RE = re.compile(r"\s+")


def normalize_text(text: str | None) -> str:
    """Normalize text for matching, preserving programming-language punctuation."""
    if not text:
        return ""
    text = unicodedata.normalize("NFKC", text)
    text = text.lower()
    # Remove unwanted punctuation but keep +, #, ., -, /
    text = _PUNCT_RE.sub(" ", text)
    text = _MULTISPACE_RE.sub(" ", text)
    return text.strip()


def clean_whitespace(text: str) -> str:
    return _MULTISPACE_RE.sub(" ", text).strip()


def tokenize(text: str) -> list[str]:
    normalized = normalize_text(text)
    return normalized.split() if normalized else []


def unique_tokens(text: str) -> list[str]:
    seen = set()
    tokens = []
    for token in tokenize(text):
        if token not in seen:
            seen.add(token)
            tokens.append(token)
    return tokens


def join_text_parts(parts: Iterable[str | None]) -> str:
    """Join text parts and normalize."""
    combined = " ".join(
        part.strip()
        for part in parts
        if part and part.strip()
    )
    return normalize_text(combined)


def extract_candidate_text(candidate: dict[str, Any]) -> str:
    """Extract all text fields from a candidate dict and return normalized."""
    parts = []
    profile = candidate.get("profile", {})
    parts.append(profile.get("summary", ""))
    parts.append(profile.get("headline", ""))
    for skill in candidate.get("skills", []):
        parts.append(skill.get("name", ""))
    for career in candidate.get("career_history", []):
        parts.append(career.get("description", ""))
        parts.append(career.get("title", ""))
    return join_text_parts(parts)


def candidate_text(candidate: dict[str, Any]) -> str:
    """Compatibility wrapper for candidate text extraction."""
    return extract_candidate_text(candidate)


def contains_phrase(text: str, phrase: str) -> bool:
    return normalize_text(phrase) in normalize_text(text)


__all__ = [
    "normalize_text",
    "clean_whitespace",
    "tokenize",
    "unique_tokens",
    "join_text_parts",
    "extract_candidate_text",
    "candidate_text",
    "contains_phrase",
]
