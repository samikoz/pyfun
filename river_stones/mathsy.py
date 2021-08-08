from __future__ import annotations

from typing import Any, Generic, TypeVar, List, Set as SetType, Sequence, Iterator, AbstractSet
from collections.abc import Set
import math

from river_stones.interfaces import ConnectableInterface


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return (self.x, self.y).__hash__()

    def distance(self, other: Point) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Circle:
    def __init__(self, coordinates: Point, radius: float) -> None:
        assert radius > 0
        self.coordinates: Point = coordinates
        self.radius: float = radius

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, self.__class__) and
            self.coordinates == other.coordinates and
            self.radius == other.radius
        )

    def __hash__(self) -> int:
        return (self.coordinates, self.radius).__hash__()

    def __repr__(self) -> str:
        return f'{str(self.__class__.__name__)}(({self.coordinates.x}, {self.coordinates.y}), {self.radius})'

    def is_adjacent(self, other: Circle) -> bool:
        return self._centre_distance(other) == self.radius + other.radius

    def is_overlapping(self, other: Circle) -> bool:
        return self._centre_distance(other) < self.radius + other.radius

    def _centre_distance(self, other: Circle) -> float:
        return self.coordinates.distance(other.coordinates)


C = TypeVar('C', bound=ConnectableInterface)


class ConnectedComponent(Generic[C], Set):
    def __init__(self, initial_member: C) -> None:
        self.component: SetType[C] = {initial_member}

    def add(self, elements: SetType[C]) -> None:
        component_elements: List[C] = list(self.component)
        component_index: int = 0
        while component_index < len(component_elements):
            connected: List[C] = self._get_all_connected(component_elements[component_index], elements)
            component_elements.extend(connected)
            elements = set(elements).difference(connected)
            component_index += 1

        self.component = set(component_elements)

    @staticmethod
    def _get_all_connected(connectee: C, candidates: Sequence[C]) -> List[C]:
        return list(filter(lambda x: connectee.is_connected(x), candidates))

    def __iter__(self) -> Iterator[C]:
        return iter(self.component)

    def __len__(self) -> int:
        return len(self.component)

    def __contains__(self, x: object) -> bool:
        return object in self.component

    def intersection(self, s: AbstractSet[C]) -> AbstractSet:
        return self.component.intersection(s)

    def union(self, s: AbstractSet[C]) -> AbstractSet[C]:
        return self.component.union(s)

    def difference(self, s: AbstractSet[C]) -> AbstractSet[C]:
        return self.component.difference(s)
