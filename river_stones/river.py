from typing import Sequence, List

from river_stones.stone import Stone


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
