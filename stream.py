import itertools
import functools


class Stream:
    """a wrapper around an iterable with useful methods for functional solutions"""

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

    def accumulate(self, f, default=None):
        return Stream(itertools.accumulate(itertools.chain([default], self.__iterable) if default else self.__iterable, f))

    def reduce(self, f, default=None):
        return functools.reduce(f, self.__iterable, default) if default else functools.reduce(f, self.__iterable)

    def filter(self, fil):
        return Stream(filter(fil, self.__iterable))

    def pair_consecutive(self):
        return Stream(itertools.dropwhile(
            lambda pair: pair[1] is None,
            itertools.accumulate(
                itertools.chain([(None, None)], self.__iterable),
                lambda previous_pair, element: (element, previous_pair[0])
            )
        ))

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
