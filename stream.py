import itertools
import functools


class Stream:
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

    def reduce(self, f):
        return functools.reduce(f, self.__iterable)

    def filter(self, fil):
        return Stream(filter(fil, self.__iterable))

    def pair_conseq(self):
        # TODO reimplement without assignments
        front, back = itertools.tee(self.__iterable)
        next(front)

        return Stream(zip(front, back))

    def chain(self, other):
        return Stream(itertools.chain(self.__iterable, other))

    def min(self):
        # TODO reimplement this and below with accumulate
        return min(list(self.__iterable))

    def max(self):
        return max(list(self.__iterable))

    def shift(self):
        return next(self.__iterable)

    def first(self, condition):
        return next(itertools.dropwhile(
            lambda x: not condition(x),
            self.__iterable)
        )

    def accumulate(self):
        pass
