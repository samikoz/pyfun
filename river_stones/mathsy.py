from __future__ import annotations

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
        self.coords: Point = coords
        self.radius: float = radius

    def is_adjacent(self, other: Circle) -> bool:
        return self.coords.distance(other.coords) == self.radius + other.radius
