from typing import List

from mathsy.graphs import Graph


class TestGraphs:
    adjacency_matrix: List[List[float]] = [
        [0, 1, 0.5, 5, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0.5, 0, 0, 0, 2, 0],
        [5, 0, 0, 0, 1, 1],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]
    ]
    graph: Graph = Graph(adjacency_matrix)

    def test_order(self):
        assert self.graph.order() == 6

    def test_get_vertex(self):
        for i in range(6):
            assert self.graph.get_vertex(i).index == i

    def test_neighbours(self):
        v: Graph.Vertex = self.graph.get_vertex(2)
        assert [neighbour.index for neighbour in v.neighbours()] == [0, 4]

    def test_adding_vertices(self):
        g: Graph = Graph([])
        g.add_vertex([0], 5.5)
        g.add_vertex([1, 0], -1)
        g.add_vertex([0, 1, 0], 0.5)

        v: Graph.Vertex = g.get_vertex(2)
        assert v.value == 0.5
        assert list(v.neighbours()) == [g.get_vertex(1)]

    def test_depth_first_traversal(self):
        v: Graph.Vertex = self.graph.get_vertex(0)
        assert self.graph.depth_first_traversal(v) == "035421"

    def test_breadth_first_traversal(self):
        v: Graph.Vertex = self.graph.get_vertex(0)
        assert self.graph.breadth_first_traversal(v) == "012345"

    def test_shortest_path_astar(self):
        vertices: List[Graph.Vertex] = [self.graph.get_vertex(i) for i in range(self.graph.order())]
        assert (
            self.graph.shortest_path_astar(vertices[1], vertices[5])
            ==
            [vertices[1], vertices[0], vertices[2], vertices[4], vertices[3], vertices[5]]
        )
