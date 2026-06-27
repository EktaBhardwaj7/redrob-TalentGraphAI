# constants.py

# Score bounds
MIN_SCORE = 0.0
MAX_SCORE = 1.0

MIN_CONF = 0.0
MAX_CONF = 1.0

# Tier labels
T_A = "A+"
T_B = "A"
T_C = "B"
T_D = "C"
T_E = "D"

TIERS = (T_A, T_B, T_C, T_D, T_E)

# Evidence strength
DIR = "direct"
REL = "related"
IMP = "implicit"

# Qualification buckets
REQ = "required"
PREF = "preferred"

# Candidate status
ACT = "active"
INACT = "inactive"
OTW = "open_to_work"

# Runtime defaults
BATCH = 1000
ENC = "utf-8"

# Output columns (submission spec)
COLS = ("candidate_id", "rank", "score", "tier", "reasoning")

# Feature names (must match registered feature names)
F_JD = "jd_coverage"
F_PROD = "production"
F_MKT = "market_validation"
F_HIRE = "hireability"
F_CONS = "consistency"
F_EXP = "experience_fit"
F_PREF = "preferred_match"
F_PEN = "penalties"

ALL_F = (F_JD, F_PROD, F_MKT, F_HIRE, F_CONS, F_EXP, F_PREF, F_PEN)

__all__ = [
    "MIN_SCORE",
    "MAX_SCORE",
    "MIN_CONF",
    "MAX_CONF",
    "TIERS",
    "T_A",
    "T_B",
    "T_C",
    "T_D",
    "T_E",
    "DIR",
    "REL",
    "IMP",
    "REQ",
    "PREF",
    "ACT",
    "INACT",
    "OTW",
    "BATCH",
    "ENC",
    "COLS",
    "F_JD",
    "F_PROD",
    "F_MKT",
    "F_HIRE",
    "F_CONS",
    "F_EXP",
    "F_PREF",
    "F_PEN",
    "ALL_F",
]