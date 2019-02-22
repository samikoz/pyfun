import itertools
import operator


def first_unique_char(word):
    """find the first non-repeating letter of a word or False."""
    try:
        return next(itertools.dropwhile(
            lambda char: word.count(char) != 1,
            iter(word)
        ))
    except StopIteration:
        return False


# TODO do some benchmarking for most efficient option
def indices(char, string):
    """gets all positions of a char in a string."""
    return [x-1 for x in itertools.accumulate(
        len(substr)+1 for substr in string.split(char)[:-1]
    )]


def repeated_min_distance(string):
    """minimal distance between repeated letters or -1."""
    return min(
        list(filter(lambda x: x > -1, [
            min(
                list(map(
                    lambda x: operator.sub(x[1], x[0]), zip(
                        indices(unique_char, string)[:-1],
                        indices(unique_char, string)[1:]
                    )
                )),
                default=-1
            )
            for unique_char in set(string)
        ])),
        default=-1
    )


class NotPermutation(Exception):
    def __init__(self, failplace):
        self.failplace = failplace


def is_permutation(comparee, compared_against):
    """case-sensitive, assumes equal lengths
    in case of a fail NotPermutation exception is thrown with the index of a
    first occurrence of a letter in comparee that is not found required number
    of times in compared_against or -1
    TODO come up with alternative solution with OrderedDict/Counter
    TODO check it for elegance, speed, conformity with contains_permutation."""

    found_positions = []
    try:
        for comparee_char in comparee:
            offset = 0
            while True:
                # the loop takes care of repeated letters
                iee = compared_against.index(comparee_char, offset)
                if iee in found_positions:
                    offset = iee + 1
                else:
                    found_positions.append(iee)
                    break
        return True
    except ValueError:
        raise NotPermutation(comparee.index(comparee_char))


def contains_permutation(permutationer, permutationee):
    """
    :param permutationer is checked to be a permutation of
    :param permutationee from some positions onwards.

    The algorithm is that of a box of length len(permutationee)
    sliding successively over permutationer. If the string in
    the box is not a permutation, we move the box beyond the first
    unfound letter or beyond the first letter that was found but
    whose repetition was not.

    :return: the position or -1 if permutation never occurs"""

    lener = len(permutationer)
    lenee = len(permutationee)
    boxpos = 0
    while boxpos + lenee <= lener:
        try:
            is_permutation(permutationer[boxpos: boxpos + lenee], permutationee)
            return boxpos
        except NotPermutation as NotPermutationYet:
            boxpos += NotPermutationYet.failplace + 1
    return -1
