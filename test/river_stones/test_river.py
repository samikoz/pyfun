from river_stones.river import River
from river_stones.stone import Stone
from river_stones.mathsy import Point


class TestRiver:
    def test_top_stones(self):
        river = River(10, [Stone(Point(12, 9), 1), Stone(Point(5, 0), 4), Stone(Point(0, 8), 3)])
        assert river.top_stones == [Stone(Point(12, 9), 1), Stone(Point(0, 8), 3)]

    def test_bottom_stones(self):
        river = River(5, [Stone(Point(1, 2), 0.5), Stone(Point(6, 5), 4), Stone(Point(17, 5), 6)])
        assert river.bottom_stones == [Stone(Point(17, 5), 6)]
