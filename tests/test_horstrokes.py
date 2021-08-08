import pytest

from horstrokes import no_of_horizontal_strokes


class TestHorStrokes:
    @pytest.mark.parametrize('blocks,strokes', [
        ((5, 3), 5),
        ((0,), 0),
        ((5, 2, 7), 10),
        ((5, 3, 1, 8, 3, 6), 15),
    ])
    def test_no_of_horizontal_strokes(self, blocks, strokes):
        assert no_of_horizontal_strokes(blocks) == strokes
