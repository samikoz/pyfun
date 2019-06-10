from collections import deque


def last_element(iterable):
    try:
        return deque(iterable, maxlen=1).pop()
    except IndexError:
        raise IndexError('Empty iterable')
