import pytest

from fun_intarray.max_non_overlapping_sum import max_non_overlapping_sum
from fun_intarray.ways_to_subaverage import ways_to_subaverage
from fun_intarray.subarray_divisible_by_size import find_divisible_subarray_by_differing_simple_subarrays, \
    find_divisible_subarray_by_iterating_fore_and_aft, find_divisible_subarray_by_pigeonhole_principle


class TestMaxNonOverlappingSum:
    @pytest.mark.parametrize('array,k,max_sum', [
        ([-1, 2, -3, 4, 5], 2, 11), ([1, 1, 1, 1, 1], 1, 3), ([5, 6, 0, 8, 15, -2], 3, 34)
    ])
    def test_max_non_overlapping_sum(self, array, k, max_sum):
        assert max_non_overlapping_sum(array, k) == max_sum


class TestWaysToSubaverage:
    @pytest.mark.parametrize('array,k,no_of_ways', [
        ([7, 9, 8, 9], 8, 5), ([3, 6, 2, 8, 7, 6, 5, 9], 5, 19), ([6, 6, 9], 8, 0), ([2, 2, 2], 2, 7)
    ])
    def test_ways_to_subaverage(self, array, k, no_of_ways):
        assert ways_to_subaverage(array, k) == no_of_ways


class TestSubarrayDivisibleBySize:

    test_arrays = ([7, 5, 3, 7], [3, 7, 14], [1, 1, 1, 4], [3, 1, 3, 1, 3])

    @pytest.mark.parametrize('array', test_arrays)
    def test_find_divisible_subarray_by_differing_simple_subarrays(self, array):
        assert sum(find_divisible_subarray_by_differing_simple_subarrays(array)) % len(array) == 0

    @pytest.mark.parametrize('array', test_arrays)
    def test_find_divisible_subarray_by_iterating_fore_and_aft(self, array):
        assert sum(find_divisible_subarray_by_iterating_fore_and_aft(array)) % len(array) == 0

    @pytest.mark.parametrize('array', test_arrays)
    def test_find_divisible_subarray_by_pigeonhole_principle(self, array):
        assert sum(find_divisible_subarray_by_pigeonhole_principle(array)) % len(array) == 0
