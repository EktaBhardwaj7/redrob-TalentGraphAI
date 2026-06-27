"""Company signal helpers used by market-validation style features."""

SIGNAL_COMPANIES = {
    "openai",
    "google",
    "meta",
    "microsoft",
    "amazon",
    "netflix",
    "linkedin",
    "uber",
    "airbnb",
}


def build_company_index(companies: list[str] | None = None) -> set[str]:
    return {company.strip().lower() for company in (companies or SIGNAL_COMPANIES) if company.strip()}


__all__ = ["SIGNAL_COMPANIES", "build_company_index"]
