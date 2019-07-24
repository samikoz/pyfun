import itertools


def count_bounded_integers_with_digits_from_set(sorted_digits, bound, length):
    # https://www.geeksforgeeks.org/count-of-integers-of-length-n-and-value-less-than-k-such-that-they-contain-digits-only-from-the-given-set/
    """counts how many numbers of given length, smaller than a given bound there are
    with digits from a given sorted array"""
    def get_count(coinciding_indices, first_smaller_index):
        number_of_possible_digits = len(sorted_digits)
        sum_so_far = 0
        position = 1
        for index in coinciding_indices:
            sum_so_far += index * number_of_possible_digits**(length - position)
            position += 1
        return sum_so_far + (first_smaller_index + 1) * number_of_possible_digits**(length - position)

    bound_digits = [int(d) for d in str(bound)]
    if bound < sorted_digits[0]*10**(length-1):
        return 0
    if bound > int(str(sorted_digits[-1])*length):
        return get_count([], len(sorted_digits) - 1)

    coinciding_bound_digits = list(itertools.takewhile(lambda d: d in sorted_digits, bound_digits))
    coinciding_digits_indices = list(map(lambda d: sorted_digits.index(d), coinciding_bound_digits))
    first_non_coinciding = bound_digits[len(coinciding_bound_digits)] if len(bound_digits) > len(coinciding_bound_digits) else -1
    smaller_than_first_non_coinciding = list(itertools.dropwhile(lambda d: d > first_non_coinciding, sorted_digits[::-1]))
    if len(smaller_than_first_non_coinciding) > 0:
        return get_count(coinciding_digits_indices, sorted_digits.index(smaller_than_first_non_coinciding[0]))
    else:
        coinciding_digits_indices = list(itertools.dropwhile(lambda d: d == 0, coinciding_digits_indices[::-1]))[::-1]
        return get_count(coinciding_digits_indices[:-1], coinciding_digits_indices[-1] - 1) if len(coinciding_digits_indices) > 0 else 0
