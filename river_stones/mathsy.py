from __future__ import annotations

from typing import Sequence
import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y

    def distance(self, other: Point) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Circle:
    def __init__(self, coords: Point, radius: float) -> None:
        assert radius > 0
        self.coordinates: Point = coords
        self.radius: float = radius

    def is_adjacent(self, other: Circle) -> bool:
        return self._centre_distance(other) == self.radius + other.radius

    def is_overlapping(self, other: Circle) -> bool:
        return self._centre_distance(other) < self.radius + other.radius

    def _centre_distance(self, other: Circle) -> float:
        return self.coordinates.distance(other.coordinates)


class Graph:
    def __init__(self, neighbours: Sequence[Graph]) -> None:
        self.neighbours: Sequence[Graph] = neighbours
