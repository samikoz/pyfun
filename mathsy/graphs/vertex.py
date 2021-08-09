import itertools
from typing import Any, Iterator, Tuple

from mathsy.graphs.interfaces import GraphInterface, VertexInterface, T


class Vertex(VertexInterface):
    def __init__(self, graph: GraphInterface, index: int, value: Any) -> None:
        self._graph: GraphInterface = graph
        self._index: int = index
        self._value: Any = value

    def __repr__(self) -> str:
        return f"Vertex({self._index})"

    def index(self) -> int:
        return self._index

    def value(self) -> T:
        return self._value

    def neighbours(self) -> Iterator[VertexInterface]:
        adjacency: Tuple[bool] = self._graph.adjacencies()[self._index]
        return (self._graph.get_vertex(i) for i in itertools.compress(range(self._graph.order()), adjacency))
