from river_stones.mathsy import Point, Circle


class TestPoint:
    def test_equality(self):
        assert Point(3.5, 12) == Point(3.5, 12)

    def test_inequality(self):
        assert Point(0, 4) != Point(0, 2)

    def test_distance(self):
        a = Point(1, 3)
        b = Point(-2, 7)
        assert a.distance(b) == 5


class TestCircle:
    def test_equality(self):
        assert Circle(Point(0, 5), 2) == Circle(Point(0, 5), 2)

    def test_inequality(self):
        assert Circle(Point(0, 1), 2) != Circle(Point(0, 0), 2)
        assert Circle(Point(0, 2), 9) != Circle(Point(0, 2), 9.1)

    def test_is_adjacent_positive(self):
        a = Circle(Point(1, 1), 3)
        b = Circle(Point(1, 7), 3)
        assert a.is_adjacent(b) is True

    def test_is_adjacent_disjoint(self):
        a = Circle(Point(-2, 0), 1)
        b = Circle(Point(1, 3), 0.5)
        assert a.is_adjacent(b) is False

    def test_is_adjacent_intersecting(self):
        a = Circle(Point(0, 0), 2)
        b = Circle(Point(1, 1), 1)
        assert a.is_adjacent(b) is False

    def test_is_overlapping_positive(self):
        a = Circle(Point(0, 0), 2)
        b = Circle(Point(1, 1), 1)
        assert a.is_overlapping(b) is True

    def test_is_overlapping_disjoint(self):
        a = Circle(Point(-2, 0), 1)
        b = Circle(Point(1, 3), 0.5)
        assert a.is_overlapping(b) is False

    def test_is_overlapping_adjacent(self):
        a = Circle(Point(1, 1), 3)
        b = Circle(Point(1, 7), 3)
        assert a.is_overlapping(b) is False
