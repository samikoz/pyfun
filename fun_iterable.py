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
    """for an integer array return number of ways to select a subarray
    whose elements average to a given k"""
    # https://www.geeksforgeeks.org/number-of-ways-to-choose-elements-from-the-array-such-that-their-average-is-k/
    pass
