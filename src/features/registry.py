# registry.py
from typing import Dict, List, Type
from .base import Feature

_registry: Dict[str, Type[Feature]] = {}


def register_feature(cls: Type[Feature]) -> Type[Feature]:
    _registry[cls.name] = cls
    return cls


def get_all_features() -> List[Type[Feature]]:
    # Return sorted by registration order for stability, but we'll use FEATURE_ORDER from config.
    # Better to use the config's order; we'll let the engine decide.
    return list(_registry.values())


def create_features(order: List[str]) -> List[Feature]:
    """Create feature instances in the specified order."""
    features = []
    for name in order:
        cls = _registry.get(name)
        if cls is None:
            # This should have been validated in loader, but we'll be defensive.
            raise ValueError(f"Feature '{name}' not registered")
        features.append(cls())
    return features