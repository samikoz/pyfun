from typing import FrozenSet

from mathsy.graphs.interfaces import VertexInterface


class Edge:
    def __init__(self, v1: VertexInterface, v2: VertexInterface, weight: float) -> None:
        self.vertices: FrozenSet[VertexInterface] = frozenset({v1, v2})
        self.weight: float = weight

    def __repr__(self) -> str:
        return f"Edge({self.vertices}, {self.weight})"
