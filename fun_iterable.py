from collections import deque


def last_element(iterable):
    return deque(iterable, maxlen=1).pop()


def max_non_overlapping_sum(array, k):
    """for an integer array of length N, selects some non-overlapping subarrays
    so that none two are adjacent, have length at most k and maximise the sum"""
    pass
