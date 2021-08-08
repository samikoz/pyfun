from __future__ import annotations

from river_stones.interfaces import ConnectableInterface
from mathsy.geometry import Circle


class Stone(ConnectableInterface, Circle):
    def is_connected(self, other: Stone) -> bool:
        return self.is_adjacent(other)
