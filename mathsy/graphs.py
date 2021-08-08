from __future__ import annotations

from typing import List, Iterator, MutableMapping, Mapping, Optional, Set
from collections import deque
import itertools
import math


class Graph:
    """defined by adjacency matrix. add weights instead of bools for a weighted graph."""

    class Vertex:
        def __init__(self, graph: Graph, value: int) -> None:
            self._graph = graph
            self.value = value

        def __repr__(self) -> str:
            return f"Vertex({self.value})"

        def neighbours(self) -> Iterator[Graph.Vertex]:
            adjacency: List[float] = self._graph._adjacencies[self.value]
            return (self._graph.get_vertex(i) for i in itertools.compress(range(self._graph.order()), adjacency))

    def _create_vertex(self, value: int) -> Vertex:
        return self.Vertex(self, value)

    def __init__(self, adjacency_matrix: List[List[float]]) -> None:
        order: int = len(adjacency_matrix)
        for adjacency in adjacency_matrix:
            assert len(adjacency) == order

        self._adjacencies: List[List[float]] = adjacency_matrix
        self._vertices: List[Graph.Vertex] = [self._create_vertex(i) for i in range(order)]

    def order(self) -> int:
        return len(self._vertices)

    def get_vertex(self, i: int) -> Vertex:
        return self._vertices[i]

    def get_weight(self, v1: Vertex, v2: Vertex) -> float:
        return self._adjacencies[v1.value][v2.value]

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

    @staticmethod
    def _recreate_path(end: Vertex, previous: Mapping[Vertex, Vertex]) -> List[Vertex]:
        path: List[Graph.Vertex] = [end]
        while end in previous:
            path.append(previous[end])
            end = previous[end]
        return list(reversed(path[:-1]))

    def shortest_path_dijkstra(self, source: Vertex, goal: Vertex) -> Optional[List[Vertex]]:
        unvisited_vertices: Set[Graph.Vertex] = {self.get_vertex(i) for i in range(self.order())}
        previous: MutableMapping[Graph.Vertex, Graph.Vertex] = {v: None for v in unvisited_vertices}
        distance: MutableMapping[Graph.Vertex, float] = {v: math.inf for v in unvisited_vertices}
        distance[source] = 0

        while unvisited_vertices:
            current: Graph.Vertex = sorted(((v, distance[v]) for v in unvisited_vertices), key=lambda t: t[1])[0][0]
            unvisited_vertices.remove(current)
            for neighbour in unvisited_vertices.intersection(current.neighbours()):
                new_distance = distance[current] + self.get_weight(current, neighbour)
                if new_distance < distance[neighbour]:
                    previous[neighbour] = current
                    distance[neighbour] = new_distance
                    if neighbour == goal:
                        return self._recreate_path(goal, previous)

        return
