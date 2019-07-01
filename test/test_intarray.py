import pytest

from fun_intarray import max_non_overlapping_sum, ways_to_subaverage, find_subarray_divisible_by_size


class TestIntArray:
    @pytest.mark.parametrize('array,k,max_sum', [
        ([-1, 2, -3, 4, 5], 2, 11), ([1, 1, 1, 1, 1], 1, 3), ([5, 6, 0, 8, 15, -2], 3, 34)
    ])
    def test_max_non_overlapping_sum(self, array, k, max_sum):
        assert max_non_overlapping_sum(array, k) == max_sum

    @pytest.mark.parametrize('array,k,no_of_ways', [
        ([7, 9, 8, 9], 8, 5), ([3, 6, 2, 8, 7, 6, 5, 9], 5, 19), ([6, 6, 9], 8, 0), ([2, 2, 2], 2, 7)
    ])
    def test_ways_to_subaverage(self, array, k, no_of_ways):
        assert ways_to_subaverage(array, k) == no_of_ways

    @pytest.mark.parametrize('array,result', ([7, 5, 3, 7], [3, 7, 14], [1, 1, 1]))
    def test_positive_find_subarray_divisible_by_size(self, array, result):
        assert sum(find_subarray_divisible_by_size(array)) % len(array) == 0

    @pytest.mark.parametrize('array', ([3, 1, 4, 1, 3]))
    def test_negative_find_subarray_divisible_by_size(self, array):
        assert find_subarray_divisible_by_size(array) == -1
