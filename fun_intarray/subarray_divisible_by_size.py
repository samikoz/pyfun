# check whether there exists a subarray whose sum is divisible by the size of the original array.
# returns any and -1 if no such exists


def find_divisible_subarray_by_differing_simple_subarrays(array):
    """first computes sub[i] as sum of elements up to ith; if any divisible by len, return.
    then any sub[i,j] = sub[i] - sub[j]"""
    length = len(array)
    simple_subarray_sums = []
    for upper_bound in range(1, length+1):
        simple_subarray_sums.append(sum(array[:upper_bound]))
        if simple_subarray_sums[-1] % length == 0:
            return array[:upper_bound]

    for lower_bound in range(0, length-1):
        for upper_bound in range(lower_bound+1, length):
            if (simple_subarray_sums[upper_bound] - simple_subarray_sums[lower_bound]) % length == 0:
                return array[lower_bound+1:upper_bound+1]
    return -1


def find_divisible_subarray_by_iterating_fore_and_aft(array):
    """uses only a single variable to store the current sum.
    first adds elements along the array until the end, then removes the first element and starts removing from the end.
    then adds third element and adds until the end, etc.
    in other words, traverses the array back and forth, removing from the start where necessary.
    more complicated than the above, but requires less storage and seems faster at least in some cases."""
    direction = 1
    current_sum = 0
    for first_index in range(len(array)):
        for second_index in range(first_index, len(array))[::direction]:

            current_sum += direction * array[second_index]

            if current_sum % len(array) == 0:
                return array[first_index:second_index+1] if direction > 0 else array[first_index:second_index]

        if direction > 0:
            current_sum -= array[first_index]
        direction *= -1
    return -1


def find_divisible_subarray_by_pigeonhole_principle(array):
    """compute first len(array) simple subarray sums as in the first approach.
    ether one of them is divisible by len(array) and we're done or two repeated in which case the difference works.
    it's clear here that -1 is never obtained."""
    length = len(array)
    modulos_to_indices = {}
    for upper_bound in range(1, len(array)+1):
        current_remainder = sum(array[:upper_bound]) % length
        if current_remainder == 0:
            return array[:upper_bound]

        if modulos_to_indices.get(current_remainder, -1) > -1:
            return array[modulos_to_indices.get(current_remainder)+1:upper_bound]
        modulos_to_indices[current_remainder] = upper_bound-1
