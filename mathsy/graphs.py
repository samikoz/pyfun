from __future__ import annotations

from typing import List, Iterator, MutableMapping, Mapping, Optional, Set, Any, Callable
from collections import deque
import itertools
import math


class Graph:
    """defined by adjacency matrix. add weights instead of bools for a weighted graph."""

    class Vertex:
        def __init__(self, graph: Graph, index: int, value: Any) -> None:
            self._graph: Graph = graph
            self.index: int = index
            self.value: Any = value

        def __repr__(self) -> str:
            return f"Vertex({self.index})"

        def neighbours(self) -> Iterator[Graph.Vertex]:
            adjacency: List[float] = self._graph._adjacencies[self.index]
            return (self._graph.get_vertex(i) for i in itertools.compress(range(self._graph.order()), adjacency))

    def __init__(self, adjacency_matrix: List[List[float]]) -> None:
        self._adjacencies: List[List[float]] = adjacency_matrix
        self._vertices: List[Graph.Vertex] = [self._create_vertex(i) for i in range(len(adjacency_matrix))]

        self._validate_adjacency()

    def _create_vertex(self, index: int, value: Any = None) -> Vertex:
        return self.Vertex(self, index, value)

    def _validate_adjacency(self) -> None:
        order: int = self.order()
        for adjacency in self._adjacencies:
            assert len(adjacency) == order

    def get_vertex(self, i: int) -> Vertex:
        return self._vertices[i]

    def add_vertex(self, adjacency: List[float], value: Any) -> None:
        for index in range(self.order()):
            self._adjacencies[index].append(adjacency[index])
        self._adjacencies.append(adjacency)
        self._vertices.append(self._create_vertex(self.order(), value))
        self._validate_adjacency()

    def order(self) -> int:
        return len(self._vertices)

    def get_weight(self, v1: Vertex, v2: Vertex) -> float:
        return self._adjacencies[v1.index][v2.index]

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

        return "".join(map(lambda vertex: str(vertex.index), visited))

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

        return "".join(map(lambda vertex: str(vertex.index), visited))

    @staticmethod
    def _recreate_path(end: Vertex, previous: Mapping[Vertex, Vertex]) -> List[Vertex]:
        path: List[Graph.Vertex] = [end]
        while end in previous:
            path.append(previous[end])
            end = previous[end]
        return list(reversed(path[:-1]))

    def shortest_path_astar(self, source: Vertex, goal: Vertex,
                            heuristic: Callable[[Vertex, Vertex], float] = lambda x, y: 0) -> Optional[List[Vertex]]:

        unvisited_vertices: Set[Graph.Vertex] = {self.get_vertex(i) for i in range(self.order())}
        previous: MutableMapping[Graph.Vertex, Graph.Vertex] = {v: None for v in unvisited_vertices}
        actual_dist: MutableMapping[Graph.Vertex, float] = {v: math.inf for v in unvisited_vertices}
        estimated_dist: MutableMapping[Graph.Vertex, float] = {v: math.inf for v in unvisited_vertices}
        actual_dist[source] = 0
        estimated_dist[source] = heuristic(source, goal)

        while unvisited_vertices:
            current: Graph.Vertex = sorted(((v, estimated_dist[v]) for v in unvisited_vertices), key=lambda t: t[1])[0][0]
            unvisited_vertices.remove(current)
            for neighbour in unvisited_vertices.intersection(current.neighbours()):
                new_distance = actual_dist[current] + self.get_weight(current, neighbour)
                if new_distance < actual_dist[neighbour]:
                    previous[neighbour] = current
                    actual_dist[neighbour] = new_distance
                    estimated_dist[neighbour] = new_distance + heuristic(neighbour, goal)
                    if neighbour == goal:
                        return self._recreate_path(goal, previous)

        return
