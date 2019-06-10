from collections import deque


def last_element(iterable):
    return deque(iterable, maxlen=1).pop()
