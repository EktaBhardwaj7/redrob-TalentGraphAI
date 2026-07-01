# src/features/__init__.py
from .base import Feature
from .registry import create_features, register_feature

# Register all features by importing them
from .jd import JDFeature
from .production import ProductionFeature
from .experience import ExperienceFeature
from .consistency import ConsistencyFeature
from .market import MarketFeature
from .hireability import HireabilityFeature
from .preferred import PreferredFeature
from .penalties import PenaltiesFeature
from .honeypot import HoneypotFeature  # <-- added

__all__ = [
    "Feature",
    "create_features",
    "register_feature",
    "JDFeature",
    "ProductionFeature",
    "ExperienceFeature",
    "ConsistencyFeature",
    "MarketFeature",
    "HireabilityFeature",
    "PreferredFeature",
    "PenaltiesFeature",
    "HoneypotFeature",
]
