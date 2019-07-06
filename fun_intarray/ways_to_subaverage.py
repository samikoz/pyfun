def ways_to_subaverage(array, k):
    """for an integer array return number of ways to select a subset whose elements average to a given k.
    dynamic programming."""

    dynamic_storage = [[[-1 for s in range(sum(array) + 1)] for n in range(len(array))] for i in range(len(array))]

    def recursive_step(index, sum_so_far, no_of_elements):
        """at each index we either include its element or not.
        the sum of included elements as well as their number is recorded.
        once we traversed it all we check whether it averages correctly."""
        if index == -1:
            return sum_so_far / no_of_elements == k if no_of_elements > 0 else 0
        if dynamic_storage[index][no_of_elements][sum_so_far] != -1:
            return dynamic_storage[index][no_of_elements][sum_so_far]
        else:
            dynamic_storage[index][no_of_elements][sum_so_far] = (
                recursive_step(index - 1, sum_so_far + array[index], no_of_elements + 1) +
                recursive_step(index - 1, sum_so_far, no_of_elements)
            )
            return dynamic_storage[index][no_of_elements][sum_so_far]

    return recursive_step(len(array) - 1, 0, 0)
