"""Build all preprocessing lookup indexes."""

from src.preprocess.company_index import build_company_index
from src.preprocess.synonym_index import build_synonym_index


def build_indexes() -> dict[str, object]:
    return {
        "companies": build_company_index(),
        "synonyms": build_synonym_index(),
    }


__all__ = ["build_indexes"]
