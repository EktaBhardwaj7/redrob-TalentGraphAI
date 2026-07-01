# reasoning.py
from src.models.candidate_state import CandidateState


def generate_reasoning(state: CandidateState) -> str:
    # Collect all evidence items with confidence > 0.5
    all_evidence = []
    for feat_res in state.features.values():
        for ev in feat_res.evidence:
            if ev.confidence >= 0.5:
                all_evidence.append(ev)

    all_evidence.sort(key=lambda e: e.confidence, reverse=True)

    if not all_evidence:
        return "Limited evidence found for the role."

    parts = []
    seen_topics = set()

    for ev in all_evidence[:8]:
        topic = ev.source
        if topic in seen_topics:
            continue
        seen_topics.add(topic)

        if topic == "jd":
            parts.append(f"Matched retrieval/ranking technology: {ev.value}")
        elif topic == "production":
            parts.append(f"Production experience: {ev.value}")
        elif topic == "profile":
            parts.append(f"Profile: {ev.value}")
        elif topic == "redrob_signals":
            if "views" in ev.value:
                parts.append(f"Recruiter interest: {ev.value}")
            elif "notice" in ev.value:
                parts.append(f"Notice period: {ev.value}")
            else:
                parts.append(f"Signal: {ev.value}")
        else:
            parts.append(f"{ev.source}: {ev.value}")

    if state.warnings:
        parts.append(f"Concerns: {', '.join(state.warnings[:2])}")

    # --- New: synthesising conclusion ---
    # Determine overall fit based on jd_coverage and production
    jd_score = state.features.get("jd_coverage", None)
    prod_score = state.features.get("production", None)
    hire_score = state.features.get("hireability", None)
    fit_words = []
    if jd_score and jd_score.normalized_score >= 0.6:
        fit_words.append("strong match for the required capabilities")
    else:
        fit_words.append("partial match for required capabilities")
    if prod_score and prod_score.normalized_score >= 0.5:
        fit_words.append("with production experience")
    else:
        fit_words.append("with limited production evidence")
    if hire_score and hire_score.normalized_score >= 0.6:
        fit_words.append("and good availability signals")
    else:
        fit_words.append("and potential availability concerns")

    conclusion = f"Overall, candidate shows {', '.join(fit_words)}."

    # Combine and return
    main_text = ". ".join(parts) + "."
    return f"{main_text} {conclusion}"