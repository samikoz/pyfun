import pytest

from fun_iterable import last_element


class TestFunIterable:
    test_iterables = (
        [15, 13, -20, 8],
        range(7),
        'ABCdefG'
    )

    @pytest.mark.parametrize('iterable', test_iterables)
    def test_last_element(self, iterable):
        assert last_element(iterable) == iterable[-1]
