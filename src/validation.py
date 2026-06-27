# validation.py
from typing import Dict, Any
from src.common.dates import parse_date
from src.common.text import candidate_text, normalize_text
from src.models.validation_result import ValidationResult
from src.models.candidate_state import CandidateState


def normalize_and_validate(candidate: Dict[str, Any], state: CandidateState) -> ValidationResult:
    """Normalize candidate fields into state and validate."""
    warnings = []
    errors = []

    # Normalize text once
    state.text = candidate_text(candidate)

    # Extract and deduplicate skills
    raw_skills = [normalize_text(s.get("name", "")) for s in candidate.get("skills", []) if s.get("name")]
    state.skills = list(dict.fromkeys([s for s in raw_skills if s]))

    # Extract titles from career history
    titles = []
    for entry in candidate.get("career_history", []):
        title = entry.get("title", "")
        if title:
            titles.append(normalize_text(title))
    state.titles = titles

    # Extract dates
    dates = []
    for entry in candidate.get("career_history", []):
        start = entry.get("start_date")
        end = entry.get("end_date")
        if start and end:
            dates.append((start, end))
    state.dates = dates

    # Validation
    if not candidate.get("candidate_id"):
        errors.append("Missing candidate_id")

    if not candidate.get("profile", {}).get("years_of_experience"):
        warnings.append("Missing years_of_experience")

    # Timeline checks
    for start, end in dates:
        s = parse_date(start)
        e = parse_date(end)
        if s and e and s > e:
            warnings.append(f"Timeline inversion: {start} > {end}")

    if not state.skills:
        warnings.append("No skills listed")

    return ValidationResult(
        is_valid=len(errors) == 0,
        warnings=warnings,
        errors=errors,
    )