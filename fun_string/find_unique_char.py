import itertools


def first_unique_char(word):
    """find the first non-repeating letter of a word or False."""
    try:
        return next(itertools.dropwhile(
            lambda char: word.count(char) != 1,
            iter(word)
        ))
    except StopIteration:
        return False
