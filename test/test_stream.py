import operator
import pytest
import functools
import itertools

from stream import Stream


class TestStream:

    test_iterables = (
        range(10),
        [1, -1, 1, -1, 1],
        'abcd',
    )

    @pytest.mark.parametrize('iterable', test_iterables)
    def test_equality(self, iterable):
        assert Stream(iterable) == Stream(iterable)

    @pytest.mark.parametrize('iterable', test_iterables)
    @pytest.mark.parametrize('unary_func', [
        lambda x: 3 * x, lambda x: (x,)
    ])
    def test_map(self, unary_func, iterable):
        assert (
            Stream(iterable).map(unary_func).to_list()
            ==
            list(map(unary_func, iterable))
        )

    @pytest.mark.parametrize('iterable', test_iterables)
    @pytest.mark.parametrize('binary_func', [
        operator.add, lambda x, y: 2 * x + y
    ])
    def test_reduce(self, binary_func, iterable):
        assert (
            Stream(iterable).reduce(binary_func)
            ==
            functools.reduce(binary_func, iterable)
        )

    def test_reduce_with_default(self):
        assert Stream(range(2, 5)).reduce(operator.add, 1) == 10

    @pytest.mark.parametrize('iterable', test_iterables)
    @pytest.mark.parametrize('a_filter', [
        lambda x: x + x > x, lambda x: not x
    ])
    def test_filter(self, a_filter, iterable):
        assert (
            Stream(iterable).filter(a_filter).to_list()
            ==
            list(filter(a_filter, iterable))
        )

    @pytest.mark.parametrize('iterable', test_iterables)
    def test_pair_consecutive(self, iterable):
        assert (
            Stream(iterable).pair_consecutive().to_list()
            ==
            list(zip(iterable[1:], iterable[:-1]))
        )

    @pytest.mark.parametrize('first,second', [
        (range(5), (-1, -2, -4)),
        ('abc', [0, 1, 2]),
    ])
    def test_chain(self, first, second):
        assert (
            Stream(first).chain(second).to_list()
            ==
            list(itertools.chain(first, second))
        )

    @pytest.mark.parametrize('iterable', test_iterables)
    def test_min(self, iterable):
        assert Stream(iterable).min() == min(list(iterable))

    def test_min_empty(self):
        assert Stream([]).min() is None
        assert Stream([]).min(5) == 5

    @pytest.mark.parametrize('iterable,condition,benchmark', [
        (range(10), lambda x: x > 5, 6),
    ])
    def test_first(self, iterable, condition, benchmark):
        assert Stream(iterable).first(condition) == benchmark

    @pytest.mark.parametrize('iterable', test_iterables)
    @pytest.mark.parametrize('binary_func', [
        operator.add, lambda x, y: 2*x + y
    ])
    def test_accumulate(self, iterable, binary_func):
        assert (
            Stream(iterable).accumulate(binary_func).to_list()
            ==
            list(itertools.accumulate(iterable, binary_func))
        )

    def test_accumulate_with_default(self):
        assert None

    def test_dropwhile(self):
        assert Stream(range(2, 5)).accumulate(operator.add, 1).to_list() == [1, 3, 6, 10]
