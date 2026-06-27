# reasoning.py
from src.models.candidate_state import CandidateState


def generate_reasoning(state: CandidateState) -> str:
    # Collect all evidence items with confidence > 0.5
    all_evidence = []
    for feat_res in state.features.values():
        for ev in feat_res.evidence:
            if ev.confidence >= 0.5:
                all_evidence.append(ev)

    # Sort by confidence descending
    all_evidence.sort(key=lambda e: e.confidence, reverse=True)

    if not all_evidence:
        return "Limited evidence found for the role."

    # Build a coherent summary
    parts = []
    seen_topics = set()

    for ev in all_evidence[:8]:  # limit to 8 items
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

    # Add warnings if present
    if state.warnings:
        parts.append(f"Concerns: {', '.join(state.warnings[:2])}")

    return ". ".join(parts) + "."