from __future__ import annotations

import abc
from typing import Iterator, Generic, TypeVar, Tuple


T = TypeVar('T')


class VertexInterface(abc. ABC, Generic[T]):
    @abc.abstractmethod
    def index(self) -> int:
        pass

    @abc.abstractmethod
    def value(self) -> T:
        pass

    @abc.abstractmethod
    def neighbours(self) -> Iterator[VertexInterface]:
        pass


class GraphInterface(abc.ABC):
    @abc.abstractmethod
    def vertex(self, i: int) -> VertexInterface:
        pass

    def vertices(self) -> Iterator[VertexInterface]:
        pass

    @abc.abstractmethod
    def get_weight(self, v1: VertexInterface, v2: VertexInterface) -> float:
        pass

    @abc.abstractmethod
    def adjacencies(self) -> Tuple[Tuple[bool]]:
        pass

    @abc.abstractmethod
    def order(self) -> int:
        pass
