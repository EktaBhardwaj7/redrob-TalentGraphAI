# Scoring

TalentGraph AI uses two scoring layers:

- Tier score: JD coverage, production, experience fit, and consistency.
- Fine score: market validation, hireability, and preferred capabilities.

Penalties are applied after feature scoring. The final score is clamped to
`[0.0, 1.0]`, and tiers are assigned using configured thresholds.
