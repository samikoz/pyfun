from __future__ import annotations

from typing import List, Iterator
from collections import deque
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

    @staticmethod
    def depth_first_traversal(v: Vertex) -> str:
        visited: List[Graph.Vertex] = []
        to_traverse: List[Graph.Vertex] = [v]
        while to_traverse:
            v: Graph.Vertex = to_traverse.pop()
            if v not in visited:
                visited.append(v)
                for n in v.neighbours():
                    to_traverse.append(n)

        return "".join(map(lambda vertex: str(vertex.value), visited))

    @staticmethod
    def breadth_first_traversal(v: Vertex) -> str:
        visited: List[Graph.Vertex] = []
        to_traverse: deque[Graph.Vertex] = deque([v])
        while len(to_traverse):
            v: Graph.Vertex = to_traverse.pop()
            if v not in visited:
                for n in v.neighbours():
                    to_traverse.appendleft(n)
                visited.append(v)

        return "".join(map(lambda vertex: str(vertex.value), visited))
