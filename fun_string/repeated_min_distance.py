import itertools
import operator

from stream import Stream


def get_indices(char, string):
    """gets all positions of a char in a string. functional."""
    return [x-1 for x in itertools.accumulate(
        len(substring)+1 for substring in string.split(char)[:-1]
    )]


def repeated_min_distance(string):
    """minimal distance between repeated letters or -1. functional."""
    return Stream(set(string)).map(
        lambda char: Stream(get_indices(char, string))
        .pair_consecutive()
        .map(lambda pair: operator.sub(pair[0], pair[1]))
        .min(-1)
    ).filter(lambda x: x > -1).min(-1)
