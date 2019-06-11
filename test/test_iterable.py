import pytest

from fun_iterable import last_element, max_non_overlapping_sum


class TestFunIterable:
    test_iterables = (
        [15, 13, -20, 8],
        range(7),
        'ABCdefG'
    )

    @pytest.mark.parametrize('iterable', test_iterables)
    def test_last_element(self, iterable):
        assert last_element(iterable) == iterable[-1]

    @pytest.mark.parametrize('array,k,max_sum', [
        ([-1, 2, -3, 4, 5], 2, 11), ([1, 1, 1, 1, 1], 1, 3), ([5, 6, 0, 8, 15, -2], 3, 34)
    ])
    def test_max_non_overlapping_sum(self, array, k, max_sum):
        assert max_non_overlapping_sum(array, k) == max_sum
