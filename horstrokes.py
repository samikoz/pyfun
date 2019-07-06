# q2 from future3 coding contest, 19.10.17

import itertools


def split(array, separator=None):
    """splits an array into subarrays separated by a separator.
    empty subarrays are not returned."""

    count = array.count(separator)
    char_indices = []
    offset = -1
    for _ in itertools.repeat(None, count):
        char_indices.append(array.index(separator, offset+1))
        offset = char_indices[-1]

    char_indices.insert(0, -1)
    char_indices.insert(count+1, len(array))

    splits = [array[char_indices[i]+1:char_indices[i+1]] for i in range(count+1)
              if char_indices[i+1] > char_indices[i]+1]
    return splits


def no_of_horizontal_strokes(heights):
    """let heights be an array of positive integers describing heights of uniform-width rectangles placed one-by-one.
    imagine we are painting the rectangles horizontally with single strokes, the height of the brush is 1.
    the function computes the minimal number of strokes needed to paint the rectangles."""

    strokes = min(heights)
    heights = [x - strokes for x in heights]
    for subarray in split(heights, 0):
        strokes += no_of_horizontal_strokes(subarray)

    return strokes