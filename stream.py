import itertools
import functools
from typing import Any


class NoParameter:
    pass


class Stream:
    """a wrapper around an iterable with useful methods for functional solutions"""
    # TODO in tests using Stream methods, monkeypatch them

    def __init__(self, an_iterable):
        self.__iterable = iter(an_iterable)

    def __eq__(self, other):
        self.__iterable, me = itertools.tee(self.__iterable)
        other.__iterable, them = itertools.tee(other.__iterable)
        return list(me) == list(them)

    def to_list(self):
        return list(self.__iterable)

    def map(self, f):
        return Stream(map(f, self.__iterable))

    def accumulate(self, f, default: Any = NoParameter()):
        return Stream(itertools.accumulate(
            self.__iterable if isinstance(default, NoParameter) else itertools.chain([default], self.__iterable),
            f
        ))

    def reduce(self, f, default: Any = NoParameter()):
        return functools.reduce(f, self.__iterable) if isinstance(default, NoParameter) \
            else functools.reduce(f, self.__iterable, default)

    def filter(self, fil):
        return Stream(filter(fil, self.__iterable))

    def dropwhile(self, condition):
        return Stream(itertools.dropwhile(condition, self.__iterable))

    def pair_consecutive(self):
        return self.accumulate(lambda previous_pair, element: (element, previous_pair[0]), (None, None))\
            .dropwhile(lambda pair: pair[1] is None)

    def chain(self, other):
        return Stream(itertools.chain(self.__iterable, other))

    def min(self, default=None):
        try:
            return self.accumulate(min).to_list().pop()
        except IndexError:
            return default

    def max(self, default=None):
        try:
            return self.accumulate(max).to_list().pop()
        except IndexError:
            return default

    def shift(self):
        return next(self.__iterable)

    def first(self, condition):
        return next(itertools.dropwhile(
            lambda x: not condition(x),
            self.__iterable)
        )
