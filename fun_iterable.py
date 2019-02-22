from collections import deque


def last_element(iterable):
    # TODO tests
    try:
        return deque(iterable, maxlen=1).pop()
    except IndexError:
        raise ValueError('file is empty')
