import dependency_injector.providers as providers
import pytest
import math
from typing import List, Any, Tuple

from mathsy.graphs import Graph, VertexFactories
from mathsy.graphs.vertex import Vertex
from mathsy.graphs.interfaces import VertexInterface, T, GraphInterface


class VertexRecordingValueAccess(Vertex):
    def __init__(self, graph: GraphInterface, index: int, value: Any) -> None:
        super().__init__(graph, index, value)
        self.value_checked: bool = False

    def value(self) -> T:
        self.value_checked = True
        return super().value()


@pytest.fixture
def override_vertex():
    VertexFactories.regular.override(providers.Factory(VertexRecordingValueAccess))
    yield lambda: None
    VertexFactories.regular.reset_override()


class TestGraphs:
    # should decouple vertex from graph tests if one cared

    adjacency_matrix: List[List[float]] = [
        [0, 1, 0.5, 5, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0.5, 0, 0, 0, 2, 0],
        [5, 0, 0, 0, 1, 1],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]
    ]
    graph: Graph = Graph(adjacency_matrix)

    @staticmethod
    def _euclidean_distance(v1: VertexInterface, v2: VertexInterface) -> float:
        v1_coords: Tuple[float, float] = v1.value()
        v2_coords: Tuple[float, float] = v2.value()
        return math.sqrt((v1_coords[0] - v2_coords[0])**2 + (v1_coords[1] - v2_coords[1])**2)

    def test_order(self):
        assert self.graph.order() == 6

    def test_vertex(self):
        for i in range(6):
            assert self.graph.vertex(i).index() == i

    def test_vertices(self):
        assert list(self.graph.vertices()) == [self.graph.vertex(i) for i in range(self.graph.order())]

    def test_edges(self):
        g: Graph = Graph([[0, 1, 1], [1, 0, 0], [1, 0, 0]])
        assert {e.vertices for e in g.edges()} == {frozenset({g.vertex(0), g.vertex(1)}), frozenset({g.vertex(0), g.vertex(2)})}

    def test_adjacency(self):
        assert (
            self.graph.adjacencies()
            ==
            ((0, 1, 1, 1, 0, 0),
             (1, 0, 0, 0, 0, 0),
             (1, 0, 0, 0, 1, 0),
             (1, 0, 0, 0, 1, 1),
             (0, 0, 1, 1, 0, 0),
             (0, 0, 0, 1, 0, 0))
        )

    def test_neighbours(self):
        v: VertexInterface = self.graph.vertex(2)
        assert [neighbour.index() for neighbour in v.neighbours()] == [0, 4]

    def test_adding_vertices(self):
        # integration test
        g: Graph = Graph([])
        g.add_vertex([0], 5.5)
        g.add_vertex([1, 0], -1)
        g.add_vertex([0, 1, 0], 0.5)

        v: VertexInterface = g.vertex(2)
        assert v.value() == 0.5
        assert list(v.neighbours()) == [g.vertex(1)]
        assert (g.adjacencies() == ((0, 1, 0), (1, 0, 1), (0, 1, 0)))
        assert {e.vertices for e in g.edges()} == {frozenset({g.vertex(0), g.vertex(1)}), frozenset({g.vertex(1), g.vertex(2)})}

    def test_depth_first_traversal(self):
        v: VertexInterface = self.graph.vertex(0)
        assert self.graph.depth_first_traversal(v) == "035421"

    def test_breadth_first_traversal(self):
        v: VertexInterface = self.graph.vertex(0)
        assert self.graph.breadth_first_traversal(v) == "012345"

    def test_shortest_path_dijkstra(self):
        vertices: List[VertexInterface] = [self.graph.vertex(i) for i in range(self.graph.order())]
        assert (
            self.graph.shortest_path_astar(vertices[1], vertices[5])
            ==
            [vertices[1], vertices[0], vertices[2], vertices[4], vertices[3], vertices[5]]
        )

    def test_astar_traverses_according_to_heuristic(self, override_vertex):
        override_vertex()
        graph: Graph = Graph([])
        graph.add_vertex([0], (0, 0))
        graph.add_vertex([1, 0], (1, 1))
        graph.add_vertex([0, 1, 0], (3, 1.5))
        graph.add_vertex([0, 0, 1, 0], (3.5, 2))
        graph.add_vertex([1, 1, 0, 0, 0], (1.5, 0.5))
        graph.add_vertex([0, 0, 0, 0, 1, 0], (1, -3))
        graph.add_vertex([0, 0, 0, 0, 0, 1, 0], (1, -4))

        source: VertexInterface = graph.vertex(0)
        goal: VertexInterface = graph.vertex(3)
        graph.shortest_path_astar(source, goal, self._euclidean_distance)

        assert graph.vertex(6).value_checked is False
