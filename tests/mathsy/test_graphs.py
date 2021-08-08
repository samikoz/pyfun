from typing import List

from mathsy.graphs import Graph


class TestGraphs:
    adjacency_matrix: List[List[bool]] = [
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]
    ]
    graph: Graph = Graph(adjacency_matrix)

    def test_order(self):
        assert self.graph.order() == 6

    def test_get_vertex(self):
        for i in range(6):
            assert self.graph.get_vertex(i).value == i

    def test_adjacency(self):
        v: Graph.Vertex = self.graph.get_vertex(2)
        assert [neighbour.value for neighbour in v.neighbours()] == [0, 4]

    def test_depth_first_traversal(self):
        v: Graph.Vertex = self.graph.get_vertex(0)
        assert self.graph.depth_first_traversal(v) == "035421"

    def test_breadth_first_traversal(self):
        v: Graph.Vertex = self.graph.get_vertex(0)
        assert self.graph.breadth_first_traversal(v) == "012345"
