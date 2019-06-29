import itertools
from collections import deque


def last_element(iterable):
    return deque(iterable, maxlen=1).pop()


def max_non_overlapping_sum(array, k):
    """for an integer array of length N, selects some non-overlapping subarrays
    so that none two are adjacent, have length at most k and maximise the sum. dynamic programming."""
    array = array.copy()
    computed = list(itertools.repeat(None, len(array)))

    k_plus_one_zeros = list(itertools.repeat(0, k+1))
    array.extend(k_plus_one_zeros)
    computed.extend(k_plus_one_zeros)

    def compute_for_subarray_above(i):
        """max_non_overlapping_sum for array[i:]. recursive.
        at index i either drop array[i] and compute for i+1 or take array[i] and compute i+2 ...
        or take array[i:i+k] and compute i+k+1"""
        if computed[i] is not None:
            return computed[i]

        computed[i] = max(sum(array[i:n]) + compute_for_subarray_above(n+1) for n in range(i, i+k+1))
        return computed[i]

    return compute_for_subarray_above(0)


def ways_to_subaverage(array, k):
    """for an integer array return number of ways to select a subarray whose elements average to a given k.
    dynamic programming."""

    computed = [[[-1 for s in range(sum(array) + 1)] for n in range(len(array))] for i in range(len(array))]

    def recursive_step(index, sum_so_far, no_of_elements):
        """at each index we either include its element or not.
        the sum of included elements as well as their number is recorded.
        once we traversed it all we check whether it averages correctly."""
        if index == -1:
            return sum_so_far / no_of_elements == k if no_of_elements > 0 else 0
        if computed[index][no_of_elements][sum_so_far] != -1:
            return computed[index][no_of_elements][sum_so_far]
        else:
            computed[index][no_of_elements][sum_so_far] = (
                recursive_step(index - 1, sum_so_far + array[index], no_of_elements + 1) +
                recursive_step(index - 1, sum_so_far, no_of_elements)
            )
            return computed[index][no_of_elements][sum_so_far]

    return recursive_step(len(array) - 1, 0, 0)
