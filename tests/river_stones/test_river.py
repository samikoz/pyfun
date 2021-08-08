import pytest

from river_stones.river import River
from river_stones.stone import Stone
from mathsy.geometry import Point


class TestRiver:
    def test_top_stones(self):
        river = River(10, [Stone(Point(12, 9), 1), Stone(Point(5, 0), 4), Stone(Point(0, 8), 3)])
        assert river.top_stones == [Stone(Point(12, 9), 1), Stone(Point(0, 8), 3)]

    def test_bottom_stones(self):
        river = River(5, [Stone(Point(1, 2), 0.5), Stone(Point(6, 5), 4), Stone(Point(17, 5), 6)])
        assert river.bottom_stones == [Stone(Point(17, 5), 6)]

    @pytest.mark.parametrize('stones', (
        ([Stone(Point(5, 5), 20)]),
        ([Stone(Point(1, 1), 3), Stone(Point(1, 6), 2), Stone(Point(6, 6), 3), Stone(Point(15, 9), 2),
            Stone(Point(15, 5), 2), Stone(Point(20, 5), 3), Stone(Point(20, 1), 1)])
    ))
    def test_is_not_traversible(self, stones):
        river = River(10, stones)
        assert river.is_traversible() is False

    @pytest.mark.parametrize('stones', (
        ([Stone(Point(2, 0), 5), Stone(Point(10, 0), 3), Stone(Point(5, 8), 2)]),
        ([Stone(Point(3, 4), 4), Stone(Point(6, 8), 1), Stone(Point(8, 8), 1), Stone(Point(10, 8), 1),
          Stone(Point(10, 5), 2), Stone(Point(10, 2), 1)])
    ))
    def test_is_traversible(self, stones):
        river = River(10, stones)
        assert river.is_traversible() is True
