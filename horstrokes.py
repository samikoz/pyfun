# q2 from future3 coding contest, 19.10.17

import itertools
from more_itertools import split_at


def no_of_horizontal_strokes(heights):
    """let heights be an array of positive integers describing heights of uniform-width rectangles placed one-by-one.
    imagine we are painting the rectangles horizontally with single strokes, the height of the brush is 1.
    the function computes the minimal number of strokes needed to paint the rectangles."""

    strokes = min(heights)
    heights = [x - strokes for x in heights]
    for subarray in itertools.filterfalse(lambda part: part == [], split_at(heights, lambda n: n == 0)):
        strokes += no_of_horizontal_strokes(subarray)

    return strokes
