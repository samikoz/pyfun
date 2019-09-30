from __future__ import annotations

from typing import Any, Generic, TypeVar, Callable, List, Iterable, Set, Sequence
import math


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


T = TypeVar('T')


class ConnectedComponent(Generic[T]):
    def __init__(self, initial_member: T, connecting_method: Callable[[T, T], bool]) -> None:
        self.component: List[T] = [initial_member]
        self.is_connected: Callable[[T, T], bool] = connecting_method

    def add(self, elements: Iterable[T]) -> None:
        candidate_connectors: List[T] = list(elements)
        component_index: int = 0
        while component_index < len(self.component):
            candidate_connectors: List[T] = self._extend_component_and_shrink_candidates_by_connectors(
                self.component[component_index],
                candidate_connectors
            )
            component_index += 1

    def _extend_component_and_shrink_candidates_by_connectors(self, connectee: T, candidates: Sequence[T]) -> List[T]:
        connected: List[T] = self._get_all_connected(connectee, candidates)
        self.component.extend(connected)
        return list(set(candidates).difference(connected))

    def _get_all_connected(self, connectee: T, candidates: Sequence[T]) -> List[T]:
        return list(filter(lambda x: self.is_connected(connectee, x), candidates))

    def get(self) -> Set[T]:
        return set(self.component)
