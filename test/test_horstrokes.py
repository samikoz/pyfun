import pytest

from horstrokes import no_of_horizontal_strokes, split


class TestHorStrokes:

    @pytest.mark.parametrize('splittee,sep,splitted', [
        ((1, 2, 3, 4, 5, 6), 3, [(1, 2), (4, 5, 6)]),
        ([1, 1, 2, 1, 7, 8, 1, 7], 1, [[2, ], [7, 8], [7, ]])
    ])
    def test_split_correctness(self, splittee, sep, splitted):
        assert split(splittee, sep) == splitted

    @pytest.mark.parametrize('splittee,sep,splitted', [
        ((1, 2, 3, 4), 8, [(1, 2, 3, 4)]),
    ])
    def test_split_separator(self, splittee, sep, splitted):
        assert split(splittee, sep) == splitted

    @pytest.mark.parametrize('blocks,strokes', [
        ((5, 3), 5),
        ((0,), 0),
        ((5, 2, 7), 10),
        ((5, 3, 1, 8, 3, 6), 15),
    ])
    def test_no_of_horizontal_strokes(self, blocks, strokes):
        assert no_of_horizontal_strokes(blocks) == strokes
