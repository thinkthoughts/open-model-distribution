"""Visualization helpers for distribution graphs."""

from __future__ import annotations

import matplotlib.pyplot as plt
import networkx as nx


def draw_replication_graph(nodes: int = 12, edges: int = 20):
    """Draw a simple peer-to-peer replication graph."""
    graph = nx.gnm_random_graph(nodes, edges, seed=42)
    nx.draw_networkx(graph, with_labels=True)
    plt.axis("off")
    return graph
