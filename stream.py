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

    def accumulate(self, f):
        return Stream(itertools.accumulate(self.__iterable, f))

    def reduce(self, f):
        return functools.reduce(f, self.__iterable)

    def filter(self, fil):
        return Stream(filter(fil, self.__iterable))

    def pair_consecutive(self):
        front, back = itertools.tee(self.__iterable)
        next(front)

        return Stream(zip(front, back))

    def chain(self, other):
        return Stream(itertools.chain(self.__iterable, other))

    def min(self):
        return self.accumulate(min).to_list().pop()

    def max(self):
        return self.accumulate(max).to_list().pop()

    def shift(self):
        return next(self.__iterable)

    def first(self, condition):
        return next(itertools.dropwhile(
            lambda x: not condition(x),
            self.__iterable)
        )
