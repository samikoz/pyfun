from __future__ import annotations

import math
import itertools
from typing import List, MutableMapping, Mapping, Optional, Any, Callable, Tuple, Iterator, Set
from collections import deque

from mathsy.graphs.interfaces import VertexInterface, GraphInterface
from mathsy.graphs.edge import Edge


class _UndirectedGraph(GraphInterface):
    """defined by an adjacency matrix. add weights instead of bools for a weighted graph."""

    def __init__(self, adjacency_matrix: List[List[float]],
                 vertex_factory: Callable[[GraphInterface, int, Any], VertexInterface]) -> None:

        self._vertex_factory: Callable[[GraphInterface, int, Any], VertexInterface] = vertex_factory
        self._adjacencies: List[List[float]] = adjacency_matrix
        self._vertices: List[VertexInterface] = [self._create_vertex(i) for i in range(len(adjacency_matrix))]
        self._edges: Set[Edge] = self._create_edges(adjacency_matrix)

        self._validate_adjacency()

    def _create_vertex(self, index: int, value: Any = None) -> VertexInterface:
        return self._vertex_factory(self, index, value)

    def _create_edges(self, adjacencies: List[List[float]]) -> Set[Edge]:
        return set(itertools.chain.from_iterable([[
            Edge(self._vertices[i], self._vertices[j], adjacencies[i][j])
            for j in range(1, len(adjacencies)) if adjacencies[i][j]
        ] for i in range(len(adjacencies))
        ]))

    def _validate_adjacency(self) -> None:
        order: int = self.order()
        for adjacency in self._adjacencies:
            assert len(adjacency) == order

    def vertex(self, i: int) -> VertexInterface:
        return self._vertices[i]

    def vertices(self) -> Iterator[VertexInterface]:
        return iter(self._vertices)
    
    def edges(self) -> Iterator[Edge]:
        return iter(self._edges)

    def get_weight(self, v1: VertexInterface, v2: VertexInterface) -> float:
        return self._adjacencies[v1.index()][v2.index()]

    def add_vertex(self, adjacency: List[float], value: Any) -> None:
        for index in range(self.order()):
            self._adjacencies[index].append(adjacency[index])
        self._adjacencies.append(adjacency)
        new_vertex: VertexInterface = self._create_vertex(self.order(), value)
        self._vertices.append(new_vertex)
        self._edges.update(Edge(new_vertex, self.vertex(i), adjacency[i]) for i in range(len(adjacency) - 1) if adjacency[i])
        self._validate_adjacency()

    def adjacencies(self) -> Tuple[Tuple[bool]]:
        # to be decommissioned after edges() takeover
        return tuple(tuple(True if x != 0 else False for x in adjacency) for adjacency in self._adjacencies)

    def order(self) -> int:
        return len(self._vertices)

    @staticmethod
    def depth_first_traversal(v: VertexInterface) -> str:
        visited: List[VertexInterface] = []
        to_traverse: List[VertexInterface] = [v]
        while to_traverse:
            v: VertexInterface = to_traverse.pop()
            if v not in visited:
                visited.append(v)
                for n in v.neighbours():
                    to_traverse.append(n)

        return "".join(map(lambda vertex: str(vertex.index()), visited))

    @staticmethod
    def breadth_first_traversal(v: VertexInterface) -> str:
        visited: List[VertexInterface] = []
        to_traverse: deque[VertexInterface] = deque([v])
        while len(to_traverse):
            v: VertexInterface = to_traverse.pop()
            if v not in visited:
                for n in v.neighbours():
                    to_traverse.appendleft(n)
                visited.append(v)

        return "".join(map(lambda vertex: str(vertex.index()), visited))

    @staticmethod
    def _recreate_path(end: VertexInterface, previous: Mapping[VertexInterface, VertexInterface]) -> List[VertexInterface]:
        path: List[VertexInterface] = [end]
        while end in previous:
            path.append(previous[end])
            end = previous[end]
        return list(reversed(path[:-1]))

    def shortest_path_astar(self, source: VertexInterface, goal: VertexInterface,
                            heuristic: Callable[[VertexInterface, VertexInterface], float] = lambda x, y: 0) \
            -> Optional[List[VertexInterface]]:

        unvisited_vertices: Set[VertexInterface] = {self.vertex(i) for i in range(self.order())}
        previous: MutableMapping[VertexInterface, VertexInterface] = {v: None for v in unvisited_vertices}
        actual_dist: MutableMapping[VertexInterface, float] = {v: math.inf for v in unvisited_vertices}
        estimated_dist: MutableMapping[VertexInterface, float] = {v: math.inf for v in unvisited_vertices}
        actual_dist[source] = 0
        estimated_dist[source] = heuristic(source, goal)

        while unvisited_vertices:
            current: VertexInterface = sorted(((v, estimated_dist[v]) for v in unvisited_vertices), key=lambda t: t[1])[0][0]
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
