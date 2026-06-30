"""Toy metrics for distribution specification notebooks."""

from __future__ import annotations


def availability(replication: float, independent_paths: float) -> float:
    """Toy availability score A ∝ R P."""
    return replication * independent_paths


def distribution_score(content: float, verification: float, replication: float, paths: float) -> float:
    """Toy open model distribution score D ∝ C V R P."""
    return content * verification * replication * paths
