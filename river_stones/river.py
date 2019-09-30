from typing import Sequence, List, Set

from river_stones.stone import Stone
from river_stones.mathsy import ConnectedComponent


class River:
    """assumed to be a section of a plane given by x > 0, 0 < y < height.
    stones can have centres only within that section; stones cannot overlap."""

    def __init__(self, height: int, stones: Sequence[Stone]):
        self.height: int = height
        self.stones: List[Stone] = []
        self.top_stones: List[Stone] = []
        self.bottom_stones: List[Stone] = []

        for stone in stones:
            self._assert_stone_within_river(stone)
            self._assert_stone_does_not_overlap(stone)

            self.stones.append(stone)
            self._append_if_top(stone)
            self._append_if_bottom(stone)

    def _assert_stone_within_river(self, stone: Stone):
        assert 0 <= stone.coordinates.y <= self.height
        assert stone.coordinates.x >= 0

    def _assert_stone_does_not_overlap(self, stone: Stone):
        for placed_stone in self.stones:
            assert stone.is_overlapping(placed_stone) is False

    def _append_if_top(self, stone: Stone) -> None:
        if stone.coordinates.y + stone.radius >= self.height:
            self.top_stones.append(stone)

    def _append_if_bottom(self, stone: Stone) -> None:
        if stone.coordinates.y - stone.radius <= 0:
            self.bottom_stones.append(stone)

    def is_traversible(self) -> bool:
        left_to_traverse: List[Stone] = self.stones
        while len(left_to_traverse) > 0:
            a_stone: Stone = left_to_traverse.pop(0)
            connected_component = ConnectedComponent(a_stone, lambda stone1, stone2: stone1.is_adjacent(stone2))
            connected_component.add(left_to_traverse)
            if self._contains_top_and_bottom(connected_component.get()):
                return False
            left_to_traverse = self._remove_already_traversed(left_to_traverse, connected_component.get())

        return True

    def _contains_top_and_bottom(self, component: Set[Stone]) -> bool:
        return len(component.intersection(self.top_stones)) > 0 and len(component.intersection(self.bottom_stones)) > 0

    @staticmethod
    def _remove_already_traversed(to_traverse: Sequence[Stone], already_traversed: Set[Stone]) -> List[Stone]:
        return list(set(to_traverse).difference(already_traversed))
