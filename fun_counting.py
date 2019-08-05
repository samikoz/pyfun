import itertools


def count_bounded_integers_with_digits_from_set(sorted_digits, bound, length):
    """counts how many numbers of given length, smaller than a given bound there are
    with digits from a given sorted array.

    the simplest cases are when the bound lies below or above all possible combinations of digits
    and these are checked first.
    if not then the bound cuts off the possibilities somewhere
    and the approach is to count the digits allowed on each position.

    refer to the documentation of the count function for further details."""
    count_function = define_count_function(sorted_digits, length)

    least_possible_number = sorted_digits[0]*10**(length-1)
    greatest_possible_number = int(str(sorted_digits[-1])*length)
    if bound < least_possible_number:
        return 0
    if bound > greatest_possible_number:
        return count_function([], len(sorted_digits) - 1)

    bounds_digits = [int(d) for d in str(bound)]
    coinciding_bound_digits = list(itertools.takewhile(lambda d: d in sorted_digits, bounds_digits))
    coinciding_digits_indices = list(map(lambda d: sorted_digits.index(d), coinciding_bound_digits))
    first_non_coinciding_digit = bounds_digits[len(coinciding_bound_digits)] \
        if len(bounds_digits) > len(coinciding_bound_digits) else -1
    smaller_than_first_non_coinciding = list(
        itertools.dropwhile(lambda d: d > first_non_coinciding_digit, reversed(sorted_digits))
    )

    if len(smaller_than_first_non_coinciding) > 0:
        return count_function(coinciding_digits_indices, sorted_digits.index(smaller_than_first_non_coinciding[0]))
    else:
        coinciding_digits_indices = list(
            itertools.dropwhile(lambda d: d == 0, reversed(coinciding_digits_indices))
        )[::-1]
        return count_function(coinciding_digits_indices[:-1], coinciding_digits_indices[-1] - 1) \
            if len(coinciding_digits_indices) > 0 else 0


def define_count_function(digit_set, length):
    """returns helper count function.

    count's first parameter [i1, i2, ...] are the indices of bound's leading digits in the given digit set.
    then for the first digit that is not in the set,
    the second parameter j is the index of the closest, smaller digit.

    on the first position we can freely have all the digits on indices < i1 (excluding 0 if present)
    and on the remaining any of the allowed.
    we can also have the i1-digit and then proceed as above with the second position, etc.

    once these are counted, the remaining possibilities are j+1 digits on the first not-in-the-given-set-position
    (unless it's the first one and zero is present in the set) and anything on the remaining positions.

    if j is nonexistent, either because no such smaller digit exist in the set
    or because every bound digit is present there, then the first parameter needs to be tweaked:
    zeros are dropped from the right side of [i1, i2, ...] and the first non-zero needs to be decreased by 1.
    this is done in the outer function, invoking the count."""
    def count(coinciding_indices, first_smaller_index):
        possibilities_count = 0
        digit_position = 1
        for index in coinciding_indices:
            possibilities_count += count_for_position(digit_position, index)
            digit_position += 1
        return possibilities_count + count_for_position(digit_position, first_smaller_index+1)

    def count_for_position(position, possibilities):
        return discount_zero_on_the_leading_position(position, possibilities) * \
               len(digit_set) ** (length - position)

    def discount_zero_on_the_leading_position(position, possibilities):
        return possibilities if 0 not in digit_set or position > 1 else possibilities - 1

    return count
