from __future__ import annotations

from typing import List, Iterator
import itertools


class Graph:

    class Vertex:
        def __init__(self, graph: Graph, value: int) -> None:
            self._graph = graph
            self.value = value

        def neighbours(self) -> Iterator[Graph.Vertex]:
            adjacency: List[bool] = self._graph._adjacencies[self.value]
            return (self._graph.get_vertex(i) for i in itertools.compress(range(self._graph.order()), adjacency))

    def _create_vertex(self, value: int) -> Vertex:
        return self.Vertex(self, value)

    def __init__(self, adjacency_matrix: List[List[bool]]) -> None:
        order: int = len(adjacency_matrix)
        for adjacency in adjacency_matrix:
            assert len(adjacency) == order

        self._adjacencies: List[List[bool]] = adjacency_matrix
        self._vertices: List[Graph.Vertex] = [self._create_vertex(i) for i in range(order)]

    def order(self) -> int:
        return len(self._vertices)

    def get_vertex(self, i: int) -> Vertex:
        return self._vertices[i]
