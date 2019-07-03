import itertools


def max_non_overlapping_sum(array, k):
    """for an integer array of length N, selects some non-overlapping subarrays
    so that none two are adjacent, have length at most k and maximise the sum. dynamic programming."""
    array = array.copy()
    dynamic_storage = list(itertools.repeat(None, len(array)))

    k_plus_one_zeros = list(itertools.repeat(0, k+1))
    array.extend(k_plus_one_zeros)
    dynamic_storage.extend(k_plus_one_zeros)

    def compute_for_subarray_above(i):
        """max_non_overlapping_sum for array[i:]. recursive.
        at index i either drop array[i] and compute for i+1 or take array[i] and compute i+2 ...
        or take array[i:i+k] and compute i+k+1"""
        if dynamic_storage[i] is not None:
            return dynamic_storage[i]

        dynamic_storage[i] = max(sum(array[i:n]) + compute_for_subarray_above(n+1) for n in range(i, i+k+1))
        return dynamic_storage[i]

    return compute_for_subarray_above(0)
